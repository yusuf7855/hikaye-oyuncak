# CLAUDE.md — Hikâye Oyuncağı (Claude Code için çalışma rehberi)

Bu dosya, depoyu açan Claude Code oturumunun (özellikle ürün sahibinin **RTX 4090'lı Windows bilgisayarındaki**
oturumun) ilk okuyacağı rehberdir. Ürün sahibiyle **Türkçe**, kısa ve sade konuş; teknik ayrıntıyı ancak sorulursa ver.
Saatleri Türkiye saatiyle (UTC+3) söyle.

## 1. Proje bir paragrafta

3–6 yaş çocuklar için **internetsiz** hikâye oyuncağı. Çocuk bir figür (Niloya, Pepee, Kral Şakir, Keloğlan, Hayri,
Doru, Maşa, Elsa, Örümcek Adam, Hello Kitty, Chase) ve bir yer seçer; **ESP32-S3 N16R8** üzerinde çalışan küçük bir
Türkçe dil modeli (c3, 5,7 M çekirdek parametre, `model.bin` 10,3 MB) her seferinde yeni bir hikâye yazar ve kartın
kendi ses modeli (~4,3 MB) kadın sesiyle okur. Model **daha büyük olamaz**: 16 MB flash / 8 MB PSRAM sınırı kesin.

## 2. Şu anki durum (2026-10-07)

| Parça | Durum |
|---|---|
| Hikâye modeli | **c3ft_karma** (10 597 hikâye: 1030 hakemli + 9567 hafif hat). Kör kıyasta eski 1030s2'yi açık farkla geçti (genel 127–37, olay 112–41); rubrik 3,17 → 4,51 / 10. Dosya: `modeller/c3ft_karma/model.bin` (depoda). Ayrıntı `degerlendirme/urun_kiyas_karma/OZET.md`. |
| Kart yazılımı | `firmware/hikaye_oyuncak/` yeni modele ve 11 figüre taşındı; PC'de sahte ESP32 başlıklarıyla derlenip `urun_uret.py` ile birebir aynı çıktı (328/328) doğrulandı. **Gerçek kartta henüz denenmedi.** |
| Ses | Öğretmen ses: ürün sahibinin seçtiği **VoxCPM2** kadın sesi (`ses/referans_ses.mp3`, Apache-2.0). Eğitim **henüz yapılmadı** — bu bilgisayarın asıl işi bu (aşağıda). Emel/edge-tts sesi Microsoft koşulları yüzünden üründe KULLANILMAZ. |
| Sıradaki büyük iş | Veriyi 20–30 bin hikâyeye çıkarıp yeniden eğitmek (`docs/YAPILACAKLAR.md`). |

## 3. Bu bilgisayarda yapılacak işler (öncelik sırasıyla)

### 3.1 Ses modelini eğit (RTX 4090)
```bat
cd hikaye-oyuncak
.venv\Scripts\activate
python ses/pc_hepsi.py
```
- Kurulum yoksa: Python 3.11 + Git kurulu olmalı; sonra
  `py -3.11 -m venv .venv`, `.venv\Scripts\activate`,
  `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124`,
  `pip install voxcpm soundfile scipy numpy`. İlk satırda `ekran kartı: NVIDIA GeForce RTX 4090` görünmeli.
- Aşamalar: [1] 25 bin cümle VoxCPM2 ile `ses_veri/mp3/` → [2] `hazirla.py` → [3] akustik (150 bin adım) →
  [4] vocoder (600 bin adım) → [5] GTA (30 bin) → [6] `deneme.wav` + `ses.bin`. Yarıda kalırsa aynı komut kaldığı
  yerden sürer. Günlükler `ses_calisma/*.log`; örnek sesler `ses_calisma/akustik/ornek`, `ses_calisma/vocoder/ornek`.
- Uzun süren komutları arka planda çalıştır ve ilerlemeyi günlükten izle; bilgisayarın uyku modu kapalı olmalı.
- [1] başladıktan sonra ilk ~250 cümlenin süresinden toplam süreyi hesaplayıp ürün sahibine söyle. Birkaç mp3'ü
  dinlet: ses referansa benzemiyorsa (`ses/referans_ses.mp3`), `veri_uret_vox.py --referans-metin "<referansın tam
  metni>"` ile tam klonlama denenebilir (metin bilinmiyor; Whisper ile çıkarılabilir).
- Bitince: `deneme.wav`'ı dinlet; `ses.bin` karta 0xBB0000 adresine yüklenir (3.3).
- Kontrol: `python firmware/hikaye_oyuncak/tools/ses_test.py --akustik ses_calisma/akustik/son.pt --vocoder
  ses_calisma/vocoder_gta/son.pt` (C çıkarımı = PyTorch).

