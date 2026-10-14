"""Generate Claude Code context files from their tool-neutral / Copilot sources.

Sources (edit these):
    .github/instructions/*.instructions.md  ->  .claude/rules/*.md
    .agents/skills/<name>/**                ->  .claude/skills/<name>/**  (mirrored)

Usage:
    uv run python scripts/sync_ai_context.py          # write generated files
    uv run python scripts/sync_ai_context.py --check  # exit 1 if out of date
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTRUCTIONS_DIR = ROOT / ".github/instructions"
INSTRUCTIONS_SUFFIX = ".instructions.md"
RULES_DIR = ROOT / ".claude/rules"
SKILLS_SRC = ROOT / ".agents/skills"
SKILLS_DST = ROOT / ".claude/skills"
MARKER = "GENERATED from"


def split_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    """Parse simple ``key: value`` YAML frontmatter; return (fields, raw block, body)."""
    if not text.startswith("---\n"):
        return {}, "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, "", text
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t", "#")):
            fields[key.strip()] = value.strip().strip("'\"")
    return fields, text[: end + 5], text[end + 5 :].lstrip("\n")


def banner(source: Path) -> str:
    rel = source.relative_to(ROOT).as_posix()
    return f"<!-- {MARKER} {rel} by scripts/sync_ai_context.py. Do not edit. -->\n"


def render_rule(source: Path) -> str:
    fields, _, body = split_frontmatter(source.read_text(encoding="utf-8"))
    out = ["---"]
    if description := fields.get("description"):
        out.append(f"description: {description}")
    if apply_to := fields.get("applyTo"):
        out.append("paths:")
        out.extend(f'  - "{glob.strip()}"' for glob in apply_to.split(",") if glob.strip())
    out.append("---")
    return "\n".join(out) + "\n" + banner(source) + "\n" + body.rstrip("\n") + "\n"


def render_skill_file(source: Path) -> bytes:
    if source.name != "SKILL.md":
        return source.read_bytes()
    _, frontmatter, body = split_frontmatter(source.read_text(encoding="utf-8"))
    return (frontmatter + banner(source) + "\n" + body).encode("utf-8")


def expected_files() -> dict[Path, bytes]:
    files: dict[Path, bytes] = {}
    for src in sorted(INSTRUCTIONS_DIR.glob(f"*{INSTRUCTIONS_SUFFIX}")):
        name = src.name.removesuffix(INSTRUCTIONS_SUFFIX) + ".md"
        files[RULES_DIR / name] = render_rule(src).encode("utf-8")
    for src in sorted(p for p in SKILLS_SRC.rglob("*") if p.is_file()):
        files[SKILLS_DST / src.relative_to(SKILLS_SRC)] = render_skill_file(src)
    return files


def stale_files(expected: dict[Path, bytes]) -> list[Path]:
    """Files that are missing, differ, or are orphaned generated outputs."""
    stale = [p for p, c in expected.items() if not p.exists() or p.read_bytes() != c]
    for rule in RULES_DIR.glob("*.md"):
        if rule not in expected and MARKER in rule.read_text("utf-8"):
            stale.append(rule)
    # .claude/skills is entirely generated: anything without a source is an orphan.
    stale.extend(p for p in SKILLS_DST.rglob("*") if p.is_file() and p not in expected)
    return stale


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    parser.add_argument("--check", action="store_true", help="fail if files are out of date")
    args = parser.parse_args(argv)

    expected = expected_files()
    stale = stale_files(expected)
    if args.check:
        for path in stale:
            print(f"out of date: {path.relative_to(ROOT)}", file=sys.stderr)
        if stale:
            print("run: uv run python scripts/sync_ai_context.py", file=sys.stderr)
        return 1 if stale else 0

    for path in stale:
        if path in expected:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected[path])
            print(f"wrote   {path.relative_to(ROOT)}")
        else:
            path.unlink()
            print(f"removed {path.relative_to(ROOT)}")
    for directory in sorted(SKILLS_DST.rglob("*"), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
