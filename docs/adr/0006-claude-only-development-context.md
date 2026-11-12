# 0006. Use a Claude-only context for developing Anvil

- Status: Proposed, amended by 0007
- Date: 2026-11-06

## Context

ADRs 0001 and 0003 set up Anvil's own development context for both Claude Code and GitHub Copilot: `AGENTS.md` as shared rules, sources in `.github/instructions/` and `.agents/skills/`, and `scripts/sync_ai_context.py` generating `.claude/` from them. Anvil is now developed with Claude Code only, so the Copilot files have no reader and the sync step adds work without benefit.

Two things had been treated as one: the context used to develop Anvil, and the context Anvil generates. Only the first is changing. ADR 0005 stays in force, and forged scaffolds remain multi-agent.

## Decision

We will keep Anvil's own development context in `CLAUDE.md` and `.claude/` only, and edit those files directly:
- `AGENTS.md` is merged into `CLAUDE.md`.
- `.claude/rules/`, `.claude/skills/`, and `.claude/agents/` become sources rather than generated output.
- `.agents/`, `.github/agents/`, `.github/instructions/`, `.github/copilot-instructions.md`, `.github/workflows/copilot-setup-steps.yml`, `.vscode/mcp.json`, and `scripts/` are removed, along with the sync checks in CI and pre-commit.
- Copilot settings are removed from `.vscode/`. Editor settings for Python, ruff, and pytest stay.

This supersedes ADRs 0001 and 0003. The `.github/instructions/` path in the Consequences of ADR 0002 is historical.

## Alternatives considered

- Keep `AGENTS.md` and have `CLAUDE.md` import it: leaves a tool-neutral file in a Claude-only repository, with one layer of indirection for no reader.
- Move the removed files under `src/anvil/templates/` as blueprint seed material: they would ship in the wheel before the template format is decided (ADR 0004).

## Consequences

- One copy of every rule, skill, and agent, with no generation step and no drift check to run.
- `CLAUDE.md` and `.claude/` remain the reference for the Claude output of the first blueprint. They no longer show what the other agents' output looks like.
- Commit `0bdaf6f` is the last one that contains the removed files. Blueprint work should recover these from it with `git show 0bdaf6f:<path>`:
  - `scripts/sync_ai_context.py`: converts `applyTo` to `paths`, mirrors skills, and provides the `--check` drift guard that forged projects are meant to include.
  - `.github/instructions/*.instructions.md`, `.github/agents/*.agent.md`, and `.github/copilot-instructions.md`: Copilot file formats.
  - `.agents/skills/`: the tool-neutral skills location.
  - `.github/workflows/copilot-setup-steps.yml` and `.vscode/mcp.json`: Copilot environment and MCP setup.
  - `AGENTS.md` and `docs/ai/README.md`: the shared-rules file and the per-tool mapping table.
