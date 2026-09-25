# Automated Literature Updates

**V2 status: data-first, manual dispatch.**

The automation still runs only when manually dispatched from the Actions tab, but it no longer edits the Research Papers section directly. New research-paper candidates are written to the structured catalog first.

## Pipeline

```text
Crossref + curated seeds
        ↓
candidate discovery
        ↓
dedupe against data/papers.json
        ↓
data/papers.json
   ↙           ↘
README.md   docs/catalog.html
        ↓
validation
        ↓
draft pull request
```

## What It Does

- scans curated Crossref queries plus high-priority seeded candidates
- applies repository-specific scope and de-duplication rules
- currently accepts **Research Papers** into the v2 structured pipeline
- writes accepted candidates to `data/papers.json`
- regenerates `README.md` and the searchable catalog
- validates duplicate titles, duplicate DOIs, metadata, and generated-file synchronization
- opens a **draft PR** instead of pushing to `main`

Dataset/resource automation remains manual until those sections are migrated to structured data.

## Files

- workflow: `.github/workflows/auto-update-awesome.yml`
- rules: `config/auto_update_rules.json`
- v2 updater: `scripts/auto_update_catalog.py`
- discovery helpers (legacy-compatible): `scripts/auto_update_readme.py`
- validator: `scripts/validate_catalog.py`
- README generator: `scripts/build_readme.py`
- catalog generator: `scripts/build_catalog.py`
- export generator: `scripts/build_exports.py`
- publication watcher: `scripts/publication_watcher.py`

## Manual Run

Preview without writing:

```bash
python scripts/auto_update_catalog.py --dry-run
```

Run the full structured update:

```bash
python scripts/auto_update_catalog.py
python scripts/validate_catalog.py
python scripts/build_readme.py --check
```

The GitHub Action performs these checks before creating a draft PR.

## Publication upgrades

A separate weekly watcher checks preprints for formal journal/conference publications. Matches are title-similarity gated and are submitted as draft PRs rather than merged automatically.
