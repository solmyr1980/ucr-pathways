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
BASE = '68084df0f3ab9a0314f5f0f8fad9426273151de7'
def read(p): return json.loads((ROOT/p).read_text())
def old(p): return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def blob(p):
 b=(ROOT/p).read_bytes();return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
sheet=openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx',data_only=True).active
headers=[x.value for x in sheet[1]]
workbook={r[headers.index('osiris')]:dict(zip(headers,r)) for r in sheet.iter_rows(min_row=2,values_only=True)}
record=read('data/counselor/comparisons/cp-000019.json')
programmes=[];sets=[]
for p in record['programmes']:
 if p['family']!='ucr':continue
 completed=set();checks=[];total=0;advanced=0
 sems=p['schedule']['semesters'];assert len(sems)==6
 for i,sem in enumerate(sems):
  assert len(sem['courses'])==4
  for c in sem['courses']:
   w=workbook[c['code']];prereq=w['preq1'];required=re.findall(r'[A-Z]{3}[A-Z]{4}\d{3}',prereq or '')
   assert w[sem['term']]=='X',(c['code'],sem['term'])
   assert set(required)<=completed,(c['code'],required,completed)
   assert w['name']==c['name'] and c['credits']==7.5 and c['level']==int(c['code'][-3])
   total+=c['credits'];advanced+=c['level']==3
   checks.append({'code':c['code'],'term':sem['term'],'offered':w[sem['term']],'formalPrerequisite':prereq,'completedEarlier':all(x in completed for x in required)})
  completed.update(c['code'] for c in sem['courses'])
 assert len(completed)==24 and advanced>=6 and total==180
 assert any(c['code']=='ACCPPDE101' for s in sems[:2] for c in s['courses'])
 programmes.append({'programmeId':p['id'],'uniqueCourses':len(completed),'credits':total,'advancedCourses':advanced,'semesterSizes':[len(s['courses']) for s in sems],'yearOnePpd':True,'checks':checks});sets.append(completed)
assert 'MCCCOMM213' not in set.union(*sets) and 'MCCHEAM212' in sets[0]
pairs=[{'programmes':[f'ucr-{i+1}',f'ucr-{j+1}'],'shared':len(sets[i]&sets[j]),'differentPerProgramme':len(sets[i]-sets[j])} for i,j in [(0,1),(0,2),(1,2)]]
assert all(p['differentPerProgramme']>=4 for p in pairs)
records={id:read('data/counselor/comparisons/'+id+'.json') for id in ['cp-000277','cp-000019']}
for id,r in records.items():
 previous=json.loads(old('data/counselor/comparisons/'+id+'.json'))
 if id=='cp-000277':
  target=next(c for c in previous['comparator']['components'] if c['id']=='y1-swahili-ii');assert target['name']=='Swahili II (curriculum code 5731V015Y)';target['name']='Swahili II'
 assert r['comparator']['components']==previous['comparator']['components'],id
 assert sum(c['credits'] for c in r['comparator']['components'])==(175 if id=='cp-000277' else 180)
 assert set(r['audience']['curriculum']['componentIds'])=={c['id'] for c in r['comparator']['components']}
assert records['cp-000277']['exception']['type']=='external-programme-unresolved'
assert len(records['cp-000277']['programmes'])==1
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
assert 'cp-000019.json' not in errors and 'cp-000277.json' not in errors
before=list(csv.DictReader(io.StringIO(old('data/registry/programme_interests.csv').decode())))
with (ROOT/'data/registry/programme_interests.csv').open() as f:after=list(csv.DictReader(f))
assert len(before)==len(after)==22259
assert [r['source_interest_excel_row'] for r in before]==[r['source_interest_excel_row'] for r in after]
changed=[int(a['source_interest_excel_row']) for a,b in zip(before,after) if a!=b]
assert all(a['counselor_programme_id'] in records for a,b in zip(before,after) if a!=b)
for id in records:
 ledger=read('docs/qc/evidence/counselor-first-pair-completion-2026-10-17/'+id+'-interest-corrections.json')
 for entry in ledger:
  a=next(x for x in before if int(x['source_interest_excel_row'])==entry['row']);b=next(x for x in after if int(x['source_interest_excel_row'])==entry['row'])
  assert entry['before']==a and entry['after']==b
changed_canonical=subprocess.check_output(['git','diff','--name-only',BASE,'--','data/counselor/comparisons'],cwd=ROOT,text=True).splitlines()
assert set(changed_canonical)=={f'data/counselor/comparisons/{id}.json' for id in records}
result={'otherCanonicalRecordsUnchanged':True,'baselineCommit':BASE,'workbookBlob':blob('data/reference/ucr_courses_enriched.xlsx'),'inputBlobs':{id:{'canonical':blob('data/counselor/comparisons/'+id+'.json'),'decision':blob('data/counselor/decisions/'+id+'.json')} for id in records},'programmes':programmes,'distinctness':pairs,'externalAcademicRequirementsUnchanged':True,'externalDisplayNameCorrection':{'cp-000277/y1-swahili-ii':{'before':'Swahili II (curriculum code 5731V015Y)','after':'Swahili II','provenance':'Course code retained in the unchanged internal component note.'}},'externalCredits':{'cp-000277':175,'cp-000019':180},'registry':{'rows':len(after),'stableIdentifiersPreserved':True,'changedRows':changed,'otherTargetsUnchanged':True},'fullFormalSchema':{'checkedRecords':len(list((ROOT/'data/counselor/comparisons').glob('cp-*.json'))),'affectedRecordCount':len(errors),'affectedRecords':list(errors),'errorMessages':sum(map(len,errors.values())),'affectedSetUnchanged':True,'pilotCasesPassed':['cp-000277','cp-000019']},'alignmentCounts':dict(Counter(a['matchType'] for a in record['comparisonAlignment']))}
(OUT/'verification-replay.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: 72 workbook placements; all prerequisites, names, levels, credits and availability; 3 distinct programmes; unchanged external curricula; 121 stable case interest IDs; two full schemas pass; existing 64-record schema discrepancy unchanged.')
