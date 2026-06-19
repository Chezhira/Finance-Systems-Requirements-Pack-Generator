from __future__ import annotations

from finance_requirements_generator.schemas import IntakeAnswers

DEFAULT_SAMPLE_INPUTS = {
    "accounts_payable": IntakeAnswers(
        process_key="accounts_payable",
        company_name="Northstar Trading Ltd",
        entity_type="Wholesale trading group",
        current_tools="Email approvals, shared AP tracker, and ERP purchase ledger",
        erp_platform="Odoo Finance",
        monthly_volume="1,200 supplier invoices per month",
        pain_points=[
            "Duplicate invoices",
            "Manual approval chasing",
            "Weak supplier master controls",
        ],
        control_concerns=["Payment approval evidence", "Segregation of duties"],
        reporting_needs="Aged approval backlog, blocked invoices, and payment readiness summary",
        compliance_focus="Internal audit review of supplier changes and payment controls",
        deadline="10 weeks",
        assumptions=["Supplier records are already uniquely identified in the ERP."],
    ),
    "bank_reconciliation": IntakeAnswers(
        process_key="bank_reconciliation",
        company_name="BlueRiver Foods Ltd",
        entity_type="Multi-site food distribution business",
        current_tools="Bank portal exports, ERP cashbook, and month-end spreadsheet reconciliation",
        erp_platform="Microsoft Dynamics 365 Business Central",
        monthly_volume="8 bank accounts with roughly 4,500 statement lines per month",
        pain_points=[
            "Unmatched bank statement lines",
            "Suspense account ageing",
            "Manual owner/status tracking",
        ],
        control_concerns=["Reviewer sign-off", "Manual match overrides"],
        reporting_needs="Daily unmatched item ageing and month-end reconciliation evidence pack",
        compliance_focus="Month-end close evidence and internal control review",
        deadline="8 weeks",
        assumptions=["Bank statement files use a consistent export format."],
    ),
    "vat_reconciliation": IntakeAnswers(
        process_key="vat_reconciliation",
        company_name="Demo Manufacturing Co",
        entity_type="VAT-registered manufacturing entity",
        current_tools="ERP tax reports, GL trial balance extracts, and offline VAT working papers",
        erp_platform="SAP Business One",
        monthly_volume="Quarterly VAT return with 15 active tax codes",
        pain_points=[
            "VAT return differences",
            "Manual source register checks",
            "Missing filing evidence",
        ],
        control_concerns=["VAT return box mapping", "GL VAT control account reconciliation"],
        reporting_needs="VAT source-to-return-to-GL reconciliation with difference owner status",
        compliance_focus="VAT filing evidence, adjustment approval, and audit trail",
        deadline="6 weeks",
        assumptions=["VAT registrations and tax codes are in scope for the pilot entity only."],
    ),
}


def validate_intake(intake: IntakeAnswers) -> None:
    missing_fields = []
    for field_name, value in intake.__dict__.items():
        if field_name == "assumptions":
            continue
        if isinstance(value, str) and not value.strip():
            missing_fields.append(field_name)
        if isinstance(value, list) and not value:
            missing_fields.append(field_name)

    if missing_fields:
        raise ValueError(f"Missing required intake fields: {', '.join(missing_fields)}")
