#!/usr/bin/env bash
# C1: V16384 d160 L10 F320 P96 (çekirdek ~3.0M, tahmini ~4.1 tok/s kartta). Yarıda kalırsa aynı komutla devam eder.
cd "$(dirname "$0")"
if pgrep -f "tag c1" >/dev/null; then echo "c1 zaten çalışıyor"; exit 0; fi
mkdir -p logs
export TS_DATA=data/tr_tinystories PYTHONPATH=src
nohup caffeinate -is .venv/bin/python -m research.tinystories.train \
  --arm ple --vocab 16384 --d-model 160 --n-layers 10 --ple-dim 96 --fixed-ffn 320 --target-core 3000000 \
  --batch-size 16 --seq-len 256 --steps 24000 --eval-every 500 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag c1 >> logs/train-c1.log 2>&1 &
echo "C1 başlatıldı (pid $!)"
