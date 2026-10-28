import unittest
import urllib.error
from unittest.mock import patch

from scripts import publication_watcher as watcher


def hit(paper, venue="Cell", score=0.99):
    return {"title": paper["title"], "venue": venue, "year": 2026, "doi": "10.1234/" + paper["id"],
            "url": "https://doi.org/10.1234/" + paper["id"], "score": score}


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
            return [hit(paper, score={"p1": 0.91, "p2": 0.99, "p4": 0.95}[paper["id"]])]

        with patch.object(watcher, "candidates_for", side_effect=fake_candidates):
            watch = watcher.collect_proposals(papers, max_updates=2)

        self.assertEqual(["p1", "p2", "p4"], calls)
        self.assertEqual(3, watch.scanned)
        self.assertEqual(0, watch.failed)
        self.assertEqual(["p2", "p4"], [paper["id"] for paper, _ in watch.proposals])

    def test_collect_proposals_records_failures_without_stopping(self):
        papers = [
            {"id": "bad", "status": "preprint", "title": "bad"},
            {"id": "good", "status": "preprint", "title": "good"},
        ]

        def fake_candidates(paper):
            if paper["id"] == "bad":
                raise RuntimeError("temporary failure")
            return [hit(paper)]

        with patch.object(watcher, "candidates_for", side_effect=fake_candidates):
            watch = watcher.collect_proposals(papers, max_updates=10)

        self.assertEqual(2, watch.scanned)
        self.assertEqual(1, watch.failed)
        self.assertEqual(["good"], [paper["id"] for paper, _ in watch.proposals])

    def test_venues_outside_the_policy_are_flagged_not_applied(self):
        papers = [{"id": "x", "status": "preprint", "title": "x"}, {"id": "r", "status": "preprint", "title": "r"}]
        lookup = lambda p: [hit(p, venue="BMC Bioinformatics")] if p["id"] == "x" else [hit(p, venue="Noetik Technical Report")]
        watch = watcher.collect_proposals(papers, max_updates=10, lookup=lookup)
        self.assertEqual(["x"], [p["id"] for p, _ in watch.outside])
        self.assertEqual(["r"], [p["id"] for p, _ in watch.proposals])

    def test_hints_are_never_proposals(self):
        papers = [{"id": "h", "status": "preprint", "title": "h"}]
        lookup = lambda p: [hit(p, venue="NeurIPS 2026 workshop") | {"hint": True}]
        watch = watcher.collect_proposals(papers, max_updates=10, lookup=lookup)
        self.assertEqual([], watch.proposals)
        self.assertEqual(["h"], [p["id"] for p, _ in watch.hints])

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
        new = {"title": "New journal title", "venue": "Cell", "year": 2026, "doi": "10.1016/j.cell.2026.01.001",
               "url": "https://doi.org/10.1016/j.cell.2026.01.001", "score": 1.0}
        watcher.apply_update(paper, new, "2026-10-13")
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
        self.assertEqual("crossref-relation", hits[0]["source"])

    def test_biorxiv_published_field_is_followed(self):
        paper = {"id": "g", "status": "preprint", "title": "GenPerturb: sequence-grounded interpretation of perturbation transcriptomes",
                 "doi": "10.64898/2026.07.01.735806", "year": 2026}
        responses = {
            "https://api.crossref.org/works/10.64898/2026.07.01.735806": {"message": {}},
            "https://api.biorxiv.org/details/biorxiv/10.64898/2026.07.01.735806": {"collection": [
                {"version": "1", "published": "NA"}, {"version": "2", "published": "10.1186/s12859-026-06689-5"}]},
            "https://api.crossref.org/works/10.1186/s12859-026-06689-5": {"message": {
                "title": ["GenPerturb: sequence-grounded interpretation of perturbation transcriptomes using pretrained models"],
                "container-title": ["BMC Bioinformatics"], "type": "journal-article", "DOI": "10.1186/s12859-026-06689-5",
                "published-online": {"date-parts": [[2026, 10, 16]]}}},
        }
        with patch.object(watcher, "get_json", side_effect=lambda url: responses[url]):
            hits = watcher.candidates_for(paper)
        self.assertEqual("BMC Bioinformatics", hits[0]["venue"])
        self.assertEqual("biorxiv-published", hits[0]["source"])

    def test_accepted_list_match_and_near_miss(self):
        index = {watcher.norm(t): {"title": t, "venue": "NeurIPS", "year": 2026, "url": "https://openreview.net/forum?id=a"}
                 for t in ["PerturbReason: A Knowledge-Grounded Benchmark and Framework for Mechanistic Reasoning",
                           "An Unrelated Paper About Robot Locomotion"]}
        exact, near = watcher.accepted_match({"title": "PertReason: A Knowledge-Grounded Benchmark and Framework for Mechanistic Reasoning"}, index)
        self.assertIsNone(near)
        self.assertEqual("NeurIPS", exact["venue"])
        self.assertIsNone(exact["doi"])
        miss, hint = watcher.accepted_match({"title": "A Knowledge Grounded Framework for Reasoning"}, index)
        self.assertIsNone(miss)
        none, none2 = watcher.accepted_match({"title": "Single-cell atlas of the mouse liver"}, index)
        self.assertIsNone(none)
        self.assertIsNone(none2)

    def test_accepted_papers_reads_papers_pages_and_skips_missing_years(self):
        def fake_text(url, retries=4):
            if url == watcher.PAPERS_PAGE.format(conf="neurips", year=2026):
                return ('<li><a href="/virtual/2026/poster/139067">CellMSA: Context Modeling</a></li>'
                        '<li><a href="/virtual/2026/session/1">Poster Session 1</a></li>'
                        '<li><a href="/virtual/2026/oral/7">Genes &amp; Cells</a></li>')
            if "CVPR2026" in url:
                return '<dt class="ptitle"><br><a href="/content/CVPR2026/html/X_CVPR_2026_paper.html">Imaging &amp; Phenomics</a></dt>'
            raise urllib.error.HTTPError(url, 404, "missing", None, None)

        with patch.object(watcher, "get_text", side_effect=fake_text):
            rows = watcher.accepted_papers([2026])
        self.assertEqual(3, len(rows))
        self.assertEqual("https://neurips.cc/virtual/2026/poster/139067", rows[watcher.norm("CellMSA: Context Modeling")]["url"])
        self.assertEqual("https://neurips.cc/virtual/2026/oral/7", rows[watcher.norm("Genes & Cells")]["url"])
        self.assertEqual("https://openaccess.thecvf.com/content/CVPR2026/html/X_CVPR_2026_paper.html",
                         rows[watcher.norm("Imaging & Phenomics")]["url"])

    def test_accepted_hit_uses_the_poster_pages_openreview_forum(self):
        paper = {"id": "p", "status": "preprint", "title": "PerturbReason: A Benchmark", "year": 2026, "doi": None,
                 "preprint_url": "https://arxiv.org/abs/2607.18777"}
        poster = "https://neurips.cc/virtual/2026/poster/139067"
        ctx = watcher.Context(arxiv={}, accepted={watcher.norm(paper["title"]): {
            "title": paper["title"], "venue": "NeurIPS", "year": 2026, "url": poster}})
        pages = {poster: '<a href="https://openreview.net/forum?id=nDBq0FPB7Y">OpenReview</a>',
                 "https://icml.cc/virtual/2026/poster/1": "no forum link on this page"}
        with patch.object(watcher, "get_text", side_effect=lambda url, retries=4: pages[url]), \
                patch.object(watcher, "linked_publication", return_value=None), \
                patch.object(watcher, "biorxiv_publication", return_value=None):
            hits = watcher.candidates_for(paper, ctx)
            fallback = watcher.openreview_link("https://icml.cc/virtual/2026/poster/1")
        self.assertEqual("https://openreview.net/forum?id=nDBq0FPB7Y", hits[0]["url"])
        self.assertEqual("https://icml.cc/virtual/2026/poster/1", fallback)

    def test_get_text_honors_retry_after(self):
        import email.message
        import io
        calls, sleeps = [], []

        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def read(self):
                return b"ok"

        def fake_urlopen(req, timeout):
            calls.append(req.full_url)
            if len(calls) == 1:
                headers = email.message.Message()
                headers["Retry-After"] = "7"
                raise urllib.error.HTTPError(req.full_url, 503, "busy", headers, io.BytesIO(b""))
            return Response()

        with patch.object(watcher.urllib.request, "urlopen", side_effect=fake_urlopen), \
                patch.object(watcher.time, "sleep", side_effect=sleeps.append):
            self.assertEqual("ok", watcher.get_text("https://example.org"))
        self.assertEqual([7], sleeps)

    def test_arxiv_records_parse_doi_and_journal_ref(self):
        feed = ('<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">'
                '<entry><id>http://arxiv.org/abs/2602.04901v2</id><arxiv:doi>10.1000/x</arxiv:doi></entry>'
                '<entry><id>http://arxiv.org/abs/2607.18777v1</id><arxiv:journal_ref>ICLR 2026 MLGenX workshop</arxiv:journal_ref></entry>'
                '</feed>')
        with patch.object(watcher, "get_text", return_value=feed):
            records = watcher.arxiv_records(["2602.04901", "2607.18777"])
        self.assertEqual("10.1000/x", records["2602.04901"]["doi"])
        self.assertEqual("ICLR 2026 MLGenX workshop", records["2607.18777"]["journal_ref"])
        self.assertIsNone(records["2607.18777"]["doi"])


if __name__ == "__main__":
    unittest.main()
