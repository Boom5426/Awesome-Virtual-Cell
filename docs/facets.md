# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **341 abstract-reviewed**, **22 project-documentation-reviewed**, and **33 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 202
- Representation Learning: 165
- Benchmarking: 73
- Gene Regulation: 55
- Evaluation & Measurement: 40
- Intervention Design: 38
- Scientific Agent: 34
- Tooling: 34
- Dynamics: 33
- Data Resource: 23
- World Modeling: 12

### modality

- Transcriptomics: 130
- Multimodal: 91
- Spatial: 62
- Morphology / Imaging: 55
- Proteomics: 36
- Sequence: 19
- Chromatin / Epigenomics: 16

### perturbation_type

- Chemical / Drug: 58
- Genetic: 52
- Combination: 8

### generalization

- Unseen Context: 19
- Unseen Perturbation: 16
- Zero-Shot: 12
- Cross-Dataset: 11
- Cross-Species: 10

### paper_type

- Method: 255
- Benchmark: 75
- Evaluation: 39
- Tool: 36
- Review: 26
- Dataset: 23

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
