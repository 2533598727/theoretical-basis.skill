# Project State

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-08-01)

**Core value:** Never implement an unsupported behavior-affecting research change without adequate evidence or explicit authorization for a falsifiable hypothesis experiment.
**Current focus:** v1.3.0 released — evidence-grounded engineering discipline complete

## Current Position

Phase: 5 of 5 (Evidence-Grounded Engineering Discipline)
Plan: 1 of 1 in current phase
Status: Complete
Last activity: 2026-08-01 — v1.3.0 validated, synchronized to Codex and Claude, pushed through proxy, and verified against remote `main`

Progress: [██████████] 100%

## Performance Metrics

**Velocity:**
- Total plans completed: 5
- Average duration: 15 min
- Total execution time: 1.35 hours

## Accumulated Context

### Decisions

- Optimize runtime policy and repository engineering together.
- Preserve root-level Skill structure and `$theoretical-basis` name.
- Execute policy, eval, and release phases sequentially.
- High-risk PASS requires primary evidence plus independent corroboration.
- Search stops after two documented passes; generic continuation cannot authorize a hypothesis.
- Twelve scenario cases plus independent forward tests define the behavior gate.
- One validator entry point is shared by local verification and read-only CI.
- The public repository uses MIT with `Copyright (c) 2026 2533598727`.
- README is bilingual distribution guidance; runtime policy remains canonical in `SKILL.md` and the evidence protocol.
- Only the three required runtime files are synchronized into the installed Skill, with SHA-256 equality checked before release.
- `$theoretical-basis` remains the proactive core; users do not need to repeatedly request theory searches.
- `$academic-search` is the retrieval layer and `$spec-skill` is the planning/execution layer; neither may issue or bypass the evidence gate.
- Verified evidence must become planning constraints and tests, not a detached citation report.
- PASS/PARTIAL produces a bounded Evidence Handoff; FAIL produces no implementation handoff.
- New substantive execution deviations return to the evidence gate before editing continues.
- Integrate compatible Karpathy-style rules directly into Theoretical Basis rather than require the external Skill at runtime.
- Ask only about decision-relevant ambiguity; do not turn caution into ceremonial blocking.
- Define minimality conceptually: the least complex implementation satisfying evidence scope, safety, tests, and necessary wiring.
- Treat the external repository as attributed engineering inspiration, not theoretical evidence or a gate authority.
- Target plugin/runtime version 1.3.0 and preserve Codex plus Claude Code host compatibility.

### Pending Todos

- None for v1.3.0.

### Blockers/Concerns

- `multica-ai/andrej-karpathy-skills` snapshot `2c606141936f1eeef17fa3043a72095b4765b9c2` declares MIT in README and Skill frontmatter but contains no standalone `LICENSE`; use attribution and original wording rather than verbatim copying.
- Clarification evidence is mainly function-level code generation; apply it only to ambiguities that can change gate or behavior and avoid universal performance claims.
- Code-review-graph parses the Python validator but not the Markdown/YAML policy surface, so impact coverage combines graph inspection with repository text search.

### Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| Evaluation | Cross-model automated scoring | v2 | Initial planning |
| Distribution | Marketplace/package release | v2 | Initial planning |

## Session Continuity

Last session: 2026-08-01
Stopped at: v1.3.0 release complete; remote `main` verified
Resume file: `.planning/phases/05-engineering-discipline/05-01-SUMMARY.md`
