# Demo Notes

This repository demonstrates how structured finance intake can become implementation-ready requirements for ERP and finance transformation work.

## Demo flow

1. Open the Streamlit app.
2. Select one of the eight supported finance processes.
3. Review the pre-filled public-safe sample intake.
4. Generate the pack and inspect the expandable sections.
5. Download Markdown or DOCX.

## What to look for

- Finance-specific requirements rather than generic project wording.
- Controls, audit trail needs, user stories, UAT cases, and acceptance criteria in every pack.
- Process coverage across AP, AR, bank reconciliation, VAT, close, inventory costing, intercompany, and payroll controls.
- Deterministic output from bundled templates, with no AI/API call in the MVP.
- Sample outputs under `examples/generated_packs`.
- Public-safe examples that use fictional company names and no operational business data.

## v0.3.0 planning direction

The next planned release should support users with SOPs and users without SOPs. The intake should not assume a workflow document already exists.

- Upload SOP / workflow document: extract current-state process details into editable intake fields before pack generation.
- Build SOP from guided finance process questions: generate a reviewable current-state SOP draft, then use that approved draft to generate the requirements pack.
- Continue using manual requirements intake: preserve the current structured intake path for users who already know the fields they want to provide.

Target-system mapping should ask the user to select the ERP or finance system, use curated capability mappings stored in the repository, and generate candidate fit-gap notes for review. The app should not use live web RAG, scrape ERP vendor websites, call external AI/APIs, or claim that any ERP capability is guaranteed.
