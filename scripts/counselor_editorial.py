"""Compare canonical counselor records with their reviewed academic snapshots."""

import hashlib
import json
from functools import lru_cache


def blob_hash(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


@lru_cache(maxsize=4)
def consistency_review(root):
    evidence = root / 'docs/qc/evidence/counselor-consistency-2026-11-24.json'
    return json.loads(evidence.read_bytes())['artifacts'] if evidence.is_file() else {}


@lru_cache(maxsize=4)
def peer_reviews(root):
    path = root / 'docs/qc/evidence/counselor-peer-review-2026-11-25.json'
    return json.loads(path.read_bytes())['changes'] if path.is_file() else {}


def matches_review(root, path, expected, actual):
    if actual == expected:
        return True
    # A dated follow-up supersedes exactly one version of a named artifact.
    relative = path.relative_to(root).as_posix()
    peer = peer_reviews(root).get(path.stem, {}).get('artifacts', {}).get(relative)
    if peer and actual == peer['after']:
        # The earlier editorial pass could change only the reviewed audience prose.
        if expected in {peer['before'], peer.get('reviewedBefore', peer['before'])}:
            return True
        actual = peer['before']
    amendment = consistency_review(root).get(relative)
    return amendment is not None and amendment == {'before': expected, 'after': actual}


def canonical_review_blob_matches(root, path, expected):
    if not path.is_file():
        return expected is None
    current = path.read_bytes()
    if matches_review(root, path, expected, blob_hash(current)):
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
    return matches_review(root, path, expected, blob_hash(reviewed))
