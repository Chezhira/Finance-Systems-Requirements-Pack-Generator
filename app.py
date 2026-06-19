from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import streamlit as st
import streamlit.components.v1 as components

from finance_requirements_generator.exports import (
    pack_control_risk_csv_bytes,
    pack_control_risk_xlsx_bytes,
    pack_process_map_html_bytes,
    pack_to_docx_bytes,
    pack_to_markdown,
)
from finance_requirements_generator.process_library import SUPPORTED_PROCESSES, load_all_templates
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.schemas import IntakeAnswers
from finance_requirements_generator.sop_intake import (
    GuidedSOPAnswers,
    extract_text_from_upload,
    guided_answers_to_mapped_fields,
    map_sop_text_to_intake,
    sop_draft_to_text,
)
from finance_requirements_generator.system_mapping import TARGET_SYSTEMS
from finance_requirements_generator.template_engine import generate_pack

PACK_PREVIEW_FIELDS = [
    ("Executive Summary", "executive_summary"),
    ("Business Problem", "business_problem"),
    ("Process Scope", "process_scope"),
    ("In Scope", "in_scope"),
    ("Out of Scope", "out_of_scope"),
    ("Stakeholders and Roles", "stakeholders_and_roles"),
    ("Functional Requirements", "functional_requirements"),
    ("Data Requirements", "data_requirements"),
    ("Controls and Audit Trail", "controls_and_audit_trail"),
    ("Reporting Requirements", "reporting_requirements"),
    ("User Stories", "user_stories"),
    ("UAT Test Cases", "uat_test_cases"),
    ("Acceptance Criteria", "acceptance_criteria"),
    ("Risks and Dependencies", "risks_and_dependencies"),
    ("Current-State SOP Draft", "current_state_sop_draft"),
    ("Target-System Fit-Gap Mapping", "target_system_fit_gap_mapping"),
]

INTAKE_MODES = [
    "Manual requirements intake",
    "Upload SOP / workflow document",
    "Build SOP from guided questions",
]


def main() -> None:
    st.set_page_config(
        page_title="Finance Requirements Pack Generator",
        layout="wide",
    )
    templates = load_all_templates()

    st.title("Finance Systems Requirements Pack Generator")
    st.caption("BRD, controls, and UAT accelerator for ERP finance transformation.")

    st.markdown(
        "Weak finance requirements can turn ERP and automation projects into rework. "
        "This app converts a structured finance intake into a practical requirements pack "
        "covering controls, data, audit trail, user stories, UAT, and acceptance criteria."
    )

    selected_process = st.selectbox(
        "Finance process",
        options=list(SUPPORTED_PROCESSES),
        format_func=lambda key: process_option_label(key, templates),
    )
    process_key = resolve_process_key(selected_process, templates)
    sample = DEFAULT_SAMPLE_INPUTS[process_key]
    intake_mode = st.radio("Intake mode", INTAKE_MODES, horizontal=True)
    target_system = st.selectbox(
        "Target ERP/system for candidate fit-gap mapping",
        options=["No target-system mapping", *TARGET_SYSTEMS],
        index=0,
        help=(
            "Uses curated repository mappings only. Candidate mapping requires implementation "
            "validation and does not guarantee ERP capability."
        ),
    )
    mapped_fields = None

    if intake_mode == "Upload SOP / workflow document":
        st.warning(
            "Upload only public-safe files. Do not upload confidential employer, client, "
            "supplier, bank, VAT, payroll, or operational data into a public demo."
        )
        uploaded_file = st.file_uploader(
            "Upload SOP or workflow document",
            type=["txt", "md", "markdown", "docx"],
        )
        if uploaded_file is not None:
            try:
                extracted_text = extract_text_from_upload(
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                )
                mapped_fields = map_sop_text_to_intake(extracted_text, sample)
                st.text_area(
                    "Extracted SOP text preview",
                    extracted_text,
                    height=160,
                    help="Review the extracted text before using mapped intake fields.",
                )
                if mapped_fields.sop_draft:
                    st.text_area(
                        "Mapped current-state SOP draft",
                        sop_draft_to_text(mapped_fields.sop_draft),
                        height=220,
                    )
            except ValueError as exc:
                st.error(str(exc))

    if intake_mode == "Build SOP from guided questions":
        mapped_fields = render_guided_sop_builder(templates[process_key]["name"], sample)

    with st.form("intake_form"):
        left, right = st.columns(2)
        with left:
            company_name = st.text_input("Fictional company name", sample.company_name)
            entity_type = st.text_input("Entity type", sample.entity_type)
            erp_platform = st.text_input(
                "ERP/current platform",
                (
                    target_system
                    if target_system != "No target-system mapping"
                    else sample.erp_platform
                ),
            )
            monthly_volume = st.text_input("Monthly/period volume", sample.monthly_volume)
            deadline = st.text_input("Target delivery window", sample.deadline)
        with right:
            current_tools = st.text_area(
                "Current tools/process",
                mapped_fields.current_tools if mapped_fields else sample.current_tools,
            )
            reporting_needs = st.text_area(
                "Reporting requirement",
                mapped_fields.reporting_needs if mapped_fields else sample.reporting_needs,
            )
            compliance_focus = st.text_area(
                "Compliance/control focus",
                mapped_fields.compliance_focus if mapped_fields else sample.compliance_focus,
            )
            pain_point_options = templates[process_key]["pain_point_prompts"]
            default_pain_points = safe_multiselect_defaults(
                mapped_fields.pain_points if mapped_fields else sample.pain_points,
                pain_point_options,
            )
            pain_points = st.multiselect(
                "Pain points",
                options=pain_point_options,
                default=default_pain_points,
            )
            control_options = templates[process_key]["controls"]
            default_controls = safe_multiselect_defaults(
                mapped_fields.control_concerns if mapped_fields else sample.control_concerns,
                control_options,
            )
            control_concerns = st.multiselect(
                "Control concerns",
                options=control_options,
                default=default_controls,
            )
        submitted = st.form_submit_button("Generate requirements pack")

    intake = IntakeAnswers(
        process_key=process_key,
        company_name=company_name,
        entity_type=entity_type,
        current_tools=current_tools,
        erp_platform=erp_platform,
        monthly_volume=monthly_volume,
        pain_points=pain_points,
        control_concerns=control_concerns,
        reporting_needs=reporting_needs,
        compliance_focus=compliance_focus,
        deadline=deadline,
        assumptions=sample.assumptions + (mapped_fields.assumptions if mapped_fields else []),
        target_system="" if target_system == "No target-system mapping" else target_system,
        current_state_sop_draft=mapped_fields.sop_draft if mapped_fields else None,
    )
    pack = generate_pack(intake)

    if submitted:
        st.success("Requirements pack generated.")

    render_pack(pack)
    render_visual_outputs(pack)
    render_downloads(pack)
    render_gallery()


