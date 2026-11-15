"""Stage 2 bookkeeping must fail closed on scope and evidence errors."""
import copy, importlib.util, json, tempfile, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('audit',Path(__file__).with_name('validate-comprehensive-reaudit.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
REAL=Path(__file__).resolve().parents[1]
class Stage2(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  self.a=json.loads((REAL/'data/counselor/qc/full-restart-2026-10-27.json').read_text());self.a['cases']=[]
  for p in [self.a['postAuditReviews'][0]['assignmentRef'],self.a['postAuditReviews'][0]['baselineRef'],'docs/qc/evidence/qualified-comparison-stage1-2026-11-15/baseline.json']:
   dest=self.root/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((REAL/p).read_bytes())
 def check(self):m.validate_stage2(self.root,self.a)
 def test_valid_and_preserved_stage1(self):self.check()
 def test_unauthorized_id(self):
  self.a['postAuditReviews'][0]['caseIds'][0]='cp-000072'
  with self.assertRaises(ValueError):self.check()
 def test_overlap(self):
  self.a['postAuditReview']['caseIds'][0]=self.a['postAuditReviews'][0]['caseIds'][0]
  with self.assertRaises(ValueError):self.check()
 def fixture(self):
  i=self.a['postAuditReviews'][0]['caseIds'][0];p='case.json';e='review.json'
  for kind in ['decisions','comparisons']:
   dest=self.root/f'data/counselor/{kind}/{i}.json';dest.parent.mkdir(parents=True);dest.write_text('{}')
  ev={'caseId':i,'reviewStatus':'completed','outcome':'external-programme-unresolved','inputBlobs':{k:m.git_blob(self.root/f'data/counselor/{v}/{i}.json') for k,v in [('decision','decisions'),('canonical','comparisons')]}}
  (self.root/e).write_text(json.dumps(ev))
  c={'academicDisposition':'external-programme-unresolved','stage2Review':{'process':self.a['postAuditReviews'][0]['id'],'status':'completed','evidenceRef':e,'evidenceBlob':m.git_blob(self.root/e)}}
  (self.root/p).write_text(json.dumps(c));self.a['cases']=[{'id':i,'evidenceFile':p}];return i
 def test_completed_exact_inputs(self):self.fixture();self.check()
 def test_missing_evidence(self):
  self.fixture();(self.root/'review.json').unlink()
  with self.assertRaises(ValueError):self.check()
 def test_stale_evidence(self):
  self.fixture();(self.root/'review.json').write_text('{}')
  with self.assertRaises(ValueError):self.check()
 def test_stale_canonical(self):
  i=self.fixture();(self.root/f'data/counselor/comparisons/{i}.json').write_text('{"changed":true}')
  with self.assertRaises(ValueError):self.check()
if __name__=='__main__':unittest.main()
