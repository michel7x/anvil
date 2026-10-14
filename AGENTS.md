# AGENTS.md

The shared, tool-agnostic context for AI coding agents (Claude Code, GitHub Copilot, and others) working in this repository.
This file is the **single source of truth**. `CLAUDE.md` and `.github/copilot-instructions.md` defer to it.

## Project overview

Anvil is a command-line tool that forges **context-engineering scaffolds for AI coding agents**. A scaffold is the set of files that gives agents such as Claude Code and GitHub Copilot the context they need to work well in a project:
- shared rules (`AGENTS.md`) and tool entry points (`CLAUDE.md`, `.github/copilot-instructions.md`)
- path-scoped rules, Agent Skills, custom agents, MCP configuration, and agent settings/hooks
- the architecture and decision docs that agents read before making changes

**Goals**
1. **Agent-ready from day one**: a new application starts with complete, accurate context for AI agents.
2. **Multi-agent, single source of truth**: one canonical context serves every supported agent (Claude Code and GitHub Copilot first). Per-tool files are generated, not maintained by hand, so they never drift.
3. **Stack-aware**: blueprints encode real commands and conventions for the target stack, starting with Python (uv, ruff, mypy, pytest).
4. **Kept current**: forged projects include the tooling (sync script, `--check` in CI and pre-commit) that keeps the context consistent as the project evolves.

**Non-goals**
- Generating application code or business logic. The scaffold describes and guides the project; it doesn't implement it.
- Being an AI agent or calling LLMs. Anvil produces context files deterministically.

Current status: the CLI structure exists (`new`, `list`, `version`), but scaffold generation is **not implemented yet**. Stub commands exit with code 1. The template format and engine are still to be decided (see `docs/adr/0004-anvil-as-scaffold-generator-cli.md`).

The context files in this repo (`AGENTS.md`, `.agents/`, `.github/`, `.claude/`) are Anvil's **own** development context. They are not templates, but they are the reference for what the first (Python) blueprint will produce.

## Tech stack

