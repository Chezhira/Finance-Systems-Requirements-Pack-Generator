import pytest
from eval_helpers import PROCESS_KEYS, generated_pack

EVIDENCE_TERMS = {
    "approval",
    "audit",
    "document",
    "evidence",
    "file",
    "history",
    "keep",
    "log",
    "notes",
    "preserve",
    "record",
    "reconciliation",
    "register",
    "report",
    "review",
    "schedule",
    "status",
    "store",
    "timestamp",
    "track",
    "workflow",
}


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_control_risk_rows_have_complete_finance_control_coverage(process_key: str) -> None:
    pack = generated_pack(process_key)

    for row in pack.control_risk_matrix:
        assert row.risk_area
        assert row.risk_description
        assert row.control_objective
        assert row.control_activity
        assert row.control_type
        assert row.owner
        assert row.evidence_required
        assert row.system_data_dependency
        assert row.residual_risk_implementation_note
        assert row.related_uat_case.startswith("UAT-")


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_control_evidence_is_specific_enough_for_finance_review(process_key: str) -> None:
    pack = generated_pack(process_key)

    for row in pack.control_risk_matrix:
        evidence = row.evidence_required.strip().lower()
        assert len(evidence) >= 20
        assert any(term in evidence for term in EVIDENCE_TERMS), evidence

