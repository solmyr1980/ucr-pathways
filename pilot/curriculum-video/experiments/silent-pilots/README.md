# Silent curriculum video pilots

These are three local renderers for the public illustrative economics, politics and global development programme. See the [project handoff](../../HANDOFF.md) for the editorial decisions and a viewing order. The review copies and exact render inputs are in the project owner’s private archive **UCR-Pathways-video-experiments-2026-11-26.zip**. The earlier 72.7-second unlabelled-map cut is included there as an MP4.

| Script | Review cut | Duration |
| --- | --- | ---: |
| `baseline.py` | `UCR-Pathways-butterfly-clusters.mp4` | 73.7 s |
| `course_in_motion.py` | `UCR-Pathways-short-pilot-course-in-motion.mp4` | 75.5 s |
| `question_led.py` | `UCR-Pathways-question-led-experiment.mp4` | 48.5 s |

## Reproduce a cut

The review environment used Python 3.12, FFmpeg 7.1.5 with libx264 and Cairo. From the repository root, put the archive’s `silent-pilot-assets/` directory under the ignored `output/` directory. It contains the exact 24-course record and course reference snapshot, curriculum SVG, branded fonts, and still frames for the semester plan, alumni destinations and QR. The archive also contains the long-form renderer snapshot used when preparing the stills.

```bash
pilot=pilot/curriculum-video/experiments/silent-pilots
mkdir -p output
python3.12 -m venv output/silent-pilot-venv
output/silent-pilot-venv/bin/python -m pip install -r "$pilot/requirements.txt"
export UCR_SILENT_PILOT_ASSETS="$PWD/output/silent-pilot-assets"
output/silent-pilot-venv/bin/python -B "$pilot/question_led.py" output/UCR-Pathways-question-led-experiment.mp4
```

Substitute the other script and its output filename to render that cut. The output is H.264, 1920 × 1080, 24 fps, with no audio track. Different encoder or library builds may give different file hashes. Review the first and last frames, all six cluster names, the content and legibility of the 24-course grid, and the QR destination. In the question-led cut, International Macroeconomics and Foundations of Comparative Politics enter Year 2, Semester 1, and History of Empires enters Year 3, Semester 1.

The assets freeze a review example. For a different programme, source the course titles, scope and feasible semesters from the current approved record and enriched course reference. Build the examples from what those courses actually teach. Source alumni examples using [the existing destination rules](../../README.md#31-alumni-destinations--25-november-2026).
