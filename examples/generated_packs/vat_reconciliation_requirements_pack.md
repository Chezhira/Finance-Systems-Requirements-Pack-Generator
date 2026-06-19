# VAT Reconciliation Requirements Pack

**Synthetic company:** Demo Manufacturing Co

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Demo Manufacturing Co needs a structured VAT Reconciliation requirements pack for SAP Business One. The MVP scope turns current finance pain points (VAT return differences, Manual source register checks, and Missing filing evidence) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for Quarterly VAT return with 15 active tax codes and prioritises VAT return box mapping, and GL VAT control account reconciliation within a target delivery window of 6 weeks.

## Current-State Problem Statement

The current vat reconciliation process relies on ERP tax reports, GL trial balance extracts, and offline VAT working papers. This creates avoidable risk around VAT return differences, Manual source register checks, and Missing filing evidence and makes vat source-to-return-to-gl reconciliation with difference owner status harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers VAT source register extraction, VAT return box mapping, GL VAT control account reconciliation, and filing evidence. Clear ownership of reconciling differences before submission. Audit trail for adjustments, review, and filing approval. It will support vat-registered manufacturing entity users on SAP Business One, with emphasis on vat filing evidence, adjustment approval, and audit trail.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- VAT registrations and tax codes are in scope for the pilot entity only.

## Functional Requirements

- FR-01: Capture VAT source register totals for sales, purchases, output tax, input tax, and adjustments.
- FR-02: Map source register totals to VAT return boxes using approved tax code rules.
- FR-03: Reconcile VAT return boxes to GL VAT control accounts for the reporting period.
- FR-04: Identify differences by tax code, transaction source, entity, and reporting period.
- FR-05: Track reconciling items with owner, status, reason, amount, and resolution action.
- FR-06: Store filing evidence including return version, approver, submission reference, and filing date.
- FR-07: Prevent submission readiness until material differences are reviewed.
- FR-08: Produce a VAT reconciliation pack for finance manager and audit review.
- FR-09: Provide reporting for VAT source-to-return-to-GL reconciliation with difference owner status.
- FR-10: Evidence VAT filing evidence, adjustment approval, and audit trail for finance review.

## Non-Functional Requirements

- NFR-01: VAT logic must be transparent to finance reviewers and not hidden in spreadsheets.
- NFR-02: The pack must preserve calculations and sign-off evidence for audit lookback.
- NFR-03: The design must support multiple VAT entities without mixing registrations.
- NFR-04: Access must separate preparer, reviewer, and filing approver duties.
- NFR-05: Exports must be clear enough for external tax advisor review.
- NFR-06: Provide reporting for VAT source-to-return-to-GL reconciliation with difference owner status.
- NFR-07: Evidence VAT filing evidence, adjustment approval, and audit trail for finance review.

## Data Requirements

- DR-01: VAT registration/entity
- DR-02: Tax code
- DR-03: Source register amount
- DR-04: VAT return box number
- DR-05: GL VAT control account
- DR-06: Reconciling difference
- DR-07: Adjustment journal reference
- DR-08: Filing submission reference
- DR-09: Provide reporting for VAT source-to-return-to-GL reconciliation with difference owner status.
- DR-10: Evidence VAT filing evidence, adjustment approval, and audit trail for finance review.

## Controls

- CTRL-01: VAT return cannot be marked ready where material differences are unresolved.
- CTRL-02: Adjustments require reason code, supporting note, and reviewer approval.
- CTRL-03: VAT return box mapping changes require finance owner sign-off.
- CTRL-04: GL VAT control account reconciliation must be completed before filing approval.
- CTRL-05: Filing evidence must include approver, date, and submission reference.
- CTRL-06: Provide reporting for VAT source-to-return-to-GL reconciliation with difference owner status.
- CTRL-07: Evidence VAT filing evidence, adjustment approval, and audit trail for finance review.

## Audit Trail Requirements

- AUD-01: Store source register extraction date, preparer, and data source.
- AUD-02: Record VAT box mapping versions and change approvals.
- AUD-03: Preserve reconciling difference owner/status history.
- AUD-04: Keep adjustment journal references and review decisions.
- AUD-05: Record filing approval and submission evidence.
- AUD-06: Provide reporting for VAT source-to-return-to-GL reconciliation with difference owner status.
- AUD-07: Evidence VAT filing evidence, adjustment approval, and audit trail for finance review.

## User Stories

- As a tax preparer, I want source registers mapped to VAT return boxes so that return totals are traceable.
- As a finance reviewer, I want GL VAT control accounts reconciled so that balance sheet VAT is explained.
- As a tax manager, I want material differences blocked before filing so that submission risk is reduced.
- As an auditor, I want VAT box mapping history so that changes to tax treatment can be reviewed.
- As a finance controller, I want filing evidence stored with the pack so that audit requests are faster.

## UAT Test Cases

- **UAT-01:** Source register total does not agree to a VAT return box. Expected result: A reconciling difference is created with owner, amount, and reason fields.
- **UAT-02:** GL VAT control account does not agree to return liability. Expected result: The variance is flagged and submission readiness is blocked if material.
- **UAT-03:** VAT return box mapping is changed. Expected result: The change is versioned and requires finance owner sign-off.
- **UAT-04:** Adjustment journal is posted after review. Expected result: Journal reference and approval evidence are stored against the difference.
- **UAT-05:** Filing approval is attempted without submission reference. Expected result: Filing evidence is incomplete and approval cannot be finalised.
- **UAT-06:** VAT reconciliation pack is exported. Expected result: The pack includes source registers, VAT return boxes, GL VAT control accounts, differences, and filing evidence.

## Acceptance Criteria

- Source registers, VAT return boxes, and GL VAT control accounts are reconciled in one pack.
- Material differences are owner-assigned and cannot be ignored before filing.
- VAT box mapping changes are versioned and approved.
- Filing evidence includes submission reference, approver, and filing date.
- Adjustments are supported by reason, journal reference, and reviewer sign-off.

## Implementation Risks and Dependencies

- Tax code mapping must be agreed before configuration.
- GL VAT control accounts may require cleanup before reliable reconciliation.
- Filing approval roles must match the finance governance model.
- External tax advisor review may be required for complex adjustments.
- Multi-entity VAT registrations need clear scope before rollout.

## Implementation Notes

- Confirm VAT Reconciliation process owner and reviewer roles before design sign-off.
- Validate the required data fields against SAP Business One configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
