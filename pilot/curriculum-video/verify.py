"""Verify the rendered p-001 pilot against its storyboard and programme."""

import argparse
import bisect
import hashlib
import io
import json
import math
import subprocess
import xml.etree.ElementTree as ET
from array import array
from pathlib import Path

import zxingcpp
from PIL import Image, ImageChops, ImageStat
from render import ASSETS, DEPENDENT, FPS, GATEWAY, HERE, OPEN_COURSE, URL, VIEW, VIEW_X, VIEW_Y, Film, H, W
from subtitles import FILENAME as SRT, stamp

FILENAME = "UCR-curriculum-pilot.mp4"


def probe(path):
    return json.loads(
        subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_streams", "-of", "json", str(path)]
        )
    )["streams"]


def decode(path, *args):
    return subprocess.check_output(
        ["ffmpeg", "-nostdin", "-xerror", "-v", "error", "-i", str(path), *args]
    )


def frame(path, time):
    png = subprocess.check_output(
        [
            "ffmpeg",
            "-nostdin",
            "-xerror",
            "-v",
            "error",
            "-ss",
            str(time),
            "-i",
            str(path),
            "-frames:v",
            "1",
            "-threads",
            "1",
            "-f",
            "image2pipe",
            "-vcodec",
            "png",
            "-",
        ]
    )
    return Image.open(io.BytesIO(png)).convert("RGB")


def image_error(a, b):
    return max(ImageStat.Stat(ImageChops.difference(a, b)).mean)


