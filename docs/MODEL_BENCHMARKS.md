# Model benchmarks

## Evidence vocabulary

| Status | Meaning |
|---|---|
| `CATALOG_ONLY` | Listed but not exposed or selected for real inference |
| `RUNTIME_AVAILABLE` | Exposed at runtime without sufficient benchmark evidence |
| `RUNTIME_VALIDATED` | Useful real inference recorded |
| `PARTIAL` | Useful behavior with truncation, timeout, rate limit, or instability |
| `REJECTED` | Unsuitable for V0 quality, stability, quota, or operational reasons |

Catalog presence or a green dashboard indicator is not autonomous-agent evidence.

## Sanitized findings

| Candidate | Sanitized finding | V0 decision |
|---|---|---|
| Grok 4.5 via Grok Build | Strong code, architecture, audit, and multi-turn behavior; some severity and length overreach | Reviewer primary; preserve for high-value review |
| Claude Sonnet 4.6 via Antigravity | Strong bounded planning and correct refusal to invent missing prior context; one transport truncation observed | Architect primary with immediate fallback |
| GLM-5.2 via NVIDIA NIM | Stable useful inference and strong general quality in observed tests | Coder primary; Architect fallback |
| Kimi 2.6 Web | Good code quality when responsive, but Web transport instability | Outside operational V0 |
| Smaller Qwen coding route | Available and code-focused, but insufficient confidence as sole autonomous executor | Outside operational V0 |
| Claude Sonnet 4.5 route tested | Missed a critical persistence issue and proposed an unsafe correction in a queue benchmark | Rejected for primary V0 roles |
| High-cost premium route tested | Strong architecture but unsustainable quota consumption | Provider path rejected for automation |

Exact account information, raw prompts, private inventory, credential metadata, and internal paths are intentionally excluded.

## What is not yet proven

- Tool calling through Hermes for any V0 role.
- Stable multi-turn implementation for the Architect primary route.
- Coder file/terminal/test/correction loop.
- Reviewer independence and SHA-bound reproduction.
- Sustainable quota and renewal behavior for high-value review.
- Live multi-account protection, rotation, and proxy distribution.

These gaps are activation blockers, not minor documentation tasks.
