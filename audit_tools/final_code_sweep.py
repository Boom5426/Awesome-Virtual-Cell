#!/usr/bin/env python3
import json, os, re, time, urllib.parse, urllib.request
from difflib import SequenceMatcher
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"audit_output"
OUT.mkdir(exist_ok=True)
PAPERS=json.loads((ROOT/"data/papers.json").read_text())["papers"]
TOKEN=os.environ.get("GH_TOKEN","")
HEAD={"Accept":"application/vnd.github+json","User-Agent":"awesome-vc-final-code-sweep"}
if TOKEN: HEAD["Authorization"]="Bearer "+TOKEN

POSITIVE={"paper_linked","repository_linked","project_match"}
UNRESOLVED={"not_found","related_only","release_pending","data_only"}
ACTION_TYPES={"Method","Benchmark","Evaluation","Tool","Dataset"}

def api(url):
    req=urllib.request.Request(url,headers=HEAD)
    with urllib.request.urlopen(req,timeout=30) as r:
        return json.load(r)

def norm(s):
    return " ".join(re.sub(r"[^a-z0-9]+"," ",(s or "").lower()).split())

STOP={"a","an","the","of","for","to","in","on","and","with","via","from","using","single","cell","cells","single-cell","model","models","learning","prediction","predicting"}

def key_terms(title):
    terms=[x for x in re.findall(r"[A-Za-z0-9][A-Za-z0-9+-]*",title) if x.lower() not in STOP and len(x)>2]
    return terms[:7]

def search_repos(q):
    url="https://api.github.com/search/repositories?per_page=5&q="+urllib.parse.quote(q)
    try: return api(url).get("items",[])
    except Exception as e: return [{"_error":str(e)}]

def readme(full):
    try:
        meta=api("https://api.github.com/repos/"+full+"/readme")
        raw=meta.get("download_url")
        if not raw:return ""
        req=urllib.request.Request(raw,headers={"User-Agent":"awesome-vc-final-code-sweep"})
        with urllib.request.urlopen(req,timeout=20) as r:
            return r.read().decode("utf-8","replace")[:20000]
    except Exception:
        return ""

def repo_score(p,item,readme):
    title=norm(p["title"]); label=norm(p.get("label"))
    blob=norm(" ".join([item.get("name",""),item.get("full_name",""),item.get("description") or "",readme]))
    score=0.0
    if label and label in blob: score+=0.35
    terms=key_terms(p["title"])
    if terms:
        hit=sum(1 for t in terms if norm(t) in blob)/len(terms)
        score+=0.35*hit
    if title and title in blob: score+=0.5
    score+=0.2*SequenceMatcher(None,title,blob[:max(len(title)*3,1)]).ratio()
    return round(score,4)

def has_code(p):
    return bool(p.get("code_url")) and p.get("code_status") not in UNRESOLVED

targets=[]
for p in PAPERS:
    pt=set((p.get("facets") or {}).get("paper_type") or [])
    if p.get("code_status")=="project_match" or (not has_code(p) and pt&ACTION_TYPES):
        targets.append(p)

rows=[]
for idx,p in enumerate(targets):
    queries=[]
    label=(p.get("label") or "").strip()
    if label and len(label)>=3:
        queries.append(f'"{label}" in:name,description,readme')
    terms=key_terms(p["title"])
    if terms:
        queries.append(" ".join(terms[:5])+" in:readme")
    seen={}
    errors=[]
    for q in queries[:2]:
        results=search_repos(q)
        for it in results:
            if "_error" in it:
                errors.append(it["_error"]); continue
            full=it.get("full_name")
            if full: seen[full]=it
        time.sleep(2.1)
    candidates=[]
    for full,it in list(seen.items())[:8]:
        rd=readme(full)
        candidates.append({
            "repo":full,
            "url":it.get("html_url"),
            "description":it.get("description"),
            "stars":it.get("stargazers_count"),
            "updated_at":it.get("updated_at"),
            "score":repo_score(p,it,rd),
            "title_exact":norm(p["title"]) in norm(rd),
            "label_in_readme":norm(label) in norm(rd) if label else False,
            "readme_excerpt":re.sub(r"\s+"," ",rd[:1600]),
        })
    candidates.sort(key=lambda x:(x["score"],x.get("stars") or 0),reverse=True)
    rows.append({
        "id":p["id"],"label":p.get("label"),"title":p["title"],"year":p["year"],"venue":p["venue"],
        "code_status":p.get("code_status"),"current_code_url":p.get("code_url"),
        "paper_url":p.get("paper_url"),"preprint_url":p.get("preprint_url"),
        "queries":queries,"errors":errors,"candidates":candidates[:5],
    })

(OUT/"final_code_sweep.json").write_text(json.dumps(rows,indent=2,ensure_ascii=False))
summary=[]
for r in rows:
    top=r["candidates"][0] if r["candidates"] else None
    if top and top["score"]>=0.45:
        summary.append({"id":r["id"],"label":r["label"],"top":top})
(OUT/"high_confidence_candidates.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False))
print(json.dumps({"targets":len(rows),"high_confidence":len(summary)},indent=2))
