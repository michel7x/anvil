#!/usr/bin/env bash
# Hand a source-control request to the Source Control Agent (GitHub Copilot CLI, local model).
# Usage, from anywhere in the repository:
#   bash .claude/skills/source-control/handoff.sh "<request in plain words>"
set -euo pipefail

if [[ $# -ne 1 || -z $1 ]]; then
  echo "usage: handoff.sh \"<source-control request>\"" >&2
  exit 2
fi

repo_root=$(git rev-parse --show-toplevel)

# Copilot's non-interactive mode denies any tool request that no rule allows.
# Allow the tools its skills need. The deny rules back up the limits in
# .github/copilot-instructions.md; deny rules win over every allow. Copilot also
# sees .claude/skills/, so the last rules stop it from calling this script again.
COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1 \
COPILOT_PROVIDER_API_KEY= \
COPILOT_PROVIDER_WIRE_API=responses \
COPILOT_MODEL=glm-4.7-flash \
  exec copilot \
    -C "$repo_root" \
    --silent \
    --no-ask-user \
    --allow-tool='shell(git:*)' \
    --allow-tool='shell(gh:*)' \
    --allow-tool='shell(uv:*)' \
    --allow-tool='shell(uvx:*)' \
    --deny-tool='shell(git reset)' \
    --deny-tool='shell(git rebase)' \
    --deny-tool='shell(git restore)' \
    --deny-tool='shell(git clean)' \
    --deny-tool='shell(git filter-repo)' \
    --deny-tool='shell(git merge)' \
    --deny-tool='shell(git tag)' \
    --deny-tool='shell(gh release)' \
    --deny-tool='shell(gh repo)' \
    --deny-tool='shell(gh secret)' \
    --deny-tool='shell(gh workflow)' \
    --deny-tool='shell(uv version)' \
    --deny-tool='shell(uv build)' \
    --deny-tool='shell(uv publish)' \
    --deny-tool='write' \
    --deny-tool='shell(copilot:*)' \
    --deny-tool='shell(bash:*)' \
    --deny-tool='shell(.claude/skills/source-control/handoff.sh)' \
    -p "$1"
