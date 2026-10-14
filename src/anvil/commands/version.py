"""``anvil version``: print the installed version."""

import typer

from anvil import __version__


def version() -> None:
    """Show the Anvil version."""
    typer.echo(f"anvil {__version__}")
