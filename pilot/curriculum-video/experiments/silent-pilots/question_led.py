from pathlib import Path
import math, sys
from functools import lru_cache
from PIL import Image, ImageChops, ImageColor, ImageDraw
from scipy.optimize import linear_sum_assignment
import numpy as np

ROOT = Path(__file__).resolve().parent
import baseline as b

W,H = 1920,1080
PAPER=b.PAPER
PLUM='#451d35'
CREAM='#fff8ed'
BG=[PAPER,(248,233,216),(233,238,233),(241,232,237),PAPER]
MOTIF_COLOURS=[
    ['#7a3b53','#a65b61','#c98d79','#dac39f','#768477'],
    ['#70354a','#974758','#b96964','#c78b70','#daa771'],
    ['#294d4c','#416c63','#61847a','#829a87','#a1ad8d'],
    ['#583346','#73465b','#946475','#af8290','#c2989f']]
LEADS=['BENECON211','GOSPOLI112','GOSHIST211']
assert all(code in b.codes for code in LEADS)
TITLES=[b.courses[code] for code in LEADS]
assert TITLES==['International Macroeconomics','Foundations of Comparative Politics','History of Empires']
questions=[
    ['Why do some countries','become rich while','others stay poor?'],
    ['What makes','economies grow?'],
    ['Who holds','political power?'],
    ['What outlasts','an empire?']]
assert 'why some countries become rich while others stay poor' in b.interest
small=['A student’s question','Economics','Politics','History']
title_sizes=[94,111,111,115]
section_inks=[PLUM,'#733b47','#305b54','#6b4159']
START=[0,4.65,9.7,14.8,20.25]
map_end=26.2
grid_end=30.6
plan_end=33.9
post_end=38.0
jobs_end=42.15
end=48.5
def ease(t): return b.smooth(t)
def ramp(t,a,z): return ease((t-a)/(z-a))
def mix(a,z,k): return a+(z-a)*k
def rgb(c): return ImageColor.getrgb(c) if isinstance(c,str) else c
def colour(a,z,k): return tuple(round(mix(x,y,k)) for x,y in zip(rgb(a),rgb(z)))
def corner(a,z,k): return tuple(round(mix(x,y,k)) for x,y in zip(a,z))
def composite(im, layer,xy,alpha=1):
    if alpha<=0: return
    mask=layer.getchannel('A')
    if alpha<.999:mask=mask.point(lambda v:round(alpha*v))
    im.paste(layer,xy,mask)
def text_layer(words,sz,family,ink):
    f=b.font(sz,family)
    bounds=f.getbbox(words,anchor='lt')
    layer=Image.new('RGBA',(max(1,round(f.getlength(words))+12),bounds[3]+16))
    ImageDraw.Draw(layer).text((5,3),words,font=f,fill=ink,anchor='lt')
    return layer
text_layer=lru_cache(None)(text_layer)

logo=Image.open(b.A/'logo.png').convert('RGBA')
logo=logo.crop(logo.getbbox()).resize((208,58),Image.Resampling.LANCZOS)
def brand(im,on_dark=False):
    ink=CREAM if on_dark else PLUM
    im.paste(ink,(70,40,278,98),logo.getchannel('A'))
    d=ImageDraw.Draw(im)
    d.text((1848,69),'Liberal Arts & Sciences',font=b.font(27,'body'),fill=ink,anchor='rm')
def put(im,xy,words,size,style,ink,alpha=1):
    composite(im,text_layer(words,size,style,ink),(round(xy[0]-5),round(xy[1]-3)),alpha)

# Each visual uses the same 24 pieces. Match nearby positions when changing the shape.
# Form = centre, radii, rotation, superellipse exponent and colour.
def shape(x,y,rx,ry,ang,n,c): return (x,y,rx,ry,ang,n,rgb(c))
def globe(t=0):
    poses=[]
    for row,n in enumerate([2,4,6,6,4,2]):
        lat=math.radians([-66,-41,-15,15,41,66][row]); cy=523+232*math.sin(lat)
        for col in range(n):
            along=((col+.5)/n-.5)*math.pi*1.14 + .085*math.sin(t*.65)
            x=1403+260*math.cos(lat)*math.sin(along)
            y=cy-23*math.cos(along)*math.cos(lat)
            rad=14+3.5*math.cos(along)
            poses.append(shape(x,y,rad,rad,0,2,MOTIF_COLOURS[0][(col+2*row)%5]))
    return poses
def money():
    poses=[]
    for col,n in enumerate([3,5,7,9]):
        for j in range(n):
            poses.append(shape(1182+145*col,714-j*28,65,23,0,2.9,
                               MOTIF_COLOURS[1][[2,3,1,0][col] if j<n-1 else 4]))
    return poses
