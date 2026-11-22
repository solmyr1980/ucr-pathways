"""Synthesize the storyboard with Alba and time visual cues against the actual take."""

import argparse
import json
import re
import subprocess
import wave
from pathlib import Path

import numpy as np
import onnxruntime as ort
import parselmouth
from parselmouth.praat import call
from piper import PiperVoice, SynthesisConfig
from piper.config import PiperConfig
from pocketsphinx import Decoder
from subtitles import FILENAME, timed_captions, words, write_srt

HERE = Path(__file__).resolve().parent


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


def accent_question(pcm, rate, word_start, word_end):
    """Gently lift the stressed word and return to Alba's own contour on either side."""
    sound = parselmouth.Sound(np.frombuffer(pcm, dtype="<i2") / 32768, rate)
    manipulation = call(sound, "To Manipulation", 0.01, 70, 500)
    tier = call(manipulation, "Extract pitch tier")
    centre = (word_start + word_end) / 2
    width = max(0.08, (word_end - word_start) / 2)
    call(tier, "Formula", f"self * 2^(1.7/12 * exp(-0.5 * ((x-{centre})/{width})^2))")
    call([tier, manipulation], "Replace pitch tier")
    revised = call(manipulation, "Get resynthesis (overlap-add)").values[0]
    samples = np.rint(np.clip(revised, -1, 32767 / 32768) * 32768).astype("<i2")
    assert len(samples) == sound.n_samples
    return samples.tobytes()


def synthesize_cue(voice, text, settings, pronunciations):
    # Keep each sentence's boundary when substituting a short raw Piper phoneme span.
    readings = re.split(r"(?<=[.?!]) +", text) if pronunciations else [text]
    for phrase, phones in pronunciations.items():
        assert text.count(phrase) == 1, phrase
        readings = [s.replace(phrase, f"[[{phones}]]") for s in readings]
    return b"".join(chunk.audio_int16_bytes for reading in readings
                    for chunk in voice.synthesize(reading, settings))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    config = json.loads(Path(str(args.model) + ".json").read_text())
    opts = ort.SessionOptions()
    opts.intra_op_num_threads = 3
    session = ort.InferenceSession(
        str(args.model), sess_options=opts, providers=["CPUExecutionProvider"]
    )
    voice = PiperVoice(session=session, config=PiperConfig.from_dict(config))
    rate = voice.config.sample_rate
    decoder = Decoder()
    decoder.add_word("specialise", decoder.lookup_word("specialize"), False)
    decoder.add_word("industrialisation", decoder.lookup_word("industrialization"), False)
    decoder.add_word("unlocks", decoder.lookup_word("unlock") + " S", False)
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
                settings = SynthesisConfig(length_scale=1.06 if focus else 1.01)
                pronunciations = scene.get("pronunciations", {}).get(str(index), {})
                pcm = synthesize_cue(voice, cue[1], settings, pronunciations)
                marks = list(scene["highlights"]) if "highlights" in scene else scene.get("sync_words", {}).get(str(index), [])
                aligned = word_times(decoder, pcm, rate, cue[1])
                if focus or marks:
                    for target in ([focus] if focus else []) + marks:
                        [(first, last)] = [(a, b) for w, a, b in aligned if w == target]
                        if target == focus:
                            pcm = accent_question(pcm, rate, first, last)
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
