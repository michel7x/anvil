---
name: create-pull-request
description: Open a GitHub pull request for a pushed feature branch, with a generated title and description. Use only when the developer explicitly asks to open or create a pull request.
argument-hint: "[issue number]"
---

# Create a pull request

1. Confirm the branch is not `main` and is pushed with no unpushed commits. If it isn't pushed, stop and ask, because pushing is a separate request.
2. Run `git log origin/main..HEAD` and `git diff origin/main...HEAD`, and read all of the changes, not only the latest commit.
3. Write the title in the commit header format from [`git-message-format.md`](../../git-message-format.md).
4. Write the body with these sections:
   - **What changed**
   - **Why**
   - **How it was verified**: list only checks that actually ran, with their results.
   - **Linked issues**: use `Closes #<n>` only if this work fully resolves the issue, otherwise `Refs #<n>`.
5. If behaviour or structure changed but `CLAUDE.md`, `docs/architecture.md`, or an ADR did not, say so in the body.
6. Run `gh pr create --base main --title "<title>" --body "<body>"`.
7. Report the pull request URL.

Never merge the pull request or enable auto-merge.
