# CLAUDE.md

@AGENTS.md

## Claude Code specifics

- **Scoped rules**: `.claude/rules/*.md` load automatically for matching paths. They are generated from `.github/instructions/`. Don't edit them directly.
- **Subagents**: `.claude/agents/` defines `planner`, `reviewer`, and `test-writer`.
- **Skills**: `.claude/skills/` is generated from `.agents/skills/`. Don't edit it directly. You invoke these workflows with `/plan-feature`, `/implement-feature`, `/write-tests`, `/review-changes`, and `/update-context`. Claude can also load `write-adr` and `add-dependency` on its own.
- **Hooks**: after edits, `.claude/settings.json` runs `ruff format` and `ruff check --fix` on changed Python files.
- Put personal, uncommitted preferences in `CLAUDE.local.md`. It is git-ignored.
