from io import BytesIO
from zipfile import ZipFile

from docx import Document

from finance_requirements_generator.exports import (
    export_docx,
    export_markdown,
    pack_to_docx_bytes,
    pack_to_markdown,
)
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.template_engine import generate_pack


def test_markdown_export_contains_key_headings(tmp_path) -> None:
    for process_key, intake in DEFAULT_SAMPLE_INPUTS.items():
        pack = generate_pack(intake)
        output_path = export_markdown(pack, tmp_path / f"{process_key}_pack.md")

        content = output_path.read_text(encoding="utf-8")
        assert f"# {pack.process_name} Requirements Pack" in content
        assert "## Functional Requirements" in content
        assert "## UAT Test Cases" in content
        assert pack_to_markdown(pack) == content


def test_markdown_export_leads_with_business_problem_not_sample_note() -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["accounts_payable"])
    content = pack_to_markdown(pack)
    top_block = "\n".join(content.splitlines()[:12]).lower()

    assert "## business problem" in content.lower()
    assert "## reporting requirements" in content.lower()
    assert "## public-safe sample data note" in content.lower()
    assert "synthetic" not in top_block
    assert "fictional" not in top_block
    assert content.index("## Reporting Requirements") < content.index("## Audit Trail Requirements")
    assert content.index("## Public-Safe Sample Data Note") > content.index(
        "## Implementation Notes"
    )


def test_docx_export_contains_key_headings(tmp_path) -> None:
    for process_key, intake in DEFAULT_SAMPLE_INPUTS.items():
        pack = generate_pack(intake)
        output_path = export_docx(pack, tmp_path / f"{process_key}_pack.docx")

        document = Document(output_path)
        text = "\n".join(paragraph.text for paragraph in document.paragraphs)
        assert pack.process_name in text
        assert "Requirements Pack" in text
        assert "Functional Requirements" in text
        assert "Reporting Requirements" in text
        assert "Public-Safe Sample Data Note" in text
        assert "UAT Test Cases" in text


def test_docx_export_uses_cover_contents_tables_and_limited_page_breaks(tmp_path) -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["accounts_payable"])
    output_path = export_docx(pack, tmp_path / "ap_pack.docx")
    document = Document(output_path)
    text = "\n".join(paragraph.text for paragraph in document.paragraphs)

    with ZipFile(output_path) as archive:
        xml = archive.read("word/document.xml").decode("utf-8")
        header_footer_parts = [
            item
            for item in archive.namelist()
            if item.startswith("word/header") or item.startswith("word/footer")
        ]

    assert "FINANCE / ERP IMPLEMENTATION" in text
    assert "Prepared for" in document.tables[0].cell(0, 0).text
    assert "Prepared by" in document.tables[0].cell(1, 0).text
    assert "Chez Solutions" in document.tables[0].cell(1, 1).text
    assert "Contents" in text
    assert len(document.tables) >= 10
    assert xml.count('w:type="page"') == 2
    assert header_footer_parts
    assert document.paragraphs[-1].text.startswith(
        "This pack was generated from fictional, public-safe sample inputs."
    )


def test_docx_download_bytes_open_as_word_document() -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["payroll_controls"])
    content = pack_to_docx_bytes(pack)
    document = Document(BytesIO(content))
    text = "\n".join(paragraph.text for paragraph in document.paragraphs)

    assert content.startswith(b"PK")
    assert "Payroll Controls" in text
