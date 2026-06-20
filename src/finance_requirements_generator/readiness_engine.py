from __future__ import annotations

import re
from itertools import cycle

from finance_requirements_generator.process_library import load_process_template
from finance_requirements_generator.schemas import (
    ImplementationReadinessPack,
    OpenDecision,
    ReadinessCheck,
    RequirementsPack,
    UATTestCase,
    WorkshopQuestion,
)


def generate_implementation_readiness_pack(
    requirements_pack: RequirementsPack,
) -> ImplementationReadinessPack:
    template = load_process_template(requirements_pack.process_key)
    readiness = template["implementation_readiness"]
    process_owner = _process_owner(requirements_pack)

    process_checks = _seed_checks(
        readiness["process_checks"],
        prefix="PIC",
        area="Process implementation",
    )
    process_checks.extend(_control_risk_checks(requirements_pack, len(process_checks) + 1))

    target_checks = _target_system_checks(requirements_pack, process_owner)
    data_checks = _data_checks(requirements_pack, process_owner)
    controls_uat_checks = _controls_uat_checks(requirements_pack, process_owner)
    workshop_questions = _workshop_questions(
        readiness["configuration_workshop_questions"]
    )
    cutover_checks = _seed_checks(
        readiness["cutover_considerations"],
        prefix="CUT",
        area="Cutover readiness",
    )
    open_decisions = _open_decisions(requirements_pack, process_owner)

    return ImplementationReadinessPack(
        process_key=requirements_pack.process_key,
        process_name=requirements_pack.process_name,
        company_name=requirements_pack.company_name,
        target_system=requirements_pack.target_system or "Not selected",
        readiness_summary=(
            f"This readiness pack translates the approved {requirements_pack.process_name} "
            "requirements, controls, data needs, UAT cases, risks, and target-system context "
            "into evidence-based implementation review prompts. All checks begin as "
            "Not assessed and require finance and implementation team validation."
        ),
        process_implementation_checklist=process_checks,
        target_system_readiness_checklist=target_checks,
        data_readiness_checklist=data_checks,
        controls_and_uat_readiness_checklist=controls_uat_checks,
        configuration_workshop_questions=workshop_questions,
        cutover_readiness_notes=cutover_checks,
        open_decisions_and_dependencies=open_decisions,
        public_safe_sample_data_note=requirements_pack.public_safe_sample_data_note,
    )


def readiness_source_references(pack: ImplementationReadinessPack) -> set[str]:
    references: set[str] = set()
    check_groups = (
        pack.process_implementation_checklist,
        pack.target_system_readiness_checklist,
        pack.data_readiness_checklist,
        pack.controls_and_uat_readiness_checklist,
        pack.cutover_readiness_notes,
    )
    for group in check_groups:
        for item in group:
            references.update(item.source_references)
    for item in pack.configuration_workshop_questions:
        references.update(item.source_references)
    for item in pack.open_decisions_and_dependencies:
        references.update(item.source_references)
    return references


def _seed_checks(items: list[dict], prefix: str, area: str) -> list[ReadinessCheck]:
    return [
        ReadinessCheck(
            check_id=f"{prefix}-{index:02d}",
            checklist_area=area,
            finance_specific_check=item["check"],
            evidence_required=item["evidence"],
            suggested_owner_role=item["owner_role"],
            source_references=list(item["source_references"]),
        )
        for index, item in enumerate(items, start=1)
    ]


def _control_risk_checks(pack: RequirementsPack, start: int) -> list[ReadinessCheck]:
    checks = []
    for index, row in enumerate(pack.control_risk_matrix, start=start):
        matrix_id = f"CRM-{index - start + 1:02d}"
        references = [matrix_id]
        if row.related_requirement_id.startswith("FR-"):
            references.append(row.related_requirement_id)
        if row.related_uat_case.startswith("UAT-"):
            references.append(row.related_uat_case)
        checks.append(
            ReadinessCheck(
                check_id=f"PIC-{index:02d}",
                checklist_area="Process risk and ownership",
                finance_specific_check=(
                    f"Confirm implementation treatment for {row.risk_area.lower()}, including "
                    f"the control activity: {row.control_activity}"
                ),
                evidence_required=row.evidence_required,
                suggested_owner_role=row.owner,
                source_references=references,
                validation_note=row.residual_risk_implementation_note,
            )
        )
    return checks


