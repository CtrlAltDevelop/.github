# Governance

Short version: one maintainer, MIT license, no committee.

This document exists so you can judge the risk of depending on these packages
without having to guess.

## Who decides

I do — [@CtrlAltDevelop](https://github.com/CtrlAltDevelop) (Mohammad Zarif). I
review every pull request, cut every release, and have the final say on scope.
There's no voting and no core team.

That means:

- Design disagreements end with my call, and I'll explain the reasoning.
- "No" to a feature isn't a judgement on the idea — it's usually about scope
  or the cost of maintaining another public API forever.
- Review latency is measured in days, not hours. These are maintained around a
  full-time job.

## Scope

Each package does one thing that was worth extracting from a production
brokerage or exchange app. Additions have to justify themselves against that
bar: something I'd actually ship, not something that's merely possible.

Anything a consumer can build in twenty lines on top of the package usually
belongs in the consumer, not here.

## Releases and versioning

- [Semantic versioning](https://semver.org), enforced honestly. A breaking
  change gets a major bump even when it's inconvenient.
- Releases go to [pub.dev](https://pub.dev) with a `CHANGELOG.md` entry per
  version.
- Fixes land on the latest version. Older majors aren't backported.
- No deprecation-free removals: anything going away is deprecated for at least
  one minor release first, with the replacement named in the deprecation
  message.

## Becoming a contributor

Send good pull requests. That's the whole path. If someone contributes
consistently and their judgement matches the direction of a package, I'll offer
commit access — but that's earned over time, not requested.

See [CONTRIBUTING.md](https://github.com/CtrlAltDevelop/.github/blob/main/CONTRIBUTING.md).

## If I stop maintaining a package

Single-maintainer projects carry bus-factor risk and it's fair to want an
answer up front:

- A package that's finished rather than abandoned will say so in its README.
  Low commit activity on a small, stable package is often the correct steady
  state, not neglect.
- If I genuinely step away, I'll mark the package as discontinued on pub.dev
  and say so in the README, rather than leaving it ambiguous.
- If someone credible wants to take one over, I'd rather transfer it than let
  it rot. Email **me.CtrlAltDev@proton.me**.
- Everything is MIT with a public repo. Forking is always available and never
  requires my permission.
