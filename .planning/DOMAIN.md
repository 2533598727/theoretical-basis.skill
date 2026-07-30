# Domain Model: Theoretical Basis Skill

**Defined:** 2026-07-30
**Interaction Gate:** Required
**Reason:** Researchers use the Skill to approve evidence, provide sources, and authorize hypothesis experiments.

## Domain Summary

The Skill governs a research change from proposal through evidence search, gate decision, implementation, and validation. Its central invariant is that an unsupported change remains paused until the researcher explicitly authorizes a falsifiable hypothesis and experiment.

## Core Concepts

| Concept | Meaning | In Scope | Out of Scope |
|---------|---------|----------|--------------|
| Change Proposal | A behavior-affecting or mechanical modification under consideration | Module, mechanism, intended benefit, assumptions, risks | An already completed undocumented change |
| Evidence Claim | The exact proposition needed to justify a proposal | Claim, basis type, applicability, confidence | A citation with no reasoning bridge |
| Evidence Source | A traceable artifact used to support or challenge a claim | Paper, book, standard, authority, encyclopedia, forum | Unverifiable bibliographic details |
| Search Pass | One bounded evidence-retrieval stage | Queries, sources checked, exclusions, result | Endless or undocumented browsing |
| Gate Decision | The permitted action after evidence assessment | PASS, PARTIAL, FAIL with rationale | A vague confidence statement without allowed action |
| Research Hypothesis | An unsupported but explicitly authorized, falsifiable proposal | Mechanism, assumptions, prediction | A claim presented as established theory |
| Experiment Protocol | A preregistered test of a hypothesis | Baseline, controls, metrics, seeds, thresholds, budget | Post-hoc success criteria |
| Evaluation Case | A repeatable scenario testing Skill behavior | Prompt, evidence state, expected gate/action | A structural-only YAML check |
| Release Artifact | The verified repository and installed Skill copy | Skill files, docs, CI, license, commit | Unverified local drafts |
| Evidence Handoff | A gate result translated into planning constraints | Claims, sources, supported scope, assumptions, forbidden scope, validation predictions | A bibliography copied into a plan without implementation consequences |
| Planning Artifact | A spec-skill plan that operationalizes verified evidence | read_first, action bounds, acceptance criteria, must_haves, verification | An implementation plan that bypasses or expands beyond the gate |

## Progressive Concept Decomposition

| Level | Parent Concept | Child Concept | Why It Exists | Decompose Further? |
|-------|----------------|---------------|---------------|--------------------|
| 1 | Evidence Gate | Scope Classification | Avoid unnecessary research for mechanical changes | No |
| 1 | Evidence Gate | Risk Tier | Set evidence strength proportional to consequence | Yes |
| 1 | Evidence Gate | Basis Type | Separate theory, derivation, empirical evidence, and informal practice | No |
| 2 | Risk Tier | Low / Medium / High | Define deterministic PASS thresholds | No |
| 1 | Hypothesis Workflow | Experiment Protocol | Prevent result-driven criteria changes | Yes |
| 2 | Experiment Protocol | Metrics / Seeds / Holdout / Stopping Rule | Make tests reproducible and falsifiable | No |

## Concept Attributes

### Gate Decision

**Required attributes:**
- `scope_class` - mechanical or behavior-affecting
- `risk_tier` - low, medium, or high
- `basis_type` - theory, derivation, empirical, expert practice, or informal observation
- `status` - PASS, PARTIAL, or FAIL
- `allowed_action` - exact implementation boundary
- `rationale` - evidence-to-change reasoning bridge

**Lifecycle / states:**
- Proposed -> Searched -> Assessed -> PASS/PARTIAL/FAIL -> Implemented or Paused -> Validated

**Business rules / invariants:**
- FAIL never permits a behavior-affecting modification.
- General instructions to continue do not authorize an unsupported hypothesis.
- Forum-only support cannot establish a general theoretical claim.

### Experiment Protocol

**Required attributes:**
- hypothesis and falsifiable prediction
- baseline, controls, and ablations
- primary metric and failure threshold
- run count and random-seed policy
- holdout or final-test isolation
- uncertainty and multiple-comparison treatment
- compute budget and stopping rule

## Relationships

| Source | Relationship | Target | Cardinality | Notes |
|--------|--------------|--------|-------------|-------|
| Change Proposal | requires | Evidence Claim | 1:N | Each substantive mechanism change needs a claim |
| Evidence Claim | is supported/challenged by | Evidence Source | N:M | Conflicting evidence must be recorded |
| Search Pass | discovers | Evidence Source | 1:N | Unsuccessful queries are also recorded |
| Evidence Claim | produces | Gate Decision | N:1 | Decision reflects the weakest unsupported critical claim |
| Gate Decision FAIL | may become, after authorization | Research Hypothesis | 0:1 | Explicit researcher permission required |
| Research Hypothesis | is tested by | Experiment Protocol | 1:1+ | Minimal implementation only |
| Evaluation Case | verifies | Gate Decision behavior | N:M | Includes adversarial and edge cases |
| Gate Decision PASS/PARTIAL | produces | Evidence Handoff | 0:1 | Only supported scope can enter implementation planning |
| Evidence Handoff | constrains | Planning Artifact | 1:N | Evidence must affect tasks, tests, and verification |
| Planning Artifact deviation | returns to | Change Proposal | 0:N | New substantive behavior requires a fresh evidence gate |

## Vocabulary Decisions

| Term | Use This Meaning | Avoid / Do Not Mean | Decision |
|------|------------------|---------------------|----------|
| Theoretical basis | A traceable theory or derivation applicable to the proposal | Any empirical improvement or forum opinion | Confirmed |
| Evidence | A broader category including theory, empirical findings, and expert practice | Automatically equivalent to theoretical support | Confirmed |
| Unsupported hypothesis | Explicitly labeled proposal with no adequate basis | Quiet permission to implement speculative behavior | Confirmed |
| Mechanical change | Change shown not to affect scientific behavior or claims | Any refactor asserted to be harmless without verification | Confirmed |
| Evidence handoff | Operational planning contract derived from a verified gate | A citation appendix with no effect on implementation | Confirmed |

## Open Domain Questions

None blocking planning. Exact wording can be refined during implementation without changing these invariants.

---
*Domain model defined: 2026-07-30*
*Last updated: 2026-07-30 after Plan approval*
