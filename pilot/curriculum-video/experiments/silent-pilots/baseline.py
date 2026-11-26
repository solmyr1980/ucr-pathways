from pathlib import Path
from functools import lru_cache
import os
import json, math, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageColor
from openpyxl import load_workbook
from lxml import etree
import cairosvg

ROOT=Path(__file__).resolve().parent
A=Path(os.environ.get('UCR_SILENT_PILOT_ASSETS', ROOT/'assets')).expanduser().resolve()
if not (A/'record.json').is_file():
    raise SystemExit(f'Extract the silent-pilot assets and set UCR_SILENT_PILOT_ASSETS. Checked {A}')
WIDTH,HEIGHT,FPS=1920,1080,24
PLUM='#491e34'
PAPER=(248,243,236)
INK='#302c2d'
MUTED='#5c5757'
LINE='#d8cdc4'
RED='#99323c'
OCHRE='#77532b'
def frame(name):
    return Image.open(A/(name+'.png')).convert('RGB')
def smooth(value):
    value=max(0,min(1,value))
    return value*value*(3-2*value)
def fade(a,b,value):
    if value<=0:return a
    if value>=1:return b
    return Image.blend(a,b,value)
def interp_box(a,b,t):
    return tuple(round(x+(y-x)*t) for x,y in zip(a,b))
def size(box):
    return box[2]-box[0],box[3]-box[1]
@lru_cache(None)
def font(n,family):
    return ImageFont.truetype(str(A/{'serif':'Ivy.otf','body':'Inter.ttf','bold':'InterBold.ttf'}[family]),n)
def text(im,point,words,n,style='body',fill=INK):
    ImageDraw.Draw(im).text(point,words,font=font(n,style),fill=fill,anchor='lt')
def wrap(words,f,width):
    out=[]
    for word in words.split():
        if not out or f.getlength(out[-1]+' '+word)>width:out.append(word)
        else:out[-1]+=' '+word
    return out

record=json.loads((A/'record.json').read_text())
programme=next(p for p in record['programmes'] if p['id']=='ucr-depth')
semesters=programme['schedule']['semesters']
book=load_workbook(A/'courses.xlsx',read_only=True)
rows=iter(book.active.values); headers=next(rows)
catalog=list(rows)
courses={r[headers.index('osiris')]:r[headers.index('name')] for r in catalog}
cluster_names={r[headers.index('dep')]:r[headers.index('deplabel')] for r in catalog
               if r[headers.index('dep')] != 'ACC'}
