#!/usr/bin/env python3
"""Render a compact Research Papers block in README.md from Schema v2."""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
START = "<!-- GENERATED:RESEARCH-PAPERS:START -->"
END = "<!-- GENERATED:RESEARCH-PAPERS:END -->"
RECENT_VISIBLE = 10


def load_papers() -> list[dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 2:
        raise SystemExit("Expected data/papers.json schema_version=2")
    return payload["papers"]


def github_repo_path(url: str | None) -> str | None:
    if not url:
        return None
    match = re.search(r"github\\.com/([^/]+/[^/#?]+)", url)
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
        links.append(f"[[code]({paper['code_url']})]")
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

    recent = recent_papers(papers)
    recent_ids = {paper["id"] for paper in recent}
    chunks: list[str] = [
        "### ✨ Recent additions",
        "",
        f"The {RECENT_VISIBLE} most recent catalog additions are shown below. "
        "Use the [searchable catalog](https://boom5426.github.io/Awesome-Virtual-Cell/) "
        "to browse and filter the full collection.",
        "",
    ]
    for paper in recent:
        chunks += [render_entry(paper), ""]

    chunks += ["### 📂 More papers by year", ""]
    for year in sorted(by_year, reverse=True):
        remaining = [p for p in by_year[year] if p["id"] not in recent_ids]
        if not remaining:
            continue
        chunks += [
            f'<a id="{year}"></a>',
            "<details>",
            f"<summary><b>{year} — {len(remaining)} more papers</b></summary>",
            "",
        ]
        for paper in remaining:
            chunks += [render_entry(paper), ""]
        chunks += ["</details>", ""]
    return "\n".join(chunks).rstrip() + "\n"


def updated_readme(current: str, generated: str) -> str:
    if START not in current or END not in current:
        raise SystemExit("Generated Research Papers markers are missing from README.md")
    before, rest = current.split(START, 1)
    _, after = rest.split(END, 1)
    return before + START + "\n\n" + generated + "\n" + END + after


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    current = README.read_text(encoding="utf-8")
    target = updated_readme(current, render(load_papers()))
    if args.check:
        if current != target:
            print("README.md is out of date. Run: python scripts/build_readme.py")
            return 1
        print("README.md is synchronized with data/papers.json")
        return 0
    README.write_text(target, encoding="utf-8")
    print("Updated README.md from data/papers.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
