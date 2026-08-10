# Roadmap

## Phase 0 — Documentation baseline

- Define architecture, routing, contracts, evidence, isolation, operations, and risks.
- Create machine-readable schemas and publication checks.
- Publish privately with no runtime code or infrastructure mutation.

**Exit:** Publisher gate passes, confidentiality test passes, private visibility verified.

## Phase 1 — Offline contract harness

- Validate schemas, state transitions, append-only evidence, path policy, and same-SHA gates using synthetic fixtures.
- No provider or production infrastructure access.

**Authorization required:** executable implementation work.

## Phase 2 — Isolated tool-calling benchmark

- Exercise Architect, Coder, and Reviewer in disposable repositories.
- Test read, patch, terminal, test, correction, diff, fallback, quota, and recovery.

**Authorization required:** provider calls, credentials, and isolated environment.

## Phase 3 — Non-production integration

- Create a second logical Hermes profile and role combos without touching current automations.
- Enforce filesystem, command, network, resource, and GitHub boundaries.

**Authorization required:** Hermes/OmniRoute configuration and service changes.

## Phase 4 — Controlled pilot

- Run a small authorized project with manual approval gates.
- Measure route quality, quota, false-success prevention, and recovery.

**Authorization required:** pilot repository and bounded spend/usage.

## Phase 5 — Publication review

- Produce real screenshots and sanitized results.
- Re-audit the full Git history and documentation before considering public visibility.

**Authorization required:** public publication.

## Risks and pending decisions

| Risk or pending item | Impact | Mitigation / evidence needed | Status |
|---|---|---|---|
| Coder tool calling unproven | Cannot implement reliably | Real isolated file/terminal/test loop | Blocking |
| Architect transport truncation | Incomplete plans | Multi-turn retest and fallback completeness | Blocking |
| Reviewer SHA workflow unproven | False approval possible | Seeded-defect review on immutable SHA | Blocking |
| Reviewer quota unknown | Review unavailable mid-run | Measure renewal and reserve calls | Blocking |
| Multi-account shields not visually confirmed | Retry storm or concentration | Sanitized observation plus controlled 429 | Pending |
| Route metadata may be absent | Weak attribution | Require OmniRoute metadata or block | Pending |
| Context loss during fallback | Incorrect continuation | Digest, minimum bundle, rejection test | Blocking |
| Workspace escape | Existing projects at risk | Path resolution, symlink, and denylist tests | Blocking |
| Crash duplicates side effects | Repository corruption | Durable state and idempotent recovery test | Blocking |
| Public release leaks private history | Confidentiality loss | Fresh history-wide audit and explicit approval | Deferred |

## Branch and commit strategy

- `main` is protected and represents reviewed documentation.
- Use short-lived `docs/*`, `test/*`, and later `feat/*` branches.
- One scoped concern per Conventional Commit.
- Tag documentation baseline as `v0.1.0` only after private verification.
- No force pushes, automatic merges, or public releases in V0.
- Implementation pilots use isolated repositories or workspaces; they do not share existing automation repositories.
