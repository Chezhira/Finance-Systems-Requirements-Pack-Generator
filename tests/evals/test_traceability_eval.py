import pytest
from eval_helpers import (
    PROCESS_KEYS,
    assert_reviewable_references,
    generated_pack,
    identifiers,
    readiness_checks,
    readiness_pack,
)


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_uat_cases_trace_to_finance_requirements(process_key: str) -> None:
    pack = generated_pack(process_key)
    requirement_ids = set(identifiers(pack.functional_requirements))
    explicit_uat_references = {
        row.related_uat_case for row in pack.control_risk_matrix if row.related_uat_case
    }
    readiness = readiness_pack(process_key)
    for item in readiness_checks(readiness):
        explicit_uat_references.update(
            reference for reference in item.source_references if reference.startswith("UAT-")
        )

    for case in pack.uat_test_cases:
        ordinal_requirement = case.test_id.replace("UAT-", "FR-", 1)
        assert ordinal_requirement in requirement_ids or case.test_id in explicit_uat_references


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_control_risk_rows_trace_to_valid_requirements_and_uat(process_key: str) -> None:
    pack = generated_pack(process_key)
    requirement_ids = set(identifiers(pack.functional_requirements))
    uat_ids = {case.test_id for case in pack.uat_test_cases}

    for row in pack.control_risk_matrix:
        assert row.related_requirement_id in requirement_ids
        assert row.related_uat_case in uat_ids


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_readiness_items_have_reviewable_source_references(process_key: str) -> None:
    pack = readiness_pack(process_key)

    for item in readiness_checks(pack):
        assert_reviewable_references(item.source_references)
    for item in pack.configuration_workshop_questions:
        assert_reviewable_references(item.source_references)
    for item in pack.open_decisions_and_dependencies:
        assert_reviewable_references(item.source_references)

