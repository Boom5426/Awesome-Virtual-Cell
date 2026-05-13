#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
RULES_PATH = ROOT / "config" / "auto_update_rules.json"
SUMMARY_PATH = ROOT / "auto_update_summary.md"

CROSSREF_API = "https://api.crossref.org/works"
BIORXIV_API = "https://api.biorxiv.org/details/biorxiv"
REQUEST_HEADERS = {
    "User-Agent": "Awesome-Virtual-Cell-AutoUpdater/1.0 (https://github.com/Boom5426/Awesome-Virtual-Cell)"
}


@dataclass
class Candidate:
    title: str
    label: str
    venue: str
    year: int
    section: str
    subsection: str | None
    tag: str | None
    primary_link: str
    code_link: str | None = None
    dataset_link: str | None = None
    doi: str | None = None
    rationale: str | None = None

    def dedupe_keys(self) -> set[str]:
        keys = {normalize_text(self.title), normalize_text(self.label)}
        if self.doi:
            keys.add(normalize_text(self.doi))
        keys.add(normalize_text(self.primary_link))
        if self.code_link:
            keys.add(normalize_text(self.code_link))
        if self.dataset_link:
            keys.add(normalize_text(self.dataset_link))
        return keys

    def to_markdown(self) -> str:
        parts: list[str] = [f"- **[{self.label}]**"]
        if self.tag and self.section == "research":
            parts.append(f"`[{self.tag}]`")
        parts.append(f"{self.title} (**{self.venue} {self.year}**)")
        links = [f"[[paper]({self.primary_link})]"]
        if self.code_link:
            links.append(f"[[code]({self.code_link})]")
            repo_path = github_repo_path(self.code_link)
            if repo_path:
                links.append(
                    f"![GitHub stars](https://img.shields.io/github/stars/{repo_path}.svg?logo=github&label=Stars)"
                )
        if self.dataset_link:
            links.append(f"[[dataset]({self.dataset_link})]")
        return " ".join(parts + links)


def normalize_text(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"https?://(dx\.)?doi\.org/", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def github_repo_path(url: str) -> str | None:
    match = re.search(r"github\.com/([^/]+/[^/#?]+)", url)
    if not match:
        return None
    return match.group(1).removesuffix(".git")


def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=REQUEST_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text())


def load_readme() -> str:
    return README_PATH.read_text()


def existing_readme_keys(readme_text: str) -> set[str]:
    keys: set[str] = set()
    for line in readme_text.splitlines():
        if line.startswith("- "):
            keys.add(normalize_text(line))
            title_match = re.search(r"\*\*\[[^\]]+\]\*\*\s+(?:`\[[^\]]+\]`\s+)?(.+?)\s+\(\*\*", line)
            if title_match:
                keys.add(normalize_text(title_match.group(1)))
        for doi in re.findall(r"https?://(?:dx\.)?doi\.org/([^\])\s]+)", line):
            keys.add(normalize_text(doi))
        for url in re.findall(r"https?://[^\])\s]+", line):
            keys.add(normalize_text(url))
        for biorxiv_id in re.findall(r"10\.\d{4,9}/[^\])\s]+", line, flags=re.IGNORECASE):
            keys.add(normalize_text(biorxiv_id))
    return keys


def title_matches_rules(title: str, rules: dict) -> bool:
    lowered = title.lower()
    topic_hit = any(keyword in lowered for keyword in rules["topic_keywords"])
    domain_hit = any(keyword in lowered for keyword in rules["domain_keywords"])
    return topic_hit and domain_hit


def venue_allowed(container_title: str, rules: dict) -> bool:
    return any(container_title.startswith(name) for name in rules["crossref_venue_allowlist"])


def infer_section(title: str) -> tuple[str, str | None]:
    lowered = title.lower()
    if any(word in lowered for word in ("dataset", "atlas", "benchmark", "challenge", "resource", "repository")):
        return "datasets", "datasets"
    return "research", None


