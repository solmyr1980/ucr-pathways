from PIL import Image,ImageOps,ImageDraw
import pathlib,json,math
B=pathlib.Path('docs/qc/evidence/counselor-full-restart-2026-10-27/cp-000238/rendered');O=pathlib.Path('work/cp238');manifest=[]
for v in ['desktop','mobile']:
 r=json.load(open(B/f'results-cp-000238-{v}.json'))['results'][0]
 for start in range(0,len(r['modals']),10):
  ms=r['modals'][start:start+10];cw=660 if v=='desktop'else 390;ch=650 if v=='desktop'else 844;out=Image.new('RGB',(cw*2,(ch+30)*5),'#ddd');dr=ImageDraw.Draw(out)
  for n,m in enumerate(ms):
   f=B/f'cp-000238-{v}-{m["code"]}.png';im=Image.open(f)
   if v=='desktop':
    g=m['geometry'];im=im.crop((max(0,g['x']-25),max(0,g['y']-10),min(im.width,g['x']+g['width']+25),min(im.height,g['y']+ch-10)))
   im.thumbnail((cw,ch));x=n%2*cw;y=n//2*(ch+30);out.paste(im,(x,y+30));dr.text((x+8,y+5),m['code'],fill='black')
  name=O/f'{v}-modals-{start}.jpg';out.save(name,quality=88);manifest.append(str(name))
 for f in sorted(B.glob(f'cp-000238-{v}-*-bottom.png')):
  pass
full=Image.open(B/'frozen-desktop-full.png');W=full.width;H=full.height
# Split full desktop vertically at1000px to see every row legibly.
for n,y in enumerate(range(0,H,1000)):
 f=O/f'desktop-curriculum-{n}.jpg';full.crop((0,y,W,min(H,y+1000))).save(f,quality=90);manifest.append(str(f))
t=json.load(open(B/'tiles.json'))
for col in range(4):
 ts=[x for x in t['tiles']if int(x['select'])==col];out=Image.new('RGB',(390*4,844*2),'white')
 for n,x in enumerate(ts):out.paste(Image.open(x['path']),(n%4*390,n//4*844))
 f=O/f'mobile-curriculum-{col}.jpg';out.save(f,quality=90);manifest.append(str(f))
# Overflow modal bottom captures not represented in main modal sheets.
fs=sorted(B.glob('*-bottom.png'))
for start in range(0,len(fs),8):
 group=fs[start:start+8];out=Image.new('RGB',(390*4,844*2),'#ddd');dr=ImageDraw.Draw(out)
 for n,p in enumerate(group):
  im=Image.open(p);im.thumbnail((390,814));x=n%4*390;y=n//4*844;out.paste(im,(x,y+30));dr.text((x+4,y+5),p.name[10:-4],fill='black')
 f=O/f'overflow-{start}.jpg';out.save(f,quality=88);manifest.append(str(f))
(O/'visual-manifest.json').write_text(json.dumps(manifest));print('visuals',len(manifest),'screens',len(list(B.glob('*.png'))),'fullsize',full.size,'overflow',len(fs))
