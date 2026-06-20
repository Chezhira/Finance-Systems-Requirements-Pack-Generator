# Finance Systems Requirements Pack Generator

[![CI](https://github.com/Chezhira/Finance-Systems-Requirements-Pack-Generator/actions/workflows/ci.yml/badge.svg)](https://github.com/Chezhira/Finance-Systems-Requirements-Pack-Generator/actions/workflows/ci.yml)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://finance-systems-requirements-pack-generator.streamlit.app/)
![Version](https://img.shields.io/github/v/tag/Chezhira/Finance-Systems-Requirements-Pack-Generator?label=version)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-cloud-ff4b4b)
![Ruff](https://img.shields.io/badge/lint-ruff-46a2f1)
![Pytest](https://img.shields.io/badge/tests-pytest-0a7f3f)
![Deterministic](https://img.shields.io/badge/design-deterministic-0e7c66)
![No External AI/API](https://img.shields.io/badge/external_AI%2FAPI-none-142238)

**Live demo:** [Finance Systems Requirements Pack Generator](https://finance-systems-requirements-pack-generator.streamlit.app/)

A deployed Streamlit application that turns finance process knowledge into implementation-ready ERP and finance transformation artefacts.

Finance systems projects often fail because requirements are vague, controls are undocumented, data needs are unclear, process ownership is not agreed, and UAT expectations are defined too late. This project addresses that gap by converting structured finance intake, SOP/workflow documentation, and guided process discovery into reviewable requirements packs, control-risk matrices, process-flow documentation, and implementation-readiness packs.

The v0.5.1 build supports the full implementation-preparation flow and adds explicit quality gates for generated finance artefacts:

```text
finance process knowledge
-> structured intake
-> requirements pack
-> SOP draft
-> target-system fit-gap mapping
-> control-risk matrix
-> visual process flow
-> implementation readiness pack
```

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
* Deterministic browser-viewable finance process flows
* Traceable CSV/XLSX control-risk matrices
* Finance-process-specific implementation readiness checks
* Polished Markdown and DOCX requirements and readiness packs

The project is designed as a public portfolio asset for roles such as:

* Business Systems Analyst
* ERP Functional Consultant
* Finance Systems Analyst
* Finance Transformation Analyst
* Finance Process Owner
* Finance Automation Specialist
* Finance Engineer

## Supported Finance Processes

The v0.5.1 build supports eight finance processes.

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

## Generated Artefacts

The app produces a coordinated set of reviewable finance systems artefacts:

| Artefact | Format and purpose |
| --- | --- |
| Requirements Pack | Markdown and professionally formatted DOCX covering scope, requirements, controls, reporting, audit trail, UAT, acceptance criteria, and implementation dependencies |
| Current-State SOP Draft | Editable process draft generated from uploaded workflow content or guided finance process discovery |
| Target-System Fit-Gap Mapping | Candidate capability mapping with requirement impacts and explicit implementation-validation notes |
| Browser-Viewable Process Flow | Deterministic HTML/CSS control flow that opens directly in a browser for finance and implementation review |
| Mermaid Source | Secondary technical output for users who need the process-map source |
| Control-Risk Matrix | CSV and styled XLSX with requirement and UAT traceability |
| Implementation Readiness Pack | Separate Markdown and DOCX pack covering evidence checks, workshop questions, cutover considerations, and open decisions |

### Requirements Pack Contents

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

The primary process-map output is a deterministic HTML/CSS finance control flow designed for implementation review by technical and non-technical stakeholders.

Each pack includes:

* Browser-viewable HTML process map for non-technical reviewers
* Plain-language process-map summary
* Trigger, intake, validation, exception, approval, reporting, evidence, and sign-off flow
* Mermaid source as a secondary technical output

The HTML process map opens directly in a browser and does not depend on Mermaid runtime rendering for the primary visual. It uses deterministic HTML/CSS nodes and connectors, supports print review, and keeps Mermaid source secondary inside a closed advanced section and a separate technical download.

The app does not call external APIs, scrape the web, or use live web RAG during export generation.

## Control-Risk Matrix Export

The generated control-risk matrix is derived from the selected process, pain points, controls, audit trail needs, UAT cases, and implementation risks.

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

This keeps risks and controls editable while preserving traceability to the requirements and UAT coverage that support implementation review.

## Finance Systems Implementation Readiness Pack

v0.5.0 adds a separate implementation-readiness layer after requirements, process discovery, controls, fit-gap mapping, and visual process documentation. Keeping readiness separate avoids bloating the core requirements pack with project-management content.

The readiness pack helps finance and implementation teams review whether a process is ready to configure, test, migrate, and implement. It includes:

* Process implementation checklist
* Target-system readiness checklist
* Data readiness checklist
* Controls and UAT readiness checklist
* Configuration workshop questions
* Cutover/readiness notes
* Open decisions and dependencies
* Source traceability back to requirements, controls, reporting, audit, UAT, risks, fit-gap rows, and control-risk rows

Every checklist item starts as `Not assessed`. The pack does not calculate readiness scores or introduce schedules, budgets, task boards, or project dashboards. Target-system checks remain candidate planning prompts that require validation against the selected edition, modules, localisation, configuration, integrations, and implementation scope.

Readiness packs can be downloaded as Markdown or professionally formatted DOCX files.

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

### Representative Implementation Readiness Packs

* [Accounts Payable readiness pack](examples/generated_packs/accounts_payable_implementation_readiness_pack.md)
* [Month-end Close readiness pack](examples/generated_packs/month_end_close_implementation_readiness_pack.md)
* [Payroll Controls readiness pack](examples/generated_packs/payroll_controls_implementation_readiness_pack.md)

### Representative Process Maps And Control-Risk Matrices

* [Accounts Payable browser-viewable process map](examples/generated_packs/accounts_payable_process_map.html)
* [Month-end Close browser-viewable process map](examples/generated_packs/month_end_close_process_map.html)
* [Payroll Controls browser-viewable process map](examples/generated_packs/payroll_controls_process_map.html)
* [Accounts Payable control-risk matrix](examples/generated_packs/accounts_payable_control_risk_matrix.csv)
* [Month-end Close control-risk matrix](examples/generated_packs/month_end_close_control_risk_matrix.xlsx)
* [Payroll Controls control-risk matrix](examples/generated_packs/payroll_controls_control_risk_matrix.xlsx)

### Sample SOPs

Public-safe sample SOPs are included for:

* Accounts Payable
* Month-end Close
* Payroll Controls

They are available in:

```text
examples/sample_sops/
```

## Live Deployment

The app is deployed on Streamlit Cloud:

[https://finance-systems-requirements-pack-generator.streamlit.app/](https://finance-systems-requirements-pack-generator.streamlit.app/)

The live deployment is intended for public-safe portfolio demonstration. Use fictional or non-confidential inputs only. Do not upload employer, client, supplier, bank, VAT, payroll, HR, customer, or operational data into the public app.

## Why This Matters For Finance Transformation

Finance systems projects rarely fail because teams cannot imagine a dashboard. They fail because process ownership, source data, approval evidence, audit trail requirements, exception handling, control design, and UAT expectations were not made specific early enough.

This project focuses on the implementation layer that often gets rushed:

```text
finance process knowledge
-> structured intake
-> requirements pack
-> SOP draft
-> target-system fit-gap mapping
-> controls, evidence, and UAT coverage
-> visual process documentation
-> implementation readiness pack
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

## Evaluation and Quality Gates

The project includes a lightweight pytest-based eval layer that checks generated finance artefacts for structure completeness, ID uniqueness, traceability, control coverage, readiness completeness, export integrity, public-safe content, and deterministic behaviour without external services. This makes the generator not only deterministic, but evaluable.

Run the finance artefact evaluations with:

```powershell
python scripts\run_evals.py
```

The evals cover all eight supported finance processes, both selected and unselected target-system readiness paths, and representative Markdown, DOCX, CSV, XLSX, HTML, and Mermaid outputs.

## Public-Safe Sample Data

The bundled examples use fictional company names and public-safe sample inputs.

The repository does not contain real employer, client, supplier, bank, VAT, payroll, HR, customer, or operational data.

The live app is intended for public-safe portfolio demonstration only. Do not upload confidential business information into the public deployment.

## Technical Overview

The application is built with:

* Python
* Streamlit and Streamlit Cloud deployment
* YAML process library
* Structured schemas
* Deterministic template generation
* Markdown export
* DOCX export
* CSV/XLSX control-risk matrix export
* Curated target-system mapping data
* Deterministic browser-viewable HTML/CSS process-flow export
* Mermaid source generation as a secondary technical output
* Markdown/DOCX implementation readiness pack export
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

This regenerates the requirements packs, representative readiness packs, control-risk matrices, and browser-viewable process maps in:

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
.streamlit/
  config.toml
app.py
src/finance_requirements_generator/
  questionnaire.py
  readiness_engine.py
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
  evals/
    eval_helpers.py
    test_pack_structure_eval.py
    test_traceability_eval.py
    test_control_coverage_eval.py
    test_readiness_eval.py
    test_export_integrity_eval.py
docs/
  screenshots/
  v0.3.0_intake_and_mapping_plan.md
scripts/
  generate_examples.py
  run_evals.py
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

The app now generates styled browser-viewable process maps, editable Mermaid source, Word-friendly process-map summaries, control-risk matrix sections, and downloadable CSV/XLSX control-risk matrices for finance systems implementation review.

### v0.5.0 - Finance Systems Implementation Readiness Pack

Added a separate readiness pack derived from requirements, process templates, data needs, controls, reporting, audit requirements, UAT cases, fit-gap mapping, control-risk rows, and implementation dependencies.

The release adds finance-process-specific implementation, target-system, data, controls/UAT, workshop, cutover, and open-decision outputs with source traceability and Markdown/DOCX downloads.

### v0.5.1 - Evaluation and Finance Artefact Quality Gates

Added pytest-based evaluations for requirements structure, ID uniqueness, traceability, control coverage, readiness completeness, export integrity, public-safe content, and deterministic generation across all supported finance processes.

## Roadmap

### Future Considerations

Potential future work may include AI-assisted drafting, but only with strict schema validation, traceability, and human review.

External AI/API calls, live web scraping, and uncontrolled web RAG are intentionally excluded from the current build.

See [v0.3.0 planning notes](docs/v0.3.0_intake_and_mapping_plan.md) for the SOP upload, guided SOP build, manual intake, and curated target-system mapping approach.
