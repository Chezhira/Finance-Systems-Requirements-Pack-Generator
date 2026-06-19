# Finance Systems Requirements Pack Generator

![CI](https://github.com/Chezhira/Finance-Systems-Requirements-Pack-Generator/actions/workflows/ci.yml/badge.svg)

A Streamlit application that turns finance process knowledge into implementation-ready requirements packs for ERP, finance systems, and finance transformation work.

Finance systems projects often fail because requirements are vague, controls are undocumented, data needs are unclear, process ownership is not agreed, and UAT expectations are defined too late. This project addresses that gap by converting structured finance intake, SOP/workflow documentation, and guided process discovery into practical requirements packs that finance and systems teams can review before configuration, automation, reporting, migration, or implementation work begins.

The app generates BRD-style outputs covering current-state problems, future-state scope, functional requirements, controls, audit trail needs, reporting requirements, user stories, UAT test cases, acceptance criteria, implementation risks, current-state SOP drafts, and optional target-system fit-gap mapping.

![Streamlit intake preview](docs/screenshots/app-intake-preview.svg)

## What This Project Demonstrates

This project demonstrates practical finance systems analysis across the early implementation work that often determines whether an ERP or finance transformation project succeeds.

It shows how finance process knowledge can be converted into:

* Clear implementation requirements
* Defined process scope and boundaries
* Control and audit trail expectations
* Data requirements for configuration and reporting
* UAT scenarios tied to finance risks and process outcomes
* Current-state SOP drafts for process review
* Candidate target-system fit-gap notes for ERP planning
* Polished Markdown and DOCX requirements packs

The project is designed as a public portfolio asset for roles such as:

* Business Systems Analyst
* ERP Functional Consultant
* Finance Systems Analyst
* Finance Transformation Analyst
* Finance Process Owner
* Finance Automation Specialist
* Finance Engineer

## Supported Finance Processes

The v0.4.0 build supports eight finance processes.

| Process | Coverage |
| --- | --- |
| Accounts Payable | Duplicate invoices, supplier invoice intake, three-way match readiness, approval routing, supplier master data controls, payment evidence, and segregation of duties |
| Bank Reconciliation | Unmatched receipts and payments, ageing, owner/status tracking, suspense clearing, reconciliation evidence, reviewer sign-off, and audit trail requirements |
| VAT Reconciliation | Source registers, VAT return boxes, GL VAT control accounts, reconciling differences, filing evidence, audit trail, and review controls |
| Accounts Receivable | Unallocated receipts, disputed invoices, collections ageing, credit notes, write-offs, customer master controls, and cash allocation evidence |
| Month-end Close | Close task ownership, reconciliation evidence, journal approvals, overdue escalation, reviewer sign-off, close reporting, and period-end readiness |
| Inventory Costing | Valuation differences, standard cost changes, landed cost allocation, stock adjustments, inventory subledger-to-GL reconciliation, and costing controls |
| Intercompany Settlements | Recharge rules, counterparty confirmation, mismatch ageing, FX differences, settlement readiness, elimination support, and intercompany evidence |
| Payroll Controls | Starter, leaver and change approvals, payroll input review, exception handling, payroll register reconciliation, and payment file approval |

## Generated Pack Contents

Each generated requirements pack can include:

* Executive summary
* Current-state business problem
* Future-state process scope
* Scope boundaries
* Stakeholders and roles
* Functional requirements
* Non-functional requirements
* Data requirements
* Controls
* Reporting requirements
* Audit trail requirements
* User stories
* UAT test cases
* Acceptance criteria
* Implementation risks and dependencies
* Implementation notes
* Optional current-state SOP draft
* Optional target-system fit-gap mapping
* Visual process documentation
* Mermaid process map
* Control-risk matrix
* Public-safe sample data note

DOCX packs include a polished cover page, contents page, headers, footers, structured tables, and client-style formatting for review.

![Generated pack preview](docs/screenshots/generated-pack-preview.svg)

## Intake Modes

The app supports three intake modes so users can start from different levels of process maturity.

### 1. Manual Requirements Intake

The manual intake mode uses a structured finance systems questionnaire.

Users can capture:

* Process area
* Business problem
* Current systems and tools
* User groups and stakeholders
* Pain points
* Data fields
* Control requirements
* Reporting needs
* Audit trail needs
* UAT expectations
* Implementation assumptions

This mode is available for all eight finance processes.

### 2. SOP / Workflow Upload

Users can upload an existing SOP or workflow document in TXT, Markdown, or DOCX format.

The app extracts plain text from the uploaded document and maps current-state process details into editable intake fields before pack generation.

This mode is useful where a finance team already has process notes, SOPs, workflow descriptions, or procedure documents, but those documents are not yet structured for ERP design, finance controls, reporting, audit trail, or UAT planning.

### 3. Guided SOP Builder

Users without an existing SOP can answer guided finance process questions covering:

* Process trigger
* Process owner
* Systems and tools used
* Key process steps
* Approvals
* Handoffs
* Controls
* Exceptions
* Escalations
* Reports
* Evidence
* Data fields
* Pain points
* Desired future-state improvements

The app generates a current-state SOP draft from the guided answers. The reviewed draft can then be used to populate the requirements pack.

## Target-System Fit-Gap Mapping

Users can optionally select a target ERP or finance system.

Supported target-system options include:

* Odoo
* NetSuite
* Microsoft Dynamics 365 Business Central
* Microsoft Dynamics 365 Finance
* SAP Business One
* Xero
* QuickBooks Online
* Generic ERP / Not decided yet

The app uses curated repository mapping data only. It does not scrape the web, call external AI services, or make guaranteed ERP capability claims.

Generated fit-gap outputs are deliberately cautious. They are framed as candidate planning notes and include validation language such as:

* Candidate mapping only
* Requires implementation validation
* Verify against selected edition, modules, localisation, configuration, integrations, and implementation scope

The target-system fit-gap section can include:

| Field | Purpose |
| --- | --- |
| Current-State Area | Finance process area, control point, or workflow concern identified during intake |
| Target-System Capability Area | Candidate system capability area that may support the requirement |
| Candidate Fit-Gap View | Initial view of likely fit, gap, configuration need, or validation concern |
| Requirement Impact | What the implementation team should clarify, configure, document, or test |
| Validation Note | Cautious reminder to validate against edition, modules, localisation, and implementation scope |

## Visual Process Documentation

v0.4.0 adds deterministic process-map output for implementation review.

Each pack includes:

* Mermaid process map text
* Plain-language process-map summary
* Trigger, intake, validation, exception, approval, reporting, evidence, and sign-off flow

The Mermaid output is editable and can be copied into Mermaid-compatible tools for rendering.

## Control-Risk Matrix Export

v0.4.0 also adds a generated control-risk matrix derived from the selected process, pain points, controls, audit trail needs, UAT cases, and implementation risks.

The matrix includes:

* Process area
* Risk area and risk description
* Control objective and control activity
* Control type
* Frequency
* Owner
* Evidence required
* System/data dependency
* Related requirement ID
* Related UAT case
* Residual risk or implementation note

Control type uses practical finance systems labels such as Preventive, Detective, Corrective, Manual, Automated, and Semi-automated.

The matrix can be downloaded as:

* CSV
* XLSX with styled headers, frozen top row, text wrapping, and usable column widths

## Example Outputs

The repository includes generated sample packs for all supported processes.

### Markdown Packs

* [Accounts Payable requirements pack](examples/generated_packs/accounts_payable_requirements_pack.md)
* [Bank Reconciliation requirements pack](examples/generated_packs/bank_reconciliation_requirements_pack.md)
* [VAT Reconciliation requirements pack](examples/generated_packs/vat_reconciliation_requirements_pack.md)
* [Accounts Receivable requirements pack](examples/generated_packs/accounts_receivable_requirements_pack.md)
* [Month-end Close requirements pack](examples/generated_packs/month_end_close_requirements_pack.md)
* [Inventory Costing requirements pack](examples/generated_packs/inventory_costing_requirements_pack.md)
* [Intercompany Settlements requirements pack](examples/generated_packs/intercompany_settlements_requirements_pack.md)
* [Payroll Controls requirements pack](examples/generated_packs/payroll_controls_requirements_pack.md)

### DOCX Packs

DOCX versions are generated by the same deterministic export pipeline and are available in:

```text
examples/generated_packs/
```

### Sample SOPs

Public-safe sample SOPs are included for:

* Accounts Payable
* Month-end Close
* Payroll Controls

They are available in:

```text
examples/sample_sops/
```

## Why This Matters For Finance Transformation

Finance systems projects rarely fail because teams cannot imagine a dashboard. They fail because process ownership, source data, approval evidence, audit trail requirements, exception handling, control design, and UAT expectations were not made specific early enough.

This project focuses on the implementation layer that often gets rushed:

```text
finance process knowledge
-> structured intake
-> clear requirements
-> controls and evidence
-> reporting needs
-> UAT coverage
-> implementation-ready pack
```

The result is a practical bridge between finance operations and finance systems delivery.

## Design Principles

This project is intentionally deterministic, reviewable, and implementation-focused.

It is not an "AI magic" requirements writer. It does not take an unreviewed process document and pretend to produce final implementation truth. Instead, it structures finance process knowledge into editable outputs that finance and systems stakeholders can review, challenge, refine, and validate.

The project does not use:

* External AI/API calls
* Live web RAG
* Web scraping
* Databases
* Authentication
* External integrations
* Real employer, client, supplier, bank, VAT, payroll, HR, customer, or operational data

Target-system mappings are curated planning prompts, not implementation guarantees. Users must validate them against the selected system edition, modules, localisation, configuration, integration landscape, and implementation scope.

## Public-Safe Sample Data

The bundled examples use fictional company names and public-safe sample inputs.

The repository does not contain real employer, client, supplier, bank, VAT, payroll, HR, customer, or operational data.

Do not upload confidential business information into a public demo.

## Technical Overview

The application is built with:

* Python
* Streamlit
* YAML process library
* Structured schemas
* Deterministic template generation
* Markdown export
* DOCX export
* CSV/XLSX control-risk matrix export
* Curated target-system mapping data
* Mermaid process map generation
* Pytest test suite
* Ruff linting
* GitHub Actions CI

The generated packs are built from structured inputs, process-library content, and curated mapping data rather than live external services.

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
streamlit run app.py
```

## Generate Sample Packs

```powershell
python scripts\generate_examples.py --output-dir examples\generated_packs
```

This regenerates the Markdown and DOCX sample packs in:

```text
examples/generated_packs/
```

## Test And Lint

```powershell
python -m ruff check .
python -m pytest
```

GitHub Actions runs ruff, pytest, and a sample generation smoke step on push and pull request.

## Project Structure

```text
app.py
src/finance_requirements_generator/
  questionnaire.py
  schemas.py
  sop_intake.py
  template_engine.py
  text_cleanup.py
  control_risk.py
  process_map.py
  exports/
  process_library/
  system_mapping/
    capabilities.yaml
examples/
  sample_inputs/
  sample_sops/
  generated_packs/
tests/
docs/
  screenshots/
  v0.3.0_intake_and_mapping_plan.md
scripts/
  generate_examples.py
```

## Release History

### v0.1.0 - Requirements Pack MVP

Initial release focused on turning structured finance process intake into implementation-ready requirements packs for Accounts Payable, Bank Reconciliation, and VAT Reconciliation.

The release included the Streamlit intake flow, Markdown and DOCX exports, generated sample packs, tests, linting, screenshots, demo notes, and GitHub Actions CI.

### v0.2.0 - Expanded Finance Process Library

Expanded the process library from three to eight finance processes by adding Accounts Receivable, Month-end Close, Inventory Costing, Intercompany Settlements, and Payroll Controls.

This widened the project from a narrow requirements generator into a broader finance transformation requirements library covering close, reconciliation, controls, working capital, inventory, intercompany, and payroll processes.

### v0.2.1 - Client-Ready Document Outputs

Improved the generated DOCX requirements packs so they are suitable for portfolio review and client-style presentation.

This release strengthened the document experience with polished cover pages, contents pages, headers, footers, structured tables, cleaner pagination, and professional formatting while preserving deterministic exports.

### v0.3.0 - SOP Intake and Target-System Mapping

Added a process discovery layer for users with or without existing SOPs.

The app now supports manual requirements intake, SOP/workflow upload, guided SOP creation, current-state SOP draft generation, and curated target-system fit-gap mapping for ERP and finance systems planning.

This release moves the project from a requirements pack generator into a broader finance systems discovery and implementation-preparation tool.

### v0.4.0 - Visual Process Documentation and Control-Risk Exports

Added deterministic visual process documentation and control-risk export outputs.

The app now generates Mermaid process maps, Word-friendly process-map summaries, control-risk matrix sections, and downloadable CSV/XLSX control-risk matrices for finance systems implementation review.

## Roadmap

### v0.5.0

Planned features:

* Implementation checklist by process
* Target ERP/system readiness checklist
* More detailed configuration planning prompts

### Future Considerations

Potential future work may include AI-assisted drafting, but only with strict schema validation, traceability, and user review.

External AI/API calls, live web scraping, and uncontrolled web RAG are intentionally excluded from the current build.

See [v0.3.0 planning notes](docs/v0.3.0_intake_and_mapping_plan.md) for the SOP upload, guided SOP build, manual intake, and curated target-system mapping approach.
