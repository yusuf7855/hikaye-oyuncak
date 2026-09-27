#!/usr/bin/env bash
# Tur 8: v7/v8 (c3u tabanı) ezberledi ve v6'nın gerisinde kaldı. Taban mı veri mi? c3 (Tur 5 tabanı) + v7/v8 verisi
# (eğitim dışı 137 kimlik, 4797 hikâye) -> c3ft_v9. v6'ya yakın/iyi çıkarsa sorun c3u tabanı, kötüyse veri.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
# NOT: bu satır ilk çalıştırmada eksikti (v8/v9 yalnız v2+v3 ile, 2102 hikâye eğitildi)
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4,oyuncak_populer EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
[ -f hf_c3ft_v9/model.bin ] || BAZ=runs/ple-c3-s0.pt STEPS=5000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v9 \
  --bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7 \
  --haric data/egitim_haric.txt >> logs/c3ft_v9.log 2>&1
[ -f degerlendirme/c3ft_v9_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v9 > logs/tur_c3ft_v9.log 2>&1
