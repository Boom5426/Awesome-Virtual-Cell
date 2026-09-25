#!/usr/bin/env python3
"""Validate data/papers.json for duplicates and malformed metadata."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
ALLOWED_STATUS = {"published", "preprint"}


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def valid_url(value: str | None) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload.get("papers", [])
    errors: list[str] = []
    warnings: list[str] = []
    if payload.get("paper_count") != len(papers):
        errors.append(f"paper_count mismatch: {payload.get('paper_count')} vs {len(papers)}")

    for i, paper in enumerate(papers, 1):
        for field in ("id", "title", "year", "status", "tags", "entry_markdown"):
            if field not in paper:
                errors.append(f"#{i}: missing field {field}")
        if paper.get("status") not in ALLOWED_STATUS:
            errors.append(f"#{i}: invalid status {paper.get('status')!r}")
        if not isinstance(paper.get("tags"), list):
            errors.append(f"#{i}: tags must be a list")
        if not re.fullmatch(r"20\d{2}", str(paper.get("year", ""))):
            errors.append(f"#{i}: invalid year {paper.get('year')!r}")
        for field in ("paper_url", "preprint_url", "code_url"):
            if not valid_url(paper.get(field)):
                errors.append(f"#{i}: invalid {field} {paper.get(field)!r}")
        if not paper.get("paper_url") and not paper.get("preprint_url"):
            warnings.append(f"#{i}: no primary URL — {paper.get('title', '')}")

    for value, count in Counter(norm_title(p["title"]) for p in papers if p.get("title")).items():
        if count > 1:
            errors.append(f"duplicate normalized title ({count}x): {value}")
    for value, count in Counter(p["doi"].lower() for p in papers if p.get("doi")).items():
        if count > 1:
            errors.append(f"duplicate DOI ({count}x): {value}")

    print(f"Catalog: {len(papers)} papers | {len(errors)} errors | {len(warnings)} warnings")
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARN:", item)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
