#!/usr/bin/env bash
# C3: aynı kart (ESP32-S3 N16R8) için büyütülmüş model. C2'ye göre çekirdek 3.0M -> 5.7M (d192 L12 F512),
# PLE tablosu 15.7M -> 11.0M (P 96 -> 56). Kartta çekirdek ve head PSRAM'de 4-bit: 7.1 MB (C2 int8 7.5 MB),
# model.bin ~10.3 MB (bölüm 11.1 MB). Hesap: docs/ESP32_BUTCE.md "C3". Tokenizer C2 ile aynı.
# Yarıda kalırsa aynı komutla kaldığı yerden devam eder (her 250 adımda kayıt).
cd "$(dirname "$0")"
mkdir -p logs
export TS_DATA=data/tr2_tinystories PYTHONPATH=src
PY=${PY:-.venv/bin/python}
exec $PY -m research.tinystories.train \
  --arm ple --vocab 16384 --d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512 --target-core 3000000 \
  --batch-size 16 --seq-len 256 --steps ${STEPS:-24000} --eval-every 500 --eval-iters 20 \
  --ckpt-every 250 --seed 0 --tag c3 >> logs/train-c3.log 2>&1
