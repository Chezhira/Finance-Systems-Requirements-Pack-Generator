from __future__ import annotations

from finance_requirements_generator.control_risk import generate_control_risk_matrix
from finance_requirements_generator.process_library import load_process_template
from finance_requirements_generator.process_map import (
    generate_process_map_flow,
    render_mermaid_process_map,
    render_process_map_summary,
)
from finance_requirements_generator.questionnaire import validate_intake
from finance_requirements_generator.schemas import IntakeAnswers, RequirementsPack, UATTestCase
from finance_requirements_generator.system_mapping import get_fit_gap_mapping
from finance_requirements_generator.text_cleanup import (
    clean_fragment,
    clean_items,
    clean_sentence,
)


def generate_pack(intake: IntakeAnswers) -> RequirementsPack:
    validate_intake(intake)
    template = load_process_template(intake.process_key)

    problem = _business_problem(intake, template)
    process_scope = _process_scope(intake, template)
    functional_requirements = _personalise_requirements(
        template["functional_requirements"],
        prefix="FR",
    )
    controls = _personalise_requirements(template["controls"], prefix="CTRL")
    audit_trail_requirements = _personalise_requirements(
        template["audit_trail_requirements"],
        prefix="AUD",
    )
    uat_test_cases = [
        UATTestCase(
            test_id=f"UAT-{index:02d}",
            scenario=item["scenario"],
            expected_result=item["expected"],
        )
        for index, item in enumerate(template["uat_test_cases"], start=1)
    ]
    process_map_flow = generate_process_map_flow(template["name"], intake)

    return RequirementsPack(
        process_key=intake.process_key,
        process_name=template["name"],
        company_name=intake.company_name,
        executive_summary=_executive_summary(intake, template),
        business_problem=problem,
        process_scope=process_scope,
        in_scope=_in_scope(intake, template),
        out_of_scope=_out_of_scope(intake, template),
        stakeholders_and_roles=_stakeholders_and_roles(intake, template),
        assumptions=_assumptions(intake),
        functional_requirements=functional_requirements,
        non_functional_requirements=_personalise_requirements(
            template["non_functional_requirements"],
            prefix="NFR",
        ),
        data_requirements=_personalise_requirements(
            template["data_requirements"],
            prefix="DR",
        ),
        controls=controls,
        reporting_requirements=_reporting_requirements(intake, template),
        audit_trail_requirements=audit_trail_requirements,
        user_stories=list(template["user_stories"]),
        uat_test_cases=uat_test_cases,
        acceptance_criteria=list(template["acceptance_criteria"]),
        risks_and_dependencies=list(template["risks_and_dependencies"]),
        implementation_notes=_implementation_notes(intake, template),
        control_risk_matrix=generate_control_risk_matrix(
            template["name"],
            intake,
            controls,
            audit_trail_requirements,
            uat_test_cases,
            functional_requirements,
            list(template["risks_and_dependencies"]),
        ),
        process_map_flow=process_map_flow,
        mermaid_process_map=render_mermaid_process_map(process_map_flow),
        process_map_summary=render_process_map_summary(process_map_flow, template["name"]),
        target_system=intake.target_system,
        target_system_fit_gap_mapping=get_fit_gap_mapping(
            intake.process_key,
            intake.target_system,
        ),
        current_state_sop_draft=intake.current_state_sop_draft,
        public_safe_sample_data_note=_public_safe_sample_data_note(),
    )


def _executive_summary(intake: IntakeAnswers, template: dict) -> str:
    pain_points = _join_items(_lower_first_items(_normalise_items(intake.pain_points)))
    return clean_sentence(
        f"{intake.company_name} needs a structured {template['name']} requirements pack "
        f"to reduce rework, clarify control ownership, and make {intake.erp_platform} "
        f"implementation decisions testable. The pack translates {pain_points} into "
        f"requirements for workflow, data, controls, reporting, audit trail, and UAT. "
        f"It is sized for {clean_fragment(intake.monthly_volume)} and frames the control design, "
        f"reporting outputs, and acceptance criteria needed within a target delivery "
        f"window of {clean_fragment(intake.deadline)}."
    )


