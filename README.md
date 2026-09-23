# Yubiz documentation draft

This repository contains source-reviewed operational guidance. It is a draft:
tenant behavior and deployed-version parity remain unverified.

## Locked local validation

The lock targets **Linux CPython 3.14 x86_64** and contains hashes only for
the wheels actually downloaded for that target. It is not a cross-platform
lock. Python 3.14.7 was used to create the local proof; CI selects the supported
`3.14` minor and records its resolved patch at runtime.

```bash
python3 -m venv .build/release-venv
.build/release-venv/bin/python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
.build/release-venv/bin/python -m pip check
.build/release-venv/bin/python -m unittest discover -s tests -p 'test_*.py'
.build/release-venv/bin/python scripts/validate_manual.py --root .
.build/release-venv/bin/python scripts/validate_manual.py --fixture tests/fixtures/manual/valid
```

## Reproducible release artifact

Builds do not modify `mkdocs.yml`. Supply an approved URL and explicit epoch;
the reserved URL below is only a local test target, not a production claim.

```bash
.build/release-venv/bin/python scripts/build_manual.py --root . --site-url https://docs.example.test/manual/ --output .build/release --source-date-epoch 1700000000 --source-commit 0000000000000000000000000000000000000000
```

The command writes a sorted manifest and normalized `manual.tar.gz` beneath
`.build/`. It normalizes every gzip output, including `sitemap.xml.gz`, before
hashing and archiving. The artifact's content hash is local identity only;
publication requires the separate U8 full-SHA gate. The placeholder SHA is not
publishable; use a reviewed full commit SHA only.

## Publication readiness

- **Implemented locally:** deterministic artifact binding and fail-closed upload guards.
- **Remote CI:** configured but not run by this repository state.
- **Deployment:** blocked until a hosting operator verifies the target and activation.

See `documentation/production-publication-runbook.md`; it documents the required
external inputs and explicitly does not claim live publication.

## Local preview

```bash
.build/release-venv/bin/python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
.build/release-venv/bin/mkdocs serve --dev-addr 127.0.0.1:8000
```

## Local check

```bash
.build/release-venv/bin/python -m unittest discover -s tests -p 'test_*.py'
.build/release-venv/bin/python scripts/validate_manual.py --root .
.build/release-venv/bin/python scripts/validate_manual.py --fixture tests/fixtures/manual/valid
.build/release-venv/bin/python -m mkdocs build --strict --clean
```

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
