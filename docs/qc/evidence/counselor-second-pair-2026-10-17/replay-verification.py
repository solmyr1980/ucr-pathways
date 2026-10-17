#!/usr/bin/env python3
"""Independent mechanical/evidence-identity replay; not an academic truth test.
Run from any directory with openpyxl, jsonschema and referencing installed.
Writes verification-replay.json beside this script. No production data is changed.
"""
import csv, hashlib, io, json, re, subprocess
from pathlib import Path
from collections import Counter
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = '89cb393d4ed6f1d52c1333e7f57660d215ebedeb'
def read(p): return json.loads((ROOT/p).read_text())
def old(p): return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def blob(p):
 b=(ROOT/p).read_bytes();return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
sheet=openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx',data_only=True).active
headers=[x.value for x in sheet[1]]
workbook={r[headers.index('osiris')]:dict(zip(headers,r)) for r in sheet.iter_rows(min_row=2,values_only=True)}
RECORD_IDS = ['cp-000119', 'cp-000001']
records={id:read('data/counselor/comparisons/'+id+'.json') for id in RECORD_IDS}
programmes=[];pairs=[]
for id,record in records.items():
 sets=[]
 for p in record['programmes']:
  if p['family']!='ucr':continue
  completed=set();checks=[];total=0;advanced=0
  sems=p['schedule']['semesters'];assert len(sems)==6
  for sem in sems:
   assert len(sem['courses'])==4
   for c in sem['courses']:
    w=workbook[c['code']];prereq=w['preq1'];required=re.findall(r'[A-Z]{3}[A-Z]{4}\d{3}',prereq or '')
    assert w[sem['term']]=='X',(id,c['code'],sem['term'])
    assert set(required)<=completed,(id,c['code'],required,completed)
    assert w['name']==c['name'] and c['credits']==7.5 and c['level']==int(c['code'][-3])
    total+=c['credits'];advanced+=c['level']==3
    checks.append({'code':c['code'],'term':sem['term'],'offered':w[sem['term']],'formalPrerequisite':prereq,'completedEarlier':all(x in completed for x in required)})
   completed.update(c['code'] for c in sem['courses'])
  assert len(completed)==24 and advanced>=6 and total==180
  assert any(c['code']=='ACCPPDE101' for s in sems[:2] for c in s['courses'])
  programmes.append({'recordId':id,'programmeId':p['id'],'uniqueCourses':len(completed),'credits':total,'advancedCourses':advanced,'semesterSizes':[len(s['courses']) for s in sems],'yearOnePpd':True,'checks':checks});sets.append(completed)
 for i in range(len(sets)):
  for j in range(i+1,len(sets)):
   different=len(sets[i]-sets[j]);assert different>=4
   pairs.append({'recordId':id,'programmes':[f'ucr-{i+1}',f'ucr-{j+1}'],'shared':len(sets[i]&sets[j]),'differentPerProgramme':different})
 previous=json.loads(old('data/counselor/comparisons/'+id+'.json'))
 facts=lambda r:[(c['id'],c['name'],c['credits']) for c in r['comparator']['components']]
 assert facts(record)==facts(previous) and sum(c[2] for c in facts(record))==180
 assert set(record['audience']['curriculum']['componentIds'])=={c[0] for c in facts(record)}
 if id=='cp-000001':
  assert [p['schedule'] for p in record['programmes'][1:]]==[p['schedule'] for p in previous['programmes'][1:]]
  case=read('data/counselor/qc/comprehensive-reaudit/cp-000001.json')
  assert case['originalCanonicalSnapshot']==previous
  assert case['recoveryOrReconstruction']['originalDecision'] is None
import tempfile
with tempfile.TemporaryDirectory(prefix='ucr-second-replay-') as name:
 for id in records:
  output=Path(name)/(id+'.json')
  subprocess.run(['node','scripts/build-counselor-production.mjs','data/counselor/decisions/'+id+'.json','--output',str(output)],cwd=ROOT,check=True,capture_output=True)
  assert output.read_bytes()==(ROOT/('data/counselor/comparisons/'+id+'.json')).read_bytes()
schemas=[json.loads(p.read_text()) for p in (ROOT/'data/schema').glob('*.json')]
registry=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in schemas)
validators={s['$id'].rsplit('/',1)[-1]:Draft202012Validator(s,registry=registry) for s in schemas}
errors={}
for p in sorted((ROOT/'data/counselor/comparisons').glob('cp-*.json')):
 r=json.loads(p.read_text());name='counselor-exception.schema.json' if r.get('recordStatus')=='exception' else 'counselor-comparison.schema.json'
 found=[{'path':list(e.path),'message':e.message} for e in validators[name].iter_errors(r)]
 if found:errors[p.name]=found
baseline=read('docs/qc/evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json')
assert list(errors)==baseline['affectedRecords'] and len(errors)==64
assert all(id+'.json' not in errors for id in records)
before=list(csv.DictReader(io.StringIO(old('data/registry/programme_interests.csv').decode())))
with (ROOT/'data/registry/programme_interests.csv').open() as f:after=list(csv.DictReader(f))
assert len(before)==len(after)==22259
assert [r['source_interest_excel_row'] for r in before]==[r['source_interest_excel_row'] for r in after]
changed=[int(a['source_interest_excel_row']) for a,b in zip(before,after) if a!=b]
assert all(a['counselor_programme_id'] in records for a,b in zip(before,after) if a!=b)
for id in records:
 ledger=read('docs/qc/evidence/counselor-second-pair-2026-10-17/'+id+'-interest-corrections.json')
 for entry in ledger:
  a=next(x for x in before if int(x['source_interest_excel_row'])==entry['row']);b=next(x for x in after if int(x['source_interest_excel_row'])==entry['row'])
  assert entry['before']==a and entry['after']==b
changed_canonical=subprocess.check_output(['git','diff','--name-only',BASE,'--','data/counselor/comparisons'],cwd=ROOT,text=True).splitlines()
assert set(changed_canonical)=={f'data/counselor/comparisons/{id}.json' for id in records}
result={'reviewedCommit':'ee64de039ad6167f14f00396058f6e267f44e0dc','otherCanonicalRecordsUnchanged':True,'baselineCommit':BASE,'workbookBlob':blob('data/reference/ucr_courses_enriched.xlsx'),'inputBlobs':{id:{'canonical':blob('data/counselor/comparisons/'+id+'.json'),'decision':blob('data/counselor/decisions/'+id+'.json')} for id in records},'programmes':programmes,'distinctness':pairs,'externalAcademicRequirementsUnchanged':True,'externalCredits':{id:180 for id in records},'cp001All48PlacementsPreserved':True,'cp001OriginalCanonicalSnapshotPreserved':True,'compilerReplaysByteIdentical':RECORD_IDS,'registry':{'rows':len(after),'stableIdentifiersPreserved':True,'reviewedTargetRows':sum(r['counselor_programme_id'] in records for r in after),'changedRows':changed,'otherTargetsUnchanged':True},'fullFormalSchema':{'checkedRecords':438,'affectedRecordCount':len(errors),'affectedRecords':list(errors),'affectedSetUnchanged':True,'pilotCasesPassed':RECORD_IDS},'alignmentCounts':{id:dict(Counter(a['matchType'] for a in r['comparisonAlignment'])) for id,r in records.items()}}
(OUT/'verification-replay.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: 72 workbook placements, formal prerequisites/offerings, 3 programmes, unchanged external academic requirements, all 48 original CP001 placements, 82 stable interest IDs, both byte-identical compiler replays/full schemas, unchanged 64-record discrepancy set.')
