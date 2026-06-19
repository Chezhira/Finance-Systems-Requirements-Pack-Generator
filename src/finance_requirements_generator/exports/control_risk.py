from __future__ import annotations

from pathlib import Path

from finance_requirements_generator.control_risk import (
    export_control_risk_csv,
    export_control_risk_xlsx,
    matrix_to_csv_bytes,
    matrix_to_xlsx_bytes,
)
from finance_requirements_generator.schemas import RequirementsPack


def pack_control_risk_csv_bytes(pack: RequirementsPack) -> bytes:
    return matrix_to_csv_bytes(pack.control_risk_matrix)


def pack_control_risk_xlsx_bytes(pack: RequirementsPack) -> bytes:
    return matrix_to_xlsx_bytes(pack.control_risk_matrix)


def export_pack_control_risk_csv(pack: RequirementsPack, output_path: str | Path) -> Path:
    return export_control_risk_csv(pack.control_risk_matrix, output_path)


def export_pack_control_risk_xlsx(pack: RequirementsPack, output_path: str | Path) -> Path:
    return export_control_risk_xlsx(pack.control_risk_matrix, output_path)
