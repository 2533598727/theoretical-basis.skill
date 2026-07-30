# Theoretical Basis Skill Optimization

## What This Is

This project hardens `theoretical-basis`, a Codex Skill that prevents unsupported scientific-algorithm changes. It serves researchers who want AI-assisted algorithm iteration while preserving traceable evidence, explicit hypothesis authorization, reproducible experiments, and a maintainable public repository.

## Core Value

The Skill must never implement a behavior-affecting research change without evidence that satisfies a defined gate or the researcher's explicit authorization to test a clearly labeled hypothesis.

## Requirements

### Domain / Interaction Gate

- **Interaction gate**: Required
- **Reason**: A researcher interacts with the Skill through a chat workflow, provides evidence or authorization, and relies on the resulting gate decision.
- **Domain model**: `.planning/DOMAIN.md`
- **Use cases**: `.planning/USE_CASES.md`

### Validated

- ✓ The Skill is installed as `$theoretical-basis`, has valid frontmatter, and is available to Codex.
- ✓ The current workflow pauses unsupported changes and requests user input before hypothesis-based experimentation.
- ✓ The public repository contains the Skill, bilingual README, interface metadata, and evidence protocol.

### Active

- [ ] Define deterministic scope, evidence-risk tiers, basis types, and gate thresholds.
- [ ] Bound evidence search and harden all external-source handling.
- [ ] Strengthen preregistered experimental validation for unsupported hypotheses.
- [ ] Add repeatable behavioral evaluation cases and automated validation.
- [ ] Add CI, licensing, documentation consistency, release verification, and installed-copy synchronization.

### Out of Scope

- Building a literature-search engine or maintaining a paper database — the Skill orchestrates available search tools.
- Automatically judging whether a scientific theory is universally true — the Skill evaluates claim support and applicability.
- Executing costly experiments without confirmation — compute and research-direction changes remain user decisions.
- Changing the GitHub repository name — the existing repository remains the distribution location.

## Context

- Existing repository: `https://github.com/2533598727/-theoretical-basis.skill`
- Existing runtime path: `~/.codex/skills/theoretical-basis`
- Review found ambiguity in PASS thresholds, unbounded search, missing hostile-source rules, incomplete experiment preregistration, and no behavior-level evaluation.
- Current files are valid UTF-8 and the installed copy matches the repository commit.

## Constraints

- **Compatibility**: Preserve Skill name `$theoretical-basis` and root-level `SKILL.md` installation.
- **Safety**: Never weaken the existing unsupported-change stop gate.
- **Verification**: Structural validation alone is insufficient; behavior scenarios and adversarial cases are required.
- **Documentation**: Keep Chinese and English installation and usage instructions accurate.
- **Git**: Use atomic commits and push only after all automated checks pass.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Optimize policy and repository engineering together | User explicitly requested the full scope | — Pending |
| Use three sequential phases | Policy must stabilize before evals; evals must pass before release | — Pending |
| Keep the Skill at repository root | Preserves current installation and discovery behavior | — Pending |
| Treat researcher and maintainer as distinct roles | Their operations and acceptance signals differ even if one person fills both roles | — Pending |

---
*Last updated: 2026-07-30 after scope confirmation and Plan approval*
