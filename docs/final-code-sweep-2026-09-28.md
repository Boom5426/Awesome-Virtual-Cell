# Final code-link sweep — 2026-09-28

This pass follows the repository-wide code audit and catalog cleanup. It focuses on the remaining unresolved method/benchmark/tool/dataset records and the residual `project_match` entries.

## Coverage change

| Metric | Before | After |
| --- | ---: | ---: |
| Papers | 285 | 285 |
| Code links | 205 | 215 |
| Documented paper↔code correspondence | 198 | 212 |
| Weaker `project_match` | 7 | 3 |
| No established code link | 80 | 70 |

## Newly established code links

- **Zero-Shot Benchmark → scFMBench** — manuscript explicitly links the benchmark code.
- **Therapeutic Design → GPS** — the Cell study's released GPS platform and figure code.
- **CRISPRi Map → crispri_scrnaseq_hipsci** — analysis repository linked to the published resource.
- **Cytokine Atlas → CytoCarto** — manuscript code/project release.
- **Spurious Correlation → phillipnicol/systema** — repository documents the paper-specific analysis directories.
- **BRIDGE → tracy666/BRIDGE** — repository identifies itself as the official implementation.
- **Cell Line Bottleneck → VirtualCellWorkbench** — companion repository explicitly cites the exact 2026 bioRxiv paper and provides a reproduction toolkit.
- **Morph-Transcriptomic GenModel → MultiVCDiff** — published study's released implementation.
- **Perturbation Representation → PerturbedVAE** — public implementation and representation-collapse analysis for the named method.
- **PertDiffBench → ZijunSong/PertDiffBench** — same branded benchmark project with implementation, retained as `project_match` because the repository's displayed workshop title differs from the catalogued bioRxiv title.

## Strengthened existing correspondences

DeepSCENIC, VCHarness, CELLens, CellPB and GREmLN now have repository/project evidence sufficient for the strict documented-correspondence filter.

Spaceland and SQUINT remain `project_match`: their public repositories clearly implement the named projects, but the evidence inspected here does not justify upgrading them to exact paper↔repository correspondence.

## Deliberately not counted as code

- **scCycleMol:** an exact-name public GitHub repository exists but is empty (size 0), so it is not treated as released code.
- **Cell-JEPA:** the similarly named CellJEPA repository remains a different project.
- **ST Agent Benchmark / CellFM-Datasets:** previously reported GitHub release URLs were unavailable during the audit; unavailable links are not counted.
- **BioM-JEPA, OCellus, CellQ/PACE, scVision, HoloCell:** retained as release-pending where the manuscript/project states code is forthcoming.
- Exact-title searches for Speciesformer, CellOS, AnnFlux, scRep, DoFormer, PerturbPFN, HarmonyCell, StateXDiff, SCALE, AlphaCell, CellxPert, CisTransCell, BioWorldModel and several other unresolved methods did not establish a public official implementation during this pass.

An unresolved record means **no established public code link was verified in this audit**, not that the work is necessarily closed-source. Code presence also does not imply successful reproduction, released checkpoints, complete dependencies or executable end-to-end training.
