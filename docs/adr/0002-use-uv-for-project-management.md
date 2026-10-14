# 0002. Use uv for all dependency, environment, and build management

- Status: Accepted
- Date: 2026-10-13

## Context

Python has many overlapping tools for interpreters, virtualenvs, dependencies, locking, and building: pip, pip-tools, poetry, pipenv, conda, setuptools, and hatch. When humans or AI agents mix them, environments drift, lockfiles go stale, and builds are not reproducible.

## Decision

We will use **uv** for every project-management task:
- Python interpreters: `uv python install` / `uv python pin`.
- Environment: `uv sync`. Running code: `uv run`.
- Dependencies: `uv add` / `uv remove` / `uv lock`, with `uv.lock` committed.
- Versioning: `uv version`.
- Build backend `uv_build`, with builds via `uv build` and publishing via `uv publish`.

No other package manager or build tool may be used, and the dependency tables and lockfile are never edited by hand.

## Alternatives considered

- Poetry: slower, and it has its own lock format and build backend. It would not also manage Python versions.
- pip + pip-tools + hatchling: more tools to coordinate and no single source of truth.

## Consequences

- One fast tool, a reproducible lockfile, and CI that fails on a stale lock (`uv sync --locked`).
- Contributors must install uv.
- The rules live in `AGENTS.md` ("uv only") and `.github/instructions/packaging.instructions.md`. Claude Code also asks for permission before `uv add` / `uv remove` and blocks pip, poetry, and pipenv.
