# Automated README Updates

**Status: the schedule is disabled.** The workflow no longer runs on its own. It
stays in the repository so it can be dispatched by hand from the Actions tab, and
the two-week `schedule` trigger is commented out at the top of the workflow file
if you want it back. README updates are curated manually for now.

This repository includes a GitHub Actions workflow that proposes literature updates as a draft pull request.

## What It Does

- runs on manual dispatch only
- scans a small set of curated update queries
- applies repository-specific scope and de-duplication rules
- updates `README.md` when high-confidence candidates are found
- opens a **draft PR** instead of pushing to `main`

## Review Model

The automation is intentionally conservative:

- it limits the number of additions per run
- it prefers high-signal venues and clearly relevant titles
- it writes a PR summary to explain why each item was proposed

You still review the PR before merge.

## Files

- workflow: `.github/workflows/auto-update-awesome.yml`
- rules: `config/auto_update_rules.json`
- update script: `scripts/auto_update_readme.py`

## Manual Run

To test locally:

```bash
python scripts/auto_update_readme.py --dry-run
```
