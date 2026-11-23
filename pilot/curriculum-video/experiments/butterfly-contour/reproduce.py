"""Rebuild the two short review clips from the saved sixth-cut package."""
import argparse
import hashlib
import json
import struct
import subprocess
import tempfile
import zipfile
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator

from contour import ORIGIN, SIZE, draw, overview_curves

HERE = Path(__file__).resolve().parent
DEFAULT_MAP = HERE.parents[3] / "assets/video/curriculum.svg"
MAP_SHA256 = "f30896fb79625b7f3fa67b6e10455a85f345c6d80d37f6c55704aa454735a43d"
BASELINE = {
    "UCR-curriculum-cut-6.mp4": "93ce02e7d7912a338c00e2d754fddac55c972aaa05d63933a1bdbe8786285ddd",
    "UCR-curriculum-cut-6.en.srt": "f14d51ccd57f7c935654926917a43807fbc609ba7657ae055da64738e6cdde09",
}
FPS, AUDIO_RATE = 24, 96000
START, INSERT, END = 410, 954, 1128  # Zero-based frames in cut six. END is exclusive.
OVERVIEW, INSERT_FRAMES, LEAD = 672, 168, 0.25
CAPTION_1 = "You can think of it as a butterfly:"
CAPTION_2 = "a spine in the middle, with two wings."


def ffmpeg(*args):
    return ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)]


def render_trace(filename, curves, words):
    marks = {word: (start, end) for word, start, end in words}
    times = [marks["think"][0], marks["butterfly"][0], marks["butterfly"][1] + .05,
             marks["middle"][1], marks["wings"][0], marks["wings"][1] + .08]
    wings = PchipInterpolator(times, [0, .105, .39, .56, .84, 1])
    spine_times = [marks["spine"][0] - .1, marks["spine"][0] + .15, marks["middle"][1] + .04]
    spine = PchipInterpolator(spine_times, [0, .24, 1])

    @lru_cache(maxsize=2)
    def pixels(wing_length, spine_length, opacity):
        if (wing_length == 0 and spine_length == 0) or opacity == 0:
            return bytes(SIZE[0] * SIZE[1] * 4)
        return draw(curves, wing_length, spine_length, opacity).tobytes()

    cmd = ffmpeg("-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{SIZE[0]}x{SIZE[1]}",
                 "-r", FPS, "-i", "-", "-c:v", "qtrle", "-threads", 2, "-pix_fmt", "argb", filename)
    with subprocess.Popen(cmd, stdin=subprocess.PIPE) as encoder:
        for frame in range(INSERT_FRAMES):
            t = frame / FPS - LEAD
            wing_length = float(wings(np.clip(t, times[0], times[-1])))
            spine_length = float(spine(np.clip(t, spine_times[0], spine_times[-1])))
            fade = np.clip((t - times[-1] - 1.05) / .57, 0, 1)
            opacity = 1 - fade * fade * (3 - 2 * fade)
            encoder.stdin.write(pixels(wing_length, spine_length, opacity))
        encoder.stdin.close()
        if encoder.wait():
            raise RuntimeError("FFmpeg could not encode the contour.")


def seconds(stamp):
    hours, minutes, sec = stamp.replace(",", ".").split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(sec)


def timestamp(sec):
    ms = round(sec * 1000)
    return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"


def write_captions(source, destination, words, prototype):
    start, insert, end = (frame / FPS for frame in (START, INSERT, END))
    cues = []
    for block in source.read_text(encoding="utf-8").strip().split("\n\n"):
        _, timing, *lines = block.splitlines()
        first, last = map(seconds, timing.split(" --> "))
        if start <= first and last <= end:
            offset = -start
            if prototype and first >= insert:
                offset += INSERT_FRAMES / FPS
            cues.append((first + offset, last + offset, "\n".join(lines)))
    if prototype:
        offset = insert - start + LEAD
        cues.extend([(offset + words[0][1], offset + words[7][2], CAPTION_1),
                     (offset + words[8][1], offset + words[-1][2], CAPTION_2)])
    blocks = [f"{i}\n{timestamp(first)} --> {timestamp(last)}\n{text}"
              for i, (first, last, text) in enumerate(sorted(cues), 1)]
    destination.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def mp4_boxes(data, start, end):
    while start < end:
        size, name = struct.unpack_from(">I4s", data, start)
        if size < 8 or start + size > end:
            raise ValueError("Invalid MP4 box in the generated short clip.")
        yield name, start + 8, start + size
        start += size


