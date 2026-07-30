#!/usr/bin/env python3
"""Validate the theoretical-basis Skill contract and evaluation corpus."""

from __future__ import annotations

import argparse
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
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "references/evidence-protocol.md",
    "evals/cases.yaml",
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
        "untrusted data",
        "not sufficient for PASS",
        "explicit authorization",
        "## Preregister an unsupported-hypothesis experiment",
        "do not emit or apply the unsupported patch",
        "references/evidence-protocol.md",
    ),
    "references/evidence-protocol.md": (
        "## Basis types",
        "## Risk-proportional thresholds",
        "Forum-only or blog-only evidence is explicitly insufficient",
        "## External-content safety",
        "## Two-pass search sequence",
        "## Search source matrix",
        "## Custom theory libraries",
        "## Search-design basis",
        "## Academic-search integration",
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
    repository_url = "https://github.com/2533598727/-theoretical-basis.skill.git"
    if repository_url not in readme:
        errors.append("README.md: canonical repository clone URL is missing")


def validate_cases(root: Path, errors: list[str]) -> None:
    path = root / "evals/cases.yaml"
    data = load_yaml(path, errors)
    if not isinstance(data, dict) or data.get("version") != 1:
        errors.append("evals/cases.yaml: version must equal 1")
        return
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 10:
        errors.append("evals/cases.yaml: at least ten cases are required")
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
