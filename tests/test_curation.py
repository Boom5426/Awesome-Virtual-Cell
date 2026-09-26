import json
import unittest
from pathlib import Path
from scripts import build_readme

ROOT=Path(__file__).resolve().parents[1]

class CurationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))['papers']
        cls.by_id={p['id']:p for p in cls.papers}
        cls.taxonomy=json.loads((ROOT/'config/taxonomy.json').read_text())['tags']

    def test_every_paper_has_unique_controlled_tags(self):
        self.assertEqual(len(self.by_id),len(self.papers))
        for p in self.papers:
            self.assertTrue(p['tags'],p['id'])
            self.assertEqual(len(p['tags']),len(set(p['tags'])),p['id'])
            self.assertTrue(set(p['tags'])<=set(self.taxonomy),p['id'])

    def test_all_research_entries_visible_and_preserved(self):
        result=build_readme.render(self.papers)
        self.assertNotIn('<details>',result)
        self.assertEqual(sum(line.startswith('- ') for line in result.splitlines()),len(self.papers))
        for year in {p['year'] for p in self.papers}:
            self.assertIn(f'<a id="{year}"></a>',result)
        for p in self.papers:self.assertIn(p['title'],result)

    def test_keywords_do_not_determine_biological_categories(self):
        self.assertNotIn('Agent',self.by_id['veloagent']['tags'])
        self.assertIn('Dynamics',self.by_id['veloagent']['tags'])
        self.assertIn('Spatial',self.by_id['veloagent']['tags'])
        for k in ['uce','scnet','saturn','biom-jepa']:
            self.assertNotIn('Protein',self.by_id[k]['tags'],k)
        self.assertIn('Intervention Design',self.by_id['pharos']['tags'])
        self.assertIn('Perturbation',self.by_id['pharos']['tags'])
        self.assertNotIn('Morphology',self.by_id['cellflow']['tags'])

    def test_supported_code_links(self):
        pairs={'scouter':'PancakeZoy/scouter','prnet':'Perturbation-Response-Prediction/PRnet',
               'scdrugmap':'QSong-github/scDrugMap','cross-context-drugpert':'Panda-myj/PertDiff',
               'cycle-consistent-genmodel':'tansey-lab/multitme','adlf':'Cellarity/drugreflector'}
        for ident,path in pairs.items():
            self.assertEqual(self.by_id[ident]['code_url'],'https://github.com/'+path)
            self.assertTrue(self.by_id[ident]['code_sources'])
        self.assertIsNone(self.by_id['biom-jepa']['code_url'])
        self.assertEqual(self.by_id['biom-jepa']['code_status'],'release_pending')
        self.assertIsNone(self.by_id['context-not-scale']['code_url'])
        self.assertEqual(self.by_id['context-not-scale']['code_status'],'related_only')
        self.assertIn('cantinilab/scPRINT',self.by_id['scprint']['code_url'])

    def test_every_curated_record_has_evidence_receipt(self):
        entries=json.loads((ROOT/'data/curation/2026-09-26.json').read_text())['records']
        self.assertEqual({p['id'] for p in entries},set(self.by_id))
        for d in entries:
            self.assertTrue(d['tag_rationale'],d['id'])
            self.assertIn(d['tag_basis'],['abstract','project_documentation','title_and_metadata'])
            self.assertEqual(d['tags'],self.by_id[d['id']]['tags'])


    def test_intervention_design_expansion(self):
        expected={'cellnavi','pdgrapher','pairing','perturbnet','arc-phenotype-landscape-reversion','nudge-cell-fate','vcdesign','pharos'}
        self.assertTrue(expected.issubset(self.by_id))
        for key in expected:
            self.assertIn('Intervention Design',self.by_id[key]['tags'],key)
        self.assertEqual(self.by_id['pdgrapher']['code_url'],'https://github.com/mims-harvard/PDGrapher')
        self.assertEqual(self.by_id['vcdesign']['code_url'],'https://github.com/Boom5426/VCDesign-CED')
        self.assertEqual(self.by_id['pairing']['code_url'],'https://doi.org/10.5281/zenodo.15848686')
        self.assertEqual(self.by_id['perturbnet']['code_url'],'https://github.com/welch-lab/PerturbNet')


    def test_evaluation_measurement_branch(self):
        expected={'pertresolve','signal-bounds-baselines','evaluation-far-from-straightforward','vcbench-in-the-wild',
                  'principled-evaluation','systema','score-distributions','projection-basis','sccontam',
                  'reliable-perturbations','spurious-correlation','deep-learning-perturbation-baselines',
                  'drifting-islands-embedding-metrics'}
        self.assertTrue(expected.issubset(self.by_id))
        for key in expected:
            self.assertIn('Evaluation & Measurement',self.by_id[key]['tags'],key)
        self.assertNotIn('Evaluation & Measurement',self.by_id['virtual-cell-challenge-2026']['tags'])
        self.assertEqual(self.by_id['pertresolve']['code_url'],'https://github.com/Boom5426/PertResolve')
        self.assertEqual(self.by_id['principled-evaluation']['code_url'],'https://github.com/Virtual-Cell-Research-Community/scPertEval')

if __name__=='__main__':unittest.main()
