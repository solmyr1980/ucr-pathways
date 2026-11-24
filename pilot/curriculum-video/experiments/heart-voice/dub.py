"""Dub the reviewed sixth cut using Kokoro Heart on the original picture timeline."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

import numpy as np
import onnxruntime as ort
import soundfile as sf
from kokoro_onnx import Kokoro
from pocketsphinx import Decoder
from scipy.signal import resample_poly

PILOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PILOT))
from subtitles import words

RATE = 24000
BASELINE_SHA = "93ce02e7d7912a338c00e2d754fddac55c972aaa05d63933a1bdbe8786285ddd"


def run(*args):
    return subprocess.run(list(map(str, args)), check=True, capture_output=True).stdout


def read_captions(srt):
    def seconds(stamp):
        h, m, s = stamp.replace(",", ".").split(":")
        return 3600 * int(h) + 60 * int(m) + float(s)

    captions = []
    for block in srt.read_text(encoding="utf-8-sig").strip().split("\n\n"):
        _, times, *lines = block.splitlines()
        start, end = map(seconds, times.split(" --> "))
        captions.append((start, end, " ".join(lines)))
    return captions


def align(decoder, audio, text):
    """Align words independently in one short passage, in seconds."""
    expected = words(text)
    decoder.set_align_text(" ".join(expected))
    decoder.start_utt()
    pcm = resample_poly(audio, 2, 3)
    decoder.process_raw(np.rint(pcm.clip(-1, .99996) * 32768).astype("<i2").tobytes(), False, True)
    decoder.end_utt()
    result = [(s.word.split("(")[0], s.start_frame / 100, (s.end_frame + 1) / 100)
              for s in decoder.seg() if not s.word.startswith("<")]
    if [w for w, _, _ in result] != expected:
        raise ValueError(f"Alignment failed for {text}: {result}")
    return result


def reference_sentences(story, captions, original, decoder):
    cue_list = []
    i = 0
    for scene in story:
        for k, (_, text) in enumerate(scene["cues"]):
            cap_start = i
            printed = []
            starts = set()
            while len(printed) < len(words(text)):
                starts.add(len(printed))
                printed.extend(words(captions[i][2]))
                i += 1
            if printed != words(text):
                raise ValueError(f"Subtitle and storyboard disagree at {text}")
            visual_words = set(scene.get("highlights", {}))
            visual_words.update(scene.get("sync_words", {}).get(str(k), []))
            cue_list.append((text, starts, visual_words, cap_start, i - 1))
    assert i == len(captions)
    for index, (text, starts, visual_words, first, last) in enumerate(cue_list):
        left = (captions[first-1][1] + captions[first][0]) / 2 if index else 0
        right = ((captions[last][1] + captions[last+1][0]) / 2
                 if last + 1 < len(captions) else captions[last][1] + .25)
        aligned = align(decoder, original[round(left*RATE):round(right*RATE)], text)
        first_word = 0
        for sentence in re.split(r"(?<=[.!?])\s+", text):
            end_word = first_word + len(words(sentence))
            marks = aligned[first_word:end_word]
            # Reserve a short margin for soft consonants. Never overlap neighbouring sentences.
            previous = aligned[first_word-1][2] if first_word else 0
            following = aligned[end_word][1] if end_word < len(aligned) else right-left
            onset = left + max((previous + marks[0][1])/2, marks[0][1] - .035)
            end = left + min((following + marks[-1][2])/2, marks[-1][2] + .035)
            anchors = {n: left + t for n, (word, t, _) in enumerate(marks)
                       if n and (word in visual_words or first_word + n in starts)}
            yield sentence, onset, end, anchors
            first_word = end_word


def read_sentence(model, text, speed):
    # The US lexicon uses these spellings and the audience hears the institution's initials.
    spoken = (text.replace("UCR", "U C R").replace("specialise", "specialize")
              .replace("Industrialisation", "Industrialization").replace("practises", "practices"))
    audio, rate = model.create(spoken, voice="af_heart", lang="en-us", speed=speed)
    assert rate == RATE
    energetic = np.flatnonzero(abs(audio) > .003)
    return audio[max(0, energetic[0] - 480):energetic[-1] + 481]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("original", "captions", "model", "voices", "work"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--rubberband", default="rubberband")
    args = parser.parse_args()
    if hashlib.sha256(args.original.read_bytes()).hexdigest() != BASELINE_SHA:
        raise ValueError("Expected the approved sixth-cut MP4.")
    args.work.mkdir(parents=True, exist_ok=True)
    out = args.work / "UCR-curriculum-cut-6-Heart.mp4"
    options = ort.SessionOptions()
    options.intra_op_num_threads = 3
    engine = Kokoro.from_session(ort.InferenceSession(str(args.model), options,
                                 providers=["CPUExecutionProvider"]), str(args.voices))
    decoder = Decoder()
    for british, american in (("specialise", "specialize"), ("industrialisation", "industrialization")):
        decoder.add_word(british, decoder.lookup_word(american), False)
    decoder.add_word("ucr", "Y UW S IY AA R", True)
    pcm = run("ffmpeg", "-v", "error", "-i", args.original, "-vn", "-ar", RATE,
              "-ac", 1, "-f", "f32le", "-")
    original = np.frombuffer(pcm, dtype="<f4")
    seconds = float(run("ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=duration", "-of", "csv=p=0", args.original))
    track = np.zeros(round(seconds * RATE), dtype=np.float32)
    story = json.loads((PILOT / "storyboard.json").read_text())
    captions = read_captions(args.captions)
    report = []
    for i, (text, start, end, anchors) in enumerate(reference_sentences(story, captions, original, decoder)):
        first, last = round(start * RATE), round(end * RATE)
        count = last - first
        speed = .97
        raw = read_sentence(engine, text, speed)
        if abs(len(raw) / count - 1) > .10:
            speed = float(np.clip(speed * len(raw) / count, .80, 1.22))
            raw = read_sentence(engine, text, speed)
        stem = args.work / f"line-{i+1:02}"
        sf.write(stem.with_suffix(".wav"), raw, RATE, subtype="FLOAT")
        keys = []
        if anchors:
            marks = align(decoder, raw, text)
            keys = [(round(marks[n][1] * RATE), round((target - start) * RATE))
                    for n, target in anchors.items()]
        mapping = stem.with_suffix(".map")
        mapping.write_text("".join(f"{x} {y}\n" for x, y in keys))
        output = stem.with_suffix(".fit.wav")
        command = [args.rubberband, "-3", "-q", "-D", str(count/RATE)]
        if keys:
            command.extend(["-M", mapping])
        run(*command, stem.with_suffix(".wav"), output)
        audio, rate = sf.read(output, dtype="float32")
        assert rate == RATE and abs(len(audio) - count) <= 2
        track[first:last] = np.pad(audio[:count], (0, max(0, count-len(audio))))
        report.append(dict(text=text, start=start, end=end, speed=speed, ratio=count/len(raw),
                           anchors={text_index: target for text_index, target in anchors.items()}))
        print(f"{i+1:02} {start:.2f}–{end:.2f} {count/len(raw):.3f} {text}", flush=True)
    (args.work / "timing.json").write_text(json.dumps(report, indent=2))
    voice = args.work / "heart.wav"
    sf.write(voice, track, RATE, subtype="PCM_24")
    run("ffmpeg", "-v", "error", "-y", "-i", args.original, "-i", voice, "-i", args.captions,
        "-map", "0:v:0", "-map", "1:a:0", "-map", "2:s:0", "-c:v", "copy",
        "-af", f"loudnorm=I=-17.2:TP=-1.5:LRA=8,aresample=96000,atrim=end_sample={round(seconds * 96000)},asetpts=N/SR/TB", "-c:a", "aac", "-b:a", "160k",
        "-ar", 96000, "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
        "-disposition:s:0", "0", "-movflags", "+faststart", out)


if __name__ == "__main__":
    main()
