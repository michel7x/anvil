"""``anvil new``: forge a context-engineering scaffold for a project."""

from pathlib import Path
from typing import Annotated

import typer

from anvil.commands._stub import not_implemented


def new(
    name: Annotated[str, typer.Argument(help="Name of the project to scaffold.")],
    template: Annotated[
        str, typer.Option("--template", "-t", help="Blueprint to forge from (target stack).")
    ] = "python",
    output: Annotated[
        Path,
        typer.Option("--output", "-o", help="Directory in which the project folder is created."),
    ] = Path("."),
    force: Annotated[
        bool, typer.Option("--force", help="Overwrite the target directory if it exists.")
    ] = False,
) -> None:
    """Forge a context-engineering scaffold for a new project from a blueprint."""
    not_implemented("new")
