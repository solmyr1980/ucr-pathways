#!/usr/bin/env bash
set -euo pipefail

dependencies=$1
mkdir -p "$dependencies/converter"
openvoice_commit=74a1d147b17a8c3092dd5430504bd83ef6c7eb23
converter_revision=f36e7edfe1684461a8343844af60babc2efbb727
piper_revision=0ca208afc2a2ee102b1e961e72e0a7e4907be3d0
piper_url="https://huggingface.co/rhasspy/piper-voices/resolve/$piper_revision/en/en_GB/alba/medium/en_GB-alba-medium.onnx"
converter_url="https://huggingface.co/myshell-ai/OpenVoiceV2/resolve/$converter_revision/converter"

fetch() {
  curl --fail --silent --show-error --location --retry 3 "$1" -o "$2"
}

fetch "https://codeload.github.com/myshell-ai/OpenVoice/tar.gz/$openvoice_commit" "$dependencies/openvoice.tar.gz"
fetch "$converter_url/config.json?download=true" "$dependencies/converter/config.json"
fetch "$converter_url/checkpoint.pth?download=true" "$dependencies/converter/checkpoint.pth"
fetch "$piper_url" "$dependencies/alba.onnx"
fetch "$piper_url.json" "$dependencies/alba.onnx.json"

(cd "$dependencies" && sha256sum --check <<'CHECKSUMS'
a0bc7e5b2968ab7f8898d237b2b36f7de46710cbc3901f97dff29781eeae8abd  openvoice.tar.gz
9dfff60350b8c63f2c664efd92a61b2516efb22671466960f0e5dfebd881fa47  converter/config.json
9652c27e92b6b2a91632590ac9962ef7ae2b712e5c5b7f4c34ec55ee2b37ab9e  converter/checkpoint.pth
1f9da809b6da1ef4190bb5dd6cce4f4af803274539e9cf9e0693085150bac3d7  alba.onnx
ed4b1f015a8aae5eb26d4bdeed7b712c660f5698a0dd954aa6df9c8be60b900b  alba.onnx.json
CHECKSUMS
)
mkdir -p "$dependencies/openvoice"
tar -xzf "$dependencies/openvoice.tar.gz" -C "$dependencies/openvoice" --strip-components=1

# Import the converter directly. Its optional web UI and speech recognizers
# are unnecessary once the reference passages have been selected.
torch_wheel='https://download-r2.pytorch.org/whl/cpu/torch-2.5.1%2Bcpu-cp312-cp312-linux_x86_64.whl#sha256=4856f9d6925121d13c2df07aa7580b767f449dfe71ae5acde9c27535d5da4840'
python -m pip install "$torch_wheel" \
  numpy==2.2.6 onnxruntime==1.21.1 piper-tts==1.8.0 librosa==0.11.0 soundfile==0.13.1 \
  eng_to_ipa==0.0.2 inflect==7.0.0 unidecode==1.3.7 pypinyin==0.50.0 \
  cn2an==0.5.22 jieba==0.42.1 langid==1.1.6
