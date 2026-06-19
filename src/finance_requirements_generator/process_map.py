from __future__ import annotations

from finance_requirements_generator.schemas import IntakeAnswers, SOPDraft
from finance_requirements_generator.text_cleanup import clean_fragment


def generate_mermaid_process_map(process_name: str, intake: IntakeAnswers) -> str:
    trigger = _trigger_label(process_name, intake.current_state_sop_draft)
    source = _source_label(intake)
    approval = _approval_label(process_name, intake.current_state_sop_draft)
    reporting = _reporting_label(intake)
    signoff = f"{process_name} sign-off / readiness"
    return "\n".join(
        [
            "flowchart TD",
            f"    A[{_escape_mermaid(trigger)}] --> B[{_escape_mermaid(source)}]",
            f"    B --> C[{_escape_mermaid('Validate data, ownership, and required evidence')}]",
            "    C --> D{Exception or control gap?}",
            "    D -- Yes --> E[Resolve exception and update evidence]",
            f"    D -- No --> F[{_escape_mermaid(approval)}]",
            f"    E --> F[{_escape_mermaid(approval)}]",
            f"    F --> G[{_escape_mermaid(reporting)}]",
            f"    G --> H[{_escape_mermaid(signoff)}]",
        ]
    )


def generate_process_map_summary(process_name: str, intake: IntakeAnswers) -> list[str]:
    return [
        f"Trigger: {_trigger_label(process_name, intake.current_state_sop_draft)}.",
        f"Intake/source: {_source_label(intake)}.",
        "Validation: confirm data completeness, ownership, control evidence, and exception status.",
        "Exception handling: route exceptions to the process owner before approval or readiness.",
        f"Approval/review: {_approval_label(process_name, intake.current_state_sop_draft)}.",
        f"Reporting/evidence: {_reporting_label(intake)}.",
        (
            f"Sign-off/readiness: confirm {process_name} evidence and acceptance criteria "
            "before build."
        ),
    ]


def _trigger_label(process_name: str, sop: SOPDraft | None) -> str:
    if sop and sop.trigger:
        return clean_fragment(sop.trigger)
    return f"{process_name} trigger"


def _source_label(intake: IntakeAnswers) -> str:
    return clean_fragment(intake.current_tools) or "Capture source documents and process data"


def _approval_label(process_name: str, sop: SOPDraft | None) -> str:
    if sop and sop.controls_and_approvals:
        return clean_fragment(sop.controls_and_approvals[0])
    return f"{process_name} approval / review"


def _reporting_label(intake: IntakeAnswers) -> str:
    return clean_fragment(intake.reporting_needs) or "Evidence and reporting"


def _escape_mermaid(value: str) -> str:
    return value.replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")")
