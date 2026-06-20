"""Bundled process template loading."""

from __future__ import annotations

from importlib import resources
from typing import Any

import yaml

TEMPLATE_PACKAGE = "finance_requirements_generator.process_library"
SUPPORTED_PROCESSES = (
    "accounts_payable",
    "bank_reconciliation",
    "vat_reconciliation",
    "accounts_receivable",
    "month_end_close",
    "inventory_costing",
    "intercompany_settlements",
    "payroll_controls",
)
REQUIRED_TEMPLATE_KEYS = {
    "key",
    "name",
    "purpose",
    "baseline_scope",
    "functional_requirements",
    "non_functional_requirements",
    "data_requirements",
    "controls",
    "audit_trail_requirements",
    "user_stories",
    "uat_test_cases",
    "acceptance_criteria",
    "risks_and_dependencies",
    "implementation_readiness",
}

READINESS_TEMPLATE_KEYS = {
    "process_checks",
    "configuration_workshop_questions",
    "cutover_considerations",
}


def load_process_template(process_key: str) -> dict[str, Any]:
    if process_key not in SUPPORTED_PROCESSES:
        raise ValueError(f"Unsupported process: {process_key}")

    template_path = resources.files(TEMPLATE_PACKAGE).joinpath(f"{process_key}.yaml")
    with template_path.open("r", encoding="utf-8") as template_file:
        template = yaml.safe_load(template_file)

    missing = REQUIRED_TEMPLATE_KEYS.difference(template)
    if missing:
        missing_keys = ", ".join(sorted(missing))
        raise ValueError(f"Template {process_key} is missing required keys: {missing_keys}")
    readiness_missing = READINESS_TEMPLATE_KEYS.difference(template["implementation_readiness"])
    if readiness_missing:
        missing_keys = ", ".join(sorted(readiness_missing))
        raise ValueError(
            f"Template {process_key} readiness configuration is missing keys: {missing_keys}"
        )
    return template


def load_all_templates() -> dict[str, dict[str, Any]]:
    return {process_key: load_process_template(process_key) for process_key in SUPPORTED_PROCESSES}
