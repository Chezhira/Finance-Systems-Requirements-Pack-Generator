from __future__ import annotations

from finance_requirements_generator.process_library import load_process_template
from finance_requirements_generator.questionnaire import validate_intake
from finance_requirements_generator.schemas import IntakeAnswers, RequirementsPack, UATTestCase


def generate_pack(intake: IntakeAnswers) -> RequirementsPack:
    validate_intake(intake)
    template = load_process_template(intake.process_key)

    problem = _current_state_problem(intake, template)
    future_scope = _future_state_scope(intake, template)
    functional_requirements = _personalise_requirements(
        template["functional_requirements"],
        intake,
        prefix="FR",
    )

    return RequirementsPack(
        process_key=intake.process_key,
        process_name=template["name"],
        company_name=intake.company_name,
        executive_summary=_executive_summary(intake, template),
        current_state_problem=problem,
        future_state_scope=future_scope,
        assumptions=_assumptions(intake),
        functional_requirements=functional_requirements,
        non_functional_requirements=_personalise_requirements(
            template["non_functional_requirements"],
            intake,
            prefix="NFR",
        ),
        data_requirements=_personalise_requirements(
            template["data_requirements"],
            intake,
            prefix="DR",
        ),
        controls=_personalise_requirements(template["controls"], intake, prefix="CTRL"),
        audit_trail_requirements=_personalise_requirements(
            template["audit_trail_requirements"],
            intake,
            prefix="AUD",
        ),
        user_stories=list(template["user_stories"]),
        uat_test_cases=[
            UATTestCase(
                test_id=f"UAT-{index:02d}",
                scenario=item["scenario"],
                expected_result=item["expected"],
            )
            for index, item in enumerate(template["uat_test_cases"], start=1)
        ],
        acceptance_criteria=list(template["acceptance_criteria"]),
        risks_and_dependencies=list(template["risks_and_dependencies"]),
        implementation_notes=_implementation_notes(intake, template),
    )


def _executive_summary(intake: IntakeAnswers, template: dict) -> str:
    pain_points = _join_items(intake.pain_points)
    concerns = _join_items(intake.control_concerns)
    return (
        f"{intake.company_name} needs a structured {template['name']} requirements pack for "
        f"{intake.erp_platform}. The MVP scope turns current finance pain points "
        f"({pain_points}) into implementable requirements covering data capture, controls, "
        f"audit trail, UAT, and reporting. The design is sized for {intake.monthly_volume} "
        f"and prioritises {concerns} within a target delivery window of {intake.deadline}."
    )


def _current_state_problem(intake: IntakeAnswers, template: dict) -> str:
    return (
        f"The current {template['name'].lower()} process relies on {intake.current_tools}. "
        f"This creates avoidable risk around {_join_items(intake.pain_points)} and makes "
        f"{intake.reporting_needs.lower()} harder to produce consistently. Finance needs "
        f"clearer ownership, data standards, and review evidence before the process is ready "
        f"for ERP optimisation or automation."
    )


def _future_state_scope(intake: IntakeAnswers, template: dict) -> str:
    scope = " ".join(template["baseline_scope"])
    return (
        f"The future-state scope covers {scope} It will support {intake.entity_type.lower()} "
        f"users on {intake.erp_platform}, with emphasis on {intake.compliance_focus.lower()}."
    )


def _assumptions(intake: IntakeAnswers) -> list[str]:
    base_assumptions = [
        "All sample names and operating details in this pack are synthetic.",
        "The pack is a requirements accelerator and does not replace finance owner sign-off.",
        "System configuration will follow approved finance policies and access controls.",
    ]
    return base_assumptions + list(intake.assumptions)


def _implementation_notes(intake: IntakeAnswers, template: dict) -> list[str]:
    return [
        f"Confirm {template['name']} process owner and reviewer roles before design sign-off.",
        f"Validate the required data fields against {intake.erp_platform} configuration.",
        "Run UAT with synthetic examples before loading production data.",
        "Keep any future AI-assisted drafting behind structured templates and human approval.",
    ]


def _personalise_requirements(items: list[str], intake: IntakeAnswers, prefix: str) -> list[str]:
    return [
        f"{prefix}-{index:02d}: {item}"
        for index, item in enumerate(items, start=1)
    ] + [
        f"{prefix}-{len(items) + 1:02d}: Provide reporting for {intake.reporting_needs}.",
        f"{prefix}-{len(items) + 2:02d}: Evidence {intake.compliance_focus} for finance review.",
    ]


def _join_items(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])}, and {items[-1]}"
