# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **486 abstract-reviewed**, **22 project-documentation-reviewed**, and **32 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 266
- Representation Learning: 213
- Benchmarking: 106
- Evaluation & Measurement: 87
- Gene Regulation: 74
- Scientific Agent: 55
- Tooling: 51
- Dynamics: 50
- Intervention Design: 49
- Data Resource: 30
- World Modeling: 15

### modality

- Transcriptomics: 245
- Multimodal: 127
- Spatial: 90
- Morphology / Imaging: 88
- Proteomics: 43
- Chromatin / Epigenomics: 28
- Sequence: 25

### perturbation_type

- Genetic: 97
- Chemical / Drug: 84
- Combination: 20

### generalization

- Unseen Context: 39
- Unseen Perturbation: 33
- Cross-Dataset: 25
- Zero-Shot: 21
- Cross-Species: 13

### paper_type

- Method: 348
- Benchmark: 107
- Evaluation: 78
- Tool: 53
- Dataset: 30
- Review: 24

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
