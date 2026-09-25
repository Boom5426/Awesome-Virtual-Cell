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

- `data/papers.json` is the structured source of truth for **Research Papers**.
- `README.md` remains the human-facing Awesome List.
- `docs/catalog.html` and `docs/index.html` are generated searchable views.
- `entry_markdown` is retained during migration so existing auxiliary links are not lost.

This is intentionally a transitional schema. Metadata is structured now, while the original entry rendering is preserved. A later normalization pass can render each entry entirely from structured fields.

## Build

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_catalog.py
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

`.github/workflows/pages.yml` deploys the `docs/` directory with the official GitHub Pages actions. The repository must have Pages configured to use **GitHub Actions** as its source before production deployment.

## Automated literature updates

`scripts/auto_update_catalog.py` reuses the conservative discovery logic from the previous updater but changes the write path:

```text
discover -> dedupe against catalog -> update JSON -> rebuild views -> validate -> draft PR
```

The workflow deliberately remains manual-dispatch-only until the v2 pipeline has been reviewed in practice.

## Migration boundary

The structured pipeline currently covers **Research Papers**. Datasets, challenges, reports, videos, and related resources remain Markdown-first and can be migrated incrementally after the paper pipeline is stable.
