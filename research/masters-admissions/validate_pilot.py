"""Validate the pilot datasets and reuse the shared UCR schedule check."""
import csv
import runpy
from collections import Counter, defaultdict
from pathlib import Path

PILOT = Path(__file__).resolve().parent
ROOT = PILOT.parents[1]


def read_csv(name):
    with (PILOT / name).open(encoding='utf-8', newline='') as source:
        return list(csv.DictReader(source))


def index(rows, key):
    result = {row[key]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f'Duplicate {key}')
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    programmes = index(read_csv('programmes.csv'), 'programme_id')
    feasibility = index(read_csv('feasibility.csv'), 'programme_id')
    sources = index(read_csv('sources.csv'), 'source_id')
    requirements = index(read_csv('admission_requirements.csv'), 'requirement_id')
    fields = Counter(row['field'] for row in programmes.values())
    require(len(fields) == 6 and set(fields.values()) == {4}, 'Expected four programmes per field')
    require(set(programmes) == set(feasibility), 'Programme and feasibility IDs differ')
    require({row['programme_id'] for row in requirements.values()} == set(programmes),
            'Every programme needs admission requirements')
    require({row['source_id'] for row in requirements.values()} == set(sources),
            'Missing or unused admission evidence')
    for row in requirements.values():
        source = sources[row['source_id']]
        require(row['programme_id'] == source['programme_id'] and bool(row['source_location'])
                and source['url'].startswith('https://') and bool(source['verified_on']),
                f"Incomplete evidence for {row['requirement_id']}")

    validator = runpy.run_path(str(ROOT / 'scripts/validate-course-feasibility.py'))
    courses, terms = validator['load_courses'](ROOT / 'data/reference/ucr_courses_enriched.xlsx')
    for key, row in feasibility.items():
        require(row['outcome'] in {'A', 'B', 'C'}, f'{key}: unknown outcome')
        require(set(row['ucr_candidate_courses'].split()) <= courses.keys(), f'{key}: unknown UCR course')
        if row['outcome'] == 'B':
            require(bool(row['identified_academic_gaps']), f'{key}: missing identified gap')
        if row['outcome'] == 'C':
            require(bool(row['unresolved_academic_requirements']), f'{key}: missing unresolved requirement')

    schedules = defaultdict(lambda: defaultdict(list))
    for row in read_csv('curriculum_schedules.csv'):
        key, code, term = row['programme_id'], row['course_code'], row['term']
        require(key in programmes and code in courses, f'{key}/{code}: unknown identifier')
        require(row['course_title'] == courses[code]['name'], f'{code}: title differs from workbook')
        schedules[key][(int(row['semester']), term)].append(dict(code=code, credits=float(row['ec'])))
    require(Counter(programmes[key]['field'] for key in schedules) == dict.fromkeys(fields, 1),
            'Expected one example per field')
    records = []
    for key, schedule in schedules.items():
        keys = sorted(schedule)
        require([number for number, _ in keys] == list(range(1, 7)), f'{key}: invalid semester numbers')
        records.append(dict(id=key, family='ucr', schedule=dict(semesters=[
            dict(term=term, courses=schedule[number, term]) for number, term in keys
        ])))
    failures = validator['check_record']({'programmes': records}, courses, terms)
    require(not failures, '\n'.join(failures))
    print(f'{len(programmes)} programmes, {len(requirements)} requirements, '
          f'{len(sources)} sources and {len(records)} curricula pass pilot validation.')


if __name__ == '__main__':
    main()
