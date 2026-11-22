"""Render three UCR thumbnail directions as 3840 × 2160 PNGs."""

from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parents[2] / "assets"
SCALE = 3
PLUM, PAPER = "#491E34", "#F8F5EE"
YELLOW, BLUE, LILAC = "#FFE1A4", "#C8DFE6", "#D0B7D0"
SUBJECTS = (("Economics", YELLOW), ("Politics", BLUE), ("History", LILAC))


def pixels(*values):
    return tuple(round(value * SCALE) for value in values)


@lru_cache(None)
def font(size, family):
    return ImageFont.truetype(ASSETS / "fonts" / family, size * SCALE)


class Thumbnail:
    def __init__(self, background):
        self.image = Image.new("RGB", pixels(1280, 720), background)
        self.draw = ImageDraw.Draw(self.image)

    def text(self, x, y, label, size, color, anchor="lt", serif=True):
        face = "IvyMode Semibold.otf" if serif else "Inter_Bold.ttf"
        typeface = font(size, face)
        position = pixels(x, y)
        left, top, right, bottom = self.draw.textbbox(
            position, label, font=typeface, anchor=anchor
        )
        assert 0 <= left < right <= self.image.width, label
        assert 0 <= top < bottom <= self.image.height, label
        self.draw.text(position, label, font=typeface, fill=color, anchor=anchor)

    def box(self, x, y, width, height, radius, fill=None, outline=None, stroke=1):
        self.draw.rounded_rectangle(
            pixels(x, y, x + width, y + height),
            radius=radius * SCALE,
            fill=fill,
            outline=outline,
            width=stroke * SCALE,
        )

    def line(self, coords, color, weight):
        self.draw.line([pixels(*point) for point in coords], fill=color,
                       width=weight * SCALE, joint="curve")

    def logo(self, color):
        source = Image.open(ASSETS / "brand/ucr-primary-plum.png").convert("RGBA")
        mask = source.getchannel("A")
        mask = mask.crop(mask.getbbox())
        width = 250 * SCALE
        mask = mask.resize(
            (width, round(mask.height * width / mask.width)), Image.Resampling.LANCZOS
        )
        self.image.paste(color, pixels(68, 51), mask)

    def grid(self, x, y, card_width, card_height, gap, rows):
        """Block out six semesters and four symbolic course positions per semester."""
        for row in range(2):
            for col in range(3):
                left = x + col * (card_width + gap)
                top = y + row * (card_height + gap)
                self.box(left, top, card_width, card_height, 10, PAPER)
                for slot, color in enumerate(rows[row * 3 + col]):
                    self.box(
                        left + 10, top + 12 + slot * ((card_height - 18) / 4),
                        card_width - 20, (card_height - 34) / 4,
                        3, color or "#E5DDE1",
                    )

    def save(self, name):
        self.image.save(HERE / (name + ".png"), optimize=True)


def disciplines():
    thumbnail = Thumbnail(PLUM)
    thumbnail.logo(PAPER)
    for index, (word, color) in enumerate(SUBJECTS):
        left, top = 104 + 163 * index, 168 + 145 * index
        thumbnail.box(left - 20, top - 16, 667, 129, 10, outline=color, stroke=2)
        thumbnail.box(left, top, 667, 129, 10, fill=color)
        thumbnail.text(left + 334, top + 65, word, 104, PLUM, "mm")
    thumbnail.save("01-disciplines")


def build():
    thumbnail = Thumbnail(PAPER)
    thumbnail.logo(PLUM)
    thumbnail.text(70, 229, "Build your", 112, PLUM)
    thumbnail.text(70, 351, "own degree", 112, PLUM)
    thumbnail.box(716, 123, 481, 449, 29, PLUM)
    thumbnail.grid(
        760, 204, 120, 135, 17,
        ((YELLOW, YELLOW, None, None), (BLUE, None, BLUE, None),
         (LILAC, None, None, None), (YELLOW, BLUE, None, None),
         (LILAC, BLUE, None, None), (None, None, None, None)),
    )
    # A single card is visibly heading toward an empty position in the grid.
    thumbnail.line([(1066, 502), (1153, 502), (1153, 468)], YELLOW, 7)
    thumbnail.line([(1139, 482), (1153, 468), (1167, 482)], YELLOW, 7)
    thumbnail.box(1008, 486, 66, 32, 6, YELLOW)
    thumbnail.save("02-build-your-degree")


def hybrid():
    thumbnail = Thumbnail(PLUM)
    thumbnail.logo(PAPER)
    for index, (word, color) in enumerate(SUBJECTS):
        thumbnail.text(71, 168 + index * 118, word, 109, color)
    thumbnail.text(74, 546, "One degree.", 75, PAPER)
    thumbnail.box(732, 131, 463, 433, 26, PAPER)
    # The three paths carry the cover's subject colors into one programme.
    for index, (_, color) in enumerate(SUBJECTS):
        for layer in (2, 1, 0):
            thumbnail.box(
                779 + 125 * index - layer * 7, 170 - layer * 6,
                116, 52, 6, color if layer == 0 else PAPER, PLUM, 2,
            )
        mid = 837 + 125 * index
        thumbnail.line([(mid, 230), (mid, 260)], PLUM, 4)
        thumbnail.line([(mid - 9, 250), (mid, 260), (mid + 9, 250)], PLUM, 4)
    # Draw the grid on plum so the paper panels remain distinct at small sizes.
    thumbnail.box(760, 270, 408, 268, 13, PLUM)
    thumbnail.grid(
        779, 286, 116, 111, 9,
        ((YELLOW, BLUE, LILAC, YELLOW), (BLUE, LILAC, YELLOW, BLUE),
         (LILAC, YELLOW, BLUE, LILAC), (LILAC, YELLOW, BLUE, YELLOW),
         (YELLOW, BLUE, LILAC, BLUE), (BLUE, LILAC, YELLOW, LILAC)),
    )
    thumbnail.save("03-hybrid")


if __name__ == "__main__":
    disciplines()
    build()
    hybrid()
