#!/usr/bin/env python3
"""Validate the theoretical-basis Skill contract and evaluation corpus."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised by environment setup
    raise SystemExit("PyYAML is required: python -m pip install PyYAML") from exc


SKILL_NAME = "theoretical-basis"
STALE_NAMES = ("ground-algorithm-changes",)
INTEGRATION_REPOSITORIES = (
    "https://github.com/2533598727/theoretical-basis.skill",
    "https://github.com/tirth8205/code-review-graph",
    "https://github.com/ustc-ai4science/academic-search",
    "https://github.com/lgwanai/spec-skill",
    "https://github.com/op7418/Humanizer-zh",
)
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "references/evidence-protocol.md",
    "evals/cases.yaml",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
)
CASE_FIELDS = {
    "id",
    "prompt",
    "supplied_evidence",
    "expected_scope",
    "expected_risk",
    "expected_basis_type",
    "expected_gate",
    "required_actions",
    "forbidden_actions",
    "rationale",
}
REQUIRED_TAGS = {
    "forum-only",
    "conflict",
    "inapplicable",
    "mechanical",
    "hostile-source",
    "generic-continue",
    "authorization",
    "retraction",
    "multi-source-search",
    "custom-library",
    "search-integration",
    "proactive-trigger",
    "spec-handoff",
    "execution-regate",
    "code-graph-integration",
    "humanized-report",
    "claude-code",
}
POLICY_CLAUSES = {
    "SKILL.md": (
        "**Mechanical:**",
        "**Behavior-affecting:**",
        "**risk tier**",
        "no more than two search passes",
        "Google Scholar",
        "user-provided theory libraries",
        "Respect robots rules, rate limits, licenses, paywalls, and access controls",
        "## Delegate retrieval to academic-search",
        "Never delegate the gate decision",
        "Do not wait for the researcher",
        "sole owner of scope classification",
        "Do not create an implementation task from FAIL or from unsupported PARTIAL scope",
        "run a fresh `$theoretical-basis` gate",
        "## Ground the proposal in repository code",
        "Code-review-graph describes code structure; it is not theoretical evidence",
        "use `$humanizer-zh` when available",
        "cannot soften FAIL/PARTIAL",
        "untrusted data",
        "not sufficient for PASS",
        "explicit authorization",
        "## Preregister an unsupported-hypothesis experiment",
        "do not emit or apply the unsupported patch",
        "references/evidence-protocol.md",
        "## Resolve Skill names by host",
        "/theoretical-basis:theoretical-basis",
    ),
    "references/evidence-protocol.md": (
        "## Basis types",
        "## Host invocation mapping",
        "## Risk-proportional thresholds",
        "Forum-only or blog-only evidence is explicitly insufficient",
        "## External-content safety",
        "## Two-pass search sequence",
        "## Search source matrix",
        "## Custom theory libraries",
        "## Search-design basis",
        "## Academic-search integration",
        "## Evidence Handoff and spec planning",
        "## Code-review-graph integration",
        "## Humanized reporting",
        "Humanization is presentation work and has no gate authority",
        "normal `$spec-skill` user confirmation",
        "retrieval adapter, not as the evidence judge",
        "Google Scholar forbids automated bulk access",
        "After Pass 2, stop.",
        "does not authorize implementation",
        "### Required preregistration fields",
        "**Multiple-comparison handling:**",
        "**Stopping rule:**",
    ),
}


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{path}: invalid UTF-8 ({exc})")
        return ""
    if "\ufffd" in text:
        errors.append(f"{path}: contains Unicode replacement characters")
    return text


def load_yaml(path: Path, errors: list[str]) -> Any:
    text = read_utf8(path, errors)
    if not text:
        return None
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML ({exc})")
        return None


def load_json(path: Path, errors: list[str]) -> Any:
    text = read_utf8(path, errors)
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON ({exc})")
        return None


def validate_frontmatter(root: Path, errors: list[str]) -> None:
    skill_path = root / "SKILL.md"
    text = read_utf8(skill_path, errors)
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md: missing YAML frontmatter")
        return
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"SKILL.md: invalid frontmatter ({exc})")
        return
    if not isinstance(meta, dict):
        errors.append("SKILL.md: frontmatter must be a mapping")
        return
    if set(meta) != {"name", "description"}:
        errors.append("SKILL.md: frontmatter must contain only name and description")
    if meta.get("name") != SKILL_NAME:
        errors.append(f"SKILL.md: name must be {SKILL_NAME!r}")
    description = meta.get("description")
    if not isinstance(description, str) or len(description.strip()) < 80:
        errors.append("SKILL.md: description is missing or too short to trigger reliably")


def validate_interface(root: Path, errors: list[str]) -> None:
    path = root / "agents/openai.yaml"
    data = load_yaml(path, errors)
    interface = data.get("interface") if isinstance(data, dict) else None
    if not isinstance(interface, dict):
        errors.append("agents/openai.yaml: interface mapping is required")
        return
    for key in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            errors.append(f"agents/openai.yaml: interface.{key} is required")
    short = interface.get("short_description", "")
    if isinstance(short, str) and not 25 <= len(short) <= 64:
        errors.append("agents/openai.yaml: short_description must be 25-64 characters")
    prompt = interface.get("default_prompt", "")
    if isinstance(prompt, str) and f"${SKILL_NAME}" not in prompt:
        errors.append(f"agents/openai.yaml: default_prompt must mention ${SKILL_NAME}")


def validate_claude_plugin(root: Path, errors: list[str]) -> None:
    repository = "https://github.com/2533598727/theoretical-basis.skill"
    plugin = load_json(root / ".claude-plugin/plugin.json", errors)
    if not isinstance(plugin, dict):
        errors.append(".claude-plugin/plugin.json: object is required")
    else:
        if plugin.get("name") != SKILL_NAME:
            errors.append(f".claude-plugin/plugin.json: name must be {SKILL_NAME!r}")
        version = plugin.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append(".claude-plugin/plugin.json: semantic version is required")
        if plugin.get("repository") != repository:
            errors.append(".claude-plugin/plugin.json: repository URL is incorrect")
        if plugin.get("license") != "MIT":
            errors.append(".claude-plugin/plugin.json: license must be MIT")
        if plugin.get("agents") != []:
            errors.append(
                ".claude-plugin/plugin.json: agents must be empty so Codex agents/openai.yaml is not loaded as a Claude agent"
            )

    marketplace = load_json(root / ".claude-plugin/marketplace.json", errors)
    if not isinstance(marketplace, dict):
        errors.append(".claude-plugin/marketplace.json: object is required")
        return
    if marketplace.get("name") != "theoretical-basis-skills":
        errors.append(
            ".claude-plugin/marketplace.json: name must be 'theoretical-basis-skills'"
        )
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        errors.append(".claude-plugin/marketplace.json: exactly one plugin is required")
        return
    entry = plugins[0]
    if not isinstance(entry, dict):
        errors.append(".claude-plugin/marketplace.json: plugin entry must be an object")
        return
    if entry.get("name") != SKILL_NAME:
        errors.append(".claude-plugin/marketplace.json: plugin name is incorrect")
    if entry.get("source") != "./":
        errors.append(".claude-plugin/marketplace.json: plugin source must be './'")
    if entry.get("strict") is not True:
        errors.append(".claude-plugin/marketplace.json: strict must be true")
    if entry.get("repository") != repository:
        errors.append(".claude-plugin/marketplace.json: repository URL is incorrect")


def validate_policy(root: Path, errors: list[str]) -> None:
    for relative, clauses in POLICY_CLAUSES.items():
        text = read_utf8(root / relative, errors)
        for clause in clauses:
            if clause not in text:
                errors.append(f"{relative}: missing required policy clause {clause!r}")

    scan_paths = [
        root / "SKILL.md",
        root / "README.md",
        root / "agents/openai.yaml",
        root / "references/evidence-protocol.md",
    ]
    combined = "\n".join(read_utf8(path, errors) for path in scan_paths)
    for stale in STALE_NAMES:
        if stale in combined:
            errors.append(f"release files: stale Skill name found: {stale}")

    runtime_text = "\n".join(
        read_utf8(path, errors)
        for path in (root / "SKILL.md", root / "references/evidence-protocol.md")
    )
    for marker in ("TODO", "FIXME", "PLACEHOLDER"):
        if marker in runtime_text:
            errors.append(f"runtime policy contains unfinished marker: {marker}")

    readme = read_utf8(root / "README.md", errors)
    for reference in ("SKILL.md", "evidence-protocol.md", f"${SKILL_NAME}"):
        if reference not in readme:
            errors.append(f"README.md: missing reference {reference!r}")
    repository_url = "https://github.com/2533598727/theoretical-basis.skill.git"
    if repository_url not in readme:
        errors.append("README.md: canonical repository clone URL is missing")
    for claude_reference in (
        "/plugin marketplace add 2533598727/theoretical-basis.skill",
        "/plugin install theoretical-basis@theoretical-basis-skills",
        "/theoretical-basis:theoretical-basis",
        "~/.claude/skills/theoretical-basis",
        "claude plugin validate . --strict",
    ):
        if claude_reference not in readme:
            errors.append(
                f"README.md: Claude Code installation reference is missing: {claude_reference}"
            )
    for integration_url in INTEGRATION_REPOSITORIES:
        if integration_url not in readme:
            errors.append(
                f"README.md: integration repository URL is missing: {integration_url}"
            )


def validate_cases(root: Path, errors: list[str]) -> None:
    path = root / "evals/cases.yaml"
    data = load_yaml(path, errors)
    if not isinstance(data, dict) or data.get("version") != 1:
        errors.append("evals/cases.yaml: version must equal 1")
        return
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 23:
        errors.append("evals/cases.yaml: at least twenty-three cases are required")
        return

    ids: list[str] = []
    tags: set[str] = set()
    gates: set[str] = set()
    scopes: set[str] = set()
    basis_types: set[str] = set()
    risks: set[str] = set()
    for index, case in enumerate(cases, start=1):
        label = f"evals/cases.yaml case {index}"
        if not isinstance(case, dict):
            errors.append(f"{label}: must be a mapping")
            continue
        missing = CASE_FIELDS - set(case)
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
            continue
        case_id = case["id"]
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9_]+", case_id):
            errors.append(f"{label}: id must use lowercase letters, digits, and underscores")
        else:
            ids.append(case_id)
        for field in ("prompt", "supplied_evidence", "rationale"):
            if not isinstance(case[field], str) or len(case[field].strip()) < 20:
                errors.append(f"{label}: {field} must be substantive text")
        for field in ("required_actions", "forbidden_actions"):
            value = case[field]
            if not isinstance(value, list) or len(value) < 1 or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                errors.append(f"{label}: {field} must be a non-empty string list")
        case_tags = case.get("tags", [])
        if not isinstance(case_tags, list) or not all(isinstance(item, str) for item in case_tags):
            errors.append(f"{label}: tags must be a string list")
        else:
            tags.update(case_tags)
        gates.add(str(case["expected_gate"]))
        scopes.add(str(case["expected_scope"]))
        basis_types.add(str(case["expected_basis_type"]))
        risks.add(str(case["expected_risk"]))

    if len(ids) != len(set(ids)):
        errors.append("evals/cases.yaml: case IDs must be unique")
    if gates != {"PASS", "PARTIAL", "FAIL"}:
        errors.append(f"evals/cases.yaml: gates must cover PASS/PARTIAL/FAIL, got {sorted(gates)}")
    if not {"mechanical", "behavior-affecting"} <= scopes:
        errors.append("evals/cases.yaml: both scope classes are required")
    if not {"none", "theory", "derivation", "empirical evidence", "informal observation"} <= basis_types:
        errors.append("evals/cases.yaml: basis-type coverage is incomplete")
    if not {"none", "low", "medium", "high"} <= risks:
        errors.append("evals/cases.yaml: risk coverage is incomplete")
    missing_tags = REQUIRED_TAGS - tags
    if missing_tags:
        errors.append(f"evals/cases.yaml: missing coverage tags {sorted(missing_tags)}")

    by_id = {case.get("id"): case for case in cases if isinstance(case, dict)}
    generic = by_id.get("generic_continue_after_fail")
    explicit = by_id.get("explicit_unsupported_hypothesis_authorization")
    if not generic or not explicit:
        errors.append("evals/cases.yaml: authorization contrast cases are required")
    elif generic.get("forbidden_actions") == explicit.get("forbidden_actions"):
        errors.append("evals/cases.yaml: generic and explicit authorization actions must differ")

    integration_cases = {
        "proactive_algorithm_change_without_reminder": ("FAIL", "proactive-trigger"),
        "pass_evidence_to_spec_handoff": ("PASS", "spec-handoff"),
        "partial_scope_to_spec_plan": ("PARTIAL", "spec-handoff"),
        "fail_cannot_enter_spec_plan": ("FAIL", "spec-handoff"),
        "execution_deviation_requires_regate": ("FAIL", "execution-regate"),
        "code_graph_grounds_change_not_gate": ("FAIL", "code-graph-integration"),
        "humanized_report_preserves_ledger": ("PASS", "humanized-report"),
        "claude_code_auto_and_direct_invocation": ("FAIL", "claude-code"),
    }
    for case_id, (expected_gate, required_tag) in integration_cases.items():
        case = by_id.get(case_id)
        if not case:
            errors.append(f"evals/cases.yaml: required integration case {case_id!r} is missing")
            continue
        if case.get("expected_gate") != expected_gate:
            errors.append(
                f"evals/cases.yaml: {case_id} must expect gate {expected_gate}"
            )
        if required_tag not in case.get("tags", []):
            errors.append(
                f"evals/cases.yaml: {case_id} must include tag {required_tag!r}"
            )


def validate_git_clean(root: Path, errors: list[str]) -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        errors.append(f"git status failed: {result.stderr.strip()}")
    elif result.stdout.strip():
        errors.append("git working tree is not clean")


def validate_root(root: Path, check_git_clean: bool = False) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors
    validate_frontmatter(root, errors)
    validate_interface(root, errors)
    validate_claude_plugin(root, errors)
    validate_policy(root, errors)
    validate_cases(root, errors)
    if check_git_clean:
        validate_git_clean(root, errors)
    return errors


def run_negative_self_test(root: Path) -> None:
    mutations = (
        ("SKILL.md", "untrusted data", "external material"),
        ("SKILL.md", "user-provided theory libraries", "optional collections"),
        ("SKILL.md", "## Delegate retrieval to academic-search", "## Use optional retrieval tools"),
        ("SKILL.md", "Do not wait for the researcher", "Wait for an explicit request"),
        ("SKILL.md", "sole owner of scope classification", "one participant in classification"),
        ("SKILL.md", "Do not create an implementation task from FAIL or from unsupported PARTIAL scope", "Planning may include any gate result"),
        ("SKILL.md", "run a fresh `$theoretical-basis` gate", "continue under the existing plan"),
        ("SKILL.md", "## Ground the proposal in repository code", "## Inspect code when convenient"),
        ("SKILL.md", "Code-review-graph describes code structure; it is not theoretical evidence", "Code structure may establish theory"),
        ("SKILL.md", "cannot soften FAIL/PARTIAL", "may improve the apparent outcome"),
        ("SKILL.md", "## Resolve Skill names by host", "## Invocation syntax"),
        ("references/evidence-protocol.md", "## Evidence Handoff and spec planning", "## Planning notes"),
        ("references/evidence-protocol.md", "## Humanized reporting", "## Report styling"),
        ("references/evidence-protocol.md", "## Custom theory libraries", "## Imported materials"),
    )
    for relative, required, replacement in mutations:
        with tempfile.TemporaryDirectory(prefix="theoretical-basis-negative-") as tmp:
            mutant = Path(tmp) / "mutant"
            shutil.copytree(root, mutant, ignore=shutil.ignore_patterns(".git", ".planning"))
            path = mutant / relative
            text = path.read_text(encoding="utf-8")
            if required not in text:
                raise SystemExit(f"SELF-TEST ERROR: source fixture lacks {required!r}")
            path.write_text(text.replace(required, replacement), encoding="utf-8")
            mutant_errors = validate_root(mutant)
            if not any(required in error for error in mutant_errors):
                raise SystemExit(f"SELF-TEST FAILED: missing clause {required!r} was not detected")
    print(f"PASS negative self-test: {len(mutations)} required policy clauses were rejected when missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    parser.add_argument("--check-git-clean", action="store_true")
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = validate_root(root, check_git_clean=args.check_git_clean)
    if errors:
        print(f"FAIL theoretical-basis validation ({len(errors)} error(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS theoretical-basis validation")
    cases = yaml.safe_load((root / "evals/cases.yaml").read_text(encoding="utf-8"))["cases"]
    print(f"PASS evaluation schema and coverage ({len(cases)} cases)")
    if args.self_test_negative:
        run_negative_self_test(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
