#!/usr/bin/env python3
"""Generate full-catalog CSV and BibTeX exports from Schema v2."""
from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
OUT_DIR = ROOT / "exports"


def load_papers() -> list[dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 2:
        raise SystemExit("Expected schema_version=2")
    return payload["papers"]


def csv_text(papers: list[dict]) -> str:
    buf = io.StringIO()
    fields = [
        "id","label","title","year","venue","status","tags","doi",
        "paper_url","preprint_url","code_url","added_at","updated_at",
    ]
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for p in papers:
        row = {k: p.get(k) for k in fields}
        row["tags"] = "|".join(p.get("tags", []))
        writer.writerow({k: "" if v is None else v for k, v in row.items()})
    return buf.getvalue()


def bib_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    for char in ("&", "%", "#", "_"):
        value = value.replace(char, "\\" + char)
    return value


def bibtex_text(papers: list[dict]) -> str:
    entries: list[str] = []
    for p in papers:
        kind = "article" if p.get("status") == "published" else "misc"
        key = re.sub(r"[^A-Za-z0-9:_-]+", "-", p["id"]).strip("-") or "paper"
        url = p.get("paper_url") or p.get("preprint_url") or ""
        fields = [
            ("title", p["title"]),
            ("year", str(p["year"])),
        ]
        if p.get("venue"):
            fields.append(("journal" if kind == "article" else "howpublished", p["venue"]))
        if p.get("doi"):
            fields.append(("doi", p["doi"]))
        if url:
            fields.append(("url", url))
        body = ",\n".join(f"  {name} = {{{bib_escape(value)}}}" for name, value in fields)
        entries.append(f"@{kind}{{{key},\n{body}\n}}")
    return "\n\n".join(entries) + "\n"


def main() -> int:
    papers = load_papers()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "papers.csv").write_text(csv_text(papers), encoding="utf-8")
    (OUT_DIR / "papers.bib").write_text(bibtex_text(papers), encoding="utf-8")
    print(f"Wrote CSV and BibTeX exports for {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
