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


# A retained alias keeps its permanent row and raw identifiers. Only the active
# owner's normalized provenance and generated target mappings are consolidated.
PROVENANCE_ARRAYS = (
    'source_excel_rows_json', 'offering_ids_json', 'programme_unit_codes_json',
    'recognized_programme_codes_json', 'variant_of_codes_json',
    'registry_record_types_json', 'source_provider_ids_json',
)


def alias_registry(rows, ledger):
    by_id = {row['counselor_programme_id']: row for row in rows}
    aliases = ledger.get('target_aliases', [])
    alias_ids = [a['alias_id'] for a in aliases]
    if len(alias_ids) != len(set(alias_ids)):
        raise ValueError('Duplicate retained alias')
    for a in aliases:
        if a['owner_id'] in alias_ids or a['owner_id'] == a['alias_id']:
            raise ValueError('Alias chains and cycles are not supported')
        if not a['sources'] or not a['reason'].strip():
            raise ValueError('Alias lacks researched evidence')
        if a['owner_id'] not in by_id or a['alias_id'] not in by_id:
            raise ValueError('Alias or owner permanent ID is missing')
        owner, alias = by_id[a['owner_id']], by_id[a['alias_id']]
        for field, value in a['alias_guard'].items():
            if alias.get(field) != value:
                raise ValueError('Changed retained alias provenance: '+field)
        if owner['production_eligible'] != 'true' or not owner['production_order']:
            raise ValueError('Alias owner is not eligible')
        if alias['current_status'] not in (a['alias_before']['current_status'], 'retained-alias'):
            raise ValueError('Conflicting alias lifecycle')
        for field, expected in [('production_eligible', 'false'), ('production_order', '')]:
            if alias[field] not in (a['alias_before'][field], expected):
                raise ValueError('Conflicting alias eligibility')
        for field, value in a['owner_guard'].items():
            if field in PROVENANCE_ARRAYS:
                first = json.loads(value)
                combined = first + [v for v in json.loads(a['alias_guard'][field]) if v not in first]
                if json.loads(owner[field]) not in (first, combined):
                    raise ValueError('Changed owner provenance: '+field)
                owner[field] = json.dumps(combined, ensure_ascii=False, separators=(',', ':'))
            elif owner.get(field) != value:
                raise ValueError('Changed alias owner identity: '+field)
        alias.update(current_status='retained-alias', production_eligible='false', production_order='')
        for row, additions in [(owner, {'absorbed_alias_ids': [a['alias_id']]}),
                               (alias, {'alias_of_counselor_programme_id': a['owner_id']})]:
            attributes = json.loads(row['corrected_attributes_json'] or '{}')
            attributes.update(additions)
            attributes['post_build_alias_id'] = a['alias_id']
            row['corrected_attributes_json'] = json.dumps(attributes, ensure_ascii=False, separators=(',', ':'))


def alias_crosswalk(original, kind, ledger):
    reader = csv.DictReader(io.StringIO(original))
    rows = list(reader)
    for a in ledger.get('target_aliases', []):
        alias_source_rows = {str(v) for v in json.loads(a['alias_guard']['source_excel_rows_json'])}
        owner_source_rows = {str(v) for v in json.loads(a['owner_guard']['source_excel_rows_json'])}
        for row in rows:
            source = row['source_excel_row']
            target = row['counselor_programme_id']
            if source in alias_source_rows:
                if target not in (a['alias_id'], a['owner_id']):
                    raise ValueError('Alias source has conflicting crosswalk owner')
                if kind == 'programme_offerings' and row['AANGEBODEN_OPLEIDINGCODE'] not in json.loads(a['alias_guard']['offering_ids_json']):
                    raise ValueError('Alias source has changed offering UUID')
                row['counselor_programme_id'] = a['owner_id']
                if kind == 'programme_source_rows':
                    row['mapping_status'] = 'merged-source-rows'
                    row['mapping_basis'] = 'post-build-retained-alias'
            elif target == a['alias_id']:
                raise ValueError('Unexpected source row mapped to retained alias')
            if kind == 'programme_source_rows' and source in owner_source_rows:
                if target != a['owner_id']:
                    raise ValueError('Owner source has conflicting crosswalk target')
                row['mapping_status'] = 'merged-source-rows'
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


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
    alias_registry(rows, ledger)
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
    parser.add_argument("--crosswalk-dir", type=Path)
    args = parser.parse_args()
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    original = args.registry.read_text(encoding="utf-8")
    updates = [(args.output or args.registry, original, apply(original, ledger))]
    crosswalk_dir = args.crosswalk_dir
    if crosswalk_dir is None and args.registry == ROOT / "data/registry/programmes.csv" and args.output is None:
        crosswalk_dir = ROOT / "data/registry"
    if crosswalk_dir is not None and ledger.get("target_aliases"):
        for kind in ("programme_offerings", "programme_source_rows", "programme_interests"):
            file = crosswalk_dir / (kind + ".csv")
            original = file.read_text(encoding="utf-8")
            updates.append((file, original, alias_crosswalk(original, kind, ledger)))
    # Validate every prospective output before writing any generated file.
    for file, original, result in updates:
        if args.check and result != original:
            raise SystemExit("Registry differs from researched post-build overrides: " + file.name)
    if not args.check:
        for file, original, result in updates:
            file.write_text(result, encoding="utf-8")
    print("Registry post-build corrections and alias crosswalks are current")
