"""Synthesize sentence groups locally and record their actual cue times."""

import argparse
import io
import json
import wave
from pathlib import Path

import onnxruntime as ort
from piper import PiperVoice, SynthesisConfig
from piper.config import PiperConfig

HERE = Path(__file__).resolve().parent


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
    story = json.loads((HERE / "storyboard.json").read_text())
    with wave.open(str(args.out / "voice.wav"), "wb") as track:
        track.setparams((1, 2, rate, 0, "NONE", "not compressed"))
        for scene in story:
            scene["start"] = track.tell() / rate
            for cue in scene["cues"]:
                cue.append(track.tell() / rate)
                buf = io.BytesIO()
                with wave.open(buf, "wb") as clip:
                    voice.synthesize_wav(
                        cue[1], clip, SynthesisConfig(length_scale=1.04)
                    )
                buf.seek(0)
                with wave.open(buf, "rb") as clip:
                    track.writeframes(clip.readframes(clip.getnframes()))
                cue.append(track.tell() / rate)
                track.writeframes(bytes(2 * round(rate * 0.42)))
            hold = {"opening": 0.4, "complete": 3.5, "invitation": 2.3}.get(
                scene["scene"], 0.24
            )
            track.writeframes(bytes(2 * round(rate * hold)))
            scene["end"] = track.tell() / rate
    (args.out / "timing.json").write_text(json.dumps(story, indent=2))


if __name__ == "__main__":
    main()
