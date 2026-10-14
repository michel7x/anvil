"""PostToolUse hook: format and lint-fix a Python file after Claude edits it."""

import json
import subprocess
import sys
from pathlib import Path

payload = json.load(sys.stdin)
path = payload.get("tool_input", {}).get("file_path", "")
if path.endswith(".py"):
    venv_ruff = Path(__file__).resolve().parents[2] / ".venv" / "bin" / "ruff"
    ruff = [str(venv_ruff)] if venv_ruff.exists() else ["uv", "run", "--quiet", "ruff"]
    subprocess.run([*ruff, "format", "--quiet", path], check=False)
    subprocess.run([*ruff, "check", "--fix", "--quiet", path], check=False)
