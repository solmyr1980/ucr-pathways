"""Produce an audio-only review of the opening storyboard with OpenVoice V2."""

import argparse
import io
import json
import math
import os
import subprocess
import tempfile
import time
import wave
from pathlib import Path

import numpy as np
import onnxruntime as ort
import soundfile as sf
import torch
from openvoice.api import OpenVoiceBaseClass, ToneColorConverter
from piper import PiperVoice, SynthesisConfig
from piper.config import PiperConfig

STORYBOARD = Path(__file__).resolve().parents[1] / "storyboard.json"
PAUSE_SECONDS = 0.32


class ReviewToneConverter(ToneColorConverter):
    def __init__(self, config_path):
        # The pinned upstream constructor forwards its watermark flag to a base
        # constructor that rejects it. This review explicitly labels WAV files.
        OpenVoiceBaseClass.__init__(self, config_path, device="cpu")
        self.watermark_model = None


def decode_reference(reference_path, folder):
    """Use short windows to average the reference speaker's tone colour."""
    decoded = folder / "reference.wav"
    subprocess.run([
        "ffmpeg", "-nostdin", "-v", "error", "-i", str(reference_path),
        "-map", "0:a:0", "-ac", "1", "-ar", "22050", str(decoded),
    ], check=True)
    audio, rate = sf.read(decoded, dtype="float32")
    duration = len(audio) / rate
    if not 180 <= duration <= 300:
        raise ValueError(f"Use a reviewed 3–5 minute reference (received {duration:.1f} s).")

    clips = []
    count = math.ceil(duration / 12)
    for index, samples in enumerate(np.array_split(audio, count)):
        if np.sqrt(np.mean(samples ** 2)) < 0.005:
            raise ValueError(f"Reference window {index + 1} has very little audio.")
        path = folder / f"reference-{index:02}.wav"
        sf.write(path, samples, rate)
        clips.append(str(path))
    return clips, duration


def synthesize_base(piper_model, cues, folder):
    config_path = piper_model.with_suffix(".onnx.json")
    config = PiperConfig.from_dict(json.loads(config_path.read_text()))
    options = ort.SessionOptions()
    options.intra_op_num_threads = 2
    session = ort.InferenceSession(
        str(piper_model), sess_options=options, providers=["CPUExecutionProvider"]
    )
    voice = PiperVoice(session=session, config=config)

    paths = []
    for index, cue in enumerate(cues):
        path = folder / f"base-{index:02}.wav"
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as clip:
            voice.synthesize_wav(cue, clip, SynthesisConfig(length_scale=1.01))
        path.write_bytes(buffer.getvalue())
        paths.append(str(path))
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("piper_model", type=Path)
    parser.add_argument("converter", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--base-review", type=Path, help="Optional comparison voice WAV")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(int(os.environ.get("OMP_NUM_THREADS", "4")))
    torch.manual_seed(42)

    scenes = json.loads(STORYBOARD.read_text())[:3]
    if [scene["scene"] for scene in scenes] != ["hook", "overview", "gateway"]:
        raise ValueError("The storyboard opening has changed. Review the selection first.")
    cues = [text for scene in scenes for _, text in scene["cues"]]
    start = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="ucr-voice-") as temporary:
        folder = Path(temporary)
        reference_segments, reference_seconds = decode_reference(args.reference, folder)
        base_segments = synthesize_base(args.piper_model, cues, folder)
        converter = ReviewToneConverter(str(args.converter / "config.json"))
        converter.load_ckpt(str(args.converter / "checkpoint.pth"))
        source = converter.extract_se(base_segments)
        target = converter.extract_se(reference_segments)
        before_conversion = time.perf_counter()
        rate = converter.hps.data.sampling_rate
        pause = np.zeros(round(PAUSE_SECONDS * rate), dtype=np.float32)
        clips = []
        cue_metrics = []
        for index, base_path in enumerate(base_segments):
            before_cue = time.perf_counter()
            clip = converter.convert(base_path, source, target)
            if not np.isfinite(clip).all() or np.sqrt(np.mean(clip ** 2)) < 0.005:
                raise ValueError(f"Invalid or inaudible clone for cue {index + 1}.")
            clips.extend((clip, pause))
            cue_metrics.append({
                "cue": index + 1,
                "duration_seconds": round(len(clip) / rate, 3),
                "conversion_seconds": round(time.perf_counter() - before_cue, 3),
            })
        if args.base_review:
            base_audio = [sf.read(path, dtype="float32") for path in base_segments]
            base_rate = base_audio[0][1]
            base_pause = np.zeros(round(PAUSE_SECONDS * base_rate), dtype=np.float32)
            sf.write(args.base_review, np.concatenate([
                part for samples, _ in base_audio for part in (samples, base_pause)
            ][:-1]), base_rate)

    audio = np.concatenate(clips[:-1])
    duration = len(audio) / rate
    if not 30 <= duration <= 60:
        raise ValueError(f"Expected 30–60 seconds of narration, received {duration:.1f} s.")
    peak = np.max(np.abs(audio))
    audio *= min(1.0, 10 ** (-1.0 / 20) / peak)

    wav_path = args.out / "UCR-voice-clone-review.wav"
    with sf.SoundFile(wav_path, "w", rate, 1, subtype="PCM_16") as wav:
        wav.title = "UCR curriculum narration review"
        wav.comment = "Synthetic narration created with OpenVoice V2 for UCR Pathways review."
        wav.write(audio)
    (args.out / "script.txt").write_text("\n\n".join(cues) + "\n")
    metrics = {
        "model": "OpenVoice V2 with Piper Alba input",
        "reference_seconds": round(reference_seconds, 3),
        "reference_windows": len(reference_segments),
        "sample_seconds": round(duration, 3),
        "sample_rate_hz": rate,
        "peak_dbfs": round(20 * math.log10(np.max(np.abs(audio))), 2),
        "rms_dbfs": round(20 * math.log10(np.sqrt(np.mean(audio ** 2))), 2),
        "setup_and_embedding_seconds": round(before_conversion - start, 3),
        "conversion_seconds": round(sum(cue["conversion_seconds"] for cue in cue_metrics), 3),
        "program_seconds": round(time.perf_counter() - start, 3),
        "cues": cue_metrics,
    }
    (args.out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
