---
name: push-branch
description: Run the project checks and push the current feature branch to origin. Use only when the developer explicitly asks to push.
---

# Push a branch

1. Run `git branch --show-current`. If the branch is `main`, refuse and explain that only feature branches can be pushed.
2. Run the project checks:

   ```bash
   uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
   ```

3. If any check fails, report the exact failure and stop. Don't change code to fix it.
4. Run `git push -u origin HEAD`.
5. If the push is rejected, report the exact error and stop. Never force-push, and never rebase or merge to get past a rejection.
6. Check for an open pull request with `gh pr view --json number,labels,assignees`. If there is one:
   - Run `git diff origin/main...HEAD` and choose the labels from the table in [`copilot-instructions.md`](../../copilot-instructions.md#pull-requests), based on all of the changes.
   - Update the labels with `gh pr edit <n> --add-label "<label>"` and `--remove-label "<label>"`.
   - If `michel7x` is not assigned, run `gh pr edit <n> --add-assignee michel7x`.
7. Report the branch, the remote, and any label or assignee changes.

Don't open a pull request. That is a separate request.
