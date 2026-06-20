import pytest
from eval_helpers import PROCESS_KEYS, readiness_checks, readiness_pack


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
@pytest.mark.parametrize("target_system", ["", "Odoo"])
def test_all_readiness_sections_generate_for_selected_and_unselected_systems(
    process_key: str,
    target_system: str,
) -> None:
    pack = readiness_pack(process_key, target_system)

    assert pack.readiness_summary
    assert pack.process_implementation_checklist
    assert pack.target_system_readiness_checklist
    assert pack.data_readiness_checklist
    assert pack.controls_and_uat_readiness_checklist
    assert pack.configuration_workshop_questions
    assert pack.cutover_readiness_notes
    assert pack.open_decisions_and_dependencies

    for item in readiness_checks(pack):
        assert item.review_status == "Not assessed"
        assert item.evidence_required
        assert item.suggested_owner_role
        assert item.validation_note


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_unselected_target_system_creates_complete_scope_decision(process_key: str) -> None:
    pack = readiness_pack(process_key)
    decisions = " ".join(
        item.decision_required for item in pack.open_decisions_and_dependencies
    ).lower()

    for expected_term in (
        "target erp",
        "edition",
        "modules",
        "localisation",
        "integration",
        "implementation scope",
    ):
        assert expected_term in decisions

