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

- Prefer peer-reviewed papers, strong preprints, and official project pages
- Use primary-source links when possible
- Avoid duplicate entries
- Avoid low-confidence sources, broken links, and overly broad biomedical AI resources with weak connection to virtual cells


## V2 Structured Catalog Workflow

Research-paper entries are maintained from `data/papers.json` on the v2 branch.

For paper additions or metadata updates:

1. Edit `data/papers.json` instead of the generated Research Papers block in `README.md`.
2. Run `python scripts/validate_catalog.py`.
3. Run `python scripts/build_readme.py`.
4. Run `python scripts/build_catalog.py`.
5. Commit the structured data and both generated views together.

CI rejects duplicate normalized titles, duplicate DOIs, malformed core metadata, or a README/catalog that is out of sync with the structured source of truth.

> The structured workflow currently covers **Research Papers** only. Other resource sections remain Markdown-first during the migration.

## Pull Request Notes

- Keep the entry style consistent with the surrounding section
- Put new research papers in the correct year bucket
- Use lightweight tags only as browsing hints, not as strict taxonomy
- Keep changes focused and easy to review
- Add one dated line to the `News` section at the top of the README describing what the PR changes
- If the entry is a competition with deadlines, also update the `Live challenges` table in `News`, and move the row into the update log once the competition closes

## How to Contribute

- Open an Issue for suggestions, corrections, or link reports
- Open a Pull Request for direct edits
- If you are not sure whether something fits, explain the connection to virtual cell research in the Issue or PR description

## Schema v2 note

Research papers are stored as structured metadata in `data/papers.json`. Do not add rendered Markdown fields. After changing paper metadata, regenerate README, catalog, CSV, and BibTeX outputs before submitting a PR.

## Tag and code review

Assign all applicable tags from [the controlled vocabulary](docs/taxonomy.md), with an abstract, methods or project-documentation basis. Do not treat an arbitrary transformer as a foundation model, protein priors as measured proteomics, or diffusion time as biological dynamics. A repository addition needs an author/paper link or documented paper correspondence. Put third-party reproductions and related implementations in named auxiliary links. Unknown code availability is not the same as code absence.

Regenerate all views and run tests before pushing one complete commit. Research Papers are shown in full, by year; keep overview/background sections selective.
