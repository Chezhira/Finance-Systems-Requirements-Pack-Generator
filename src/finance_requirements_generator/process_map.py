from __future__ import annotations

from finance_requirements_generator.schemas import IntakeAnswers, ProcessMapFlow, SOPDraft
from finance_requirements_generator.text_cleanup import clean_fragment


def generate_process_map_flow(process_name: str, intake: IntakeAnswers) -> ProcessMapFlow:
    return ProcessMapFlow(
        trigger=_trigger_label(process_name, intake.current_state_sop_draft),
        source=_source_label(intake),
        validation="Validate data, ownership, and required evidence",
        decision="Exception or control gap?",
        exception_resolution="Resolve exception and update evidence",
        approval=_approval_label(process_name, intake.current_state_sop_draft),
        reporting=_reporting_label(intake),
        signoff=f"{process_name} sign-off / readiness",
    )


def render_mermaid_process_map(flow: ProcessMapFlow) -> str:
    return "\n".join(
        [
            "flowchart LR",
            f"    A[{_escape_mermaid(flow.trigger)}] --> B[{_escape_mermaid(flow.source)}]",
            f"    B --> C[{_escape_mermaid(flow.validation)}]",
            f"    C --> D{{{_escape_mermaid(flow.decision)}}}",
            f"    D -- Yes --> E[{_escape_mermaid(flow.exception_resolution)}]",
            f"    D -- No --> F[{_escape_mermaid(flow.approval)}]",
            f"    E --> F[{_escape_mermaid(flow.approval)}]",
            f"    F --> G[{_escape_mermaid(flow.reporting)}]",
            f"    G --> H[{_escape_mermaid(flow.signoff)}]",
            "    class A,H gate",
            "    class B,C,F,G step",
            "    class D decide",
            "    class E fix",
            "    classDef gate fill:#0f1b2d,stroke:#0f1b2d,color:#ffffff,font-weight:600",
            "    classDef step fill:#ffffff,stroke:#0e7c66,color:#0f1b2d,stroke-width:2px",
            "    classDef decide fill:#fef3c7,stroke:#b45309,color:#7c2d12,stroke-width:2px",
            "    classDef fix fill:#fee2e2,stroke:#b91c1c,color:#7f1d1d,stroke-width:2px",
        ]
    )


def render_process_map_summary(flow: ProcessMapFlow, process_name: str) -> list[str]:
    return [
        f"Trigger: {flow.trigger}.",
        f"Intake/source: {flow.source}.",
        "Validation: confirm data completeness, ownership, control evidence, and exception status.",
        "Exception handling: route exceptions to the process owner before approval or readiness.",
        f"Approval/review: {flow.approval}.",
        f"Reporting/evidence: {flow.reporting}.",
        (
            f"Sign-off/readiness: confirm {process_name} evidence and acceptance criteria "
            "before build."
        ),
    ]


def generate_mermaid_process_map(process_name: str, intake: IntakeAnswers) -> str:
    return render_mermaid_process_map(generate_process_map_flow(process_name, intake))


def generate_process_map_summary(process_name: str, intake: IntakeAnswers) -> list[str]:
    flow = generate_process_map_flow(process_name, intake)
    return render_process_map_summary(flow, process_name)


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
