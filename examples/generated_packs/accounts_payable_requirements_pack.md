# Accounts Payable Requirements Pack

**Synthetic company:** Northstar Trading Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Northstar Trading Ltd needs a structured Accounts Payable requirements pack for Odoo Finance. The MVP scope turns current finance pain points (Duplicate invoices, Manual approval chasing, and Weak supplier master controls) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 1,200 supplier invoices per month and prioritises Payment approval evidence, and Segregation of duties within a target delivery window of 10 weeks.

## Current-State Problem Statement

The current accounts payable process relies on Email approvals, shared AP tracker, and ERP purchase ledger. This creates avoidable risk around Duplicate invoices, Manual approval chasing, and Weak supplier master controls and makes aged approval backlog, blocked invoices, and payment readiness summary harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Supplier invoice intake, validation, coding, approval, payment readiness, and evidence capture. Three-way match readiness across purchase order, goods receipt, and supplier invoice data. Segregation of duties between supplier maintenance, invoice approval, and payment release. It will support wholesale trading group users on Odoo Finance, with emphasis on internal audit review of supplier changes and payment controls.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Supplier records are already uniquely identified in the ERP.

## Functional Requirements

- FR-01: Capture supplier invoice number, supplier name, invoice date, due date, tax amount, purchase order reference, and payment status.
- FR-02: Detect potential duplicate invoices using supplier, invoice number, invoice date, currency, and gross amount.
- FR-03: Flag invoices without purchase order or goods receipt evidence where three-way match is required.
- FR-04: Route invoices to the correct approver based on cost centre, amount threshold, and supplier category.
- FR-05: Prevent payment release until invoice approval controls are complete.
- FR-06: Maintain supplier master data change history for bank details, tax identifiers, and payment terms.
- FR-07: Record exception reasons for blocked, disputed, or partially matched invoices.
- FR-08: Provide an aged invoice and approval backlog view for finance review.
- FR-09: Provide reporting for Aged approval backlog, blocked invoices, and payment readiness summary.
- FR-10: Evidence Internal audit review of supplier changes and payment controls for finance review.

## Non-Functional Requirements

- NFR-01: The workflow must be auditable by finance users without database access.
- NFR-02: Screen labels and exports must use finance-friendly terminology.
- NFR-03: The solution must support month-end reporting without manual spreadsheet consolidation.
- NFR-04: Access must separate invoice preparation, approval, supplier maintenance, and payment release duties.
- NFR-05: Exported evidence should be readable by internal audit and external audit reviewers.
- NFR-06: Provide reporting for Aged approval backlog, blocked invoices, and payment readiness summary.
- NFR-07: Evidence Internal audit review of supplier changes and payment controls for finance review.

## Data Requirements

- DR-01: Supplier master ID
- DR-02: Supplier invoice number
- DR-03: Purchase order reference
- DR-04: Goods receipt reference
- DR-05: Invoice gross amount
- DR-06: Tax amount
- DR-07: Approval owner
- DR-08: Payment batch reference
- DR-09: Provide reporting for Aged approval backlog, blocked invoices, and payment readiness summary.
- DR-10: Evidence Internal audit review of supplier changes and payment controls for finance review.

## Controls

- CTRL-01: Duplicate invoice warning before approval or payment release.
- CTRL-02: Approval threshold control by amount and cost centre.
- CTRL-03: Supplier bank detail change review before first payment after change.
- CTRL-04: Three-way match exception review for PO-backed purchases.
- CTRL-05: Segregation of duties control between supplier maintenance and payment approval.
- CTRL-06: Provide reporting for Aged approval backlog, blocked invoices, and payment readiness summary.
- CTRL-07: Evidence Internal audit review of supplier changes and payment controls for finance review.

## Audit Trail Requirements

- AUD-01: Store invoice creation, coding, approval, rejection, and payment readiness timestamps.
- AUD-02: Record every approval decision with approver, date, amount, and delegation status.
- AUD-03: Keep before-and-after supplier master data values for sensitive changes.
- AUD-04: Preserve evidence links for invoice image, purchase order, goods receipt, and payment batch.
- AUD-05: Track exception resolution notes and reviewer sign-off.
- AUD-06: Provide reporting for Aged approval backlog, blocked invoices, and payment readiness summary.
- AUD-07: Evidence Internal audit review of supplier changes and payment controls for finance review.

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
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
