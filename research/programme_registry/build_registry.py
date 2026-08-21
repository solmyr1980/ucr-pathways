#!/usr/bin/env python3
"""Build the private UCR Pathways working programme registry from DUO/RIO.

The raw DUO/RIO file remains the source of truth. The derived registry contains
only selected and aggregated DUO fields: it keeps the original DUO columns and
adds no Pathways-owned enrichment or placeholder fields.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

REFERENCE_DATE = "2026-09-01"
BREDA_UAS_BOARD_ID = "107B542"
NON_BACHELOR_NAME = re.compile(
    r"(pre[- ]?master|premaster|schakel(?:opleiding|programma)|doorstroomminor|"
    r"bijvakstudent|educatieve\s+(?:minor|module)|\bminor\b)",
    re.IGNORECASE,
)


def clean(value: str | None) -> str:
    return (value or "").strip()


def student_facing_name(row: dict[str, str]) -> str:
    return clean(row.get("EIGENNAAM")) or clean(row.get("NAAM_LANG"))


def parent_code(row: dict[str, str]) -> str:
    return (
        clean(row.get("VARIANT_VAN"))
        or clean(row.get("ERKENDEOPLEIDINGSCODE"))
        or clean(row.get("OPLEIDINGSEENHEIDCODE"))
    )


def active_on_reference_date(row: dict[str, str]) -> bool:
    start = clean(row.get("AANGEBODEN_OPLEIDING_BEGINDATUM")) or clean(row.get("BEGINDATUM"))
    end = clean(row.get("AANGEBODEN_OPLEIDING_EINDDATUM")) or clean(row.get("EINDDATUM"))
    first = clean(row.get("EERSTE_INSTROOMDATUM"))
    last = clean(row.get("LAATSTE_INSTROOMDATUM"))
    return not (
        (start and start > REFERENCE_DATE)
        or (end and end < REFERENCE_DATE)
        or (first and first > REFERENCE_DATE)
        or (last and last < REFERENCE_DATE)
    )


def relevant_row(row: dict[str, str]) -> bool:
    return (
        clean(row.get("NIVEAU")).upper() == "WO-BA"
        and bool(clean(row.get("ONDERWIJSAANBIEDERID")))
        and clean(row.get("ONDERWIJSBESTUURID")) != BREDA_UAS_BOARD_ID
        and active_on_reference_date(row)
        and not NON_BACHELOR_NAME.search(student_facing_name(row))
    )


def unique_join(values) -> str:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        value = clean(value)
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return " | ".join(result)


def programme_groups(rows: list[dict[str, str]]) -> list[list[dict[str, str]]]:
    """Group source rows into distinct current student-facing bachelor choices.

    Rows in the same institution + recognised programme family are merged when
    they share either the same student-facing name or the same offered-programme
    code. Differently named student-facing variants therefore remain separate.
    """

    families: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        families[(clean(row.get("ONDERWIJSBESTUURID")), parent_code(row))].append(row)

    result: list[list[dict[str, str]]] = []
    for family_rows in families.values():
        parent = list(range(len(family_rows)))

        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_b] = root_a

        by_name: dict[str, list[int]] = defaultdict(list)
        by_offering: dict[str, list[int]] = defaultdict(list)
        for i, row in enumerate(family_rows):
            by_name[student_facing_name(row).casefold()].append(i)
            offering = clean(row.get("AANGEBODEN_OPLEIDINGCODE"))
            if offering:
                by_offering[offering].append(i)

        for indices in list(by_name.values()) + list(by_offering.values()):
            for i in indices[1:]:
                union(indices[0], i)

        buckets: dict[int, list[dict[str, str]]] = defaultdict(list)
        for i, row in enumerate(family_rows):
            buckets[find(i)].append(row)
        result.extend(buckets.values())

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise SystemExit(f"No header found in {args.input}")
        fields = list(reader.fieldnames)
        raw_rows = [dict(row) for row in reader]

    selected = [row for row in raw_rows if relevant_row(row)]
    records = [
        {field: unique_join(row.get(field) for row in group) for field in fields}
        for group in programme_groups(selected)
    ]
    records.sort(
        key=lambda row: (
            clean(row.get("ONDERWIJSBESTUUR_NAAM")).casefold(),
            (clean(row.get("EIGENNAAM")) or clean(row.get("NAAM_LANG"))).casefold(),
        )
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    print(f"{len(records)} programme records written with {len(fields)} original DUO columns")


if __name__ == "__main__":
    main()