- Python 3.14+ in a `src/` layout. The package lives at `src/anvil/`.
- [uv](https://docs.astral.sh/uv/) manages **everything** about the project: Python versions, virtualenvs, dependencies, the lockfile (`uv.lock`, always committed), and building (`uv_build` backend). See [uv only](#uv-only) below.
- [ruff](https://docs.astral.sh/ruff/) handles linting and formatting. [mypy](https://mypy.readthedocs.io/) runs in strict mode. [pytest](https://docs.pytest.org/) runs the tests.
- [Typer](https://typer.tiangolo.com/) is the CLI framework. It brings Rich in for help output.

## Commands

Run everything through `uv run` so the project environment is always used.

| Task | Command |
|------|---------|
| Install / sync deps | `uv sync` |
| Run the CLI | `uv run anvil --help` (or `uv run python -m anvil`) |
| Install CLI globally | `uv tool install .` |
| Tests | `uv run pytest` |
| Single test | `uv run pytest tests/test_smoke.py::test_version_is_set` |
| Coverage | `uv run pytest --cov=anvil --cov-report=term-missing` |
| Lint (autofix) | `uv run ruff check --fix .` |
| Format | `uv run ruff format .` |
| Type-check | `uv run mypy` |
| Sync AI context | `uv run python scripts/sync_ai_context.py` |
| Add a dependency | `uv add <pkg>` (runtime) / `uv add --dev <pkg>` (dev) / `uv add --group <name> <pkg>` |
| Remove a dependency | `uv remove <pkg>` |
| Upgrade a dependency | `uv lock --upgrade-package <pkg> && uv sync` |
| Show dependency tree | `uv tree` |
| Install / pin Python | `uv python install` / `uv python pin 3.14` |
| Bump version | `uv version --bump patch` (or `minor` / `major`) |
| Build sdist + wheel | `uv build` |
| Run a one-off tool | `uvx <tool>` |

Before you call a task done, these must pass: `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`.

## uv only

All dependency, environment, settings, and build operations go through `uv`. No other tool is allowed for these jobs.

- **Dependencies**: use only `uv add`, `uv remove`, and `uv lock`. Never use `pip install`, `python -m pip`, `pipx`, `poetry`, `pipenv`, `conda`, or `requirements.txt` files.
- **Don't hand-edit** `[project.dependencies]`, `[dependency-groups]`, `[project.optional-dependencies]`, or `uv.lock`. Change them with `uv` commands. If you need a `requirements.txt` for some other system, generate it with `uv export`.
- **Version**: change it with `uv version`, not by editing `pyproject.toml`.
- **Python interpreter**: get it with `uv python install`. The `.python-version` file is managed by `uv python pin`.
- **Environment**: `.venv/` is created and updated only by `uv sync`. Run code with `uv run`, not by activating the venv or calling the system `python`.
- **Build and publish**: use `uv build` and `uv publish`. The build backend is `uv_build`. Configure it under `[tool.uv.build-backend]`.
- **Tool settings**: put project-level uv settings under `[tool.uv]` in `pyproject.toml`, not in a per-user `uv.toml`.
- Commit `pyproject.toml` and `uv.lock` together. CI runs `uv sync --locked`, so it fails if the lockfile is stale.

## Repository layout

```
src/anvil/cli.py       Typer app: global options + command registration
src/anvil/commands/    one module per command (parse input, delegate; no logic)
src/anvil/templates/   blueprints Anvil forges from (empty for now)
src/anvil/errors.py    project exceptions (AnvilError)
src/anvil/__main__.py  `python -m anvil` (thin)
tests/              pytest suite, mirrors src/ structure
scripts/            developer tooling (not shipped)
docs/architecture.md  system overview: read before structural changes
docs/adr/           architecture decision records
docs/plans/         implementation plans written by agents
docs/ai/            how the AI context layer works
.github/instructions   SOURCE of path-scoped AI rules
.agents/skills         SOURCE of Agent Skills (reusable workflows)
.claude/rules, .claude/skills   GENERATED from the above. Do not edit.
```

## Coding conventions

- Type-annotate every function signature. Avoid `Any`. Prefer `collections.abc` types and `X | None`.
- Keep functions small and pure where possible. Push I/O to the edges.
- Use `logging.getLogger(__name__)`, never `print`, for diagnostics. CLI output is the only exception.
- Use `pathlib.Path`, not `os.path`.
- Raise specific exceptions. Never use bare `except:` or swallow errors silently.
- Write docstrings for public modules, classes, and functions, in Google style, and keep them brief.
- Configuration comes from environment variables or config files. Never hard-code secrets or URLs.
- Follow existing patterns before you introduce a new library or abstraction.

## Testing

- Every behaviour change needs a test. Bug fixes start with a failing test.
- Tests are fast, deterministic, and offline. Mock the network, time, and randomness.
- Use plain `assert`, fixtures in `conftest.py`, and `pytest.mark.parametrize` for tables of cases.

## Git & pull requests

- Keep commits small and focused, with imperative subject lines (`Add X`, `Fix Y`).
- Each PR describes *what* changed and *why*, and how it was verified.
- Update docs (`AGENTS.md`, `docs/architecture.md`, ADRs) in the same PR when behaviour or structure changes.

## Boundaries

- **Never** commit secrets, `.env` files, or credentials.
- **Never** edit generated files in `.claude/rules/` or `.claude/skills/`. Edit `.github/instructions/` or `.agents/skills/` instead and run the sync script.
- **Ask first** before you add a dependency, change public APIs, change CI, or delete files.
- Don't disable lint rules, type checks, or tests to make things pass. Fix the cause.

## More context

- Architecture: `docs/architecture.md`
- Decisions: `docs/adr/`
- AI context layout and customization: `docs/ai/README.md`
