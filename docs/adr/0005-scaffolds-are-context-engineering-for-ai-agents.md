# 0005. Anvil scaffolds are context engineering for AI agents

- Status: Accepted
- Date: 2026-10-14

## Context

ADR 0004 described Anvil as a generator of "project scaffolds" in general terms: directory layout, tooling, CI, *and* an AI context layer. That framing invites scope creep towards a general-purpose project generator, a crowded space (cookiecutter, copier, `uv init`). What Anvil uniquely provides is the context-engineering layer that makes AI coding agents effective in a project.

## Decision

The product of Anvil is a **context-engineering scaffold for AI coding agents**:
- shared rules (`AGENTS.md`) and agent entry points (`CLAUDE.md`, `.github/copilot-instructions.md`)
- path-scoped rules, Agent Skills, custom agents, MCP configuration, and agent settings/hooks
- architecture and decision docs, plus the sync tooling that keeps per-agent files from drifting

Goals: agent-ready from day one, multi-agent with a single source of truth, stack-aware blueprints (Python first), and context that stays current.

Non-goals: generating application code or business logic, and acting as an AI agent or calling LLMs.

## Alternatives considered

- **General project generator, with the context layer as one feature**: it competes with mature tools and dilutes the focus.

## Consequences

- Blueprints are judged on the quality and accuracy of the agent context they produce.
- Stack tooling (for example `pyproject.toml`) is in scope only where the context relies on it. For example, the commands listed in `AGENTS.md` must actually work.
- CLI help, package metadata, README, and `AGENTS.md` use this wording.
