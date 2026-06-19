from docx import Document

from finance_requirements_generator.exports import export_docx, export_markdown, pack_to_markdown
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


def test_docx_export_contains_key_headings(tmp_path) -> None:
    for process_key, intake in DEFAULT_SAMPLE_INPUTS.items():
        pack = generate_pack(intake)
        output_path = export_docx(pack, tmp_path / f"{process_key}_pack.docx")

        document = Document(output_path)
        text = "\n".join(paragraph.text for paragraph in document.paragraphs)
        assert f"{pack.process_name} Requirements Pack" in text
        assert "Functional Requirements" in text
        assert "UAT Test Cases" in text
