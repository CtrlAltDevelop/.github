# Security Policy

Several of these packages sit in the request path of financial applications —
token handling, API clients, error boundaries. Vulnerability reports are taken
seriously and are always welcome.

## Reporting a vulnerability

**Please don't open a public issue.** Use one of these instead:

1. **GitHub private vulnerability reporting** — go to the repository's
   **Security** tab → **Report a vulnerability**. This is the preferred route:
   it keeps the discussion attached to the repo and private until a fix ships.
2. **Email** — **me.CtrlAltDev@proton.me**, subject line starting with
   `SECURITY:`.

Helpful things to include:

- Which package and version, and the Dart or Flutter SDK you're on
- What an attacker can actually achieve — data disclosure, token leakage,
  bypassed validation
- A minimal reproduction, ideally a failing test or a short `main.dart`
- Any suggested fix, if you have one in mind

## What to expect

| Stage | Timing |
|---|---|
| Acknowledgement that I've read it | within 3 days |
| Initial assessment and severity | within 7 days |
| Fix released to pub.dev | as fast as the severity warrants |
| Public advisory and credit | after the fix is published |

I'll keep you updated while it's in progress, and I'm happy to credit you by
name or handle in the advisory and changelog — tell me which you prefer, or if
you'd rather stay anonymous.

Please give me a reasonable window to ship a fix before disclosing publicly.

## Supported versions

The latest published minor of each package on
[pub.dev](https://pub.dev) is supported. Fixes are released as a new patch
version rather than backported to older majors.

## Out of scope

- Vulnerabilities in Dart, Flutter, or third-party dependencies — report those
  upstream, though I'd still like to know so I can bump the constraint
- Findings that require an already-compromised device or a modified SDK
- Automated scanner output with no demonstrated impact

## Not covered here

This policy covers the open source packages. The production applications
(DeltaFX CRM, BTCB) are not open source — for anything concerning those, email
the address above and I'll route it to the right security team.
