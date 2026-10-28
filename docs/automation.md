# Automated Curation

Automation proposes, a maintainer decides. No workflow pushes to `main` or adds a paper on its own.

| Workflow | Trigger | Output |
| --- | --- | --- |
| Weekly Curation (`.github/workflows/weekly-curation.yml`) | Mondays 04:00 UTC, or manual dispatch | one rolling draft PR with publication upgrades, and one digest issue with ranked candidates |
| Validate Catalog (`.github/workflows/catalog-ci.yml`) | push and pull request | validation, tests and byte-identical rebuilds of every generated view |
| Auto Update Awesome Virtual Cell (`.github/workflows/auto-update-awesome.yml`) | manual dispatch only | legacy Crossref discovery, as a draft PR |

## Inclusion policy in code

`config/venue_policy.json` holds the venue allowlist decided on 2026-10-28. `scripts/validate_catalog.py` rejects a published record whose venue is not listed, unless the venue ends in ` Technical Report`. The publication watcher and the candidate digest read the same file, so a policy change is one edit. The preprint bar (methods compared against baselines, or datasets and benchmarks) needs judgment and is applied by the maintainer when reviewing the digest.

## Publication watcher

`scripts/publication_watcher.py` scans every preprint in `data/papers.json` for a formal publication. No single source is complete, so it asks several in order of precedence and keeps the first applicable hit:

1. Crossref `is-preprint-of` relations on the preprint DOI.
2. The bioRxiv/medRxiv details API `published` field.
3. The arXiv API `doi` field.
4. The NeurIPS, ICML, ICLR and CVPR accepted-paper lists for this year and last year, matched by title (similarity of at least 0.90). The NeurIPS, ICML and ICLR lists come from each virtual site's `papers.html` page, and a hit takes the OpenReview forum linked from the poster page. The orals-posters JSON feed is not used: on 2026-10-28 two regenerations of the NeurIPS 2026 feed each held a different 62-70% subset of the 9,130 accepted papers. CVPR comes from the CVF open-access listing.
5. A Crossref title search, also at similarity 0.90.

The 2026-10-27 audit shows why the conference lists matter: Crossref found 1 of 9 upgrades and the lists found the other 8.

Hits are sorted into three groups:

- **Upgrades**: the venue is in the allowlist. Applied with `--apply`, at most `--max-updates` per run (default 10), highest similarity first.
- **Published outside the allowlist**: never applied. The maintainer decides whether to remove the record or to add the venue to the policy.
- **Review-only hints**: an arXiv `journal_ref` string, or a conference title between 0.75 and 0.90 similarity. Never applied.

A failed source is reported as a warning and the other sources still run. The run writes `publication_update_summary.md` (also shown on the Actions run page) and `publication_watch.json`, which the digest reads. The summary lists how many titles each conference list held, so a truncated list is visible.

The workflow commits upgrades to the fixed branch `auto/publication-watch` and opens or updates a single draft PR, instead of one PR per run.

## Candidate digest

`scripts/candidate_digest.py` builds the weekly issue:

- new records from the bioRxiv details API (first versions only), the arXiv API and Europe PMC (`SRC:MED`) over the window, with the queries in `config/digest.json`;
- records already in the catalog, and journal articles outside the venue policy, are dropped;
- the rest are scored with the keyword screen of the October sweeps (+2 per pattern in the title, +1 in the abstract, -3 without a cell term; patterns in `config/digest.json`);
- records scoring 3 or more are listed with an abstract snippet, records scoring 2 as titles only, highest score first;
- watcher items that need a decision and live-challenge warnings from `data/challenges.json` are listed at the top.

The workflow opens the issue "Curation digest YYYY-MM-DD" with the `curation-digest` label and closes older open digests. The digest does not read conference accepted lists. When a conference publishes its list, screen it once by hand, from the `papers.html` page.

### Why keyword screening, and why score 2

A learned ranker was tested before shipping. The backtest pool was every record the 2026-10-27 sweep pulled from bioRxiv, arXiv and Europe PMC for 2026-09-01 to 2026-10-27 that was not already in the catalog: 13,439 records, about 1,700 a week. The positives were the 124 sweep additions found in that pool. The gate, fixed in advance: ship a model if it reaches 90% recall within the top 300 records (about 2% of the pool), otherwise keep keyword screening.

| Ranker | Recall in top 40 | top 300 | top 1,000 | Depth for 90% recall |
| --- | --- | --- | --- | --- |
| Keyword screen | 0.218 | 0.677 | 0.952 | 711 |
| TF-IDF logistic regression, titles | 0.202 | 0.565 | 0.871 | 1,203 |
| TF-IDF logistic regression, title and abstract | 0.218 | 0.694 | 0.952 | 670 |

No ranker passed, so the digest keeps the keyword screen. The listing threshold is the smallest one that met the same 90% recall target: score 2 kept 96.0% of the positives (about 150 records a week), while score 3 kept 87.9% (about 66 a week). The positives were found through the same keyword screen, so these recalls are upper bounds. The result rules out this TF-IDF model as a filter. It does not rule out rankers built on text embeddings, or active learning from the maintainer's accept and reject decisions, which a future backtest against the same gate could test.

## Manual runs

```bash
python scripts/publication_watcher.py                  # dry run: writes the summary and report only
python scripts/publication_watcher.py --apply          # also edits data/papers.json
python -m scripts.candidate_digest --days 7            # writes candidate_digest.md
python -m scripts.auto_update_catalog --dry-run        # legacy Crossref discovery
```

`candidate_digest` and `auto_update_catalog` import from the `scripts` package, so run them with `python -m` from the repository root. After any change to `data/papers.json`, rebuild and check:

```bash
python scripts/build_readme.py && python scripts/build_catalog.py && python scripts/build_landscape.py
python scripts/build_exports.py && python scripts/build_facets_doc.py
python scripts/validate_catalog.py && python -m unittest discover -s tests && node tests/test_catalog_ui.cjs
```

## Legacy discovery

`scripts/auto_update_catalog.py` runs curated Crossref queries plus seeded candidates (`config/auto_update_rules.json`) and writes accepted papers to `data/papers.json`, then opens a draft PR. It predates the venue policy and the digest, stays manual-dispatch-only, and is kept for seeded additions.
