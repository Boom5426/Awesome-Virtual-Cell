# Literature sweep — 2026-10-02

This local-only sweep expanded the structured catalog from 285 to 327 papers. It prioritized primary publication pages and preprint records, used repository and project pages only to establish code correspondence, and applied the repository's existing core/near-core virtual-cell scope.

## Coverage added

- Recent perturbation-response and virtual-cell methods, including papers posted in September 2026.
- Spatial transcriptomics, spatial proteomics, multimodal integration, and modality-translation methods.
- Single-cell foundation-model scaling, deployment, robustness, interpretability, and domain-specific evaluation.
- Roadmaps, perspectives, and reviews that sharpen the field's evaluation and validation boundaries.

Generic disease atlases and broad medical-AI papers without a direct cell-modeling, perturbation, or representation-learning contribution were left out.

## Records added

### Perturbation prediction, intervention, and signaling

- `recoverable-resolution` — The recoverable resolution of cellular perturbation-response prediction
- `pop-corn` — Pop-Corn: Predicting Perturbation Phenotype Effects Across Single-Cell and Spatial Contexts
- `perturbbridge` — PerturbBridge: Conditional Latent Schrödinger Bridge for Single-Cell Perturbation Response Prediction
- `biopert` — A biological-response compound representation allows chemical perturbation prediction across cell lines
- `spectra-perturb` — SPECTRA: predicting cellular perturbation responses with Graph Learning over Gene Regulatory Networks
- `isp3` — ISP³ Platform powered by Geneformer
- `cellrft` — CellRFT: Reinforcement Fine-Tuning for Single-Cell Perturbation Modeling
- `poppert` — PopPert: Population-level Joint-Distribution Modeling for Single-Cell Perturbation Prediction
- `scldm` — scLDM: a conditional diffusion framework for single-cell perturbation prediction
- `csgda` — CSGDA: A Cell State-Guided Graph Domain Adaptation Network for Single-Cell Drug Response Prediction
- `iris-signaling-history` — Reconstructing signaling histories of single cells via perturbation screens and transfer learning
- `map-unprofiled-drugs` — A knowledge-driven framework for predicting single-cell responses for unprofiled drugs
- `crisp` — Predicting drug responses of unseen cell types through transfer learning with foundation models
- `xpert` — Modelling drug-induced cellular perturbation responses with a biologically informed dual-branch transformer

### Spatial, multimodal, and representation methods

- `nexust` — NexuST: A Hierarchical Foundation Model for Spatial Transcriptomics
- `epizoo` — EpiZoo: a DNA sequence-aware foundation model for cross-species single-cell epigenomics
- `stformer` — stFormer integrates spatial ligand signaling into a foundation model for spatial transcriptomics
- `depass` — The dual-enhanced graph learning framework DePass allows paired data integration in single-cell and spatial multiomics
- `scdmc` — scDMC: Unlocking biological insight from single-cell data with an interpretable dual-stream foundation model
- `cellvq` — CellVQ: Illuminating cell states by a comprehensive and interpretable single cell foundation model
- `spatialformer` — SpatialFormer: universal spatial representation learning from subcellular molecular to multicellular landscapes
- `virtues` — The Virtual Tissues foundation model resolves spatial proteomics across scales
- `hex-virtual-proteomics` — AI-enabled virtual spatial proteomics from histopathology for interpretable biomarker discovery in lung cancer
- `spemo` — Leveraging Multi-Modal Foundation Models for Analyzing Spatial Multi-Omic and Histopathology Data
- `ragcell` — RAGCell: Retrieval-Augmented Generation as Supervision for Versatile Single-cell Analysis

### Benchmarks, scaling, and practical evaluation

- `aging-scfm-benchmark` — Benchmarking single-cell foundation models for aging biology
- `stp-bench` — STP-BENCH: A Unified Systematic Benchmark for Virtual Spatial Transcriptomics from Histopathology Images
- `scmbench` — SCMBench: benchmarking domain-specific and foundation models for single-cell multi-omics data integration
- `geneformer-v2` — Scaling and quantization of large-scale foundation model enables resource-efficient predictions in network biology
- `scaling-pain` — Scaling up training dataset size for transcriptomic AI models is much pain with little gain
- `benchmarking-biomedical-fms` — Benchmarking biomedical foundation models
- `sctranslation` — scTranslation: A Comprehensive Benchmark for Single-Cell Multi-Omics Modality Translation
- `nuisance-robustness` — Robustness to nuisance perturbations enables unsupervised evaluation of single-cell foundation models
- `scaling-recipes` — Scaling recipes for single-cell RNA sequencing foundation models: when do scaling laws hold?
- `accessible-scfm-deployment` — Accessible and reproducible deployment reveals the practical boundaries of single-cell foundation models
- `parameter-free-representations` — Parameter-free representations outperform single-cell foundation models on downstream benchmarks

### Reviews and field framing

- `trustworthy-virtual-cells` — Toward trustworthy virtual cells
- `interpretation-extrapolation-perturbation` — Interpretation, extrapolation and perturbation of single cells
- `ai-digital-organism` — How to build an AI-driven digital organism
- `world-models-biomedicine` — World models for biomedicine
- `fifteen-challenges` — Fifteen challenges for generative AI applications to cell biology
- `compositional-foundation-models` — From modality-specific to compositional foundation models for cell biology

## Generated surfaces

The sweep was applied to `data/papers.json`, then propagated through the repository generators to the README, web catalog, research landscape, CSV export, and BibTeX export. Historical audit documents retain the catalog counts that were correct when they were written.