def safe_multiselect_defaults(defaults: list[str], options: list[str]) -> list[str]:
    return [item for item in defaults if item in options] or options[:2]


def process_option_label(process_key: str, templates: dict) -> str:
    if process_key in templates:
        return templates[process_key]["name"]
    return process_key


def resolve_process_key(selected_process: str, templates: dict) -> str:
    if selected_process in templates:
        return selected_process
    for process_key, template in templates.items():
        if selected_process == template["name"]:
            return process_key
    raise ValueError(f"Unsupported process selection: {selected_process}")


def render_pack(pack) -> None:
    st.subheader(f"{pack.process_name} Pack Preview")
    for title, value in preview_sections(pack):
        with st.expander(title, expanded=title == "Executive Summary"):
            if isinstance(value, str):
                st.write(value)
            else:
                for item in value:
                    st.markdown(f"- {item}")


def preview_sections(pack) -> list[tuple[str, object]]:
    values = []
    for title, field_name in PACK_PREVIEW_FIELDS:
        if field_name == "current_state_sop_draft" and not pack.current_state_sop_draft:
            continue
        if field_name == "target_system_fit_gap_mapping" and not pack.target_system_fit_gap_mapping:
            continue
        if field_name == "controls_and_audit_trail":
            value = pack.controls + pack.audit_trail_requirements
        elif field_name == "uat_test_cases":
            value = [
                f"{case.test_id}: {case.scenario} Expected result: {case.expected_result}"
                for case in pack.uat_test_cases
            ]
        elif field_name == "current_state_sop_draft":
            value = sop_draft_to_text(pack.current_state_sop_draft)
        elif field_name == "target_system_fit_gap_mapping":
            value = [
                (
                    f"{row.current_state_area}: {row.candidate_fit_gap_view} "
                    f"Impact: {row.requirement_impact} Validation: {row.validation_note}"
                )
                for row in pack.target_system_fit_gap_mapping
            ]
        else:
            value = getattr(pack, field_name)
        values.append((title, value))
    return values


