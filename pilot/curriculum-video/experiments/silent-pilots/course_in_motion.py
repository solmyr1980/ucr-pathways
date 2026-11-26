from pathlib import Path
import math
import sys
from PIL import Image, ImageDraw
import baseline as b

lead = b.codes[0]
assert b.courses[lead] == 'Introduction to Economics'
others = [code for code in b.codes if code != lead]
duration = 5.875
crest = (73, 350, 960, 500)
hero = Image.new('RGB', b.size(crest), b.PAPER)
draw = ImageDraw.Draw(hero)
draw.rounded_rectangle((0, 0, hero.width - 1, hero.height - 1), radius=12,
                       fill='#fffcf8', outline=b.LINE, width=2)
draw.rounded_rectangle((3, 11, 11, hero.height - 12), radius=4, fill=b.RED)
b.text(hero, (33, 20), b.cluster_names[lead[:3]], 27, 'bold', b.RED)
b.text(hero, (30, 66), b.courses[lead], 68, 'serif', b.PLUM)
assert b.font(68,'serif').getlength(b.courses[lead]) < hero.width - 60

def phase(t, start, end):
    return b.smooth((t - start) / (end - start))

# Draw the lead separately in every phase so it has exactly one visible position.
source_background = b.selected.copy()
r = b.map_boxes[lead]
source_background.paste(b.PAPER, r)
quiet_map = b.map_without.copy()
dim_tiles = {c: b.fade(b.map_fragments[c], Image.new('RGB', b.map_fragments[c].size, b.PAPER), .53)
             for c in others}
for c in others:
    quiet_map.paste(dim_tiles[c], b.map_boxes[c][:2])

destination_panel = (51, 185, 648, 528)
map_and_panel = quiet_map.copy()
map_and_panel.paste(b.empty.crop(destination_panel), destination_panel[:2])
# The card flies alone into its semester. The other courses wait on the right.
handoff_background = b.map_without.copy()
handoff_background.paste(b.empty.crop(destination_panel), destination_panel[:2])

def lead_flight(scene, progress, start, end, first, second, bend):
    box = list(b.interp_box(start,end,progress))
    offset = round(bend * math.sin(math.pi*progress))
    box[1] += offset
    box[3] += offset
    dimensions = b.size(box)
    plain = Image.new('RGB', dimensions, '#fffcf8')
    if progress < .23:
        tile = b.fade(first.resize(dimensions,Image.Resampling.LANCZOS),plain,phase(progress,.03,.23))
    else:
        tile = b.fade(plain,second.resize(dimensions,Image.Resampling.LANCZOS),phase(progress,.23,.52))
    scene.paste(tile, box[:2])

heading = (0, 108, b.WIDTH, 204)
paper_heading = b.base.crop(heading)
plan_heading = paper_heading.copy()
plan_heading.paste(b.empty.crop((0,108,b.WIDTH,182)),(0,0))
map_heading = quiet_map.crop(heading)
handoff_background.paste(plan_heading,heading[:2])
handoff_background.paste(b.empty.crop(destination_panel),destination_panel[:2])

