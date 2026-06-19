from __future__ import annotations

from io import BytesIO
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Inches, Pt

from finance_requirements_generator.exports.markdown import SECTION_TITLES
from finance_requirements_generator.schemas import RequirementsPack, UATTestCase


def pack_to_docx_bytes(pack: RequirementsPack) -> bytes:
    document = _build_document(pack)
    buffer = BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def export_docx(pack: RequirementsPack, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    _build_document(pack).save(path)
    return path


def _build_document(pack: RequirementsPack) -> Document:
    document = Document()
    _configure_document(document)
    document.add_heading(f"{pack.process_name} Requirements Pack", level=0)
    document.add_paragraph(f"Prepared for: {pack.company_name}")
    purpose = document.add_paragraph()
    purpose.add_run("Purpose: ").bold = True
    purpose.add_run(
        "Translate finance process pain points into implementation-ready ERP "
        "requirements, controls, reporting needs, audit trail expectations, and UAT coverage."
    )

    for field_name, title in SECTION_TITLES.items():
        document.add_heading(title, level=1)
        _add_value(document, getattr(pack, field_name))
        if title == "Stakeholders and Roles":
            document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    return document


def _configure_document(document: Document) -> None:
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

    styles = document.styles
    styles["Normal"].font.name = "Arial"
    styles["Normal"].font.size = Pt(10)
    for style_name, size in [("Title", 20), ("Heading 1", 14), ("Heading 2", 12)]:
        styles[style_name].font.name = "Arial"
        styles[style_name].font.size = Pt(size)


def _add_value(document: Document, value: object) -> None:
    if isinstance(value, str):
        document.add_paragraph(value)
        return

    if isinstance(value, list) and value and isinstance(value[0], UATTestCase):
        for case in value:
            paragraph = document.add_paragraph(style="List Bullet")
            paragraph.add_run(f"{case.test_id}: ").bold = True
            paragraph.add_run(f"{case.scenario} Expected result: {case.expected_result}")
        return

    if isinstance(value, list):
        for item in value:
            document.add_paragraph(str(item), style="List Bullet")
        return

    document.add_paragraph(str(value))
