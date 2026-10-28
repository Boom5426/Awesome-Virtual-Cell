#!/usr/bin/env python3
"""Render research papers and live challenges from structured data; preserve year anchors."""
from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
CHALLENGES = ROOT / "data" / "challenges.json"
README = ROOT / "README.md"
START = "<!-- GENERATED:RESEARCH-PAPERS:START -->"
END = "<!-- GENERATED:RESEARCH-PAPERS:END -->"
CH_START = "<!-- GENERATED:LIVE-CHALLENGES:START -->"
CH_END = "<!-- GENERATED:LIVE-CHALLENGES:END -->"
RECENT_VISIBLE = 10
MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def load_papers() -> list[dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 2:
        raise SystemExit("Expected data/papers.json schema_version=2")
    return payload["papers"]


def github_repo_path(url: str | None) -> str | None:
    if not url:
        return None
    match = re.search(r"github\.com/([^/]+/[^/#?]+)", url)
    return match.group(1).removesuffix(".git") if match else None


def render_entry(paper: dict) -> str:
    parts: list[str] = ["-"]
    if paper.get("label"):
        parts.append(f"**[{paper['label']}]**")
    for tag in paper.get("tags", []):
        parts.append(f"`[{tag}]`")
    parts.append(paper["title"])
    venue = paper.get("venue") or "Unknown venue"
    parts.append(f"(**{venue} {paper['year']}**)")

    links: list[str] = []
    if paper.get("paper_url"):
        links.append(f"[[paper]({paper['paper_url']})]")
    if paper.get("preprint_url"):
        links.append(f"[[preprint]({paper['preprint_url']})]")
    if paper.get("code_url"):
        code_label = "code (project)" if paper.get("code_status") == "project_match" else "code"
        links.append(f"[[{code_label}]({paper['code_url']})]")
        repo = github_repo_path(paper["code_url"])
        if repo:
            links.append(
                f"![GitHub stars](https://img.shields.io/github/stars/{repo}.svg?logo=github&label=Stars)"
            )
    for item in paper.get("links", []):
        links.append(f"[[{item['label']}]({item['url']})]")
    return " ".join(parts + links)


def recent_papers(papers: list[dict]) -> list[dict]:
    indexed = list(enumerate(papers))
    indexed.sort(
        key=lambda pair: (
            pair[1].get("added_at") or "",
            -pair[0],
        ),
        reverse=True,
    )
    return [paper for _, paper in indexed[:RECENT_VISIBLE]]


def render(papers: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for paper in papers:
        by_year[int(paper["year"])].append(paper)
    years = sorted(by_year, reverse=True)
    navigation = " · ".join(f"[{y} ({len(by_year[y])})](#{y})" for y in years)
    chunks = [f"**{len(papers)} papers** · {navigation}", "",
              "Papers can have multiple topics. [Search and combine topics](https://boom5426.github.io/Awesome-Virtual-Cell/) · [Tag definitions](docs/taxonomy.md)", ""]
    for year in years:
        chunks += [f'<a id="{year}"></a>', f"### 🗓️ {year} — {len(by_year[year])} papers", ""]
        for paper in by_year[year]:
            chunks += [render_entry(paper), ""]
    return "\n".join(chunks).rstrip() + "\n"


def load_challenges() -> dict:
    payload = json.loads(CHALLENGES.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise SystemExit("Expected data/challenges.json schema_version=1")
    return payload


def render_challenges(payload: dict) -> str:
    rows = payload["challenges"]
    if not rows:
        return "**Live challenges**: none open right now.\n"
    oldest = min(date.fromisoformat(c["checked_on"]) for c in rows)
    lines = [f"**Live challenges** (dates as published by the organizers, checked on "
             f"{oldest.day} {MONTHS[oldest.month - 1]} {oldest.year})", "",
             "| Challenge | Phase now | Next milestone | Final call |", "| --- | --- | --- | --- |"]
    for c in rows:
        lines.append(f"| [{c['name']}]({c['anchor']}) | {c['phase_now']} | {c['next_milestone']} | {c['final_call']} |")
    return "\n".join(lines) + "\n"


def challenge_warnings(payload: dict, today: date) -> list[str]:
    """Staleness notes for the live-challenges table; they warn and never fail a build."""
    notes: list[str] = []
    for c in payload["challenges"]:
        checked = date.fromisoformat(c["checked_on"])
        milestones = [(date.fromisoformat(m["date"]), m["label"]) for m in c["milestones"]]
        if milestones and max(when for when, _ in milestones) < today:
            notes.append(f"{c['name']}: its last milestone has passed; move it to the update log "
                         "and remove it from data/challenges.json")
            continue
        age = (today - checked).days
        if age > payload["stale_after_days"]:
            notes.append(f"{c['name']}: last checked {checked} ({age} days ago); re-check {', '.join(c['sources'])}")
        for when, label in milestones:
            if checked < when <= today:
                notes.append(f"{c['name']}: milestone '{label}' on {when} passed after the check on {checked}; "
                             "update the row")
    return notes


def replace_block(current: str, start: str, end: str, generated: str, name: str) -> str:
    if start not in current or end not in current:
        raise SystemExit(f"Generated {name} markers are missing from README.md")
    before, rest = current.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + "\n\n" + generated + "\n" + end + after


def updated_readme(current: str, generated: str) -> str:
    return replace_block(current, START, END, generated, "Research Papers")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    current = README.read_text(encoding="utf-8")
    challenges = load_challenges()
    target = updated_readme(current, render(load_papers()))
    target = replace_block(target, CH_START, CH_END, render_challenges(challenges), "Live Challenges")
    prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") == "true" else "WARN: "
    for note in challenge_warnings(challenges, date.today()):
        print(prefix + "Live challenges: " + note)
    if args.check:
        if current != target:
            print("README.md is out of date. Run: python scripts/build_readme.py")
            return 1
        print("README.md is synchronized with data/papers.json and data/challenges.json")
        return 0
    README.write_text(target, encoding="utf-8")
    print("Updated README.md from data/papers.json and data/challenges.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