def assembly():
    poses=[]
    for row,num in enumerate([5,8,11]):
        radius=124+row*77
        for k in range(num):
            ang=math.radians(193+154*(k+.5)/num)
            poses.append(shape(1400+radius*math.cos(ang),672+radius*math.sin(ang),
                               24,23,0,2.6,MOTIF_COLOURS[2][(k//3+row)%5]))
    return poses
def arch():
    poses=[]
    for i in range(12):
        a=-math.pi+(i+.5)*math.pi/12
        poses.append(shape(1400+162*math.cos(a),558+162*math.sin(a),20,46,
                           a+math.pi/2,8,MOTIF_COLOURS[3][i%4]))
    for k in [-1,1]:
        for j in range(3):
            poses.append(shape(1400+162*k,576+j*51,45,24,0,11,MOTIF_COLOURS[3][(j+1)%4]))
        poses.append(shape(1400+162*k,727,59,18,0,11,MOTIF_COLOURS[3][0]))
    for j in range(4):
        poses.append(shape(1400+(j-1.5)*103,328,50,16,0,11,MOTIF_COLOURS[3][j%3+1]))
    return poses

def align(before,after):
    cost=np.array([[(a[0]-z[0])**2+(a[1]-z[1])**2 for z in after] for a in before])
    _,matched=linear_sum_assignment(cost)
    return [after[k] for k in matched]
poses=[globe(4.65)]
for spec in [money(),assembly(),arch()]:poses.append(align(poses[-1],spec))
angles=np.arange(56)*math.tau/56
unit_cos,unit_sin=np.cos(angles),np.sin(angles)
def polygon(d,state,bg):
    x,y,rx,ry,turn,p,c=state
    # Full HD rasterization keeps the moving contour smooth at playback scale.
    vx=rx*np.sign(unit_cos)*np.power(np.abs(unit_cos),2/p)
    vy=ry*np.sign(unit_sin)*np.power(np.abs(unit_sin),2/p)
    cs=math.cos(turn); sn=math.sin(turn)
    pts=np.stack([x+cs*vx-sn*vy,y+sn*vx+cs*vy],axis=1).round().astype(int)
    d.polygon(list(map(tuple,pts)),fill=c,outline=bg,width=2)
def between(a,z,k):
    rotation=(z[4]-a[4]+math.pi/2)%math.pi-math.pi/2
    return (*[mix(a[i],z[i],k) for i in range(4)],a[4]+rotation*k,mix(a[5],z[5],k),colour(a[6],z[6],k))
def globe_lines(im,bg,opacity):
    if opacity<=0:return
    ink=colour(bg,'#b8a99a',opacity*.59);d=ImageDraw.Draw(im)
    for dx in (257,168,70):
        d.ellipse((1403-dx,290,1403+dx,756),outline=ink,width=2)
    for y,half in [(386,211),(505,256),(628,226)]:
        d.arc((1403-half,y-25,1403+half,y+25),0,180,fill=ink,width=2)
def assembly_detail(im,bg,alpha):
    if alpha<=0:return
    d=ImageDraw.Draw(im); ink=colour(bg,'#486f65',alpha*.77)
    d.arc((1067,337,1733,1003),194,346,fill=ink,width=3)
    d.rounded_rectangle((1364,661,1436,679),radius=6,fill=ink)
def chapter_text(im,index,age,exit_fade=1):
    if index==0:
        x,y=82,285;spacing=111
    else:
        x,y=82,306;spacing=137
    label_alpha=(1 if index==0 else ramp(age,.02,.45))*exit_fade
    put(im,(83,208),small[index],36,'bold',section_inks[index],label_alpha)
    for i,line in enumerate(questions[index]):
        onset=0 if index==0 and i==0 else .10+.115*i
        alpha=(1 if index==0 and i==0 else ramp(age,onset,onset+.45))*exit_fade
        put(im,(x,y+i*spacing+17*(1-alpha)),line,title_sizes[index],'serif',PLUM,alpha)

# The displayed course titles move into three bookmarks, then into their actual slots.
accent=['#963f4d','#416b61','#845164']
def course_chip(index,width,height,compact=False):
    lay=Image.new('RGBA',(width,height))
    d=ImageDraw.Draw(lay);title=TITLES[index]
    sx=round(.33*height)
    d.rounded_rectangle((0,0,width-1,height-1),radius=round(.46*height),
                        fill='#fffaf2',outline='#cdbeb4',width=2)
    rr=round(height*.105); cx=sx;cy=height//2
    d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr),fill=accent[index])
    sz=32 if compact else 43
    while b.font(sz,'body').getlength(title)>width-sx-rr-38:sz-=1
    d.text((sx+rr+15,cy),title,font=b.font(sz,'body'),fill=PLUM,anchor='lm')
    return lay
hero_box=[(80,658,900,753),(80,658,1024,753),(80,658,662,753)]
rail_box=[(73,945,620,1014),(650,945,1290,1014),(1320,945,1847,1014)]
hero=[course_chip(i,*b.size(hero_box[i])) for i in range(3)]
rail=[course_chip(i,*b.size(rail_box[i]),compact=True) for i in range(3)]
def fly_chip(im,i,k,src,dst,start,finish,opacity=1):
    box=b.interp_box(src,dst,k)
    wh=b.size(box)
    # Use the larger master for the moving title, then settle into the destination styling.
    lay=start.resize(wh,Image.Resampling.LANCZOS)
    if k>.70:
        lay=Image.blend(lay,finish.resize(wh,Image.Resampling.LANCZOS),ramp(k,.70,1))
    composite(im,lay,box[:2],opacity)
def bookmarks(im,t):
    for i in range(3):
        t0=START[i+1]; nxt=START[i+2]
        if t<t0+.65:continue
        if t<nxt:
            alpha=ramp(t,t0+.65,t0+1.40)
            box=hero_box[i]
            composite(im,hero[i],(box[0],box[1]+round(19*(1-alpha))),alpha)
        elif t<nxt+.84:
            fly_chip(im,i,ramp(t,nxt,nxt+.84),hero_box[i],rail_box[i],hero[i],rail[i])
        else:composite(im,rail[i],rail_box[i][:2])
def chapters(t):
    idx=max(i for i,a in enumerate(START[:4]) if t>=a)
    age=t-START[idx]; prev=max(0,idx-1)
    k=ramp(age,0,1.1) if idx else 1
    bg=colour(BG[prev],BG[idx],k)
    im=Image.new('RGB',(W,H),bg)
    brand(im)
    globe_lines(im,bg,1 if idx==0 else (1-k if idx==1 else 0))
    assembly_detail(im,bg,k if idx==2 else 1-k if idx==3 else 0)
    if idx==0:states=globe(t)
    else:
        states=[]
        for j,(a,z) in enumerate(zip(poses[prev],poses[idx])):
            if idx==1:
                order=(714-z[1])/224
            elif idx==2:
                order=math.hypot(z[0]-1400,z[1]-672)/278
            else:
                order=(727-z[1])/399
            delay=.57*max(0,min(1,order))+.014*(j%4)
            k=ramp(age,delay,1.16+1.02*order+.018*(j%4))
            state=list(between(a,z,k))
            state[1]-=(19 if idx==3 else 13)*math.sin(math.pi*k)
            states.append(state)
    d=ImageDraw.Draw(im)
    for state in sorted(states,key=lambda v:v[1]):polygon(d,state,bg)
    if idx and age<.28:
        chapter_text(im,prev,4,1-ramp(age,0,.28))
    if idx==0 or age>=.25:chapter_text(im,idx,age if idx==0 else age-.25)
    bookmarks(im,t)
    return im

# Use the real board and source-to-semester geometry for all 24 courses.
map_crop=(38,260,1870,956); mx,my,ms=91,231,.94
def scaled(r):
    return tuple(round((p-map_crop[i%2])*ms+(mx if i%2==0 else my)) for i,p in enumerate(r))
map_box={code:scaled(b.map_boxes[code]) for code in b.codes}
clean=b.unlit.crop(map_crop)
ImageDraw.Draw(clean).rectangle((5,0,460,52),fill=PAPER)
map_back=Image.new('RGB',(W,H),PAPER)
brand(map_back)
put(map_back,(80,126),'UCR’s six academic clusters',72,'serif',PLUM)
map_back.paste(clean.resize((round(clean.width*ms),round(clean.height*ms)),Image.Resampling.LANCZOS),(mx,my))
for code in b.codes:
    r=map_box[code]
    ImageDraw.Draw(map_back).rectangle((r[0],r[1],r[2]-1,r[3]-1),fill=PAPER)
# Use original tile colour and shape for the settled image.
tiles={code:b.map_fragments[code].resize(b.size(map_box[code]),Image.Resampling.LANCZOS) for code in b.codes}
map_full=map_back.copy()
for code in b.codes:map_full.paste(tiles[code],map_box[code][:2])
for i,code in enumerate(LEADS):
    x,y,z,w=map_box[code]
    ImageDraw.Draw(map_full).rounded_rectangle((x-4,y-4,z+3,w+3),radius=6,outline=accent[i],width=4)

map_states=[shape((r[0]+r[2])/2,(r[1]+r[3])/2,(r[2]-r[0])/2,(r[3]-r[1])/2,0,6,'#845366') for r in map_box.values()]
map_states=align(poses[-1],map_states)
def map_scene(age):
    if age>=1.7:
        im=map_full.copy();bookmarks(im,START[4]+age);return im
    bg=colour(BG[3],PAPER,ramp(age,0,.95))
    im=Image.new('RGB',(W,H),bg);brand(im)
    if age<.35:chapter_text(im,3,4,1-ramp(age,0,.35))
    im=b.fade(im,map_back,ramp(age,.32,1.22)).copy()
    d=ImageDraw.Draw(im)
    for j,(a,z) in enumerate(zip(poses[-1],map_states)):
        s=between(a,z,ramp(age,(j%5)*.04,1.19+.019*(j%6)))
        polygon(d,s,bg)
    im=b.fade(im,map_full,ramp(age,1.20,1.65)).copy()
    bookmarks(im,START[4]+age)
    return im

def plan_reveal(age):
    # Keep the three titles in view as the map recedes. The other courses
    # appear in their final slots, so no in-flight text can hide the three examples.
    paper=Image.new('RGB',(W,H),PAPER)
    brand(paper)
    cleared=b.fade(map_full,paper,ramp(age,0,.63))
    im=b.fade(cleared,b.empty,ramp(age,.52,1.14)).copy()
    for i,code in enumerate(LEADS):
        t=ramp(age,.12+.20*i,1.31+.21*i)
        fly_chip(im,i,t,rail_box[i],b.tile_boxes[code],rail[i],b.plan_tiles[code].convert('RGBA'))
    for j,code in enumerate(b.codes):
        if code in LEADS: continue
        r=b.tile_boxes[code]
        semester,row=divmod(j,4)
        onset=1.99+.22*semester+.072*row
        opacity=ramp(age,onset,onset+.37)
        if opacity:
            tile=b.plan_tiles[code].convert('RGBA')
            composite(im,tile,(r[0],r[1]+round((1-opacity)*8)),opacity)
    return b.fade(im,b.plan,ramp(age,3.77,4.18))

def end_frame():
    im=Image.new('RGB',(W,H),PLUM);brand(im,True)
    put(im,(80,237),'What would',152,'serif',CREAM)
    put(im,(80,408),'you build?',152,'serif',CREAM)
    put(im,(86,690),'Tell UCR what you want to study.',48,'body',CREAM)
    put(im,(87,801),'ucr.nl/tell-us-about-your-interests/',38,'bold',CREAM)
    qr=b.close.crop((1340,248,1820,728));mat=Image.new('RGB',(552,552),'white')
    mat.paste(qr,(36,36));im.paste(mat,(1279,270))
    return im
close=end_frame()
def film(t):
    if t<START[4]:return chapters(t)
    if t<map_end:return map_scene(t-START[4])
    if t<grid_end:return plan_reveal(t-map_end)
    if t<plan_end:return b.plan
    if t<post_end:return b.fade(b.plan,b.post,ramp(t,plan_end,plan_end+.30))
    if t<jobs_end:return b.fade(b.post,b.jobs,ramp(t,post_end,post_end+.28))
    return b.fade(b.jobs,close,ramp(t,jobs_end,jobs_end+.34))
if __name__=='__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: question_led.py <output.mp4> | preview')
    if sys.argv[1]=='preview':
        times=[2,5.3,7,12.1,18,21.1,24,27.8,29.1,31.7,36.3,40,46]
        sh=Image.new('RGB',(1440,270*math.ceil(len(times)/3)),'white')
        for idx,t in enumerate(times):
            sh.paste(film(t).resize((480,270),Image.Resampling.LANCZOS),(idx%3*480,idx//3*270))
        sh.save(ROOT/'preview.jpg',quality=93)
    else:
        # Use static frames for settled reading holds; cache them in the encoder input loop.
        intervals=[(0,4.65,None),(4.65,7.2,None),(7.2,9.7,8),(9.7,12.25,None),
                   (12.25,14.8,13),(14.8,17.35,None),(17.35,20.25,18),(20.25,22,None),
                   (22,map_end,24),(map_end,grid_end,None),(grid_end,plan_end,32),
                   (plan_end,plan_end+.32,None),(plan_end+.32,post_end,36),
                   (post_end,post_end+.32,None),(post_end+.32,jobs_end,40),
                   (jobs_end,jobs_end+.39,None),(jobs_end+.39,end,46)]
        b.segments=[]
        for a,z,hold in intervals:
            first,last=round(a*b.FPS),round(z*b.FPS)
            fn=film(hold) if hold is not None else (lambda p,f=first,l=last:film((f+p*(l-f-1))/b.FPS))
            b.segments.append((last-first,fn))
        b.write_video(Path(sys.argv[1]))
