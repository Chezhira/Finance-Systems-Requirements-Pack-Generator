from __future__ import annotations

from io import BytesIO
from pathlib import Path

from docx import Document

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
    document.add_heading(f"{pack.process_name} Requirements Pack", level=0)
    document.add_paragraph(f"Synthetic company: {pack.company_name}")
    document.add_paragraph(
        "Synthetic demo output only. Do not use this sample as client, employer, "
        "or operational data."
    )

    for field_name, title in SECTION_TITLES.items():
        document.add_heading(title, level=1)
        _add_value(document, getattr(pack, field_name))

    return document


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
