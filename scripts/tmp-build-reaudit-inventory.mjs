import fs from 'node:fs';
import path from 'node:path';
const root=process.cwd();
const out=[];
for(let i=1;i<=4;i++){
  const id=`cp-${String(i).padStart(6,'0')}`;
  const p=path.join(root,'data','counselor','comparisons',`${id}.json`);
  const r=JSON.parse(fs.readFileSync(p,'utf8'));
  const compById=new Map((r.comparator?.components||[]).map(c=>[c.id,c]));
  const unmatched=(r.comparisonAlignment||[]).filter(a=>a.matchType==='unmatched').map(a=>({componentId:a.componentId,name:compById.get(a.componentId)?.name,credits:compById.get(a.componentId)?.credits,rationale:a.rationale}));
  const rows=[];
  for(const block of r.blocks||[]){
    for(const row of block.rows||[]){
      const ucr=Object.entries(row.cells||{}).filter(([k])=>k!=='comparator').map(([programme,cell])=>({programme,courseCode:cell.courseCode,name:cell.text}));
      if(ucr.length){ rows.push({block:block.id,blockTitle:block.title,ucr,comparator:row.cells?.comparator?{componentId:row.cells.comparator.componentId,name:row.cells.comparator.text}:null}); }
    }
  }
  out.push({id,programme:r.comparator?.name,unmatched,ucrRows:rows});
}
fs.writeFileSync(path.join(root,'data','counselor','tmp-reaudit-inventory.json'),JSON.stringify(out,null,2)+'\n');
