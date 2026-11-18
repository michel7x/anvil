#!/usr/bin/env bash
# Smoke-test the anvil CLI: run representative commands, check exit codes and output.
# Run from the repository root:  bash .claude/skills/run-anvil/smoke.sh
# Update the expectations below when a stub command gets implemented.
set -uo pipefail

# Typer forces ANSI output when GITHUB_ACTIONS is set; this turns it off.
export _TYPER_FORCE_DISABLE_TERMINAL=1

fail=0

# check <expected-exit> <expected-output-substring> <anvil args...>
check() {
  local want_code=$1 want_text=$2
  shift 2
  local out code
  out=$(uv run --locked anvil "$@" 2>&1)
  code=$?
  if [[ $code -eq $want_code && $out == *"$want_text"* ]]; then
    echo "PASS  anvil $*  (exit $code)"
  else
    echo "FAIL  anvil $*  (exit $code, want $want_code; want output containing '$want_text')"
    echo "$out" | sed 's/^/      /'
    fail=1
  fi
}

check 0 "anvil $(uv version --short)" version
check 0 "anvil $(uv version --short)" -v version
check 0 "Commands"                  --help
check 2 "Usage: anvil"              # no args: help, exit 2
check 2 "No such command 'bogus'"   bogus
check 1 "list: not implemented yet" list
check 1 "new: not implemented yet"  new demo
check 1 "new: not implemented yet"  new demo --template python --output /tmp/anvil-smoke --force
check 2 "Missing argument 'name'"   new

if [[ $fail -eq 0 ]]; then echo "smoke: all passed"; else echo "smoke: FAILED"; fi
exit $fail
