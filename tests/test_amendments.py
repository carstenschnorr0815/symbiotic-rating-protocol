"""MIT. Prevent a publication record from masquerading as adoption."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("amendment_validator", ROOT / "tools/validate_amendments.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AmendmentTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / "amendments/index.json").read_text(encoding="utf-8"))

    def test_all_current_candidates_are_unadopted(self):
        self.assertEqual(module.validate(self.record), [])

    def test_missing_decision_cannot_establish_ratification(self):
        self.record["proposals"][0]["status"] = "ratified"
        self.assertTrue(module.validate(self.record))

    def test_proposal_cannot_claim_effective_date(self):
        self.record["proposals"][0]["effective_from"] = "2026-10-16"
        self.assertTrue(module.validate(self.record))

    def test_maintainer_route_cannot_claim_community_ratification(self):
        p = self.record["proposals"][0]
        p.update(status="ratified", adoption_route="maintainer_reference", decision_ref="RATIFICATION.md", text_commit="a" * 40)
        self.assertTrue(module.validate(self.record))

    def test_active_requires_constitution_and_effective_date(self):
        p = self.record["proposals"][0]
        p.update(status="active", adoption_route="community_ratification", decision_ref="RATIFICATION.md", text_commit="a" * 40, effective_from="2026-10-16")
        self.assertTrue(module.validate(self.record))
        self.record["constitutional_status"] = "community_ratified"
        p["effective_from"] = None
        self.assertTrue(module.validate(self.record))

    def test_duplicate_ids_self_reference_and_cycles(self):
        record = copy.deepcopy(self.record)
        record["proposals"].append(copy.deepcopy(record["proposals"][0]))
        self.assertTrue(module.validate(record))
        self.record["proposals"][0]["supersedes"] = ["AM-P001"]
        self.assertTrue(module.validate(self.record))
        self.record["proposals"][0]["supersedes"] = ["AM-P002"]
        self.record["proposals"][1]["supersedes"] = ["AM-P001"]
        self.assertTrue(module.validate(self.record))

    def test_unknown_references_and_external_paths_rejected(self):
        self.record["proposals"][0]["repeals"] = ["AM-P999"]
        self.assertTrue(module.validate(self.record))
        self.record["proposals"][0]["repeals"] = []
        self.record["proposals"][0]["text_path"] = "../.work/check-repository.py"
        self.assertTrue(module.validate(self.record))


if __name__ == "__main__":
    unittest.main()
