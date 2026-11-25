"""Synthesize the storyboard with Kokoro Heart and time visual cues against the actual take."""

import argparse
import json
import re
import subprocess
import wave
from pathlib import Path

import numpy as np
import onnxruntime as ort
from kokoro_onnx import Kokoro
from pocketsphinx import Decoder
from subtitles import FILENAME, timed_captions, words, write_srt

HERE = Path(__file__).resolve().parent
RATE = 24000


def word_times(decoder, pcm, rate, text):
    """Align the known script to this cue. Times are relative to its first sample."""
    expected = words(text)
    decoder.set_align_text(" ".join(expected))
    mono = subprocess.run(
        ["ffmpeg", "-v", "error", "-f", "s16le", "-ar", str(rate), "-ac", "1",
         "-i", "-", "-ar", "16000", "-f", "s16le", "-"],
        input=pcm, capture_output=True, check=True,
    ).stdout
    decoder.start_utt()
    decoder.process_raw(mono, False, True)
    decoder.end_utt()
    aligned = [(s.word.split("(")[0], s.start_frame / 100, (s.end_frame + 1) / 100)
               for s in decoder.seg() if not s.word.startswith("<")]
    if [word for word, _, _ in aligned] != expected:
        raise ValueError(f"Could not align spoken cue: {text!r}. Decoded: {aligned}")
    return aligned


def synthesize_cue(voice, text, speed):
    """Read complete sentences in Heart's US voice, keeping the printed script intact."""
    spoken = (text.replace("UCR", "U C R").replace("specialise", "specialize")
              .replace("Industrialisation", "Industrialization").replace("practises", "practices"))
    sentences = []
    for sentence in re.split(r"(?<=[.?!]) +", spoken):
        audio, rate = voice.create(sentence, voice="af_heart", speed=speed, lang="en-us")
        if rate != RATE:
            raise ValueError(f"Unexpected Kokoro sample rate {rate}")
        active = np.flatnonzero(abs(audio) > .003)
        if not active.size:
            raise ValueError(f"Empty narration for {sentence!r}")
        audio = audio[max(0, active[0] - 480):active[-1] + 481]
        sentences.append(np.rint(audio.clip(-1, 32767/32768) * 32768).astype("<i2").tobytes())
    pause = bytes(2 * round(RATE * .32))
    return pause.join(sentences)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("voices", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    opts = ort.SessionOptions()
    opts.intra_op_num_threads = 3
    session = ort.InferenceSession(
        str(args.model), sess_options=opts, providers=["CPUExecutionProvider"]
    )
    voice = Kokoro.from_session(session, str(args.voices))
    rate = RATE
    decoder = Decoder()
    decoder.add_word("specialise", decoder.lookup_word("specialize"), False)
    decoder.add_word("industrialisation", decoder.lookup_word("industrialization"), False)
    decoder.add_word("ucr", "Y UW S IY AA R", True)
    story = json.loads((HERE / "storyboard.json").read_text())
    with wave.open(str(args.out / "voice.wav"), "wb") as track:
        track.setparams((1, 2, rate, 0, "NONE", "not compressed"))
        for scene in story:
            scene["start"] = track.tell() / rate
            scene["captions"] = []
            for index, cue in enumerate(scene["cues"]):
                start = track.tell() / rate
                focus = scene.get("question_focus", {}).get(str(index))
                pcm = synthesize_cue(voice, cue[1], speed=.92 if focus else .97)
                marks = list(scene["highlights"]) if "highlights" in scene else scene.get("sync_words", {}).get(str(index), [])
                aligned = word_times(decoder, pcm, rate, cue[1])
                if focus or marks:
                    for target in ([focus] if focus else []) + marks:
                        [(first, last)] = [(a, b) for w, a, b in aligned if w == target]
                        scene.setdefault("word_times", {})[target] = [start + first, start + last]
                track.writeframes(pcm)
                end = track.tell() / rate
                cue.extend([start, end])
                scene["captions"].extend(timed_captions(cue[1], aligned, start, end))
                track.writeframes(bytes(2 * round(rate * 0.32)))
            hold = {
                "overview": 1.1,
                "interest": 0.6,
                "complete": 0.9,
                "invitation": 3.0,
            }.get(scene["scene"], 0.24)
            track.writeframes(bytes(2 * round(rate * hold)))
            scene["end"] = track.tell() / rate
    (args.out / "timing.json").write_text(json.dumps(story, indent=2))
    write_srt(args.out / FILENAME, story)


if __name__ == "__main__":
    main()
