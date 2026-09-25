#!/usr/bin/env bash
# Kendi bilgisayarında eğitime devam etmek için hazırlık (Mac, Linux ya da Windows'ta WSL).
# Yapar: veri_paketi/'ndeki genel Türkçe veriyi data/tr2_tinystories/vocab-16384/ altına açar, tokenizer'ı koyar,
#        sağlama toplamlarını kontrol eder, C araçlarını derler. Ayrıntı: docs/YEREL_EGITIM.md
set -euo pipefail
cd "$(dirname "$0")"
H=data/tr2_tinystories/vocab-16384
mkdir -p "$H" runs logs
[ -f "$H/train.bin" ] || xz -dc veri_paketi/tr2_train.bin.xz > "$H/train.bin"
cp veri_paketi/tr2_val.bin "$H/val.bin"
cp modeller/c2_tokenizer.json "$H/tokenizer.json"
if command -v sha256sum >/dev/null; then (cd "$H" && sha256sum -c ../../../veri_paketi/SHA256SUMS)
else (cd "$H" && shasum -a 256 -c ../../../veri_paketi/SHA256SUMS); fi
cc -O2 -o gen_verify runtime/host_verify/verify.c -lm
cc -O3 -o gen runtime/host_verify/gen.c -lm
echo "Hazır. Eğitim için: docs/YEREL_EGITIM.md"
