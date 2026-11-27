"""Verify local or deployed HTML, the public index and navigation against the selected sources."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen
from lxml import html

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PUBLIC = ROOT / 'study-options-pilot'
LIVE = 'https://solmyr1980.github.io/ucr-pathways/study-options-pilot/'

QUERIES = [
    ('film', 'film-literature', True),
    ('government and law', 'politics-law', True),
    ('business and data', 'economics-business-data', True),
    ('AI and neuroscience', 'ai-language-brain', True),
    ('genetics and pharmacology', 'biomedical-science', True),
    ('climate and economics', 'earth-climate-economics', True),
    ('climate and machine learning', 'environment-data', True),
    ('film and aerospace engineering', 'film-literature', False),
    ('veterinary dentistry', None, False),
]


def fetch(url):
    req = Request(url, headers={'Cache-Control':'no-cache', 'User-Agent':'UCR-study-options-verification'})
    with urlopen(req, timeout=35) as response:
        assert response.status == 200, url
        return response.read()


def check_html(live):
    options = json.loads((HERE / 'options.json').read_text())
    destinations = json.loads((HERE / 'destinations.json').read_text())
    descriptions = {k:v for p in (ROOT / 'pilot/shiny/data/courses').glob('???.json')
                    for k,v in json.loads(p.read_text())['descriptions'].items()}
    files = {p.relative_to(PUBLIC).as_posix() for p in PUBLIC.rglob('*') if p.is_file()}
    expected = {'index.html','index.json','app.js','style.css','search.js'} | {o['slug']+'/index.html' for o in options}
    assert files == expected, files ^ expected

    def get(name):
        local = (PUBLIC / name).read_bytes()
        if live:
            url = LIVE + (name.removesuffix('index.html') if name.endswith('index.html') else name)
            downloaded = fetch(url)
            assert sha256(downloaded).digest() == sha256(local).digest(), url
            return downloaded
        return local

    pages = {name:get(name) for name in sorted(expected)}
    index = json.loads(pages['index.json'])
    assert set(index) == {'topics','options'}
    assert index['topics'] == json.loads((HERE / 'aliases.json').read_text())
    assert index['options'] == [{'slug':o['slug'], 'topics':list(o['topics'])} for o in options]
    home = html.fromstring(pages['index.html'].decode())
    assert set(home.xpath('//li/h3/a/@href')) == {o['slug']+'/' for o in options}
    for o in options:
        slug = o['slug']
        page = html.fromstring(pages[slug+'/index.html'].decode())
        assert page.xpath('string(//h1)') == o['title']
        source = json.loads((ROOT / ('data/counselor/comparisons/'+o['source']+'.json')).read_text())
        programme = next(p for p in source['programmes'] if p['id'] == o['alternative'])
        terms = page.xpath('//section[@class="year"]/div/section')
        assert len(terms) == 6
        for term, sem in zip(terms, programme['schedule']['semesters']):
            items = term.xpath('.//details')
            assert len(items) == 4
            for item, c in zip(items, sem['courses']):
                assert item.xpath('string(summary)') == c['name']
                assert item.xpath('string(p[1])') == f"{c['code']} · {c['credits']:g} EC"
                assert item.xpath('string(p[2])') == descriptions[c['code']]
        for heading, items in [('Master’s programmes', [' — '.join(pair) for pair in destinations[slug]['masters']]),
                               ('Employers', destinations[slug]['employers'])]:
            actual = page.xpath('//section[h3=$heading]/ul/li',heading=heading)
            assert [li.text_content() for li in actual] == items
            assert bool(page.xpath('//h3[text()=$heading]',heading=heading)) == bool(items)
        assert 'cp-000' not in page.text_content().lower()
        assert not page.xpath('//script')
    if live:
        assert fetch(urljoin(LIVE,'../')) == (ROOT/'index.html').read_bytes()
    print(f'{"Live" if live else "Local"}: all {len(expected)} public files checked; seven complete 24-course schedules and selected destinations verified from static HTML.')


def check_browser(live, benchmark):
    from playwright.sync_api import sync_playwright
    import mimetypes
    import os
    import shutil
    from benchmark import QUERIES as timed_queries, fixture

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=os.environ.get('UCR_BROWSER_EXECUTABLE') or shutil.which('chromium-headless-shell') or None)
        url = LIVE if live else 'http://pilot.test/ucr-pathways/study-options-pilot/'
        def local_file(route):
            path = unquote(urlsplit(route.request.url).path).removeprefix('/ucr-pathways/')
            file = (ROOT / path).resolve()
            if file.is_dir(): file = file / 'index.html'
            if not file.is_relative_to(ROOT) or not file.is_file():
                route.fulfill(status=404,body='')
                return
            route.fulfill(body=file.read_bytes(), content_type=mimetypes.guess_type(file.name)[0] or 'application/octet-stream')

        for js in (False,True):
            ctx = browser.new_context(java_script_enabled=js, viewport={'width':360,'height':800})
            if not live: ctx.route('http://pilot.test/**',local_file)
            page = ctx.new_page()
            errors = []
            page.on('pageerror', lambda exc: errors.append(str(exc)))
            page.goto(url)
            if js:
                box = page.get_by_role('searchbox')
                box.wait_for()
                for query, slug, full in QUERIES:
                    box.fill(query)
                    first = page.locator('#options li').first
                    if slug:
                        assert first.get_attribute('data-option') == slug, query
                        assert first.locator('.match').text_content().startswith('Matches' if full else 'Partial match'), query
                    else:
                        assert page.locator('#options li').count() == 0 and 'No study options' in page.locator('#status').text_content()
                box.fill('climate and economics')
                page.reload()
                assert box.input_value() == 'climate and economics'
                page.locator('#options li').first.get_by_role('link').click()
                assert page.url.endswith('earth-climate-economics/')
                page.go_back()
                page.get_by_role('button',name='Show all options').click()
            assert page.locator('#options li').count() == 7
            for width in (320,390,1280):
                page.set_viewport_size({'width':width,'height':820})
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.get_by_role('link', name='Film, literature and visual culture').click()
                assert page.locator('details').count() == 24
                page.locator('summary').first.click()
                assert page.locator('details').first.get_attribute('open') is not None
                page.get_by_role('link',name='Alumni destinations').click()
                assert page.url.endswith('#destinations')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.get_by_role('link',name='Browse all study options').click()
            if js and benchmark:
                data = json.dumps(fixture(), separators=(',', ':'), ensure_ascii=False)
                timing = page.evaluate('''async ([data, queries]) => {
                  const {createSearch} = await import('./search.js');
                  const t0 = performance.now(); const run = createSearch(JSON.parse(data));
                  const init = performance.now()-t0;
                  for(let i=0;i<40;i++) run(queries[i%queries.length]);
                  const times = [];
                  for(let i=0;i<500;i++){
                    const t=performance.now(); run(queries[i%queries.length]); times.push(performance.now()-t);
                  }
                  times.sort((a,b)=>a-b);
                  return {init, median:times[249],p95:times[474]};
                }''',[data,timed_queries])
                print('Chromium',browser.version,'fixture bytes',len(data.encode()),'ms',timing)
            assert not errors, errors
            ctx.close()
        browser.close()
    print('Browser checks passed at 320, 390 and 1280 CSS pixels, with and without JavaScript.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live',action='store_true')
    parser.add_argument('--browser',action='store_true')
    parser.add_argument('--benchmark',action='store_true')
    args = parser.parse_args()
    check_html(args.live)
    if args.browser: check_browser(args.live, args.benchmark)
