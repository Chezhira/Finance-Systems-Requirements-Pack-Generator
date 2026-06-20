from __future__ import annotations

from pathlib import Path

from finance_requirements_generator.schemas import (
    ImplementationReadinessPack,
    OpenDecision,
    ReadinessCheck,
    WorkshopQuestion,
)


def pack_to_readiness_markdown(pack: ImplementationReadinessPack) -> str:
    lines = [
        f"# {pack.process_name} Implementation Readiness Pack",
        "",
        f"**Prepared for:** {pack.company_name}",
        "",
        f"**Target system:** {pack.target_system}",
        "",
        "## Readiness Summary",
        "",
        pack.readiness_summary,
        "",
    ]
    _append_check_section(
        lines,
        "Process Implementation Checklist",
        pack.process_implementation_checklist,
    )
    _append_check_section(
        lines,
        "Target-System Readiness",
        pack.target_system_readiness_checklist,
    )
    _append_check_section(lines, "Data Readiness", pack.data_readiness_checklist)
    _append_check_section(
        lines,
        "Controls and UAT Readiness",
        pack.controls_and_uat_readiness_checklist,
    )
    _append_workshop_section(lines, pack.configuration_workshop_questions)
    _append_check_section(lines, "Cutover Readiness", pack.cutover_readiness_notes)
    _append_decisions_section(lines, pack.open_decisions_and_dependencies)
    _append_traceability(lines, pack)
    lines.extend(
        [
            "## Public-Safe Sample Data Note",
            "",
            pack.public_safe_sample_data_note,
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def export_readiness_markdown(
    pack: ImplementationReadinessPack,
    output_path: str | Path,
) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(pack_to_readiness_markdown(pack), encoding="utf-8")
    return path


def _append_check_section(
    lines: list[str],
    title: str,
    checks: list[ReadinessCheck],
) -> None:
    lines.extend(
        [
            f"## {title}",
            "",
            "| ID | Finance-Specific Check | Evidence Required | Suggested Owner | "
            "Status | Source References | Validation Note |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in checks:
        lines.append(
            "| "
            f"{item.check_id} | {_cell(item.finance_specific_check)} | "
            f"{_cell(item.evidence_required)} | {_cell(item.suggested_owner_role)} | "
            f"{item.review_status} | {', '.join(item.source_references)} | "
            f"{_cell(item.validation_note)} |"
        )
    lines.append("")


def _append_workshop_section(lines: list[str], items: list[WorkshopQuestion]) -> None:
    lines.extend(
        [
            "## Configuration Workshop Questions",
            "",
            "| ID | Question | Implementation Relevance | Source References |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in items:
        lines.append(
            "| "
            f"{item.question_id} | {_cell(item.question)} | "
            f"{_cell(item.implementation_relevance)} | "
            f"{', '.join(item.source_references)} |"
        )
    lines.append("")


def _append_decisions_section(lines: list[str], items: list[OpenDecision]) -> None:
    lines.extend(
        [
            "## Open Decisions and Dependencies",
            "",
            "| ID | Decision Required | Dependency or Impact | Suggested Owner | "
            "Source References |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in items:
        lines.append(
            "| "
            f"{item.decision_id} | {_cell(item.decision_required)} | "
            f"{_cell(item.dependency_or_impact)} | "
            f"{_cell(item.suggested_decision_owner)} | "
            f"{', '.join(item.source_references)} |"
        )
    lines.append("")


def _append_traceability(lines: list[str], pack: ImplementationReadinessPack) -> None:
    lines.extend(
        [
            "## Source Traceability",
            "",
            "| Readiness Item | Source References |",
            "| --- | --- |",
        ]
    )
    for item_id, references in _traceability_rows(pack):
        lines.append(f"| {item_id} | {', '.join(references)} |")
    lines.append("")


def _traceability_rows(pack: ImplementationReadinessPack) -> list[tuple[str, list[str]]]:
    rows: list[tuple[str, list[str]]] = []
    for group in (
        pack.process_implementation_checklist,
        pack.target_system_readiness_checklist,
        pack.data_readiness_checklist,
        pack.controls_and_uat_readiness_checklist,
        pack.cutover_readiness_notes,
    ):
        rows.extend((item.check_id, item.source_references) for item in group)
    rows.extend(
        (item.question_id, item.source_references)
        for item in pack.configuration_workshop_questions
    )
    rows.extend(
        (item.decision_id, item.source_references)
        for item in pack.open_decisions_and_dependencies
    )
    return rows


def _cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
