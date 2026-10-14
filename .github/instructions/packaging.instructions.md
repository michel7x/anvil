---
description: Rules for project metadata, dependencies, and build configuration (uv only)
applyTo: "pyproject.toml,uv.lock,.python-version"
---

# Packaging rules (uv)

`uv` owns these files. Change them with uv commands, not by hand, whenever a command exists:

| Change | Command |
|--------|---------|
| Add / remove a runtime dependency | `uv add <pkg>` / `uv remove <pkg>` |
| Dev or other dependency group | `uv add --dev <pkg>` / `uv add --group <name> <pkg>` |
| Optional extra | `uv add --optional <extra> <pkg>` |
| Upgrade | `uv lock --upgrade-package <pkg>` (or `uv lock --upgrade`) |
| Refresh lock after a manual metadata edit | `uv lock` |
| Python version | `uv python pin <ver>`, and update `requires-python` to match |
| Project version | `uv version <ver>` / `uv version --bump patch` |
| Export for an external system | `uv export --format requirements-txt` (never commit the output) |

- Never edit `uv.lock` by hand.
- Hand edits are allowed only for tool settings that have no uv command: `[tool.ruff]`, `[tool.mypy]`, `[tool.pytest.*]`, `[tool.uv]`, `[tool.uv.build-backend]`, and descriptive `[project]` metadata. Run `uv lock` afterwards.
- The build backend is `uv_build`. Don't switch to setuptools, hatchling, poetry-core, or another backend without an ADR.
- Never add `setup.py`, `setup.cfg`, `requirements*.txt`, `Pipfile`, or `environment.yml`.
