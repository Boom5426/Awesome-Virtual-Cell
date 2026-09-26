# Faceted catalog schema

Topics describe **what a paper is about**. Facets provide orthogonal search dimensions for task, modality, perturbation type, generalization regime, and paper type.

## Evidence rule

Current evidence basis: **251 abstract-reviewed**, **19 project-documentation-reviewed**, and **15 title/metadata-only provisional** records. Abstracts are primary. Provisional records do not receive inferred fine-grained perturbation/generalization facets.

| Dimension | Meaning | Controlled values |
| --- | --- | --- |
| `task` | Primary scientific/computational tasks. | Representation Learning · Perturbation Modeling · World Modeling · Dynamics · Gene Regulation · Intervention Design · Evaluation & Measurement · Benchmarking · Scientific Agent · Data Resource · Tooling |
| `modality` | Biological/readout modalities explicitly supported by reviewed evidence. | Transcriptomics · Proteomics · Morphology / Imaging · Spatial · Chromatin / Epigenomics · Sequence · Multimodal |
| `perturbation_type` | Intervention type explicitly supported by abstract/project evidence. | Genetic · Chemical / Drug · Combination |
| `generalization` | Generalization regime explicitly supported by abstract/project evidence. | Unseen Perturbation · Unseen Context · Cross-Dataset · Cross-Species · Zero-Shot |
| `paper_type` | Study/resource form. | Method · Benchmark · Evaluation · Dataset · Review · Tool |

## Coverage

### task

- Perturbation Modeling: 157
- Representation Learning: 125
- Benchmarking: 56
- Gene Regulation: 44
- Tooling: 28
- Intervention Design: 27
- Dynamics: 25
- Scientific Agent: 25
- Evaluation & Measurement: 21
- Data Resource: 16
- World Modeling: 12

### modality

- Multimodal: 70
- Transcriptomics: 61
- Spatial: 49
- Morphology / Imaging: 42
- Proteomics: 30
- Sequence: 13
- Chromatin / Epigenomics: 10

### perturbation_type

- Chemical / Drug: 33
- Genetic: 21
- Combination: 3

### generalization

- Cross-Species: 6
- Unseen Context: 4
- Unseen Perturbation: 2
- Cross-Dataset: 1

### paper_type

- Method: 182
- Benchmark: 56
- Tool: 28
- Evaluation: 21
- Review: 19
- Dataset: 16

Empty facet arrays mean the reviewed evidence did not support a confident assignment.
