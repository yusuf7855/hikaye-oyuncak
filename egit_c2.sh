#!/usr/bin/env bash
# C2: C1 mimarisi (V16384 d160 L10 F320 P96, çekirdek ~3.0M) + figür isimlerini tek token yapan tokenizer
# (research/tinystories/prepare_tr2.py). Yarıda kalırsa aynı komutla devam eder. macOS'ta uyku engellenir.
cd "$(dirname "$0")"
if pgrep -f -- "--tag c2( |$)" >/dev/null; then echo "c2 zaten çalışıyor"; exit 0; fi
mkdir -p logs
export TS_DATA=data/tr2_tinystories PYTHONPATH=src
PY=${PY:-.venv/bin/python}
UYANIK=$(command -v caffeinate >/dev/null && echo "caffeinate -is" || echo "")
nohup $UYANIK $PY -m research.tinystories.train \
  --arm ple --vocab 16384 --d-model 160 --n-layers 10 --ple-dim 96 --fixed-ffn 320 --target-core 3000000 \
  --batch-size 16 --seq-len 256 --steps ${STEPS:-24000} --eval-every 500 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag c2 >> logs/train-c2.log 2>&1 &
echo "C2 başlatıldı (pid $!)"
