# Paper code-link audit — 2026-09-28

Baseline: `304c9a23cc0b42e638e5024fdf1e590ab2a4162d`. The paper collection remains at **285 records**.

**Initial pass:** 36 missing code links added; 1 data-only link removed from code availability. Code links moved **159 → 194**.

**Follow-up pass:** 11 previously missing code links were added, 37 existing `project_match` entries were upgraded after stronger paper↔repository evidence, and scDifformer's official release URL was corrected. Current totals are **205 code links**, **198 documented correspondences**, **7 project matches**, and **80 records without an established code link**. The latter does not establish that their authors have not released code. See [catalog cleanup follow-up](catalog-cleanup-2026-09-28.md).

## Verification and coverage

- Checked every one of the 159 pre-existing code URLs for reachability; all returned HTTP 200. GitHub source trees and README content were collected for triage. Reachability alone was not treated as paper correspondence.
- Ran a GitHub label/acronym search for all 126 initially missing-code records; all requests succeeded. An additional exact-title pass succeeded for 75 records; 51 requests were rate-limited (HTTP 403). These failed requests are recorded, not treated as negative search evidence.
- Attempted the linked paper source pages and manually followed selected full-text, code-availability, project and repository evidence. Some pages were blocked, rate-limited or unavailable. The Coladan code link was verified on page 68 of its accepted-manuscript PDF, including visual inspection.
- New links require paper-to-repository or repository-to-exact-paper correspondence and visible implementation/analysis files. An acronym match, a nonempty repository, a cited baseline, a dataset link or a lab website alone does not qualify.
- This audit did not read all 285 PDFs or run third-party implementations. Source availability is not a guarantee of complete dependencies, checkpoints, training data, reproduction instructions or successful execution.

## Added code links

