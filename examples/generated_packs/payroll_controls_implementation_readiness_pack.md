# Payroll Controls Implementation Readiness Pack

**Prepared for:** Riverstone Care Ltd

**Target system:** Not selected

## Readiness Summary

This readiness pack translates the approved Payroll Controls requirements, controls, data needs, UAT cases, risks, and target-system context into evidence-based implementation review prompts. All checks begin as Not assessed and require finance and implementation team validation.

## Process Implementation Checklist

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| PIC-01 | Confirm starter, leaver, pay-change, payroll-run, and payment-file approvals have segregated owners. | Approved payroll control matrix and system access design. | Payroll Controls Owner | Not assessed | FR-01, FR-03, FR-06, CTRL-01 | Requires finance and implementation team review. |
| PIC-02 | Confirm payroll register, GL posting, and payment-file totals reconcile before release. | Approved payroll-to-GL and payment reconciliation procedure. | Payroll Finance Controller | Not assessed | FR-05, CTRL-04, AUD-04 | Requires finance and implementation team review. |
| PIC-03 | Confirm implementation treatment for starter and leaver control gaps, including the control activity: Starter, leaver, salary, deduction, and bank detail changes require approval before payroll processing. | Store payroll master change request, approval, processing, and effective date history. | Payroll Controls Owner | Not assessed | CRM-01, FR-01, UAT-01 | HR and payroll ownership of master data changes must be agreed. |
| PIC-04 | Confirm implementation treatment for payroll change approval delays, including the control activity: Payroll input files require preparer and reviewer sign-off before calculation. | Record payroll input file version, preparer, reviewer, approval, and cutoff timestamp. | Payroll Controls Owner | Not assessed | CRM-02, FR-02, UAT-02 | Payroll cutoff rules and approval thresholds require policy sign-off. |
| PIC-05 | Confirm implementation treatment for manual payroll input checks, including the control activity: Payroll exceptions over threshold require investigation and approval. | Preserve exception review notes and approval decisions. | Payroll Controls Owner | Not assessed | CRM-03, FR-03, UAT-03 | Sensitive payroll access roles must be configured carefully. |
| PIC-06 | Confirm implementation treatment for starter and leaver control gaps, including the control activity: Payroll register must reconcile to GL control accounts and payment file totals. | Track payroll reconciliation owner/status history by period. | Payroll Controls Owner | Not assessed | CRM-04, FR-04, UAT-04 | GL account mapping must be validated before reconciliation testing. |
| PIC-07 | Confirm implementation treatment for payroll change approval delays, including the control activity: Payroll payment file release requires finance approval. | Keep payment file approval evidence with approver, date, amount, and bank file reference. | Payroll Controls Owner | Not assessed | CRM-05, FR-05, UAT-05 | Historic payroll exception categories may need standardisation before rollout. |

## Target-System Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| SYS-01 | Confirm the target system, edition, modules, localisation, integrations, and implementation scope for Payroll Controls. | Approved target-system scope and architecture decision. | Finance Transformation Lead | Not assessed | INTAKE-TARGET-SYSTEM | No target-system capability conclusion can be made until the selection and implementation scope are confirmed. |

## Data Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| DATA-01 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Employee ID. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-01 | Validate completeness and control usability using representative data. |
| DATA-02 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Payroll period. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-02 | Validate completeness and control usability using representative data. |
| DATA-03 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Payroll change type. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-03 | Validate completeness and control usability using representative data. |
| DATA-04 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Effective date. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-04 | Validate completeness and control usability using representative data. |
| DATA-05 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Approval reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-05 | Validate completeness and control usability using representative data. |
| DATA-06 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Gross-to-net total. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-06 | Validate completeness and control usability using representative data. |
| DATA-07 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Payroll control account. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-07 | Validate completeness and control usability using representative data. |
| DATA-08 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Payment file reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Payroll Controls Owner and Finance Data Owner | Not assessed | DR-08 | Validate completeness and control usability using representative data. |

