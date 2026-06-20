from __future__ import annotations

import inspect
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
    pack_to_readiness_docx_bytes,
    pack_to_readiness_markdown,
)
from finance_requirements_generator.process_library import SUPPORTED_PROCESSES, load_all_templates
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.readiness_engine import generate_implementation_readiness_pack
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

APP_STYLES = """
<style>
  :root {
    --finance-ink:#142238;
    --finance-green:#0e7c66;
    --finance-gold:#b78323;
    --finance-muted:#667085;
    --finance-line:#d9e0e8;
    --finance-surface:#ffffff;
    --finance-bg:#f4f6f8;
  }
  [data-testid="stAppViewContainer"] { background:var(--finance-bg); }
  [data-testid="stHeader"] { background:rgba(244,246,248,.94); }
  .block-container { max-width:1480px; padding-top:1.8rem; padding-bottom:3.5rem; }
  .app-header {
    padding:0 0 1.35rem; margin-bottom:1.2rem; border-bottom:1px solid var(--finance-line);
  }
  .app-eyebrow {
    margin:0 0 .45rem; color:var(--finance-green); font-size:.72rem; font-weight:700;
    letter-spacing:.16em; text-transform:uppercase;
  }
  .app-header h1 {
    margin:0; color:var(--finance-ink); font-size:2rem; line-height:1.2; letter-spacing:0;
  }
  .app-header p {
    max-width:860px; margin:.55rem 0 0; color:#475467; font-size:1rem; line-height:1.55;
  }
  .section-heading { margin:.2rem 0 .8rem; }
  .section-index {
    display:inline-block; min-width:2rem; color:var(--finance-gold); font-size:.72rem;
    font-weight:800; letter-spacing:.12em;
  }
  .section-heading h2 {
    display:inline; margin:0; color:var(--finance-ink); font-size:1.32rem; letter-spacing:0;
  }
  .section-heading p { margin:.32rem 0 0 2.05rem; color:var(--finance-muted); font-size:.9rem; }
  div[data-testid="stForm"] {
    padding:1.2rem 1.25rem 1.3rem; background:var(--finance-surface);
    border:1px solid var(--finance-line); border-radius:8px;
  }
  div[data-testid="stExpander"] {
    background:var(--finance-surface); border-color:var(--finance-line);
  }
  div[data-testid="stTabs"] [data-baseweb="tab-list"] { gap:.25rem; }
  div[data-testid="stTabs"] button { font-weight:600; }
  div[data-testid="stDownloadButton"] button { width:100%; min-height:2.55rem; }
  div[data-testid="stAlert"] { border-radius:6px; }
  .download-group-title {
    margin:0 0 .2rem; color:var(--finance-ink); font-size:.93rem; font-weight:700;
  }
  .download-group-copy { margin:0 0 .75rem; color:var(--finance-muted); font-size:.8rem; }
  .public-safe-note { color:var(--finance-muted); font-size:.8rem; }
  [data-testid="stMetric"] {
    background:var(--finance-surface); border:1px solid var(--finance-line);
    border-radius:8px; padding:1rem 1.15rem;
  }
  [data-testid="stMetricLabel"] {
    color:var(--finance-muted); text-transform:uppercase;
    font-size:.7rem; letter-spacing:.08em;
  }
  [data-testid="stMetricValue"] { color:var(--finance-ink); font-weight:700; }
  .empty-state {
    padding:1.3rem 1.4rem; background:var(--finance-surface);
    border:1px dashed var(--finance-line); border-radius:8px;
  }
  .empty-state p { margin:0; color:var(--finance-muted); font-size:.92rem; line-height:1.55; }
  hr { border-color:var(--finance-line); opacity:.55; margin:1.6rem 0; }
</style>
"""


