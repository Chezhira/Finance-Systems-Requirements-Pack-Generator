import app
from finance_requirements_generator import generate_pack
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS


def test_app_and_core_imports() -> None:
    assert callable(app.main)
    assert callable(generate_pack)


def test_sample_generation_smoke() -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["bank_reconciliation"])

    assert pack.process_name == "Bank Reconciliation"
    assert pack.uat_test_cases[0].test_id == "UAT-01"
