# Bank Reconciliation Requirements Pack

**Synthetic company:** BlueRiver Foods Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

BlueRiver Foods Ltd needs a structured Bank Reconciliation requirements pack for Microsoft Dynamics 365 Business Central. The MVP scope turns current finance pain points (Unmatched bank statement lines, Suspense account ageing, and Manual owner/status tracking) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 8 bank accounts with roughly 4,500 statement lines per month and prioritises Reviewer sign-off, and Manual match overrides within a target delivery window of 8 weeks.

## Current-State Problem Statement

The current bank reconciliation process relies on Bank portal exports, ERP cashbook, and month-end spreadsheet reconciliation. This creates avoidable risk around Unmatched bank statement lines, Suspense account ageing, and Manual owner/status tracking and makes daily unmatched item ageing and month-end reconciliation evidence pack harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Bank statement ingestion, matching status, exception ownership, suspense clearing, and reviewer sign-off. Daily visibility of unmatched receipts, payments, fees, and transfers. Month-end reconciliation evidence suitable for finance and audit review. It will support multi-site food distribution business users on Microsoft Dynamics 365 Business Central, with emphasis on month-end close evidence and internal control review.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Bank statement files use a consistent export format.

## Functional Requirements

- FR-01: Import or capture bank statement date, value date, description, amount, currency, and bank account.
- FR-02: Match bank lines to ledger transactions using reference, amount, date tolerance, and counterparty.
- FR-03: Track unmatched lines with owner, status, reason code, ageing, and expected resolution date.
- FR-04: Separate unreconciled receipts, unreconciled payments, bank fees, transfers, and unknown items.
- FR-05: Link suspense account entries to the originating bank line and clearing journal.
- FR-06: Require reviewer sign-off once reconciliation differences are explained or cleared.
- FR-07: Produce a month-end reconciliation pack with outstanding items and movement commentary.
- FR-08: Escalate high-value or aged unmatched lines based on finance policy thresholds.
- FR-09: Provide reporting for Daily unmatched item ageing and month-end reconciliation evidence pack.
- FR-10: Evidence Month-end close evidence and internal control review for finance review.

## Non-Functional Requirements

- NFR-01: Matching status must be clear to preparers, reviewers, and auditors.
- NFR-02: The reconciliation evidence must be exportable without manual spreadsheet formatting.
- NFR-03: The workflow must support daily review and formal month-end sign-off.
- NFR-04: The system must retain historic reconciliation packs for audit lookback.
- NFR-05: User permissions must distinguish preparer updates from reviewer approval.
- NFR-06: Provide reporting for Daily unmatched item ageing and month-end reconciliation evidence pack.
- NFR-07: Evidence Month-end close evidence and internal control review for finance review.

## Data Requirements

- DR-01: Bank account ID
- DR-02: Statement line ID
- DR-03: Ledger transaction ID
- DR-04: Match status
- DR-05: Exception owner
- DR-06: Ageing bucket
- DR-07: Suspense account reference
- DR-08: Reviewer sign-off timestamp
- DR-09: Provide reporting for Daily unmatched item ageing and month-end reconciliation evidence pack.
- DR-10: Evidence Month-end close evidence and internal control review for finance review.

## Controls

- CTRL-01: Reviewer sign-off required before a reconciliation period is marked complete.
- CTRL-02: Aged unmatched lines escalate after the policy threshold.
- CTRL-03: Suspense clearing entries require reason codes and supporting notes.
- CTRL-04: Manual match overrides require reviewer approval.
- CTRL-05: Reconciliation status is locked after period close except through controlled reopen.
- CTRL-06: Provide reporting for Daily unmatched item ageing and month-end reconciliation evidence pack.
- CTRL-07: Evidence Month-end close evidence and internal control review for finance review.

## Audit Trail Requirements

- AUD-01: Store all matching, unmatching, manual override, and suspense clearing actions.
- AUD-02: Record preparer completion and reviewer sign-off timestamps.
- AUD-03: Keep owner/status history for aged unmatched lines.
- AUD-04: Preserve supporting notes and evidence links for unresolved differences.
- AUD-05: Record period reopen requests with reason, requester, approver, and date.
- AUD-06: Provide reporting for Daily unmatched item ageing and month-end reconciliation evidence pack.
- AUD-07: Evidence Month-end close evidence and internal control review for finance review.

## User Stories

- As a reconciliation preparer, I want unmatched lines grouped by ageing so that old differences are prioritised.
- As a finance manager, I want suspense clearing status so that unresolved items do not hide at month end.
- As a reviewer, I want clear sign-off evidence so that reconciliation completion is defensible.
- As an auditor, I want manual match override history so that judgemental matches can be reviewed.
- As a treasury analyst, I want bank fees and transfers separated so that routine items are cleared quickly.

## UAT Test Cases

- **UAT-01:** A bank statement line has no ledger match after import. Expected result: The line is marked unmatched with owner, ageing, and reason fields required.
- **UAT-02:** A suspense item remains open past the policy threshold. Expected result: The item is escalated and appears in the aged suspense view.
- **UAT-03:** A preparer manually matches two transactions. Expected result: The manual override is logged and requires reviewer approval.
- **UAT-04:** Reviewer signs off a completed reconciliation. Expected result: Reviewer name, timestamp, and outstanding item summary are saved.
- **UAT-05:** A closed reconciliation period is reopened. Expected result: Reopen reason and approver are recorded before edits are allowed.
- **UAT-06:** Month-end pack is exported. Expected result: The pack includes unmatched lines, ageing, suspense movements, and reviewer sign-off.

## Acceptance Criteria

- Unmatched lines show owner, status, ageing, reason, and expected resolution date.
- Suspense account items can be traced from bank line to clearing journal.
- Reviewer sign-off is mandatory before period completion.
- Manual overrides are visible in the audit trail.
- Month-end reconciliation pack exports without manual formatting.

## Implementation Risks and Dependencies

- Bank statement formats must be standardised across accounts.
- Ledger reference quality may limit automated matching rates.
- Finance policy thresholds for ageing and escalation must be approved.
- Reviewer roles must be configured before go-live.
- Historic suspense items may need cleanup before migration.

## Implementation Notes

- Confirm Bank Reconciliation process owner and reviewer roles before design sign-off.
- Validate the required data fields against Microsoft Dynamics 365 Business Central configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
