#!/usr/bin/env bash
# Tur 9: int4 tavlanmış uzun ön eğitim (c3uq) + TAM veri (v2, v3, v4, popüler; eğitim dışı data/egitim_haric.txt)
# -> c3ft_v10. v7 (c3u + tam veri) int4 hassasiyetinden kaybetti; v8/v9 yanlışlıkla yalnız v2+v3 ile eğitildi.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_v10/model.bin ] || BAZ=runs/ple-c3uq-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v10 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric.txt >> logs/c3ft_v10.log 2>&1
[ -f degerlendirme/c3ft_v10_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v10 > logs/tur_c3ft_v10.log 2>&1
