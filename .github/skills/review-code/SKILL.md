---
name: review-code
description: Review a pull request or local diff against the project conventions and report findings. Use only when the developer explicitly asks for a code review.
argument-hint: "[pull request number]"
---

# Review code

1. Get the target the developer named:
   - Pull request: `gh pr view <n>` and `gh pr diff <n>`
   - Local changes: `git diff` and `git diff --staged`
   - Branch: `git diff origin/main...HEAD`
2. Read `CLAUDE.md` and the rules in `.claude/rules/` that match the changed paths.
3. Check for:
   - correctness bugs and unhandled failures
   - missing tests for changed behaviour
   - secrets, credentials, or private data
   - changes to dependencies, public APIs, or CI that needed approval
   - docs or ADRs that should have changed with the code
4. Report findings most severe first, each with `path:line`, the problem, and a suggested fix. If you find nothing, say so.
5. Post to the pull request only if the developer asked, using `gh pr review <n> --comment --body "<findings>"`.
6. Use `--approve` or `--request-changes` only if the developer asks for that outcome specifically.

Never change code during a review.
