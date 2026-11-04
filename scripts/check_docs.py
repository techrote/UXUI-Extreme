#!/usr/bin/env python3
"""Offline Markdown link/anchor checks for UXUI-Extreme (stdlib only).

Checks local links and headings; external GitHub/module URLs are *not*
asserted live. Cross-repository state requires the source checks in the audit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?\\[[^\\]\n]*\\]\\(([^)\n]+)\\)")
FENCE = re.compile(r"^\\s*(`{3,}|~{3,})")
HEADING = re.compile(r"^\\s{0,3}(#{1,6})\\s+(.+?)\\s*#*\\s*$")
INLINE_CODE = re.compile(r"`+[^`\n]*`+")


def visible_lines(markdown: str):
    """Yield line numbers/text excluding fenced code; preserve source lines."""
    fence_char = None
    fence_length = 0
    for number, line in enumerate(markdown.splitlines(), start=1):
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char, fence_length = marker[0], len(marker)
                continue
            if marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = None
            continue
        if fence_char is None:
            yield number, INLINE_CODE.sub("", line)


def heading_anchors(markdown: str) -> set[str]:
    """Approximate GitHub's slugging for normal ATX headings, including repeats."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for _, line in visible_lines(markdown):
        match = HEADING.match(line)
        if not match:
            continue
        label = re.sub(r"!?\\[([^]]+)\\]\\([^)]+\\)", r"\\1", match.group(2))
        label = re.sub(r"<[^>]+>", "", label).casefold()
        slug = re.sub(r"[^\\w\\- ]", "", label).replace(" ", "-")
        if not slug:
            continue
        suffix = counts.get(slug, 0)
        counts[slug] = suffix + 1
        anchors.add(f"{slug}-{suffix}" if suffix else slug)
    return anchors


def check_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    documents = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    for source in documents:
        markdown = source.read_text(encoding="utf-8")
        for line_no, line in visible_lines(markdown):
            for match in LINK.finditer(line):
                dest = match.group(1).strip().split(" ", 1)[0].strip("<>")
                url = urlsplit(dest)
                if url.scheme or url.netloc:
                    continue  # External links are checked against live sources manually.
                path = unquote(url.path)
                if path.startswith("/") or path.startswith("\\"):
                    errors.append(f"{source.relative_to(root)}:{line_no}: absolute local link: {dest}")
                    continue
                target = (source.parent / path).resolve() if path else source
                if not target.is_relative_to(root):
                    errors.append(f"{source.relative_to(root)}:{line_no}: escapes repository: {dest}")
                elif not target.exists():
                    errors.append(f"{source.relative_to(root)}:{line_no}: missing local target: {dest}")
                elif url.fragment and target.is_file() and target.suffix.lower() == ".md":
                    anchor = unquote(url.fragment).casefold()
                    if anchor not in heading_anchors(target.read_text(encoding="utf-8")):
                        errors.append(f"{source.relative_to(root)}:{line_no}: missing heading: {dest}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_repository(root)
    if errors:
        print("Documentation quality checks failed:", file=sys.stderr)
        for error in errors:
            print("  " + error, file=sys.stderr)
        return 1
    print("Documentation quality checks passed (local files and heading anchors).")
    print("External URLs, CI claims and owner acceptance require separate verification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
