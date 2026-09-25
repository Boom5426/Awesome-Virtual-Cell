#!/usr/bin/env python3
"""Data-first literature updater for Awesome-Virtual-Cell Schema v2."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

from scripts import auto_update_readme as discovery
from scripts import build_catalog, build_exports, build_readme

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
SUMMARY_PATH = ROOT / "auto_update_summary.md"


def load_catalog() -> dict:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 2:
        raise SystemExit("Expected data/papers.json schema_version=2")
    return payload


def catalog_keys(payload: dict) -> set[str]:
    keys: set[str] = set()
    for paper in payload.get("papers", []):
        for value in (
            paper.get("title"),
            paper.get("label"),
            paper.get("doi"),
            paper.get("paper_url"),
            paper.get("preprint_url"),
            paper.get("code_url"),
        ):
            if value:
                keys.add(discovery.normalize_text(str(value)))
        for link in paper.get("links", []):
            value = link.get("url") if isinstance(link, dict) else None
            if value:
                keys.add(discovery.normalize_text(str(value)))
    return keys


def doi_from_candidate(candidate: discovery.Candidate) -> str | None:
    if candidate.doi:
        return candidate.doi.strip()
    match = re.search(r"doi\.org/(.+)$", candidate.primary_link, flags=re.IGNORECASE)
    return match.group(1).strip() if match else None


def status_for(candidate: discovery.Candidate) -> str:
    venue = candidate.venue.lower()
    return "preprint" if any(
        x in venue for x in ("biorxiv", "medrxiv", "arxiv", "research square", "preprint")
    ) else "published"


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:80] or "paper"


def candidate_to_record(candidate: discovery.Candidate) -> dict:
    status = status_for(candidate)
    doi = doi_from_candidate(candidate)
    primary = candidate.primary_link
    today = dt.date.today().isoformat()
    return {
        "id": slug(candidate.label or candidate.title),
        "label": candidate.label or None,
        "title": candidate.title.strip(),
        "year": int(candidate.year),
        "venue": candidate.venue.strip(),
        "status": status,
        "tags": [candidate.tag] if candidate.tag else [],
        "doi": doi,
        "paper_url": primary if status == "published" else None,
        "preprint_url": primary if status == "preprint" else None,
        "code_url": candidate.code_link,
        "links": (
            [{"label": "dataset", "url": candidate.dataset_link}]
            if candidate.dataset_link else []
        ),
        "added_at": today,
        "updated_at": today,
    }


def merge_records(payload: dict, candidates: list[discovery.Candidate]) -> dict:
    new_records = [candidate_to_record(c) for c in candidates]
    updated = dict(payload)
    updated["papers"] = new_records + list(payload.get("papers", []))
    updated["paper_count"] = len(updated["papers"])
    updated["schema_version"] = 2
    return updated


def summary_markdown(candidates: list[discovery.Candidate]) -> str:
    today = dt.date.today().isoformat()
    lines = [
        "# Automated Structured Catalog Update",
        "",
        f"- Date: {today}",
        f"- Proposed research papers: {len(candidates)}",
        "- Source of truth: `data/papers.json`",
        "- Generated views: README, web catalog, CSV, and BibTeX",
        "",
        "## Proposed Additions",
        "",
    ]
    for candidate in candidates:
        lines += [
            f"- **{candidate.label}**",
            f"  - Title: {candidate.title}",
            f"  - Source: {candidate.venue} {candidate.year}",
            f"  - Tag: {candidate.tag or 'unassigned'}",
            f"  - Why: {candidate.rationale or 'Matched update rules'}",
            f"  - Primary link: {candidate.primary_link}",
        ]
    lines += [
        "",
        "## Review Notes",
        "",
        "- This PR is intentionally created as a draft.",
        "- Verify scientific relevance and metadata before merging.",
        "- Dataset/resource sections remain Markdown-first for now.",
        "",
    ]
    return "\n".join(lines)


def regenerate_views() -> None:
    current = build_readme.README.read_text(encoding="utf-8")
    target = build_readme.updated_readme(
        current, build_readme.render(build_readme.load_papers())
    )
    build_readme.README.write_text(target, encoding="utf-8")
    build_catalog.main()
    build_exports.main()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-additions", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rules = discovery.load_rules()
    payload = load_catalog()
    cutoff = (dt.date.today() - dt.timedelta(days=180)).isoformat()
    candidates = (
        discovery.seeded_manual_candidates()
        + discovery.crossref_candidates(rules, cutoff)
    )

    candidates = [c for c in candidates if c.section == "research"]
    unique = discovery.dedupe_candidates(candidates, catalog_keys(payload))
    limit = args.max_additions or int(rules["max_additions_per_run"])
    chosen = unique[:limit]

    if not chosen:
        SUMMARY_PATH.write_text(
            "# Automated Structured Catalog Update\n\n"
            "- No high-confidence research-paper additions were found.\n",
            encoding="utf-8",
        )
        print("No changes.")
        return 0

    if args.dry_run:
        print(summary_markdown(chosen))
        return 0

    updated = merge_records(payload, chosen)
    DATA_PATH.write_text(
        json.dumps(updated, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    regenerate_views()
    SUMMARY_PATH.write_text(summary_markdown(chosen), encoding="utf-8")
    print(f"Updated structured catalog with {len(chosen)} additions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
