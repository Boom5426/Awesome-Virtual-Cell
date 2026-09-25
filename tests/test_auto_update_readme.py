import unittest

from scripts import auto_update_catalog as v2
from scripts import auto_update_readme as discovery
from scripts import build_readme


class StructuredCatalogUpdateTests(unittest.TestCase):
    def test_catalog_dedupe_uses_structured_source_of_truth(self) -> None:
        candidate = discovery.Candidate(
            title="Example virtual cell perturbation model",
            label="ExampleVC",
            venue="bioRxiv",
            year=2026,
            section="research",
            subsection=None,
            tag="Virtual Cell",
            primary_link="https://doi.org/10.1234/example",
            doi="10.1234/example",
        )
        payload = {
            "papers": [{
                "title": candidate.title,
                "label": candidate.label,
                "doi": candidate.doi,
                "paper_url": None,
                "preprint_url": candidate.primary_link,
                "code_url": None,
                "links": [],
            }]
        }
        kept = discovery.dedupe_candidates([candidate], v2.catalog_keys(payload))
        self.assertEqual([], kept)

    def test_candidate_becomes_schema_v2_record(self) -> None:
        candidate = discovery.Candidate(
            title="Example virtual cell perturbation model",
            label="ExampleVC",
            venue="Nature Methods",
            year=2026,
            section="research",
            subsection=None,
            tag="Perturbation",
            primary_link="https://doi.org/10.1234/example",
            code_link="https://github.com/example/example-vc",
            doi="10.1234/example",
        )
        record = v2.candidate_to_record(candidate)
        self.assertEqual("published", record["status"])
        self.assertEqual(["Perturbation"], record["tags"])
        self.assertEqual("10.1234/example", record["doi"])
        self.assertNotIn("entry_markdown", record)
        self.assertIsInstance(record["links"], list)
        self.assertIsNotNone(record["added_at"])

    def test_render_entry_uses_structured_fields(self) -> None:
        paper = {
            "id": "example",
            "label": "ExampleVC",
            "title": "Example title",
            "year": 2026,
            "venue": "Nature Methods",
            "status": "published",
            "tags": ["Perturbation"],
            "doi": "10.1234/example",
            "paper_url": "https://doi.org/10.1234/example",
            "preprint_url": None,
            "code_url": "https://github.com/example/example",
            "links": [{"label": "project", "url": "https://example.org"}],
            "added_at": "2026-09-26",
            "updated_at": "2026-09-26",
        }
        rendered = build_readme.render_entry(paper)
        self.assertIn("**[ExampleVC]**", rendered)
        self.assertIn("[[paper](https://doi.org/10.1234/example)]", rendered)
        self.assertIn("[[project](https://example.org)]", rendered)

    def test_seeded_research_candidates_are_already_known(self) -> None:
        payload = v2.load_catalog()
        existing = v2.catalog_keys(payload)
        seeded = [c for c in discovery.seeded_manual_candidates() if c.section == "research"]
        deduped = discovery.dedupe_candidates(seeded, existing)
        self.assertEqual([], [c.label for c in deduped])


if __name__ == "__main__":
    unittest.main()
