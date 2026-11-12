# Anvil

**Anvil forges context-engineering scaffolds for AI coding agents.** It is a command-line tool that equips a project with everything agents like **Claude Code** and **GitHub Copilot** need to work well in it, generated from proven blueprints.

## What is a context-engineering scaffold?

It is the set of files AI agents read to understand a project and act correctly in it:

| Layer | Examples |
|---|---|
| Shared rules (single source of truth) | `AGENTS.md` |
| Agent entry points | `CLAUDE.md`, `.github/copilot-instructions.md` |
| Path-scoped rules | `.github/instructions/*.instructions.md` → `.claude/rules/` |
| Reusable workflows | Agent Skills in `.agents/skills/` → `.claude/skills/` |
| Custom agents | `.github/agents/`, `.claude/agents/` |
| Tools & guardrails | MCP config, agent permissions and hooks |
| Project knowledge | `docs/architecture.md`, ADRs |
| Drift protection | sync script with `--check` in CI and pre-commit |

## Goals

1. **Agent-ready from day one**: new applications start with complete, accurate context for AI agents.
2. **Multi-agent, single source of truth**: one canonical context serves every supported agent. Per-tool files are generated, so they never drift.
3. **Stack-aware**: blueprints encode the real commands and conventions of the target stack, starting with Python (uv, ruff, mypy, pytest).
4. **Kept current**: forged projects include the tooling that keeps their context consistent as they evolve.

**Non-goals:** Anvil doesn't generate application code, and it isn't an AI agent itself. It produces context files deterministically, without calling any LLM.

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
anvil new my-app                     # forge a context scaffold (not implemented yet)
anvil new my-app -t python -o ~/src  # choose template and output directory
anvil list                           # list available blueprints (not implemented yet)
anvil version                        # show version
```

## Run in a container

The image runs Anvil without uv or Python on the host. [`containers/anvil.containerfile`](containers/anvil.containerfile) builds with any OCI engine. Run the build from the repository root:

```bash
docker build -f containers/anvil.containerfile -t anvil .
podman build -f containers/anvil.containerfile -t anvil .
```

The container works in `/work`, so mount the directory where the scaffold should go. The flags differ per engine, so that generated files end up owned by you:

```bash
docker run --rm -v "$PWD:/work" --user "$(id -u):$(id -g)" anvil new my-app
podman run --rm -v "$PWD:/work:Z" --userns=keep-id anvil new my-app   # rootless
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

All dependency, environment, version, and build operations go through **uv**. See the "uv only" section of [`CLAUDE.md`](CLAUDE.md).

Contributor and AI-agent guidelines are in [`CLAUDE.md`](CLAUDE.md). The AI context layer is explained in [`docs/ai/README.md`](docs/ai/README.md), architecture in [`docs/architecture.md`](docs/architecture.md), and decisions in [`docs/adr/`](docs/adr/).

## License

MIT
