#!/usr/bin/env python3
"""Compatibility entry point for the shared offline documentation checker.

The implementation lives in tools/check_docs.py. Keep the original list[str]
diagnostic API and heading helper for existing callers, without a second parser.
"""

from __future__ import annotations

from pathlib import Path
import sys

# Direct execution sets sys.path[0] to scripts/, even from another directory.
# Import by package name so this wrapper cannot accidentally import itself.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import check_docs as _checker


def check_repository(root: Path) -> list[str]:
    """Return the shared checker's diagnostics in the original string format."""
    return [str(error) for error in _checker.check_repository(root).errors]


def heading_anchors(markdown: str) -> set[str]:
    """Use the shared heading parser, including its fenced-code exclusion."""
    return _checker._anchors(_checker._without_blocks(markdown))


def main(argv: list[str] | None = None) -> int:
    return _checker.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
