"""Common storyboard, synthesis and level helpers for the Qwen listening tests."""

import json
import re
import subprocess
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


def synthesize(models, prompt_wav, prompt_txt, text, destination, seed=42):
    subprocess.run([
        str(models / "build" / "qwen-tts"),
        "--model", str(models / "qwen-talker-1.7b-base-Q8_0.gguf"),
        "--codec", str(models / "qwen-tokenizer-12hz-Q8_0.gguf"),
        "--ref-wav", str(prompt_wav), "--ref-text", str(prompt_txt),
        "--lang", "English", "--device", "CPU", "--seed", str(seed), "--max-new", "750",
        "-o", str(destination),
    ], input=text.strip() + "\n", text=True, check=True, stdout=subprocess.DEVNULL,
       stderr=subprocess.DEVNULL)


def normalize(paced, wav):
    levels = loudness(paced)
    filt = ("loudnorm=I=-18:TP=-1.5:LRA=11:linear=true"
            f":measured_I={levels['input_i']}:measured_TP={levels['input_tp']}"
            f":measured_LRA={levels['input_lra']}:measured_thresh={levels['input_thresh']}"
            f":offset={levels['target_offset']}")
    subprocess.run([
        "ffmpeg", "-y", "-nostdin", "-v", "error", "-i", str(paced), "-af", filt,
        "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", "-metadata",
        "comment=Synthetic narration for UCR Pathways voice review.", str(wav),
    ], check=True)
