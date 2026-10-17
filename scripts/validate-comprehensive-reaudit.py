#!/usr/bin/env python3
"""Read-only consistency checks for the comprehensive re-audit register (stdlib only).

This checks bookkeeping and approval evidence structure, not academic truth or
reviewer independence. Run from the repository root, or pass --root for fixtures.
"""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re

REGISTER = 'data/counselor/qc/comprehensive-reaudit.json'
CASE_DIR = 'data/counselor/qc/comprehensive-reaudit'
STATES = ['not-started', 'in-progress', 'reviewed-with-blockers', 'approved']
OUTCOMES = ['retain', 'correct', 'reconstruct', 'blocked']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def validate(root):
    root = root.resolve()

    def reference(ref):
        require(isinstance(ref, str) and ref, 'Empty evidence reference')
        if ref.startswith(('https://', 'http://')):
            return
        name, _, fragment = ref.partition('#')
        target = (root / name).resolve()
        require(target.is_relative_to(root) and target.is_file(), f'Missing/unsafe reference: {ref}')
        if fragment.startswith('/'):
            value = read_json(target)
            for token in fragment[1:].split('/'):
                token = token.replace('~1', '/').replace('~0', '~')
                value = value[int(token)] if isinstance(value, list) else value[token]

    def evidence_refs(refs):
        require(isinstance(refs, list) and refs, 'Verification needs evidenceRefs')
        for ref in refs:
            reference(ref)

    d = read_json(root / REGISTER)
    require(d['schemaVersion'] == '2.0', 'Unsupported register version')
    require(d['caseLifecycleVocabulary'] == STATES, 'Unexpected lifecycle vocabulary')
    require(d['stageOutcomeVocabulary'] == OUTCOMES, 'Unexpected stage vocabulary')
    for key in ['protocol', 'preparationReport']:
        reference(d[key])
    baseline = d['baselineCaseOrder']
    require(len(baseline) == len(set(baseline)) == d['baselineCounts']['inScope'], 'Baseline count/ID mismatch')
    require(all(re.fullmatch(r'cp-\d{6}', x) for x in baseline), 'Invalid baseline ID')
    with (root / 'data/registry/programmes.csv').open(encoding='utf-8-sig', newline='') as f:
        registry = list(csv.DictReader(f))
    scoped = [r for r in registry if r['production_eligible'] == 'true'
              and r['production_order'].strip() and r['programme_type'] == 'standard']
    scope = {r['counselor_programme_id'] for r in scoped}
    # Scope changes must be explicit; never replace the baseline denominator.
    added = {x['id'] for x in d['scopeChanges'] if x['change'] == 'added'}
    withdrawn = {x['id'] for x in d['scopeChanges'] if x['change'] == 'withdrawn'}
    for change in d['scopeChanges']:
        require(change['change'] in ['added', 'withdrawn', 'changed'] and change.get('reason'), 'Invalid scope change')
    require(added == scope - set(baseline) and withdrawn == set(baseline) - scope, 'Undocumented registry scope change')
    if not d['scopeChanges']:
        require(baseline == [r['counselor_programme_id'] for r in sorted(scoped, key=lambda r: int(r['production_order']))], 'Baseline order differs from registry')
    records = {}
    for file in (root / 'data/counselor/comparisons').glob('cp-*.json'):
        record = read_json(file)
        require(record['id'] == file.stem == record['programmeProvider']['counselorProgrammeId'], f'Canonical identity mismatch: {file}')
        records[file.stem] = record
    require(set(records) == scope, 'Active canonical records and registry scope differ')
    ids = [c['id'] for c in d['cases']]
    require(len(ids) == len(set(ids)) and set(ids) <= (set(baseline) | added), 'Duplicate/out-of-scope case entry')
    issues = {s['id']: s for s in d['sharedIssues']}
    require(len(issues) == len(d['sharedIssues']), 'Duplicate shared issue')
    for issue in issues.values():
        require(set(issue['affectedStages']) <= set(range(1, 7)), f"{issue['id']}: invalid shared dependency")
        if issue['status'] == 'verified':
            require(issue['implementationCommits'], f"{issue['id']}: verified issue lacks implementation")
            evidence_refs(issue.get('verificationEvidenceRefs'))
    for dependency in d.get('releaseDependencies', []):
        issue_id = dependency['sharedIssueId']
        require(issue_id in issues and dependency['requiredDisposition'], 'Invalid release dependency')
        issue = issues[issue_id]
        require(issue.get('blocksFinalPublication') is True, f'{issue_id}: release blocker flag missing')
        reference(issue['evidenceRef'])
        evidence = read_json(root / issue['evidenceRef'])
        require(issue['affectedRecordCount'] == evidence['affectedRecordCount'], f'{issue_id}: discrepancy count differs')
        require(all((root / 'data/counselor/comparisons' / name).is_file() for name in evidence['affectedRecords']), f'{issue_id}: discrepancy record missing')
    pilot = [x for pair in d['pilotPairs'] for x in pair]
    require(all(len(pair) == 2 for pair in d['pilotPairs']) and len(pilot) == len(set(pilot)) == 6, 'Pilot must retain three distinct pairs')
    require(set(pilot) <= set(ids), 'Missing pilot metadata')
    with (root / 'data/registry/programme_interests.csv').open(encoding='utf-8-sig', newline='') as f:
        interests = list(csv.DictReader(f))
    detail_paths = set()
    states = dict.fromkeys(baseline, 'not-started')
    for entry in d['cases']:
        case_id = entry['id']
        require(entry['state'] in STATES, f'{case_id}: invalid state')
        if case_id in states:
            states[case_id] = entry['state']
        require(set(entry['sharedIssueIds']) <= set(issues), f'{case_id}: unknown shared issue')
        if entry['state'] == 'not-started':
            require(not entry.get('stages') and not entry.get('stageOutcomes') and not entry.get('finalReview'), f'{case_id}: unstarted case has findings')
            require(not entry.get('evidenceFile'), f'{case_id}: unstarted evidence file')
            continue
        file = entry['evidenceFile']
        require(file == f'{CASE_DIR}/{case_id}.json', f'{case_id}: unstable evidence path')
        reference(file)
        detail_paths.add(file)
        case = read_json(root / file)
        require(case['id'] == case_id and case['auditId'] == d['auditId'] and case['schemaVersion'] == '2.0', f'{case_id}: detail identity/version mismatch')
        for key in ['state', 'sharedIssueIds', 'unresolved', 'downstreamReassessments', 'implementationCommits', 'presentationApproval']:
            require(entry[key] == case[key], f'{case_id}: central/detail {key} mismatch')
        require(entry['stageOutcomes'] == {n: s['outcome'] for n, s in case['stages'].items()}, f'{case_id}: stage outcomes differ')
        require(set(case['stages']) <= set('123456'), f'{case_id}: invalid stage')
        for n, stage in case['stages'].items():
            require(stage['outcome'] in OUTCOMES and stage['finding'] and stage['evidence'], f'{case_id}/{n}: incomplete finding')
            require(set(stage['reassessStages']) <= set(range(1, 7)), f'{case_id}/{n}: invalid dependency stage')
            for action in stage['actions']:
                require(action['state'] in ['proposed', 'implemented', 'verified'] and action['scope'], f'{case_id}/{n}: invalid action')
                if action['state'] in ['implemented', 'verified']:
                    require(action.get('implementationCommit') in case['implementationCommits'], f'{case_id}/{n}: action missing implementation commit')
                if action['state'] == 'verified':
                    evidence_refs(action.get('verificationEvidenceRefs'))
            if 'interestRows' in stage:
                rows = [r['row'] for r in stage['interestRows']]
                target = [int(r['source_interest_excel_row']) for r in interests if r['counselor_programme_id'] == case_id]
                require(len(rows) == len(set(rows)) and set(rows) == set(target), f'{case_id}: incomplete/duplicate interest review')
                require(dict(Counter(r['outcome'] for r in stage['interestRows'])) == stage['rowOutcomeCounts'], f'{case_id}: interest counts differ')
        for history in case.get('reviewHistory', []):
            snapshot = history['snapshot']
            raw = (json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n').encode()
            require(snapshot['id'] == case_id and hashlib.sha256(raw).hexdigest() == history['originalFileSha256'], f'{case_id}: preserved original review snapshot changed')
        for dependency in case['downstreamReassessments']:
            require(dependency['trigger'] and dependency['scope'] and set(dependency['stages']) <= set(range(1, 7)), f'{case_id}: invalid reassessment')
        for source in case['evidenceSources']:
            urls = source.get('urls', [source.get('url')])
            require(urls and all(isinstance(u, str) and u.startswith('https://') for u in urls), f'{case_id}: invalid source reference')
        for image in case['renderedEvidence']:
            reference(image['path'])
            require(image['recordId'] == case_id and hashlib.sha256((root / image['path']).read_bytes()).hexdigest() == image['sha256'], f'{case_id}: screenshot identity/hash mismatch')
            require(image['viewport']['width'] > 0 and image['viewport']['height'] > 0 and image['inputCommit'] and image['presentationMode'], f'{case_id}: incomplete screenshot metadata')
        if entry['state'] == 'reviewed-with-blockers':
            require(set(case['stages']) == set('123456'), f'{case_id}: review did not reach all six stages')
            require(case['unresolved'] or any(s['blockedBy'] for s in case['stages'].values()), f'{case_id}: blocker missing')
            require(case['presentationApproval'] is False, f'{case_id}: blocked case has presentation approval')
        if entry['state'] == 'approved' or case['presentationApproval']:
            require(entry['state'] == 'approved' and case['presentationApproval'] is True, f'{case_id}: inconsistent approval')
            require(set(case['stages']) == set('123456') and not case['unresolved'] and not case['downstreamReassessments'], f'{case_id}: approval has unfinished review/dependencies')
            require(all(s['outcome'] != 'blocked' and not s['blockedBy'] and not s['reassessStages'] and all(a['state'] == 'verified' for a in s['actions']) for s in case['stages'].values()), f'{case_id}: approval has blocked stage/unverified correction')
            require(all(issues[x]['status'] == 'verified' for x in case['sharedIssueIds']), f'{case_id}: approval depends on unresolved shared issue')
            academic_record = records[case_id]
            audience = academic_record.get('audience', {})
            require(audience.get('schemaVersion') == '1.0' and audience.get('programmeDescription') and audience.get('comparisonExplanation'), f'{case_id}: final audience explanations missing')
            curriculum = audience.get('curriculum', {})
            components = academic_record['comparator']['components']
            require(curriculum.get('status') == 'complete' and set(curriculum.get('componentIds', [])) == {c['id'] for c in components} and abs(sum(c['credits'] for c in components) - 180) < .001 and academic_record.get('exception', {}).get('type') != 'external-programme-unresolved', f'{case_id}: approved curriculum must be complete and verified')
            programme_ids = {p['id'] for p in academic_record['programmes'] if p.get('family') == 'ucr'}
            require(set(audience.get('conceptProgrammeIds', [])) == programme_ids, f'{case_id}: final canonical concepts not selected for display')
            final = case['finalReview']
            require(final and all(final.get(k) for k in ['reviewerOrPass', 'independenceMethod', 'reviewedOn', 'reviewedCommit']), f'{case_id}: independent final review missing')
            evidence_refs(final.get('sourceEvidenceRefs'))
            for area in ['academic', 'mechanical', 'rendered']:
                check = final['checks'][area]
                require(check['status'] == 'passed', f'{case_id}: {area} final check failed')
                evidence_refs(check.get('evidenceRefs'))
            for kind, name in [('canonical', 'comparisons'), ('decision', 'decisions')]:
                current = root / f'data/counselor/{name}/{case_id}.json'
                require(final['inputBlobs'][kind] == (git_blob(current) if current.exists() else None), f'{case_id}: final approval refers to stale {kind}')
    actual_details = {str(p.relative_to(root)) for p in (root / CASE_DIR).glob('cp-*.json')}
    require(detail_paths == actual_details, 'Orphaned or missing case evidence file')
    counts = Counter(states.values())
    expected = {'approved': counts['approved'], 'inProgress': counts['in-progress'], 'reviewedWithBlockers': counts['reviewed-with-blockers'], 'notStarted': counts['not-started'], 'pilotStarted': sum(states[x] != 'not-started' for x in pilot)}
    require(d['progress'] == expected, f'Progress differs: expected {expected}')
    for batch in d['batches']:
        require(len(batch['caseIds']) == len(set(batch['caseIds'])) == 2 and set(batch['caseIds']) <= set(ids), 'Invalid batch references')
        reference(batch['reportSection'])
    sequence = d['executionSequence']
    require(sequence['batchSize'] == 2 and sequence['writerPolicy'], 'Batch/writer policy missing')
    require([s['step'] for s in sequence['steps']] == [1, 2, 3, 4, 5], 'Execution sequence incomplete')
    require(sequence['steps'][1]['caseIds'] == d['pilotPairs'][0] and sequence['steps'][2]['caseIds'] == pilot[2:], 'Execution sequence and pilot pairs differ')
    print(f'Re-audit register consistent: {len(baseline)} baseline targets; {expected}; {len(detail_paths)} case evidence files. No academic approval inferred.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate(args.root)
    except (ValueError, KeyError, TypeError, OSError, IndexError) as error:
        parser.exit(1, f'Re-audit consistency failure: {error}\n')
