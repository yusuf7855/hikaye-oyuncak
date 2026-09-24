#!/usr/bin/env bash
# C2 zinciri: v2+v3 oyuncak verisi -> ince ayar (+QAT) -> 4-bit dışa aktar -> C doğrulaması -> web paketi.
# Kullanım: ./ince_ayar_c2.sh <etiket> [ek prepare_ft2 argümanları]
#   BAZ=runs/ple-c2-s0.pt (ön-eğitim)   STEPS=3000   LR=3e-4   PY=.venv/bin/python
#   PAKET="--tema --satir-yasak --eot-on" (web paketi ayarları)
# Çıktı: hf_<etiket>/ (model.bin, tokenizer.json, golden) ve web/m/<etiket>/ (tarayıcı arayüzü için)
set -euo pipefail
cd "$(dirname "$0")"
TAG=${1:?etiket gerekli, ör. c2ft}; shift || true
PY=${PY:-.venv/bin/python}
BAZ=${BAZ:-runs/ple-c2-s0.pt}
UYANIK=$(command -v caffeinate >/dev/null && echo "caffeinate -is" || echo "")
export PYTHONPATH=src
[ -f "$BAZ" ] || { echo "önce ön-eğitim bitmeli: $BAZ yok"; exit 1; }
[ -x ./gen_verify ] || cc -O2 -o gen_verify runtime/host_verify/verify.c -lm
[ -x ./gen ] || cc -O3 -o gen runtime/host_verify/gen.c -lm
if [ ! -f runs/ple-$TAG-s0.pt ]; then
  $PY -m research.tinystories.prepare_ft2 --vocab 16384 --genel tr2_tinystories \
    --kaynak oyuncak_v2,oyuncak_v3 --out tr_$TAG "$@"
  TS_DATA=data/tr_$TAG $UYANIK $PY -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 160 --n-layers 10 --ple-dim 96 --fixed-ffn 320 --target-core 3000000 \
    --batch-size 16 --seq-len 256 --steps ${STEPS:-3000} --lr ${LR:-3e-4} --warmup 50 --eval-every 250 \
    --eval-iters 20 --ckpt-every 250 --seed 0 --tag $TAG --init-from "$BAZ" --qat-emb
fi
$PY -c "
import sys; sys.argv=['export','ple-$TAG-s0','--tokenizer','data/tr_$TAG/vocab-16384/tokenizer.json']
from research.tinystories import export
export.OUT='hf_$TAG'
export.main()"
./gen_verify hf_$TAG/model.bin hf_$TAG/golden.txt > logs/verify-$TAG.log || { cat logs/verify-$TAG.log; exit 1; }
tail -1 logs/verify-$TAG.log
$PY web/paketle.py $TAG hf_$TAG ${PAKET:-}
