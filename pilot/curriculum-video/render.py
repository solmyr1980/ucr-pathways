"""Animate the public programme. Its record owns positions and the workbook owns titles."""

import argparse
import bisect
import json
import math
import subprocess
from functools import lru_cache
from pathlib import Path

import openpyxl
from maps import ASSETS, CLUSTERS, PLUM, CourseMap
from PIL import Image, ImageColor, ImageDraw, ImageFont
from subtitles import FILENAME as SRT

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
W, H, FPS = 1920, 1080, 24
PAPER, INK, MUTED, RULE = "#F8F5EE", "#2E2D2D", "#5C606B", "#D9D4CC"
LILAC, BLUE, YELLOW = "#D0B7D0", "#C8DFE6", "#FFE1A4"
COLORS = {"BEN": "#9C333D", "GOS": "#77532B", "ENS": "#4A6857", "ACC": PLUM}
URL = "https://ucr.nl/tell-us-about-your-interests/"
VIEW = (492, 320)
VIEW_X, VIEW_Y = 52, 417
GUIDE_SIZE = (1450, 624)
GUIDE_X, GUIDE_Y = (W - GUIDE_SIZE[0]) // 2, 260
GUIDE_ORDER = ("left", "right", "middle")


@lru_cache(None)
def font(size, kind="regular"):
    files = {
        "regular": "Inter_Medium.ttf",
        "bold": "Inter_Bold.ttf",
        "serif": "IvyMode Semibold.otf",
        "display": "IvyMode Regular.otf",
    }
    return ImageFont.truetype(str(ROOT / "assets/fonts" / files[kind]), size)


def label(d, xy, value, size, color=INK, kind="regular"):
    d.text(xy, value, font=font(size, kind), fill=color, anchor="lt")


@lru_cache(None)
def lines(value, width, size, kind):
    words = value.split()
    result = [words.pop(0)]
    for word in words:
        trial = result[-1] + " " + word
        if font(size, kind).getlength(trial) <= width:
            result[-1] = trial
        else:
            result.append(word)
    return result


def paragraph(d, xy, value, width, size, leading, kind="regular", color=INK):
    x, y = xy
    for line in lines(value, width, size, kind):
        label(d, (x, y), line, size, color, kind)
        y += leading
    return y


def ease(x):
    x = max(0, min(1, x))
    return x * x * (3 - 2 * x)


def mix(a, b, p):
    return a + (b - a) * p


def source_data():
    record = json.loads((ROOT / "data/examples/p-001.json").read_text())
    prog = next(p for p in record["programmes"] if p["id"] == "ucr-depth")
    semesters = prog["schedule"]["semesters"]
    book = openpyxl.load_workbook(
        ROOT / "data/reference/ucr_courses_enriched.xlsx", read_only=True
    )
    rows = iter(book.active.values)
    keys = next(rows)
    catalog = {row[keys.index("osiris")]: dict(zip(keys, row)) for row in rows}
    book.close()
    names = {}
    for cluster in CLUSTERS:
        labels = {row["deplabel"] for row in catalog.values() if row["dep"] == cluster}
        if len(labels) != 1 or not all(labels):
            raise ValueError(f"Expected one official display label for {cluster}: {labels}")
        names[cluster] = labels.pop()
    assert len(semesters) == 6 and all(len(s["courses"]) == 4 for s in semesters)
    slots = {
        c["code"]: (i, j, catalog[c["code"]]["name"])
        for i, s in enumerate(semesters)
        for j, c in enumerate(s["courses"])
    }
    assert len(slots) == 24
    return (
        record["interests"],
        prog["label"],
        slots,
        [s["label"] for s in semesters],
        names, catalog,
    )


def tween(a, b, p):
    return tuple(mix(x, y, p) for x, y in zip(a, b))


