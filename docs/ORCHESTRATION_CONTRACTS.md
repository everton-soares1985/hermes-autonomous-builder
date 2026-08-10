# Orchestration contracts

## Contract layers

All inter-role exchanges use the shared [`handoff.schema.json`](../schemas/handoff.schema.json). The role-specific requirements below narrow that common envelope. Reviewer output also validates against [`review-verdict.schema.json`](../schemas/review-verdict.schema.json).

## Architect → Coder

Required semantic content:

- authorized goal, explicit non-goals, constraints, and allowed paths;
- small tasks with dependencies and verifiable acceptance criteria;
- approved commands or command classes;
- risk notes and minimum context digest;
- immutable plan artifact hash.

The Coder rejects the bundle when tasks are ambiguous, allowed paths are absent, context is incomplete, or requested work exceeds authorization.

## Coder → Reviewer

Required semantic content:

- tested Git SHA and diff summary;
- complete changed-file list;
- commands, exit codes, durations, and test counts;
- acceptance-criterion-to-evidence map;
- artifact hashes and append-only attempt history;
- pending, blocked, and known-failure items;
- effective model, provider, and actual route.

The Reviewer rejects a workspace whose SHA differs from the bundle or whose required evidence cannot be reproduced.

## Reviewer → Orchestrator

The verdict is one of `APPROVED`, `CHANGES_REQUESTED`, or `BLOCKED`. It names the reviewed SHA, independent reviewer identity at the model/route level, reproduced commands, criterion results, and findings with severity and reproduction evidence.

Approval is invalid when:

- reviewer and author are the same effective model for the run;
- a required command was skipped or failed;
- a critical/high finding is open;
- the tested SHA changed;
- an out-of-scope file changed;
- route or context identity is insufficient.

## Shared handoff fields

The minimum envelope includes `schema_version`, project/run/task/iteration identifiers, role transition, effective routing, goal and scope, tasks and dependencies, acceptance criteria, SHA and diff, commands and test counts, artifacts and hashes, status lists, append-only errors, context digest, and `min_context_ok`.

## Receiver algorithm

```text
validate schema
verify role transition is allowed
verify context digest and min_context_ok
verify workspace SHA equals handoff SHA
verify every changed path is allowlisted
verify required evidence hashes
if any check fails: reject and BLOCK
otherwise: accept and record immutable receipt
```

Errors are appended; they are never deleted or rewritten by a later attempt.
