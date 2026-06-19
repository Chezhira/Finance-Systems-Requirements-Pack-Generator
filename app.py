from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import streamlit as st

from finance_requirements_generator.exports import pack_to_docx_bytes, pack_to_markdown
from finance_requirements_generator.process_library import SUPPORTED_PROCESSES, load_all_templates
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.schemas import IntakeAnswers
from finance_requirements_generator.template_engine import generate_pack


def main() -> None:
    st.set_page_config(
        page_title="Finance Requirements Pack Generator",
        layout="wide",
    )
    templates = load_all_templates()

    st.title("Finance Systems Requirements Pack Generator")
    st.caption("Synthetic BRD, controls, and UAT accelerator for ERP finance transformation.")

    st.markdown(
        "Weak finance requirements can turn ERP and automation projects into rework. "
        "This app converts a structured finance intake into a practical requirements pack "
        "covering controls, data, audit trail, user stories, UAT, and acceptance criteria."
    )

    process_key = st.selectbox(
        "Finance process",
        options=list(SUPPORTED_PROCESSES),
        format_func=lambda key: templates[key]["name"],
    )
    sample = DEFAULT_SAMPLE_INPUTS[process_key]

    with st.form("intake_form"):
        left, right = st.columns(2)
        with left:
            company_name = st.text_input("Synthetic company name", sample.company_name)
            entity_type = st.text_input("Entity type", sample.entity_type)
            erp_platform = st.text_input("ERP/current platform", sample.erp_platform)
            monthly_volume = st.text_input("Monthly/period volume", sample.monthly_volume)
            deadline = st.text_input("Target delivery window", sample.deadline)
        with right:
            current_tools = st.text_area("Current tools/process", sample.current_tools)
            reporting_needs = st.text_area("Reporting requirement", sample.reporting_needs)
            compliance_focus = st.text_area("Compliance/control focus", sample.compliance_focus)
            pain_points = st.multiselect(
                "Pain points",
                options=templates[process_key]["pain_point_prompts"],
                default=sample.pain_points,
            )
            control_options = templates[process_key]["controls"]
            default_controls = [
                item for item in sample.control_concerns if item in control_options
            ] or control_options[:2]
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
        assumptions=sample.assumptions,
    )
    pack = generate_pack(intake)

    if submitted:
        st.success("Requirements pack generated.")

    render_pack(pack)
    render_downloads(pack)
    render_gallery()


def render_pack(pack) -> None:
    st.subheader(f"{pack.process_name} Pack Preview")
    for title, value in [
        ("Executive Summary", pack.executive_summary),
        ("Current-State Problem Statement", pack.current_state_problem),
        ("Future-State Process Scope", pack.future_state_scope),
        ("Functional Requirements", pack.functional_requirements),
        ("Controls and Audit Trail", pack.controls + pack.audit_trail_requirements),
        ("User Stories", pack.user_stories),
        (
            "UAT Test Cases",
            [
                f"{case.test_id}: {case.scenario} Expected result: {case.expected_result}"
                for case in pack.uat_test_cases
            ],
        ),
        ("Acceptance Criteria", pack.acceptance_criteria),
        ("Risks and Dependencies", pack.risks_and_dependencies),
    ]:
        with st.expander(title, expanded=title == "Executive Summary"):
            if isinstance(value, str):
                st.write(value)
            else:
                for item in value:
                    st.markdown(f"- {item}")


def render_downloads(pack) -> None:
    st.subheader("Export")
    col_a, col_b = st.columns(2)
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


def render_gallery() -> None:
    st.subheader("Example Gallery")
    gallery_links = [
        "[Accounts payable pack](examples/generated_packs/accounts_payable_requirements_pack.md)",
        (
            "[Bank reconciliation pack]"
            "(examples/generated_packs/bank_reconciliation_requirements_pack.md)"
        ),
        (
            "[VAT reconciliation pack]"
            "(examples/generated_packs/vat_reconciliation_requirements_pack.md)"
        ),
    ]
    st.markdown("\n".join(f"- {link}" for link in gallery_links))
    st.caption("All bundled examples are synthetic and safe for public portfolio use.")


if __name__ == "__main__":
    main()
