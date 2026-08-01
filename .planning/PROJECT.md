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
- ✓ Scope, risk, basis, bounded search, source safety, and hypothesis preregistration contract — Phase 1.
- ✓ Twelve behavior scenarios, deterministic validation, independent forward tests, and read-only CI — Phase 2.
- ✓ Concise bilingual documentation, MIT licensing, generated metadata, synchronized installation, and remotely verified release — Phase 3.
- ✓ Proactive evidence triggering, structured Evidence Handoff, spec planning constraints, execution re-gating, and 20 behavior scenarios — Phase 4.
- ✓ Claude Code plugin compatibility, host-native invocation mapping, 23 behavior scenarios, and bilingual installation guidance — v1.2 maintenance release.

### Active

- Phase 5: integrate evidence-compatible engineering discipline inspired by `multica-ai/andrej-karpathy-skills` without sharing or weakening gate authority.

### Out of Scope

- Building a literature-search engine or maintaining a paper database — the Skill orchestrates available search tools.
- Automatically judging whether a scientific theory is universally true — the Skill evaluates claim support and applicability.
- Executing costly experiments without confirmation — compute and research-direction changes remain user decisions.
- Changing the GitHub repository name — the existing repository remains the distribution location.

## Context

- Existing repository: `https://github.com/2533598727/theoretical-basis.skill`
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
| Optimize policy and repository engineering together | User explicitly requested the full scope | ✓ Good |
| Use three sequential phases | Policy must stabilize before evals; evals must pass before release | ✓ Good |
| Keep the Skill at repository root | Preserves current installation and discovery behavior | ✓ Good |
| Treat researcher and maintainer as distinct roles | Their operations and acceptance signals differ even if one person fills both roles | ✓ Good |
| License the public repository under MIT | Simple permissive reuse with attribution matches the user's selection | ✓ Good |
| Keep Theoretical Basis as the orchestration core | Search and planning integrations must not replace evidence judgment | ✓ Good |
| Treat evidence as an implementation constraint | Citations are useful only when they shape scope, tests, and verification | ✓ Good |
| Internalize compatible Karpathy-style engineering rules instead of adding a runtime dependency | Assumption handling, minimal design, surgical diffs, and fixed verification criteria should remain subordinate to the evidence gate | Planned |
| Target v1.3.0 for the behavior-contract change | The runtime policy and evaluation corpus change while the Skill name and host contracts stay compatible | Planned |

---
*Last updated: 2026-08-01 during Phase 5 planning*
