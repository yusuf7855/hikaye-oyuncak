#!/bin/bash
# Colab terminalinden ses modelinin bütün eğitimi, sırayla. Önce defterin 1. ve 2. hücresini çalıştırın (Drive + depo),
# sonra Colab'da Terminal açıp:
#   cd /content/hikaye-oyuncak && nohup bash ses/colab_hepsi.sh > /content/hepsi.log 2>&1 &
#   tail -f /content/hepsi.log
# Her şey Drive'da (hikaye_ses_v2/): oturum koparsa aynı iki adımı tekrarlayın, kaldığı yerden sürer.
set -e
cd "$(dirname "$0")/.."
DRIVE=${DRIVE:-/content/drive/MyDrive/hikaye_ses_v2}
[ -d /content/drive/MyDrive ] || { echo "Drive bağlı değil: defterin 1. hücresini çalıştırın"; exit 1; }
mkdir -p "$DRIVE/ses_calisma" "$DRIVE/ses_veri_mp3/mp3"
ln -sfn "$DRIVE/ses_calisma" ses_calisma
pip -q install voxcpm soundfile scipy
IS=$(( $(nproc) < 8 ? $(nproc) : 8 ))
TAR="$DRIVE/ses_veri.tar"

if [ -f "$TAR" ]; then
  echo "[1-2/5] veri Drive'dan açılıyor"
  tar xf "$TAR"
else
  echo "[1/5] 25 bin cümle seçilen sesle seslendiriliyor (VoxCPM2, GPU) $(date)"
  mkdir -p ses_veri && ln -sfn "$DRIVE/ses_veri_mp3/mp3" ses_veri/mp3
  [ -f "$DRIVE/ses_veri_mp3/metin.tsv" ] && cp "$DRIVE/ses_veri_mp3/metin.tsv" ses_veri/metin.tsv
  python ses/veri_uret_vox.py --cikti ses_veri --adet 25000
  cp ses_veri/metin.tsv "$DRIVE/ses_veri_mp3/metin.tsv"
  echo "[2/5] hazırlık: 16 kHz, mel, perde $(date)"
  python ses/hazirla.py --veri ses_veri --is "$(nproc)"
  tar cf /content/ses_veri.tar ses_veri/hazir ses_veri/egitim.txt ses_veri/dogrulama.txt ses_veri/uzunluk.tsv ses_veri/metin.tsv
  cp /content/ses_veri.tar "$TAR.tmp" && mv "$TAR.tmp" "$TAR"
fi
wc -l ses_veri/egitim.txt ses_veri/dogrulama.txt

echo "[3/5] akustik model (metin -> mel) $(date)"
python ses/egit_akustik.py --is $IS 2>&1 | tee -a ses_calisma/akustik.log | grep -E --line-buffered "adım [0-9]+000 |==|devam|cihaz|bitti|Error|error"
echo "[4/5] vocoder (mel -> ses) $(date)"
python ses/egit_vocoder.py --is $IS --adim 600000 2>&1 | tee -a ses_calisma/vocoder.log | grep -E --line-buffered "adım [0-9]+000 |==|devam|cihaz|bitti|Error|error"
echo "[5/5] vocoder ince ayar (GTA) $(date)"
python ses/egit_vocoder.py --gta --cikti ses_calisma/vocoder_gta --adim 30000 --sadece-mel 0 --lr 1e-4 \
  --baslangic ses_calisma/vocoder/son.pt --is $IS 2>&1 | tee -a ses_calisma/gta.log | grep -E --line-buffered "adım [0-9]+000 |==|devam|başlangıç|cihaz|bitti|Error|error"
python ses/sentezle.py --vocoder ses_calisma/vocoder_gta/son.pt --cikti "$DRIVE/deneme.wav" --kuant
python ses/disa_aktar.py --akustik ses_calisma/akustik/son.pt --vocoder ses_calisma/vocoder_gta/son.pt \
  --cikti "$DRIVE/ses.bin" --altin "$DRIVE/ses_altin.bin"
echo "BİTTİ $(date): Drive hikaye_ses_v2/deneme.wav (dinleyin) ve ses.bin (karta 0xBB0000)"