def compare_encoded(actual, expected, context):
    # H.264 4:2:0 stores only one chroma sample per 2x2 block. Compare text
    # and placement at native-resolution luminance, and colour on an area average.
    small = (max(1, actual.width // 4), max(1, actual.height // 4))
    luma = image_error(actual.convert("L"), expected.convert("L"))
    colour = image_error(
        actual.resize(small, Image.Resampling.BOX),
        expected.resize(small, Image.Resampling.BOX),
    )
    assert luma < 3.5 and colour < 3.5, (
        f"{context}: native luminance MAE={luma:.3f}, area-colour MAE={colour:.3f}"
    )


def verify_subtitles(out, scenes, duration, samples, rate):
    captions = [caption for scene in scenes for caption in scene["captions"]]
    assert captions
    expected = " ".join(cue[1] for scene in scenes for cue in scene["cues"])
    assert " ".join(" ".join(lines) for _, _, lines in captions) == expected
    blocks = (out / SRT).read_text(encoding="utf-8").strip().split("\n\n")
    assert len(blocks) == len(captions)
    previous_end = 0
    peak_speed = 0
    for index, (block, (start, end, lines)) in enumerate(zip(blocks, captions), 1):
        assert block.splitlines() == [str(index), f"{stamp(start)} --> {stamp(end)}", *lines]
        assert previous_end <= start < end <= duration
        assert 1 <= len(lines) <= 2 and all(0 < len(line) <= 42 for line in lines)
        speed = len(" ".join(lines)) / (end - start)
        peak_speed = max(peak_speed, speed)
        assert speed <= 24, (lines, speed)
        speech = samples[round(start * rate):round(end * rate)]
        assert max(map(abs, speech)) > 500, f"Subtitle outside audible speech at {start:.2f}s"
        previous_end = end
    print(f"Verified {len(captions)} English subtitles, exact script text, timing and {peak_speed:.1f} peak characters/second.")


def verify(out):
    movie = out / FILENAME
    film = Film(out / "timing.json")
    storyboard = json.loads((HERE / "storyboard.json").read_text())
    assert len(film.scenes) == len(storyboard)
    assert len(film.events) == 24
    video, audio = probe(movie)

    assert (
        video["codec_name"],
        video["width"],
        video["height"],
        video["avg_frame_rate"],
    ) == ("h264", W, H, f"{FPS}/1")
    assert (audio["codec_name"], audio["channels"]) == ("aac", 1)
    duration = float(video["duration"])
    assert math.isfinite(duration)
    assert abs(duration - film.ends[-1]) <= 1 / FPS
    assert abs(float(audio["duration"]) - duration) <= 0.1
    assert audio["sample_rate"] == "96000"

    decode(movie, "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-")
    rate = 8000
    samples = array(
        "h",
        decode(
            movie,
            "-map",
            "0:a:0",
            "-ar",
            str(rate),
            "-c:a",
            "pcm_s16le",
            "-f",
            "s16le",
            "-",
        ),
    )
    previous_end = 0
    for scene, source in zip(film.scenes, storyboard):
        assert scene["scene"] == source["scene"]
        assert scene["start"] == previous_end < scene["end"]
        assert [cue[:2] for cue in scene["cues"]] == source["cues"]
        previous_cue_end = scene["start"]
        for _, _, start, end in scene["cues"]:
            assert previous_cue_end <= start < end < scene["end"]
            speech = samples[round(start * rate) : round(end * rate)]
            assert max(map(abs, speech)) > 500, f"Missing narration at {start:.2f}s"
            previous_cue_end = end
        previous_end = scene["end"]

    verify_subtitles(out, film.scenes, duration, samples, rate)

    # Use decoded MP4 frames for content, motion, continuity and QR tests.
    def at(time):
        # Seek into a numbered frame, clear of a millisecond rounding boundary.
        index = math.ceil(time * FPS)
        actual = frame(movie, (index - 0.25) / FPS)
        compare_encoded(
            actual, film.frame(index / FPS), f"Frame at {time:.2f}s, index {index}"
        )
        return actual

    for scene in film.scenes:
        at((scene["start"] + scene["end"]) / 2)
        if scene["scene"] == "hook":
            for _, _, start, end in scene["cues"]:
                at((start + end) / 2)
        if scene["scene"] == "bridge":
            frames = [
                at(scene["start"] - 0.15),
                at((scene["start"] + scene["end"]) / 2),
                at(scene["end"] - 0.08),
            ]
            # The atlas changes twice. All previously filled and empty slots stay fixed.
            for current in frames[1:]:
                assert (
                    image_error(
                        frames[0].crop((583, 219, 1868, 998)),
                        current.crop((583, 219, 1868, 998)),
                    )
                    < 2
                )
            assert (
                image_error(
                    frames[1].crop(
                        (VIEW_X, VIEW_Y, VIEW_X + VIEW[0], VIEW_Y + VIEW[1])
                    ),
                    frames[-1].crop(
                        (VIEW_X, VIEW_Y, VIEW_X + VIEW[0], VIEW_Y + VIEW[1])
                    ),
                )
                > 4
            )

    # Check the independent SVG text anchor, the encoded focus at its camera position,
    # and the settled card in its fixed slot for every selection.
    docs = {k: ET.parse(ASSETS / f"{k}.svg") for k in film.maps}
    for i, (start, code) in enumerate(film.events):
        settled = at(start + 1.26)
        motion = at(start + 0.82)
        k = code[:3] if code[:3] != "ACC" else "curriculum"
        m = film.maps[k]
        text = next(n for n in docs[k].findall(".//{*}text") if n.text == code)
        x, y = float(text.get("x")), float(text.get("y"))
        l, t, r, b = m.boxes[code]
        assert l <= x <= r and t <= y <= b, code
        camera = m.close(code, VIEW)
        ax = VIEW_X + (x - camera[0]) * VIEW[0] / camera[2]
        ay = VIEW_Y + (y - camera[1]) * VIEW[1] / camera[3]
        assert VIEW_X <= ax < VIEW_X + VIEW[0] and VIEW_Y <= ay < VIEW_Y + VIEW[1], code
        local = (round(ax) - 3, round(ay) - 16, round(ax) + 25, round(ay) + 1)
        assert (
            image_error(
                settled.crop(local).convert("L"),
                film.frame(math.ceil((start + 1.26) * FPS) / FPS)
                .crop(local)
                .convert("L"),
            )
            < 7
        ), code
        assert image_error(settled, motion) > 0.035, f"No card movement for {code}"
        sid = bisect.bisect_right(film.ends, start + 1.26)
        grid, boxes = film.base(sid, i + 1)
        compare_encoded(
            settled.crop(boxes[code]), grid.crop(boxes[code]), f"Arrival of {code}"
        )

    final = next(s for s in film.scenes if s["scene"] == "complete")
    grid, boxes = film.base(film.scenes.index(final), 24, 1)
    actual = at(final["end"] - 0.1)
    for code, box in boxes.items():
        compare_encoded(actual.crop(box), grid.crop(box), f"Final card {code}")

    # These are disciplinary families in the approved schedule, independent of
    # the storyboard selectors. Sample encoded card backgrounds away from text.
    expected = {"economics": "BENECON", "politics": "GOSPOLI",
                "history": "GOSHIST", "sustainability": "ENSDELT"}
    for word, prefix in expected.items():
        first, last = final["word_times"][word]
        assert final["start"] < first < last < final["end"]
        actual = at((first + last) / 2)
        tinted = set()
        for code, box in boxes.items():
            point = (box[2] - 13, box[3] - 13)
            difference = max(abs(a - b) for a, b in zip(actual.getpixel(point), grid.getpixel(point)))
            if difference > 10:
                tinted.add(code)
        assert tinted == {c for c in boxes if c.startswith(prefix)} and tinted, (word, tinted)
        print(f"{word.capitalize()} spoken at {first:.2f}–{last:.2f}s: {', '.join(sorted(tinted))}")

    assert all(s["scene"] != "gateway" for s in film.scenes)
    gateway = next(s for s in film.scenes if s.get("gateway_demo"))
    events = {code: time for time, code in film.events}
    release = gateway["word_times"]["unlocks"][0]
    assert events[OPEN_COURSE] < events[GATEWAY] < release < events[DEPENDENT]
    locked = at(release - 0.20)
    unlocked = at(release + 0.33)
    state = (52, 333, 544, 401)
    compare_encoded(locked.crop(state), film.course_status("locked"), "Econometrics locked")
    compare_encoded(unlocked.crop(state), film.course_status("unlocked"), "Econometrics unlocked")
    grid_region = (583, 219, 1868, 998)
    compare_encoded(locked.crop(grid_region), unlocked.crop(grid_region), "Grid while Econometrics unlocks")
    open_course = at(events[OPEN_COURSE] + 1.26)
    compare_encoded(open_course.crop(state), film.course_status("open"), "Introduction to Economics open")
    gateway_course = at(events[GATEWAY] + 1.26)
    compare_encoded(gateway_course.crop(state), film.course_status("gateway"), "Research Methods & Statistics gateway")
    for scene in film.scenes:
        if "question_focus" in scene:
            for index, word in scene["question_focus"].items():
                _, question, start, end = scene["cues"][int(index)]
                first, last = scene["word_times"][word]
                assert start <= first < last <= end and question.endswith("?")
                print(f"Question at {start:.2f}–{end:.2f}s, focus on '{word}' at {first:.2f}s.")
    print("Scene starts (seconds):", ", ".join(f"{s['scene']} {s['start']:.2f}" for s in film.scenes))
    print(f"Econometrics unlocks in the accumulating grid at {release:.2f}s.")
    print("Gateway review frames (seconds):", ", ".join(
        f"{code} {events[code]:.2f}" for code in (OPEN_COURSE, GATEWAY, DEPENDENT)
    ))

    for time in (film.scenes[-1]["start"] + 1.3, duration - 1):
        actual = at(time)
        for size in [(W, H), (960, 540)]:
            qr = zxingcpp.read_barcode(actual.resize(size, Image.Resampling.LANCZOS))
            assert qr and qr.text == URL, f"QR mismatch at {time:.2f}s, {size}"

    print(
        f"Verified {W} × {H}, {FPS} fps, {duration:.3f} seconds, H.264 with mono AAC."
    )
    print("Full audio/video decode passed. All measured cues contain speech.")
    print(
        "Verified 24 distinct source labels, card movements, arrivals and final semester positions."
    )
    print(
        "Both transitions retain the same grid. The closing QR decodes to the displayed URL at 1080p and 540p."
    )
    with movie.open("rb") as stream:
        print("MP4 SHA-256:", hashlib.file_digest(stream, "sha256").hexdigest())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    verify(args.out)
