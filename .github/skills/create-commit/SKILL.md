---
name: create-commit
description: Stage changes and create one commit with a Commitizen-format message. Use only when the developer explicitly asks to create a commit or commit changes.
argument-hint: "[what to commit]"
---

# Create a commit

1. Run `git status` and `git diff`, and read what changed.
2. If the current branch is `main`, stop and offer to create a branch. Don't commit to `main`.
3. Stage specific paths with `git add <path>`.
   - Include only the changes the developer asked to commit.
   - Keep `pyproject.toml` and `uv.lock` together.
   - If unrelated changes are mixed in, propose separate commits and ask which to make.
4. Run `git diff --staged` and check it for secrets, `.env` files, and credentials. If you find any, stop and warn the developer.
5. Write the message from the staged diff, following [`git-message-format.md`](../../git-message-format.md).
6. Validate the message:

   ```bash
   uvx --from commitizen cz check --message "<message>"
   ```

   This check does not reject `bump` commits or check subject casing, so confirm those rules yourself.
7. Run `git commit -m "<header>"`, adding `-m "<body>"` and `-m "<footer>"` if the message has them.
8. If a pre-commit hook fails, report the exact failure. If a hook reformatted files, review those changes, stage them again, and create the commit again. Never use `--no-verify` or `--amend`.
9. Report the commit hash and subject.

Don't push. Pushing is a separate request.
