#!/usr/bin/env bash
# Oyuncak hikâyeleriyle ince ayar (ple-tr-s0 üzerinden). Yarıda kalırsa aynı komutla devam eder.
cd "$(dirname "$0")"
if pgrep -f research.tinystories.train >/dev/null; then echo "bir eğitim zaten çalışıyor"; exit 0; fi
mkdir -p logs
export TS_DATA=data/tr_ft PYTHONPATH=src
nohup caffeinate -is .venv/bin/python -m research.tinystories.train \
  --arm ple --vocab 32768 --d-model 96 --n-layers 6 --ple-dim 128 --target-core 560000 \
  --batch-size 16 --seq-len 256 --steps 2000 --lr 3e-4 --warmup 50 --eval-every 200 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag trft --init-from runs/ple-tr-s0.pt >> logs/train-trft.log 2>&1 &
echo "ince ayar başlatıldı (pid $!), log: logs/train-trft.log"
