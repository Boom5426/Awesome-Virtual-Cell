import json,unittest
from pathlib import Path
from scripts import build_landscape
ROOT=Path(__file__).resolve().parents[1]
class LandscapeTests(unittest.TestCase):
 def test_landscape(self):
  ps=json.loads((ROOT/'data/papers.json').read_text())['papers'];tags={t for p in ps for t in p['tags']};cfg=json.loads((ROOT/'config/landscape.json').read_text())
  for b in cfg['branches']:
   for c in b['children']:self.assertIn(c['tag'],tags)
  self.assertIn('location.href="./?tag="+encodeURIComponent(tag)',(ROOT/'docs/landscape.template.html').read_text())
  e=build_landscape.render();self.assertEqual((ROOT/'landscape.html').read_text(),e);self.assertEqual((ROOT/'docs/landscape.html').read_text(),e)
if __name__=='__main__':unittest.main()
