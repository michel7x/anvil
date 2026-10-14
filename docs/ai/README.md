# AI context layer

This repository ships context for **Claude Code** and **GitHub Copilot**. The goal is that both tools follow the same rules and nothing is maintained twice.

## What each tool reads

| Purpose | Source of truth | Claude Code | GitHub Copilot |
|---------|-----------------|-------------|----------------|
| Project-wide rules (incl. "uv only") | `AGENTS.md` | via `CLAUDE.md` → `@AGENTS.md` | `AGENTS.md` (native) + `.github/copilot-instructions.md` |
| Path-scoped rules | `.github/instructions/*.instructions.md` | `.claude/rules/*.md` *(generated)* | same file (`applyTo`) |
| Custom agents | written per tool, same body | `.claude/agents/*.md` | `.github/agents/*.agent.md` |
| Skills / reusable workflows | `.agents/skills/*/SKILL.md` | `.claude/skills/` *(generated)* → `/name` | same folder (native) → `/name` |
| MCP servers | written per tool | `.mcp.json` | `.vscode/mcp.json` |
| Settings / hooks | written per tool | `.claude/settings.json` | `.vscode/settings.json` |
| Cloud agent env | n/a | n/a | `.github/workflows/copilot-setup-steps.yml` |
| Architecture & decisions | `docs/architecture.md`, `docs/adr/` | linked from `AGENTS.md` | linked from `AGENTS.md` |

## Editing workflow

1. **Project-wide rule** → edit `AGENTS.md`. Keep it short (under about 150 lines). Move detail into `docs/` and link to it.
2. **Rule for certain files** → add or edit `.github/instructions/<name>.instructions.md` with `applyTo: "glob,glob"`.
3. **Reusable workflow** → add `.agents/skills/<name>/SKILL.md` with `name`, `description`, and optionally `argument-hint`. Add `disable-model-invocation: true` if it should run only when invoked with `/name`. Refer to "the user's request or arguments" instead of a placeholder variable, so the same text works in both tools. Don't use prompt files (`*.prompt.md`): VS Code has deprecated them.
4. Run `uv run python scripts/sync_ai_context.py`. CI and pre-commit run it with `--check`.
5. **Agent** → edit both `.claude/agents/<name>.md` and `.github/agents/<name>.agent.md`. Keep the bodies identical.
6. Supporting files (templates, scripts) go next to `SKILL.md` and are mirrored too.

## Adding an MCP server

Add the server to both files. The top-level keys differ:

```jsonc
// .mcp.json (Claude Code)
{ "mcpServers": { "example": { "command": "uvx", "args": ["example-mcp"] } } }

// .vscode/mcp.json (Copilot)
{ "servers": { "example": { "command": "uvx", "args": ["example-mcp"] } } }
```

Never put secrets in these files. Use environment variables or input prompts.

## Personal overrides (not committed)

- Claude: `CLAUDE.local.md` and `.claude/settings.local.json`.
- Copilot: VS Code user settings, plus `~/.copilot/skills` and `~/.copilot/instructions`.

## Writing good context

- Write rules that are specific and checkable ("annotate every function"), not vague ("write clean code").
- Prefer commands and examples over prose.
- When an agent makes the same mistake twice, add a rule. When a rule no longer matters, delete it.
- Run the `/update-context` skill after significant changes.
