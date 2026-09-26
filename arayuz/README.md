# Hikâye Oyuncağı — kart arayüzü

ESP32-S3 kartındaki hikâye yazılımını (`firmware/hikaye_oyuncak`) bilgisayardan kullanmak için basit bir yerel web
arayüzü. Kart hikâyeyi yazdıkça metin tarayıcıda kelime kelime akar; önce plan (Sorun/Çözüm), sonra hikâye gösterilir.

Kartta yazılım ve `model.bin` yüklü olmalı: bkz. `firmware/hikaye_oyuncak/README.md`.

## Kurulum (bir kez)

```bash
python3 -m venv .venv-kart
# Mac / Linux
.venv-kart/bin/pip install flask pyserial
# Windows
.venv-kart\Scripts\pip install flask pyserial
```

## Çalıştırma

Depo klasöründe:

```bash
# Mac / Linux
.venv-kart/bin/python arayuz/app.py
# Windows
.venv-kart\Scripts\python arayuz\app.py
```

Tarayıcı kendiliğinden `http://127.0.0.1:5055` adresini açar (açmazsa adresi elle yazın). Kapatmak için komut
penceresinde **Ctrl+C**. Tarayıcıyı açmasın isterseniz: `TARAYICI_ACMA=1 python arayuz/app.py`.

> Arduino IDE'nin Seri Monitörü açıkken arayüz porta bağlanamaz (port meşgul). Önce onu kapatın.

## Kullanım

1. **Bağlantı**: portu seçin (ESP32 portu `(ESP32?)` işaretli ve en üstte; Mac'te `/dev/cu.usbmodem…`, Linux'ta
   `/dev/ttyACM0`, Windows'ta `COM5` gibi) → **Bağlan**. Port açılınca kart genellikle yeniden başlar; açılış
   satırları (model, PSRAM, `fp=…`, boş bellek) bağlantı kutusunun altında görünür. Figür ve yer listeleri kartın
   `?` çıktısından otomatik alınır.
2. **Hikâye**: 1. figürü, isterseniz 2. figürü ve yeri seçin. **Aday sayısı**:
   - **1 (canlı)** — hikâye yazıldıkça akar.
   - **4 (en iyisi)** — kart 4 aday üretir, her adayın puanı listelenir, en iyisi sonunda gösterilir (~4 kat sürer).
3. **Hikâye yaz** ya da **Rastgele**. Kart yazarken düğmeler kilitlenir.
4. Her hikâyenin sonunda **token/s**, **süre**, token ve aday sayısı gösterilir.
5. **Geçmiş**: her hikâye `arayuz/hikayeler.jsonl` dosyasına (satır başına bir JSON: tarih, figürler, yer, aday,
   token, sure_s, token_s, sorun, cozum, hikaye) eklenir ve listelenir. Bir kayda tıklayınca tamamı açılır.
6. **Günlük**: ham seri çıktıyı gösterir; buradan karta elle komut da gönderebilirsiniz (`?`, `10 1`, `r` …).

Kartın komutları: `10 1` = 10. figür, 1. yer · `1,3 4` = iki figür, 4. yer · `10 1 4` = 4 aday · `r` = rastgele ·
`?` = liste.

## Sorun giderme

| Belirti | Çözüm |
|---|---|
| "…açılamadı: Resource busy" | Portu başka program (Arduino Seri Monitörü, başka arayüz) kullanıyor; kapatın. |
| Bağlandı ama liste gelmiyor | Günlüğü açın. Boşsa kartta RST'ye basın; hâlâ boşsa firmware README'deki "USB CDC On Boot" ayarına bakın. |
| Günlükte `waiting for download` | Kart yükleme moduna düşmüş: RST'ye basın (BOOT'a basmadan). |
| Türkçe harfler bozuk | Arayüz UTF-8 okur; bozuksa günlükteki ham çıktıyı geliştiriciye gönderin. |
