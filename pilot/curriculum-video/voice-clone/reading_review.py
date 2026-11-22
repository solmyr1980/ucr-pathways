"""Select a prompt from a private script reading and synthesize a fresh review WAV."""
import argparse
import hashlib
import json
import re
import subprocess
import time
import wave
from difflib import SequenceMatcher
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import sherpa_onnx
from faster_whisper import WhisperModel
from jiwer import process_words

from phrased_qwen import RATE, read_phrase
from qwen_audio import STORYBOARD, loudness, normalize, passage, synthesize


def tokens(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("’", "'"))


def decode(path, rate):
    raw = subprocess.check_output(["ffmpeg", "-nostdin", "-v", "error", "-i", str(path),
                                   "-ac", "1", "-ar", str(rate), "-f", "f32le", "-"])
    return np.frombuffer(raw, dtype="<f4")


def write_wav(path, data):
    with wave.open(str(path), "wb") as out:
        out.setparams((1, 2, RATE, 0, "NONE", "not compressed"))
        out.writeframes(np.rint(data * 32768).clip(-32768, 32767).astype("<i2").tobytes())


def transcribe(asr, path):
    samples = decode(path, 16000).copy()
    segments, _ = asr.transcribe(samples, language="en", beam_size=5, word_timestamps=True,
                                 condition_on_previous_text=False, vad_filter=True)
    return [w for segment in segments for w in segment.words]


def candidates(words, target):
    # Match complete storyboard sentences against the actual ASR words. Combine
    # adjacent sentences when a single sentence would make a very short prompt.
    board = json.loads(STORYBOARD.read_text())
    scenes = [" ".join(t for _, t in scene["cues"]) for scene in board]
    sentences = [s for scene in scenes for s in re.split(r"(?<=[.!?])\s+", scene)]
    spoken = [w for w in words for _ in tokens(w.word)]
    transcript = [t for w in words for t in tokens(w.word)]
    target_text = " " + " ".join(tokens(target)) + " "
    options = []
    for i in range(len(sentences)):
        for count in (1, 2):
            group = sentences[i:i + count]
            if any(" " + " ".join(tokens(s)) + " " in target_text for s in group):
                continue
            text = " ".join(group)
            pattern = tokens(text)
            if not 10 <= len(pattern) <= 35:
                continue
            for start, token in enumerate(transcript):
                end = start + len(pattern)
                if token != pattern[0] or transcript[start:end] != pattern:
                    continue
                left = spoken[start - 1].end if start else 0
                right = spoken[end].start if end < len(spoken) else spoken[end - 1].end + .2
                a = max(0, spoken[start].start - .14, (left + spoken[start].start) / 2)
                b = min(spoken[end - 1].end + .18, (spoken[end - 1].end + right) / 2)
                if 5 <= b - a <= 14:
                    confidence = np.mean([w.probability for w in spoken[start:end]])
                    score = confidence - .012 * abs((b - a) - 8.5)
                    options.append((score, a, b, text))
    prompts = []
    for _, a, b, text in sorted(options, reverse=True):
        if all(b + 1 < old.start or a > old.end + 1 for old in prompts):
            prompts.append(SimpleNamespace(start=a, end=b, text=text))
        if len(prompts) == 2:
            break
    if not prompts:
        raise ValueError("No clean, precisely transcribed non-target utterance found.")
    return prompts


def embed(extractor, samples):
    stream = extractor.create_stream()
    stream.accept_waveform(16000, np.ascontiguousarray(samples, dtype=np.float32))
    stream.input_finished()
    vector = np.asarray(extractor.compute(stream))
    return vector / np.linalg.norm(vector)


def windows(data, size=6):
    length = size * 16000
    for start in range(0, len(data) - length + 1, length):
        part = data[start:start + length]
        if np.mean(part.astype(float) ** 2) > 1e-7:
            yield start / 16000, part


