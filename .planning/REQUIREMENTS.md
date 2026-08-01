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

- [x] **EVAL-01**: Maintainer can run at least ten behavior scenarios covering PASS, PARTIAL, FAIL, forum-only, conflicts, inapplicability, generic continuation, explicit authorization, mechanical change, and hostile-source content. (Use case: UC-005; Concepts: Evaluation Case)
- [x] **EVAL-02**: Automated validation checks Skill metadata, required policy clauses, eval schema, stale names, documentation links, UTF-8, and repository cleanliness in CI. (Use case: UC-005; Concepts: Release Artifact)
- [x] **DOCS-01**: Maintainer has concise bilingual documentation whose policy summary cannot silently diverge from the runtime contract. (Use case: UC-006; Concepts: Release Artifact)
- [x] **DIST-01**: Repository includes a user-approved open-source license and accurate cross-platform installation instructions. (Use case: UC-006; Concepts: Release Artifact)
- [x] **REL-01**: Release process validates, commits atomically, synchronizes the installed Skill, verifies hashes, pushes `main`, and confirms remote commit identity. (Use case: UC-006; Concepts: Release Artifact)

## v1.1 Requirements

### Proactive evidence-to-plan workflow

- [x] **AUTO-01**: Agent proactively triggers `$theoretical-basis` whenever it intends a behavior-affecting research change, without waiting for the researcher to request theoretical support. (Use case: UC-007; Concepts: Change Proposal, Gate Decision)
- [x] **HAND-01**: PASS/PARTIAL produces a structured evidence handoff with claims, sources, supported and forbidden scope, assumptions, limitations, and validation predictions; FAIL produces no implementation handoff. (Use case: UC-007; Concepts: Gate Decision, Evidence Handoff)
- [x] **PLAN-01**: When `$spec-skill` is available, the handoff is represented in read_first inputs, bounded task actions, acceptance criteria, must_haves, and verification commands while preserving the user's plan confirmation checkpoint. (Use case: UC-007; Concepts: Evidence Handoff, Planning Artifact)
- [x] **EXEC-01**: Execution and verification stop and return to the evidence gate when implementation introduces a new substantive change or exceeds the supported evidence scope. (Use case: UC-007; Concepts: Planning Artifact, Change Proposal)

## v1.3 Requirements

### Evidence-grounded engineering discipline

