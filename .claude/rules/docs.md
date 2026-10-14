---
description: Conventions for Markdown documentation
paths:
  - "docs/**"
  - "**/*.md"
---
<!-- GENERATED from .github/instructions/docs.instructions.md by scripts/sync_ai_context.py. Do not edit. -->

# Documentation rules

- Write for a new contributor: lead with the purpose, then how, then details.
- Use sentence-case headings, short paragraphs, and fenced code blocks with a language tag.
- Commands must be copy-pasteable and use `uv run ...`.
- Architecture decisions go in `docs/adr/NNNN-title.md`, following `docs/adr/0000-template.md`. Never rewrite an accepted ADR. Supersede it with a new one.
- When a change affects commands, layout, or conventions, update `AGENTS.md` in the same change.
- Don't duplicate content across files. Link to the canonical source instead.
