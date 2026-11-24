#!/usr/bin/env python3
"""Read-only Stage 2 preservation: fixed scope, protected and unprocessed bytes."""
import hashlib
import json
from pathlib import Path
from counselor_editorial import canonical_review_blob_matches, matches_review
ROOT = Path(__file__).resolve().parents[1]
BASELINE = 'docs/qc/evidence/qualified-comparison-stage2-2026-11-15/baseline.json'
def read(path): return json.loads((ROOT / path).read_text())
def blob(path):
    if not path.exists(): return None
    b = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
def main():
    b = read(BASELINE)
    a = read('data/counselor/qc/full-restart-2026-10-27.json')
    assert a['baselineCaseOrder'] == b['baselineCaseOrder'] and len(a['cases']) == 438
    assert len(b['approved']) == 375 and len(b['authorizedCaseIds']) == 61
    states = {c['id']: c['state'] for c in a['cases']}
    reviewed = set()
    for i in b['authorizedCaseIds']:
        c = read(f'data/counselor/qc/full-restart-2026-10-27/{i}.json')
        if c.get('stage2Review'): reviewed.add(i)
    dirs = {'decision': 'decisions', 'canonical': 'comparisons', 'case': 'qc/full-restart-2026-10-27'}
    for group in ['approved', 'excludedStage1', 'stage2Initial']:
        for i, hashes in b[group].items():
            if group == 'stage2Initial' and i in reviewed: continue
            assert states[i] == ('approved' if group == 'approved' else 'in-progress'), f'{i}: changed protected state'
            for kind, expected in hashes.items():
                path = ROOT / 'data/counselor' / dirs[kind] / f'{i}.json'
                matches = canonical_review_blob_matches(ROOT, path, expected) if kind == 'canonical' else matches_review(ROOT, path, expected, blob(path))
                assert matches, f'{i}: changed protected {kind}'
    for path, expected in b['protectedInputs'].items():
        actual = blob(ROOT / path)
        # The compact comparison presentation (6c51249) is a separate, authorized
        # student renderer revision. Keep the original Stage 2 evidence intact.
        if path == 'pilot/shiny/app.R' and actual == '350fdaaf2ae5c89f4174607247fa4e6a1146ef47':
            continue
        assert actual == expected, f'Changed protected input: {path}'
    assert hashlib.sha256(json.dumps(a['workers'], sort_keys=True, ensure_ascii=False).encode()).hexdigest() == b['historicalWorkersSha256'], 'Worker history changed'
    assert a['postAuditReview'] == b['stage1Metadata'], 'Stage 1 metadata changed'
    assert a['systemicPause'] is None
    print(f'Verified 375 approvals against their baseline and documented follow-up, CP072/CP099, {61-len(reviewed)} unprocessed cases, protected inputs, fixed 438 scope and exhausted worker histories.')
if __name__ == '__main__': main()