def _target_system_checks(
    pack: RequirementsPack,
    process_owner: str,
) -> list[ReadinessCheck]:
    if not _has_confirmed_target(pack):
        return [
            ReadinessCheck(
                check_id="SYS-01",
                checklist_area="Target system selection",
                finance_specific_check=(
                    f"Confirm the target system, edition, modules, localisation, integrations, "
                    f"and implementation scope for {pack.process_name}."
                ),
                evidence_required="Approved target-system scope and architecture decision.",
                suggested_owner_role="Finance Transformation Lead",
                source_references=["INTAKE-TARGET-SYSTEM"],
                validation_note=(
                    "No target-system capability conclusion can be made until the selection "
                    "and implementation scope are confirmed."
                ),
            )
        ]

    if not pack.target_system_fit_gap_mapping:
        return [
            ReadinessCheck(
                check_id="SYS-01",
                checklist_area="Target-system capability validation",
                finance_specific_check=(
                    f"Validate the {pack.process_name} configuration, data, control, reporting, "
                    f"audit, and UAT requirements directly with the {pack.target_system} "
                    "implementation team."
                ),
                evidence_required=(
                    "Documented capability walkthrough, configuration decisions, identified "
                    "gaps, and test evidence."
                ),
                suggested_owner_role=f"{process_owner} and ERP Functional Lead",
                source_references=["INTAKE-TARGET-SYSTEM"],
                validation_note=(
                    "No curated process mapping is available for this selection. Do not assume "
                    "fit; validate the selected edition, modules, localisation, configuration, "
                    "integrations, and implementation scope."
                ),
            )
        ]

    checks = []
    for index, row in enumerate(pack.target_system_fit_gap_mapping, start=1):
        checks.append(
            ReadinessCheck(
                check_id=f"SYS-{index:02d}",
                checklist_area="Target-system fit validation",
                finance_specific_check=(
                    f"Validate how {pack.target_system} will support "
                    f"{row.target_system_capability_area.lower()} for "
                    f"{row.current_state_area.lower()}."
                ),
                evidence_required=(
                    f"Documented configuration decision and test evidence. "
                    f"Implementation impact: {row.requirement_impact}"
                ),
                suggested_owner_role=f"{process_owner} and ERP Functional Lead",
                source_references=[f"FG-{index:02d}"],
                validation_note=(
                    "Candidate mapping only; requires implementation validation against the "
                    f"selected edition, modules, localisation, configuration, integrations, and "
                    f"scope. {row.validation_note}"
                ),
            )
        )
    return checks


def _data_checks(pack: RequirementsPack, process_owner: str) -> list[ReadinessCheck]:
    return [
        ReadinessCheck(
            check_id=f"DATA-{index:02d}",
            checklist_area="Data readiness",
            finance_specific_check=(
                f"Confirm the source, definition, ownership, cleansing rule, migration treatment, "
                f"and reconciliation approach for {_without_id(item)}."
            ),
            evidence_required=(
                "Approved data definition, source-to-target mapping, quality result, and "
                "reconciliation evidence."
            ),
            suggested_owner_role=f"{process_owner} and Finance Data Owner",
            source_references=[_identifier(item)],
            validation_note=(
                "Validate completeness and control usability using representative data."
            ),
        )
        for index, item in enumerate(pack.data_requirements, start=1)
    ]


