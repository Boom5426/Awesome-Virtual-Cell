# Structured paper catalog

`papers.json` is the Schema v2 source of truth for the `Research Papers` section and the searchable catalog.

## Schema v2

Each paper contains structured metadata only:

- `id`: stable identifier
- `label`: short model/project name when available
- `title`, `year`, `venue`
- `status`: `published` or `preprint`
- `tags`: lightweight browsing topics
- `doi`
- `paper_url`, `preprint_url`, `code_url`
- `links`: auxiliary links such as project pages, datasets, Chinese summaries, or DeepWiki
- `added_at`, `updated_at`: ISO dates when known

Markdown is **not** stored in the data layer. README entries are generated from these fields.

## Generated views

```bash
python scripts/validate_catalog.py
python scripts/build_readme.py
python scripts/build_catalog.py
python scripts/build_exports.py
```

Generated artifacts:

- `README.md`
- `index.html`, `docs/index.html`, `docs/catalog.html`
- `exports/papers.csv`
- `exports/papers.bib`

Do not hand-edit the generated Research Papers block.
