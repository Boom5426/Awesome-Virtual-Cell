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
python scripts/build_exports.py
```

Check that README is synchronized:

```bash
python scripts/build_readme.py --check
```

## Searchable catalog

The catalog supports combined filtering by:

- free-text search
- year
- topic tag
- `published` vs `preprint`
- code availability in the displayed metadata

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

## Automated literature updates

`scripts/auto_update_catalog.py` reuses the conservative discovery logic from the previous updater but changes the write path:

```text
discover -> dedupe against catalog -> update JSON -> rebuild views -> validate -> draft PR
```

The workflow deliberately remains manual-dispatch-only until the v2 pipeline has been reviewed in practice.

## Migration boundary

The structured pipeline currently covers **Research Papers**. Datasets, challenges, reports, videos, and related resources remain Markdown-first and can be migrated incrementally after the paper pipeline is stable.

## Publication watcher

`scripts/publication_watcher.py` checks existing preprints against Crossref and proposes high-confidence upgrades to formal publications. A scheduled workflow opens draft PRs for human review.

## Exports

The full catalog is generated as `exports/papers.csv` and `exports/papers.bib`. The web catalog can also export the currently filtered result set.
\n## Evidence-backed facets\n\nThe catalog supports task, modality, perturbation-type, generalization and paper-type facets with per-paper evidence provenance.\n\n## Research Landscape\n\n`scripts/build_landscape.py` generates the interactive SVG mind map with zoom, pan, fit-to-view and filtered deep links.\n