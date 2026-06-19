# Payroll Controls Requirements Pack

**Synthetic company:** Riverstone Care Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Riverstone Care Ltd needs a structured Payroll Controls requirements pack for Sage Payroll and Xero Finance. The MVP scope turns current finance pain points (Starter and leaver control gaps, Payroll change approval delays, and Manual payroll input checks) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 650 employees and monthly payroll control review and prioritises Starter, leaver, salary, deduction, and bank detail changes require approval before payroll processing. within a target delivery window of 9 weeks.

## Current-State Problem Statement

The current payroll controls process relies on Payroll bureau portal, HR change forms, GL payroll journals, and bank approval workflow. This creates avoidable risk around Starter and leaver control gaps, Payroll change approval delays, and Manual payroll input checks and makes payroll changes, exceptions, register-to-gl reconciliation, and payment approval summary harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Payroll master changes, input approval, exception review, payroll reconciliation, payment approval, and evidence retention. Controls over starters, leavers, salary changes, bank detail changes, overtime, deductions, and payroll payment files. Period-end payroll sign-off evidence for finance, HR, and audit review. It will support multi-site care services provider users on Sage Payroll and Xero Finance, with emphasis on payroll master data approval, exception review, payment file approval, and reconciliation.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Public sample packs use fictional employee identifiers only.

## Functional Requirements

- FR-01: Capture employee ID, payroll period, change type, effective date, requester, approver, and payroll status.
- FR-02: Route starters, leavers, salary changes, bank detail changes, and deductions for approval before payroll processing.
- FR-03: Track payroll input files with preparer, reviewer, version, cutoff date, and approval status.
- FR-04: Identify payroll exceptions for duplicate employees, negative pay, unusual overtime, net pay variance, and missing approvals.
- FR-05: Reconcile payroll register totals to GL payroll control accounts and payment file totals.
- FR-06: Require payroll payment file approval before release to bank.
- FR-07: Store leaver final pay checks, access removal confirmation, and termination effective date evidence.
- FR-08: Produce payroll control pack with changes, exceptions, reconciliation, payment approval, and sign-off details.
- FR-09: Provide reporting for Payroll changes, exceptions, register-to-GL reconciliation, and payment approval summary.
- FR-10: Evidence Payroll master data approval, exception review, payment file approval, and reconciliation for finance review.

## Non-Functional Requirements

- NFR-01: Payroll control reporting must be clear to finance, HR, payroll, and audit reviewers.
- NFR-02: Sensitive payroll evidence must be access-controlled by role.
- NFR-03: The workflow must support payroll period cutoff discipline and controlled late changes.
- NFR-04: Audit evidence must preserve approvals without exposing unnecessary personal data in public examples.
- NFR-05: Reconciliation reporting must avoid manual spreadsheet rebuilds for core control totals.
- NFR-06: Provide reporting for Payroll changes, exceptions, register-to-GL reconciliation, and payment approval summary.
- NFR-07: Evidence Payroll master data approval, exception review, payment file approval, and reconciliation for finance review.

## Data Requirements

- DR-01: Employee ID
- DR-02: Payroll period
- DR-03: Payroll change type
- DR-04: Effective date
- DR-05: Approval reference
- DR-06: Gross-to-net total
- DR-07: Payroll control account
- DR-08: Payment file reference
- DR-09: Provide reporting for Payroll changes, exceptions, register-to-GL reconciliation, and payment approval summary.
- DR-10: Evidence Payroll master data approval, exception review, payment file approval, and reconciliation for finance review.

## Controls

- CTRL-01: Starter, leaver, salary, deduction, and bank detail changes require approval before payroll processing.
- CTRL-02: Payroll input files require preparer and reviewer sign-off before calculation.
- CTRL-03: Payroll exceptions over threshold require investigation and approval.
- CTRL-04: Payroll register must reconcile to GL control accounts and payment file totals.
- CTRL-05: Payroll payment file release requires finance approval.
- CTRL-06: Provide reporting for Payroll changes, exceptions, register-to-GL reconciliation, and payment approval summary.
- CTRL-07: Evidence Payroll master data approval, exception review, payment file approval, and reconciliation for finance review.

## Audit Trail Requirements

- AUD-01: Store payroll master change request, approval, processing, and effective date history.
- AUD-02: Record payroll input file version, preparer, reviewer, approval, and cutoff timestamp.
- AUD-03: Preserve exception review notes and approval decisions.
- AUD-04: Track payroll reconciliation owner/status history by period.
- AUD-05: Keep payment file approval evidence with approver, date, amount, and bank file reference.
- AUD-06: Provide reporting for Payroll changes, exceptions, register-to-GL reconciliation, and payment approval summary.
- AUD-07: Evidence Payroll master data approval, exception review, payment file approval, and reconciliation for finance review.

## User Stories

- As a payroll manager, I want approved starter and leaver changes so that payroll master data is controlled.
- As a finance reviewer, I want payroll register-to-GL reconciliation so that payroll costs are supported.
- As a payroll preparer, I want exception checks before payment so that unusual items are investigated.
- As an approver, I want payment file evidence so that bank release is controlled.
- As an auditor, I want payroll change approval history so that sensitive changes are traceable.

## UAT Test Cases

- **UAT-01:** Salary change is entered after payroll cutoff. Expected result: The change requires late-change approval before processing.
- **UAT-02:** Employee bank details are changed before payroll run. Expected result: Payroll processing is blocked until approval evidence is captured.
- **UAT-03:** Payroll register does not reconcile to the GL control account. Expected result: A reconciliation difference is created with owner, amount, and reason fields.
- **UAT-04:** Net pay variance exceeds exception threshold. Expected result: The exception appears in the payroll review queue and requires approval.
- **UAT-05:** Payment file is prepared for release. Expected result: Finance approval is required before payment file status becomes released.
- **UAT-06:** Payroll control pack is exported. Expected result: The pack includes changes, exceptions, reconciliation, payment approval, and sign-off evidence.

## Acceptance Criteria

- Payroll master changes require approval and retain requester, approver, and effective date.
- Payroll exceptions are visible with owner, status, reason, and approval evidence.
- Payroll register reconciles to GL control accounts and payment file totals.
- Payment file release cannot occur without finance approval.
- Payroll control pack exports with change, exception, reconciliation, and sign-off evidence.

## Implementation Risks and Dependencies

- HR and payroll ownership of master data changes must be agreed.
- Payroll cutoff rules and approval thresholds require policy sign-off.
- Sensitive payroll access roles must be configured carefully.
- GL account mapping must be validated before reconciliation testing.
- Historic payroll exception categories may need standardisation before rollout.

## Implementation Notes

- Confirm Payroll Controls process owner and reviewer roles before design sign-off.
- Validate the required data fields against Sage Payroll and Xero Finance configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
