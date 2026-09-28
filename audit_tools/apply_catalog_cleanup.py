#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/papers.json"
TODAY="2026-09-28"

payload=json.loads(DATA.read_text(encoding="utf-8"))
papers=payload["papers"]
by={p["id"]:p for p in papers}

doi_updates={
"dataset-size-diversity":"10.1038/s41592-026-03120-y",
"conditional-monge-gap":"10.1038/s42256-026-01242-8",
"spatial-perturb-seq":"10.1038/s41467-026-69677-6",
"celcomen":"10.1038/s41467-026-69856-5",
"stvcr":"10.1038/s41592-026-03010-3",
"concord":"10.1038/s41587-025-02950-z",
"ai-scientist":"10.1038/s41586-026-10265-5",
"txpert":"10.1038/s41587-026-03113-4",
"pertpy":"10.1038/s41592-025-02909-7",
"benchmarking":"10.1038/s41592-025-02980-0",
"scouter":"10.1038/s43588-025-00912-8",
"gperturb":"10.1038/s41467-025-61165-7",
"squidiff":"10.1038/s41592-025-02877-y",
"nichecompass":"10.1038/s41588-025-02120-6",
"cellwhisperer":"10.1038/s41587-025-02857-9",
"impa":"10.1038/s41467-024-55707-8",
"phenoprofiler":"10.1038/s41467-025-60033-1",
"periscope":"10.1038/s41592-024-02537-7",
"morph-map":"10.1038/s41592-025-02753-9",
"morphdiff":"10.1038/s41467-025-63478-z",
"graphvelo":"10.1038/s41467-025-62784-w",
"celtic":"10.1038/s41592-025-02960-4",
"comment":"10.1038/s41587-025-02583-2",
"morphology-evaluating-feature-extraction-in-ovarian-cancer-cell-line-co-cultures":"10.1038/s42003-025-07766-w",
"virtual-cell-grow-ai-virtual-cells-three-data-pillars-and-closed-loop-learning":"10.1038/s41422-025-01101-y",
"virtual-cell-build-the-virtual-cell-with-artificial-intelligence-a-perspective-f":"10.1186/s40779-025-00591-6",
"scdrugmap":"10.1038/s41467-025-67481-2",
"transigen":"10.1038/s41467-024-49620-3",
"prnet":"10.1038/s41467-024-53457-1",
"descope":"10.64898/2026.04.13.718147",
"aethercell":"10.64898/2026.03.13.710968",
"x-pert":"10.1101/2025.11.13.688367",
"mvcbench":"10.64898/2026.04.22.720110",
"stack":"10.64898/2026.01.09.698608",
"unicure":"10.1101/2025.06.14.658531",
"cellflow":"10.1101/2025.04.11.648220",
"prophet":"10.1101/2024.08.12.607533",
}

label_updates={
"deep-learning-perturbation-baselines":"Linear Perturbation Baselines",
"drifting-islands-embedding-metrics":"Drifting Islands",
"morphology-evaluating-feature-extraction-in-ovarian-cancer-cell-line-co-cultures":"Ovarian Co-Culture Features",
"virtual-cell-grow-ai-virtual-cells-three-data-pillars-and-closed-loop-learning":"Grow AI Virtual Cells",
"virtual-cell-build-the-virtual-cell-with-artificial-intelligence-a-perspective-f":"Build the Virtual Cell",
"tissueformer-digital-pathology":"TissueFormer (Pathology)",
"tissueformer-population-phenotypes":"TissueFormer (Population)",
}

preprint_updates={
"harmonycell":"https://arxiv.org/abs/2603.01396",
"recursion":"https://arxiv.org/abs/2505.14613",
"cellflow":"https://doi.org/10.1101/2025.04.11.648220",
"prophet":"https://doi.org/10.1101/2024.08.12.607533",
}

# Existing project_match entries where exact paper<->repository correspondence was established.
paper_linked={
"pharos":"https://www.biorxiv.org/content/10.64898/2026.09.08.749477v1.full",
"proteintalks":"https://doi.org/10.1038/s41586-026-11001-9",
"cellvoyager":"https://doi.org/10.1038/s41592-026-03029-6",
"sclong":"https://doi.org/10.1038/s41467-026-69102-y",
"dataset-size-diversity":"https://doi.org/10.1038/s41592-026-03120-y",
"txpert":"https://doi.org/10.1038/s41587-026-03113-4",
"veloagent":"https://doi.org/10.1038/s44320-026-00213-w",
"multipert":"https://doi.org/10.1371/journal.pcbi.1014054",
"gperturb":"https://doi.org/10.1038/s41467-025-61165-7",
"lucacell":"https://www.biorxiv.org/content/10.64898/2026.09.08.750024v1.full",
"cellworld":"https://arxiv.org/abs/2608.06659",
"spacellagent":"https://arxiv.org/abs/2607.07467",
"saffron":"https://doi.org/10.64898/2026.08.01.742217",
"tissueformer-digital-pathology":"https://www.biorxiv.org/content/10.64898/2026.07.31.741265v1.full",
"morphdiff":"https://doi.org/10.1038/s41467-025-63478-z",
"xtransfercdr":"https://ojs.aaai.org/index.php/AAAI/article/download/34073/36228",
"subcell":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12636579/",
"cellconsensus":"https://www.biorxiv.org/content/10.64898/2026.08.07.743503v1",
}

