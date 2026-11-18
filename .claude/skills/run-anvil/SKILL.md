---
name: run-anvil
description: Build, install, run, and smoke-test the anvil CLI. Use when asked to run anvil, start or try a command (new, list, version), check that the CLI works after a change, run its tests, or build its package or container image.
---

Anvil is a Typer CLI. You drive it with `uv run anvil ...`. The smoke script `.claude/skills/run-anvil/smoke.sh` runs representative commands and checks their exit codes and output. All paths are relative to the repository root.

## Prerequisites

- uv 0.13.x (`uv --version`). uv provides Python 3.14 from `.python-version`.
- Docker only for the container image (see Gotchas).

## Setup

```bash
uv sync --locked
```

## Run (agent path)

Run the smoke script after every CLI change:

```bash
bash .claude/skills/run-anvil/smoke.sh
```

It prints `PASS`/`FAIL` per command, then `smoke: all passed`, and exits 0 only if all checks pass. When you implement a stub command (`new`, `list`), update its expectation in the script.

Run one command:

```bash
uv run anvil version
# -> anvil 0.1.0
```

```bash
uv run anvil new demo --template python --output /tmp/anvil-smoke --force
# -> new: not implemented yet   (stderr, exit 1)
```

Current exit codes:

| Invocation | Exit | Output |
|---|---|---|
| `anvil version`, `anvil --help` | 0 | version / help |
| `anvil list`, `anvil new <name>` | 1 | `<cmd>: not implemented yet` on stderr |
| `anvil` (no args) | 2 | help |
| unknown command, missing argument | 2 | Typer error box |

## Direct invocation

Call the Typer app in-process, the same way the tests do:

```bash
uv run python -c "
from typer.testing import CliRunner
from anvil.cli import app
r = CliRunner().invoke(app, ['version'])
print(r.exit_code, r.output, end='')
"
# -> 0 anvil 0.1.0
```

## Run from a built package

This builds a wheel from the working tree into a throwaway environment. It doesn't touch `.venv`:

```bash
uvx --from . anvil version
```

## Test

```bash
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```

There are 11 tests, and all of them pass.

## Gotchas

- **Running `anvil` with no arguments exits 2, not 0.** `no_args_is_help=True` prints the help, then exits with the usage-error code.
- **`GITHUB_ACTIONS` forces ANSI output.** When this variable is set, Typer forces Rich terminal rendering, and escape codes split strings such as `--template`. `NO_COLOR=1` doesn't stop this. Set `_TYPER_FORCE_DISABLE_TERMINAL=1` instead. The smoke script sets it, and `tests/conftest.py` patches `FORCE_TERMINAL`.
- **Typer shows arguments in lower case.** A missing argument prints `Missing argument 'name'`, and the usage line shows `{name}`, not `NAME`.
- **Docker can be missing under WSL.** On WSL, `docker` may be the Docker Desktop shim, which fails until Docker Desktop's WSL integration is turned on. The image build (`docker build -f containers/anvil.containerfile -t anvil .`) has not been verified in this environment.

## Troubleshooting

- **`The command 'docker' could not be found in this WSL 2 distro.`**: Docker Desktop's WSL integration is turned off. Turn it on in Docker Desktop settings, or skip the image build.
