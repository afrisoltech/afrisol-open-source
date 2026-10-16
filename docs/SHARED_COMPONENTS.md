# Shared-component programme

Afrisol maintains public, independently usable components. APOS can consume tested releases through private dependency-update PRs. Public contributions never confer access to APOS, customer systems or supplier accounts.

## Initial component and next candidates

| Component | State | Acceptance |
| --- | --- | --- |
| Python localization helpers | Released v0.1.0; initial downstream governance-check integration proposed | Normalization, malformed input, supported-language fallback and compatibility tests |
| Accessibility checks and reusable interface primitives | Proposal only | Independent fixtures, keyboard/semantic/contrast checks and documented limits |
| Low-bandwidth delivery utilities | Proposal only | Reproducible payload and retry tests; no customer telemetry |

The Python utility is a validation dependency for APOS's locale policy, not a Python service in PHP request handling. APOS may extend its own language coverage; public updates must not narrow it.

## Public → private

The downstream repository polls published, non-prerelease versions. It resolves an annotated tag to a full commit, reads an explicit public-path allowlist at that commit and records hashes and MIT attribution. It opens a private PR with changed source and a lockfile. Read-only PR CI verifies hashes, component behavior and APOS compatibility. A maintainer reviews, approves and merges through the existing branch rules. Existing APOS release gates remain authoritative for deployment. Reverting the lock and vendor snapshot restores the prior version.

## Private → public

Changes to the downstream vendor snapshot generate a **private** upstream-review bundle. That bundle contains only allowlisted public component files and a patch against the hash-verified public baseline. It contains no APOS repository metadata or whole-tree export. Automated path/secret checks are aids, not proof of safe disclosure.

A maintainer must review redistribution rights, provenance, synthetic tests and confidential material before opening a public PR. Never publish a private issue, log, diff or archive wholesale. Security findings use private vulnerability reporting first. There is intentionally no cross-repository write token and no unattended publication.

## Contributor journey

1. Choose an open task or discuss a component in Ideas; use Q&A for help and Welcome for introductions.
2. Reproduce with synthetic fixtures; keep dependencies small and document behavior and limits.
3. Submit source, tests and docs under the repository license. Complete the disclosure checklist.
4. Maintainers review security, licensing, correctness, compatibility and relevance before acceptance.
5. Accepted changes enter a versioned release; downstream update automation proposes adoption.

Ubunifu, universities, TVETs and developer communities can participate through these same public channels. No partnership, student assignment, invitation or contribution volume is assumed.

## Ownership and measurements

CODEOWNERS names the current repository maintainer. Add maintainers through separately reviewed access changes; do not invent staff assignments. Track time to first response, accepted contributions, component defects, release adoption and downstream regressions in public issues with aggregate data only. Sponsorship does not buy approval or private access.

## Release contract

Use semantic version tags and the existing release policy. Publish annotated tags on tested commits; attach release notes describing changed behavior and compatibility. No PyPI publishing is implied. The machine-readable `shared-components.json` declares the initial component's public source allowlist; adding files or dependencies requires explicit downstream review.
