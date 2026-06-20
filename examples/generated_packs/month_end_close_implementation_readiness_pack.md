# Month-end Close Implementation Readiness Pack

**Prepared for:** Cedar Grove Retail Ltd

**Target system:** Not selected

## Readiness Summary

This readiness pack translates the approved Month-end Close requirements, controls, data needs, UAT cases, risks, and target-system context into evidence-based implementation review prompts. All checks begin as Not assessed and require finance and implementation team validation.

## Process Implementation Checklist

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| PIC-01 | Confirm the close calendar defines every task owner, reviewer, dependency, due point, and evidence requirement. | Approved close calendar and responsibility matrix. | Financial Controller | Not assessed | FR-01, FR-02, CTRL-01 | Requires finance and implementation team review. |
| PIC-02 | Confirm journals and high-risk reconciliations cannot reach completion without required approval and sign-off. | Approved journal and reconciliation control workflow. | Close Process Owner | Not assessed | FR-04, FR-05, CTRL-03, CTRL-04 | Requires finance and implementation team review. |
| PIC-03 | Confirm implementation treatment for late close tasks, including the control activity: Reviewer sign-off required before high-risk reconciliations are marked complete. | Store task status changes, evidence uploads, preparer completion, and reviewer sign-off timestamps. | Financial Controller | Not assessed | CRM-01, FR-01, UAT-01 | Close task ownership must be agreed across finance teams. |
| PIC-04 | Confirm implementation treatment for manual close status tracking, including the control activity: Manual journals require approval before posting to closed periods. | Record journal submission, approval, rejection, posting, and reversal history. | Financial Controller | Not assessed | CRM-02, FR-02, UAT-02 | Balance sheet reconciliation risk ratings may need finance controller approval. |
| PIC-05 | Confirm implementation treatment for missing reconciliation evidence, including the control activity: Overdue close tasks escalate based on close calendar thresholds. | Preserve reopen reasons and approval decisions for closed tasks. | Financial Controller | Not assessed | CRM-03, FR-03, UAT-03 | Journal approval thresholds must align with delegation of authority. |
| PIC-06 | Confirm implementation treatment for late close tasks, including the control activity: Reopened tasks require reason, requester, approver, and timestamp. | Track reconciliation owner/status history for each close period. | Financial Controller | Not assessed | CRM-04, FR-04, UAT-04 | Legacy spreadsheet trackers may need migration or archive decisions. |
| PIC-07 | Confirm implementation treatment for manual close status tracking, including the control activity: Period close completion requires all mandatory tasks and reconciliations to be signed off. | Keep close pack export timestamp, preparer, reviewer, and final approver evidence. | Financial Controller | Not assessed | CRM-05, FR-05, UAT-05 | Users need discipline to attach evidence before sign-off. |

## Target-System Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| SYS-01 | Confirm the target system, edition, modules, localisation, integrations, and implementation scope for Month-end Close. | Approved target-system scope and architecture decision. | Finance Transformation Lead | Not assessed | INTAKE-TARGET-SYSTEM | No target-system capability conclusion can be made until the selection and implementation scope are confirmed. |

## Data Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| DATA-01 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Close period. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-01 | Validate completeness and control usability using representative data. |
| DATA-02 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Close task ID. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-02 | Validate completeness and control usability using representative data. |
| DATA-03 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Task owner. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-03 | Validate completeness and control usability using representative data. |
| DATA-04 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Reviewer. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-04 | Validate completeness and control usability using representative data. |
| DATA-05 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Balance sheet account. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-05 | Validate completeness and control usability using representative data. |
| DATA-06 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Journal batch reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-06 | Validate completeness and control usability using representative data. |
| DATA-07 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Completion evidence link. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-07 | Validate completeness and control usability using representative data. |
| DATA-08 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Sign-off timestamp. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Financial Controller and Finance Data Owner | Not assessed | DR-08 | Validate completeness and control usability using representative data. |

## Controls and UAT Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CU-01 | Confirm configuration, ownership, negative-path testing, and evidence for Reviewer sign-off required before high-risk reconciliations are marked complete. | UAT evidence demonstrating: Reviewer sign-off is blocked until evidence is attached. Audit evidence must also support Store task status changes, evidence uploads, preparer completion, and reviewer sign-off timestamps. | Financial Controller and Controls/UAT Lead | Not assessed | CTRL-01, AUD-01, RPT-01, UAT-02 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-02 | Confirm configuration, ownership, negative-path testing, and evidence for Manual journals require approval before posting to closed periods. | UAT evidence demonstrating: Posting is blocked until the correct approver signs off. Audit evidence must also support Record journal submission, approval, rejection, posting, and reversal history. | Financial Controller and Controls/UAT Lead | Not assessed | CTRL-02, AUD-02, RPT-02, UAT-03 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-03 | Confirm configuration, ownership, negative-path testing, and evidence for Overdue close tasks escalate based on close calendar thresholds. | UAT evidence demonstrating: The pack includes task completion, reconciliations, journals, overdue items, and sign-off evidence. Audit evidence must also support Preserve reopen reasons and approval decisions for closed tasks. | Financial Controller and Controls/UAT Lead | Not assessed | CTRL-03, AUD-03, RPT-03, UAT-06 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-04 | Confirm configuration, ownership, negative-path testing, and evidence for Reopened tasks require reason, requester, approver, and timestamp. | UAT evidence demonstrating: Reopen reason, requester, approver, and timestamp are recorded. Audit evidence must also support Track reconciliation owner/status history for each close period. | Financial Controller and Controls/UAT Lead | Not assessed | CTRL-04, AUD-04, RPT-04, UAT-04 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-05 | Confirm configuration, ownership, negative-path testing, and evidence for Period close completion requires all mandatory tasks and reconciliations to be signed off. | UAT evidence demonstrating: The pack includes task completion, reconciliations, journals, overdue items, and sign-off evidence. Audit evidence must also support Keep close pack export timestamp, preparer, reviewer, and final approver evidence. | Financial Controller and Controls/UAT Lead | Not assessed | CTRL-05, AUD-05, RPT-05, UAT-06 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |

