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

if __name__=='__main__':unittest.main()
