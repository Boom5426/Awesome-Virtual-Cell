#!/usr/bin/env python3
"""Weekly candidate digest for human review; it never edits the catalog.

Collects new records from bioRxiv, arXiv and Europe PMC, drops those already in the catalog or in
journals outside config/venue_policy.json, and lists the rest by the keyword score of the October
sweeps. A TF-IDF logistic-regression ranker was backtested on the 2026-10-27 sweep pool and failed
its pre-registered gate (recall 0.694 within the top 300 of 13,439, against a 0.90 bar; keyword
screening reached 0.677), so it is not used. The listing depth is the smallest keyword threshold
that met the 0.90 recall target in that backtest: score 2 (recall 0.960, about 150 records a week).
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import time
import urllib.parse
from pathlib import Path

from scripts import publication_watcher as pw

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
CONFIG = ROOT / "config" / "digest.json"
OUT = ROOT / "candidate_digest.md"
BIORXIV = "https://api.biorxiv.org/details/biorxiv/{start}/{end}/{cursor}"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
DOI = re.compile(r"10\.\d{4,9}/[^\s?#\])]+", re.I)
ISSUE_LIMIT = 60000  # GitHub caps issue bodies at 65,536 characters


def norm(text: str) -> str:
    return pw.norm(text or "")


def keyword_hits(title: str, abstract: str, cfg: dict) -> tuple[int, list[str]]:
    """The 2026-10-27 sweep's screening score: +2 per pattern in the title, +1 in the abstract."""
    text, low_title = f"{title} {abstract}".lower(), title.lower()
    matched = [p for p in cfg["keyword_patterns"] if re.search(p, text)]
    score = sum(2 if re.search(p, low_title) else 1 for p in matched)
    if not re.search(cfg["cell_pattern"], text):
        score -= 3
    return score, matched


class CatalogIndex:
    """DOIs, arXiv ids and normalized titles already in the catalog."""

    def __init__(self, papers: list[dict]):
        self.dois: set[str] = set()
        self.arxiv: set[str] = set()
        self.titles = {norm(p["title"]) for p in papers}
        for p in papers:
            for key in ("doi", "paper_url", "preprint_url"):
                value = p.get(key) or ""
                for doi in DOI.findall(value):
                    self.dois.add(doi.lower().rstrip("./"))
                aid = pw.ARXIV_ID.search(value)
                if aid:
                    self.arxiv.add(aid.group(1))
        self.title_list = list(self.titles)

    def contains(self, record: dict) -> bool:
        if record.get("doi") and record["doi"].lower() in self.dois:
            return True
        if record.get("arxiv") and record["arxiv"] in self.arxiv:
            return True
        key = norm(record["title"])
        return key in self.titles or bool(difflib.get_close_matches(key, self.title_list, n=1, cutoff=0.9))


def venue_allowed(journal: str, allowed: set[str], aliases: dict[str, str]) -> str | None:
    """Map a Europe PMC journal title to the catalog's venue name if the policy lists it."""
    cleaned = re.sub(r"\s*\([^)]*\)\s*$", "", journal or "").strip()
    key = re.sub(r"[^a-z0-9]+", " ", cleaned.lower().replace("&", "and")).strip()
    if key in aliases:
        return aliases[key]
    by_key = {re.sub(r"[^a-z0-9]+", " ", v.lower().replace("&", "and")).strip(): v for v in allowed}
    return by_key.get(key)


def fetch_biorxiv(start: str, end: str) -> list[dict]:
    """New bioRxiv preprints (version 1) posted in [start, end]."""
    out: dict[str, dict] = {}
    cursor = 0
    while True:
        data = pw.get_json(BIORXIV.format(start=start, end=end, cursor=cursor))
        rows = data.get("collection") or []
        for r in rows:
            if str(r.get("version")) == "1" and r.get("doi"):
                out[r["doi"].lower()] = {"source": "bioRxiv", "venue": "bioRxiv", "title": " ".join(r.get("title", "").split()),
                                         "abstract": r.get("abstract") or "", "date": r.get("date"), "doi": r["doi"].lower(),
                                         "arxiv": None, "url": f"https://doi.org/{r['doi']}"}
        total = int((data.get("messages") or [{}])[0].get("total") or 0)
        cursor += len(rows)
        if not rows or cursor >= total:
            return list(out.values())


