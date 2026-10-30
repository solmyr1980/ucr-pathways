#!/usr/bin/env python3
"""Strict full JSON Schema validation; --report-only inventories legacy defects without approval."""
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]


def validators(root=ROOT):
    schemas = [json.loads(p.read_text()) for p in (root / 'data/schema').glob('*.json')]
    registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
    result = {}
    for schema in schemas:
        Draft202012Validator.check_schema(schema)
        result[schema['$id'].rsplit('/', 1)[-1]] = Draft202012Validator(schema, registry=registry)
    return result


def record_errors(record, checks):
    name = 'counselor-exception.schema.json' if record.get('recordStatus') == 'exception' else 'counselor-comparison.schema.json'
    # allOf can report the same inherited failure twice; do not inflate the inventory.
    return sorted({('/' + '/'.join(map(str, e.path)), e.message) for e in checks[name].iter_errors(record)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('records', nargs='*', type=Path)
    parser.add_argument('--report-only', action='store_true', help='Read-only legacy inventory; never a release or changed-record gate')
    args = parser.parse_args()
    checks = validators()
    paths = args.records or sorted((ROOT / 'data/counselor/comparisons').glob('cp-*.json'))
    failures = {}
    for path in paths:
        errors = record_errors(json.loads(path.read_text()), checks)
        if errors:
            failures[path.name] = [{'path': p, 'message': m} for p, m in errors]
    if failures:
        print(json.dumps({'checked': len(paths), 'failed': len(failures), 'failures': failures,
                          'mode': 'inventory-only; not approval' if args.report_only else 'strict'}, indent=2))
        if not args.report_only:
            parser.exit(1, 'Full JSON Schema validation failed. Repair the affected evidence/contract; no approval is inferred.\n')
    else:
        print(f'{len(paths)} canonical records pass full JSON Schema validation.')


if __name__ == '__main__':
    main()
