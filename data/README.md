# Structured paper catalog

`papers.json` is the v2 source of truth for the `Research Papers` section.

## Schema

Each entry contains:

- `id`: stable, URL-friendly identifier
- `label`: short project/model name when available
- `title`: canonical paper title
- `year`: publication or preprint year
- `venue`: journal, conference, or preprint server
- `status`: `published` or `preprint`
- `tags`: lightweight browsing tags
- `doi`: DOI when the primary URL exposes one
- `paper_url`: formal paper URL when available
- `preprint_url`: preprint URL when separately available
- `code_url`: primary code repository when available
- `links`: other named links preserved from the original entry
- `entry_markdown`: migration-safe original README rendering

## Editing rule

For v2 research-paper changes, edit `data/papers.json` first and regenerate the views:

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_catalog.py
```

Do not hand-edit content inside the generated Research Papers block in `README.md`.
