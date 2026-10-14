---
name: write-tests
description: Write or improve pytest tests for a module or behaviour
argument-hint: Module path, function, or behaviour
disable-model-invocation: true
---

# Write tests

Write pytest tests for the module, function, or behaviour named in the user's request or arguments.

- Follow the testing rules in `AGENTS.md` and the `tests/` instructions.
- Cover the happy path, edge cases (empty, boundary, invalid input), and error paths.
- Use `parametrize` for tables of cases and keep tests offline and deterministic.
- Run `uv run pytest --cov=anvil --cov-report=term-missing` and report the coverage change for the target.
- Don't modify production code unless a bug is found. If one is, stop and report it.
