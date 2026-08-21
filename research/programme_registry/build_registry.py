#!/usr/bin/env python3
"""Build the private UCR Pathways programme registry from DUO/RIO HO Opleidingsoverzicht.

The script keeps source-derived fields separate from Pathways-owned fields. It can
optionally reconcile against a previous registry, preserving every column whose
name starts with ``pathways_`` for programme keys that still exist.

No raw or processed programme data is intended to be committed to the public
repository. The GitHub workflow stores outputs only as a temporary Actions
artifact for transfer into private Project Sources.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

SOURCE_DATASET = "DUO/RIO HO Opleidingsoverzicht"
SOURCE_DATASET_URL = "https://onderwijsdata.duo.nl/datasets/ho_opleidingsoverzicht"
SOURCE_DOWNLOAD_URL = (
    "https://onderwijsdata.duo.nl/dataset/7c0686f4-b5c2-418e-8e44-7be0057d8084/"
    "resource/ffffa7ad-e6a2-4ba7-9fc2-a09df4128555/download/ho_opleidingsoverzicht.csv"
)
SOURCE_LICENSE = "CC BY 4.0"
REGISTRY_SCHEMA_VERSION = "1.0"

BASE_FIELDS = [
    "programme_key",
    "registry_schema_version",
    "institution_id",
    "institution_name",
    "recognised_programme_code",
    "programme_unit_codes",
    "programme_name",
    "international_name",
    "level",
    "degree",
    "study_load_ec",
    "modes",
    "languages",
    "locations",
    "websites",
    "source_types",
    "variant_names",
    "offering_codes",
    "offering_start_date",
    "offering_end_date",
    "is_bachelor",
    "is_wo",
    "is_hbo",
    "has_full_time",
    "has_part_time",
    "has_dual",
    "source_row_count",
    "source_dataset",
    "source_dataset_url",
    "source_license",
    "source_acquired_date",
    "pathways_interest_source",
    "pathways_comparator_candidate",
    "pathways_comparator_eligible",
    "pathways_disciplinary_class",
    "pathways_review_status",
    "pathways_interest_tags",
    "pathways_interest_notes",
    "pathways_interest_source_urls",
    "pathways_verified_comparator_record_id",
    "pathways_notes",
]

SOURCE_COMPARE_FIELDS = [
    f
    for f in BASE_FIELDS
    if not f.startswith("pathways_") and f not in {"source_acquired_date"}
]


def clean(value: str | None) -> str:
    return (value or "").strip()


def unique_join(values) -> str:
    return "; ".join(sorted({clean(v) for v in values if clean(v)}, key=str.casefold))


def bool_text(value: bool) -> str:
    return "TRUE" if value else "FALSE"


def parent_code(row: dict[str, str]) -> str:
    return (
        clean(row.get("VARIANT_VAN"))
        or clean(row.get("ERKENDEOPLEIDINGSCODE"))
        or clean(row.get("OPLEIDINGSEENHEIDCODE"))
    )


def choose_name(rows: list[dict[str, str]], field: str) -> str:
    parent_rows = [r for r in rows if clean(r.get("SOORT")).upper() == "OPLEIDING"]
    for pool in (parent_rows, rows):
        values = [clean(r.get(field)) for r in pool if clean(r.get(field))]
        if values:
            counts: dict[str, int] = defaultdict(int)
            for value in values:
                counts[value] += 1
            return sorted(counts, key=lambda x: (-counts[x], x.casefold()))[0]
    return ""


def min_date(values) -> str:
    vals = sorted({clean(v)[:10] for v in values if clean(v)})
    return vals[0] if vals else ""


def max_open_date(values) -> str:
    raw = [clean(v) for v in values]
    if not raw or any(v == "" for v in raw):
        return ""
    vals = sorted({v[:10] for v in raw})
    return vals[-1] if vals else ""


def make_record(rows: list[dict[str, str]], acquired_date: str) -> dict[str, str]:
    first = rows[0]
    institution_id = clean(first.get("ONDERWIJSAANBIEDERID"))
    recognised = parent_code(first)
    level_values = [clean(r.get("NIVEAU")) for r in rows]
    degree_values = [clean(r.get("GRAAD")) for r in rows]
    study_load_values = [clean(r.get("STUDIELAST")) for r in rows]
    levels = unique_join(level_values)
    degrees = unique_join(degree_values)
    study_load = unique_join(study_load_values)

    upper_levels = {v.upper() for v in level_values if v}
    upper_degrees = {v.upper() for v in degree_values if v}
    bachelor = "BACHELOR" in upper_degrees or any(v.endswith("-BA") for v in upper_levels)
    wo = any(v.startswith("WO") for v in upper_levels)
    hbo = any(v.startswith("HBO") for v in upper_levels)

    modes = [clean(r.get("VORM")).upper() for r in rows]
    full_time = "VOLTIJD" in modes
    part_time = "DEELTIJD" in modes
    dual = "DUAAL" in modes

    source_types = [clean(r.get("SOORT")) for r in rows]
    variant_names = [
        clean(r.get("NAAM_LANG"))
        for r in rows
        if clean(r.get("SOORT")).upper() == "VARIANT"
    ]

    candidate = bachelor and wo

    return {
        "programme_key": f"{institution_id}::{recognised}",
        "registry_schema_version": REGISTRY_SCHEMA_VERSION,
        "institution_id": institution_id,
        "institution_name": choose_name(rows, "ONDERWIJSAANBIEDER_NAAM"),
        "recognised_programme_code": recognised,
        "programme_unit_codes": unique_join(r.get("OPLEIDINGSEENHEIDCODE") for r in rows),
        "programme_name": choose_name(rows, "NAAM_LANG"),
        "international_name": choose_name(rows, "INTERNATIONALE_NAAM"),
        "level": levels,
        "degree": degrees,
        "study_load_ec": study_load,
        "modes": unique_join(r.get("VORM") for r in rows),
        "languages": unique_join(r.get("VOERTAAL") for r in rows),
        "locations": unique_join(r.get("ONDERWIJSLOCATIEPLAATS") for r in rows),
        "websites": unique_join(r.get("WEBSITE") for r in rows),
        "source_types": unique_join(source_types),
        "variant_names": unique_join(variant_names),
        "offering_codes": unique_join(r.get("AANGEBODEN_OPLEIDINGCODE") for r in rows),
        "offering_start_date": min_date(r.get("AANGEBODEN_OPLEIDING_BEGINDATUM") for r in rows),
        "offering_end_date": max_open_date(r.get("AANGEBODEN_OPLEIDING_EINDDATUM") for r in rows),
        "is_bachelor": bool_text(bachelor),
        "is_wo": bool_text(wo),
        "is_hbo": bool_text(hbo),
        "has_full_time": bool_text(full_time),
        "has_part_time": bool_text(part_time),
        "has_dual": bool_text(dual),
        "source_row_count": str(len(rows)),
        "source_dataset": SOURCE_DATASET,
        "source_dataset_url": SOURCE_DATASET_URL,
        "source_license": SOURCE_LICENSE,
        "source_acquired_date": acquired_date,
        "pathways_interest_source": bool_text(candidate),
        "pathways_comparator_candidate": bool_text(candidate),
        "pathways_comparator_eligible": "",
        "pathways_disciplinary_class": "",
        "pathways_review_status": "unreviewed" if candidate else "out_of_scope_default",
        "pathways_interest_tags": "",
        "pathways_interest_notes": "",
        "pathways_interest_source_urls": "",
        "pathways_verified_comparator_record_id": "",
        "pathways_notes": "",
    }


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise SystemExit(f"No header found in {path}")
        rows = [dict(row) for row in reader]
        return list(reader.fieldnames), rows


def read_previous(path: Path | None) -> tuple[list[str], dict[str, dict[str, str]]]:
    if not path:
        return [], {}
    fields, rows = read_csv(path)
    by_key = {clean(r.get("programme_key")): r for r in rows if clean(r.get("programme_key"))}
    return fields, by_key


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--changes", required=True, type=Path)
    parser.add_argument("--previous-registry", type=Path)
    parser.add_argument("--acquired-date", default=date.today().isoformat())
    args = parser.parse_args()

    raw_fields, raw_rows = read_csv(args.input)
    required = {
        "ONDERWIJSAANBIEDERID",
        "ONDERWIJSAANBIEDER_NAAM",
        "SOORT",
        "OPLEIDINGSEENHEIDCODE",
        "ERKENDEOPLEIDINGSCODE",
        "VARIANT_VAN",
        "NAAM_LANG",
        "INTERNATIONALE_NAAM",
        "NIVEAU",
        "GRAAD",
        "STUDIELAST",
        "VORM",
        "VOERTAAL",
        "WEBSITE",
        "AANGEBODEN_OPLEIDINGCODE",
        "ONDERWIJSLOCATIEPLAATS",
    }
    missing = sorted(required - set(raw_fields))
    if missing:
        raise SystemExit("Missing expected DUO fields: " + ", ".join(missing))

    # The raw source includes recognition-only rows without a provider. The programme
    # registry represents programmes actually attached to a provider, while the raw
    # file remains the lossless source for everything else.
    offered_rows = [r for r in raw_rows if clean(r.get("ONDERWIJSAANBIEDERID"))]
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in offered_rows:
        institution_id = clean(row.get("ONDERWIJSAANBIEDERID"))
        code = parent_code(row)
        if not code:
            continue
        groups[(institution_id, code)].append(row)

    records = [make_record(rows, args.acquired_date) for _, rows in sorted(groups.items())]

    previous_fields, previous = read_previous(args.previous_registry)
    preserved_custom_fields = [
        field
        for field in previous_fields
        if field.startswith("pathways_") and field not in BASE_FIELDS
    ]
    output_fields = BASE_FIELDS + preserved_custom_fields

    for record in records:
        old = previous.get(record["programme_key"])
        if old:
            for field in [f for f in previous_fields if f.startswith("pathways_")]:
                if field in old:
                    record[field] = clean(old.get(field))

    current_by_key = {r["programme_key"]: r for r in records}
    changes: list[dict[str, str]] = []
    if previous:
        all_keys = sorted(set(previous) | set(current_by_key))
        for key in all_keys:
            old = previous.get(key)
            new = current_by_key.get(key)
            if old is None:
                changes.append({"programme_key": key, "change_type": "new", "changed_source_fields": ""})
            elif new is None:
                changes.append({"programme_key": key, "change_type": "removed", "changed_source_fields": ""})
            else:
                changed = [f for f in SOURCE_COMPARE_FIELDS if clean(old.get(f)) != clean(new.get(f))]
                if changed:
                    changes.append(
                        {
                            "programme_key": key,
                            "change_type": "changed",
                            "changed_source_fields": "; ".join(changed),
                        }
                    )

    write_csv(args.output, output_fields, records)
    write_csv(args.changes, ["programme_key", "change_type", "changed_source_fields"], changes)

    counts = {
        "raw_rows": len(raw_rows),
        "provider_attached_source_rows": len(offered_rows),
        "registry_programmes": len(records),
        "wo_bachelor_programmes": sum(
            r["is_wo"] == "TRUE" and r["is_bachelor"] == "TRUE" for r in records
        ),
        "hbo_bachelor_programmes": sum(
            r["is_hbo"] == "TRUE" and r["is_bachelor"] == "TRUE" for r in records
        ),
        "default_interest_source_programmes": sum(r["pathways_interest_source"] == "TRUE" for r in records),
        "default_comparator_candidates": sum(r["pathways_comparator_candidate"] == "TRUE" for r in records),
        "changes_against_previous": len(changes),
    }
    manifest = {
        "source": {
            "dataset": SOURCE_DATASET,
            "dataset_url": SOURCE_DATASET_URL,
            "download_url": SOURCE_DOWNLOAD_URL,
            "license": SOURCE_LICENSE,
            "acquired_date": args.acquired_date,
            "sha256": sha256(args.input),
        },
        "registry": {
            "schema_version": REGISTRY_SCHEMA_VERSION,
            "row_unit": "programme x education provider; modes, languages, locations and offering variants aggregated",
            "programme_key": "ONDERWIJSAANBIEDERID::(VARIANT_VAN or ERKENDEOPLEIDINGSCODE or OPLEIDINGSEENHEIDCODE)",
            "counts": counts,
            "pathways_fields_preserved_from_previous_registry": True,
        },
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