def infer_tag(title: str, rules: dict) -> str | None:
    lowered = title.lower()
    for tag, keywords in rules["tag_rules"].items():
        if any(keyword in lowered for keyword in keywords):
            return tag
    return None


def infer_label(title: str) -> str:
    leading = re.split(r"[:\-]", title, maxsplit=1)[0].strip()
    if 2 <= len(leading) <= 24 and leading[0].isalnum():
        return leading
    words = re.findall(r"[A-Za-z0-9]+", title)
    caps = [word for word in words if word.isupper() and len(word) > 1]
    if caps:
        return caps[0]
    stop = {"a", "an", "the", "of", "for", "and", "to", "with", "through", "using", "in"}
    filtered = [word for word in words if word.lower() not in stop]
    initials = "".join(word[0].upper() for word in filtered[:4])
    return initials or words[0][:12]


def infer_code_link(doi: str | None, title: str) -> str | None:
    known = {
        "10.1016/j.cell.2025.05.027": None,
        "10.1016/j.cell.2025.02.012": None,
        "10.1016/j.cell.2022.05.013": "https://github.com/thomasmaxwellnorman/Perturbseq_GI",
        "10.1126/science.abi6983": "https://registry.opendata.aws/czb-opencell/",
        "10.1126/science.aal3321": None,
        "10.1016/j.cell.2017.10.049": None,
        "10.64898/2026.03.13.710968": None,
    }
    if doi and doi in known:
        link = known[doi]
        if link and "registry.opendata.aws" not in link:
            return link
        return None

    lowered = title.lower()
    if "hest-1k" in lowered:
        return "https://github.com/mahmoodlab/HEST"
    if "three million images and morphological profiles" in lowered:
        return "https://github.com/jump-cellpainting/2024_Chandrasekaran_NatureMethods"
    return None


def infer_dataset_link(doi: str | None, title: str) -> str | None:
    if doi == "10.1016/j.cell.2017.10.049":
        return "https://clue.io/data/CMap2020#LINCS2020"
    lowered = title.lower()
    if "three million images and morphological profiles" in lowered:
        return "https://registry.opendata.aws/cellpainting-gallery/"
    if "a subcellular map of the human proteome" in lowered:
        return "https://www.proteinatlas.org/humanproteome/subcellular"
    if "opencell" in lowered:
        return "https://registry.opendata.aws/czb-opencell/"
    return None


def crossref_candidates(rules: dict, cutoff_date: str) -> list[Candidate]:
    candidates: list[Candidate] = []
    for query in rules["crossref_queries"]:
        params = {
            "query.title": query,
            "filter": f"from-pub-date:{cutoff_date}",
            "rows": "20",
            "sort": "published",
            "order": "desc",
            "select": "title,DOI,URL,container-title,published-print,published-online,type",
        }
        url = f"{CROSSREF_API}?{urllib.parse.urlencode(params)}"
        try:
            data = http_get_json(url)
        except urllib.error.URLError:
            continue
        for item in data.get("message", {}).get("items", []):
            titles = item.get("title") or []
            containers = item.get("container-title") or []
            if not titles or not containers:
                continue
            title = titles[0].strip()
            venue = containers[0].strip()
            if not venue_allowed(venue, rules):
                continue
            if not title_matches_rules(title, rules):
                continue
            year = extract_year(item)
            if not year:
                continue
            section, subsection = infer_section(title)
            doi = item.get("DOI")
            candidates.append(
                Candidate(
                    title=title,
                    label=infer_label(title),
                    venue=venue,
                    year=year,
                    section=section,
                    subsection=subsection,
                    tag=infer_tag(title, rules),
                    primary_link=item.get("URL") or f"https://doi.org/{doi}",
                    code_link=infer_code_link(doi, title),
                    dataset_link=infer_dataset_link(doi, title),
                    doi=doi,
                    rationale=f"Matched Crossref query '{query}'",
                )
            )
    return candidates


def extract_year(item: dict) -> int | None:
    for field in ("published-print", "published-online", "issued"):
        parts = item.get(field, {}).get("date-parts") or []
        if parts and parts[0]:
            return int(parts[0][0])
    return None


