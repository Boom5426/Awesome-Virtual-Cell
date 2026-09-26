#!/usr/bin/env python3
from __future__ import annotations
import csv,io,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/"data"/"papers.json";OUT=ROOT/"exports";FF=("task","modality","perturbation_type","generalization","paper_type")
def load():return json.loads(DATA.read_text())["papers"]
def csv_text(ps):
    b=io.StringIO();fields=["id","label","title","year","venue","status","tags",*FF,"doi","paper_url","preprint_url","code_url","added_at","updated_at","code_status","tag_review_basis","facet_review_basis"];w=csv.DictWriter(b,fieldnames=fields,lineterminator="\n");w.writeheader()
    for p in ps:
        row={k:p.get(k) for k in fields};row["tags"]="|".join(p.get("tags",[]))
        for k in FF:row[k]="|".join(p.get("facets",{}).get(k,[]))
        w.writerow({k:"" if v is None else v for k,v in row.items()})
    return b.getvalue()
def esc(v):
    v=v.replace("\\","\\\\")
    for c in("&","%","#","_"):v=v.replace(c,"\\"+c)
    return v
def bib(ps):
    out=[]
    for p in ps:
        kind="article" if p.get("status")=="published" else "misc";key=re.sub(r"[^A-Za-z0-9:_-]+","-",p["id"]).strip("-") or "paper";u=p.get("paper_url") or p.get("preprint_url") or "";fs=[("title",p["title"]),("year",str(p["year"]))]
        if p.get("venue"):fs.append(("journal" if kind=="article" else "howpublished",p["venue"]))
        if p.get("doi"):fs.append(("doi",p["doi"]))
        if u:fs.append(("url",u))
        out.append(f"@{kind}{{{key},\n"+",\n".join(f"  {k} = {{{esc(v)}}}" for k,v in fs)+"\n}")
    return "\n\n".join(out)+"\n"
def main():
    ps=load();OUT.mkdir(exist_ok=True);(OUT/"papers.csv").write_text(csv_text(ps));(OUT/"papers.bib").write_text(bib(ps));print(f"Wrote exports for {len(ps)} papers");return 0
if __name__=="__main__":raise SystemExit(main())
