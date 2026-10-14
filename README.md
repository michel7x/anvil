# Anvil

**Anvil forges project scaffolds.** It is a command-line tool that generates new applications from proven blueprints. A blueprint covers the directory layout, tooling (uv, ruff, mypy, pytest), CI, and an AI context-engineering layer for Claude Code and GitHub Copilot.

> **Status:** early. The CLI structure is in place, but scaffold generation is not implemented yet.

## Install

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14+.

```bash
uv tool install .        # install the `anvil` command from a checkout
# or, without installing:
uv run anvil --help
```

## Usage

```bash
anvil --help                         # list commands
anvil new my-app                     # forge a new project (not implemented yet)
anvil new my-app -t python -o ~/src  # choose template and output directory
anvil list                           # list available templates (not implemented yet)
anvil version                        # show version
```

## Development

```bash
uv sync                  # create .venv and install everything
uv run pytest            # tests
uv run ruff check --fix . && uv run ruff format .
uv run mypy
uv add <pkg>             # add a dependency (never pip install)
uv build                 # build sdist + wheel into dist/
```

All dependency, environment, version, and build operations go through **uv**. See the "uv only" section of [`AGENTS.md`](AGENTS.md).

Contributor and AI-agent guidelines are in [`AGENTS.md`](AGENTS.md). The AI context layer is explained in [`docs/ai/README.md`](docs/ai/README.md), architecture in [`docs/architecture.md`](docs/architecture.md), and decisions in [`docs/adr/`](docs/adr/).

## License

MIT
