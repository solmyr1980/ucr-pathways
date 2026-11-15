#!/usr/bin/env python3
"""Read-only preservation proof for the authorized Stage 1 implementation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / 'docs/qc/evidence/qualified-comparison-stage1-2026-11-15/baseline.json'

def blob(path):
    b = path.read_bytes()
    return hashlib.sha1(f'blob {len(b)}\0'.encode() + b).hexdigest()

def main():
    baseline = json.loads(BASELINE.read_text())
    audit = json.loads((ROOT / 'data/counselor/qc/full-restart-2026-10-27.json').read_text())
    states = {c['id']: c['state'] for c in audit['cases']}
    directories = {'decision': 'decisions', 'canonical': 'comparisons', 'case': 'qc/full-restart-2026-10-27'}
    assert len(baseline['approved']) == 367
    assert len(baseline['otherDeferred']) == 61
    for group in ['approved', 'otherDeferred']:
        for case_id, hashes in baseline[group].items():
            assert states[case_id] == ('approved' if group == 'approved' else 'in-progress'), f'{case_id}: changed protected state'
            for kind, expected in hashes.items():
                path = ROOT / 'data/counselor' / directories[kind] / f'{case_id}.json'
                assert (blob(path) if path.exists() else None) == expected, f'Changed protected {kind}: {case_id}'
    for path, expected in baseline['protectedInputs'].items():
        assert blob(ROOT / path) == expected, f'Changed protected input: {path}'
    workers = hashlib.sha256(json.dumps(audit['workers'], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    assert workers == baseline['historicalWorkersSha256'], 'Exhausted worker history changed'
    assert audit['systemicPause'] is None
    print('Preserved byte-identically: 367 original approvals and 61 other deferrals (decision, canonical and case evidence); protected course/registry/student inputs and exhausted worker history unchanged.')

if __name__ == '__main__':
    main()
