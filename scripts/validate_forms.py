#!/usr/bin/env python3
"""Validate the issue and discussion forms before they reach every repo.

A broken form here breaks the new-issue page on every public repository that
inherits it, so this runs in CI on each push.
"""

from __future__ import annotations

import pathlib
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent

NEEDS_OPTIONS = {"dropdown", "checkboxes"}
NEEDS_LABEL = {"input", "textarea", "dropdown", "checkboxes"}
KNOWN_TYPES = {"markdown", "input", "textarea", "dropdown", "checkboxes"}

errors: list[str] = []


def fail(path: pathlib.Path, message: str) -> None:
    errors.append(f"{path.relative_to(REPO)}: {message}")


def check_form(path: pathlib.Path, *, is_issue_form: bool) -> None:
    try:
        form = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        fail(path, f"invalid YAML — {exc}")
        return

    if not isinstance(form, dict):
        fail(path, "top level must be a mapping")
        return

    if is_issue_form:
        for key in ("name", "description"):
            if not form.get(key):
                fail(path, f"missing required top-level key `{key}`")

    body = form.get("body")
    if not isinstance(body, list) or not body:
        fail(path, "`body` must be a non-empty list")
        return

    seen_ids: set[str] = set()
    for index, field in enumerate(body):
        where = f"body[{index}]"

        if not isinstance(field, dict):
            fail(path, f"{where} must be a mapping")
            continue

        kind = field.get("type")
        if kind not in KNOWN_TYPES:
            fail(path, f"{where} has unknown type {kind!r}")
            continue

        attributes = field.get("attributes")
        if not isinstance(attributes, dict):
            fail(path, f"{where} ({kind}) is missing `attributes`")
            continue

        if kind in NEEDS_LABEL and not attributes.get("label"):
            fail(path, f"{where} ({kind}) is missing `attributes.label`")

        if kind == "markdown" and not attributes.get("value"):
            fail(path, f"{where} (markdown) is missing `attributes.value`")

        if kind in NEEDS_OPTIONS:
            options = attributes.get("options")
            if not isinstance(options, list) or not options:
                fail(path, f"{where} ({kind}) needs a non-empty `options` list")
            elif kind == "checkboxes":
                for option in options:
                    if not isinstance(option, dict) or not option.get("label"):
                        fail(path, f"{where} (checkboxes) has an option without a label")

        # GitHub rejects `validations` on checkboxes.
        if kind == "checkboxes" and "validations" in field:
            fail(path, f"{where} (checkboxes) must not declare `validations`")

        field_id = field.get("id")
        if field_id is not None:
            if field_id in seen_ids:
                fail(path, f"{where} reuses id {field_id!r}")
            seen_ids.add(field_id)


def main() -> int:
    forms = sorted((REPO / "ISSUE_TEMPLATE").glob("*.yml"))
    discussions = sorted((REPO / "DISCUSSION_TEMPLATE").glob("*.yml"))

    for path in forms:
        if path.name == "config.yml":
            config = yaml.safe_load(path.read_text())
            if not isinstance(config, dict):
                fail(path, "top level must be a mapping")
                continue
            for link in config.get("contact_links") or []:
                missing = [k for k in ("name", "url", "about") if not link.get(k)]
                if missing:
                    fail(path, f"contact link {link.get('name')!r} missing {missing}")
            continue
        check_form(path, is_issue_form=True)

    for path in discussions:
        check_form(path, is_issue_form=False)

    checked = len(forms) + len(discussions)
    if errors:
        print(f"{len(errors)} problem(s) across {checked} file(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"All {checked} form file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
