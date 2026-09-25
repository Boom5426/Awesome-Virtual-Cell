#!/usr/bin/env python3
"""Build searchable catalog pages from the HTML template and data/papers.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
TEMPLATE = ROOT / "docs" / "catalog.template.html"
CATALOG = ROOT / "docs" / "catalog.html"
INDEX = ROOT / "docs" / "index.html"
ROOT_INDEX = ROOT / "index.html"
PLACEHOLDER = "__PAPERS_JSON__"


def render() -> str:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload["papers"]
    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise SystemExit(f"Missing {PLACEHOLDER} in catalog template")
    data = json.dumps(papers, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return template.replace(PLACEHOLDER, data)


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    document = render()
    CATALOG.write_text(document, encoding="utf-8")
    INDEX.write_text(document, encoding="utf-8")
    ROOT_INDEX.write_text(document, encoding="utf-8")
    print(f"Wrote index.html, docs/index.html, and docs/catalog.html with {len(payload['papers'])} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