def seeded_manual_candidates() -> list[Candidate]:
    return [
        Candidate(
            title="AetherCell: A generative engine for virtual cell perturbation and in vivo drug discovery",
            label="AetherCell",
            venue="bioRxiv",
            year=2026,
            section="research",
            subsection=None,
            tag="Virtual Cell",
            primary_link="https://www.biorxiv.org/content/10.64898/2026.03.13.710968v1",
            rationale="Seeded high-priority virtual cell perturbation preprint",
        ),
        Candidate(
            title="STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging",
            label="STAMP",
            venue="Cell",
            year=2025,
            section="research",
            subsection=None,
            tag="Tool",
            primary_link="https://doi.org/10.1016/j.cell.2025.05.027",
            rationale="Seeded multimodal imaging/transcriptomics paper",
        ),
        Candidate(
            title="Simultaneous CRISPR screening and spatial transcriptomics reveal intracellular, intercellular, and functional transcriptional circuits",
            label="Perturb-FISH",
            venue="Cell",
            year=2025,
            section="research",
            subsection=None,
            tag="Spatial",
            primary_link="https://doi.org/10.1016/j.cell.2025.02.012",
            rationale="Seeded spatial perturbation paper",
        ),
        Candidate(
            title="A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles",
            label="L1000/CMap",
            venue="Cell",
            year=2017,
            section="datasets",
            subsection="datasets",
            tag=None,
            primary_link="https://doi.org/10.1016/j.cell.2017.10.049",
            dataset_link="https://clue.io/data/CMap2020#LINCS2020",
            rationale="Seeded foundational perturbation dataset",
        ),
        Candidate(
            title="Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations",
            label="CPJUMP1",
            venue="Nature Methods",
            year=2024,
            section="datasets",
            subsection="datasets",
            tag=None,
            primary_link="https://www.nature.com/articles/s41592-024-02241-6",
            code_link="https://github.com/jump-cellpainting/2024_Chandrasekaran_NatureMethods",
            dataset_link="https://registry.opendata.aws/cellpainting-gallery/",
            rationale="Seeded matched chemical/genetic morphology resource",
        ),
        Candidate(
            title="HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis",
            label="HEST-1k",
            venue="NeurIPS",
            year=2024,
            section="datasets",
            subsection="datasets",
            tag=None,
            primary_link="https://arxiv.org/abs/2406.16192",
            code_link="https://github.com/mahmoodlab/HEST",
            rationale="Seeded spatial transcriptomics and histology dataset",
        ),
        Candidate(
            title="A subcellular map of the human proteome",
            label="HPA Cell Atlas",
            venue="Science",
            year=2017,
            section="historical",
            subsection=None,
            tag="Morphology",
            primary_link="https://doi.org/10.1126/science.aal3321",
            dataset_link="https://www.proteinatlas.org/humanproteome/subcellular",
            rationale="Seeded protein localization resource",
        ),
        Candidate(
            title="OpenCell: Endogenous tagging for the cartography of human cellular organization",
            label="OpenCell",
            venue="Science",
            year=2022,
            section="historical",
            subsection=None,
            tag="Morphology",
            primary_link="https://doi.org/10.1126/science.abi6983",
            dataset_link="https://registry.opendata.aws/czb-opencell/",
            rationale="Seeded endogenous tagging atlas",
        ),
        Candidate(
            title="Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq",
            label="Perturb-seq",
            venue="Cell",
            year=2022,
            section="historical",
            subsection=None,
            tag="Perturbation",
            primary_link="https://doi.org/10.1016/j.cell.2022.05.013",
            code_link="https://github.com/thomasmaxwellnorman/Perturbseq_GI",
            rationale="Seeded foundational genome-scale Perturb-seq paper",
        ),
    ]


def dedupe_candidates(candidates: Iterable[Candidate], readme_keys: set[str]) -> list[Candidate]:
    seen = set(readme_keys)
    kept: list[Candidate] = []
    for candidate in candidates:
        keys = candidate.dedupe_keys()
        if keys & seen:
            continue
        kept.append(candidate)
        seen.update(keys)
    return kept


