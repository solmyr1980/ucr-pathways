"""Build readable English SRT cues from the narration's measured word boundaries."""

import re
import textwrap

FILENAME = "UCR-curriculum-pilot.en.srt"
WIDTH = 42


def words(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower().replace("’", "'"))


def wrap(text):
    return textwrap.wrap(text, width=WIDTH, break_long_words=False, break_on_hyphens=False)


def caption_lines(tokens):
    text = " ".join(tokens)
    if len(text) <= WIDTH:
        return [text]
    candidates = []
    for i in range(1, len(tokens)):
        left, right = " ".join(tokens[:i]), " ".join(tokens[i:])
        if len(left) <= WIDTH and len(right) <= WIDTH:
            # Prefer balanced lines and keep articles and prepositions with their phrases.
            penalty = 12 if tokens[i - 1].lower() in {"a", "an", "the", "to", "of", "and"} else 0
            # Keep title-case names together, including a connecting “and”.
            before, after = tokens[i - 1].rstrip(",.?!:"), tokens[i]
            inside_name = (
                (tokens[i - 1] == before and before.istitle() and after.istitle())
                or (before.istitle() and after == "and" and i + 1 < len(tokens) and tokens[i + 1].istitle())
                or (before == "and" and i >= 2 and tokens[i - 2].istitle() and after.istitle())
            )
            candidates.append((inside_name, abs(len(left) - len(right)) + penalty, left, right))
    assert candidates, text
    _, _, left, right = min(candidates)
    return [left, right]


def cue_break(tokens, first, last):
    candidates = []
    for i in range(last, first, -1):
        if len(" ".join(tokens[first:i])) < 24:
            break
        if len(" ".join(tokens[i:])) < 19:
            continue
        previous = tokens[i - 1]
        following = tokens[i].lower()
        if previous.lower() in {"and", "or"}:
            continue
        if previous.endswith((".", "?", "!", ":")):
            priority = 3
        elif previous.endswith(",") and previous not in {"Here,", "Together,"}:
            priority = 2
        elif following in {"and", "or", "how", "what", "whether", "when", "where", "which"}:
            priority = 1
        else:
            priority = 0
        candidates.append((priority, i))
    return max(candidates)[1] if candidates else last


def timed_captions(text, aligned, offset, cue_end):
    tokens = text.split()
    # A printed token such as “six-semester” can occupy two alignment words.
    boundaries = [0]
    for token in tokens:
        boundaries.append(boundaries[-1] + len(words(token)))
    assert boundaries[-1] == len(aligned)

    groups = []
    first = 0
    while first < len(tokens):
        last = first + 1
        while last < len(tokens) and len(wrap(" ".join(tokens[first:last + 1]))) <= 2:
            last += 1
        # Give each substantive sentence its own cue, even when two would fit.
        sentence = next((i for i in range(first + 1, last + 1)
                         if tokens[i - 1].endswith((".", "?", "!"))
                         and len(" ".join(tokens[first:i])) >= 24
                         and len(" ".join(tokens[i:])) >= 24), None)
        if sentence is not None:
            last = sentence
        elif last < len(tokens):
            last = cue_break(tokens, first, last)
        start = offset + aligned[boundaries[first]][1]
        end = min(cue_end, offset + aligned[boundaries[last] - 1][2])
        groups.append((start, end, caption_lines(tokens[first:last])))
        first = last

    captions = []
    for i, (start, end, lines) in enumerate(groups):
        next_start = groups[i + 1][0] if i + 1 < len(groups) else cue_end + 0.29
        # Hold briefly through short pauses to give the viewer more reading time.
        display_start = max(offset, start - 0.06)
        target = max(1.0, len(" ".join(lines)) / 18)
        display_end = min(next_start - 0.06, max(end + 0.12, display_start + target))
        captions.append((display_start, display_end, lines))
    return captions


def stamp(seconds):
    minutes, ms = divmod(round(seconds * 1000), 60_000)
    hours, minutes = divmod(minutes, 60)
    seconds, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{ms:03}"


def write_srt(path, scenes):
    captions = [caption for scene in scenes for caption in scene["captions"]]
    blocks = [
        f"{index}\n{stamp(start)} --> {stamp(end)}\n" + "\n".join(lines)
        for index, (start, end, lines) in enumerate(captions, 1)
    ]
    path.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
