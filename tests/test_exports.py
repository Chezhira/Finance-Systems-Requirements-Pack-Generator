from docx import Document

from finance_requirements_generator.exports import export_docx, export_markdown, pack_to_markdown
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS
from finance_requirements_generator.template_engine import generate_pack


def test_markdown_export_contains_key_headings(tmp_path) -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["accounts_payable"])
    output_path = export_markdown(pack, tmp_path / "ap_pack.md")

    content = output_path.read_text(encoding="utf-8")
    assert "# Accounts Payable Requirements Pack" in content
    assert "## Functional Requirements" in content
    assert "## UAT Test Cases" in content
    assert "Duplicate invoice" in content
    assert pack_to_markdown(pack) == content


def test_docx_export_contains_key_headings(tmp_path) -> None:
    pack = generate_pack(DEFAULT_SAMPLE_INPUTS["vat_reconciliation"])
    output_path = export_docx(pack, tmp_path / "vat_pack.docx")

    document = Document(output_path)
    text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    assert "VAT Reconciliation Requirements Pack" in text
    assert "Functional Requirements" in text
    assert "VAT return boxes" in text
