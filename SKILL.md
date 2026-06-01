---
name: "vizantu-documentacao"
description: "Use when the task involves Vizantu's operation, client context, content strategy, ClickUp workflow, internal POPs, approved decisions, automations, or maintaining the living documentation in this repository. Read the relevant base files and the specific client context before proposing actions or generating deliverables."
---

# Vizantu Documentacao

Use this skill as the operating manual for Vizantu. The repository is the source of truth for client context, approved decisions, POPs, automation ideas, and operational updates.

## Core rules

- Never store documentation from other technical projects here, especially `vizantu-os`.
- Read only the files needed for the current task.
- Before generating anything for a client, read that client's `clientes/[slug]/context-[slug].md`.
- If a client context is still a template or has missing sections, explicitly say what is unknown instead of inventing details.
- When the user asks to preserve a new learning, update the correct file in this repository instead of leaving the insight only in chat.

## Quick routing

Choose the smallest set of files that answers the request:

- Operational overview, current team, and global understanding:
  `01-contexto-atual.md`
- Incremental learnings discovered in conversation:
  `02-descobertas-da-conversa.md`
- Decisions that were explicitly approved:
  `03-decisoes-aprovadas.md`
- Standard operating procedures, task patterns, delivery structure, and workflow rules:
  `04-pops.md`
- Automation ideas and approved automations:
  `05-automacoes.md`
- Problems, opportunities, and future improvements:
  `06-backlog-de-otimizacao.md`

For client work, also read the matching file under `clientes/[slug]/`.

## Client workflow

When the request is client-specific:

1. Identify the client slug.
2. Read `clientes/[slug]/context-[slug].md` first.
3. If the task involves execution standards, also read `04-pops.md`.
4. If there are deliverables in the client folder such as reports, strategies, or campaign files, read only the files relevant to the ask.
5. Ground every recommendation in the documented context: market, audience, tone of voice, channels, offers, and operational constraints.

If no client slug is obvious, inspect the `clientes/` directory and infer the best match from the client name.

## Documentation update workflow

When the user wants to register new information, use this routing:

- New fact about Vizantu's current operation -> `01-contexto-atual.md`
- New learning discovered during discussion -> `02-descobertas-da-conversa.md`
- Approved decision -> `03-decisoes-aprovadas.md`
- New or revised standard procedure -> `04-pops.md`
- Automation requirement or approved automation -> `05-automacoes.md`
- Improvement opportunity, bottleneck, or optimization idea -> `06-backlog-de-otimizacao.md`
- New or revised client intelligence -> `clientes/[slug]/context-[slug].md`

Keep updates concrete, operational, and easy to reuse later.

## Output guidance

- For strategy or content work, stay faithful to the documented client context instead of producing generic marketing advice.
- For operational recommendations, prefer existing POPs and approved decisions over new process invention.
- For ambiguous or missing information, state the gap and propose the minimum next question or documentation update needed.
- When creating new client folders, follow the existing pattern: `clientes/[slug]/context-[slug].md`.

## Repository map

- `clientes/[slug]/context-[slug].md` -> complete client context and operating rules
- `clientes/[slug]/[data]-*.md|html` -> client-specific deliverables, reports, plans, or campaign artifacts
- `CLAUDE.md` -> legacy repository instructions that can help with intent, but prefer `SKILL.md` as the primary entry point for Codex

