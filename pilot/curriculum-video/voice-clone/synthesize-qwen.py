"""Synthesize the economics passage using a private, transcribed voice prompt."""

import argparse
import json
import resource
import subprocess
import tempfile
import time
import wave
import zipfile
from pathlib import Path

from qwen_audio import loudness, normalize, passage, synthesize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_zip", type=Path, help="ZIP containing prompt.wav and prompt.txt")
    parser.add_argument("models", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--target-wpm", type=float, default=152, help="Speaking rate measured in the reference")
    parser.add_argument("--take", choices=(2, 3), type=int, default=2)
    args = parser.parse_args()
    if not 90 <= args.target_wpm <= 220:
        parser.error("Choose a reference speaking rate between 90 and 220 words/minute.")
    args.out.mkdir(parents=True, exist_ok=True)
    script = passage()
    start = time.monotonic()
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        with zipfile.ZipFile(args.prompt_zip) as archive:
            for name, limit in (("prompt.wav", 1500000), ("prompt.txt", 3000)):
                member = archive.getinfo(name)
                if not 0 < member.file_size <= limit:
                    raise ValueError(f"Unexpected size of {name}.")
                (work / name).write_bytes(archive.read(member))
        with wave.open(str(work / "prompt.wav")) as ref:
            prompt_duration = ref.getnframes() / ref.getframerate()
            if not (3 <= prompt_duration <= 20 and ref.getnchannels() == 1
                    and ref.getsampwidth() == 2 and ref.getframerate() == 24000):
                raise ValueError("Supply a 3–20 second, mono, 24 kHz PCM16 WAV.")
        if not (work / "prompt.txt").read_text(encoding="utf-8").strip():
            raise ValueError("Supply the matching English transcript.")

        def generate(text, destination):
            synthesize(args.models, work / "prompt.wav", work / "prompt.txt", text, destination)

        if args.take == 3:
            from phrased_qwen import render
            paced, take_metrics = render(script, work, generate)
        else:
            raw = work / "candidate.wav"
            generate(script, raw)
            with wave.open(str(raw)) as original:
                raw_duration = original.getnframes() / original.getframerate()
            raw_wpm = 60 * len(script.split()) / raw_duration
            # Preserve the model's relative pauses and stress. Limit time stretching
            # to 15% in either direction to avoid a large change to articulation.
            tempo = min(1.15, max(0.85, args.target_wpm / raw_wpm))
            paced = work / "paced.wav"
            subprocess.run([
                "ffmpeg", "-nostdin", "-v", "error", "-i", str(raw),
                "-af", f"atempo={tempo:.6f}", str(paced),
            ], check=True)
            take_metrics = {"raw_words_per_minute": round(raw_wpm, 1),
                            "target_wpm": args.target_wpm, "tempo_multiplier": round(tempo, 4)}
        synthesis = time.monotonic() - start
        wav = args.out / f"UCR-voice-clone-take-{args.take}.wav"
        normalize(paced, wav)
    with wave.open(str(wav)) as result:
        duration = result.getnframes() / result.getframerate()
    final = loudness(wav)
    if not (30 <= duration <= 60 and -20 <= float(final["input_i"]) <= -16
            and float(final["input_tp"]) < -0.9):
        raise ValueError(f"Check review length or levels: {duration:.2f} s, {final}")
    metrics = {
        "model": "Qwen3-TTS 1.7B Base Q8_0", "seed": 42,
        "words": len(script.split()), "prompt_seconds": round(prompt_duration, 2),
        **take_metrics,
        "delivered_wpm": round(60 * len(script.split()) / duration, 1),
        "audio_seconds": round(duration, 3), "synthesis_seconds": round(synthesis, 2),
        "peak_child_rss_kib_linux": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "integrated_lufs": float(final["input_i"]), "true_peak_dbtp": float(final["input_tp"]),
    }
    (args.out / "script.txt").write_text(script + "\n")
    (args.out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