## Configuration Workshop Questions

| ID | Question | Implementation Relevance | Source References |
| --- | --- | --- | --- |
| CWQ-01 | Which close tasks are entity-specific, group-wide, dependent, recurring, or conditional? | Defines reusable close templates and dependency sequencing. | FR-01, DR-01, UAT-01 |
| CWQ-02 | Which reconciliation risk ratings require additional review or evidence? | Aligns reconciliation workflow with finance risk policy. | FR-04, CTRL-03, UAT-03 |
| CWQ-03 | Which journal types and thresholds require preparer, reviewer, and final approver separation? | Establishes journal workflow and segregation before configuration. | FR-05, CTRL-04, UAT-04 |

## Cutover Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CUT-01 | Approve migration or archive treatment for legacy close trackers and evidence links. | Signed tracker transition plan and retained-evidence inventory. | Close Process Owner | Not assessed | DR-08, RISK-04 | Requires finance and implementation team review. |
| CUT-02 | Load and dry-run the first close calendar with owners, dependencies, and reviewer capacity confirmed. | Completed mock close with documented timing and unresolved gaps. | Financial Controller | Not assessed | FR-01, RISK-01 | Requires finance and implementation team review. |

## Open Decisions and Dependencies

| ID | Decision Required | Dependency or Impact | Suggested Owner | Source References |
| --- | --- | --- | --- | --- |
| DEC-00 | Confirm the target ERP or finance system, edition, modules, localisation, integration boundaries, and implementation scope. | Target-system readiness and detailed configuration workshops remain provisional until this selection is approved. | Finance Transformation Lead | INTAKE-TARGET-SYSTEM |
| DEC-01 | Confirm implementation treatment for: Close task ownership must be agreed across finance teams. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Financial Controller | RISK-01 |
| DEC-02 | Confirm implementation treatment for: Balance sheet reconciliation risk ratings may need finance controller approval. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Financial Controller | RISK-02 |
| DEC-03 | Confirm implementation treatment for: Journal approval thresholds must align with delegation of authority. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Financial Controller | RISK-03 |
| DEC-04 | Confirm implementation treatment for: Legacy spreadsheet trackers may need migration or archive decisions. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Financial Controller | RISK-04 |
| DEC-05 | Confirm implementation treatment for: Users need discipline to attach evidence before sign-off. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Financial Controller | RISK-05 |

## Source Traceability

| Readiness Item | Source References |
| --- | --- |
| PIC-01 | FR-01, FR-02, CTRL-01 |
| PIC-02 | FR-04, FR-05, CTRL-03, CTRL-04 |
| PIC-03 | CRM-01, FR-01, UAT-01 |
| PIC-04 | CRM-02, FR-02, UAT-02 |
| PIC-05 | CRM-03, FR-03, UAT-03 |
| PIC-06 | CRM-04, FR-04, UAT-04 |
| PIC-07 | CRM-05, FR-05, UAT-05 |
| SYS-01 | INTAKE-TARGET-SYSTEM |
| DATA-01 | DR-01 |
| DATA-02 | DR-02 |
| DATA-03 | DR-03 |
| DATA-04 | DR-04 |
| DATA-05 | DR-05 |
| DATA-06 | DR-06 |
| DATA-07 | DR-07 |
| DATA-08 | DR-08 |
| CU-01 | CTRL-01, AUD-01, RPT-01, UAT-02 |
| CU-02 | CTRL-02, AUD-02, RPT-02, UAT-03 |
| CU-03 | CTRL-03, AUD-03, RPT-03, UAT-06 |
| CU-04 | CTRL-04, AUD-04, RPT-04, UAT-04 |
| CU-05 | CTRL-05, AUD-05, RPT-05, UAT-06 |
| CUT-01 | DR-08, RISK-04 |
| CUT-02 | FR-01, RISK-01 |
| CWQ-01 | FR-01, DR-01, UAT-01 |
| CWQ-02 | FR-04, CTRL-03, UAT-03 |
| CWQ-03 | FR-05, CTRL-04, UAT-04 |
| DEC-00 | INTAKE-TARGET-SYSTEM |
| DEC-01 | RISK-01 |
| DEC-02 | RISK-02 |
| DEC-03 | RISK-03 |
| DEC-04 | RISK-04 |
| DEC-05 | RISK-05 |

## Public-Safe Sample Data Note

This pack was generated from fictional, public-safe sample inputs. It does not contain real employer, client, supplier, bank, VAT, payroll, or operational data. Do not upload confidential business information into a public demo.
