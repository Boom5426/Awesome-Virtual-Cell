#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/papers.json"
TODAY="2026-09-28"
payload=json.loads(DATA.read_text(encoding="utf-8"))
papers=payload["papers"]
by={p["id"]:p for p in papers}

UNRESOLVED={"not_found","related_only","release_pending","data_only"}
def has_code(p):
    return bool(p.get("code_url")) and p.get("code_status") not in UNRESOLVED
def documented(p):
    return has_code(p) and p.get("code_status") in {"paper_linked","repository_linked"}

before={
    "papers":len(papers),
    "code_links":sum(has_code(p) for p in papers),
    "documented":sum(documented(p) for p in papers),
    "project_match":sum(p.get("code_status")=="project_match" for p in papers),
    "no_established":sum(not has_code(p) for p in papers),
}

new_code={
    "zero-shot-benchmark":(
        "https://github.com/ShellyCoder/scFMBench","paper_linked",
        ["https://www.biorxiv.org/content/10.64898/2026.06.18.733285v1.full",
         "https://github.com/ShellyCoder/scFMBench/blob/main/README.md"]),
    "therapeutic-design":(
        "https://github.com/Bin-Chen-Lab/GPS","paper_linked",
        ["https://doi.org/10.1016/j.cell.2026.02.016",
         "https://github.com/Bin-Chen-Lab/GPS/blob/main/README.md"]),
    "crispri-map":(
        "https://github.com/claudiafeng123/crispri_scrnaseq_hipsci","paper_linked",
        ["https://pmc.ncbi.nlm.nih.gov/articles/PMC12903452/",
         "https://github.com/claudiafeng123/crispri_scrnaseq_hipsci/blob/main/README.md"]),
    "cytokine-atlas":(
        "https://github.com/poconnel3/CytoCarto","paper_linked",
        ["https://www.biorxiv.org/content/10.64898/2026.07.27.740961v1.full",
         "https://github.com/poconnel3/CytoCarto/blob/main/README.md"]),
    "spurious-correlation":(
        "https://github.com/phillipnicol/systema","paper_linked",
        ["https://www.biorxiv.org/content/10.64898/2026.05.07.723486v1.full",
         "https://github.com/phillipnicol/systema/blob/main/README.md"]),
    "bridge":(
        "https://github.com/tracy666/BRIDGE","paper_linked",
        ["https://www.biorxiv.org/content/10.64898/2026.05.05.722971v1.full",
         "https://github.com/tracy666/BRIDGE/blob/main/README.md"]),
    "morph-transcriptomic-genmodel":(
        "https://github.com/prsigma/MultiVCDiff","paper_linked",
        ["https://doi.org/10.1016/j.crmeth.2026.101459",
         "https://github.com/prsigma/MultiVCDiff/blob/main/README.md"]),
    "perturbation-representation":(
        "https://github.com/week3ndzZ/PerturbedVAE","repository_linked",
        ["https://arxiv.org/abs/2605.19343",
         "https://github.com/week3ndzZ/PerturbedVAE/blob/main/README.md"]),
    "pertdiffbench":(
        "https://github.com/ZijunSong/PertDiffBench","project_match",
        ["https://github.com/ZijunSong/PertDiffBench/blob/main/README.md"]),
}

upgrades={
    "deepscenic":("repository_linked",[
        "https://doi.org/10.64898/2026.09.18.752607",
        "https://github.com/aertslab/deepSCENIC_analyses/blob/main/README.md",
        "https://github.com/aertslab/deepSCENIC/blob/main/README.md"]),
    "vcharness":("repository_linked",[
        "https://www.biorxiv.org/content/10.64898/2026.04.11.717183v1",
        "https://genbio-ai.github.io/VCHarness/",
        "https://github.com/genbio-ai/VCHarness"]),
    "cellens":("repository_linked",[
        "https://arxiv.org/abs/2608.08430",
        "https://github.com/hnu-vis/CELLens/blob/main/README.md"]),
    "cellpb":("repository_linked",[
        "https://www.biorxiv.org/content/10.1101/2024.12.20.629581v2",
        "https://github.com/Chen-Li-17/CellPB/blob/main/README.md"]),
    "gremln":("repository_linked",[
        "https://doi.org/10.1101/2025.07.03.663009",
        "https://github.com/czi-ai/GREmLN/blob/main/README.md"]),
}

