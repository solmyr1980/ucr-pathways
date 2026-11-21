"""Generate the curriculum-video opening with Chatterbox Nano on CPU."""

import argparse
import json
import math
import os
import subprocess
import tempfile
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS

STORYBOARD = Path(__file__).resolve().parents[1] / "storyboard.json"
PROMPT_LENGTH = 12.2
PAUSE_SECONDS = 0.32


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("model", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--prompt-start", type=float, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    reference_duration = float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "csv=p=0", str(args.reference),
    ]))
    if not 180 <= reference_duration <= 300:
        raise ValueError(f"Use a reviewed 3–5 minute reference (received {reference_duration:.1f} s).")
    if not 0 <= args.prompt_start <= reference_duration - PROMPT_LENGTH:
        raise ValueError("The prompt must fit entirely within the reviewed reference.")

    torch.set_num_threads(int(os.environ.get("OMP_NUM_THREADS", "4")))
    torch.manual_seed(42)
    scenes = json.loads(STORYBOARD.read_text())[:3]
    if [scene["scene"] for scene in scenes] != ["hook", "overview", "gateway"]:
        raise ValueError("The storyboard opening has changed. Review the selection first.")
    cues = [text for scene in scenes for _, text in scene["cues"]]

    with tempfile.TemporaryDirectory(prefix="ucr-nano-") as directory:
        prompt = Path(directory) / "prompt.wav"
        subprocess.run([
            "ffmpeg", "-nostdin", "-v", "error", "-ss", str(args.prompt_start),
            "-i", str(args.reference), "-t", str(PROMPT_LENGTH),
            "-map", "0:a:0", "-ac", "1", "-ar", "16000", str(prompt),
        ], check=True)
        model = ChatterboxTurboTTS.from_local(args.model, device="cpu", nano=True)
        model.prepare_conditionals(prompt)

    before_conversion = time.perf_counter()
    pause = np.zeros(round(PAUSE_SECONDS * model.sr), dtype=np.float32)
    clips = []
    cue_metrics = []
    for index, cue in enumerate(cues):
        before_cue = time.perf_counter()
        audio = model.generate(cue, temperature=0.67).squeeze(0).numpy()
        if not np.isfinite(audio).all() or np.sqrt(np.mean(audio ** 2)) < 0.005:
            raise ValueError(f"Invalid or inaudible clone for cue {index + 1}.")
        clips.extend((audio, pause))
        cue_metrics.append({
            "cue": index + 1,
            "duration_seconds": round(len(audio) / model.sr, 3),
            "conversion_seconds": round(time.perf_counter() - before_cue, 3),
        })

    audio = np.concatenate(clips[:-1])
    duration = len(audio) / model.sr
    if not 30 <= duration <= 60:
        raise ValueError(f"Expected 30–60 seconds of narration, received {duration:.1f} s.")
    audio *= min(1.0, 10 ** (-1.0 / 20) / np.max(np.abs(audio)))
    with sf.SoundFile(args.out / "UCR-voice-clone-review.wav", "w", model.sr, 1, subtype="PCM_16") as wav:
        wav.title = "UCR curriculum narration review"
        wav.comment = "Synthetic narration created with Chatterbox Nano for UCR Pathways review."
        wav.write(audio)
    (args.out / "script.txt").write_text("\n\n".join(cues) + "\n")
    metrics = {
        "model": "Chatterbox Nano",
        "reference_seconds": round(reference_duration, 3),
        "prompt_seconds": PROMPT_LENGTH,
        "prompt_start_seconds": args.prompt_start,
        "sample_seconds": round(duration, 3),
        "sample_rate_hz": model.sr,
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
