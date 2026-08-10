# Model routing

## Principle

One combo represents one role. Hermes selects the role; OmniRoute selects an allowed route within that role. A fallback is a transport or availability decision, never a promotion into another role.

## V0 combinations

| Combo | Preferred route | Normal fallback | Evidence status |
|---|---|---|---|
| `builder-architect` | Claude Sonnet 4.6 via Antigravity | GLM-5.2 via NVIDIA NIM | Architecture quality accepted; real Hermes tool calling pending |
| `builder-coder` | GLM-5.2 via NVIDIA NIM | None | Runtime conversation validated; real file/tool loop pending |
| `builder-reviewer` | Grok 4.5 via Grok Build | Claude Sonnet 4.6 via Antigravity | Review quality accepted; SHA-bound review pending |

Kimi Web and smaller Qwen coding routes are outside V0 because observed transport stability or confidence was insufficient. GLM-5.2 cannot review a run it authored. If another model implements in a future version, GLM-5.2 may become eligible only after the independence policy is evaluated for that run.

## Route record

Every attempt records:

- role and combo;
- requested and effective model;
- provider and actual route identifier;
- abstract account reference, never account identity;
- run, task, iteration, and attempt identifiers;
- start/end timestamps and latency;
- result class, rate-limit signal, and fallback reason;
- Git SHA and context digest.

Routing metadata supplied by OmniRoute is preferred over inference from response text. Unknown effective route means evidence is incomplete and the workflow blocks when route identity is required.

## Eligibility rules

1. `CATALOG_ONLY` is not runnable evidence.
2. `RUNTIME_AVAILABLE` is not enough for autonomous use.
3. `RUNTIME_VALIDATED` requires a useful real inference, but tool execution still needs separate proof.
4. `PARTIAL` requires fallback protection and retesting.
5. A route with unknown sustainable quota is reserved for high-value calls.
6. A model cannot approve work it authored in the same run.
7. Missing minimum context returns `CONTEXT_INSUFFICIENT`; the fallback must not guess.

## Planned route tests

- Multi-turn continuity with an earlier artifact dependency.
- Structured JSON matching the handoff schema.
- File read, patch, terminal command, test execution, correction, and diff.
- Primary timeout, 429, empty response, malformed response, and fallback recovery.
- Reviewer verdict tied to immutable SHA and independent context.
