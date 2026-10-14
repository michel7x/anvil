---
name: implement-feature
description: Implement a feature (optionally from a plan in docs/plans/) with tests
argument-hint: Feature description or path to plan
disable-model-invocation: true
---
<!-- GENERATED from .agents/skills/implement-feature/SKILL.md by scripts/sync_ai_context.py. Do not edit. -->

# Implement a feature

Implement the following. If it refers to a plan in `docs/plans/`, follow that plan.

Task: the feature description or `docs/plans/` path given in the user's request or arguments.

Steps:
1. Re-read `AGENTS.md` for conventions and commands.
2. Write or extend tests first, and confirm they fail for the right reason.
3. Implement the smallest change that makes them pass. Reuse existing code.
4. Run `uv run ruff check --fix . && uv run ruff format . && uv run mypy && uv run pytest`, and fix anything that fails.
5. Update the docs (`AGENTS.md`, `docs/architecture.md`) if commands, layout, or behaviour changed.
6. Summarise what changed, how you verified it, and any follow-ups.
