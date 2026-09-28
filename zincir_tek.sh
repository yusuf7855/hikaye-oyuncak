#!/usr/bin/env bash
# Tek figür modeli (c3ft_tek): kullanıcı tek figür seçer, yer ve yan karakterleri sistem figürün dünyasından seçer.
# Veri: v6 (Tur 5) verisi eksi bütün ikili hikâyeler (data/egitim_haric_tek.txt = Tur 5 listesi + ikililer +
# sonradan eklenen 4 _2 dosyası). Taban c3, 5000 adım, v6 ile aynı tarif.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_tek/model.bin ] || BAZ=runs/ple-c3-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_tek \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric_tek.txt >> logs/c3ft_tek.log 2>&1
