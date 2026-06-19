from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from finance_requirements_generator.exports import export_docx, export_markdown  # noqa: E402
from finance_requirements_generator.questionnaire import DEFAULT_SAMPLE_INPUTS  # noqa: E402
from finance_requirements_generator.template_engine import generate_pack  # noqa: E402


def generate_examples(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for process_key, intake in DEFAULT_SAMPLE_INPUTS.items():
        pack = generate_pack(intake)
        generated.append(export_markdown(pack, output_dir / f"{process_key}_requirements_pack.md"))
        generated.append(export_docx(pack, output_dir / f"{process_key}_requirements_pack.docx"))
    return generated


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "examples" / "generated_packs")
    args = parser.parse_args()
    for path in generate_examples(args.output_dir):
        print(path)


if __name__ == "__main__":
    main()
