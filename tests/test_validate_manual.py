from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
import re
import json
from pathlib import Path

import yaml

from scripts.validate_manual import anchor_ids, validate_manual


PROJECT_ROOT = Path(__file__).parent.parent
FIXTURES = Path(__file__).parent / "fixtures" / "manual"


class ValidateManualTests(unittest.TestCase):
    def copy_manual(self) -> Path:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        destination = Path(temporary_directory.name) / "manual"
        shutil.copytree(PROJECT_ROOT, destination, ignore=shutil.ignore_patterns(".git", ".build", "__pycache__", ".venv"))
        return destination

    def migration(self, root: Path) -> dict[str, object]:
        return yaml.safe_load((root / "documentation/task-manual-migration.yml").read_text(encoding="utf-8"))

    def write_migration(self, root: Path, migration: dict[str, object]) -> None:
        (root / "documentation/task-manual-migration.yml").write_text(
            yaml.safe_dump(migration, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )

    def copy_fixture(self, name: str) -> Path:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        destination = Path(temporary_directory.name) / name
        shutil.copytree(FIXTURES / name, destination)
        return destination

    def metadata(self, root: Path, name: str) -> dict[str, object]:
        return yaml.safe_load((root / "documentation" / name).read_text(encoding="utf-8"))

    def write_metadata(self, root: Path, name: str, value: dict[str, object]) -> None:
        (root / "documentation" / name).write_text(yaml.safe_dump(value, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def test_contract_manual_is_complete(self) -> None:
        report = validate_manual(PROJECT_ROOT)
        migration = self.migration(PROJECT_ROOT)
        records = migration["compatibility"]["records"]

        self.assertTrue(report.is_valid, report.diagnostics)
        self.assertEqual(83, report.ficha_count)
        self.assertEqual(12, len({entry["group"] for entry in migration["active_entries"]}))
        self.assertEqual(88, len(records))
        self.assertEqual(352, sum(len(record["fragments"]) for record in records))
        self.assertEqual(1320, sum(len(record["historical_fragments"]) for record in records))

    def test_frozen_baseline_retains_numbered_and_renamed_heading_fragments(self) -> None:
        fixture = yaml.safe_load((FIXTURES.parent / "compatibility/legacy-heading-fragments.yml").read_text(encoding="utf-8"))
        self.assertEqual(set(fixture["fragments"]), anchor_ids(fixture["source"]))
        self.assertTrue(validate_manual(PROJECT_ROOT, audit_compatibility=True).is_valid)

    def test_v1_rendered_baseline_rejects_a_missing_captured_h1_alias(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/catalogo/gestionar-productos.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace('<a id="41-registrar-y-actualizar-productos"></a>\n', "", 1), encoding="utf-8")
        self.assertTrue(any("v1-rendered-anchor" in item for item in validate_manual(root).diagnostics))

    def test_progress_requires_exact_v2_titles_and_paths(self) -> None:
        root = self.copy_manual()
        progress = self.metadata(root, "task-manual-v2-progress.yml")
        progress["contract_targets"][1]["tasks"][5]["imprimirla o comunicarla"] = None
        self.write_metadata(root, "task-manual-v2-progress.yml", progress)
        self.assertTrue(any("progress-target-shape" in item for item in validate_manual(root).diagnostics))

    def test_procedure_evidence_requires_immutable_revision_and_bounded_execution(self) -> None:
        root = self.copy_manual()
        inventory = self.metadata(root, "inventory.yml")
        evidence = next(document["procedure_evidence"] for document in inventory["documents"] if "procedure_evidence" in document)
        evidence["reviewed_revision"] = "330857"
        self.write_metadata(root, "inventory.yml", inventory)
        self.assertTrue(any("invalid-procedure-evidence" in item for item in validate_manual(root).diagnostics))

    def test_source_fact_revisions_allow_scoped_mixed_evidence_and_preserve_default_evidence(self) -> None:
        root = self.copy_manual()
        catalog = self.metadata(root, "source-fact-catalog.yml")
        requirements = {item["guide_id"]: item for item in catalog["requirements"]}

        self.assertEqual("330857197e5e01c24147d03452f7c59909abc968", catalog["default_reviewed_revision"])
        self.assertNotIn("reviewed_revision", requirements["sales-register-cash-sale"])
        self.assertEqual("500a335498a2206b2d3361bb9958095366207e99", requirements["catalog-manage-series"]["reviewed_revision"])
        self.assertTrue(validate_manual(root).is_valid)

    def test_source_fact_revisions_reject_unknown_invalid_and_mismatched_pins(self) -> None:
        root = self.copy_manual()
        catalog = self.metadata(root, "source-fact-catalog.yml")
        requirement = next(item for item in catalog["requirements"] if item["guide_id"] == "catalog-manage-series")
        requirement["reviewed_revision"] = "f" * 40
        self.write_metadata(root, "source-fact-catalog.yml", catalog)
        self.assertTrue(any("source-fact-revision: guide revision is not approved" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        catalog = self.metadata(root, "source-fact-catalog.yml")
        requirement = next(item for item in catalog["requirements"] if item["guide_id"] == "catalog-manage-series")
        requirement["reviewed_revision"] = "500a335"
        self.write_metadata(root, "source-fact-catalog.yml", catalog)
        self.assertTrue(any("source-fact-revision: guide revision is not approved" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        catalog = self.metadata(root, "source-fact-catalog.yml")
        requirement = next(item for item in catalog["requirements"] if item["guide_id"] == "catalog-manage-series")
        requirement["facts"][1]["reviewed_revision"] = "330857197e5e01c24147d03452f7c59909abc968"
        self.write_metadata(root, "source-fact-catalog.yml", catalog)
        self.assertTrue(any("source-fact-revision: fact revision differs from guide revision" in item for item in validate_manual(root).diagnostics))

    def test_scoped_source_facts_require_visible_direct_and_indirect_controls(self) -> None:
        root = self.copy_manual()
        series = root / "docs/catalogo/gestionar-series.md"
        series.write_text(series.read_text(encoding="utf-8").replace("**Reclasificar serie**", "**Reclasificar**", 1), encoding="utf-8")
        self.assertTrue(any("series-reclassify" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        load = root / "docs/distribucion/consultar-orden-de-carga.md"
        load.write_text(load.read_text(encoding="utf-8").replace("**Imprimir productos**", "**Imprimir**", 1), encoding="utf-8")
        self.assertTrue(any("load-product-summary" in item for item in validate_manual(root).diagnostics))

    def test_rendered_search_excludes_declared_compatibility_only_pages(self) -> None:
        root = self.copy_manual()
        site = root / ".build" / "search-exclusion"
        subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean", "--site-dir", str(site)],
            check=True,
            cwd=root,
        )
        migration = self.migration(root)
        search = json.loads((site / "search/search_index.json").read_text(encoding="utf-8"))["docs"]
        locations = {entry["location"].split("#", 1)[0] for entry in search}
        hidden = {path.removesuffix(".md") + "/" for path in migration["compatibility"]["search_hidden"]}
        active = {entry["target"].removesuffix(".md") + "/" for entry in migration["active_entries"]}
        self.assertFalse(hidden & locations)
        self.assertTrue(active & locations)
        indexed_text = json.dumps(search, ensure_ascii=False)
        for title in (
            "Registrar y consultar cargas de contenedores",
            "Registrar categorías de gasto y costos fijos",
            "Registrar y actualizar usuarios",
            "Registrar y actualizar vendedores",
            "Asignar establecimientos a vendedores",
        ):
            self.assertNotIn(title, indexed_text)

    def test_searchable_page_cannot_link_to_a_held_task(self) -> None:
        root = self.copy_manual()
        index = root / "docs/inventario/index.md"
        index.write_text("# Inventario\n\n[Histórico](gestionar-cargas-de-contenedores.md)\n", encoding="utf-8")
        self.assertTrue(any("searchable-held-link" in item for item in validate_manual(root).diagnostics))

    def test_missing_required_core_section_fails(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("## Pasos", "## Recorrido", 1), encoding="utf-8")

        self.assertTrue(any("required-section" in item for item in validate_manual(root).diagnostics))

    def test_access_audit_requires_complete_literal_routes_and_honest_gaps(self) -> None:
        root = self.copy_manual()
        audit = yaml.safe_load((root / "documentation/access-audit.yml").read_text(encoding="utf-8"))
        audit["records"].pop()
        (root / "documentation/access-audit.yml").write_text(yaml.safe_dump(audit, allow_unicode=True, sort_keys=False), encoding="utf-8")
        self.assertTrue(any("access-audit-coverage" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        guide = root / "docs/ventas/gestionar-cotizaciones.md"
        guide.write_text(re.sub(r"(## Cómo acceder\n\n).*?(?=\n## )", r"\1Abra el formulario de cotización.\n", guide.read_text(encoding="utf-8"), count=1, flags=re.S), encoding="utf-8")
        self.assertTrue(any("access-label-coverage" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("## Cómo acceder\n\n", "## Cómo acceder\n\nNo se confirmó una entrada lateral literal\n", 1), encoding="utf-8")
        self.assertTrue(any("access-public-audit-note" in item for item in validate_manual(root).diagnostics))

    def test_access_audit_requires_meaningful_ordered_steps_for_confirmed_routes(self) -> None:
        root = self.copy_manual()
        audit = yaml.safe_load((root / "documentation/access-audit.yml").read_text(encoding="utf-8"))
        record = next(record for record in audit["records"] if record["guide"] == "2.4")
        record["access_steps"] = ["Abra el formulario."]
        (root / "documentation/access-audit.yml").write_text(yaml.safe_dump(audit, allow_unicode=True, sort_keys=False), encoding="utf-8")
        self.assertTrue(any("access-audit-steps" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        guide = root / "docs/ventas/gestionar-cotizaciones.md"
        guide.write_text(re.sub(r"\n3\. .*?(?=\n## )", "", guide.read_text(encoding="utf-8"), count=1, flags=re.S), encoding="utf-8")
        self.assertTrue(any("access-step-coverage" in item for item in validate_manual(root).diagnostics))

    def test_access_audit_supports_dynamic_three_level_and_detail_routes(self) -> None:
        root = self.copy_manual()
        audit = yaml.safe_load((root / "documentation/access-audit.yml").read_text(encoding="utf-8"))
        commission = next(record for record in audit["records"] if record["guide"] == "2.13")
        self.assertEqual(["Ventas", "Reportes", "Ingreso egreso dinero"], commission["sidebar"])
        confirmation = next(record for record in audit["records"] if record["guide"] == "6.3")
        self.assertIn("doble clic", confirmation["access_steps"][2])
        self.assertIn("Confirmar", confirmation["access_steps"][2])
        self.assertEqual("quickstart", next(record for record in audit["records"] if record["guide"] == "1.1")["classification"])
        self.assertEqual([], [record["guide"] for record in audit["records"] if record["classification"] == "technical-gap"])

    def test_source_facts_reject_missing_product_reveal_with_markers_intact(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/catalogo/gestionar-productos.md"
        text = guide.read_text(encoding="utf-8")
        mutated, mutations = re.subn(
            r"(?m)^(\d+\.\s+Para crear un producto, en el encabezado de \*\*Lista de productos\*\*)\s+abra el icono de tres puntos verticales\b[^\n]*?\s+y seleccione\s+(\*\*Nuevo producto\*\*\s+en el menú desplegable\.\s+Se abrirá el formulario\s+\*\*Agregar producto\*\*\.)$",
            r"\1 seleccione \2",
            text,
            count=1,
        )
        self.assertEqual(1, mutations)
        self.assertNotEqual(text, mutated)
        guide.write_text(mutated, encoding="utf-8")
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_source_facts_reject_joint_product_edit_omission(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/catalogo/gestionar-productos.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("haga doble clic en ella. Se abrirá el formulario **Editar producto**.", "abra el producto.", 1), encoding="utf-8")
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_source_facts_reject_wrong_product_delete_container(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/catalogo/eliminar-producto.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("encabezado del modal", "lista de productos"), encoding="utf-8")
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_source_facts_reject_budget_header_omission(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/compras/crear-consultar-periodos-presupuestarios.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("menú de acciones de tres puntos verticales y seleccione **Nuevo periodo**", "acción de la lista", 1), encoding="utf-8")
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_source_facts_reject_joint_sale_payment_omission(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-cobro-posterior-y-consultar-saldo.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("3. Localice la venta y haga doble clic en su fila para abrir el detalle.\n4. En el menú de acciones del detalle, seleccione **Registrar pago**. Se abrirá **Pagos / Agregar**.\n", ""), encoding="utf-8")
        audit = self.metadata(root, "access-audit.yml")
        record = next(record for record in audit["records"] if record["id"] == "sales-collect-later-and-check-balance")
        record["access_steps"] = record["access_steps"][:2]
        self.write_metadata(root, "access-audit.yml", audit)
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_source_facts_reject_reversed_hidden_action_order(self) -> None:
        cases = (
            (
                "manual-9-3",
                "docs/distribucion/confirmar-orden-de-carga.md",
                "En la lista, abra el detalle con doble clic en la fila y, en el menú de más opciones, seleccione **Confirmar**.",
                "En la lista, seleccione **Confirmar**.\n4. Abra el detalle con doble clic en la fila y el menú de más opciones.",
                "load-confirm",
            ),
            (
                "manual-2-9",
                "docs/ventas/canjear-documento-de-venta.md",
                "3. Localice la venta y haga doble clic en su fila para abrir el detalle.\n4. En el menú de acciones del detalle, seleccione **Canjear** solo si está habilitado. Se abrirá el formulario de canje de la nota de venta.",
                "3. Seleccione **Canjear** solo si está habilitado.\n4. Localice la venta, haga doble clic en su fila y abra el menú de acciones del detalle.",
                "sale-document-exchange",
            ),
            (
                "purchases-register-payments-and-balances",
                "docs/compras/registrar-pagos-y-saldos.md",
                "3. Localice la compra y haga doble clic en su fila para abrir el detalle.\n4. En el menú de acciones del detalle, seleccione **Registrar pago**. Se abrirá **Pagos / Agregar**.",
                "3. Seleccione **Registrar pago**.\n4. Localice la compra, haga doble clic en su fila y abra el menú de acciones del detalle.",
                "purchase-payment-detail",
            ),
        )
        for guide_id, relative_path, original, reversed_order, fact_id in cases:
            with self.subTest(guide_id=guide_id):
                root = self.copy_manual()
                guide = root / relative_path
                guide.write_text(guide.read_text(encoding="utf-8").replace(original, reversed_order, 1), encoding="utf-8")
                audit = self.metadata(root, "access-audit.yml")
                record = next(record for record in audit["records"] if record["id"] == guide_id)
                record["access_steps"][-2:] = [reversed_order]
                self.write_metadata(root, "access-audit.yml", audit)
                diagnostics = validate_manual(root).diagnostics
                self.assertIn(f"source-fact-visible-order: {relative_path.removeprefix('docs/')} lacks {fact_id}", diagnostics)

        self.assertTrue(validate_manual(self.copy_manual()).is_valid)

    def test_typed_source_facts_reject_joint_hidden_action_omissions(self) -> None:
        cases = (
            ("docs/reportes/consultar-tabla-pagos.md", "menú de acciones de tres puntos", "Generar EXCEL"),
            ("docs/ventas/convertir-cotizacion-en-venta.md", "menú de tres puntos verticales", "Convertir venta"),
        )
        for relative_path, reveal, control in cases:
            with self.subTest(path=relative_path):
                root = self.copy_manual()
                guide = root / relative_path
                guide.write_text(guide.read_text(encoding="utf-8").replace(reveal + " y seleccione **" + control + "**", "seleccione **" + control + "**", 1), encoding="utf-8")
                audit = self.metadata(root, "access-audit.yml")
                for record in audit["records"]:
                    if record["path"] == relative_path.removeprefix("docs/"):
                        record["access_steps"] = [step.replace(reveal + " y seleccione **" + control + "**", "seleccione **" + control + "**") for step in record["access_steps"]]
                self.write_metadata(root, "access-audit.yml", audit)
                self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

    def test_typed_source_facts_reject_wrong_row_gesture_and_keep_direct_form_valid(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/consultar-ventas.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("Haga doble clic", "Seleccione", 1), encoding="utf-8")
        self.assertTrue(any("source-fact-visible-coverage" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        self.assertTrue(validate_manual(root).is_valid)

    def test_source_facts_require_a_final_batch_guide(self) -> None:
        root = self.copy_manual()
        catalog = self.metadata(root, "source-fact-catalog.yml")
        catalog["requirements"] = [item for item in catalog["requirements"] if item["guide_id"] != "manual-8-5"]
        self.write_metadata(root, "source-fact-catalog.yml", catalog)
        self.assertTrue(any("source-fact-coverage" in item for item in validate_manual(root).diagnostics))

    def test_duplicate_or_missing_contract_entry_fails(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        migration["active_entries"][1]["number"] = "1.1"
        self.write_migration(root, migration)

        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("duplicate-active-entry" in item for item in diagnostics))

    def test_navigation_title_number_and_path_must_match_registry(self) -> None:
        root = self.copy_manual()
        config = root / "mkdocs.yml"
        config.write_text(config.read_text(encoding="utf-8").replace("2.1 Registrar una venta al contado", "2.9 Registrar una venta al contado", 1), encoding="utf-8")

        self.assertTrue(any("nav-parity" in item for item in validate_manual(root).diagnostics))

    def test_legacy_path_and_exact_anchor_are_required(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        records = migration["compatibility"]["records"]
        records.pop()
        self.write_migration(root, migration)
        self.assertTrue(any("legacy-path-coverage" in item for item in validate_manual(root).diagnostics))

        root = self.copy_manual()
        migration = self.migration(root)
        record = next(record for record in migration["compatibility"]["records"] if record["fragments"])
        alias = record["fragments"][0]
        source = root / "docs" / record["path"]
        source.write_text(source.read_text(encoding="utf-8").replace(f'<a id="{alias}"></a>', "", 1), encoding="utf-8")
        self.assertTrue(any("legacy-historical-anchor" in item for item in validate_manual(root).diagnostics))

    def test_compatibility_page_cannot_be_active_or_navigated(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        compatibility_path = next(record["path"] for record in migration["compatibility"]["records"] if record["path"] not in {entry["target"] for entry in migration["active_entries"]})
        migration["active_entries"][0]["target"] = compatibility_path
        self.write_migration(root, migration)

        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("active-title" in item for item in diagnostics))
        self.assertTrue(any("inventory-parity" in item for item in diagnostics))

    def test_unclassified_markdown_and_private_content_fail(self) -> None:
        root = self.copy_manual()
        orphan = root / "docs/orphan.md"
        orphan.write_text("# Orphan\n", encoding="utf-8")
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\ntoken = secret-value\n", encoding="utf-8")

        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("unclassified-markdown" in item for item in diagnostics))
        self.assertTrue(any("privacy-secret-assignment" in item for item in diagnostics))

    def test_legacy_valid_and_numbered_fixtures_remain_exercised(self) -> None:
        self.assertTrue(validate_manual(self.copy_fixture("valid")).is_valid)
        self.assertTrue(validate_manual(self.copy_fixture("numbered")).is_valid)

    def test_legacy_fixture_requires_its_core_sections_without_leaking_content(self) -> None:
        root = self.copy_fixture("valid")
        guide = root / "docs/ventas/elegir-establecimiento.md"
        guide.write_text("# secreto-de-prueba\n", encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("required-section" in item for item in diagnostics))
        self.assertFalse(any("secreto-de-prueba" in item for item in diagnostics))

    def test_legacy_final_mode_rejects_pending_enrichment(self) -> None:
        diagnostics = validate_manual(self.copy_fixture("valid"), final=True).diagnostics
        self.assertIn("pending-enrichment", diagnostics)

    def test_legacy_duplicate_capability_and_numbering_regressions_fail(self) -> None:
        root = self.copy_fixture("valid")
        inventory = self.metadata(root, "inventory.yml")
        inventory["documents"][1]["capability_ids"] = ["CAP-01"]
        self.write_metadata(root, "inventory.yml", inventory)
        self.assertTrue(any("duplicate-capability-id" in item for item in validate_manual(root).diagnostics))
        root = self.copy_fixture("numbered")
        config = root / "mkdocs.yml"
        config.write_text(config.read_text(encoding="utf-8").replace("1.2 Seleccionar", "1.1 Seleccionar"), encoding="utf-8")
        self.assertTrue(any("numbering-nav" in item for item in validate_manual(root).diagnostics))

    def test_checkpoint_revision_and_pending_range_are_consistent(self) -> None:
        root = self.copy_manual()
        checkpoint = self.metadata(root, "source-checkpoint.yml")
        checkpoint["source_revision"] = "not-a-sha"
        checkpoint["source_sync"]["pending"]["count"] = 0
        self.write_metadata(root, "source-checkpoint.yml", checkpoint)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("checkpoint-source-revision" in item for item in diagnostics))

    def test_checkpoint_preserves_independent_pending_states(self) -> None:
        root = self.copy_manual()
        checkpoint = self.metadata(root, "source-checkpoint.yml")
        checkpoint["runtime_status"] = "verified"
        self.write_metadata(root, "source-checkpoint.yml", checkpoint)
        self.assertTrue(any("checkpoint-states" in item for item in validate_manual(root).diagnostics))

    def test_final_mode_requires_the_existing_complete_content_scope(self) -> None:
        root = self.copy_manual()
        checkpoint = self.metadata(root, "source-checkpoint.yml")
        checkpoint["scope_state"] = "slice_pending"
        self.write_metadata(root, "source-checkpoint.yml", checkpoint)
        self.assertTrue(any("scope-state" in item for item in validate_manual(root, final=True).diagnostics))

    def test_scoped_source_alignment_cannot_advance_the_global_pin(self) -> None:
        root = self.copy_manual()
        inventory = self.metadata(root, "inventory.yml")
        inventory["documents"][0]["source_revision"] = inventory["active_content_revision"]
        inventory["scoped_source_bases"][0]["reviewed_revision"] = "not-a-sha"
        self.write_metadata(root, "inventory.yml", inventory)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("invalid-document-status: source_revision" in item for item in diagnostics))
        self.assertTrue(any("invalid-scoped-source-basis" in item for item in diagnostics))

    def test_catalog_rejects_duplicate_ids_and_invalid_dispositions(self) -> None:
        root = self.copy_manual()
        catalog = self.metadata(root, "capability-dispositions.yml")
        catalog["capabilities"].append(dict(catalog["capabilities"][0]))
        catalog["capabilities"][1]["disposition"] = "coverage_gap"
        self.write_metadata(root, "capability-dispositions.yml", catalog)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("duplicate-capability-id" in item for item in diagnostics))
        self.assertTrue(any("illegal-disposition" in item for item in diagnostics))

    def test_catalog_exclusions_and_historical_gaps_are_checkpoint_bound(self) -> None:
        root = self.copy_manual()
        catalog = self.metadata(root, "capability-dispositions.yml")
        excluded = next(item for item in catalog["capabilities"] if item["disposition"] == "owner_excluded_from_documentation")
        excluded["disposition"] = "documented"
        self.write_metadata(root, "capability-dispositions.yml", catalog)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("owner-exclusion-parity" in item for item in diagnostics))

    def test_active_capabilities_must_match_real_catalog_canonicals(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        migration["active_entries"][0]["capability_ids"] = ["SAL-04"]
        self.write_migration(root, migration)
        self.assertTrue(any("active-capability-parity" in item for item in validate_manual(root).diagnostics))

    def test_inventory_rejects_duplicate_ids_and_unsafe_paths(self) -> None:
        root = self.copy_manual()
        inventory = self.metadata(root, "inventory.yml")
        inventory["documents"][1]["doc_id"] = inventory["documents"][0]["doc_id"]
        inventory["documents"][2]["path"] = "../outside.md"
        self.write_metadata(root, "inventory.yml", inventory)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("duplicate-doc-id" in item for item in diagnostics))
        self.assertTrue(any("unsafe-document-path" in item for item in diagnostics))

    def test_contract_titles_and_group_order_are_exact(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        migration["active_entries"][0]["title"] = "Otro título"
        self.write_migration(root, migration)
        self.assertTrue(any("contract-parity" in item for item in validate_manual(root).diagnostics))

    def test_compatibility_rejects_duplicate_fragments_and_bad_classification(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        record = migration["compatibility"]["records"][0]
        record["fragments"].append(record["fragments"][0])
        migration["compatibility"]["indexes"].append(record["path"])
        self.write_migration(root, migration)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("duplicate-legacy-fragment" in item for item in diagnostics))
        self.assertTrue(any("invalid-markdown-classification" in item for item in diagnostics))

    def test_compatibility_rejects_loss_of_a_generated_historical_heading(self) -> None:
        root = self.copy_manual()
        migration = self.migration(root)
        record = next(record for record in migration["compatibility"]["records"] if record["path"] == "ventas/registrar-venta-al-contado.md")
        record["historical_fragments"].remove("24-registrar-venta-al-contado")
        self.write_migration(root, migration)
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("legacy-historical-anchor-coverage" in item for item in diagnostics))

    def test_links_require_exact_html_ids_and_generated_heading_anchors(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\n[Correcto](#cómo-acceder)\n[Incorrecto](#como-acceder)\n<a id=\"legacy.fragment\"></a>\n[Alias](#legacy-fragment)\n", encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("broken-anchor" in item for item in diagnostics))

    def test_links_reject_empty_bare_and_file_targets(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\n[](otro.md)\n[Vacío]()\n[Archivo](file:///tmp/private)\n", encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("bare-link" in item for item in diagnostics))
        self.assertTrue(any("empty-link" in item for item in diagnostics))
        self.assertTrue(any("unsafe-link-scheme" in item for item in diagnostics))

    def test_privacy_sanitizes_paths_urls_secrets_and_email_examples(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\napplication/controllers/private.php\nhttps://internal.example.test/private\ntoken = super-secret\nAuthorization: Bearer value\n-----BEGIN PRIVATE KEY-----\nname@example.test\n", encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        for predicate in ("privacy-source-path", "privacy-private-url", "privacy-secret-assignment", "privacy-authorization", "privacy-pem", "privacy-email-example"):
            self.assertTrue(any(predicate in item for item in diagnostics), predicate)
        self.assertFalse(any("super-secret" in item for item in diagnostics))

    def test_optional_headings_are_not_required_but_core_headings_are(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        clean = guide.read_text(encoding="utf-8").replace("## Antes de empezar", "## Preparación opcional", 1)
        guide.write_text(clean, encoding="utf-8")
        self.assertFalse(any("required-section" in item for item in validate_manual(root).diagnostics))
        guide.write_text(clean.replace("## Compruebe el resultado", "## Resultado", 1), encoding="utf-8")
        self.assertTrue(any("required-section" in item for item in validate_manual(root).diagnostics))

    def test_active_guides_reject_legacy_template_headings(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\n## Acceso condicional\n", encoding="utf-8")
        self.assertTrue(any("legacy-template-heading" in item for item in validate_manual(root).diagnostics))

    def test_home_cannot_link_to_compatibility_areas_or_claim_legacy_coverage(self) -> None:
        root = self.copy_manual()
        home = root / "docs/index.md"
        home.write_text(home.read_text(encoding="utf-8") + '\n<a href="recorridos/ventas/">Histórico</a>\n18 áreas\n', encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("home-compat-navigation" in item for item in diagnostics))
        self.assertTrue(any("home-legacy-coverage-claim" in item for item in diagnostics))

    def test_home_cards_use_rendered_directory_urls(self) -> None:
        root = self.copy_manual()
        site = root / ".build" / "home-cards"
        subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean", "--site-dir", str(site)],
            check=True,
            cwd=root,
        )
        rendered = (site / "index.html").read_text(encoding="utf-8")
        links = re.findall(r'<a href="([^"]+)"><strong>', rendered)
        self.assertEqual(15, len(links))
        self.assertFalse(any(link.endswith(".md") for link in links))
        self.assertTrue(all((site / link / "index.html").is_file() for link in links))

    def test_quickstart_must_include_session_actions(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/inicio/iniciar-sesion.md"
        guide.write_text(guide.read_text(encoding="utf-8").replace("Cerrar Sesión", "Salir", 1), encoding="utf-8")
        self.assertTrue(any("quickstart-incomplete" in item for item in validate_manual(root).diagnostics))

    def test_active_guide_cannot_continue_to_compatibility_only_page(self) -> None:
        root = self.copy_manual()
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\n[Anterior](elegir-establecimiento.md)\n", encoding="utf-8")
        self.assertTrue(any("active-compat-continuation" in item for item in validate_manual(root).diagnostics))

    def test_raw_reader_statuses_remain_forbidden_only_in_markdown(self) -> None:
        root = self.copy_manual()
        inventory = root / "documentation/inventory.yml"
        inventory.write_text(inventory.read_text(encoding="utf-8") + "\nmachine_status: source_reviewed_draft\n", encoding="utf-8")
        self.assertTrue(validate_manual(root).is_valid)
        guide = root / "docs/ventas/registrar-venta-al-contado.md"
        guide.write_text(guide.read_text(encoding="utf-8") + "\nsource_reviewed_draft\nBorrador revisado en código · verificación en entorno pendiente\n<a id=\"revision-de-fuente-revisada-en-codigo\"></a>\n", encoding="utf-8")
        diagnostics = validate_manual(root).diagnostics
        self.assertTrue(any("raw-reader-status" in item for item in diagnostics))
        self.assertTrue(any("reader-process-notice" in item for item in diagnostics))


if __name__ == "__main__":
    unittest.main()
