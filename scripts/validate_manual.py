"""Validate the task-manual contract and its explicit legacy compatibility map."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import markdown
import yaml


REQUIRED_SECTIONS = ("Cómo acceder", "Pasos", "Compruebe el resultado")
LEGACY_TEMPLATE_HEADINGS = (
    "Objetivo", "Acceso condicional", "Requisitos y datos", "Punto de partida",
    "Campos y validaciones observados", "Resultado esperado", "Advertencias y casos límite",
    "Problemas frecuentes y condiciones de detención", "Enlaces relacionados",
)
QUICKSTART_ACTIONS = ("Establecimiento", "menú lateral", "Mi perfil", "Cerrar Sesión")
LEGACY_REQUIRED_SECTIONS = (
    "Objetivo", "Acceso condicional", "Requisitos y datos", "Punto de partida", "Pasos",
    "Campos y validaciones observados", "Resultado esperado", "Advertencias y casos límite",
    "Problemas frecuentes y condiciones de detención", "Enlaces relacionados",
)
RAW_READER_STATUS_TOKENS = ("source_reviewed_draft", "pending_runtime_verification")
PUBLIC_ACCESS_AUDIT_NOTE = "No se confirmó una entrada lateral literal"
READER_PROCESS_PATTERNS = (
    r"(?i)Borrador revisado en código · verificación en entorno pendiente",
    r"(?i)Revisión de fuente: revisada en código",
    r"(?i)Verificación en entorno: pendiente",
    r"(?i)Paridad con la versión desplegada: pendiente",
    r"(?i)\brevisad[oa] en (?:código|fuente)\b",
    r"(?i)\b(?:requiere|requieren|quedan) (?:verificación en |pendientes? de )(?:runtime|entorno)\b",
)
SHA_PATTERN = re.compile(r"[a-f0-9]{40}")
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^]]*)\]\(([^)]*)\)")


@dataclass(frozen=True)
class ValidationReport:
    ficha_count: int
    diagnostics: tuple[str, ...]
    document_count: int = 0
    capability_ids: tuple[str, ...] = ()

    @property
    def is_valid(self) -> bool:
        return not self.diagnostics


def load(path: Path, diagnostics: list[str]) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        diagnostics.append(f"invalid-yaml: {path.as_posix()}")
        return {}


def validate_manual(root: Path, *, final: bool = False, audit_compatibility: bool = False) -> ValidationReport:
    diagnostics: list[str] = []
    docs_root = root / "docs"
    if not docs_root.is_dir():
        return ValidationReport(0, ("missing-docs-root: docs directory was not found",))
    migration_path = root / "documentation/task-manual-migration.yml"
    if not migration_path.is_file():
        return validate_legacy_manual(root, docs_root, final, diagnostics)
    migration = load(migration_path, diagnostics)
    if isinstance(migration, dict) and not migration:
        return validate_legacy_manual(root, docs_root, final, diagnostics)
    if not isinstance(migration, dict) or migration.get("schema_version") != 2:
        diagnostics.append("migration-schema: task-manual migration schema_version 2 is required")
        return ValidationReport(0, tuple(diagnostics))
    if migration.get("contract_version") != 2:
        diagnostics.append("migration-contract-version: explicit contract version 2 is required")
        return ValidationReport(0, tuple(diagnostics))
    active = migration.get("active_entries")
    compatibility = migration.get("compatibility", {})
    if not isinstance(active, list) or not isinstance(compatibility, dict):
        diagnostics.append("migration-shape: active entries and compatibility are required")
        return ValidationReport(0, tuple(diagnostics))
    validate_active(root, docs_root, active, diagnostics)
    validate_progress(root, active, diagnostics)
    validate_access_audit(root, docs_root, active, diagnostics)
    validate_compatibility(root, docs_root, compatibility, active, diagnostics, audit_compatibility)
    validate_v1_rendered_baseline(root, docs_root, diagnostics)
    validate_active_continuations(docs_root, active, compatibility, diagnostics)
    validate_inventory(root, active, diagnostics)
    validate_technical_metadata(root, active, final, diagnostics)
    validate_navigation(root, active, diagnostics)
    group_indexes = migration.get("group_indexes", {}) if isinstance(migration, dict) else {}
    validate_indexes(docs_root, active, group_indexes, diagnostics)
    for path in docs_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        label = path.relative_to(root).as_posix()
        validate_links(text, path, docs_root, label, diagnostics)
        validate_privacy(text, label, diagnostics)
        if reader_process_marker(text):
            diagnostics.append(f"reader-process-notice: {label}")
        if raw_status_tokens(text):
            diagnostics.append(f"raw-reader-status: {label}")
    return ValidationReport(len(active), tuple(diagnostics), len(active))


def validate_active(root: Path, docs_root: Path, active: list[object], diagnostics: list[str]) -> None:
    contract_name = "task-oriented-manual-contract-v2.md"
    migration = load(root / "documentation/task-manual-migration.yml", diagnostics)
    if isinstance(migration, dict) and isinstance(migration.get("contract"), str):
        contract_name = migration["contract"]
    contract = root / "documentation" / contract_name
    if not contract.is_file():
        diagnostics.append("missing-contract: task-oriented-manual-contract.md")
    seen_numbers: set[str] = set()
    seen_targets: set[str] = set()
    groups: dict[str, int] = {}
    for entry in active:
        if not isinstance(entry, dict):
            diagnostics.append("invalid-active-entry")
            continue
        number, title, target, group = (entry.get(key) for key in ("number", "title", "target", "group"))
        if not all(isinstance(value, str) and value for value in (number, title, target, group)):
            diagnostics.append("invalid-active-entry")
            continue
        if number in seen_numbers or target in seen_targets:
            diagnostics.append("duplicate-active-entry")
        seen_numbers.add(number)
        seen_targets.add(target)
        groups[group] = groups.get(group, 0) + 1
        file = docs_root / target
        if not file.is_file():
            diagnostics.append("missing-active-guide")
            continue
        text = file.read_text(encoding="utf-8")
        h1 = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "")
        if h1 != f"{number} {title}":
            diagnostics.append("active-title: heading does not match contract entry")
        if not intro_after_h1(text):
            diagnostics.append("active-introduction: guide requires non-empty introduction")
        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in text:
                diagnostics.append(f"required-section: {target} lacks {section}")
        for heading in LEGACY_TEMPLATE_HEADINGS:
            if f"## {heading}" in text:
                diagnostics.append(f"legacy-template-heading: {target} retains {heading}")
        if target == "inicio/iniciar-sesion.md" and not all(action in text for action in QUICKSTART_ACTIONS):
            diagnostics.append("quickstart-incomplete: sign-in guide must include session actions")
    expected = contract_entries_v2(contract, diagnostics)
    actual = [(entry.get("number"), entry.get("title"), entry.get("group")) for entry in active if isinstance(entry, dict)]
    if expected and actual != expected:
        diagnostics.append("contract-parity: active entries differ from the approved contract")
    expected_groups = [1, 15, 7, 1, 15, 8, 14, 4, 2, 3, 9, 4]
    if len(active) != 83 or [groups.get(group) for group in (
        "Panel principal", "Ventas", "Internado", "Campañas de descuento", "Inventario",
        "Distribución", "Compras", "Contactos", "Socios", "Presupuesto", "Estancia", "Preventa",
    )] != expected_groups:
        diagnostics.append("contract-coverage: expected 83 entries in the 12 V2 contract groups")


def validate_progress(root: Path, active: list[object], diagnostics: list[str]) -> None:
    progress = load(root / "documentation/task-manual-v2-progress.yml", diagnostics)
    if not isinstance(progress, dict) or progress.get("contract_target_count") != 83 or progress.get("implemented_in_this_batch") != 83:
        diagnostics.append("progress-status: final V2 progress metadata is required")
        return
    targets = progress.get("contract_targets")
    guides = progress.get("guides")
    if not isinstance(targets, list) or not isinstance(guides, list):
        diagnostics.append("progress-shape: targets and guides are required")
        return
    expected = [(entry.get("group"), entry.get("title")) for entry in active if isinstance(entry, dict)]
    actual: list[tuple[object, object]] = []
    for module in targets:
        if not isinstance(module, dict) or set(module) != {"module", "tasks"} or not isinstance(module.get("tasks"), list):
            diagnostics.append("progress-target-shape")
            continue
        for task in module["tasks"]:
            if not isinstance(task, dict) or set(task) != {"title", "status"} or task.get("status") != "active_v2":
                diagnostics.append("progress-target-shape")
                continue
            actual.append((module["module"], task["title"]))
    if actual != expected or len(actual) != 83:
        diagnostics.append("progress-contract-parity: exact V2 titles and groups are required")
    by_path = {entry.get("target"): entry for entry in active if isinstance(entry, dict)}
    if len(guides) != 19:
        diagnostics.append("progress-guide-coverage: expected 19 newly supported guides")
    for guide in guides:
        if not isinstance(guide, dict) or set(guide) != {"title", "path", "status", "basis"}:
            diagnostics.append("progress-guide-shape")
            continue
        entry = by_path.get(guide["path"])
        if not isinstance(entry, dict) or entry.get("title") != guide["title"] or guide.get("status") != "active_v2":
            diagnostics.append("progress-guide-parity: guide title and path must match the active registry")


def validate_access_audit(root: Path, docs_root: Path, active: list[object], diagnostics: list[str]) -> None:
    audit = load(root / "documentation/access-audit.yml", diagnostics)
    records = audit.get("records") if isinstance(audit, dict) and audit.get("schema_version") == 2 else None
    if not isinstance(records, list):
        diagnostics.append("access-audit-shape: schema_version 2 records are required")
        return
    expected = {entry["doc_id"]: entry for entry in active if isinstance(entry, dict) and isinstance(entry.get("doc_id"), str)}
    found: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            diagnostics.append("access-audit-record: record must be a mapping")
            continue
        doc_id, guide, path, classification = (record.get(key) for key in ("id", "guide", "path", "classification"))
        if not all(isinstance(value, str) and value for value in (doc_id, guide, path, classification)) or doc_id not in expected or doc_id in found:
            diagnostics.append("access-audit-record: id must uniquely match an active guide")
            continue
        found.add(doc_id)
        entry = expected[doc_id]
        if guide != entry["number"] or path != entry["target"]:
            diagnostics.append("access-audit-parity: guide number or path differs from active registry")
            continue
        text = (docs_root / path).read_text(encoding="utf-8")
        match = re.search(r"## Cómo acceder\n\n(.*?)(?=\n## |\Z)", text, re.S)
        access = match.group(1) if match else ""
        if PUBLIC_ACCESS_AUDIT_NOTE in access:
            diagnostics.append(f"access-public-audit-note: {path}")
        labels = record.get("sidebar")
        if classification in {"direct", "indirect"}:
            if not isinstance(labels, list) or len(labels) < 2 or not all(isinstance(label, str) and label for label in labels):
                diagnostics.append("access-audit-route: direct and indirect records require two literal sidebar labels")
                continue
            steps = record.get("access_steps")
            if not isinstance(steps, list) or len(steps) < 2 or not all(isinstance(step, str) and step for step in steps):
                diagnostics.append("access-audit-steps: direct and indirect records require ordered access steps")
                continue
            numbered = "\n".join(f"{number}. {step}" for number, step in enumerate(steps, start=1))
            if numbered not in access:
                diagnostics.append(f"access-step-coverage: {path} lacks its audited ordered steps")
            if not all(f"**{label}**" in access for label in labels):
                diagnostics.append(f"access-label-coverage: {path} lacks its audited sidebar labels")
            if re.fullmatch(r"(?is)\s*(?:abra|en)\s+(?:el\s+)?(?:formulario|listado|lista).*", access.strip()):
                diagnostics.append(f"access-vague-start: {path} starts without a navigation route")
        elif classification == "quickstart":
            if "inicio de sesión" not in access.lower():
                diagnostics.append("access-quickstart: sign-in must start before authenticated navigation")
        elif classification == "technical-gap":
            action = record.get("entry_action")
            if not isinstance(action, str) or not action:
                diagnostics.append(f"access-technical-gap: {path} requires an opaque gap identifier")
        else:
            diagnostics.append("access-audit-classification: unsupported classification")
    if found != set(expected) or len(records) != len(expected):
        diagnostics.append("access-audit-coverage: every active guide requires exactly one access record")
    validate_control_catalog(root, expected, docs_root, diagnostics)


def validate_action_profiles(
    audit: dict[str, object], expected: dict[str, object], docs_root: Path, diagnostics: list[str]
) -> None:
    """Validate frozen source relations separately from editable access prose."""
    profiles = audit.get("action_profiles")
    if not isinstance(profiles, list):
        diagnostics.append("action-profile-shape: source-derived action profiles are required")
        return
    batch_ids = {
        entry["doc_id"] for entry in expected.values()
        if isinstance(entry, dict)
    }
    found: set[str] = set()
    for profile in profiles:
        if not isinstance(profile, dict):
            diagnostics.append("action-profile-record")
            continue
        doc_id, evidence, owner, transitions = (
            profile.get("id"), profile.get("evidence"), profile.get("current_action_owner"), profile.get("transitions")
        )
        if not isinstance(doc_id, str) or doc_id not in batch_ids or doc_id in found:
            diagnostics.append("action-profile-record")
            continue
        found.add(doc_id)
        if evidence != {"kind": "source", "revision": "330857197e5e01c24147d03452f7c59909abc968"} or owner != "source" or not isinstance(transitions, list) or not transitions:
            diagnostics.append("action-profile-evidence")
            continue
        for transition in transitions:
            required = {"screen", "container", "control", "gesture", "reveal", "next_state"}
            if not isinstance(transition, dict) or set(transition) != required or not all(isinstance(value, str) and value for value in transition.values()):
                diagnostics.append("action-profile-transition")
    if found != batch_ids or len(profiles) != len(batch_ids):
        diagnostics.append("action-profile-coverage: every reviewed batch guide requires one source profile")
    validate_control_catalog(audit, expected, docs_root, diagnostics)


def validate_control_catalog(root: Path, expected: dict[str, object], docs_root: Path, diagnostics: list[str]) -> None:
    """Check source-first requirements without treating editable audit prose as evidence."""
    catalog = load(root / "documentation/source-fact-catalog.yml", diagnostics)
    if not isinstance(catalog, dict) or catalog.get("schema_version") != 3:
        diagnostics.append("source-fact-catalog-schema: schema_version 3 is required")
        return
    checkpoint = load(root / "documentation/source-checkpoint.yml", diagnostics)
    sync = checkpoint.get("source_sync") if isinstance(checkpoint, dict) else None
    revisions = sync.get("evidence_revisions") if isinstance(sync, dict) else None
    approved_revisions = {
        item.get("source_commit") for item in revisions
        if isinstance(item, dict) and isinstance(item.get("source_commit"), str) and SHA_PATTERN.fullmatch(item["source_commit"])
    } if isinstance(revisions, list) else set()
    default_revision = catalog.get("default_reviewed_revision")
    if not isinstance(default_revision, str) or default_revision not in approved_revisions:
        diagnostics.append("source-fact-catalog-revision: approved default source revision is required")
        return
    requirements, pending = catalog.get("requirements"), catalog.get("pending_guides")
    if not isinstance(requirements, list) or not isinstance(pending, list):
        diagnostics.append("source-fact-catalog-shape: requirements and pending_guides are required")
        return
    covered: set[str] = set()
    required_fact_keys = {"id", "source_fact_kind", "proof_ref", "container", "control", "gesture", "reveal", "dependencies", "next_state", "visible"}
    for requirement in requirements:
        if not isinstance(requirement, dict) or not {"guide_id", "facts"} <= set(requirement) or set(requirement) - {"guide_id", "facts", "reviewed_revision"}:
            diagnostics.append("source-fact-requirement")
            continue
        doc_id, facts = requirement["guide_id"], requirement["facts"]
        if not isinstance(doc_id, str) or doc_id not in expected or doc_id in covered or not isinstance(facts, list) or not facts:
            diagnostics.append("source-fact-requirement")
            continue
        covered.add(doc_id)
        reviewed_revision = requirement.get("reviewed_revision", default_revision)
        if not isinstance(reviewed_revision, str) or reviewed_revision not in approved_revisions:
            diagnostics.append("source-fact-revision: guide revision is not approved")
            continue
        entry = expected[doc_id]
        if not isinstance(entry, dict):
            diagnostics.append("source-fact-requirement")
            continue
        text = visible_control_procedure_text((docs_root / entry["target"]).read_text(encoding="utf-8"))
        for fact in facts:
            if not isinstance(fact, dict) or not required_fact_keys <= set(fact) or set(fact) - (required_fact_keys | {"reviewed_revision"}):
                diagnostics.append("source-fact-shape")
                continue
            if fact.get("reviewed_revision", reviewed_revision) != reviewed_revision:
                diagnostics.append("source-fact-revision: fact revision differs from guide revision")
                continue
            values = [fact[key] for key in required_fact_keys - {"visible"}]
            variants = fact["visible"]
            if not all(isinstance(value, str) and value for value in values) or not isinstance(variants, list) or not variants:
                diagnostics.append("source-fact-shape")
                continue
            if all(isinstance(check, dict) for check in variants):
                validate_typed_visible_checks(entry["target"], fact, text, diagnostics)
                continue
            positions: list[int] = []
            for alternatives in variants:
                if not isinstance(alternatives, list) or not alternatives or not all(isinstance(value, str) and value for value in alternatives):
                    diagnostics.append("source-fact-shape")
                    break
                position = next((visible_phrase_position(text, value) for value in alternatives if visible_phrase_position(text, value) >= 0), -1)
                positions.append(position)
            else:
                if any(position < 0 for position in positions):
                    diagnostics.append(f"source-fact-visible-coverage: {entry['target']} lacks {fact['id']}")
                elif list_visible_route_requires_order(fact):
                    ordered_positions = [
                        next((visible_exact_phrase_position(text, value) for value in alternatives if visible_exact_phrase_position(text, value) >= 0), position)
                        for alternatives, position in zip(variants, positions)
                    ]
                    steps = visible_step_positions(text, ordered_positions)
                    if steps != sorted(steps):
                        diagnostics.append(f"source-fact-visible-order: {entry['target']} lacks {fact['id']}")
    pending_ids = {item for item in pending if isinstance(item, str)}
    if len(pending_ids) != len(pending) or covered | pending_ids != set(expected) or covered & pending_ids:
        diagnostics.append("source-fact-coverage: every active guide must be inspected or explicitly pending")
    elif pending_ids:
        diagnostics.append("source-fact-incomplete: all active guides require source-first requirements")


def control_procedure_text(text: str) -> str:
    """Limit token checks to the access and action flow, not incidental guide prose."""
    sections = []
    for heading in ("Cómo acceder", "Pasos"):
        match = re.search(rf"## {re.escape(heading)}\n\n(.*?)(?=\n## |\Z)", text, re.S)
        if match:
            sections.append(match.group(1))
    return "\n".join(sections)


def visible_control_procedure_text(text: str) -> str:
    """Exclude comments and HTML-only aliases before checking reader-visible instructions."""
    return re.sub(r"<[^>]+>", "", re.sub(r"<!--.*?-->", "", control_procedure_text(text), flags=re.S))


def visible_phrase_position(text: str, phrase: str) -> int:
    position = text.casefold().find(phrase.casefold())
    if position >= 0:
        return position
    # Localized inflections such as "guarde" and "guardado" are the same UI action,
    # but labels and multiword controls still require their complete visible phrase.
    if " " not in phrase and len(phrase) >= 5:
        return text.casefold().find(phrase.casefold()[:5])
    return -1


def visible_exact_phrase_position(text: str, phrase: str) -> int:
    match = re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.I)
    return match.start() if match else -1


def list_visible_route_requires_order(fact: dict[str, object]) -> bool:
    """Order record-detail menu routes without parsing word order in one action sentence."""
    route = f"{fact['container']} {fact['reveal']}".casefold()
    variants = fact["visible"]
    visible_reveal = any(
        any(marker in alternative.casefold() for marker in ("menú", "menu", "opciones", "puntos"))
        for alternatives in variants
        for alternative in alternatives
    )
    visible_record_open = any(
        any(marker in alternative.casefold() for marker in ("doble clic", "fila"))
        for alternatives in variants
        for alternative in alternatives
    )
    return visible_reveal and visible_record_open and any(marker in route for marker in ("menu", "dropdown", "ellipsis"))


def visible_step_positions(text: str, positions: list[int]) -> list[int]:
    """Compare interaction steps, not incidental word order within one instruction."""
    starts = [match.start() for match in re.finditer(r"^\d+\. ", text, re.M)]
    return [sum(start <= position for start in starts) for position in positions]


def validate_typed_visible_checks(target: str, fact: dict[str, object], text: str, diagnostics: list[str]) -> None:
    """Require the reader-visible route for source-owned, multi-step UI actions."""
    checks = fact["visible"]
    kind = typed_ui_kind(fact)
    required_dimensions = {
        "dropdown_action": ("owner", "reveal", "control", "next_state"),
        "row_open": ("gesture", "row", "next_state"),
        "direct_form": ("scope", "control"),
    }
    expected = required_dimensions.get(kind)
    if expected is None or len(checks) != len(expected):
        diagnostics.append(f"source-fact-typed-shape: {target} lacks {fact['id']}")
        return
    position = -1
    for check, dimension in zip(checks, expected):
        if set(check) != {"dimension", "alternatives"} or check["dimension"] != dimension:
            diagnostics.append(f"source-fact-typed-shape: {target} lacks {fact['id']}")
            return
        alternatives = check["alternatives"]
        if not isinstance(alternatives, list) or not alternatives or not all(isinstance(value, str) and value for value in alternatives):
            diagnostics.append(f"source-fact-typed-shape: {target} lacks {fact['id']}")
            return
        matches = [visible_phrase_position(text, value) for value in alternatives]
        next_position = next((value for value in matches if value > position), -1)
        if next_position < 0:
            diagnostics.append(f"source-fact-visible-coverage: {target} lacks {fact['id']} {dimension}")
            return
        position = next_position


def typed_ui_kind(fact: dict[str, object]) -> str:
    container = str(fact["container"]).casefold()
    gesture = str(fact["gesture"]).casefold()
    if "menu" in container or "dropdown" in container:
        return "dropdown_action"
    if "row" in container or "doble clic" in gesture:
        return "row_open"
    return "direct_form"


def intro_after_h1(text: str) -> bool:
    match = re.search(r"^# .+?\n+([^#\n][^\n]*)", text, re.MULTILINE)
    return bool(match and match.group(1).strip())


def contract_entries(contract: Path, diagnostics: list[str]) -> list[tuple[str, str, str]]:
    if not contract.is_file():
        return []
    entries: list[tuple[str, str, str]] = []
    number: str | None = None
    group: str | None = None
    expected_count: int | None = None
    count = 0
    for line in contract.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if group is not None and count != expected_count:
                diagnostics.append("contract-group-count")
            number = group = None
            expected_count = None
            continue
        heading = re.match(r"^### (\d+)\. (.+) \((\d+)\)$", line)
        if heading:
            if group is not None and count != expected_count:
                diagnostics.append("contract-group-count")
            number, group, expected_count_text = heading.groups()
            expected_count = int(expected_count_text)
            count = 0
            continue
        item = re.match(r"^- (.+)\.$", line)
        if item and number is not None and group is not None:
            count += 1
            entries.append((f"{number}.{count}", item.group(1), group))
    if group is not None and count != expected_count:
        diagnostics.append("contract-group-count")
    return entries


def contract_entries_v2(contract: Path, diagnostics: list[str]) -> list[tuple[str, str, str]]:
    """Parse the authorized V2 table catalog, not the retired V1 bullet contract."""
    if not contract.is_file():
        diagnostics.append("missing-contract: task-oriented-manual-contract-v2.md")
        return []
    entries: list[tuple[str, str, str]] = []
    group: str | None = None
    expected_count: int | None = None
    count = 0
    for line in contract.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if group is not None and count != expected_count:
                diagnostics.append("contract-group-count")
            group = None
            expected_count = None
            count = 0
            continue
        heading = re.match(r"^### (.+) \((\d+)\)$", line)
        if heading:
            if group is not None and count != expected_count:
                diagnostics.append("contract-group-count")
            group, expected_text = heading.groups()
            expected_count = int(expected_text)
            count = 0
            continue
        if group is None or not line.startswith("|") or line.startswith("| ---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "Tarea propuesta":
            continue
        count += 1
        entries.append((f"{len({item[2] for item in entries if item[2] != group}) + 1}.{count}", cells[0], group))
    if group is not None and count != expected_count:
        diagnostics.append("contract-group-count")
    return entries


def validate_compatibility(
    root: Path,
    docs_root: Path,
    compatibility: dict[str, object],
    active: list[object],
    diagnostics: list[str],
    audit: bool,
) -> None:
    records = compatibility.get("records")
    if not isinstance(records, list):
        diagnostics.append("compatibility-records: explicit legacy records are required")
        return
    frozen_base = compatibility.get("frozen_legacy_base")
    expected_explicit = compatibility.get("legacy_explicit_fragment_count")
    expected_historical = compatibility.get("legacy_historical_fragment_count")
    if not isinstance(frozen_base, str) or not SHA_PATTERN.fullmatch(frozen_base):
        diagnostics.append("compatibility-frozen-base: immutable legacy revision is required")
    if expected_explicit != 352:
        diagnostics.append("legacy-explicit-anchor-coverage: expected preserved 352 explicit fragments")
    if expected_historical != 1320:
        diagnostics.append("legacy-historical-anchor-coverage: expected frozen historical fragment total")
    paths: set[str] = set()
    explicit_by_path: set[tuple[str, str]] = set()
    historical_by_path: set[tuple[str, str]] = set()
    explicit_count = 0
    historical_count = 0
    for record in records:
        if not isinstance(record, dict):
            diagnostics.append("invalid-compatibility-record")
            continue
        path, target = record.get("path"), record.get("target")
        explicit, historical = record.get("fragments"), record.get("historical_fragments")
        if not isinstance(path, str) or not isinstance(target, str) or not isinstance(explicit, list) or not isinstance(historical, list):
            diagnostics.append("invalid-compatibility-record")
            continue
        if path in paths:
            diagnostics.append("duplicate-legacy-path")
        paths.add(path)
        if not is_within((docs_root / path).resolve(), docs_root.resolve()) or not is_within((docs_root / target).resolve(), docs_root.resolve()):
            diagnostics.append("unsafe-legacy-path")
            continue
        source, destination = docs_root / path, docs_root / target
        if not source.is_file() or not destination.is_file():
            diagnostics.append("legacy-target: path or target is missing")
            continue
        source_anchors = anchor_ids(source.read_text(encoding="utf-8"))
        explicit_set: set[str] = set()
        historical_set: set[str] = set()
        for alias in explicit:
            if isinstance(alias, str) and (path, alias) in explicit_by_path:
                diagnostics.append("duplicate-legacy-fragment")
            if isinstance(alias, str):
                explicit_by_path.add((path, alias))
                explicit_set.add(alias)
            explicit_count += 1
        for alias in historical:
            if isinstance(alias, str) and (path, alias) in historical_by_path:
                diagnostics.append("duplicate-historical-fragment")
            if isinstance(alias, str):
                historical_by_path.add((path, alias))
                historical_set.add(alias)
            if not isinstance(alias, str) or alias not in source_anchors:
                diagnostics.append("legacy-historical-anchor: exact fragment does not resolve")
            historical_count += 1
        if not explicit_set <= historical_set:
            diagnostics.append("legacy-explicit-subset: explicit fragments must remain historical aliases")
    if len(paths) != 88:
        diagnostics.append("legacy-path-coverage: expected all 88 baseline paths")
    if explicit_count != expected_explicit:
        diagnostics.append("legacy-explicit-anchor-coverage: preserved explicit fragment count differs")
    if historical_count != expected_historical:
        diagnostics.append("legacy-historical-anchor-coverage: frozen historical fragment count differs")
    if audit and isinstance(frozen_base, str) and SHA_PATTERN.fullmatch(frozen_base) and frozen_base_available(root, frozen_base):
        for record in records:
            if not isinstance(record, dict) or not isinstance(record.get("path"), str) or not isinstance(record.get("historical_fragments"), list):
                continue
            if legacy_fragments(root, frozen_base, record["path"]) != record["historical_fragments"]:
                diagnostics.append("legacy-baseline-fragments: frozen historical fragments differ")
    indexes = compatibility.get("indexes")
    if not isinstance(indexes, list) or not all(isinstance(path, str) for path in indexes):
        diagnostics.append("compatibility-indexes: explicit index classification is required")
        return
    if len(indexes) != len(set(indexes)):
        diagnostics.append("duplicate-index-path")
    active_paths = {entry.get("target") for entry in active if isinstance(entry, dict)}
    progress = load(root / "documentation/task-manual-v2-progress.yml", diagnostics)
    drafts: set[str] = set()
    if isinstance(progress, dict):
        guides = progress.get("guides")
        if isinstance(guides, list):
            for guide in guides:
                if isinstance(guide, dict) and guide.get("status") == "drafted" and isinstance(guide.get("path"), str):
                    drafts.add(guide["path"])
    inactive = compatibility.get("inactive", [])
    if not isinstance(inactive, list) or not all(isinstance(path, str) for path in inactive):
        diagnostics.append("compatibility-inactive: explicit inactive classification is required")
        return
    if len(inactive) != len(set(inactive)):
        diagnostics.append("duplicate-inactive-path")
    if (paths | active_paths | drafts) & (set(indexes) | set(inactive)):
        diagnostics.append("invalid-markdown-classification")
    classified = paths | active_paths | drafts | set(indexes) | set(inactive)
    for file in docs_root.rglob("*.md"):
        if file.relative_to(docs_root).as_posix() not in classified:
            diagnostics.append("unclassified-markdown: every page must be active, compatible, or indexed")
    search_hidden = compatibility.get("search_hidden")
    compatibility_only = paths - active_paths
    if not isinstance(search_hidden, list) or set(search_hidden) != compatibility_only or len(search_hidden) != len(set(search_hidden)):
        diagnostics.append("compatibility-search-hidden: every compatibility-only page must be declared")
        return
    for path in compatibility_only:
        if not search_excluded((docs_root / path).read_text(encoding="utf-8")):
            diagnostics.append(f"compatibility-search-hidden: {path} must be excluded from search")
    for path in active_paths:
        if isinstance(path, str) and search_excluded((docs_root / path).read_text(encoding="utf-8")):
            diagnostics.append(f"active-search-hidden: {path} is an active canonical target")
    validate_searchable_references(root, docs_root, active_paths, paths, diagnostics)


def validate_searchable_references(
    root: Path, docs_root: Path, active_paths: set[object], compatibility_paths: set[str], diagnostics: list[str]
) -> None:
    baseline = load(root / "documentation/v1-rendered-baseline.yml", diagnostics)
    records = baseline.get("records", []) if isinstance(baseline, dict) else []
    historical_tasks = {
        record.get("path") for record in records
        if isinstance(record, dict) and isinstance(record.get("path"), str)
    }
    blocked = (compatibility_paths | historical_tasks) - {path for path in active_paths if isinstance(path, str)}
    for source in docs_root.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        if search_excluded(text):
            continue
        for raw_target in re.findall(r"(?<!!)\[[^]]*\]\(([^)\s]+)", text) + re.findall(r"href=[\"']([^\"'#?]+)", text):
            target_path = raw_target.partition("#")[0]
            if not target_path or re.match(r"[a-z][a-z0-9+.-]*:", target_path, re.IGNORECASE):
                continue
            target = resolve_target(source, docs_root, target_path)
            if target is not None and target.relative_to(docs_root.resolve()).as_posix() in blocked:
                diagnostics.append(f"searchable-held-link: {source.relative_to(docs_root).as_posix()}")


def validate_v1_rendered_baseline(root: Path, docs_root: Path, diagnostics: list[str]) -> None:
    baseline = load(root / "documentation/v1-rendered-baseline.yml", diagnostics)
    if not isinstance(baseline, dict) or baseline.get("schema_version") != 1 or baseline.get("kind") != "current_v1_rendered_baseline":
        diagnostics.append("v1-baseline-schema")
        return
    records = baseline.get("records")
    if not isinstance(records, list) or len(records) != 78:
        diagnostics.append("v1-baseline-records: expected 78 captured V1 routes")
        return
    paths: set[str] = set()
    raw_count = chrome_count = content_count = 0
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("path"), str) or not isinstance(record.get("fragments"), list):
            diagnostics.append("v1-baseline-record")
            continue
        path = record["path"]
        if path in paths:
            diagnostics.append("v1-baseline-duplicate-route")
        paths.add(path)
        fragments = record["fragments"]
        if len(fragments) != len(set(fragments)) or not all(isinstance(fragment, str) for fragment in fragments):
            diagnostics.append("v1-baseline-duplicate-fragment")
        raw_count += len(fragments)
        content = [fragment for fragment in fragments if not fragment.startswith("__")]
        chrome_count += len(fragments) - len(content)
        content_count += len(content)
        source = docs_root / path
        if not source.is_file() or not set(content) <= anchor_ids(source.read_text(encoding="utf-8")):
            diagnostics.append(f"v1-rendered-anchor: {path} is missing a captured V1 content id")
    if (raw_count, chrome_count, content_count) != (3548, 2496, 1052):
        diagnostics.append("v1-baseline-counts: expected 3548 raw, 2496 Material chrome, and 1052 reader ids")


def search_excluded(text: str) -> bool:
    if not text.startswith("---\n"):
        return False
    _, separator, remainder = text[4:].partition("\n---\n")
    if not separator:
        return False
    metadata = yaml.safe_load(text[4:4 + len(text[4:]) - len(remainder) - len(separator)])
    return isinstance(metadata, dict) and isinstance(metadata.get("search"), dict) and metadata["search"].get("exclude") is True


def validate_inventory(root: Path, active: list[object], diagnostics: list[str]) -> None:
    inventory = load(root / "documentation/inventory.yml", diagnostics)
    if not isinstance(inventory, dict) or inventory.get("schema_version") != 3:
        diagnostics.append("inventory-schema: schema_version 3 is required")
        return
    documents = inventory.get("documents")
    if not isinstance(documents, list):
        diagnostics.append("inventory-documents: active document records are required")
        return
    expected = {
        (entry["doc_id"], entry["target"], entry["title"], entry["group"], tuple(entry["capability_ids"]))
        for entry in active
        if isinstance(entry, dict)
        and all(isinstance(entry.get(key), str) for key in ("doc_id", "target", "title", "group"))
        and isinstance(entry.get("capability_ids"), list)
    }
    actual: set[tuple[object, ...]] = set()
    ids: set[str] = set()
    paths: set[str] = set()
    for document in documents:
        if not isinstance(document, dict):
            diagnostics.append("invalid-document: active document record must be a mapping")
            continue
        doc_id, path, title, group, capability_ids = (
            document.get(key) for key in ("doc_id", "path", "title", "group", "capability_ids")
        )
        if not all(isinstance(value, str) and value for value in (doc_id, path, title, group)) or not isinstance(capability_ids, list):
            diagnostics.append("invalid-document: doc_id, path, title, group, and capability_ids are required")
            continue
        if doc_id in ids:
            diagnostics.append("duplicate-doc-id")
        if path in paths:
            diagnostics.append("duplicate-path")
        ids.add(doc_id)
        paths.add(path)
        if not is_within((root / "docs" / path).resolve(), (root / "docs").resolve()):
            diagnostics.append("unsafe-document-path")
        actual.add((doc_id, path, title, group, tuple(capability_ids)))
    if actual != expected:
        diagnostics.append("inventory-parity: active registry and inventory differ")


def validate_active_continuations(
    docs_root: Path, active: list[object], compatibility: dict[str, object], diagnostics: list[str]
) -> None:
    records = compatibility.get("records")
    if not isinstance(records, list):
        return
    active_paths = {entry.get("target") for entry in active if isinstance(entry, dict)}
    compatibility_only = {
        record.get("path") for record in records
        if isinstance(record, dict) and isinstance(record.get("path"), str) and record.get("path") not in active_paths
    }
    for entry in active:
        if not isinstance(entry, dict) or not isinstance(entry.get("target"), str):
            continue
        source = docs_root / entry["target"]
        if not source.is_file():
            continue
        for _, raw_target in MARKDOWN_LINK.findall(source.read_text(encoding="utf-8")):
            parts = raw_target.strip().split(maxsplit=1)
            if not parts:
                continue
            target_path = parts[0].partition("#")[0]
            target = resolve_target(source, docs_root, target_path) if target_path else source
            if target is not None and target.relative_to(docs_root.resolve()).as_posix() in compatibility_only:
                diagnostics.append(f"active-compat-continuation: {entry['target']} points to a compatibility-only page")


def validate_technical_metadata(root: Path, active: list[object], final: bool, diagnostics: list[str]) -> None:
    inventory = load(root / "documentation/inventory.yml", diagnostics)
    checkpoint = load(root / "documentation/source-checkpoint.yml", diagnostics)
    catalog = load(root / "documentation/capability-dispositions.yml", diagnostics)
    if not isinstance(inventory, dict) or not isinstance(checkpoint, dict) or not isinstance(catalog, dict):
        diagnostics.append("invalid-metadata-shape")
        return
    source_revision = checkpoint.get("source_revision")
    sync = checkpoint.get("source_sync")
    if not isinstance(source_revision, str) or not SHA_PATTERN.fullmatch(source_revision) or not isinstance(sync, dict):
        diagnostics.append("checkpoint-source-revision")
        return
    completed, target, pending = sync.get("completed"), sync.get("target"), sync.get("pending")
    if not isinstance(completed, dict) or completed.get("source_commit") != source_revision:
        diagnostics.append("checkpoint-completed-revision")
    target_revision = target.get("source_commit") if isinstance(target, dict) else None
    if not isinstance(target_revision, str) or not SHA_PATTERN.fullmatch(target_revision):
        diagnostics.append("checkpoint-target-revision")
    if not isinstance(pending, dict) or pending.get("count") != 332:
        diagnostics.append("checkpoint-pending-range")
    ranges = sync.get("range_audit")
    if not isinstance(ranges, dict) or ranges.get("total_paths") != 332 or ranges.get("target_commit") != target_revision:
        diagnostics.append("checkpoint-range-audit")
    if checkpoint.get("source_review_status") != "source_reviewed_draft" or checkpoint.get("runtime_status") != "pending_runtime_verification" or checkpoint.get("deployed_parity_status") != "pending_runtime_verification":
        diagnostics.append("checkpoint-states")
    validate_catalog(catalog, checkpoint, active, diagnostics)
    documents = inventory.get("documents")
    bases = inventory.get("scoped_source_bases")
    if inventory.get("active_content_revision") != target_revision[:6]:
        diagnostics.append("active-content-revision")
    if not isinstance(documents, list) or not isinstance(bases, list):
        diagnostics.append("inventory-metadata-shape")
        return
    base_by_doc = {base.get("doc_id"): base for base in bases if isinstance(base, dict) and isinstance(base.get("doc_id"), str)}
    if len(base_by_doc) != len(bases):
        diagnostics.append("invalid-scoped-source-basis")
    for document in documents:
        if not isinstance(document, dict):
            continue
        doc_id = document.get("doc_id")
        for key, expected in (
            ("content_status", "source_backed_enriched"),
            ("source_review_status", "source_reviewed_draft"),
            ("runtime_status", "pending_runtime_verification"),
            ("deployed_parity_status", "pending_runtime_verification"),
            ("source_revision", source_revision),
        ):
            if document.get(key) != expected:
                diagnostics.append(f"invalid-document-status: {key}")
        scoped = document.get("scoped_source_basis")
        if scoped is not None:
            basis = base_by_doc.get(doc_id)
            if not isinstance(scoped, str) or scoped != target_revision or not isinstance(basis, dict) or basis.get("reviewed_revision") != target_revision:
                diagnostics.append("invalid-scoped-source-basis")
        evidence = document.get("procedure_evidence")
        if evidence is not None:
            allowed = {
                "browser_screen", "browser_control", "browser_screen_and_limited_source",
                "source_derived_modal_and_table_controls", "source_derived_modal_and_overflow_controls",
                "source_derived_table_and_overflow_controls", "source_derived_crud_form",
            }
            if not isinstance(evidence, dict) or set(evidence) != {"source_basis", "reviewed_revision", "runtime_execution"} or evidence.get("source_basis") not in allowed or evidence.get("reviewed_revision") != target_revision or evidence.get("runtime_execution") != "not_performed":
                diagnostics.append("invalid-procedure-evidence")
    if sum(isinstance(document, dict) and document.get("procedure_evidence") is not None for document in documents) != 19:
        diagnostics.append("procedure-evidence-coverage: expected 19 bounded source records")
    if set(base_by_doc) != {document.get("doc_id") for document in documents if isinstance(document, dict) and document.get("scoped_source_basis") is not None}:
        diagnostics.append("scoped-source-basis-parity")
    if final and checkpoint.get("scope_state") != "scope_complete":
        diagnostics.append("scope-state")


def validate_catalog(catalog: dict[str, object], checkpoint: dict[str, object], active: list[object], diagnostics: list[str]) -> None:
    capabilities = catalog.get("capabilities")
    if catalog.get("schema_version") != 2 or not isinstance(capabilities, list):
        diagnostics.append("catalog-schema")
        return
    by_id: dict[str, dict[str, object]] = {}
    documented_ids: set[str] = set()
    owner_excluded: set[str] = set()
    out_of_scope: set[str] = set()
    gaps: set[str] = set()
    rules = {
        "core": {"documented", "owner_excluded_from_documentation"},
        "conditional": {"documented", "owner_excluded_from_documentation", "out_of_current_menu_scope", "not_enabled_for_documented_scope"},
        "uncertain": {"coverage_gap"},
        "internal_not_public": {"internal_not_public"},
    }
    historical_documents = checkpoint.get("document_ids")
    if not isinstance(historical_documents, list) or len(historical_documents) != len(set(historical_documents)) or not all(isinstance(value, str) for value in historical_documents):
        diagnostics.append("checkpoint-historical-document-ids")
        historical_documents = []
    for capability in capabilities:
        if not isinstance(capability, dict) or not isinstance(capability.get("id"), str):
            diagnostics.append("invalid-capability")
            continue
        capability_id = capability["id"]
        if capability_id in by_id:
            diagnostics.append("duplicate-capability-id")
        by_id[capability_id] = capability
        classification, disposition = capability.get("classification"), capability.get("disposition")
        if disposition not in rules.get(classification, set()):
            diagnostics.append("illegal-disposition")
        canonical = capability.get("canonical_doc_id")
        if disposition == "documented":
            if not isinstance(canonical, str) or canonical not in historical_documents:
                diagnostics.append("canonical-doc-id")
            documented_ids.add(capability_id)
        elif canonical is not None:
            diagnostics.append("noncanonical-disposition")
        if disposition == "owner_excluded_from_documentation":
            if capability.get("reason_category") != "owner_scope_exclusion":
                diagnostics.append("excluded-capability-reason")
            owner_excluded.add(capability_id)
        if disposition == "out_of_current_menu_scope":
            if capability.get("reason_category") != "legacy_menu_not_in_current_scope":
                diagnostics.append("out-of-scope-capability-reason")
            out_of_scope.add(capability_id)
        if disposition == "coverage_gap":
            gaps.add(capability_id)
    expected_owner = checkpoint_ids(checkpoint.get("exclusions"), "owner_scope_exclusion", diagnostics)
    expected_scope = checkpoint_ids(checkpoint.get("out_of_current_menu_scope"), "legacy_menu_not_in_current_scope", diagnostics)
    expected_gaps = checkpoint_ids(checkpoint.get("gaps"), "browser_workflow_not_proven", diagnostics)
    if owner_excluded != expected_owner:
        diagnostics.append("owner-exclusion-parity")
    if out_of_scope != expected_scope:
        diagnostics.append("out-of-scope-parity")
    if gaps != expected_gaps:
        diagnostics.append("coverage-gap-parity")
    for entry in active:
        if not isinstance(entry, dict):
            continue
        for capability_id in entry.get("capability_ids", []):
            capability = by_id.get(capability_id)
            if not isinstance(capability, dict) or capability.get("disposition") != "documented" or capability.get("canonical_doc_id") != entry.get("doc_id"):
                diagnostics.append("active-capability-parity")


def checkpoint_ids(value: object, reason: str, diagnostics: list[str]) -> set[str]:
    if not isinstance(value, list):
        diagnostics.append("invalid-checkpoint-disposition")
        return set()
    if not all(isinstance(item, dict) and isinstance(item.get("id"), str) and isinstance(item.get("reason_category"), str) for item in value):
        diagnostics.append("invalid-checkpoint-disposition")
    ids = {item["id"] for item in value if isinstance(item, dict) and item.get("reason_category") == reason and isinstance(item.get("id"), str)}
    return ids


def validate_legacy_manual(root: Path, docs_root: Path, final: bool, diagnostics: list[str]) -> ValidationReport:
    """Validate preserved pre-v2 fixtures without applying the active task contract."""
    inventory = load(root / "documentation/inventory.yml", diagnostics)
    catalog = load(root / "documentation/capability-dispositions.yml", diagnostics)
    checkpoint = load(root / "documentation/source-checkpoint.yml", diagnostics)
    config = load(root / "mkdocs.yml", diagnostics)
    if not all(isinstance(value, dict) for value in (inventory, catalog, checkpoint, config)):
        diagnostics.append("invalid-metadata-shape")
        return ValidationReport(0, tuple(diagnostics))
    documents = inventory.get("documents")
    capabilities = catalog.get("capabilities")
    if inventory.get("schema_version") != 2 or not isinstance(documents, list) or not isinstance(capabilities, list):
        diagnostics.append("legacy-schema")
        return ValidationReport(0, tuple(diagnostics))
    document_ids: set[str] = set()
    document_paths: set[str] = set()
    inventory_ids: set[str] = set()
    for document in documents:
        if not isinstance(document, dict):
            diagnostics.append("invalid-document")
            continue
        doc_id, path, capability_ids = document.get("doc_id"), document.get("path"), document.get("capability_ids")
        if not isinstance(doc_id, str) or not isinstance(path, str) or not isinstance(capability_ids, list):
            diagnostics.append("invalid-document")
            continue
        if doc_id in document_ids:
            diagnostics.append("duplicate-doc-id")
        if path in document_paths:
            diagnostics.append("duplicate-path")
        document_ids.add(doc_id)
        document_paths.add(path)
        if not is_within((docs_root / path).resolve(), docs_root.resolve()):
            diagnostics.append("unsafe-document-path")
        for capability_id in capability_ids:
            if not isinstance(capability_id, str):
                diagnostics.append("invalid-capability-id")
            elif capability_id in inventory_ids:
                diagnostics.append("duplicate-capability-id")
            else:
                inventory_ids.add(capability_id)
        if final and document.get("content_status") == "pending_enrichment":
            diagnostics.append("pending-enrichment")
    files = {path.relative_to(docs_root).as_posix() for path in docs_root.rglob("*.md") if path.name != "index.md"}
    if files != document_paths:
        diagnostics.append("file-parity")
    nav_paths = {path for _, path in nav_entries(config.get("nav")) if not path.endswith("index.md")}
    if nav_paths != files:
        diagnostics.append("nav-parity")
    validate_legacy_numbering(config.get("nav"), docs_root, diagnostics)
    validate_legacy_catalog(capabilities, document_ids, inventory_ids, checkpoint, diagnostics)
    for path in docs_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        label = path.relative_to(root).as_posix()
        if path.name != "index.md":
            for section in LEGACY_REQUIRED_SECTIONS:
                if f"## {section}" not in text:
                    diagnostics.append(f"required-section: {label} lacks {section}")
        validate_links(text, path, docs_root, label, diagnostics)
        validate_privacy(text, label, diagnostics)
        if raw_status_tokens(text):
            diagnostics.append(f"raw-reader-status: {label}")
    return ValidationReport(len(files), tuple(diagnostics), len(documents), tuple(sorted(inventory_ids)))


def validate_legacy_catalog(capabilities: list[object], documents: set[str], inventory_ids: set[str], checkpoint: dict[str, object], diagnostics: list[str]) -> None:
    catalog_ids: set[str] = set()
    documented_ids: set[str] = set()
    for capability in capabilities:
        if not isinstance(capability, dict) or not isinstance(capability.get("id"), str):
            diagnostics.append("invalid-capability")
            continue
        capability_id = capability["id"]
        if capability_id in catalog_ids:
            diagnostics.append("duplicate-capability-id")
        catalog_ids.add(capability_id)
        disposition, canonical = capability.get("disposition"), capability.get("canonical_doc_id")
        if disposition == "documented":
            if canonical not in documents:
                diagnostics.append("canonical-doc-id")
            documented_ids.add(capability_id)
        if disposition == "owner_excluded_from_documentation" and (canonical is not None or capability_id in inventory_ids):
            diagnostics.append("excluded-capability-document")
    if documented_ids != inventory_ids:
        diagnostics.append("catalog-inventory-parity")
    if checkpoint.get("document_ids") != sorted(documents):
        diagnostics.append("checkpoint-parity")


def validate_legacy_numbering(nav: object, docs_root: Path, diagnostics: list[str]) -> None:
    if not isinstance(nav, list):
        diagnostics.append("numbering-nav")
        return
    if not any(isinstance(entry, dict) and len(entry) == 1 and isinstance(next(iter(entry)), str) and re.match(r"^\d+\. ", next(iter(entry))) for entry in nav):
        return
    for chapter, entry in enumerate(nav, start=1):
        if not isinstance(entry, dict) or len(entry) != 1:
            diagnostics.append("numbering-nav")
            continue
        label, children = next(iter(entry.items()))
        if not isinstance(label, str) or not label.startswith(f"{chapter}. "):
            diagnostics.append("numbering-chapter")
        ordinal = 0
        for guide_label, path in nav_entries(children):
            if path.endswith("index.md"):
                continue
            ordinal += 1
            expected = f"{chapter}.{ordinal} "
            if not guide_label.startswith(expected):
                diagnostics.append("numbering-nav")
            guide = docs_root / path
            if guide.is_file() and not guide.read_text(encoding="utf-8").startswith(f"# {chapter}.{ordinal} "):
                diagnostics.append("numbering-h1")


def is_within(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def validate_navigation(root: Path, active: list[object], diagnostics: list[str]) -> None:
    config = load(root / "mkdocs.yml", diagnostics)
    nav = config.get("nav") if isinstance(config, dict) else None
    expected = [(f"{entry['number']} {entry['title']}", entry["target"]) for entry in active if isinstance(entry, dict)]
    actual = nav_entries(nav)
    actual = [(label, path) for label, path in actual if path != "index.md"]
    if actual != expected:
        diagnostics.append("nav-parity: navigation titles, numbers, or paths differ from active registry")
    migration = load(root / "documentation/task-manual-migration.yml", diagnostics)
    group_indexes = migration.get("group_indexes", {}) if isinstance(migration, dict) else {}
    validate_home_navigation(root / "docs" / "index.md", active, config, group_indexes, diagnostics)


def published_url(target: str, use_directory_urls: bool) -> str:
    path = Path(target)
    if use_directory_urls:
        stem = path.with_suffix("")
        return f"{stem.parent.as_posix()}/" if stem.name == "index" else f"{stem.as_posix()}/"
    return path.with_suffix(".html").as_posix()


def validate_home_navigation(home: Path, active: list[object], config: object, group_indexes: object, diagnostics: list[str]) -> None:
    if not home.is_file():
        diagnostics.append("home-navigation: home page is missing")
        return
    text = home.read_text(encoding="utf-8")
    compatibility = {"recorridos/", "caja/", "configuracion/", "especializados/", "reportes/", "reportes-especializados/"}
    use_directory_urls = config.get("use_directory_urls", True) if isinstance(config, dict) else True
    active_indexes: set[str] = set()
    active_urls: set[str] = set()
    seen_groups: set[str] = set()
    explicit_indexes = group_indexes if isinstance(group_indexes, dict) else {}
    for entry in active:
        if isinstance(entry, dict) and isinstance(entry.get("group"), str) and isinstance(entry.get("target"), str):
            active_urls.add(published_url(entry["target"], use_directory_urls))
            if entry["group"] not in seen_groups:
                index = explicit_indexes.get(entry["group"], str(Path(entry["target"]).parent / "index.md"))
                active_indexes.add(published_url(str(index), use_directory_urls))
                seen_groups.add(entry["group"])
    links = re.findall(r"href=[\"']([^\"'#?]+)", text)
    if any(link.startswith(prefix) for link in links for prefix in compatibility):
        diagnostics.append("home-compat-navigation: home task navigation points to a compatibility area")
    if not active_indexes <= set(links):
        diagnostics.append("home-group-coverage: home page must link to every active group")
    if any(link.endswith(".md") or link not in active_urls | active_indexes for link in links):
        diagnostics.append("home-published-url: home cards must use canonical published URLs")
    if re.search(r"\b18 áreas\b|\bsiete recorridos\b", text, re.IGNORECASE):
        diagnostics.append("home-legacy-coverage-claim")


def validate_indexes(docs_root: Path, active: list[object], group_indexes: object, diagnostics: list[str]) -> None:
    explicit_indexes = group_indexes if isinstance(group_indexes, dict) else {}
    groups: dict[str, list[dict[str, str]]] = {}
    for entry in active:
        if isinstance(entry, dict):
            groups.setdefault(entry["group"], []).append(entry)
    for group, entries in groups.items():
        configured = explicit_indexes.get(group)
        index = docs_root / (configured if isinstance(configured, str) else Path(entries[0]["target"]).parent / "index.md")
        if not index.is_file():
            diagnostics.append("index-parity: group index is missing")
            continue
        text = index.read_text(encoding="utf-8")
        actual = []
        for label, link in re.findall(r"(?<!!)\[([^]]+)\]\(([^)\s]+)", text):
            target = resolve_target(index, docs_root, link)
            if target is not None:
                actual.append((label, target.relative_to(docs_root.resolve()).as_posix()))
        expected = [(f"{entry['number']} {entry['title']}", entry["target"]) for entry in entries]
        if actual != expected:
            diagnostics.append("index-parity: titles, numbers, or paths differ from active registry")


def nav_entries(value: object) -> list[tuple[str, str]]:
    if isinstance(value, list):
        return [item for child in value for item in nav_entries(child)]
    if isinstance(value, dict):
        entries: list[tuple[str, str]] = []
        for label, child in value.items():
            if isinstance(label, str) and isinstance(child, str):
                entries.append((label, child))
            else:
                entries.extend(nav_entries(child))
        return entries
    return []


def validate_links(text: str, source: Path, docs_root: Path, label: str, diagnostics: list[str]) -> None:
    for label_text, raw_target in MARKDOWN_LINK.findall(text):
        if not label_text.strip():
            diagnostics.append(f"bare-link: {label}")
        target = raw_target.strip().split(maxsplit=1)[0] if raw_target.strip() else ""
        if not target:
            diagnostics.append(f"empty-link: {label}")
            continue
        target_path, _, anchor = target.partition("#")
        if re.match(r"[a-z][a-z0-9+.-]*:", target_path, re.IGNORECASE):
            if target_path.lower().startswith("file:"):
                diagnostics.append(f"unsafe-link-scheme: {label}")
            continue
        candidate = source if not target_path else resolve_target(source, docs_root, target_path)
        if candidate is None or not candidate.is_file():
            diagnostics.append(f"broken-link: {label}")
        elif anchor and anchor not in anchor_ids(candidate.read_text(encoding="utf-8")):
            diagnostics.append(f"broken-anchor: {label}")


def resolve_target(source: Path, docs_root: Path, target: str) -> Path | None:
    candidate = (docs_root / target.lstrip("/")) if target.startswith("/") else source.parent / target
    if not candidate.suffix:
        candidate = candidate / "index.md" if target.endswith("/") else candidate.with_suffix(".md")
    resolved = candidate.resolve()
    return resolved if is_within(resolved, docs_root.resolve()) else None


def anchor_ids(text: str) -> set[str]:
    return set(re.findall(r"\bid=[\"']([^\"']+)", rendered_html(text)))


def rendered_html(text: str) -> str:
    return markdown.Markdown(extensions=("toc", "tables", "fenced_code")).convert(text)


def frozen_base_available(root: Path, revision: str) -> bool:
    return subprocess.run(
        ("git", "-C", str(root), "cat-file", "-e", f"{revision}^{{commit}}"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def legacy_fragments(root: Path, revision: str, path: str) -> list[str]:
    source = subprocess.run(
        ("git", "-C", str(root), "show", f"{revision}:docs/{path}"),
        capture_output=True,
        check=True,
        text=True,
    ).stdout
    return re.findall(r"\bid=[\"']([^\"']+)", rendered_html(source))


def raw_status_tokens(text: str) -> bool:
    return any(token in text for token in RAW_READER_STATUS_TOKENS)


def reader_process_marker(text: str) -> bool:
    visible_text = re.sub(r"<a\s+id=[\"'][^\"']+[\"']\s*></a>", "", text, flags=re.IGNORECASE)
    return any(re.search(pattern, visible_text) for pattern in READER_PROCESS_PATTERNS)


def validate_privacy(text: str, label: str, diagnostics: list[str]) -> None:
    for predicate, pattern in {
        "privacy-source-path": r"(?:^|[\s`])application/(?:controllers|views|config)/",
        "privacy-private-url": r"https?://[^\s/]*(?:localhost|127\.0\.0\.1|internal)[^\s]*",
        "privacy-secret-assignment": r"(?i)\b(?:token|password|secret|api[_-]?key)\b\s*[:=]\s*\S+",
        "privacy-authorization": r"(?i)authorization\s*:\s*bearer\s+\S+",
        "privacy-pem": r"-----BEGIN [A-Z ]+-----",
        "privacy-source-sha": r"\b[a-f0-9]{40}\b",
        "privacy-email-example": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    }.items():
        if re.search(pattern, text):
            diagnostics.append(f"{predicate}: {label}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--audit-compatibility", action="store_true")
    args = parser.parse_args()
    report = validate_manual(args.root, audit_compatibility=args.audit_compatibility)
    print(f"manual validation: {'PASS' if report.is_valid else 'FAIL'} ({report.ficha_count} active guides; structural scope)")
    audit = load(args.root / "documentation/access-audit.yml", [])
    records = audit.get("records", []) if isinstance(audit, dict) else []
    if isinstance(records, list):
        verified = sum(isinstance(record, dict) and record.get("classification") in {"direct", "indirect", "quickstart"} for record in records)
        pending = sum(isinstance(record, dict) and record.get("classification") == "technical-gap" for record in records)
        print(f"access audit: {verified} verified entries; {pending} technical gaps")
    for diagnostic in report.diagnostics:
        print(f"- {diagnostic}")
    return 0 if report.is_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
