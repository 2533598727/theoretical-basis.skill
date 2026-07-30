# Evidence Protocol

## Source ranking

Use the strongest applicable source available rather than mechanically requiring the highest-ranked category.

1. Peer-reviewed primary papers, standards, official technical reports, and original method documentation.
2. Scholarly books, graduate textbooks, systematic reviews, and high-quality surveys.
3. Universities, professional societies, government or other authoritative institutions.
4. Curated encyclopedias and reputable technical reference works.
5. Author statements, maintainer discussions, and high-quality technical forums.
6. Blogs, informal posts, and unverified discussions; use mainly as search leads or clearly labeled expert practice.

Forum evidence may explain implementation details or reveal failure modes, but it does not by itself establish a general theoretical claim. Corroborate it when the proposed modification depends on that claim.

## Basis types

Assign every supporting item one basis type:

- **Theory:** A theorem, established principle, or formal model applicable to the required claim.
- **Derivation:** A transparent mathematical or logical argument from stated premises. Verify each step and every imported premise.
- **Empirical evidence:** Observed results from experiments, benchmarks, simulations, or datasets.
- **Expert practice:** A recommendation or implementation convention from a qualified author, maintainer, or institution.
- **Informal observation:** A forum report, blog claim, anecdote, or unverified practical experience.

Evidence may combine several basis types. Report them separately. Empirical evidence can support an expected outcome without proving a general theoretical mechanism. Expert practice and informal observation can guide implementation or further search, but cannot alone establish theoretical PASS.

## Risk-proportional thresholds

Use the proposal's scientific consequence, reversibility, and claim centrality to assign a risk tier. Apply these minimum thresholds:

| Risk tier | Typical scope | Minimum PASS threshold |
|-----------|---------------|------------------------|
| Low | Local, reversible, non-central behavior change | One reliable, directly applicable source or a fully checked derivation with explicit premises |
| Medium | Material output, optimization, evaluation, or multi-module change | One strong primary or authoritative source plus an explicit reasoning bridge; seek independent corroboration when the claim is disputed |
| High | Core scientific claim, data validity, safety, identifiability, irreversible processing, or result-invalidating decision | A primary source plus an independent corroborating source, both compatible with the current assumptions and task |

A lower-ranked source does not become sufficient merely because no stronger source was found. Forum-only or blog-only evidence is explicitly insufficient for theoretical PASS. If the available evidence meets only part of the applicable threshold, return PARTIAL or FAIL and restrict the allowed action accordingly.

## Acceptance rules

Accept evidence only when all applicable checks pass:

- **Traceable:** Give a working link, DOI, ISBN and page/chapter, standard number, or stable identifier.
- **Accurate:** Verify that the source actually makes the attributed claim.
- **Applicable:** Compare the source's assumptions, task, data regime, objective, and algorithm variant with the current module.
- **Sufficient:** Explain any derivation between the cited statement and the proposed change.
- **Current enough:** Check whether later work, corrections, or changed software invalidate the claim when recency matters.
- **Independent enough:** Seek more than one source for consequential or disputed claims when practical.

Do not fabricate bibliographic details. If only an abstract, snippet, or second-hand description is available, say so and lower confidence.

## Search sequence

1. Formulate the claim as searchable technical terms.
2. Search primary literature and official documentation.
3. Use surveys and textbooks to find terminology and foundational citations.
4. Follow backward citations and later work that tests, extends, or disputes the result.
5. Search adjacent disciplines and synonymous formulations.
6. Consult encyclopedias and forums for orientation, implementation experience, and additional leads.
7. Record unsuccessful searches as well as useful results.

## Evidence record

Use this compact structure for each proposed change:

```text
Module:
Proposed change:
Scope class:
Behavior-preservation evidence:
Risk tier and rationale:
Theoretical dimension:
Claim required:
Evidence:
- [basis type / source type] citation/link — supported statement
Assumptions and applicability:
Conflicting evidence or limitations:
Confidence:
Gate: PASS | PARTIAL | FAIL
Allowed action:
Validation:
```

## Unsupported-hypothesis protocol

After Codex's search and the user's own-source check both fail:

1. Keep the modification paused.
2. Ask whether to formulate an unsupported research hypothesis.
3. If authorized, state the hypothesis, mechanism, assumptions, and falsifiable prediction.
4. Specify baseline, controls, ablations, metrics, failure threshold, sample or run count, uncertainty treatment, and compute budget as appropriate.
5. Ask for confirmation if the experiment changes research direction, costs substantial resources, or introduces a new success criterion.
6. Implement only the minimum change needed to test the hypothesis.
7. Report negative and null results alongside positive results.
