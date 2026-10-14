---
name: update-context
description: Refresh AGENTS.md and docs so AI context matches the current codebase
argument-hint: Optional notes on what changed
disable-model-invocation: true
---

# Update AI context

Bring the AI context files up to date with the code. Use any notes in the user's request or arguments about what changed.

1. Compare `AGENTS.md` (commands, layout, stack, conventions) with the actual repository: `pyproject.toml`, the directory tree, and CI workflows.
2. Compare `docs/architecture.md` with the current modules and their dependencies.
3. Fix anything stale. Fill in `TODO` placeholders you can answer from the code. List the rest.
4. If scoped rules in `.github/instructions/` or skills in `.agents/skills/` changed, run `uv run python scripts/sync_ai_context.py`.
5. Keep `AGENTS.md` concise. Move detail into `docs/` and link to it.
6. Summarise each change and why you made it.