def _business_problem(intake: IntakeAnswers, template: dict) -> str:
    return clean_sentence(
        f"The current {template['name']} process relies on {intake.current_tools}. "
        f"That creates avoidable risk around "
        f"{_join_items(_lower_first_items(_normalise_items(intake.pain_points)))} "
        f"and leaves finance without a consistent requirements baseline for process design, "
        f"configuration, controls, reporting, and UAT. The implementation needs clearer "
        f"ownership, defined data fields, control evidence, and acceptance criteria before "
        f"ERP optimisation or automation can be delivered with confidence."
    )


def _process_scope(intake: IntakeAnswers, template: dict) -> str:
    scope = _semicolon_join(_normalise_items(template["baseline_scope"]))
    return clean_sentence(
        f"The future-state scope covers {scope}. The design will support "
        f"{intake.entity_type.lower()} users on {intake.erp_platform}, with emphasis on "
        f"{intake.compliance_focus.lower()}."
    )


def _in_scope(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        f"{template['name']} requirements for the agreed {intake.entity_type.lower()} process.",
        (
            "Workflow, data, controls, reporting, audit trail, and UAT requirements "
            f"for {intake.erp_platform}."
        ),
        (
            "Process pain points covering "
            f"{_join_items(_lower_first_items(_normalise_items(intake.pain_points)))}."
        ),
        f"Reporting requirement: {clean_fragment(intake.reporting_needs)}.",
        (
            "Implementation window and readiness assumptions for the "
            f"{clean_fragment(intake.deadline)} target window."
        ),
    ]


def _out_of_scope(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        "Live system configuration, data migration execution, and production cutover.",
        "Custom integration build or external workflow automation.",
        "Legal, tax, HR, or statutory sign-off outside the finance process owner remit.",
        "Direct processing of operational production data.",
        f"Process areas outside {template['name']} unless approved as a separate phase.",
    ]


def _stakeholders_and_roles(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        f"{intake.sponsor}: accountable for business sign-off and prioritisation.",
        f"{template['name']} process owner: validates workflow scope, controls, and exceptions.",
        "Finance systems analyst: translates requirements into configuration and UAT coverage.",
        "Preparer or operational user: confirms day-to-day inputs, handoffs, and evidence needs.",
        (
            "Reviewer or controller: approves control design, reporting outputs, and "
            "acceptance criteria."
        ),
    ]


def _assumptions(intake: IntakeAnswers) -> list[str]:
    base_assumptions = [
        "The pack is a requirements accelerator and does not replace finance owner sign-off.",
        "System configuration will follow approved finance policies and access controls.",
    ]
    return base_assumptions + list(intake.assumptions)


def _implementation_notes(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        f"Confirm {template['name']} process owner and reviewer roles before design sign-off.",
        f"Validate the required data fields against {intake.erp_platform} configuration.",
        "Run UAT with approved sample scenarios before production data migration or cutover.",
        "Keep any future AI-assisted drafting behind structured templates and human approval.",
    ]


def _reporting_requirements(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        f"RPT-01: Provide {clean_fragment(intake.reporting_needs)}.",
        (
            "RPT-02: Show owner, status, ageing, exception reason, and next action "
            f"where relevant to {template['name']}."
        ),
        "RPT-03: Support finance manager review with exportable period-end evidence.",
        "RPT-04: Separate open exceptions from completed, approved, or signed-off items.",
        (
            "RPT-05: Make reporting outputs readable by finance users without system "
            "administrator access."
        ),
    ]


def _public_safe_sample_data_note() -> str:
    return (
        "This pack was generated from fictional, public-safe sample inputs. It does not "
        "contain real employer, client, supplier, bank, VAT, payroll, or operational data. "
        "Do not upload confidential business information into a public demo."
    )


def _personalise_requirements(items: list[str], prefix: str) -> list[str]:
    return [
        f"{prefix}-{index:02d}: {item}"
        for index, item in enumerate(items, start=1)
    ]


def _join_items(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def _normalise_items(items: list[str]) -> list[str]:
    return clean_items(items)


def _lower_first_items(items: list[str]) -> list[str]:
    return [f"{item[:1].lower()}{item[1:]}" if item else item for item in items]


def _semicolon_join(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]}; and {items[1]}"
    return f"{'; '.join(items[:-1])}; and {items[-1]}"
