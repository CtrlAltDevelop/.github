## What this changes

<!-- One or two sentences. What behaviour is different after this PR? -->

## Why

<!-- The problem being solved. Link the issue: Fixes #123 -->

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation
- [ ] Tests
- [ ] Chore / tooling

## Checks

```bash
dart format .
dart analyze --fatal-infos
dart test
dart pub publish --dry-run
```

- [ ] `dart format .` leaves no changes
- [ ] `dart analyze --fatal-infos` is clean
- [ ] `dart test` passes
- [ ] New public members have doc comments (`public_member_api_docs`)
- [ ] Tests added — a bug fix has a test that failed before the fix
- [ ] `CHANGELOG.md` updated under `## Unreleased`
- [ ] `README.md` updated if usage changed
- [ ] Version in `pubspec.yaml` left alone — bumped at release time

## Breaking changes

<!-- Delete this section if nothing breaks. Otherwise: what breaks, and how
     does a caller migrate? Two sentences is usually enough. -->

## Anything the reviewer should know

<!-- Trade-offs you weighed, alternatives you rejected, parts you're unsure
     about. Optional. -->