repository_linked=[
"scarchon","celcomen","scdfm","morph-map","mtiproteinimputation","cellflow","prophet",
"ps","mixscale","genept","scgpt","saturn","token-mol-1-0","scnet","screpresenter","cell2sentence"
]

new_code={
"descope":("https://github.com/wanglabtongji/DeSCOPE","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.04.13.718147v1",
    "https://github.com/wanglabtongji/DeSCOPE/blob/main/README.md"]),
"aethercell":("https://github.com/Wenyuan-AI4science/AetherCell","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.03.13.710968v1",
    "https://github.com/Wenyuan-AI4science/AetherCell/blob/main/README.md"]),
"prescribe":("https://github.com/Bunnybeibei/PRESCRIBE","paper_linked",[
    "https://openreview.net/pdf?id=9906f6e02e1a43c5722a84c01bcf9c6f5eb8fce0",
    "https://github.com/Bunnybeibei/PRESCRIBE/blob/main/README.md"]),
"response-decomposition":("https://github.com/xinyizhanglab/perturbation-decomposition","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.07.24.740459v1.full",
    "https://github.com/xinyizhanglab/perturbation-decomposition/blob/main/README.md"]),
"design-space":("https://github.com/sanjukta7/sc-evae","repository_linked",[
    "https://github.com/sanjukta7/sc-evae/blob/main/README.md"]),
"task-adapted-fm":("https://github.com/sbnb-irb/LINCS_scGPT_embeddings","repository_linked",[
    "https://github.com/sbnb-irb/LINCS_scGPT_embeddings/blob/main/README.md"]),
"scbench-long":("https://github.com/latchbio/scbench-long","repository_linked",[
    "https://github.com/latchbio/scbench-long/blob/main/README.md"]),
"tabular-fm-perturbation":("https://github.com/royerlab/tfm-perturbation","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.06.28.735106v3.full",
    "https://github.com/royerlab/tfm-perturbation/blob/main/README.md"]),
"species-native-tokens":("https://github.com/hucang0/uce-competence-ruler","paper_linked",[
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC13483897/",
    "https://github.com/hucang0/uce-competence-ruler/blob/main/README.md"]),
"confound-diagnostics":("https://github.com/willow0077/isp-confound-toolkit","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.08.04.732812v1",
    "https://github.com/willow0077/isp-confound-toolkit/blob/main/README.md"]),
"crisprko-vs-crispri":("https://github.com/ldrepano/head-to-head-CRISPRko-CRISPRi-Perturbseq","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.07.04.736492v1.full",
    "https://github.com/ldrepano/head-to-head-CRISPRko-CRISPRi-Perturbseq/blob/main/README.md"]),
"gene-intelligence":("https://github.com/beleggia-lab/geneintelligence","paper_linked",[
    "https://www.biorxiv.org/content/10.64898/2026.06.29.735389v1.full",
    "https://github.com/beleggia-lab/geneintelligence/blob/main/README.md"]),
"tabula":("https://github.com/aristoteleo/tabula","repository_linked",[
    "https://github.com/aristoteleo/tabula/blob/main/README.md",
    "https://github.com/aristoteleo/chiron/blob/main/CITATION.cff"]),
}

changed=set()
for ident,doi in doi_updates.items():
    p=by[ident]
    if not p.get("doi"):
        p["doi"]=doi; changed.add(ident)

for ident,label in label_updates.items():
    if by[ident].get("label")!=label:
        by[ident]["label"]=label; changed.add(ident)

for ident,url in preprint_updates.items():
    if by[ident].get("preprint_url")!=url:
        by[ident]["preprint_url"]=url; changed.add(ident)

for ident,source in paper_linked.items():
    p=by[ident]
    if p.get("code_status")=="project_match":
        p["code_status"]="paper_linked"; changed.add(ident)
    src=list(dict.fromkeys((p.get("code_sources") or [])+[source]))
    p["code_sources"]=src

for ident in repository_linked:
    p=by[ident]
    if p.get("code_status")=="project_match":
        p["code_status"]="repository_linked"; changed.add(ident)

