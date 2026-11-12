# 0007. Give GitHub Copilot ownership of source control

- Status: Proposed
- Date: 2026-11-09

## Context

ADR 0006 makes Anvil's development context Claude-only and removes `.github/copilot-instructions.md`. The developer now wants one agent to be the expert on source control: local git work, commit messages, branches, pull requests, issues, and code review on GitHub. Copilot is that agent. Claude Code keeps code, tests, and docs.

Commit format also needed settling. `CLAUDE.md` asked for imperative subjects such as `Add X`, while existing commits use `feat:` and `chore:` prefixes.

## Decision

We will give GitHub Copilot exclusive ownership of source control in this repository. This narrows ADR 0006, which still applies to everything else.

- Copilot's role and limits are in `.github/copilot-instructions.md`, with project facts linked from `CLAUDE.md`.
- Copilot acts only when the developer explicitly asks.
- Copilot may branch, commit, push feature branches, open pull requests and issues, and review code. Each action has a skill in `.github/skills/`.
- Copilot must not force-push, merge, release, or run destructive operations.
- Claude Code does not commit, push, or create branches, pull requests, or issues.
- All commits follow the Commitizen default format, as specified by Conventional Commits 1.0.0. The rules are in `.github/git-message-format.md`.

## Alternatives considered

- Keep source control with Claude Code: rejected because the developer wants Copilot to be the single expert for it.
- Let both agents do source control: rejected because two sets of rules could drift and blur who is responsible.
- Keep imperative subjects with no type prefix: rejected in favour of a standard format that matches existing history and tooling.

## Consequences

- Each agent has one clear responsibility, and changes wait in the working tree for handoff.
- The repository again has Copilot files to maintain, and the skills are written by hand, not generated.
- Rules in the instructions file and skills guide Copilot but do not enforce anything. Branch protection on `main`, a `commit-msg` hook, or a CI check could enforce them, and each needs separate approval.
- `uvx --from commitizen cz check` validates message format without adding a dependency. It accepts `bump` and does not check subject casing, so those rules rely on Copilot following them.
- The skills depend on `gh` being logged in on the developer's machine.
