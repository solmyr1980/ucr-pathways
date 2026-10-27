import json,pathlib,re,hashlib,subprocess,tempfile,csv,collections
import openpyxl
from jsonschema import Draft202012Validator
from referencing import Registry,Resource
B=pathlib.Path('docs/qc/evidence/counselor-full-restart-2026-10-27/cp-000002');d=json.load(open('data/counselor/decisions/cp-000002.json'));r=json.load(open('data/counselor/comparisons/cp-000002.json'));rs=list(openpyxl.load_workbook('data/reference/ucr_courses_enriched.xlsx',data_only=True).active.values);w={x[2]:dict(zip(rs[0],x))for x in rs[1:]};checks=[];sets=[]
for i,a in enumerate(d['alternatives']):
 done=set();advanced=0;cc=[]
 for si,sem in enumerate(a['semesters']):
  assert len(sem)==4;term=['2026h2','2027h1','2027h2','2028h1','2028h2','2029h1'][si]
  for code in sem:
   x=w[code];req=re.findall('[A-Z]{7}[0-9]{3}',x['preq1']or'');assert code not in done and set(req)<=done and x[term]=='X',(i,code,term,req);advanced+=code[-3]=='3';cc.append({'code':code,'term':term,'formalPrerequisite':x['preq1'],'prerequisitesEarlier':True,'offered':True})
  done.update(sem)
 assert len(done)==24 and advanced>=6 and 'ACCPPDE101'in sum(a['semesters'][:2],[]);sets.append(done);checks.append({'programmeId':f'ucr-{i+1}','placements':cc,'credits':180,'uniqueCourses':24,'advanced':advanced,'year1PPD':True})
pairs=[{'programmes':[i+1,j+1],'differentEach':len(a-b),'differentEC':len(a-b)*7.5}for i,a in enumerate(sets)for j,b in enumerate(sets)if j>i];assert all(x['differentEach']>=4 for x in pairs)
ss=[json.load(open(p))for p in pathlib.Path('data/schema').glob('*.json')];reg=Registry().with_resources((s['$id'],Resource.from_contents(s))for s in ss if '$id'in s)
for name,val in [('counselor-comparison',r),('counselor-final-methodology',r),('counselor-audience',r['audience'])]:Draft202012Validator(json.load(open('data/schema/'+name+'.schema.json')),registry=reg).validate(val)
with tempfile.TemporaryDirectory()as td:
 o=pathlib.Path(td)/'replay.json';subprocess.run(['node','scripts/build-counselor-production.mjs','data/counselor/decisions/cp-000002.json','--output',str(o)],check=True,capture_output=True);assert o.read_bytes()==pathlib.Path('data/counselor/comparisons/cp-000002.json').read_bytes()
assert sum(c[2]for c in d['comparator']['components'])==180
profiles=[w[c]for c in sorted(set.union(*sets))];(B/'enriched-course-review.json').write_text(json.dumps({'workbookBlob':subprocess.check_output(['git','hash-object','data/reference/ucr_courses_enriched.xlsx'],text=True).strip(),'actualProfilesRead':profiles,'courseContributions':d['trace']},indent=2,ensure_ascii=False)+'\n');(B/'mechanical-schema-replay.json').write_text(json.dumps({'checks':checks,'pairwise':pairs,'fullComparisonSchema':'passed','fullFinalMethodologySchema':'passed','fullAudienceSchema':'passed','compilerReplay':'byte-exact','externalEC':180,'externalComponents':len(d['comparator']['components']),'uniqueProfiles':len(profiles)},indent=2)+'\n');print('PASS',len(profiles),'profiles,48placements,fullschemas,byteexactreplay',pairs)
