"""Live-challenges rendering and staleness warnings; no external network."""
import unittest
from datetime import date
from pathlib import Path
from scripts import build_readme

ROOT=Path(__file__).resolve().parents[1]

def sample(checked='2026-10-27'):
    return {'stale_after_days':14,'challenges':[{'name':'Demo','anchor':'#demo','checked_on':checked,
        'phase_now':'P1','next_milestone':'Due 5 Nov 2026','final_call':'Winners 30 Nov 2026',
        'milestones':[{'date':'2026-11-05','label':'final submissions due'},{'date':'2026-11-30','label':'winners announced'}],
        'sources':['https://example.org']}]}

class ChallengeTests(unittest.TestCase):
    def test_readme_block_matches_data(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        block=readme.split(build_readme.CH_START,1)[1].split(build_readme.CH_END,1)[0]
        self.assertEqual(block.strip(),build_readme.render_challenges(build_readme.load_challenges()).strip())

    def test_news_sits_above_research_papers(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertLess(readme.index('<a id="news"></a>'),readme.index('<a id="research-papers"></a>'))

    def test_header_uses_oldest_check(self):
        p=sample();p['challenges'].append(dict(p['challenges'][0],name='Older',checked_on='2026-10-01'))
        self.assertIn('checked on 1 October 2026',build_readme.render_challenges(p))

    def test_fresh_table_has_no_warnings(self):
        self.assertEqual(build_readme.challenge_warnings(sample(),date(2026,10,30)),[])

    def test_passed_milestone_and_age_warn(self):
        notes=build_readme.challenge_warnings(sample(),date(2026,11,12))
        self.assertTrue(any("milestone 'final submissions due'" in n for n in notes),notes)
        self.assertTrue(any('16 days ago' in n for n in notes),notes)

    def test_finished_challenge_asks_to_move(self):
        notes=build_readme.challenge_warnings(sample(),date(2026,12,1))
        self.assertEqual(len(notes),1)
        self.assertIn('move it to the update log',notes[0])

    def test_no_live_challenges(self):
        self.assertIn('none open',build_readme.render_challenges({'challenges':[]}))

if __name__=='__main__':unittest.main()
