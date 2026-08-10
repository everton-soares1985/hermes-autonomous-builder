# Security and isolation

## Isolation strategy

The future builder receives an exclusive root, one isolated workspace and branch per project/run, and a service identity restricted to that root and approved repositories. Existing automation projects remain inaccessible or read-only. Writes resolve to absolute paths and are rejected when the final path escapes the active workspace, including through symlinks or traversal.

## Controls

- Path allowlist and denied sensitive-path patterns.
- Command allowlist with argument validation, timeout, output limit, and no interactive shell expansion by default.
- No access to job-automation credentials or existing Hermes memory.
- Per-project Git credentials with least privilege; no organization-wide token.
- Reversible commits; no automatic merge, force push, or public visibility.
- Resource limits for process count, CPU, memory, disk, and execution time.
- Network egress limited to approved providers and package sources during authorized phases.
- Secret scanning before commit and before push.

## Confidentiality classes

| Class | Example | Repository treatment |
|---|---|---|
| Public design | State machine, generic schemas | Allowed after review |
| Private sanitized | Detailed benchmark result without identity | Allowed in private repo; re-review before public release |
| Confidential | Account metadata, private route setup, internal host/path | Never commit |
| Secret | Key, cookie, token, OAuth/SSH material | Never store; rotate on exposure |

## Publication checklist

- [ ] Repository visibility is private unless separately authorized.
- [ ] No `.env`, key, cookie, token, OAuth artifact, email, account identity/count, private URL, chat ID, host, or credential appears.
- [ ] No raw internal audit or provider inventory is copied.
- [ ] Screenshots are real and visually inspected for metadata and notifications.
- [ ] Examples use abstract identities and synthetic hashes.
- [ ] Git history and staged diff pass secret and private-path scans.
- [ ] Required documentation and license are present.
- [ ] Tests and GrowthTech GitHub Publisher check pass.
- [ ] Public release, if ever requested, receives a fresh independent sanitization audit.

## Incident response

Stop publication, preserve a private incident record, rotate exposed credentials outside Git, remove sensitive history through an approved process, invalidate affected evidence, and repeat all gates. Never “fix” exposure only by deleting the current file while leaving the secret in history.
