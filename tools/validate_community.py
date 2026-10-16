"""MIT. Structural community-record checks; no authenticity or merge authority."""
import argparse
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = {}
for kind in ("statement", "decision"):
    schema = json.loads((ROOT / f"schemas/community-{kind}.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    VALIDATORS[kind] = Draft202012Validator(schema, format_checker=FormatChecker())


def structural(kind, record):
    return [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
            for e in VALIDATORS[kind].iter_errors(record)]


def validate_statement(record):
    errors = structural("statement", record)
    if errors:
        return sorted(errors)
    if record["mandate"]["kind"] == "delegated":
        if date.fromisoformat(record["mandate"]["valid_until"]) < date.fromisoformat(record["issued_at"]):
            errors.append("mandate: delegation expired before statement issuance")
    return sorted(errors)


def validate_decision(record, statements):
    errors = structural("decision", record)
    if errors:
        return sorted(errors)
    for statement in statements:
        errors.extend(validate_statement(statement))
    if errors:
        return sorted(errors)
    by_id = {s["statement_id"]: s for s in statements}
    if len(by_id) != len(statements):
        errors.append("statements: duplicate identifiers")
    reviews = record["review_statement_ids"]
    ratifiers = record["ratifier_statement_ids"]
    if not set(ratifiers).issubset(reviews):
        errors.append("ratifiers: must be included in reviewed statements")
    for ref in reviews + ratifiers:
        if ref not in by_id:
            errors.append(f"statements: missing reference {ref!r}")
    dispositions = {o["statement_id"]: o for o in record["objections"]}
    if len(dispositions) != len(record["objections"]):
        errors.append("objections: duplicate dispositions")
    for ref in dispositions:
        if ref not in reviews or ref not in by_id or by_id[ref]["verdict"] != "object":
            errors.append("objections: disposition must reference a reviewed objection")
    if errors:
        return sorted(set(errors))
    opened = date.fromisoformat(record["opened_at"])
    decided = date.fromisoformat(record["decided_at"])
    if decided < opened:
        errors.append("dates: decision precedes proposal opening")
    if date.fromisoformat(record["next_review"]) <= decided:
        errors.append("dates: next review must follow decision")
    accepted = record["outcome"] == "accepted"
    expected_label = ("maintainer_reference" if record["route"] == "maintainer_adoption" else "scoped_community_ratification") if accepted else "no_adoption"
    if record["adoption_label"] != expected_label:
        errors.append("adoption_label: incompatible with route and outcome")
    if accepted:
        minimum_days = {"editorial": 0, "technical": 7, "normative": 14, "constitutional": 30}[record["change_class"]]
        if (decided - opened).days < minimum_days:
            errors.append("review: proposed minimum period not met; emergency cases require separate review")
    for ref in reviews:
        s = by_id[ref]
        if s["proposal_id"] != record["proposal_id"] or s["target_commit"] != record["target_commit"]:
            errors.append("review: statement targets a different proposal or candidate commit")
        if not record["fictional"] and s["fictional"]:
            errors.append("review: fictional statement cannot support a real decision")
        issued = date.fromisoformat(s["issued_at"])
        if not opened <= issued <= decided:
            errors.append("review: statement date outside review window")
        if accepted and s["verdict"] == "object" and not s["withdrawn"]:
            if ref not in dispositions or dispositions[ref]["disposition"] == "deferred":
                errors.append("objections: accepted decision requires recorded treatment of each active objection")
    if record["route"] == "maintainer_adoption":
        if record["stage"] != "maintainer_led":
            errors.append("stage: maintainer adoption is only available in the maintainer-led stage")
        if ratifiers:
            errors.append("ratifiers: maintainer adoption must not claim community ratifiers")
    elif accepted:
        if record["stage"] != "community_governed" or not record["roster_ref"]:
            errors.append("ratification: adopted community stage and roster reference required")
        author, facilitator = record["author"], record["facilitator"]
        if (not author["control_domain"] or not facilitator["control_domain"] or
                author["actor_id"] == facilitator["actor_id"] or
                author["control_domain"] == facilitator["control_domain"]):
            errors.append("facilitator: non-author distinct declared control domain required")
        domains, actors = set(), set()
        for ref in ratifiers:
            s, actor = by_id[ref], by_id[ref]["actor"]
            if (s["statement_kind"] != "delegated_approval" or s["verdict"] != "support" or s["withdrawn"]):
                errors.append("ratifier: active delegated support required")
            mandate = s["mandate"]
            if (mandate["kind"] != "delegated" or "ratification" not in mandate.get("scope", []) or
                    date.fromisoformat(mandate.get("valid_until", "0001-01-01")) < decided):
                errors.append("ratifier: ratification mandate must remain valid on decision date")
            domain = actor["control_domain"]
            if (not domain or domain == author["control_domain"] or actor["id"] == author["actor_id"] or
                    s["independence"]["status"] != "declared"):
                errors.append("ratifier: distinct author-independent declared control required")
            if domain in domains or actor["id"] in actors:
                errors.append("ratifier: repeated actor/control domain cannot multiply standing")
            domains.add(domain)
            actors.add(actor["id"])
        if len(ratifiers) < 2:
            errors.append("ratification: at least two eligible independent ratifier records required")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("statement", "decision"))
    parser.add_argument("record", type=Path)
    parser.add_argument("--statements", type=Path, nargs="*", default=[])
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
        statements = [json.loads(p.read_text(encoding="utf-8")) for p in args.statements]
    except (OSError, ValueError) as error:
        print(f"Cannot read record: {error}")
        return 1
    errors = validate_statement(record) if args.kind == "statement" else validate_decision(record, statements)
    if errors:
        print("Invalid record:\n" + "\n".join(errors))
        return 1
    print("Record structurally valid under the proposed profile; authenticity, independence, consent, and authority are not verified. No merge is authorized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
