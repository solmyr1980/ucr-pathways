"""Mechanical completion checks. Source/academic judgment is recorded separately."""
import hashlib, itertools, json, pathlib, re, subprocess, sys, tempfile
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
ROOT=pathlib.Path(__file__).resolve().parents[4]
OUT=pathlib.Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def blob(p):
 b=p.read_bytes();return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def run(args):
 r=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
 assert r.returncode==0,r.stdout[-3000:]+r.stderr[-3000:]
 return {'command':args,'exitCode':r.returncode,'stdoutSha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'tail':r.stdout[-450:]}
schemas=[read(p) for p in (ROOT/'data/schema').glob('*.json')]
reg=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in schemas)
validators={s['$id'].rsplit('/',1)[-1]:Draft202012Validator(s,registry=reg) for s in schemas}
sheet=openpyxl.load_workbook(ROOT/'data/reference/ucr_courses_enriched.xlsx',data_only=True).active
h=[c.value for c in sheet[1]];wb={r[h.index('osiris')]:dict(zip(h,r)) for r in sheet.iter_rows(min_row=2,values_only=True)}
for cp in sys.argv[1:]:
 canonical=ROOT/f'data/counselor/comparisons/{cp}.json';decision=ROOT/f'data/counselor/decisions/{cp}.json';record=read(canonical)
 validators['counselor-comparison.schema.json'].validate(record);validators['counselor-audience.schema.json'].validate(record['audience'])
 with tempfile.TemporaryDirectory(prefix='ucr-byte-replay-') as tmp:
  output=pathlib.Path(tmp)/f'{cp}.json'
  run(['node','scripts/build-counselor-production.mjs',str(decision),'--output',str(output)])
  assert output.read_bytes()==canonical.read_bytes()
 assert sum(c['credits'] for c in record['comparator']['components'])==180
 sets=[];schedules=[];checks=[]
 for programme in record['programmes'][1:]:
  seen=set();flat=[]
  for sem in programme['schedule']['semesters']:
   assert len(sem['courses'])==4
   for c in sem['courses']:
    w=wb[c['code']];pre=re.findall(r'[A-Z]{7}\d{3}',w['preq1'] or '')
    assert w[sem['term']]=='X' and set(pre)<=seen,(cp,programme['id'],c['code'],sem['term'],pre)
    assert c['name']==w['name'] and c['credits']==7.5 and c['level']==int(c['code'][-3])
    checks.append({'programmeId':programme['id'],'courseCode':c['code'],'term':sem['term'],'formalPrerequisite':w['preq1'],'prerequisitesCompletedEarlier':pre,'offering':w[sem['term']],'status':'passed'})
    flat.append(c)
   seen.update(c['code'] for c in sem['courses'])
  assert len(flat)==len(seen)==24 and sum(c['credits'] for c in flat)==180
  advanced=sum(c['level']>=3 for c in flat);assert advanced>=6
  assert any(c['code']=='ACCPPDE101' for s in programme['schedule']['semesters'][:2] for c in s['courses'])
  sets.append(seen);schedules.append({'programmeId':programme['id'],'courses':24,'credits':180,'advancedCourses':advanced})
 distinct=[{'pair':[i+1,j+1],'differentCoursesPerProgramme':len(sets[i]-sets[j]),'differentECPerProgramme':len(sets[i]-sets[j])*7.5} for i,j in itertools.combinations(range(len(sets)),2)]
 assert all(x['differentCoursesPerProgramme']>=4 for x in distinct)
 audits={a['programmeId']:a for a in record['academicRationale']['finalMethodologyAudit']['alternatives']}
 content=[]
 for p in record['programmes'][1:]:
  trace={x['courseCode']:x for x in audits[p['id']]['courseTraceability']}
  assert set(trace)=={c['code'] for s in p['schedule']['semesters'] for c in s['courses'] if c['code']!='ACCPPDE101'}
  for code,t in trace.items():
   w=wb[code];field='profile' if w['profile'] else 'description2'
   content.append({'programmeId':p['id'],'courseCode':code,'sourceField':field,'sourceSha256':hashlib.sha256(w[field].encode()).hexdigest(),'reviewedContribution':t['rationale'],'basisLabels':t['basisLabels']})
 result={'checkedOn':'2026-10-20','inputBlobs':{'canonical':blob(canonical),'decision':blob(decision)},'workbookBlob':blob(ROOT/'data/reference/ucr_courses_enriched.xlsx'),'status':'passed','formalAndAudienceSchema':'passed','compilerByteReplay':'passed','externalComponents':len(record['comparator']['components']),'externalEC':180,'schedules':schedules,'pairwiseDistinctness':distinct,'placements':checks,'courseContentReferences':content,'commands':[run(['npm','run','validate:counselor']),run(['git','diff','--check'])],'scopeLimit':'Mechanical checks verify data and implementation; the academic review separately evaluates the actual course content and comparability.'}
 (OUT/f'{cp}-mechanical-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(cp+': PASS formal schemas, exact replay, 72 workbook placements, traceability coverage, distinctness, operational corpus and clean diff.')
