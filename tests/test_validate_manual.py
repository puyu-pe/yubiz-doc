from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_manual import validate_manual


FIXTURES = Path(__file__).parent / "fixtures" / "manual"
PROJECT_ROOT = Path(__file__).parent.parent


class ValidateManualTests(unittest.TestCase):
    def copy_fixture(self, name: str) -> Path:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        destination = Path(temporary_directory.name) / name
        shutil.copytree(FIXTURES / name, destination)
        return destination

    def test_counts_only_non_index_fichas_at_any_depth(self) -> None:
        report = validate_manual(self.copy_fixture("valid"))

        self.assertTrue(report.is_valid)
        self.assertEqual(2, report.ficha_count)

    def test_requires_all_sections_and_visible_statuses(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(ficha.read_text(encoding="utf-8").replace("## Pasos\n", ""), encoding="utf-8")

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertIn("required-section", report.diagnostics[0])
        self.assertIn("Pasos", report.diagnostics[0])

    def test_redacts_fixture_content_from_diagnostics(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text("# secreto-de-prueba\n", encoding="utf-8")

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertIn("missing-status", report.diagnostics[0])
        self.assertNotIn("secreto-de-prueba", report.diagnostics[0])

    def test_final_mode_rejects_pending_enrichment(self) -> None:
        report = validate_manual(self.copy_fixture("valid"), final=True)

        self.assertFalse(report.is_valid)
        self.assertIn("pending-enrichment", report.diagnostics[0])

    def test_live_partial_manual_accepts_legacy_pending_enrichment_fichas(self) -> None:
        report = validate_manual(PROJECT_ROOT)

        self.assertTrue(report.is_valid, report.diagnostics)
        self.assertEqual(report.document_count, report.ficha_count)

    def test_valid_fixture_enforces_metadata_parity_and_canonical_ids(self) -> None:
        report = validate_manual(self.copy_fixture("valid"))

        self.assertTrue(report.is_valid)
        self.assertEqual(2, report.document_count)
        self.assertEqual({"CAP-01", "CAP-02", "CAP-03"}, set(report.capability_ids))

    def test_reports_duplicate_capability_and_missing_navigation_parity(self) -> None:
        root = self.copy_fixture("valid")
        inventory = root / "documentation" / "inventory.yml"
        inventory.write_text(inventory.read_text(encoding="utf-8").replace("CAP-03", "CAP-01"), encoding="utf-8")
        config = root / "mkdocs.yml"
        config.write_text(config.read_text(encoding="utf-8").replace("      - Cliente: ventas/seleccionar-cliente.md\n", ""), encoding="utf-8")

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("duplicate-capability-id" in item for item in report.diagnostics))
        self.assertTrue(any("nav-parity" in item for item in report.diagnostics))

    def test_rejects_invalid_final_classification_and_pending_states(self) -> None:
        root = self.copy_fixture("valid")
        catalog = root / "documentation" / "capability-dispositions.yml"
        catalog.write_text(catalog.read_text(encoding="utf-8").replace("classification: conditional", "classification: uncertain"), encoding="utf-8")

        report = validate_manual(root, final=True)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("illegal-disposition" in item for item in report.diagnostics))
        self.assertTrue(any("pending-enrichment" in item for item in report.diagnostics))

    def test_allows_documented_conditional_without_grant_fields(self) -> None:
        report = validate_manual(self.copy_fixture("valid"))

        self.assertTrue(report.is_valid, report.diagnostics)

    def test_rejects_excluded_capability_with_inventory_or_canonical_document(self) -> None:
        root = self.copy_fixture("valid")
        catalog = root / "documentation" / "capability-dispositions.yml"
        catalog.write_text(
            catalog.read_text(encoding="utf-8").replace(
                "classification: core\n    disposition: documented\n    canonical_doc_id: sales-context",
                "classification: core\n    disposition: owner_excluded_from_documentation\n    reason_category: owner_scope_exclusion\n    canonical_doc_id: sales-context",
                1,
            ),
            encoding="utf-8",
        )

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("excluded-capability-document" in item for item in report.diagnostics))

    def test_validates_links_anchors_and_redacts_privacy_matches(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(
            ficha.read_text(encoding="utf-8")
            + "\n[Ancla inválida](seleccionar-cliente.md#sin-destino)\n"
            + "token = super-secret-value\n",
            encoding="utf-8",
        )

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("broken-anchor" in item for item in report.diagnostics))
        self.assertTrue(any("privacy-secret-assignment" in item for item in report.diagnostics))
        self.assertFalse(any("super-secret-value" in item for item in report.diagnostics))

    def test_allows_safe_words_and_yaml_source_revision(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(ficha.read_text(encoding="utf-8") + "\nEl token de turno y la API se verifican en runtime.\n", encoding="utf-8")

        report = validate_manual(root)

        self.assertTrue(report.is_valid)

    def test_allows_human_three_row_status_banner_during_transition(self) -> None:
        report = validate_manual(self.copy_fixture("valid"))
        self.assertTrue(report.is_valid, report.diagnostics)

    def test_rejects_raw_reader_status_tokens(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(
            ficha.read_text(encoding="utf-8").replace(
                "- Revisión de fuente: revisada en código\n- Verificación en entorno: pendiente\n- Paridad con la versión desplegada: pendiente",
                "- `source_reviewed_draft`\n- `pending_runtime_verification`",
            ),
            encoding="utf-8",
        )
        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("raw-reader-status" in item for item in report.diagnostics))

    def test_requires_all_three_human_status_rows(self) -> None:
        root = self.copy_fixture("valid")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(
            ficha.read_text(encoding="utf-8")
            .replace("- Paridad con la versión desplegada: pendiente\n", ""),
            encoding="utf-8",
        )

        report = validate_manual(root)

        self.assertFalse(report.is_valid)
        self.assertTrue(any("missing-status" in item for item in report.diagnostics))

    def test_allows_machine_status_in_yaml_but_rejects_private_reader_path(self) -> None:
        root = self.copy_fixture("valid")
        inventory = root / "documentation" / "inventory.yml"
        inventory.write_text(
            inventory.read_text(encoding="utf-8") + "\nmachine_status: source_reviewed_draft\n",
            encoding="utf-8",
        )
        self.assertTrue(validate_manual(root).is_valid)
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(ficha.read_text(encoding="utf-8") + "\napplication/controllers/private.php\n", encoding="utf-8")
        report = validate_manual(root)
        self.assertTrue(any("privacy-source-path" in item for item in report.diagnostics))

    def test_candidate_admission_needs_no_grant_and_does_not_change_exclusions(self) -> None:
        report = validate_manual(PROJECT_ROOT)
        catalog = __import__("yaml").safe_load((PROJECT_ROOT / "documentation" / "capability-dispositions.yml").read_text(encoding="utf-8"))
        documented = {"SRV-01", "SRV-02", "SRV-03", "SRV-04", "SRV-05", "SPC-01", "SPC-02", "SPC-03", "SPC-04", "CUS-01", "CUS-02", "CUS-03", "CUS-04", "CUS-05"}
        qal = {"QAL-01", "QAL-02", "QAL-03", "QAL-04", "QAL-05"}
        states = {item["id"]: item["disposition"] for item in catalog["capabilities"]}
        self.assertTrue(report.is_valid, report.diagnostics)
        self.assertTrue(all(states[item] == "documented" for item in documented))
        self.assertTrue(all(states[item] == "out_of_current_menu_scope" for item in qal))

    def test_requires_independent_deployed_parity_for_enriched_inventory(self) -> None:
        root = self.copy_fixture("valid")
        inventory = root / "documentation" / "inventory.yml"
        inventory.write_text(inventory.read_text(encoding="utf-8").replace("content_status: pending_enrichment", "content_status: source_backed_enriched", 1), encoding="utf-8")
        report = validate_manual(root)
        self.assertTrue(any("invalid-document-status: deployed_parity_status" in item for item in report.diagnostics))

    def test_rejects_path_escapes_and_multiple_privacy_predicates(self) -> None:
        root = self.copy_fixture("valid")
        inventory = root / "documentation" / "inventory.yml"
        inventory.write_text(inventory.read_text(encoding="utf-8").replace("ventas/seleccionar-cliente.md", "../outside.md"), encoding="utf-8")
        ficha = root / "docs" / "ventas" / "elegir-establecimiento.md"
        ficha.write_text(
            ficha.read_text(encoding="utf-8")
            + "\napplication/controllers/private.php\n"
            + "https://internal.example.test/private\n"
            + "-----BEGIN PRIVATE KEY-----\n",
            encoding="utf-8",
        )

        report = validate_manual(root)

        self.assertTrue(any("unsafe-document-path" in item for item in report.diagnostics))
        self.assertTrue(any("privacy-source-path" in item for item in report.diagnostics))
        self.assertTrue(any("privacy-private-url" in item for item in report.diagnostics))
        self.assertTrue(any("privacy-pem" in item for item in report.diagnostics))

    def test_menu_scope_reconciliation_final_set(self) -> None:
        expected_excluded = {
            "FIN-06", "FIN-07", "INV-09", "PSD-01", "PSD-02", "PSD-03",
            "PRD-01", "PRD-02", "PRD-03", "PRD-04", "ACC-01", "ACC-02",
            "CRM-01", "CRM-02",
        }
        expected_retained_paths = {
            "compras/gestionar-presupuesto.md",
            "preventa/crear-pedido.md",
            "preventa/consultar-y-editar.md",
            "preventa/confirmar-anular-convertir.md",
            "distribucion/crear-orden-de-carga.md",
            "distribucion/gestionar-orden-de-carga.md",
            "distribucion/recargas-y-compromisos.md",
            "distribucion/registrar-descarga-y-entrega.md",
            "reportes-especializados/ventas-por-usuario-y-cliente.md",
        }
        report = validate_manual(PROJECT_ROOT)
        checkpoint = yaml.safe_load((PROJECT_ROOT / "documentation" / "source-checkpoint.yml").read_text(encoding="utf-8"))
        inventory = yaml.safe_load((PROJECT_ROOT / "documentation" / "inventory.yml").read_text(encoding="utf-8"))
        catalog = yaml.safe_load((PROJECT_ROOT / "documentation" / "capability-dispositions.yml").read_text(encoding="utf-8"))
        inventory_paths = {document["path"] for document in inventory["documents"]}
        excluded = {
            item["id"]
            for item in catalog["capabilities"]
            if item["disposition"] == "owner_excluded_from_documentation"
        }

        self.assertTrue(report.is_valid, report.diagnostics)
        self.assertEqual(88, report.ficha_count)
        self.assertEqual(114, len(catalog["capabilities"]))
        self.assertEqual(expected_excluded, excluded)
        self.assertTrue(all(
            item.get("reason_category") == "owner_scope_exclusion"
            and "canonical_doc_id" not in item
            for item in catalog["capabilities"]
            if item["id"] in expected_excluded
        ))
        self.assertTrue(expected_retained_paths <= inventory_paths)
        self.assertTrue(all((PROJECT_ROOT / "docs" / path).is_file() for path in expected_retained_paths))
        self.assertFalse((PROJECT_ROOT / "docs" / "crm" / "index.md").exists())
        self.assertFalse(any(path.startswith("crm/") for path in inventory_paths))
        self.assertNotIn("crm/", (PROJECT_ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        self.assertNotIn("crm/", (PROJECT_ROOT / "docs" / "index.md").read_text(encoding="utf-8"))
        self.assertEqual({"scope_complete": True}, checkpoint["menu_scope_reconciliation"])

    def test_navigation_groups_keep_all_areas_and_fichas(self) -> None:
        config = yaml.safe_load((PROJECT_ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        top_groups = [next(iter(item)) for item in config["nav"]]
        expected_hubs = {
            "recorridos/ventas/index.md",
            "recorridos/contactos-catalogo/index.md",
            "recorridos/servicios-estancias/index.md",
            "recorridos/compras-finanzas/index.md",
            "recorridos/operacion-comercial/index.md",
            "recorridos/administracion-configuracion/index.md",
        }
        expected_area_indexes = {
            "inicio/index.md", "ventas/index.md", "reportes-especializados/index.md",
            "contactos/index.md", "catalogo/index.md", "inventario/index.md",
            "servicios/index.md", "estancias/index.md", "especializados/index.md",
            "compras/index.md", "gastos/index.md", "caja/index.md", "reportes/index.md",
            "preventa/index.md", "distribucion/index.md", "fidelizacion/index.md",
            "administracion/index.md", "configuracion/index.md",
        }

        def leaves(value: object) -> list[str]:
            if isinstance(value, str):
                return [value]
            if isinstance(value, list):
                return [path for item in value for path in leaves(item)]
            if isinstance(value, dict):
                return [path for item in value.values() for path in leaves(item)]
            return []

        def assert_unique_labels(value: object) -> None:
            if isinstance(value, list):
                labels = [next(iter(item)) for item in value if isinstance(item, dict)]
                self.assertEqual(len(labels), len(set(labels)))
                for item in value:
                    assert_unique_labels(item)
            elif isinstance(value, dict):
                for item in value.values():
                    assert_unique_labels(item)

        nav_paths = leaves(config["nav"])
        ficha_paths = {
            document["path"]
            for document in yaml.safe_load((PROJECT_ROOT / "documentation" / "inventory.yml").read_text(encoding="utf-8"))["documents"]
        }
        homepage = (PROJECT_ROOT / "docs" / "index.md").read_text(encoding="utf-8")

        self.assertEqual(
            ["Inicio", "Ventas", "Contactos y catálogo", "Inventario", "Servicios y estancias", "Compras, gastos y caja", "Operación comercial", "Administración y configuración"],
            top_groups,
        )
        self.assertTrue(expected_area_indexes <= set(nav_paths))
        self.assertEqual(1, nav_paths.count("inventario/index.md"))
        self.assertEqual(expected_hubs, {path for path in nav_paths if path.startswith("recorridos/")})
        self.assertTrue(all(nav_paths.count(path) == 1 for path in expected_hubs))
        self.assertEqual(len(nav_paths), len(set(nav_paths)))
        self.assertEqual(ficha_paths, {path for path in nav_paths if not path.endswith("index.md")})
        self.assertEqual(88, len(ficha_paths))
        self.assertEqual(
            [
                "ventas/elegir-establecimiento/", "inicio/iniciar-sesion/", "recorridos/contactos-catalogo/",
                "recorridos/ventas/", "recorridos/contactos-catalogo/", "inventario/index/",
                "recorridos/servicios-estancias/", "recorridos/compras-finanzas/", "recorridos/operacion-comercial/",
                "recorridos/administracion-configuracion/",
            ],
            __import__("re").findall(r'href="([^"]+)"', homepage),
        )
        self.assertTrue(all((PROJECT_ROOT / "docs" / path).is_file() for path in expected_hubs))
        self.assertTrue(all((PROJECT_ROOT / "docs" / path).read_text(encoding="utf-8").count("](") >= 2 for path in expected_hubs))
        self.assertTrue({"navigation.path", "navigation.footer", "navigation.instant", "navigation.instant.progress"} <= set(config["theme"]["features"]))
        assert_unique_labels(config["nav"])



if __name__ == "__main__":
    unittest.main()
