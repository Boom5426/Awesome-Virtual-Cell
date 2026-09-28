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

## Topics and repository correspondence

`tags` is a nonempty multi-label list using `config/taxonomy.json`. See [definitions](../docs/taxonomy.md). A tag describes the paper's scope, not a verified performance claim.

`code_status` distinguishes `paper_linked`, `repository_linked`, and `project_match` from `not_found`, `related_only`, `release_pending`, and `data_only`. Negative states must not populate `code_url`; auxiliary datasets and pending project pages belong under `links`. `code_sources` records the supporting URLs; `tag_review_basis` distinguishes abstracts, project documentation, and title/metadata-only provisional classification. A reachable repository is not by itself evidence of authorship or reproducibility.

The dated record in `curation/2026-09-26.json` preserves the earlier curation decisions. The [2026-09-28 code-link audit](../docs/code-audit-2026-09-28.md) and `curation/code-audit-2026-09-28.json` record newer code-link decisions, before/after metadata, search limitations, and unresolved cases.
\n## Evidence-backed facets\n\nEach paper stores `facets`, `facet_review_basis`, and `facet_sources`. Abstracts are primary evidence. See [docs/facets.md](../docs/facets.md).\n