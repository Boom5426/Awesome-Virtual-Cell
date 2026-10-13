#!/usr/bin/env python3
"""Find high-confidence preprint -> formal-publication upgrades via Crossref."""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
SUMMARY = ROOT / "publication_update_summary.md"
CROSSREF = "https://api.crossref.org/works"
HEADERS = {"User-Agent": "Awesome-Virtual-Cell-PublicationWatcher/1.0 (https://github.com/Boom5426/Awesome-Virtual-Cell)"}
# bioRxiv/medRxiv (date-stamped 10.1101 and 10.64898), Research Square, arXiv; CSHL journals also use 10.1101.
PREPRINT_DOI = re.compile(r"^10\.(1101/\d{4}\.\d{2}\.\d{2}\.|64898/|21203/rs\.|48550/arxiv\.)", re.I)
SELECT = "title,DOI,URL,container-title,published-print,published-online,issued,type"
# Crossref container titles -> the short venue names used throughout the catalog.
VENUE_ALIASES = [
    (r"SIGKDD Conference on Knowledge Discovery", "KDD"),
    (r"Conference on Bioinformatics, Computational Biology,? and Health Informatics", "ACM BCB"),
    (r"Annual Meeting of the Association for Computational Linguistics", "ACL"),
    (r"Advances in Neural Information Processing Systems", "NeurIPS"),
    (r"International Conference on Machine Learning", "ICML"),
    (r"International Conference on Learning Representations", "ICLR"),
    (r"AAAI Conference on Artificial Intelligence", "AAAI"),
    (r"Research in Computational Molecular Biology", "RECOMB"),
    (r"^Proceedings of the National Academy of Sciences", "PNAS"),
]


def norm(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def normalize_venue(venue: str) -> str:
    for pattern, short in VENUE_ALIASES:
        if re.search(pattern, venue, re.I):
            return short
    return venue


def get_json(url: str, retries: int = 4) -> dict:
    """GET JSON, backing off on Crossref rate limits (429) and transient 5xx errors."""
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == retries:
                raise
        time.sleep(2 ** attempt * 2)
    raise RuntimeError("unreachable")


def year_of(item: dict) -> int | None:
    # The catalog dates papers by first (online) publication, matching publisher pages.
    for field in ("published-online", "published-print", "issued"):
        parts = item.get(field, {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def to_candidate(item: dict, paper: dict, score: float) -> dict | None:
    titles = item.get("title") or []
    venues = item.get("container-title") or []
    if not titles or not venues or item.get("type") == "posted-content":
        return None
    if re.search(r"bioRxiv|medRxiv|arXiv|Research Square", venues[0], re.I):
        return None
    doi = item.get("DOI")
    if paper.get("doi") and doi and paper["doi"].lower() == doi.lower():
        return None
    return {
        "title": titles[0],
        "venue": normalize_venue(venues[0]),
        "year": year_of(item) or paper["year"],
        "doi": doi,
        "url": f"https://doi.org/{doi}" if doi else item.get("URL"),
        "score": score,
    }


def linked_publication(paper: dict) -> dict | None:
    """Follow Crossref's is-preprint-of relation from a bioRxiv/medRxiv/Research Square DOI."""
    doi = paper.get("doi") or ""
    if not PREPRINT_DOI.match(doi):
        return None
    message = get_json(f"{CROSSREF}/{urllib.parse.quote(doi)}").get("message", {})
    for rel in (message.get("relation") or {}).get("is-preprint-of", []):
        if rel.get("id-type") != "doi":
            continue
        item = get_json(f"{CROSSREF}/{urllib.parse.quote(rel['id'])}").get("message", {})
        # Publisher-asserted link: accept retitled versions, but reject obviously unrelated records.
        title = (item.get("title") or [""])[0]
        if title and similarity(paper["title"], title) >= 0.5:
            return to_candidate(item, paper, 1.0)
    return None


def candidates_for(paper: dict) -> list[dict]:
    linked = linked_publication(paper)
    if linked:
        return [linked]
    params = {"query.title": paper["title"], "rows": "8", "select": SELECT}
    data = get_json(CROSSREF + "?" + urllib.parse.urlencode(params))
    found: list[dict] = []
    for item in data.get("message", {}).get("items", []):
        titles = item.get("title") or []
        if not titles:
            continue
        score = similarity(paper["title"], titles[0])
        if score < 0.90:
            continue
        candidate = to_candidate(item, paper, score)
        if candidate:
            found.append(candidate)
    found.sort(key=lambda x: x["score"], reverse=True)
    return found


def collect_proposals(papers: list[dict], max_updates: int) -> tuple[list[tuple[dict,dict]], int, int]:
    proposals: list[tuple[dict,dict]] = []
    scanned = 0
    failed = 0
    for paper in papers:
        if paper.get("status") != "preprint":
            continue
        scanned += 1
        try:
            hits = candidates_for(paper)
        except Exception as exc:
            failed += 1
            print(f"WARN: Crossref lookup failed for {paper['id']}: {exc}")
            continue
        if hits:
            proposals.append((paper, hits[0]))
    proposals.sort(key=lambda x: x[1]["score"], reverse=True)
    return proposals[:max_updates], scanned, failed


def update_links(paper: dict) -> None:
    core_urls = {paper.get("paper_url"), paper.get("preprint_url"), paper.get("code_url")}
    paper["links"] = [x for x in paper.get("links", []) if x.get("url") not in core_urls]


def apply_update(paper: dict, hit: dict, today: str) -> None:
    old_primary = paper.get("preprint_url") or paper.get("paper_url")
    if hit.get("title") and norm(hit["title"]) != norm(paper["title"]):
        paper["title"] = hit["title"]
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
    proposals, scanned, failed = collect_proposals(payload["papers"], args.max_updates)

    lines = [
        "# Publication Upgrade Watch",
        "",
        f"- Date: {today}",
        f"- Preprints scanned: {scanned}",
        f"- Lookup failures: {failed}",
        f"- High-confidence candidates selected: {len(proposals)}",
        f"- Per-run update cap: {args.max_updates}",
        "",
    ]
    for paper, hit in proposals:
        lines += [
            f"## {paper.get('label') or paper['title']}",
            "",
            f"- Preprint: {paper['venue']} {paper['year']}",
            f"- Candidate publication: {hit['venue']} {hit['year']}",
            f"- Title similarity: {hit['score']:.3f}" + (" (Crossref is-preprint-of link)" if hit["score"] == 1.0 and norm(hit["title"]) != norm(paper["title"]) else ""),
            f"- Published title: {hit['title']}",
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
        print(f"Scanned {scanned} preprints; applied {len(proposals)} publication upgrades; {failed} lookups failed")
    else:
        print(f"Scanned {scanned} preprints; found {len(proposals)} publication upgrade candidates; {failed} lookups failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
