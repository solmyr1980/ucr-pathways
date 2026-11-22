"""Render UCR's SVG maps and carry their course coordinates into each camera view."""

import io
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw

ASSETS = Path(__file__).resolve().parents[2] / "assets/video"
CLUSTERS = ("BEN", "DIS", "ENS", "GOS", "HCB", "MCC")
PLUM = "#491E34"


class CourseMap:
    def __init__(self, key):
        path = ASSETS / f"{key}.svg"
        doc = ET.parse(path)
        x0, y0, self.w, self.h = map(float, doc.getroot().get("viewBox").split())
        assert (x0, y0) == (0, 0)
        self.boxes = {}
        for node in doc.findall(".//{*}rect[@data-id]"):
            code = node.get("data-id")
            if code == "No GATE":
                continue
            x, y, w, h = (float(node.get(v)) for v in ("x", "y", "width", "height"))
            assert code not in self.boxes and w > 0 and h > 0
            self.boxes[code] = (x, y, x + w, y + h)
        # Keep the source colours, including the muted gateway-dependent courses.
        data = cairosvg.svg2png(url=str(path), scale=2)
        self.image = Image.open(io.BytesIO(data)).convert("RGB")
        self.scale = self.image.width / self.w

    def view(self, camera, size, selected=(), dim=0.0, outlines=True):
        """Camera and boxes share viewBox units. Return visible highlight centres."""
        x, y, w, h = camera
        width, height = size
        extent = tuple(v * self.scale for v in (x, y, x + w, y + h))
        raw = self.image.transform(
            size,
            Image.Transform.EXTENT,
            extent,
            Image.Resampling.BICUBIC,
            fillcolor="white",
        )
        im = (
            Image.blend(raw, Image.new("RGB", size, "white"), dim)
            if dim
            else raw.copy()
        )
        draw = ImageDraw.Draw(im)
        centres = {}
        for code in selected:
            a, b, c, d = self.boxes[code]
            left, top, right, bottom = (
                round(v)
                for v in (
                    (a - x) * width / w,
                    (b - y) * height / h,
                    (c - x) * width / w,
                    (d - y) * height / h,
                )
            )
            clipped = (
                max(0, left),
                max(0, top),
                min(width, right),
                min(height, bottom),
            )
            if clipped[2] <= clipped[0] or clipped[3] <= clipped[1]:
                continue
            if dim:
                im.paste(raw.crop(clipped), clipped[:2])
            if outlines:
                draw.rectangle(
                    (left, top, right - 1, bottom - 1), outline=PLUM, width=4
                )
            centres[code] = ((left + right) / 2, (top + bottom) / 2)
        return im, centres

    def fit(self, size, codes=None, margin=8):
        boxes = [self.boxes[c] for c in codes] if codes else [(0, 0, self.w, self.h)]
        l, t = min(b[0] for b in boxes) - margin, min(b[1] for b in boxes) - margin
        r, b = max(v[2] for v in boxes) + margin, max(v[3] for v in boxes) + margin
        w = max(r - l, (b - t) * size[0] / size[1])
        h = w * size[1] / size[0]
        return ((l + r - w) / 2, (t + b - h) / 2, w, h)

    def close(self, code, size):
        l, t, r, b = self.boxes[code]
        width = max(225, (r - l) * 2.05)
        height = width * size[1] / size[0]
        # At an edge, keep the neighbouring tiles in view.
        x = max(0, min(self.w - width, (l + r - width) / 2))
        y = max(0, min(self.h - height, (t + b - height) / 2))
        return (x, y, width, height)
