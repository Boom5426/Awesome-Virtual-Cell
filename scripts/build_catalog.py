#!/usr/bin/env python3
"""Build docs/catalog.html from docs/catalog.template.html and data/papers.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
TEMPLATE = ROOT / "docs" / "catalog.template.html"
OUT = ROOT / "docs" / "catalog.html"
PLACEHOLDER = "__PAPERS_JSON__"


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload["papers"]
    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise SystemExit(f"Missing {PLACEHOLDER} in catalog template")
    data = json.dumps(papers, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    OUT.write_text(template.replace(PLACEHOLDER, data), encoding="utf-8")
    print(f"Wrote docs/catalog.html with {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
