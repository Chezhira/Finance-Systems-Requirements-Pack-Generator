from __future__ import annotations

from importlib import resources
from typing import Any

import yaml

from finance_requirements_generator.schemas import FitGapMappingRow

TARGET_SYSTEMS = [
    "Odoo",
    "NetSuite",
    "Microsoft Dynamics 365 Business Central",
    "Microsoft Dynamics 365 Finance",
    "SAP Business One",
    "Xero",
    "QuickBooks Online",
    "Generic ERP / Not decided yet",
]

MAPPING_PACKAGE = "finance_requirements_generator.system_mapping"


def load_capability_mappings() -> dict[str, Any]:
    path = resources.files(MAPPING_PACKAGE).joinpath("capabilities.yaml")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def get_fit_gap_mapping(process_key: str, target_system: str) -> list[FitGapMappingRow]:
    if not target_system or target_system == "No target-system mapping":
        return []

    mappings = load_capability_mappings()
    process_mappings = mappings.get("processes", {}).get(process_key, [])
    rows = []
    for item in process_mappings:
        system_note = item.get("systems", {}).get(
            target_system,
            item.get("systems", {}).get("Generic ERP / Not decided yet", {}),
        )
        rows.append(
            FitGapMappingRow(
                current_state_area=item["current_state_area"],
                target_system_capability_area=item["capability_area"],
                candidate_fit_gap_view=system_note.get(
                    "candidate_fit_gap_view",
                    item.get("default_fit_gap_view", "Configuration dependent"),
                ),
                requirement_impact=item["requirement_impact"],
                validation_note=system_note.get(
                    "validation_note",
                    item["validation_note"],
                ),
            )
        )
    return rows
