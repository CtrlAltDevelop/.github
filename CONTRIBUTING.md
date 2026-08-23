# Contributing

Thanks for taking the time. These packages are extracted from production
brokerage and exchange apps, so the bar is "would I ship this to traders on a
Monday morning" — but that mostly means small, tested, documented changes, not
ceremony.

## Before you write code

- **Bugs** — open an issue first with a reproduction. A failing test is the best
  possible bug report.
- **Small fixes** (typos, a wrong doc comment, an obvious off-by-one) — just
  send the pull request, no issue needed.
- **New features or public API changes** — open an issue and let's agree on the
  shape first. Every public symbol becomes a compatibility promise, and I'd
  rather discuss it than reject a finished PR.

## Getting set up

```bash
git clone https://github.com/CtrlAltDevelop/<repo>.git
cd <repo>
dart pub get        # or: flutter pub get, for the Flutter packages
```

## Before you open the pull request

Run all four. CI runs the same ones, and a package that fails any of them can't
be published at full pub points.

```bash
dart format .
dart analyze --fatal-infos
dart test
dart pub publish --dry-run
```

Notes on the analyzer: the packages enable `strict-casts`, `strict-inference`
and `strict-raw-types`, plus `public_member_api_docs`. That last one means
**every new public member needs a doc comment** — the analyzer will tell you
which ones are missing.

## Commits

[Conventional Commits](https://www.conventionalcommits.org), lowercase subject,
no trailing period:

```
feat: add a paginated list bloc
fix: keep the last good data through an error state
docs: document the failure hierarchy
test: cover the mapper behaviour
chore: require dart 3.13
```

`feat:` and `fix:` are the ones that show up in a changelog, so pick them
deliberately.

## Pull requests

- One logical change per PR. Two unrelated fixes are two pull requests.
- Add tests for anything behavioural. Bug fixes get a test that fails before
  the fix.
- Update the `README.md` if you changed how something is used, and add a
  `CHANGELOG.md` entry under an `## Unreleased` heading.
- Don't bump the version in `pubspec.yaml` — I do that at release time.
- Keep the diff free of formatting churn in code you didn't otherwise touch.

## Breaking changes

Sometimes necessary, never casual. If a change breaks existing callers, say so
explicitly in the PR description and describe the migration in one or two
sentences. It'll land in a major version.

## Licensing

Everything here is MIT. By contributing you agree your work is released under
the same license.
