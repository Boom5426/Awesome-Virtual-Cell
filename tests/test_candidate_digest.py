"""Candidate digest: ranking, de-duplication, venue policy and source parsing; no external network."""
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import candidate_digest as cd

ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'config/digest.json').read_text(encoding='utf-8'))

class CandidateDigestTests(unittest.TestCase):
    def test_rank_keeps_the_threshold_and_orders_by_score_then_date(self):
        cfg=CFG|{'min_keyword_score':2}
        recs=[{'title':'Perturb-seq screen in T cells','abstract':'We profile single cells.','date':'2026-10-22'},
              {'title':'Single-cell atlas of the liver','abstract':'We profile perturbation responses in cells.','date':'2026-10-20'},
              {'title':'Single-cell atlas of the lung','abstract':'We profile perturbation responses in cells.','date':'2026-10-24'},
              {'title':'A virtual cell benchmark','abstract':'Perturbation response prediction in single cells.','date':'2026-10-20'},
              {'title':'Bridge corrosion','abstract':'salt spray','date':'2026-10-23'}]
        ranked=cd.rank(recs,cfg)
        self.assertEqual([(r['title'],r['keyword_score']) for r in ranked],
                         [('A virtual cell benchmark',5),('Single-cell atlas of the lung',3),('Single-cell atlas of the liver',3),
                          ('Perturb-seq screen in T cells',2)])

    def test_keyword_score_matches_the_sweep_screen(self):
        score,matched=cd.keyword_hits('A virtual cell benchmark','We evaluate perturbation response prediction in single cells.',CFG)
        self.assertEqual(score,2+2+1)
        self.assertIn('virtual cell',matched)
        self.assertLess(cd.keyword_hits('Agent benchmark for code','Large language model agents write programs.',CFG)[0],2)

    def test_catalog_index_matches_doi_arxiv_and_title(self):
        idx=cd.CatalogIndex([{'title':'CellMSA: Context Modeling for Single-Cell Representation Learning','doi':None,
                              'paper_url':'https://doi.org/10.1038/s41592-026-00001-1','preprint_url':'https://arxiv.org/abs/2609.38908'}])
        self.assertTrue(idx.contains({'title':'x','doi':'10.1038/s41592-026-00001-1'}))
        self.assertTrue(idx.contains({'title':'y','arxiv':'2609.38908'}))
        self.assertTrue(idx.contains({'title':'CellMSA: context modeling for single-cell representation learning.'}))
        self.assertFalse(idx.contains({'title':'An unrelated atlas of the mouse liver'}))

    def test_venue_mapping_follows_the_policy(self):
        allowed={'Nature Methods','Bioinformatics','PNAS','Nature Structural & Molecular Biology'}
        aliases=CFG['journal_aliases']
        self.assertEqual(cd.venue_allowed('Nature methods',allowed,aliases),'Nature Methods')
        self.assertEqual(cd.venue_allowed('Bioinformatics (Oxford, England)',allowed,aliases),'Bioinformatics')
        self.assertEqual(cd.venue_allowed('Proceedings of the National Academy of Sciences of the United States of America',allowed,aliases),'PNAS')
        self.assertEqual(cd.venue_allowed('Nature structural & molecular biology',allowed,aliases),'Nature Structural & Molecular Biology')
        self.assertIsNone(cd.venue_allowed('Scientific reports',allowed,aliases))

    def test_biorxiv_fetch_pages_and_keeps_first_versions(self):
        pages={0:{'messages':[{'total':'3'}],'collection':[{'doi':'10.64898/a','title':'A','version':'1','date':'2026-10-20','abstract':'x'},
                                                             {'doi':'10.64898/b','title':'B','version':'2','date':'2026-10-20','abstract':'y'}]},
               2:{'messages':[{'total':'3'}],'collection':[{'doi':'10.64898/c','title':'C','version':'1','date':'2026-10-21','abstract':'z'}]}}
        with patch.object(cd.pw,'get_json',side_effect=lambda url:pages[int(url.rsplit('/',1)[1])]):
            rows=cd.fetch_biorxiv('2026-10-20','2026-10-26')
        self.assertEqual(sorted(r['doi'] for r in rows),['10.64898/a','10.64898/c'])

    def test_europepmc_fetch_follows_cursor(self):
        pages={'*':{'nextCursorMark':'n1','resultList':{'result':[{'title':'T1.','doi':'10.1/X','journalInfo':{'journal':{'title':'Nature methods'}},
                                                                   'abstractText':'<b>A</b>','firstPublicationDate':'2026-10-21'}]}},
               'n1':{'nextCursorMark':'n1','resultList':{'result':[]}}}
        def fake(url):
            import urllib.parse
            return pages[urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['cursorMark'][0]]
        with patch.object(cd.pw,'get_json',side_effect=fake):
            rows=cd.fetch_europepmc('2026-10-20','2026-10-26','TITLE_ABS:"single-cell"')
        self.assertEqual(len(rows),1)
        self.assertEqual((rows[0]['title'],rows[0]['doi'],rows[0]['venue'],rows[0]['abstract'].strip()),('T1','10.1/x','Nature methods','A'))

    def test_arxiv_fetch_parses_one_page(self):
        feed=('<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom"><entry>'
              '<id>http://arxiv.org/abs/2610.01234v1</id><title>A Virtual\n Cell</title><summary> Abstract text </summary>'
              '<published>2026-10-21T00:00:00Z</published></entry></feed>')
        with patch.object(cd.pw,'get_text',return_value=feed):
            rows=cd.fetch_arxiv('2026-10-20','2026-10-26','cat:q-bio.GN')
        self.assertEqual((rows[0]['arxiv'],rows[0]['title'],rows[0]['date']),('2610.01234','A Virtual Cell','2026-10-21'))

    def test_render_lists_warnings_watch_items_and_both_tiers(self):
        ranked=[{'title':'P','url':'https://x','venue':'bioRxiv','date':'2026-10-21','abstract':'word '*100,'keyword_score':3},
                {'title':'Q','url':'https://q','venue':'arXiv','date':'2026-10-21','abstract':'short','keyword_score':2}]
        meta={'start':'2026-10-20','end':'2026-10-26','counts':{'bioRxiv':1},'in_catalog':2,'outside_policy':1,'problems':['arXiv unavailable: timeout']}
        watch={'outside':[{'id':'g','label':'GenPerturb','venue':'BMC Bioinformatics','url':'https://doi.org/10.1186/x'}],'hints':[]}
        text=cd.render(ranked,meta,['VCC: re-check'],watch,3)
        for part in ['WARNING: arXiv unavailable','VCC: re-check','GenPerturb: published in BMC Bioinformatics','**[P](https://x)**','kw 3',
                     'titles only (1)','- [Q](https://q) (arXiv, kw 2)']:
            self.assertIn(part,text)
        self.assertNotIn('short',text)
        self.assertLess(len(cd.render(ranked*400,meta,[],None,3)),cd.ISSUE_LIMIT+100)

if __name__=='__main__':unittest.main()
