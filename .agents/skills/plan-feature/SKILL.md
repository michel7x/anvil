---
name: plan-feature
description: Explore the codebase and write an implementation plan for a feature
argument-hint: Describe the feature
disable-model-invocation: true
---

# Plan a feature

Plan the following feature. Do not write implementation code yet.

Feature: the one described in the user's request or arguments. If none is given, ask.

Steps:
1. Read `AGENTS.md` and `docs/architecture.md`, and any relevant ADRs in `docs/adr/`.
2. Explore the code the feature touches. Identify existing functions and patterns to reuse.
3. Write the plan to `docs/plans/<short-kebab-name>.md` with these sections:
   - **Context**: why the feature exists and what outcome it should have.
   - **Approach**: the recommended design, plus one sentence on rejected alternatives.
   - **Changes**: the files to create or modify, and what changes in each.
   - **Tests**: new or updated tests, and the edge cases they cover.
   - **Risks / open questions**.
4. If the plan needs an architectural decision, propose an ADR.
5. Summarise the plan and list any questions that need answers before implementation.
