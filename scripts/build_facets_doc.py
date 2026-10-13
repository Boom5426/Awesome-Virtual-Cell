#!/usr/bin/env python3
"""Render docs/facets.md (evidence basis and facet coverage) from data/papers.json and config/facets.json."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
CONFIG = ROOT / "config" / "facets.json"
DOC = ROOT / "docs" / "facets.md"


def render() -> str:
    papers = json.loads(DATA.read_text(encoding="utf-8"))["papers"]
    dimensions = json.loads(CONFIG.read_text(encoding="utf-8"))["dimensions"]
    basis = Counter(p["facet_review_basis"] for p in papers)
    lines = [
        "# Faceted catalog schema",
        "",
        "Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.",
        "",
        "## Evidence rule",
        "",
        f"Current evidence basis: **{basis['abstract']} abstract-reviewed**, "
        f"**{basis['project_documentation']} project-documentation-reviewed**, and "
        f"**{basis['title_and_metadata']} title/metadata-only provisional** records. "
        "Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.",
        "",
        "| Dimension | Meaning | Controlled values |",
        "| --- | --- | --- |",
    ]
    for name, spec in dimensions.items():
        lines.append(f"| `{name}` | {spec['description']} | {' · '.join(spec['values'])} |")
    lines += ["", "## Coverage", ""]
    for name, spec in dimensions.items():
        order = {value: i for i, value in enumerate(spec["values"])}
        counts = Counter(value for p in papers for value in p["facets"][name])
        lines += [f"### {name}", ""]
        for value, count in sorted(counts.items(), key=lambda kv: (-kv[1], order.get(kv[0], len(order)))):
            lines.append(f"- {value}: {count}")
        lines.append("")
    lines.append("Empty facet arrays mean the reviewed evidence did not support a confident assignment.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if docs/facets.md is out of date")
    args = parser.parse_args()
    document = render()
    if args.check:
        if DOC.read_text(encoding="utf-8") != document:
            print("docs/facets.md is out of date; run python scripts/build_facets_doc.py")
            return 1
        print("docs/facets.md is synchronized with data/papers.json")
        return 0
    DOC.write_text(document, encoding="utf-8")
    print("Wrote docs/facets.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
