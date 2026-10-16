"""MIT. Register consistency only; no ratification, compatibility, or activation authority."""
import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/amendment-register.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def validate(record, root=ROOT):
    errors = [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}"
              for e in VALIDATOR.iter_errors(record)]
    if errors:
        return sorted(errors)
    root = Path(root).resolve()
    proposals = record["proposals"]
    by_id = {p["proposal_id"]: p for p in proposals}
    if len(by_id) != len(proposals):
        errors.append("proposals: duplicate IDs")
    graph = {}
    for p in proposals:
        pid = p["proposal_id"]
        graph[pid] = p["supersedes"] + p["repeals"]
        for ref in graph[pid]:
            if ref not in by_id or ref == pid:
                errors.append(f"{pid}: invalid/self-referencing replacement or repeal")
        for value in [p["text_path"]] + ([p["decision_ref"]] if p["decision_ref"] else []):
            candidate = (root / value).resolve()
            if not candidate.is_relative_to(root) or not candidate.is_file():
                errors.append(f"{pid}: referenced file missing or outside repository")
        adopted = p["status"] in ("maintainer_reference", "ratified", "active", "superseded", "repealed")
        if adopted:
            if not p["decision_ref"] or not p["text_commit"]:
                errors.append(f"{pid}: adopted status requires decision reference and exact text commit")
            expected = "maintainer_reference" if p["status"] == "maintainer_reference" else "community_ratification"
            if p["adoption_route"] != expected:
                errors.append(f"{pid}: adopted status inconsistent with adoption route")
        elif any(p[k] is not None for k in ("adoption_route", "decision_ref", "text_commit", "effective_from")):
            errors.append(f"{pid}: unadopted proposal must not claim adoption metadata")
        if p["status"] == "active":
            if not p["effective_from"]:
                errors.append(f"{pid}: active status requires effective date")
            if record["constitutional_status"] != "community_ratified":
                errors.append(f"{pid}: active community amendment cannot rest on an unratified constitution")
    visited, visiting = set(), set()
    def visit(pid):
        if pid in visiting:
            return True
        if pid in visited:
            return False
        visiting.add(pid)
        cyclic = any(visit(ref) for ref in graph.get(pid, []) if ref in graph)
        visiting.remove(pid)
        visited.add(pid)
        return cyclic
    if any(visit(pid) for pid in graph):
        errors.append("proposals: cyclic replacement/repeal relationship")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.register.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Cannot read register: {error}")
        return 1
    errors = validate(record)
    if errors:
        print("Invalid register:\n" + "\n".join(errors))
        return 1
    print("Register structurally consistent. Ratification, decision authenticity, temporal activation, and constitutional compatibility are not established.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
