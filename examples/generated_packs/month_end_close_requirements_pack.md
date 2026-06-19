# Month-end Close Requirements Pack

**Synthetic company:** Cedar Grove Retail Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Cedar Grove Retail Ltd needs a structured Month-end Close requirements pack for Microsoft Dynamics 365 Finance. The MVP scope turns current finance pain points (Late close tasks, Manual close status tracking, and Missing reconciliation evidence) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 125 close tasks, 70 reconciliations, and 220 journals per period and prioritises Reviewer sign-off required before high-risk reconciliations are marked complete. within a target delivery window of 12 weeks.

## Current-State Problem Statement

The current month-end close process relies on Close checklist spreadsheet, ERP journals, and shared evidence folders. This creates avoidable risk around Late close tasks, Manual close status tracking, and Missing reconciliation evidence and makes close task status, overdue items, reconciliation risk, and journal approval dashboard harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Close task calendar, preparer/reviewer ownership, journal approval, reconciliation completion, and close reporting. Daily close status visibility with overdue task escalation and dependency tracking. Evidence pack for finance leadership, internal controls, and audit review. It will support multi-entity retail group users on Microsoft Dynamics 365 Finance, with emphasis on close evidence, journal approvals, reviewer sign-off, and period completion controls.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Close task owners and reviewer roles have been agreed by finance leadership.

## Functional Requirements

- FR-01: Maintain a close calendar with task owner, reviewer, due date, dependency, status, and completion evidence.
- FR-02: Track balance sheet reconciliations by account, preparer, reviewer, risk rating, and sign-off status.
- FR-03: Route manual journals for approval based on journal type, value, and account risk.
- FR-04: Escalate overdue tasks to close lead and finance controller based on policy thresholds.
- FR-05: Capture close commentary for material movements, open items, and unresolved exceptions.
- FR-06: Lock completed tasks after reviewer sign-off unless reopened through controlled approval.
- FR-07: Produce a close dashboard showing task completion, late items, high-risk reconciliations, and journal status.
- FR-08: Export a month-end close evidence pack with task, reconciliation, journal, and sign-off details.
- FR-09: Provide reporting for Close task status, overdue items, reconciliation risk, and journal approval dashboard.
- FR-10: Evidence Close evidence, journal approvals, reviewer sign-off, and period completion controls for finance review.

## Non-Functional Requirements

- NFR-01: Close status must be visible without relying on offline spreadsheet trackers.
- NFR-02: Task and reconciliation evidence must be understandable to finance managers and auditors.
- NFR-03: The workflow must support daily close stand-up review and formal period completion.
- NFR-04: Access must separate preparer completion, reviewer approval, and close administrator changes.
- NFR-05: Close reporting must preserve historic period evidence for audit lookback.
- NFR-06: Provide reporting for Close task status, overdue items, reconciliation risk, and journal approval dashboard.
- NFR-07: Evidence Close evidence, journal approvals, reviewer sign-off, and period completion controls for finance review.

## Data Requirements

- DR-01: Close period
- DR-02: Close task ID
- DR-03: Task owner
- DR-04: Reviewer
- DR-05: Balance sheet account
- DR-06: Journal batch reference
- DR-07: Completion evidence link
- DR-08: Sign-off timestamp
- DR-09: Provide reporting for Close task status, overdue items, reconciliation risk, and journal approval dashboard.
- DR-10: Evidence Close evidence, journal approvals, reviewer sign-off, and period completion controls for finance review.

## Controls

- CTRL-01: Reviewer sign-off required before high-risk reconciliations are marked complete.
- CTRL-02: Manual journals require approval before posting to closed periods.
- CTRL-03: Overdue close tasks escalate based on close calendar thresholds.
- CTRL-04: Reopened tasks require reason, requester, approver, and timestamp.
- CTRL-05: Period close completion requires all mandatory tasks and reconciliations to be signed off.
- CTRL-06: Provide reporting for Close task status, overdue items, reconciliation risk, and journal approval dashboard.
- CTRL-07: Evidence Close evidence, journal approvals, reviewer sign-off, and period completion controls for finance review.

## Audit Trail Requirements

- AUD-01: Store task status changes, evidence uploads, preparer completion, and reviewer sign-off timestamps.
- AUD-02: Record journal submission, approval, rejection, posting, and reversal history.
- AUD-03: Preserve reopen reasons and approval decisions for closed tasks.
- AUD-04: Track reconciliation owner/status history for each close period.
- AUD-05: Keep close pack export timestamp, preparer, reviewer, and final approver evidence.
- AUD-06: Provide reporting for Close task status, overdue items, reconciliation risk, and journal approval dashboard.
- AUD-07: Evidence Close evidence, journal approvals, reviewer sign-off, and period completion controls for finance review.

## User Stories

- As a close lead, I want overdue tasks escalated so that blockers are visible before reporting deadlines.
- As a preparer, I want one place to attach reconciliation evidence so that reviewer sign-off is faster.
- As a reviewer, I want high-risk accounts highlighted so that review effort follows materiality.
- As a finance controller, I want journal approval status so that unposted adjustments do not surprise the close.
- As an auditor, I want close task and journal approval history by period so that evidence is traceable.

## UAT Test Cases

- **UAT-01:** A mandatory close task passes its due date without completion. Expected result: The task is escalated and appears in the overdue close view.
- **UAT-02:** A high-risk reconciliation is submitted without evidence. Expected result: Reviewer sign-off is blocked until evidence is attached.
- **UAT-03:** Manual journal exceeds the approval threshold. Expected result: Posting is blocked until the correct approver signs off.
- **UAT-04:** A completed close task is reopened. Expected result: Reopen reason, requester, approver, and timestamp are recorded.
- **UAT-05:** Period completion is attempted with open mandatory tasks. Expected result: Completion is blocked and open tasks are listed.
- **UAT-06:** Month-end close pack is exported. Expected result: The pack includes task completion, reconciliations, journals, overdue items, and sign-off evidence.

## Acceptance Criteria

- Close calendar shows owner, reviewer, due date, dependency, status, and evidence for each task.
- High-risk reconciliations require reviewer sign-off before period completion.
- Journal approvals are visible and traceable by journal batch.
- Overdue tasks escalate without manual tracker updates.
- Close evidence pack exports with task, reconciliation, journal, and sign-off details.

## Implementation Risks and Dependencies

- Close task ownership must be agreed across finance teams.
- Balance sheet reconciliation risk ratings may need finance controller approval.
- Journal approval thresholds must align with delegation of authority.
- Legacy spreadsheet trackers may need migration or archive decisions.
- Users need discipline to attach evidence before sign-off.

## Implementation Notes

- Confirm Month-end Close process owner and reviewer roles before design sign-off.
- Validate the required data fields against Microsoft Dynamics 365 Finance configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
