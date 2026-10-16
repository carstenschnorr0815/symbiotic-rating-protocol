"""MIT. Boundary cases against simulated consent and stale or dependent reviews."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("community_validator", ROOT / "tools/validate_community.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CommunityTests(unittest.TestCase):
    def setUp(self):
        self.statement = json.loads((ROOT / "examples/community-statement.json").read_text(encoding="utf-8"))
        self.decision = json.loads((ROOT / "examples/community-decision.json").read_text(encoding="utf-8"))

    def community_case(self):
        decision = copy.deepcopy(self.decision)
        decision.update(route="community_ratification", stage="community_governed", adoption_label="scoped_community_ratification", roster_ref="Fictional adopted roster", objections=[])
        decision["facilitator"] = {"actor_id": "facilitator", "control_domain": "facilitator-domain", "mandate_ref": "Fictional appointment"}
        statements = []
        for i, kind in enumerate(("human", "ai_system")):
            s = copy.deepcopy(self.statement)
            s.update(statement_id=f"review-{i}", statement_kind="delegated_approval", verdict="support")
            s["actor"].update(id=f"ratifier-{i}", kind=kind, operator=f"operator-{i}", control_domain=f"independent-{i}")
            s["mandate"] = {"kind": "delegated", "principal": f"constituency-{i}", "reference": "Fictional appointment", "scope": ["ratification"], "valid_until": "2027-01-01"}
            s["independence"] = {"status": "declared", "basis": "Synthetic distinct control for a test, not a real independence finding."}
            statements.append(s)
        decision["review_statement_ids"] = decision["ratifier_statement_ids"] = [s["statement_id"] for s in statements]
        return decision, statements

    def test_fictional_bootstrap_example_is_explicitly_scoped(self):
        self.assertEqual(module.validate_statement(self.statement), [])
        self.assertEqual(module.validate_decision(self.decision, [self.statement]), [])

    def test_delegated_approval_requires_a_delegation(self):
        self.statement.update(statement_kind="delegated_approval", verdict="support")
        self.assertTrue(module.validate_statement(self.statement))

    def test_bootstrap_cannot_claim_community_ratification(self):
        self.decision["adoption_label"] = "scoped_community_ratification"
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))
        self.decision.update(adoption_label="maintainer_reference", stage="community_governed")
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))

    def test_synthetic_community_records_pass_without_claiming_authenticity(self):
        d, ss = self.community_case()
        self.assertEqual(module.validate_decision(d, ss), [])

    def test_agent_copies_cannot_multiply_one_control_domain(self):
        d, ss = self.community_case()
        ss[1]["actor"]["control_domain"] = ss[0]["actor"]["control_domain"]
        self.assertTrue(module.validate_decision(d, ss))

    def test_author_control_or_unknown_independence_cannot_satisfy_quorum(self):
        for defect in ("author_domain", "unknown_domain", "disputed"):
            d, ss = self.community_case()
            if defect == "author_domain": ss[0]["actor"]["control_domain"] = d["author"]["control_domain"]
            if defect == "unknown_domain": ss[0]["actor"]["control_domain"] = None
            if defect == "disputed": ss[0]["independence"]["status"] = "disputed"
            with self.subTest(defect=defect): self.assertTrue(module.validate_decision(d, ss))

    def test_no_roster_or_inadequate_quorum_rejected(self):
        d, ss = self.community_case()
        d["roster_ref"] = None
        self.assertTrue(module.validate_decision(d, ss))
        d, ss = self.community_case()
        d["ratifier_statement_ids"] = [ss[0]["statement_id"]]
        self.assertTrue(module.validate_decision(d, ss))

    def test_stale_commit_withdrawn_or_expired_support_rejected(self):
        for defect in ("stale", "withdrawn", "expired", "non_ratifying_scope", "ordinary_position"):
            d, ss = self.community_case()
            if defect == "stale": ss[0]["target_commit"] = "b" * 40
            if defect == "withdrawn": ss[0]["withdrawn"] = True
            if defect == "expired": ss[0]["mandate"]["valid_until"] = "2026-10-15"
            if defect == "non_ratifying_scope": ss[0]["mandate"]["scope"] = ["technical_review"]
            if defect == "ordinary_position": ss[0]["statement_kind"] = "reasoned_position"
            with self.subTest(defect=defect): self.assertTrue(module.validate_decision(d, ss))

    def test_objection_cannot_be_ignored_or_left_deferred_on_acceptance(self):
        self.decision["objections"] = []
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))
        self.decision["objections"] = [{"statement_id": self.statement["statement_id"], "disposition": "deferred", "rationale": "Not resolved", "response_ref": "Fictional response"}]
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))

    def test_fictional_statements_cannot_support_real_decision(self):
        self.decision["fictional"] = False
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))

    def test_review_window_and_dates(self):
        self.decision["opened_at"] = "2026-10-15"
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))
        self.decision["opened_at"] = "2026-02-30"
        self.assertTrue(module.validate_decision(self.decision, [self.statement]))

    def test_self_facilitation_and_duplicate_statements_rejected(self):
        d, ss = self.community_case()
        d["facilitator"] = copy.deepcopy(d["author"])
        self.assertTrue(module.validate_decision(d, ss))
        d, ss = self.community_case()
        self.assertTrue(module.validate_decision(d, ss + [copy.deepcopy(ss[0])]))


if __name__ == "__main__":
    unittest.main()
