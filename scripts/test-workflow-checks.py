#!/usr/bin/env python3
"""Focused regression checks for feasibility, provenance, schema and derived review state."""
import copy
import fnmatch
import hashlib
import importlib.util
import json
from pathlib import Path
import os
import re
import subprocess
import tempfile
import textwrap
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), ROOT / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


feasibility = module('validate-course-feasibility')
descriptions = module('validate-course-descriptions')
schema = module('validate-counselor-schema')
reviews = module('validate-comprehensive-reaudit')


def fixture():
    terms = ['2026h2', '2027h1', '2027h2', '2028h1', '2028h2', '2029h1']
    codes = ['ACCPPDE101'] + [f'TSTTEST{100 + i:03}' for i in range(1, 16)] + [f'TSTTEST{300 + i:03}' for i in range(8)]
    courses = {c: {'name': c, 'preq1': 'NONE', **dict.fromkeys(terms, 'X')} for c in codes}
    semesters = [{'term': t, 'courses': [{'code': c, 'credits': 7.5} for c in codes[i * 4:i * 4 + 4]]} for i, t in enumerate(terms)]
    return {'programmes': [{'id': 'ucr-1', 'family': 'ucr', 'schedule': {'semesters': semesters}}]}, courses, set(terms)


class WorkflowChecks(unittest.TestCase):
    def test_feasible_and_hard_failures(self):
        record, courses, terms = fixture()
        self.assertEqual(feasibility.check_record(record, courses, terms), [])
        courses['TSTTEST101']['preq1'] = 'ACCPPDE101'
        self.assertTrue(any('must be completed earlier' in e for e in feasibility.check_record(record, courses, terms)))
        courses['TSTTEST101']['preq1'] = 'NONE'
        courses['TSTTEST104']['preq1'] = 'ACCPPDE101'
        self.assertEqual(feasibility.check_record(record, courses, terms), [])
        courses['TSTTEST104']['2027h1'] = None
        self.assertTrue(any('not planned' in e for e in feasibility.check_record(record, courses, terms)))
        self.assertTrue(any('horizon' in e for e in feasibility.check_record(record, courses, terms - {'2029h1'})))
        courses['TSTTEST104']['preq1'] = 'ACCPPDE101 OR TSTTEST101'
        self.assertTrue(any('unsupported' in e for e in feasibility.check_record(record, courses, terms)))

    def test_exception_does_not_invent_schedule(self):
        self.assertEqual(feasibility.check_record({'recordStatus': 'exception', 'programmes': []}, {}, set()), [])

    def test_supported_role_only_records_are_checked(self):
        for role in ['ucr-alternative', 'ucr-depth', 'ucr-balanced', 'ucr-thematic']:
            with self.subTest(role=role):
                record, courses, terms = fixture()
                programme = record['programmes'][0]
                programme.pop('family')
                programme['role'] = role
                self.assertEqual(feasibility.check_record(record, courses, terms), [])
                courses['TSTTEST104']['2027h1'] = None
                self.assertTrue(any('not planned' in e for e in feasibility.check_record(record, courses, terms)))
                record['recordStatus'] = 'exception'
                self.assertTrue(feasibility.check_record(record, courses, terms))

    def test_duplicate_missing_course_and_credit_failures(self):
        record, courses, terms = fixture()
        items = record['programmes'][0]['schedule']['semesters'][0]['courses']
        items[1]['code'] = items[0]['code']
        self.assertTrue(any('duplicate course' in e for e in feasibility.check_record(record, courses, terms)))
        items[1]['code'] = 'UNKNOWN301'
        items[1]['credits'] = 15
        errors = feasibility.check_record(record, courses, terms)
        self.assertTrue(any('absent from active reference' in e for e in errors))
        self.assertTrue(any('7.5 EC' in e for e in errors))

    def test_change_report_preserves_unused_capability_warning(self):
        record, before, _ = fixture()
        record['id'] = 'cp-000001'
        record['programmes'][0].pop('family')
        record['programmes'][0]['role'] = 'ucr-depth'
        after = copy.deepcopy(before)
        after['TSTTEST104']['2027h1'] = None
        after['TSTNEW301'] = {'name': 'New content', 'profile': 'New content'}
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'record.json'
            path.write_text(json.dumps(record))
            result = feasibility.compare_courses(before, after, [path])
        self.assertEqual(result['recordsUsingChangedCourses'], {'cp-000001': ['TSTTEST104']})
        self.assertIn('TSTNEW301', result['coursesForTargetedSubjectAreaReassessment'])

    def test_provenance_uses_field_and_name_not_whole_workbook(self):
        sha = lambda text: hashlib.sha256(text.encode()).hexdigest()
        row = {'name': 'Course', 'profile': 'Evidence', 'description2': 'Official'}
        source = {'workbook': 'data/reference/ucr_courses_enriched.xlsx', 'workbookBlob': 'a' * 40,
                  'courseName': 'Course', 'sourceField': 'profile', 'sourceSha256': sha('Evidence'),
                  'descriptionSha256': sha('Evidence'), 'reviewNote': 'Reviewed', 'reviewedOn': '2026-10-30', 'mode': 'verbatim'}
        descriptions.check_description('TEST', source, row, 'Evidence')
        source['workbookBlob'] = 'b' * 40
        row['description2'] = 'Unrelated source-field edit'
        descriptions.check_description('TEST', source, row, 'Evidence')
        for changed in [{'name': 'Renamed'}, {'profile': 'Changed evidence'}]:
            with self.assertRaises(AssertionError):
                descriptions.check_description('TEST', source, {**row, **changed}, 'Evidence')
        with self.assertRaises(AssertionError):
            descriptions.check_description('TEST', source, row, 'Unreviewed prose')

    def test_schema_keeps_missing_evidence_a_failure(self):
        checks = schema.validators()
        record = json.loads((ROOT / 'data/counselor/decisions/_regression/expected/cp-000004.json').read_text())
        self.assertEqual(schema.record_errors(record, checks), [])
        component = checks['example.schema.json'].schema['$defs']['comparatorComponent']
        from jsonschema import Draft202012Validator
        v = Draft202012Validator(component)
        v.validate({'id': 'y1-U10108-B-3', 'name': 'Component', 'credits': 5})
        self.assertTrue(list(v.iter_errors({'id': 'bad id', 'name': 'Component', 'credits': 5})))
        candidate = {'label': 'Candidate', 'basisType': 'programme-interest-cluster',
                     'generatingInterestRows': [2], 'supportingInterestRows': [], 'disposition': 'rejected', 'rejectionReason': 'not-feasible'}
        record['academicRationale']['interestSelection']['candidateDirections'].append(candidate)
        self.assertTrue(any('evidence' in m for _, m in schema.record_errors(record, checks)))
        candidate['evidence'] = []
        self.assertTrue(any(p.endswith('/evidence') for p, _ in schema.record_errors(record, checks)))

    def test_sync_is_idempotent_and_preserves_pause_and_claims(self):
        # Exercise the derivation with synthetic files only. CI separately runs
        # the complete read-only validator against the accepted register/evidence.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pointer = root / reviews.REGISTER
            pointer.parent.mkdir(parents=True)
            register_path = pointer.parent / 'current.json'
            case_path = pointer.parent / 'case.json'
            pointer.write_text(json.dumps({'activeAudit': {'register': str(register_path.relative_to(root))}}))
            ids = [f'cp-{n:06}' for n in range(1, 7)]
            case = {'id': ids[0], 'auditId': 'fixture', 'state': 'in-progress', 'sharedIssueIds': [],
                    'unresolved': [], 'downstreamReassessments': [], 'implementationCommits': [],
                    'presentationApproval': False, 'stages': {'1': {'outcome': 'retain'}}}
            case_path.write_text(json.dumps(case))
            pause = {'type': 'user-requested-hold'}
            claim = {'caseId': ids[0], 'token': 'preserve'}
            register = {'auditId': 'fixture', 'baselineCaseOrder': ids,
                        'pilotPairs': [ids[:2], ids[2:4], ids[4:]],
                        'cases': [{'id': ids[0], 'evidenceFile': str(case_path.relative_to(root)), 'state': 'not-started'}],
                        'progress': {'approved': 999}, 'status': 'paused-by-user', 'systemicPause': pause,
                        'workers': {'A': {'assignedCases': ids[:3], 'activeClaim': claim},
                                    'B': {'assignedCases': ids[3:], 'activeClaim': None}}}
            register_path.write_text(json.dumps(register))
            with mock.patch.object(reviews, 'validate') as validate:
                self.assertTrue(reviews.sync_summaries(root))
                actual = json.loads(register_path.read_text())
                self.assertEqual(actual['progress'], {'approved': 0, 'inProgress': 1,
                                 'reviewedWithBlockers': 0, 'notStarted': 5, 'pilotStarted': 1})
                self.assertEqual(actual['systemicPause'], pause)
                self.assertEqual(actual['workers']['A']['activeClaim'], claim)
                self.assertEqual(actual['workers']['A']['completedCases'], [])
                self.assertFalse(actual['cases'][0]['presentationApproval'])
                self.assertFalse(reviews.sync_summaries(root))
                self.assertEqual(validate.call_count, 2)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pointer = root / reviews.REGISTER
            pointer.parent.mkdir(parents=True)
            bad = {'baselineCaseOrder': [], 'cases': [], 'pilotPairs': [], 'workers': {}, 'status': 'paused-by-user'}
            pointer.write_text(json.dumps(bad))
            original = pointer.read_bytes()
            with self.assertRaises((KeyError, ValueError)):
                reviews.sync_summaries(root)
            self.assertEqual(pointer.read_bytes(), original)

    def test_ci_scope_keeps_case_checks_and_skips_unrelated_private_checks(self):
        workflow = (ROOT / '.github/workflows/validate-shiny.yml').read_text()
        section = workflow.split('- name: Identify changed inputs', 1)[1]
        code = textwrap.dedent(re.search(r"python - <<'PY'\n(.*?)\n          PY", section, re.S).group(1))
        with tempfile.TemporaryDirectory() as d:
            cwd = Path(d)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-q')
            git('config', 'user.email', 'fixture@example.test')
            git('config', 'user.name', 'Fixture')
            (cwd / 'README.md').write_text('Fixture')
            git('add', '.')
            git('commit', '-qm', 'Baseline')
            scenarios = [(['data/counselor/qc/state.json'], False, False),
                         (['data/counselor/comparisons/cp-000001.json', 'docs/qc/report.md',
                           'docs/qc/evidence/desktop.png'], False, True),
                         (['docs/qc/follow-up.md', 'docs/qc/evidence/mobile.png'], False, False),
                         (['pilot/shared.R'], True, True)]
            for paths, shared, runtime in scenarios:
                before = git('rev-parse', 'HEAD')
                for path in paths:
                    target = cwd / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('{}')
                git('add', *paths)
                git('commit', '-qm', 'Change')
                output = cwd / 'outputs.txt'
                output.write_text('')
                subprocess.run(['python', '-c', code], cwd=cwd, check=True,
                               env={**os.environ, 'EVENT_NAME': 'push', 'BEFORE': before, 'GITHUB_OUTPUT': str(output)})
                values = dict(line.split('=', 1) for line in output.read_text().splitlines())
                self.assertEqual(values['shared'], str(shared).lower())
                self.assertEqual(values['runtime'], str(runtime).lower())
                self.assertEqual(json.loads(values['records']), [p for p in paths if '/comparisons/' in p])

    def test_pdf_build_tracks_its_inputs_not_review_helpers(self):
        workflow = (ROOT / '.github/workflows/build-linkedin-pdf.yml').read_text()
        section = workflow.split('  push:\n', 1)[1].split('\npermissions:', 1)[0]
        paths = re.findall(r"^\s+- '([^']+)'$", section, re.M)
        triggered = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in paths)
        for path in ['data/examples/p-001.json', 'assets/js/comparison.js',
                     'scripts/build-linkedin-html.mjs', 'scripts/build-open-day-html.mjs',
                     'scripts/render-linkedin-pdf.mjs', 'scripts/render-open-day-pdf.mjs',
                     'scripts/validate-example.mjs', 'scripts/example-utils.mjs',
                     'scripts/quality.test.mjs', 'data/schema/example.schema.json']:
            self.assertTrue(triggered(path), path)
        for path in ['scripts/validate-course-feasibility.py', 'scripts/test-workflow-checks.py',
                     'scripts/validate-comprehensive-reaudit.py', 'docs/qc/report.md',
                     'data/counselor/comparisons/cp-000001.json',
                     'data/schema/counselor-comparison.schema.json']:
            self.assertFalse(triggered(path), path)


if __name__ == '__main__':
    unittest.main()
