from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
b=Path('docs/qc/evidence/counselor-corpus-A-cp055-2026-10-25/execution-2/rendered');files=[]
for size,width,height,columns,per in [('desktop',1000,695,1,2),('mobile',390,844,4,8)]:
 tiles=sorted(b.glob(size+'-slice-*.png'),key=lambda p:int(p.stem.split('-')[-1]));rows=(per+columns-1)//columns
 for st in range(0,len(tiles),per):
  sheet=Image.new('RGB',((width+20)*columns,(height+35)*rows),'#ddd');draw=ImageDraw.Draw(sheet)
  for i,p in enumerate(tiles[st:st+per]):
   im=Image.open(p);im.thumbnail((width,height));x=(i%columns)*(width+20)+10;y=(i//columns)*(height+35)+25;sheet.paste(im,(x,y));draw.text((x,y-18),f'{size} slice {st+i+1}',fill='black')
  p=b/f'{size}-sheet-{st//per+1}.jpg';sheet.save(p,quality=92)
