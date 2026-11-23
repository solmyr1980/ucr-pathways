# Butterfly contour experiment

**Archived on 23 November 2026. The sixth cut remains the production version.** This directory holds a manually runnable experiment. The production storyboard, renderer and Actions workflow do not load it.

## What was tested

Would tracing a butterfly help prospective students recognize and remember the structure of the full six-cluster curriculum? The sixth cut first shows all six clusters, then uses Business & Entrepreneurship to explain Open, Locked and Gateway. The prototype returns to the full overview for seven seconds just before the student’s story. Alba says the following sentence.

> You can think of it as a butterfly: a spine in the middle, with two wings.

A thin plum line traces the collective open-course area on the left and the gateway-dependent area on the right. The spine follows the central gateway stack, steps out around the second Environment & Sustainability gateway and stops above the Media, Culture & Communication “No GATE” cell. The asymmetric wings follow the actual course positions. The completed contour holds for 1.05 seconds, fades over 0.57 seconds and leaves the original overview visible before the cut to the student.

In the 1280 × 720 playback review, the spine helped direct attention to the gateways. The upper-left wing enclosed considerable white space, and the left lower wing extended further than the right. The butterfly became recognizable chiefly when Alba named it. The editorial decision was to keep the shorter sixth cut. Student recall was not tested.

## Inputs and reproduction

The only media to retrieve is **UCR-curriculum-cut-6-YouTube-package.zip**, saved in the project owner’s ChatGPT Library under **UCR Pathways** on 22 November 2026. It contains the exact MP4 and English SRT. The script checks both against their SHA-256 digests before rendering. The two reviewed outputs are also saved in that folder under the filenames below. The production renderer and source map are pinned at the [sixth-cut commit](https://github.com/solmyr1980/ucr-pathways/commit/6a9ce28b70ec9e495b979a8ddec21ef9cb4b5e4e).

| Archived input | Purpose |
| --- | --- |
| `contour.py` | The two hand-fitted wing paths, gateway edges, line weights and colours. It maps the original SVG coordinates into the 1160 × 663 overview panel at (708, 219) in the 1920 × 1080 frame. |
| `narration.wav` and `spoken.json` | The exact 4.714-second Alba take, mono at 22,050 Hz, and its word boundaries in seconds from the start of the WAV. These preserve the timing without running speech synthesis again. |
| `reproduce.py` and `requirements.txt` | The drawing sequence, measured speech cues, excerpt boundaries, audio mix, optional English captions and export settings for both review clips. |
| `assets/video/curriculum.svg` in the repository | The source geometry for all six clusters. The script checks the asset against the sixth cut. |

From the repository root, use Python 3.12 and FFmpeg with libx264. Set `package` to the downloaded ZIP. The commands below write both clips under the repository’s ignored `output/` directory.

```bash
experiment=pilot/curriculum-video/experiments/butterfly-contour
package="/path/to/UCR-curriculum-cut-6-YouTube-package.zip"
python3 -m venv output/butterfly-venv
output/butterfly-venv/bin/python -m pip install -r "$experiment/requirements.txt"
output/butterfly-venv/bin/python -B "$experiment/reproduce.py" "$package" output/butterfly-contour
```

If the working copy’s map has since changed, recover the sixth-cut asset and pass it to the same command with `--map output/cut-6-curriculum.svg`.

```bash
git show 6a9ce28b70ec9e495b979a8ddec21ef9cb4b5e4e:assets/video/curriculum.svg > output/cut-6-curriculum.svg
```

The comparison covers source frames 410 through 1127 at 24 fps (17.083–47.000 seconds, end exclusive). The prototype inserts 168 frames before source frame 954, using the complete overview at frame 672 as the background. The take starts 0.25 seconds into the insert. In the short clip the trace begins at about 0:23. Both exports have selectable English subtitles and preserve the lower 180 pixels for captions.

| Reviewed output | Frames | SHA-256 with the review environment |
| --- | ---: | --- |
| `UCR-butterfly-contour-prototype.mp4` | 886 | `a90bd7a5610fb6f6248eeccab7c8980d9098dc73524cde149e6d20a179287fff` |
| `UCR-sixth-cut-comparison.mp4` | 718 | `0e7d672d0193a281f6a8e296e7ef92dba793626a0faf05c31896b22290ebd85c` |

A clean replay from the saved ZIP reproduced both reviewed MP4s byte for byte. The review environment used Debian FFmpeg 7.1.5-0+deb13u1 and the package versions in `requirements.txt`. Other encoders or builds can produce different file hashes. The original review checked the clean map before and after the trace, the English wording against the decoded audio and the empty subtitle area in every frame.

## If the production decision changes

1. Insert a dedicated full-overview scene between `gateway_overview` and `interest` in the production storyboard. Use the scene boundary for placement. Frame 954 belongs specifically to the sixth cut.
2. Reuse `Film.overview()` as the background and composite the RGBA crop returned by `contour.draw()` at `contour.ORIGIN`. Mark the moving frames in `Film.frame_key()` so the renderer redraws the trace. If the map or camera has changed, refit the hand-drawn wings and check the gateway edges against the new overview.
3. Use the saved take and word boundaries to preserve this reading. For a new reading, the recorded settings were the sixth cut’s pinned Piper Alba medium model, Piper 1.8.0 and `length_scale=1.01`. Align the new take and use its actual word times to drive the trace and captions. The prototype’s −3.7 dB gain matched an already mastered excerpt. A production render should mix the scene with its other narration before final mastering.
4. Review the transition at normal playback size, with captions on and off. Check that all six clusters stay visible during the trace, the line clears the course labels, the contour disappears completely and the student sequence remains synchronized. Use the regular full-cut checks if this scene enters production.
