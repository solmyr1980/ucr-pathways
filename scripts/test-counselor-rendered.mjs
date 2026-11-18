// End-to-end checks against real Shiny output, plus isolated runtime-only fixtures.
import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
const require = createRequire(import.meta.url);
const {chromium} = require(process.env.UCR_PLAYWRIGHT_MODULE || 'playwright');
const out = path.resolve(process.env.UCR_RENDERED_EVIDENCE_DIR || '/tmp/ucr-counselor-shared-rendered');
fs.mkdirSync(out, {recursive:true});
const results=[];
const cases = {
  actual: [['cp-000377','Actuarial Science'],['cp-000003','Pedagogical'],['cp-000001','Public Administration'],['cp-000019','Arts and Culture'],['cp-000035','Biology'],['cp-000330','Mechanical Engineering'],['cp-000119','Theology'],['cp-000428','Religious Studies'],['cp-000277','African Studies'],['cp-000311','Notarial Law']],
  fixtures: [['cp-000004','Psychology'],['cp-000002','Management of International'],['cp-000005','Psychology'],['cp-000119','Theology'],['cp-000428','Religious Studies'],['cp-000277','African Studies'],['cp-000019','Arts and Culture'],['cp-000003','Pedagogical']]
};
// Stage 1 representatives use actual canonical data, including still-unresolved controls.
for (const [id,query] of [['cp-000250','Clinical Technology'],['cp-000060','Dutch Language'],['cp-000033','Business Administration'],['cp-000396','Tax Law'],['cp-000440','Business and Consumer'],['cp-000317','Law'],['cp-000099','Health and Life'],['cp-000072','Spanish Language'],['cp-000266','Industrial Design']]) {
 const r=JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`));
 if(r.acceptance || ['cp-000099','cp-000072'].includes(id)) cases.actual.push([id,query]);
}
// Stage 2 representative: real qualified 180-EC content with bounded entry uncertainty.
if (JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000041.json')).acceptance) {
 cases.actual.push(['cp-000041','Economics and Business Economics']);
}
if (JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000040.json')).acceptance) {
 cases.actual.push(['cp-000040','German Language and Culture']);
}
// Stage 2 integration covers multiple-core options, the177-EC qualification and a partial-core robust no-match.
for (const [id,query] of [['cp-000113','National Politics'],['cp-000397','Fiscal Economics'],['cp-000263','Architecture, Urbanism']]) {
 if(JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`)).acceptance) cases.actual.push([id,query]);
}
const browser = await chromium.launch({headless:true,executablePath:process.env.UCR_CHROMIUM_PATH || undefined,args:['--no-sandbox']});
try {
 for (const [vi,variant] of ['actual','fixtures'].entries()) {
  const port=3850+vi, url=`http://127.0.0.1:${port}`;
  const logfile=fs.openSync(path.join(out,`${variant}-server.log`),'w');
  const server=spawn(process.env.UCR_RSCRIPT || 'Rscript',['scripts/test-counselor-rendered-server.R',variant,String(port)],{cwd:process.cwd(),env:process.env,stdio:['ignore',logfile,logfile]});
  try {
   let ready=false;
   for(let i=0;i<60;i++) {try{if((await fetch(url)).ok){ready=true;break;}}catch{}await new Promise(r=>setTimeout(r,250));}
   assert.ok(ready,`Shiny ${variant} did not start`);
   for(const [size,viewport] of [['desktop',{width:1440,height:1000}],['mobile',{width:390,height:844}]]) {
    const page=await browser.newPage({viewport});const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(url);await page.locator('#search_text').waitFor();
    for(const [id,query] of cases[variant]) {
     await page.locator('#search_text').fill(query);
     const open=page.locator(`.open-comparison[data-id="${id}"]`);await open.waitFor({timeout:20000});
     const displayName = await open.locator('..').locator('h3').innerText();
     await open.click();
     await page.locator('.comparison-shell').waitFor();
     const body=await page.locator('.comparison-shell').innerText();
     assert.ok(!body.includes('INTERNAL-SENTINEL'),`${variant}/${id}: research leakage`);
     assert.ok(!body.includes('First-listed Culture and Economics'),`${id}: cell bookkeeping exposed`);
     assert.ok(!body.includes('2261'),`${id}: catalogue code exposed`);
     if (await page.locator('.compare-view').count()) {
      assert.ok(!body.includes('What this comparison shows'));
      assert.ok(await page.locator('.closest-match h2').isVisible());
      assert.ok(await page.getByText('This pre-produced comparison is the same for every student.', {exact:true}).isVisible());
      assert.match(await page.locator('.equivalence-note').innerText(), /degree equivalence, professional qualification or automatic eligibility/);
      assert.match(await page.locator('.comparison-legend').innerText(), /partial matches.*blank cell.*Optional independent research.*180 EC/);
     }
     const details = page.locator('.audience-context .comparison-details');
     let detailsText = '';
     if (await details.count()) {
      assert.equal(await details.evaluate(el=>el.open),false);
      assert.ok(await details.evaluate(el=>Boolean(el.compareDocumentPosition(document.querySelector('.compare-view')) & Node.DOCUMENT_POSITION_FOLLOWING)));
      await details.locator('summary').click();
      assert.equal(await details.evaluate(el=>el.open),true);
      detailsText = await details.innerText();
      assert.ok(!detailsText.includes('INTERNAL-SENTINEL'),`${variant}/${id}: research leakage in details`);
      await details.locator('summary').click();
     }
     if (id==='cp-000377') {
      const actuarial = JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000377.json'));
      assert.equal(await page.locator('.comparison-head h1').innerText(),actuarial.comparator.name);
      assert.ok(body.includes(actuarial.academicRationale.alternatives[0].concept));
      assert.ok(detailsText.includes('no dedicated insurance or pension sequence or actuarial thesis'));
     }
     assert.equal(await page.locator('.comparison-shell a[href^="https://"]').count()>0,true);
     const source=JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`,'utf8')).comparator.primarySourceUrl;
     assert.ok(await page.locator('.comparison-shell a').evaluateAll((xs,url)=>xs.some(x=>x.href===url),source),`${id}: official link missing`);
     const geometry=await page.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth,tableWidth:document.querySelector('.compare-table')?.getBoundingClientRect().width,tableHeight:document.querySelector('.compare-table')?.getBoundingClientRect().height}));
     assert.ok(geometry.document<=viewport.width+1,`${id}: page overflow`);
     const nav=page.locator('.comparison-navigation');
     let columns=[];
     if(await nav.count() && size==='mobile') {
      const options=await page.locator('.column-select option').allTextContents();
      for(let i=0;i<options.length;i++) {
       await page.locator('.column-select').selectOption(String(i));
       await page.waitForFunction(i=>Number(document.querySelector('.column-select').value)===i && Math.abs(document.querySelector('.compare-scroll').scrollLeft-i*document.querySelector('.compare-table').getBoundingClientRect().width/Number(document.querySelector('.compare-view').dataset.count))<3,i);
       const g=await page.locator('.compare-table').evaluate(t=>({cellWidth:t.querySelector('thead th').getBoundingClientRect().width,overlap:[...t.querySelectorAll('td .cell-text,th .programme-title')].some(x=>x.scrollWidth>x.clientWidth+1)}));
       assert.ok(g.cellWidth>=300 && !g.overlap,`${id}: cramped or overlapping mobile content`);
       const block=await page.locator('.block-title').first().boundingBox();
       assert.ok(block.x>=0&&block.x+block.width<=viewport.width+1,`${id}: block title inaccessible`);
       assert.equal(await page.locator('.column-name').innerText(),options[i]);
       columns.push({label:options[i],...g});
      }
      await page.locator('.column-previous').click();
      await page.waitForFunction(()=>!document.querySelector('.column-next').disabled);
      await page.locator('.column-next').click();
      await page.locator('.column-select').selectOption('0');
      await page.waitForFunction(()=>document.querySelector('.compare-scroll').scrollLeft<2);
      await page.locator('.compare-view').evaluate(el=>window.scrollTo(0,el.getBoundingClientRect().top+window.scrollY));
      await page.screenshot({path:path.join(out,`${variant}-${id}-${size}-table.png`)});
      await page.locator('.comparison-navigation a').click();
     }
     const modals=[];
     if(variant==='fixtures' && id==='cp-000019') {
      assert.ok(body.includes('Qualified academic-core comparison') && body.includes('Nominal external degree: 180 EC') && body.includes('Unknown requirements are not open electives'));
      assert.equal(await page.locator('.compare-view').count(),1);
     }
     if(id==='cp-000019') {
      for(const code of ['BENBUSI211','MCCHEAM316','MCCHEAM212','DISARIN111']) {
       const button=page.locator(`.course-link[data-code="${code}"]`).first();
       if(size==='mobile') {
        const index=await button.evaluate(b=>Array.from(b.closest('tr').children).indexOf(b.closest('td')));
        await page.locator('.column-select').selectOption(String(index));await page.waitForTimeout(250);
       }
       await button.click();await page.locator('.modal.in').waitFor();
       await page.waitForTimeout(350); // Inspect the settled Bootstrap transition, not its fade-in frame.
       const box=await page.locator('.modal-dialog').boundingBox();
       assert.ok(box.x>=0 && box.y>=0 && box.x+box.width<=viewport.width+1,`${code}: inaccessible modal`);
       const text=await page.locator('.modal.in').innerText();
       assert.ok(text.includes(code==='BENBUSI211'?'business, economic and societal':code==='MCCHEAM316'?'history of art history':code==='MCCHEAM212'?'Renaissance Italy':'philosophical and psychological'),`${code}: wrong modal content`);
       assert.ok(!text.includes('description is not currently available'));
       modals.push({code,text});
       await page.screenshot({path:path.join(out,`${variant}-${code}-${size}.png`)});
       await page.locator('.modal.in button', {hasText:'Close'}).click();await page.locator('.modal').waitFor({state:'hidden'});await page.locator('.modal-backdrop').waitFor({state:'hidden'});
      }
     }
     if(id==='cp-000019') {
      await page.evaluate(()=>Shiny.setInputValue('course_click',{code:'MCCMISSING999',name:'Unavailable test course'},{priority:'event'}));
      await page.locator('.modal.in').waitFor();
      assert.ok((await page.locator('.modal.in').innerText()).includes('A course description is not currently available.'));
      await page.locator('.modal.in button',{hasText:'Close'}).click();await page.locator('.modal').waitFor({state:'hidden'});await page.locator('.modal-backdrop').waitFor({state:'hidden'});
     }
     const current=JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`));
     const externalOnly = (variant === 'fixtures' && id === 'cp-000002') || id === 'cp-000311';
     if(variant==='actual' && current.acceptance?.basis==='qualified-comparison' && !externalOnly) {
      assert.equal(await page.locator('.compare-view').count(),1);
      assert.ok(body.includes(current.audience.comparisonScope.label) && body.includes(current.audience.comparisonScope.excluded));
      assert.ok(body.includes('Nominal external degree: 180 EC') && body.includes('Unknown requirements are not open electives'));
      assert.equal(await page.locator('.course-link').count()>0,true);
      if(id==='cp-000317') assert.ok(body.includes('final 30 EC') && body.includes('150 EC'));
      if(id==='cp-000040') {
       assert.equal(current.acceptance.scope,'academic-core');
       assert.equal(current.comparator.components.reduce((sum,c)=>sum+c.credits,0),165);
       assert.ok(body.includes('165') && body.includes('15 EC') && body.includes('restricted Arts minor'));
      }
      if(id==='cp-000113') {assert.equal(current.acceptance.scope,'academic-core');assert.equal(current.programmes.length,3);assert.ok(body.includes('150')&&/final\s+30\s+EC/.test(body));}
      if(id==='cp-000397') {assert.equal(current.acceptance.scope,'documented-curriculum');assert.equal(current.comparator.components.reduce((sum,c)=>sum+c.credits,0),177);assert.ok(body.includes('177')&&/3\s+EC/.test(body));}
      if(id==='cp-000266') assert.equal(current.programmes.length,3,'Two independently reviewed UCR options must be present');
      const scopeBox=await page.locator('.qualified-scope').boundingBox(),contextBox=await page.locator('.audience-context').first().boundingBox();
      assert.ok(scopeBox && contextBox && scopeBox.y<contextBox.y,`${id}: scope must precede explanatory prose`);
      const codes={'cp-000250':'HCBBIOM211','cp-000060':'HCBCOGN312','cp-000033':'BENBUSI112','cp-000440':'BENENTR111','cp-000317':'GOSLAWJ311','cp-000266':'ENSDELT311','cp-000041':'BENBUSI312','cp-000040':'MCCCOMM312','cp-000113':'MCCCOMM311','cp-000397':'BENECON311'};
      const code=codes[id],button=page.locator(`.course-link[data-code="${code}"]`).first();
      if(size==='mobile'){const index=await button.evaluate(b=>Array.from(b.closest('tr').children).indexOf(b.closest('td')));await page.locator('.column-select').selectOption(String(index));await page.waitForTimeout(250);}
      await button.click();await page.locator('.modal.in').waitFor();
      const description=JSON.parse(fs.readFileSync(`pilot/shiny/data/courses/${code.slice(0,3)}.json`)).descriptions[code];
      assert.ok(description && (await page.locator('.modal.in').innerText()).replace(/\s+/g,' ').includes(description.replace(/\s+/g,' ').trim()),`${id}/${code}: wrong selected description`);
      const qualifiedText=await page.locator('.modal.in').innerText();
      modals.push({code,text:qualifiedText});
      await page.waitForTimeout(350);
      await page.screenshot({path:path.join(out,`${variant}-${code}-${size}.png`)});
      await page.locator('.modal.in button',{hasText:'Close'}).click();await page.locator('.modal-backdrop').waitFor({state:'hidden'});

     }
     const evidence = page.locator('.exception-evidence');
     if (current.recordStatus === 'exception' || externalOnly) {
      assert.equal(await evidence.count(), 1);
      const noMatch = current.exception?.type === 'no-defensible-ucr-match' &&
        !(variant === 'fixtures' && id === 'cp-000277');
      const status = noMatch ? 'No sufficiently close UCR comparison' :
        externalOnly ? 'Only the external programme is shown' :
        'Insufficient verified evidence for a reliable comparison';
      assert.equal(await page.locator('.comparison-status').innerText(), status);
      assert.equal(await page.locator('.comparison-head h1').innerText(), displayName);
      assert.equal(await page.locator('.comparison-institution').innerText(), current.comparator.institution);
      assert.ok(await page.getByRole('link', {name: /Official programme source/}).isVisible());
      assert.equal(await page.locator('.compare-view,.qualified-scope,.column-select,.course-link').count(), 0);
      assert.equal(await evidence.evaluate(el => el.open), false);
      assert.ok(!body.includes('About this programme') && !body.includes('External programme components'));
      const table = evidence.locator('.external-table');
      assert.equal(await table.isVisible(), false);

      if (variant === 'actual') {
       const reviewed = current.audience;
       assert.ok(body.includes(`Academic year ${reviewed.curriculum.yearLabel}`));
       if (noMatch) assert.ok(body.includes(reviewed.comparisonExplanation), `${id}: reviewed explanation missing`);
       if (externalOnly) {
        assert.ok(body.includes(reviewed.programmeDescription));
        assert.ok(!body.includes(reviewed.comparisonExplanation), `${id}: withheld comparison surfaced`);
       }
       if (reviewed.curriculum.status === 'partial') {
        assert.ok(body.includes('External curriculum verification is incomplete.'));
       }
       if (reviewed.curriculum.limitation) assert.ok(!body.includes(reviewed.curriculum.limitation), `${id}: verification paragraph visible before expansion`);
      }
      const toggle = evidence.locator('summary');
      await toggle.focus();
      await toggle.press('Enter');
      assert.equal(await evidence.evaluate(el => el.open), true);
      const evidenceText = await evidence.innerText();
      assert.ok(!evidenceText.includes('INTERNAL-SENTINEL'), `${variant}/${id}: research leakage in evidence`);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
      if (variant === 'actual') {
       const reviewed = current.audience;
       if (reviewed.curriculum.limitation) assert.ok(evidenceText.includes(reviewed.curriculum.limitation));
       assert.equal(await table.locator('tbody tr').count(), reviewed.curriculum.componentIds.length);
       if (reviewed.curriculum.status === 'partial') {
        assert.ok(evidenceText.includes('Verified partial curriculum'));
        assert.ok(!evidenceText.includes('Complete external curriculum'));
       }
       if (current.acceptance?.basis === 'robust-no-match') {
        assert.ok(evidenceText.includes(reviewed.comparisonScope.assessed));
        assert.ok((body + evidenceText).includes(reviewed.comparisonScope.excluded));
       }
       if (id === 'cp-000277') {
        assert.ok(body.includes('compulsory second-year 5-EC component remains unnamed'));
        assert.ok(evidenceText.includes('175 EC') && evidenceText.includes('compulsory T.B.A. 5 EC'));
       }
       if (id === 'cp-000263') assert.match(evidenceText, /130 EC.*40\/45 EC/s);
      } else if (id === 'cp-000277') {
       assert.ok(evidenceText.includes('175 EC') && evidenceText.includes('required 5 EC'));
      }
      if (id === 'cp-000277' && variant === 'actual') {
       await page.screenshot({path: path.join(out, `${variant}-${id}-${size}-evidence.png`)});
      }
      await toggle.click();
      assert.equal(await evidence.evaluate(el => el.open), false);
     }
     if (id === 'cp-000119' && variant === 'actual') assert.ok(!body.includes('Philosophy, myth & cultural meaning'));
     if (id === 'cp-000330') assert.ok(!body.includes('Computational systems, robotics & sustainable technology'));
     if(variant==='fixtures'&&id==='cp-000005'){assert.ok(detailsText.includes('other content remains under review'));assert.ok(body.includes('Curriculum details are awaiting review'));}
     if(variant==='fixtures'&&id==='cp-000004')assert.ok(body.includes('specialist subjects or forms of training may differ'));
     if(variant==='actual'&&id==='cp-000035') {
      const currentBiology = JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000035.json', 'utf8'));
      assert.ok(detailsText.includes(currentBiology.audience.comparisonExplanation), 'CP035 reviewed comparison explanation missing');
      for(const [code,expected] of [['ENSECOL111','diversity of living organisms'],['ENSECOL112','human-driven biodiversity loss'],['ENSECOL211','genes to populations']]) {
       const button=page.locator(`.course-link[data-code="${code}"]`).first();
       if(size==='mobile') {const index=await button.evaluate(b=>Array.from(b.closest('tr').children).indexOf(b.closest('td')));await page.locator('.column-select').selectOption(String(index));await page.waitForTimeout(250);}
       await button.click();await page.locator('.modal.in').waitFor();const text=await page.locator('.modal.in').innerText();assert.ok(text.includes(expected));assert.ok(!/Wizard and the Prophet|policy advice/.test(text));modals.push({code,text});
       await page.locator('.modal.in button',{hasText:'Close'}).click();await page.locator('.modal-backdrop').waitFor({state:'hidden'});
      }
     }
     await page.evaluate(()=>window.scrollTo(0,0));await page.screenshot({path:path.join(out,`${variant}-${id}-${size}-top.png`)});
     fs.writeFileSync(path.join(out,`${variant}-${id}-${size}-text.txt`),body);
     await page.locator('#back_to_search').click();await page.locator('#search_text').waitFor();assert.equal(await page.locator('#search_text').inputValue(),query);
     results.push({variant,id,size,viewport,geometry,columns,modals,textFile:`${variant}-${id}-${size}-text.txt`,pageErrors:[...errors]});
    }
    assert.deepEqual(errors,[]);await page.close();
   }
  } finally {server.kill('SIGTERM');fs.closeSync(logfile);}
 }
 fs.writeFileSync(path.join(out,'rendered-results.json'),JSON.stringify({testedOn:new Date().toISOString(),results},null,2)+'\n');
 console.log(`PASS ${results.length} actual rendered case/viewport tests; text and screenshots in ${out}`);
} finally {await browser.close();}
