from __future__ import annotations

from pathlib import Path

from finance_requirements_generator.schemas import RequirementsPack, UATTestCase

SECTION_TITLES = {
    "executive_summary": "Executive Summary",
    "business_problem": "Business Problem",
    "process_scope": "Process Scope",
    "in_scope": "In Scope",
    "out_of_scope": "Out of Scope",
    "stakeholders_and_roles": "Stakeholders and Roles",
    "functional_requirements": "Functional Requirements",
    "data_requirements": "Data Requirements",
    "controls": "Controls",
    "reporting_requirements": "Reporting Requirements",
    "audit_trail_requirements": "Audit Trail Requirements",
    "user_stories": "User Stories",
    "uat_test_cases": "UAT Test Cases",
    "acceptance_criteria": "Acceptance Criteria",
    "risks_and_dependencies": "Implementation Risks and Dependencies",
    "implementation_notes": "Implementation Notes",
    "public_safe_sample_data_note": "Public-Safe Sample Data Note",
}


def pack_to_markdown(pack: RequirementsPack) -> str:
    lines = [
        f"# {pack.process_name} Requirements Pack",
        "",
        f"**Prepared for:** {pack.company_name}",
        "",
        "**Purpose:** Translate finance process pain points into implementation-ready "
        "ERP requirements, controls, reporting needs, audit trail expectations, and UAT coverage.",
        "",
    ]

    for field_name in SECTION_TITLES:
        value = getattr(pack, field_name)
        lines.extend([f"## {SECTION_TITLES[field_name]}", ""])
        lines.extend(_render_value(value))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def export_markdown(pack: RequirementsPack, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(pack_to_markdown(pack), encoding="utf-8")
    return path


def _render_value(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        if value and isinstance(value[0], UATTestCase):
            return [
                f"- **{case.test_id}:** {case.scenario} Expected result: {case.expected_result}"
                for case in value
            ]
        return [f"- {item}" for item in value]
    return [str(value)]
