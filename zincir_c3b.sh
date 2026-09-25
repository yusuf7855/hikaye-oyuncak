#!/usr/bin/env bash
# Tur 4: C3 + v2/v3/v4/v5/popüler ince ayar (10/10 almayanlar data/veri_haric.txt ile dışarıda) ve ölçüm.
set -euo pipefail
cd "$(dirname "$0")"
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_v5/model.bin ] || BAZ=runs/ple-c3-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v5 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/veri_haric.txt >> logs/c3ft_v5.log 2>&1
[ -f degerlendirme/c3ft_v5_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v5 > logs/tur_c3ft_v5.log 2>&1
echo "zincir bitti"
