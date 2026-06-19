from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.schemas import REQUIRED_SECTIONS
from finance_requirements_generator.template_engine import generate_pack


def test_sample_packs_include_required_sections() -> None:
    for intake in DEFAULT_SAMPLE_INPUTS.values():
        pack = generate_pack(intake)
        sections = pack.section_map()

        for section_name in REQUIRED_SECTIONS:
            assert sections[section_name], section_name

        assert len(pack.functional_requirements) >= 8
        assert len(pack.controls) >= 5
        assert len(pack.audit_trail_requirements) >= 5
        assert len(pack.reporting_requirements) >= 5
        assert len(pack.user_stories) >= 5
        assert len(pack.uat_test_cases) >= 6
        assert len(pack.acceptance_criteria) >= 5


def test_process_specific_language_is_present() -> None:
    rendered = {
        key: str(generate_pack(intake).section_map()).lower()
        for key, intake in DEFAULT_SAMPLE_INPUTS.items()
    }

    assert "duplicate invoice" in rendered["accounts_payable"]
    assert "payment approval" in rendered["accounts_payable"]
    assert "unmatched lines" in rendered["bank_reconciliation"]
    assert "ageing" in rendered["bank_reconciliation"]
    assert "suspense" in rendered["bank_reconciliation"]
    assert "reviewer sign-off" in rendered["bank_reconciliation"]
    assert "source registers" in rendered["vat_reconciliation"]
    assert "vat return boxes" in rendered["vat_reconciliation"]
    assert "gl vat control accounts" in rendered["vat_reconciliation"]
    assert "unallocated cash" in rendered["accounts_receivable"]
    assert "credit note" in rendered["accounts_receivable"]
    assert "write-off" in rendered["accounts_receivable"]
    assert "close task" in rendered["month_end_close"]
    assert "journal approval" in rendered["month_end_close"]
    assert "reviewer sign-off" in rendered["month_end_close"]
    assert "inventory valuation" in rendered["inventory_costing"]
    assert "landed cost" in rendered["inventory_costing"]
    assert "subledger-to-gl" in rendered["inventory_costing"]
    assert "counterparty confirmation" in rendered["intercompany_settlements"]
    assert "fx difference" in rendered["intercompany_settlements"]
    assert "elimination" in rendered["intercompany_settlements"]
    assert "starter" in rendered["payroll_controls"]
    assert "payment file" in rendered["payroll_controls"]
    assert "payroll register" in rendered["payroll_controls"]