| Paper / project | Code | Evidence |
| --- | --- | --- |
| NUDGE | [chopper6/NUDGE](https://github.com/chopper6/NUDGE) | [Paper explicitly links code](https://www.pnas.org/doi/10.1073/pnas.2604777123) |
| scKITE | [BaoJiee/scKITE](https://github.com/BaoJiee/scKITE) | [Repository identifies the exact paper](https://github.com/BaoJiee/scKITE/blob/main/README.md) |
| Cell Shapes | [CellProfiling/2D_shapespace](https://github.com/CellProfiling/2D_shapespace) | [Paper explicitly links code](https://pmc.ncbi.nlm.nih.gov/articles/PMC12132440/) |
| SpatialJEPA | [li-lab-mcgill/SpatialJEPA](https://github.com/li-lab-mcgill/SpatialJEPA) | [Repository identifies the exact paper](https://github.com/li-lab-mcgill/SpatialJEPA/blob/main/README.md) |
| Literature-Authored Embeddings | [NiklasBrunn/blueprint-embedding](https://github.com/NiklasBrunn/blueprint-embedding) | [Repository identifies the exact paper](https://github.com/NiklasBrunn/blueprint-embedding/blob/main/README.md) |
| Harmonised FM Benchmark | [iced-soda/FM-benchmark](https://github.com/iced-soda/FM-benchmark) | [Repository identifies the exact paper](https://github.com/iced-soda/FM-benchmark/blob/main/README.md) |
| scContam | [sarwanpasha/scContam](https://github.com/sarwanpasha/scContam) | [Repository identifies the exact paper](https://github.com/sarwanpasha/scContam/blob/main/README.md) |
| U-Pert | [QiangweiPeng/UPT](https://github.com/QiangweiPeng/UPT) | [Repository identifies the exact paper](https://github.com/QiangweiPeng/UPT/blob/main/README.md) |
| TranScouter | [PancakeZoy/TranScouter](https://github.com/PancakeZoy/TranScouter) | [Repository identifies the exact paper](https://github.com/PancakeZoy/TranScouter/blob/main/README.md) |
| COMPASS | [rohitsinghlab/compass](https://github.com/rohitsinghlab/compass) | [Repository identifies the exact paper](https://github.com/rohitsinghlab/compass/blob/main/README.md) |
| Coladan | [99wzj/Coladan](https://github.com/99wzj/Coladan) | [Paper explicitly links code](https://link.springer.com/content/pdf/10.1186/s13073-026-01713-y_reference.pdf#page=68) |
| VOICE | [Luosanj/VOICE_HE_ST_Pred](https://github.com/Luosanj/VOICE_HE_ST_Pred) | [Repository identifies the exact paper](https://github.com/Luosanj/VOICE_HE_ST_Pred/blob/main/README.md) |
| VISTA | [23AIBox/VISTA](https://github.com/23AIBox/VISTA) | [Repository identifies the exact paper](https://github.com/23AIBox/VISTA/blob/main/README.md) |
| SciCore-Omics | [OpenBMB/Scicore-Omics](https://github.com/OpenBMB/Scicore-Omics) | [Repository identifies the exact paper](https://github.com/OpenBMB/Scicore-Omics/blob/main/README.md) |
| Morphodynamics-Expr | [cancer-dynamics/MMIST_Copperman_2026](https://github.com/cancer-dynamics/MMIST_Copperman_2026) | [Repository identifies the exact paper](https://github.com/cancer-dynamics/MMIST_Copperman_2026/blob/main/README.md) |
| RegFormer | [BGIResearch/RegFormer](https://github.com/BGIResearch/RegFormer) | [Paper explicitly links code](https://www.nature.com/articles/s41467-026-72198-x) |
| Lingshu-Cell | [alibaba-damo-academy/Lingshu-Cell](https://github.com/alibaba-damo-academy/Lingshu-Cell) | [Repository identifies the exact paper](https://github.com/alibaba-damo-academy/Lingshu-Cell/blob/main/README.md) |
| Conformation Description Language | [jiachengxiong/ConfSeq](https://github.com/jiachengxiong/ConfSeq) | [Repository identifies the exact paper](https://github.com/jiachengxiong/ConfSeq/blob/main/README.md) |
| Departures | [ChangxiChi/Departures](https://github.com/ChangxiChi/Departures) | [Paper explicitly links code](https://ojs.aaai.org/index.php/AAAI/article/view/39190) |
| Latent Causal Processes | [week3ndzZ/CITEVAE](https://github.com/week3ndzZ/CITEVAE) | [Repository identifies the exact paper](https://github.com/week3ndzZ/CITEVAE) |
| msInfer | [YuzhiSun/msInfer](https://github.com/YuzhiSun/msInfer) | [Repository identifies the exact paper](https://github.com/YuzhiSun/msInfer/blob/main/README.md) |
| Gene Importance | [Genentech/SIGnature](https://github.com/Genentech/SIGnature) | [Repository identifies the exact paper](https://github.com/Genentech/SIGnature/blob/main/README.rst) |
| Hi-C FM | [Noble-Lab/HiCFoundation](https://github.com/Noble-Lab/HiCFoundation) | [Repository identifies the exact paper](https://github.com/Noble-Lab/HiCFoundation/blob/main/README.md) |
| Virtual Spatial Tumor | [lilab-stanford/CANVAS](https://github.com/lilab-stanford/CANVAS) | [Repository identifies the exact paper](https://github.com/lilab-stanford/CANVAS/blob/main/README.md) |
| Tissueformer | [ZadorLaboratory/TissueFormer](https://github.com/ZadorLaboratory/TissueFormer) | [Paper explicitly links code](https://link.springer.com/article/10.1186/s12859-026-06490-4) |
| CytoSignal | [welch-lab/cytosignal](https://github.com/welch-lab/cytosignal) | [Paper explicitly links code](https://www.nature.com/articles/s41588-026-02624-9) |
| graphene-seq | [LiuLab-Bioelectronics-Harvard/Graphene_seq](https://github.com/LiuLab-Bioelectronics-Harvard/Graphene_seq) | [Paper explicitly links code](https://www.nature.com/articles/s41467-026-73883-7) |
| SpaMosaic | [JinmiaoChenLab/SpaMosaic](https://github.com/JinmiaoChenLab/SpaMosaic) | [Paper explicitly links code](https://www.nature.com/articles/s41588-026-02573-3) |
| Morphodynamics | [Sedzinski-Lab/trackomics/tree/v1_paper](https://github.com/Sedzinski-Lab/trackomics/tree/v1_paper) | [Paper explicitly links code](https://link.springer.com/article/10.1038/s44320-026-00212-x) |
| Single Cell Notebooks | [integrativebioinformatics/scNotebooks](https://github.com/integrativebioinformatics/scNotebooks) | [Repository identifies the exact paper](https://github.com/integrativebioinformatics/scNotebooks/blob/main/README.md) |
| scpFormer | [qfchou/scpFormer](https://github.com/qfchou/scpFormer) | [Repository identifies the exact paper](https://github.com/qfchou/scpFormer/blob/main/README.md) |
| STAMP | [Single-Cell-Genomics-Group-CNAG-CRG/STAMP](https://github.com/Single-Cell-Genomics-Group-CNAG-CRG/STAMP) | [Repository identifies the exact paper](https://github.com/Single-Cell-Genomics-Group-CNAG-CRG/STAMP/blob/main/README.md) |
| Perturb-FISH | [lbinan/Perturb-FISH](https://github.com/lbinan/Perturb-FISH) | [Paper explicitly links code](https://www.cell.com/cell/fulltext/S0092-8674(25)00197-7) |
| GDE | [njwfish/DistributionEmbeddings](https://github.com/njwfish/DistributionEmbeddings) | [Paper explicitly links code](https://arxiv.org/html/2505.18150) |
| Cell Maps | [idekerlab/cellmaps_pipeline](https://github.com/idekerlab/cellmaps_pipeline) | [Paper explicitly links code](https://www.nature.com/articles/s41586-025-08878-3) |
| Evaluating Feature Extraction in Ovarian Cancer Cell Line Co-Cultures Using Deep Neural Networks | [Functional-Precision-Medicine-Lab/Evaluating-Feature-Extraction-in-Ovarian-Cancer-Cell-Line-Co-Cultures-Using-Deep-Neural-Networks](https://github.com/Functional-Precision-Medicine-Lab/Evaluating-Feature-Extraction-in-Ovarian-Cancer-Cell-Line-Co-Cultures-Using-Deep-Neural-Networks) | [Repository identifies the exact paper](https://github.com/Functional-Precision-Medicine-Lab/Evaluating-Feature-Extraction-in-Ovarian-Cancer-Cell-Line-Co-Cultures-Using-Deep-Neural-Networks/blob/main/README.md) |

## Data-only and pending releases

| Entry | Decision | Evidence / note |
| --- | --- | --- |
| BioM-JEPA | `release_pending`; `code_url` remains empty | Paper says BioM-JEPA software/checkpoint will be released. Its CellBench-LS GitHub link is an evaluation-data source, not the BioM-JEPA implementation. [Source](https://arxiv.org/html/2608.05928). |
| PertReason | `data_only`; `code_url` remains empty | README identifies a dataset repository. The complete inspected tree contains dataset/prompt JSONL files and documentation, not implementation code. [Source](https://github.com/dongkwan-kim/PertReasonQA/blob/main/README.md). |
| scVision | `release_pending`; `code_url` remains empty | Paper states source is reserved and planned for public release upon publication. Lab website source is not scVision implementation. [Source](https://arxiv.org/html/2607.14163). |
| HoloCell | `release_pending`; `code_url` remains empty | README explicitly says source code, weights, processing scripts, tutorials and benchmark pipelines will be released in a future update; no implementation files present. [Source](https://github.com/bjzgcai/HoloCell/blob/main/README.md). |

PertReasonQA is preserved as a **dataset** link. HoloCell and scVision project links are preserved without being counted as released code.

## Deliberately unconfirmed or rejected candidates

| Entry | Decision | Reason and evidence |
| --- | --- | --- |
| Cell-JEPA | `reject_candidate` | CellJEPA is an independent benchmark-driven project; the README does not identify the catalogued Cell-JEPA paper. Similar name is not sufficient. [Inspected candidate](https://github.com/jameshyojaelee/CellJEPA/blob/main/README.md). |
| Reliable Perturbations | `unconfirmed_candidate` | Code-bearing benchmark repository found, but exact correspondence to the listed reliable-perturbations paper was not established. Not added. [Inspected candidate](https://github.com/BrainStOrmics/Perturbation_benchmark). |
| Cytokine Atlas | `reject_candidate` | This is a Japanese cytokine reference-site generator; no demonstrated correspondence to the human cytokine-response atlas paper. [Inspected candidate](https://github.com/ichihara1205/cytokine-atlas/blob/main/README.md). |
| PertDiffBench | `unconfirmed_candidate` | Strong same-project candidate with code and matching tasks. README uses a different workshop title and leaves the paper citation pending; exact manuscript correspondence remains unconfirmed. [Inspected candidate](https://github.com/ZijunSong/PertDiffBench). |
| AlphaCell | `unconfirmed_candidate` | Code-bearing, method-aligned repository exists, but the exact paper/author correspondence was not established by accessible primary evidence. Not added to the code filter. [Inspected candidate](https://github.com/DELTA-TJ-submission/AlphaCell). |
| Perturbation Representation | `reject_candidate` | IMPA and X-Pert are implementations of different papers. Their relevance to perturbation modelling does not establish code correspondence. [Inspected candidate](https://github.com/theislab/IMPA). |
| DrugPT | `reject_candidate` | DrugPT-Net is a different project/paper (perturbation-guided visible neural network), not the listed flexible gene/chemical-representation framework. [Inspected candidate](https://github.com/syjssj95/DrugPT-Net). |
| OmniPert | `unconfirmed_candidate` | Benchmark implementation found, but repository does not establish itself as the listed OmniPert paper implementation. Not added. [Inspected candidate](https://github.com/micheetong/OmniPert_benchmark). |
| CZI Evaluation | `reject_candidate` | Independent Virtual Cell Challenge side project, not implementation of the CZI workshop recommendations. [Inspected candidate](https://github.com/shrutisshikhare/sc-virtualcell-bench). |

Homonyms were disambiguated: the population-phenotype TissueFormer uses **ZadorLaboratory/TissueFormer**, not the Uhler-lab model. CellJEPA and DrugPT-Net were not accepted merely because their names resembled catalog entries.

## Interpretation of the code filters

`Has a code link` includes released implementation or paper-analysis links in the catalog, including existing `project_match` entries whose exact-paper correspondence remains weaker. `Documented correspondence` includes only `paper_linked` or `repository_linked` entries.

`not_found`, `related_only`, `release_pending` and `data_only` must have an empty `code_url` and cannot pass either positive code filter. Their auxiliary resources can remain under `links`. `not_found` means unresolved, not closed source.

The 44 pre-existing `project_match` entries were not silently upgraded by this audit. Code files, public checkpoints and full reproducibility are different claims; for example scKITE has implementation source but still describes some release/reproduction materials as pending.

The source data, README, searchable catalog and exports are regenerated together. Regression tests cover positive, missing, pending and data-only filter behavior.

[Machine-readable audit for all 285 records](../data/curation/code-audit-2026-09-28.json) contains before/after metadata, per-record access/search outcomes, reviewed evidence URLs, and unresolved candidates.
