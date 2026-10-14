---
description: Typer CLI conventions for the anvil command layer
applyTo: "src/anvil/cli.py,src/anvil/commands/**"
---

# CLI rules (Typer)

- Put one command per module in `src/anvil/commands/`, and register it in `src/anvil/cli.py` with `app.command()`.
- Declare parameters with `Annotated[T, typer.Argument(help=...)]` or `Annotated[T, typer.Option("--long", "-s", help=...)]`. Every parameter has help text.
- The command function's docstring is its help text. Make the first line a short imperative sentence.
- Commands only parse and validate input, call core logic, and render output. Put no business logic here. Core modules must be testable without Typer.
- Print with `typer.echo`, and send errors to stderr with `err=True`. Never use `print`.
- Exit codes: 0 means success, 1 means failure, and 2 means a usage error (Typer raises this itself). Exit with `raise typer.Exit(code=...)`, never `sys.exit`.
- Catch `AnvilError` at the command boundary, report a concise message, and exit with 1. Let unexpected exceptions propagate.
- Test commands with `typer.testing.CliRunner` in `tests/test_cli.py` or `tests/commands/`.
