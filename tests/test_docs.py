"""Regression tests for the offline Markdown documentation checker."""

import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import check_repository, heading_anchors


class DocumentationCheckerTests(unittest.TestCase):
    def test_internal_link_and_unicode_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "guide.md").write_text("# Phase 1 — Setup\n", encoding="utf-8")
            (root / "README.md").write_text("[guide](docs/guide.md#phase-1--setup)\n", encoding="utf-8")
            self.assertEqual([], check_repository(root))

    def test_missing_path_and_anchor_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.md").write_text("# Hello\n[bad](missing.md)\n[bad heading](a.md#absent)\n")
            errors = check_repository(root)
            self.assertEqual(2, len(errors))
            self.assertIn("local target does not exist", errors[0])
            self.assertIn("heading fragment #absent does not exist", errors[1])

    def test_fences_inline_code_external_and_escaped_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fence = chr(96) * 3
            tick = chr(96)
            (root / "a.md").write_text(
                fence + "md\n[not a link](missing.md)\n" + fence + "\n"
                + tick + "[not a link](missing.md)" + tick + "\n"
                + "[public](https://github.com/techrote/UXUI-Extreme)\n"
                + "[unsafe](../outside.md)\n"
            )
            errors = check_repository(root)
            self.assertEqual(1, len(errors))
            self.assertIn("escapes repository", errors[0])

    def test_duplicate_headings_get_distinct_slugs(self):
        self.assertEqual({"heading", "heading-1"}, heading_anchors("# Heading\n# Heading\n"))


if __name__ == "__main__":
    unittest.main()
