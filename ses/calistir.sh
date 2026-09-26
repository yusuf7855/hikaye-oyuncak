#!/bin/bash
# Ses modelinin bütün eğitimi, sırayla (Mac'te aynı anda tek eğitim). Yarıda kesilirse aynı komutla devam eder.
#   ./ses/calistir.sh            -> hepsi
#   ./ses/calistir.sh akustik    -> yalnız o aşama (veri | hazirla | akustik | vocoder | gta)
# Günlükler: ses_calisma/*.log   Örnek sesler: ses_calisma/akustik/ornek, ses_calisma/vocoder/ornek
set -e
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
mkdir -p ses_calisma
asama=${1:-hepsi}
calis() { [ "$asama" = hepsi ] || [ "$asama" = "$1" ]; }

if calis veri; then
  echo "[1/5] veri: 25 bin cümle Emel sesiyle indiriliyor (1-3 saat)"
  until $PY ses/veri_uret.py --cikti ses_veri --es 8 >> ses_calisma/veri.log 2>&1 && \
        [ "$(ls ses_veri/mp3 | wc -l)" -ge 24900 ]; do echo "  eksik var, tekrar"; sleep 30; done
fi
if calis hazirla; then
  echo "[2/5] hazırlık: 16 kHz, mel, perde"
  $PY ses/hazirla.py --veri ses_veri --is 6 >> ses_calisma/hazirla.log 2>&1
  tail -1 ses_calisma/hazirla.log
fi
if calis akustik; then
  echo "[3/5] akustik model (metin -> mel), 150 bin adım"
  $PY ses/egit_akustik.py >> ses_calisma/akustik.log 2>&1
fi
if calis vocoder; then
  echo "[4/5] vocoder (mel -> ses), 600 bin adım"
  $PY ses/egit_vocoder.py >> ses_calisma/vocoder.log 2>&1
fi
if calis gta; then
  echo "[5/5] vocoder ince ayar (akustiğin kendi çıktısıyla), +100 bin adım"
  $PY ses/egit_vocoder.py --gta --cikti ses_calisma/vocoder_gta --adim 100000 --sadece-mel 0 \
      --lr 1e-4 --baslangic ses_calisma/vocoder/son.pt >> ses_calisma/gta.log 2>&1
fi
echo "bitti. Deneme: $PY ses/sentezle.py --vocoder ses_calisma/vocoder_gta/son.pt --cikti deneme.wav"
