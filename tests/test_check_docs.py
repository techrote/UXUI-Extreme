"""Navigation regressions use temporary repositories, not prose assertions."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_docs import check_repository, main


class CheckDocsTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, path, content):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
        return file

    def errors(self):
        return [str(error) for error in check_repository(self.root).errors]

    def test_valid_navigation_then_broken_path_and_fragment(self):
        self.write("README.md", "# Home\n[Guide](docs/guide.md#usage)\n![Picture](images/demo.png)\n")
        self.write("docs/guide.md", "# Guide\n## Usage\n[Home](../README.md#home)\n")
        image = self.write("images/demo.png", "fixture image")
        self.assertEqual(self.errors(), [])
        image.unlink()
        self.write("docs/guide.md", "# Guide\n## Renamed\n[Home](../README.md#home)\n")
        errors = self.errors()
        self.assertEqual(len(errors), 2)
        self.assertIn("README.md:2:", errors[0])
        self.assertIn("fragment #usage", errors[0])
        self.assertIn("README.md:3:", errors[1])
        self.assertIn("does not exist", errors[1])

    def test_reference_links_images_and_duplicate_heading_collisions(self):
        self.write("README.md", """# Home
[first][ GUIDE ] [guide][] [guide]
![icon][image]
[last](guide.md#repeat-1-1)
[guide]: guide.md#repeat-1 "Description"
[image]: picture.svg
""")
        self.write("guide.md", "# Repeat\n# Repeat\n# Repeat-1\n")
        self.write("picture.svg", "<svg/>")
        self.assertEqual(self.errors(), [])
        self.write("guide.md", "# Repeat\n# Other\n# Repeat-1\n")
        self.assertEqual(len(self.errors()), 1)
        self.assertIn("#repeat-1-1", self.errors()[0])

    def test_unused_malformed_reference_is_ignored_but_used_one_fails(self):
        self.write("README.md", "# Home\n[unused]:\nThis [ordinary text] is not a link.\n")
        self.assertEqual(self.errors(), [])
        self.write("README.md", "# Home\n[used][]\n[used]:\n\n[missing][unknown]\n")
        errors = self.errors()
        self.assertEqual(len(errors), 2)
        self.assertIn("malformed definition at line 3", errors[0])
        self.assertIn("undefined reference 'unknown'", errors[1])

    def test_reference_destinations_and_titles_can_continue_on_next_line(self):
        self.write("README.md", """# Home
[guide] [home]
[guide]:
  docs/guide.md
  "title with [example](not-a-real-link.md)"
[home]: #home
  'another title'
""")
        self.write("docs/guide.md", "# Guide\n")
        self.assertEqual(self.errors(), [])

    def test_malformed_unused_definition_does_not_hide_prose_links(self):
        self.write("README.md", "# Home\n[unused]:\nRead [real](missing.md)\n")
        errors = self.errors()
        self.assertEqual(len(errors), 1)
        self.assertIn("README.md:3:", errors[0])
        self.assertIn("local target does not exist", errors[0])

    def test_fences_code_spans_comments_and_escaped_examples_are_ignored(self):
        self.write("README.md", r"""# Visible
```md
[broken](gone.md)
# Hidden
```
~~~~
[missing][unknown]
~~~
[still hidden](gone.md)
~~~~
`[example](gone.md)` and ``[example ` nested](gone.md)``
<!-- [hidden](gone.md) -->
\[escaped](gone.md)
[works](#visible)
""")
        self.assertEqual(self.errors(), [])
        self.write("other.md", "[no](README.md#hidden)\n")
        self.assertIn("fragment #hidden", self.errors()[0])
        self.write("other.md", "`multi-line code\n# Fake\n`\n[no](#fake)\n")
        self.assertIn("fragment #fake", self.errors()[0])

    def test_comment_and_fence_examples_do_not_swallow_following_links(self):
        self.write("README.md", """# Home
```html
<!-- unfinished comment inside a code example
```
<!--
``` unfinished fence inside a comment
-->
[real](missing.md)
""")
        errors = self.errors()
        self.assertEqual(len(errors), 1)
        self.assertIn("README.md:8:", errors[0])
        self.write("README.md", "# Home\n`<!--` is a code example.\n[real](missing.md)\n")
        self.assertEqual(len(self.errors()), 1)
        self.assertIn("README.md:3:", self.errors()[0])

    def test_url_decoding_queries_and_parentheses(self):
        self.write("README.md", r"""# Home
[space](docs/a%20b.md?raw=1#hello-world)
[hash](docs/hash%23name.md)
[question](docs/what%3F.md)
[paren](docs/a(b).md)
[escaped](docs/a\(b\).md)
[angle](<docs/a b.md> "a title (with parentheses)")
[entity](docs/a&amp;b.md)
""")
        for name in ("a b.md", "hash#name.md", "what?.md", "a(b).md", "a&b.md"):
            self.write("docs/" + name, "# Hello world\n")
        self.assertEqual(self.errors(), [])
        self.write("README.md", "[bad](missing.md?file=docs/a%20b.md)\n[bad](docs/a%20b.md?raw=1#missing%2Dheading)\n[bad](missing%00.md)\n")
        errors = self.errors()
        self.assertEqual(len(errors), 3)
        self.assertIn("local target does not exist", errors[0])
        self.assertIn("#missing-heading", errors[1])

    def test_traversal_and_external_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "outside.md"
            external.write_text("# Outside\n", encoding="utf-8")
            self.write("README.md", "[outside](../outside.md)\n[encoded](%2e%2e/outside.md)\n")
            errors = self.errors()
            self.assertEqual(len(errors), 2)
            self.assertTrue(all("escapes repository" in e for e in errors))
            try:
                (self.root / "alias").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symbolic links unavailable")
            self.write("README.md", "[alias](alias/outside.md)\n")
            self.assertIn("escapes repository", self.errors()[0])

    def test_external_urls_are_not_fetched(self):
        self.write("README.md", """# Home
[web](https://example.invalid/absent#missing)
[mail](mailto:nobody@example.invalid)
[network](//example.invalid/file)
[custom](custom-scheme:resource)
""")
        result = check_repository(self.root)
        self.assertEqual(result.local_links, 0)
        self.assertEqual(result.errors, [])

    def test_unicode_formatted_and_setext_headings(self):
        self.write("README.md", """# Café: `Setup` & **Usage**
[accent](#caf%C3%A9-setup--usage)
[linked](#see-guide)
## See [guide](guide.md)
[emphasis](#emphasized-and-bold)
## _Emphasized_ and __bold__
[code](#_code_-and-foo_bar)
## `_code_` and foo_bar
[setext](#another-heading)

Another heading
---------------
""")
        self.write("guide.md", "# Guide\n")
        self.assertEqual(self.errors(), [])

    def test_balanced_link_destinations_and_multiline_setext_in_headings(self):
        self.write("README.md", """# [Guide](a(b).md)
[go](#guide)

First line
second line
===========
[go](#first-line-second-line)
""")
        self.write("a(b).md", "# Destination\n")
        self.assertEqual(self.errors(), [])

    def test_optional_titles_empty_destinations_and_friendly_cli_exit(self):
        self.write("README.md", "# Home\n[home]()\n[home](#home 'title')\n[home](#home (title))\n")
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self.assertIn("3 local links; 0 error(s)", output.getvalue())
        self.write("README.md", "# Home\n[broken](oops.md)\n")
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(["--root", str(self.root)]), 1)
        self.assertIn("README.md:2:", output.getvalue())

    def test_malformed_inline_target_is_a_diagnostic(self):
        self.write("README.md", "# Home\n[broken](<unterminated)\n")
        self.assertIn("malformed inline link destination", self.errors()[0])


if __name__ == "__main__":
    unittest.main()
