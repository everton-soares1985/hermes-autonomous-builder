# Evidence and gates

## Evidence before review

| Gate | Required proof |
|---|---|
| Build | Command, exit code, duration, and artifact hash when applicable |
| Tests | Real command, passed/failed/skipped counts, exit code |
| Scope | Git diff plus complete changed-file list matched to allowed paths |
| Repository | Branch, commit SHA, and clean state or explicit justified residue |
| Acceptance | One evidence reference for every criterion |
| Routing | Effective role, model, provider, route, attempt, and latency |
| Recovery | Append-only errors and correction-attempt count |

## Gate before `DONE`

The orchestrator requires reviewer independence, approval for the exact tested SHA, zero open critical/high findings, zero skipped mandatory tests, zero out-of-scope files, and reversible branch/commit identity. A natural-language statement such as “it works” has no evidentiary value by itself.

## Evidence model

Artifacts are content-addressed with SHA-256 and referenced by stable identifiers. Commands are captured as structured records. Sensitive output is redacted before storage, and redaction itself is recorded. Evidence is append-only per run.

## Acceptance mapping example

```json
{
  "criterion_id": "AC-05",
  "status": "passed",
  "evidence_refs": ["command:test-suite", "artifact:test-report"],
  "git_sha": "0123456789abcdef0123456789abcdef01234567"
}
```

## Failure semantics

- Required test failure: `CHANGES_REQUESTED` or `FAILED`, never partial success.
- Missing test/tool/context/authorization: `BLOCKED`.
- Infrastructure transient: retry within policy, then `BLOCKED` with evidence.
- Two unsuccessful automatic corrections: stop edits and escalate.
- Mutation after approval: invalidate verdict and re-enter `REVIEWING`.

## Test plan

1. Happy-path command execution with exact exit-code capture.
2. Test runner that reports zero tests while exiting zero; gate must reject it.
3. One failed test hidden among passed tests; gate must reject it.
4. Dirty file outside allowed paths; scope gate must reject it.
5. Artifact modified after hashing; integrity gate must reject it.
6. Reviewer approval on an older SHA; final gate must reject it.
7. Same-model author/reviewer; independence gate must reject it.
