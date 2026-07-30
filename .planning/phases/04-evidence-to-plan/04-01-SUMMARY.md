---
phase: 04-evidence-to-plan
plan: 01
subsystem: skill-policy
tags: [theoretical-basis, academic-search, spec-skill, evidence-handoff, evals]

requires:
  - phase: 03-distribution-release
    provides: Verified bilingual Skill release and synchronized installation
provides:
  - Proactive evidence-gate triggering for agent-intended research changes
  - PASS/PARTIAL Evidence Handoff mapped into spec planning and verification
  - Fail-closed execution re-gating and 20-scenario evaluation coverage
affects: [research-change-planning, skill-evaluation, installed-runtime]

tech-stack:
  added: []
  patterns: [proactive evidence gate, evidence-to-plan handoff, fail-closed execution re-gate]

key-files:
  created: []
  modified: [SKILL.md, references/evidence-protocol.md, agents/openai.yaml, evals/cases.yaml, scripts/validate_skill.py, README.md]

key-decisions:
  - "Theoretical Basis remains the proactive core and sole PASS/PARTIAL/FAIL owner."
  - "Academic Search retrieves, while spec-skill operationalizes only verified supported scope."
  - "FAIL and unsupported PARTIAL scope cannot become implementation tasks."

patterns-established:
  - "Evidence Handoff: verified evidence becomes read_first, bounded actions, acceptance criteria, must_haves, and verification."
  - "Execution re-gate: new substantive deviations stop before editing and return to Theoretical Basis."

requirements-completed: [AUTO-01, HAND-01, PLAN-01, EXEC-01]
domain-trace:
  interaction_gate: required
  use_cases: [UC-007]
  actors: [Codex Agent, Researcher, Skill Maintainer]
  concepts: [Change Proposal, Gate Decision, Evidence Handoff, Planning Artifact, Evaluation Case]
  derived_access_rules_verified:
    - "allowed: Codex Agent creates planning constraints from PASS/PARTIAL supported scope"
    - "denied: FAIL and unsupported PARTIAL scope do not produce implementation work"
    - "denied: new substantive execution deviations do not bypass a fresh evidence gate"

duration: 20min
completed: 2026-07-30
---

# Phase 4: Evidence-to-Plan Enforcement Summary

**Theoretical Basis now triggers proactively and carries verified evidence into bounded spec plans, tests, and execution stopping rules.**

## Performance

- **Duration:** 20 min
- **Started:** 2026-07-30T12:12:00+08:00
- **Completed:** 2026-07-30T12:32:46+08:00
- **Tasks:** 3
- **Files modified:** 6 repository files plus 3 synchronized installed runtime files

## Accomplishments

- Added mandatory proactive triggering and kept `$theoretical-basis` as the sole evidence-gate owner.
- Defined Evidence Handoff fields and mapped them into `$spec-skill` planning, tests, confirmation, and execution re-gating.
- Expanded evaluation from 15 to 20 cases, added three integration tags, and increased negative policy mutations from 4 to 9.
- Updated the bilingual README with a direct three-Skill workflow and synchronized the installed runtime byte-for-byte.

## Domain Trace Evidence

| Trace Item | Code Artifact(s) | Verification Evidence |
|------------|------------------|-----------------------|
| Actor: Codex Agent | `SKILL.md`, `scripts/validate_skill.py` | Proactive trigger and fail-closed clauses are required by validator mutations |
| Actor: Researcher | `SKILL.md`, `references/evidence-protocol.md` | Normal spec plan confirmation and explicit hypothesis authorization remain mandatory |
| Use Case: UC-007 | `evals/cases.yaml` | PASS, PARTIAL, FAIL, proactive-trigger, spec-handoff, and execution-regate cases pass |
| Concept: Evidence Handoff | `references/evidence-protocol.md` | Complete schema and plan-field mapping validated |
| Derived access: PASS/PARTIAL supported scope may enter planning | `SKILL.md`, `evals/cases.yaml` | PASS and PARTIAL forward/eval cases produce bounded planning behavior |
| Derived access: FAIL and deviations cannot bypass the gate | `SKILL.md`, `scripts/validate_skill.py` | FAIL pressure test refused implementation planning; re-gate clause is mutation-tested |

## Task Commits

1. **Task 1: Define proactive evidence handoff and planning enforcement** - `a91e993`
2. **Task 2: Add fail-closed integration evaluation** - `7ebbb05`
3. **Task 3: Document, synchronize, and publish the integration** - `1c97ce5`

**Plan metadata:** `eb223fc`

## Files Created/Modified

- `SKILL.md` - proactive core, planning handoff, FAIL/PARTIAL boundaries, and execution re-gate
- `references/evidence-protocol.md` - Evidence Handoff schema and spec field mapping
- `agents/openai.yaml` - generated UI metadata naming both subordinate integrations
- `evals/cases.yaml` - 20 behavior scenarios
- `scripts/validate_skill.py` - integration tags, policy clauses, required cases, and 9 negative mutations
- `README.md` - humanized Chinese and English three-Skill workflow

## Decisions Made

- Theoretical Basis owns evidence applicability and gate status; retrieval and planning Skills remain subordinate.
- PASS and PARTIAL authorize planning only within supported scope, never automatic execution.
- A new mechanism, assumption, metric, data meaning, or evaluation rule discovered during execution is a new proposal.

## Deviations from Plan

None - the approved scope and three-task sequence were preserved.

## Issues Encountered

- The official metadata generator and validator needed UTF-8 mode and PyYAML in the local Windows environment. The generator was run with its supported `--name` option, and PyYAML was isolated in a temporary validation directory rather than installed globally.
- The first UTF-8 scan included an ignored Python bytecode file; the release scan was corrected to validate every tracked file plus all modified runtime files.

## User Setup Required

None - no external service configuration required.

## Verification Evidence

- Repository validator: PASS
- Evaluation coverage: PASS, 20 cases
- Negative self-test: PASS, 9 policy mutations rejected
- Official Skill validation: PASS for repository and installed copy
- Spec trace validation: PASS
- Independent forward tests: proactive request paused for evidence; PASS produced a bounded handoff and confirmation stop; FAIL pressure refused implementation planning
- Installed runtime SHA-256: all three files match repository bytes
- Remote `main`: `1c97ce51e9ba6c1879e0c1d2d8806d3a4420c021`, equal to local HEAD at release

## Next Phase Readiness

Phase 4 implementation is complete and ready for formal phase verification and transition. No blockers remain.

## Self-Check: PASSED

---
*Phase: 04-evidence-to-plan*
*Completed: 2026-07-30*
