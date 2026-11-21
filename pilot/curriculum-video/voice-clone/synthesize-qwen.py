"""Synthesize the economics passage using a private, transcribed voice prompt."""

import argparse
import json
import re
import resource
import subprocess
import tempfile
import time
import wave
import zipfile
from pathlib import Path

STORYBOARD = Path(__file__).resolve().parents[1] / "storyboard.json"


def passage():
    scenes = json.loads(STORYBOARD.read_text())
    interest = next(s for s in scenes if s["scene"] == "interest")
    growth = next(s for s in scenes if s.get("heading") == "Who benefits from growth?")
    firms = next(s for s in scenes if s.get("heading") == "How do firms create wealth?")
    paragraphs = [interest["cues"], growth["cues"], firms["cues"][:1]]
    return "\n\n".join(" ".join(text for _, text in cues) for cues in paragraphs)


def loudness(path):
    measurement = subprocess.run([
        "ffmpeg", "-nostdin", "-hide_banner", "-i", str(path), "-af",
        "loudnorm=I=-18:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-",
    ], check=True, capture_output=True, text=True)
    match = re.search(r'\{\s*"input_i".*?\}', measurement.stderr, re.DOTALL)
    if not match:
        raise RuntimeError("FFmpeg returned no loudness measurement.")
    return json.loads(match.group())


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
            subprocess.run([
                str(args.models / "build" / "qwen-tts"),
                "--model", str(args.models / "qwen-talker-1.7b-base-Q8_0.gguf"),
                "--codec", str(args.models / "qwen-tokenizer-12hz-Q8_0.gguf"),
                "--ref-wav", str(work / "prompt.wav"), "--ref-text", str(work / "prompt.txt"),
                "--lang", "English", "--device", "CPU", "--seed", "42", "--max-new", "750",
                "-o", str(destination),
            ], input=text.strip() + "\n", text=True, check=True, stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)

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
        levels = loudness(paced)
        filt = ("loudnorm=I=-18:TP=-1.5:LRA=11:linear=true"
                f":measured_I={levels['input_i']}:measured_TP={levels['input_tp']}"
                f":measured_LRA={levels['input_lra']}:measured_thresh={levels['input_thresh']}"
                f":offset={levels['target_offset']}")
        wav = args.out / f"UCR-voice-clone-take-{args.take}.wav"
        subprocess.run([
            "ffmpeg", "-y", "-nostdin", "-v", "error", "-i", str(paced), "-af", filt,
            "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", "-metadata",
            "comment=Synthetic narration for UCR Pathways voice review.", str(wav),
        ], check=True)
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
