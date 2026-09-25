#!/usr/bin/env bash
# İyileştirme döngüsünün bir turunu ölç: yeni model hf_<etiket> için aday üret, seç (son seçici), hakem işlerini hazırla.
# Kullanım: ./tur_degerlendir.sh <etiket> [<taban_kol>=c2ft_plan_olay2]
#   Test seti (36 vaka) ve doğrulama vakaları (129) için 8'er aday, plan modu, satır yasağı, EOT öneki.
#   Çıktı: degerlendirme/<etiket>/ (rubrik partileri), degerlendirme/ikili_<etiket>__<taban>/ (genel + olay ikilileri),
#          hf_<etiket>/otomatik_<etiket>.json (kural ölçüleri)
set -euo pipefail
cd "$(dirname "$0")"
TAG=${1:?etiket}; TABAN=${2:-c2ft_plan_olay2}
PY=${PY:-.venv/bin/python}
D=data/tr_c2ft_plan/vocab-16384/dogrulama.json   # sabit doğrulama vakaları (bölme her kolda aynı)
AYAR="--aday 8 --baslik plan --satir-yasak --eot-on"
$PY degerlendirme/uret.py hf_$TAG $TAG $AYAR
$PY degerlendirme/uret.py hf_$TAG ${TAG}_dog $AYAR --dogrulama $D
$PY degerlendirme/otomatik.py hf_$TAG --ad $TAG $AYAR | tail -20
$PY degerlendirme/olay.py hf_$TAG/adaylar_$TAG.json --model hf_c2ft 2>/dev/null | tail -5 || true
$PY degerlendirme/hakem.py hazirla $TAG --parti 2 --hakem 2 | head -1
$PY degerlendirme/ikili.py hazirla $TAG $TABAN --parti 1 --hakem 1 | head -1
DTABAN=${TABAN/c2ft_plan_olay2/c2ft_plan_dog_olay2}
$PY degerlendirme/ikili.py hazirla ${TAG}_dog $DTABAN --parti 2 --hakem 1 | head -1
