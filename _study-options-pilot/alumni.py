"""Check the pilot’s public destination labels against the private reviewed shortlists."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
MASTER_TYPES = {"master", "research master", "llm", "msc", "ma", "mba", "mphil"}


def label(value):
    value = re.sub(r'\s+', ' ', value.strip())
    return re.sub(r'\bUni\b\.?', 'University', value)


def candidates(workbook, options):
    pools = {o["slug"]: (Counter(), Counter()) for o in options}
    sheet = load_workbook(workbook, read_only=True, data_only=True).active
    rows = iter(sheet.values)
    assert list(next(rows)) == [*(f'track{i}' for i in range(1, 7)),
                               *(f'deg{i}' for i in range(1, 4)), *(f'job{i}' for i in range(1, 6))]
    for row in rows:
        tracks = {x.split(';', 1)[0].strip() for x in row[:6] if x}
        matches = [pools[o['slug']] for o in options if len(tracks.intersection(o['tracks'])) >= 2]
        if not matches:
            continue
        degrees, employers = set(), set()
        for entry in filter(None, row[6:9]):
            fields = [x.strip() for x in entry.split(';')]
            if len(fields) >= 4 and fields[2].lower() in MASTER_TYPES and fields[1] and fields[3]:
                degrees.add((label(fields[3]), label(fields[1])))
        for entry in filter(None, row[9:]):
            fields = entry.split(';')
            if len(fields) >= 3 and fields[1].strip():
                employers.add(label(fields[1]))
        for degree_counts, employer_counts in matches:
            degree_counts.update(degrees)
            employer_counts.update(employers)
    return pools


def reviewed_selection(workbook, options):
    slugs = {(o['source'], o['alternative']): o['slug'] for o in options}
    if len(slugs) != len(options):
        raise ValueError('Pilot alternatives must have distinct source IDs')
    selection = {slug: {'masters': [], 'employers': []} for slug in slugs.values()}
    mixed = set()
    counts = {}
    book = load_workbook(workbook, read_only=True, data_only=True)
    try:
        rows = iter(book['Shortlist coverage'].values)
        header = next(rows)
        employer_count = header.index('Employers selected')
        degree_count = header.index('Programmes selected')
        for row in rows:
            slug = slugs.get(row[:2])
            if slug:
                if slug in counts:
                    raise ValueError(f'Duplicate coverage record for {slug}')
                counts[slug] = (row[degree_count], row[employer_count])

        rows = iter(book['Shortlists'].values)
        if tuple(next(rows)) != ('Comparison ID', 'Alternative ID', 'UCR curriculum', 'Destination type',
                                 'Employer or postgraduate programme', 'Institution', 'Qualification'):
            raise ValueError('Unexpected Shortlists columns')
        for comparison, alternative, _, kind, name, institution, award in rows:
            slug = slugs.get((comparison, alternative))
            if not slug:
                continue
            if not isinstance(name, str) or not name.strip():
                raise ValueError(f'Missing destination name for {slug}')
            if kind == 'Employer' and institution is None and award is None:
                selection[slug]['employers'].append(name)
            elif kind == 'Postgraduate' and isinstance(institution, str) and institution.strip():
                if not isinstance(award, str) or award.lower() not in MASTER_TYPES | {'professional doctorate', 'phd'}:
                    raise ValueError(f'Unrecognised postgraduate award for {slug}')
                if award.lower() not in MASTER_TYPES:
                    mixed.add(slug)
                selection[slug]['masters'].append([name, institution])
            else:
                raise ValueError(f'Unexpected destination record for {slug}')
    finally:
        book.close()

    for slug, group in selection.items():
        degrees, employers = group['masters'], group['employers']
        if counts.get(slug) != (len(degrees), len(employers)):
            raise ValueError(f'Shortlist coverage differs for {slug}')
        if (max(len(degrees), len(employers)) > 20 or len(set(employers)) != len(employers)
                or len(set(map(tuple, degrees))) != len(degrees)):
            raise ValueError(f'Duplicate or oversized shortlist for {slug}')
        if slug in mixed:
            selection[slug] = {'postgraduate': degrees, 'employers': employers}
    return selection


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path)
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--write', action='store_true', help='Write the approved pilot labels from the reviewed workbook')
    action.add_argument('--candidates', metavar='SLUG', help='Inspect distinct labels in the historical source export')
    args = parser.parse_args()
    options = json.loads((HERE / 'options.json').read_text())
    if args.candidates:
        for group in candidates(args.workbook, options)[args.candidates]:
            for i, item in enumerate(sorted(group, key=lambda k: (-group[k], k))):
                print(i, ' — '.join(item) if isinstance(item, tuple) else item)
        return
    selection = reviewed_selection(args.workbook, options)
    public_file = HERE / 'destinations.json'
    if args.write:
        public_file.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if json.loads(public_file.read_text()) != selection:
        raise ValueError('Public destination labels differ from the reviewed pilot shortlists')
    print(f'All selected labels verified for {len(options)} curricula.')


if __name__ == '__main__':
    main()
