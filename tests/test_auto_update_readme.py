import unittest

from scripts import auto_update_readme as updater


class AutoUpdateReadmeTests(unittest.TestCase):
    def test_seeded_candidates_are_deduped_against_current_readme(self) -> None:
        readme_text = updater.load_readme()
        existing = updater.existing_readme_keys(readme_text)
        candidates = updater.seeded_manual_candidates()

        deduped = updater.dedupe_candidates(candidates, existing)

        self.assertEqual(
            [],
            [candidate.label for candidate in deduped],
            "Seeded candidates already in README should not be proposed again.",
        )


if __name__ == "__main__":
    unittest.main()
