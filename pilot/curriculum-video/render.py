"""Render the public pilot. The record owns positions, the workbook owns titles."""

import argparse
import bisect
import json
import math
import subprocess
from functools import lru_cache
from pathlib import Path

import openpyxl
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
W, H, FPS = 1920, 1080, 24
PLUM, INK, MUTED = "#482438", "#252329", "#615B60"
PAPER, RULE = "#FAF9F7", "#DBD6D4"
COLORS = {"BEN": "#A33541", "GOS": "#785322", "ENS": "#53683A", "ACC": PLUM}
NAMES = {
    "BEN": "Business & Entrepreneurship",
    "GOS": "Government & Society",
    "ENS": "Environment & Sustainability",
    "ACC": "Academic core",
}
# Left/top edge of real PNG tiles, measured at native 1440 x 765 resolution.
TILES = {
    "BENECON111": (721, 341),
    "BENECON211": (894, 341),
    "BENECON212": (981, 341),
    "BENECON311": (1067, 341),
    "BENECON314": (1240, 341),
    "BENECON312": (1153, 341),
    "BENGATE101": (807, 81, 85, 249),
    "BENBUSI112": (635, 81),
    "BENBUSI211": (721, 81),
    "BENBUSI312": (981, 81),
    "BENENTR312": (1067, 211),
    "BENGATE102": (807, 341, 85, 379),
    "GOSPOLI111": (289, 471),
    "GOSPOLI112": (375, 471),
    "GOSPOLI212": (462, 471),
    "GOSPOLI311": (548, 471),
    "GOSGATE102": (807, 81, 85, 639),
    "GOSPOLI313": (721, 471),
    "GOSHIST111": (289, 211),
    "GOSHIST211": (462, 211),
    "GOSHIST312": (721, 211),
    "GOSSOCI212": (462, 601),
    "ENSDELT312": (721, 297, 84, 99),
    "ACCPPDE101": (807, 44, 85, 26),
}


@lru_cache(None)
def font(size, kind="regular"):
    files = {
        "regular": "open-sans/OpenSans-Regular",
        "bold": "open-sans/OpenSans-Semibold",
        "serif": "dejavu/DejaVuSerif",
        "italic": "liberation/LiberationSerif-Italic",
    }
    return ImageFont.truetype("/usr/share/fonts/truetype/" + files[kind] + ".ttf", size)


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


def rect(code):
    x, y, *size = TILES[code]
    w, h = size or (84, 119)
    return x, y, w, h


def source_data():
    record = json.loads((ROOT / "data/examples/p-001.json").read_text())
    prog = next(p for p in record["programmes"] if p["id"] == "ucr-depth")
    semesters = prog["schedule"]["semesters"]
    book = openpyxl.load_workbook(
        ROOT / "data/reference/ucr_courses_enriched.xlsx", read_only=True
    )
    rows = iter(book.active.values)
    keys = next(rows)
    titles = {r[keys.index("osiris")]: r[keys.index("name")] for r in rows}
    book.close()
    assert len(semesters) == 6 and all(len(s["courses"]) == 4 for s in semesters)
    slots = {
        c["code"]: (i, j, titles[c["code"]])
        for i, s in enumerate(semesters)
        for j, c in enumerate(s["courses"])
    }
    assert len(slots) == 24 and set(slots) == set(TILES)
    return record["interests"], prog["label"], slots


