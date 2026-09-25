#!/usr/bin/env python3
"""Validate Awesome-Virtual-Cell Schema v2."""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
ALLOWED_STATUS = {"published", "preprint"}
REQUIRED = {
    "id","label","title","year","venue","status","tags","doi",
    "paper_url","preprint_url","code_url","links","added_at","updated_at",
}


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def valid_url(value: str | None) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_date(value: str | None) -> bool:
    if value is None:
        return True
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload.get("papers", [])
    vocabulary = set(json.loads((ROOT / "config" / "taxonomy.json").read_text(encoding="utf-8"))["tags"])
    errors: list[str] = []
    warnings: list[str] = []

    if payload.get("schema_version") != 2:
        errors.append(f"expected schema_version=2, got {payload.get('schema_version')!r}")
    if payload.get("paper_count") != len(papers):
        errors.append(f"paper_count mismatch: {payload.get('paper_count')} vs {len(papers)}")

    for i, p in enumerate(papers, 1):
        missing = sorted(REQUIRED - set(p))
        if missing:
            errors.append(f"#{i}: missing fields {missing}")
            continue
        if "entry_markdown" in p:
            errors.append(f"#{i} {p['id']}: legacy entry_markdown is not allowed in Schema v2")
        if p["status"] not in ALLOWED_STATUS:
            errors.append(f"#{i} {p['id']}: invalid status {p['status']!r}")
        if not re.fullmatch(r"20\d{2}", str(p["year"])):
            errors.append(f"#{i} {p['id']}: invalid year {p['year']!r}")
        if not isinstance(p["tags"], list) or not p["tags"]:
            errors.append(f"#{i} {p['id']}: tags must be a nonempty list")
        else:
            if any(not isinstance(t, str) or t not in vocabulary for t in p["tags"]):
                errors.append(f"#{i} {p['id']}: unknown topic tag")
            if len(set(p["tags"])) != len(p["tags"]):
                errors.append(f"#{i} {p['id']}: duplicate topic tags")
        status = p.get("code_status", "unreviewed")
        if status not in {"unreviewed", "paper_linked", "repository_linked", "project_match", "not_found", "related_only", "release_pending"}:
            errors.append(f"#{i} {p['id']}: unknown code_status")
        if status in {"paper_linked", "repository_linked", "project_match"} and not p.get("code_url"):
            errors.append(f"#{i} {p['id']}: linked-code status requires code_url")
        if status in {"not_found", "related_only", "release_pending"} and p.get("code_url"):
            errors.append(f"#{i} {p['id']}: unresolved-code status cannot be counted as available code")
        if status in {"paper_linked", "repository_linked"} and not p.get("code_sources"):
            errors.append(f"#{i} {p['id']}: verified correspondence requires supporting sources")
        if not isinstance(p["links"], list):
            errors.append(f"#{i} {p['id']}: links must be a list")
        else:
            for link in p["links"]:
                if not isinstance(link, dict) or set(link) != {"label", "url"}:
                    errors.append(f"#{i} {p['id']}: invalid auxiliary link {link!r}")
                elif not valid_url(link["url"]):
                    errors.append(f"#{i} {p['id']}: invalid auxiliary URL {link['url']!r}")
        for field in ("paper_url","preprint_url","code_url"):
            if not valid_url(p[field]):
                errors.append(f"#{i} {p['id']}: invalid {field}={p[field]!r}")
        for field in ("added_at","updated_at"):
            if not valid_date(p[field]):
                errors.append(f"#{i} {p['id']}: invalid {field}={p[field]!r}")
        if p["status"] == "preprint" and not p["preprint_url"]:
            warnings.append(f"#{i} {p['id']}: preprint has no preprint_url")
        if not (p["paper_url"] or p["preprint_url"] or p["links"]):
            warnings.append(f"#{i} {p['id']}: no primary or auxiliary URL")

    for value, count in Counter(p["id"] for p in papers).items():
        if count > 1:
            errors.append(f"duplicate id ({count}x): {value}")
    for value, count in Counter(norm_title(p["title"]) for p in papers).items():
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
