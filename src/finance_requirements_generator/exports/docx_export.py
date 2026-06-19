from __future__ import annotations

from datetime import date
from io import BytesIO
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

from finance_requirements_generator.exports.markdown import SECTION_TITLES
from finance_requirements_generator.schemas import RequirementsPack, UATTestCase

BODY_SECTION_KEYS = [
    "executive_summary",
    "business_problem",
    "process_scope",
    "in_scope",
    "out_of_scope",
    "stakeholders_and_roles",
    "functional_requirements",
    "data_requirements",
    "controls",
    "reporting_requirements",
    "audit_trail_requirements",
    "user_stories",
    "uat_test_cases",
    "acceptance_criteria",
    "risks_and_dependencies",
    "implementation_notes",
    "public_safe_sample_data_note",
]


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
    _add_cover_page(document, pack)
    document.add_page_break()
    _add_body_section(document, pack)
    _add_header_footer(document, pack)
    _add_contents_page(document, pack)
    document.add_page_break()
    _add_pack_sections(document, pack)
    return document


def _configure_document(document: Document) -> None:
    section = document.sections[0]
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)
    section.header_distance = Inches(0.25)
    section.footer_distance = Inches(0.25)

    styles = document.styles
    styles["Normal"].font.name = "Arial"
    styles["Normal"].font.size = Pt(9)
    styles["Normal"].paragraph_format.space_after = Pt(4)
    styles["Normal"].paragraph_format.line_spacing = 1.05

    for style_name, size, color in [
        ("Title", 22, RGBColor(31, 41, 55)),
        ("Heading 1", 13, RGBColor(30, 64, 175)),
        ("Heading 2", 11, RGBColor(31, 41, 55)),
    ]:
        styles[style_name].font.name = "Arial"
        styles[style_name].font.size = Pt(size)
        styles[style_name].font.color.rgb = color
        styles[style_name].paragraph_format.space_before = Pt(6)
        styles[style_name].paragraph_format.space_after = Pt(4)


def _add_cover_page(document: Document, pack: RequirementsPack) -> None:
    _add_label(document, "FINANCE / ERP IMPLEMENTATION")
    title = document.add_paragraph()
    title.style = document.styles["Title"]
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run(f"{pack.process_name}\nRequirements Pack").bold = True

    meta = document.add_table(rows=5, cols=2)
    _style_table(meta)
    rows = [
        ("Prepared for", pack.company_name),
        ("Prepared by", "Chez Solutions"),
        ("Date", date.today().strftime("%d %B %Y")),
        ("Status", "Draft for Review"),
        ("Document type", "Finance systems requirements pack"),
    ]
    for row, (label, value) in zip(meta.rows, rows, strict=True):
        row.cells[0].text = label
        row.cells[1].text = value
        _shade_cell(row.cells[0], "E5E7EB")
        _bold_cell(row.cells[0])

    document.add_paragraph()
    stats = document.add_table(rows=1, cols=5)
    stats.alignment = WD_TABLE_ALIGNMENT.CENTER
    stat_values = [
        ("Volume", pack_volume(pack)),
        ("Delivery", _extract_delivery_window(pack)),
        ("Functional", str(len(pack.functional_requirements))),
        ("Controls", str(len(pack.controls))),
        ("UAT Cases", str(len(pack.uat_test_cases))),
    ]
    for cell, (label, value) in zip(stats.rows[0].cells, stat_values, strict=True):
        _shade_cell(cell, "EFF6FF")
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.text = ""
        label_para = cell.paragraphs[0]
        label_run = label_para.add_run(label.upper())
        label_run.bold = True
        label_run.font.size = Pt(7)
        label_run.font.color.rgb = RGBColor(30, 64, 175)
        value_para = cell.add_paragraph()
        value_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        value_run = value_para.add_run(value)
        value_run.bold = True
        value_run.font.size = Pt(9)

    document.add_paragraph()
    _add_heading_like(document, "PURPOSE", level=2)
    document.add_paragraph(
        "Translate finance process pain points into implementation-ready ERP requirements "
        "covering workflow, data, controls, reporting, audit trail, and UAT coverage."
    )


def _add_body_section(document: Document, pack: RequirementsPack) -> None:
    section = document.add_section(WD_SECTION.CONTINUOUS)
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)
    section.header_distance = Inches(0.25)
    section.footer_distance = Inches(0.25)
    section.different_first_page_header_footer = False
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    _add_header_footer(document, pack, section=section)


def _add_header_footer(
    document: Document,
    pack: RequirementsPack,
    section=None,
) -> None:
    target = section or document.sections[-1]
    header = target.header
    header.paragraphs[0].text = f"{pack.process_name} Requirements Pack | {pack.company_name}"
    header.paragraphs[0].style = document.styles["Normal"]
    header.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    footer = target.footer
    paragraph = footer.paragraphs[0]
    paragraph.clear()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run("Chez Solutions | Public-safe sample document | Page ")
    _add_page_number(paragraph)


