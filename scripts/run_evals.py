from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

def main() -> int:
    from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/evals", "-q"],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        return result.returncode

    print("\n# Finance Artefact Evaluation Summary")
    print(f"- Supported processes checked: {len(DEFAULT_SAMPLE_INPUTS)}")
    print(f"- Requirements packs evaluated: {len(DEFAULT_SAMPLE_INPUTS)}")
    print("- Structure and ID uniqueness checks: passed")
    print("- Traceability checks: passed")
    print("- Control coverage checks: passed")
    print("- Readiness checks for selected and unselected systems: passed")
    print("- Representative export checks: passed")
    print("- Public-safe and deterministic-generation checks: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
