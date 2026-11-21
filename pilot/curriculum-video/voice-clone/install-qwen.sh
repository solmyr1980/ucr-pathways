#!/usr/bin/env bash
set -euo pipefail
dir=$1
mkdir -p "$dir"
git init -q "$dir/source"
git -C "$dir/source" fetch -q --depth 1 https://github.com/ServeurpersoCom/qwentts.cpp.git 2edb35f87b709a070b2d5379f77e5c52a1daa585
git -C "$dir/source" checkout -q --detach FETCH_HEAD
git -C "$dir/source" submodule update --init --depth 1
cmake -S "$dir/source" -B "$dir/build" -DCMAKE_BUILD_TYPE=Release -DGGML_NATIVE=ON -DGGML_BLAS=OFF
cmake --build "$dir/build" --target qwen-tts --parallel 4

base=https://huggingface.co/Serveurperso/Qwen3-TTS-GGUF/resolve/b7ee2e8c7459c3bea99da23e3d178125a7d1713c
for name in qwen-talker-1.7b-base-Q8_0.gguf qwen-tokenizer-12hz-Q8_0.gguf; do
  curl -fsSL --retry 3 "$base/$name?download=true" -o "$dir/$name"
done
(cd "$dir" && sha256sum --check <<'HASH'
4b9a33a236908dd9435a42f7a396e38038329d053b704342a6413c08544c4fda  qwen-talker-1.7b-base-Q8_0.gguf
1883beeed99348fc35e23dd225e9082f93f6f8c109330a33d935baa8acdbfd94  qwen-tokenizer-12hz-Q8_0.gguf
HASH
)
