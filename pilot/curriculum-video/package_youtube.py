"""Stage the approved assets for manual review and delivery."""

import argparse
import shutil
from pathlib import Path

from PIL import Image
from subtitles import FILENAME

HERE = Path(__file__).resolve().parent
APPROVED = HERE / "_youtube-prototype"
REVIEW_SENTENCE = (
    "Before publication, a human reviews the entire video, checking the course choices, "
    "academic claims, visuals, narration and subtitles."
)


def package(out):
    source = (APPROVED / "README.md").read_text(encoding="utf-8")
    package_dir = out / "youtube"
    package_dir.mkdir(exist_ok=True)
    for filename, heading in [
        ("YouTube-title.txt", "Approved YouTube title"),
        ("YouTube-description.txt", "Approved YouTube description"),
        ("YouTube-pinned-comment.txt", "Approved pinned comment"),
    ]:
        text = source.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0].strip()
        if filename == "YouTube-title.txt":
            text = text.removeprefix("> ")
        if filename == "YouTube-description.txt":
            assert text.count(REVIEW_SENTENCE) == 1
            text = text.replace(" " + REVIEW_SENTENCE, "")
        (package_dir / filename).write_text(text + "\n", encoding="utf-8")

    thumbnail = APPROVED / "03-hybrid.png"
    with Image.open(thumbnail) as image:
        assert image.format == "PNG" and image.size == (3840, 2160)
        image.verify()
    assert thumbnail.stat().st_size < 2_000_000
    shutil.copyfile(thumbnail, package_dir / "YouTube-thumbnail.png")
    shutil.copyfile(out / FILENAME, package_dir / FILENAME)
    (package_dir / "REVIEW.md").write_text(
        "# UCR curriculum video review\n\n"
        "The title, hybrid thumbnail, description and pinned comment accompany the MP4 "
        "in the UCR-curriculum-pilot artifact. The English SRT comes from the same render.\n\n"
        "Human review of this final MP4 is pending. After reviewing the course choices, "
        "academic claims, visuals, narration and subtitles in the full video, add the following "
        "approved sentence at the end of the ‘How this video was made’ paragraph.\n\n"
        f"> {REVIEW_SENTENCE}\n\n"
        "The English subtitle file accompanies the video in YouTube Studio. "
        "Use the series playlist when publication and playlist actions have been authorized.\n",
        encoding="utf-8",
    )
    print("Staged the approved YouTube copy, hybrid thumbnail and verified English SRT.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("out", type=Path)
    package(parser.parse_args().out)
