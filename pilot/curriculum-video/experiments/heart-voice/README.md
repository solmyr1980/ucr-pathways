# Heart narration comparison

The comparison uses the stock American English Heart voice from Kokoro v1.0 for an open, upbeat reading of the sixth cut. Alba remains the narrator in the approved cut. The two MP4s share the same 4,780 video frames, timecodes and script. The Heart MP4 includes the existing 55 English captions as a selectable subtitle track.

[Download the Heart comparison](https://github.com/solmyr1980/ucr-pathways/actions/runs/45361383751/artifacts/14904293490) · [Download the original Alba cut](https://github.com/solmyr1980/ucr-pathways/actions/runs/45027282662/artifacts/14756745304)

The dubbing script reads the original audio to locate sentence boundaries and the words that trigger highlights. It synthesizes each complete sentence, adjusts its duration without shifting pitch and matches the soundtrack level to the original. At 0:29–0:39 the narrator describes the three columns in the gateway diagram. At 2:46–2:58 the four discipline names cue the highlights on the completed grid.

## Reproduce the comparison

[Run the comparison workflow](https://github.com/solmyr1980/ucr-pathways/actions/workflows/compare-curriculum-voice.yml) while the [original sixth-cut artifact](https://github.com/solmyr1980/ucr-pathways/actions/runs/45027282662/artifacts/14756745304) is available. The workflow produces a separate review artifact.

For a local run, extract the MP4 and English SRT from the archived sixth-cut package. Install the pinned Python packages, FFmpeg and the Rubber Band CLI as listed in the [workflow file](../../../../.github/workflows/compare-curriculum-voice.yml). Download the model and voices from the [Kokoro ONNX v1.0 release](https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0). From the repository root, run the following command with the extracted media and model paths.

```sh
python pilot/curriculum-video/experiments/heart-voice/dub.py \
  UCR-curriculum-cut-6.mp4 UCR-curriculum-cut-6.en.srt \
  kokoro-v1.0.onnx voices-v1.0.bin comparison
```

The output is `comparison/UCR-curriculum-cut-6-Heart.mp4`. The script verifies the input MP4 against the sixth-cut SHA-256 before synthesis.
