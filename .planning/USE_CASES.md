# Use Cases: Theoretical Basis Skill

**Defined:** 2026-07-30
**Depends on:** `.planning/DOMAIN.md`
**Interaction Gate:** Required

## Actors and Roles

| Actor / Role | Description | Primary Goal | Notes |
|--------------|-------------|--------------|-------|
| Researcher | Person requesting or reviewing an algorithm change | Receive justified changes and retain control over unsupported hypotheses | May also be the repository maintainer |
| Skill Maintainer | Person publishing and installing the Skill | Release a verified, documented, reproducible Skill | Operates repository workflow rather than research gate |
| Codex Agent | Agent applying the Skill | Search, assess, pause, implement, and report within the policy | Cannot self-authorize unsupported hypotheses |

## Role Relationships

| Relationship | Meaning | Notes |
|--------------|---------|-------|
| Researcher -> Codex Agent | Requests and reviews research changes | Researcher supplies missing evidence or explicit hypothesis authorization |
| Skill Maintainer -> Release Artifact | Owns validation and publication | Release occurs only after policy and eval checks pass |

## Use Case Matrix

| Use Case ID | Actor / Role | Domain Concept(s) | Goal / Operation | Outcome | Requirement IDs |
|-------------|--------------|-------------------|------------------|---------|-----------------|
| UC-001 | Researcher | Change Proposal, Gate Decision | Request a module change | Receives a scoped evidence decision before implementation | SCOPE-01, EVID-01, EVID-02 |
| UC-002 | Codex Agent | Search Pass, Evidence Source, Evidence Claim | Search and assess evidence | Produces bounded, traceable, safe evidence records | SRCH-01, SAFE-01, REPT-01 |
| UC-003 | Researcher | Gate Decision, Evidence Source | Respond to a failed gate with a source | Agent re-evaluates rather than bypassing the gate | EVID-02, HYP-01 |
| UC-004 | Researcher | Research Hypothesis, Experiment Protocol | Explicitly authorize hypothesis testing | Agent preregisters and minimally implements a falsifiable experiment | HYP-01, EXPT-01 |
| UC-005 | Skill Maintainer | Evaluation Case, Release Artifact | Validate Skill behavior | Required and adversarial scenarios pass reproducibly | EVAL-01, EVAL-02 |
| UC-006 | Skill Maintainer | Release Artifact | Publish and install a verified release | Repository and installed copy match after checks | DOCS-01, DIST-01, REL-01 |
| UC-007 | Codex Agent, Researcher | Evidence Handoff, Planning Artifact, Gate Decision | Proactively carry verified theory into spec planning and execution | Supported evidence becomes task scope and tests; unsupported work remains absent | AUTO-01, HAND-01, PLAN-01, EXEC-01 |

## Derived Access Rules

| Status | Domain Concept | Operation | Actor(s) | Source / Reason |
|--------|----------------|-----------|----------|-----------------|
| allowed | Evidence Source | Provide source | Researcher | UC-003 |
| allowed | Research Hypothesis | Explicitly authorize test | Researcher | UC-004 |
| denied | Research Hypothesis | Self-authorize unsupported change | Codex Agent | Core safety invariant |
| allowed | Gate Decision | Assess and report | Codex Agent | UC-001, UC-002 |
| denied | Gate Decision FAIL | Implement behavior-affecting change | Codex Agent | UC-001 safety outcome |
| allowed | Release Artifact | Publish after verification | Skill Maintainer | UC-005, UC-006 |
| denied | Release Artifact | Publish with failed required checks | Skill Maintainer / Codex Agent | Release invariant |
| allowed | Evidence Handoff | Create planning constraints from PASS/PARTIAL | Codex Agent | UC-007 |
| denied | Planning Artifact | Add implementation work from FAIL or unsupported PARTIAL scope | Codex Agent | UC-007 and core invariant |
| denied | Planning Artifact | Execute a new substantive deviation without re-running the evidence gate | Codex Agent | UC-007 |

## Use Case Details

### UC-001: Request an evidence-gated change

**Actor:** Researcher
**Domain concepts:** Change Proposal, Evidence Claim, Gate Decision
**Goal:** Obtain a justified algorithm modification without unsupported behavior changes.

**Main flow:**
1. Researcher proposes a module change.
2. Agent classifies scope and risk before editing.
3. Agent identifies required claims, searches evidence, and returns a gate decision.
4. Agent implements only the allowed portion.

**Acceptance signal:** Unsupported critical claims never result in an applied patch.

### UC-004: Authorize an unsupported hypothesis experiment

**Actor:** Researcher
**Domain concepts:** Research Hypothesis, Experiment Protocol
**Goal:** Explore novelty only after evidence search and an explicit decision.

**Main flow:**
1. Agent reports FAIL and requests researcher-provided theory.
2. Researcher and agent confirm no adequate basis is available.
3. Agent asks whether to formulate an unsupported hypothesis.
4. Researcher explicitly authorizes it.
5. Agent preregisters the experiment before minimal implementation.

**Acceptance signal:** “Continue” alone does not authorize implementation; explicit hypothesis authorization does.

### UC-006: Publish a verified release

**Actor:** Skill Maintainer
**Domain concepts:** Evaluation Case, Release Artifact
**Goal:** Keep the public repository and installed Skill trustworthy and synchronized.

**Main flow:**
1. Run structural, semantic, and behavior evaluations.
2. Update bilingual documentation and license.
3. Validate repository and installed copy hashes.
4. Commit and push only when required checks pass.

**Acceptance signal:** Remote `main` matches the verified local commit and installed runtime files.

### UC-007: Carry theory into planning and execution

**Actors:** Codex Agent, Researcher
**Domain concepts:** Gate Decision, Evidence Handoff, Planning Artifact
**Goal:** Make theoretical support affect implementation rather than ending as a report.

**Main flow:**
1. Agent proactively detects an intended behavior-affecting change without waiting for a user reminder.
2. Agent retrieves and verifies evidence, then issues PASS, PARTIAL, or FAIL.
3. PASS/PARTIAL becomes an evidence handoff containing supported scope, sources, assumptions, forbidden scope, and validation predictions.
4. When `$spec-skill` is available, the handoff becomes read-first sources, bounded actions, acceptance criteria, must-haves, and verification commands.
5. Researcher confirms the plan through the normal Ask-Plan-Execute checkpoint.
6. Any new substantive deviation returns to the evidence gate before implementation.

**Acceptance signal:** A user can request ordinary algorithm work without repeating “find theory”; supported evidence is visible in the plan and FAIL never becomes an implementation task.

## Out-of-Scope Actors / Use Cases

| Actor / Use Case | Reason |
|------------------|--------|
| Anonymous third-party publisher | Repository ownership and marketplace publishing are not in scope |
| Agent autonomously running costly experiments | Requires researcher confirmation and compute budget |

## Open Use-Case Questions

None blocking planning.

---
*Use cases defined: 2026-07-30*
*Last updated: 2026-07-30 after Plan approval*
