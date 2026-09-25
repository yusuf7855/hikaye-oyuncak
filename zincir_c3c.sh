#!/usr/bin/env bash
# Tur 5: C3 + tüm popüler karakter paketleri (1152 hikâye, 1063 tam puan). Hakemde 10 almayanlar ve
# hakemlenmemiş v5 dosyaları data/egitim_haric.txt ile dışarıda.
set -euo pipefail
cd "$(dirname "$0")"
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_v6/model.bin ] || BAZ=runs/ple-c3-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v6 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric.txt >> logs/c3ft_v6.log 2>&1
[ -f degerlendirme/c3ft_v6_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v6 > logs/tur_c3ft_v6.log 2>&1
echo "zincir bitti"