### 3.2 Hikâye modelini GPU'da eğitmek (bulutta CPU ile ~2,5 saat; 4090'da dakikalar)
Eğitim zinciri bash betiği: Windows'ta **Git Bash** ya da **WSL** ile çalıştır.
```bash
TAG=c3ft_karma2 IZIN=data/urun_karma/izin.txt TEKRAR=2 GENEL=4000000 STEPS=12000 bash zincir_urun.sh
```
`data/urun_karma/` depoda değil (gitignore): `python degerlendirme/urun_hafif_topla.py topla` ve `birlestir` ile
`data/urun_v2` + `data/urun_v3`'ten yeniden kurulur. Genel Türkçe veri `data/tr2_tinystories` ve taban model
`runs/ple-c3-s0.pt` gerekir — depoda yoksa ürün sahibine sor, uydurma.

### 3.3 Kartı derle ve yükle (ESP32-S3 N16R8 USB ile bağlıysa)
- Arduino IDE 2 ya da `arduino-cli` (esp32 by Espressif 3.x). Ayarlar `firmware/hikaye_oyuncak/README.md`:
  ESP32S3 Dev Module, 16MB, **OPI PSRAM**, Partition **Custom** (`partitions.csv`), USB CDC On Boot.
- Model ve ses: `python -m esptool --chip esp32s3 --port COMx --baud 921600 write_flash 0x110000
  modeller\c3ft_karma\model.bin 0xBB0000 ses.bin` (adresleri README'den doğrula; değişmiş olabilir).
- Seri monitör 115200: açılışta model parmak izi `fp=00ea3e55`; `?` figür listesi, `1 1` hikâye, `b` hız testi.
  Çıktıyı (hız, profil satırı, birkaç hikâye) kaydet ve ürün sahibine özetle.

## 4. Depo haritası

| Yol | Ne |
|---|---|
| `degerlendirme/urun_uret.py` | PC'de ürün üretimi (istem, isim süzgeci, K aday + seçici). Kartın referansı. |
| `zincir_urun.sh`, `research/tinystories/` | Hikâye modeli veri hazırlama, eğitim (`--en-iyi`), dışa aktarma. |
| `data/urun_v2/` (hakemli), `data/urun_v3/` (hafif hat) | Eğitim hikâyeleri; `data/urun_kartlari.json` figür kartları. |
| `firmware/hikaye_oyuncak/` | ESP32 yazılımı; `tools/kart_pc/` PC'de sahte başlıklarla derleme, `tools/*_karsilastir.py` eşitlik testleri. |
| `runtime/` | C çıkarım motoru (`llm.h`, `ornekle.h`, `isim_suzgec.h`), `host_verify/gen.c`. |
| `ses/` | Kart sesi: veri (`veri_uret_vox.py`), eğitim, `disa_aktar.py` → `ses.bin`, `pc_hepsi.py` tek komut. |
| `web/` | Tarayıcıda Hikâye Atölyesi (`web/atolye.html`, paketler `web/m/`). |
| `docs/` | `YAPILACAKLAR.md` (sıradaki işler), `ESP32_BUTCE.md`, `SES_ARASTIRMASI.md`, `KUSURSUZ_VERI.md`, `PAZAR_ARASTIRMASI.md`. |

## 5. Kurallar ve dersler

- **Model boyutunu büyütme.** Kalite artışı veriden geldi (10 kat veri olay örgüsünü düzeltti; %40 fazlası düzeltmedi).
- Kaliteyi yalnız **kör** kıyasla ölç (`degerlendirme/IKILI_GENEL.md`, `IKILI.md`, `RUBRIK.md`); anahtar dosyası
  hakemlik süresince hakemlerin göreceği klasörde durmaz. Doğrulama kaybı tek başına karar vermez.
- Uzun eğitimlerde `--en-iyi` kullan (en iyi doğrulama adımının ağırlıkları saklanır).
- Kart kodu değişince PC eşitlik testlerini çalıştır: `python firmware/hikaye_oyuncak/tools/kart_pc_karsilastir.py`,
  `python firmware/hikaye_oyuncak/tools/secici_karsilastir.py --urun`, `python -m pytest -q tests`.
- Ses: yalnız ticari kullanıma açık kaynaklar (VoxCPM2 Apache-2.0, Supertonic Open RAIL-M). dfki, Emel, XTTS, F5-TTS
  vb. ASLA (`docs/SES_ARASTIRMASI.md`). Ambalajda "ses yapay zekâ ile üretilmiştir" notu.
- Figürler lisanslı karakterler: satıştan önce lisans gerekir (`docs/PAZAR_ARASTIRMASI.md`).
- Commit mesajları Türkçe; çalışma dalı `claude/wonderful-pasteur-x7seiq`. Büyük veri/model dosyalarını (ses_veri,
  ses_calisma, runs, hf_*) commit etme; yalnız ürün sahibinin istediği son model `modeller/` altına girer.