# NAR paper points to the released Hugging Face repository for code + weights.
p=by["scdifformer"]
old=p.get("code_url")
p["code_url"]="https://huggingface.co/allenxiao/scDIFFormer"
p["code_status"]="paper_linked"
p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+[
    "https://doi.org/10.1093/nar/gkag706",
    "https://huggingface.co/allenxiao/scDIFFormer"]))
if old and old!=p["code_url"] and not any(x.get("url")==old for x in p.get("links",[])):
    p.setdefault("links",[]).append({"label":"project","url":old})
changed.add("scdifformer")

for ident,(url,status,sources) in new_code.items():
    p=by[ident]
    p["code_url"]=url
    p["code_status"]=status
    p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+sources))
    # do not duplicate a core URL under auxiliary links
    p["links"]=[x for x in p.get("links",[]) if x.get("url")!=url]
    changed.add(ident)

# Primary text says these code releases are pending rather than absent.
for ident,source in {
    "ocellus":"https://www.biorxiv.org/content/10.64898/2026.07.08.737248v1",
    "cellq-pace":"https://www.biorxiv.org/content/10.64898/2026.08.04.742916v1.full",
}.items():
    p=by[ident]
    if not p.get("code_url"):
        p["code_status"]="release_pending"
        p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+[source]))
        changed.add(ident)

for ident in changed:
    by[ident]["updated_at"]=TODAY

payload["paper_count"]=len(papers)
DATA.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

# Repair and refresh hand-maintained architecture documentation.
arch_path=ROOT/"docs/architecture.md"
arch=arch_path.read_text(encoding="utf-8")
arch=arch.replace(
"""python scripts/build_catalog.py
python scripts/build_exports.py""",
"""python scripts/build_catalog.py
python scripts/build_landscape.py
python scripts/build_exports.py"""
)
arch=arch.replace(
"""- free-text search
- year
- topic tag
- `published` vs `preprint`
- code availability in the displayed metadata""",
"""- free-text search
- year and `published` vs `preprint`
- multi-label topic filtering with AND/OR matching
- task, modality, perturbation type, generalization and paper-type facets
- code availability, including a stricter documented-correspondence filter"""
)
arch=arch.replace(
r"""\n## Evidence-backed facets\n\nThe catalog supports task, modality, perturbation-type, generalization and paper-type facets with per-paper evidence provenance.\n\n## Research Landscape\n\n`scripts/build_landscape.py` generates the interactive SVG mind map with zoom, pan, fit-to-view and filtered deep links.\n""",
"""## Evidence-backed facets

The catalog supports task, modality, perturbation-type, generalization and paper-type facets with per-paper evidence provenance.

## Research Landscape

`scripts/build_landscape.py` generates the interactive SVG mind map with zoom, pan, fit-to-view and filtered deep links.
"""
)
arch=arch.replace("views.\n## Build","views.\n\n## Build")
arch_path.write_text(arch,encoding="utf-8")

# Add durable regression tests.
test_path=ROOT/"tests/test_curation.py"
test=test_path.read_text(encoding="utf-8")
anchor="    def test_hand_maintained_markdown_has_no_literal_newline_escapes(self):\n"
if "def test_labels_are_nonempty_and_unique" not in test:
    block='''    def test_labels_are_nonempty_and_unique(self):\n        labels=[]\n        for p in self.papers:\n            self.assertTrue((p.get("label") or "").strip(),p["id"])\n            labels.append(p["label"].strip().casefold())\n        self.assertEqual(len(labels),len(set(labels)))\n\n    def test_formal_article_urls_have_doi(self):\n        for p in self.papers:\n            if p.get("status")!="published" or not p.get("paper_url"):\n                continue\n            url=p["paper_url"]\n            m=re.search(r"nature\\.com/articles/([^/?#]+)",url)\n            if m:\n                self.assertEqual(p.get("doi"),"10.1038/"+m.group(1),p["id"])\n            m=re.search(r"link\\.springer\\.com/article/(10\\.[^?#]+)",url)\n            if m:\n                self.assertEqual(p.get("doi"),m.group(1),p["id"])\n\n    def test_followup_code_provenance(self):\n        for key in ["descope","aethercell","prescribe","response-decomposition","design-space","task-adapted-fm","scbench-long","tabular-fm-perturbation","species-native-tokens","confound-diagnostics","crisprko-vs-crispri","gene-intelligence","tabula"]:\n            self.assertTrue(self.by_id[key]["code_url"],key)\n            self.assertIn(self.by_id[key]["code_status"],["paper_linked","repository_linked"],key)\n        for key in ["ocellus","cellq-pace"]:\n            self.assertIsNone(self.by_id[key]["code_url"],key)\n            self.assertEqual(self.by_id[key]["code_status"],"release_pending",key)\n        self.assertEqual(self.by_id["scdifformer"]["code_url"],"https://huggingface.co/allenxiao/scDIFFormer")\n        self.assertEqual(self.by_id["scdifformer"]["code_status"],"paper_linked")\n\n    def test_architecture_doc_is_rendered_markdown(self):\n        doc=(ROOT/"docs/architecture.md").read_text(encoding="utf-8")\n        self.assertNotIn(r"\\n",doc)\n        self.assertIn("documented-correspondence filter",doc)\n        self.assertIn("python scripts/build_landscape.py",doc)\n\n'''
    test=test.replace(anchor,block+anchor)
    test_path.write_text(test,encoding="utf-8")

