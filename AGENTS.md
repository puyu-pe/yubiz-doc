# Contributor instructions

## Documentation baseline

- Use neutral Spanish for reader-facing pages and English for technical files.
- Keep reader-facing operational documentation separate from editorial and review
  metadata; do not require draft or runtime-verification banners or footers.
- A presentation-only edit does not establish runtime verification or deployment;
  retain pending states until supported by runtime evidence.
- Do not state universal labels, permissions, policies, screenshots, or deployed
  behavior without runtime evidence.
- Keep detailed source traces in private Engram evidence only.

## Local tooling

- Use `.venv/bin/python` and `.venv/bin/mkdocs`; activation is not required.
- Do not use a global `mkdocs` or move an existing virtual environment;
  recreate `.venv` with the supported interpreter when needed.
- Run the daily preview at `http://127.0.0.1:8000/`; release builds keep their
  explicit URL and `.build/` output arguments.

## Project skills

- `.agents/skills/yubiz-source-backed-ficha/SKILL.md` — review and refresh a
  source-backed ficha without exposing internal traces.
