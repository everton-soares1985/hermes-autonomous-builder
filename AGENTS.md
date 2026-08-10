# Agent instructions

## Scope

This repository is the sanitized documentation and portfolio baseline for Hermes Autonomous Builder V0. Do not add executable builder code, provider credentials, live configuration, or infrastructure mutations without explicit, separate authorization.

## Non-negotiable rules

- Preserve the Architect → Coder → independent Reviewer separation.
- Hermes changes roles; OmniRoute only routes within the current role.
- A model cannot approve work it authored in the same run.
- Only the orchestrator may emit `DONE`, and only for the exact tested and approved SHA.
- Missing context, route, quota, authorization, tool, or required test produces `BLOCKED`.
- Limit automatic repair to two attempts per task in V0.
- Keep errors append-only and evidence content-addressed.
- Never publish secrets, account identities or counts, private paths, endpoints, or raw audits.
- Consult `PROJECT_MAP.md` before creating a new file to prevent duplication.

## Publication protocol

Before every push, run the GrowthTech GitHub Publisher audit/check and repository tests. A failed check blocks commit publication. Keep the repository private unless the user separately authorizes public visibility after a new sanitization audit.

## Language

Use English for canonical documentation. Keep the Portuguese README as a short digest.
