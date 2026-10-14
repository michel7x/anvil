---
description: Python coding standards for all source files
paths:
  - "**/*.py"
---
<!-- GENERATED from .github/instructions/python.instructions.md by scripts/sync_ai_context.py. Do not edit. -->

# Python rules

- Target Python 3.14+. Use modern syntax: `X | None`, `list[int]`, `match`, and `typing.Self`. Use `type` aliases where they make types clearer.
- Annotate every parameter and return type. Code must pass `mypy --strict`. Use `cast` only when a comment explains why.
- Import abstract types from `collections.abc` (`Iterable`, `Mapping`, `Callable`).
- Model structured data with `@dataclass(frozen=True, slots=True)`, or with pydantic if the project uses it. Don't pass bare dicts around.
- Use one module-level `logger = logging.getLogger(__name__)`. Log with lazy formatting: `logger.info("x=%s", x)`.
- Catch the narrowest exception you can, and re-raise with `raise ... from err`. Define project exceptions in `exceptions.py`.
- Avoid mutable default arguments and module-level mutable state.
- Use `pathlib.Path` for file paths and context managers (`with`) for resources.
- Order imports stdlib, third-party, first-party (ruff `I` enforces this). Use absolute imports from the package.
- Keep `__main__.py` and CLI layers thin. Put business logic in importable, testable modules.
