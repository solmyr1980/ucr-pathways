#!/usr/bin/env bash
set -euo pipefail

dependencies=$1
mkdir -p "$dependencies/nano" "$dependencies/chatterbox"
source_commit=ab55923c27757c90cfcc407baa57dc25a7d25217
model_revision=71ccd1d0081b430592cea481f4307e764e07bc64
model_url="https://huggingface.co/ResembleAI/chatterbox-nano/resolve/$model_revision"

fetch() {
  curl --fail --silent --show-error --location --retry 3 "$1" -o "$2"
}

fetch "https://codeload.github.com/resemble-ai/chatterbox/tar.gz/$source_commit" "$dependencies/chatterbox.tar.gz"
for name in added_tokens.json merges.txt s3gen_meanflow.safetensors special_tokens_map.json \
    t3_nano_v1.safetensors tokenizer_config.json ve.safetensors vocab.json; do
  fetch "$model_url/$name?download=true" "$dependencies/nano/$name"
done

(cd "$dependencies" && sha256sum --check <<'CHECKSUMS'
46ee991e5b68f7c8adad6bb68a8f2465b5f8f669e95116e859b34b67ada3a3d6  chatterbox.tar.gz
72e4ab6acb0d9309ac3df4b526ae5fd80a2da5bc5ab7bb02d85096a374f69193  nano/added_tokens.json
1ce1664773c50f3e0cc8842619a93edc4624525b728b188a9e0be33b7726adc5  nano/merges.txt
d65cb687a2ed581ee6cc297e919ffefa63386944f42364ae13b78a594945514f  nano/s3gen_meanflow.safetensors
92ba8063bf40aa163eadebbfe0de07c2aebe44cf0d4a9e8726580b0781fd2640  nano/special_tokens_map.json
72b110185087d945dbdf54dee4e333848e1811bdd5fd6cb16ceb8da50006f0c9  nano/t3_nano_v1.safetensors
bca16a2ac1ddbd78b8d6228f0031884cc74b6ea54b967d6f6d2ebae9ccde23e6  nano/tokenizer_config.json
f0921cab452fa278bc25cd23ffd59d36f816d7dc5181dd1bef9751a7fb61f63c  nano/ve.safetensors
f6bd25a65e4e63ca31360e9fb11c7e4f9a391a78385d640acd814092dd6eee4f  nano/vocab.json
CHECKSUMS
)
tar -xzf "$dependencies/chatterbox.tar.gz" -C "$dependencies/chatterbox" --strip-components=1

# The published wheel supplies dependency pins. Nano is implemented in the
# pinned source archive, selected with PYTHONPATH in the workflow.
python -m pip install --index-url https://download.pytorch.org/whl/cpu torch==2.6.0 torchaudio==2.6.0
python -m pip install chatterbox-tts==0.1.7
