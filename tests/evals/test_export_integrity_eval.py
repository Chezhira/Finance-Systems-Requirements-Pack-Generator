import ast
import re
from pathlib import Path

import pytest
from eval_helpers import PROCESS_KEYS, REPRESENTATIVE_PROCESS_KEYS, generated_pack, readiness_pack

from finance_requirements_generator.exports import (
    pack_control_risk_csv_bytes,
    pack_control_risk_xlsx_bytes,
    pack_process_map_html_bytes,
    pack_to_docx_bytes,
    pack_to_markdown,
    pack_to_readiness_docx_bytes,
    pack_to_readiness_markdown,
)
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS


@pytest.mark.parametrize("process_key", REPRESENTATIVE_PROCESS_KEYS)
def test_representative_finance_exports_are_complete(process_key: str) -> None:
    pack = generated_pack(process_key)
    readiness = readiness_pack(process_key)
    requirements_markdown = pack_to_markdown(pack)
    readiness_markdown = pack_to_readiness_markdown(readiness)

    for heading in (
        "## Business Problem",
        "## Functional Requirements",
        "## Controls",
        "## UAT Test Cases",
        "## Control-Risk Matrix",
    ):
        assert heading in requirements_markdown
    for heading in (
        "## Process Implementation Checklist",
        "## Target-System Readiness",
        "## Controls and UAT Readiness",
        "## Open Decisions and Dependencies",
        "## Source Traceability",
    ):
        assert heading in readiness_markdown

    assert pack_to_docx_bytes(pack).startswith(b"PK")
    assert pack_to_readiness_docx_bytes(readiness).startswith(b"PK")
    assert pack_control_risk_csv_bytes(pack).startswith(b"\xef\xbb\xbfProcess Area")
    assert pack_control_risk_xlsx_bytes(pack).startswith(b"PK")
    assert pack_process_map_html_bytes(pack).startswith(b"<!DOCTYPE html>")
    assert pack.mermaid_process_map.startswith("flowchart LR")


@pytest.mark.parametrize("process_key", PROCESS_KEYS)
def test_generated_outputs_remain_public_safe(process_key: str) -> None:
    pack = generated_pack(process_key)
    content = pack_to_markdown(pack)
    forbidden_patterns = (
        r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b",
        r"\b\d{2}-\d{2}-\d{2}\b",
        r"\b(?:GB)?\d{9}\b",
        r"\b(?:account|payroll)\s*(?:number|no\.?)[\s:]+\d{8,16}\b",
    )

    assert pack.company_name in {item.company_name for item in DEFAULT_SAMPLE_INPUTS.values()}
    assert "public-safe" in pack.public_safe_sample_data_note.lower()
    for pattern in forbidden_patterns:
        assert not re.search(pattern, content, flags=re.IGNORECASE)


def test_generation_is_deterministic_without_external_service_imports() -> None:
    first = generated_pack("accounts_payable")
    second = generated_pack.__wrapped__("accounts_payable")

    assert first == second
    assert pack_to_markdown(first) == pack_to_markdown(second)
    assert pack_control_risk_csv_bytes(first) == pack_control_risk_csv_bytes(second)
    assert pack_process_map_html_bytes(first) == pack_process_map_html_bytes(second)

    root = Path(__file__).resolve().parents[2]
    source_files = [
        *(root / "src").rglob("*.py"),
        *(root / "tests" / "evals").glob("*.py"),
        root / "scripts" / "run_evals.py",
    ]
    forbidden_modules = {"anthropic", "httpx", "openai", "requests"}
    for path in source_files:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        imported_modules = {
            alias.name.split(".", 1)[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        imported_modules.update(
            node.module.split(".", 1)[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        )
        assert imported_modules.isdisjoint(forbidden_modules), path
