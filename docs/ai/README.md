# AI context layer

This repository is developed with **Claude Code**, so its own context is Claude-only and is edited in place. The exception is source control, which **GitHub Copilot** owns. This is separate from what Anvil produces: forged scaffolds still target other agents too. See [ADR 0006](../adr/0006-claude-only-development-context.md) and [ADR 0007](../adr/0007-copilot-owns-source-control.md).

## What Claude Code reads

| Purpose | File |
|---------|------|
| Project-wide rules (incl. "uv only") | `CLAUDE.md` |
| Path-scoped rules | `.claude/rules/*.md` |
| Custom agents | `.claude/agents/*.md` |
| Skills / reusable workflows | `.claude/skills/*/SKILL.md` → `/name` |
| MCP servers | `.mcp.json` |
| Settings / hooks | `.claude/settings.json` |
| Architecture & decisions | `docs/architecture.md`, `docs/adr/` (linked from `CLAUDE.md`) |

## What GitHub Copilot reads

Copilot handles commits, branches, pushes, pull requests, issues, and code review, and acts only when the developer asks. The developer can ask Copilot directly, or ask Claude, which passes the request on with the `source-control` skill (`.claude/skills/source-control/handoff.sh`).

| Purpose | File |
|---------|------|
| Role, allowed actions, and limits | `.github/copilot-instructions.md` |
| Commit message format | `.github/git-message-format.md` |
| One skill per allowed action | `.github/skills/*/SKILL.md` → `/name` |
| Commit message and PR description buttons in VS Code | `.vscode/settings.json` |

## Editing workflow

1. **Project-wide rule** → edit `CLAUDE.md`. Keep it short (under about 150 lines). Move detail into `docs/` and link to it.
2. **Rule for certain files** → add or edit `.claude/rules/<name>.md` with a `paths:` list of globs in the frontmatter.
3. **Reusable workflow** → add `.claude/skills/<name>/SKILL.md` with `name`, `description`, and optionally `argument-hint`. Add `disable-model-invocation: true` if it should run only when invoked with `/name`. Refer to "the user's request or arguments" instead of a placeholder variable.
4. **Agent** → edit `.claude/agents/<name>.md`.
5. Supporting files (templates, scripts) go next to `SKILL.md`.

## Adding an MCP server

Add the server to `.mcp.json`:

```json
{ "mcpServers": { "example": { "command": "uvx", "args": ["example-mcp"] } } }
```

Never put secrets in this file. Use environment variables or input prompts.

## Personal overrides (not committed)

Use `CLAUDE.local.md` and `.claude/settings.local.json`.

## Writing good context

- Write rules that are specific and checkable ("annotate every function"), not vague ("write clean code").
- Prefer commands and examples over prose.
- When an agent makes the same mistake twice, add a rule. When a rule no longer matters, delete it.
- Run the `/update-context` skill after significant changes.