def main() -> None:
    st.set_page_config(
        page_title="Finance Requirements Pack Generator",
        layout="wide",
    )
    inject_app_styles()
    templates = load_all_templates()
    render_app_header()
    render_section_header(
        "01",
        "Intake",
        "Set the finance process, discovery route, target-system context, and "
        "implementation needs.",
    )
    selector_left, selector_right = st.columns([1, 1])
    with selector_left:
        selected_process = st.selectbox(
            "Finance process",
            options=list(SUPPORTED_PROCESSES),
            format_func=lambda key: process_option_label(key, templates),
        )
    process_key = resolve_process_key(selected_process, templates)
    sample = DEFAULT_SAMPLE_INPUTS[process_key]
    with selector_right:
        target_system = st.selectbox(
            "Target ERP/system",
            options=["No target-system mapping", *TARGET_SYSTEMS],
            index=0,
            help=(
                "Uses curated repository mappings only. Candidate mapping requires implementation "
                "validation and does not guarantee ERP capability."
            ),
        )
    intake_mode = select_intake_mode()
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
        st.markdown("#### Organisation and delivery context")
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
                "Current tools and workflow",
                mapped_fields.current_tools if mapped_fields else sample.current_tools,
            )
            reporting_needs = st.text_area(
                "Reporting and management information",
                mapped_fields.reporting_needs if mapped_fields else sample.reporting_needs,
            )
        st.divider()
        st.markdown("#### Process risks, controls, and evidence")
        left, right = st.columns(2)
        with left:
            compliance_focus = st.text_area(
                "Compliance, control, and audit focus",
                mapped_fields.compliance_focus if mapped_fields else sample.compliance_focus,
            )
            pain_point_options = templates[process_key]["pain_point_prompts"]
            default_pain_points = safe_multiselect_defaults(
                mapped_fields.pain_points if mapped_fields else sample.pain_points,
                pain_point_options,
            )
            pain_points = st.multiselect(
                "Priority pain points",
                options=pain_point_options,
                default=default_pain_points,
            )
        with right:
            control_options = templates[process_key]["controls"]
            default_controls = safe_multiselect_defaults(
                mapped_fields.control_concerns if mapped_fields else sample.control_concerns,
                control_options,
            )
            control_concerns = st.multiselect(
                "Priority control concerns",
                options=control_options,
                default=default_controls,
            )
        submitted = st.form_submit_button("Generate finance systems pack", type="primary")

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
    if submitted:
        st.session_state["pack_generated"] = True

    if not st.session_state.get("pack_generated"):
        render_empty_state()
        render_gallery()
        return

    pack = generate_pack(intake)
    readiness_pack = generate_implementation_readiness_pack(pack)
    process_map_html = pack_process_map_html_bytes(pack)

    if submitted:
        st.success("Finance systems requirements and readiness outputs generated.")

    st.divider()
    render_section_header(
        "02",
        "Requirements Pack",
        "Review scope, requirements, controls, UAT coverage, and implementation dependencies.",
    )
    render_pack_summary(pack, readiness_pack)
    render_pack(pack)
    st.divider()
    render_section_header(
        "03",
        "Visual Process Documentation",
        "Inspect the deterministic finance control flow and keep Mermaid as a secondary artefact.",
    )
    render_visual_outputs(pack, process_map_html)
    st.divider()
    render_section_header(
        "04",
        "Control-Risk Matrix",
        "Compare process risks, control activities, evidence expectations, and related UAT cases.",
    )
    render_control_risk_matrix(pack)
    st.divider()
    render_section_header(
        "05",
        "Implementation Readiness",
        "Review readiness evidence, target-system validation, workshop prompts, and "
        "open decisions.",
    )
    render_implementation_readiness(readiness_pack)
    st.divider()
    render_section_header(
        "06",
        "Downloads",
        "Download each implementation artefact in its most useful review format.",
    )
    render_downloads(pack, readiness_pack, process_map_html)
    render_gallery()


def inject_app_styles() -> None:
    st.markdown(APP_STYLES, unsafe_allow_html=True)


def render_app_header() -> None:
    st.markdown(
        """<header class="app-header">
          <p class="app-eyebrow">Finance systems · ERP implementation</p>
          <h1>Finance Systems Requirements Pack Generator</h1>
          <p>Turn finance process knowledge into reviewable requirements, controls, UAT evidence,
          process documentation, and implementation-readiness outputs.</p>
        </header>""",
        unsafe_allow_html=True,
    )


def render_section_header(index: str, title: str, description: str) -> None:
    st.markdown(
        f"""<div class="section-heading">
          <span class="section-index">{index}</span><h2>{title}</h2>
          <p>{description}</p>
        </div>""",
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        '<div class="empty-state"><p>Configure the intake above, then select '
        "<strong>Generate finance systems pack</strong> to produce the requirements, controls, "
        "UAT coverage, process map, and implementation-readiness outputs.</p></div>",
        unsafe_allow_html=True,
    )


