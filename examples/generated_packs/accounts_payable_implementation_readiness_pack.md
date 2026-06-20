# Accounts Payable Implementation Readiness Pack

**Prepared for:** Northstar Trading Ltd

**Target system:** Not selected

## Readiness Summary

This readiness pack translates the approved Accounts Payable requirements, controls, data needs, UAT cases, risks, and target-system context into evidence-based implementation review prompts. All checks begin as Not assessed and require finance and implementation team validation.

## Process Implementation Checklist

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| PIC-01 | Confirm invoice intake, matching, approval, and payment-readiness states are signed off end to end. | Approved AP workflow showing owners, thresholds, exception routes, and payment holds. | AP Process Owner | Not assessed | FR-03, FR-04, FR-05, CTRL-02 | Requires finance and implementation team review. |
| PIC-02 | Confirm supplier master and bank-detail changes are segregated from invoice and payment approval. | Approved role matrix and sensitive supplier-field change procedure. | AP Controller | Not assessed | FR-06, CTRL-03, AUD-03 | Requires finance and implementation team review. |
| PIC-03 | Confirm implementation treatment for duplicate invoices, including the control activity: Duplicate invoice warning before approval or payment release. | Store invoice creation, coding, approval, rejection, and payment readiness timestamps. | Accounts Payable Process Owner | Not assessed | CRM-01, FR-01, UAT-01 | Supplier master data may require cleansing before controls can operate reliably. |
| PIC-04 | Confirm implementation treatment for manual approval chasing, including the control activity: Approval threshold control by amount and cost centre. | Record every approval decision with approver, date, amount, and delegation status. | Accounts Payable Process Owner | Not assessed | CRM-02, FR-02, UAT-02 | Purchase order and goods receipt data must be available for three-way match readiness. |
| PIC-05 | Confirm implementation treatment for weak supplier master controls, including the control activity: Supplier bank detail change review before first payment after change. | Keep before-and-after supplier master data values for sensitive changes. | Accounts Payable Process Owner | Not assessed | CRM-03, FR-03, UAT-03 | Delegated approval rules must be signed off by finance leadership. |
| PIC-06 | Confirm implementation treatment for duplicate invoices, including the control activity: Three-way match exception review for PO-backed purchases. | Preserve evidence links for invoice image, purchase order, goods receipt, and payment batch. | Accounts Payable Process Owner | Not assessed | CRM-04, FR-04, UAT-04 | Payment platform integration scope must be confirmed before build. |
| PIC-07 | Confirm implementation treatment for manual approval chasing, including the control activity: Segregation of duties control between supplier maintenance and payment approval. | Track exception resolution notes and reviewer sign-off. | Accounts Payable Process Owner | Not assessed | CRM-05, FR-05, UAT-05 | Users need training on exception reason codes to avoid inconsistent reporting. |

## Target-System Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| SYS-01 | Confirm the target system, edition, modules, localisation, integrations, and implementation scope for Accounts Payable. | Approved target-system scope and architecture decision. | Finance Transformation Lead | Not assessed | INTAKE-TARGET-SYSTEM | No target-system capability conclusion can be made until the selection and implementation scope are confirmed. |

## Data Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| DATA-01 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Supplier master ID. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-01 | Validate completeness and control usability using representative data. |
| DATA-02 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Supplier invoice number. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-02 | Validate completeness and control usability using representative data. |
| DATA-03 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Purchase order reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-03 | Validate completeness and control usability using representative data. |
| DATA-04 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Goods receipt reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-04 | Validate completeness and control usability using representative data. |
| DATA-05 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Invoice gross amount. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-05 | Validate completeness and control usability using representative data. |
| DATA-06 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Tax amount. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-06 | Validate completeness and control usability using representative data. |
| DATA-07 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Approval owner. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-07 | Validate completeness and control usability using representative data. |
| DATA-08 | Confirm the source, definition, ownership, cleansing rule, migration treatment, and reconciliation approach for Payment batch reference. | Approved data definition, source-to-target mapping, quality result, and reconciliation evidence. | Accounts Payable Process Owner and Finance Data Owner | Not assessed | DR-08 | Validate completeness and control usability using representative data. |

## Controls and UAT Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CU-01 | Confirm configuration, ownership, negative-path testing, and evidence for Duplicate invoice warning before approval or payment release. | UAT evidence demonstrating: The system flags the invoice and blocks payment readiness until reviewed. Audit evidence must also support Store invoice creation, coding, approval, rejection, and payment readiness timestamps. | Accounts Payable Process Owner and Controls/UAT Lead | Not assessed | CTRL-01, AUD-01, RPT-01, UAT-01 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-02 | Confirm configuration, ownership, negative-path testing, and evidence for Approval threshold control by amount and cost centre. | UAT evidence demonstrating: Approval routes to the higher authority approver. Audit evidence must also support Record every approval decision with approver, date, amount, and delegation status. | Accounts Payable Process Owner and Controls/UAT Lead | Not assessed | CTRL-02, AUD-02, RPT-02, UAT-03 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-03 | Confirm configuration, ownership, negative-path testing, and evidence for Supplier bank detail change review before first payment after change. | UAT evidence demonstrating: The payment is held until supplier master review is complete. Audit evidence must also support Keep before-and-after supplier master data values for sensitive changes. | Accounts Payable Process Owner and Controls/UAT Lead | Not assessed | CTRL-03, AUD-03, RPT-03, UAT-04 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-04 | Confirm configuration, ownership, negative-path testing, and evidence for Three-way match exception review for PO-backed purchases. | UAT evidence demonstrating: The invoice appears in the three-way match exception queue. Audit evidence must also support Preserve evidence links for invoice image, purchase order, goods receipt, and payment batch. | Accounts Payable Process Owner and Controls/UAT Lead | Not assessed | CTRL-04, AUD-04, RPT-04, UAT-02 | Confirm the control operates with production-like roles, data, reporting, and retained evidence before sign-off. |
| CU-05 | Confirm configuration, ownership, negative-path testing, and evidence for Segregation of duties control between supplier maintenance and payment approval. | A dedicated positive and negative-path UAT case must be defined. Audit evidence must also support Track exception resolution notes and reviewer sign-off. | Accounts Payable Process Owner and Controls/UAT Lead | Not assessed | CTRL-05, AUD-05, RPT-05 | No directly aligned UAT case was identified; add one before control design sign-off. |

