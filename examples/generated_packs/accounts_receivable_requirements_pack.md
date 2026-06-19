# Accounts Receivable Requirements Pack

**Synthetic company:** Harbour Lane Services Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Harbour Lane Services Ltd needs a structured Accounts Receivable requirements pack for NetSuite. The MVP scope turns current finance pain points (Unallocated customer receipts, Disputed invoices, and Collections ageing visibility) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 900 customer invoices and 700 receipts per month and prioritises Credit notes require approval based on amount, reason code, and customer risk. within a target delivery window of 9 weeks.

## Current-State Problem Statement

The current accounts receivable process relies on ERP sales ledger, customer remittance mailbox, and offline collections tracker. This creates avoidable risk around Unallocated customer receipts, Disputed invoices, and Collections ageing visibility and makes customer ageing, dispute status, unallocated cash, and collections owner summary harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Customer invoice generation, receipt matching, dispute tracking, collections ownership, and credit note approval. Clear customer account ageing with owner, status, and next action evidence. Controls over customer master data, credit limits, write-offs, and cash allocation. It will support professional services group users on NetSuite, with emphasis on credit note approval, write-off evidence, and customer master data controls.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Customer account IDs are unique across the sales ledger.

## Functional Requirements

- FR-01: Capture customer invoice number, customer account, invoice date, due date, currency, tax amount, and payment status.
- FR-02: Match customer receipts to open invoices using customer reference, amount, remittance advice, and bank receipt date.
- FR-03: Track unallocated cash with owner, ageing, reason code, and expected resolution action.
- FR-04: Record invoice disputes with dispute type, owner, status, value, and target resolution date.
- FR-05: Route credit notes and write-offs through approval thresholds before posting.
- FR-06: Maintain customer master data changes for payment terms, credit limits, billing contacts, and tax identifiers.
- FR-07: Produce collections ageing views by customer, region, owner, and risk category.
- FR-08: Link dunning activity, customer responses, and promise-to-pay dates to the customer account.
- FR-09: Provide reporting for Customer ageing, dispute status, unallocated cash, and collections owner summary.
- FR-10: Evidence Credit note approval, write-off evidence, and customer master data controls for finance review.

## Non-Functional Requirements

- NFR-01: Collections status must be understandable to finance, sales, and credit control users.
- NFR-02: The workflow must support daily cash allocation and formal month-end AR review.
- NFR-03: Exported evidence must be readable by auditors without system administrator access.
- NFR-04: Access must separate customer master maintenance, invoice posting, credit note approval, and write-off approval.
- NFR-05: AR reporting must avoid manual spreadsheet consolidation for core ageing and dispute views.
- NFR-06: Provide reporting for Customer ageing, dispute status, unallocated cash, and collections owner summary.
- NFR-07: Evidence Credit note approval, write-off evidence, and customer master data controls for finance review.

## Data Requirements

- DR-01: Customer account ID
- DR-02: Customer invoice number
- DR-03: Receipt reference
- DR-04: Remittance advice reference
- DR-05: Dispute status
- DR-06: Collections owner
- DR-07: Credit limit
- DR-08: Write-off approval reference
- DR-09: Provide reporting for Customer ageing, dispute status, unallocated cash, and collections owner summary.
- DR-10: Evidence Credit note approval, write-off evidence, and customer master data controls for finance review.

## Controls

- CTRL-01: Credit notes require approval based on amount, reason code, and customer risk.
- CTRL-02: Customer credit limit changes require finance owner review.
- CTRL-03: Unallocated cash over the policy threshold escalates to the collections lead.
- CTRL-04: Write-offs require supporting evidence and approval before posting.
- CTRL-05: Receipts cannot be marked resolved without allocation or approved reason code.
- CTRL-06: Provide reporting for Customer ageing, dispute status, unallocated cash, and collections owner summary.
- CTRL-07: Evidence Credit note approval, write-off evidence, and customer master data controls for finance review.

## Audit Trail Requirements

- AUD-01: Store invoice posting, receipt matching, dispute creation, credit note approval, and write-off timestamps.
- AUD-02: Record customer master data changes with old value, new value, requester, reviewer, and date.
- AUD-03: Preserve collections notes, dunning actions, and promise-to-pay updates.
- AUD-04: Track unallocated cash owner/status history.
- AUD-05: Keep approval evidence for credit notes, write-offs, and credit limit changes.
- AUD-06: Provide reporting for Customer ageing, dispute status, unallocated cash, and collections owner summary.
- AUD-07: Evidence Credit note approval, write-off evidence, and customer master data controls for finance review.

## User Stories

- As a cash allocator, I want remittance-backed receipt matching so that unallocated cash is reduced quickly.
- As a collections analyst, I want aged disputed invoices by owner so that customer follow-up is prioritised.
- As a credit controller, I want customer credit limit changes reviewed so that exposure is controlled.
- As a finance manager, I want credit note approval evidence so that revenue adjustments are defensible.
- As an auditor, I want write-off approvals and customer master changes traceable by user and date.

## UAT Test Cases

- **UAT-01:** Customer receipt arrives without a matching invoice reference. Expected result: The receipt is marked unallocated with owner, ageing, and reason fields required.
- **UAT-02:** Invoice is placed into dispute by the collections team. Expected result: Dispute type, owner, value, status, and target resolution date are stored.
- **UAT-03:** Credit note exceeds the standard threshold. Expected result: Posting is blocked until the correct approval is captured.
- **UAT-04:** Customer credit limit is increased. Expected result: Old value, new value, requester, reviewer, and approval timestamp are retained.
- **UAT-05:** A write-off is requested for an aged balance. Expected result: Supporting evidence and approval are required before write-off posting.
- **UAT-06:** Collections ageing report is exported. Expected result: Report shows customer, invoice, ageing bucket, owner, dispute status, and next action.

## Acceptance Criteria

- Unallocated receipts show owner, ageing, reason code, and expected resolution action.
- Disputed invoices are visible in AR ageing and cannot be hidden from collections reporting.
- Credit notes and write-offs require approval evidence before posting.
- Customer master changes for credit limits and payment terms are auditable.
- Collections reporting shows ageing, risk, owner, and next action without manual rework.

## Implementation Risks and Dependencies

- Customer remittance reference quality may limit automated matching rates.
- Historic unallocated cash may need cleanup before go-live.
- Credit policy thresholds must be approved by finance leadership.
- Sales and finance ownership of disputes must be agreed before workflow design.
- Customer master data may need cleansing before credit controls are reliable.

## Implementation Notes

- Confirm Accounts Receivable process owner and reviewer roles before design sign-off.
- Validate the required data fields against NetSuite configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
