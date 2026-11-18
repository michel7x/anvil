"""Shared pytest fixtures. Keep fixtures small and composable."""

import pytest
import typer.rich_utils


@pytest.fixture(autouse=True)
def plain_cli_output(monkeypatch: pytest.MonkeyPatch) -> None:
    """Render CLI output without ANSI styles, even when CI forces a terminal.

    Typer forces Rich terminal rendering when ``GITHUB_ACTIONS`` is set, which
    splits option names such as ``--template`` with escape codes.
    """
    monkeypatch.setattr(typer.rich_utils, "FORCE_TERMINAL", False)
