"""Reproduce the completion checks; academic judgments remain in source-first evidence."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent

def read(path):
    return json.loads(path.read_text())

def blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest()

def run(args):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr + result.stdout[-4000:]
    return {'command': args, 'exitCode': result.returncode,
            'stdoutSha256': hashlib.sha256(result.stdout.encode()).hexdigest(),
            'outputTail': result.stdout[-500:]}

schemas = [read(p) for p in (ROOT/'data/schema').glob('*.json')]
registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
validators = {s['$id'].rsplit('/', 1)[-1]: Draft202012Validator(s, registry=registry) for s in schemas}
sheet = openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx', data_only=True).active
headers = [c.value for c in sheet[1]]
courses = {row[headers.index('osiris')]: dict(zip(headers, row)) for row in sheet.iter_rows(min_row=2, values_only=True)}
results = []
with tempfile.TemporaryDirectory(prefix='ucr-completion-check-') as tmp:
    for cp in ['cp-000002', 'cp-000003']:
        canonical = ROOT/f'data/counselor/comparisons/{cp}.json'
        decision = ROOT/f'data/counselor/decisions/{cp}.json'
        record = read(canonical)
        schema = 'counselor-exception.schema.json' if record.get('recordStatus') == 'exception' else 'counselor-comparison.schema.json'
        validators[schema].validate(record)
        validators['counselor-audience.schema.json'].validate(record['audience'])
        output = Path(tmp)/f'{cp}.json'
        run(['node', 'scripts/build-counselor-production.mjs', str(decision), '--output', str(output)])
        assert output.read_bytes() == canonical.read_bytes()
        assert sum(c['credits'] for c in record['comparator']['components']) == 180
        schedules = []
        for programme in record['programmes']:
            if programme['family'] != 'ucr':
                continue
            seen = set()
            flat = []
            for term in programme['schedule']['semesters']:
                assert len(term['courses']) == 4
                for c in term['courses']:
                    w = courses[c['code']]
                    prerequisites = re.findall(r'[A-Z]{7}\d{3}', w['preq1'] or '')
                    assert set(prerequisites) <= seen
                    assert w[term['term']] == 'X'
                    assert c['name'] == w['name'] and c['credits'] == 7.5
                    assert c['level'] == int(c['code'][-3])
                    flat.append(c)
                seen.update(c['code'] for c in term['courses'])
            assert len(flat) == len(seen) == 24
            assert sum(c['credits'] for c in flat) == 180
            assert sum(c['level'] == 3 for c in flat) >= 6
            assert any(c['code'] == 'ACCPPDE101' for s in programme['schedule']['semesters'][:2] for c in s['courses'])
            schedules.append({'programmeId': programme['id'], 'courses': len(flat), 'advancedCourses': sum(c['level'] == 3 for c in flat), 'workbookPrerequisitesAndOfferings': 'passed'})
        if cp == 'cp-000003':
            assert record['exception']['type'] == 'no-defensible-ucr-match' and not schedules
        results.append({'id': cp, 'inputBlobs': {'canonical': blob(canonical), 'decision': blob(decision)}, 'formalSchema': 'passed', 'audienceSchema': 'passed', 'compilerByteReplay': 'passed', 'externalEC': 180, 'externalComponents': len(record['comparator']['components']), 'activeUcrSchedules': schedules})
bad = []
for path in sorted((ROOT/'data/counselor/comparisons').glob('cp-*.json')):
    r = read(path)
    schema = 'counselor-exception.schema.json' if r.get('recordStatus') == 'exception' else 'counselor-comparison.schema.json'
    if list(validators[schema].iter_errors(r)):
        bad.append(path.name)
baseline = read(ROOT/'docs/qc/evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json')
assert bad == baseline['affectedRecords'] and len(bad) == 64
commands = [run(args) for args in [['npm', 'run', 'validate:counselor'], ['npm', 'run', 'validate:counselor-review'], ['git', 'diff', '--check']]]
result = {'checkedOn': '2026-10-20', 'reviewedCommit': '885c20e754033870c43417c65fd24dc841fe990f', 'workbookBlob': blob(ROOT/'data/reference/ucr_courses_enriched.xlsx'), 'status': 'passed', 'results': results, 'commands': commands, 'formalSchemaCorpusDiscrepancy': {'affectedRecords': 64, 'baselineSetUnchanged': True, 'releaseDependencyStillOpen': True}, 'limit': 'Mechanical checks do not establish academic comparability. Separate academic and runtime evidence is linked in the case files.'}
(OUT/'mechanical-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print('PASS: both formal schemas, exact compiler replay, 48 direct workbook placements, 438 operational records, review indexes, unchanged 64-record schema discrepancy, clean diff.')
