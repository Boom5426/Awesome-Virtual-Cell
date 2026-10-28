# Contributing

Thanks for helping improve `Awesome Virtual Cell`.

## What to Submit

- New papers directly relevant to virtual cells, perturbation modeling, cellular foundation models, spatial or morphology modeling, evaluation, or biological AI agents
- New datasets, benchmarks, challenges, reports, talks, blogs, or project pages that are useful for the virtual cell community
- Link fixes, metadata corrections, and removals of low-confidence or broken entries

## Preferred Submission Format

Please include as much of the following as possible:

- Title
- Venue and year
- Primary paper or official project link
- Code link
- Dataset or benchmark link
- Short note on why the item is relevant to virtual cell research

## Quality Bar

- Published papers must come from a venue listed in [config/venue_policy.json](config/venue_policy.json). Papers in other journals are not accepted.
- Preprints must present a new method compared against established baselines, or a new dataset or benchmark. Reviews, perspectives and position papers wait for formal publication.
- Company and institute technical reports must be first-party and release a model, dataset or code, or report a quantitative evaluation. A blog that announces a listed paper becomes a link on that paper.
- Use primary-source links when possible
- Avoid duplicate entries
- Avoid low-confidence sources, broken links, and overly broad biomedical AI resources with weak connection to virtual cells


## V2 Structured Catalog Workflow

Research-paper entries are maintained from `data/papers.json` on the v2 branch.

For paper additions or metadata updates:

1. Edit `data/papers.json` instead of the generated Research Papers block in `README.md`.
2. Run `python scripts/validate_catalog.py`.
3. Run `python scripts/build_readme.py`.
4. Run `python scripts/build_catalog.py`, `python scripts/build_landscape.py`, `python scripts/build_exports.py` and `python scripts/build_facets_doc.py`.
5. Add a curation receipt for every new paper to `data/curation/2026-09-26.json` (tags, evidence basis, sources, code status); the validator rejects reviewed papers without one.
6. Commit the structured data and all generated views together.

CI rejects duplicate normalized titles, duplicate DOIs, malformed core metadata, published records that use a preprint DOI or preprint-server venue, published records whose venue is not in `config/venue_policy.json`, missing curation receipts, or a README/catalog/facet document that is out of sync with the structured source of truth.

> The structured workflow currently covers **Research Papers** only. Other resource sections remain Markdown-first during the migration.

## Pull Request Notes

- Keep the entry style consistent with the surrounding section
- Put new research papers in the correct year bucket
- Use lightweight tags only as browsing hints, not as strict taxonomy
- Keep changes focused and easy to review
- Add one dated line to the `News` section at the top of the README describing what the PR changes
- If the entry is a competition with deadlines, edit `data/challenges.json` (it renders the `Live challenges` table in `News`) and run `python scripts/build_readme.py`. Once the competition closes, add a dated line to the update log and remove its entry from that file

## How to Contribute

- Open an Issue for suggestions, corrections, or link reports
- Open a Pull Request for direct edits
- If you are not sure whether something fits, explain the connection to virtual cell research in the Issue or PR description

## Schema v2 note

Research papers are stored as structured metadata in `data/papers.json`. Do not add rendered Markdown fields. After changing paper metadata, regenerate README, catalog, CSV, and BibTeX outputs before submitting a PR.

## Tag and code review

Assign all applicable tags from [the controlled vocabulary](docs/taxonomy.md), with an abstract, methods or project-documentation basis. Do not treat an arbitrary transformer as a foundation model, protein priors as measured proteomics, or diffusion time as biological dynamics. A repository addition needs an author/paper link or documented paper correspondence. Put third-party reproductions and related implementations in named auxiliary links. Unknown code availability is not the same as code absence.

Regenerate all views and run tests before pushing one complete commit. Research Papers are shown in full, by year; keep overview/background sections selective.
