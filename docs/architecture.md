# Architecture

Keep this document short and current. Agents read it before making structural changes.

## Purpose

Anvil is a CLI that forges project scaffolds. From a named template (blueprint), it generates the directory structure, tooling configuration, and AI context-engineering layer for a new application, so that every project starts from the same proven baseline.

## Components

| Module | Responsibility |
|--------|----------------|
| `anvil.cli` | Typer application: global options (`--verbose`), logging setup, command registration. |
| `anvil.commands.*` | One module per command (`new`, `list`, `version`). Each parses and validates input, then delegates. No business logic. |
| `anvil.commands._stub` | Temporary helper: reports "not implemented yet" and exits with code 1. |
| `anvil.templates` | Package data: the blueprints Anvil forges from. Empty for now. |
| `anvil.errors` | `AnvilError` hierarchy. Core logic raises these, and the CLI maps them to exit codes. |
| `anvil.__main__` | `python -m anvil` entry point. Console script: `anvil = anvil.cli:app`. |

Planned (not yet created): core modules for template discovery and rendering, which the commands will call. They will be importable and testable without Typer.

## Data flow

<!-- TODO: define once the template format/engine is decided (future ADR). Expected: `anvil new NAME -t TEMPLATE` → resolve template → collect variables → render into OUTPUT/NAME → post-generation steps (e.g. `uv sync`, `git init`). -->

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Failure (including "not implemented yet") |
| 2 | Usage error (Typer/Click) |

## External dependencies

- **Typer** (with Rich): CLI parsing and help rendering.

## Cross-cutting concerns

- **Logging**: stdlib `logging`, configured once in the `cli.main` callback. `--verbose` sets the level to DEBUG.
- **Output**: user-facing text goes through `typer.echo`. Errors go to stderr (`err=True`).
- **Errors**: core code raises `AnvilError` subclasses and never calls `sys.exit`.
