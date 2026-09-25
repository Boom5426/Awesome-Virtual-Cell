# Awesome-Virtual-Cell 2.0 Architecture

The v2 branch separates **content**, **rendering**, and **validation**.

```text
Literature Scout / human contributor
              |
              v
       data/papers.json
        /      |       \
       v       v        v
  README.md  catalog   future CSV/BibTeX
       ^       ^
       |       |
 build_readme.py   build_catalog.py
        \      /
         validator
```

## Source of truth

- `data/papers.json` is the structured source of truth for **Research Papers**.
- `README.md` remains the human-facing Awesome List.
- `docs/catalog.html` is a generated searchable view.
- `entry_markdown` is retained during the migration so no existing auxiliary links are lost.

This is intentionally a transitional schema: metadata is structured now, while the original entry rendering is preserved. A later normalization pass can render every entry entirely from fields such as `title`, `venue`, `tags`, and `links`.

## Build

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_catalog.py
```

To verify that committed generated files are current:

```bash
python scripts/build_readme.py --check
```

## Searchable catalog

`docs/catalog.html` is self-contained and can be opened through a static web server:

```bash
python -m http.server 8000
# then open http://localhost:8000/docs/catalog.html
```

It supports combined filtering by keyword, year, topic tag, and publication status.

## Migration boundary

In this MVP, only the `Research Papers` section has been migrated to structured data. Datasets, challenges, reports, videos, and related resources still use the original Markdown representation. They can be migrated incrementally after the paper pipeline is stable.

## Next migration step

The existing `scripts/auto_update_readme.py` is legacy and still proposes direct README edits. Before v2 is merged into `main`, the literature updater should be redirected to propose changes to `data/papers.json`, followed by regeneration of README and catalog outputs.
