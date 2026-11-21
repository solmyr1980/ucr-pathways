"""Verify the rendered p-001 pilot against its storyboard and programme."""

import argparse
import io
import json
import math
import subprocess
from array import array
from pathlib import Path

from PIL import Image, ImageChops, ImageStat

from render import Film, FPS, H, HERE, W

FILENAME = "UCR-curriculum-pilot.mp4"
REVIEW_DURATION = 197.208


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-of", "json", str(path)
    ]))["streams"]


def decode(path, *args):
    return subprocess.check_output([
        "ffmpeg", "-nostdin", "-xerror", "-v", "error", "-i", str(path), *args
    ])


def frame(path, time):
    png = subprocess.check_output([
        "ffmpeg", "-nostdin", "-xerror", "-v", "error", "-ss", str(time),
        "-i", str(path), "-frames:v", "1", "-threads", "1", "-f", "image2pipe",
        "-vcodec", "png", "-"
    ])
    return Image.open(io.BytesIO(png)).convert("RGB")


def image_error(a, b):
    return max(ImageStat.Stat(ImageChops.difference(a, b)).mean)


def verify(out, reference=None):
    movie = out / FILENAME
    film = Film(out / "timing.json")
    storyboard = json.loads((HERE / "storyboard.json").read_text())
    assert len(film.scenes) == len(storyboard)
    assert len(film.events) == 24
    video, audio = probe(movie)

    assert (video["codec_name"], video["width"], video["height"],
            video["avg_frame_rate"]) == ("h264", W, H, f"{FPS}/1")
    assert (audio["codec_name"], audio["channels"]) == ("aac", 1)
    duration = float(video["duration"])
    assert abs(duration - REVIEW_DURATION) <= 3
    assert abs(duration - film.ends[-1]) <= 1 / FPS
    assert abs(float(audio["duration"]) - duration) <= 0.1
    assert audio["sample_rate"] == "96000"

    decode(movie, "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-")
    rate = 8000
    samples = array("h", decode(movie, "-map", "0:a:0", "-ar", str(rate),
                                "-c:a", "pcm_s16le", "-f", "s16le", "-"))
    previous_end = 0
    for scene, source in zip(film.scenes, storyboard):
        assert scene["scene"] == source["scene"]
        assert scene["start"] == previous_end < scene["end"]
        assert [cue[:2] for cue in scene["cues"]] == source["cues"]
        previous_cue_end = scene["start"]
        for _, _, start, end in scene["cues"]:
            assert previous_cue_end <= start < end < scene["end"]
            speech = samples[round(start * rate):round(end * rate)]
            assert max(map(abs, speech)) > 500, f"Missing narration at {start:.2f}s"
            previous_cue_end = end
        previous_end = scene["end"]

    # Sample the reveal, each thematic scene, card motion and the closing invitation.
    times = [1, 4.25, 8, duration - 2]
    times.extend((scene["start"] + scene["end"]) / 2 for scene in film.scenes[1:-1])
    times.extend(start + 0.7 for start, _ in film.events)
    for time in times:
        timestamp = math.ceil(time * FPS) / FPS
        difference = image_error(frame(movie, timestamp), film.frame(timestamp))
        assert difference < 3, f"Unexpected frame at {timestamp:.2f}s ({difference:.2f})"

    # Compare every encoded card with its position in the rendered programme.
    final = next(scene for scene in film.scenes if scene["scene"] == "complete")
    grid, boxes = film.base(film.scenes.index(final), 24)
    actual = frame(movie, (final["start"] + final["end"]) / 2)
    for code, box in boxes.items():
        assert image_error(actual.crop(box), grid.crop(box)) < 4, code

    if reference is not None:
        archived_grid = frame(reference, 183)
        for code, box in boxes.items():
            assert image_error(actual.crop(box), archived_grid.crop(box)) < 6, code
        print("All 24 cards also match the local archived semester grid.")

    print(f"Verified {W} × {H}, {FPS} fps, {duration:.3f} seconds, H.264 with mono AAC.")
    print("The full video and audio decoded, all narration cues contain speech, and all 24 cards match the programme grid.")
    print("Opening reveal, thematic scenes, card motion and closing frames match the storyboard render.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("out", type=Path)
    parser.add_argument("--reference", type=Path, help="Path to the original review MP4")
    args = parser.parse_args()
    verify(args.out, args.reference)
