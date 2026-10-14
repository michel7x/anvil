"""``anvil new``: forge a new project scaffold."""

from pathlib import Path
from typing import Annotated

import typer

from anvil.commands._stub import not_implemented


def new(
    name: Annotated[str, typer.Argument(help="Name of the project to create.")],
    template: Annotated[
        str, typer.Option("--template", "-t", help="Template (blueprint) to forge from.")
    ] = "python",
    output: Annotated[
        Path,
        typer.Option("--output", "-o", help="Directory in which the project folder is created."),
    ] = Path("."),
    force: Annotated[
        bool, typer.Option("--force", help="Overwrite the target directory if it exists.")
    ] = False,
) -> None:
    """Forge a new project scaffold from a template."""
    not_implemented("new")