def cosine(queries, references):
    centroid = np.mean(references, axis=0)
    centroid /= np.linalg.norm(centroid)
    return round(float(np.median(np.asarray(queries) @ centroid)), 3)


def check_words(expected, actual):
    result = process_words(" ".join(tokens(expected)), " ".join(tokens(actual)))
    return result.substitutions + result.insertions + result.deletions


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("recording", "models", "private", "out"):
        p.add_argument(name, type=Path)
    args = p.parse_args()
    work, out = args.private, args.out
    script = passage()
    sentences = re.split(r"(?<=[.!?])\s+", script.strip())
    if len(sentences) != 10 or sentences[7] != "Consider a new business.":
        raise ValueError("Review the phrasing against the revised storyboard.")
    phrases = [" ".join(sentences[a:b]) for a, b in [(0, 1), (1, 2), (2, 4), (4, 5), (5, 7), (7, 10)]]
    rests = [.38, .90, .72, .42, .92, 0]
    start = time.monotonic()
    ref = decode(args.recording, RATE)
    # The new microphone is quiet. Use a constant gain for analysis and
    # conditioning. Preserve pitch, relative dynamics, and frequency balance.
    ref = ref * min(15.85, .80 / max(float(np.max(np.abs(ref))), 1e-5))
    lifted = work / "analysis.wav"
    write_wav(lifted, ref)
    asr = WhisperModel(str(args.models / "whisper"), device="cpu", compute_type="int8", cpu_threads=4)
    words = transcribe(asr, lifted)
    prompts = candidates(words, script)
    cfg = sherpa_onnx.SpeakerEmbeddingExtractorConfig(model=str(args.models / "speaker.onnx"),
                                                       num_threads=2, provider="cpu")
    extractor = sherpa_onnx.SpeakerEmbeddingExtractor(cfg)
    recorded_windows = [(t, embed(extractor, part)) for t, part in windows(decode(lifted, 16000))
                        if all(t + 6 < v.start or t > v.end for v in prompts)
                        and sum(max(0, min(w.end, t + 6) - max(w.start, t)) for w in words) >= 2.5]
    if len(recorded_windows) < 8:
        raise ValueError("Too few independent speech windows for assessment.")
    tune, test = recorded_windows[::2], recorded_windows[1::2]
    def score(path, refs):
        data = decode(path, 16000)
        vectors = [embed(extractor, part) for _, part in windows(data)]
        return cosine(vectors or [embed(extractor, data)], [v for _, v in refs])

    prepared = time.monotonic()
    auditions = []
    for i, prompt in enumerate(prompts):
        prompt.wav, prompt.txt = work / f"ref{i}.wav", work / f"ref{i}.txt"
        write_wav(prompt.wav, ref[round(prompt.start * RATE):round(prompt.end * RATE)])
        prompt.txt.write_text(prompt.text)
        prompt.audition = work / f"audition{i}.wav"
        synthesize(args.models, prompt.wav, prompt.txt, phrases[0], prompt.audition)
        heard = " ".join(w.word.strip() for w in transcribe(asr, prompt.audition))
        err = check_words(phrases[0], heard)
        similarity = score(prompt.audition, tune)
        auditions.append((err, -similarity, i))
    best = min(auditions)[2]
    prompt = prompts[best]
    audition_end = time.monotonic()
    pieces, timing = [], []
    cursor = 0
    for i, (phrase, rest) in enumerate(zip(phrases, rests)):
        attempts = []
        for seed in (42, 73):
            path = work / f"group-{i}-{seed}.wav"
            if i == 0 and seed == 42:
                path = prompt.audition
            else:
                synthesize(args.models, prompt.wav, prompt.txt, phrase, path, seed)
            heard = " ".join(w.word.strip() for w in transcribe(asr, path))
            errors = check_words(phrase, heard)
            attempts.append((errors, seed, path))
            if not errors:
                break
        errors, seed, path = min(attempts)
        voiced = read_phrase(path)
        silence = np.zeros(round(rest * RATE))
        pieces.extend((voiced, silence))
        timing.append(dict(text=phrase, start=round(cursor / RATE, 3),
                           end=round((cursor + len(voiced)) / RATE, 3), rest=rest,
                           seed=seed, recognized_word_errors=errors))
        cursor += len(voiced) + len(silence)
    assembled = work / "assembled.wav"
    write_wav(assembled, np.concatenate(pieces))
    final = out / "UCR-voice-clone-script-reading.wav"
    normalize(assembled, final)
    generated = time.monotonic()
    output = decode(final, 16000)
    output_words = transcribe(asr, final)
    heard = " ".join(w.word.strip() for w in output_words)
    levels = loudness(final)
    seconds = len(output) / 16000
    errors = check_words(script, heard)
    if not (30 <= seconds <= 60 and -20 <= float(levels["input_i"]) <= -16
            and float(levels["input_tp"]) < -.9):
        raise ValueError(f"Check sample duration or levels: {seconds}, {levels}")
    baseline = [cosine([v], [x for j, (_, x) in enumerate(test) if i != j]) for i, (_, v) in enumerate(test)]
    gaps = [b.start - a.end for a, b in zip(output_words, output_words[1:])]
    metrics = dict(source_seconds=round(len(ref) / RATE, 2), source_recognized_words=len(words),
                   prompt_intervals=[[round(v.start, 2), round(v.end, 2)] for v in prompts],
                   auditions=[dict(prompt_index=i, word_errors=e, speaker_cosine=-s) for e, s, i in auditions],
                   selected_prompt_index=best, evaluation_windows=[t for t, _ in test],
                   synthesized_speaker_cosine=score(final, test),
                   genuine_leave_one_out_cosine=round(float(np.median(baseline)), 3),
                   duration_seconds=round(seconds, 3), words=len(tokens(script)),
                   words_per_minute=round(60 * len(tokens(script)) / seconds, 1),
                   recognized_text=heard, recognized_word_errors=errors,
                   gaps_over_half_second=sum(1 for gap in gaps if gap >= .5), phrases=timing,
                   integrated_lufs=float(levels["input_i"]), true_peak_dbtp=float(levels["input_tp"]),
                   preparation_s=round(prepared-start, 1), auditions_s=round(audition_end-prepared, 1),
                   remaining_synthesis_and_assembly_s=round(generated-audition_end, 1),
                   assessment_s=round(time.monotonic()-generated, 1),
                   sha256=hashlib.sha256(final.read_bytes()).hexdigest())
    old = work / "previous" / "UCR-voice-clone-take-3.wav"
    if old.is_file():
        if hashlib.sha256(old.read_bytes()).hexdigest() != "f64741696dabd274edaa6acb71fe62029168be166f968a527e8c34d5d26c0212":
            raise ValueError("Unexpected comparison WAV.")
        metrics["previous_synthetic_speaker_cosine"] = score(old, test)
    # Locate the reader's corresponding passage for independent playback checks.
    # Its timing is never passed to synthesis.
    full_text = [t for w in words for t in tokens(w.word)]
    positions = [w for w in words for _ in tokens(w.word)]
    blocks = [b for b in SequenceMatcher(None, tokens(script), full_text, autojunk=False).get_matching_blocks() if b.size]
    if (blocks and sum(b.size for b in blocks) >= .9 * len(tokens(script))
            and blocks[-1].b + blocks[-1].size - blocks[0].b < 1.25 * len(tokens(script))):
        metrics["recorded_passage_interval_s"] = [round(positions[blocks[0].b].start, 2),
                                                round(positions[blocks[-1].b + blocks[-1].size - 1].end, 2)]
    report = json.dumps(metrics, indent=2, default=np.generic.item, allow_nan=False)
    (out / "metrics.json").write_text(report + "\n")
    (out / "script.txt").write_text(script + "\n")
    print(report)


if __name__ == "__main__":
    main()
