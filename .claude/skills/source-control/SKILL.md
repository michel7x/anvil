---
name: source-control
description: Hand a source-control request (commit, branch, push, pull request, issue, PR review) to the Source Control Agent (GitHub Copilot CLI). Use ONLY when the user explicitly asks in this conversation for that source-control action. Never use it on your own initiative, including when work looks finished.
---

# Hand off to the Source Control Agent

GitHub Copilot owns source control for Anvil (see `docs/adr/0007-copilot-owns-source-control.md`). Claude Code never runs git write commands or `gh` write commands itself. This skill passes the user's request to Copilot through [handoff.sh](handoff.sh). Copilot then does the work with its own skills in `.github/skills/`.

## When to use this skill

Use it only when the user explicitly asks for a source-control action, for example "commit the changes" or "open a PR".

- Never call it on your own initiative. This includes when a task ends, when tests pass, or when a plan says to commit.
- Hand off only the action the user asked for. A request to commit is not a request to push.
- If the request is ambiguous, ask the user before you hand it off.
- For read-only inspection, such as `git status`, `git diff`, and `git log`, run the commands yourself. You don't need this skill.

## Steps

1. Write the prompt for Copilot:
   - State the exact action the user asked for, in plain words.
   - For a commit, describe what changed and why, in one or two sentences. Copilot writes the commit message from the staged diff and this summary.
   - Pass on any details the user gave, such as a branch name, an issue number, or which files to include.
   - Never include secrets or credentials.
2. Run the handoff from the repository root with a 10-minute timeout (`timeout: 600000`). A run usually takes one to three minutes:

   ```bash
   bash .claude/skills/source-control/handoff.sh "<prompt>"
   ```

3. Report Copilot's answer to the user, including any hash, URL, or failure, exactly as Copilot gave it. Then run `git status` or `git log -1` yourself to confirm the result.
4. If Copilot fails or refuses, report the exact output and stop. Don't retry with a different prompt, and don't do the git work yourself, unless the user asks.

Example prompt:

```bash
bash .claude/skills/source-control/handoff.sh "Commit the current uncommitted changes. They add the run-anvil skill, a smoke script for the CLI. Don't push."
```

## What handoff.sh does

It runs `copilot -p` in non-interactive mode against the local Ollama model `glm-4.7-flash` at `http://localhost:11434/v1`.

Non-interactive mode denies every tool call that no rule allows, so the script:
- allows `git`, `gh`, `uv`, and `uvx`
- denies the commands that `.github/copilot-instructions.md` forbids, such as `git reset`, `git rebase`, `git merge`, `git tag`, `gh release`, `uv build`, and file writes
- denies `copilot`, `bash`, and `handoff.sh`, so that Copilot can't call this skill again (Copilot also loads `.claude/skills/`)

Shell rules only match the first subcommand, so the script can't deny `gh pr merge` or `git push --force` alone. Those limits rely on Copilot's instructions.

## Troubleshooting

- **`Warning: Skipped repository hooks ... because the folder ... is not trusted.`**: This warning is harmless. Copilot still loads `.github/copilot-instructions.md` and its skills. To list what it loads, run `copilot instruction list` and `copilot skill list`.
- **The connection is refused, or the model is not found.**: Ollama isn't running, or the model isn't pulled. Run `curl -s http://localhost:11434/v1/models` and check that it lists `glm-4.7-flash:latest`.
