#!/usr/bin/env python3
"""Check local Markdown navigation without network access or dependencies.

Supports inline/image and reference links, ATX/Setext headings, and duplicate
heading slugs. Fenced code, code spans and HTML comments are ignored. This is a
small documentation checker, not a complete CommonMark renderer: raw HTML/MDX
links and anchors, indented code and complex container blocks are not parsed.
Fragments are checked only for Markdown targets; external URLs are not checked.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import html
from pathlib import Path
import re
import string
import unicodedata
from urllib.parse import unquote, urlsplit


MARKDOWN = {".md", ".markdown"}
ESCAPE = re.compile(r"\\([" + re.escape(string.punctuation) + r"])")
REFERENCE = re.compile(r"^ {0,3}\[((?:\\.|[^\]\\])+)\]:[ \t]*(.*)$")


@dataclass(frozen=True)
class Diagnostic:
    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path.as_posix()}:{self.line}: {self.message}"


@dataclass
class Result:
    documents: int
    local_links: int
    errors: list[Diagnostic]


def _blank(text: str) -> str:
    return re.sub(r"[^\n]", " ", text)


def _escaped(text: str, index: int) -> bool:
    start = index
    while start and text[start - 1] == "\\":
        start -= 1
    return (index - start) % 2 == 1


def _without_blocks(text: str) -> str:
    lines = text.splitlines(keepends=True)
    visible_lines = _without_spans(text).splitlines(keepends=True)
    fence = None
    comment = False
    for index, line in enumerate(lines):
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}[ \t]*\n?", line):
                fence = None
            lines[index] = _blank(line)
        else:
            # Comments inside code do not hide subsequent prose, and fence-like
            # examples inside comments do not open real code blocks.
            position = 0
            while position < len(line):
                start = position if comment else visible_lines[index].find("<!--", position)
                if start < 0:
                    break
                end = line.find("-->", start + (0 if comment else 4))
                comment = end < 0
                end = len(line) if comment else end + 3
                line = line[:start] + _blank(line[start:end]) + line[end:]
                position = end
            lines[index] = line
            match = re.match(r" {0,3}(`{3,}|~{3,})([^\n]*)", line)
            if match and not (match[1][0] == "`" and "`" in match[2]):
                fence = match[1]
                lines[index] = _blank(line)
    return "".join(lines)


def _without_spans(text: str) -> str:
    runs = list(re.finditer(r"`+", text))
    result = list(text)
    index = 0
    while index < len(runs):
        start = runs[index]
        end_index = index + 1
        if not _escaped(text, start.start()):
            while end_index < len(runs) and runs[end_index][0] != start[0]:
                end_index += 1
            if end_index < len(runs):
                end = runs[end_index].end()
                result[start.start():end] = _blank(text[start.start():end])
                index = end_index
        index += 1
    return "".join(result)


def _target(text: str, index: int, inline: bool) -> tuple[str, int] | None:
    """Parse a destination and optional title; return the raw URL and end."""
    while index < len(text) and text[index].isspace():
        index += 1
    start = index
    if index < len(text) and text[index] == "<":
        start = index = index + 1
        while index < len(text) and (text[index] != ">" or _escaped(text, index)):
            if text[index] in "\n<":
                return None
            index += 1
        if index == len(text):
            return None
        destination = text[start:index]
        index += 1
    else:
        depth = 0
        while index < len(text):
            char = text[index]
            if char == "\\" and index + 1 < len(text) and text[index + 1] in string.punctuation:
                index += 2
                continue
            if char.isspace() or (char == ")" and depth == 0):
                break
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            elif char == "<":
                return None
            index += 1
        if depth or (index == start and not inline):
            return None
        destination = text[start:index]
    after_destination = index
    while index < len(text) and text[index].isspace():
        index += 1
    if index > after_destination and index < len(text) and text[index] in "\"'(":
        delimiter = ")" if text[index] == "(" else text[index]
        index += 1
        while index < len(text) and (text[index] != delimiter or _escaped(text, index)):
            index += 1
        if index == len(text):
            return None
        index += 1
        while index < len(text) and text[index].isspace():
            index += 1
    if inline:
        return (destination, index + 1) if index < len(text) and text[index] == ")" else None
    return (destination, index) if index == len(text) else None


def _label(text: str) -> str:
    return " ".join(ESCAPE.sub(r"\1", text).split()).casefold()


def _bracket_end(text: str, start: int) -> int | None:
    depth = 1
    for index in range(start + 1, len(text)):
        if _escaped(text, index):
            continue
        if text[index] == "[":
            depth += 1
        elif text[index] == "]":
            depth -= 1
            if not depth:
                return index
    return None


def _links(text: str):
    definitions = {}
    lines = text.splitlines(keepends=True)
    index = 0
    while index < len(lines):
        line = lines[index]
        match = REFERENCE.match(line.rstrip("\n"))
        if match:
            source, consumed = match[2], 1
            if not source.strip() and index + 1 < len(lines) and lines[index + 1].strip():
                source += "\n" + lines[index + 1].rstrip("\n")
                consumed += 1
            parsed = _target(source, 0, False)
            if parsed and index + consumed < len(lines):
                continuation = lines[index + consumed].strip()
                if continuation[:1] in {"\"", "'", "("}:
                    extended = _target(source + "\n" + continuation, 0, False)
                    if extended:
                        parsed = extended
                        consumed += 1
            if parsed is None:
                # A failed continuation is ordinary prose, and can contain
                # real links independently of this unused malformed definition.
                consumed = 1
            key = _label(match[1])
            if key not in definitions or definitions[key][0] is None:
                definitions[key] = (parsed, index + 1)
            for offset in range(consumed):
                lines[index + offset] = _blank(lines[index + offset])
            index += consumed
        else:
            index += 1
    text = _without_spans("".join(lines))
    index = 0
    while index < len(text):
        if text[index] != "[" or _escaped(text, index):
            index += 1
            continue
        close = _bracket_end(text, index)
        if close is None:
            index += 1
            continue
        label = text[index + 1:close]
        line = text.count("\n", 0, index) + 1
        end = close + 1
        if end < len(text) and text[end] == "(":
            parsed = _target(text, end + 1, True)
            if parsed:
                yield line, parsed[0], None
                end = parsed[1]
            else:
                yield line, None, "malformed inline link destination"
        else:
            explicit = end < len(text) and text[end] == "["
            if explicit:
                ref_end = _bracket_end(text, end)
                if ref_end is None:
                    index = end
                    continue
                label = text[end + 1:ref_end] or label
                end = ref_end + 1
            key = _label(label)
            if key in definitions:
                parsed, definition_line = definitions[key]
                if parsed:
                    yield line, parsed[0], None
                else:
                    yield line, None, f"reference {label!r} has a malformed definition at line {definition_line}"
            elif explicit:
                yield line, None, f"undefined reference {label!r}"
        index = end


def _display_links(text: str) -> str:
    """Keep link labels in heading text, consuming balanced URL destinations."""
    result = []
    index = 0
    while index < len(text):
        if text[index] == "[" and not _escaped(text, index):
            close = _bracket_end(text, index)
            if close is not None and close + 1 < len(text):
                after = close + 1
                end = None
                if text[after] == "(":
                    parsed = _target(text, after + 1, True)
                    if parsed:
                        end = parsed[1]
                elif text[after] == "[":
                    ref_end = _bracket_end(text, after)
                    if ref_end is not None:
                        end = ref_end + 1
                if end is not None:
                    result.append(_display_links(text[index + 1:close]))
                    index = end
                    continue
        result.append(text[index])
        index += 1
    return "".join(result)


def _anchors(text: str) -> set[str]:
    anchors = set()
    lines = text.splitlines()
    visible_lines = _without_spans(text).splitlines()
    for index, line in enumerate(lines):
        heading = re.match(r"^ {0,3}#{1,6}(?:[ \t]+(.*)|[ \t]*)$", line)
        if heading and re.match(r"^ {0,3}#", visible_lines[index]):
            title = re.sub(r"[ \t]+#+[ \t]*$", "", heading[1] or "")
        elif index + 1 < len(lines) and line.strip() and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", visible_lines[index + 1]):
            start = index
            while start and lines[start - 1].strip():
                previous = lines[start - 1]
                if REFERENCE.match(previous) or re.match(r"^ {0,3}(?:#{1,6}(?:\s|$)|[-=]+\s*$|>|[-+*]\s|\d+[.)]\s)", previous):
                    break
                start -= 1
            title = " ".join(part.strip() for part in lines[start:index + 1])
        else:
            continue
        # Heading slugs retain displayed code/link text, not Markdown markup.
        code = []
        def protect_code(match):
            code.append(match[2])
            return f"\x00{len(code) - 1}\x00"
        title = re.sub(r"(`+)(.+?)\1(?!`)", protect_code, title)
        title = _display_links(title)
        title = re.sub(r"<[^>]*>", "", title)
        title = re.sub(r"(\*\*|__)(.+?)\1", r"\2", title)
        title = re.sub(r"(?<!\w)([*_])(?=\S)(.+?)(?<=\S)\1(?!\w)", r"\2", title)
        title = re.sub(r"\x00(\d+)\x00", lambda m: code[int(m[1])], title)
        title = html.unescape(ESCAPE.sub(r"\1", title)).lower().strip()
        slug = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LMN").replace(" ", "-")
        candidate, suffix = slug, 0
        while candidate in anchors:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        anchors.add(candidate)
    return anchors


def check_repository(root: Path) -> Result:
    root = root.resolve()
    errors: list[Diagnostic] = []
    documents = {}
    for path in sorted(root.rglob("*")):
        if ".git" in path.relative_to(root).parts or path.suffix.lower() not in MARKDOWN:
            continue
        try:
            resolved = path.resolve()
            resolved.relative_to(root)
            if path.is_file():
                documents[path] = _without_blocks(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, RuntimeError) as exc:
            errors.append(Diagnostic(path.relative_to(root), 1, f"cannot read Markdown inside repository: {exc}"))
    anchors = {path.resolve(): _anchors(text) for path, text in documents.items()}
    local_links = 0
    for path, text in documents.items():
        for line, destination, error in _links(text):
            if error:
                errors.append(Diagnostic(path.relative_to(root), line, error))
                continue
            try:
                url = urlsplit(html.unescape(ESCAPE.sub(r"\1", destination)))
                if url.scheme or url.netloc:
                    continue
                local_links += 1
                target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
                try:
                    target.relative_to(root)
                except ValueError:
                    raise ValueError("local target escapes repository") from None
                if not target.exists():
                    raise ValueError("local target does not exist")
                fragment = unquote(url.fragment)
                if fragment and target in anchors and fragment not in anchors[target]:
                    raise ValueError(f"heading fragment #{fragment} does not exist")
            except (OSError, ValueError, RuntimeError) as exc:
                errors.append(Diagnostic(path.relative_to(root), line, f"{destination!r}: {exc}"))
    return Result(len(documents), local_links, errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error("--root must be an existing directory")
    result = check_repository(args.root)
    for error in result.errors:
        print(error)
    print(f"Checked {result.documents} Markdown files and {result.local_links} local links; {len(result.errors)} error(s). External URLs were not checked.")
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
