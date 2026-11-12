---
name: create-branch
description: Create a local feature branch from an up-to-date main. Use only when the developer explicitly asks to create or start a branch.
argument-hint: "[short summary or issue number]"
---

# Create a branch

1. Run `git status` and note any uncommitted changes.
2. Choose the name `<type>/<short-kebab-summary>`, using a type from [`git-message-format.md`](../../git-message-format.md). Include the issue number if there is one, such as `feat/42-forge-command`.
3. Run `git fetch origin`.
4. Run `git switch -c <name> origin/main`.
5. If git refuses because uncommitted changes would be overwritten, report the exact error and stop. Don't stash or discard anything.
6. Report the branch name and any uncommitted changes carried over.

Don't push the branch. Pushing is a separate request.
