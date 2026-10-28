# Awesome-Virtual-Cell 2.0 Architecture

V2 separates **content**, **discovery**, **rendering**, **validation**, and **delivery**.

```text
          Literature Scout / Contributor
                     |
                     v
              Candidate discovery
                     |
                     v
              data/papers.json
             /       |        \
            v        v         v
       README.md   Catalog   future exports
            ^        ^
            |        |
       generators + validator
                     |
                     v
                 Draft PR

Catalog -> GitHub Pages -> searchable web UI
```

## Source of truth

- `data/papers.json` (Schema v2) is the structured source of truth for **Research Papers**; generated Markdown is not stored in the data layer.
- `README.md` remains the human-facing Awesome List.
- `docs/catalog.html` and `docs/index.html` are generated searchable views.

## Build

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_catalog.py
python scripts/build_landscape.py
python scripts/build_exports.py
python scripts/build_facets_doc.py
```

Check that README and the facet documentation are synchronized:

```bash
python scripts/build_readme.py --check
python scripts/build_facets_doc.py --check
```

## Searchable catalog

The catalog supports combined filtering by:

- free-text search
- year and `published` vs `preprint`
- multi-label topic filtering with AND/OR matching
- task, modality, perturbation type, generalization and paper-type facets
- code availability, including a stricter documented-correspondence filter

Local preview:

```bash
python -m http.server 8000
# open http://localhost:8000/docs/
```

Public target URL:

```text
https://boom5426.github.io/Awesome-Virtual-Cell/
```

GitHub Pages is published from the repository through the built-in Pages/Jekyll deployment. The root `index.html` is generated from the same structured catalog, so the public homepage opens directly into the searchable interface.

## Automated curation

The Weekly Curation workflow runs the publication watcher and the candidate digest every Monday. Both write through the same path as manual edits:

```text
discover -> dedupe against catalog -> venue policy -> update JSON or open digest issue -> rebuild views -> validate -> draft PR
```

`scripts/auto_update_catalog.py`, the earlier Crossref updater, stays manual-dispatch-only. See [automation.md](automation.md) for sources, gates and manual runs.

## Migration boundary

The structured pipeline currently covers **Research Papers** and the **Live challenges** table in News. The table is rendered from `data/challenges.json` by `scripts/build_readme.py`, which also prints a warning when a row is older than `stale_after_days`, when a milestone has passed since the last check, or when a competition has ended. Datasets, the challenge write-ups, reports, videos, and related resources remain Markdown-first and can be migrated incrementally after the paper pipeline is stable.

## Publication watcher

`scripts/publication_watcher.py` checks existing preprints against Crossref relations, the bioRxiv and arXiv APIs, the NeurIPS/ICML/ICLR/CVPR accepted-paper lists and a Crossref title search. Upgrades into allowlisted venues go to one rolling draft PR; publications outside `config/venue_policy.json` and near-miss titles are reported, never applied.

## Exports

The full catalog is generated as `exports/papers.csv` and `exports/papers.bib`. The web catalog can also export the currently filtered result set.
## Evidence-backed facets

The catalog supports task, modality, perturbation-type, generalization and paper-type facets with per-paper evidence provenance.

## Research Landscape

`scripts/build_landscape.py` generates the interactive SVG mind map with zoom, pan, fit-to-view and filtered deep links.
