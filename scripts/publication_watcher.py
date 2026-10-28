#!/usr/bin/env python3
"""Find preprint -> formal-publication upgrades from several independent sources.

No single source is complete: in the 2026-10-27 audit the Crossref checks found 1 of 9
upgrades and the conference accepted-paper lists found the other 8. Sources, in order of
precedence: Crossref is-preprint-of relations, the bioRxiv/medRxiv `published` field, the arXiv
`doi` field, NeurIPS/ICML/ICLR/CVPR accepted-paper lists, and a Crossref title search.
Publications in venues outside config/venue_policy.json, arXiv journal_ref strings and near-miss
conference titles are reported for review and never applied.

Conference lists come from each virtual site's papers page, not its orals-posters JSON feed: on
2026-10-28 two regenerations of the NeurIPS 2026 feed each held a different 62-70% subset of the
9,130 accepted papers, while the papers page listed all of them.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
VENUE_POLICY = ROOT / "config" / "venue_policy.json"
SUMMARY = ROOT / "publication_update_summary.md"
REPORT = ROOT / "publication_watch.json"
CROSSREF = "https://api.crossref.org/works"
BIORXIV = "https://api.biorxiv.org/details/{server}/{doi}"
ARXIV = "https://export.arxiv.org/api/query"
PAPERS_PAGE = "https://{conf}.cc/virtual/{year}/papers.html?filter=titles"
OPENREVIEW_FORUM = re.compile(r"https://openreview\.net/forum\?id=[A-Za-z0-9_-]+")
CVF = "https://openaccess.thecvf.com/CVPR{year}?day=all"
CONFERENCES = {"neurips": "NeurIPS", "icml": "ICML", "iclr": "ICLR"}
HEADERS = {"User-Agent": "Awesome-Virtual-Cell-PublicationWatcher/1.0 (https://github.com/Boom5426/Awesome-Virtual-Cell)"}
# bioRxiv/medRxiv (date-stamped 10.1101 and 10.64898), Research Square, arXiv; CSHL journals also use 10.1101.
PREPRINT_DOI = re.compile(r"^10\.(1101/\d{4}\.\d{2}\.\d{2}\.|64898/|21203/rs\.|48550/arxiv\.)", re.I)
BIORXIV_DOI = re.compile(r"^10\.(1101/\d{4}\.\d{2}\.\d{2}\.|64898/)", re.I)
ARXIV_ID = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
ACCEPT_SIMILARITY = 0.90  # same bar as the Crossref title search
HINT_SIMILARITY = 0.75  # near-miss conference titles are listed for review, never applied
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


@dataclass
class Context:
    """Batch-fetched sources shared by all preprints in one run."""
    arxiv: dict[str, dict] = field(default_factory=dict)
    accepted: dict[str, dict] = field(default_factory=dict)


@dataclass
class Watch:
    proposals: list[tuple[dict, dict]]
    outside: list[tuple[dict, dict]]
    hints: list[tuple[dict, dict]]
    scanned: int
    failed: int


def norm(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def normalize_venue(venue: str) -> str:
    for pattern, short in VENUE_ALIASES:
        if re.search(pattern, venue, re.I):
            return short
    return venue


def get_text(url: str, retries: int = 4) -> str:
    """GET text, backing off on rate limits (429, arXiv's 503) and transient 5xx errors.

    A server-supplied Retry-After (seconds, capped at 120) takes precedence over the default backoff.
    """
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == retries:
                raise
            retry_after = (exc.headers or {}).get("Retry-After", "")
            exc.close()
        time.sleep(min(int(retry_after), 120) if retry_after.isdigit() else 2 ** attempt * 2)
    raise RuntimeError("unreachable")


def get_json(url: str, retries: int = 4) -> dict:
    return json.loads(get_text(url, retries))


def allowed_venues() -> tuple[set[str], str]:
    policy = json.loads(VENUE_POLICY.read_text(encoding="utf-8"))
    return set(policy["published_venues"]) | set(policy["other_venues"]), policy["report_suffix"]


def year_of(item: dict) -> int | None:
    # The catalog dates papers by first (online) publication, matching publisher pages.
    for field_name in ("published-online", "published-print", "issued"):
        parts = item.get(field_name, {}).get("date-parts") or []
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


def asserted_publication(doi: str, paper: dict, source: str) -> dict | None:
    """Resolve a DOI that a preprint server or publisher links to the preprint."""
    item = get_json(f"{CROSSREF}/{urllib.parse.quote(doi)}").get("message", {})
    # Asserted links: accept retitled versions, but reject obviously unrelated records.
    title = (item.get("title") or [""])[0]
    if not title or similarity(paper["title"], title) < 0.5:
        return None
    candidate = to_candidate(item, paper, 1.0)
    if candidate:
        candidate["source"] = source
    return candidate


def linked_publication(paper: dict) -> dict | None:
    """Follow Crossref's is-preprint-of relation from a bioRxiv/medRxiv/Research Square DOI."""
    doi = paper.get("doi") or ""
    if not PREPRINT_DOI.match(doi):
        return None
    message = get_json(f"{CROSSREF}/{urllib.parse.quote(doi)}").get("message", {})
    for rel in (message.get("relation") or {}).get("is-preprint-of", []):
        if rel.get("id-type") == "doi":
            candidate = asserted_publication(rel["id"], paper, "crossref-relation")
            if candidate:
                return candidate
    return None


def biorxiv_publication(paper: dict) -> dict | None:
    """Follow the journal DOI that bioRxiv or medRxiv itself records for the preprint."""
    doi = paper.get("doi") or ""
    if not BIORXIV_DOI.match(doi):
        return None
    for server in ("biorxiv", "medrxiv"):
        rows = get_json(BIORXIV.format(server=server, doi=doi)).get("collection") or []
        if rows:
            published = rows[-1].get("published") or "NA"
            return None if published == "NA" else asserted_publication(published, paper, "biorxiv-published")
    return None


def arxiv_id(paper: dict) -> str | None:
    match = ARXIV_ID.search(paper.get("preprint_url") or paper.get("paper_url") or "")
    return match.group(1) if match else None


def arxiv_records(ids: list[str]) -> dict[str, dict]:
    """Batch-fetch arXiv doi and journal_ref fields; arXiv asks for one request every 3 seconds."""
    out: dict[str, dict] = {}
    for start in range(0, len(ids), 50):
        if start:
            time.sleep(3)
        query = urllib.parse.urlencode({"id_list": ",".join(ids[start:start + 50]), "max_results": "50"})
        root = ET.fromstring(get_text(f"{ARXIV}?{query}"))
        for entry in root.findall(f"{ATOM}entry"):
            match = re.search(r"abs/(\d{4}\.\d{4,5})", entry.findtext(f"{ATOM}id") or "")
            if match:
                out[match.group(1)] = {"doi": entry.findtext(f"{ARXIV_NS}doi"),
                                       "journal_ref": entry.findtext(f"{ARXIV_NS}journal_ref")}
    return out


def accepted_papers(years: list[int]) -> dict[str, dict]:
    """Conference accepted-paper lists keyed by normalized title; Crossref indexes none of them."""
    rows: dict[str, dict] = {}
    for year in sorted(years, reverse=True):
        for conf, venue in CONFERENCES.items():
            try:
                page = get_text(PAPERS_PAGE.format(conf=conf, year=year))
            except urllib.error.HTTPError as exc:
                if exc.code == 404:
                    exc.close()
                    continue  # this year's list is not published yet
                raise
            for kind, event, title in re.findall(rf'<a href="/virtual/{year}/(poster|oral)/(\d+)">([^<]+)</a>', page):
                title = html.unescape(title).strip()
                rows.setdefault(norm(title), {"title": title, "venue": venue, "year": year,
                                              "url": f"https://{conf}.cc/virtual/{year}/{kind}/{event}"})
        try:
            page = get_text(CVF.format(year=year))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                exc.close()
                continue
            raise
        for href, title in re.findall(r'<dt class="ptitle"><br><a href="([^"]+)">([^<]+)</a>', page):
            title = html.unescape(title).strip()
            rows.setdefault(norm(title), {"title": title, "venue": "CVPR", "year": year,
                                          "url": urllib.parse.urljoin("https://openaccess.thecvf.com", href)})
    return rows


def accepted_match(paper: dict, index: dict[str, dict]) -> tuple[dict | None, dict | None]:
    """Return (accepted-list hit, near-miss hint) for a preprint title."""
    key = norm(paper["title"])
    if key in index:
        best, score = key, 1.0
    else:
        close = difflib.get_close_matches(key, index.keys(), n=1, cutoff=HINT_SIMILARITY)
        if not close:
            return None, None
        # same argument order as get_close_matches, so the score agrees with the cutoff
        best, score = close[0], difflib.SequenceMatcher(None, close[0], key).ratio()
    row = index[best]
    candidate = {"title": row["title"], "venue": row["venue"], "year": row["year"], "doi": None,
                 "url": row["url"], "score": round(score, 3), "source": "accepted-list"}
    return (candidate, None) if score >= ACCEPT_SIMILARITY else (None, candidate | {"hint": True})


def openreview_link(url: str) -> str:
    """The OpenReview forum a conference poster page links to (the catalog's usual paper URL), else the page."""
    if "openaccess.thecvf.com" in url:
        return url
    forums = set(OPENREVIEW_FORUM.findall(get_text(url)))
    return forums.pop() if len(forums) == 1 else url


def crossref_title_matches(paper: dict) -> list[dict]:
    params = {"query.title": paper["title"], "rows": "8", "select": SELECT}
    data = get_json(CROSSREF + "?" + urllib.parse.urlencode(params))
    found: list[dict] = []
    for item in data.get("message", {}).get("items", []):
        titles = item.get("title") or []
        if not titles:
            continue
        score = similarity(paper["title"], titles[0])
        if score < ACCEPT_SIMILARITY:
            continue
        candidate = to_candidate(item, paper, score)
        if candidate:
            found.append(candidate | {"source": "crossref-title"})
    found.sort(key=lambda x: x["score"], reverse=True)
    return found


def candidates_for(paper: dict, ctx: Context | None = None) -> list[dict]:
    """Applicable hits first; when none exist, review-only hints (marked with "hint")."""
    for finder in (linked_publication, biorxiv_publication):
        hit = finder(paper)
        if hit:
            return [hit]
    hints: list[dict] = []
    if ctx is not None:
        aid = arxiv_id(paper)
        record = ctx.arxiv.get(aid or "", {})
        if record.get("doi"):
            hit = asserted_publication(record["doi"], paper, "arxiv-doi")
            if hit:
                return [hit]
        hit, near = accepted_match(paper, ctx.accepted)
        if hit:
            return [hit | {"url": openreview_link(hit["url"])}]
        if near:
            hints.append(near)
        if record.get("journal_ref"):
            hints.append({"title": paper["title"], "venue": record["journal_ref"], "year": paper["year"],
                          "doi": None, "url": f"https://arxiv.org/abs/{aid}", "score": 0.0,
                          "source": "arxiv-journal-ref", "hint": True})
    return crossref_title_matches(paper) or hints


def collect_proposals(papers: list[dict], max_updates: int,
                      lookup: Callable[[dict], list[dict]] | None = None) -> Watch:
    lookup = lookup or candidates_for
    allowed, report_suffix = allowed_venues()
    watch = Watch([], [], [], 0, 0)
    for paper in papers:
        if paper.get("status") != "preprint":
            continue
        watch.scanned += 1
        try:
            hits = lookup(paper)
        except Exception as exc:
            watch.failed += 1
            print(f"WARN: publication lookup failed for {paper['id']}: {exc}")
            continue
        if not hits:
            continue
        top = hits[0]
        if top.get("hint"):
            watch.hints += [(paper, hit) for hit in hits]
        elif top["venue"] in allowed or top["venue"].endswith(report_suffix):
            watch.proposals.append((paper, top))
        else:
            watch.outside.append((paper, top))
    watch.proposals.sort(key=lambda x: x[1]["score"], reverse=True)
    watch.proposals = watch.proposals[:max_updates]
    return watch


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


def build_context(papers: list[dict], today: dt.date) -> tuple[Context, list[str]]:
    """Fetch the batch sources; a failed source is reported, and the others still run."""
    ctx, problems = Context(), []
    ids = sorted({aid for p in papers if p.get("status") == "preprint" for aid in [arxiv_id(p)] if aid})
    try:
        ctx.arxiv = arxiv_records(ids)
    except Exception as exc:
        problems.append(f"arXiv metadata unavailable: {exc}")
    try:
        ctx.accepted = accepted_papers([today.year, today.year - 1])
    except Exception as exc:
        problems.append(f"conference accepted lists unavailable: {exc}")
    return ctx, problems


def describe(paper: dict, hit: dict) -> list[str]:
    return [
        f"## {paper.get('label') or paper['title']}",
        "",
        f"- Preprint: {paper['venue']} {paper['year']}",
        f"- Candidate publication: {hit['venue']} {hit['year']}",
        f"- Source: {hit.get('source', 'n/a')}; title similarity {hit['score']:.3f}",
        f"- Published title: {hit['title']}",
        f"- DOI: {hit.get('doi') or 'n/a'}",
        f"- URL: {hit.get('url') or 'n/a'}",
        "",
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--max-updates", type=int, default=10)
    parser.add_argument("--data", type=Path, default=DATA)
    parser.add_argument("--summary", type=Path, default=SUMMARY)
    parser.add_argument("--report", type=Path, default=REPORT)
    args = parser.parse_args()

    payload = json.loads(args.data.read_text(encoding="utf-8"))
    today = dt.date.today()
    ctx, problems = build_context(payload["papers"], today)
    watch = collect_proposals(payload["papers"], args.max_updates, lambda p: candidates_for(p, ctx))
    sizes = Counter(f"{row['venue']} {row['year']}" for row in ctx.accepted.values())

    lines = [
        "# Publication Upgrade Watch",
        "",
        f"- Date: {today.isoformat()}",
        f"- Preprints scanned: {watch.scanned}",
        f"- Lookup failures: {watch.failed}",
        f"- Upgrades selected: {len(watch.proposals)} (per-run cap {args.max_updates})",
        f"- Published outside the venue allowlist: {len(watch.outside)}",
        f"- Review-only hints: {len(watch.hints)}",
        f"- Accepted-list titles: {', '.join(f'{k} {n}' for k, n in sorted(sizes.items())) or 'none'}",
        "",
    ] + [f"> WARNING: {p}" for p in problems] + ([""] if problems else [])
    for paper, hit in watch.proposals:
        lines += describe(paper, hit)
        if args.apply:
            apply_update(paper, hit, today.isoformat())
    if watch.outside:
        lines += ["# Published outside the venue allowlist (not applied)", "",
                  "These preprints appear in a venue that config/venue_policy.json does not list. "
                  "Decide whether to remove each record or to add the venue to the policy.", ""]
        for paper, hit in watch.outside:
            lines += describe(paper, hit)
    if watch.hints:
        lines += ["# Review-only hints (not applied)", ""]
        for paper, hit in watch.hints:
            lines += describe(paper, hit)

    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    report = {"date": today.isoformat(), "scanned": watch.scanned, "failed": watch.failed, "problems": problems,
              "accepted_list_sizes": dict(sorted(sizes.items())),
              **{name: [{"id": p["id"], "label": p.get("label"), **hit} for p, hit in rows]
                 for name, rows in (("proposals", watch.proposals), ("outside", watch.outside), ("hints", watch.hints))}}
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.apply and watch.proposals:
        payload["paper_count"] = len(payload["papers"])
        args.data.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    verb = "applied" if args.apply else "found"
    print(f"Scanned {watch.scanned} preprints; {verb} {len(watch.proposals)} upgrades; "
          f"{len(watch.outside)} outside the allowlist; {len(watch.hints)} hints; {watch.failed} lookups failed")
    for problem in problems:
        print("WARN:", problem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
