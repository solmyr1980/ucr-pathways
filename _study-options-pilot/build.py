"""Build the static UCR interest-led pilot from its reviewed selections."""
from html import escape
import json
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'study-options-pilot'


def read(path):
    return json.loads(path.read_text())


def page(title, intro, body, detail=False):
    assets = '../../assets/' if detail else '../assets/'
    pilot = '../' if detail else './'
    back = '<a href="../">Study options</a>' if detail else ''
    script = '' if detail else '<script type="module" src="app.js"></script>'
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | University College Roosevelt</title>
<meta name="description" content="{escape(intro, quote=True)}">
<link rel="stylesheet" href="{assets}css/brand.css"><link rel="stylesheet" href="{pilot}style.css">
{script}
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="wrap mast"><a class="brand" href="https://ucr.nl/"><img src="{assets}brand/ucr-primary-plum.png" alt="University College Roosevelt"></a>
<nav aria-label="Main">{back}<a href="https://program.ucr.nl/">Programme builder</a></nav></div></header>
<main id="main">{body}</main>
</body></html>
'''


def link_card(option):
    return f'''<li data-option="{option['slug']}"><h3><a href="{option['slug']}/">{escape(option['title'])}</a></h3>
<p>{escape(option['summary'])}</p><p class="match" hidden></p></li>'''


def home(options):
    intro = 'Explore how your interests could fit together in a three-year Liberal Arts and Sciences degree at University College Roosevelt.'
    cards = '\n'.join(link_card(o) for o in sorted(options, key=lambda o: o['title']))
    body = f'''<section class="hero"><div class="wrap"><h1>What would you like to study?</h1>
<p class="lede">{intro}</p>
<form id="search" role="search" hidden><label for="interest">Search by interest</label>
<div class="searchbox"><input type="search" id="interest" name="q" placeholder="Try climate and economics" autocomplete="off" maxlength="250">
<button type="submit">Search</button></div></form></div></section>
<section class="wrap section" aria-labelledby="browse"><div class="results-head"><h2 id="browse">Browse study options</h2>
<button id="reset" type="button" hidden>Show all options</button></div>
<p id="status" role="status" aria-live="polite"></p>
<ul class="options" id="options">{cards}</ul></section>'''
    return page('Explore study options', intro, body)


def course_list(semester, descriptions):
    rows = []
    for course in semester['courses']:
        code = course['code']
        rows.append(f'''<li><details><summary>{escape(course['name'])}</summary>
<p class="code">{escape(code)} · {course['credits']:g} EC</p>
<p>{escape(descriptions[code])}</p></details></li>''')
    return '<ul class="courses">' + '\n'.join(rows) + '</ul>'


def curriculum(option, semesters, descriptions, selected):
    years = []
    for y in range(3):
        cols = []
        for j in range(2):
            s = semesters[2*y+j]
            assert s['label'] == f'Year {y+1} · Semester {j+1}', s['label']
            cols.append(f'<section><h4>Semester {j+1}</h4>{course_list(s, descriptions)}</section>')
        years.append(f'<section class="year"><h3>Year {y+1}</h3><div class="terms">{"".join(cols)}</div></section>')
    masters = ''.join(f'<li>{escape(name)} <span>— {escape(institution)}</span></li>' for name, institution in selected['masters'])
    employers = ''.join(f'<li>{escape(name)}</li>' for name in selected['employers'])
    groups = []
    if masters:
        groups.append(f'<section><h3>Master’s programmes</h3><ul class="destinations">{masters}</ul></section>')
    if employers:
        groups.append(f'<section><h3>Employers</h3><ul class="destinations">{employers}</ul></section>')
    alumni = ''
    if groups:
        alumni = f'''<section class="alumni" id="destinations"><div class="wrap section">
