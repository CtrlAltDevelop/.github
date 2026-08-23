# .github

Default community health files for every public repository under
[@CtrlAltDevelop](https://github.com/CtrlAltDevelop).

GitHub reads the files in this repository whenever one of my public repos does
**not** provide its own copy. Adding a file here means it applies everywhere at
once; adding the same file to an individual repo overrides this one for that
repo.

## What lives here

| File | Applies to |
|---|---|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Shown when someone opens an issue or pull request |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Linked from the repo's community profile |
| [`GOVERNANCE.md`](GOVERNANCE.md) | How decisions, releases and hand-over work |
| [`SECURITY.md`](SECURITY.md) | Shown under the repo's **Security** tab |
| [`SUPPORT.md`](SUPPORT.md) | Linked from the new-issue page |
| [`FUNDING.yml`](FUNDING.yml) | Renders the **Sponsor** button |
| [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE) | Issue forms and the new-issue chooser |
| [`DISCUSSION_TEMPLATE/`](DISCUSSION_TEMPLATE) | Forms for repos with Discussions enabled |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Prefills the pull request body |

That is every file type GitHub supports as a default community health file.

## One rule when editing

The inherited files render **in the context of the repository that inherits
them**, not this one. A relative link like `[SECURITY.md](SECURITY.md)` would
resolve against `verdict` or `ohlcv_chart` and 404, so every link in an
inherited file must be an absolute URL. `README.md` is exempt — it is not
inherited.

[`scripts/check_links.py`](scripts/check_links.py) enforces that, and
[`scripts/validate_forms.py`](scripts/validate_forms.py) checks the issue and
discussion forms parse and satisfy GitHub's schema. Both run in CI on every
push, because a malformed form here breaks the new-issue page on every repo
that inherits it.

```bash
python3 scripts/validate_forms.py && python3 scripts/check_links.py
```

## What does *not* inherit

These have to live in each repository individually — putting them here does
nothing:

- `LICENSE`
- `CODEOWNERS`
- `.github/workflows/` — Actions never run from this repo on another repo's behalf
- `README.md`

Inheritance also only reaches **public** repositories. Private and internal
repos need their own copies.

## Not the profile README

My profile README is a separate repository,
[CtrlAltDevelop/CtrlAltDevelop](https://github.com/CtrlAltDevelop/CtrlAltDevelop).
The `profile/README.md` convention is for organization accounts only and has no
effect here.
