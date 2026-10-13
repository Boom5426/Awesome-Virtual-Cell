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

    def test_proceedings_titles_are_normalized_to_short_venues(self):
        self.assertEqual("KDD", watcher.normalize_venue(
            "Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2"))
        self.assertEqual("ACM BCB", watcher.normalize_venue(
            "Proceedings of the 17th ACM International Conference on Bioinformatics, Computational Biology and Health Informatics"))
        self.assertEqual("NeurIPS", watcher.normalize_venue("Advances in Neural Information Processing Systems 38"))
        self.assertEqual("Nature Methods", watcher.normalize_venue("Nature Methods"))

    def test_year_prefers_online_publication(self):
        item = {"published-print": {"date-parts": [[2026, 2]]}, "published-online": {"date-parts": [[2025, 10, 3]]}}
        self.assertEqual(2025, watcher.year_of(item))
        self.assertEqual(2026, watcher.year_of({"published-print": {"date-parts": [[2026, 2]]}}))

    def test_apply_update_adopts_formal_title_and_keeps_preprint(self):
        paper = {"id": "x", "title": "Old preprint title", "status": "preprint", "venue": "bioRxiv", "year": 2025,
                 "doi": "10.1101/2025.01.01.000001", "paper_url": None,
                 "preprint_url": "https://doi.org/10.1101/2025.01.01.000001", "code_url": None, "links": []}
        hit = {"title": "New journal title", "venue": "Cell", "year": 2026, "doi": "10.1016/j.cell.2026.01.001",
               "url": "https://doi.org/10.1016/j.cell.2026.01.001", "score": 1.0}
        watcher.apply_update(paper, hit, "2026-10-13")
        self.assertEqual("New journal title", paper["title"])
        self.assertEqual("published", paper["status"])
        self.assertEqual("10.1016/j.cell.2026.01.001", paper["doi"])
        self.assertEqual("https://doi.org/10.1101/2025.01.01.000001", paper["preprint_url"])

    def test_crossref_preprint_relation_is_followed_even_when_retitled(self):
        paper = {"id": "x", "status": "preprint", "title": "UniCure: A Foundation Model for Predicting Cancer Therapy Response",
                 "doi": "10.1101/2025.06.14.658531", "year": 2025}
        responses = {
            "https://api.crossref.org/works/10.1101/2025.06.14.658531": {"message": {"relation": {
                "is-preprint-of": [{"id-type": "doi", "id": "10.1016/j.ccell.2026.07.010"}]}}},
            "https://api.crossref.org/works/10.1016/j.ccell.2026.07.010": {"message": {
                "title": ["UniCure: A multi-modal model for predicting personalized cancer therapy response"],
                "container-title": ["Cancer Cell"], "type": "journal-article", "DOI": "10.1016/j.ccell.2026.07.010",
                "published-print": {"date-parts": [[2026, 10]]}}},
        }
        with patch.object(watcher, "get_json", side_effect=lambda url: responses[url]):
            hits = watcher.candidates_for(paper)
        self.assertEqual(1, len(hits))
        self.assertEqual("Cancer Cell", hits[0]["venue"])
        self.assertEqual(2026, hits[0]["year"])
        self.assertEqual(1.0, hits[0]["score"])


if __name__ == "__main__":
    unittest.main()
