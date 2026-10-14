---
name: review-changes
description: Review the current changes against project conventions
argument-hint: Optional area to focus on
disable-model-invocation: true
---
<!-- GENERATED from .agents/skills/review-changes/SKILL.md by scripts/sync_ai_context.py. Do not edit. -->

# Review changes

Review the current uncommitted changes, or the branch diff against `main` if there are none.
If the user's request or arguments name a focus area, give it extra attention.

Check:
1. **Correctness**: logic errors, unhandled edge cases, error handling, and concurrency.
2. **Conventions**: typing, logging, structure, and naming, as `AGENTS.md` and the scoped instructions describe.
3. **Tests**: is new behaviour tested? Are the tests meaningful and deterministic?
4. **Security**: secrets, injection, unsafe deserialisation, and path traversal.
5. **Docs**: do `AGENTS.md`, the architecture doc, and ADRs need updates?

Report findings ordered by severity, each with `file:line`, the problem, and a suggested fix. Don't edit files.
