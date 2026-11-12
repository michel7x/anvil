---
name: create-issue
description: Create a GitHub issue for a bug or feature after checking for duplicates. Use only when the developer explicitly asks to create or file an issue.
argument-hint: "[summary]"
---

# Create an issue

1. Search for duplicates with `gh issue list --state all --search "<keywords>"`. If you find a likely duplicate, report it and ask before you continue.
2. Write a short, specific title. Issue titles don't use the commit format.
3. Write the body:
   - **Bug**: steps to reproduce, expected behaviour, actual behaviour, and version (`uv run anvil version`).
   - **Feature**: the problem, the proposal, and acceptance criteria.
4. Use only facts the developer gave you or that you verified. Mark anything unknown as unknown.
5. Check the available labels with `gh label list`. Use only labels that exist, and don't create new ones.
6. Run `gh issue create --title "<title>" --body "<body>"`, adding `--label "<label>"` if a label applies.
7. Report the issue URL.