changed=set()
for ident,(url,status,sources) in new_code.items():
    p=by[ident]
    p["code_url"]=url
    p["code_status"]=status
    p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+sources))
    p["links"]=[x for x in p.get("links",[]) if x.get("url")!=url]
    p["updated_at"]=TODAY
    changed.add(ident)

for ident,(status,sources) in upgrades.items():
    p=by[ident]
    if p.get("code_status")=="project_match":
        p["code_status"]=status
    p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+sources))
    p["updated_at"]=TODAY
    changed.add(ident)

# Stable metadata fixes discovered during the same review.
p=by["crispri-map"]
p["doi"]="10.1016/j.xgen.2025.101076"
old_url=p.get("paper_url")
p["paper_url"]="https://doi.org/10.1016/j.xgen.2025.101076"
if old_url and old_url!=p["paper_url"] and not any(x.get("url")==old_url for x in p.get("links",[])):
    p.setdefault("links",[]).append({"label":"publisher","url":old_url})
p["updated_at"]=TODAY
changed.add("crispri-map")

p=by["llm4cell"]
p["doi"]="10.18653/v1/2026.acl-long.1942"
p["updated_at"]=TODAY
changed.add("llm4cell")

# Useful auxiliary resources explicitly reported by the cytokine-atlas paper.
p=by["cytokine-atlas"]
for item in [
    {"label":"project","url":"https://cytocarto.vercel.app"},
    {"label":"dataset","url":"https://zenodo.org/records/21497681"},
]:
    if not any(x.get("url")==item["url"] for x in p.get("links",[])):
        p.setdefault("links",[]).append(item)

payload["paper_count"]=len(papers)
DATA.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

after={
    "papers":len(papers),
    "code_links":sum(has_code(p) for p in papers),
    "documented":sum(documented(p) for p in papers),
    "project_match":sum(p.get("code_status")=="project_match" for p in papers),
    "no_established":sum(not has_code(p) for p in papers),
}

report=f"""# Final code-link sweep — 2026-09-28

This pass follows the repository-wide code audit and catalog cleanup. It focuses on the remaining unresolved method/benchmark/tool/dataset records and the residual `project_match` entries.

## Coverage change

| Metric | Before | After |
| --- | ---: | ---: |
| Papers | {before['papers']} | {after['papers']} |
| Code links | {before['code_links']} | {after['code_links']} |
| Documented paper↔code correspondence | {before['documented']} | {after['documented']} |
| Weaker `project_match` | {before['project_match']} | {after['project_match']} |
| No established code link | {before['no_established']} | {after['no_established']} |

## Newly established code links

- **Zero-Shot Benchmark → scFMBench** — manuscript explicitly links the benchmark code.
- **Therapeutic Design → GPS** — the Cell study's released GPS platform and figure code.
- **CRISPRi Map → crispri_scrnaseq_hipsci** — analysis repository linked to the published resource.
- **Cytokine Atlas → CytoCarto** — manuscript code/project release.
- **Spurious Correlation → phillipnicol/systema** — repository documents the paper-specific analysis directories.
- **BRIDGE → tracy666/BRIDGE** — repository identifies itself as the official implementation.
- **Morph-Transcriptomic GenModel → MultiVCDiff** — published study's released implementation.
- **Perturbation Representation → PerturbedVAE** — public implementation and representation-collapse analysis for the named method.
- **PertDiffBench → ZijunSong/PertDiffBench** — same branded benchmark project with implementation, retained as `project_match` because the repository's displayed workshop title differs from the catalogued bioRxiv title.

## Strengthened existing correspondences

DeepSCENIC, VCHarness, CELLens, CellPB and GREmLN now have repository/project evidence sufficient for the strict documented-correspondence filter.

Spaceland and SQUINT remain `project_match`: their public repositories clearly implement the named projects, but the evidence inspected here does not justify upgrading them to exact paper↔repository correspondence.

## Deliberately not counted as code

- **scCycleMol:** an exact-name public GitHub repository exists but is empty (size 0), so it is not treated as released code.
- **Cell-JEPA:** the similarly named CellJEPA repository remains a different project.
- **ST Agent Benchmark / CellFM-Datasets:** previously reported GitHub release URLs were unavailable during the audit; unavailable links are not counted.
- **BioM-JEPA, OCellus, CellQ/PACE, scVision, HoloCell:** retained as release-pending where the manuscript/project states code is forthcoming.
- Exact-title searches for Speciesformer, CellOS, AnnFlux, scRep, DoFormer, PerturbPFN, HarmonyCell, StateXDiff, SCALE, AlphaCell, CellxPert, CisTransCell, BioWorldModel and several other unresolved methods did not establish a public official implementation during this pass.

An unresolved record means **no established public code link was verified in this audit**, not that the work is necessarily closed-source. Code presence also does not imply successful reproduction, released checkpoints, complete dependencies or executable end-to-end training.
"""
(ROOT/"docs/final-code-sweep-2026-09-28.md").write_text(report,encoding="utf-8")

