#!/usr/bin/env bash
# Tur 6: C3 ön-eğitimini uzat (kart aynı, model aynı boyut). 24k adımda doğrulama hâlâ düşüyordu (2.1467) ve
# genel veri yalnız ~1.8 kez görülmüştü; hakemin en sık iki kusuru bozuk dil (%82) ve mantıksızlık (%89).
# Adım 1: runs/ple-c3-s0.pt'den devam, 48k adım daha (kosinüs, lr 6e-4) -> runs/ple-c3u-s0.pt (~13 saat).
# Adım 2: c3ft_v6 tarifiyle ince ayar -> c3ft_v7; adım 3: ölçüm. Yarıda kalırsa aynı komutla kaldığı yerden sürer.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
PY=${PY:-.venv/bin/python}
if [ ! -f runs/ple-c3u-s0.pt ]; then
  TS_DATA=data/tr2_tinystories PYTHONPATH=src $PY -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512 --target-core 3000000 \
    --batch-size 16 --seq-len 256 --steps 48000 --lr 6e-4 --warmup 500 --eval-every 1000 --eval-iters 20 \
    --ckpt-every 250 --seed 0 --tag c3u --init-from runs/ple-c3-s0.pt >> logs/train-c3u.log 2>&1
fi
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_v7/model.bin ] || BAZ=runs/ple-c3u-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v7 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric.txt >> logs/c3ft_v7.log 2>&1
[ -f degerlendirme/c3ft_v7_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v7 > logs/tur_c3ft_v7.log 2>&1
echo "zincir bitti"
