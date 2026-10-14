"""Typer application: global options and command registration."""

import logging
from typing import Annotated

import typer

from anvil.commands.list_templates import list_templates
from anvil.commands.new import new
from anvil.commands.version import version

app = typer.Typer(
    name="anvil",
    help="Forge context-engineering scaffolds for AI coding agents.",
    no_args_is_help=True,
    add_completion=False,
)


@app.callback()
def main(
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable debug logging.")] = False,
) -> None:
    """Forge context-engineering scaffolds for AI coding agents."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )


app.command()(new)
app.command(name="list")(list_templates)
app.command()(version)
