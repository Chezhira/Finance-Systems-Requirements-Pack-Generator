# Demo Notes

This repository demonstrates how structured finance intake can become implementation-ready requirements for ERP and finance transformation work.

## Demo flow

1. Open the Streamlit app.
2. Select one of the eight supported finance processes.
3. Choose an intake mode: manual intake, SOP upload, or guided SOP builder.
4. Select a target ERP/system if candidate fit-gap mapping is useful.
5. Review the editable intake fields before generating the pack.
6. Generate the pack and inspect the expandable sections.
7. Preview the Mermaid process map and control-risk matrix.
8. Download Markdown, DOCX, CSV, or XLSX outputs.

## What to look for

- Finance-specific requirements rather than generic project wording.
- Controls, audit trail needs, user stories, UAT cases, and acceptance criteria in every pack.
- Process coverage across AP, AR, bank reconciliation, VAT, close, inventory costing, intercompany, and payroll controls.
- SOP upload support for TXT, Markdown, and DOCX workflow notes.
- Guided SOP builder support for teams that do not have a documented SOP yet.
- Curated target-system mapping notes that use repository data only.
- Mermaid process map output for process documentation.
- Control-risk matrix export as CSV and XLSX.
- Deterministic output from bundled templates, with no external AI/API calls, no web scraping, and no live web RAG.
- Sample outputs under `examples/generated_packs`.
- Public-safe examples that use fictional company names and no operational business data.

## v0.4.0 review direction

The v0.3.0 flow supports users with SOPs and users without SOPs. The intake does not assume a workflow document already exists.

- Upload SOP / workflow document: extract current-state process details into editable intake fields before pack generation.
- Build SOP from guided finance process questions: generate a reviewable current-state SOP draft, then use that approved draft to generate the requirements pack.
- Continue using manual requirements intake: preserve the current structured intake path for users who already know the fields they want to provide.

Target-system mapping should ask the user to select the ERP or finance system, use curated capability mappings stored in the repository, and generate candidate fit-gap notes for review. The app should not use live web RAG, scrape ERP vendor websites, call external AI/APIs, or claim that any ERP capability is guaranteed.

The v0.4.0 outputs add visual process documentation and control-risk exports without changing that deterministic posture. Review the Mermaid text, Word-friendly process-map summary, CSV matrix, and XLSX matrix as implementation-preparation artefacts.