## Configuration Workshop Questions

| ID | Question | Implementation Relevance | Source References |
| --- | --- | --- | --- |
| CWQ-01 | Which supplier, invoice, currency, amount, and date combinations should trigger duplicate-invoice review? | Defines duplicate detection configuration without blocking legitimate recurring invoices. | FR-02, CTRL-01, UAT-01 |
| CWQ-02 | How should approval thresholds vary by cost centre, amount, supplier category, and delegation status? | Establishes AP routing and delegation rules before workflow configuration. | FR-04, CTRL-02, UAT-03 |
| CWQ-03 | Which exceptions can proceed without purchase-order or goods-receipt evidence, and who approves them? | Defines controlled non-PO and match-exception treatment. | FR-03, CTRL-04, UAT-02 |

## Cutover Readiness

| ID | Finance-Specific Check | Evidence Required | Suggested Owner | Status | Source References | Validation Note |
| --- | --- | --- | --- | --- | --- | --- |
| CUT-01 | Cleanse supplier masters, duplicate suppliers, bank details, tax identifiers, and payment terms before migration. | Signed supplier cleansing results and unresolved-exception log. | Supplier Master Data Owner | Not assessed | DR-01, RISK-01 | Requires finance and implementation team review. |
| CUT-02 | Resolve or explicitly migrate blocked invoices and unmatched purchase-order or receipt exceptions. | Approved open-item migration treatment and reconciliation totals. | AP Controller | Not assessed | DR-03, DR-04, RISK-02 | Requires finance and implementation team review. |

## Open Decisions and Dependencies

| ID | Decision Required | Dependency or Impact | Suggested Owner | Source References |
| --- | --- | --- | --- | --- |
| DEC-00 | Confirm the target ERP or finance system, edition, modules, localisation, integration boundaries, and implementation scope. | Target-system readiness and detailed configuration workshops remain provisional until this selection is approved. | Finance Transformation Lead | INTAKE-TARGET-SYSTEM |
| DEC-01 | Confirm implementation treatment for: Supplier master data may require cleansing before controls can operate reliably. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Accounts Payable Process Owner | RISK-01 |
| DEC-02 | Confirm implementation treatment for: Purchase order and goods receipt data must be available for three-way match readiness. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Accounts Payable Process Owner | RISK-02 |
| DEC-03 | Confirm implementation treatment for: Delegated approval rules must be signed off by finance leadership. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Accounts Payable Process Owner | RISK-03 |
| DEC-04 | Confirm implementation treatment for: Payment platform integration scope must be confirmed before build. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Accounts Payable Process Owner | RISK-04 |
| DEC-05 | Confirm implementation treatment for: Users need training on exception reason codes to avoid inconsistent reporting. | Configuration, data preparation, control design, testing, or cutover cannot be fully confirmed until this dependency is resolved. | Accounts Payable Process Owner | RISK-05 |

## Source Traceability

| Readiness Item | Source References |
| --- | --- |
| PIC-01 | FR-03, FR-04, FR-05, CTRL-02 |
| PIC-02 | FR-06, CTRL-03, AUD-03 |
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
| CU-01 | CTRL-01, AUD-01, RPT-01, UAT-01 |
| CU-02 | CTRL-02, AUD-02, RPT-02, UAT-03 |
| CU-03 | CTRL-03, AUD-03, RPT-03, UAT-04 |
| CU-04 | CTRL-04, AUD-04, RPT-04, UAT-02 |
| CU-05 | CTRL-05, AUD-05, RPT-05 |
| CUT-01 | DR-01, RISK-01 |
| CUT-02 | DR-03, DR-04, RISK-02 |
| CWQ-01 | FR-02, CTRL-01, UAT-01 |
| CWQ-02 | FR-04, CTRL-02, UAT-03 |
| CWQ-03 | FR-03, CTRL-04, UAT-02 |
| DEC-00 | INTAKE-TARGET-SYSTEM |
| DEC-01 | RISK-01 |
| DEC-02 | RISK-02 |
| DEC-03 | RISK-03 |
| DEC-04 | RISK-04 |
| DEC-05 | RISK-05 |

## Public-Safe Sample Data Note

This pack was generated from fictional, public-safe sample inputs. It does not contain real employer, client, supplier, bank, VAT, payroll, or operational data. Do not upload confidential business information into a public demo.
