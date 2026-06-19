from finance_requirements_generator.process_library import (
    REQUIRED_TEMPLATE_KEYS,
    SUPPORTED_PROCESSES,
    load_all_templates,
)


def test_all_process_templates_have_required_keys() -> None:
    templates = load_all_templates()

    assert len(SUPPORTED_PROCESSES) == 8
    assert set(templates) == set(SUPPORTED_PROCESSES)
    for process_key, template in templates.items():
        assert REQUIRED_TEMPLATE_KEYS.issubset(template), process_key
        assert len(template["functional_requirements"]) >= 8
        assert len(template["non_functional_requirements"]) >= 5
        assert len(template["data_requirements"]) >= 8
        assert len(template["controls"]) >= 5
        assert len(template["audit_trail_requirements"]) >= 5
        assert len(template["user_stories"]) >= 5
        assert len(template["uat_test_cases"]) >= 6
        assert len(template["acceptance_criteria"]) >= 5
        assert len(template["risks_and_dependencies"]) >= 5
