#!/usr/bin/env bash
# Türkçe modeli eğit. Yarıda kalırsa aynı komutla kaldığı yerden devam eder (runs/*.ckpt.pt).
# caffeinate: fişteyken Mac uyumasın.
cd "$(dirname "$0")"
if pgrep -f research.tinystories.train >/dev/null; then echo "eğitim zaten çalışıyor"; exit 0; fi
mkdir -p logs
export TS_DATA=data/tr_tinystories PYTHONPATH=src
nohup caffeinate -is .venv/bin/python -m research.tinystories.train \
  --arm ple --vocab 32768 --d-model 96 --n-layers 6 --ple-dim 128 --target-core 560000 \
  --batch-size 16 --seq-len 256 --steps 12500 --eval-every 500 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag tr >> logs/train-tr.log 2>&1 &
echo "eğitim başlatıldı (pid $!), log: logs/train-tr.log"
