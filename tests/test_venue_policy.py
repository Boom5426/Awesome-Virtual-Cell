"""Venue allowlist invariants (owner decision 2026-10-28); no external network."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class VenuePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy=json.loads((ROOT/'config/venue_policy.json').read_text(encoding='utf-8'))
        cls.allowed=set(cls.policy['published_venues'])|set(cls.policy['other_venues'])
        cls.papers=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))['papers']
        cls.receipts=json.loads((ROOT/'data/curation/2026-09-26.json').read_text(encoding='utf-8'))

    def test_published_venues_are_allowlisted(self):
        for p in self.papers:
            if p['status']=='published':
                self.assertTrue(p['venue'] in self.allowed or p['venue'].endswith(self.policy['report_suffix']),p['id'])

    def test_excluded_venues_stay_excluded(self):
        self.assertFalse(set(self.policy['excluded_venues'])&self.allowed)
        for v in ['BMC Bioinformatics','Cells','Frontiers in Cell and Developmental Biology']:
            self.assertIn(v,self.policy['excluded_venues'])

    def test_validator_rejects_unlisted_venue(self):
        import contextlib,io,tempfile
        from scripts import validate_catalog
        data=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))
        next(p for p in data['papers'] if p['status']=='published')['venue']='Cells'
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'papers.json';path.write_text(json.dumps(data),encoding='utf-8')
            old=validate_catalog.DATA;validate_catalog.DATA=path
            try:
                out=io.StringIO()
                with contextlib.redirect_stdout(out):code=validate_catalog.main()
            finally:validate_catalog.DATA=old
        self.assertEqual(code,1)
        self.assertIn("published venue 'Cells' is not in config/venue_policy.json",out.getvalue())

    def test_removed_records_keep_receipts(self):
        live={p['id'] for p in self.papers}
        removed=[r for r in self.receipts['removed'] if r['removed_at']=='2026-10-28']
        self.assertEqual(len(removed),11)
        for r in removed:
            self.assertNotIn(r['id'],live)
            self.assertIn(r['venue'],self.policy['excluded_venues'])
            self.assertTrue(r['reason'])
            self.assertEqual(r['receipt']['id'],r['id'])

if __name__=='__main__':unittest.main()
