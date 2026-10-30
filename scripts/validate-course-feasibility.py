#!/usr/bin/env python3
"""Check explicit canonical schedules against the course reference; never select courses.

Pass canonical JSON paths (including private student records), or use
--compare-workbook OLD.xlsx for a read-only change/impact report.
"""
import argparse
import json
import re
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
TERM = re.compile(r'^\d{4}h[12]$')
CODE = re.compile(r'^[A-Z]{3,}[0-9]{3}$')


def load_courses(path):
    sheet = openpyxl.load_workbook(path, data_only=True).active
    values = list(sheet.values)
    headers = list(values[0])
    required = {'osiris', 'name', 'preq1'}
    if not required <= set(headers) or len(headers) != len(set(headers)):
        raise ValueError('Missing or duplicate course-reference headers')
    courses = {}
    for row in values[1:]:
        if not any(v is not None for v in row):
            continue
        item = dict(zip(headers, row))
        code = item['osiris']
        if not isinstance(code, str) or not CODE.fullmatch(code) or code in courses:
            raise ValueError(f'Invalid/duplicate course code: {code}')
        courses[code] = item
    return courses, {h for h in headers if isinstance(h, str) and TERM.fullmatch(h)}


def check_record(record, courses, terms):
    errors = []
    programmes = [p for p in record.get('programmes', []) if p.get('family') == 'ucr']
    if record.get('recordStatus') == 'exception':
        return ['Exception contains a UCR programme'] if programmes else []
    if not programmes:
        return ['No explicit UCR programme to check']
    for programme in programmes:
        label = programme.get('id', '?')
        semesters = programme.get('schedule', {}).get('semesters', [])
        if len(semesters) != 6:
            errors.append(f'{label}: expected six semesters')
        assigned = [s.get('term') for s in semesters]
        if any(t not in terms for t in assigned):
            errors.append(f'{label}: planning horizon missing terms {sorted({str(t) for t in assigned if t not in terms})}')
        if any(not isinstance(t, str) or not TERM.fullmatch(t) for t in assigned):
            errors.append(f'{label}: invalid term code')
        elif assigned != sorted(set(assigned)) or any(
                int(b[:4]) * 2 + int(b[-1]) != int(a[:4]) * 2 + int(a[-1]) + 1
                for a, b in zip(assigned, assigned[1:])):
            errors.append(f'{label}: semesters must be consecutive and chronological')
        completed, seen = set(), set()
        total, advanced, ppd = 0, 0, []
        for index, semester in enumerate(semesters):
            items = semester.get('courses', [])
            term = semester.get('term')
            if len(items) != 4:
                errors.append(f'{label}/{term}: expected four courses')
            current = set()
            for course in items:
                code = course.get('code')
                if code in seen:
                    errors.append(f'{label}: duplicate course {code}')
                seen.add(code)
                current.add(code)
                credit = course.get('credits')
                if isinstance(credit, bool) or not isinstance(credit, (int, float)) or credit != 7.5:
                    errors.append(f'{label}/{code}: expected 7.5 EC')
                else:
                    total += credit
                if code == 'ACCPPDE101':
                    ppd.append(index)
                if isinstance(code, str) and CODE.fullmatch(code) and int(code[-3]) >= 3:
                    advanced += 1
                source = courses.get(code)
                if source is None:
                    errors.append(f'{label}: course absent from active reference: {code}')
                    continue
                if term in terms and source.get(term) != 'X':
                    errors.append(f'{label}/{term}: {code} not planned')
                prerequisite = source.get('preq1')
                if prerequisite == 'NONE':
                    pass
                elif not isinstance(prerequisite, str) or not CODE.fullmatch(prerequisite):
                    errors.append(f'{label}/{code}: unsupported or missing prerequisite expression {prerequisite!r}')
                elif prerequisite not in completed:
                    errors.append(f'{label}/{code}: prerequisite {prerequisite} must be completed earlier')
            completed.update(current)
        if len(seen) != 24 or total != 180:
            errors.append(f'{label}: expected 24 unique courses / 180 EC')
        if advanced < 6:
            errors.append(f'{label}: fewer than six 300-level courses')
        if len(ppd) != 1 or ppd[0] > 1:
            errors.append(f'{label}: PPD must occur exactly once in Year 1')
    return errors


def compare_courses(before, after, records):
    changes = {}
    for code in sorted(before.keys() | after.keys()):
        old, new = before.get(code, {}), after.get(code, {})
        fields = sorted(k for k in old.keys() | new.keys() if old.get(k) != new.get(k))
        if fields:
            changes[code] = {'fields': fields, 'added': code not in before, 'removed': code not in after}
    affected = {}
    for path in records:
        record = json.loads(path.read_text())
        used = {c['code'] for p in record.get('programmes', []) if p.get('family') == 'ucr'
                for s in p.get('schedule', {}).get('semesters', []) for c in s.get('courses', [])}
        codes = sorted(used & changes.keys())
        if codes:
            affected[record['id']] = codes
    content = {'description2', 'profile', 'discipline', 'topics', 'methods'}
    broader = [c for c, d in changes.items() if d['added'] or content.intersection(d['fields'])]
    return {'courses': changes, 'recordsUsingChangedCourses': affected,
            'coursesForTargetedSubjectAreaReassessment': broader,
            'note': 'Changes identify review scope, not automatic invalidity. New or changed content may affect unused courses and prior no-match cases. No academic approval is inferred.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('records', nargs='*', type=Path)
    parser.add_argument('--workbook', type=Path, default=ROOT / 'data/reference/ucr_courses_enriched.xlsx')
    parser.add_argument('--compare-workbook', type=Path)
    args = parser.parse_args()
    courses, terms = load_courses(args.workbook)
    if args.compare_workbook:
        before, _ = load_courses(args.compare_workbook)
        paths = args.records or sorted((ROOT / 'data/counselor/comparisons').glob('cp-*.json'))
        print(json.dumps(compare_courses(before, courses, paths), ensure_ascii=False, indent=2))
        return
    if not args.records:
        parser.error('Supply canonical JSON paths; existing unreviewed corpus is not implicitly revalidated')
    failures = []
    for path in args.records:
        errors = check_record(json.loads(path.read_text()), courses, terms)
        failures.extend(f'{path.name}: {e}' for e in errors)
    if failures:
        parser.exit(1, '\n'.join(failures) + '\n')
    print(f'{len(args.records)} canonical records pass course-reference feasibility checks. Academic relevance is not assessed.')


if __name__ == '__main__':
    main()