def _add_contents_page(document: Document, pack: RequirementsPack) -> None:
    _add_heading_like(document, "Contents", level=1, numbered=False)
    contents = document.add_table(rows=len(BODY_SECTION_KEYS), cols=2)
    _style_table(contents)
    for index, field_name in enumerate(BODY_SECTION_KEYS, start=1):
        row = contents.rows[index - 1]
        row.cells[0].text = f"{index:02d}"
        row.cells[1].text = SECTION_TITLES[field_name]
        _bold_cell(row.cells[0])
        _shade_cell(row.cells[0], "EFF6FF")


def _add_pack_sections(document: Document, pack: RequirementsPack) -> None:
    for index, field_name in enumerate(BODY_SECTION_KEYS, start=1):
        title = SECTION_TITLES[field_name]
        _add_heading_like(document, f"{index:02d}  {title}", level=1)
        value = getattr(pack, field_name)
        _add_section_value(document, field_name, value)


def _add_section_value(document: Document, field_name: str, value: object) -> None:
    if isinstance(value, str):
        document.add_paragraph(value)
        return

    if field_name in {
        "in_scope",
        "out_of_scope",
        "acceptance_criteria",
        "risks_and_dependencies",
        "implementation_notes",
    }:
        _add_bullet_list(document, value)
        return

    if field_name == "stakeholders_and_roles":
        _add_two_column_table(document, ["Role", "Responsibility"], value)
        return

    if field_name in {
        "data_requirements",
        "controls",
        "reporting_requirements",
        "audit_trail_requirements",
    }:
        _add_two_column_table(document, ["ID", "Requirement"], value)
        return

    if field_name == "functional_requirements":
        _add_two_column_table(document, ["ID", "Functional Requirement"], value)
        return

    if field_name == "user_stories":
        _add_two_column_table(document, ["Story", "User Need"], value, numbered=True)
        return

    if field_name == "uat_test_cases":
        _add_uat_table(document, value)
        return

    if isinstance(value, list):
        _add_bullet_list(document, value)
        return

    document.add_paragraph(str(value))


def _add_two_column_table(
    document: Document,
    headers: list[str],
    items: list[str],
    numbered: bool = False,
) -> None:
    table = document.add_table(rows=1, cols=2)
    _style_table(table)
    _set_header_row(table.rows[0], headers)
    for index, item in enumerate(items, start=1):
        left, right = _split_identifier(item, fallback=f"{index:02d}" if numbered else "")
        row = table.add_row()
        row.cells[0].text = left
        row.cells[1].text = right


def _add_uat_table(document: Document, cases: list[UATTestCase]) -> None:
    table = document.add_table(rows=1, cols=3)
    _style_table(table)
    _set_header_row(table.rows[0], ["Test ID", "Scenario", "Expected Result"])
    for case in cases:
        row = table.add_row()
        row.cells[0].text = case.test_id
        row.cells[1].text = case.scenario
        row.cells[2].text = case.expected_result


def _add_bullet_list(document: Document, items: list[str]) -> None:
    for item in items:
        paragraph = document.add_paragraph(style="List Bullet")
        paragraph.paragraph_format.space_after = Pt(2)
        paragraph.add_run(str(item))


def _add_heading_like(
    document: Document,
    text: str,
    level: int,
    numbered: bool = True,
) -> None:
    paragraph = document.add_heading(level=level)
    paragraph.text = text if numbered else text
    paragraph.paragraph_format.keep_with_next = True


def _add_label(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(text)
    run.bold = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(30, 64, 175)


def _style_table(table) -> None:
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    for row in table.rows:
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.line_spacing = 1.0


def _set_header_row(row, headers: list[str]) -> None:
    for cell, header in zip(row.cells, headers, strict=True):
        cell.text = header
        _shade_cell(cell, "DBEAFE")
        _bold_cell(cell)


def _shade_cell(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), fill)
    tc_pr.append(shading)


def _bold_cell(cell) -> None:
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.bold = True


def _split_identifier(item: str, fallback: str) -> tuple[str, str]:
    if ": " in item:
        left, right = item.split(": ", 1)
        return left, right
    return fallback, item


def _add_page_number(paragraph) -> None:
    run = paragraph.add_run()
    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")
    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = "PAGE"
    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_char_begin)
    run._r.append(instr_text)
    run._r.append(fld_char_end)


def pack_volume(pack: RequirementsPack) -> str:
    for line in pack.executive_summary.split(". "):
        marker = "It is sized for "
        if marker in line:
            return line.split(marker, 1)[1].split(" and frames", 1)[0]
    return "Defined in intake"


def _extract_delivery_window(pack: RequirementsPack) -> str:
    marker = "target delivery window of "
    if marker in pack.executive_summary:
        return pack.executive_summary.split(marker, 1)[1].rstrip(".")
    return "Draft"
