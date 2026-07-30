---
name: theoretical-basis
description: Require traceable theoretical support before changing scientific-research algorithms or behavior-affecting modules. Use when Codex designs, implements, tunes, replaces, refactors, or iterates an algorithm, model component, loss function, optimization method, data-processing step, evaluation method, or research-code module whose behavior or scientific claim may change. Search papers, books, authoritative institutions, encyclopedias, and relevant technical forums; pause unsupported changes and ask the user before treating them as hypotheses for experimental validation.
---

# Theoretical Basis

Use an evidence gate before making behavior-affecting research or algorithm changes. Never invent a citation or describe an empirical convention as established theory.

## Apply the evidence gate

1. State the proposed change precisely: affected module, changed mechanism, intended benefit, assumptions, and likely side effects.
2. Identify the theoretical dimension that must support it, such as convergence, stability, optimization geometry, statistical validity, information preservation, computational complexity, robustness, identifiability, or domain mechanism.
3. Search for evidence before editing. Browse the web when sources are not already supplied, and prefer primary or authoritative sources.
4. Map every substantive change to at least one source and the exact claim it supports. Read `references/evidence-protocol.md` for source ranking, acceptance rules, and the evidence record format.
5. Decide whether the gate passes:
   - **Pass:** The source directly or by a clearly explained derivation supports the mechanism under compatible assumptions. Proceed with the smallest justified change.
   - **Partial:** Evidence supports only part of the change. Implement only the supported portion and pause the rest.
   - **Fail:** No adequate basis exists. Do not modify the unsupported behavior.
6. After a failed gate, broaden the search using synonyms, adjacent fields, survey citations, cited-by trails, textbooks, authoritative institutions, encyclopedias, and clearly labeled forum discussions.
7. If the broader search still fails, tell the user what was searched, what was found, and why it is insufficient. Ask whether the user can provide a theory, paper, book passage, domain principle, or other relevant source.
8. If neither Codex nor the user can find support, ask for explicit permission before treating the proposal as a research hypothesis. Do not infer permission from a general request to continue.
9. Only after permission, label the change **unsupported hypothesis**, state falsifiable predictions, and design a controlled experiment before implementation. Obtain confirmation on the proposed hypothesis and experiment when they materially affect research direction, compute cost, or evaluation criteria.

## Implement supported changes

- Keep the implementation within the assumptions and scope of the cited basis.
- Preserve unrelated behavior and record deviations from the referenced method.
- Add or update tests for mathematical invariants, boundary conditions, shapes, numerical stability, and regression behavior as relevant.
- Do not use a citation merely because it mentions the same technique; explain the reasoning bridge from source to change.
- Distinguish theory, empirical evidence, expert practice, and informal discussion in the report.

## Validate the result

Define validation before judging success. Use suitable baselines, ablations, controlled variables, repeated runs, uncertainty estimates, statistical tests, or complexity measurements. Compare observed results with the prediction derived from the evidence. Treat contradictory results as a reason to revisit assumptions, implementation, or applicability—not as a reason to conceal the mismatch.

## Report each iteration

Return a concise evidence ledger containing:

- module and proposed change;
- theoretical dimension and claim;
- source, source type, and link or stable bibliographic identifier;
- applicability assumptions and limitations;
- gate result: pass, partial, or fail;
- code or design changes actually made;
- validation plan and observed result;
- unresolved risks and next decision required from the user.

When the gate fails, lead with **“已暂停修改”** and do not emit or apply the unsupported patch.