class Film:
    def __init__(self, timing):
        self.interest, self.title, self.slots, self.labels, self.names, catalog = source_data()
        self.scenes = json.loads(timing.read_text())
        hook = next(s for s in self.scenes if s["scene"] == "hook")
        self.subjects = [subject["label"] for subject in hook["subjects"]]
        for subject in hook["subjects"]:
            assert subject["courses"] and set(subject["courses"]) <= self.slots.keys()
            phrase = subject.get("interest_phrase", subject["label"])
            assert phrase.casefold() in self.interest.casefold()
            assert subject["label"].casefold() in hook["cues"][0][1].casefold()
        self.ends = [s["end"] for s in self.scenes]
        self.maps = {k: CourseMap(k) for k in ("curriculum", *CLUSTERS)}
        self.map = self.maps["curriculum"]
        for k in CLUSTERS:
            assert {c for c in self.map.boxes if c.startswith(k)} == {
                c for c in self.maps[k].boxes if c.startswith(k)
            }
        guide = next(s for s in self.scenes if s["scene"] == "gateway_overview")
        self.guide_map = self.maps[guide["cluster"]]
        codes = {code for code, row in catalog.items() if row["dep"] == guide["cluster"]}
        assert codes == self.guide_map.boxes.keys()
        required = {catalog[code]["preq1"] for code in codes} - {"NONE"}
        assert required and required <= codes
        self.regions = {
            "left": [c for c in codes if catalog[c]["preq1"] == "NONE" and c not in required],
            "middle": sorted(required),
            "right": [c for c in codes if catalog[c]["preq1"] in required],
        }
        # This reading guide applies to a real map with three separate columns.
        boxes = self.guide_map.boxes
        bounds = [(min(boxes[c][0] for c in group), max(boxes[c][2] for c in group))
                  for group in self.regions.values()]
        assert sum(map(len, self.regions.values())) == len(codes)
        assert all(a[1] < b[0] for a, b in zip(bounds, bounds[1:]))
        self.guide_camera = self.guide_map.fit(GUIDE_SIZE, codes, margin=3)
        x, _, width, _ = self.guide_camera
        self.guide_columns = {
            side: (round(GUIDE_X + (left - x) * GUIDE_SIZE[0] / width) - 2,
                   round(GUIDE_X + (right - x) * GUIDE_SIZE[0] / width) + 2)
            for side, (left, right) in zip(self.regions, bounds)
        }
        self.events = []
        for s in self.scenes:
            for codes, _, start, end in s["cues"]:
                for i, code in enumerate(codes):
                    assert code.startswith(s["scene"]) and code in self.map.boxes
                    assert code in self.source(code).boxes
                    when = start + 0.08 + (end - start) * i / len(codes)
                    self.events.append((when, code))
        self.times = [t for t, _ in self.events]
        assert self.times == sorted(self.times)
        assert sorted(c for t, c in self.events) == sorted(self.slots)
        logo = Image.open(ROOT / "assets/brand/ucr-primary-plum.png").convert("RGBA")
        self.logo = logo.crop(logo.getbbox())
        self.qr = Image.open(ASSETS / "qr-code.png").convert("RGB")

    def source(self, code):
        return self.map if code.startswith("ACC") else self.maps[code[:3]]

    @lru_cache(None)
    def shell(self):
        im = Image.new("RGB", (W, H), PAPER)
        d = ImageDraw.Draw(im)
        logo = self.logo.resize((212, 59), Image.Resampling.LANCZOS)
        im.paste(logo, (52, 23), logo)
        d.text(
            (1868, 49), "Liberal Arts & Sciences", anchor="rm", font=font(25), fill=PLUM
        )
        d.line((52, 100, 1868, 100), fill=RULE, width=2)
        return im

    def hook(self, age, turn):
        im = Image.new("RGB", (W, H), PLUM)
        d = ImageDraw.Draw(im)
        p = ease((age - turn) / 1.25)
        title = "Choosing a degree" if age < turn else "But what if your interests"
        label(d, (96, 118), title, 91, PAPER, "display")
        if age >= turn:
            label(d, (96, 224), "cross those boundaries?", 91, PAPER, "display")
        colors = (YELLOW, BLUE, LILAC)
        count = len(self.subjects)
        # Centre both arrangements. Each subject's evidence belongs to the example.
        width = min(370, 1480 // count)
        apart = min(600, (W - 260 - width) / max(1, count - 1))
        for i, name in enumerate(self.subjects):
            color = colors[i % len(colors)]
            intro = ease((age - i * 0.22) / 0.95)
            offset = i - (count - 1) / 2
            x = round((W - width) / 2 + offset * mix(apart, width + 5, p))
            y = round(mix(490 + offset * 34, 561, p) + 55 * (1 - intro))
            for j in range(3):
                left = x + round((j - 2) * mix(27, 0, p))
                top = y + round((j - 2) * mix(32, 0, p))
                d.rounded_rectangle(
                    (left, top, left + width, top + 157),
                    radius=8,
                    fill=color if j == 2 else PLUM,
                    outline=color,
                    width=3,
                )
            size = 51
            while font(size, "serif").getlength(name) > width - 44:
                size -= 1
            d.text((left + width / 2, top + 78), name, anchor="mm",
                   font=font(size, "serif"), fill=PLUM)
        return im

    @lru_cache(None)
    def overview(self):
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        label(d, (52, 148), "Six academic clusters", 80, PLUM, "serif")
        # The six small silhouettes are taken from the actual six cluster close-ups.
        for i, (k, name) in enumerate(self.names.items()):
            y = 318 + i * 101
            m = self.maps[k]
            stamp, _ = m.view(m.fit((95, 61)), (95, 61))
            im.paste(stamp, (54, y))
            label(d, (167, y + 14), name, 27, INK)
        size = (1160, 663)
        diagram, _ = self.map.view(self.map.fit(size), size)
        im.paste(diagram, (708, 219))
        return im

    @lru_cache(None)
    def guide_frame(self, cluster, active):
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        label(d, (52, 126), self.names[cluster], 63, PLUM, "serif")
        panel, _ = self.guide_map.view(self.guide_camera, GUIDE_SIZE)
        im.paste(panel, (GUIDE_X, GUIDE_Y))
        for side, title in (("left", "Open"), ("middle", "Gateway"), ("right", "Locked")):
            left, right = self.guide_columns[side]
            selected = side == active
            d.rounded_rectangle((left, 201, right, 251), radius=6,
                                fill=PLUM if selected else "#EDE8E3")
            d.text(((left + right) / 2, 226), title, anchor="mm", font=font(28, "bold"),
                   fill="white" if selected else PLUM)
            if selected:
                # Enclose the region without recolouring its original SVG tiles.
                d.rectangle((left, GUIDE_Y, right, GUIDE_Y + GUIDE_SIZE[1] - 1),
                            outline=PLUM, width=3)
        return im

    def guide_region(self, scene, t):
        return next((side for side in reversed(GUIDE_ORDER)
                     if t >= scene["word_times"][side][0]), None)

    @lru_cache(None)
    def interest_frame(self):
        im = self.shell().copy()
        size = (1430, 731)
        diagram, _ = self.map.view(self.map.fit(size), size)
        im.paste(diagram, (434, 154))
        d = ImageDraw.Draw(im)
        # The full map's upper-left white space is deliberately reserved for the quotation.
        d.rectangle((52, 165, 900, 516), fill=PAPER)
        label(d, (58, 186), "A student’s interests", 30, PLUM, "bold")
        paragraph(d, (54, 255), "“" + self.interest + "”", 810, 62, 76, "display", PLUM)
        return im

    def grid(self, im, count, expand=0, emphasis=None, strength=0):
        d = ImageDraw.Draw(im)
        # Keep all six semesters above the lower sixth used by two-line subtitles.
        start = round(mix(583, 52, expand))
        gap = 16
        width = (1868 - start - 2 * gap) // 3
        visible = {c for _, c in self.events[:count]}
        coords = {}
        for code, (s, r, title) in self.slots.items():
            x = start + (s % 3) * (width + gap)
            y = 186 + (s // 3) * 358
            if r == 0:
                d.rounded_rectangle(
                    (x, y, x + width, y + 342),
                    radius=12,
                    fill="white",
                    outline=RULE,
                    width=2,
                )
                label(d, (x + 16, y + 9), self.labels[s], 26, PLUM, "bold")
                d.line((x + 16, y + 39, x + width - 16, y + 39), fill=RULE, width=1)
            cy = y + 45 + r * 72
            box = (x + 12, cy, x + width - 12, cy + 70)
            coords[code] = box
            if code not in visible:
                d.rounded_rectangle(box, radius=5, fill="#F5F4F1")
                continue
            accent = COLORS[code[:3]]
            fill = "#F8F6F2"
            if emphasis and code.startswith(emphasis):
                fill = tuple(
                    round(v)
                    for v in tween(
                        ImageColor.getrgb(fill),
                        ImageColor.getrgb(accent),
                        strength * 0.34,
                    )
                )
            d.rounded_rectangle(box, radius=5, fill=fill)
            d.rounded_rectangle(
                (x + 12, cy + 2, x + 17, cy + 68), radius=2, fill=accent
            )
            label(d, (x + 25, cy + 3), code, 17, accent, "bold")
            size = round(mix(25, 29, expand))
            if expand == 1:
                while size > 25 and font(size).getlength(title) > width - 48:
                    size -= 1
            while len(lines(title, width - 48, size, "regular")) > 2:
                size -= 1
            assert size >= 21
            leading = min(25, size + 1)
            for j, line in enumerate(lines(title, width - 48, size, "regular")):
                assert font(size).getlength(line) <= width - 48
                d.text(
                    (x + 25, cy + 23 + j * leading),
                    line,
                    font=font(size),
                    fill=INK,
                    anchor="lt",
                )
        return coords

    @lru_cache(maxsize=5)
    def base(self, sid, count, expand=0, emphasis=None, strength=0):
        s = self.scenes[sid]
        k = s["scene"]
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        x = round(mix(583, 52, expand))
        label(d, (x, 117), self.title, round(mix(43, 56, expand)), PLUM, "serif")
        d.text((1866, 143), f"{count} / 24", font=font(23), fill=MUTED, anchor="rm")
        coords = self.grid(im, count, expand, emphasis, strength)
        if k == "complete":
            label(d, (302, 39), "Illustrative programme", 24, MUTED)
            if emphasis:
                field = next(word for word, prefix in s["highlights"].items() if prefix == emphasis)
                d.text((1465, 49), field.capitalize(), anchor="rm",
                       font=font(27, "bold"), fill=COLORS[emphasis[:3]])
        else:
            section = (
                "Across clusters"
                if k == "bridge"
                else ("Academic core" if k == "ACC" else self.names[k])
            )
            label(d, (52, 143), section, 26, COLORS.get(k, PLUM), "bold")
            paragraph(d, (50, 211), s["heading"], 490, 51, 59, "serif", PLUM)
            d.line((561, 132, 561, 886), fill=RULE, width=2)
        return im, coords

    def focus(self, im, code, prev, p):
        m = self.source(code)
        camera = m.close(code, VIEW)
        if prev and prev[:3] == code[:3] and p < 1:
            camera = tween(m.close(prev, VIEW), camera, p)
        panel, centres = m.view(camera, VIEW, [code], 0.58)
        im.paste(panel, (VIEW_X, VIEW_Y))
        d = ImageDraw.Draw(im)
        d.rectangle(
            (VIEW_X - 1, VIEW_Y - 1, VIEW_X + VIEW[0], VIEW_Y + VIEW[1]),
            outline=RULE,
            width=1,
        )
        label(d, (52, 754), code, 23, COLORS[code[:3]], "bold")
        paragraph(d, (50, 799), self.slots[code][2], 494, 39, 47, "serif", PLUM)
        cx, cy = centres.get(code, (VIEW[0] / 2, VIEW[1] / 2))
        return VIEW_X + max(0, min(VIEW[0], cx)), VIEW_Y + max(0, min(VIEW[1], cy))

    @lru_cache(maxsize=12)
    def bridge_view(self, stage, fields):
        if stage in CLUSTERS:
            m = self.maps[stage]
            return m.view(m.fit(VIEW), VIEW)[0]
        codes = [c for c in self.map.boxes if c.startswith(fields)]
        return self.map.view(self.map.fit(VIEW), VIEW, codes, 0.72, False)[0]

    def bridge(self, sid, n, t):
        s = self.scenes[sid]
        fields = (s["from"], s["to"])
        u = ease((t - s["start"]) / 1.25)
        v = ease((t - s["end"] + 1.35) / 1.35)
        im = self.base(sid, n)[0].copy()
        codes = [c for c in self.map.boxes if c.startswith(fields)]
        if u < 1 or v > 0:
            k = fields[0] if u < 1 else fields[1]
            field = [c for c in codes if c.startswith(k)]
            full = self.map.fit(VIEW)
            # The full map and the close-up use different layouts. Zoom on the full map
            # and dissolve into the separate SVG only at the matching field.
            progress = (1 - u) if u < 1 else v
            cam = tween(full, self.map.fit(VIEW, field), progress)
            panel, _ = self.map.view(cam, VIEW, codes, 0.72, False)
            panel = Image.blend(
                panel, self.bridge_view(k, fields), ease((progress - 0.42) / 0.58)
            )
        else:
            panel = self.bridge_view("both", fields)
        im.paste(panel, (VIEW_X, VIEW_Y))
        d = ImageDraw.Draw(im)
        for i, k in enumerate(fields):
            y = 759 + 66 * i
            d.rounded_rectangle((52, y + 4, 66, y + 30), radius=3, fill=COLORS[k])
            label(d, (83, y), self.names[k], 29, PLUM, "bold")
        return im

    def selection(self, sid, n, t):
        s = self.scenes[sid]
        k = s["scene"]
        if n == 0 or self.events[n - 1][1][:3] != k:
            code = next(c for st, c in self.events if st >= s["start"])
            im = self.base(sid, n)[0].copy()
            self.focus(im, code, None, 1)
            return im
        start, code = self.events[n - 1]
        age = t - start
        prev = self.events[n - 2][1] if n >= 2 else None
        arrived = age >= 1.2
        base, boxes = self.base(sid, n if arrived else n - 1)
        im = base.copy()
        origin = self.focus(im, code, prev, ease(age / 0.45))
        if not arrived:
            x, y, x2, y2 = boxes[code]
            flight = ease((age - 0.45) / 0.75)
            if flight > 0:
                card = self.base(sid, n)[0].crop((x, y, x2 + 1, y2 + 1))
                scale = mix(0.39, 1, flight)
                card = card.resize(
                    (round(card.width * scale), round(card.height * scale)),
                    Image.Resampling.BILINEAR,
                )
                px = mix(origin[0] - card.width / 2, x, flight)
                py = mix(origin[1] - card.height / 2, y, flight) - 55 * math.sin(
                    math.pi * flight
                )
                im.paste(card, (round(px), round(py)))
        return im

    @lru_cache(None)
    def invitation(self):
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        label(d, (67, 155), "What would you build?", 101, PLUM, "display")
        label(d, (73, 379), "A curriculum around your interests", 53, PLUM, "serif")
        paragraph(d, (74, 482), "Tell UCR what you want to study. We can propose a personalised curriculum.",
                  1080, 39, 57)
        label(d, (73, 646), URL, 38, PLUM, "bold")
        qr = self.qr.resize((480, 480), Image.Resampling.NEAREST)
        im.paste(qr, (1340, 248))
        d.line((73, 749, 1848, 749), fill=RULE, width=2)
        label(d, (73, 771), "An idea for a future video", 48, PLUM, "serif")
        label(d, (74, 842), "Leave your academic interests in the video comments.", 37)
        return im

    def frame(self, t):
        sid = min(len(self.ends) - 1, bisect.bisect_right(self.ends, t))
        s = self.scenes[sid]
        k = s["scene"]
        age = t - s["start"]
        n = bisect.bisect_right(self.times, t)
        if k == "hook":
            return self.hook(age, s["cues"][1][2] - s["start"])
        if k == "overview":
            p = ease(age / 0.85)
            if p < 1:
                hook = self.scenes[sid - 1]
                return Image.blend(
                    self.hook(hook["end"], hook["cues"][1][2]), self.overview(), p
                )
            return self.overview()
        if k == "gateway_overview":
            return self.guide_frame(s["cluster"], self.guide_region(s, t))
        if k == "interest":
            return self.interest_frame()
        if k == "bridge":
            return self.bridge(sid, n, t)
        if k == "complete":
            p = ease(age / 1.05)
            if p < 1:
                # Draw the grid in its actual interpolated slots; its cards remain legible.
                im, _ = self.base(sid, 24, p)
                if p < 0.99:
                    previous = self.selection(sid - 1, 24, s["start"] - 0.01)
                    edge = round(mix(566, 42, p))
                    if edge > 52:
                        im = im.copy()
                        region = previous.crop((0, 110, 566, 1005))
                        region = region.resize((edge, 895), Image.Resampling.BILINEAR)
                        im.paste(
                            Image.blend(
                                region, Image.new("RGB", region.size, PAPER), p
                            ),
                            (0, 110),
                        )
                return im
            # Anchor each pass to the named word in the continuous final reading.
            words = list(s["highlights"])
            for i, word in enumerate(words):
                start, end = s["word_times"][word]
                stop = end + 0.65
                if i + 1 < len(words):
                    stop = min(stop, s["word_times"][words[i + 1]][0])
                if start <= t < stop:
                    strength = min(ease((t - start) / 0.12), ease((stop - t) / 0.18))
                    return self.base(sid, 24, 1, s["highlights"][word], strength)[0]
            return self.base(sid, 24, 1)[0]
        if k == "invitation":
            im = self.invitation()
            p = ease(age / 1.1)
            if p == 1:
                return im
            last = self.base(sid - 1, 24, 1)[0]
            nx, ny, nw, nh = (
                round(v) for v in tween((0, 0, W, H), (73, 666, 370, 208), p)
            )
            im = im.copy()
            small = last.resize((nw, nh), Image.Resampling.BILINEAR)
            patch = im.crop((nx, ny, nx + nw, ny + nh))
            im.paste(Image.blend(small, patch, ease((p - 0.56) / 0.44)), (nx, ny))
            return im
        return self.selection(sid, n, t)

    def frame_key(self, t):
        sid = min(len(self.ends) - 1, bisect.bisect_right(self.ends, t))
        s = self.scenes[sid]
        n = bisect.bisect_right(self.times, t)
        age = t - s["start"]
        cue = max(0, bisect.bisect_right([c[2] for c in s["cues"]], t) - 1)
        cue_age = t - s["cues"][cue][2]
        k = s["scene"]
        if k == "gateway_overview":
            return sid, self.guide_region(s, t)
        moving = (
            (k == "hook" and (age < 1.6 or (cue == 1 and cue_age < 1.35)))
            or (k == "overview" and age < 0.9)
            or k == "complete"
            or (k == "invitation" and age < 1.15)
            or (k == "bridge" and (age < 1.3 or s["end"] - t < 1.4))
            or (k in (*CLUSTERS, "ACC") and n and t - self.times[n - 1] < 1.25)
        )
        return sid, n, cue, t if moving else None

    def render(self, out):
        cmd = [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "-s",
            f"{W}x{H}",
            "-r",
            str(FPS),
            "-i",
            "-",
            "-i",
            str(out / "voice.wav"),
            "-i",
            str(out / SRT),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-map",
            "2:s:0",
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=eng",
            "-disposition:s:0",
            "0",
            "-c:v",
            "libx264",
            "-threads",
            "4",
            "-preset",
            "veryfast",
            "-crf",
            "18",
            "-vf",
            "scale=out_color_matrix=bt709:out_range=tv",
            "-colorspace",
            "bt709",
            "-color_primaries",
            "bt709",
            "-color_trc",
            "bt709",
            "-color_range",
            "tv",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-af",
            "loudnorm=I=-17:TP=-1.5:LRA=8",
            "-t",
            str(math.ceil(self.ends[-1] * FPS) / FPS),
            "-movflags",
            "+faststart",
            str(out / "UCR-curriculum-pilot.mp4"),
        ]
        with subprocess.Popen(cmd, stdin=subprocess.PIPE) as proc:
            last = None
            for i in range(math.ceil(self.ends[-1] * FPS)):
                t = i / FPS
                key = self.frame_key(t)
                if key != last:
                    data = self.frame(t).tobytes()
                    last = key
                proc.stdin.write(data)
            proc.stdin.close()
            if proc.wait():
                raise RuntimeError("Video encoding failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    Film(args.out / "timing.json").render(args.out)
