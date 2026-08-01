# Phase 5 Context: Evidence-Grounded Engineering Discipline

**Defined:** 2026-08-01
**Status:** Ready for execution planning
**Depends on:** Phase 4, released v1.2.0 host compatibility

## User intent

Integrate the useful overlap from [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) into `theoretical-basis` so an agent does not stop at finding evidence. The supported implementation should also expose material assumptions, avoid over-engineering, touch only authorized scope, and verify a predefined goal.

## Locked decisions

- Internalize compatible behavior in the canonical `SKILL.md`; do not require Karpathy Guidelines as a runtime dependency.
- Keep `$theoretical-basis` as the sole owner of scope classification, evidence applicability, and PASS/PARTIAL/FAIL.
- Treat Karpathy Guidelines as attributed engineering inspiration, not theoretical evidence.
- Ask questions only for decision-relevant ambiguity: competing interpretations that can change evidence claims, gate outcome, allowed scope, or behavior.
- For clear work, state any reasonable assumption and continue without ceremonial confirmation.
- Define minimality conceptually, not by raw line count: choose the least complex candidate that satisfies supported scope, safety, tests, documentation, and necessary wiring.
- Require line- or hunk-level change traceability to the researcher request, Evidence Handoff, necessary integration, or cleanup newly caused by the change.
- Do not edit unrelated pre-existing cleanup; report it separately.
- Freeze evidence-derived success and failure criteria before implementation and reject post-hoc goal movement.
- Bump the behavior contract to v1.3.0 while preserving Codex, Claude personal Skill, and Claude plugin invocation.

## Explicitly forbidden

- No claim that the four-rule prompt universally improves all coding agents.
- No performance percentage derived from the external repository unless independently verified for this Skill.
- No verbatim wholesale copy of the external Skill.
- No requirement to ask the researcher about obvious, low-risk, unambiguous work.
- No use of simplicity or surgical scope to omit required tests, safety checks, documentation, Evidence Handoff constraints, or fresh re-gating.
- No external engineering Skill may issue, upgrade, replace, or bypass PASS/PARTIAL/FAIL.

## Code context

- Repository snapshot at planning: `7008ba6dc3824887f57271ab6eb5dae6125ab899`.
- code-review-graph was initially empty, then rebuilt successfully at this snapshot.
- The graph parsed `scripts/validate_skill.py` as one Python file with 13 nodes and 241 edges.
- Markdown and YAML policy surfaces were not represented in the graph, so impact analysis also used direct inspection of `SKILL.md`, `references/evidence-protocol.md`, `evals/cases.yaml`, `README.md`, and planning files.
- The validator currently owns policy-clause checks, required integration repositories, scenario tags, integration-case expectations, and negative mutations.

## Target behavior examples

### Material ambiguity

If “replace normalization” could mean changing only numerical implementation or changing the mathematical estimator, the agent names the two interpretations and asks the smallest question needed before defining evidence claims.

### Clear supported work

If the Evidence Handoff already names the exact symbol, mechanism, and supported transformation, the agent does not ask the user to reconfirm those facts. It chooses the least complex implementation and proceeds after the normal plan checkpoint.

### Surgical implementation

If the target file contains unrelated dead code, the agent mentions it but leaves it unchanged. If the authorized edit makes one import unused, that newly orphaned import is removed in the same patch.

### Fixed verification

Before editing, the plan states which invariant, regression test, and evidence-derived prediction must pass or fail. Observed results cannot redefine those criteria.

## Release target

- Plugin/runtime version: `1.3.0`
- Behavior scenarios: 29 total after six additions
- Negative policy mutations: 19 total after five additions
- Distribution: repository, Codex installed Skill, Claude personal Skill, Claude plugin manifest, bilingual README