# Keep the earlier code-audit report's headline current without rewriting its historical detail.
audit=ROOT/"docs/code-audit-2026-09-28.md"
if audit.exists():
    s=audit.read_text(encoding="utf-8")
    marker="[Machine-readable audit for all 285 records]"
    note=f"""\n> **Current catalog after the final 2026-09-28 sweep:** {after['code_links']} code links, {after['documented']} documented correspondences, {after['project_match']} project matches, and {after['no_established']} records without an established code link. See [final code-link sweep](final-code-sweep-2026-09-28.md).\n\n"""
    if "Current catalog after the final 2026-09-28 sweep" not in s and marker in s:
        s=s.replace(marker,note+marker)
        audit.write_text(s,encoding="utf-8")

# Add a durable regression test to protect the reviewed decisions.
test=ROOT/"tests/test_code_metadata.py"
s=test.read_text(encoding="utf-8")
if "test_final_sweep_reviewed_links" not in s:
    insert='''\n    def test_final_sweep_reviewed_links(self):\n        papers=json.loads((ROOT/'data/papers.json').read_text())['papers']\n        by={p['id']:p for p in papers}\n        expected={\n            'zero-shot-benchmark':('https://github.com/ShellyCoder/scFMBench','paper_linked'),\n            'therapeutic-design':('https://github.com/Bin-Chen-Lab/GPS','paper_linked'),\n            'crispri-map':('https://github.com/claudiafeng123/crispri_scrnaseq_hipsci','paper_linked'),\n            'cytokine-atlas':('https://github.com/poconnel3/CytoCarto','paper_linked'),\n            'spurious-correlation':('https://github.com/phillipnicol/systema','paper_linked'),\n            'bridge':('https://github.com/tracy666/BRIDGE','paper_linked'),\n            'morph-transcriptomic-genmodel':('https://github.com/prsigma/MultiVCDiff','paper_linked'),\n            'perturbation-representation':('https://github.com/week3ndzZ/PerturbedVAE','repository_linked'),\n            'pertdiffbench':('https://github.com/ZijunSong/PertDiffBench','project_match'),\n        }\n        for key,(url,status) in expected.items():\n            self.assertEqual(by[key]['code_url'],url,key)\n            self.assertEqual(by[key]['code_status'],status,key)\n        for key in ['deepscenic','vcharness','cellens','cellpb','gremln']:\n            self.assertIn(by[key]['code_status'],{'paper_linked','repository_linked'},key)\n        self.assertEqual(by['spaceland']['code_status'],'project_match')\n        self.assertEqual(by['squint']['code_status'],'project_match')\n        self.assertIsNone(by['sccyclemol']['code_url'])\n        self.assertEqual(by['crispri-map']['doi'],'10.1016/j.xgen.2025.101076')\n        self.assertEqual(by['llm4cell']['doi'],'10.18653/v1/2026.acl-long.1942')\n'''
    s=s.replace("\nif __name__=='__main__':unittest.main()\n",insert+"\nif __name__=='__main__':unittest.main()\n")
    test.write_text(s,encoding="utf-8")

print(json.dumps({"before":before,"after":after,"changed_records":len(changed)},indent=2))
