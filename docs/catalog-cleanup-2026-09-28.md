# Catalog cleanup follow-up — 2026-09-28

This follow-up starts from the code-link audit and addresses metadata/provenance issues that directly affect search, exports, deduplication, and the strict code-correspondence filter.

## Current catalog state

- Papers: **285**
- Code links: **205**
- Documented paper↔code correspondence: **198**
- Remaining `project_match`: **7**
- No established code link: **80**

## Changes in this pass

- Filled **37** DOI fields that were deterministically recoverable from formal publisher or preprint URLs.
- Normalized four direct-PDF preprint links to stable abstract/DOI URLs.
- Replaced empty or generic duplicate short labels and disambiguated the two unrelated TissueFormer entries.
- Added **11 previously missing code links**: PRESCRIBE, response decomposition, ExpressionVAE/design-space analysis, task-adapted FM analysis, scBench-Long, Tabular FM perturbation, Species-Native Tokens, Confound Diagnostics, CRISPRko-vs-CRISPRi, Gene Intelligence, and Tabula. DeSCOPE and AetherCell already had code URLs; this pass strengthened their provenance/status rather than adding new links.
- Upgraded 37 pre-existing `project_match` records only where stronger paper↔repository evidence was found.
- Corrected scDifformer's official code/weights release to the Hugging Face repository identified by the published paper; retained the previous GitHub project as an auxiliary project link.
- Marked OCellus and CellQ/PACE as `release_pending` based on their manuscript code-availability statements.
- The CellFM-datasets manuscript reports a GitHub code URL, but that repository returned 404 during this audit, so it is deliberately not counted as available code.
- The ST Agent Benchmark manuscript similarly points to `yiqunchen/Gen2Bench`, which returned 404 during this audit; it is not counted as available code.
- Spaceland's manuscript still states that source code is being prepared for release; a same-project public repository exists, but it remains `project_match` rather than documented paper correspondence.
- The publication watcher found **0** additional high-confidence preprint→formal-publication upgrades on 2026-09-28.

## Guardrails added

Regression tests now require non-empty unique display labels, DOI consistency for formal Nature/Springer article URLs, and the reviewed code/release-pending examples above.

As before, a code link establishes a source/code resource, not successful reproduction, complete dependencies, released checkpoints, or executable end-to-end training.
