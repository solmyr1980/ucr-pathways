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
  actual: [['cp-000003','Pedagogical'],['cp-000001','Public Administration'],['cp-000019','Arts and Culture'],['cp-000035','Biology'],['cp-000330','Mechanical Engineering'],['cp-000119','Theology'],['cp-000428','Religious Studies'],['cp-000277','African Studies']],
  fixtures: [['cp-000004','Psychology'],['cp-000002','Management of International'],['cp-000005','Psychology'],['cp-000119','Theology'],['cp-000428','Religious Studies'],['cp-000277','African Studies'],['cp-000019','Arts and Culture'],['cp-000003','Pedagogical']]
};
// Stage 1 representatives use actual canonical data, including still-unresolved controls.
for (const [id,query] of [['cp-000250','Clinical Technology'],['cp-000060','Dutch Language'],['cp-000033','Business Administration'],['cp-000396','Tax Law'],['cp-000440','Business and Consumer'],['cp-000317','Law'],['cp-000099','Health and Life'],['cp-000072','Spanish Language'],['cp-000266','Industrial Design']]) {
 const r=JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`));
 if(r.acceptance || ['cp-000099','cp-000072'].includes(id)) cases.actual.push([id,query]);
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
     const open=page.locator(`.open-comparison[data-id="${id}"]`);await open.waitFor({timeout:20000});await open.click();
     await page.locator('.comparison-shell').waitFor();
     const body=await page.locator('.comparison-shell').innerText();
     assert.ok(!body.includes('INTERNAL-SENTINEL'),`${variant}/${id}: research leakage`);
     assert.ok(!body.includes('First-listed Culture and Economics'),`${id}: cell bookkeeping exposed`);
     assert.ok(!body.includes('2261'),`${id}: catalogue code exposed`);
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
     if(variant==='actual' && current.acceptance?.basis==='qualified-comparison') {
      assert.equal(await page.locator('.compare-view').count(),1);
      assert.ok(body.includes(current.audience.comparisonScope.label) && body.includes(current.audience.comparisonScope.excluded));
      assert.ok(body.includes('Nominal external degree: 180 EC') && body.includes('Unknown requirements are not open electives'));
      assert.equal(await page.locator('.course-link').count()>0,true);
      if(id==='cp-000317') assert.ok(body.includes('final 30 EC') && body.includes('150 EC'));
      if(id==='cp-000266') assert.equal(current.programmes.length,3,'Two independently reviewed UCR options must be present');
      const scopeBox=await page.locator('.qualified-scope').boundingBox(),contextBox=await page.locator('.audience-context').first().boundingBox();
      assert.ok(scopeBox && contextBox && scopeBox.y<contextBox.y,`${id}: scope must precede explanatory prose`);
      const codes={'cp-000250':'HCBBIOM211','cp-000060':'HCBCOGN312','cp-000033':'BENBUSI112','cp-000440':'BENENTR111','cp-000317':'GOSLAWJ311','cp-000266':'ENSDELT311'};
      const code=codes[id],button=page.locator(`.course-link[data-code="${code}"]`).first();
      if(size==='mobile'){const index=await button.evaluate(b=>Array.from(b.closest('tr').children).indexOf(b.closest('td')));await page.locator('.column-select').selectOption(String(index));await page.waitForTimeout(250);}
      await button.click();await page.locator('.modal.in').waitFor();
      const description=JSON.parse(fs.readFileSync(`pilot/shiny/data/courses/${code.slice(0,3)}.json`)).descriptions[code];
      assert.ok(description && (await page.locator('.modal.in').innerText()).replace(/\s+/g,' ').includes(description.replace(/\s+/g,' ').trim()),`${id}/${code}: wrong selected description`);
      await page.locator('.modal.in button',{hasText:'Close'}).click();await page.locator('.modal-backdrop').waitFor({state:'hidden'});

     }
     if(variant==='actual' && ['cp-000099','cp-000072'].includes(id)) assert.equal(await page.locator('.compare-view').count(),0);
     if(variant==='actual' && current.acceptance?.basis==='robust-no-match') {assert.equal(await page.locator('.compare-view').count(),0);assert.ok(body.includes('cannot construct a sufficiently close programme') && body.includes(current.audience.comparisonScope.excluded));}
     if(id==='cp-000277' && (variant==='fixtures' || current.exception?.type==='external-programme-unresolved')) {
      assert.ok(body.includes('no complete degree pathway is certified'));
      if(variant==='actual' && !JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`)).audience?.curriculum) assert.equal(await page.locator('.external-curriculum').count(),0);
      else {assert.ok(body.includes('175 EC')&&body.includes('required 5 EC'));assert.ok(body.includes('Verified partial curriculum'));}
     }
     if(id==='cp-000428')assert.ok(body.includes('cannot construct a sufficiently close programme'));
     if(id==='cp-000119' && variant==='actual') {
      assert.ok(body.includes('cannot construct a sufficiently close programme'));
      assert.ok(body.includes('Complete external curriculum') && body.includes(current.audience.programmeDescription));
      assert.ok(!body.includes('Philosophy, myth & cultural meaning'));
      assert.equal(await page.locator('.compare-view,.column-select,.course-link').count(),0);
      assert.equal(await page.locator('.external-table tbody tr').count(),current.audience.curriculum.componentIds.length);
     }
     if(variant==='fixtures'&&id==='cp-000002'){assert.ok(body.includes('withheld from presentation'));assert.equal(await page.locator('.compare-view').count(),0);assert.ok(body.includes('Complete external curriculum'));}
     if(variant==='fixtures'&&id==='cp-000005'){assert.ok(body.includes('other content remains under review'));assert.ok(body.includes('Curriculum details are awaiting review'));}
     if(id==='cp-000330') {
      assert.ok(body.includes('cannot construct a sufficiently close programme'));
      assert.ok(body.includes(current.audience.comparisonExplanation) && body.includes('Complete external curriculum'));
      assert.ok(!body.includes('withheld from presentation') && !body.includes('Computational systems, robotics & sustainable technology'));
      assert.equal(await page.locator('.compare-view,.column-select,.course-link').count(),0);
      assert.equal(await page.locator('.external-table tbody tr').count(),current.audience.curriculum.componentIds.length);
     }
     if(variant==='fixtures'&&id==='cp-000004')assert.ok(body.includes('specialist subjects or forms of training may differ'));
     if(id==='cp-000003') {assert.ok(body.includes('cannot construct a sufficiently close programme') && body.includes('Complete external curriculum'));assert.equal(await page.locator('.compare-view,.column-select,.course-link').count(),0);assert.equal(await page.locator('.external-table tbody tr').count(),current.audience.curriculum.componentIds.length);}
     if(variant==='actual'&&id==='cp-000035') {
      const currentBiology = JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000035.json', 'utf8'));
      assert.ok(body.includes(currentBiology.audience.comparisonExplanation), 'CP035 reviewed comparison explanation missing');
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
