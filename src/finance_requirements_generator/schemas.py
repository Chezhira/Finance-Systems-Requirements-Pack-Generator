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


@dataclass(frozen=True)
class UATTestCase:
    test_id: str
    scenario: str
    expected_result: str


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
    public_safe_sample_data_note: str

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
            "public_safe_sample_data_note": self.public_safe_sample_data_note,
        }
