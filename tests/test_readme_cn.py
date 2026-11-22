"""The Chinese latest-paper index must be generated from the same catalog as English."""
import json
import unittest
from pathlib import Path
from scripts import build_readme

ROOT = Path(__file__).resolve().parents[1]


class ChineseReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))["papers"]
        cls.cn = (ROOT / "README_CN.md").read_text(encoding="utf-8")

    def test_latest_batch_matches_source(self):
        section = self.cn.split(build_readme.CN_START, 1)[1].split(build_readme.CN_END, 1)[0]
        self.assertEqual(section.strip(), build_readme.render_recent_cn(self.papers).strip())

    def test_all_latest_papers_and_statuses_appear(self):
        latest_date = max(p.get("added_at") or "" for p in self.papers)
        latest = [p for p in self.papers if p.get("added_at") == latest_date]
        rendered = build_readme.render_recent_cn(self.papers)
        self.assertIn(f"{len(latest)} 篇论文", rendered)
        for paper in latest:
            self.assertIn(paper["title"], rendered)
            if paper.get("code_url"):
                self.assertIn(paper["code_url"], rendered)
            elif paper.get("code_status") == "release_pending":
                self.assertIn("代码待公开", rendered)

    def test_pending_code_is_not_shown_as_released(self):
        lingocell = next(p for p in self.papers if p["id"] == "nov26-lingocell")
        self.assertIsNone(lingocell["code_url"])
        self.assertEqual(lingocell["code_status"], "release_pending")
        self.assertIn("https://lingocell.com/resources.html", self.cn)


if __name__ == "__main__":
    unittest.main()
