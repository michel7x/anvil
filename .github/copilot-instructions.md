# Copilot instructions

The full project context lives in [`AGENTS.md`](../AGENTS.md) at the repository root. Read it first and follow it.

Must-follow rules (summary):

- Python 3.14+, `src/` layout. **uv manages everything**: dependencies (`uv add` / `uv remove`), the lockfile, the venv (`uv sync`), Python versions (`uv python`), the version number (`uv version`), and builds (`uv build`, `uv_build` backend). Run code with `uv run ...`.
- Never use `pip`, `poetry`, `pipenv`, `conda`, or `requirements.txt`. Never hand-edit dependency tables in `pyproject.toml` or `uv.lock`.
- Before finishing, these must pass: `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`.
- Type-annotate every function (mypy strict). Use `logging`, not `print`. Use `pathlib`, not `os.path`.
- Every behaviour change needs a pytest test. Tests are offline and deterministic.
- Never commit secrets. Ask before you add dependencies or change public APIs.
- Path-specific rules are in `.github/instructions/`. Reusable workflows are Agent Skills in `.agents/skills/` (e.g. `/plan-feature`).
