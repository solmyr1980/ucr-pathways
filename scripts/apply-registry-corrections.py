"""Replay researched post-build overrides without changing upstream provenance."""
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    "programme_type", "current_status", "production_eligible", "production_order",
    "study_load_ec", "duration_years", "languages_json", "modes_json",
    "institution_ids_json", "display_name_en", "consortium",
}


def apply(registry, ledger):
    reader = csv.DictReader(io.StringIO(registry))
    rows = list(reader)
    ids = [row["counselor_programme_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate permanent IDs in registry")
    by_id = dict(zip(ids, rows))
    seen = set()
    for correction in ledger["corrections"]:
        target = correction["counselor_programme_id"]
        if target in seen or target not in by_id:
            raise ValueError(f"Duplicate or missing correction target: {target}")
        seen.add(target)
        row = by_id[target]
        if not correction["sources"] or not correction["reason"].strip():
            raise ValueError(f"Missing research evidence: {target}")
        for field, value in correction["identity_guard"].items():
            if row.get(field) != value:
                raise ValueError(f"{target}: changed identity/provenance field {field}")
        for field, value in correction["overrides"].items():
            if field not in ALLOWED or not isinstance(value, str):
                raise ValueError(f"{target}: unsupported override {field}")
            if row.get(field) not in (correction["before"][field], value):
                raise ValueError(f"{target}: conflicting current value for {field}")
            row[field] = value
        attributes = json.loads(row["corrected_attributes_json"] or "{}")
        attributes.update(correction["overrides"])
        attributes["post_build_correction_id"] = correction["correction_id"]
        row["corrected_attributes_json"] = json.dumps(attributes, ensure_ascii=False, separators=(",", ":"))
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "data/registry/programmes.csv")
    parser.add_argument("--ledger", type=Path, default=ROOT / "data/registry/post-build-corrections.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    original = args.registry.read_text(encoding="utf-8")
    result = apply(original, json.loads(args.ledger.read_text(encoding="utf-8")))
    if args.check:
        if result != original:
            raise SystemExit("Registry differs from researched post-build overrides")
        print("Registry post-build corrections are current")
    else:
        (args.output or args.registry).write_text(result, encoding="utf-8")
        print("Applied registry post-build corrections")
