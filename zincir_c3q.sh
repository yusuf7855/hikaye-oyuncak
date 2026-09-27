#!/usr/bin/env bash
# Tur 7: c3u (uzun ön-eğitim) float'ta daha iyi (genel 2.052 < 2.146) ama int4 gömme/çıkışta çok bozuluyor
# (genel 3.382; c3: 2.515). c3ft_v7 ince ayarı bu hasarı onarmakla geçti. Burada:
# Adım 1: c3u'yu genel veride --qat-emb ile kısa tavla (4000 adım, lr 2e-4) -> runs/ple-c3uq-s0.pt
# Adım 2: c3ft_v7 tarifiyle ince ayar -> c3ft_v8; adım 3: ölçüm. Yarıda kalırsa aynı komutla sürer.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
# NOT: bu satır ilk çalıştırmada eksikti (v8/v9 yalnız v2+v3 ile, 2102 hikâye eğitildi)
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
PY=${PY:-.venv/bin/python}
if [ ! -f runs/ple-c3uq-s0.pt ]; then
  TS_DATA=data/tr2_tinystories PYTHONPATH=src $PY -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512 --target-core 3000000 \
    --batch-size 16 --seq-len 256 --steps 4000 --lr 2e-4 --warmup 200 --eval-every 500 --eval-iters 20 \
    --ckpt-every 250 --seed 0 --tag c3uq --init-from runs/ple-c3u-s0.pt --qat-emb >> logs/train-c3uq.log 2>&1
fi
[ -f hf_c3ft_v8/model.bin ] || BAZ=runs/ple-c3uq-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v8 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric.txt >> logs/c3ft_v8.log 2>&1
[ -f degerlendirme/c3ft_v8_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v8 > logs/tur_c3ft_v8.log 2>&1
