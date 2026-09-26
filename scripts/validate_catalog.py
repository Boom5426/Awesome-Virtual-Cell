#!/usr/bin/env python3
"""Validate topics, evidence-backed facets and source metadata."""
from __future__ import annotations
import json,re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/"data"/"papers.json";BASES={"abstract","project_documentation","title_and_metadata","unreviewed"}
REQ={"id","label","title","year","venue","status","tags","doi","paper_url","preprint_url","code_url","links","added_at","updated_at","facets","facet_review_basis","facet_sources"}
def good_url(x):
    if not x:return True
    p=urlparse(x);return p.scheme in {"http","https"} and bool(p.netloc)
def good_date(x):
    if x is None:return True
    try:date.fromisoformat(x);return True
    except ValueError:return False
def main():
    d=json.loads(DATA.read_text());ps=d.get("papers",[]);topics=set(json.loads((ROOT/"config"/"taxonomy.json").read_text())["tags"]);fc=json.loads((ROOT/"config"/"facets.json").read_text())["dimensions"];err=[];warn=[]
    if d.get("schema_version")!=2:err.append("expected schema_version=2")
    if d.get("facet_schema_version")!=1:err.append("expected facet_schema_version=1")
    if d.get("paper_count")!=len(ps):err.append("paper_count mismatch")
    for i,p in enumerate(ps,1):
        miss=REQ-set(p)
        if miss:err.append(f"#{i}: missing {sorted(miss)}");continue
        if p["status"] not in {"published","preprint"}:err.append(f"#{i} {p['id']}: bad status")
        if not p["tags"] or not set(p["tags"])<=topics or len(p["tags"])!=len(set(p["tags"])):err.append(f"#{i} {p['id']}: bad topics")
        if set(p["facets"])!=set(fc):err.append(f"#{i} {p['id']}: facet keys")
        else:
            for k,v in p["facets"].items():
                if not isinstance(v,list) or not set(v)<=set(fc[k]["values"]) or len(v)!=len(set(v)):err.append(f"#{i} {p['id']}: facet {k}")
        if p["facet_review_basis"] not in BASES:err.append(f"#{i} {p['id']}: facet basis")
        if not isinstance(p["facet_sources"],list) or any(not good_url(x) for x in p["facet_sources"]):err.append(f"#{i} {p['id']}: facet sources")
        if p["facet_review_basis"]=="title_and_metadata" and (p["facets"]["perturbation_type"] or p["facets"]["generalization"]):err.append(f"#{i} {p['id']}: provisional fine facet")
        cs=p.get("code_status","unreviewed")
        if cs in {"paper_linked","repository_linked","project_match"} and not p.get("code_url"):err.append(f"#{i} {p['id']}: code URL")
        if cs in {"not_found","related_only","release_pending"} and p.get("code_url"):err.append(f"#{i} {p['id']}: unresolved code URL")
        for k in ("paper_url","preprint_url","code_url"):
            if not good_url(p.get(k)):err.append(f"#{i} {p['id']}: {k}")
        if not isinstance(p["links"],list):err.append(f"#{i} {p['id']}: links")
        for k in ("added_at","updated_at"):
            if not good_date(p.get(k)):err.append(f"#{i} {p['id']}: {k}")
        if p["status"]=="preprint" and not p.get("preprint_url"):warn.append(f"#{i} {p['id']}: missing preprint URL")
    for v,n in Counter(p["id"] for p in ps).items():
        if n>1:err.append("duplicate id "+v)
    for v,n in Counter(re.sub(r"[^a-z0-9]+"," ",p["title"].lower()).strip() for p in ps).items():
        if n>1:err.append("duplicate title "+v)
    for v,n in Counter(p["doi"].lower() for p in ps if p.get("doi")).items():
        if n>1:err.append("duplicate doi "+v)
    print(f"Catalog: {len(ps)} papers | {len(err)} errors | {len(warn)} warnings")
    for x in err:print("ERROR:",x)
    for x in warn:print("WARN:",x)
    return 1 if err else 0
if __name__=="__main__":raise SystemExit(main())
