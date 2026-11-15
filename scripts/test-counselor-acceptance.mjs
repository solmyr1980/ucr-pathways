import assert from 'node:assert/strict';
import fs from 'node:fs';
import {buildProductionRecord} from './build-counselor-production.mjs';
import {validateAcceptance} from './counselor-acceptance.mjs';
import {validateAudience} from './counselor-audience.mjs';
import {validateExample} from './example-utils.mjs';
import {stripOptionalIndependentResearch} from './optional-independent-research.mjs';
const read=p=>JSON.parse(fs.readFileSync(p));
const ordinary=read('data/counselor/decisions/cp-000019.json');
assert.deepEqual(buildProductionRecord(ordinary,process.cwd()),read('data/counselor/comparisons/cp-000019.json'));
export function fixture() {
 const d=structuredClone(ordinary);
 // Deliberately incomplete external boundary; no components invented to close it.
 const removed=d.comparator.components.pop()[0];
 d.blocks=d.blocks.map(([id,title,rows])=>[id,title,rows.filter(([code,component])=>code||component!==removed).map(([code,component,rationale])=>component===removed?[code,null,null]:[code,component,rationale])]);
 if(d.researchComponentId===removed)d.researchComponentId=null;
 const ids=d.comparator.components.map(c=>c[0]);
 d.audience={...d.audience,curriculum:{status:'partial',componentIds:ids,limitation:'Some required study is unverified and excluded.'},comparisonScope:{label:'Qualified academic-core comparison',assessed:'Documented subjects only.',excluded:'Unverified required final study and culminating assessment.',nominalCredits:180}};
 d.acceptance={standard:'bounded-materiality-2026-11-15',basis:'qualified-comparison',scope:'academic-core',claim:'A meaningful response to the documented academic core.',targetContext:'Synthetic regression fixture only; no production approval.',reviewedOn:'2026-11-15',verifiedComponentIds:ids,externalEvidenceRefs:['docs/qc/deferred-case-qualified-comparison-stage1-implementation-assignment-2026-11-15.md'],ucrEvidenceRefs:['data/reference/ucr_courses_enriched.xlsx'],challengeEvidenceRefs:['scripts/test-counselor-acceptance.mjs'],challengeMethod:'Synthetic contract test, not an academic review.',uncertainties:[{fact:'Final study unknown.',evidenceRefs:['scripts/test-counselor-acceptance.mjs'],adverseResolutions:[{resolution:'Final study is practical.',effectOnClaim:'Culminating training remains excluded.',claimSurvives:true},{resolution:'Final study is research.',effectOnClaim:'Culminating training remains excluded.',claimSurvives:true}]}]};
 return d;
}
const d=fixture(),r=buildProductionRecord(d,process.cwd());
assert.deepEqual(r.acceptance,d.acceptance);assert.deepEqual(r.audience,d.audience);
assert.deepEqual(validateAcceptance(r),[]);assert.deepEqual(validateAudience(r),[]);
assert.deepEqual(validateExample(stripOptionalIndependentResearch(r)).errors,[]);
function reject(mutator) {const x=structuredClone(d);mutator(x);assert.throws(()=>buildProductionRecord(x,process.cwd()));}
reject(x=>delete x.acceptance);
reject(x=>x.acceptance.uncertainties[0].adverseResolutions[0].claimSurvives=false);
reject(x=>x.acceptance.uncertainties=[]);
reject(x=>x.acceptance.verifiedComponentIds.pop());
reject(x=>delete x.acceptance.challengeEvidenceRefs);
reject(x=>delete x.audience.comparisonScope);
reject(x=>x.audience.curriculum.status='complete');
reject(x=>x.acceptance.basis='robust-no-match');
reject(x=>x.alternatives[0].semesters[0].pop());
const no=read('data/counselor/decisions/cp-000277.json');no.exception.type='no-defensible-ucr-match';no.exception.ucrCourseEvidence='Synthetic strongest-response negative proof.';
no.acceptance={...d.acceptance,basis:'robust-no-match',verifiedComponentIds:no.comparator.components.map(c=>c[0])};no.audience={...d.audience,comparisonScope:{...d.audience.comparisonScope,label:'Academic no-match: documented substance'},conceptProgrammeIds:[],noteTypes:[],cellNotes:[],componentNotes:{},curriculum:{...d.audience.curriculum,componentIds:no.acceptance.verifiedComponentIds}};
assert.deepEqual(validateAcceptance(buildProductionRecord(no,process.cwd())),[]);
const bad=structuredClone(no);delete bad.acceptance;assert.throws(()=>buildProductionRecord(bad,process.cwd()),/complete 180/);
const unresolved=read('data/counselor/decisions/cp-000099.json');unresolved.acceptance=no.acceptance;assert.throws(()=>buildProductionRecord(unresolved,process.cwd()));
if(process.env.UCR_ACCEPTANCE_FIXTURE_OUTPUT)fs.writeFileSync(process.env.UCR_ACCEPTANCE_FIXTURE_OUTPUT,JSON.stringify(r,null,2)+'\n');
console.log('Bounded acceptance: ordinary byte-compatible replay; partial positive/negative; adverse tests, scope, unresolved fallback and UCR gates passed.');
