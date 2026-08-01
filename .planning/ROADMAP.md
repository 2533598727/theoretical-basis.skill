# Roadmap: Theoretical Basis Skill Optimization

## Overview

The optimization proceeds from policy contract to behavior verification to public release. Each phase produces independently verifiable value and preserves the unsupported-change stop gate.

## Planning Inputs

- **Domain model:** `.planning/DOMAIN.md` (Required)
- **Use cases:** `.planning/USE_CASES.md` (Required)
- **Requirements:** `.planning/REQUIREMENTS.md`

## Phases

- [x] **Phase 1: Evidence Contract** - Make scope, search, gate, source safety, and hypothesis experimentation deterministic.
- [x] **Phase 2: Behavioral Verification** - Add repeatable scenario evals, semantic validation, and CI enforcement.
- [x] **Phase 3: Distribution and Release** - Align bilingual docs, license the repository, synchronize installation, and publish a verified release.
- [x] **Phase 4: Evidence-to-Plan Enforcement** - Keep Theoretical Basis proactive and carry verified evidence into spec planning, execution, and verification.
- [x] **Phase 5: Evidence-Grounded Engineering Discipline** - Add targeted clarification, minimum supported design, surgical diffs, and fixed verification criteria without weakening gate ownership.

## Phase Details

### Phase 1: Evidence Contract
**Goal**: The Skill makes predictable, safe, risk-proportional decisions before algorithm changes.
**Depends on**: Nothing
**Requirements**: [SCOPE-01, EVID-01, EVID-02, REPT-01, SRCH-01, SAFE-01, HYP-01, EXPT-01]
**Use Cases**: [UC-001, UC-002, UC-003, UC-004]
**Domain Concepts**: [Change Proposal, Evidence Claim, Evidence Source, Search Pass, Gate Decision, Research Hypothesis, Experiment Protocol]
**Success Criteria**:
  1. Researcher receives a scope class, risk tier, basis type, gate decision, and exact allowed action before implementation.
  2. Codex Agent stops after two documented search passes and asks the Researcher for evidence when support remains insufficient.
  3. Codex Agent ignores instructions embedded in sources and cannot self-authorize an unsupported change.
  4. Researcher can explicitly authorize a hypothesis only after FAIL, and the Agent preregisters a complete experiment before minimal implementation.
**Plans**: 1 plan

Plans:
- [x] 01-01: Rewrite the runtime evidence contract and protocol.

### Phase 2: Behavioral Verification
**Goal**: Required policy behavior is reproducible and enforced before merge or release.
**Depends on**: Phase 1
**Requirements**: [EVAL-01, EVAL-02]
**Use Cases**: [UC-005]
**Domain Concepts**: [Evaluation Case, Gate Decision, Release Artifact]
**Success Criteria**:
  1. Skill Maintainer can run at least ten scenario cases with explicit expected decisions and forbidden actions.
  2. Automated validation fails on missing safety clauses, stale names, invalid metadata, broken docs, or malformed eval cases.
  3. CI runs the same validation on pushes and pull requests.
**Plans**: 1 plan

Plans:
- [x] 02-01: Add scenario corpus, validator, forward tests, and CI.

### Phase 3: Distribution and Release
**Goal**: The public repository is concise, licensed, installable, synchronized, and verified remotely.
**Depends on**: Phase 2
**Requirements**: [DOCS-01, DIST-01, REL-01]
**Use Cases**: [UC-006]
**Domain Concepts**: [Release Artifact]
**Success Criteria**:
  1. Skill Maintainer can install the Skill using documented Windows and POSIX commands and invoke `$theoretical-basis`.
  2. Bilingual README summarizes rather than duplicates the runtime contract and links to canonical policy files.
  3. Repository contains the user-approved license and generated interface metadata is current.
  4. Installed Skill files match the validated repository and remote `main` matches the released commit.
**Plans**: 1 plan

Plans:
- [x] 03-01: Finalize documentation, license, metadata, synchronization, and release.

### Phase 4: Evidence-to-Plan Enforcement
**Goal**: Theoretical Basis proactively gates AI-authored research changes and makes verified evidence constrain the resulting spec plan and execution.
**Depends on**: Phase 1, Phase 2, installed `$academic-search`, available `$spec-skill`
**Requirements**: [AUTO-01, HAND-01, PLAN-01, EXEC-01]
**Use Cases**: [UC-007]
**Domain Concepts**: [Change Proposal, Gate Decision, Evidence Handoff, Planning Artifact, Evaluation Case]
**Success Criteria**:
  1. Codex triggers the evidence gate for its own intended research changes without a user reminder.
  2. PASS/PARTIAL evidence produces a structured handoff that materially shapes read_first, action scope, acceptance criteria, must_haves, and verification.
  3. FAIL and unsupported PARTIAL scope cannot appear as implementation tasks.
  4. New substantive execution deviations stop and return to Theoretical Basis before code changes continue.
  5. Behavioral evaluation covers proactive triggering, PASS/PARTIAL/FAIL planning outcomes, and execution re-gating.
**Plans**: 1 plan

Plans:
- [x] 04-01: Add proactive evidence handoff and spec-skill enforcement.

### Phase 5: Evidence-Grounded Engineering Discipline
**Goal**: Make every supported implementation explicit about decision-relevant ambiguity, choose the least complex supported design, keep diffs traceable to authorized scope, and freeze verification criteria before execution.
**Depends on**: Phase 4, verified `multica-ai/andrej-karpathy-skills` snapshot, directly checked clarification and code-review sources
**Requirements**: [ASMP-01, MIN-01, SURG-01, GOAL-01, BOUND-01, EVAL-04, REL-02]
**Use Cases**: [UC-008]
**Domain Concepts**: [Decision-Relevant Ambiguity, Implementation Candidate, Change Trace, Verification Criterion, Evidence Handoff, Gate Decision]
**Success Criteria**:
  1. The Agent asks a targeted question only when an ambiguity can change evidence claims, gate outcome, allowed scope, or implementation behavior; otherwise it records the assumption and proceeds.
  2. PASS/PARTIAL selects the least complex implementation that satisfies the supported scope and refuses speculative abstraction, configurability, or unrelated functionality.
  3. Every changed line traces to the researcher request, Evidence Handoff, or necessary integration; unrelated cleanup remains unmodified and only newly orphaned code is removed.
  4. Evidence-derived success and failure criteria are defined before editing, verified with checks capable of detecting broken behavior, and are not moved after results appear.
  5. Karpathy Guidelines remains attributed engineering inspiration, never a source of theoretical PASS or a replacement for Theoretical Basis gate authority.
  6. Behavior cases, negative mutations, host validators, installed runtime hashes, and remote commit identity all pass for v1.3.0.
**Plans**: 1 plan

Plans:
- [x] 05-01: Integrate evidence-grounded engineering discipline, evaluation, documentation, and release.

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Evidence Contract | 1/1 | Complete | 2026-07-30 |
| 2. Behavioral Verification | 1/1 | Complete | 2026-07-30 |
| 3. Distribution and Release | 1/1 | Complete | 2026-07-30 |
| 4. Evidence-to-Plan Enforcement | 1/1 | Complete | 2026-07-30 |
| 5. Evidence-Grounded Engineering Discipline | 1/1 | Complete | 2026-08-01 |
