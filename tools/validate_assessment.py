"""MIT. Structural checks only; no truth, compliance, or deployment verdict."""
import argparse
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/assessment.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def validate(record):
    errors = [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
              for e in VALIDATOR.iter_errors(record)]
    if errors:
        return sorted(errors)
    for collection in ("participants", "evidence"):
        ids = [item["id"] for item in record[collection]]
        if len(ids) != len(set(ids)):
            errors.append(f"{collection}: duplicate identifiers")
    evidence = {item["id"] for item in record["evidence"]}
    for law, finding in record["laws"].items():
        for ref in finding["evidence_refs"]:
            if ref not in evidence:
                errors.append(f"laws/{law}: unknown evidence reference {ref!r}")
    start, end = (date.fromisoformat(record["period"][key]) for key in ("start", "end"))
    if end < start:
        errors.append("period: end precedes start")
    if date.fromisoformat(record["review"]["next_review"]) <= end:
        errors.append("review: next_review must follow observation period")
    if not record["fictional"] and any(e["access"] == "fictional" for e in record["evidence"]):
        errors.append("evidence: fictional evidence cannot support a non-fictional record")
    return sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Cannot read assessment: {error}")
        return 1
    errors = validate(record)
    if errors:
        print("Invalid record:\n" + "\n".join(errors))
        return 1
    print("Record structurally valid; this is not approval or a rating.")
    needs_review = [law for law, finding in record["laws"].items() if finding["status"] != "supported"]
    print("Findings requiring review: " + (", ".join(needs_review) or "none flagged; institutional review still required"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
