"""Animate the public programme. Its record owns positions and the workbook owns titles."""

import argparse
import bisect
import json
import math
import subprocess
from functools import lru_cache
from pathlib import Path

import openpyxl
from maps import ASSETS, NAMES, PLUM, CourseMap
from PIL import Image, ImageColor, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
W, H, FPS = 1920, 1080, 24
PAPER, INK, MUTED, RULE = "#F8F5EE", "#2E2D2D", "#5C606B", "#D9D4CC"
LILAC, BLUE, YELLOW = "#D0B7D0", "#C8DFE6", "#FFE1A4"
COLORS = {"BEN": "#9C333D", "GOS": "#77532B", "ENS": "#4A6857", "ACC": PLUM}
URL = "https://ucr.nl/tell-us-about-your-interests/"
VIEW = (492, 320)
VIEW_X, VIEW_Y = 52, 417
GATEWAY, DEPENDENT, OPEN_INTRO, OPEN_ADVANCED = (
    "BENGATE102",
    "BENECON312",
    "BENECON111",
    "ENSDELT312",
)


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
    assert catalog[OPEN_INTRO]["preq1"] == catalog[OPEN_ADVANCED]["preq1"] == "NONE"
    assert OPEN_ADVANCED[-3] == "3" and OPEN_INTRO[-3] == "1"
    assert catalog[DEPENDENT]["preq1"] == GATEWAY
    assert catalog[GATEWAY]["preq1"] == "NONE"
    assert len(semesters) == 6 and all(len(s["courses"]) == 4 for s in semesters)
    slots = {
        c["code"]: (i, j, catalog[c["code"]]["name"])
        for i, s in enumerate(semesters)
        for j, c in enumerate(s["courses"])
    }
    assert len(slots) == 24
    unplanned = {
        c["code"]
        for s in semesters
        for c in s["courses"]
        if not catalog[c["code"]].get(s["term"])
    }
    return (
        record["interests"],
        prog["label"],
        slots,
        [s["label"] for s in semesters],
        unplanned,
    )


def tween(a, b, p):
    return tuple(mix(x, y, p) for x, y in zip(a, b))


