# 0004. Turn Anvil into a scaffold-generator CLI built with Typer

- Status: Accepted
- Date: 2026-10-14

## Context

Anvil started as a template repository: a Python skeleton with a context-engineering layer for Claude Code and GitHub Copilot. Copying a template repo by hand is static. Every project then needs manual renaming, there is no choice of variants, and improvements to the baseline don't reach projects that already exist. We want a tool that generates ("forges") scaffolds on demand.

## Decision

We will turn Anvil into a command-line tool that forges project scaffolds. It is built with **Typer**, has the console script `anvil`, and starts with the commands `new`, `list`, and `version`. Templates will be stored as package data under `src/anvil/templates/`. The template format and rendering engine are decided separately, in a later ADR.

The context layer in this repository stays as Anvil's own development context.

## Alternatives considered

- **argparse**: no extra dependency, but verbose and without type-hint-driven parameters.
- **click**: mature, and Typer is built on it. Typer gives the same power with less boilerplate, plus typed signatures that suit mypy strict.
- **Using cookiecutter or copier directly with no CLI of our own**: still possible as the *engine* behind Anvil. That choice is left to the template-engine ADR.

## Consequences

- Typer (and Rich) become runtime dependencies.
- Commands are stubs until the generation logic lands. They exit with code 1 and print "not implemented yet".
- The "Use this template" workflow in the README is replaced by installing and running the CLI.
