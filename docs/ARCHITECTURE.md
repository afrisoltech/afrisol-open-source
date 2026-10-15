# Public Open Source Architecture

## Scope
This repository is a community-facing home for independently developed libraries, examples, documentation and reusable components. It is not the Afrisol Platform Operating System (APOS) source tree or a deployment channel for customer environments.

## Proposed layout
- `src/`: small, independently authored packages with explicit licences and tests
- `tests/`: deterministic unit and integration tests using synthetic fixtures only
- `examples/`: educational, low-cost examples with no production credentials
- `docs/`: design decisions, accessibility and developer documentation
- `.github/`: community templates, funding configuration and CI

## Engineering principles
- Mobile-first, low-bandwidth and offline-tolerant design where appropriate
- Accessible documentation and interfaces; localization without assuming one language or currency across Africa
- Minimal dependencies, reproducible tests, explicit versions and supply-chain checks
- No direct coupling to proprietary APOS services, private provider APIs or customer systems
- Security by default, least-privilege workflows and no secrets in source control

## Publication gates
Require maintainer review, licence compatibility, secret scanning, passing relevant CI and clear scope boundaries before merging. Publishing to package registries or external cloud infrastructure requires separate authorization and verifiable release provenance.
