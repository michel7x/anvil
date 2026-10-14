---
name: add-dependency
description: Add, upgrade, or remove a Python dependency with uv. Use whenever a package needs to be installed or a dependency changed. Never use pip, poetry, or hand edits.
---

# Manage a dependency (uv only)

Every dependency change goes through `uv`. Never run `pip install`, `python -m pip`, `poetry add`, or `pipenv install`. Never hand-edit the dependency tables in `pyproject.toml`, and never edit `uv.lock`.

Get the user's approval before you add a runtime dependency (see `AGENTS.md`, Boundaries).

1. **Justify it.** Check whether the stdlib or an existing dependency already covers the need. Run `uv tree` to see what is installed.
2. **Vet it.** Confirm the package is maintained (recent releases), widely used, has typed code or stubs, and has a licence compatible with MIT.
3. **Add it** with a lower-bound constraint:
   - Runtime: `uv add "<pkg>>=X.Y"`
   - Dev only: `uv add --dev "<pkg>>=X.Y"`
   - Another group: `uv add --group <name> "<pkg>>=X.Y"`
   - Optional extra: `uv add --optional <extra> "<pkg>>=X.Y"`
   - If the package is untyped, add its stubs as a dev dependency: `uv add --dev types-<pkg>`.
4. **Verify.** Run `uv run ruff check . && uv run mypy && uv run pytest`.
5. **Commit** `pyproject.toml` and `uv.lock` together.
6. **Document it.** If the package is significant (a framework, database, or client), add it to the Tech stack section in `AGENTS.md` and consider an ADR using the `write-adr` skill.

Other operations:
- Upgrade one package: `uv lock --upgrade-package <pkg> && uv sync`
- Remove one: `uv remove <pkg>`, then delete its imports and any mention in the docs.
- One-off CLI tool that isn't a project dependency: `uvx <tool>`.