## Controls and UAT Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CU-01 | Confirm configuration, ownership, negative-path testing, and evidence for Starter, leaver, salary, deduction, and bank detail changes require approval before payroll processing. | UAT evidence demonstrating: Payroll processing is blocked until approval evidence is captured. Audit evidence must also support Store payroll master change request, approval, processing, and effective date history. | Payroll Controls Owner and Controls/UAT Lead | Not assessed | CTRL-01, AUD-01, RPT-01, UAT-02 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-02 | Confirm configuration, ownership, negative-path testing, and evidence for Payroll input files require preparer and reviewer sign-off before calculation. | UAT evidence demonstrating: The pack includes changes, exceptions, reconciliation, payment approval, and sign-off evidence. Audit evidence must also support Record payroll input file version, preparer, reviewer, approval, and cutoff timestamp. | Payroll Controls Owner and Controls/UAT Lead | Not assessed | CTRL-02, AUD-02, RPT-02, UAT-06 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-03 | Confirm configuration, ownership, negative-path testing, and evidence for Payroll exceptions over threshold require investigation and approval. | UAT evidence demonstrating: The pack includes changes, exceptions, reconciliation, payment approval, and sign-off evidence. Audit evidence must also support Preserve exception review notes and approval decisions. | Payroll Controls Owner and Controls/UAT Lead | Not assessed | CTRL-03, AUD-03, RPT-03, UAT-06 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-04 | Confirm configuration, ownership, negative-path testing, and evidence for Payroll register must reconcile to GL control accounts and payment file totals. | UAT evidence demonstrating: A reconciliation difference is created with owner, amount, and reason fields. Audit evidence must also support Track payroll reconciliation owner/status history by period. | Payroll Controls Owner and Controls/UAT Lead | Not assessed | CTRL-04, AUD-04, RPT-04, UAT-03 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-05 | Confirm configuration, ownership, negative-path testing, and evidence for Payroll payment file release requires finance approval. | UAT evidence demonstrating: Finance approval is required before payment file status becomes released. Audit evidence must also support Keep payment file approval evidence with approver, date, amount, and bank file reference. | Payroll Controls Owner and Controls/UAT Lead | Not assessed | CTRL-05, AUD-05, RPT-05, UAT-05 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |

## Configuration Workshop Questions

| ID | Question | Implementation Relevance | Source References |
| --- | --- | --- | --- |
| CWQ-01 | Which HR and payroll changes require dual approval, effective dating, and cutoff enforcement? | Defines sensitive payroll change controls and late-change treatment. | FR-01, CTRL-01, UAT-01 |
| CWQ-02 | Which exception categories and thresholds must stop payroll or payment-file release? | Establishes controlled payroll exception handling before configuration. | FR-03, CTRL-03, UAT-03 |
| CWQ-03 | How should payroll results map to GL accounts, dimensions, entities, and payment totals? | Defines reconciliation and posting design across payroll and finance systems. | FR-05, DR-07, UAT-04 |

## Cutover Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CUT-01 | Validate employee payroll masters, effective-dated changes, access roles, and statutory fields. | Signed payroll data and access validation with protected exception handling. | Payroll Controls Owner | Not assessed | DR-01, RISK-01, RISK-03 | Requires finance and implementation team review. |
| CUT-02 | Complete parallel payroll, GL reconciliation, and payment-file control testing before cutover. | Approved parallel-run reconciliation and unresolved variance log. | Payroll Finance Controller | Not assessed | UAT-04, UAT-05, RISK-04 | Requires finance and implementation team review. |

## Open Decisions and Dependencies

| ID | Decision Required | Dependency or Impact | Suggested Owner | Source References |
| --- | --- | --- | --- | --- |
| DEC-00 | Confirm the target ERP or finance system, edition, modules, localisation, integration boundaries, and implementation scope. | Target-system readiness and detailed configuration workshops remain provisional until this selection is approved. | Finance Transformation Lead | INTAKE-TARGET-SYSTEM |
| DEC-01 | Confirm implementation treatment for: HR and payroll ownership of master data changes must be agreed. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Payroll Controls Owner | RISK-01 |
| DEC-02 | Confirm implementation treatment for: Payroll cutoff rules and approval thresholds require policy sign-off. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Payroll Controls Owner | RISK-02 |
| DEC-03 | Confirm implementation treatment for: Sensitive payroll access roles must be configured carefully. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Payroll Controls Owner | RISK-03 |
| DEC-04 | Confirm implementation treatment for: GL account mapping must be validated before reconciliation testing. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Payroll Controls Owner | RISK-04 |
| DEC-05 | Confirm implementation treatment for: Historic payroll exception categories may need standardisation before rollout. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Payroll Controls Owner | RISK-05 |

## Source Traceability

| Readiness Item | Source References |
| --- | --- |
| PIC-01 | FR-01, FR-03, FR-06, CTRL-01 |
| PIC-02 | FR-05, CTRL-04, AUD-04 |
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
| CU-02 | CTRL-02, AUD-02, RPT-02, UAT-06 |
| CU-03 | CTRL-03, AUD-03, RPT-03, UAT-06 |
| CU-04 | CTRL-04, AUD-04, RPT-04, UAT-03 |
| CU-05 | CTRL-05, AUD-05, RPT-05, UAT-05 |
| CUT-01 | DR-01, RISK-01, RISK-03 |
| CUT-02 | UAT-04, UAT-05, RISK-04 |
| CWQ-01 | FR-01, CTRL-01, UAT-01 |
| CWQ-02 | FR-03, CTRL-03, UAT-03 |
| CWQ-03 | FR-05, DR-07, UAT-04 |
| DEC-00 | INTAKE-TARGET-SYSTEM |
| DEC-01 | RISK-01 |
| DEC-02 | RISK-02 |
| DEC-03 | RISK-03 |
| DEC-04 | RISK-04 |
| DEC-05 | RISK-05 |

## Public-Safe Sample Data Note

This pack was generated from fictional, public-safe sample inputs. It does not contain real employer, client, supplier, bank, VAT, payroll, or operational data. Do not upload confidential business information into a public demo.
