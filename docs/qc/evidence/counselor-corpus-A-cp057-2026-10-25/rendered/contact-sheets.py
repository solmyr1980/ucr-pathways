from PIL import Image,ImageDraw
from pathlib import Path
import json
b=Path('docs/qc/evidence/counselor-corpus-A-cp057-2026-10-25/rendered');r=json.load(open(b/'results-cp-000057.json'));(b/'results-cp-000057.json').write_text(json.dumps(r,indent=2)+'\n');files=[];items=[]
for rr in r['results']:
 for m in rr['modals']:
  p=b/f'cp-000057-{rr["size"]}-{m["code"]}.png';im=Image.open(p);g=m['geometry'];im=im.crop((max(0,int(g['x'])-4),max(0,int(g['y'])-4),min(im.width,int(g['x']+g['width'])+4),min(im.height,int(g['y']+g['height'])+4)));items.append((rr['size']+' '+m['code'],im))
for q in sorted(b.glob('*-scroll-bottom.png')):
 items.append(('Long-modal bottom '+q.name,Image.open(q)))
for start in range(0,len(items),8):
 sheet=Image.new('RGB',(2400,1760),'#dddddd');dr=ImageDraw.Draw(sheet)
 for i,(label,im) in enumerate(items[start:start+8]):
  im.thumbnail((588,842));sheet.paste(im,((i%4)*600+6,(i//4)*880+30));dr.text(((i%4)*600+6,(i//4)*880+8),label,fill='black')
 p=b/f'modal-sheet-{start//8+1}.jpg';sheet.save(p,quality=88);files.append(p.name)
p=b/'cp-000057-desktop-full-page.png';im=Image.open(p)
for y in range(0,im.height,1500):
 p=b/f'desktop-slice-{y//1500+1}.jpg';im.crop((0,y,im.width,min(im.height,y+1550))).save(p,quality=88);files.append(p.name)
s=json.load(open(b/'supplement-cp-000057.json'))
for start in range(0,len(s['tiles']),8):
 im=Image.new('RGB',(1640,1780),'#dddddd');dr=ImageDraw.Draw(im)
 for i,t in enumerate(s['tiles'][start:start+8]):
  src=Image.open(t['path']);im.paste(src,((i%4)*410+6,(i//4)*890+30));dr.text(((i%4)*410+6,(i//4)*890+8),f'Column{t["column"]}, y{t["y"]:.0f}',fill='black')
 p=b/f'aligned-sheet-{start//8+1}.jpg';im.save(p,quality=88);files.append(p.name)
for name in files:
 with Image.open(b/name) as im:im.verify()
(b/'final-visual-manifest.json').write_text(json.dumps({'sheets':files,'modalOpenings':sum(len(x['modals'])for x in r['results']),'selectedUniqueCourses':len(r['results'][0]['modals']),'modalImagesIncludingBottoms':len(items),'alignedMobileSlices':len(s['tiles']),'excluded':'FullPage mobile captures superseded by aligned ordinary viewport slices.'},indent=2)+'\n');print('Images',len(files),'modalOpenings',len(items),'alignedSlices',len(s['tiles']))
