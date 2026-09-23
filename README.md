# Yubiz documentation draft

This repository contains source-reviewed operational guidance. It is a draft:
tenant behavior and deployed-version parity remain unverified.

## Daily workflow

Use a local `.venv`; activation is not required. Create it with an available
Python 3.14 interpreter, then use its tools instead of a global `mkdocs`.

### Install

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
.venv/bin/python -m pip check
```

The lock targets **Linux CPython 3.14 x86_64** and contains hashes only for
the wheels downloaded for that target. It is not a cross-platform lock.
Environments have absolute interpreter paths and are not portable: recreate
them; never move them.

### Preview

```bash
.venv/bin/mkdocs serve --dev-addr 127.0.0.1:8000
```

Open `http://127.0.0.1:8000/`. Stop the preview with `Ctrl+C`.

### Validate and build

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py'
.venv/bin/python scripts/validate_manual.py --root . --final
.venv/bin/python scripts/validate_manual.py --fixture tests/fixtures/manual/valid
.venv/bin/mkdocs build --strict --clean
```

The normal build is written to ignored `site/`.

## Advanced release artifact

Builds do not modify `mkdocs.yml`. Supply an approved URL and explicit epoch;
the reserved URL below is only a local test target, not a production claim.

```bash
.venv/bin/python scripts/build_manual.py --root . --site-url https://docs.example.test/manual/ --output .build/release --source-date-epoch 1700000000 --source-commit 0000000000000000000000000000000000000000
```

The command writes a sorted manifest and normalized `manual.tar.gz` beneath
`.build/`. It normalizes every gzip output, including `sitemap.xml.gz`, before
hashing and archiving. The artifact's content hash is local identity only;
publication requires a reviewed full documentation commit SHA. The placeholder
SHA is not publishable.

## Publication readiness

- **Implemented locally:** deterministic artifact binding and fail-closed upload guards.
- **Remote CI:** configured but not run by this repository state.
- **Deployment:** blocked until a hosting operator verifies the target and activation.

See `documentation/production-publication-runbook.md`; it documents the required
external inputs and explicitly does not claim live publication.

`scripts/preview_manual.py` is an optional base-path QA helper, not a daily
preview command. Always give it an explicit compatible `--site-dir` artifact
and a `--base-path` matching that build. It does not rewrite canonical or 404
URLs; host, scheme, and HTTPS require deployment evidence.

## Authoring boundary

- Write reader guidance in neutral Spanish.
- Keep internal source paths and traces out of public files.
- Mark unknown labels, permissions, tenant behavior, and runtime outcomes as
  pending verification.
- Maintain v2 `inventory.yml`, `capability-dispositions.yml`, and
  `source-checkpoint.yml` together; use opaque capability IDs in public metadata.
- Set `scope_state: scope_complete` only after the private evidence review and
  final reconciliation cover every documented or explicitly dispositioned ID;
  it does not verify runtime behavior, deployed parity, or publication.

See `AGENTS.md` for the maintenance skill and `documentation/` for the public
review status.

## Source sync maintenance

Request a documentation sync through the Yubiz source-backed ficha workflow.
`documentation/source-checkpoint.yml` records the completed pin, the current
read-only source target, and any pending range. Pending paths do not advance the
completed pin or the 88 ficha revisions; source repositories are never modified
by this documentation workflow.