book.close()
codes=[c['code'] for semester in semesters for c in semester['courses']]
assert len(semesters)==6 and all(len(s['courses'])==4 for s in semesters) and len(set(codes))==24
plan=frame('plan')
base=Image.new('RGB',(WIDTH,HEIGHT),PAPER)
base.paste(plan.crop((0,0,WIDTH,106)),(0,0))
# The section label in the master belongs only to the completed plan.
ImageDraw.Draw(base).rectangle((298,22,780,80),fill=PAPER)
plan_tiles={}
tile_boxes={}
empty=plan.copy()
empty_draw=ImageDraw.Draw(empty)
blank_plan=plan.copy()
blank_draw=ImageDraw.Draw(blank_plan)
for idx,code in enumerate(codes):
    s,r=divmod(idx,4)
    width=(1868-52-32)//3
    x=52+(s%3)*(width+16); y=186+(s//3)*358+45+r*72
    box=(x+12,y,x+width-11,y+71)
    tile_boxes[code]=box
    plan_tiles[code]=plan.crop(box)
    empty_draw.rectangle((box[0]-1,box[1]-1,box[2],box[3]),fill='white')
    empty_draw.rounded_rectangle((box[0],box[1],box[2]-1,box[3]-1),radius=6,fill='#f4f1ed')
empty_draw.rectangle((1740,117,1880,167),fill=PAPER)

# Use the official SVG geometry. Cairo preserves positions and the original course codes.
MW=1170
MH=round(MW*676.8/1152)
MX=688; MY=262
def render_map(width,height):
    rgba=Image.open(__import__('io').BytesIO(cairosvg.svg2png(url=str(A/'map.svg'),output_width=width,output_height=height))).convert('RGBA')
    rgb=Image.new('RGB',(width,height),'white')
    rgb.paste(rgba,mask=rgba.getchannel('A'))
    return ImageChops.multiply(rgb,Image.new('RGB',rgb.size,PAPER))
map_rgb=render_map(MW,MH)
map_doc=etree.parse(str(A/'map.svg'))
map_boxes={}
for code in codes:
    hits=map_doc.xpath('//*[@data-id=$code and @width]',code=code)
    assert len(hits)==1
    hit=hits[0]
    assert not any(n.get('transform') for n in hit.iterancestors())
    x,y,w,h=map(float,(hit.get(k) for k in ('x','y','width','height')))
    map_boxes[code]=(round(x*MW/1152)+MX-1,round(y*MH/676.8)+MY-1,
                     round((x+w)*MW/1152)+MX+1,round((y+h)*MH/676.8)+MY+1)

hook=base.copy()
mini=render_map(1418,833).resize((805,473),Image.Resampling.LANCZOS)
hook.paste(mini,(1045,314))
text(hook,(78,205),'A student gave us three interests.',43,'bold',PLUM)
interest=record['interests']
quote_lines=['“Economics, politics,','and why some countries','become rich while','others stay poor”']
assert ' '.join(quote_lines).strip('“”')==interest
for i,line in enumerate(quote_lines):
    assert font(81,'serif').getlength(line)<945
    text(hook,(75,343+i*105),line,81,'serif',PLUM)

unlit=base.copy()
text(unlit,(56,129),'Here’s the degree we built around them.',63,'serif',PLUM)
unlit.paste(map_rgb,(MX,MY))
selected=unlit.copy()
selected.paste(fade(map_rgb,Image.new('RGB',map_rgb.size,PAPER),.80),(MX,MY))
text(selected,(1530,155),'24 selected courses',28,'bold',PLUM)
map_fragments={}
for code,b in map_boxes.items():
    tile=unlit.crop(b)
    ImageDraw.Draw(tile).rectangle((0,0,tile.width-1,tile.height-1),outline=PLUM,width=2)
    map_fragments[code]=tile
    selected.paste(tile,b[:2])

def cluster_labels():
    layer=Image.new('RGBA',(WIDTH,HEIGHT))
    d=ImageDraw.Draw(layer)
    text(layer,(55,274),'Six academic clusters',29,'bold',PLUM)
    assert len(cluster_names)==6
    for dep,name in cluster_names.items():
        tiles=map_doc.xpath('//*[@width and starts-with(@data-id,$dep)]',dep=dep)
        top=min(float(tile.get('y')) for tile in tiles)
        bottom=max(float(tile.get('y'))+float(tile.get('height')) for tile in tiles)
        y=round(MY+(top+bottom)*MH/(2*676.8))
        left=round(MX+min(float(tile.get('x')) for tile in tiles)*MW/1152)
        accent=min((tile.get('fill') for tile in tiles),key=lambda c:sum(ImageColor.getrgb(c)))
        face=font(39,'body')
        end=77+round(face.getlength(name))
        assert end+14 < left, name
        d.rounded_rectangle((55,y-17,61,y+17),radius=2,fill=accent)
        d.text((77,y),name,font=face,fill=INK,anchor='lm')
        if left-end>=54:
            d.line((end+17,y,left-13,y),fill=LINE,width=2)
    return layer

map_without=selected.copy()
for b in map_boxes.values():
    ImageDraw.Draw(map_without).rectangle((b[0],b[1],b[2]-1,b[3]-1),fill=PAPER)
labels=cluster_labels()
for im in (unlit,selected):
    im.paste(labels,mask=labels.getchannel('A'))
labelled_background=map_without.copy()
labelled_background.paste(labels,mask=labels.getchannel('A'))
def animate_card(im,code,t,src,dst,first,second,curve=0):
    if t<=0:
        im.paste(first,src[:2]);return
    if t>=1:
        im.paste(second,dst[:2]);return
    b=list(interp_box(src,dst,t))
    offset=round(curve*math.sin(math.pi*t))
    b[1]+=offset;b[3]+=offset
    wh=size(b); f=smooth((t-.12)/.62)
    if f<1:
        left=first.resize(wh,Image.Resampling.BILINEAR)
    if f>0:
        right=second.resize(wh,Image.Resampling.BILINEAR)
    card=left if f==0 else right if f==1 else fade(left,right,f)
    im.paste(card,b[:2])
def build(t):
    if t<=0:return selected
    if t>=1:return plan
    # Clear the cluster names as the tiles depart, before the plan text appears.
    departing=fade(labelled_background,map_without,smooth(t/.20))
    im=fade(departing,empty,smooth(t/.78)).copy()
    for code in codes:
        b=map_boxes[code]
        delay=.09*(b[0]-MX)/MW+.07*(b[1]-MY)/MH
        phase=smooth((t-delay)/.83)
        animate_card(im,code,phase,b,tile_boxes[code],map_fragments[code],plan_tiles[code],-27)
    if t>.95:
        im=fade(im,plan,smooth((t-.95)/.05))
    return im

# Each focus view opens directly from the selected courses' six-semester positions.
groups=[
    ('Economics, business & entrepreneurship','Study how economies grow and how businesses make decisions.',
     [c for c in codes if c.startswith('BEN') and c!='BENGATE102'],RED),
    ('Politics','Compare political systems and explore how states cooperate or come into conflict.',
     [c for c in codes if c.startswith('GOSPOLI')],OCHRE),
    ('History','Trace how empires and the rise of the United States shaped the modern world.',
     [c for c in codes if c.startswith('GOSHIST')],OCHRE)
]
assert [len(g[2]) for g in groups]==[11,5,3]
class Focus:
    def __init__(self,idx):
        heading,explanation,self.items,accent=groups[idx]
        self.back=base.copy()
        self.tiles={};self.boxes={}
        self.depart=plan.copy()
        d=ImageDraw.Draw(self.depart)
        for c in self.items:
            b=tile_boxes[c]
            d.rectangle((b[0]-1,b[1]-1,b[2],b[3]),fill='white')
        if idx==0:
            text(self.back,(64,148),heading,65,'serif',PLUM)
            text(self.back,(67,250),explanation,35,'body',INK)
            for i,c in enumerate(self.items):
                col,row=divmod(i,6)
                x=67+col*903;y=342+row*107
                self.boxes[c]=(x,y,x+883,y+94)
        else:
            text(self.back,(66,285),heading,88,'serif',PLUM)
            for i,line in enumerate(wrap(explanation,font(41,'body'),564)):
                text(self.back,(70,435+58*i),line,41)
            n=len(self.items);h=117;gap=15
            top=round(573-(n*h+(n-1)*gap)/2)
            for r,c in enumerate(self.items):
                x=727;y=top+r*(h+gap)
                self.boxes[c]=(x,y,1847,y+h)
        for c in self.items:
            w,h=size(self.boxes[c])
            tile=Image.new('RGB',(w,h),PAPER)
            td=ImageDraw.Draw(tile)
            td.rounded_rectangle((0,0,w-1,h-1),radius=9,fill='#fffcf8',outline=LINE,width=2)
            td.rounded_rectangle((2,7,8,h-8),radius=3,fill=accent)
            text(tile,(23,12 if idx==0 else 16),c,20 if idx==0 else 22,'bold',accent)
            sz=37 if idx==0 else 47
            while font(sz,'body').getlength(courses[c])>w-47:sz-=1
            assert sz>=34
            text(tile,(22,43 if idx==0 else 53),courses[c],sz,'body')
            self.tiles[c]=tile
        self.full=self.back.copy()
        for c in self.items:self.full.paste(self.tiles[c],self.boxes[c][:2])
    def move(self,t):
        if t<=0:return plan
        if t>=1:return self.full
        im=fade(self.depart,self.back,smooth(t)).copy()
        for c in self.items:
            animate_card(im,c,smooth(t),tile_boxes[c],self.boxes[c],plan_tiles[c],self.tiles[c])
        return im
focus=[Focus(i) for i in range(3)]
post=frame('postgraduate');jobs=frame('employers');close=frame('closing')
for im,line in [
    (post,'UCR graduates who studied a similar mix of subjects went on to these programmes.'),
    (jobs,'UCR graduates who studied a similar mix of subjects have worked at these organisations.')
]:
    text(im,(72,951),line,31,'body',PLUM)

# Half-open intervals, in frames; frame endpoints include the settled static composition.
segments=[]
def hold(sec,im):segments.append((round(sec*FPS),im))
def move(sec,fn):segments.append((round(sec*FPS),fn))
def blend(sec,left,right):move(sec,lambda t:fade(left,right,smooth(t)))
hold(6,hook)
blend(.4,hook,unlit);hold(2.8,unlit)
blend(.48,unlit,selected);hold(2.9,selected)
move(4,build);hold(3.2,plan)
for i,secs in enumerate([8.5,6.3,6.0]):
    f=focus[i]
    move(.96,f.move);hold(secs,f.full);move(.84,lambda t,f=f:f.move(1-t))
    hold(1.0 if i<2 else 2.5,plan)
blend(.4,plan,post);hold(8.1,post)
blend(.36,post,jobs);hold(6.8,jobs)
blend(.4,jobs,close);hold(7.1,close)

def write_video(path):
    args=['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{WIDTH}x{HEIGHT}','-r',str(FPS),'-i','pipe:0',
          '-an','-c:v','libx264','-preset','veryfast','-crf','17','-threads','4','-pix_fmt','yuv420p','-movflags','+faststart',str(path)]
    with subprocess.Popen(args,stdin=subprocess.PIPE) as proc:
        for k,(n,source) in enumerate(segments):
            print(f'{k+1}/{len(segments)}',flush=True)
            if isinstance(source,Image.Image):
                data=source.tobytes()
                for _ in range(n):proc.stdin.write(data)
            else:
                for j in range(n):proc.stdin.write(source(j/(n-1)).tobytes())
        proc.stdin.close()
        if proc.wait():raise RuntimeError('ffmpeg failed')
    print(f'{sum(n for n,_ in segments)} frames',flush=True)
if __name__=='__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: baseline.py <output.mp4> | --preview')
    if sys.argv[1] == '--preview':
        ims=[hook,selected,build(.55),plan,focus[0].full,focus[1].full,focus[2].full,post,jobs]
        sheet=Image.new('RGB',(1200,675),'white')
        for i,im in enumerate(ims):sheet.paste(im.resize((400,225),Image.Resampling.LANCZOS),(i%3*400,i//3*225))
        sheet.save(ROOT/'preview.jpg',quality=85)
    else:write_video(Path(sys.argv[1]))
