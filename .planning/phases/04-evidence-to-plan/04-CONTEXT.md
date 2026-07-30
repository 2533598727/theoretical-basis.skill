# Phase 4: Evidence-to-Plan Enforcement — Discovery Context

**Created:** 2026-07-30
**Source:** User discussion and confirmed `Proceed to Plan`

## Phase Scope

**What this phase builds:**

Make `Theoretical Basis / 理论依据` the proactive core of the workflow. Codex must identify and research theoretical support for its own intended algorithm changes without waiting for the user to keep reminding it. After PASS/PARTIAL, verified evidence must be carried into `$spec-skill` planning so it constrains implementation and verification.

**What this phase does not build:**

- A replacement for `$academic-search` retrieval or `$spec-skill` planning.
- A change to the installed system `$spec-skill` package.
- Permission to plan or implement FAIL decisions.
- Automatic execution without the normal spec-skill user-confirmation checkpoint.

## Design Decisions

### Decision 1: Theoretical Basis remains the core

- **Context:** The user does not want to chase the AI with repeated requests for theory.
- **Options considered:** Make evidence optional in plans; let spec-skill request research; keep Theoretical Basis proactive.
- **Decision:** Theoretical Basis detects intended behavior-affecting work before planning or editing and owns PASS/PARTIAL/FAIL.
- **Rationale:** Search and planning tools are supporting capabilities; neither can judge scientific applicability.

### Decision 2: Evidence becomes an operational handoff

- **Context:** A citation report can be ignored during implementation.
- **Options considered:** Attach bibliography only; add a structured evidence handoff that controls plan fields.
- **Decision:** Produce an evidence handoff with claims, sources, risk, supported scope, forbidden scope, assumptions, limitations, and validation predictions.
- **Rationale:** Each field maps to a concrete spec artifact and can be verified mechanically or behaviorally.

### Decision 3: FAIL and deviations fail closed

- **Context:** Planning can accidentally make unsupported work look authorized.
- **Decision:** FAIL may create research/blocker/checkpoint work only. PARTIAL may plan only supported scope. Any new substantive execution deviation returns to the evidence gate.
- **Rationale:** The planning layer must preserve, not weaken, the original gate.

## User Preferences

- **Core behavior:** AI proactively finds theory for its own changes.
- **Search integration:** `$academic-search` may retrieve but not judge.
- **Planning integration:** `$spec-skill` must turn evidence into executable constraints.

## Assumptions

- `$spec-skill` may be unavailable in some environments; the Skill must report this and still produce a portable evidence handoff.
- No change to spec-skill's own files is required; compatibility is instruction-based.

## Open Questions Resolved

- **Q:** Who owns the final decision?
  **A:** `$theoretical-basis` always owns evidence classification and gate status.
- **Q:** Does the user need to request theory explicitly?
  **A:** No. Intended behavior-affecting research changes trigger the gate proactively.

## Constraints

- Preserve the two-pass search bound and explicit hypothesis authorization.
- Preserve spec-skill Ask-Plan-Execute confirmation checkpoints.
- Keep README bilingual and runtime files synchronized after validation.

## References

- `.planning/PROJECT.md`
- `.planning/DOMAIN.md`
- `.planning/USE_CASES.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `C:/Users/25335/.codex/skills/spec-skill/SKILL.md`

