# Accounts Payable Requirements Pack

**Prepared for:** Northstar Trading Ltd

**Purpose:** Translate finance process pain points into implementation-ready ERP requirements, controls, reporting needs, audit trail expectations, and UAT coverage.

## Executive Summary

Northstar Trading Ltd needs a structured Accounts Payable requirements pack to reduce rework, clarify control ownership, and make Odoo Finance implementation decisions testable. The pack translates duplicate invoices, manual approval chasing, and weak supplier master controls into requirements for workflow, data, controls, reporting, audit trail, and UAT. It is sized for 1,200 supplier invoices per month and frames the control design, reporting outputs, and acceptance criteria needed within a target delivery window of 10 weeks.

## Business Problem

The current Accounts Payable process relies on Email approvals, shared AP tracker, and ERP purchase ledger. That creates avoidable risk around duplicate invoices, manual approval chasing, and weak supplier master controls and leaves finance without a consistent requirements baseline for process design, configuration, controls, reporting, and UAT. The implementation needs clearer ownership, defined data fields, control evidence, and acceptance criteria before ERP optimisation or automation can be delivered with confidence.

## Process Scope

The future-state scope covers Supplier invoice intake, validation, coding, approval, payment readiness, and evidence capture; Three-way match readiness across purchase order, goods receipt, and supplier invoice data; and Segregation of duties between supplier maintenance, invoice approval, and payment release. The design will support wholesale trading group users on Odoo Finance, with emphasis on internal audit review of supplier changes and payment controls.

## In Scope

- Accounts Payable requirements for the agreed wholesale trading group process.
- Workflow, data, controls, reporting, audit trail, and UAT requirements for Odoo Finance.
- Process pain points covering duplicate invoices, manual approval chasing, and weak supplier master controls.
- Reporting requirement: Aged approval backlog, blocked invoices, and payment readiness summary.
- Implementation window and readiness assumptions for the 10 weeks target window.

## Out of Scope

- Live system configuration, data migration execution, and production cutover.
- Custom integration build or external workflow automation.
- Legal, tax, HR, or statutory sign-off outside the finance process owner remit.
- Direct processing of operational production data.
- Process areas outside Accounts Payable unless approved as a separate phase.

## Stakeholders and Roles

- Finance Transformation Lead: accountable for business sign-off and prioritisation.
- Accounts Payable process owner: validates workflow scope, controls, and exceptions.
- Finance systems analyst: translates requirements into configuration and UAT coverage.
- Preparer or operational user: confirms day-to-day inputs, handoffs, and evidence needs.
- Reviewer or controller: approves control design, reporting outputs, and acceptance criteria.

## Functional Requirements

- FR-01: Capture supplier invoice number, supplier name, invoice date, due date, tax amount, purchase order reference, and payment status.
- FR-02: Detect potential duplicate invoices using supplier, invoice number, invoice date, currency, and gross amount.
- FR-03: Flag invoices without purchase order or goods receipt evidence where three-way match is required.
- FR-04: Route invoices to the correct approver based on cost centre, amount threshold, and supplier category.
- FR-05: Prevent payment release until invoice approval controls are complete.
- FR-06: Maintain supplier master data change history for bank details, tax identifiers, and payment terms.
- FR-07: Record exception reasons for blocked, disputed, or partially matched invoices.
- FR-08: Provide an aged invoice and approval backlog view for finance review.

## Data Requirements

- DR-01: Supplier master ID
- DR-02: Supplier invoice number
- DR-03: Purchase order reference
- DR-04: Goods receipt reference
- DR-05: Invoice gross amount
- DR-06: Tax amount
- DR-07: Approval owner
- DR-08: Payment batch reference

## Controls

- CTRL-01: Duplicate invoice warning before approval or payment release.
- CTRL-02: Approval threshold control by amount and cost centre.
- CTRL-03: Supplier bank detail change review before first payment after change.
- CTRL-04: Three-way match exception review for PO-backed purchases.
- CTRL-05: Segregation of duties control between supplier maintenance and payment approval.

## Reporting Requirements

- RPT-01: Provide Aged approval backlog, blocked invoices, and payment readiness summary.
- RPT-02: Show owner, status, ageing, exception reason, and next action where relevant to Accounts Payable.
- RPT-03: Support finance manager review with exportable period-end evidence.
- RPT-04: Separate open exceptions from completed, approved, or signed-off items.
- RPT-05: Make reporting outputs readable by finance users without system administrator access.

## Audit Trail Requirements

- AUD-01: Store invoice creation, coding, approval, rejection, and payment readiness timestamps.
- AUD-02: Record every approval decision with approver, date, amount, and delegation status.
- AUD-03: Keep before-and-after supplier master data values for sensitive changes.
- AUD-04: Preserve evidence links for invoice image, purchase order, goods receipt, and payment batch.
- AUD-05: Track exception resolution notes and reviewer sign-off.

## User Stories

- As an AP clerk, I want duplicate invoice warnings so that I can stop duplicate payments before approval.
- As a finance manager, I want approval ageing by owner so that overdue invoices can be escalated.
- As an AP controller, I want three-way match exceptions grouped by reason so that supplier disputes can be resolved.
- As an internal auditor, I want supplier bank detail change history so that payment fraud risk can be reviewed.
- As a payment approver, I want evidence that invoice approval controls are complete before release.

## UAT Test Cases

- **UAT-01:** Duplicate invoice number is entered for the same supplier and gross amount. Expected result: The system flags the invoice and blocks payment readiness until reviewed.
- **UAT-02:** PO-backed invoice is missing goods receipt evidence. Expected result: The invoice appears in the three-way match exception queue.
- **UAT-03:** Invoice value exceeds the standard approval threshold. Expected result: Approval routes to the higher authority approver.
- **UAT-04:** Supplier bank details are changed before a payment run. Expected result: The payment is held until supplier master review is complete.
- **UAT-05:** Invoice is rejected by the approver. Expected result: The rejection reason and timestamp are stored in the audit trail.
- **UAT-06:** AP manager opens the month-end backlog report. Expected result: The report shows aged invoices, blocked invoices, and approval owner status.

## Acceptance Criteria

- Duplicate invoice/payment approval controls are configured and visible in test evidence.
- At least 95% of supplier invoices contain required supplier, invoice, tax, approval, and payment fields.
- Three-way match exceptions can be exported with owner, reason, and ageing.
- Supplier master changes show old value, new value, requester, reviewer, and timestamp.
- Payment readiness cannot be reached without required approval evidence.

## Implementation Risks and Dependencies

- Supplier master data may require cleansing before controls can operate reliably.
- Purchase order and goods receipt data must be available for three-way match readiness.
- Delegated approval rules must be signed off by finance leadership.
- Payment platform integration scope must be confirmed before build.
- Users need training on exception reason codes to avoid inconsistent reporting.

## Implementation Notes

- Confirm Accounts Payable process owner and reviewer roles before design sign-off.
- Validate the required data fields against Odoo Finance configuration.
- Run UAT with approved sample scenarios before production data migration or cutover.
- Keep any future AI-assisted drafting behind structured templates and human approval.

## Public-Safe Sample Data Note

This pack was generated from fictional, public-safe sample inputs. It does not contain real employer, client, supplier, bank, VAT, payroll, or operational data. Do not upload confidential business information into a public demo.