def fetch_arxiv(start: str, end: str, query: str) -> list[dict]:
    """arXiv records submitted in [start, end] that match the configured category/keyword query."""
    out: dict[str, dict] = {}
    span = f"submittedDate:[{start.replace('-', '')}0000 TO {end.replace('-', '')}2359]"
    for offset in range(0, 5000, 100):
        if offset:
            time.sleep(3)  # arXiv asks for one request every 3 seconds
        params = {"search_query": f"({query}) AND {span}", "start": str(offset), "max_results": "100",
                  "sortBy": "submittedDate", "sortOrder": "descending"}
        root = pw.ET.fromstring(pw.get_text(f"{pw.ARXIV}?{urllib.parse.urlencode(params)}"))
        entries = root.findall(f"{pw.ATOM}entry")
        for e in entries:
            m = re.search(r"abs/(\d{4}\.\d{4,5})", e.findtext(f"{pw.ATOM}id") or "")
            if m:
                out[m.group(1)] = {"source": "arXiv", "venue": "arXiv", "title": " ".join((e.findtext(f"{pw.ATOM}title") or "").split()),
                                   "abstract": " ".join((e.findtext(f"{pw.ATOM}summary") or "").split()),
                                   "date": (e.findtext(f"{pw.ATOM}published") or "")[:10],
                                   "doi": (e.findtext(f"{pw.ARXIV_NS}doi") or "").lower() or None,
                                   "arxiv": m.group(1), "url": f"https://arxiv.org/abs/{m.group(1)}"}
        if len(entries) < 100:
            break
    return list(out.values())


def fetch_europepmc(start: str, end: str, query: str) -> list[dict]:
    """Journal articles (SRC:MED) first published in [start, end] that match the configured query."""
    out: list[dict] = []
    cursor = "*"
    full = f"({query}) AND FIRST_PDATE:[{start} TO {end}] AND SRC:MED"
    while True:
        params = {"query": full, "format": "json", "resultType": "core", "pageSize": "500", "cursorMark": cursor}
        data = pw.get_json(f"{EUROPEPMC}?{urllib.parse.urlencode(params)}")
        rows = (data.get("resultList") or {}).get("result") or []
        for r in rows:
            journal = ((r.get("journalInfo") or {}).get("journal") or {}).get("title") or ""
            doi = (r.get("doi") or "").lower() or None
            out.append({"source": "Europe PMC", "venue": journal, "title": " ".join((r.get("title") or "").split()).rstrip("."),
                        "abstract": re.sub(r"<[^>]+>", " ", r.get("abstractText") or ""), "date": r.get("firstPublicationDate"),
                        "doi": doi, "arxiv": None, "url": f"https://doi.org/{doi}" if doi else f"https://europepmc.org/article/MED/{r.get('pmid')}"})
        nxt = data.get("nextCursorMark")
        if not rows or not nxt or nxt == cursor:
            return out
        cursor = nxt


def rank(records: list[dict], cfg: dict) -> list[dict]:
    """Records at or above the configured keyword score, highest first, then newest."""
    for r in records:
        r["keyword_score"], r["keywords"] = keyword_hits(r["title"], r["abstract"], cfg)
    kept = sorted((r for r in records if r["keyword_score"] >= cfg["min_keyword_score"]), key=lambda r: r["title"])
    return sorted(kept, key=lambda r: (r["keyword_score"], r.get("date") or ""), reverse=True)


