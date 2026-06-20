import pytest
from eval_helpers import (
    PROCESS_KEYS,
    assert_unique,
    generated_pack,
    identifiers,
    readiness_checks,
    readiness_pack,
)


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_requirements_pack_has_complete_finance_structure(process_key: str) -> None:
    pack = generated_pack(process_key)

    assert pack.executive_summary
    assert pack.business_problem
    assert pack.process_scope
    assert pack.functional_requirements
    assert pack.data_requirements
    assert pack.controls
    assert pack.audit_trail_requirements
    assert pack.reporting_requirements
    assert pack.uat_test_cases
    assert pack.acceptance_criteria
    assert pack.risks_and_dependencies


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_generated_finance_artefact_ids_are_unique(process_key: str) -> None:
    pack = generated_pack(process_key)
    readiness = readiness_pack(process_key)

    for label, values in (
        ("functional requirement IDs", identifiers(pack.functional_requirements)),
        ("data requirement IDs", identifiers(pack.data_requirements)),
        ("control IDs", identifiers(pack.controls)),
        ("audit requirement IDs", identifiers(pack.audit_trail_requirements)),
        ("reporting requirement IDs", identifiers(pack.reporting_requirements)),
        ("UAT IDs", [case.test_id for case in pack.uat_test_cases]),
        ("readiness check IDs", [item.check_id for item in readiness_checks(readiness)]),
        (
            "workshop question IDs",
            [item.question_id for item in readiness.configuration_workshop_questions],
        ),
        (
            "open decision IDs",
            [item.decision_id for item in readiness.open_decisions_and_dependencies],
        ),
    ):
        assert_unique(values, label)

