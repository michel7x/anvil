"""Placeholder behaviour for commands whose logic is not implemented yet."""

from typing import NoReturn

import typer


def not_implemented(command: str) -> NoReturn:
    """Report that ``command`` is not implemented yet and exit with code 1."""
    typer.echo(f"{command}: not implemented yet", err=True)
    raise typer.Exit(code=1)
