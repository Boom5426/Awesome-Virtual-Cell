import unittest
from unittest.mock import patch

from scripts import publication_watcher as watcher


class PublicationWatcherTests(unittest.TestCase):
    def test_collect_proposals_scans_all_preprints_before_capping(self):
        papers = [
            {"id": "p1", "status": "preprint", "title": "one"},
            {"id": "p2", "status": "preprint", "title": "two"},
            {"id": "p3", "status": "published", "title": "three"},
            {"id": "p4", "status": "preprint", "title": "four"},
        ]
        calls = []

        def fake_candidates(paper):
            calls.append(paper["id"])
            scores = {"p1": 0.91, "p2": 0.99, "p4": 0.95}
            return [{
                "title": paper["title"],
                "venue": "Example Journal",
                "year": 2026,
                "doi": "10.1234/" + paper["id"],
                "url": "https://doi.org/10.1234/" + paper["id"],
                "score": scores[paper["id"]],
            }]

        with patch.object(watcher, "candidates_for", side_effect=fake_candidates):
            proposals, scanned, failed = watcher.collect_proposals(papers, max_updates=2)

        self.assertEqual(["p1", "p2", "p4"], calls)
        self.assertEqual(3, scanned)
        self.assertEqual(0, failed)
        self.assertEqual(["p2", "p4"], [paper["id"] for paper, _ in proposals])

    def test_collect_proposals_records_failures_without_stopping(self):
        papers = [
            {"id": "bad", "status": "preprint", "title": "bad"},
            {"id": "good", "status": "preprint", "title": "good"},
        ]

        def fake_candidates(paper):
            if paper["id"] == "bad":
                raise RuntimeError("temporary failure")
            return [{
                "title": "good",
                "venue": "Example Journal",
                "year": 2026,
                "doi": "10.1234/good",
                "url": "https://doi.org/10.1234/good",
                "score": 0.99,
            }]

        with patch.object(watcher, "candidates_for", side_effect=fake_candidates):
            proposals, scanned, failed = watcher.collect_proposals(papers, max_updates=10)

        self.assertEqual(2, scanned)
        self.assertEqual(1, failed)
        self.assertEqual(["good"], [paper["id"] for paper, _ in proposals])


if __name__ == "__main__":
    unittest.main()
