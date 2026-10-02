# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **275 abstract-reviewed**, **19 project-documentation-reviewed**, and **33 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 173
- Representation Learning: 137
- Benchmarking: 61
- Gene Regulation: 49
- Intervention Design: 31
- Tooling: 31
- Dynamics: 30
- Evaluation & Measurement: 27
- Scientific Agent: 25
- Data Resource: 17
- World Modeling: 12

### modality

- Transcriptomics: 82
- Multimodal: 76
- Spatial: 55
- Morphology / Imaging: 44
- Proteomics: 31
- Sequence: 15
- Chromatin / Epigenomics: 11

### perturbation_type

- Chemical / Drug: 43
- Genetic: 30
- Combination: 6

### generalization

- Unseen Context: 11
- Cross-Dataset: 10
- Cross-Species: 9
- Unseen Perturbation: 7
- Zero-Shot: 2

### paper_type

- Method: 206
- Benchmark: 63
- Tool: 32
- Evaluation: 30
- Review: 25
- Dataset: 17

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
