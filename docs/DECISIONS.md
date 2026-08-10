# Decision log

## ADR-001 — One orchestrator, three roles

**Status:** accepted for V0. Hermes owns state transitions; Architect, Coder, and Reviewer receive isolated role contexts. Three separate Hermes installations were rejected as unnecessary complexity.

## ADR-002 — OmniRoute fallback stays inside a role

**Status:** accepted. A provider fallback cannot silently become a Coder, Reviewer, or Architect transition. This keeps responsibilities and evidence attributable.

## ADR-003 — Independent reviewer and exact SHA

**Status:** accepted. The effective author model cannot approve the same run. Review approval is bound to the tested SHA and invalidated by any later code change.

## ADR-004 — Sequential V0

**Status:** accepted. Parallel execution, automatic merge, and public publication are deferred until the basic cycle is reliable.

## ADR-005 — Markdown and schemas as operational memory

**Status:** accepted. V0 uses a specification-first Markdown record and JSON schemas. External memory layers and additional skill systems remain backlog items.

## ADR-006 — Private-first portfolio repository

**Status:** accepted. Documentation is sanitized from creation, the initial repository remains private, and any future public release requires a fresh audit. Raw internal research is not copied.

## ADR-007 — Model allocation

**Status:** accepted pending tool validation. Sonnet 4.6 is Architect primary, GLM-5.2 is Coder primary and Architect fallback, Grok 4.5 is Reviewer primary, and Sonnet 4.6 is Reviewer fallback. GLM-5.2 may not review its own V0 implementation.