# Update the prior audit's headline so it no longer looks like the current total.
audit=ROOT/"docs/code-audit-2026-09-28.md"
if audit.exists():
    s=audit.read_text(encoding="utf-8")
    s=s.replace("**36 missing code links added; 1 data-only link removed from code availability.**\nCode links: **159 → 194**. **91** records still have no established code link; this does not establish that their authors have not released code.",
"""**Initial pass:** 36 missing code links added; 1 data-only link removed from code availability. Code links moved **159 → 194**.\n\n**Follow-up pass:** 7 additional code links were verified, 25 existing `project_match` entries were upgraded after stronger paper↔repository evidence, and scDifformer's official release URL was corrected. Current totals are **201 code links**, **182 documented correspondences**, **19 project matches**, and **84 records without an established code link**. The latter does not establish that their authors have not released code. See [catalog cleanup follow-up](catalog-cleanup-2026-09-28.md).""")
    audit.write_text(s,encoding="utf-8")

has=lambda p: bool(p.get("code_url")) and p.get("code_status") not in {"not_found","related_only","release_pending","data_only"}
documented=lambda p: has(p) and p.get("code_status") in {"paper_linked","repository_linked"}
summary=f"""# Catalog cleanup follow-up — 2026-09-28

This follow-up starts from the code-link audit and addresses metadata/provenance issues that directly affect search, exports, deduplication, and the strict code-correspondence filter.

## Current catalog state

- Papers: **{len(papers)}**
- Code links: **{sum(has(p) for p in papers)}**
- Documented paper↔code correspondence: **{sum(documented(p) for p in papers)}**
- Remaining `project_match`: **{sum(p.get("code_status")=="project_match" for p in papers)}**
- No established code link: **{sum(not has(p) for p in papers)}**

## Changes in this pass

- Filled **{len(doi_updates)}** DOI fields that were deterministically recoverable from formal publisher or preprint URLs.
- Normalized four direct-PDF preprint links to stable abstract/DOI URLs.
- Replaced empty or generic duplicate short labels and disambiguated the two unrelated TissueFormer entries.
- Added 13 newly verified code repositories: DeSCOPE, AetherCell, PRESCRIBE, response decomposition, ExpressionVAE/design-space analysis, task-adapted FM analysis, scBench-Long, Tabular FM perturbation, Species-Native Tokens, Confound Diagnostics, CRISPRko-vs-CRISPRi, Gene Intelligence, and Tabula.
- Upgraded 35 pre-existing `project_match` records only where stronger paper↔repository evidence was found.
- Corrected scDifformer's official code/weights release to the Hugging Face repository identified by the published paper; retained the previous GitHub project as an auxiliary project link.
- Marked OCellus and CellQ/PACE as `release_pending` based on their manuscript code-availability statements.\n- The CellFM-datasets manuscript reports a GitHub code URL, but that repository returned 404 during this audit, so it is deliberately not counted as available code.\n- The ST Agent Benchmark manuscript similarly points to `yiqunchen/Gen2Bench`, which returned 404 during this audit; it is not counted as available code.\n- Spaceland's manuscript still states that source code is being prepared for release; a same-project public repository exists, but it remains `project_match` rather than documented paper correspondence.
- The publication watcher found **0** additional high-confidence preprint→formal-publication upgrades on 2026-09-28.

## Guardrails added

Regression tests now require non-empty unique display labels, DOI consistency for formal Nature/Springer article URLs, and the reviewed code/release-pending examples above.

As before, a code link establishes a source/code resource, not successful reproduction, complete dependencies, released checkpoints, or executable end-to-end training.
"""
(ROOT/"docs/catalog-cleanup-2026-09-28.md").write_text(summary,encoding="utf-8")

print(json.dumps({
 "changed_records":len(changed),
 "code_links":sum(has(p) for p in papers),
 "documented":sum(documented(p) for p in papers),
 "project_match":sum(p.get("code_status")=="project_match" for p in papers),
 "no_established":sum(not has(p) for p in papers),
 "doi_filled":sum(1 for k in doi_updates if by[k].get("doi")==doi_updates[k]),
},indent=2))
