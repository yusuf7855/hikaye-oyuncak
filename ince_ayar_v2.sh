#!/usr/bin/env bash
# v2 zinciri: veri hazırla -> ince ayar (+QAT) -> 4-bit dışa aktar -> C doğrulama. Yarıda kalırsa tekrar çalıştır.
set -e
cd "$(dirname "$0")"
mkdir -p logs
export PYTHONPATH=src
[ -f runs/ple-trbig-s0.pt ] || { echo "önce büyük model bitmeli (runs/ple-trbig-s0.pt yok)"; exit 1; }
if pgrep -f research.tinystories.train >/dev/null; then echo "bir eğitim zaten çalışıyor"; exit 0; fi
if [ ! -f runs/ple-trv2-s0.pt ]; then
  .venv/bin/python -m research.tinystories.prepare_ft2 --vocab 16384
  TS_DATA=data/tr_ft2 caffeinate -is .venv/bin/python -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 128 --n-layers 8 --ple-dim 128 --fixed-ffn 256 --target-core 1700000 \
    --batch-size 16 --seq-len 256 --steps 3000 --lr 3e-4 --warmup 50 --eval-every 250 --eval-iters 20 \
    --ckpt-every 250 --seed 0 --tag trv2 --init-from runs/ple-trbig-s0.pt --qat-emb
fi
.venv/bin/python -c "
import sys; sys.argv=['export','ple-trv2-s0','--tokenizer','data/tr_ft2/vocab-16384/tokenizer.json']
from research.tinystories import export
export.OUT='hf_v2'
export.main()"
cc -O2 -o gen_verify runtime/host_verify/verify.c -lm
./gen_verify hf_v2/model.bin hf_v2/golden.txt | tail -2
