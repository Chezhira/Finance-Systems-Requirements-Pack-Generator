import app
from finance_requirements_generator import generate_pack
from finance_requirements_generator.process_library import load_all_templates
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS


def test_app_and_core_imports() -> None:
    assert callable(app.main)
    assert callable(generate_pack)


def test_sample_generation_smoke() -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["bank_reconciliation"])

    assert pack.process_name == "Bank Reconciliation"
    assert pack.uat_test_cases[0].test_id == "UAT-01"


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