<h2>Where alumni went next</h2><p>Examples from UCR graduates who studied related subjects.</p>
<div class="destination-groups">{"".join(groups)}</div></div></section>'''
    alumni_link = '<a href="#destinations">Alumni destinations</a>' if alumni else ''
    term = semesters[0]['term']
    season = {'h1':'spring', 'h2':'autumn'}[term[4:]]
    start = f'{season} {int(term[:4])}'
    title, intro = option['title'], option['summary']
    body = f'''<section class="hero detail"><div class="wrap"><p class="eyebrow">Liberal Arts and Sciences</p>
<h1>{escape(title)}</h1><p class="lede">{escape(intro)}</p><nav class="jump" aria-label="On this page">
<a href="#curriculum">Six-semester plan</a>{alumni_link}</nav></div></section>
<section class="wrap section" id="curriculum"><h2>Your example curriculum</h2>
<p>24 courses · 180 EC · Starting in {start}</p>
{"".join(years)}</section>{alumni}
<div class="wrap footerlinks"><a href="../">Browse all study options</a><a href="https://program.ucr.nl/">Build your own programme</a></div>'''
    return page(title, intro, body, detail=True)


def build():
    options = read(HERE / 'options.json')
    aliases = read(HERE / 'aliases.json')
    selected = read(HERE / 'destinations.json')
    interests = {(r['programmeProviderId'], r['sourceInterestExcelRow']) for r in
                 read(ROOT / 'data/counselor/interests.json')['interests'] if r['targetMappingStatus'] == 'mapped'}
    descriptions = {k: v for f in (ROOT / 'pilot/shiny/data/courses').glob('???.json')
                    for k, v in read(f)['descriptions'].items()}
    index = {'topics': aliases, 'options': []}
    schedules = set()
    slugs = [o['slug'] for o in options]
    assert len(slugs) == len(set(slugs)) and set(slugs) == set(selected)
    approved_topics = {t for o in options for t in o['topics']}
    assert approved_topics == aliases.keys()
    OUT.mkdir(exist_ok=True)
    for o in options:
        slug, source = o['slug'], o['source']
        assert slug == quote(slug, safe='') and '/' not in slug and slug not in {'.', '..'}
        record = read(ROOT / f'data/counselor/comparisons/{source}.json')
        qc = read(ROOT / f'data/counselor/qc/full-restart-2026-10-27/{source}.json')
        assert record['origin'] == 'counselor' and qc['state'] == 'approved', source
        p = next(x for x in record['programmes'] if x['id'] == o['alternative'] and x['family'] == 'ucr')
        semesters = p['schedule']['semesters']
        courses = [c for s in semesters for c in s['courses']]
        codes = frozenset(c['code'] for c in courses)
        assert len(semesters) == 6 and all(len(s['courses']) == 4 for s in semesters)
        assert len(codes) == 24 and sum(c['credits'] for c in courses) == 180 and codes not in schedules
        schedules.add(codes)
        assessed = {x['sourceInterestExcelRow'] for x in record['academicRationale']['interestSelection']['assessedInterests']}
        for topic, evidence in o['topics'].items():
            assert evidence['courses'] and set(evidence['courses']) <= codes, (slug, topic)
            rows = evidence['interestRows']
            assert rows and all((source, row) in interests and row in assessed for row in rows), (slug, topic)
        dest = selected[slug]
        assert set(dest) == {'masters', 'employers'}
        for key, values in dest.items():
            assert len(values) <= 20
            assert all((isinstance(v, str) and v.strip()) if key == 'employers' else
                       (isinstance(v, list) and len(v) == 2 and all(isinstance(s, str) and s.strip() for s in v))
                       for v in values)
        folder = OUT / slug
        folder.mkdir(exist_ok=True)
        (folder / 'index.html').write_text(curriculum(o, semesters, descriptions, dest))
        index['options'].append({'slug':slug, 'topics':list(o['topics'])})
    (OUT / 'index.html').write_text(home(options))
    (OUT / 'index.json').write_text(json.dumps(index, separators=(',', ':'), ensure_ascii=False) + '\n')
    print(f'Built {len(options)} study options.')


if __name__ == '__main__':
    build()
