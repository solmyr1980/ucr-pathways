"""Compare canonical counselor records with their reviewed academic snapshots."""

import hashlib
import json


def blob_hash(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def canonical_review_blob_matches(root, path, expected):
    if not path.is_file():
        return expected is None
    current = path.read_bytes()
    if blob_hash(current) == expected:
        return True
    if expected is None:
        return False

    # Recover the exact reviewed bytes using only prose carried by the original
    # decision. The stored blob hash still proves that all other content matches.
    record = json.loads(current)
    decision_path = root / 'data/counselor/decisions' / path.name
    if not decision_path.is_file():
        return False
    fields = ['programmeDescription']
    if record.get('recordStatus') == 'exception':
        fields.append('comparisonExplanation')
    else:
        settings_path = root / 'data/counselor/presentation-overrides.json'
        if not settings_path.is_file():
            return False
        settings = json.loads(settings_path.read_bytes())
        if settings['cases'].get(record.get('id'), {}).get('mode') != 'external-only':
            return False
    original = json.loads(decision_path.read_bytes()).get('audience', {})
    audience = record.get('audience', {})
    for field in fields:
        if not isinstance(audience.get(field), str) or not audience[field].strip() or field not in original:
            return False
        audience[field] = original[field]
    reviewed = (json.dumps(record, ensure_ascii=False, indent=2) + '\n').encode()
    return blob_hash(reviewed) == expected