def render(ranked: list[dict], meta: dict, warnings: list[str], watch: dict | None, detail_score: int) -> str:
    lines = [f"# Curation digest {meta['end']}", "",
             f"Window {meta['start']} to {meta['end']}. Sources: " + ", ".join(f"{k} {v}" for k, v in meta["counts"].items())
             + f". Dropped {meta['in_catalog']} already in the catalog and {meta['outside_policy']} in journals outside "
             "`config/venue_policy.json`.", "",
             f"Listed by the keyword score (`kw`) used in the October sweeps; {len(ranked)} records reach the listing "
             "threshold. Inclusion follows the README rules: preprints must be methods compared against baselines, "
             "or datasets and benchmarks. Nothing here is added automatically.", ""]
    for problem in meta["problems"]:
        lines += [f"> WARNING: {problem}", ""]
    if warnings:
        lines += ["## Live challenges to re-check", ""] + [f"- {w}" for w in warnings] + [""]
    if watch and (watch.get("outside") or watch.get("hints")):
        lines += ["## Publication watcher items needing a decision", ""]
        for row in watch.get("outside", []):
            lines.append(f"- {row.get('label') or row['id']}: published in {row['venue']} (outside the venue policy) {row.get('url') or ''}")
        for row in watch.get("hints", []):
            lines.append(f"- {row.get('label') or row['id']}: hint from {row['source']}: {row['venue']} {row.get('url') or ''}")
        lines.append("")
    detail = [r for r in ranked if r["keyword_score"] >= detail_score]
    rest = [r for r in ranked if r["keyword_score"] < detail_score]
    lines += [f"## Candidates with kw {detail_score} or more ({len(detail)})", ""]
    for i, r in enumerate(detail, 1):
        snippet = r["abstract"][:280].rsplit(" ", 1)[0] + ("..." if len(r["abstract"]) > 280 else "")
        lines += [f"{i}. **[{r['title']}]({r['url']})** ({r['venue']}, {r['date']}) kw {r['keyword_score']}", f"   {snippet}", ""]
    if rest:
        lines += [f"## Lower-scoring candidates, titles only ({len(rest)})", ""]
        lines += [f"- [{r['title']}]({r['url']}) ({r['venue']}, kw {r['keyword_score']})" for r in rest] + [""]
    text = "\n".join(lines) + "\n"
    return text if len(text) <= ISSUE_LIMIT else text[:ISSUE_LIMIT].rsplit("\n\n", 1)[0] + "\n\n(truncated to fit an issue)\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--end", default=dt.date.today().isoformat())
    parser.add_argument("--days", type=int)
    parser.add_argument("--watch-report", type=Path, default=pw.REPORT)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    end = dt.date.fromisoformat(args.end)
    start = end - dt.timedelta(days=(args.days or cfg["window_days"]) - 1)
    papers = json.loads(DATA.read_text(encoding="utf-8"))["papers"]
    allowed, _ = pw.allowed_venues()
    index = CatalogIndex(papers)

    fetched: list[dict] = []
    problems: list[str] = []
    counts: dict[str, int] = {}
    for name, fetch in (("bioRxiv", lambda: fetch_biorxiv(start.isoformat(), end.isoformat())),
                        ("arXiv", lambda: fetch_arxiv(start.isoformat(), end.isoformat(), cfg["arxiv_query"])),
                        ("Europe PMC", lambda: fetch_europepmc(start.isoformat(), end.isoformat(), cfg["europepmc_query"]))):
        try:
            rows = fetch()
        except Exception as exc:
            problems.append(f"{name} unavailable: {exc}")
            rows = []
        counts[name] = len(rows)
        fetched += rows

    records, seen, in_catalog, outside = [], set(), 0, 0
    for r in fetched:
        if r["source"] == "Europe PMC":
            venue = venue_allowed(r["venue"], allowed, cfg["journal_aliases"])
            if not venue:
                outside += 1
                continue
            r["venue"] = venue
        key = r.get("doi") or r.get("arxiv") or norm(r["title"])
        if key in seen or not r["title"]:
            continue
        seen.add(key)
        if index.contains(r):
            in_catalog += 1
            continue
        records.append(r | {"key": key})

    ranked = rank(records, cfg)
    from scripts import build_readme
    warnings = build_readme.challenge_warnings(build_readme.load_challenges(), end)
    watch = json.loads(args.watch_report.read_text(encoding="utf-8")) if args.watch_report.exists() else None
    meta = {"start": start.isoformat(), "end": end.isoformat(), "counts": counts, "in_catalog": in_catalog,
            "outside_policy": outside, "problems": problems}
    args.out.write_text(render(ranked, meta, warnings, watch, cfg["detail_keyword_score"]), encoding="utf-8")
    print(f"{len(fetched)} fetched, {in_catalog} already in the catalog, {outside} outside the venue policy, "
          f"{len(ranked)} listed; digest written to {args.out}")
    for problem in problems:
        print("WARN:", problem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
