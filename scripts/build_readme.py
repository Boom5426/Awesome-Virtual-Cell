#!/usr/bin/env python3
"""Render the Research Papers block in README.md from data/papers.json."""
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


def load_papers() -> list[dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    return payload["papers"]


def render(papers: list[dict]) -> str:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for paper in papers:
        by_year[int(paper["year"])].append(paper)
    chunks: list[str] = []
    for year in sorted(by_year, reverse=True):
        chunks += [f'<a id="{year}"></a>', f"### 🗓️ {year}", ""]
        for paper in by_year[year]:
            chunks += [paper["entry_markdown"].rstrip(), ""]
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