def render_pack_summary(pack, readiness_pack) -> None:
    col_a, col_b, col_c, col_d, col_e = st.columns(5)
    col_a.metric("Functional requirements", len(pack.functional_requirements))
    col_b.metric("Controls", len(pack.controls) + len(pack.audit_trail_requirements))
    col_c.metric("UAT cases", len(pack.uat_test_cases))
    col_d.metric("Risk areas", len(pack.control_risk_matrix))
    col_e.metric("Open decisions", len(readiness_pack.open_decisions_and_dependencies))


def select_intake_mode() -> str:
    if hasattr(st, "segmented_control"):
        selected = st.segmented_control(
            "Intake approach",
            INTAKE_MODES,
            default=INTAKE_MODES[0],
            selection_mode="single",
        )
        return selected or INTAKE_MODES[0]
    return st.radio("Intake approach", INTAKE_MODES, horizontal=True)


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
    sections = dict(preview_sections(pack))
    tabs = st.tabs(
        [
            "Scope & context",
            "Requirements",
            "Controls & evidence",
            "Stories & UAT",
            "Delivery",
        ]
    )
    groups = [
        [
            "Executive Summary",
            "Business Problem",
            "Process Scope",
            "In Scope",
            "Out of Scope",
            "Stakeholders and Roles",
        ],
        ["Functional Requirements", "Data Requirements", "Reporting Requirements"],
        ["Controls and Audit Trail", "Acceptance Criteria"],
        ["User Stories", "UAT Test Cases"],
        ["Risks and Dependencies", "Current-State SOP Draft", "Target-System Fit-Gap Mapping"],
    ]
    for tab, titles in zip(tabs, groups, strict=True):
        with tab:
            for title in titles:
                if title not in sections:
                    continue
                with st.expander(title, expanded=title == "Executive Summary"):
                    _render_preview_value(sections[title])


