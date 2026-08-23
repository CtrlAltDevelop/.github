#!/usr/bin/env python3
"""Guard against relative links in the files other repositories inherit.

These files are rendered in the context of the *consuming* repository, so a
relative link like `[SECURITY.md](SECURITY.md)` resolves against that repo and
404s. Inherited files must use absolute URLs.
"""

from __future__ import annotations

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

# README.md is not inherited, so its relative links are fine.
INHERITED = [
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "SUPPORT.md",
    "PULL_REQUEST_TEMPLATE.md",
]

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ABSOLUTE = ("http://", "https://", "mailto:", "#")

errors: list[str] = []

for name in INHERITED:
    path = REPO / name
    if not path.exists():
        continue
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        for target in LINK.findall(line):
            if not target.startswith(ABSOLUTE):
                errors.append(f"{name}:{number}: relative link `{target}`")

if errors:
    print(f"{len(errors)} relative link(s) in inherited files:\n")
    for error in errors:
        print(f"  - {error}")
    print("\nInherited files render on other repos — use absolute URLs.")
    sys.exit(1)

print(f"No relative links in {len(INHERITED)} inherited file(s).")
