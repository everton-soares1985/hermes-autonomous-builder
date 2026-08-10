# Multi-account operations

This document records an approved policy, not proof that controls are enabled on live accounts.

## Policy

- Use multi-account mode only where the provider and authorization permit it.
- Enable rate-limit protection for every configured account, including single-account routes.
- Rate-limit protection does not create quota; it prevents repeated calls to a limited account and enables cooldown or rotation.
- Use abstract identifiers such as `provider-account-a` in evidence visible to the project.
- Keep per-account proxy distribution only when real, stable proxies exist and their use is authorized.
- Distribution does not create different source IPs when accounts share the same upstream proxy.

## Balancing

Start with `least-used` to spread measured consumption. Evaluate `p2c` after sufficient latency and error observations. Avoid `fill-first` when the goal is balanced distribution and reduced concentration risk.

## Interface interpretation

- A grey key icon may still represent active per-account distribution; verify the tooltip or explicit state instead of inferring from color.
- A value such as `~18m` may describe OAuth token expiry, not remaining usage quota.
- `unprotected` means the rate-limit shield is disabled, not that the account has unlimited capacity.

## Required evidence before claiming activation

| Claim | Minimum evidence |
|---|---|
| Rate-limit protection enabled | Sanitized configuration observation plus controlled 429/cooldown test |
| Rotation working | Attempts showing abstract account change and preserved role context |
| Proxy distribution active | Sanitized explicit setting and approved network observation |
| Balancer effective | Sample window with selection counts, latency, and errors |
| Token refresh healthy | Expiry/refresh event with no credential value recorded |

No screenshot, log, or document may expose account identity, account count, token, cookie, proxy credential, or private endpoint.
