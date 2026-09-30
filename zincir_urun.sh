#!/usr/bin/env bash
# Ürün modeli (c3ft_urun): YALNIZ hakemlerden geçmiş urun_v2 hikâyeleriyle ince ayar (docs/KUSURSUZ_VERI.md Adım 11).
# Veri: prepare_ft2 --yalniz data/urun_v2/izin.txt (11 çizgi film figürü, figür başına >=50 kabul).
# Taban c3 (runs/ple-c3-s0.pt), c3ft_tek ile aynı boyut. Veri ~5x küçük: tekrar 4, genel dilim 3M token (oyuncak payı
# ~%11; 8M'de %4 kalırdı), 2000 adım (~2,4 geçiş, her hikâye ~10 kez görülür; Adım 11 ~13 kez önerir).
# Çıktı: hf_c3ft_urun/ (model.bin, tokenizer.json, golden, manifest_urun.json) ve web/m/c3ft_urun/.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
TAG=${TAG:-c3ft_urun}
PY=${PY:-.venv/bin/python}
BAZ=${BAZ:-runs/ple-c3-s0.pt}
export PYTHONPATH=src
[ -f "$BAZ" ] || { echo "taban yok: $BAZ"; exit 1; }
[ -x ./gen_verify ] || cc -O2 -o gen_verify runtime/host_verify/verify.c -lm
[ -x ./gen ] || cc -O3 -o gen runtime/host_verify/gen.c -lm
if [ ! -f runs/ple-$TAG-s0.pt ]; then
  $PY -m research.tinystories.prepare_ft2 --vocab 16384 --genel tr2_tinystories \
    --yalniz data/urun_v2/izin.txt --tekrar ${TEKRAR:-4} --genel-token ${GENEL:-3000000} --blok-eot --out tr_$TAG --manifest hf_$TAG/manifest_urun.json
  TS_DATA=data/tr_$TAG $PY -m research.tinystories.train \
    --arm ple --vocab 16384 --d-model 192 --n-layers 12 --ple-dim 56 --fixed-ffn 512 --target-core 3000000 \
    --batch-size 16 --seq-len 256 --steps ${STEPS:-2000} --lr ${LR:-3e-4} --warmup 50 --eval-every 250 \
    --eval-iters 20 --ckpt-every 250 --seed 0 --tag $TAG --init-from "$BAZ" --qat-emb
fi
$PY -c "
import sys; sys.argv=['export','ple-$TAG-s0','--tokenizer','data/tr_$TAG/vocab-16384/tokenizer.json']
from research.tinystories import export
export.OUT='hf_$TAG'
export.main()"
./gen_verify hf_$TAG/model.bin hf_$TAG/golden.txt > logs/verify-$TAG.log || { cat logs/verify-$TAG.log; exit 1; }
tail -1 logs/verify-$TAG.log
$PY web/paketle.py $TAG hf_$TAG ${PAKET:---urun --plan --satir-yasak --eot-on}
