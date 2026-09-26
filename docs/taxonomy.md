# Topic taxonomy

Topics are multi-label: a paper can match several independent aspects of a user query. The vocabulary is descriptive, not a quality ranking.

| Tag | Scope / boundary |
| --- | --- |
| Virtual Cell | Integrated cellular models or perspectives explicitly addressing virtual cells; not every single-cell method. |
| World Model | Cellular transition/simulation world-model formulation, or a paper specifically evaluating that formulation. |
| JEPA | Joint-embedding predictive objectives explicitly used or studied; not all self-distillation or contrastive learning. |
| Perturbation | Experimental or computational cellular intervention responses, including their prediction, analysis or evaluation. |
| Foundation Model | Broadly pretrained, transferable biological models, or studies specifically evaluating them. A transformer alone is insufficient. |
| Spatial | Tissue coordinates, neighborhoods, spatial omics or explicit spatial cellular interactions; not generic cell-state geometry. |
| Morphology | Microscopy, Cell Painting, image-derived phenotypes, histology or cell shape. |
| Protein | Protein-level measurements, localization, structure or functional readouts. PPI or protein-sequence priors alone do not qualify. |
| Agent | Autonomous scientific reasoning or tool-using AI systems. Agent-based biophysical simulation alone does not qualify. |
| Benchmark | A standardized task, challenge, dataset, leaderboard, or systematic model comparison. Routine model evaluation is insufficient. |
| Evaluation & Measurement | Evaluation protocols, metric behavior, empirical bounds/baselines, ground-truth reliability, measurement resolution, confounding, contamination, reproducibility, or benchmark validity. Can co-occur with Benchmark when both apply. |
| Tool | A reusable analysis, integration, processing or visualization workflow/framework. |
| Related | Adjacent molecular, biomedical or general scientific AI rather than core cell-state modeling. |
| Multimodal | Joint modeling/alignment of distinct assays, omics, images, biological text or chemical representations. Multiple datasets of one modality alone do not qualify. |
| Dynamics | Biological time, RNA velocity, trajectories, development, fate or temporal transitions. Diffusion-model sampling time alone does not qualify. |
| Gene Regulation | Gene-regulatory networks, regulatory sequences, transcription-factor activity or explicit regulatory-mechanism inference. |
| Intervention Design | Selecting or optimizing interventions towards a target state or outcome. Forward response prediction alone is insufficient. |
| Representation Learning | Reusable learned cell/gene/phenotype embeddings, including non-foundation methods. |
| Dataset | A primary atlas, dataset, structured biological resource or curated data collection. |
| Review | Reviews, perspectives, position papers, editorials, roadmaps, overviews or thesis-level syntheses. |

## Evidence and uncertainty

The 2026-09-26 curation work began with a full 275-record audit and was extended with source-checked Intervention Design and Evaluation & Measurement additions. The current catalog contains 285 papers.

Do not force tags merely because a model name contains “Agent”, “Spatial”, “Protein”, or “Foundation”. For example, veloAgent models spatial cell dynamics rather than being an LLM agent; SATURN/UCE/scNET use protein-related priors but are not automatically proteomics methods.

## Code correspondence

- **paper_linked**: a paper, author release or official model card supplies the implementation URL.
- **repository_linked**: the repository explicitly references this paper by title or identifier.
- **project_match**: the matching project and method are documented, but the inspected source does not establish an exact paper citation. Displayed as “Code (project)”, not counted by the verified-correspondence filter.
- **not_found / release_pending / related_only**: no established implementation link in the inspected evidence; this is not proof that no code exists.

Code inspection here checks identity and links, not whether training or inference reproduces the paper. Fork status alone does not decide officialness.


### Benchmark vs Evaluation & Measurement

Use **Benchmark** when a paper primarily defines a standardized task, challenge, dataset, leaderboard, or systematic model comparison. Use **Evaluation & Measurement** when the scientific question is whether an evaluation protocol, metric, experimental measurement, reference, bound, baseline, confound, or benchmark interpretation is valid or informative. The tags can co-occur.

Examples:

- Virtual Cell Challenge → `Benchmark`
- PertResolve → `Benchmark` + `Evaluation & Measurement`
- Towards Principled Evaluation → `Benchmark` + `Evaluation & Measurement`
- scContam → `Benchmark` + `Evaluation & Measurement`