def render_guided_sop_builder(process_name: str, sample: IntakeAnswers):
    st.markdown(
        "Answer current-state process questions to build a reviewable SOP draft before "
        "requirements pack generation."
    )
    left, right = st.columns(2)
    with left:
        trigger = st.text_input("Process trigger", "Invoice, period-end, or payroll event occurs")
        owner = st.text_input("Process owner", f"{process_name} Process Owner")
        systems = st.text_input("Systems/tools used", sample.current_tools)
        steps = st.text_area(
            "Key process steps",
            "Receive input\nValidate data\nReview exceptions\nApprove and post\nRetain evidence",
        )
        approvals = st.text_area("Approvals", "Process owner approval\nReviewer sign-off")
        handoffs = st.text_area("Handoffs", "Finance preparer to reviewer\nFinance to systems team")
    with right:
        controls = st.text_area("Controls", "\n".join(sample.control_concerns))
        reports = st.text_area("Reports", sample.reporting_needs)
        exceptions = st.text_area("Exceptions", "Missing evidence\nLate approval\nData mismatch")
        data_fields = st.text_area("Data fields", "Owner\nStatus\nAmount\nPeriod\nEvidence link")
        audit_evidence = st.text_area("Audit evidence", sample.compliance_focus)
        pain_points = st.text_area("Pain points", "\n".join(sample.pain_points))
        improvements = st.text_area(
            "Desired future-state improvements",
            "Clear owner workflow\nBetter reporting\nReviewable audit trail",
        )

    answers = GuidedSOPAnswers(
        process_trigger=trigger,
        process_owner=owner,
        systems_tools=systems,
        key_process_steps=split_lines(steps),
        approvals=split_lines(approvals),
        handoffs=split_lines(handoffs),
        controls=split_lines(controls),
        reports=split_lines(reports),
        exceptions=split_lines(exceptions),
        data_fields=split_lines(data_fields),
        audit_evidence=split_lines(audit_evidence),
        pain_points=split_lines(pain_points),
        desired_future_state_improvements=split_lines(improvements),
    )
    mapped_fields = guided_answers_to_mapped_fields(answers, process_name, sample.entity_type)
    if mapped_fields.sop_draft:
        st.text_area(
            "Current-state SOP draft for review",
            sop_draft_to_text(mapped_fields.sop_draft),
            height=260,
        )
    return mapped_fields


def split_lines(value: str) -> list[str]:
    return [line.strip(" -*") for line in value.splitlines() if line.strip(" -*")]


def render_downloads(pack) -> None:
    st.subheader("Export")
    col_a, col_b, col_c, col_d = st.columns(4)
    filename_base = pack.process_key.replace("_", "-")
    with col_a:
        st.download_button(
            "Download Markdown",
            data=pack_to_markdown(pack),
            file_name=f"{filename_base}-requirements-pack.md",
            mime="text/markdown",
        )
    with col_b:
        st.download_button(
            "Download DOCX",
            data=pack_to_docx_bytes(pack),
            file_name=f"{filename_base}-requirements-pack.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    with col_c:
        st.download_button(
            "Download Control-Risk CSV",
            data=pack_control_risk_csv_bytes(pack),
            file_name=f"{filename_base}-control-risk-matrix.csv",
            mime="text/csv",
        )
    with col_d:
        st.download_button(
            "Download Control-Risk XLSX",
            data=pack_control_risk_xlsx_bytes(pack),
            file_name=f"{filename_base}-control-risk-matrix.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )


def render_visual_outputs(pack) -> None:
    st.subheader("Visual Process Documentation")
    process_map_html = pack_process_map_html_bytes(pack)
    if hasattr(st, "iframe"):
        st.iframe(process_map_html.decode("utf-8"), height=720)
    else:
        components.html(process_map_html.decode("utf-8"), height=720, scrolling=True)
    st.caption("Open the downloaded HTML file directly in a browser to review or print the map.")
    html_col, source_col = st.columns(2)
    with html_col:
        st.download_button(
            "Download process map as HTML",
            data=process_map_html,
            file_name=f"{pack.process_key.replace('_', '-')}-process-map.html",
            mime="text/html",
        )
    with source_col:
        st.download_button(
            "Download Mermaid source",
            data=pack.mermaid_process_map,
            file_name=f"{pack.process_key.replace('_', '-')}-process-map.mmd",
            mime="text/plain",
        )
    with st.expander("Advanced: Mermaid source", expanded=False):
        st.code(pack.mermaid_process_map, language="mermaid")
    with st.expander("Control-risk matrix preview", expanded=False):
        st.dataframe(
            [
                {
                    "Risk Area": row.risk_area,
                    "Control Activity": row.control_activity,
                    "Control Type": row.control_type,
                    "Evidence Required": row.evidence_required,
                    "Related UAT Case": row.related_uat_case,
                }
                for row in pack.control_risk_matrix
            ],
            use_container_width=True,
        )


def render_gallery() -> None:
    st.subheader("Example Gallery")
    templates = load_all_templates()
    gallery_links = [
        (
            f"[{templates[process_key]['name']} pack]"
            f"(examples/generated_packs/{process_key}_requirements_pack.md)"
        )
        for process_key in SUPPORTED_PROCESSES
    ]
    st.markdown("\n".join(f"- {link}" for link in gallery_links))
    st.caption("Safety note: bundled examples use fictional, public-safe sample inputs.")


if __name__ == "__main__":
    main()
