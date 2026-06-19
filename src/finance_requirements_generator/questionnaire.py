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
    "accounts_receivable": IntakeAnswers(
        process_key="accounts_receivable",
        company_name="Harbour Lane Services Ltd",
        entity_type="Professional services group",
        current_tools=(
            "ERP sales ledger, customer remittance mailbox, and offline collections tracker"
        ),
        erp_platform="NetSuite",
        monthly_volume="900 customer invoices and 700 receipts per month",
        pain_points=[
            "Unallocated customer receipts",
            "Disputed invoices",
            "Collections ageing visibility",
        ],
        control_concerns=[
            "Credit notes require approval based on amount, reason code, and customer risk."
        ],
        reporting_needs=(
            "Customer ageing, dispute status, unallocated cash, and collections owner summary"
        ),
        compliance_focus=(
            "Credit note approval, write-off evidence, and customer master data controls"
        ),
        deadline="9 weeks",
        assumptions=["Customer account IDs are unique across the sales ledger."],
    ),
    "month_end_close": IntakeAnswers(
        process_key="month_end_close",
        company_name="Cedar Grove Retail Ltd",
        entity_type="Multi-entity retail group",
        current_tools="Close checklist spreadsheet, ERP journals, and shared evidence folders",
        erp_platform="Microsoft Dynamics 365 Finance",
        monthly_volume="125 close tasks, 70 reconciliations, and 220 journals per period",
        pain_points=[
            "Late close tasks",
            "Manual close status tracking",
            "Missing reconciliation evidence",
        ],
        control_concerns=[
            "Reviewer sign-off required before high-risk reconciliations are marked complete."
        ],
        reporting_needs=(
            "Close task status, overdue items, reconciliation risk, and journal approval dashboard"
        ),
        compliance_focus=(
            "Close evidence, journal approvals, reviewer sign-off, and period completion controls"
        ),
        deadline="12 weeks",
        assumptions=[
            "Close task owners and reviewer roles have been agreed by finance leadership."
        ],
    ),
    "inventory_costing": IntakeAnswers(
        process_key="inventory_costing",
        company_name="MapleWorks Components Ltd",
        entity_type="Light manufacturing business",
        current_tools="ERP inventory module, warehouse adjustment logs, and costing spreadsheets",
        erp_platform="SAP Business One",
        monthly_volume="4 warehouses, 2,800 SKUs, and monthly standard cost review",
        pain_points=[
            "Inventory valuation differences",
            "Cost variance review gaps",
            "Manual landed cost allocation",
        ],
        control_concerns=["Standard cost changes require approval before effective date."],
        reporting_needs=(
            "Inventory valuation, cost variance, landed cost, and subledger-to-GL summary"
        ),
        compliance_focus=(
            "Cost change approvals, stock adjustment controls, and valuation audit evidence"
        ),
        deadline="11 weeks",
        assumptions=["Item master data includes active SKU and warehouse identifiers."],
    ),
    "intercompany_settlements": IntakeAnswers(
        process_key="intercompany_settlements",
        company_name="Summit Group Holdings Ltd",
        entity_type="Multi-entity group with shared service recharges",
        current_tools="Entity ERP ledgers, recharge spreadsheets, and group consolidation workbook",
        erp_platform="Oracle NetSuite OneWorld",
        monthly_volume="14 entities, 320 intercompany lines, and 5 settlement currencies per month",
        pain_points=[
            "Intercompany mismatch ageing",
            "Recharge rule ambiguity",
            "FX difference review gaps",
        ],
        control_concerns=["Counterparty confirmation is required before settlement readiness."],
        reporting_needs=(
            "Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary"
        ),
        compliance_focus=(
            "Counterparty confirmation, recharge approval, settlement evidence, and "
            "elimination support"
        ),
        deadline="10 weeks",
        assumptions=["Entity codes and counterparty mappings are available for the pilot group."],
    ),
    "payroll_controls": IntakeAnswers(
        process_key="payroll_controls",
        company_name="Riverstone Care Ltd",
        entity_type="Multi-site care services provider",
        current_tools=(
            "Payroll bureau portal, HR change forms, GL payroll journals, and bank "
            "approval workflow"
        ),
        erp_platform="Sage Payroll and Xero Finance",
        monthly_volume="650 employees and monthly payroll control review",
        pain_points=[
            "Starter and leaver control gaps",
            "Payroll change approval delays",
            "Manual payroll input checks",
        ],
        control_concerns=[
            "Starter, leaver, salary, deduction, and bank detail changes require "
            "approval before payroll processing."
        ],
        reporting_needs=(
            "Payroll changes, exceptions, register-to-GL reconciliation, and "
            "payment approval summary"
        ),
        compliance_focus=(
            "Payroll master data approval, exception review, payment file approval, "
            "and reconciliation"
        ),
        deadline="9 weeks",
        assumptions=["Public sample packs use fictional employee identifiers only."],
    ),
}


def validate_intake(intake: IntakeAnswers) -> None:
    missing_fields = []
    optional_fields = {"assumptions", "target_system", "current_state_sop_draft"}
    for field_name, value in intake.__dict__.items():
        if field_name in optional_fields:
            continue
        if isinstance(value, str) and not value.strip():
            missing_fields.append(field_name)
        if isinstance(value, list) and not value:
            missing_fields.append(field_name)

    if missing_fields:
        raise ValueError(f"Missing required intake fields: {', '.join(missing_fields)}")
