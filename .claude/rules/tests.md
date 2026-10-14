---
description: pytest conventions for the test suite
paths:
  - "tests/**"
---
<!-- GENERATED from .github/instructions/tests.instructions.md by scripts/sync_ai_context.py. Do not edit. -->

# Testing rules

- Use pytest only, not `unittest.TestCase`. Write plain functions named `test_<behaviour>`.
- Mirror the source layout: `src/anvil/foo/bar.py` → `tests/foo/test_bar.py`.
- Structure each test as Arrange / Act / Assert. Assert one behaviour per test, and give it a descriptive name.
- Use `@pytest.mark.parametrize` for input/output tables instead of loops.
- Use the built-in fixtures: `tmp_path` for files, `monkeypatch` for env vars and attributes, `caplog` for logs, and `capsys` for stdout.
- Put shared fixtures in the nearest `conftest.py`. Keep them small and composable.
- Never touch the real network, clock, or filesystem outside `tmp_path`. Mock at the boundary.
- Annotate test functions with `-> None`, and annotate fixture parameters.
- Assert exceptions with `pytest.raises(SpecificError, match="...")`.
