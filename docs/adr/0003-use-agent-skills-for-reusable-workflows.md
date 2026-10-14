# 0003. Use Agent Skills instead of prompt files for reusable workflows

- Status: Accepted
- Date: 2026-10-13

## Context

ADR 0001 kept reusable prompts in `.github/prompts/*.prompt.md` and generated Claude Code commands from them. VS Code has since deprecated prompt files: the new Copilot (Agent Host) harness doesn't load them, and the Local agent that still does will be removed. The `chat.promptFilesLocations` and `chat.instructionsFilesLocations` settings are deprecated as well. The Copilot harness reads skills from `.github/skills/` or `.agents/skills/`. Claude Code reads them from `.claude/skills/`.

## Decision

We will express all reusable workflows as Agent Skills (`SKILL.md`), with the source in `.agents/skills/`. That is the tool-neutral location, matching `AGENTS.md`, and Copilot reads it natively. `scripts/sync_ai_context.py` mirrors it to `.claude/skills/` for Claude Code. Former prompts become skills with `disable-model-invocation: true`, so they run only when invoked with `/name`. Prompt files and deprecated location settings are not used.

## Alternatives considered

- Source in `.claude/skills/` and mirror to `.github/skills/`: ties the canonical copy to one vendor.
- Symlinking `.claude/skills` to `.agents/skills`: unreliable on Windows checkouts.

## Consequences

- One format serves both tools. Workflows can bundle supporting files such as templates and scripts.
- Prompt-only features (`${input:...}` variables, and per-prompt `agent`/`model`/`tools`) are gone. Skills refer to "the user's request or arguments" instead. Workflows that need a fixed tool set use custom agents.