def _controls_uat_checks(
    pack: RequirementsPack,
    process_owner: str,
) -> list[ReadinessCheck]:
    audit_cycle = cycle(pack.audit_trail_requirements)
    report_cycle = cycle(pack.reporting_requirements)
    checks = []
    for index, control in enumerate(pack.controls, start=1):
        audit = next(audit_cycle)
        report = next(report_cycle)
        uat = _best_uat_match(control, pack.uat_test_cases)
        evidence = (
            f"UAT evidence demonstrating: {uat.expected_result} Audit evidence must also "
            f"support {_without_id(audit)}"
            if uat
            else (
                "A dedicated positive and negative-path UAT case must be defined. Audit evidence "
                f"must also support {_without_id(audit)}"
            )
        )
        source_references = [
            _identifier(control),
            _identifier(audit),
            _identifier(report),
        ]
        if uat:
            source_references.append(uat.test_id)
        checks.append(
            ReadinessCheck(
                check_id=f"CU-{index:02d}",
                checklist_area="Controls and UAT readiness",
                finance_specific_check=(
                    f"Confirm configuration, ownership, negative-path testing, and evidence for "
                    f"{_without_id(control)}"
                ),
                evidence_required=evidence,
                suggested_owner_role=f"{process_owner} and Controls/UAT Lead",
                source_references=source_references,
                validation_note=(
                    "Confirm the control operates with production-like roles, data, reporting, "
                    "and retained evidence before sign-off."
                    if uat
                    else (
                        "No directly aligned UAT case was identified; add one before control "
                        "design sign-off."
                    )
                ),
            )
        )
    return checks


def _workshop_questions(items: list[dict]) -> list[WorkshopQuestion]:
    return [
        WorkshopQuestion(
            question_id=f"CWQ-{index:02d}",
            question=item["question"],
            implementation_relevance=item["relevance"],
            source_references=list(item["source_references"]),
        )
        for index, item in enumerate(items, start=1)
    ]


def _open_decisions(pack: RequirementsPack, process_owner: str) -> list[OpenDecision]:
    decisions = [
        OpenDecision(
            decision_id=f"DEC-{index:02d}",
            decision_required=f"Confirm implementation treatment for: {risk}",
            dependency_or_impact=(
                "Configuration, data preparation, control design, testing, or cutover cannot be "
                "fully confirmed until this dependency is resolved."
            ),
            suggested_decision_owner=process_owner,
            source_references=[f"RISK-{index:02d}"],
        )
        for index, risk in enumerate(pack.risks_and_dependencies, start=1)
    ]
    if not _has_confirmed_target(pack):
        decisions.insert(
            0,
            OpenDecision(
                decision_id="DEC-00",
                decision_required=(
                    "Confirm the target ERP or finance system, edition, modules, localisation, "
                    "integration boundaries, and implementation scope."
                ),
                dependency_or_impact=(
                    "Target-system readiness and detailed configuration workshops remain "
                    "provisional until this selection is approved."
                ),
                suggested_decision_owner="Finance Transformation Lead",
                source_references=["INTAKE-TARGET-SYSTEM"],
            ),
        )
    return decisions


def _process_owner(pack: RequirementsPack) -> str:
    if pack.control_risk_matrix:
        return pack.control_risk_matrix[0].owner
    return f"{pack.process_name} Process Owner"


def _has_confirmed_target(pack: RequirementsPack) -> bool:
    return bool(
        pack.target_system
        and pack.target_system not in {"Generic ERP / Not decided yet", "No target-system mapping"}
    )


def _identifier(value: str) -> str:
    return value.split(":", 1)[0]


def _without_id(value: str) -> str:
    return value.split(":", 1)[1].strip() if ":" in value else value


def _best_uat_match(control: str, cases: list[UATTestCase]) -> UATTestCase | None:
    control_terms = _meaningful_terms(_without_id(control))
    ranked = []
    for case in cases:
        case_terms = _meaningful_terms(f"{case.scenario} {case.expected_result}")
        ranked.append((len(control_terms.intersection(case_terms)), case.test_id, case))
    score, _test_id, case = max(ranked, default=(0, "", None))
    return case if score > 0 else None


def _meaningful_terms(value: str) -> set[str]:
    stopwords = {
        "and",
        "approval",
        "before",
        "control",
        "for",
        "from",
        "invoice",
        "must",
        "payment",
        "require",
        "requires",
        "supplier",
        "the",
        "with",
    }
    return {
        term
        for term in re.findall(r"[a-z0-9]+", value.lower())
        if len(term) > 2 and term not in stopwords
    }
