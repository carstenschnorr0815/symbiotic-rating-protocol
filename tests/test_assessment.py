"""MIT. Boundary cases that prevent misleading structural acceptance."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("assessment_validator", ROOT / "tools/validate_assessment.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / "examples/watershed-assessment.json").read_text(encoding="utf-8"))

    def test_example_and_explicit_unknown_without_evidence(self):
        self.assertEqual(module.validate(self.record), [])
        self.record["laws"]["I"]["evidence_refs"] = []
        self.assertEqual(module.validate(self.record), [])

    def test_all_four_laws_required(self):
        for law in ("I", "II", "III", "IV"):
            with self.subTest(law=law):
                record = copy.deepcopy(self.record)
                del record["laws"][law]
                self.assertTrue(module.validate(record))

    def test_support_requires_referenced_evidence(self):
        self.record["laws"]["IV"]["evidence_refs"] = []
        self.assertTrue(module.validate(self.record))
        self.record["laws"]["IV"]["evidence_refs"] = ["invented-id"]
        self.assertTrue(module.validate(self.record))

    def test_duplicate_ids_are_rejected(self):
        for collection in ("participants", "evidence"):
            with self.subTest(collection=collection):
                record = copy.deepcopy(self.record)
                record[collection].append(copy.deepcopy(record[collection][0]))
                self.assertTrue(module.validate(record))

    def test_invalid_or_reversed_dates(self):
        for key, value in (("start", "2026-02-30"), ("end", "2020-01-01")):
            with self.subTest(key=key):
                record = copy.deepcopy(self.record)
                record["period"][key] = value
                self.assertTrue(module.validate(record))
        self.record["review"]["next_review"] = self.record["period"]["end"]
        self.assertTrue(module.validate(self.record))

    def test_unknown_consent_is_valid_but_arbitrary_value_is_not(self):
        self.record["participants"][0]["consent"] = "implied_by_model"
        self.assertTrue(module.validate(self.record))

    def test_fictional_evidence_cannot_be_presented_as_real(self):
        self.record["fictional"] = False
        self.assertTrue(module.validate(self.record))

    def test_empty_rationale_and_extra_approval_fields_rejected(self):
        self.record["laws"]["I"]["rationale"] = "   "
        self.assertTrue(module.validate(self.record))
        self.record["laws"]["I"]["rationale"] = "Unknown pending investigation."
        self.record["approved"] = True
        self.assertTrue(module.validate(self.record))


if __name__ == "__main__":
    unittest.main()
