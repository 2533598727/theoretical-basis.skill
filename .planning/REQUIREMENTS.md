# Requirements: Theoretical Basis Skill Optimization

**Defined:** 2026-07-30
**Core Value:** Never implement an unsupported behavior-affecting research change without adequate evidence or explicit authorization for a falsifiable hypothesis experiment.
**Interaction Gate:** Required
**Domain Model:** `.planning/DOMAIN.md`
**Use Cases:** `.planning/USE_CASES.md`

## v1 Requirements

### Evidence gate

- [x] **SCOPE-01**: Researcher receives an explicit mechanical-versus-behavior-affecting classification before evidence search. (Use case: UC-001; Concepts: Change Proposal)
- [x] **EVID-01**: Researcher receives a low/medium/high risk tier with deterministic evidence thresholds. (Use case: UC-001; Concepts: Evidence Claim, Gate Decision)
- [x] **EVID-02**: Agent distinguishes theory, derivation, empirical evidence, expert practice, and informal observation and never treats the latter categories as automatic theoretical PASS. (Use cases: UC-001, UC-003; Concepts: Evidence Claim, Evidence Source)
- [x] **REPT-01**: Every gate report records scope, risk, basis type, claim, applicability, contradictions, confidence, and allowed action. (Use case: UC-002; Concepts: Gate Decision)

### Search and safety

- [x] **SRCH-01**: Agent performs no more than two defined search passes before reporting queries, sources, exclusions, and insufficiency to the researcher. (Use case: UC-002; Concepts: Search Pass)
- [x] **SAFE-01**: Agent treats all external source content as untrusted data, ignores embedded instructions, and does not execute source code or commands without independent task-scoped review. (Use case: UC-002; Concepts: Evidence Source)

### Hypothesis and experiment

- [x] **HYP-01**: Agent requires explicit researcher authorization after evidence search and researcher source check before creating an unsupported hypothesis. (Use cases: UC-003, UC-004; Concepts: Research Hypothesis)
- [x] **EXPT-01**: Agent preregisters prediction, baseline, controls, ablations, primary metric, failure threshold, seeds/runs, holdout isolation, uncertainty, multiple comparisons, budget, and stopping rule before implementation. (Use case: UC-004; Concepts: Experiment Protocol)

### Evaluation and engineering

- [ ] **EVAL-01**: Maintainer can run at least ten behavior scenarios covering PASS, PARTIAL, FAIL, forum-only, conflicts, inapplicability, generic continuation, explicit authorization, mechanical change, and hostile-source content. (Use case: UC-005; Concepts: Evaluation Case)
- [ ] **EVAL-02**: Automated validation checks Skill metadata, required policy clauses, eval schema, stale names, documentation links, UTF-8, and repository cleanliness in CI. (Use case: UC-005; Concepts: Release Artifact)
- [ ] **DOCS-01**: Maintainer has concise bilingual documentation whose policy summary cannot silently diverge from the runtime contract. (Use case: UC-006; Concepts: Release Artifact)
- [ ] **DIST-01**: Repository includes a user-approved open-source license and accurate cross-platform installation instructions. (Use case: UC-006; Concepts: Release Artifact)
- [ ] **REL-01**: Release process validates, commits atomically, synchronizes the installed Skill, verifies hashes, pushes `main`, and confirms remote commit identity. (Use case: UC-006; Concepts: Release Artifact)

## v2 Requirements

- **EVAL-03**: Automate model-backed eval scoring across multiple Codex model families.
- **DIST-02**: Package and publish the Skill through a marketplace or release archive.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Full paper retrieval/indexing service | External search infrastructure is not part of the Skill |
| Automated costly experiment execution | Requires project-specific authority and resources |
| Universal scientific truth scoring | Applicability is claim- and context-specific |

## Traceability

| Requirement | Actor / Role | Use Case | Domain Concept(s) | Phase | Status |
|-------------|--------------|----------|-------------------|-------|--------|
| SCOPE-01 | Researcher | UC-001 | Change Proposal | Phase 1 | Complete |
| EVID-01 | Researcher | UC-001 | Evidence Claim, Gate Decision | Phase 1 | Complete |
| EVID-02 | Researcher, Codex Agent | UC-001, UC-003 | Evidence Claim, Evidence Source | Phase 1 | Complete |
| REPT-01 | Codex Agent | UC-002 | Gate Decision | Phase 1 | Complete |
| SRCH-01 | Codex Agent | UC-002 | Search Pass | Phase 1 | Complete |
| SAFE-01 | Codex Agent | UC-002 | Evidence Source | Phase 1 | Complete |
| HYP-01 | Researcher, Codex Agent | UC-003, UC-004 | Research Hypothesis | Phase 1 | Complete |
| EXPT-01 | Researcher, Codex Agent | UC-004 | Experiment Protocol | Phase 1 | Complete |
| EVAL-01 | Skill Maintainer | UC-005 | Evaluation Case | Phase 2 | Pending |
| EVAL-02 | Skill Maintainer | UC-005 | Release Artifact | Phase 2 | Pending |
| DOCS-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Pending |
| DIST-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Pending |
| REL-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Pending |

## Derived Access Notes

| Status | Operation | Role(s) | Source Use Case(s) / Reason | Requirement(s) |
|--------|-----------|---------|-----------------------------|----------------|
| allowed | Explicitly authorize hypothesis test | Researcher | UC-004 | HYP-01 |
| denied | Self-authorize unsupported behavior change | Codex Agent | Core invariant | HYP-01 |
| denied | Implement a FAIL decision | Codex Agent | UC-001 | EVID-01 |
| allowed | Publish after checks pass | Skill Maintainer | UC-005, UC-006 | EVAL-02, REL-01 |
| denied | Publish with failed required checks | Skill Maintainer / Codex Agent | Release invariant | REL-01 |

**Coverage:**
- v1 requirements: 13 total
- Mapped to phases: 13
- Unmapped: 0 ✓

---
*Requirements defined: 2026-07-30*
*Last updated: 2026-07-30 after Plan approval*
