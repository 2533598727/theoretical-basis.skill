---
phase: 01-evidence-contract
plan: 01
subsystem: policy
tags: [evidence-gate, research-safety, hypothesis-testing, source-validation]
requires: []
provides:
  - Risk-proportional evidence thresholds and basis taxonomy
  - Bounded two-pass search with hostile-source safeguards
  - Explicit hypothesis authorization and complete experiment preregistration
affects: [02-behavioral-verification, 03-distribution-release]
tech-stack:
  added: []
  patterns: [risk-proportional gate, two-pass search, frozen experiment protocol]
key-files:
  created: []
  modified: [SKILL.md, references/evidence-protocol.md]
key-decisions:
  - "Mechanical changes bypass literature search only after behavior preservation is demonstrated"
  - "High-risk PASS requires primary evidence plus independent corroboration"
  - "Search stops after two documented passes"
  - "Generic continuation never authorizes an unsupported hypothesis"
patterns-established:
  - "Scope -> Risk -> Basis -> Search -> Gate -> Allowed action"
  - "FAIL -> Researcher source check -> Explicit hypothesis authorization -> Preregistered experiment"
requirements-completed: [SCOPE-01, EVID-01, EVID-02, REPT-01, SRCH-01, SAFE-01, HYP-01, EXPT-01]
domain-trace:
  interaction_gate: required
  use_cases: [UC-001, UC-002, UC-003, UC-004]
  actors: [Researcher, Codex Agent]
  concepts: [Change Proposal, Evidence Claim, Evidence Source, Search Pass, Gate Decision, Research Hypothesis, Experiment Protocol]
  derived_access_rules_verified:
    - "Researcher may provide sources and explicitly authorize hypothesis testing"
    - "Codex Agent cannot self-authorize unsupported behavior changes"
    - "Codex Agent cannot implement a FAIL decision"
duration: 10min
completed: 2026-07-30
---

# Phase 1: Evidence Contract Summary

**Risk-tiered evidence decisions, bounded source-safe search, and frozen hypothesis experiments now make unsupported changes predictably non-executable.**

## Performance

- **Duration:** 10 min
- **Completed:** 2026-07-30T10:01:13+08:00
- **Tasks:** 3
- **Files modified:** 2

## Accomplishments

- Added mechanical/behavior-affecting scope classification, low/medium/high risk tiers, five basis types, and risk-proportional PASS thresholds.
- Replaced open-ended browsing with two search passes, a required search log, source-context verification, retraction/conflict checks, and untrusted-content safeguards.
- Required explicit unsupported-hypothesis authorization and preregistered metrics, seeds, holdout isolation, uncertainty, multiple comparisons, budget, and stopping rules.

## Domain Trace Evidence

| Trace Item | Code Artifact(s) | Verification Evidence |
|------------|------------------|-----------------------|
| Actor: Researcher | `SKILL.md` | Receives scope/risk/gate report; asked for sources after Pass 2; controls hypothesis authorization |
| Actor: Codex Agent | `SKILL.md`, `references/evidence-protocol.md` | Implements only PASS/PARTIAL allowed action; FAIL remains paused |
| Use Cases: UC-001/UC-002 | Both policy files | Scope, search, source safety, evidence record, and gate fields are present |
| Use Cases: UC-003/UC-004 | Both policy files | Generic continuation is rejected; explicit authorization precedes preregistration and minimal implementation |
| Derived access | Both policy files | Unsupported patch prohibition remains explicit and validated |

## Task Commits

1. **Define evidence risk and PASS thresholds** — `58685c7`
2. **Bound and secure evidence search** — `feeac53`
3. **Preregister unsupported hypothesis tests** — `4388032`

**Planning baseline:** `f6325dd`

## Files Modified

- `SKILL.md` — Runtime scope, risk, search, gate, authorization, experiment, and reporting workflow.
- `references/evidence-protocol.md` — Canonical source taxonomy, thresholds, safety rules, search log, evidence record, and preregistration schema.

## Decisions Made

- Treat unverified refactors as behavior-affecting rather than mechanical.
- Require corroboration proportionate to scientific consequence.
- Disallow a silent third search pass and return control to the researcher.
- Freeze experimental success criteria before results are observed.

## Deviations from Plan

None — all three tasks executed as approved.

## Issues Encountered

- A verification assertion initially matched curly quotation marks too literally in the PowerShell pipeline; the file content was correct, and the assertion was changed to an encoding-independent semantic check. No product file change was required.

## User Setup Required

None.

## Verification Evidence

- Official Skill quick validation: PASS
- UTF-8 decode and replacement-character check: PASS
- Old Skill name absence: PASS
- PASS/PARTIAL/FAIL and unsupported-patch prohibition: PASS
- Phase 1 requirement clause coverage: 8/8 PASS
- Git diff whitespace check: PASS

## Self-Check: PASSED

- All task acceptance criteria were rerun after the final production commit.
- All three task commits exist in Git history.
- Both modified artifacts exist and the `SKILL.md` protocol link is intact.
- Actor, use-case, concept, and denied-action traces match the approved plan.

## Next Phase Readiness

- Phase 2 can now encode deterministic scenario expectations from the stabilized policy contract.
- No blocker prevents eval, validator, or CI implementation.

---
*Phase: 01-evidence-contract*
*Completed: 2026-07-30*
