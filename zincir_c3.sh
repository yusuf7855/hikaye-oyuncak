#!/usr/bin/env bash
# Tur 4 zinciri: C3 ön-eğitimi bitince (runs/ple-c3-s0.pt) ince ayar + ölçüm; ardından karşılaştırma için C2 + v4 verisi.
# Yarıda kalırsa aynı komutla tekrar çalıştırılır: biten adımlar (çıktısı olanlar) atlanır.
set -euo pipefail
cd "$(dirname "$0")"
ORTAK="--bolme data/bolme.json --blok-eot --plan data/oyuncak_plan/plan_hepsi.jsonl --plan-orani 0.7"
export KAYNAK=oyuncak_v2,oyuncak_v3,oyuncak_v4 EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on'
until [ -f runs/ple-c3-s0.pt ] && ! pgrep -f -- "--tag c3( |$)" >/dev/null; do sleep 60; done
[ -f hf_c3ft_v4/model.bin ] || BAZ=runs/ple-c3-s0.pt STEPS=4000 \
  BOYUT="--d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512" ./ince_ayar_c2.sh c3ft_v4 $ORTAK >> logs/c3ft_v4.log 2>&1
[ -f degerlendirme/c3ft_v4_dog/hikayeler.json ] || ./tur_degerlendir.sh c3ft_v4 > logs/tur_c3ft_v4.log 2>&1
[ -f hf_c2ft_v4/model.bin ] || BAZ=runs/ple-c2-s0.pt STEPS=3000 ./ince_ayar_c2.sh c2ft_v4 $ORTAK >> logs/c2ft_v4.log 2>&1
[ -f degerlendirme/c2ft_v4_dog/hikayeler.json ] || ./tur_degerlendir.sh c2ft_v4 > logs/tur_c2ft_v4.log 2>&1
echo "zincir bitti"