class Film:
    def __init__(self, timing):
        self.interest, self.title, self.slots = source_data()
        self.scenes = json.loads(timing.read_text())
        self.ends = [s["end"] for s in self.scenes]
        self.images = {
            k: Image.open(ROOT / "assets/video" / (k + ".png")).convert("RGB")
            for k in ("BEN", "GOS", "ENS", "curriculum")
        }
        assert all(im.size == (1440, 765) for im in self.images.values())
        self.events = []
        for s in self.scenes:
            for codes, _, start, end in s["cues"]:
                for i, code in enumerate(codes):
                    assert code.startswith(s["scene"])
                    self.events.append(
                        (start + 0.08 + (end - start) * i / len(codes), code)
                    )
        self.times = [t for t, _ in self.events]
        assert sorted(c for t, c in self.events) == sorted(self.slots)

    def shell(self):
        im = Image.new("RGB", (W, H), PAPER)
        d = ImageDraw.Draw(im)
        label(d, (52, 32), "University College Roosevelt", 30, PLUM, "serif")
        label(d, (1530, 39), "LIBERAL ARTS & SCIENCES", 22, MUTED, "bold")
        d.line((52, 86, 1868, 86), fill=RULE, width=2)
        return im

    @lru_cache(None)
    def opening(self, end=False):
        im = self.shell()
        d = ImageDraw.Draw(im)
        d.rectangle((52, 120, 1868, 1016), fill="white")
        diagram = self.images["curriculum"].crop((99, 41, 1334, 757))
        diagram.thumbnail((1250, 800), Image.Resampling.LANCZOS)
        im.paste(diagram, (580, 222))
        # Use the natural white space above the left wing for the student's words.
        label(
            d,
            (100, 183),
            "THE STUDENT’S INTERESTS" if not end else "YOUR INTERESTS",
            23,
            PLUM,
            "bold",
        )
        value = (
            "“" + self.interest + "”" if not end else "What would you like to explore?"
        )
        paragraph(d, (96, 255), value, 725, 58, 76, "serif", PLUM)
        if end:
            paragraph(
                d,
                (102, 556),
                "Submit your interests to explore a possible UCR programme.",
                570,
                32,
                45,
            )
        return im

    @lru_cache(None)
    def intro_close(self):
        im = self.shell()
        d = ImageDraw.Draw(im)
        label(d, (76, 220), "BUSINESS & ENTREPRENEURSHIP", 23, COLORS["BEN"], "bold")
        paragraph(d, (70, 289), "“" + self.interest + "”", 730, 56, 74, "serif", PLUM)
        tilemap = (
            self.images["BEN"]
            .crop((625, 72, 1335, 730))
            .resize((872, 808), Image.Resampling.LANCZOS)
        )
        im.paste(tilemap, (920, 145))
        return im

    def grid(self, im, count, large=False):
        d = ImageDraw.Draw(im)
        start = 52 if large else 576
        gap = 16
        width = (1868 - start - 2 * gap) // 3
        visible = {code for _, code in self.events[:count]}
        coords = {}
        for code, (s, r, title) in self.slots.items():
            x = start + (s % 3) * (width + gap)
            y = 211 + (s // 3) * 416
            if r == 0:
                d.rounded_rectangle(
                    (x, y, x + width, y + 400),
                    radius=14,
                    fill="white",
                    outline=RULE,
                    width=2,
                )
                label(
                    d,
                    (x + 16, y + 16),
                    f"Year {s//2+1}  ·  Semester {s%2+1}",
                    26,
                    PLUM,
                    "bold",
                )
            cy = y + 61 + 82 * r
            coords[code] = (x + 14, cy, x + width - 14, cy + 75)
            if code not in visible:
                d.rounded_rectangle(coords[code], radius=6, fill="#F5F3F1")
                continue
            accent = COLORS[code[:3]]
            d.rounded_rectangle(coords[code], radius=6, fill="#F6F3F1")
            d.rectangle((x + 14, cy + 5, x + 18, cy + 70), fill=accent)
            label(d, (x + 27, cy + 5), code, 16, accent, "bold")
            size = 27 if large else 24
            while len(lines(title, width - 52, size, "bold")) > 2:
                size -= 1
            assert size >= 21
            paragraph(d, (x + 27, cy + 26), title, width - 52, size, 25, "bold")
        return coords

    @lru_cache(maxsize=3)
    def base(self, sid, count):
        s = self.scenes[sid]
        complete = s["scene"] == "complete"
        im = self.shell()
        d = ImageDraw.Draw(im)
        label(
            d,
            (52 if complete else 576, 123),
            self.title,
            46 if complete else 42,
            PLUM,
            "serif",
        )
        coords = self.grid(im, count, complete)
        if complete:
            label(
                d,
                (52, 1043),
                "Illustrative programme. Course availability varies by semester.",
                20,
                MUTED,
            )
        else:
            k = s["scene"]
            label(d, (52, 133), NAMES[k].upper(), 21, COLORS[k], "bold")
            paragraph(d, (49, 194), s["heading"], 485, 46, 56, "serif", PLUM)
            d.line((551, 121, 551, 1019), fill=RULE, width=2)
        return im, coords

    def focus(self, im, code, prev, p):
        k = code[:3]
        x, y, w, h = rect(code)
        cx, cy = x + w / 2, y + h / 2
        if prev and prev[:3] == k:
            ox, oy, ow, oh = rect(prev)
            cx, cy = mix(ox + ow / 2, cx, p), mix(oy + oh / 2, cy, p)
        src = self.images["curriculum" if k == "ACC" else k]
        z = 2.25 if k == "ACC" else 1.55
        vw, vh = 484, 338
        left = max(0, min(src.width - vw / z, cx - vw / z / 2))
        top = max(0, min(src.height - vh / z, cy - vh / z / 2))
        crop = src.transform(
            (vw, vh),
            Image.Transform.EXTENT,
            (left, top, left + vw / z, top + vh / z),
            Image.Resampling.BICUBIC,
        )
        box = [
            round((x - left) * z),
            round((y - top) * z),
            round((x + w - left) * z) - 1,
            round((y + h - top) * z) - 1,
        ]
        # Dim surrounding tiles, preserving the original ink and gateway colour inside the focus.
        dim = Image.blend(crop, Image.new("RGB", crop.size, "white"), 0.57)
        dim.paste(crop.crop(tuple(box[:2] + [box[2] + 1, box[3] + 1])), tuple(box[:2]))
        cd = ImageDraw.Draw(dim)
        cd.rectangle(box, outline=PLUM, width=4)
        im.paste(dim, (52, 392))
        d = ImageDraw.Draw(im)
        d.rectangle((51, 391, 536, 730), outline=RULE, width=2)
        label(d, (52, 777), code, 21, COLORS[k], "bold")
        paragraph(d, (50, 822), self.slots[code][2], 480, 39, 48, "serif", PLUM)
        return (
            52 + max(0, min(vw, (x + w / 2 - left) * z)),
            392 + max(0, min(vh, (y + h / 2 - top) * z)),
        )

    def frame(self, t):
        sid = min(len(self.ends) - 1, bisect.bisect_right(self.ends, t))
        s = self.scenes[sid]
        k = s["scene"]
        if k == "opening":
            # Shrink the BEN close-up into its position in the revealed butterfly.
            u = ease((t - 3.3) / 2.1)
            if u == 0:
                return self.intro_close()
            if u == 1:
                return self.opening()
            im = Image.blend(self.intro_close(), self.opening(), u)
            src = self.images["BEN"].crop((625, 72, 1335, 730))
            scale = mix(1, 0.44, u)
            dims = (round(872 * scale), round(808 * scale))
            overlay = src.resize(dims, Image.Resampling.BILINEAR)
            patch = im.crop(
                (
                    round(mix(920, 1210, u)),
                    round(mix(145, 259, u)),
                    round(mix(920, 1210, u)) + dims[0],
                    round(mix(145, 259, u)) + dims[1],
                )
            )
            im.paste(
                Image.blend(patch, overlay, 1 - u),
                (round(mix(920, 1210, u)), round(mix(145, 259, u))),
            )
            return im
        if k == "invitation":
            return self.opening(True)
        if k == "complete":
            return self.base(sid, 24)[0]
        n = bisect.bisect_right(self.times, t)
        if n == 0 or self.events[n - 1][1][:3] != k:
            code = next(c for st, c in self.events if st >= s["start"])
            prev = None
            age = 0
        else:
            start, code = self.events[n - 1]
            prev = self.events[n - 2][1] if n >= 2 else None
            age = t - start
        p = ease(age / 0.72)
        arrived = age >= 1.2 or n == 0 or self.events[n - 1][1] != code
        base, boxes = self.base(sid, n if arrived else n - 1)
        im = base.copy()
        origin = self.focus(im, code, prev, p)
        if not arrived:
            x, y, x2, y2 = boxes[code]
            dest = (x + 10, (y + y2) / 2)
            flight = ease((age - 0.32) / 0.88)
            px = mix(origin[0], dest[0], flight)
            py = mix(origin[1], dest[1], flight) - 65 * math.sin(math.pi * flight)
            d = ImageDraw.Draw(im)
            if flight > 0:
                # Carry the actual card from the source tile into its fixed slot.
                card = self.base(sid, n)[0].crop((x, y, x2 + 1, y2 + 1))
                scale = mix(0.36, 1, flight)
                card = card.resize(
                    (round(card.width * scale), round(card.height * scale)),
                    Image.Resampling.BILINEAR,
                )
                im.paste(
                    card,
                    (
                        round(mix(origin[0] - card.width / 2, x, flight)),
                        round(py - card.height / 2),
                    ),
                )
            else:
                d.ellipse(
                    (px - 7, py - 7, px + 7, py + 7),
                    fill=COLORS[k],
                    outline="white",
                    width=2,
                )
        return im

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
            "-movflags",
            "+faststart",
            str(out / "UCR-curriculum-pilot.mp4"),
        ]
        with subprocess.Popen(cmd, stdin=subprocess.PIPE) as proc:
            last = None
            for i in range(math.ceil(self.ends[-1] * FPS)):
                t = i / FPS
                sid = bisect.bisect_right(self.ends, t)
                n = bisect.bisect_right(self.times, t)
                moving = (3.3 <= t <= 5.4) or (n and t - self.times[n - 1] < 1.3)
                key = (sid, n, i if moving else None)
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
