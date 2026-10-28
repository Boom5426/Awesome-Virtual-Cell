# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **498 abstract-reviewed**, **22 project-documentation-reviewed**, and **32 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 269
- Representation Learning: 215
- Benchmarking: 108
- Evaluation & Measurement: 89
- Gene Regulation: 77
- Scientific Agent: 56
- Dynamics: 53
- Tooling: 51
- Intervention Design: 49
- Data Resource: 31
- World Modeling: 15

### modality

- Transcriptomics: 255
- Multimodal: 130
- Spatial: 93
- Morphology / Imaging: 92
- Proteomics: 43
- Chromatin / Epigenomics: 29
- Sequence: 25

### perturbation_type

- Genetic: 100
- Chemical / Drug: 85
- Combination: 20

### generalization

- Unseen Context: 40
- Unseen Perturbation: 34
- Cross-Dataset: 25
- Zero-Shot: 22
- Cross-Species: 13

### paper_type

- Method: 358
- Benchmark: 109
- Evaluation: 79
- Tool: 53
- Dataset: 31
- Review: 24

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
