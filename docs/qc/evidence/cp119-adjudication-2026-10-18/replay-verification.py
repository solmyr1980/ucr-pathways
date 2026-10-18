#!/usr/bin/env python3
"""Read-only adjudication replay; writes only the adjacent evidence result.
Requires openpyxl, jsonschema and referencing. Academic judgment is not automated.
"""
import hashlib, json, re, subprocess, tempfile
from pathlib import Path
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
BASE='bc0c34d5d7c0c20e9ef70ea42d7acb4b554e8f7e'
CP='cp-000119'
def read(p):return json.loads(p.read_text())
def blob(p):
 b=p.read_bytes();return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def original(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
r=read(ROOT/f'data/counselor/comparisons/{CP}.json')
old=read(OUT/'superseded-comparison.json')
for kind,name in [('comparisons','superseded-comparison.json'),('decisions','superseded-decision.json')]:
 assert (OUT/name).read_bytes()==original(f'data/counselor/{kind}/{CP}.json')
assert r['comparator']['components']==old['comparator']['components']
assert len(r['comparator']['components'])==26 and sum(c['credits'] for c in r['comparator']['components'])==180
assert r['recordStatus']=='exception' and r['exception']['type']=='no-defensible-ucr-match'
assert len(r['programmes'])==1 and r['programmes'][0]['family']=='comparator'
assert not any(k in r for k in ['blocks','academicRationale','optionalIndependentResearch','comparisonAlignment'])
assert r['audience']['curriculum']['status']=='complete' and r['audience']['conceptProgrammeIds']==[]
assert read(ROOT/'data/counselor/presentation-overrides.json')['cases'][CP]['mode']=='external-only'
assert set(r['audience']['curriculum']['componentIds'])=={c['id'] for c in r['comparator']['components']}
sheet=openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx',data_only=True).active
h=[c.value for c in sheet[1]];wb={row[h.index('osiris')]:dict(zip(h,row)) for row in sheet.iter_rows(min_row=2,values_only=True)}
p=old['programmes'][1];seen=set();checks=[]
for sem in p['schedule']['semesters']:
 assert len(sem['courses'])==4
 for c in sem['courses']:
  w=wb[c['code']];required=re.findall(r'[A-Z]{3}[A-Z]{4}\d{3}',w['preq1'] or '')
  assert w[sem['term']]=='X' and set(required)<=seen
  assert c['name']==w['name'] and c['credits']==7.5 and c['level']==int(c['code'][-3])
  checks.append({'code':c['code'],'term':sem['term'],'formalPrerequisite':w['preq1'],'offered':True,'completedEarlier':True})
 seen.update(c['code'] for c in sem['courses'])
assert len(seen)==24 and len(checks)==24 and len(p['schedule']['semesters'])==6
assert sum(c['level']==3 for s in p['schedule']['semesters'] for c in s['courses'])==6
assert any(c['code']=='ACCPPDE101' for s in p['schedule']['semesters'][:2] for c in s['courses'])
with tempfile.TemporaryDirectory(prefix='cp119-adjudication-replay-') as name:
 for decision,expected,label in [(ROOT/f'data/counselor/decisions/{CP}.json',ROOT/f'data/counselor/comparisons/{CP}.json','current exception'),(OUT/'superseded-decision.json',OUT/'superseded-comparison.json','archived comparison')]:
  output=Path(name)/(label.replace(' ','-')+'.json')
  subprocess.run(['node','scripts/build-counselor-production.mjs',str(decision),'--output',str(output)],cwd=ROOT,check=True,capture_output=True)
  assert output.read_bytes()==expected.read_bytes(),label
schemas=[read(p) for p in (ROOT/'data/schema').glob('*.json')];registry=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in schemas)
validators={s['$id'].rsplit('/',1)[-1]:Draft202012Validator(s,registry=registry) for s in schemas};bad=[]
for p in sorted((ROOT/'data/counselor/comparisons').glob('cp-*.json')):
 x=read(p);v=validators['counselor-exception.schema.json' if x.get('recordStatus')=='exception' else 'counselor-comparison.schema.json']
 if list(v.iter_errors(x)):bad.append(p.name)
expected=read(ROOT/'docs/qc/evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json')['affectedRecords']
assert bad==expected and len(bad)==64 and CP+'.json' not in bad
paths=subprocess.check_output(['git','diff','--name-only',BASE,'--','data/counselor/comparisons','data/counselor/decisions'],cwd=ROOT,text=True).splitlines()
assert set(paths)=={f'data/counselor/{kind}/{CP}.json' for kind in ['comparisons','decisions']}
assert (ROOT/'data/registry/programme_interests.csv').read_bytes()==original('data/registry/programme_interests.csv')
cp001case='data/counselor/qc/comprehensive-reaudit/cp-000001.json'
assert (ROOT/cp001case).read_bytes()==original(cp001case)
for p in (ROOT/'pilot/shiny/data/courses').glob('*.json'):
 assert p.read_bytes()==original(str(p.relative_to(ROOT)))
result={'baselineCommit':BASE,'inputBlobs':{'canonical':blob(ROOT/f'data/counselor/comparisons/{CP}.json'),'decision':blob(ROOT/f'data/counselor/decisions/{CP}.json')},'academicDisposition':'no-defensible-ucr-match','external':{'components':26,'credits':180,'unchanged':True},'preservedProgramme':{'uniqueCourses':24,'advanced':6,'mechanicallyValid':True,'comparabilityApproved':False,'checks':checks},'compilerReplays':{'currentException':'byte-identical','archivedComparison':'byte-identical'},'supersededEvidenceByteIdentical':True,'otherAcademicRecordsUnchanged':True,'cp001CaseUnchanged':True,'entireInterestRegistryUnchanged':True,'reviewedModalCacheUnchanged':True,'formalSchema':{'targetPassed':True,'affectedSetUnchanged':True,'affectedRecordCount':64}}
(OUT/'verification-replay.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: exact archived records, feasible archived24-course programme, unchanged26-component/180-EC external curriculum, both byte-identical compiler replays, current exception full schema, unchanged64-record discrepancy and all other academic/interest records including CP001.')
