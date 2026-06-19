from __future__ import annotations

from pathlib import Path

from finance_requirements_generator.control_risk import CONTROL_RISK_HEADERS
from finance_requirements_generator.schemas import (
    ControlRiskRow,
    FitGapMappingRow,
    RequirementsPack,
    SOPDraft,
    UATTestCase,
)

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

    if pack.current_state_sop_draft:
        lines.extend(["## Current-State SOP Draft", ""])
        lines.extend(_render_sop(pack.current_state_sop_draft))
        lines.append("")

    if pack.target_system_fit_gap_mapping:
        lines.extend(["## Target-System Fit-Gap Mapping", ""])
        lines.append(f"**Target system:** {pack.target_system}")
        lines.append(
            "**Validation guardrail:** Candidate mapping only; requires implementation "
            "validation against selected edition, modules, localisation, and configuration."
        )
        lines.append("")
        lines.append(
            "| Current-State Area | Target-System Capability Area | Candidate Fit-Gap View | "
            "Requirement Impact | Validation Note |"
        )
        lines.append("| --- | --- | --- | --- | --- |")
        for row in pack.target_system_fit_gap_mapping:
            lines.append(
                "| "
                f"{_escape_table(row.current_state_area)} | "
                f"{_escape_table(row.target_system_capability_area)} | "
                f"{_escape_table(row.candidate_fit_gap_view)} | "
                f"{_escape_table(row.requirement_impact)} | "
                f"{_escape_table(row.validation_note)} |"
            )
        lines.append("")

    lines.extend(["## Visual Process Documentation", ""])
    lines.append(
        "The Mermaid diagram below can be copied into Mermaid-compatible tools for rendering."
    )
    lines.append("")
    lines.extend(["```mermaid", pack.mermaid_process_map, "```", ""])
    lines.append("### Process Map Summary")
    lines.append("")
    lines.extend(f"- {item}" for item in pack.process_map_summary)
    lines.append("")

    lines.extend(["## Control-Risk Matrix", ""])
    lines.append(
        "| "
        + " | ".join(CONTROL_RISK_HEADERS)
        + " |"
    )
    lines.append("| " + " | ".join("---" for _ in CONTROL_RISK_HEADERS) + " |")
    for row in pack.control_risk_matrix:
        lines.append(
            "| "
            + " | ".join(_escape_table(value) for value in _control_risk_values(row))
            + " |"
        )
    lines.append("")

    lines.extend(["## Public-Safe Sample Data Note", ""])
    lines.extend(_render_value(pack.public_safe_sample_data_note))

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
        if value and isinstance(value[0], FitGapMappingRow):
            return [
                (
                    f"- **{row.current_state_area}:** {row.candidate_fit_gap_view} "
                    f"Impact: {row.requirement_impact} Validation: {row.validation_note}"
                )
                for row in value
            ]
        if value and isinstance(value[0], ControlRiskRow):
            return [
                f"- **{row.risk_area}:** {row.control_activity} Evidence: {row.evidence_required}"
                for row in value
            ]
        return [f"- {item}" for item in value]
    return [str(value)]


def _render_sop(sop: SOPDraft) -> list[str]:
    sections: list[tuple[str, str | list[str]]] = [
        ("Purpose", sop.purpose),
        ("Scope", sop.scope),
        ("Trigger", sop.trigger),
        ("Roles and Responsibilities", sop.roles_and_responsibilities),
        ("Step-by-Step Procedure", sop.step_by_step_procedure),
        ("Controls and Approvals", sop.controls_and_approvals),
        ("Exceptions and Escalations", sop.exceptions_and_escalations),
        ("Reports and Evidence", sop.reports_and_evidence),
        ("Systems and Data Used", sop.systems_and_data_used),
        ("Review and Sign-off", sop.review_and_sign_off),
    ]
    lines = []
    for title, value in sections:
        lines.extend([f"### {title}", ""])
        if isinstance(value, list):
            lines.extend(f"- {item}" for item in value if item)
        else:
            lines.append(value)
        lines.append("")
    return lines


def _escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def _control_risk_values(row: ControlRiskRow) -> list[str]:
    return [
        row.process_area,
        row.risk_area,
        row.risk_description,
        row.control_objective,
        row.control_activity,
        row.control_type,
        row.frequency,
        row.owner,
        row.evidence_required,
        row.system_data_dependency,
        row.related_requirement_id,
        row.related_uat_case,
        row.residual_risk_implementation_note,
    ]
