"""MIT. Validate a context record's structure; no semantic or consent verdict."""
import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/context-record.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA)


def validate(record):
    errors = [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
              for e in VALIDATOR.iter_errors(record)]
    if errors:
        return sorted(errors)
    ids = [p["id"] for p in record["participants"]]
    if len(ids) != len(set(ids)):
        errors.append("participants: duplicate identifiers")
    if record["change"]["proposer"] not in ids:
        errors.append("change: proposer must reference a listed participant")
    ack_ids = [a["participant_id"] for a in record["acknowledgements"]]
    if len(ack_ids) != len(set(ack_ids)) or set(ack_ids) != set(ids):
        errors.append("acknowledgements: exactly one entry per listed participant required")
    definitions = record["level_vocabulary"]["definitions"]
    for level in record["levels"] + record["change"]["previous_levels"]:
        if level not in definitions:
            errors.append(f"levels: undeclared level {level!r}")
    parent, version = record["parent_version"], record["context_version"]
    if version == 1 and parent is not None:
        errors.append("parent_version: initial context must have no parent")
    if version > 1 and (parent is None or parent >= version):
        errors.append("parent_version: revised context must refer to an earlier version")
    return sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Cannot read context: {error}")
        return 1
    errors = validate(record)
    if errors:
        print("Invalid context record:\n" + "\n".join(errors))
        return 1
    print("Context record structurally valid; understanding, consent, and authority are not established.")
    pending = [a["participant_id"] for a in record["acknowledgements"] if a["status"] != "confirmed"]
    print("Unconfirmed or disputed framing: " + (", ".join(pending) or "none recorded; no action approval follows"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
