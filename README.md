# Awesome Virtual Cell [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of papers, datasets, benchmarks, talks, and community resources for AI-powered virtual cell research.

Here, **AIVC** stands for **Artificial Intelligence Virtual Cell**, a term popularized by the *Cell* perspective ["How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities."](https://doi.org/10.1016/j.cell.2024.11.015) The focus of this repository is broad but practical: resources that help researchers understand, model, benchmark, or build virtual cells and related cellular foundation models.

For scientific figure ideas and plotting templates, see [Awesome Scientific Figures](Awesome-Scientific-Figures/README_Figure.md).

## Contents

- [Scope](#scope)
- [Inclusion Rules](#inclusion-rules)
- [Overview Papers](#overview-papers)
- [Research Papers](#research-papers)
- [Datasets](#datasets)
- [Reports and Blogs](#reports-and-blogs)
- [Videos](#videos)
- [Historical and Foundational Works](#historical-and-foundational-works)
- [Related Resources](#related-resources)

## Scope

- In scope: virtual cell perspectives, perturbation modeling, single-cell and multimodal foundation models, spatial and morphology modeling, biological AI agents, datasets, benchmarks, and community resources closely connected to virtual cell research.
- Also included: adjacent work that is broadly useful for the virtual cell community, especially when it contributes data, evaluation methods, or modeling tools for cellular systems.
- Usually out of scope: generic biomedical AI work with weak cell-modeling relevance, low-confidence secondary sources, broken links, or items that do not add clear value beyond more central references already listed here.

## Inclusion Rules

- Prefer peer-reviewed papers, high-signal preprints, official project pages, and primary-source links.
- Include code, datasets, project pages, or Chinese summaries when they are clearly useful.
- Keep entries concise and broadly reusable for readers who are scanning the field.
- Use lightweight tags in `Research Papers` only as browsing aids. They are intentionally approximate, not rigid taxonomy.

## Overview Papers

- **[Nature News]** Can AI Build a Virtual Cell? Scientists Race to Model Life's Smallest Unit (**Nature 2025**) [[paper](https://www.nature.com/articles/d41586-025-02011-0)] [[中文解读](https://mp.weixin.qq.com/s/s-tH8ccpyBAag_QMpv0toQ)]

- **[Nature Perspective]** Towards Multimodal Foundation Models in Molecular Cell Biology (**Nature 2025**) [[paper](https://www.nature.com/articles/s41586-025-08710-y)] [[中文解读](https://mp.weixin.qq.com/s/BQw0kzfcREYHAyaYqm5MrA)]

- **[Nature Methods]** The virtual cell (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-025-02951-5)]

- **[Nature]** The Human Cell Atlas from a cell census to a unified foundation model (**Nature 2024**) [[paper](https://www.nature.com/articles/s41586-024-08338-4)]

- **[Nature Review]** Interpretation, extrapolation and perturbation of single cells (**Nature Reviews Genetics 2026**) [[paper](https://www.nature.com/articles/s41576-025-00920-4)]

- **[Nature Review]** Revisiting the blueprint for an interpretable virtual cell (**Nature Reviews Genetics 2026**) [[paper](https://www.nature.com/articles/s41576-026-00940-8)]

- **[npj Digital Medicine]** AI-driven virtual cell models in preclinical research: technical pathways, validation mechanisms, and clinical translation potential (**npj Digital Medicine 2025**) [[paper](https://www.nature.com/articles/s41746-025-02198-6)]

- **[Nature Review]** Adapting systems biology to address the complexity of human disease in the single-cell era (**Nature Reviews Genetics 2025**) [[paper](https://www.nature.com/articles/s41576-025-00821-6)]

- **[Nature Genetics]** Causal machine learning for single-cell genomics (**Nature Genetics 2025**) [[paper](https://www.nature.com/articles/s41588-025-02124-2)]

- **[Nature Methods]** Multimodal foundation transformer models for multiscale genomics (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-025-02918-6)]

- **[Cell Perspective]** Empowering Biomedical Discovery with AI Agents (**Cell 2024**) [[paper](https://www.cell.com/cell/fulltext/S0092-8674(24)01070-5)] [[中文解读](https://mp.weixin.qq.com/s/QX1jzqrIMjy4_fL6brfYlQ)]

- **[Cell Perspective]** How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities (**Cell 2024**) [[paper](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1)] [[中文解读](https://mp.weixin.qq.com/s/JSV6zclrx3UloG401khHRQ)]

- **[Cell Review]** Toward a Foundation Model of Causal Cell and Tissue Biology with a Perturbation Cell and Tissue Atlas (**Cell 2024**) [[paper](https://doi.org/10.1016/j.cell.2024.07.035)] [[中文解读](https://mp.weixin.qq.com/s/uXdSz-XCR_2gC2enwN_lDg)]

## Research Papers

Tag hints: `[Virtual Cell]`, `[Perturbation]`, `[Foundation Model]`, `[Spatial]`, `[Morphology]`, `[Agent]`, `[Benchmark]`, `[Tool]`, `[Related]`. Tags are lightweight and non-exhaustive.

### 2026

- **[Tabular FM Perturbation]** `[Foundation Model]` Tabular Foundation Models Are Competitive Cellular Perturbation Predictors Across Biological Scales (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.28.735106)]

- **[CellFM-Datasets]** `[Foundation Model]` Cellfm-datasets: A Unified Data Infrastructure for Single-Cell and Spatial Transcriptomics Foundation Model Pretraining (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.11.731508)]

- **[OCOO-T]** `[Virtual Cell]` OCOO-T : A Simple and Scalable Virtual Cell Model for Transcriptional Perturbation Response Prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2606.12838)]

- **[Glitch Genes]** `[Foundation Model]` Glitch genes: embedding geometry predicts functional fragility in single-cell foundation models (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.22.733850)]

- **[VCBench]** `[Benchmark]` VCBench: A Multi-Dimensional Benchmark for Single-Cell Foundation Models (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.18.733146)] [[code](https://github.com/AppliedScientific/VCBench)] ![GitHub stars](https://img.shields.io/github/stars/AppliedScientific/VCBench.svg?logo=github&label=Stars)

- **[Design Space]** `[Perturbation]` Elucidating the Design Space of Generative Models for Single-Cell Perturbation Prediction (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.15.732063)]

- **[PertDiffBench]** `[Benchmark]` PertDiffBench: Benchmarking Diffusion Models for Single-Cell Perturbation Response Prediction (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.13.732013)]

- **[Zero-Shot Benchmark]** `[Benchmark]` Systematic benchmarking of zero-shot utility and robustness in single-cell transcriptomic foundation models (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.18.733285)]

- **[DeepSpot-M]** `[Virtual Cell]` DeepSpot-M: a multimodal foundation model for transcriptome-wide virtual spatial transcriptomics from histology (**medRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.19.26356060)] [[code](https://github.com/ratschlab/DeepSpotM)] ![GitHub stars](https://img.shields.io/github/stars/ratschlab/DeepSpotM.svg?logo=github&label=Stars)

- **[V3Cell]** `[Virtual Cell]` V3Cell: A Vision-Guided Virtual 3D Cell Framework for Phenotypic Modeling and Perturbation Prediction (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.23.734130)] [[code](https://github.com/Laineyoulu/V3Cell)] ![GitHub stars](https://img.shields.io/github/stars/Laineyoulu/V3Cell.svg?logo=github&label=Stars)

- **[Cross-Context DrugPert]** `[Perturbation]` Enhancing Cross-Context Generalization in Drug Perturbation Prediction with a Multimodal Conditional Diffusion Framework (**Bioinformatics 2026**) [[paper](https://doi.org/10.1093/bioinformatics/btag482)]

- **[SciCore-Omics]** `[Foundation Model]` SciCore-Omics: a tri-modal foundation model unifying histology, spatial transcriptomics and language for spatial biology (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.30.728937)]

- **[HoloCell]** `[Virtual Cell]` HoloCell: A Generative Foundation Model for Holistic Cellular Modeling (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.06.07.730684)]

- **[FM Roadmap]** `[Foundation Model]` A User’s Roadmap to Foundation Models on Single-Cell and Spatial-Omics – Cell Type and Lineage applications (**National Science Review 2026**) [[paper](https://doi.org/10.1093/nsr/nwag371)]

- **[PerturbCellRL]** `[Perturbation]` PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2606.27752)]

- **[KG-Reasoning LLM]** `[Perturbation]` Knowledge Graphs and Reasoning LLMs for Finding Simple Yet Effective Transcriptomic Perturbation Predictors (**arXiv 2026**) [[paper](https://arxiv.org/abs/2606.08816)]

- **[Cross-Modal Transfer]** `[Foundation Model]` Single-Cell Cross-Modal Transfer by Adversarial Fine-Tuning of Foundation Models (**arXiv 2026**) [[paper](https://arxiv.org/abs/2606.07676)]

- **[BRIDGE]** `[Virtual Cell]` BRIDGE: A Multi-organ Histo-ST Foundation Model Enables Virtual Spatial Transcriptomics for Enhanced Few-shot Cancer Diagnosis (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.05.722971)]

- **[Morphodynamics-Expr]** `[Morphology]` Single-cell morphodynamical trajectories enable prediction of gene expression accompanying cell state change (**Cell Systems 2026**) [[paper](https://doi.org/10.1016/j.cels.2026.101567)]

- **[Morph-Transcriptomic GenModel]** `[Morphology]` A generative framework for predicting cellular morphological and transcriptomic perturbation responses (**Cell Reports Methods 2026**) [[paper](https://doi.org/10.1016/j.crmeth.2026.101459)]

- **[DoFormer]** `[Perturbation]` DoFormer: Causal Transformer for Gene Perturbation (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.02.722054)]

- **[RegFormer]** `[Foundation Model]` RegFormer: a single-cell foundation model powered by gene regulatory hierarchies (**Nature Communications 2026**) [[paper](https://doi.org/10.1038/s41467-026-72198-x)]

- **[Spurious Correlation]** `[Benchmark]` Spurious correlation inflates performance in single-cell perturbation prediction (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.07.723486)]

- **[scArchon]** `[Benchmark]` scArchon: a scalable benchmarking framework for assessing single-cell perturbation models (**Genome Biology 2026**) [[paper](https://doi.org/10.1186/s13059-026-04104-z)] [[code](https://github.com/hdsu-bioquant/scArchon)] ![GitHub stars](https://img.shields.io/github/stars/hdsu-bioquant/scArchon.svg?logo=github&label=Stars)

- **[Chemical Pert DL]** `[Perturbation]` Deep learning models for chemical perturbation prediction do not yet utilise drug molecular features (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.13.724458)]

- **[Cycle-Consistent GenModel]** `[Spatial]` Cycle-consistent deep generative modeling unifies cellular states across unpaired spatial and single-cell modalities (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.05.25.727736)]

- **[StateXDiff]** `[Perturbation]` StateXDiff: Cell State-Contextualized Multimodal Diffusion for Single-Cell Perturbation Prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2605.16104)]

- **[DeSCOPE]** `[Virtual Cell]` Decoding Single-Cell Omics of Perturbation Responses Using DeSCOPE (**bioRxiv 2026**) [[paper](https://www.biorxiv.org/content/10.64898/2026.04.13.718147v1)] [[code](https://github.com/Peg-Wu/DeSCOPE)] ![GitHub stars](https://img.shields.io/github/stars/Peg-Wu/DeSCOPE.svg?logo=github&label=Stars)

- **[Dataset Size & Diversity]** `[Foundation Model]` Evaluating the role of pretraining dataset size and diversity on single-cell foundation model performance (**Nature Methods 2026**) [[paper](https://www.nature.com/articles/s41592-026-03120-y)] [[code](https://github.com/microsoft/scFM-dataselection)] ![GitHub stars](https://img.shields.io/github/stars/microsoft/scFM-dataselection.svg?logo=github&label=Stars)

- **[Lingshu-Cell]** `[Virtual Cell]` Lingshu-Cell: A generative cellular world model for transcriptome modeling toward virtual cells (**arXiv 2026**) [[paper](https://arxiv.org/abs/2603.25240)] [[homepage](https://github.com/alibaba-damo-academy/lingshu-cell-homepage)]

- **[SCALE]** `[Perturbation]` SCALE: Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2603.17380)]

- **[Conditional Monge Gap]** `[Perturbation]` Conditional Monge Gap enables generalizable single-cell perturbation modelling (**Nature Machine Intelligence 2026**) [[paper](https://www.nature.com/articles/s42256-026-01242-8)] [[code](https://github.com/AI4SCR/conditional-monge-gap)] ![GitHub stars](https://img.shields.io/github/stars/AI4SCR/conditional-monge-gap.svg?logo=github&label=Stars)

- **[ProtiCelli]** `[Virtual Cell]` Generative machine learning unlocks the first proteome-wide image of human cells (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.03.31.715748)] [[code](https://github.com/CellProfiling/ProtiCelli)] ![GitHub stars](https://img.shields.io/github/stars/CellProfiling/ProtiCelli.svg?logo=github&label=Stars)

- **[AetherCell]** `[Virtual Cell]` AetherCell: A generative engine for virtual cell perturbation and in vivo drug discovery (**bioRxiv 2026**) [[paper](https://www.biorxiv.org/content/10.64898/2026.03.13.710968v1)] [[code](https://github.com/Wenyuan-AI4science/AetherCell)] ![GitHub stars](https://img.shields.io/github/stars/Wenyuan-AI4science/AetherCell.svg?logo=github&label=Stars)

- **[AlphaCell]** `[Virtual Cell]` Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.03.02.709176)]

- **[VCWorld]** `[Virtual Cell]` VCWorld: A Biological World Model for Virtual Cell Simulation (**ICLR 2026 Poster**) [[paper](https://openreview.net/forum?id=hhq89Hs7T3)] [[code](https://github.com/GENTEL-lab/VCWorld)] ![GitHub stars](https://img.shields.io/github/stars/GENTEL-lab/VCWorld.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/GENTEL-lab/VCWorld)]

- **[Spatial Perturb-seq]** `[Spatial]` Spatial perturb-seq: single-cell functional genomics within intact tissue architecture (**Nature Communications 2026**) [[paper](https://www.nature.com/articles/s41467-026-69677-6)][[code](https://github.com/kimberle9/spatialperturbseq)] ![GitHub stars](https://img.shields.io/github/stars/kimberle9/spatialperturbseq.svg?logo=github&label=Stars)

- **[Celcomen]** `[Spatial]` Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling (**Nature Communications 2026**) [[paper](https://www.nature.com/articles/s41467-026-69856-5)] [[code](https://github.com/Teichlab/celcomen)] ![GitHub stars](https://img.shields.io/github/stars/Teichlab/celcomen.svg?logo=github&label=Stars)

- **[stVCR]** `[Spatial]` stVCR: spatiotemporal dynamics of single cells (**Nature Methods 2026**) [[paper](https://www.nature.com/articles/s41592-026-03010-3)] [[code](https://github.com/QiangweiPeng/stVCR)] ![GitHub stars](https://img.shields.io/github/stars/QiangweiPeng/stVCR.svg?logo=github&label=Stars)

- **[CONCORD]** `[Foundation Model]` Revealing a coherent cell-state landscape across single-cell datasets with CONCORD (**Nature Biotechnology 2026**) [[paper](https://www.nature.com/articles/s41587-025-02950-z)][[code](https://github.com/Gartner-Lab/Concord)] ![GitHub stars](https://img.shields.io/github/stars/Gartner-Lab/Concord.svg?logo=github&label=Stars)

- **[AI Scientist]** `[Related]` Towards end-to-end automation of AI research (**Nature 2026**) [[paper](https://www.nature.com/articles/s41586-026-10265-5)] [[code](https://github.com/SakanaAI/AI-Scientist)] ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist.svg?logo=github&label=Stars)

- **[Conformation Description Language]** `[Related]` Bridging three-dimensional molecular structures and artificial intelligence with a conformation description language (**Nature Machine Intelligence 2026**) [[paper](https://doi.org/10.1038/s42256-026-01068-4)]

- **[CRISPRi Map]** `[Perturbation]` A genome-scale single-cell CRISPRi map of trans gene regulation across human pluripotent stem cell lines (**Cell Genomics 2026**) [[paper](https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00332-5?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2666979X25003325%3Fshowall%3Dtrue)]

- **[TxPert]** `[Perturbation]` TxPert: using multiple knowledge graphs for prediction of transcriptomic perturbation effects (**Nature Biotechnology 2026**) [[paper](https://www.nature.com/articles/s41587-026-03113-4)] [[code](https://github.com/valence-labs/TxPert)] ![GitHub stars](https://img.shields.io/github/stars/valence-labs/TxPert.svg?logo=github&label=Stars)

- **[Therapeutic Design]** `[Related]` Deep-learning-based de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes (**Cell 2026**) [[paper](https://doi.org/10.1016/j.cell.2026.02.016)]

- **[X-Pert]** `[Perturbation]` Unified Multimodal Learning Enables Generalized Cellular Response Prediction to Diverse Perturbations (**bioRxiv**) [[paper](https://www.biorxiv.org/content/10.1101/2025.11.13.688367v2)] [[code](https://github.com/Chen-Li-17/X-Pert)] ![GitHub stars](https://img.shields.io/github/stars/Chen-Li-17/X-Pert.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/Chen-Li-17/X-Pert)]

- **[MVCBench]** `[Benchmark]` MVCBench: A Multimodal Benchmark for Drug-induced Virtual Cell Phenotypes (**bioRxiv**) [[paper](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1)] [[code](https://github.com/QSong-github/MVCBench)] ![GitHub stars](https://img.shields.io/github/stars/QSong-github/MVCBench.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/QSong-github/MVCBench)]

- **[HarmonyCell]** `[Perturbation]` HarmonyCell: Automating Single-Cell Perturbation Modeling under Semantic and Distribution Shifts (**bioRxiv**) [[paper](https://arxiv.org/pdf/2603.01396)]

- **[scDFM]** `[Perturbation]` scDFM: Distributional Flow Matching Model for Robust Single-Cell Perturbation Prediction (**ICLR 2026 Poster**) [[paper](https://openreview.net/forum?id=QSGanMEcUV)] [[code](https://github.com/AI4Science-WestlakeU/scDFM)] ![GitHub stars](https://img.shields.io/github/stars/AI4Science-WestlakeU/scDFM.svg?logo=github&label=Stars)

- **[Doloris]** `[Perturbation]` Doloris: Dual Conditional Diffusion Implicit Bridges with Sparsity Masking Strategy for Unpaired Single-Cell Perturbation Estimation (**ICLR 2026 Poster**) [[paper](https://openreview.net/forum?id=rvpDHfoTd2)] [[code](https://github.com/ChangxiChi/Doloris)] ![GitHub stars](https://img.shields.io/github/stars/ChangxiChi/Doloris.svg?logo=github&label=Stars)

- **[Departures]** `[Perturbation]` Departures: Distributional Transport for Single-Cell Perturbation Prediction with Neural Schrödinger Bridges (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39190)] [[preprint](https://arxiv.org/abs/2511.13124)]

- **[PETRI]** `[Foundation Model]` PETRI: Learning Unified Cell Embeddings from Unpaired Modalities via Early-Fusion Joint Reconstruction (**ICLR 2026 Poster**) [[paper](https://openreview.net/forum?id=Vu8YXDooG5)]

- **[STRAND]** `[Perturbation]` STRAND: Sequence-Conditioned Transport for Single-Cell Perturbations (**arXiv 2026**) [[paper](https://arxiv.org/abs/2602.10156)]

- **[PerturbDiff]** `[Perturbation]` PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling (**arXiv 2026**) [[paper](https://arxiv.org/abs/2602.19685)] [[code](https://github.com/DeepGraphLearning/PerturbDiff)] ![GitHub stars](https://img.shields.io/github/stars/DeepGraphLearning/PerturbDiff.svg?logo=github&label=Stars) [[project](https://katarinayuan.github.io/PerturbDiff-ProjectPage/)]

- **[scBIG]** `[Perturbation]` Beyond Independent Genes: Learning Module-Inductive Representations for Gene Perturbation Prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2602.04901)] [[code](https://github.com/ttruan2426-dot/scBIG)] ![GitHub stars](https://img.shields.io/github/stars/ttruan2426-dot/scBIG.svg?logo=github&label=Stars) [[code](https://github.com/ttruan2426-dot/scBIG)] ![GitHub stars](https://img.shields.io/github/stars/ttruan2426-dot/scBIG.svg?logo=github&label=Stars)

- **[CellxPert]** `[Perturbation]` CellxPert: Inference-Time MCMC Steering of a Multi-Omics Single-Cell Foundation Model for In-Silico Perturbation (**arXiv 2026**) [[paper](https://arxiv.org/abs/2605.00930)]

- **[Perturbation Representation]** `[Perturbation]` What Makes a Representation Good for Single-Cell Perturbation Prediction? (**arXiv 2026**) [[paper](https://arxiv.org/abs/2605.19343)]

- **[CisTransCell]** `[Perturbation]` CisTransCell: Single-Cell Perturbation Prediction via Gene Function, Regulatory Control, and Cellular Context (**arXiv 2026**) [[paper](https://arxiv.org/abs/2606.13713)]

- **[Latent Causal Processes]** `[Perturbation]` Learning Latent Dynamical Causal Processes for Single-Cell Perturbation Prediction (**arXiv 2026**) [[paper](https://arxiv.org/abs/2605.25581)]

- **[msInfer]** `[Tool]` Large-scale proteome inference from unpaired single-cell transcriptomic and proteomic data by msInfer (**Research Square 2026**) [[paper](https://doi.org/10.21203/rs.3.rs-9068677/v1)]

- **[Stack]** `[Foundation Model]` Stack: In-Context Learning of Single-Cell Biology (**bioRxiv**) [[paper](https://www.biorxiv.org/content/10.64898/2026.01.09.698608v1)] [[code](https://github.com/ArcInstitute/stack)] ![GitHub stars](https://img.shields.io/github/stars/ArcInstitute/stack.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/ArcInstitute/stack)]

- **[BioWorldModel]** `[Related]` BioWorldModel: a single architecture predicts phenotype from genotype across four kingdoms of life (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.03.27.714912)]

- **[Gene Importance]** `[Foundation Model]` Scoring gene importance by interpreting single-cell foundation models (**Nature Biotechnology 2026**) [[paper](https://doi.org/10.1038/s41587-026-03112-5)]

- **[Hi-C FM]** `[Foundation Model]` A generalizable Hi-C foundation model for chromatin architecture, single-cell and multiomics analysis across species (**Nature Methods 2026**) [[paper](https://doi.org/10.1038/s41592-026-03097-8)]

- **[Virtual Spatial Tumor]** `[Virtual Cell]` Cellular architecture and neighborhood-informed virtual spatial tumor profiling from histopathology (**Cell 2026**) [[paper](https://doi.org/10.1016/j.cell.2026.05.031)]

- **[SynCell]** `[Virtual Cell]` A framework for building a synthetic cell from the SynCell Asia Initiative (**Nature Biotechnology 2026**) [[paper](https://doi.org/10.1038/s41587-026-03153-w)]

- **[3D Genome FM]** `[Foundation Model]` A foundation model to help understand the regulatory implications of 3D genome organization (**Nature Methods 2026**) [[paper](https://doi.org/10.1038/s41592-026-03098-7)]

- **[Tissueformer]** `[Foundation Model]` Tissueformer: extending single-cell foundation models to predict population-level phenotypes (**BMC Bioinformatics 2026**) [[paper](https://doi.org/10.1186/s12859-026-06490-4)]

- **[CytoSignal]** `[Spatial]` CytoSignal detects locations and dynamics of ligand–receptor signaling at cellular resolution from spatial transcriptomic data (**Nature Genetics 2026**) [[paper](https://doi.org/10.1038/s41588-026-02624-9)]

- **[graphene-seq]** `[Spatial]` In situ graphene-seq: spatial transcriptomics and chronic electrophysiological characterization of tissue microenvironments (**Nature Communications 2026**) [[paper](https://doi.org/10.1038/s41467-026-73883-7)]

- **[Deep Molecular Profiling]** `[Spatial]` Deep molecular profiling in three dimensions (**Nature Methods 2026**) [[paper](https://doi.org/10.1038/s41592-026-03149-z)]

- **[SpaMosaic]** `[Spatial]` Mosaic integration of spatial multi-omics with SpaMosaic (**Nature Genetics 2026**) [[paper](https://doi.org/10.1038/s41588-026-02573-3)]

- **[Computational Landscape]** `[Perturbation]` Charting the computational landscape of single-cell genetic perturbation (**Journal of Advanced Research 2026**) [[paper](https://doi.org/10.1016/j.jare.2026.06.012)]

- **[veloAgent]** `[Agent]` Dissecting and steering cell dynamics using spatially-informed RNA velocity with veloAgent (**Molecular Systems Biology 2026**) [[paper](https://doi.org/10.1038/s44320-026-00213-w)] [[code](https://github.com/mcgilldinglab/veloAgent)] ![GitHub stars](https://img.shields.io/github/stars/mcgilldinglab/veloAgent.svg?logo=github&label=Stars)

- **[Morphodynamics]** `[Morphology]` Single-cell morphodynamics predict cell fate decisions during mucociliary epithelial differentiation (**Molecular Systems Biology 2026**) [[paper](https://doi.org/10.1038/s44320-026-00212-x)]

- **[Single Cell Notebooks]** `[Tool]` The Single Cell Notebooks for inclusive and accessible training in single-cell and spatial omics (**Nature Genetics 2026**) [[paper](https://doi.org/10.1038/s41588-026-02584-0)]

### 2025

- **[Pertpy]** `[Tool]` Pertpy: an End-to-end Framework for Perturbation Analysis (**Nature Methods**) [[paper](https://www.nature.com/articles/s41592-025-02909-7)] [[code](https://github.com/scverse/pertpy)] ![GitHub stars](https://img.shields.io/github/stars/scverse/pertpy.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/scverse/pertpy)]

- **[Benchmarking]** `[Benchmark]` Benchmarking Algorithms for Generalizable Single-Cell Perturbation Response Prediction (**Nature Methods**) [[paper](https://www.nature.com/articles/s41592-025-02980-0)] [[code](https://github.com/bm2-lab/scPerturBench/)] ![GitHub stars](https://img.shields.io/github/stars/bm2-lab/scPerturBench.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/bm2-lab/scPerturBench)]

- **[DeepSpot2Cell]** `[Virtual Cell]` DeepSpot2Cell: Predicting Virtual Single-Cell Spatial Transcriptomics from H&E images using Spot-Level Supervision (**NeurIPS 2025**) [[paper](https://openreview.net/forum?id=ofCkwXQKaz)] [[code](https://github.com/ratschlab/DeepSpot2Cell)] ![GitHub stars](https://img.shields.io/github/stars/ratschlab/DeepSpot2Cell.svg?logo=github&label=Stars)

- **[Scouter]** `[Perturbation]` Scouter predicts transcriptional responses to genetic perturbations with large language model embeddings (**Nature Computational Science 2025**) [[paper](https://www.nature.com/articles/s43588-025-00912-8)]

- **[GPerturb]** `[Perturbation]` GPerturb: Gaussian process modelling of single-cell perturbation data (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-61165-7)] [[code](https://github.com/hwxing3259/GPerturb)] ![GitHub stars](https://img.shields.io/github/stars/hwxing3259/GPerturb.svg?logo=github&label=Stars)

- **[Squidiff]** `[Perturbation]` Squidiff: Predicting Cellular Development and Responses to Perturbations using a Diffusion Model (**Nature Methods**) [[paper](https://www.nature.com/articles/s41592-025-02877-y)] [[code](https://github.com/siyuh/Squidiff)] ![GitHub stars](https://img.shields.io/github/stars/siyuh/Squidiff.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/siyuh/Squidiff)]

- **[Nicheformer]** `[Spatial]` Nicheformer: A Foundation Model for Single-Cell and Spatial Omics (**Nature Methods**) [[paper](https://doi.org/10.1038/s41592-025-02814-z)] [[中文解读](https://mp.weixin.qq.com/s/dCOncaXH2O1ArVxYiI4tjA)] [[code](https://github.com/theislab/nicheformer)] ![GitHub stars](https://img.shields.io/github/stars/theislab/nicheformer.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/theislab/nicheformer)]

- **[NicheCompass]** `[Spatial]` Quantitative characterization of cell niches in spatially resolved omics data (**Nature Genetics 2025**) [[paper](https://www.nature.com/articles/s41588-025-02120-6)] [[code](https://github.com/Lotfollahi-lab/nichecompass)] ![GitHub stars](https://img.shields.io/github/stars/Lotfollahi-lab/nichecompass.svg?logo=github&label=Stars)

- **[STAMP]** `[Tool]` STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging (**Cell 2025**) [[paper](https://doi.org/10.1016/j.cell.2025.05.027)]

- **[Perturb-FISH]** `[Spatial]` Simultaneous CRISPR screening and spatial transcriptomics reveal intracellular, intercellular, and functional transcriptional circuits (**Cell 2025**) [[paper](https://doi.org/10.1016/j.cell.2025.02.012)]

- **[ADLF]** `[Perturbation]` Active Learning Framework Leveraging Transcriptomics Identifies Modulators of Disease Phenotypes (**Science**) [[paper](https://doi.org/10.1126/science.adi8577)] [[code](https://doi.org/10.5281/zenodo.16921928)]

- **[Tahoe-x1]** `[Foundation Model]` Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.10.23.683759)] [[code](https://github.com/tahoebio/tahoe-x1)] ![GitHub stars](https://img.shields.io/github/stars/tahoebio/tahoe-x1.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/tahoebio/tahoe-x1)] [[hugging face files](https://huggingface.co/tahoebio/Tahoe-x1/tree/main)]

- **[LPM]** `[Perturbation]` In Silico Biological Discovery with Large Perturbation Models (**Nature Computational Science 2025**) [[paper](https://doi.org/10.1038/s43588-025-00870-1)] [[中文解读](https://mp.weixin.qq.com/s/i_UllqEDVwPQnw-X7dR2BQ)] [[code](https://github.com/perturblib/perturblib)] ![GitHub stars](https://img.shields.io/github/stars/perturblib/perturblib.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/perturblib/perturblib)]

- **[CellNavi]** `[Perturbation]` CellNavi Predicts Genes Directing Cellular Transitions by Learning a Gene Graph-Enhanced Cell State Manifold (**Nature Cell Biology 2025**) [[paper](https://doi.org/10.1038/s41556-025-01755-1)] [[中文解读](https://mp.weixin.qq.com/s/RqLpybJxpHz-8epY7IXA3w)] [[code](https://github.com/DLS5-Omics/CellNavi)] ![GitHub stars](https://img.shields.io/github/stars/DLS5-Omics/CellNavi.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/DLS5-Omics/CellNavi)]

- **[EpiAgent]** `[Foundation Model]` EpiAgent: Foundation Model for Single-Cell Epigenomics (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02822-z)] [[中文解读](https://mp.weixin.qq.com/s/Zuguvzdvx6YOIPT8O889NQ)] [[code](https://github.com/xy-chen16/EpiAgent)] ![GitHub stars](https://img.shields.io/github/stars/xy-chen16/EpiAgent.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/xy-chen16/EpiAgent)]

- **[CellWhisperer]** `[Tool]` Multimodal learning enables chat-based exploration of single-cell data (**Nature Biotechnology 2025**) [[paper](https://www.nature.com/articles/s41587-025-02857-9)] [[code](https://github.com/epigen/CellWhisperer)] ![GitHub stars](https://img.shields.io/github/stars/epigen/CellWhisperer.svg?logo=github&label=Stars)

- **[CRISPR-GPT]** `[Agent]` CRISPR-GPT for Agentic Automation of Gene-Editing Experiments (**Nature Biomedical Engineering 2025**) [[paper](https://doi.org/10.1038/s41551-025-01463-z)] [[中文解读](https://mp.weixin.qq.com/s/KuKndV469cvTczi9CePcqQ)] [[code](https://github.com/cong-lab/crispr-gpt-pub)] ![GitHub stars](https://img.shields.io/github/stars/cong-lab/crispr-gpt-pub.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/cong-lab/crispr-gpt-pub)]

- **[Cell-o1]** `[Agent]` Cell-o1: Training LLMs to Solve Single-Cell Reasoning Puzzles with Reinforcement Learning (**arXiv 2025**) [[paper](https://arxiv.org/abs/2506.02911)] [[code](https://github.com/ncbi-nlp/cell-o1)] ![GitHub stars](https://img.shields.io/github/stars/ncbi-nlp/cell-o1.svg?logo=github&label=Stars) [[hugging face](https://huggingface.co/ncbi/Cell-o1/)] [[ask deepwiki](https://deepwiki.com/ncbi-nlp/cell-o1)]

- **[Systema]** `[Benchmark]` Systema: A Framework for Evaluating Genetic Perturbation Response Prediction Beyond Systematic Variation (**Nature Biotechnology 2025**) [[paper](https://doi.org/10.1038/s41587-025-02777-8)] [[中文解读](https://mp.weixin.qq.com/s/QIhPbz034nwCPRBvd0P_tQ)] [[code](https://github.com/mlbio-epfl/systema)] ![GitHub stars](https://img.shields.io/github/stars/mlbio-epfl/systema.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/mlbio-epfl/systema)]

- **[RegVelo]** `[Perturbation]` RegVelo: Gene-Regulatory-Informed Dynamics of Single Cells (**bioRxiv**) [[paper](https://doi.org/10.1101/2024.12.11.627935)] [[code](https://github.com/theislab/regvelo)] ![GitHub stars](https://img.shields.io/github/stars/theislab/regvelo.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/theislab/regvelo)]

- **[IMPA]** `[Morphology]` Predicting cell morphological responses to perturbations using generative modeling (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-024-55707-8)] [[code](https://github.com/theislab/IMPA)] ![GitHub stars](https://img.shields.io/github/stars/theislab/IMPA.svg?logo=github&label=Stars)

- **[PhenoProfiler]** `[Morphology]` PhenoProfiler: Advancing Morphology Representations for Image-based Drug Discovery (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-60033-1)] [[code](https://github.com/QSong-github/PhenoProfiler)] ![GitHub stars](https://img.shields.io/github/stars/QSong-github/PhenoProfiler.svg?logo=github&label=Stars) [[webserver](https://phenoprofiler.org/)] [[ask deepwiki](https://deepwiki.com/QSong-github/PhenoProfiler)]

- **[PERISCOPE]** `[Morphology]` A genome-wide atlas of human cell morphology (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-024-02537-7)] [[dataset](https://registry.opendata.aws/cellpainting-gallery/)] [[code](https://github.com/broadinstitute/2022_PERISCOPE)] ![GitHub stars](https://img.shields.io/github/stars/broadinstitute/2022_PERISCOPE.svg?logo=github&label=Stars)

- **[Morph Map]** `[Morphology]` Morphological map of under- and overexpression of genes in human cells (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-025-02753-9)] [[dataset](https://github.com/jump-cellpainting/2025_Chandrasekaran_NatureMethods_Morphmap/blob/main/README.md)] [[code](https://github.com/jump-cellpainting/2025_Chandrasekaran_NatureMethods_Morphmap)] ![GitHub stars](https://img.shields.io/github/stars/jump-cellpainting/2025_Chandrasekaran_NatureMethods_Morphmap.svg?logo=github&label=Stars)

- **[MorphDiff]** `[Morphology]` Prediction of Cellular Morphology Changes under Perturbations with a Transcriptome-Guided Diffusion Model (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-63478-z)] [[中文解读](https://mp.weixin.qq.com/s/f_4Q0DEuy3K4sy_jsYhabQ)] [[code](https://github.com/biomap-research/MorphDiff)] ![GitHub stars](https://img.shields.io/github/stars/biomap-research/MorphDiff.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/biomap-research/MorphDiff)]

- **[rBio-1]** `[Agent]` rBio1-Training Scientific Reasoning LLMs with Biological World Models as Soft Verifiers (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.08.18.670981)] [[中文解读](https://mp.weixin.qq.com/s/QPS1L1MRQr9-F8u8fZsNWw)] [[code](https://github.com/czi-ai/rbio)] ![GitHub stars](https://img.shields.io/github/stars/czi-ai/rbio.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/czi-ai/rbio)]

- **[TranscriptFormer]** `[Foundation Model]` A Cross-Species Generative Cell Atlas across 1.5 Billion Years of Evolution: The Transcriptformer Single-Cell Model (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.04.25.650731)] [[code](https://github.com/czi-ai/transcriptformer)] ![GitHub stars](https://img.shields.io/github/stars/czi-ai/transcriptformer.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/czi-ai/transcriptformer)]

- **[CellAtria]** `[Agent]` An Agentic AI Framework for Ingestion and Standardization of Single-Cell RNA-Seq Data Analysis (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.07.31.667880)] [[中文解读](https://mp.weixin.qq.com/s/F7SeT3NJEbjpbRBOIZihKw)] [[code](https://github.com/AstraZeneca/cellatria)] ![GitHub stars](https://img.shields.io/github/stars/AstraZeneca/cellatria.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/AstraZeneca/cellatria)]

- **[Scvi-hub]** `[Tool]` Scvi-hub: An Actionable Repository for Model-Driven Single-Cell Analysis (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02799-9)] [[中文解读](https://mp.weixin.qq.com/s/VzGqZAUmpC4z4rq_laK8KQ)] [[code](https://github.com/YosefLab/scvi-hub-reproducibility)] ![GitHub stars](https://img.shields.io/github/stars/YosefLab/scvi-hub-reproducibility.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/YosefLab/scvi-hub-reproducibility)]

- **[GraphVelo]** `[Spatial]` GraphVelo Allows for Accurate Inference of Multimodal Velocities and Molecular Mechanisms for Single Cells (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-62784-w)] [[中文解读](https://mp.weixin.qq.com/s/zhZOzhhPiYYBYwfAipM_-Q)] [[code](https://github.com/xing-lab-pitt/GraphVelo)] ![GitHub stars](https://img.shields.io/github/stars/xing-lab-pitt/GraphVelo.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/xing-lab-pitt/GraphVelo)]

- **[Stereo-Cell]** `[Spatial]` Stereo-Cell: Spatial Enhanced-Resolution Single-Cell Sequencing with High-Density DNA Nanoball-Patterned Arrays (**Science 2025**) [[paper](https://doi.org/10.1126/science.adr0475)] [[中文解读](https://mp.weixin.qq.com/s/vlzSO2QTsAm3QIIdpp4wXQ)] [[code](https://github.com/haoshijie13/Stereo-cell-paper-code)] ![GitHub stars](https://img.shields.io/github/stars/haoshijie13/Stereo-cell-paper-code.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/haoshijie13/Stereo-cell-paper-code)]

- **[SToFM]** `[Spatial]` SToFM: A Multi-scale Foundation Model for Spatial Transcriptomics (**ICML 2025 Poster**) [[paper](https://openreview.net/forum?id=PQx66EJUu0)] [[中文解读](https://mp.weixin.qq.com/s/BevOy589OoJ6qnKt_wG3sg)] [[code](https://github.com/PharMolix/SToFM)] ![GitHub stars](https://img.shields.io/github/stars/PharMolix/SToFM.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/PharMolix/SToFM)]

- **[NicheFlow]** `[Spatial]` Modeling Microenvironment Trajectories on Spatial Transcriptomics with NicheFlow (**NeurIPS 2025**) [[paper](https://openreview.net/forum?id=5ofJyjgrth)] [[code](https://github.com/kristiyansakalyan/nicheflow)] ![GitHub stars](https://img.shields.io/github/stars/kristiyansakalyan/nicheflow.svg?logo=github&label=Stars)

- **[scGPT-spatial]** `[Spatial]` scGPT-spatial: Continual Pretraining of Single-Cell Foundation Model for Spatial Transcriptomics (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.02.05.636714)] [[code](https://github.com/bowang-lab/scGPT-spatial)] ![GitHub stars](https://img.shields.io/github/stars/bowang-lab/scGPT-spatial.svg?logo=github&label=Stars)

- **[SpatialAgent]** `[Agent]` SpatialAgent: An Autonomous AI Agent for Spatial Biology (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.04.03.646459)] [[中文解读](https://mp.weixin.qq.com/s/uoJ3RGxR2fa5Wy3gUcjeLQ)] [[code](https://github.com/Genentech/SpatialAgent)] ![GitHub stars](https://img.shields.io/github/stars/Genentech/SpatialAgent.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/Genentech/SpatialAgent)]

- **[CellFlux]** `[Morphology]` CellFlux: Simulating Cellular Morphology Changes via Flow Matching (**ICML 2025 Poster**) [[paper](https://openreview.net/forum?id=3NLNmdheIi)] [[code](https://github.com/yuhui-zh15/CellFlux)] ![GitHub stars](https://img.shields.io/github/stars/yuhui-zh15/CellFlux.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/yuhui-zh15/CellFlux)]

- **[CellCLIP]** `[Morphology]` CellCLIP: Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning (**NeurIPS 2025**) [[paper](https://papers.nips.cc/paper_files/paper/2025/hash/b4689a8e6ac04c0919f7162365f1248d-Abstract-Conference.html)] [[code](https://github.com/suinleelab/CellCLIP)] ![GitHub stars](https://img.shields.io/github/stars/suinleelab/CellCLIP.svg?logo=github&label=Stars)

- **[CELTIC]** `[Morphology]` Cell context-dependent in silico organelle localization in label-free microscopy images (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-025-02960-4)] [[code](https://github.com/zaritskylab/CELTIC)] ![GitHub stars](https://img.shields.io/github/stars/zaritskylab/CELTIC.svg?logo=github&label=Stars)

- **[MorphoDiff]** `[Morphology]` MorphoDiff: Cellular Morphology Painting with Diffusion Models (**ICLR 2025**) [[paper](https://openreview.net/forum?id=PstM8YfhvI)] [[preprint](https://doi.org/10.1101/2024.12.19.629451)] [[code](https://github.com/bowang-lab/MorphoDiff)] ![GitHub stars](https://img.shields.io/github/stars/bowang-lab/MorphoDiff.svg?logo=github&label=Stars)

- **[PRESCRIBE]** `[Perturbation]` PRESCRIBE: Predicting Single-Cell Responses with Bayesian Estimation (**NeurIPS 2025 Poster**) [[paper](https://openreview.net/forum?id=A5O41ntKjk)]

- **[GDE]** `[Related]` Generative Distribution Embeddings: Lifting Autoencoders to the Space of Distributions for Multiscale Representation Learning (**NeurIPS 2025 Poster**) [[paper](https://openreview.net/forum?id=ERQRSnqLRb)] [[preprint](https://arxiv.org/abs/2505.18150)]

- **[CellPB]** `[Benchmark]` Benchmarking AI Models for in Silico Gene Perturbation of Cells (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2024.12.20.629581)] [[code](https://github.com/Chen-Li-17/CellPB)] ![GitHub stars](https://img.shields.io/github/stars/Chen-Li-17/CellPB.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/Chen-Li-17/CellPB)]

- **[PerturBench]** `[Benchmark]` Benchmarking Machine Learning Models for Cellular Perturbation Analysis (**NeurIPS 2025 Datasets and Benchmarks Track**) [[paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8aee537279a66ced96319dfca3c00002-Abstract-Datasets_and_Benchmarks_Track.html)] [[code](https://github.com/altoslabs/perturbench)] ![GitHub stars](https://img.shields.io/github/stars/altoslabs/perturbench.svg?logo=github&label=Stars)

- **[CellForge]** `[Agent]` CellForge: Agentic Design of Virtual Cell Models (**arXiv 2025**) [[paper](https://arxiv.org/abs/2508.02276)] [[中文解读](https://mp.weixin.qq.com/s/kX43st2-SYRgxP57_xOoWw)] [[code](https://github.com/gersteinlab/CellForge)] ![GitHub stars](https://img.shields.io/github/stars/gersteinlab/CellForge.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/gersteinlab/CellForge)]

- **[Cradle-VAE]** `[Perturbation]` Cradle-VAE: Enhancing Single-Cell Gene Perturbation Modeling with Counterfactual Reasoning-based Artifact Disentanglement (**AAAI 2025**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/33695)] [[code](https://github.com/dmis-lab/CRADLE-VAE)] ![GitHub stars](https://img.shields.io/github/stars/dmis-lab/CRADLE-VAE.svg?logo=github&label=Stars) [[code](https://github.com/dmis-lab/CRADLE-VAE)] ![GitHub stars](https://img.shields.io/github/stars/dmis-lab/CRADLE-VAE.svg?logo=github&label=Stars)

- **[XTransferCDR]** `[Perturbation]` Learning Cross-Domain Representations for Transferable Drug Perturbations on Single-Cell Transcriptional Responses (**AAAI 2025**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/34073)] [[code](https://github.com/hliulab/XTransferCDR)] ![GitHub stars](https://img.shields.io/github/stars/hliulab/XTransferCDR.svg?logo=github&label=Stars)

- **[Brief Communication]** `[Benchmark]` Deep-Learning-Based Gene Perturbation Effect Prediction Does Not Yet Outperform Simple Linear Baselines (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02772-6)] [[code](https://github.com/const-ae/linear_perturbation_prediction-Paper)] ![GitHub stars](https://img.shields.io/github/stars/const-ae/linear_perturbation_prediction-Paper.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/const-ae/linear_perturbation_prediction-Paper)]

- **[Brief Communication]** `[Benchmark]` Limitations of Cell Embedding Metrics Assessed Using Drifting Islands (**Nature Biotechnology 2025**) [[paper](https://doi.org/10.1038/s41587-025-02702-z)] [[code](https://github.com/Genentech/Islander)] ![GitHub stars](https://img.shields.io/github/stars/Genentech/Islander.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/Genentech/Islander)]

- **[GeneAgent]** `[Agent]` GeneAgent: Self-Verification Language Agent for Gene-Set Analysis Using Domain Databases (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02748-6)] [[code](https://github.com/ncbi-nlp/GeneAgent)] ![GitHub stars](https://img.shields.io/github/stars/ncbi-nlp/GeneAgent.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/ncbi-nlp/GeneAgent)]

- **[Theory]** `[Virtual Cell]` Human Interpretable Grammar Encodes Multicellular Systems Biology Models to Democratize Virtual Cell Laboratories (**Cell 2025**) [[paper](https://doi.org/10.1016/j.cell.2025.06.048)] [[code](https://github.com/physicell-models/grammar_samples)] ![GitHub stars](https://img.shields.io/github/stars/physicell-models/grammar_samples.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/PhysiCell-Models/grammar_samples)]

- **[GREmLN]** `[Foundation Model]` GREmLN: A Cellular Regulatory Network-Aware Transcriptomics Foundation Model (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.07.03.663009)] [[中文解读](https://mp.weixin.qq.com/s/YlgiFnb-6MmhAcE5qZAwKA)] [[code](https://github.com/czi-ai/GREmLN)] ![GitHub stars](https://img.shields.io/github/stars/czi-ai/GREmLN.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/czi-ai/GREmLN)]

- **[CellVoyager]** `[Agent]` CellVoyager: AI CompBio Agent Generates New Insights by Autonomously Analyzing Biological Data (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.06.03.657517)] [[中文解读](https://mp.weixin.qq.com/s/BSWKav3U6MBxdf3ePAxzOg)] [[code](https://github.com/zou-group/CellVoyager)] ![GitHub stars](https://img.shields.io/github/stars/zou-group/CellVoyager.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/zou-group/CellVoyager)]

- **[CausCell]** `[Perturbation]` Causal Disentanglement for Single-Cell Representations and Controllable Counterfactual Generation (**Nature Communications 2025**) [[paper](https://doi.org/10.1038/s41467-025-62008-1)] [[中文解读](https://mp.weixin.qq.com/s/N8nG9g3ur99zbcXhHC2xAQ)] [[code](https://github.com/bm2-lab/CausCell)] ![GitHub stars](https://img.shields.io/github/stars/bm2-lab/CausCell.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/bm2-lab/CausCell)]

- **[CLIP^n]** `[Morphology]` Transitive Prediction of Small-Molecule Function through Alignment of High-Content Screening Resources (**Nature Biotechnology 2025**) [[paper](https://doi.org/10.1038/s41587-025-02729-2)] [[code](https://github.com/AltschulerWu-Lab/CLIPn)] ![GitHub stars](https://img.shields.io/github/stars/AltschulerWu-Lab/CLIPn.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/AltschulerWu-Lab/CLIPn)]

- **[DrugPT]** `[Perturbation]` DrugPT: A Flexible Framework for Integrating Gene and Chemical Representations in Perturbation Modeling (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.07.25.665130)]

- **[OmniPert]** `[Perturbation]` OmniPert: A Deep Learning Foundation Model for Predicting Responses to Genetic and Chemical Perturbations in Single Cancer Cells (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.07.02.662744)]

- **[UNAGI]** `[Perturbation]` A Deep Generative Model for Deciphering Cellular Dynamics and in Silico Drug Discovery in Complex Diseases (**Nature Biomedical Engineering 2025**) [[paper](https://doi.org/10.1038/s41551-025-01423-7)] [[code](https://github.com/mcgilldinglab/UNAGI)] ![GitHub stars](https://img.shields.io/github/stars/mcgilldinglab/UNAGI.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/mcgilldinglab/UNAGI)]

- **[OmiCLIP]** `[Spatial]` A Visual-Omics Foundation Model to Bridge Histopathology with Spatial Transcriptomics (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02707-1)] [[code](https://github.com/GuangyuWangLab2021/Loki)] ![GitHub stars](https://img.shields.io/github/stars/GuangyuWangLab2021/Loki.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/GuangyuWangLab2021/Loki)]

- **[Biomni]** `[Agent]` Biomni: A General-Purpose Biomedical AI Agent (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.05.30.656746)] [[code](https://github.com/snap-stanford/biomni)] ![GitHub stars](https://img.shields.io/github/stars/snap-stanford/biomni.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/snap-stanford/Biomni)]

- **[OCTO-vc]** `[Virtual Cell]` OCTO-vc: Virtual Cells in Real Tissue (**© by Noetik 2025**) [[technical report](https://www.noetik.ai/octo-vc)] [[online demonstration](https://celleporter.noetik.ai/)]

- **[STATE]** `[Perturbation]` Predicting Cellular Responses to Perturbation across Diverse Contexts with STATE (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2025.06.26.661135v2)] [[code](https://github.com/ArcInstitute/state)] ![GitHub stars](https://img.shields.io/github/stars/ArcInstitute/state.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/ArcInstitute/state)]

- **[UniPert-G2CP]** `[Perturbation]` Genetic-To-Chemical Perturbation Transfer Learning through Unified Multimodal Molecular Representations (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.02.02.635055)] [[code](https://github.com/TencentAILabHealthcare/UniPert)] ![GitHub stars](https://img.shields.io/github/stars/TencentAILabHealthcare/UniPert.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/TencentAILabHealthcare/UniPert)]

- **[UniCure]** `[Perturbation]` Unicure: A Foundation Model for Predicting Personalized Cancer Therapy Response (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2025.06.14.658531v1)] [[code](https://github.com/ZexiChen502/UniCure)] ![GitHub stars](https://img.shields.io/github/stars/ZexiChen502/UniCure.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/ZexiChen502/UniCure)]

- **[Cell-GraphCompass]** `[Foundation Model]` Cell-GraphCompass: Modeling Single Cells with Graph Structure Foundation Model (**National Science Review 2025**) [[paper](https://doi.org/10.1093/nsr/nwaf255)] [[code](https://github.com/epang-ucas/Cell-Graph-Compass)] ![GitHub stars](https://img.shields.io/github/stars/epang-ucas/Cell-Graph-Compass.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/epang-ucas/Cell-Graph-Compass)]

- **[scPRINT]** `[Foundation Model]` scPRINT: Pre-training on 50 Million Cells Allows Robust Gene Network Predictions (**Nature Communications 2025**) [[paper](https://doi.org/10.1038/s41467-025-58699-1)] [[code](https://github.com/cantinilab/scPRINT)] ![GitHub stars](https://img.shields.io/github/stars/cantinilab/scPRINT.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/cantinilab/scPRINT)]

- **[CellFM]** `[Foundation Model]` CellFM: A Large-Scale Foundation Model Pre-trained on Transcriptomics of 100 Million Human Cells (**Nature Communications 2025**) [[paper](https://doi.org/10.1038/s41467-025-59926-5)] [[中文解读](https://mp.weixin.qq.com/s/bZLJIiiGh8nhRC8923hOzw)] [[code](https://github.com/biomed-AI/CellFM)] ![GitHub stars](https://img.shields.io/github/stars/biomed-AI/CellFM.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/biomed-AI/CellFM)]

- **[C2S-Scale]** `[Foundation Model]` C2S-Scale: Scaling Large Language Models for Next-Generation Single-Cell Analysis (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.04.14.648850)] [[中文解读](https://mp.weixin.qq.com/s/QTBpfyoNExkPN1fbqb6ggg)] [[code](https://github.com/vandijklab/cell2sentence)] ![GitHub stars](https://img.shields.io/github/stars/vandijklab/cell2sentence.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/vandijklab/cell2sentence)]

- **[scNET]** `[Foundation Model]` scNET: Learning Context-Specific Gene and Cell Embeddings by Integrating Single-Cell Gene Expression Data with Protein-Protein Interactions (**Nature Methods 2025**) [[paper](https://doi.org/10.1038/s41592-025-02627-0)] [[code](https://github.com/madilabcode/scNET)] ![GitHub stars](https://img.shields.io/github/stars/madilabcode/scNET.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/madilabcode/scNET)]

- **[ProCyon]** `[Foundation Model]` ProCyon: A multimodal foundation model for protein phenotypes (**bioRxiv**) [[paper](https://doi.org/10.1101/2024.12.10.627665)] [[project](https://zitniklab.hms.harvard.edu/ProCyon/)] [[code](https://github.com/mims-harvard/ProCyon)] ![GitHub stars](https://img.shields.io/github/stars/mims-harvard/ProCyon.svg?logo=github&label=Stars)

- **[SubCell]** `[Foundation Model]` SubCell: Proteome-aware vision foundation models for microscopy capture single-cell biology (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2024.12.06.627299)] [[code](https://github.com/CellProfiling/subcell-embed)] ![GitHub stars](https://img.shields.io/github/stars/CellProfiling/subcell-embed.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/CellProfiling/subcell-embed)]

- **[Token-Mol 1.0]** `[Related]` Token-Mol 1.0: Tokenized Drug Design with Large Language Models (**Nature Communications 2025**) [[paper](https://doi.org/10.1038/s41467-025-59628-y)] [[code](https://github.com/jkwang93/Token-Mol)] ![GitHub stars](https://img.shields.io/github/stars/jkwang93/Token-Mol.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/jkwang93/Token-Mol)]

- **[Comment]** `[Virtual Cell]` Virtual Cells for Predictive Immunotherapy (**Nature Biotechnology Comment 2025**) [[paper](https://www.nature.com/articles/s41587-025-02583-2)]

- **[Recursion]** `[Virtual Cell]` Virtual Cells: Predict, Explain, Discover (**arXiv 2025**) [[paper](https://arxiv.org/pdf/2505.14613)]

### 2024

- **[Zero-Shot Perturbation]** `[Perturbation]` Efficient Fine-Tuning of Single-Cell Foundation Models Enables Zero-Shot Molecular Perturbation Prediction (**arXiv 2024**) [[paper](https://arxiv.org/abs/2412.13478)]

- **[Cell Maps]** `[Virtual Cell]` Multimodal cell maps as a foundation for structural and functional genomics (**Nature 2025**) [[paper](https://doi.org/10.1038/s41586-025-08878-3)] [[project](https://musicmaps.ai/u2os-cellmap/)]

- **[CellFlow]** `[Morphology]` CellFlow Enables Generative Single-Cell Phenotype Modeling with Flow Matching (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2025.04.11.648220v1.full.pdf)] [[code](https://github.com/theislab/CellFlow)] ![GitHub stars](https://img.shields.io/github/stars/theislab/CellFlow.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/theislab/CellFlow)]

- **[Cell Shapes]** `[Morphology]` Cell shapes decode molecular phenotypes in image-based spatial proteomics (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.05.13.653868)]

- **[Prophet]** `[Perturbation]` Scalable and Universal Prediction of Cellular Phenotypes (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2024.08.12.607533v2.full.pdf)] [[code](https://github.com/theislab/prophet)] ![GitHub stars](https://img.shields.io/github/stars/theislab/prophet.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/theislab/prophet)]

- `[Morphology]` Evaluating Feature Extraction in Ovarian Cancer Cell Line Co-Cultures Using Deep Neural Networks (**Communications Biology 2025**) [[paper](https://www.nature.com/articles/s42003-025-07766-w)]

- **[ProteinTalks]** `[Foundation Model]` A Perturbation Proteomics-Based Foundation Model for Virtual Cell Construction (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.02.07.637070)] [[中文解读](https://mp.weixin.qq.com/s/iAmR6EhV7KYfneRktRaEfw)] [[code](https://github.com/guomics-lab/PTV-1/tree/main/ProteinTalks)] ![GitHub stars](https://img.shields.io/github/stars/guomics-lab/PTV-1.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/guomics-lab/PTV-1)]

- `[Virtual Cell]` Grow AI Virtual Cells: Three Data Pillars and Closed-Loop Learning (**Cell Research 2025**) [[paper](https://www.nature.com/articles/s41422-025-01101-y)] [[中文解读](https://mp.weixin.qq.com/s/kPQmgzAbySrw3rp-B6JGfw)]

- `[Virtual Cell]` Build the Virtual Cell with Artificial Intelligence: A Perspective for Cancer Research (**Military Medical Research 2025**) [[paper](https://link.springer.com/article/10.1186/s40779-025-00591-6)]

- **[PS]** `[Perturbation]` Decoding Heterogeneous Single-Cell Perturbation Responses (**Nature Cell Biology 2025**) [[paper](https://doi.org/10.1038/s41556-025-01626-9)] [[code](https://github.com/davidliwei/PS)] ![GitHub stars](https://img.shields.io/github/stars/davidliwei/PS.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/davidliwei/PS)]

- **[Mixscale]** `[Perturbation]` Systematic Reconstruction of Molecular Pathway Signatures Using Scalable Single-Cell Perturbation Screens (**Nature Cell Biology 2025**) [[paper](https://doi.org/10.1038/s41556-025-01622-z)] [[code](https://github.com/satijalab/Mixscale)] ![GitHub stars](https://img.shields.io/github/stars/satijalab/Mixscale.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/satijalab/Mixscale)]

- **[scDrugMap]** `[Benchmark]` scDrugMap: benchmarking large foundation models for drug response prediction (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-67481-2)]

- **[VCC Commentary]** `[Benchmark]` Virtual Cell Challenge: Toward a Turing Test for the Virtual Cell (**Cell Commentary 2025**) [[paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0)] [[homepage](https://virtualcellchallenge.org/)] [[beginner's guidance](https://fleetwood.dev/posts/virtual-cell-challenge)]

- **[CZI Evaluation]** `[Benchmark]` Benchmarking and Evaluation of AI Models in Biology: Outcomes and Recommendations from the CZI Virtual Cells Workshop (**arXiv 2025**) [[paper](https://arxiv.org/abs/2507.10502)] [[中文解读](https://mp.weixin.qq.com/s/5iGqIUMq1IoHEm0Ssl84-w)]

- **[Virtual Organs]** `[Benchmark]` From Virtual Cell Challenge to Virtual Organs: Navigating the Deep Waters of Medical AI Models (**iCell 2025**) [[paper](https://doi.org/10.71373/IQHA9494)]

- **[GET]** `[Foundation Model]` A Foundation Model of Transcription across Human Cell Types (**Nature 2025**) [[paper](https://doi.org/10.1038/s41586-024-08391-z)] [[code](https://github.com/GET-Foundation/get_model)] ![GitHub stars](https://img.shields.io/github/stars/GET-Foundation/get_model.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/GET-Foundation/get_model)]

### 2024

- **[TranSiGen]** `[Perturbation]` Deep Representation Learning of Chemical-Induced Transcriptional Profile for Phenotype-Based Drug Discovery (**Nature Communications 2024**) [[paper](https://www.nature.com/articles/s41467-024-49620-3)] [[code](https://github.com/myzhengSIMM/TranSiGen)] ![GitHub stars](https://img.shields.io/github/stars/myzhengSIMM/TranSiGen.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/myzhengSIMM/TranSiGen)]

- **[PRnet]** `[Perturbation]` Predicting transcriptional responses to novel chemical perturbations using deep generative model for drug discovery (**Nature Communications 2024**) [[paper](https://www.nature.com/articles/s41467-024-53457-1)]

- **[GenePT]** `[Foundation Model]` Simple and Effective Embedding Model for Single-Cell Biology Built from ChatGPT (**Nature Biomedical Engineering 2024**) [[paper](https://doi.org/10.1038/s41551-024-01284-6)] [[code](https://github.com/yiqunchen/GenePT)] ![GitHub stars](https://img.shields.io/github/stars/yiqunchen/GenePT.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/yiqunchen/GenePT)]

- **[SCimilarity]** `[Foundation Model]` A Cell Atlas Foundation Model for Scalable Search of Similar Human Cells (**Nature 2024**) [[paper](https://doi.org/10.1038/s41586-024-08411-y)] [[code](https://github.com/Genentech/scimilarity)] ![GitHub stars](https://img.shields.io/github/stars/Genentech/scimilarity.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/Genentech/scimilarity)]

- **[scLong]** `[Foundation Model]` scLong: A Billion-Parameter Foundation Model for Capturing Long-Range Gene Context in Single-Cell Transcriptomics (**bioRxiv 2024**) [[paper](https://doi.org/10.1101/2024.11.09.622759)] [[code](https://github.com/BaiDing1234/scLong)] ![GitHub stars](https://img.shields.io/github/stars/BaiDing1234/scLong.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/BaiDing1234/scLong)]

- **[scFoundation]** `[Foundation Model]` Large-Scale Foundation Model on Single-Cell Transcriptomics (**Nature Methods 2024**) [[paper](https://doi.org/10.1038/s41592-024-02305-7)] [[code](https://github.com/biomap-research/scFoundation)] ![GitHub stars](https://img.shields.io/github/stars/biomap-research/scFoundation.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/biomap-research/scFoundation)]

- **[scGPT]** `[Foundation Model]` scGPT: Toward Building a Foundation Model for Single-Cell Multi-Omics Using Generative AI (**Nature Methods 2024**) [[paper](https://doi.org/10.1038/s41592-024-02201-0)] [[code](https://github.com/bowang-lab/scGPT)] ![GitHub stars](https://img.shields.io/github/stars/bowang-lab/scGPT.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/bowang-lab/scGPT)]

- **[TamGen]** `[Related]` TamGen: Drug Design with Target-Aware Molecule Generation through a Chemical Language Model (**Nature Communications 2024**) [[paper](https://doi.org/10.1038/s41467-024-53632-4)] [[code](https://github.com/SigmaGenX/TamGen)] ![GitHub stars](https://img.shields.io/github/stars/SigmaGenX/TamGen.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/SigmaGenX/TamGen)]

- **[GeneCompass]** `[Foundation Model]` GeneCompass: Deciphering Universal Gene Regulatory Mechanisms with a Knowledge-Informed Cross-Species Foundation Model (**Cell Research 2024**) [[paper](https://doi.org/10.1038/s41422-024-01034-y)] [[code](https://github.com/xCompass-AI/GeneCompass)] ![GitHub stars](https://img.shields.io/github/stars/xCompass-AI/GeneCompass.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/xCompass-AI/GeneCompass)]

- **[scTab]** `[Foundation Model]` scTab: Scaling Cross-Tissue Single-Cell Annotation Models (**Nature Communications 2024**) [[paper](https://doi.org/10.1038/s41467-024-51059-5)] [[code](https://github.com/theislab/scTab)] ![GitHub stars](https://img.shields.io/github/stars/theislab/scTab.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/theislab/scTab)]

- **[SATURN]** `[Foundation Model]` Toward Universal Cell Embeddings: Integrating Single-Cell RNA-Seq Datasets across Species with SATURN (**Nature Methods 2024**) [[paper](https://doi.org/10.1038/s41592-024-02191-z)] [[code](https://github.com/snap-stanford/saturn)] ![GitHub stars](https://img.shields.io/github/stars/snap-stanford/saturn.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/snap-stanford/saturn)]

- **[UCE]** `[Foundation Model]` Universal Cell Embeddings: A Foundation Model for Cell Biology (**bioRxiv 2024**) [[paper](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)] [[code](https://github.com/snap-stanford/UCE)] ![GitHub stars](https://img.shields.io/github/stars/snap-stanford/UCE.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/snap-stanford/UCE)]

- **[Cell2Sentence]** `[Foundation Model]` Cell2Sentence: Teaching Large Language Models the Language of Biology (**ICML 2024 Poster**) [[paper](https://icml.cc/virtual/2024/poster/34580)] [[code](https://github.com/vandijklab/cell2sentence)] ![GitHub stars](https://img.shields.io/github/stars/vandijklab/cell2sentence.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/vandijklab/cell2sentence)]

- **[LangCell]** `[Foundation Model]` LangCell: Language-Cell Pre-training for Cell Identity Understanding (**ICML 2024 Poster**) [[paper](https://icml.cc/virtual/2024/poster/34495)] [[code](https://github.com/PharMolix/LangCell)] ![GitHub stars](https://img.shields.io/github/stars/PharMolix/LangCell.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/PharMolix/LangCell)]

- **[CellPLM]** `[Foundation Model]` CellPLM: Pre-training of Cell Language Model beyond Single Cells (**ICLR 2024 Poster**) [[paper](https://openreview.net/forum?id=BKXvPDekud)] [[code](https://github.com/OmicsML/CellPLM)] ![GitHub stars](https://img.shields.io/github/stars/OmicsML/CellPLM.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/OmicsML/CellPLM)]

- **[Stanford PhD Thesis]** `[Virtual Cell]` Engineering Cells Using Artificial Intelligence (**© by Yusuf Roohani 2024**) [[paper](https://stacks.stanford.edu/file/jw766pz3938/PhD_Thesis_Roohani_Yusuf_2024-augmented.pdf)] [[GitHub Homepage](https://github.com/yhr91)] [[Arc profile](https://arcinstitute.org/news/yusuf-roohani-virtual-cell-architecture)]

## Datasets

### Perturbation and Cell-State Atlases

- **[Arc Virtual Cell Atlas]** Large-scale perturbation atlas and codebase from Arc Institute [[resource](https://arcinstitute.org/tools/virtualcellatlas)] [[repo](https://github.com/ArcInstitute/arc-virtual-cell-atlas)]

- **[Tahoe-100M]** Tahoe-100M: A Giga-Scale Single-Cell Perturbation Atlas for Context-Dependent Gene Function and Cellular Modeling (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2025.02.20.639398v1)] [[code](https://github.com/ArcInstitute/arc-virtual-cell-atlas)] ![GitHub stars](https://img.shields.io/github/stars/ArcInstitute/arc-virtual-cell-atlas.svg?logo=github&label=Stars)

- **[X-Atlas/Orion]** Genome-Wide Perturb-Seq Datasets via a Scalable Fix-Cryopreserve Platform for Training Dose-Dependent Biological Foundation Models (**bioRxiv 2025**) [[paper](https://www.biorxiv.org/content/10.1101/2025.06.11.659105v1)] [[dataset](https://doi.org/10.25452/figshare.plus.29190726)]

- **[scPerturb]** scPerturb: Harmonized Single-Cell Perturbation Data (**Nature Methods 2024**) [[paper](https://www.nature.com/articles/s41592-023-02144-y)] [[dataset](https://projects.sanderlab.org/scperturb/)] [[code](https://github.com/sanderlab/scPerturb)] ![GitHub stars](https://img.shields.io/github/stars/sanderlab/scPerturb.svg?logo=github&label=Stars)

- **[CIGS]** High-Throughput Profiling of Chemical-Induced Gene Expression across 93,644 Perturbations (**Nature Methods 2025**) [[paper](https://www.nature.com/articles/s41592-025-02781-5)] [[dataset](https://cigs.iomicscloud.com/)] [[code](https://github.com/Wang-lab302/CIGS)] ![GitHub stars](https://img.shields.io/github/stars/Wang-lab302/CIGS.svg?logo=github&label=Stars)

- **[L1000/CMap]** A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles (**Cell 2017**) [[paper](https://doi.org/10.1016/j.cell.2017.10.049)] [[dataset](https://clue.io/data/CMap2020#LINCS2020)]

- **[Sci-Plex]** Massively Multiplex Chemical Transcriptomics at Single-Cell Resolution (**Science 2019**) [[paper](https://doi.org/10.1126/science.aax6234)] [[dataset](https://figshare.com/articles/dataset/sciPlex_dataset/24681285)] [[code](https://github.com/cole-trapnell-lab/sci-plex)] ![GitHub stars](https://img.shields.io/github/stars/cole-trapnell-lab/sci-plex.svg?logo=github&label=Stars)

- **[Perturb-seq datasets]** Genome-scale and combinatorial Perturb-seq datasets from Replogle, Norman, Dixit, Adamson, and related screens [[overview](https://github.com/sanderlab/scPerturb)]

- **[Virtual Cell Challenge]** Community perturbation-prediction challenge and hidden evaluation resources [[homepage](https://virtualcellchallenge.org/)]

### Single-Cell Reference Atlases

- **[scBaseCount]** scBaseCount: An AI Agent-Curated, Uniformly Processed, and Continually Expanding Single Cell Data Repository (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2025.02.27.640494)] [[code-scRecounter](https://github.com/ArcInstitute/scRecounter)] [[code-SRAgent](https://github.com/ArcInstitute/SRAgent)] ![GitHub stars](https://img.shields.io/github/stars/ArcInstitute/SRAgent.svg?logo=github&label=Stars)

- **[CZ CELLxGENE Discover]** A single-cell data platform for scalable exploration, analysis, and modeling of aggregated data (**NAR 2025**) [[paper](https://academic.oup.com/nar/article/53/D1/D886/7912032)] [[dataset](https://cellxgene.cziscience.com/)]

- **[Human Cell Atlas]** International atlas of human cells and tissues [[portal](https://data.humancellatlas.org/)] [[paper](https://www.nature.com/articles/s41586-024-08338-4)]

- **[Tabula Sapiens]** A multiple-organ single-cell transcriptomic atlas of humans (**Science 2022**) [[paper](https://www.science.org/doi/10.1126/science.abl4896)] [[dataset](https://tabula-sapiens-portal.ds.czbiohub.org/)]

- **[Human BioMolecular Atlas Program]** HuBMAP healthy human tissue atlas and common coordinate framework [[portal](https://hubmapconsortium.org/)] [[paper](https://www.nature.com/articles/s41592-024-02563-5)]

- **[GTEx]** Genotype-Tissue Expression project for human tissue expression baselines [[portal](https://gtexportal.org/)] [[overview](https://www.genome.gov/Funded-Programs-Projects/Genotype-Tissue-Expression-Project)]

### Multimodal, Morphology, and Imaging

- **[scGeneScope]** scGeneScope: A Treatment-Matched Single Cell Imaging and Transcriptomics Dataset and Benchmark for Treatment Response Modeling (**NeurIPS 2025 Datasets and Benchmarks Track**) [[paper](https://openreview.net/forum?id=918POZbZ50)] [[dataset](https://huggingface.co/datasets/altoslabs/scGeneScope)]

- **[CPJUMP1]** Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations (**Nature Methods 2024**) [[paper](https://www.nature.com/articles/s41592-024-02241-6)] [[dataset](https://registry.opendata.aws/cellpainting-gallery/)] [[code](https://github.com/jump-cellpainting/2024_Chandrasekaran_NatureMethods)] ![GitHub stars](https://img.shields.io/github/stars/jump-cellpainting/2024_Chandrasekaran_NatureMethods.svg?logo=github&label=Stars)

- **[Cell Painting Gallery]** Public high-content cell painting datasets from Broad and partners [[dataset](https://registry.opendata.aws/cellpainting-gallery/)] [[overview](https://github.com/broadinstitute/cellpainting-gallery)]

- **[RxRx]** Recursion high-content cellular imaging datasets for perturbation and batch-correction research [[datasets](https://www.rxrx.ai/datasets)]

- **[CM4AI]** Cell Maps for Artificial Intelligence: AI-Ready Maps of Human Cell Architecture from Disease-Relevant Cell Lines (**bioRxiv 2024**) [[paper](https://doi.org/10.1101/2024.05.21.589311)] [[dataset](https://cm4ai.org/)]

- **[STAMP]** Single-cell transcriptomics analysis and multimodal profiling through imaging (**Cell 2025**) [[paper](https://doi.org/10.1016/j.cell.2025.05.027)]

### Spatial and Tissue Context

- **[HEST-1k]** HEST-1k: A Dataset for Spatial Transcriptomics and Histology Image Analysis (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2406.16192)] [[code](https://github.com/mahmoodlab/HEST)] ![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/HEST.svg?logo=github&label=Stars)

- **[TCGA virtual ST atlas]** TCGA virtual spatial transcriptomics atlas: DeepSpot-M predicted transcriptome-wide ST for TCGA H&E (FF + FFPE; ~28.7k slides / 32 cancer types) (**medRxiv 2026**) [[paper](https://www.medrxiv.org/content/10.64898/2026.06.19.26356060v1)] [[dataset](https://huggingface.co/datasets/ratschlab/TCGA_virtual_spatial_transcriptomics_atlas)] [[code](https://github.com/ratschlab/DeepSpotM)] ![GitHub stars](https://img.shields.io/github/stars/ratschlab/DeepSpotM.svg?logo=github&label=Stars)

- **[HEST Xenium virtual ST]** HEST Xenium virtual spatial transcriptomics: DeepSpot-M predicted transcriptome-wide ST for 59 HEST-1k 10x Xenium samples (~13.3M cells) (**medRxiv 2026**) [[paper](https://www.medrxiv.org/content/10.64898/2026.06.19.26356060v1)] [[dataset](https://huggingface.co/datasets/ratschlab/HEST_Xenium_virtual_spatial_transcriptomics)] [[code](https://github.com/ratschlab/DeepSpotM)] ![GitHub stars](https://img.shields.io/github/stars/ratschlab/DeepSpotM.svg?logo=github&label=Stars)

- **[Spatial Perturb-seq]** Spatial perturb-seq data for functional genomics within intact tissue architecture (**Nature Communications 2026**) [[paper](https://www.nature.com/articles/s41467-026-69677-6)] [[code](https://github.com/kimberle9/spatialperturbseq)]

- **[Perturb-FISH]** CRISPR screening with imaging-based spatial transcriptomics (**Cell 2025**) [[paper](https://doi.org/10.1016/j.cell.2025.02.012)]

- **[10x Genomics spatial datasets]** Visium, Xenium, and related public spatial transcriptomics example datasets [[datasets](https://www.10xgenomics.com/datasets)]

- **[Vizgen MERFISH datasets]** Public MERFISH example datasets for spatial transcriptomics [[datasets](https://vizgen.com/data-release-program/)]

### Protein, Organelle, and Molecular Priors

- **[Human Protein Atlas]** Subcellular and tissue protein expression atlases [[resource](https://www.proteinatlas.org/)] [[subcellular](https://www.proteinatlas.org/humanproteome/subcellular)] [[paper](https://doi.org/10.1126/science.aal3321)]

- **[OpenCell]** Endogenous protein tagging, localization, and interaction data for human cellular organization (**Science 2022**) [[paper](https://doi.org/10.1126/science.abi6983)] [[dataset](https://registry.opendata.aws/czb-opencell/)]

- **[ProtiCelli]** Proteome-wide image generation resources for human cell protein localization (**bioRxiv 2026**) [[paper](https://doi.org/10.64898/2026.03.31.715748)] [[code](https://github.com/CellProfiling/ProtiCelli)]

- **[SubCell]** Proteome-aware microscopy foundation model resources based on HPA images (**bioRxiv 2025**) [[paper](https://doi.org/10.1101/2024.12.06.627299)] [[code](https://github.com/CellProfiling/subcell-embed)]

- **[STRING]** Protein functional association and interaction networks [[resource](https://string-db.org/)] [[paper](https://academic.oup.com/nar/article/53/D1/D730/7903368)]

- **[OmniPath]** Signaling, ligand-receptor, and causal network priors for multi-omics analysis [[resource](https://omnipathdb.org/)] [[paper](https://academic.oup.com/nar/article/54/D1/D652/8326458)]

### Chemical, Drug, and Target Resources

- **[Drug Repurposing Hub]** Curated compound library with targets, mechanisms, and clinical annotations (**Nature Medicine 2017**) [[paper](https://www.nature.com/articles/nm.4306)] [[resource](https://clue.io/repurposing)]

- **[DepMap/CCLE/PRISM]** Cancer dependency, molecular profile, and drug-response resources for cell-line perturbation modeling [[resource](https://depmap.org/portal/)] [[paper](https://www.nature.com/articles/s41568-024-00763-x)]

- **[ChEMBL]** Drug-like molecules, bioactivities, targets, and assays [[resource](https://www.ebi.ac.uk/chembl/)] [[paper](https://academic.oup.com/nar/article/52/D1/D1180/7337608)]

- **[BindingDB]** Protein-small molecule binding affinity knowledgebase [[resource](https://www.bindingdb.org/)] [[paper](https://academic.oup.com/nar/article/53/D1/D1633/7906836)]

- **[PubChem]** Compound identifiers, structures, assays, and bioactivity records [[resource](https://pubchem.ncbi.nlm.nih.gov/)] [[paper](https://academic.oup.com/nar/article/51/D1/D1373/6777787)]

## Reports and Blogs

- **[Symposium]** AI Proteomics and Virtual Cell (**© by Westlake University 2025**) [[media](https://mp.weixin.qq.com/s/45Evl-tKw9DAY8xdcWSlPg)] [[中文解读](https://mp.weixin.qq.com/s/efB7nMeXLjxEqpfbhv8AWg?scene=1)]

- **[Report]** Projections at the Frontier: Snapshot 2025 (**© by Decoding Bio's Team 2025**) [[slide](https://drive.google.com/file/d/15ku6sly5P9yjehvMnfrija8F2oFl7koR/view)] [[中文解读](https://mp.weixin.qq.com/s/XMtP2LZJIAl6a3nDsw-AEQ?scene=1&click_id=10)]

- **[Post]** Chan Zuckerberg Initiative's rBio Uses Virtual Cells to Train AI, Bypassing Lab Work (**© by Michael Nuñez 2025**) [[blog](https://venturebeat.com/ai/chan-zuckerberg-initiatives-rbio-uses-virtual-cells-to-train-ai-bypassing-lab-work)]

- **[Blog]** AI's Next Frontier: Modeling Life Itself (**© by Chan Zuckerberg Initiative 2025**) [[blog](https://www.freethink.com/artificial-intelligence/virtual-cells)] [[中文解读](https://mp.weixin.qq.com/s/nVJDT3LqzRY6QZUU6odNLQ)]

- **[Blog]** The State of Research on Virtual Cell Modeling (**© by Will Connell 2025**) [[blog](https://behindbioml.substack.com/p/the-state-of-research-on-virtual)]

- **[Blog]** What Are Virtual Cells? Learning "Universal Representations" of Life's Fundamental Unit (**© by Elliot Hershberg 2025**) [[blog](https://centuryofbio.com/p/virtual-cell)]

- **[中文 Blog]** 什么是虚拟细胞：AI 生物学的“登月时刻”和“苦涩教训” (**© by 范阳 2025**) [[blog](https://mp.weixin.qq.com/s/vmXIwW1XNCOVinI31Eh1Bw)]

- **[Introduction]** Virtual Cells (**© by Udara Jay 2025**) [[blog](https://udara.io/science/virtual-cells)]

## Videos

- **[Arc Institute]** Predicting Cellular Responses to Perturbation across Diverse Contexts with STATE [[YouTube](https://www.youtube.com/watch?v=rPWzpPf-3N0)]

- **[Valence Labs]** Virtual Cells: Predict, Explain, Discover [[YouTube](https://www.youtube.com/watch?v=QSfVjsa1i4g)]

- **[EPFL]** Virtual Cells and Digital Twins: AI in Personalized Medicine [[YouTube](https://www.youtube.com/watch?v=AJL7fMYvCKE)]

- **[SciLifeLab]** Emma Lundberg: AI Virtual Cells Could Revolutionize Biological Science [[YouTube](https://www.youtube.com/watch?v=Ifc1FDdDlvw)]

- **[Chan Zuckerberg Initiative]** AI Virtual Cell Models: How AI is Accelerating Science [[YouTube](https://www.youtube.com/watch?v=bzSdgzDVpq4)]

- **[Chan Zuckerberg Initiative]** CZI's Vision for AI-Powered "Virtual Cells" [[YouTube](https://www.youtube.com/watch?v=DxVL0oVMr60)]

- **[Podcast]** Google DeepMind CEO: We Want to Build a Virtual Cell [[YouTube](https://www.youtube.com/watch?v=CEOOMYxMvY4)]

## Historical and Foundational Works

- **[HPA Cell Atlas]** `[Morphology]` A subcellular map of the human proteome (**Science 2017**) [[paper](https://doi.org/10.1126/science.aal3321)] [[resource](https://www.proteinatlas.org/humanproteome/subcellular)]

- **[OpenCell]** `[Morphology]` OpenCell: Endogenous tagging for the cartography of human cellular organization (**Science 2022**) [[paper](https://doi.org/10.1126/science.abi6983)] [[dataset](https://registry.opendata.aws/czb-opencell/)]

- **[Perturb-seq]** `[Perturbation]` Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq (**Cell 2022**) [[paper](https://doi.org/10.1016/j.cell.2022.05.013)] [[code](https://github.com/thomasmaxwellnorman/Perturbseq_GI)]

- **[GEARS]** `[Perturbation]` Predicting transcriptional outcomes of novel multigene perturbations with GEARS (**Nature Biotechnology 2023**) [[paper](https://www.nature.com/articles/s41587-023-01905-6)] [[code](https://github.com/snap-stanford/GEARS)] ![GitHub stars](https://img.shields.io/github/stars/snap-stanford/GEARS.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/snap-stanford/GEARS)]

- **[Geneformer]** `[Foundation Model]` Transfer Learning Enables Predictions in Network Biology (**Nature 2023**) [[paper](https://doi.org/10.1038/s41586-023-06139-9)] [[code](https://github.com/jkobject/geneformer)] ![GitHub stars](https://img.shields.io/github/stars/jkobject/geneformer.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/jkobject/geneformer)]

- **[CellOT]** `[Perturbation]` Learning Single-Cell Perturbation Responses Using Neural Optimal Transport (**Nature Methods 2023**) [[paper](https://www.nature.com/articles/s41592-023-01969-x)] [[code](https://github.com/bunnech/cellot)] ![GitHub stars](https://img.shields.io/github/stars/bunnech/cellot.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/bunnech/cellot)]

- **[tGPT]** `[Foundation Model]` Generative Pretraining from Large-Scale Transcriptomes for Single-Cell Deciphering (**iScience 2023**) [[paper](https://doi.org/10.1016/j.isci.2023.106536)] [[code](https://github.com/deeplearningplus/tGPT)] ![GitHub stars](https://img.shields.io/github/stars/deeplearningplus/tGPT.svg?logo=github&label=Stars) [[ask deepwiki](https://deepwiki.com/deeplearningplus/tGPT)]

- `[Virtual Cell]` Building the Next Generation of Virtual Cells to Understand Cellular Biology (**Biophysical Journal 2023**) [[paper](https://doi.org/10.1016/j.bpj.2023.04.006)]

- **[Research Highlight]** `[Virtual Cell]` Simulating a Whole Cell (**Nature Methods 2022**) [[paper](https://doi.org/10.1038/s41592-022-01429-y)]

- **[Comment]** Personalized Medicine: Time for One-Person Trials (**Nature Comment 2015**) [[paper](https://doi.org/10.1038/520609a)]

- **[Theory]** `[Virtual Cell]` A Whole-Cell Computational Model Predicts Phenotype from Genotype (**Cell 2012**) [[paper](https://doi.org/10.1016/j.cell.2012.05.044)]

- **[Virtual Cell]** The Virtual Cell - A Candidate Co-Ordinator for "Middle-Out" Modelling of Biological Systems (**BIB 2009**) [[paper](https://doi.org/10.1093/bib/bbp010)]

- **[VCell 7.7]** `[Virtual Cell]` Virtual Cell Modelling and Simulation Software Environment (**IET Systems Biology 2008**) [[paper](https://doi.org/10.1049/iet-syb:20080102)] [[software](https://vcell.org/)]

- Quantitative Cell Biology with the Virtual Cell (**Trends in Cell Biology 2003**) [[paper](https://doi.org/10.1016/j.tcb.2003.09.002)]

- **[Review]** The Virtual Cell: A Software Environment for Computational Cell Biology (**Trends in Biotechnology 2001**) [[paper](https://doi.org/10.1016/S0167-7799(01)01740-1)]

- **[Opinion]** Whole-Cell Simulation: A Grand Challenge of the 21st Century (**Trends in Biotechnology 2001**) [[paper](https://doi.org/10.1016/S0167-7799(01)01636-5)]

## Related Resources

- **[Virtual Cell Challenge]** Official challenge site for evaluation and community updates [[homepage](https://virtualcellchallenge.org/)]

- **[Arc Virtual Cell Atlas]** Large-scale perturbation atlas and codebase from Arc Institute [[repo](https://github.com/ArcInstitute/arc-virtual-cell-atlas)]

- **[VCell Software]** Long-running software environment for computational cell biology [[site](https://vcell.org/)]

- **[Noetik OCTO-vc]** Technical report and demo for virtual cells in tissue [[report](https://www.noetik.ai/octo-vc)] [[demo](https://celleporter.noetik.ai/)]

## Contributing

If you want to suggest a paper, dataset, benchmark, blog, or project, open an Issue or Pull Request. Please follow [CONTRIBUTING.md](CONTRIBUTING.md) for the submission format and quality bar.
