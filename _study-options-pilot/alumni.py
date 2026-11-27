"""Read the private workbook locally. Emit only distinct labels or verify the public selection."""
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path)
    parser.add_argument('--candidates', metavar='SLUG', help='Print distinct labels for local editorial review')
    args = parser.parse_args()
    options = json.loads((HERE / 'options.json').read_text())
    pools = candidates(args.workbook, options)
    if args.candidates:
        for group in pools[args.candidates]:
            for i, item in enumerate(sorted(group, key=lambda k: (-group[k], k))):
                print(i, ' — '.join(item) if isinstance(item, tuple) else item)
        return
    approved = json.loads((HERE / 'destinations.json').read_text())
    assert approved.keys() == pools.keys(), 'Curricula in destination selection differ'
    for slug, (degrees, employers) in pools.items():
        for selected, pool in [(list(map(tuple, approved[slug]['masters'])), degrees),
                               (approved[slug]['employers'], employers)]:
            assert len(selected) <= 20 and len(set(selected)) == len(selected), slug
            assert all(item in pool for item in selected), f'Unverified destination in {slug}'
    print(f'All selected labels verified for {len(options)} curricula.')


if __name__ == '__main__':
    main()
