#!/usr/bin/env bash
# C1 zinciri: v2+v3 oyuncak verisi -> ince ayar (+QAT) -> 4-bit dışa aktar -> doğrula -> test seti (16 aday).
# Kullanım: ./ince_ayar_c1.sh <etiket> [ek prepare_ft2 argümanları]
set -e
cd "$(dirname "$0")"
TAG=${1:-c1ft}; shift || true
export PYTHONPATH=src
[ -f runs/ple-c1-s0.pt ] || { echo "önce C1 bitmeli"; exit 1; }
if [ ! -f runs/ple-$TAG-s0.pt ]; then
  .venv/bin/python -m research.tinystories.prepare_ft2 --vocab 16384 --kaynak oyuncak_v2,oyuncak_v3 --out tr_$TAG "$@"
  TS_DATA=data/tr_$TAG caffeinate -is .venv/bin/python -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 160 --n-layers 10 --ple-dim 96 --fixed-ffn 320 --target-core 3000000 \
    --batch-size 16 --seq-len 256 --steps ${STEPS:-3000} --lr 3e-4 --warmup 50 --eval-every 250 --eval-iters 20 \
    --ckpt-every 250 --seed 0 --tag $TAG --init-from runs/ple-c1-s0.pt --qat-emb
fi
.venv/bin/python -c "
import sys; sys.argv=['export','ple-$TAG-s0','--tokenizer','data/tr_$TAG/vocab-16384/tokenizer.json']
from research.tinystories import export
export.OUT='hf_$TAG'
export.main()"
./gen_verify hf_$TAG/model.bin hf_$TAG/golden.txt | tail -1
.venv/bin/python degerlendirme/uret.py hf_$TAG ${TAG}_t05_sec16 --aday 16 --temp 0.5 --rep 1.1