def make_captions_optional(path):
    # FFmpeg 7.1 enables a sole MOV text track despite -disposition:s:0 0.
    # Clear only track_enabled in the subtitle's tkhd after the new file is muxed.
    data = bytearray(path.read_bytes())
    for kind, left, right in mp4_boxes(data, 0, len(data)):
        if kind != b"moov":
            continue
        for name, x, y in mp4_boxes(data, left, right):
            if name != b"trak":
                continue
            track = {k: (a, b) for k, a, b in mp4_boxes(data, x, y)}
            media = {k: (a, b) for k, a, b in mp4_boxes(data, *track[b"mdia"])}
            handler = media[b"hdlr"][0]
            if data[handler + 8:handler + 12] in (b"sbtl", b"text", b"subt"):
                data[track[b"tkhd"][0] + 3] &= 0xfe
                path.write_bytes(data)
                return
    raise ValueError("Generated MP4 lacks an English subtitle track.")


def export(work, out, words, prototype):
    video = work / "UCR-curriculum-cut-6.mp4"
    srt = work / "excerpt.srt"
    write_captions(work / "UCR-curriculum-cut-6.en.srt", srt, words, prototype)
    samples = AUDIO_RATE // FPS
    if prototype:
        inputs = ["-i", video, "-i", work / "trace.mov", "-i", HERE / "narration.wav", "-i", srt]
        streams = [
            f"[0:v]trim=start_frame={START}:end_frame={INSERT},setpts=PTS-STARTPTS[v1]",
            f"[0:v]select=eq(n\\,{OVERVIEW}),trim=end_frame=1,setpts=PTS-STARTPTS,"
            f"tpad=stop_mode=clone:stop={INSERT_FRAMES-1},setpts=N/({FPS}*TB)[base]",
            f"[base][1:v]overlay=x={ORIGIN[0]}:y={ORIGIN[1]}:alpha=straight:format=yuv420:shortest=1[v2]",
            f"[0:v]trim=start_frame={INSERT}:end_frame={END},setpts=PTS-STARTPTS[v3]",
            "[v1][v2][v3]concat=n=3:v=1:a=0[v]",
            f"[0:a]atrim=start_sample={START*samples}:end_sample={INSERT*samples},asetpts=PTS-STARTPTS[a1]",
            f"[2:a]aresample={AUDIO_RATE},volume=-3.7dB,adelay={round(LEAD*AUDIO_RATE)}S,apad,"
            f"atrim=end_sample={INSERT_FRAMES*samples},asetpts=PTS-STARTPTS[a2]",
            f"[0:a]atrim=start_sample={INSERT*samples}:end_sample={END*samples},asetpts=PTS-STARTPTS[a3]",
            "[a1][a2][a3]concat=n=3:v=0:a=1[a]",
        ]
        subtitle_stream = "3:s:0"
        output = out / "UCR-butterfly-contour-prototype.mp4"
    else:
        inputs = ["-i", video, "-i", srt]
        streams = [f"[0:v]trim=start_frame={START}:end_frame={END},setpts=PTS-STARTPTS[v]",
                   f"[0:a]atrim=start_sample={START*samples}:end_sample={END*samples},asetpts=PTS-STARTPTS[a]"]
        subtitle_stream = "1:s:0"
        output = out / "UCR-sixth-cut-comparison.mp4"
    subprocess.run(ffmpeg(*inputs, "-filter_complex_threads", 3, "-filter_complex", ";".join(streams),
        "-map", "[v]", "-map", "[a]", "-map", subtitle_stream, "-r", FPS, "-fps_mode:v", "cfr",
        "-enc_time_base:v", "1:24", "-c:v", "libx264", "-threads", 4, "-preset", "fast", "-crf", 13,
        "-pix_fmt", "yuv420p", "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709",
        "-color_trc", "bt709", "-c:a", "aac", "-ar", 48000, "-ac", 1, "-b:a", "160k", "-c:s", "mov_text",
        "-metadata:s:s:0", "language=eng", "-metadata:s:s:0", "handler_name=English",
        "-disposition:s:0", "0", "-movflags", "+faststart", output), check=True)
    make_captions_optional(output)
    print(f"{hashlib.sha256(output.read_bytes()).hexdigest()}  {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Original cut-six YouTube package ZIP")
    parser.add_argument("output", type=Path, help="Directory for the two rebuilt review clips")
    parser.add_argument("--map", type=Path, default=DEFAULT_MAP, help="Cut-six curriculum.svg")
    args = parser.parse_args()
    if hashlib.sha256(args.map.read_bytes()).hexdigest() != MAP_SHA256:
        parser.error("The overview asset differs from the sixth cut. See README for the pinned map.")
    words = json.loads((HERE / "spoken.json").read_text(encoding="utf-8"))
    curves = overview_curves(args.map)
    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(args.package) as package:
        work = Path(tmp)
        for name, digest in BASELINE.items():
            data = package.read(name)
            if hashlib.sha256(data).hexdigest() != digest:
                parser.error(f"{name} differs from the reviewed baseline.")
            (work / name).write_bytes(data)
        render_trace(work / "trace.mov", curves, words)
        export(work, args.output, words, prototype=True)
        export(work, args.output, words, prototype=False)


if __name__ == "__main__":
    main()
