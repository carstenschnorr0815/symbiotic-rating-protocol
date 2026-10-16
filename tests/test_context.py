"""MIT. Prevent structurally misleading context/acknowledgement records."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("context_validator", ROOT / "tools/validate_context.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / "examples/context-record.json").read_text(encoding="utf-8"))

    def test_example_allows_unknown_and_disputed_framing(self):
        self.assertEqual(module.validate(self.record), [])
        self.record["acknowledgements"][1]["status"] = "disputed"
        self.assertEqual(module.validate(self.record), [])

    def test_missing_or_duplicate_acknowledgements_rejected(self):
        for operation in ("missing", "duplicate", "unlisted"):
            record = copy.deepcopy(self.record)
            if operation == "missing": record["acknowledgements"].pop()
            if operation == "duplicate": record["acknowledgements"].append(copy.deepcopy(record["acknowledgements"][0]))
            if operation == "unlisted": record["acknowledgements"][0]["participant_id"] = "forest"
            with self.subTest(operation=operation): self.assertTrue(module.validate(record))

    def test_participant_and_proposer_integrity(self):
        self.record["change"]["proposer"] = "unlisted"
        self.assertTrue(module.validate(self.record))
        self.record["change"]["proposer"] = "human"
        self.record["participants"].append(copy.deepcopy(self.record["participants"][0]))
        self.assertTrue(module.validate(self.record))

    def test_multiple_and_custom_levels_are_valid_if_declared(self):
        self.record["level_vocabulary"]["definitions"]["HABITAT"] = "Locally defined habitat observation context"
        self.record["levels"] = ["ARCHITECTURE", "HABITAT"]
        self.assertEqual(module.validate(self.record), [])
        self.record["levels"].append("UNDECLARED")
        self.assertTrue(module.validate(self.record))

    def test_parent_order_and_initial_state(self):
        for parent in (None, 2, 3):
            with self.subTest(parent=parent):
                self.record["parent_version"] = parent
                self.assertTrue(module.validate(self.record))
        self.record["context_version"] = 1
        self.record["parent_version"] = None
        self.assertEqual(module.validate(self.record), [])
        self.record["parent_version"] = 1
        self.assertTrue(module.validate(self.record))

    def test_marker_cannot_supply_an_approval_field(self):
        self.record["approved"] = True
        self.assertTrue(module.validate(self.record))


if __name__ == "__main__":
    unittest.main()
