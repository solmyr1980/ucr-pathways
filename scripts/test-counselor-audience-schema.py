#!/usr/bin/env python3
"""Validate the new audience JSON Schema independently of manual JS checks."""
import copy
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

root = Path(__file__).resolve().parents[1]
schemas = [json.loads(p.read_text()) for p in (root / 'data/schema').glob('*.json')]
registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
validators = {s['$id'].rsplit('/', 1)[-1]: Draft202012Validator(s, registry=registry) for s in schemas}
for validator in validators.values():
    validator.check_schema(validator.schema)
for filename in ['counselor-comparison.schema.json', 'counselor-exception.schema.json']:
    assert validators[filename].schema['properties']['audience']['$ref'] == './counselor-audience.schema.json'
v = validators['counselor-audience.schema.json']
valid = [
    {'schemaVersion': '1.0'},
    {'schemaVersion': '1.0', 'curriculum': {'status': 'partial', 'componentIds': ['a'], 'limitation': 'A required component is unidentified.'}},
    {'schemaVersion': '1.0', 'curriculum': {'status': 'unresolved', 'componentIds': [], 'limitation': 'Requirements remain unresolved.'}},
    {'schemaVersion': '1.0', 'conceptProgrammeIds': ['ucr-1']}
]
invalid = [
    {'schemaVersion': '1.0', 'internalFallback': True},
    {'schemaVersion': '1.0', 'curriculum': {'status': 'partial', 'componentIds': []}},
    {'schemaVersion': '1.0', 'curriculum': {'status': 'unresolved', 'componentIds': ['a'], 'limitation': 'Unresolved'}},
    {'schemaVersion': '1.0', 'curriculum': {'status': 'complete', 'componentIds': [], 'yearLabel': 'API year 2261'}},
    {'schemaVersion': '1.0', 'cellNotes': [{'programmeId': 'ucr-1', 'text': 'Missing stable reference'}]}
]
for item in valid:
    v.validate(item)
for item in invalid:
    assert list(v.iter_errors(item)), item
# Check that audience data is accepted/rejected through both canonical schemas.
for case_id, schema_name in [('cp-000019', 'counselor-comparison.schema.json'), ('cp-000277', 'counselor-exception.schema.json')]:
    record = json.loads((root / f'data/counselor/comparisons/{case_id}.json').read_text())
    # The control detects existing unrelated schema failures separately.
    baseline = {(tuple(e.path), e.message) for e in validators[schema_name].iter_errors(record)}
    record['audience'] = copy.deepcopy(valid[0])
    assert {(tuple(e.path), e.message) for e in validators[schema_name].iter_errors(record)} == baseline
    record['audience'] = copy.deepcopy(invalid[0])
    assert any(list(e.path) == ['audience'] for e in validators[schema_name].iter_errors(record))
print('Audience JSON Schema, canonical references and positive/negative fixtures pass.')
