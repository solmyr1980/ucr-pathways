// Actual local Shiny verification; no deployment or corpus mutations.
const fs=require('fs'),path=require('path'),assert=require('assert'),{spawn,execFileSync}=require('child_process');
const {chromium}=require(process.env.UCR_PLAYWRIGHT_MODULE||'playwright');
(async()=>{const out=process.env.UCR_ADJUDICATION_EVIDENCE_DIR||'/tmp/ucr-cp119-adjudication-rendered';fs.mkdirSync(out,{recursive:true});const fd=fs.openSync(path.join(out,'server.log'),'w'),port=3864;
 const server=spawn(process.env.UCR_RSCRIPT||'Rscript',['scripts/test-counselor-rendered-server.R','actual',String(port)],{stdio:['ignore',fd,fd]});let browser;const results=[];
 try{let ready=false;for(let i=0;i<80;i++){try{if((await fetch(`http://127.0.0.1:${port}`)).ok){ready=true;break;}}catch{}await new Promise(r=>setTimeout(r,250));}assert(ready,'Actual Shiny server failed to start');browser=await chromium.launch({headless:true,args:['--no-sandbox']});
  const r=JSON.parse(fs.readFileSync('data/counselor/comparisons/cp-000119.json'));assert.equal(r.exception.type,'no-defensible-ucr-match');
  for(const [size,viewport]of [['desktop',{width:1440,height:1000}],['mobile',{width:390,height:844}]]){
   const p=await browser.newPage({viewport}),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.goto(`http://127.0.0.1:${port}`);await p.locator('#search_text').fill('Theology');await p.locator('.open-comparison[data-id="cp-000119"]').click();await p.locator('.comparison-shell').waitFor();const text=await p.locator('.comparison-shell').innerText();
   assert(text.includes('cannot construct a sufficiently close programme'));assert(text.includes('religious traditions, sacred texts and lived religion'));assert(text.includes('Complete external curriculum — 180 EC'));
   for(const forbidden of ['Philosophy, myth & cultural meaning','withheld from presentation','awaiting review','INTERNAL-SENTINEL','G_BATRS','_x000D_','23 non-PPD','course-by-course challenge'])assert(!text.includes(forbidden),forbidden);
   assert.equal(await p.locator('.compare-view,.column-select,.course-link').count(),0);assert.equal(await p.locator('.external-table tbody tr').count(),26);
   const cells=await p.locator('.external-table .cell-text').allTextContents();assert.deepEqual(cells,r.comparator.components.map(c=>c.name));const credits=(await p.locator('.external-table .ec-badge').allTextContents()).map(x=>Number(x.match(/[0-9.]+/)[0]));assert.equal(credits.reduce((a,b)=>a+b,0),180);
   assert(await p.locator(`a[href="${r.comparator.primarySourceUrl}"]`).count()>0);
   const geometry=await p.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth,overlap:[...document.querySelectorAll('.cell-text')].some(x=>x.scrollWidth>x.clientWidth+1)}));assert(geometry.document<=geometry.viewport+1&&!geometry.overlap);
   await p.evaluate(()=>scrollTo(0,0));await p.screenshot({path:path.join(out,`cp-000119-${size}-summary.png`)});await p.locator('.external-curriculum').evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY));await p.screenshot({path:path.join(out,`cp-000119-${size}-curriculum.png`)});
   await p.locator('#back_to_search').click();assert.equal(await p.locator('#search_text').inputValue(),'Theology');assert.deepEqual(errors,[]);results.push({size,viewport,displayedText:text,geometry,externalComponents:26,externalCredits:180,ucrControls:0,sourceHref:r.comparator.primarySourceUrl,backNavigation:'passed',pageErrors:errors});await p.close();
  }
  const git=args=>execFileSync('git',args,{encoding:'utf8'}).trim();fs.writeFileSync(path.join(out,'rendered-results.json'),JSON.stringify({inputCommit:git(['rev-parse','HEAD']),inputBlobs:{canonical:git(['hash-object','data/counselor/comparisons/cp-000119.json']),decision:git(['hash-object','data/counselor/decisions/cp-000119.json'])},results},null,2)+'\n');console.log('PASS: actual desktop/mobile no-match,26 components/180 EC, no UCR comparison or internal research, source href, navigation and readable layout.');
 }finally{if(browser)await browser.close();server.kill();fs.closeSync(fd);}
})().catch(e=>{console.error(e);process.exit(1)});
