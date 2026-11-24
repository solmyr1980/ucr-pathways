// End-to-end checks against real Shiny output, plus isolated runtime-only fixtures.
import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
import {isUcrProgramme, normalizeCell, UCR_DEFAULT_COURSE_EC} from './example-utils.mjs';
const require = createRequire(import.meta.url);
const {chromium} = require(process.env.UCR_PLAYWRIGHT_MODULE || 'playwright');
const out = path.resolve(process.env.UCR_RENDERED_EVIDENCE_DIR || '/tmp/ucr-counselor-shared-rendered');
fs.mkdirSync(out, {recursive:true});
const results=[];
const settings = JSON.parse(fs.readFileSync('data/counselor/presentation-overrides.json')).cases;
const cases = {
  actual: [['cp-000030','American Studies'],['cp-000388','Cultural Anthropology'],['cp-000441','Biology'],['cp-000150','Business Administration'],['cp-000373','UCR Liberal Arts'],['cp-000410','Artificial Intelligence'],['cp-000377','Actuarial Science'],['cp-000003','Pedagogical'],['cp-000001','Public Administration'],['cp-000002','International Social Challenges'],['cp-000043','English Language and Culture'],['cp-000097','Medicine'],['cp-000269','Psychology & Technology'],['cp-000019','Arts and Culture'],['cp-000035','Biology'],['cp-000330','Mechanical Engineering'],['cp-000119','Theology'],['cp-000428','Religious Studies'],['cp-000277','African Studies'],['cp-000311','Notarial Law'],['cp-000013','Philosophy of a Specific Discipline'],['cp-000227','Public Governance']],
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
    if (variant === 'actual' && size === 'desktop') {
     await page.locator('#search_text').fill('Actuarial Science');
     const selector = page.locator('#language + .selectize-control');
     for (const [value,label] of [['ENG','English'], ['NLD','Dutch'], ['All','All']]) {
      await selector.locator('.selectize-input').click();
      await selector.locator(`.option[data-value="${value}"]`).filter({hasText:label}).click();
      await page.locator('.open-comparison[data-id="cp-000377"]').waitFor();
     }
    }
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
      const unexpected = page.locator('.comparison-cell > :not(.cell-text):not(.ec-badge), .cell-note');
      assert.equal(await unexpected.count(), 0, `${id}: unexpected course commentary`);
      if (variant === 'actual') {
       const record = JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`));
       const qualified = record.acceptance?.basis === 'qualified-comparison';
       assert.equal(await page.locator('.comparison-intro').count(),1);
       assert.equal(await page.locator('.comparison-intro a[href="#scope-boundary"]').count(),qualified ? 1 : 0);
       assert.equal(await page.locator('.comparison-shell details').count(),qualified ? 1 : 0);
       assert.equal(await page.locator('.programme-source[href="https://ucr.nl/education/courses/"]').count(),record.programmes.length-1);
       const paragraph = settings[id]?.introduction;
       const total = record.comparator.components.reduce((sum,c) => sum+c.credits, 0);
       const introText = await page.locator('.comparison-intro').innerText();
       if (paragraph) assert.ok(introText.includes(paragraph.replace('{credits}', `${total} of 180 EC`)));
       else assert.match(introText, /first UCR column shows the closest feasible option/);
       const expected = record.blocks.flatMap(block => block.rows.map(row => record.programmes.map(programme => {
        const cell = normalizeCell(row.cells[programme.id]);
        if (!cell) return null;
        const isUcr = isUcrProgramme(programme);
        const ec = cell.credits ?? (isUcr ? UCR_DEFAULT_COURSE_EC : null);
        const credit = cell.comparisonElementId === 'optional-independent-research' ? `${ec} EC outside the scheduled 180 EC` : ec == null ? '' : `${ec} EC`;
        return [cell.text, credit, isUcr ? cell.courseCode || '' : ''];
       })));
       const displayed = await page.locator('.compare-view tbody tr:not(.block-row)').evaluateAll(rows =>
        rows.map(row => Array.from(row.cells, cell => cell.classList.contains('empty-cell') ? null : [
         cell.querySelector('.cell-text').textContent.trim(),
         cell.querySelector('.ec-badge')?.textContent || '',
         cell.querySelector('.course-link')?.dataset.code || ''
        ])));
       for (let i = 1; i < record.programmes.length; i++) {
        assert.equal(displayed.filter(row => row[i]?.[1] === '15 EC outside the scheduled 180 EC').length, 1);
       }
       const signatures = rows => rows.map(row => JSON.stringify(row)).sort();
       assert.deepEqual(signatures(displayed), signatures(expected), `${id}: course rows, blanks, credits or links changed`);
      }
      assert.ok(!body.includes('What this comparison shows'));
      assert.equal(await page.locator('.summary-card,.comparison-summary,.comparison-legend').count(), 0);
      const intro = await page.locator('.comparison-intro').innerText();
      assert.match(intro, /blank cell/i);
      assert.equal(intro.split('Courses in the same row cover related material without necessarily being equivalent.').length, 2);
      assert.ok(intro.split(/\s+/).length <= 90);
      assert.equal(await page.locator('.comparison-head p:not(.comparison-institution)').count(),1);
      const layout = await page.locator('.comparison-shell').evaluate(el => ({
       sections: Array.from(el.children, child => child.classList[0]),
       tableTop: el.querySelector('.compare-table').getBoundingClientRect().top,
       firstCourseTop: el.querySelector('tbody tr:not(.block-row)').getBoundingClientRect().top,
       scroll: window.scrollY
      }));
      const hasScope = await page.locator('.qualified-scope').count();
      assert.deepEqual(layout.sections, ['comparison-toolbar','comparison-head',
       'compare-view',...(hasScope ? ['comparison-details'] : []),'cta-row']);
      assert.equal(layout.scroll, 0, `${id}: opening from search must start at the title`);
      assert.ok(layout.tableTop < viewport.height, `${id}: table below the fold (${layout.tableTop}px)`);
      if (size==='desktop')
       assert.ok(layout.firstCourseTop < viewport.height, `${id}: first course below the fold (${layout.firstCourseTop}px)`);
      assert.ok(await page.locator('.cta-row a[href="https://program.ucr.nl/"]').count());
     }
     const details = page.locator('.comparison-details details');
     const texts = [];
     for (const disclosure of await details.all()) {
      assert.equal(await disclosure.evaluate(el => el.open), false);
      assert.ok(await disclosure.evaluate(el => Boolean(document.querySelector('.compare-view')
       .compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)));
      await disclosure.locator('summary').click();
      assert.equal(await disclosure.evaluate(el => el.open), true);
      texts.push(await disclosure.innerText());
      await disclosure.locator('summary').click();
     }
     const detailsText = texts.join('\n');
     assert.ok(!detailsText.includes('INTERNAL-SENTINEL'), `${variant}/${id}: research leakage in details`);
     if (texts.length) {
      assert.equal(texts.length, 1);
      assert.match(detailsText, /Outside the assessed scope/);
     }
     if (id==='cp-000377') {
      assert.match(await page.locator('.comparison-intro').innerText(), /insurance and pensions sequence/);
      assert.equal(texts.length, 0);
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
      assert.ok(await page.locator('#comparison-overview').evaluate(el=>Math.abs(el.getBoundingClientRect().top)<2));
     }
     const modals=[];
     if(variant==='fixtures' && id==='cp-000019') {
      assert.ok(body.includes('full external pathway remains unverified') && body.includes('of 180 EC') && detailsText.includes('Outside the assessed scope'));
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
      const scope = current.audience.comparisonScope;
      const total = current.comparator.components.reduce((sum,c) => sum+c.credits, 0);
      const banner = page.locator('.qualified-scope');
      assert.ok((await banner.innerText()).includes(`${total} of 180 EC`));
      assert.ok(!(await banner.innerText()).includes(scope.excluded));
      await banner.getByRole('link').click();
      const boundary = page.locator('#scope-boundary');
      assert.ok(await boundary.isVisible());
      const scopeText = await boundary.innerText();
      assert.ok(scopeText.includes(scope.assessed) && scopeText.includes(scope.excluded));
      assert.ok(await page.locator('.course-link').count()>0);
      if(id==='cp-000317') assert.ok(scopeText.includes('final 30 EC') && total===150);
      if(id==='cp-000040') {
       assert.equal(current.acceptance.scope,'academic-core');
       assert.equal(total,165);
       assert.ok(scopeText.includes('15 EC') && scopeText.includes('restricted Arts minor'));
      }
      if(id==='cp-000113') {assert.equal(current.acceptance.scope,'academic-core');assert.equal(current.programmes.length,3);assert.ok(total===150&&/final\s+30\s+EC/.test(scopeText));}
      if(id==='cp-000397') {assert.equal(current.acceptance.scope,'documented-curriculum');assert.ok(total===177&&/3\s+EC/.test(scopeText));}
      if(id==='cp-000266') assert.equal(current.programmes.length,3,'Two independently reviewed UCR options must be present');
      await boundary.locator('..').locator('summary').click();
      const codes={'cp-000250':'HCBBIOM211','cp-000060':'HCBCOGN312','cp-000033':'BENBUSI112','cp-000440':'BENENTR111','cp-000317':'GOSLAWJ311','cp-000266':'ENSDELT311','cp-000041':'BENBUSI312','cp-000040':'MCCCOMM312','cp-000113':'MCCCOMM311','cp-000397':'BENECON311'};
      const code=codes[id] ?? current.programmes[1].schedule.semesters[0].courses[0].code,button=page.locator(`.course-link[data-code="${code}"]`).first();
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
     if (current.recordStatus === 'exception' || externalOnly) {
      const noMatch = current.exception?.type === 'no-defensible-ucr-match' &&
        !(variant === 'fixtures' && id === 'cp-000277');
      const status = noMatch ? 'No sufficiently close UCR comparison' :
        externalOnly ? 'Only the external programme is shown' :
        current.exception?.type === 'registry-exception' ? 'Programme details need verification' :
        'Insufficient verified evidence for a reliable comparison';
      assert.equal(await page.locator('.comparison-status').innerText(), status);
      assert.equal(await page.locator('.comparison-head h1').innerText(), displayName);
      assert.equal(await page.locator('.comparison-institution').innerText(), current.comparator.institution);
      assert.ok(await page.getByRole('link', {name: /Official programme source/}).isVisible());
      assert.equal(await page.locator('.comparison-shell details,.compare-view,.qualified-scope,.column-select,.course-link').count(), 0);
      assert.doesNotMatch(body, /Assessed scope|Outside the assessed scope|External programme components/);

      if (variant === 'actual') {
       const reviewed = current.audience;
       assert.ok(body.includes(`Academic year ${reviewed.curriculum.yearLabel}`));
       assert.equal(await page.locator('.exception-description').innerText(), reviewed.programmeDescription);
       if (externalOnly) assert.ok(!body.includes(reviewed.comparisonExplanation), `${id}: comparison prose surfaced`);
       else assert.equal(await page.locator('.exception-explanation').innerText(), reviewed.comparisonExplanation);
       const opening = await page.locator('.exception-summary > p').allTextContents();
       assert.equal(opening.length, current.acceptance?.basis === 'robust-no-match' ? 2 : 1);
       assert.equal(opening[0].trim().replace(/\s+/g,' '), externalOnly ? reviewed.programmeDescription :
        reviewed.programmeDescription + ' ' + reviewed.comparisonExplanation);
       const selected = current.comparator.components.filter(component => reviewed.curriculum.componentIds.includes(component.id));
       const table = page.locator('.external-table');
       assert.equal(await table.count(), selected.length ? 1 : 0);
       if (selected.length) {
        assert.ok(await table.isVisible());
        assert.equal(await page.locator('.external-curriculum h2').innerText(),
          reviewed.curriculum.status === 'complete' ? 'Complete external curriculum' : 'Verified partial curriculum');
        const rows = await table.locator('tbody tr').evaluateAll(rows =>
          rows.map(row => Array.from(row.cells, cell => cell.textContent)));
        assert.deepEqual(rows, selected.map(component => [component.name, `${component.credits} EC`]));
        assert.ok(await table.evaluate(node => node.scrollWidth <= node.parentElement.clientWidth + 1));
       }
       if (reviewed.curriculum.limitation) assert.ok(!body.includes(reviewed.curriculum.limitation));
       if (current.acceptance?.basis === 'robust-no-match') {
        assert.ok(body.includes('Some external requirements remain unverified. The conclusion rests on the established academic core.'));
        assert.ok(!body.includes(reviewed.comparisonScope.assessed));
        assert.ok(!body.includes(reviewed.comparisonScope.excluded));
       }
       assert.doesNotMatch(await page.locator('.exception-summary').innerText(),
         /\b\d+(?:[.-]\d+)?[ -]EC\b|(?:table|components) (?:shown|below)/i);
      } else if (id === 'cp-000277') {
       assert.ok(body.includes('while a required component remains unidentified'));
       assert.ok(!body.includes('175 EC'));
       assert.ok(await page.locator('.external-table').isVisible());
      }
     }
     if (id === 'cp-000119' && variant === 'actual') assert.ok(!body.includes('Philosophy, myth & cultural meaning'));
     if (id === 'cp-000330') assert.ok(!body.includes('Computational systems, robotics & sustainable technology'));
     if(variant==='fixtures' && id==='cp-000005') {
      assert.equal(texts.length,0);
      assert.ok(!body.includes('other content remains under review'));
     }
     if(variant==='fixtures' && id==='cp-000004') assert.match(body, /specialist subjects or training/);
     if(variant==='actual' && id==='cp-000097') assert.match(body, /supervised contact and placements/);
     if(variant==='actual' && id==='cp-000035') {
      assert.match(body, /research internship/);
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