class Film:
    def __init__(self, timing):
        self.interest, self.title, self.slots, self.labels, self.unplanned = (
            source_data()
        )
        self.scenes = json.loads(timing.read_text())
        self.ends = [s["end"] for s in self.scenes]
        self.maps = {k: CourseMap(k) for k in ("curriculum", *NAMES)}
        self.map = self.maps["curriculum"]
        for k in NAMES:
            assert {c for c in self.map.boxes if c.startswith(k)} == {
                c for c in self.maps[k].boxes if c.startswith(k)
            }
        self.events = []
        for s in self.scenes:
            for codes, _, start, end in s["cues"]:
                for i, code in enumerate(codes):
                    assert code.startswith(s["scene"]) and code in self.map.boxes
                    assert code in self.source(code).boxes
                    self.events.append(
                        (start + 0.08 + (end - start) * i / len(codes), code)
                    )
        self.times = [t for t, _ in self.events]
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
        # Three subject paths start apart; their coloured blocks join below the question.
        for i, (name, color) in enumerate(
            zip(("Economics", "Psychology", "Politics"), (YELLOW, LILAC, BLUE))
        ):
            intro = ease((age - i * 0.22) / 0.95)
            x = round(mix(95 + i * 600, 396 + i * 375, p))
            y = round(mix(478 + i * 34, 561, p) + 55 * (1 - intro))
            for j in range(3):
                left = x + round(j * mix(27, 0, p))
                top = y + round(j * mix(32, 0, p))
                d.rounded_rectangle(
                    (left, top, left + 370, top + 157),
                    radius=8,
                    fill=color if j == 2 else PLUM,
                    outline=color,
                    width=3,
                )
            label(d, (left + 30, top + 55), name, 51, PLUM, "serif")
        return im

    @lru_cache(None)
    def overview(self):
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        label(d, (52, 148), "Six academic clusters", 80, PLUM, "serif")
        # The six small silhouettes are taken from the actual six cluster close-ups.
        for i, (k, name) in enumerate(NAMES.items()):
            y = 318 + i * 101
            m = self.maps[k]
            stamp, _ = m.view(m.fit((95, 61)), (95, 61))
            im.paste(stamp, (54, y))
            label(d, (167, y + 14), name, 27, INK)
        size = (1160, 755)
        diagram, _ = self.map.view(self.map.fit(size), size)
        im.paste(diagram, (708, 252))
        return im

    @lru_cache(None)
    def gateway(self, step):
        im = self.shell().copy()
        d = ImageDraw.Draw(im)
        k = "ENS" if step == 2 else "BEN"
        label(d, (52, 150), NAMES[k], 70, PLUM, "serif")
        tag = ["Open course", "Gateway required", "Open advanced course"][step]
        label(d, (62, 325), tag.upper(), 24, COLORS[k], "bold")
        codes = [(OPEN_INTRO,), (GATEWAY, DEPENDENT), (OPEN_ADVANCED,)][step]
        y = 394
        for i, c in enumerate(codes):
            label(d, (62, y), c, 25, COLORS[k], "bold")
            y = (
                paragraph(d, (60, y + 45), self.slots[c][2], 560, 49, 57, "serif", PLUM)
                + 32
            )
            if i == 0 and step == 1:
                label(d, (62, y), "provides the foundation for", 24, MUTED)
                y += 68
        if step != 1:
            label(
                d,
                (62, y + 16),
                ("100-level" if step == 0 else "300-level")
                + "  ·  No gateway required",
                27,
            )
        m = self.maps[k]
        size = (1100, 670)
        # Keep the entire cluster in view while naming the specific relationship alongside it.
        panel, _ = m.view(m.fit(size), size, codes, 0.46)
        im.paste(panel, (767, 274))
        return im

    @lru_cache(None)
    def interest_frame(self):
        im = self.shell().copy()
        size = (1430, 845)
        diagram, _ = self.map.view(self.map.fit(size), size)
        im.paste(diagram, (434, 165))
        d = ImageDraw.Draw(im)
        # The full map's upper-left white space is deliberately reserved for the quotation.
        d.rectangle((52, 165, 900, 516), fill=PAPER)
        label(d, (58, 186), "A student’s interests", 30, PLUM, "bold")
        paragraph(d, (54, 255), "“" + self.interest + "”", 810, 62, 76, "display", PLUM)
        return im

    def grid(self, im, count, expand=0, emphasis=None, strength=0):
        d = ImageDraw.Draw(im)
        start = round(mix(583, 52, expand))
        gap = 16
        width = (1868 - start - 2 * gap) // 3
        visible = {c for _, c in self.events[:count]}
        coords = {}
        for code, (s, r, title) in self.slots.items():
            x = start + (s % 3) * (width + gap)
            y = 219 + (s // 3) * 397
            if r == 0:
                d.rounded_rectangle(
                    (x, y, x + width, y + 380),
                    radius=12,
                    fill="white",
                    outline=RULE,
                    width=2,
                )
                label(d, (x + 16, y + 14), self.labels[s], 26, PLUM, "bold")
                d.line((x + 16, y + 52, x + width - 16, y + 52), fill=RULE, width=1)
            cy = y + 63 + r * 77
            box = (x + 12, cy, x + width - 12, cy + 72)
            coords[code] = box
            if code not in visible:
                d.rounded_rectangle(box, radius=5, fill="#F5F4F1")
                continue
            accent = COLORS[code[:3]]
            fill = "#F8F6F2"
            if code[:3] == emphasis:
                fill = tuple(
                    round(v)
                    for v in tween(
                        ImageColor.getrgb(fill),
                        ImageColor.getrgb(accent),
                        strength * 0.19,
                    )
                )
            d.rounded_rectangle(box, radius=5, fill=fill)
            d.rounded_rectangle(
                (x + 12, cy + 2, x + 17, cy + 69), radius=2, fill=accent
            )
            display_code = code + (" *" if expand and code in self.unplanned else "")
            label(d, (x + 25, cy + 3), display_code, 17, accent, "bold")
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
                    (x + 25, cy + 24 + j * leading),
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
        label(d, (x, 138), self.title, round(mix(43, 56, expand)), PLUM, "serif")
        d.text((1866, 160), f"{count} / 24", font=font(23), fill=MUTED, anchor="rm")
        coords = self.grid(im, count, expand, emphasis, strength)
        if k == "complete":
            note = "Illustrative schedule."
            if self.unplanned:
                note += (
                    "  * These courses have no planned offering in the semester shown."
                )
            label(d, (52, 1020), note, 24, MUTED)
        else:
            section = (
                "Across clusters"
                if k == "bridge"
                else ("Academic core" if k == "ACC" else NAMES[k])
            )
            label(d, (52, 143), section, 26, COLORS.get(k, PLUM), "bold")
            paragraph(d, (50, 211), s["heading"], 490, 51, 59, "serif", PLUM)
            d.line((561, 132, 561, 997), fill=RULE, width=2)
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
        label(d, (52, 786), code, 23, COLORS[code[:3]], "bold")
        paragraph(d, (50, 837), self.slots[code][2], 494, 39, 47, "serif", PLUM)
        cx, cy = centres.get(code, (VIEW[0] / 2, VIEW[1] / 2))
        return VIEW_X + max(0, min(VIEW[0], cx)), VIEW_Y + max(0, min(VIEW[1], cy))

    @lru_cache(maxsize=12)
    def bridge_view(self, stage, fields):
        if stage in NAMES:
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
            y = 789 + 65 * i
            d.rounded_rectangle((52, y + 4, 66, y + 30), radius=3, fill=COLORS[k])
            label(d, (83, y), NAMES[k], 29, PLUM, "bold")
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
        label(d, (65, 210), "What would", 111, PLUM, "display")
        label(d, (65, 341), "you build?", 111, PLUM, "display")
        label(d, (71, 534), "Share your interests with UCR.", 39, INK)
        d.line((72, 623, 1105, 623), fill=RULE, width=2)
        label(d, (71, 666), URL, 37, PLUM, "bold")
        qr = self.qr.resize((550, 550), Image.Resampling.NEAREST)
        im.paste(qr, (1255, 220))
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
        if k == "gateway":
            i = max(0, bisect.bisect_right([c[2] for c in s["cues"]], t) - 1)
            p = ease((t - s["cues"][i][2]) / 0.55)
            old = self.gateway(i - 1) if i else self.overview()
            return Image.blend(old, self.gateway(i), p) if p < 1 else self.gateway(i)
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
            # Briefly tint the contributing courses as the voice names the fields.
            phase = (age - 1.1) / max(1, s["cues"][0][3] - s["start"] - 2.2) * 3
            if 0 <= phase < 3:
                group = ("BEN", "GOS", "ENS")[int(phase)]
                strength = math.sin(math.pi * (phase % 1)) ** 2
                return self.base(sid, 24, 1, group, strength)[0]
            return self.base(sid, 24, 1)[0]
        if k == "invitation":
            im = self.invitation()
            p = ease(age / 1.1)
            if p == 1:
                return im
            last = self.base(sid - 1, 24, 1)[0]
            nx, ny, nw, nh = (
                round(v) for v in tween((0, 0, W, H), (73, 804, 370, 208), p)
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
        moving = (
            (k == "hook" and (age < 1.6 or (cue == 1 and cue_age < 1.35)))
            or (k == "gateway" and cue_age < 0.60)
            or (k == "overview" and age < 0.9)
            or k == "complete"
            or (k == "invitation" and age < 1.15)
            or (k == "bridge" and (age < 1.3 or s["end"] - t < 1.4))
            or (k in (*NAMES, "ACC") and n and t - self.times[n - 1] < 1.25)
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
            "-c:v",
            "libx264",
            "-threads",
            "4",
            "-preset",
            "veryfast",
            "-crf",
            "18",
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
