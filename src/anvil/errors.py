"""Project exceptions. Raise these from core logic; the CLI maps them to exit codes."""


class AnvilError(Exception):
    """Base class for all Anvil errors."""
