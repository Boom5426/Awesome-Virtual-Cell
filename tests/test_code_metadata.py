"""Code-status invariants; no external network or third-party model execution."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CodeMetadataTests(unittest.TestCase):
    def test_code_status_and_provenance(self):
        for p in json.loads((ROOT/'data/papers.json').read_text())['papers']:
            with self.subTest(paper=p['id']):
                status=p.get('code_status')
                if status in {'not_found','related_only','release_pending','data_only'}:
                    self.assertFalse(p.get('code_url'))
                if status in {'paper_linked','repository_linked','project_match'}:
                    self.assertTrue(p.get('code_url'))
                    self.assertTrue(p.get('code_sources'))

    def test_dated_audit_is_internally_consistent(self):
        audit=json.loads((ROOT/'data/curation/code-audit-2026-09-28.json').read_text())
        records=audit['records'];summary=audit['summary']
        self.assertEqual(len(records),summary['papers'])
        self.assertEqual(len({r['id'] for r in records}),len(records))
        for when in ['before','after']:
            self.assertEqual(sum(bool(r[when]['code_url']) for r in records),summary['code_links_'+when])
        for r in records:
            m=r.get('manual_review',{})
            if m.get('decision')=='add_code':
                self.assertFalse(r['before']['code_url'])
                self.assertTrue(r['after']['code_url'])
                self.assertTrue(m['sources'])
                self.assertTrue(m.get('code_paths_sample'))

    def test_final_sweep_reviewed_links(self):
        papers=json.loads((ROOT/'data/papers.json').read_text())['papers']
        by={p['id']:p for p in papers}
        expected={
            'zero-shot-benchmark':('https://github.com/ShellyCoder/scFMBench','paper_linked'),
            'therapeutic-design':('https://github.com/Bin-Chen-Lab/GPS','paper_linked'),
            'crispri-map':('https://github.com/claudiafeng123/crispri_scrnaseq_hipsci','paper_linked'),
            'cytokine-atlas':('https://github.com/poconnel3/CytoCarto','paper_linked'),
            'spurious-correlation':('https://github.com/phillipnicol/systema','paper_linked'),
            'bridge':('https://github.com/tracy666/BRIDGE','paper_linked'),
            'morph-transcriptomic-genmodel':('https://github.com/prsigma/MultiVCDiff','paper_linked'),
            'perturbation-representation':('https://github.com/week3ndzZ/PerturbedVAE','repository_linked'),
            'pertdiffbench':('https://github.com/ZijunSong/PertDiffBench','project_match'),
        }
        for key,(url,status) in expected.items():
            self.assertEqual(by[key]['code_url'],url,key)
            self.assertEqual(by[key]['code_status'],status,key)
        for key in ['deepscenic','vcharness','cellens','cellpb','gremln']:
            self.assertIn(by[key]['code_status'],{'paper_linked','repository_linked'},key)
        self.assertEqual(by['spaceland']['code_status'],'project_match')
        self.assertEqual(by['squint']['code_status'],'project_match')
        self.assertIsNone(by['sccyclemol']['code_url'])
        self.assertEqual(by['crispri-map']['doi'],'10.1016/j.xgen.2025.101076')
        self.assertEqual(by['llm4cell']['doi'],'10.18653/v1/2026.acl-long.1942')

if __name__=='__main__':unittest.main()