- [x] **ASMP-01**: Agent identifies assumptions and asks a targeted clarification only when an ambiguity can change required evidence, gate outcome, supported scope, or implementation behavior; unambiguous low-risk work proceeds without ceremonial questioning. (Use case: UC-008; Concepts: Decision-Relevant Ambiguity, Change Proposal)
- [x] **MIN-01**: After PASS/PARTIAL, Agent selects the least complex implementation that fully satisfies supported scope and does not add speculative abstractions, configurability, or features. (Use case: UC-008; Concepts: Implementation Candidate, Evidence Handoff)
- [x] **SURG-01**: Every modified line traces to the researcher request, Evidence Handoff, or necessary integration; unrelated cleanup is reported but not edited, and only code orphaned by the current change is removed. (Use case: UC-008; Concepts: Change Trace, Planning Artifact)
- [x] **GOAL-01**: Agent defines evidence-derived success and failure criteria before implementation, uses checks capable of failing when behavior is wrong, and does not move criteria after observing results. (Use case: UC-008; Concepts: Verification Criterion, Evidence Handoff)
- [x] **BOUND-01**: Karpathy Guidelines is treated as attributed engineering inspiration and cannot issue, upgrade, replace, or bypass Theoretical Basis PASS/PARTIAL/FAIL. (Use case: UC-008; Concepts: Gate Decision, Evidence Source)
- [x] **EVAL-04**: Evaluation and negative mutation coverage enforce targeted clarification, minimum supported design, surgical change traceability, fixed verification criteria, and gate-ownership boundaries. (Use case: UC-005, UC-008; Concepts: Evaluation Case, Release Artifact)
- [x] **REL-02**: v1.3.0 release updates plugin and README version metadata, synchronizes Codex and Claude personal Skill copies, passes host validators, pushes through the configured proxy, and verifies remote identity. (Use cases: UC-006, UC-008; Concepts: Release Artifact)

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
| EVAL-01 | Skill Maintainer | UC-005 | Evaluation Case | Phase 2 | Complete |
| EVAL-02 | Skill Maintainer | UC-005 | Release Artifact | Phase 2 | Complete |
| DOCS-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Complete |
| DIST-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Complete |
| REL-01 | Skill Maintainer | UC-006 | Release Artifact | Phase 3 | Complete |
| AUTO-01 | Codex Agent, Researcher | UC-007 | Change Proposal, Gate Decision | Phase 4 | Complete |
| HAND-01 | Codex Agent | UC-007 | Gate Decision, Evidence Handoff | Phase 4 | Complete |
| PLAN-01 | Codex Agent, Researcher | UC-007 | Evidence Handoff, Planning Artifact | Phase 4 | Complete |
| EXEC-01 | Codex Agent | UC-007 | Planning Artifact, Change Proposal | Phase 4 | Complete |
| ASMP-01 | Codex Agent, Researcher | UC-008 | Decision-Relevant Ambiguity, Change Proposal | Phase 5 | Complete |
| MIN-01 | Codex Agent | UC-008 | Implementation Candidate, Evidence Handoff | Phase 5 | Complete |
| SURG-01 | Codex Agent, Skill Maintainer | UC-008 | Change Trace, Planning Artifact | Phase 5 | Complete |
| GOAL-01 | Codex Agent, Researcher | UC-008 | Verification Criterion, Evidence Handoff | Phase 5 | Complete |
| BOUND-01 | Codex Agent | UC-008 | Gate Decision, Evidence Source | Phase 5 | Complete |
| EVAL-04 | Skill Maintainer | UC-005, UC-008 | Evaluation Case, Release Artifact | Phase 5 | Complete |
| REL-02 | Skill Maintainer | UC-006, UC-008 | Release Artifact | Phase 5 | Complete |

## Derived Access Notes

| Status | Operation | Role(s) | Source Use Case(s) / Reason | Requirement(s) |
|--------|-----------|---------|-----------------------------|----------------|
| allowed | Explicitly authorize hypothesis test | Researcher | UC-004 | HYP-01 |
| denied | Self-authorize unsupported behavior change | Codex Agent | Core invariant | HYP-01 |
| denied | Implement a FAIL decision | Codex Agent | UC-001 | EVID-01 |
| allowed | Publish after checks pass | Skill Maintainer | UC-005, UC-006 | EVAL-02, REL-01 |
| denied | Publish with failed required checks | Skill Maintainer / Codex Agent | Release invariant | REL-01 |
| allowed | Create implementation planning constraints from PASS/PARTIAL | Codex Agent | UC-007 | HAND-01, PLAN-01 |
| denied | Create implementation tasks from FAIL or unsupported PARTIAL scope | Codex Agent | Core invariant and UC-007 | HAND-01, PLAN-01 |
| denied | Continue executing a new substantive deviation without a fresh gate | Codex Agent | UC-007 | EXEC-01 |
| allowed | Ask a targeted question when ambiguity changes evidence or implementation behavior | Codex Agent | UC-008 | ASMP-01 |
| denied | Block a clear low-risk task with ceremonial or unrelated questions | Codex Agent | UC-008 | ASMP-01 |
| allowed | Choose the least complex candidate inside PASS/PARTIAL scope | Codex Agent | UC-008 | MIN-01 |
| denied | Add speculative abstractions, configurability, features, or unrelated cleanup | Codex Agent | UC-008 | MIN-01, SURG-01 |
| denied | Let external engineering guidelines issue or bypass a gate decision | Codex Agent | Core invariant and UC-008 | BOUND-01 |

**Coverage:**
- v1 requirements: 13 total
- v1.1 requirements: 4 total
- v1.3 requirements: 7 total
- Mapped to phases: 24
- Unmapped: 0 ✓

---
*Requirements defined: 2026-07-30*
*Last updated: 2026-08-01 during Phase 5 planning*
