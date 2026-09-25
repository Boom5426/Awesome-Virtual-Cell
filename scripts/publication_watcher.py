#!/usr/bin/env python3
"""Find high-confidence preprint -> formal-publication upgrades via Crossref."""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
SUMMARY = ROOT / "publication_update_summary.md"
CROSSREF = "https://api.crossref.org/works"
HEADERS = {"User-Agent": "Awesome-Virtual-Cell-PublicationWatcher/1.0 (https://github.com/Boom5426/Awesome-Virtual-Cell)"}


def norm(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def year_of(item: dict) -> int | None:
    for field in ("published-print","published-online","issued"):
        parts = item.get(field, {}).get("date-parts") or []
        if parts and parts[0]:
            return int(parts[0][0])
    return None


def candidates_for(paper: dict) -> list[dict]:
    params = {
        "query.title": paper["title"],
        "rows": "8",
        "select": "title,DOI,URL,container-title,published-print,published-online,issued,type",
    }
    data = get_json(CROSSREF + "?" + urllib.parse.urlencode(params))
    found: list[dict] = []
    for item in data.get("message", {}).get("items", []):
        titles = item.get("title") or []
        venues = item.get("container-title") or []
        if not titles or not venues:
            continue
        venue = venues[0]
        if re.search(r"bioRxiv|medRxiv|arXiv|Research Square", venue, re.I):
            continue
        score = similarity(paper["title"], titles[0])
        if score < 0.90:
            continue
        doi = item.get("DOI")
        if paper.get("doi") and doi and paper["doi"].lower() == doi.lower():
            continue
        found.append({
            "title": titles[0],
            "venue": venue,
            "year": year_of(item) or paper["year"],
            "doi": doi,
            "url": item.get("URL") or (f"https://doi.org/{doi}" if doi else None),
            "score": score,
        })
    found.sort(key=lambda x: x["score"], reverse=True)
    return found


def update_links(paper: dict) -> None:
    core_urls = {paper.get("paper_url"), paper.get("preprint_url"), paper.get("code_url")}
    paper["links"] = [x for x in paper.get("links", []) if x.get("url") not in core_urls]


def apply_update(paper: dict, hit: dict, today: str) -> None:
    old_primary = paper.get("preprint_url") or paper.get("paper_url")
    paper["status"] = "published"
    paper["venue"] = hit["venue"]
    paper["year"] = int(hit["year"])
    paper["doi"] = hit.get("doi")
    paper["paper_url"] = hit.get("url")
    if not paper.get("preprint_url"):
        paper["preprint_url"] = old_primary
    paper["updated_at"] = today
    update_links(paper)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--max-updates", type=int, default=10)
    args = parser.parse_args()

    payload = json.loads(DATA.read_text(encoding="utf-8"))
    today = dt.date.today().isoformat()
    proposals: list[tuple[dict,dict]] = []

    for paper in payload["papers"]:
        if paper.get("status") != "preprint":
            continue
        try:
            hits = candidates_for(paper)
        except Exception as exc:
            print(f"WARN: Crossref lookup failed for {paper['id']}: {exc}")
            continue
        if hits:
            proposals.append((paper, hits[0]))
        if len(proposals) >= args.max_updates:
            break

    lines = ["# Publication Upgrade Watch", "", f"- Date: {today}", f"- High-confidence candidates: {len(proposals)}", ""]
    for paper, hit in proposals:
        lines += [
            f"## {paper.get('label') or paper['title']}",
            "",
            f"- Preprint: {paper['venue']} {paper['year']}",
            f"- Candidate publication: {hit['venue']} {hit['year']}",
            f"- Title similarity: {hit['score']:.3f}",
            f"- DOI: {hit.get('doi') or 'n/a'}",
            f"- URL: {hit.get('url') or 'n/a'}",
            "",
        ]
        if args.apply:
            apply_update(paper, hit, today)

    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if args.apply and proposals:
        payload["paper_count"] = len(payload["papers"])
        DATA.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Applied {len(proposals)} publication upgrades")
    else:
        print(f"Found {len(proposals)} publication upgrade candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
