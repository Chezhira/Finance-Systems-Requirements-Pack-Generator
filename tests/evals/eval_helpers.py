from __future__ import annotations

import re
from dataclasses import replace
from functools import cache

from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.readiness_engine import (
    generate_implementation_readiness_pack,
)
from finance_requirements_generator.schemas import (
    ImplementationReadinessPack,
    ReadinessCheck,
    RequirementsPack,
)
from finance_requirements_generator.template_engine import generate_pack

PROCESS_KEYS = tuple(DEFAULT_SAMPLE_INPUTS)
REPRESENTATIVE_PROCESS_KEYS = (
    "accounts_payable",
    "month_end_close",
    "payroll_controls",
)
PLACEHOLDER_REFERENCES = {"", "N/A", "NONE", "PLACEHOLDER", "TBD", "TODO", "UNKNOWN"}
IDENTIFIER_PATTERN = re.compile(r"^([A-Z]+-\d+):")


@cache
def generated_pack(process_key: str, target_system: str = "") -> RequirementsPack:
    intake = replace(DEFAULT_SAMPLE_INPUTS[process_key], target_system=target_system)
    return generate_pack(intake)


@cache
def readiness_pack(
    process_key: str,
    target_system: str = "",
) -> ImplementationReadinessPack:
    return generate_implementation_readiness_pack(generated_pack(process_key, target_system))


def identifiers(values: list[str]) -> list[str]:
    ids = []
    for value in values:
        match = IDENTIFIER_PATTERN.match(value)
        assert match, f"Expected an ID-prefixed finance artefact: {value}"
        ids.append(match.group(1))
    return ids


def readiness_checks(pack: ImplementationReadinessPack) -> list[ReadinessCheck]:
    return [
        *pack.process_implementation_checklist,
        *pack.target_system_readiness_checklist,
        *pack.data_readiness_checklist,
        *pack.controls_and_uat_readiness_checklist,
        *pack.cutover_readiness_notes,
    ]


def assert_unique(values: list[str], label: str) -> None:
    assert values, f"{label} must not be empty"
    assert len(values) == len(set(values)), f"Duplicate {label}: {values}"


def assert_reviewable_references(references: list[str]) -> None:
    assert references
    for reference in references:
        assert reference.strip()
        assert reference.strip().upper() not in PLACEHOLDER_REFERENCES
