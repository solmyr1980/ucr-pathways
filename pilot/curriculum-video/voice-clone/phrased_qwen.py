"""Render the economics review with pauses and reference-guided EQ."""

import re
import subprocess
import wave

import numpy as np

RATE = 24000
# Each boundary serves a different purpose. The longest rests follow the
# opening question and precede the shift from households to the new business.
PAUSES = [0.78, 1.50, 0.65, 1.15, 0.85, 0.58, 1.55, 0.72, 1.00]
END_WORDS = ["poor", "them", "firms", "produce", "view", "growth",
             "incentives", "business", "venture", "them"]
BANDS = [100, 200, 315, 500, 800, 1250, 2000, 3150, 5000, 7500]
# Median over twelve independent six-second excerpts of the reviewed voice.
REFERENCE_DB = np.array([8.15, 11.76, 14.16, 12.23, -5.57, -7.13, -13.83, -15.84, -31.83])


def read_phrase(path):
    with wave.open(str(path)) as wav:
        if (wav.getframerate(), wav.getnchannels(), wav.getsampwidth()) != (RATE, 1, 2):
            raise ValueError("Unexpected synthesizer PCM format.")
        samples = np.frombuffer(wav.readframes(wav.getnframes()), dtype="<i2").astype(float) / 32768
    hop = RATE // 100
    if len(samples) < 30 * hop:
        raise ValueError("Empty or unexpectedly short sentence.")
    frames = samples[:len(samples) // hop * hop].reshape(-1, hop)
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    active = np.flatnonzero(rms > max(0.0005, rms.max() * 0.012))
    if not active.size:
        raise ValueError("No speech detected in the sentence.")
    # Keep a margin for soft initial consonants and final breaths. Internal
    # gaps stay intact. Fade only the outside five milliseconds at either edge.
    begin = max(0, (active[0] - 8) * hop)
    end = min(len(samples), (active[-1] + 12) * hop)
    kept = samples[begin:end].copy()
    ramp = np.linspace(0, 1, RATE // 200)
    kept[:len(ramp)] *= ramp
    kept[-len(ramp):] *= ramp[::-1]
    return kept


def spectral_profile(path):
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(path), "-ar", "16000",
        "-ac", "1", "-f", "f32le", "-",
    ])
    samples = np.frombuffer(raw, dtype="<f4")
    frames = np.lib.stride_tricks.sliding_window_view(samples, 640)[::320]
    energy = np.mean(frames.astype(float) ** 2, axis=1)
    # Select stronger speech frames after excluding pauses.
    audible = energy > energy.max() * 1e-4
    active = frames[energy > np.quantile(energy[audible], 0.55)]
    spectrum = abs(np.fft.rfft(active * np.hanning(640), axis=1)) ** 2
    frequencies = np.fft.rfftfreq(640, 1 / 16000)
    levels = [spectrum[:, (frequencies >= a) & (frequencies < b)].mean(axis=1)
              for a, b in zip(BANDS, BANDS[1:])]
    db = 10 * np.log10(np.stack(levels, axis=1) + 1e-12)
    return (db - db[:, 2:7].mean(axis=1, keepdims=True)).mean(axis=0)


def render(script, work, generate):
    sentences = re.split(r"(?<=[.?!])\s+", script.strip())
    if [sentence.rstrip(".?!").split()[-1].lower() for sentence in sentences] != END_WORDS:
        raise ValueError("The storyboard text changed. Review the planned pause locations.")
    parts = []
    timing = []
    cursor = 0
    for index, sentence in enumerate(sentences):
        path = work / f"sentence-{index + 1}.wav"
        generate(sentence, path)
        speech = read_phrase(path)
        gap = PAUSES[index] if index < len(PAUSES) else 0
        start = cursor / RATE
        cursor += len(speech)
        timing.append({"text": sentence, "start_s": round(start, 3),
                       "end_s": round(cursor / RATE, 3), "pause_after_s": gap})
        silence = np.zeros(round(gap * RATE))
        parts.extend([speech, silence])
        cursor += len(silence)

    assembled = work / "phrased.wav"
    with wave.open(str(assembled), "wb") as wav:
        wav.setparams((1, 2, RATE, 0, "NONE", "not compressed"))
        wav.writeframes(np.rint(np.concatenate(parts) * 32768).clip(-32768, 32767).astype("<i2").tobytes())

    before = spectral_profile(assembled)
    delta = REFERENCE_DB - before
    # Correct broad colour differences gently. Do not move individual vowel
    # formants or apply a pitch shift. High-frequency noise is excluded.
    bass = float(np.clip(delta[:2].mean(), -5, 3))
    presence = float(np.clip(delta[7], -2.5, 3.5))
    corrected = work / "tone.wav"
    subprocess.run([
        "ffmpeg", "-v", "error", "-i", str(assembled), "-af",
        f"bass=f=310:g={bass:.2f},equalizer=f=3800:t=o:w=1.3:g={presence:.2f}",
        str(corrected),
    ], check=True)
    metrics = {"phrases": timing, "inserted_pause_seconds": round(sum(PAUSES), 2),
               "low_shelf_db": round(bass, 2), "presence_gain_db": round(presence, 2),
               "band_edges_hz": BANDS, "reference_relative_db": REFERENCE_DB.tolist(),
               "uncorrected_relative_db": before.round(2).tolist(),
               "corrected_relative_db": spectral_profile(corrected).round(2).tolist()}
    return corrected, metrics