def _render_preview_value(value) -> None:
    if isinstance(value, str):
        st.write(value)
        return
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
    st.markdown("##### Guided current-state discovery")
    st.caption(
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


def render_downloads(pack, readiness_pack, process_map_html: bytes) -> None:
    col_a, col_b, col_c, col_d = st.columns(4)
    filename_base = pack.process_key.replace("_", "-")
    with col_a:
        with st.container(border=True):
            _download_group_header(
                "Requirements Pack",
                "Core scope, requirements, controls, and UAT.",
            )
            st.download_button(
                "Download DOCX",
                data=pack_to_docx_bytes(pack),
                file_name=f"{filename_base}-requirements-pack.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                type="primary",
            )
            st.download_button(
                "Download Markdown",
                data=pack_to_markdown(pack),
                file_name=f"{filename_base}-requirements-pack.md",
                mime="text/markdown",
            )
    with col_b:
        with st.container(border=True):
            _download_group_header("Process Flow", "Browser review plus technical Mermaid source.")
            st.download_button(
                "Download process map as HTML",
                data=process_map_html,
                file_name=f"{filename_base}-process-map.html",
                mime="text/html",
            )
            st.download_button(
                "Download Mermaid source",
                data=pack.mermaid_process_map,
                file_name=f"{filename_base}-process-map.mmd",
                mime="text/plain",
            )
    with col_c:
        with st.container(border=True):
            _download_group_header("Control-Risk Matrix", "Editable implementation control matrix.")
            st.download_button(
                "Download Control-Risk XLSX",
                data=pack_control_risk_xlsx_bytes(pack),
                file_name=f"{filename_base}-control-risk-matrix.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            st.download_button(
                "Download Control-Risk CSV",
                data=pack_control_risk_csv_bytes(pack),
                file_name=f"{filename_base}-control-risk-matrix.csv",
                mime="text/csv",
            )
    with col_d:
        with st.container(border=True):
            _download_group_header(
                "Implementation Readiness",
                "Evidence checks and workshop decisions.",
            )
            st.download_button(
                "Download readiness DOCX",
                data=pack_to_readiness_docx_bytes(readiness_pack),
                file_name=f"{filename_base}-implementation-readiness-pack.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                type="primary",
            )
            st.download_button(
                "Download readiness Markdown",
                data=pack_to_readiness_markdown(readiness_pack),
                file_name=f"{filename_base}-implementation-readiness-pack.md",
                mime="text/markdown",
            )


def _download_group_header(title: str, description: str) -> None:
    st.markdown(
        f'<p class="download-group-title">{title}</p>'
        f'<p class="download-group-copy">{description}</p>',
        unsafe_allow_html=True,
    )


def render_visual_outputs(pack, process_map_html: bytes) -> None:
    if hasattr(st, "iframe"):
        st.iframe(process_map_html.decode("utf-8"), height=680)
    else:
        components.html(process_map_html.decode("utf-8"), height=680, scrolling=True)
    with st.expander("Advanced: Mermaid source", expanded=False):
        st.code(pack.mermaid_process_map, language="mermaid")


def render_control_risk_matrix(pack) -> None:
    render_dataframe(
        [
            {
                "Risk Area": row.risk_area,
                "Control Activity": row.control_activity,
                "Control Type": row.control_type,
                "Evidence Required": row.evidence_required,
                "Related Requirement": row.related_requirement_id,
                "Related UAT Case": row.related_uat_case,
            }
            for row in pack.control_risk_matrix
        ]
    )
    st.caption(
        "The preview is intentionally compact. Use the XLSX download for the full "
        "implementation matrix."
    )


def render_implementation_readiness(readiness_pack) -> None:
    st.write(readiness_pack.readiness_summary)
    tabs = st.tabs(
        [
            "Process",
            "Target system",
            "Data",
            "Controls & UAT",
            "Workshop questions",
            "Cutover",
            "Open decisions",
        ]
    )
    check_sections = [
        readiness_pack.process_implementation_checklist,
        readiness_pack.target_system_readiness_checklist,
        readiness_pack.data_readiness_checklist,
        readiness_pack.controls_and_uat_readiness_checklist,
    ]
    for tab, checks in zip(tabs[:4], check_sections, strict=True):
        with tab:
            render_dataframe(_readiness_check_rows(checks))
    with tabs[4]:
        render_dataframe(
            [
                {
                    "ID": item.question_id,
                    "Question": item.question,
                    "Implementation relevance": item.implementation_relevance,
                    "Sources": ", ".join(item.source_references),
                }
                for item in readiness_pack.configuration_workshop_questions
            ]
        )
    with tabs[5]:
        render_dataframe(_readiness_check_rows(readiness_pack.cutover_readiness_notes))
    with tabs[6]:
        render_dataframe(
            [
                {
                    "ID": item.decision_id,
                    "Decision required": item.decision_required,
                    "Dependency / impact": item.dependency_or_impact,
                    "Suggested owner": item.suggested_decision_owner,
                    "Sources": ", ".join(item.source_references),
                }
                for item in readiness_pack.open_decisions_and_dependencies
            ]
        )
    st.caption(
        "All checks start as Not assessed. Review evidence and decisions with finance and the "
        "implementation team before configuration or cutover sign-off."
    )


def _readiness_check_rows(checks) -> list[dict[str, str]]:
    return [
        {
            "ID": item.check_id,
            "Finance-specific check": item.finance_specific_check,
            "Evidence required": item.evidence_required,
            "Suggested owner": item.suggested_owner_role,
            "Status": item.review_status,
            "Sources": ", ".join(item.source_references),
            "Validation note": item.validation_note,
        }
        for item in checks
    ]


def render_dataframe(data) -> None:
    if "width" in inspect.signature(st.dataframe).parameters:
        st.dataframe(data, width="stretch")
    else:
        st.dataframe(data, use_container_width=True)


def render_gallery() -> None:
    templates = load_all_templates()
    gallery_links = [
        (
            f"[{templates[process_key]['name']} pack]"
            f"(examples/generated_packs/{process_key}_requirements_pack.md)"
        )
        for process_key in SUPPORTED_PROCESSES
    ]
    with st.expander("Representative example outputs", expanded=False):
        st.markdown("\n".join(f"- {link}" for link in gallery_links))
    st.markdown(
        '<p class="public-safe-note">Public-safe note: bundled examples use fictional inputs. '
        "Do not upload confidential business information into a public demo.</p>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
