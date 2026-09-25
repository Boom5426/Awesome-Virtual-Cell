#!/usr/bin/env python3
"""Render a compact Research Papers block in README.md from data/papers.json."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
START = "<!-- GENERATED:RESEARCH-PAPERS:START -->"
END = "<!-- GENERATED:RESEARCH-PAPERS:END -->"
RECENT_VISIBLE = 12


def load_papers() -> list[dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    return payload["papers"]


def render(papers: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for paper in papers:
        by_year[int(paper["year"])].append(paper)

    recent = papers[:RECENT_VISIBLE]
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
        chunks += [paper["entry_markdown"].rstrip(), ""]

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
            chunks += [paper["entry_markdown"].rstrip(), ""]
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
