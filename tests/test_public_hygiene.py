from pathlib import Path

PRIVATE_TERMS = {
    "confiden" + "tial",
    "past " + "employer",
    "client " + "details",
    "payroll " + "details",
}
BINARY_EXTENSIONS = {".docx", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".xlsx"}
SKIPPED_PARTS = {
    ".git",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
}


def test_public_tree_uses_synthetic_positioning() -> None:
    root = Path(__file__).resolve().parents[1]
    searchable_files = [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not SKIPPED_PARTS.intersection(path.parts)
        and not any(part.endswith(".egg-info") for part in path.parts)
        and path.suffix.lower() not in BINARY_EXTENSIONS
        and path.suffix.lower() != ".pyc"
    ]

    content = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore") for path in searchable_files
    )
    lowered = content.lower()
    assert "synthetic" in lowered
    for term in PRIVATE_TERMS:
        assert term not in lowered
