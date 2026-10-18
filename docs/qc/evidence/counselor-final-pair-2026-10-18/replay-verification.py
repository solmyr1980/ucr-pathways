#!/usr/bin/env python3
"""Read-only independent workbook/schema/compiler replay; not academic approval.
Run with target CP IDs. Writes a target-scoped result beside this script.
"""
import csv,hashlib,io,json,re,subprocess,sys,tempfile
from pathlib import Path
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry,Resource
ROOT=Path(__file__).resolve().parents[4];OUT=Path(__file__).resolve().parent
BASE='b313800f147d37afaaa6b9efa11e61d9a990f571'
ids=sys.argv[1:] or ['cp-000035','cp-000330']
def blob(p):
 b=p.read_bytes();return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def read(p):return json.loads(p.read_text())
sheet=openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx',data_only=True).active
h=[c.value for c in sheet[1]];wb={r[h.index('osiris')]:dict(zip(h,r)) for r in sheet.iter_rows(min_row=2,values_only=True)}
programmes=[];pairs=[];records={};inputs={}
for id in ids:
 r=read(ROOT/f'data/counselor/comparisons/{id}.json');records[id]=r
 old=read(OUT/f'{id}-original-comparisons.json')
 for kind in ['decisions','comparisons']:
  assert (OUT/f'{id}-original-{kind}.json').read_bytes()==subprocess.check_output(['git','show',BASE+f':data/counselor/{kind}/{id}.json'],cwd=ROOT)
 with tempfile.TemporaryDirectory() as t:
  archived=Path(t)/'archived.json';subprocess.run(['node','scripts/build-counselor-production.mjs',str(OUT/f'{id}-original-decisions.json'),'--output',str(archived)],cwd=ROOT,check=True,capture_output=True)
  assert archived.read_bytes()==(OUT/f'{id}-original-comparisons.json').read_bytes()
 facts=lambda x:[(c['id'],c['name'],c['credits']) for c in x['comparator']['components']]
 assert facts(r)==facts(old) and sum(c[2] for c in facts(r))==180
 assert set(r['audience']['curriculum']['componentIds'])=={c[0] for c in facts(r)}
 sets=[]
 # Archive feasibility also tested when active comparison is withdrawn.
 for p in old['programmes']:
  if p['family']!='ucr':continue
  completed=set();checks=[];advanced=0
  for sem in p['schedule']['semesters']:
   assert len(sem['courses'])==4
   for c in sem['courses']:
    w=wb[c['code']];req=w['preq1'];required=re.findall(r'[A-Z]{3}[A-Z]{4}\d{3}',req or '')
    assert req=='NONE' or required, (c['code'],req)
    assert set(required)<=completed and w[sem['term']]=='X',(id,c['code'],sem['term'],req)
    assert c['name']==w['name'] and c['level']==int(c['code'][-3]) and c['credits']==7.5
    advanced+=c['level']==3
    checks.append({'code':c['code'],'term':sem['term'],'offered':w[sem['term']],'prerequisite':req,'completedEarlier':True})
   completed.update(c['code'] for c in sem['courses'])
  assert len(completed)==24 and advanced>=6 and any(c['code']=='ACCPPDE101' for s in p['schedule']['semesters'][:2] for c in s['courses'])
  if not r.get('exception'):
   current=next(z for z in r['programmes'] if z['id']==p['id']);assert current['schedule']==p['schedule']
  programmes.append({'id':id,'programmeId':p['id'],'scope':'active' if not r.get('exception') else 'preserved superseded composition, not current academic approval','credits':180,'uniqueCourses':24,'advancedCourses':advanced,'checks':checks});sets.append(completed)
 for i in range(len(sets)):
  for j in range(i+1,len(sets)):
   n=len(sets[i]-sets[j]);assert n>=4;pairs.append({'id':id,'pair':[i+1,j+1],'differentPerProgramme':n})
 with tempfile.TemporaryDirectory() as d:
  o=Path(d)/'record.json';subprocess.run(['node','scripts/build-counselor-production.mjs',f'data/counselor/decisions/{id}.json','--output',str(o)],cwd=ROOT,check=True,capture_output=True);assert o.read_bytes()==(ROOT/f'data/counselor/comparisons/{id}.json').read_bytes()
 inputs[id]={k:blob(ROOT/f'data/counselor/{folder}/{id}.json') for k,folder in [('canonical','comparisons'),('decision','decisions')]}
sc=[read(p) for p in (ROOT/'data/schema').glob('*.json')];reg=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in sc);vs={s['$id'].split('/')[-1]:Draft202012Validator(s,registry=reg) for s in sc}
errors=[]
for p in sorted((ROOT/'data/counselor/comparisons').glob('cp-*.json')):
 r=read(p);v=vs['counselor-exception.schema.json' if r.get('recordStatus')=='exception' else 'counselor-comparison.schema.json']
 if list(v.iter_errors(r)):errors.append(p.name)
baseline=read(ROOT/'docs/qc/evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json');assert errors==baseline['affectedRecords'] and len(errors)==64;assert all(id+'.json' not in errors for id in ids)
raw=subprocess.check_output(['git','show',BASE+':data/registry/programme_interests.csv'],cwd=ROOT);assert raw==(ROOT/'data/registry/programme_interests.csv').read_bytes()
changed=subprocess.check_output(['git','diff','--name-only',BASE,'--','data/counselor/comparisons'],cwd=ROOT,text=True).splitlines();assert set(changed)<={f'data/counselor/comparisons/{id}.json' for id in ['cp-000035','cp-000330']}
result={'inputCommit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'inputBlobs':inputs,'workbookBlob':blob(ROOT/'data/reference/ucr_courses_enriched.xlsx'),'externalRequirementsPreserved':True,'registryUnchanged':True,'originalDecisionAndCanonicalBytesPreserved':True,'archivedCompilerReplaysByteIdentical':ids,'otherCanonicalRecordsUnchanged':True,'programmes':programmes,'distinctness':pairs,'compilerReplayByteIdentical':ids,'formalSchema':{'recordsChecked':438,'targetCasesPassed':ids,'preExistingAffectedCount':64,'affectedSetUnchanged':True,'baselineEvidence':'docs/qc/evidence/counselor-shared-foundation-2026-10-17/preexisting-schema-discrepancies.json'}}
(OUT/('verification-replay-'+'-'.join(ids)+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('PASS workbook, preserved curricula/schedules, exact compiler replays, full target schemas, unchanged 64-record discrepancy and non-target records/registry',ids)
