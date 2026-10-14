import subprocess
import sys

import pytest
from typer.testing import CliRunner

from anvil import __version__
from anvil.cli import app

runner = CliRunner()


def test_no_args_shows_help_with_all_commands() -> None:
    result = runner.invoke(app, [])

    assert "Usage" in result.output
    for command in ("new", "list", "version"):
        assert command in result.output


@pytest.mark.parametrize("command", ["new", "list", "version"])
def test_command_help(command: str) -> None:
    result = runner.invoke(app, [command, "--help"])

    assert result.exit_code == 0
    assert "Usage" in result.output


def test_new_help_lists_options() -> None:
    result = runner.invoke(app, ["new", "--help"])

    for option in ("--template", "--output", "--force"):
        assert option in result.output


def test_version_prints_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == f"anvil {__version__}"


@pytest.mark.parametrize(
    ("args", "command"),
    [(["new", "demo"], "new"), (["list"], "list")],
)
def test_stub_commands_report_not_implemented(args: list[str], command: str) -> None:
    result = runner.invoke(app, args)

    assert result.exit_code == 1
    assert f"{command}: not implemented yet" in result.output


def test_new_without_name_is_usage_error() -> None:
    result = runner.invoke(app, ["new"])

    assert result.exit_code == 2


def test_verbose_flag_is_accepted() -> None:
    result = runner.invoke(app, ["--verbose", "version"])

    assert result.exit_code == 0


def test_module_entry_point() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "anvil", "--help"], capture_output=True, text=True, check=False
    )

    assert result.returncode == 0
    assert "context-engineering scaffolds" in result.stdout
