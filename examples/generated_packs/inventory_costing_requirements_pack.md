# Inventory Costing Requirements Pack

**Synthetic company:** MapleWorks Components Ltd

> Synthetic demo output only. Do not use this sample as client, employer, or operational data.

## Executive Summary

MapleWorks Components Ltd needs a structured Inventory Costing requirements pack for SAP Business One. The MVP scope turns current finance pain points (Inventory valuation differences, Cost variance review gaps, and Manual landed cost allocation) into implementable requirements covering data capture, controls, audit trail, UAT, and reporting. The design is sized for 4 warehouses, 2,800 SKUs, and monthly standard cost review and prioritises Standard cost changes require approval before effective date. within a target delivery window of 11 weeks.

## Current-State Problem Statement

The current inventory costing process relies on ERP inventory module, warehouse adjustment logs, and costing spreadsheets. This creates avoidable risk around Inventory valuation differences, Cost variance review gaps, and Manual landed cost allocation and makes inventory valuation, cost variance, landed cost, and subledger-to-gl summary harder to produce consistently. Finance needs clearer ownership, data standards, and review evidence before the process is ready for ERP optimisation or automation.

## Future-State Process Scope

The future-state scope covers Inventory valuation, cost updates, landed cost allocation, variance review, stock adjustments, and GL reconciliation. Visibility of standard cost, actual cost, purchase price variance, production variance, and inventory ageing. Controls over costing method changes, manual adjustments, and reconciliation sign-off. It will support light manufacturing business users on SAP Business One, with emphasis on cost change approvals, stock adjustment controls, and valuation audit evidence.

## Assumptions

- All sample names and operating details in this pack are synthetic.
- The pack is a requirements accelerator and does not replace finance owner sign-off.
- System configuration will follow approved finance policies and access controls.
- Item master data includes active SKU and warehouse identifiers.

## Functional Requirements

- FR-01: Capture SKU, warehouse, quantity, unit cost, valuation method, cost version, and inventory value.
- FR-02: Reconcile inventory subledger balances to GL inventory control accounts by period and location.
- FR-03: Track standard cost updates with effective date, reason, requester, reviewer, and approval status.
- FR-04: Allocate landed costs using approved allocation basis and link charges to receipt or shipment references.
- FR-05: Identify purchase price variance, production variance, and manual cost adjustments by materiality threshold.
- FR-06: Route stock adjustments and write-downs for approval before posting.
- FR-07: Produce inventory valuation reports by SKU, warehouse, ageing bucket, cost method, and variance category.
- FR-08: Preserve costing assumptions and supporting evidence for finance review.
- FR-09: Provide reporting for Inventory valuation, cost variance, landed cost, and subledger-to-GL summary.
- FR-10: Evidence Cost change approvals, stock adjustment controls, and valuation audit evidence for finance review.

## Non-Functional Requirements

- NFR-01: Costing reports must be understandable to finance, operations, and inventory control users.
- NFR-02: The workflow must support period-end valuation review without offline spreadsheet rebuilds.
- NFR-03: Access must separate cost maintenance, stock adjustment entry, adjustment approval, and GL posting.
- NFR-04: Valuation evidence must be retained for audit and management review.
- NFR-05: The design must support location-level reporting without mixing warehouse responsibilities.
- NFR-06: Provide reporting for Inventory valuation, cost variance, landed cost, and subledger-to-GL summary.
- NFR-07: Evidence Cost change approvals, stock adjustment controls, and valuation audit evidence for finance review.

## Data Requirements

- DR-01: SKU/item ID
- DR-02: Warehouse/location
- DR-03: Quantity on hand
- DR-04: Unit cost
- DR-05: Valuation method
- DR-06: Landed cost reference
- DR-07: Inventory control account
- DR-08: Cost variance reason code
- DR-09: Provide reporting for Inventory valuation, cost variance, landed cost, and subledger-to-GL summary.
- DR-10: Evidence Cost change approvals, stock adjustment controls, and valuation audit evidence for finance review.

## Controls

- CTRL-01: Standard cost changes require approval before effective date.
- CTRL-02: Stock adjustments and write-downs require reason codes and reviewer sign-off.
- CTRL-03: Inventory subledger-to-GL differences over threshold require owner assignment.
- CTRL-04: Landed cost allocation basis must be approved and retained.
- CTRL-05: Costing method changes require finance controller approval.
- CTRL-06: Provide reporting for Inventory valuation, cost variance, landed cost, and subledger-to-GL summary.
- CTRL-07: Evidence Cost change approvals, stock adjustment controls, and valuation audit evidence for finance review.

## Audit Trail Requirements

- AUD-01: Store cost version changes with old value, new value, requester, approver, and effective date.
- AUD-02: Record stock adjustment creation, approval, posting, and reversal history.
- AUD-03: Preserve landed cost allocation inputs, basis, reviewer, and timestamp.
- AUD-04: Track subledger-to-GL reconciliation owner/status history.
- AUD-05: Keep valuation report export and sign-off evidence by period.
- AUD-06: Provide reporting for Inventory valuation, cost variance, landed cost, and subledger-to-GL summary.
- AUD-07: Evidence Cost change approvals, stock adjustment controls, and valuation audit evidence for finance review.

## User Stories

- As a cost accountant, I want cost variance exceptions by SKU so that material valuation issues are reviewed.
- As a finance manager, I want inventory subledger-to-GL reconciliation so that balance sheet inventory is supported.
- As an operations manager, I want stock adjustments routed for approval so that shrinkage and corrections are controlled.
- As a controller, I want standard cost change history so that margin movements can be explained.
- As an auditor, I want landed cost allocation evidence so that inventory valuation assumptions are traceable.

## UAT Test Cases

- **UAT-01:** Standard cost is changed for a material SKU. Expected result: Old value, new value, reason, requester, approver, and effective date are recorded.
- **UAT-02:** Inventory subledger does not match the GL control account. Expected result: A reconciliation difference is created with owner, amount, and reason fields.
- **UAT-03:** Landed cost allocation is posted. Expected result: Allocation basis, source charge, receipt reference, and reviewer evidence are stored.
- **UAT-04:** Stock adjustment exceeds approval threshold. Expected result: Posting is blocked until reviewer sign-off is captured.
- **UAT-05:** Cost variance exceeds materiality threshold. Expected result: The variance appears in the costing exception report with owner and category.
- **UAT-06:** Inventory valuation pack is exported. Expected result: The pack includes valuation, variances, adjustments, landed costs, and GL reconciliation status.

## Acceptance Criteria

- Inventory valuation reports show SKU, location, quantity, unit cost, value, and cost method.
- Standard cost changes and costing method changes are approved and auditable.
- Stock adjustments cannot post without reason code and approval where required.
- Subledger-to-GL differences are owner-assigned and visible by period.
- Landed cost allocation evidence is retained with basis and reviewer sign-off.

## Implementation Risks and Dependencies

- Item master data and warehouse locations may need cleanup before reliable valuation reporting.
- Approved costing method and standard cost policy must be confirmed.
- Landed cost source data may depend on procurement and logistics integration.
- Historic stock adjustments may require review before migration.
- Operations and finance ownership of variance resolution must be agreed.

## Implementation Notes

- Confirm Inventory Costing process owner and reviewer roles before design sign-off.
- Validate the required data fields against SAP Business One configuration.
- Run UAT with synthetic examples before loading production data.
- Keep any future AI-assisted drafting behind structured templates and human approval.