def course_journey(progress):
    if progress <= 0:
        return b.selected
    if progress >= 1:
        return b.plan
    t = progress * duration
    if t < 3.85:
        if t < 2.48:
            scene = b.fade(source_background, quiet_map, phase(t, 0, .39)).copy()
        else:
            scene = b.fade(quiet_map, map_and_panel, phase(t, 2.48, 3.12)).copy()
        if t >= 2.18:
            if t < 2.59:
                title = b.fade(map_heading, paper_heading, phase(t,2.18,2.59))
            else:
                title = b.fade(paper_heading, plan_heading, phase(t,2.59,3.16))
            scene.paste(title, heading[:2])
            if t >= 2.48:
                panel_top = (destination_panel[0], destination_panel[1],destination_panel[2],heading[3])
                panel = b.fade(scene.crop(panel_top),b.empty.crop(panel_top),phase(t,2.48,3.12))
                scene.paste(panel,panel_top[:2])
        if t < 1.20:
            lead_flight(scene, phase(t, .27, 1.20), r, crest,
                           b.map_fragments[lead], hero, -32)
        elif t < 2.65:
            scene.paste(hero, crest[:2])
        else:
            lead_flight(scene, phase(t, 2.65, 3.47), crest, b.tile_boxes[lead],
                           hero, b.plan_tiles[lead], -12)
        return scene

    elapsed = t - 3.85
    scene = b.fade(handoff_background, b.empty, phase(elapsed, 0, 1.46)).copy()
    for code in others:
        source = b.map_boxes[code]
        delay = .17 * (source[0] - b.MX) / b.MW + .08 * (source[1] - b.MY) / b.MH
        tile = b.fade(dim_tiles[code], b.map_fragments[code], phase(elapsed,0,.35))
        b.animate_card(scene, code, phase(elapsed, delay, delay+1.53), source,
                       b.tile_boxes[code], tile, b.plan_tiles[code], -25)
    scene.paste(b.plan_tiles[lead], b.tile_boxes[lead][:2])
    return b.fade(scene, b.plan, phase(t, 5.58, duration))

def invitation():
    cream = '#fcf6eb'
    im = Image.new('RGB', (b.WIDTH,b.HEIGHT), '#451d35')
    d = ImageDraw.Draw(im)
    logo = Image.open(b.A/'logo.png').convert('RGBA')
    logo = logo.crop(logo.getbbox()).resize((211,59),Image.Resampling.LANCZOS)
    im.paste(cream,(68,34,279,93),logo.getchannel('A'))
    d.text((1848,61),'Liberal Arts & Sciences',font=b.font(28,'body'),fill=cream,anchor='rm')
    d.line((70,115,1850,115), fill='#7a596d',width=2)
    b.text(im,(71,199),'What would',148,'serif',cream)
    b.text(im,(72,351),'you build?',148,'serif',cream)
    b.text(im,(80,599),'Tell UCR what you want to study.',41,'body',cream)
    b.text(im,(80,658),'We can propose a personalised curriculum.',41,'body',cream)
    b.text(im,(80,764),'ucr.nl/tell-us-about-your-interests/',38,'bold',cream)
    # Preserve the branded QR from the approved cut, at its native module size.
    qr = b.close.crop((1340,248,1820,728))
    mat = Image.new('RGB',(546,546),'white')
    mat.paste(qr,(33,33))
    im.paste(mat,(1260,227))
    d.line((76,878,1847,878),fill='#856979',width=2)
    b.text(im,(80,918),'An idea for a future video?',39,'serif',cream)
    b.text(im,(81,981),'Leave your academic interests in the video comments.',31,'body',cream)
    return im

new_close = invitation()
# Replace only the construction animation and closing composition.
updated = []
for length, source in b.segments[:-2]:
    updated.append((round(duration*b.FPS), course_journey) if source is b.build else (length,source))
assert sum(source is course_journey for _,source in updated) == 1
b.segments = updated
b.blend(.4,b.jobs,new_close)
b.hold(7.1,new_close)

if __name__=='__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: course_in_motion.py <output.mp4> | preview')
    if sys.argv[1]=='preview':
        times = [0,.65,1.3,2.9,3.54,4.5,5.6]
        grid = Image.new('RGB',(1500,4*281),'white')
        for i,im in enumerate([course_journey(t/duration) for t in times]+[new_close]):
            grid.paste(im.resize((500,281),Image.Resampling.LANCZOS),(500*(i%3),281*(i//3)))
        grid.crop((0,0,1500,843)).save(b.ROOT/'review.jpg',quality=93)
        new_close.resize((960,540),Image.Resampling.LANCZOS).save(b.ROOT/'closing-preview.png')
    else:
        b.write_video(Path(sys.argv[1]))
