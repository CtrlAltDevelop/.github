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
| [`SECURITY.md`](SECURITY.md) | Shown under the repo's **Security** tab |
| [`SUPPORT.md`](SUPPORT.md) | Linked from the new-issue page |
| [`FUNDING.yml`](FUNDING.yml) | Renders the **Sponsor** button |
| [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE) | Issue forms and the new-issue chooser |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Prefills the pull request body |

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
