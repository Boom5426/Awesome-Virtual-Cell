# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **524 abstract-reviewed**, **22 project-documentation-reviewed**, and **32 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 281
- Representation Learning: 223
- Benchmarking: 109
- Evaluation & Measurement: 94
- Gene Regulation: 78
- Dynamics: 58
- Scientific Agent: 57
- Tooling: 54
- Intervention Design: 50
- Data Resource: 34
- World Modeling: 17

### modality

- Transcriptomics: 275
- Multimodal: 137
- Spatial: 97
- Morphology / Imaging: 96
- Proteomics: 45
- Chromatin / Epigenomics: 31
- Sequence: 26

### perturbation_type

- Genetic: 110
- Chemical / Drug: 87
- Combination: 22

### generalization

- Unseen Context: 43
- Unseen Perturbation: 36
- Cross-Dataset: 25
- Zero-Shot: 23
- Cross-Species: 13

### paper_type

- Method: 380
- Benchmark: 110
- Evaluation: 80
- Tool: 53
- Dataset: 33
- Review: 24

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