def insert_line_after_anchor(text: str, anchor: str, line: str) -> str:
    marker = f"{anchor}\n\n"
    if marker not in text:
        raise ValueError(f"Anchor not found: {anchor}")
    return text.replace(marker, f"{anchor}\n\n{line}\n\n", 1)


def insert_research_candidate(text: str, candidate: Candidate) -> str:
    heading = f"### {candidate.year}"
    pattern = re.compile(rf"({re.escape(heading)}\n\n)", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Year heading not found: {heading}")
    start = match.end()
    return text[:start] + candidate.to_markdown() + "\n\n" + text[start:]


def insert_dataset_candidate(text: str, candidate: Candidate) -> str:
    return insert_line_after_anchor(text, "### Datasets", candidate.to_markdown())


def insert_historical_candidate(text: str, candidate: Candidate) -> str:
    return insert_line_after_anchor(text, "## Historical and Foundational Works", candidate.to_markdown())


def apply_candidates(readme_text: str, candidates: list[Candidate]) -> str:
    updated = readme_text
    for candidate in sorted(candidates, key=sort_key):
        if candidate.section == "research":
            updated = insert_research_candidate(updated, candidate)
        elif candidate.section == "datasets":
            updated = insert_dataset_candidate(updated, candidate)
        elif candidate.section == "historical":
            updated = insert_historical_candidate(updated, candidate)
        else:
            raise ValueError(f"Unsupported section: {candidate.section}")
    return updated


def sort_key(candidate: Candidate) -> tuple[int, int, str]:
    section_order = {"research": 0, "datasets": 1, "historical": 2}
    return (section_order[candidate.section], -candidate.year, candidate.title.lower())


def summary_markdown(candidates: list[Candidate]) -> str:
    today = dt.date.today().isoformat()
    lines = [
        "# Automated README Update Summary",
        "",
        f"- Date: {today}",
        f"- Added items: {len(candidates)}",
        "",
        "## Proposed Additions",
        "",
    ]
    for candidate in candidates:
        location = candidate.section
        if candidate.section == "research":
            location = f"Research Papers / {candidate.year}"
        elif candidate.section == "datasets":
            location = "Datasets and Benchmarks / Datasets"
        elif candidate.section == "historical":
            location = "Historical and Foundational Works"
        lines.extend(
            [
                f"- **{candidate.label}**",
                f"  - Title: {candidate.title}",
                f"  - Source: {candidate.venue} {candidate.year}",
                f"  - Suggested section: {location}",
                f"  - Why: {candidate.rationale or 'Matched update rules'}",
                f"  - Primary link: {candidate.primary_link}",
            ]
        )
    lines.extend(
        [
            "",
            "## Review Notes",
            "",
            "- This PR is created as `draft` by automation.",
            "- Please verify relevance, metadata, and placement before merging.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(readme_text: str, candidates: list[Candidate]) -> None:
    README_PATH.write_text(readme_text)
    SUMMARY_PATH.write_text(summary_markdown(candidates))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-additions", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rules = load_rules()
    readme_text = load_readme()
    cutoff = (dt.date.today() - dt.timedelta(days=180)).isoformat()
    candidates = seeded_manual_candidates() + crossref_candidates(rules, cutoff)
    unique_candidates = dedupe_candidates(candidates, existing_readme_keys(readme_text))
    max_additions = args.max_additions or int(rules["max_additions_per_run"])
    chosen = unique_candidates[:max_additions]

    if not chosen:
        SUMMARY_PATH.write_text(
            "# Automated README Update Summary\n\n- No high-confidence additions were found in this run.\n"
        )
        print("No changes.")
        return 0

    updated_readme = apply_candidates(readme_text, chosen)
    if args.dry_run:
        print(summary_markdown(chosen))
        return 0

    write_outputs(updated_readme, chosen)
    print(f"Updated README with {len(chosen)} additions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
