#!/usr/bin/env python3
"""Package each skill's source into an `application/agentskill+zip` artifact.

Reads every `skills/<name>/SKILL.md` and writes a `docs/skills/<name>/skill.zip`
so MkDocs publishes it (the catalog at /.well-known/ai-catalog.json points at
these URLs). Run from the repo root:

    python3 skills/build_skills.py
"""

from __future__ import annotations

import pathlib
import zipfile

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_SRC = REPO_ROOT / "skills"
SKILLS_OUT = REPO_ROOT / "docs" / "skills"


def main() -> None:
    built = 0
    for skill_md in sorted(SKILLS_SRC.glob("*/SKILL.md")):
        name = skill_md.parent.name
        out_dir = SKILLS_OUT / name
        out_dir.mkdir(parents=True, exist_ok=True)
        zip_path = out_dir / "skill.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(skill_md, arcname="SKILL.md")
        print(f"built {zip_path.relative_to(REPO_ROOT)}")
        built += 1
    print(f"done: {built} skill(s) packaged")


if __name__ == "__main__":
    main()
