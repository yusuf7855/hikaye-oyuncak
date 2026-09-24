#!/usr/bin/env bash
# Büyük çekirdekli model (aday B: V16384 d128 L8 F256 P128, çekirdek ~1.7M). Yarıda kalırsa aynı komutla devam eder.
cd "$(dirname "$0")"
if pgrep -f research.tinystories.train >/dev/null; then echo "bir eğitim zaten çalışıyor"; exit 0; fi
mkdir -p logs
export TS_DATA=data/tr_tinystories PYTHONPATH=src
if [ ! -f data/tr_tinystories/vocab-16384/train.bin ]; then
  .venv/bin/python -m research.tinystories.prepare_tr --vocab 16384 >> logs/prepare-16k.log 2>&1 || exit 1
fi
nohup caffeinate -is .venv/bin/python -m research.tinystories.train \
  --arm ple --vocab 16384 --d-model 128 --n-layers 8 --ple-dim 128 --fixed-ffn 256 --target-core 1700000 \
  --batch-size 16 --seq-len 256 --steps 20000 --eval-every 500 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag trbig >> logs/train-trbig.log 2>&1 &
echo "büyük model eğitimi başlatıldı (pid $!), log: logs/train-trbig.log"
