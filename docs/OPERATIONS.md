# Operations

This runbook is a planned contract. It does not indicate that the builder or any live route has been activated.

## Sequential run

1. Validate authorization, repository, allowed paths, and clean baseline.
2. Create run ID, isolated workspace, branch, evidence ledger, and context digest.
3. Enter `PLANNING`; request an Architect bundle.
4. Validate the bundle and enter `PLAN_READY`.
5. Enter `IMPLEMENTING`; the Coder performs scoped changes.
6. Enter `TESTING`; record all commands and deterministic gates.
7. Freeze the tested SHA and enter `REVIEWING` with independent context.
8. On reproducible findings, enter `CHANGES_REQUESTED`; invalidate prior approval.
9. On valid same-SHA approval, enter `APPROVED`; only then may Hermes emit `DONE`.

## Recovery matrix

| Event | Expected behavior | Result |
|---|---|---|
| Primary route timeout/empty response | Record attempt; use allowed in-role fallback with full context | Continue or `BLOCKED` |
| Rate limit | Apply cooldown/eligible rotation; no tight retry loop | Continue or `BLOCKED` |
| Quota exhausted | Preserve state and evidence; await quota or authorized route | `BLOCKED` |
| Context digest mismatch | Reject handoff; do not reconstruct by guessing | `BLOCKED` |
| Process crash | Reload durable state and verify workspace/SHA before resuming | Same state or `BLOCKED` |
| Test failure | Allow scoped correction, maximum two attempts | Retry or escalate |
| Reviewer route unavailable | Use independent in-role fallback | Review or `BLOCKED` |
| Post-review mutation | Invalidate verdict and rerun review | `REVIEWING` |

## Operational telemetry

Record timestamps, state transitions, effective route, abstract account, latency, attempt reason, command result, test counts, artifact hashes, token/rate-limit signals when available, and final disposition. Never log credential values or raw environment output.

## Validation scenarios before activation

- Real file read/patch/terminal/test/diff loop for the Coder route.
- Architect multi-turn continuity and truncated-response fallback.
- Reviewer reproduction against exact SHA with a seeded defect.
- 429, timeout, empty/malformed output, quota exhaustion, and provider recovery.
- Crash between patch and test, between test and review, and after approval.
- Path traversal, symlink escape, unapproved command, and secret-output redaction.
