"""Estimate voiced pitch in a review file (optionally, just the matched passage)."""
import argparse
import json
import subprocess

import numpy as np


def pitch_summary(path, start, end):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ss", str(start)]
    if end is not None:
        cmd += ["-t", str(end - start)]
    cmd += ["-ac", "1", "-ar", "8000", "-f", "f32le", "-"]
    samples = np.frombuffer(subprocess.check_output(cmd), "<f4").astype(float)
    frames = np.lib.stride_tricks.sliding_window_view(samples, 400)[::120]
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    threshold = max(np.percentile(rms, 92) * .10, rms.max() * .006)
    lags = np.arange(22, 110)
    pitches = []
    for frame in frames[rms > threshold]:
        frame = frame - frame.mean()
        energy = np.r_[0, np.cumsum(frame ** 2)]
        corr = np.correlate(frame, frame, mode="full")[len(frame)-1 + lags]
        corr /= np.sqrt(np.maximum(1e-15, energy[-1-lags] * (energy[-1] - energy[lags])))
        peaks = np.flatnonzero((corr[1:-1] > corr[:-2]) & (corr[1:-1] >= corr[2:])) + 1
        if peaks.size and max(corr[peaks]) >= .77:
            peak = peaks[corr[peaks] > .94 * max(corr[peaks])][0]
            pitches.append(8000 / lags[peak])
    if not pitches:
        raise ValueError("No periodic voiced frames.")
    low, median, high = np.percentile(pitches, [10, 50, 90])
    return {"voiced_frames": len(pitches), "median_hz": round(median, 1),
            "central_80_percent_semitones": round(12 * np.log2(high / low), 1)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--start", type=float, default=0)
    parser.add_argument("--end", type=float)
    args = parser.parse_args()
    if args.start < 0 or (args.end is not None and args.end <= args.start):
        parser.error("Choose a nonempty interval within the audio.")
    print(json.dumps(pitch_summary(args.file, args.start, args.end), indent=2))
