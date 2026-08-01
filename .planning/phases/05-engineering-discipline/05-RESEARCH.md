# Phase 5 Research: Evidence and Applicability

**Completed:** 2026-08-01
**Gate:** PASS
**Risk tier:** Low
**Scope:** Reversible operational behavior change to the Skill contract; no scientific algorithm or project data is modified.

## Required claims

1. Material ambiguity should be surfaced with targeted clarification before code generation, while clear requirements should not incur unnecessary questioning.
2. Supported implementations should avoid speculative complexity and prefer focused changes.
3. Logic changes and refactors should carry relevant tests capable of detecting broken behavior.
4. The external Karpathy Guidelines can inspire engineering rules but cannot establish theoretical truth or inherit gate authority.

## Search log

### Pass 1: direct source and authority

- Inspected `multica-ai/andrej-karpathy-skills` at commit `2c606141936f1eeef17fa3043a72095b4765b9c2`, including `skills/karpathy-guidelines/SKILL.md`, `README.md`, and `README.zh.md`.
- Opened Google Engineering Practices pages for code-review complexity, small focused changes, and tests.
- Opened the full arXiv HTML for ClarifyGPT rather than relying on a search snippet or abstract alone.

### Pass 2: broaden and challenge

- Checked the Google Research record for *Modern Code Review: A Case Study at Google* for empirical context around modern review practice.
- Searched for newer ambiguity-focused code-generation studies and contrary workflow concerns.
- Considered the external Skill's own tradeoff note that caution can slow trivial work.
- Checked repository licensing surface: README and Skill frontmatter say MIT, but the inspected snapshot has no standalone `LICENSE` file.

## Verified sources and applicable passages

1. **Empirical evidence / primary research:** Fangwen Mu et al., *ClarifyGPT: Empowering LLM-based Code Generation with Intention Clarification*, arXiv:2310.10996. <https://arxiv.org/abs/2310.10996>
   - The paper reports that ambiguous requirements can lead LLMs to divergent implementations and evaluates targeted clarification before final generation.
   - Its introduction explicitly warns that asking about unambiguous requirements creates unnecessary interactions and harms efficiency/user experience.
   - Applicability: supports conditional, targeted clarification. It does not justify blocking every repository-level task or guarantee the reported benchmark gains for this Skill.
2. **Authoritative engineering practice:** Google Engineering Practices, *What to look for in a code review*. <https://google.github.io/eng-practices/review/reviewer/looking-for.html>
   - Directly advises against over-engineering, speculative generality, future functionality not presently required, major unrelated style changes, and tests that cannot reveal broken code.
   - Applicability: supports least-complex candidates, exclusion of opportunistic changes, and meaningful tests. It is institutional human-engineering practice, not a theorem about AI agents.
3. **Authoritative engineering practice:** Google Engineering Practices, *Small CLs*. <https://google.github.io/eng-practices/review/developer/small-cls.html>
   - Defines smallness conceptually as one focused change rather than a simplistic line count; requires related tests and test coverage for behavior-preserving refactors.
   - Applicability: supports conceptual minimality, bounded diffs, necessary test work, and separation of unrelated refactoring.
4. **Empirical context / primary research:** Caitlin Sadowski et al., *Modern Code Review: A Case Study at Google*, ICSE SEIP 2018. <https://research.google/pubs/modern-code-review-a-case-study-at-google/>
   - Studies review practices using interviews, survey responses, and nine million reviewed changes.
   - Applicability: corroborates the relevance of focused, reviewable changes but does not prove the exact four-rule prompt.
5. **Expert practice / original method documentation:** `multica-ai/andrej-karpathy-skills`, commit `2c606141936f1eeef17fa3043a72095b4765b9c2`. <https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2>
   - Defines four guidelines: surface assumptions, prefer simple implementations, make surgical changes, and use verifiable goals.
   - Applicability: supplies the integration vocabulary and failure modes requested by the user. Its exact prompt bundle has no independent evaluation in the inspected repository.

## Evidence Handoff

```text
Gate: PASS
Risk tier: Low
Required claims: targeted clarification for material ambiguity; least-complex supported implementation; focused change traceability; meaningful predefined verification; external guideline cannot own the evidence gate
Verified sources and applicable passages: ClarifyGPT arXiv:2310.10996; Google Engineering Practices complexity/tests and Small CLs pages; Modern Code Review ICSE SEIP 2018; multica-ai repository snapshot 2c606141936f1eeef17fa3043a72095b4765b9c2
Supported scope: add conditional assumption surfacing, minimum supported design, surgical diff traceability, fixed verification criteria, attribution, eval coverage, versioned host-compatible release
Forbidden scope: universal effectiveness claims; benchmark percentages for this Skill; ceremonial questioning; verbatim wholesale copying; external gate authority; omitting required tests/safety/docs in the name of minimality
Assumptions: operational workflow is low-risk and reversible; Google human-engineering practices transfer only as engineering constraints; ClarifyGPT evidence transfers only to decision-relevant ambiguity handling
Limitations: ClarifyGPT is mainly function-level; exact four-rule bundle lacks independent evaluation; inspected external snapshot lacks standalone LICENSE; code graph excludes Markdown/YAML
Validation predictions: new scenarios reject silent material assumptions, unnecessary questions, speculative design, unrelated cleanup, moved criteria, and gate delegation; validators fail when any new clause is removed
Unresolved risks: prompt bloat and excessive caution; mitigate through concise runtime wording, progressive disclosure, and explicit clear-task fast path
```

## Decision

The evidence meets the low-risk threshold for the bounded engineering-discipline integration. It does not support claims of universal agent-performance improvement. Execute only the supported scope in `05-01-PLAN.md`.

