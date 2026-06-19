from streamlit.testing.v1 import AppTest

import app
from finance_requirements_generator import generate_pack
from finance_requirements_generator.process_library import load_all_templates
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS


def test_app_and_core_imports() -> None:
    assert callable(app.main)
    assert callable(generate_pack)


def test_process_option_label_handles_keys_and_display_labels() -> None:
    templates = load_all_templates()

    assert app.process_option_label("accounts_payable", templates) == "Accounts Payable"
    assert app.process_option_label("Accounts Payable", templates) == "Accounts Payable"
    assert app.resolve_process_key("accounts_payable", templates) == "accounts_payable"
    assert app.resolve_process_key("Accounts Payable", templates) == "accounts_payable"


def test_sample_generation_smoke() -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["bank_reconciliation"])

    assert pack.process_name == "Bank Reconciliation"
    assert pack.uat_test_cases[0].test_id == "UAT-01"


def test_streamlit_process_map_source_is_secondary_and_collapsed() -> None:
    streamlit_app = AppTest.from_file("app.py", default_timeout=30).run()
    streamlit_app.button[0].click().run()

    assert not streamlit_app.exception
    download_labels = {item.label for item in streamlit_app.get("download_button")}
    advanced = [
        item
        for item in streamlit_app.expander
        if item.label == "Advanced: Mermaid source"
    ]

    assert advanced
    assert not advanced[0].proto.expanded
    assert "Download process map as HTML" in download_labels
    assert "Download Mermaid source" in download_labels


def test_streamlit_preview_fields_exist_on_generated_packs() -> None:
    for intake in DEFAULT_SAMPLE_INPUTS.values():
        pack = generate_pack(intake)
        preview = app.preview_sections(pack)

        assert preview
        preview_titles = [title for title, _value in preview]
        configured_titles = [title for title, _field in app.PACK_PREVIEW_FIELDS]
        assert set(preview_titles).issubset(configured_titles)
        assert "Current-State SOP Draft" not in preview_titles
        assert "Target-System Fit-Gap Mapping" not in preview_titles
        assert all(value for _title, value in preview)


def test_sample_pain_point_defaults_are_streamlit_safe() -> None:
    templates = load_all_templates()

    for process_key, sample in DEFAULT_SAMPLE_INPUTS.items():
        options = templates[process_key]["pain_point_prompts"]
        defaults = app.safe_multiselect_defaults(sample.pain_points, options)

        assert defaults
        assert set(defaults).issubset(options)


def test_sample_control_defaults_are_streamlit_safe() -> None:
    templates = load_all_templates()

    for process_key, sample in DEFAULT_SAMPLE_INPUTS.items():
        options = templates[process_key]["controls"]
        defaults = app.safe_multiselect_defaults(sample.control_concerns, options)

        assert defaults
        assert set(defaults).issubset(options)


def test_safe_multiselect_defaults_falls_back_to_first_two_options() -> None:
    defaults = app.safe_multiselect_defaults(
        ["Legacy label that is no longer an option"],
        ["Current option one", "Current option two", "Current option three"],
    )

    assert defaults == ["Current option one", "Current option two"]
