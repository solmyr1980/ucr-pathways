// Actual local Shiny; no deployment or fixture/corpus mutations.
const fs=require('fs'),path=require('path'),assert=require('assert'),{spawn,execFileSync}=require('child_process');
const {chromium}=require(process.env.UCR_PLAYWRIGHT_MODULE||'playwright');
(async()=>{
 const ids=process.argv.slice(2),out=process.env.UCR_PAIR_RENDERED_EVIDENCE_DIR||'/tmp/ucr-final-pair-rendered';fs.mkdirSync(out,{recursive:true});
 const fd=fs.openSync(out+'/server.log','w'),port=3865,server=spawn(process.env.UCR_RSCRIPT||'Rscript',['scripts/test-counselor-rendered-server.R','actual',String(port)],{stdio:['ignore',fd,fd]});let browser;const results=[];
 try{
  let ready=false;for(let i=0;i<80;i++){try{if((await fetch(`http://127.0.0.1:${port}`)).ok){ready=true;break;}}catch{}await new Promise(r=>setTimeout(r,250));}assert(ready);
  browser=await chromium.launch({headless:true,args:['--no-sandbox']});
  for(const [size,viewport]of [['desktop',{width:1440,height:1000}],['mobile',{width:390,height:844}]]){
   const p=await browser.newPage({viewport}),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.goto(`http://127.0.0.1:${port}`);
   for(const id of ids){
    const r=JSON.parse(fs.readFileSync(`data/counselor/comparisons/${id}.json`)),query=r.programmeProvider.registryName;await p.locator('#search_text').fill(query);await p.locator(`.open-comparison[data-id="${id}"]`).click();await p.locator('.comparison-shell').waitFor();
    const text=await p.locator('.comparison-shell').innerText();
    for(const s of ['awaiting review','INTERNAL-SENTINEL','sourceNotes','cursuscode=','source-first','_x000D_','formal prerequisite','stoppingReason','semantic review'])assert(!text.includes(s),s);
    assert(text.includes(r.audience.programmeDescription)&&text.includes(r.audience.comparisonExplanation));assert(await p.locator(`a[href="${r.comparator.primarySourceUrl}"]`).count()>0);
    await p.evaluate(()=>scrollTo(0,0));await p.screenshot({path:`${out}/${id}-${size}-summary.png`});
    const columns=[],modals=[];let displayedComponents;
    if(['partial','unresolved'].includes(r.audience.curriculum.status)){
     assert(text.includes(r.audience.curriculum.limitation));assert(!text.includes('Complete external curriculum — 180 EC'));assert.equal(await p.locator('.compare-view,.column-select,.course-link').count(),0);
     const verified=r.comparator.components.filter(c=>r.audience.curriculum.componentIds.includes(c.id));displayedComponents=await p.locator('.external-table .cell-text').allTextContents();assert.deepEqual(displayedComponents,verified.map(c=>c.name));
     if(r.audience.curriculum.status==='unresolved'){assert.equal(displayedComponents.length,0);assert(text.includes('withheld from presentation'));}
     await p.locator('.comparison-summary').evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));
    }else if(r.recordStatus==='exception'){
     assert.equal(r.exception.type,'no-defensible-ucr-match');assert(text.includes('cannot construct a sufficiently close programme'));assert.equal(await p.locator('.compare-view,.column-select,.course-link').count(),0);
     displayedComponents=await p.locator('.external-table .cell-text').allTextContents();assert.deepEqual(displayedComponents,r.comparator.components.map(c=>c.name));
     const credits=(await p.locator('.external-table .ec-badge').allTextContents()).map(x=>Number(x.match(/[0-9.]+/)[0]));assert.equal(credits.reduce((a,b)=>a+b,0),180);
     await p.locator('.external-curriculum').evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));
    }else{
     assert(r.programmes.length>=2&&r.programmes.length<=4);if(r.audience.curriculum.limitation)assert(text.includes(r.audience.curriculum.limitation));if(size==='desktop')for(const c of r.comparator.components)assert(text.includes(c.name),'Missing external component '+c.id); for(const concept of r.academicRationale.alternatives)assert(text.includes(concept.concept));
     if(size==='mobile'){
      const opts=await p.locator('.column-select option').allTextContents();assert.equal(opts.length,r.programmes.length);
      for(let i=0;i<opts.length;i++){
       await p.locator('.column-select').selectOption(String(i));await p.waitForTimeout(120);
       const g=await p.locator('.compare-table').evaluate(t=>({cellWidth:t.querySelector('th').getBoundingClientRect().width,overlap:[...t.querySelectorAll('.cell-text,.programme-title')].some(x=>x.scrollWidth>x.clientWidth+1)}));assert(g.cellWidth>=300&&!g.overlap);assert.equal(await p.locator('.column-name').innerText(),opts[i]);columns.push({label:opts[i],...g});if(process.env.UCR_CAPTURE_ALL==='1'){await p.locator('.compare-view').scrollIntoViewIfNeeded();await p.screenshot({path:`${out}/${id}-${size}-column-${i}.png`});}
      }
      await p.locator('.column-select').selectOption('1');await p.waitForTimeout(150);
     }
     await p.locator('.compare-view').evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));
    }
    await p.screenshot({path:`${out}/${id}-${size}-curriculum.png`});
    if(!r.exception&&!['partial','unresolved'].includes(r.audience.curriculum.status)){
     const codes=[...new Set(r.programmes.filter(z=>z.family==='ucr').flatMap(z=>z.schedule.semesters.flatMap(s=>s.courses.map(c=>c.code))))].sort();
     for(const code of codes){
      const btn=p.locator(`.course-link[data-code="${code}"]`).first();
      if(size==='mobile'){const index=await btn.evaluate(b=>[...b.closest('tr').children].indexOf(b.closest('td')));await p.locator('.column-select').selectOption(String(index));await p.waitForTimeout(100);}
      await btn.click();await p.locator('.modal.in').waitFor();await p.waitForTimeout(350);const modalBox=await p.locator('.modal-dialog').boundingBox();assert(modalBox.x>=0&&modalBox.y>=0&&modalBox.x+modalBox.width<=viewport.width+1&&modalBox.y+modalBox.height<=viewport.height+1,'modal exceeds viewport');const t=await p.locator('.modal.in').innerText();assert(!/not currently available|_x000D_/.test(t));
      const cache=JSON.parse(fs.readFileSync(`pilot/shiny/data/courses/${code.slice(0,3)}.json`));// innerText collapses HTML whitespace (GOSHIST311 contains a double space). Preserve every word/punctuation.
      const visibleText=s=>s.replace(/_x000D_/g,'').replace(/\s+/g,' ').trim();assert(visibleText(t).includes(visibleText(cache.descriptions[code])),'Modal description differs: '+code+' '+size);
      if(process.env.UCR_CAPTURE_ALL==='1'||['GOSPHIL214','BENBUSI211','GOSLAWJ211'].includes(code)){await p.screenshot({path:`${out}/${id}-${size}-${code}.png`});}
      if(process.env.UCR_CAPTURE_ALL==='1'){const body=p.locator('.modal.in .modal-body');const overflow=await body.evaluate(e=>e.scrollHeight>e.clientHeight+1);if(overflow){await body.evaluate(e=>e.scrollTop=e.scrollHeight);await p.screenshot({path:`${out}/${id}-${size}-${code}-bottom.png`});}}modals.push({code,text:t,geometry:modalBox});await p.locator('.modal.in button',{hasText:'Close'}).click();await p.locator('.modal-backdrop').waitFor({state:'hidden'});
     }
    }
    const geometry=await p.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth,overlap:[...document.querySelectorAll('.cell-text')].some(x=>x.scrollWidth>x.clientWidth+1)}));assert(geometry.document<=geometry.viewport+1&&!geometry.overlap);
    await p.locator('#back_to_search').click();assert.equal(await p.locator('#search_text').inputValue(),query);assert.deepEqual(errors,[]);
    const git=a=>execFileSync('git',a,{encoding:'utf8'}).trim();results.push({id,size,viewport,presentationMode:r.audience.curriculum.status,deferredGates:['partial','unresolved'].includes(r.audience.curriculum.status)?['Final external curriculum source verification','Included-programme and every-selected-modal inspection after verified curriculum is restored']:[],displayedText:text,columns,displayedComponents,modals,geometry,sourceHref:r.comparator.primarySourceUrl,backNavigation:'passed',pageErrors:errors,inputBlobs:{canonical:git(['hash-object',`data/counselor/comparisons/${id}.json`]),decision:git(['hash-object',`data/counselor/decisions/${id}.json`])}});
   }await p.close();
  }
  fs.writeFileSync(`${out}/results-${ids.join('-')}.json`,JSON.stringify({inputCommit:execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim(),results},null,2)+'\n');console.log('PASS actual desktop/mobile assertions for the applicable presentation; see result for inspected content and deferred gates.');
 }finally{if(browser)await browser.close();server.kill();fs.closeSync(fd);}
})().catch(e=>{console.error(e);process.exit(1)});
