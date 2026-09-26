#!/usr/bin/env python3
"""Build the interactive Research Landscape from shared catalog data."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/"data"/"papers.json";CONFIG=ROOT/"config"/"landscape.json";TEMPLATE=ROOT/"docs"/"landscape.template.html";OUTPUTS=(ROOT/"landscape.html",ROOT/"docs"/"landscape.html")
def render():
    ps=json.loads(DATA.read_text(encoding="utf-8"))["papers"];cfg=json.loads(CONFIG.read_text(encoding="utf-8"))
    compact=[{"id":p["id"],"label":p.get("label"),"title":p["title"],"year":p["year"],"tags":p.get("tags",[])} for p in ps]
    t=TEMPLATE.read_text(encoding="utf-8")
    return t.replace("__LANDSCAPE_DATA__",json.dumps(compact,ensure_ascii=False,separators=(",",":")).replace("</","<\\/")).replace("__LANDSCAPE_CONFIG__",json.dumps(cfg,ensure_ascii=False,separators=(",",":")).replace("</","<\\/"))
def main():
    d=render()
    for p in OUTPUTS:p.write_text(d,encoding="utf-8")
    print("Wrote Research Landscape");return 0
if __name__=="__main__":raise SystemExit(main())
