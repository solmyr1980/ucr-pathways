from PIL import Image,ImageDraw
from pathlib import Path
import json,hashlib
b=Path('docs/qc/evidence/counselor-corpus-A-cp061-2026-10-25/rendered');s=json.load(open(b/'supplement-cp-000061.json'));files=[]
im=Image.open(b/'cp-000061-desktop-full-page.png')
for y in range(0,max(1,im.height-80),1400):
 p=b/f'desktop-sheet-{y//1400+1}.jpg';im.crop((0,y,im.width,min(im.height,y+1450))).save(p,quality=90);files.append(p.name)
ms=next(r for r in s['results']if r['size']=='mobile')['tiles']
for start in range(0,len(ms),8):
 sheet=Image.new('RGB',(1640,1760),'#dddddd');draw=ImageDraw.Draw(sheet)
 for i,p in enumerate(ms[start:start+8]):
  im=Image.open(p);sheet.paste(im,((i%4)*410+8,(i//4)*880+30));draw.text(((i%4)*410+8,(i//4)*880+8),f'Mobile slice {start+i+1}',fill='black')
 p=b/f'mobile-sheet-{start//8+1}.jpg';sheet.save(p,quality=90);files.append(p.name)
(b/'visual-manifest.json').write_text(json.dumps({'caseId':'cp-000061','inputCommit':'e069e3d0730d8f9076a082e9a15e4e3a1ea4424b','sheets':[{'path':str(b/f),'sha256':hashlib.sha256((b/f).read_bytes()).hexdigest()}for f in files],'desktopFullPage':True,'ordinaryViewportSlices':{r['size']:len(r['tiles'])for r in s['results']},'selectedUCRAlternatives':0,'selectedCourseModals':0,'scope':'Complete180ECexternal no-match curriculum only; no invented UCR schedules.','visuallyInspected':False},indent=2)+'\n');print(files)
