"""Draw the reviewed annotation in the sixth cut's 1920 × 1080 overview coordinates."""
import math
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image, ImageDraw
from svgpathtools import parse_path

# The transparent annotation is cropped to this rectangle in the video frame.
ORIGIN = (724, 174)
SIZE = (1141, 712)
SUPERSAMPLE = 3
WING_STROKES = [((255, 252, 246, 150), 5.2), ((84, 43, 59, 236), 2.7)]
SPINE_STROKES = [((253, 247, 240, 245), 5.0), ((80, 36, 53, 235), 1.8)]


def overview_curves(svg):
    root = ET.parse(svg).getroot()
    _, _, width, height = map(float, root.get("viewBox").split())
    # Film.overview() fits the sheet into this panel with an 8-unit margin.
    scale = min(1160 / (width + 16), 663 / (height + 16))
    ox = 708 + (1160 - width * scale) / 2
    oy = 219 + (663 - height * scale) / 2
    boxes = {}
    for rect in root.findall(".//{*}rect[@data-id]"):
        x, y, w, h = (float(rect.get(k)) for k in ("x", "y", "width", "height"))
        boxes[rect.get("data-id")] = (ox + x * scale, oy + y * scale,
                                      ox + (x + w) * scale, oy + (y + h) * scale)

    x0, y0, x1, _ = boxes["BENGATE101"]
    _, _, _, y1 = boxes["HCBGATE102"]
    _, t2, r2, b2 = boxes["ENSGATE201"]
    # Hand-fitted outer wings follow the occupied areas and turn through the
    # white space below GOS. The lowest open courses reach further left.
    left = f'''M {x0-2} {y0-2}
     C 1312 275 1283 271 1235 257
     C 1168 235 1089 225 1032 224
     C 1012 224 1002 229 996 242
     C 975 291 950 391 908 495
     C 884 557 867 606 893 648
     C 913 679 980 683 1081 685
     C 1143 686 1210 686 1222 693
     C 1230 698 1210 705 1180 711
     C 1090 730 974 739 891 751
     C 821 761 765 776 745 791
     C 733 801 731 812 740 822
     C 768 850 853 874 925 877
     C 1038 883 1252 882 1337 875
     Q 1364 874 1365 870
     L 1365.4 {y1}'''
    right = f'''M {x1+2} {y0-2}
     C 1494 276 1530 276 1567 258
     C 1645 230 1760 220 1814 224
     C 1835 225 1844 233 1845 251
     C 1850 298 1840 355 1840 426
     C 1840 504 1861 564 1838 594
     C 1814 622 1717 614 1613 620
     C 1552 624 1524 627 1524 635
     C 1525 644 1557 650 1600 653
     C 1716 655 1818 673 1839 699
     C 1854 720 1854 751 1838 774
     C 1819 802 1740 805 1669 800
     C 1573 796 1507 779 {x1+2} {y1+3}'''
    # The right edge picks up the adjacent ENS gateway. Both edges stop above No GATE.
    spines = [
        f"M {x0+7} {y0+2} Q {x0+2} {y0+2} {x0+2} {y0+8} "
        f"L {x0+2} {y1-8} Q {x0+2} {y1-2} {x0+7} {y1-2}",
        f"M {x1-7} {y0+2} Q {x1-2} {y0+2} {x1-2} {y0+8} "
        f"L {x1-2} {t2+1.8} L {r2-2} {t2+1.8} L {r2-2} {b2-2} "
        f"L {x1-2} {b2-2} L {x1-2} {y1-8} Q {x1-2} {y1-2} {x1-7} {y1-2}",
    ]
    return [sample_curve(path) for path in (left, right, *spines)]


def sample_curve(path):
    points = []
    for segment in parse_path(path):
        steps = math.ceil(segment.length() / 1.65)
        points.extend(segment.point(k / steps) for k in range(steps))
    points.append(segment.end)
    xy = np.array([(z.real, z.imag) for z in points])
    distance = np.r_[0, np.cumsum(np.linalg.norm(np.diff(xy, axis=0), axis=1))]
    return xy, distance / distance[-1]


def draw(curves, wings, spine, opacity):
    """Return a transparent RGBA crop to composite at ORIGIN."""
    image = Image.new("RGBA", tuple(side * SUPERSAMPLE for side in SIZE))
    pen = ImageDraw.Draw(image)
    for index, (xy, distance) in enumerate(curves):
        is_wing = index < 2
        count = np.searchsorted(distance, wings if is_wing else spine, side="right")
        if count < 2:
            continue
        points = [tuple(p) for p in np.round((xy[:count] - ORIGIN) * SUPERSAMPLE).astype(int)]
        for color, weight in WING_STROKES if is_wing else SPINE_STROKES:
            width = round(weight * SUPERSAMPLE)
            radius = width / 2
            pen.line(points, fill=color, width=width, joint="curve")
            for x, y in (points[0], points[-1]):
                pen.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    image = image.resize(SIZE, Image.Resampling.LANCZOS)
    if opacity < 1:
        image.putalpha(image.getchannel("A").point(lambda a: round(a * opacity)))
    return image
