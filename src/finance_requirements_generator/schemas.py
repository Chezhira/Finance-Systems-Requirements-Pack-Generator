from __future__ import annotations

from dataclasses import dataclass, field

REQUIRED_SECTIONS = [
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


@dataclass(frozen=True)
class IntakeAnswers:
    process_key: str
    company_name: str
    entity_type: str
    current_tools: str
    erp_platform: str
    monthly_volume: str
    pain_points: list[str]
    control_concerns: list[str]
    reporting_needs: str
    compliance_focus: str
    deadline: str
    sponsor: str = "Finance Transformation Lead"
    assumptions: list[str] = field(default_factory=list)
    target_system: str = ""
    current_state_sop_draft: SOPDraft | None = None


@dataclass(frozen=True)
class UATTestCase:
    test_id: str
    scenario: str
    expected_result: str


@dataclass(frozen=True)
class FitGapMappingRow:
    current_state_area: str
    target_system_capability_area: str
    candidate_fit_gap_view: str
    requirement_impact: str
    validation_note: str


@dataclass(frozen=True)
class ControlRiskRow:
    process_area: str
    risk_area: str
    risk_description: str
    control_objective: str
    control_activity: str
    control_type: str
    frequency: str
    owner: str
    evidence_required: str
    system_data_dependency: str
    related_requirement_id: str
    related_uat_case: str
    residual_risk_implementation_note: str


@dataclass(frozen=True)
class ProcessMapFlow:
    trigger: str
    source: str
    validation: str
    decision: str
    exception_resolution: str
    approval: str
    reporting: str
    signoff: str


@dataclass(frozen=True)
class ReadinessCheck:
    check_id: str
    checklist_area: str
    finance_specific_check: str
    evidence_required: str
    suggested_owner_role: str
    source_references: list[str]
    review_status: str = "Not assessed"
    validation_note: str = "Requires finance and implementation team review."


@dataclass(frozen=True)
class WorkshopQuestion:
    question_id: str
    question: str
    implementation_relevance: str
    source_references: list[str]


@dataclass(frozen=True)
class OpenDecision:
    decision_id: str
    decision_required: str
    dependency_or_impact: str
    suggested_decision_owner: str
    source_references: list[str]


@dataclass(frozen=True)
class ImplementationReadinessPack:
    process_key: str
    process_name: str
    company_name: str
    target_system: str
    readiness_summary: str
    process_implementation_checklist: list[ReadinessCheck]
    target_system_readiness_checklist: list[ReadinessCheck]
    data_readiness_checklist: list[ReadinessCheck]
    controls_and_uat_readiness_checklist: list[ReadinessCheck]
    configuration_workshop_questions: list[WorkshopQuestion]
    cutover_readiness_notes: list[ReadinessCheck]
    open_decisions_and_dependencies: list[OpenDecision]
    public_safe_sample_data_note: str


@dataclass(frozen=True)
class SOPDraft:
    purpose: str
    scope: str
    trigger: str
    roles_and_responsibilities: str
    step_by_step_procedure: list[str]
    controls_and_approvals: list[str]
    exceptions_and_escalations: list[str]
    reports_and_evidence: list[str]
    systems_and_data_used: list[str]
    review_and_sign_off: str


@dataclass(frozen=True)
class RequirementsPack:
    process_key: str
    process_name: str
    company_name: str
    executive_summary: str
    business_problem: str
    process_scope: str
    in_scope: list[str]
    out_of_scope: list[str]
    stakeholders_and_roles: list[str]
    assumptions: list[str]
    functional_requirements: list[str]
    non_functional_requirements: list[str]
    data_requirements: list[str]
    controls: list[str]
    reporting_requirements: list[str]
    audit_trail_requirements: list[str]
    user_stories: list[str]
    uat_test_cases: list[UATTestCase]
    acceptance_criteria: list[str]
    risks_and_dependencies: list[str]
    implementation_notes: list[str]
    control_risk_matrix: list[ControlRiskRow] = field(default_factory=list)
    process_map_flow: ProcessMapFlow | None = None
    mermaid_process_map: str = ""
    process_map_summary: list[str] = field(default_factory=list)
    target_system: str = ""
    target_system_fit_gap_mapping: list[FitGapMappingRow] = field(default_factory=list)
    current_state_sop_draft: SOPDraft | None = None
    public_safe_sample_data_note: str = ""

    @property
    def current_state_problem(self) -> str:
        return self.business_problem

    @property
    def future_state_scope(self) -> str:
        return self.process_scope

    def section_map(self) -> dict[str, object]:
        return {
            "executive_summary": self.executive_summary,
            "business_problem": self.business_problem,
            "process_scope": self.process_scope,
            "in_scope": self.in_scope,
            "out_of_scope": self.out_of_scope,
            "stakeholders_and_roles": self.stakeholders_and_roles,
            "functional_requirements": self.functional_requirements,
            "data_requirements": self.data_requirements,
            "controls": self.controls,
            "reporting_requirements": self.reporting_requirements,
            "audit_trail_requirements": self.audit_trail_requirements,
            "user_stories": self.user_stories,
            "uat_test_cases": self.uat_test_cases,
            "acceptance_criteria": self.acceptance_criteria,
            "risks_and_dependencies": self.risks_and_dependencies,
            "implementation_notes": self.implementation_notes,
            "visual_process_documentation": self.process_map_summary,
            "control_risk_matrix": self.control_risk_matrix,
            "target_system_fit_gap_mapping": self.target_system_fit_gap_mapping,
            "public_safe_sample_data_note": self.public_safe_sample_data_note,
        }
