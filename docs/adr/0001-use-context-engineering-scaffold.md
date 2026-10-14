# 0001. Use a shared context-engineering scaffold for AI agents

- Status: Accepted (amended by 0003)
- Date: 2026-10-13

## Context

The project is developed with help from both Claude Code and GitHub Copilot. Each tool reads instructions from different files and formats. Context that is duplicated by hand drifts out of sync, and the agents then follow outdated rules.

## Decision

We will keep the shared project context in `AGENTS.md`, which both tools read. Path-scoped rules and reusable prompts are authored once in Copilot format under `.github/`. `scripts/sync_ai_context.py` generates the Claude Code equivalents in `.claude/`, and CI checks that they are in sync.

## Alternatives considered

- Separate hand-maintained files per tool: rejected because they drift.
- Symlinks: rejected because the frontmatter formats differ, and symlinks behave poorly on Windows.

## Consequences

- Edit rules and prompts only in `.github/`, then run the sync script.
- Custom agents are still written per tool, because their tool lists differ. Keep their bodies identical.
