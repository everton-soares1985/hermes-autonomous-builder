# Contributing

This repository is documentation-only in V0. Changes should improve contracts, evidence requirements, safety, or clarity without introducing operational credentials or executable infrastructure.

## Workflow

1. Create a focused branch from `main`: `docs/<topic>`, `test/<topic>`, or `chore/<topic>`.
2. Keep one concern per commit and use Conventional Commits.
3. Update the decision log when a model, route, state, gate, or security boundary changes.
4. Run the repository contract test and the GrowthTech GitHub Publisher check.
5. Request review; do not merge while a critical or high finding remains open.

## Documentation rules

- Keep canonical technical documentation in English.
- Keep `README.pt-BR.md` concise instead of duplicating the full manual.
- Distinguish `validated`, `partial`, `available`, and `planned`; never promote a plan to an operational fact.
- Use abstract account labels such as `provider-account-a` when an example requires one.
- Do not paste raw audits, private paths, account counts, emails, tokens, cookies, keys, endpoints, chat IDs, or infrastructure identifiers.

## Required checks

```powershell
.venv\Scripts\activate
python -X utf8 -m unittest discover -s tests -v
project-publisher check .
git diff --check
```

The Publisher command may be run from its canonical environment when it is not installed globally.
