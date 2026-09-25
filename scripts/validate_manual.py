"""Validate a documentation manual tree without invoking external tools."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_SECTIONS = (
    "Objetivo",
    "Acceso condicional",
    "Requisitos y datos",
    "Punto de partida",
    "Pasos",
    "Campos y validaciones observados",
    "Resultado esperado",
    "Advertencias y casos límite",
    "Problemas frecuentes y condiciones de detención",
    "Enlaces relacionados",
)
RAW_READER_STATUS_TOKENS = (
    "source_reviewed_draft",
    "pending_runtime_verification",
)
READER_PROCESS_PATTERNS = (
    r"(?i)Borrador revisado en código · verificación en entorno pendiente",
    r"(?i)Revisión de fuente: revisada en código",
    r"(?i)Verificación en entorno: pendiente",
    r"(?i)Paridad con la versión desplegada: pendiente",
    r"(?i)\brevisad[oa] en (?:código|fuente)\b",
    r"(?i)\b(?:requiere|requieren|quedan) (?:verificación en |pendientes? de )(?:runtime|entorno)\b",
    r"(?i)\b(?:la fuente|en la fuente|fuente revisada|revisados en fuente|observados en la fuente)\b",
    r"(?i)\b(?:verificación|validación) en runtime\b",
    r"(?i)\bel navegador envía\b",
)
PENDING_ENRICHMENT = "pending_enrichment"


@dataclass(frozen=True)
class ValidationReport:
    ficha_count: int
    diagnostics: tuple[str, ...]
    document_count: int = 0
    capability_ids: tuple[str, ...] = ()

    @property
    def is_valid(self) -> bool:
        return not self.diagnostics


def validate_manual(root: Path, *, final: bool = False) -> ValidationReport:
    """Validate Markdown fichas under an explicit fixture or manual root."""
    docs_root = root / "docs"
    if not docs_root.is_dir():
        return ValidationReport(0, ("missing-docs-root: docs directory was not found",))

    diagnostics: list[str] = []
    metadata = load_metadata(root, diagnostics)
    documents = metadata.get("inventory", {}).get("documents", [])
    capabilities = metadata.get("catalog", {}).get("capabilities", [])
    checkpoint = metadata.get("checkpoint", {})
    fichas: list[Path] = []
    for path in sorted(path for path in docs_root.rglob("*.md") if path.name != "index.md"):
        if is_within(path.resolve(), docs_root.resolve()):
            fichas.append(path)
        else:
            diagnostics.append("unsafe-ficha-path: Markdown target escapes docs root")
    for ficha in fichas:
        text = ficha.read_text(encoding="utf-8")
        label = ficha.relative_to(root).as_posix()
        if reader_process_marker(text):
            diagnostics.append(f"reader-process-notice: {label} contains editorial process prose")
        if raw_status_tokens(text):
            diagnostics.append(f"raw-reader-status: {label} contains machine status tokens")
        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in text:
                diagnostics.append(f"required-section: {label} lacks {section}")
        validate_links(text, ficha, docs_root, label, diagnostics)
        validate_privacy(text, label, diagnostics)
        if final and PENDING_ENRICHMENT in text:
            diagnostics.append(f"pending-enrichment: {label} cannot pass final validation")

    validate_metadata(
        root, docs_root, fichas, documents, capabilities, checkpoint, metadata.get("nav", {}), final, diagnostics
    )
    capability_ids = tuple(item.get("id", "") for item in capabilities if isinstance(item, dict))
    return ValidationReport(len(fichas), tuple(diagnostics), len(documents), capability_ids)


def load_metadata(root: Path, diagnostics: list[str]) -> dict[str, object]:
    paths = {
        "nav": root / "mkdocs.yml",
        "inventory": root / "documentation" / "inventory.yml",
        "checkpoint": root / "documentation" / "source-checkpoint.yml",
        "catalog": root / "documentation" / "capability-dispositions.yml",
    }
    loaded: dict[str, object] = {}
    for name, path in paths.items():
        if not path.is_file():
            diagnostics.append(f"missing-metadata: {path.relative_to(root).as_posix()}")
            loaded[name] = {}
            continue
        try:
            loaded[name] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            diagnostics.append(f"invalid-yaml: {path.relative_to(root).as_posix()}")
            loaded[name] = {}
    return loaded


def validate_metadata(
    root: Path,
    docs_root: Path,
    fichas: list[Path],
    documents: object,
    capabilities: object,
    checkpoint: object,
    nav: object,
    final: bool,
    diagnostics: list[str],
) -> None:
    if not all(isinstance(value, (list, dict)) for value in (documents, capabilities, checkpoint, nav)):
        diagnostics.append("invalid-metadata-shape: expected mapping and lists")
        return
    documents = documents if isinstance(documents, list) else []
    capabilities = capabilities if isinstance(capabilities, list) else []
    checkpoint = checkpoint if isinstance(checkpoint, dict) else {}
    nav = nav if isinstance(nav, dict) else {}
    file_paths = {path.relative_to(docs_root).as_posix() for path in fichas}
    document_paths: set[str] = set()
    doc_ids: set[str] = set()
    inventory_ids: set[str] = set()
    for document in documents:
        if not isinstance(document, dict):
            diagnostics.append("invalid-document: inventory record must be a mapping")
            continue
        doc_id, path = document.get("doc_id"), document.get("path")
        ids = document.get("capability_ids")
        if not isinstance(doc_id, str) or not isinstance(path, str) or not isinstance(ids, list) or not ids:
            diagnostics.append("invalid-document: doc_id, path, and capability_ids are required")
            continue
        if document.get("content_status") != PENDING_ENRICHMENT:
            for status_key in ("source_review_status", "runtime_status", "deployed_parity_status"):
                if not isinstance(document.get(status_key), str):
                    diagnostics.append(f"invalid-document-status: {status_key} is required for enriched content")
        if not is_within((docs_root / path).resolve(), docs_root.resolve()):
            diagnostics.append("unsafe-document-path: inventory path escapes docs root")
        add_unique(doc_ids, doc_id, "duplicate-doc-id", diagnostics)
        add_unique(document_paths, path, "duplicate-path", diagnostics)
        for capability_id in ids:
            if not isinstance(capability_id, str):
                diagnostics.append("invalid-capability-id: inventory record")
            else:
                add_unique(inventory_ids, capability_id, "duplicate-capability-id", diagnostics)
        if final and document.get("content_status") == PENDING_ENRICHMENT:
            diagnostics.append("pending-enrichment: inventory cannot pass final validation")
    if file_paths != document_paths:
        diagnostics.append("file-parity: ficha files and inventory paths differ")
    nav_paths = {item for item in nav_leaves(nav.get("nav")) if not item.endswith("index.md")}
    if nav_paths != file_paths:
        diagnostics.append("nav-parity: navigation and ficha files differ")
    validate_numbering(nav.get("nav"), docs_root, diagnostics)
    validate_indexes(docs_root, documents, diagnostics)
    catalog_ids: set[str] = set()
    catalog_inventory_ids: set[str] = set()
    for capability in capabilities:
        if not isinstance(capability, dict):
            diagnostics.append("invalid-capability: catalog record must be a mapping")
            continue
        capability_id = capability.get("id")
        classification = capability.get("classification")
        disposition = capability.get("disposition")
        canonical = capability.get("canonical_doc_id")
        reason_category = capability.get("reason_category")
        if not isinstance(capability_id, str):
            diagnostics.append("invalid-capability-id: catalog record")
            continue
        add_unique(catalog_ids, capability_id, "duplicate-capability-id", diagnostics)
        if not legal_disposition(classification, disposition, final):
            diagnostics.append("illegal-disposition: classification and disposition combination")
        if disposition == "documented" and canonical not in doc_ids:
            diagnostics.append("canonical-doc-id: documented capability has no inventory document")
        if disposition == "owner_excluded_from_documentation" and (
            canonical is not None or capability_id in inventory_ids
        ):
            diagnostics.append("excluded-capability-document: excluded capability owns a document")
        if disposition == "owner_excluded_from_documentation" and reason_category != "owner_scope_exclusion":
            diagnostics.append("excluded-capability-reason: excluded capability lacks owner scope reason")
        if disposition == "out_of_current_menu_scope" and reason_category != "legacy_menu_not_in_current_scope":
            diagnostics.append("out-of-scope-capability-reason: legacy menu scope reason is required")
        if disposition == "documented" and isinstance(capability_id, str):
            catalog_inventory_ids.add(capability_id)
        if disposition == "pending" and canonical in doc_ids and isinstance(capability_id, str):
            catalog_inventory_ids.add(capability_id)
        if disposition == "documented" and capability_id not in inventory_ids:
            diagnostics.append("catalog-parity: documented capability is absent from inventory")
    if inventory_ids != catalog_inventory_ids:
        diagnostics.append("catalog-inventory-parity: canonical capability IDs differ")
    if checkpoint.get("document_ids") != sorted(doc_ids):
        diagnostics.append("checkpoint-parity: checkpoint document IDs differ")
    if final and checkpoint.get("scope_state") != "scope_complete":
        diagnostics.append("scope-state: final validation requires scope_complete")


def add_unique(seen: set[str], value: str, predicate: str, diagnostics: list[str]) -> None:
    if value in seen:
        diagnostics.append(f"{predicate}: duplicate value")
    seen.add(value)


def reader_process_marker(text: str) -> bool:
    """Keep editorial review and runtime notices out of reader-facing Markdown."""
    visible_text = re.sub(r"<a\s+id=[\"'][^\"']+[\"']\s*></a>", "", text, flags=re.IGNORECASE)
    return any(re.search(pattern, visible_text) for pattern in READER_PROCESS_PATTERNS)


def validate_numbering(nav: object, docs_root: Path, diagnostics: list[str]) -> None:
    """Keep chapter and ficha numbers derived from the ordered MkDocs navigation."""
    if not isinstance(nav, list):
        diagnostics.append("numbering-nav: navigation must be a list")
        return
    numbered_tree = any(
        isinstance(entry, dict)
        and len(entry) == 1
        and isinstance(next(iter(entry)), str)
        and re.match(r"^\d+\. ", next(iter(entry)))
        for entry in nav
    )
    if not numbered_tree:
        return
    for chapter, entry in enumerate(nav, start=1):
        if not isinstance(entry, dict) or len(entry) != 1:
            diagnostics.append("numbering-nav: invalid chapter entry")
            continue
        chapter_label, items = next(iter(entry.items()))
        if not isinstance(chapter_label, str):
            diagnostics.append("numbering-chapter: chapter label is invalid")
            continue
        if not chapter_label.startswith(f"{chapter}. "):
            diagnostics.append("numbering-chapter: chapter label does not match navigation order")
        for ordinal, (label, path) in enumerate(numbered_nav_leaves(items), start=1):
            expected = f"{chapter}.{ordinal} "
            if not label.startswith(expected):
                diagnostics.append("numbering-nav: ficha label does not match navigation order")
            text_path = docs_root / path
            if not text_path.is_file():
                continue
            text = text_path.read_text(encoding="utf-8")
            heading = next((line for line in text.splitlines() if line.startswith("# ")), "")
            if not heading.startswith(f"# {chapter}.{ordinal} "):
                diagnostics.append("numbering-h1: ficha heading does not match navigation order")
            index = text_path.parent / "index.md"
            if not index.is_file():
                diagnostics.append("numbering-index: owning index is missing")
                continue
            labels = {
                target: index_label
                for index_label, link in markdown_link_pairs(section_content(index.read_text(encoding="utf-8")))
                for target in [resolve_target(index, docs_root, link)]
                if target is not None
            }
            target = text_path.resolve()
            if not labels.get(target, "").startswith(expected):
                diagnostics.append("numbering-index: ficha label does not match navigation order")


def numbered_nav_leaves(value: object) -> list[tuple[str, str]]:
    if isinstance(value, list):
        return [leaf for child in value for leaf in numbered_nav_leaves(child)]
    if isinstance(value, dict):
        leaves: list[tuple[str, str]] = []
        for label, child in value.items():
            if isinstance(child, str) and not child.endswith("index.md") and isinstance(label, str):
                leaves.append((label, child))
            else:
                leaves.extend(numbered_nav_leaves(child))
        return leaves
    return []


def raw_status_tokens(text: str) -> bool:
    """Keep machine-only status values out of reader-facing Markdown."""
    return any(token in text for token in RAW_READER_STATUS_TOKENS)


def legal_disposition(classification: object, disposition: object, final: bool) -> bool:
    rules = {
        "core": {"documented", "pending", "owner_excluded_from_documentation"},
        "conditional": {"documented", "pending", "out_of_current_menu_scope", "not_enabled_for_documented_scope", "owner_excluded_from_documentation"},
        "uncertain": {"coverage_gap"},
        "internal_not_public": {"internal_not_public"},
    }
    if not isinstance(classification, str) or disposition not in rules.get(classification, set()):
        return False
    return not (final and disposition == "pending")


def nav_leaves(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for child in value for item in nav_leaves(child)]
    if isinstance(value, dict):
        return [item for child in value.values() for item in nav_leaves(child)]
    return []


def validate_indexes(docs_root: Path, documents: list[object], diagnostics: list[str]) -> None:
    expected: dict[str, set[str]] = {}
    for document in documents:
        if isinstance(document, dict) and isinstance(document.get("group"), str) and isinstance(document.get("path"), str):
            expected.setdefault(document["group"], set()).add(document["path"])
    for group, paths in expected.items():
        index = docs_root / group / "index.md"
        if not index.is_file():
            diagnostics.append("index-parity: designated Fichas disponibles links differ")
            continue
        actual = {
            target.relative_to(docs_root.resolve()).as_posix()
            for link in section_links(index.read_text(encoding="utf-8"))
            for target in [resolve_target(index, docs_root, link)]
            if target is not None
        }
        if actual != paths:
            diagnostics.append("index-parity: designated Fichas disponibles links differ")


def section_links(text: str) -> list[str]:
    return markdown_links(section_content(text))


def section_content(text: str) -> str:
    match = re.search(r"^## Fichas disponibles\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    return match.group(1) if match else ""


def markdown_link_pairs(text: str) -> list[tuple[str, str]]:
    return [(match.group(1), match.group(2).split()[0]) for match in re.finditer(r"(?<!!)\[([^]]+)\]\(([^)]+)\)", text)]


def validate_links(text: str, source: Path, docs_root: Path, label: str, diagnostics: list[str]) -> None:
    for target in markdown_links(text):
        target_path, _, anchor = target.partition("#")
        if re.match(r"[a-z][a-z0-9+.-]*:", target_path, re.IGNORECASE):
            continue
        candidate = source if not target_path else resolve_target(source, docs_root, target_path)
        if candidate is None or not candidate.is_file():
            diagnostics.append(f"broken-link: {label}")
            continue
        if anchor and anchor not in anchor_ids(candidate.read_text(encoding="utf-8")):
            diagnostics.append(f"broken-anchor: {label}")


def anchor_ids(text: str) -> set[str]:
    """Recognize Markdown heading anchors and deliberate legacy HTML aliases."""
    headings = {slugify(match.group(1)) for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE)}
    aliases = {match.group(1) for match in re.finditer(r"<a\s+id=[\"']([^\"']+)[\"']\s*></a>", text, re.IGNORECASE)}
    return headings | aliases


def markdown_links(text: str) -> list[str]:
    return [match.group(1).split()[0] for match in re.finditer(r"(?<!!)\[[^]]+\]\(([^)]+)\)", text)]


def resolve_target(source: Path, docs_root: Path, target: str) -> Path | None:
    relative = target.lstrip("/")
    candidate = (docs_root / relative) if target.startswith("/") else (source.parent / relative)
    if not candidate.suffix:
        candidate = candidate / "index.md" if target.endswith("/") else candidate.with_suffix(".md")
    resolved = candidate.resolve()
    return resolved if is_within(resolved, docs_root.resolve()) else None


def is_within(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def slugify(value: str) -> str:
    return re.sub(r"[^\w-]+", "-", value.lower()).strip("-")


def validate_privacy(text: str, label: str, diagnostics: list[str]) -> None:
    predicates = {
        "privacy-source-path": r"(?:^|[\s`])application/(?:controllers|views|config)/",
        "privacy-private-url": r"https?://[^\s/]*(?:localhost|127\.0\.0\.1|internal)[^\s]*",
        "privacy-secret-assignment": r"(?i)\b(?:token|password|secret|api[_-]?key)\b\s*[:=]\s*\S+",
        "privacy-authorization": r"(?i)authorization\s*:\s*bearer\s+\S+",
        "privacy-pem": r"-----BEGIN [A-Z ]+-----",
        "privacy-source-sha": r"\b[a-f0-9]{40}\b",
    }
    for number, line in enumerate(text.splitlines(), start=1):
        for predicate, pattern in predicates.items():
            if re.search(pattern, line):
                diagnostics.append(f"{predicate}: {label}:{number}")



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an explicit manual tree.")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--root", type=Path, help="Manual root containing docs/.")
    target.add_argument("--fixture", type=Path, help="Fixture directory containing docs/.")
    parser.add_argument("--final", action="store_true", help="Reject pending enrichment states.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.fixture or args.root
    report = validate_manual(root, final=args.final)
    if report.is_valid:
        print(f"manual validation: PASS ({report.ficha_count} fichas)")
        return 0
    print("manual validation: FAIL")
    for diagnostic in report.diagnostics:
        print(f"- {diagnostic}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
