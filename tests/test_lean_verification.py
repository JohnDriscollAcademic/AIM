"""Regression checks for project selection and truthful metadata coverage."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import yaml
import jsonschema

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

projects = load("lean_projects", ROOT / "tools/lean/projects.py")
manifest = load("lean_manifest", ROOT / "tools/lean/validate_manifest.py")
SCHEMA = json.loads((ROOT / "docs/lean/schema/v0.4.schema.json").read_text())

class ProjectSelectionTests(unittest.TestCase):
    def setUp(self):
        self.projects = [
            {"id": "001", "project": "research/lean/001", "canonical": "problems/001-first.md"},
            {"id": "652", "project": "research/lean/652", "canonical": "research/resolved/652-second.md"}]

    def catalogue(self, root, rows=None, retired=None):
        (root / "data").mkdir(exist_ok=True)
        (root / "data/test.json").write_text(json.dumps(
            rows if rows is not None else [{"id": "001", "file": "problems/001-first.md"}]))
        (root / "catalogue.json").write_text(json.dumps({"retired": retired or []}))

    def test_problem_proof_change_selects_only_that_problem(self):
        self.assertEqual(projects.select(self.projects, ["research/lean/652/Solution.lean"]),
                         [self.projects[1]])

    def test_canonical_statement_change_rechecks_its_project(self):
        self.assertEqual(projects.select(self.projects, ["problems/001-first.md"]),
                         [self.projects[0]])

    def test_archived_record_change_rechecks_its_project(self):
        self.assertEqual(projects.select(self.projects, ["research/resolved/652-second.md"]),
                         [self.projects[1]])

    def test_shared_checker_or_schema_change_rechecks_every_project(self):
        for change in ["tools/lean/harness.py", "docs/lean/schema/v0.4.schema.json",
                       ".github/workflows/lean-verification.yml", "catalogue.json", "data/test.json"]:
            with self.subTest(change=change):
                self.assertEqual(projects.select(self.projects, [change]), self.projects)

    def test_unrelated_document_does_not_rebuild_proofs(self):
        for change in ["README.md", "problems/002-other.md", "research/resolved/653-other.md",
                       "research/lean/README.md", "research/lean/0010/Draft.lean"]:
            with self.subTest(change=change):
                self.assertEqual(projects.select(self.projects, [change]), [])

    def test_control_fixture_toolchain_does_not_rebuild_problem_projects(self):
        self.assertEqual(projects.select(self.projects, ["docs/lean/ci-toolchain/lean-toolchain"]), [])

    def test_discovery_uses_existing_catalogue_and_detects_incomplete_project(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root, retired=[{"id": "652", "record": "research/resolved/652-second.md"}])
            for entry in self.projects:
                project = root / entry["project"]
                project.mkdir(parents=True)
                (project / "formalization.yaml").write_text("version: v0.4\n")
            self.assertEqual(projects.discover(root), self.projects)

    def test_invalid_canonical_paths_are_rejected(self):
        for path in ["../outside/README.md", "/problems/001.md", "problems/../001.md",
                     "problems//001.md", "problems/001.txt", "research/001.md"]:
            with self.subTest(path=path), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.catalogue(root, rows=[{"id": "001", "file": path}])
                with self.assertRaises(ValueError):
                    projects.discover(root)

    def test_invalid_or_noncanonical_ids_are_rejected(self):
        for identifier in ["1", "01", "0001", "000", "ABC", "../001", 1]:
            with self.subTest(identifier=identifier), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.catalogue(root, rows=[{"id": identifier, "file": "problems/001-first.md"}])
                with self.assertRaises(ValueError):
                    projects.discover(root)

    def test_four_digit_ids_are_supported_and_sorted_numerically(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root, rows=[{"id": identifier, "file": f"problems/{identifier}-first.md"}
                                       for identifier in ["1000", "999"]])
            for identifier in ["1000", "999"]:
                (root / "research/lean" / identifier).mkdir(parents=True)
            self.assertEqual([entry["id"] for entry in projects.discover(root)], ["999", "1000"])

    def test_duplicate_id_across_active_and_retired_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root, retired=[{"id": "001", "record": "research/resolved/001-first.md"}])
            with self.assertRaisesRegex(ValueError, "Duplicate AIM problem ID"):
                projects.discover(root)

    def test_malformed_retired_mapping_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root, retired=[{"id": "652"}])
            with self.assertRaisesRegex(ValueError, "Missing canonical record"):
                projects.discover(root)

    def test_source_only_project_cannot_skip_verification(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root)
            project = root / "research/lean/001"
            project.mkdir(parents=True)
            (project / "Challenge.lean").write_text("-- incomplete source-only draft\n")
            self.assertEqual(projects.discover(root), [self.projects[0]])

    def test_unknown_project_cannot_skip_verification(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root)
            (root / "research/lean/999").mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "Unregistered AIM Lean project"):
                projects.discover(root)

    def test_symlinked_project_or_ancestor_is_rejected(self):
        for relative in ["research", "research/lean", "research/lean/001"]:
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.catalogue(root)
                (root / "elsewhere").mkdir()
                project = root / relative
                project.parent.mkdir(parents=True, exist_ok=True)
                project.symlink_to(root / "elsewhere", target_is_directory=True)
                with self.assertRaisesRegex(ValueError, "ordinary directory"):
                    projects.discover(root)

    def test_broken_symlinked_project_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root)
            project = root / "research/lean/001"
            project.parent.mkdir(parents=True)
            project.symlink_to(root / "missing", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "ordinary directory"):
                projects.discover(root)

    def test_project_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.catalogue(root)
            project = root / "research/lean/001"
            project.parent.mkdir(parents=True)
            project.write_text("not a directory")
            with self.assertRaisesRegex(ValueError, "ordinary directory"):
                projects.discover(root)


class ProjectSelectionGitTests(unittest.TestCase):
    """Exercise the CLI against real base/head trees, including Git path quoting."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        self.root.mkdir()
        self.output = Path(self.temporary.name) / "github-output"
        self.git("init", "-q")
        self.registry = {"001": "problems/001-first.md",
                         "652": "research/resolved/652-second.md",
                         "003": "problems/003-third.md"}
        (self.root / "data").mkdir()
        (self.root / "data/test.json").write_text(json.dumps(
            [{"id": identifier, "file": path} for identifier, path in self.registry.items()
             if identifier != "652"]))
        (self.root / "catalogue.json").write_text(json.dumps(
            {"retired": [{"id": "652", "record": self.registry["652"]}]}))
        for identifier, canonical in self.registry.items():
            readme = self.root / canonical
            readme.parent.mkdir(parents=True, exist_ok=True)
            readme.write_text(f"# {identifier}\n\n**Status:** Lean verified\n")
            if identifier != "003":
                project = self.root / "research/lean" / identifier
                project.mkdir(parents=True)
                for name in ["Challenge.lean", "Solution.lean"]:
                    (project / name).write_text("-- source-presence fixture\n")
        self.commit("base fixture")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args],
                                       text=True, stderr=subprocess.STDOUT)

    def commit(self, message):
        self.git("add", "-A")
        self.git("-c", "user.name=Lean selector test", "-c", "user.email=test@localhost",
                 "commit", "-qm", message)

    def run_selection(self, base=None, all_projects=False):
        self.output.write_text("")
        mode = ["--all"] if all_projects else ["--base-ref", base or self.base]
        return subprocess.run(
            [sys.executable, str(ROOT / "tools/lean/projects.py"), "--root", str(self.root),
             *mode, "--github-output", str(self.output)], text=True, capture_output=True)

    def selected_ids(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        entries = json.loads(result.stdout)["include"]
        for entry in entries:
            self.assertEqual(set(entry), {"id", "project"})
        return [entry["id"] for entry in entries]

    def run_tools_changed(self, base=None):
        workflow = yaml.safe_load((ROOT / ".github/workflows/lean-verification.yml").read_text())
        step = next(step for step in workflow["jobs"]["select"]["steps"]
                    if step.get("id") == "projects")
        detector = re.search(r"<<'PY'\n(.*?)\nPY(?:\n|$)", step["run"], re.S)
        self.assertIsNotNone(detector, "workflow must retain its inline shared-tool detector")
        self.output.write_text("")
        result = subprocess.run([sys.executable, "-", base or self.base, str(self.output)],
                                input=detector.group(1), cwd=self.root,
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return self.output.read_text()

    def test_all_projects_returns_only_id_and_project_fields(self):
        self.assertEqual(self.selected_ids(self.run_selection(all_projects=True)), ["001", "652"])
        self.assertIn("count=2\n", self.output.read_text())

    def test_unicode_quoted_and_newline_filenames_select_project(self):
        for name in ["Δ.lean", 'quoted"name.lean', "line\nbreak.lean"]:
            with self.subTest(name=name):
                base = self.git("rev-parse", "HEAD").strip()
                (self.root / "research/lean/001" / name).write_text("-- changed proof input\n")
                self.commit("proof input with special filename")
                self.assertEqual(self.selected_ids(self.run_selection(base)), ["001"])

    def test_complete_project_deletion_fails_selection(self):
        shutil.rmtree(self.root / "research/lean/001")
        self.commit("remove project while retaining its canonical page")
        result = self.run_selection()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("research/lean/001", result.stderr)
        self.assertIn("removed or renamed", result.stderr)
        self.assertEqual(self.output.read_text(), "")

    def test_complete_project_rename_fails_selection(self):
        (self.root / "research/lean/001").rename(self.root / "research/001-lean-archive")
        self.commit("rename project away from its registered location")
        result = self.run_selection()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("research/lean/001", result.stderr)
        self.assertIn("removed or renamed", result.stderr)
        self.assertEqual(self.output.read_text(), "")

    def test_project_and_registry_entry_deletion_cannot_hide_project(self):
        shutil.rmtree(self.root / "research/lean/001")
        (self.root / "data/test.json").write_text(json.dumps(
            [{"id": "003", "file": self.registry["003"]}]))
        self.commit("remove project and its registration")
        result = self.run_selection()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("removed or renamed", result.stderr)
        self.assertEqual(self.output.read_text(), "")

    def test_partial_project_deletion_still_selects_project(self):
        (self.root / "research/lean/001/Solution.lean").unlink()
        self.commit("remove one proof input")
        self.assertEqual(self.selected_ids(self.run_selection()), ["001"])

    def test_renamed_file_selects_both_surviving_projects(self):
        (self.root / "research/lean/001/Solution.lean").rename(
            self.root / "research/lean/652/Moved.lean")
        self.commit("move a proof input between projects")
        self.assertEqual(self.selected_ids(self.run_selection()), ["001", "652"])

    def test_new_source_only_project_for_existing_id_is_selected(self):
        project = self.root / "research/lean/003"
        project.mkdir()
        (project / "Draft.lean").write_text("-- incomplete new formalization\n")
        self.commit("add source-only project")
        self.assertEqual(self.selected_ids(self.run_selection()), ["003"])

    def test_active_and_retired_canonical_changes_select_only_corresponding_project(self):
        for identifier in ["001", "652"]:
            with self.subTest(identifier=identifier):
                base = self.git("rev-parse", "HEAD").strip()
                (self.root / self.registry[identifier]).write_text("# Changed canonical statement\n")
                self.commit("update canonical statement")
                self.assertEqual(self.selected_ids(self.run_selection(base)), [identifier])

    def test_base_before_lean_infrastructure_is_supported(self):
        shutil.rmtree(self.root / "research/lean")
        self.commit("fixture without Lean projects")
        base = self.git("rev-parse", "HEAD").strip()
        project = self.root / "research/lean/001"
        project.mkdir(parents=True)
        (project / "Draft.lean").write_text("-- first Lean project\n")
        self.commit("introduce first project")
        self.assertEqual(self.selected_ids(self.run_selection(base)), ["001"])

    def test_base_before_catalogue_infrastructure_is_supported(self):
        self.git("rm", "-r", "research/lean", "catalogue.json", "data")
        self.commit("fixture before catalogue and Lean infrastructure")
        base = self.git("rev-parse", "HEAD").strip()
        self.git("checkout", self.base, "--", "research/lean", "catalogue.json", "data")
        self.commit("introduce catalogue and Lean projects")
        self.assertEqual(self.selected_ids(self.run_selection(base)), ["001", "652"])

    def test_workflow_unicode_quoted_newline_tool_changes_request_controls(self):
        directory = self.root / "tools/lean"
        directory.mkdir(parents=True)
        for name in ["Δ.py", 'quoted"name.py', "line\nbreak.py"]:
            with self.subTest(name=name):
                base = self.git("rev-parse", "HEAD").strip()
                (directory / name).write_text("# shared control fixture\n")
                self.commit("shared tool with special filename")
                self.assertEqual(self.run_tools_changed(base), "tools_changed=true\n")

    def test_workflow_renamed_away_tool_requests_controls(self):
        tool = self.root / "tools/lean/helper.py"
        tool.parent.mkdir(parents=True)
        tool.write_text("# identical contents for rename detection\n")
        self.commit("shared tool before rename")
        base = self.git("rev-parse", "HEAD").strip()
        archive = self.root / "archive/helper.py"
        archive.parent.mkdir()
        tool.rename(archive)
        self.commit("rename shared tool outside control directory")
        self.assertEqual(self.run_tools_changed(base), "tools_changed=true\n")

    def test_workflow_control_fixture_toolchain_requests_only_controls(self):
        pin = self.root / "docs/lean/ci-toolchain/lean-toolchain"
        pin.parent.mkdir(parents=True)
        pin.write_text("control fixture toolchain\n")
        self.commit("control fixture pin change")
        self.assertEqual(self.run_tools_changed(), "tools_changed=true\n")
        self.assertEqual(self.selected_ids(self.run_selection()), [])


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "Solution.lean").write_text("-- source-presence fixture, not a proof\n")
        self.config = {"challenge_module": "Challenge", "solution_module": "Solution",
                       "theorem_names": ["NLA.Test.result"], "definition_names": [],
                       "permitted_axioms": sorted(manifest.ALLOWED_AXIOMS)}
        self.metadata = {
            "version": "v0.4",
            "project": {"name": "Fixture", "authors": ["Test author"], "license": "Apache-2.0"},
            "sources": [{"title": "Test source", "type": "original-proof"}],
            "automation": {"methods": [{"method": "manual"}]},
            "review": {"status": "unchecked"},
            "status": {"sorry_count": 0, "sorry_in_definitions": 0, "axioms": [],
                       "main_results": [{"declaration": "NLA.Test.result", "file": "Solution.lean",
                                         "sorry_count": 0, "axioms": [],
                                         "comparator_config": "comparator.json"}]}}

    def run_check(self):
        (self.root / "formalization.yaml").write_text(yaml.safe_dump(self.metadata))
        (self.root / "comparator.json").write_text(json.dumps(self.config))
        manifest.validate(self.root, SCHEMA)

    def test_valid_consistent_metadata(self):
        self.run_check()

    def test_duplicate_yaml_status_is_rejected(self):
        (self.root / "formalization.yaml").write_text(
            "status:\n  sorry_count: 1\n" + yaml.safe_dump(self.metadata))
        (self.root / "comparator.json").write_text(json.dumps(self.config))
        with self.assertRaisesRegex(ValueError, "Duplicate.*status"):
            manifest.validate(self.root, SCHEMA)

    def test_duplicate_nested_yaml_key_is_rejected(self):
        (self.root / "formalization.yaml").write_text(
            yaml.safe_dump(self.metadata).replace("sorry_count: 0", "sorry_count: 1\n  sorry_count: 0", 1))
        (self.root / "comparator.json").write_text(json.dumps(self.config))
        with self.assertRaisesRegex(ValueError, "Duplicate.*sorry_count"):
            manifest.validate(self.root, SCHEMA)

    def test_duplicate_comparator_key_is_rejected(self):
        (self.root / "formalization.yaml").write_text(yaml.safe_dump(self.metadata))
        (self.root / "comparator.json").write_text(
            '{"permitted_axioms":["sorryAx"],' + json.dumps(self.config)[1:])
        with self.assertRaisesRegex(ValueError, "Duplicate.*permitted_axioms"):
            manifest.validate(self.root, SCHEMA)

    def test_missing_required_schema_field(self):
        del self.metadata["sources"]
        with self.assertRaises(jsonschema.ValidationError): self.run_check()

    def test_unchecked_export_is_rejected(self):
        self.metadata["status"]["main_results"].append({
            "declaration": "NLA.Test.unchecked", "file": "Solution.lean", "sorry_count": 0,
            "axioms": [], "comparator_config": "comparator.json"})
        with self.assertRaises(ValueError): self.run_check()

    def test_empty_theorem_list_is_rejected(self):
        self.config["theorem_names"] = []
        with self.assertRaises(ValueError): self.run_check()

    def test_custom_or_native_trust_is_rejected(self):
        for axiom in ["sorryAx", "Lean.ofReduceBool", "NLA.secretAx"]:
            self.config["permitted_axioms"] = [axiom]
            with self.assertRaises(ValueError): self.run_check()

    def test_nonzero_proof_sorries_rejected(self):
        self.metadata["status"]["sorry_count"] = 1
        with self.assertRaises(ValueError): self.run_check()

    def test_definition_hole_rejected(self):
        self.config["definition_names"] = ["NLA.Test.meaning"]
        with self.assertRaises(ValueError): self.run_check()

    def test_result_source_outside_project_rejected(self):
        self.metadata["status"]["main_results"][0]["file"] = "../other/Solution.lean"
        with self.assertRaises(ValueError): self.run_check()

    def test_result_specific_unchecked_axiom_rejected(self):
        self.metadata["status"]["main_results"][0]["axioms"] = ["NLA.assumeTarget"]
        with self.assertRaises(ValueError): self.run_check()

if __name__ == "__main__":
    unittest.main()
