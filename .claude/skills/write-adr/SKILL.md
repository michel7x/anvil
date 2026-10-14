---
name: write-adr
description: Record an architecture decision as a numbered ADR in docs/adr/. Use when a change introduces or alters a framework, data store, external service, module boundary, or other hard-to-reverse design choice.
---
<!-- GENERATED from .agents/skills/write-adr/SKILL.md by scripts/sync_ai_context.py. Do not edit. -->

# Write an ADR

1. List `docs/adr/` and choose the next number. Use four digits, for example `0007`.
2. Copy [template.md](template.md) to `docs/adr/NNNN-short-kebab-title.md`.
3. Fill in every section. Keep it to about a page:
   - **Context**: the forces and constraints, stated as facts.
   - **Decision**: "We will ...", in active voice.
   - **Alternatives considered**: one or two lines each, with the reason each was rejected.
   - **Consequences**: positive, negative, and follow-up work.
4. Set the status to `Proposed`. A human changes it to `Accepted`.
5. If the ADR supersedes an earlier one, set the old ADR's status to `Superseded by NNNN`. Don't change anything else in it.
6. If the decision changes the stack, commands, or layout, update `AGENTS.md` and `docs/architecture.md` too.
