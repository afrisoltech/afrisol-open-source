# Release and Security Acceptance

## Before merging
1. Confirm the change is original or properly licensed, and contains no secrets, customer information or proprietary APOS material.
2. Review dependencies, permissions, code paths, documentation and relevant threat scenarios.
3. Run exact-commit tests and review CI results; do not equate a workflow file with a passing workflow.
4. Obtain the repository's required reviews and branch-protection checks.

## Before publishing a package
1. Verify licence, version, changelog, supported runtime and reproducible build.
2. Run package tests, dependency vulnerability checks and source-content inspection.
3. Create a release tag and verify artefact provenance.
4. Announce only tested capabilities; do not imply production readiness without operational evidence.

## Security incidents
Use the private reporting route in [SECURITY.md](../SECURITY.md). Coordinate fixes and advisories without exposing customer environments.
