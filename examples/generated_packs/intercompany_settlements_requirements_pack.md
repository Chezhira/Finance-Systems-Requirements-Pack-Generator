# Intercompany Settlements Requirements Pack

**Synthetic company:** Summit Group Holdings Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

Summit Group Holdings Ltd needs a structured Intercompany Settlements requirements pack for Oracle NetSuite OneWorld. The MVP scope turns current finance pain points (Intercompany mismatch ageing, Recharge rule ambiguity, and FX difference review gaps) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 14 entities, 320 intercompany lines, and 5 settlement currencies per month and prioritises Counterparty confirmation is required before settlement readiness. within a target delivery window of 10 weeks.

## Current-State Problem Statement

The current intercompany settlements process relies on Entity ERP ledgers, recharge spreadsheets, and group consolidation workbook. This creates avoidable risk around Intercompany mismatch ageing, Recharge rule ambiguity, and FX difference review gaps and makes entity-pair ageing, unmatched balances, recharge approvals, and fx difference summary harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Intercompany recharge creation, counterparty confirmation, matching, settlement tracking, FX difference review, and elimination support. Visibility of balances by entity, counterparty, transaction type, currency, owner, and ageing. Controls over recharge approval, settlement readiness, and period-end elimination evidence. It will support multi-entity group with shared service recharges users on Oracle NetSuite OneWorld, with emphasis on counterparty confirmation, recharge approval, settlement evidence, and elimination support.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Entity codes and counterparty mappings are available for the pilot group.

## Functional Requirements

- FR-01: Capture originating entity, counterparty entity, recharge type, currency, amount, tax treatment, and settlement status.
- FR-02: Match intercompany AR/AP balances by counterparty, invoice reference, amount, currency, and period.
- FR-03: Track unmatched intercompany balances with owner, ageing, reason code, and expected settlement date.
- FR-04: Store recharge rules, allocation basis, supporting calculation, requester, reviewer, and approval status.
- FR-05: Identify FX differences by entity pair, currency, transaction reference, and materiality threshold.
- FR-06: Require counterparty confirmation before settlement readiness or elimination support sign-off.
- FR-07: Produce intercompany ageing and mismatch reports by entity pair and transaction type.
- FR-08: Export elimination support evidence for group reporting review.
- FR-09: Provide reporting for Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary.
- FR-10: Evidence Counterparty confirmation, recharge approval, settlement evidence, and elimination support for finance review.

## Non-Functional Requirements

- NFR-01: Intercompany status must be understandable to entity finance teams and group finance.
- NFR-02: Reporting must support period-end review without manual consolidation of entity spreadsheets.
- NFR-03: Access must separate recharge preparation, counterparty confirmation, approval, and settlement release.
- NFR-04: Evidence must be retained by period for audit and group reporting review.
- NFR-05: The workflow must support multi-currency balances and FX difference commentary.
- NFR-06: Provide reporting for Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary.
- NFR-07: Evidence Counterparty confirmation, recharge approval, settlement evidence, and elimination support for finance review.

## Data Requirements

- DR-01: Originating entity
- DR-02: Counterparty entity
- DR-03: Recharge reference
- DR-04: Counterparty invoice reference
- DR-05: Transaction currency
- DR-06: Settlement status
- DR-07: FX difference
- DR-08: Elimination support reference
- DR-09: Provide reporting for Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary.
- DR-10: Evidence Counterparty confirmation, recharge approval, settlement evidence, and elimination support for finance review.

## Controls

- CTRL-01: Recharge rules and allocation basis require finance owner approval.
- CTRL-02: Counterparty confirmation is required before settlement readiness.
- CTRL-03: Aged unmatched intercompany balances escalate to group finance.
- CTRL-04: FX differences over materiality threshold require review and explanation.
- CTRL-05: Elimination support cannot be marked complete until mismatches are resolved or approved.
- CTRL-06: Provide reporting for Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary.
- CTRL-07: Evidence Counterparty confirmation, recharge approval, settlement evidence, and elimination support for finance review.

## Audit Trail Requirements

- AUD-01: Store recharge creation, approval, counterparty confirmation, settlement, and elimination sign-off timestamps.
- AUD-02: Record allocation basis changes with requester, reviewer, reason, and effective period.
- AUD-03: Track unmatched balance owner/status history by entity pair.
- AUD-04: Preserve FX difference explanations and reviewer decisions.
- AUD-05: Keep counterparty confirmation evidence and settlement approval references.
- AUD-06: Provide reporting for Entity-pair ageing, unmatched balances, recharge approvals, and FX difference summary.
- AUD-07: Evidence Counterparty confirmation, recharge approval, settlement evidence, and elimination support for finance review.

## User Stories

- As an entity accountant, I want counterparty confirmation so that intercompany mismatches are resolved before close.
- As group finance, I want ageing by entity pair so that old balances are escalated quickly.
- As a recharge preparer, I want approved allocation rules so that recharge calculations are consistent.
- As a reviewer, I want FX differences explained so that group reporting variances are defensible.
- As an auditor, I want elimination support evidence so that consolidation adjustments are traceable.

## UAT Test Cases

- **UAT-01:** Intercompany AR balance does not match the counterparty AP balance. Expected result: A mismatch is created with entity pair, owner, ageing, and reason fields.
- **UAT-02:** Recharge allocation basis is changed. Expected result: The change requires approval and stores reason, requester, reviewer, and effective period.
- **UAT-03:** Counterparty confirmation is missing. Expected result: Settlement readiness and elimination sign-off are blocked.
- **UAT-04:** FX difference exceeds materiality threshold. Expected result: Review explanation and approval are required before completion.
- **UAT-05:** Aged unmatched balance passes escalation threshold. Expected result: Group finance receives escalation and the item appears in the aged mismatch report.
- **UAT-06:** Intercompany settlement pack is exported. Expected result: The pack includes balances, mismatches, confirmations, FX differences, settlement status, and elimination evidence.

## Acceptance Criteria

- Intercompany balances show entity pair, currency, reference, owner, status, and ageing.
- Recharge allocation rules are approved and versioned.
- Counterparty confirmation is required before settlement readiness.
- FX differences above threshold are explained and approved.
- Elimination support exports with mismatch and sign-off evidence.

## Implementation Risks and Dependencies

- Entity chart-of-account mapping must be aligned for counterparty matching.
- Recharge policies and allocation methods require group finance approval.
- Multi-currency treatment must align with accounting policy.
- Historic unmatched balances may need remediation before rollout.
- Entity teams must agree ownership of mismatch resolution.

## Implementation Notes

- Confirm Intercompany Settlements process owner and reviewer roles before design sign-off.
- Validate the required data fields against Oracle NetSuite OneWorld configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
