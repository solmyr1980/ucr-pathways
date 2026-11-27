"""Build an unpublished scale fixture in memory and time the production JS matcher."""
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
QUERIES = ['film', 'climate and economics', 'climate and machine learning', 'AI and neuroscience',
           'politics, law and human rights', 'biology and business', 'film and aerospace engineering',
           'economics and data science', 'veterinary dentistry', 'data']


def fixture():
    # Assign proxy topic labels by scheduled courses for payload/CPU testing only.
    # Retain every actual counselor alternative, including repeated schedules.
    seed = json.loads((HERE / 'options.json').read_text())
    topics = {}
    for option in seed:
        for topic, evidence in option['topics'].items():
            topics.setdefault(topic, set()).update(evidence['courses'])
    rows = []
    for path in sorted((ROOT / 'data/counselor/comparisons').glob('cp-*.json')):
        for programme in json.loads(path.read_text()).get('programmes', []):
            if programme.get('family') != 'ucr':
                continue
            codes = {c['code'] for s in programme['schedule']['semesters'] for c in s['courses']}
            rows.append({'slug':f"study-option-{len(rows)+1}", 'topics':[t for t, cs in topics.items() if codes & cs]})
    return {'topics':json.loads((HERE / 'aliases.json').read_text()), 'options':rows}


def main():
    data = json.dumps(fixture(), separators=(',', ':'), ensure_ascii=False)
    runner = '''
import {createSearch} from './study-options-pilot/search.js';
import fs from 'node:fs';
const {data, queries} = JSON.parse(fs.readFileSync(0,'utf8'));
const start = performance.now();
const index = JSON.parse(data);
const run = createSearch(index);
const init = performance.now() - start;
for (let i = 0; i < 40; i++) run(queries[i % queries.length]);
const times = [];
for (let i = 0; i < 500; i++) {
  const t = performance.now(); run(queries[i % queries.length]); times.push(performance.now()-t);
}
times.sort((a,b) => a-b);
console.log(index.options.length, "options,", Buffer.byteLength(data), "bytes;",
            "parse/init",init.toFixed(2),"ms; median",times[249].toFixed(2),"ms; p95",times[474].toFixed(2),"ms");
'''
    subprocess.run(['node','--input-type=module','-e',runner], cwd=ROOT, check=True,
                   input=json.dumps({'data':data,'queries':QUERIES}), text=True)


if __name__ == '__main__':
    main()
