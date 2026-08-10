# Security policy

## Supported scope

The current V0 is a documentation artifact. Security reports should cover accidental disclosure, unsafe contracts, scope-escape paths, evidence bypasses, or publication risks.

## Reporting

Report vulnerabilities privately to the repository owner through GitHub's private security reporting channel. Do not create a public issue containing sensitive data. Include a minimal reproduction, affected document or schema, impact, and a proposed safe correction when possible.

## Prohibited repository content

Never commit API keys, cookies, session tokens, OAuth artifacts, email addresses used for provider access, account identity or count, `.env` files, SSH material, VPS credentials, private URLs, chat IDs, raw provider inventories, or unsanitized audit exports.

If sensitive material is committed, stop publication, revoke or rotate the credential outside this repository, remove it from history using an approved incident process, and document only the sanitized incident outcome.

## Operational boundary

This repository does not authorize connecting to providers, modifying OmniRoute, deploying Hermes, changing services, or accessing production infrastructure. Those actions require a separate approved implementation plan and isolated credentials.
