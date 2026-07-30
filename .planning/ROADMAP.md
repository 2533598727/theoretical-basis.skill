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

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Evidence Contract | 1/1 | Complete | 2026-07-30 |
| 2. Behavioral Verification | 1/1 | Complete | 2026-07-30 |
| 3. Distribution and Release | 1/1 | Complete | 2026-07-30 |
