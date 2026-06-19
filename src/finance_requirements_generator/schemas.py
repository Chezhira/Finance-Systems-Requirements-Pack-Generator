from __future__ import annotations

from dataclasses import dataclass, field

REQUIRED_SECTIONS = [
    "executive_summary",
    "current_state_problem",
    "future_state_scope",
    "functional_requirements",
    "non_functional_requirements",
    "data_requirements",
    "controls",
    "audit_trail_requirements",
    "user_stories",
    "uat_test_cases",
    "acceptance_criteria",
    "risks_and_dependencies",
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
    current_state_problem: str
    future_state_scope: str
    assumptions: list[str]
    functional_requirements: list[str]
    non_functional_requirements: list[str]
    data_requirements: list[str]
    controls: list[str]
    audit_trail_requirements: list[str]
    user_stories: list[str]
    uat_test_cases: list[UATTestCase]
    acceptance_criteria: list[str]
    risks_and_dependencies: list[str]
    implementation_notes: list[str]

    def section_map(self) -> dict[str, object]:
        return {
            "executive_summary": self.executive_summary,
            "current_state_problem": self.current_state_problem,
            "future_state_scope": self.future_state_scope,
            "functional_requirements": self.functional_requirements,
            "non_functional_requirements": self.non_functional_requirements,
            "data_requirements": self.data_requirements,
            "controls": self.controls,
            "audit_trail_requirements": self.audit_trail_requirements,
            "user_stories": self.user_stories,
            "uat_test_cases": self.uat_test_cases,
            "acceptance_criteria": self.acceptance_criteria,
            "risks_and_dependencies": self.risks_and_dependencies,
        }
