# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **496 abstract-reviewed**, **22 project-documentation-reviewed**, and **33 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 274
- Representation Learning: 215
- Benchmarking: 109
- Evaluation & Measurement: 91
- Gene Regulation: 75
- Scientific Agent: 55
- Dynamics: 51
- Tooling: 51
- Intervention Design: 50
- Data Resource: 30
- World Modeling: 15

### modality

- Transcriptomics: 249
- Multimodal: 129
- Spatial: 92
- Morphology / Imaging: 89
- Proteomics: 44
- Chromatin / Epigenomics: 28
- Sequence: 26

### perturbation_type

- Genetic: 102
- Chemical / Drug: 88
- Combination: 21

### generalization

- Unseen Context: 41
- Unseen Perturbation: 36
- Cross-Dataset: 25
- Zero-Shot: 21
- Cross-Species: 13

### paper_type

- Method: 350
- Benchmark: 109
- Evaluation: 79
- Tool: 53
- Review: 32
- Dataset: 30

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
