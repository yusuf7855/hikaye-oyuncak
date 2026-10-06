# Hikâye Oyuncağı — ESP32-S3 üzerinde offline Türkçe hikâye anlatan yapay zekâ

Çocuk bir figürü (🐰 Pamuk, 🦊 Kızıl…) oyuncağa yaklaştırır, oyuncak **o figürle ilgili, daha önce hiç
anlatılmamış bir Türkçe hikâye** üretir ve sesli okur. İnternet yok, bulut yok: dil modeli birkaç dolarlık
bir **ESP32-S3** mikrodenetleyicinin üzerinde çalışır.

Proje, [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) deposunun (28.9M parametreli bir dil modelini
ESP32-S3'te çalıştıran *Per-Layer Embeddings* mimarisi) üzerine kuruldu. Orijinal README:
[`docs/UPSTREAM_README.md`](docs/UPSTREAM_README.md).

---

## İçindekiler
1. [Ürün fikri](#ürün-fikri)
2. [Güncel durum ve sonuçlar](#güncel-durum-ve-sonuçlar)
3. [Nasıl çalışıyor](#nasıl-çalışıyor)
4. [Figürler](#figürler)
5. [Veri](#veri)
6. [Modeller ve eğitim](#modeller-ve-eğitim)
7. [Hikâye üretimi: başlık, yasak isimler, aday seçimi](#hikâye-üretimi)
8. [Kalite ölçümü (hakem düzeni)](#kalite-ölçümü-hakem-düzeni)
9. [PC'de test arayüzü](#pcde-test-arayüzü)
10. [Kurulum ve komutlar](#kurulum-ve-komutlar)
11. [ESP32'ye geçiş planı ve donanım](#esp32ye-geçiş-planı-ve-donanım)
12. [Önemli bulgular / dersler](#önemli-bulgular--dersler)
13. [Yol haritası](#yol-haritası)
14. [Dizin yapısı](#dizin-yapısı)
15. [Lisanslar ve teşekkür](#lisanslar-ve-teşekkür)

---

## Ürün fikri

| | |
|---|---|
| Hedef kitle | 3–6 yaş |
| Donanım | ESP32-S3 N16R8 (16 MB flash, 8 MB PSRAM), NFC okuyucu (PN532 / RC522), MAX98357A I2S amfi + hoparlör, pil |
| Etkileşim | Figürün içinde bir NFC etiketi (NTAG213) — etikette sadece figür **kimliği** yazar |
| Tek figür | 🐰 okut → Pamuk'un hikâyesi |
| İki figür | 🐰 + 🦊 okut (3 sn içinde) → Pamuk ile Kızıl'ın birlikte hikâyesi |
| Yer kartı | isteğe bağlı: 🌲 orman, 🌊 deniz, 🏡 ev, 🌳 park, 🏰 şato, ⛰️ dağ (okutulmazsa rastgele) |
| Maliyet hedefi | Düşük: ESP32 şart (Raspberry Pi değil) |
| İş modeli fikri | Oyuncak + ayrıca satılan yeni figürler (her figür = yeni hikâye dünyası) |

---

## Güncel durum ve sonuçlar

> Son güncelleme: 2026-10-07. Claude Code ile çalışırken önce [`CLAUDE.md`](CLAUDE.md) okunur.

### Ekim 2026: ürün modeli

| Parça | Durum |
|---|---|
| Figürler | 11 çizgi film figürü (Niloya, Pepee, Kral Şakir, Keloğlan, Hayri, Doru, Maşa, Elsa, Örümcek Adam, Hello Kitty, Chase); kartları `data/urun_kartlari.json`. Satış için lisans gerekir ([`docs/PAZAR_ARASTIRMASI.md`](docs/PAZAR_ARASTIRMASI.md)). |
| Hikâye modeli | **c3ft_karma** (C3, 10,3 MB, ESP32-S3 N16R8'e sığar): 1030 hakemli + 9567 hafif hat hikâye. Kör kıyasta önceki modeli genel kalitede 127–37, olay örgüsünde 112–41 yendi; rubrik 3,17 → 4,51 ([OZET](degerlendirme/urun_kiyas_karma/OZET.md)). |
| Üretim | Plan modu (Sorun/Çözüm → hikâye), isim süzgeci (başka figür adları yazılamaz), K aday + seçici ([`degerlendirme/urun_uret.py`](degerlendirme/urun_uret.py)). |
| Kart yazılımı | [`firmware/hikaye_oyuncak`](firmware/hikaye_oyuncak): yeni model + 11 figür; PC'de `urun_uret` ile birebir aynı (328/328). Gerçek kartta denenecek. |
| Ses | Öğretmen ses VoxCPM2 (ürün sahibinin seçtiği kadın sesi, Apache-2.0); eğitim RTX 4090'da (`ses/pc_hepsi.py`, [`docs/WINDOWS_CLAUDE_CODE.md`](docs/WINDOWS_CLAUDE_CODE.md)). |
| Sıradaki | Veriyi 20–30 bine çıkarmak ([`docs/YAPILACAKLAR.md`](docs/YAPILACAKLAR.md)). |

### Eylül 2026 (hayvan figürleri dönemi)

### Modeller

| Model | Çekirdek | Kelime dağarcığı | Flash (4-bit) | Tahmini ESP32 hızı* | Doğrulama perplexity |
|---|---|---|---|---|---|
| Orijinal İngilizce (upstream) | 0.56 M | 25 353 | 14.9 MB | 10.5 tok/s (ölçülmüş) | 11.4 (İngilizce) |
| Türkçe küçük (`ple-tr-s0`) | 0.56 M | 32 768 | 14.9 MB | 8.9 tok/s | 15.2 |
| **B** (`ple-trbig-s0`) | 1.71 M | 16 384 | 10.6 MB | 6.5 tok/s | 10.25 |
| **C1** (`ple-c1-s0`) | 3.03 M | 16 384 | 11.1 MB | 4.1 tok/s | **9.28** |
| C1 + oyuncak ince ayarı (`ple-c1ft-s0`) | 3.03 M | 16 384 | 11.1 MB | 4.1 tok/s | **7.36** (oyuncak hikâyelerinde, 4-bit) |

\* Hız, upstream'in gerçek ESP32-S3 ölçümüyle (94.9 ms/token) orantılanarak **tahmin** edilmiştir
(`tools_boyut.py`). Kartta ölçülene kadar ±%30 belirsiz kabul edin. Türkçe sesli okuma için ~4 tok/s yeterli;
ayrıca oyuncak hikâyeleri boştayken önceden üretir.

### Hikâye kalitesi (hakem puanı, 10 üzerinden)

Aynı sabit 36 vakalık test seti (24 tek figür + 12 ikili), katı bir rubrikle bağımsız hakem ajanlar tarafından
puanlandı ([rubrik](degerlendirme/RUBRIK.md)).

| Adım | Puan |
|---|---|
| v2 modeli, sadece başlık + yasak isim listesi | 2.67 |
| + temp 0.4, rep 1.1, en iyi 4 aday | 4.50 |
| + temp 0.5, en iyi 8 aday, geliştirilmiş seçici | **4.94** |
| C1 + v2/v3 ince ayar, en iyi 16 aday | *ölçülüyor* |
| **Referans: eğitim verisinin kendisi (v3 hikâyeleri)** | **9.83** (24 hikâyenin 21'i tam 10) |

**Özet:** Eğitim verisi 10/10 kalitede; darboğaz, küçük modelin bu kaliteyi taklit edebilmesi. En sık
kalan kusurlar: mantıksız olay örgüsü, uydurma kelime, karakter karışıklığı.

---

## Nasıl çalışıyor

```
 NFC etiket(ler)i ──► kimlik ──► karakterler.json ──► başlık:  "Karakter: tavşan, tilki | Yer: orman\n\n"
                                                        │
                                                        ▼
                               ┌──────────────── ESP32-S3 ────────────────┐
                               │  PLE dil modeli (4-bit)                  │
                               │   • SRAM  : aktivasyonlar, norm          │
                               │   • PSRAM : çekirdek + çıkış katmanı     │
                               │   • FLASH : 15.7M parametrelik PLE       │
                               │             tablosu (token başına        │
                               │             birkaç satır okunur)         │
                               │  örnekleme: temp + top-k + tekrar cezası │
                               │            + yasak isim listesi          │
                               │  K aday üret → seçici → en iyisini sakla │
                               └──────────────────────────────────────────┘
                                                        │ hikâye metni
                                                        ▼
                                  TTS (kelime/hece bankası, SD kart) ──► I2S amfi ──► hoparlör
```

**Per-Layer Embeddings (PLE):** Parametrelerin çoğu, hesaplama yapılmayan büyük bir arama tablosunda durur.
Tablo yavaş flash'ta kalır; her token için sadece birkaç satırı okunur. Böylece 512 KB SRAM'li bir çipte
çok daha büyük bir model "sığar". Ayrıntılar: [`RESULTS.md`](RESULTS.md) (upstream ölçümleri).

---

## Figürler

Sabit isimler bilinçli bir tasarım kararı: küçük model birden çok isimle karşılaşınca karakterleri
karıştırıyordu ("isim çorbası"). Artık **sadece figürlerin ismi var**, diğer herkes isimsiz
("annesi", "küçük bir yengeç"). Kaynak: [`data/karakterler.json`](data/karakterler.json)

| Figür | Tür | İsim | Özellik |
|---|---|---|---|
| 🐰 | tavşan | Pamuk | bembeyaz, uzun kulaklı, zıplamayı ve havucu sever, biraz utangaç |
| 🐱 | kedi | Tekir | çizgili, çok meraklı, mırlayarak sevinir |
| 🐶 | köpek | Karabaş | sadık, neşeli, top oyununu sever |
| 🐻 | ayı | Bal | kocaman ve yumuşacık, bal sever, uykucu |
| 🦊 | tilki | Kızıl | turuncu, akıllı, plan yapmayı sever |
| 🐦 | kuş | Cikcik | minik, şarkı söyler, gökyüzünden her şeyi görür |
| 🐢 | kaplumbağa | Tosbi | yavaş ama sabırlı ve bilge |
| 🐧 | penguen | Paytak | paytak paytak yürür, kayar, yüzer |
| 🦕 | dinozor | Dino | uzun boyunlu, büyük ama nazik |
| 🐉 | ejderha | Alev | ateş yerine renkli baloncuklar üfler |
| 👧 | kız | Elif | meraklı ve cesur |
| 👦 | oğlan | Can | enerjik ve yardımsever |

Yeni figür eklemek: `karakterler.json`'a satır ekle → o figürün hikâyelerini yaz → ince ayarı tekrarla.

---

## Veri

### 1. Genel Türkçe ön-eğitim verisi
[esat-krky/TinyStories_Turkish](https://huggingface.co/datasets/esat-krky/TinyStories_Turkish) —
359 954 kısa Türkçe çocuk hikâyesi (~52 M token, CDLA-Sharing-1.0). Depoya dahil **değil**; indirme komutu
aşağıda. Not: hikâyelerin ~%65'inde İngilizce isimler (Lily, Tim…) geçiyor; üretimde yasak isim listesiyle
engelleniyor.

### 2. Oyuncak hikâyeleri (Claude Code ajanlarıyla yazıldı — depoda)

| Set | Klasör | İçerik | Kural seti |
|---|---|---|---|
| v1 | `data/oyuncak_hikayeleri/` | 960 hikâye, 8 karakter × 6 yer × 20 tema | [YAZIM_KILAVUZU.md](data/oyuncak_hikayeleri/YAZIM_KILAVUZU.md) — çok isimli, **eğitimde kullanılmıyor** |
| v2 | `data/oyuncak_v2/` | 1248 hikâye: 720 tek figür + 528 ikili (66 ikilinin hepsi) | [KILAVUZ.md](data/oyuncak_v2/KILAVUZ.md) — sabit isimler, 100–150 kelime |
| v3 | `data/oyuncak_v3/` | ~1116 hikâye: 720 tek figür + 396 ikili | [KILAVUZ.md](data/oyuncak_v3/KILAVUZ.md) — v2 + karakter karışıklığını önleyen ek kurallar |

v3 ek kuralları (hakem bulgularından türetildi): en fazla bir yan karakter ve hep aynı adla anılır;
her konuşmada konuşan açıkça yazılır; figür kendine hitap etmez; nesneler konuşmaz; figürün özelliği görünür
ve çelişilmez; basit sebep-sonuç.

Her klasörde:
- `kontrol.py` — biçim, uzunluk (kartın 256 token sınırı), isim/tür doğruluğu, uydurma isim, kendine
  gönderme, konuşan nesne kontrolleri
- `birim.py` + `KUYRUK.json` — paralel yazar ajanlar için dosya kilitli iş kuyruğu

Dosya biçimi:
```
### tavşan, tilki | orman | birlikte çalışmak
Ormanın kenarında Pamuk adında bembeyaz bir tavşan ile Kızıl adında turuncu bir tilki yaşardı. ...
```

---

## Modeller ve eğitim

Tüm eğitim M3 Mac'te (MPS) yapıldı. Eğitim betiği her 250 adımda **kaldığı yerden devam edilebilir**
checkpoint alır (`runs/*.ckpt.pt`) ve ilerlemeyi `runs/*.progress.json`'a yazar.

| Aşama | Komut | Süre (M3) |
|---|---|---|
| Türkçe tokenizer + token dosyaları | `TS_DATA=data/tr_tinystories PYTHONPATH=src .venv/bin/python -m research.tinystories.prepare_tr --vocab 16384` | ~10 dk |
| B ön-eğitimi (1.7M çekirdek) | `./egit_buyuk.sh` | ~1.7 sa |
| C1 ön-eğitimi (3.0M çekirdek) | `./egit_c1.sh` | ~2.8 sa |
| B + v2 ince ayar + QAT + dışa aktarma | `./ince_ayar_v2.sh` | ~20 dk |
| C1 + v2/v3 ince ayar + QAT + dışa aktarma + test seti | `./ince_ayar_c1.sh c1ft` | ~30 dk |
| Sadece oyuncak verisiyle ince ayar (deney) | `STEPS=2500 ./ince_ayar_c1.sh c1saf --genel-token 0 --tekrar 20` | ~20 dk |

Eğitim koduna eklenenler (`research/tinystories/train.py`):
- `--ckpt-every`, otomatik devam, `*.progress.json`
- `--init-from` (ince ayar için)
- `--qat-emb` — **sıkıştırmaya duyarlı eğitim**: kelime tablosu ileri geçişte 4-bit ızgarada görülür
  (straight-through). Aşağıdaki "Önemli bulgular"a bakın.

Dışa aktarma (`research/tinystories/export.py`) tek bir `model.bin` (ESP32 formatı) + `golden.txt` üretir;
`runtime/host_verify/verify.c` C motorunun PyTorch ile birebir aynı sonucu verdiğini doğrular.

Model boyutu / flash / hız tahmini: `python tools_boyut.py`

---

## Hikâye üretimi

Kartta ve PC'de aynı mantık (`runtime/host_verify/gen.c`, `baslangic.py`, `degerlendirme/sec.py`):

1. **Başlık:** `Karakter: <tür[, tür2]> | Yer: <yer>\n\n` — eğitimdeki biçim, ikili sırası katalog sırası.
2. **Örnekleme:** temperature 0.5, top-k 40, **tekrar cezası 1.1** (son 64 token, her token bir kez).
3. **Yasak isim listesi:** okutulmayan figürlerin ve sık görülen yabancı isimlerin token'ları maskelenir.
   Ölçüm: yanlış/yabancı isim oranı %47 → **%0**, figürlerin hikâyede kalması %88 → %93.
4. **Aday seçimi:** K aday üretilir (oyuncak boştayken / şarjdayken), en yüksek puanlı saklanır.
   Puan = kural cezaları + 2 × ortalama log-olasılık. Kurallar: figür yeterince geçmiyor / sonda kayboluyor,
   "X ve X", kendine gönderme, aynı konuşmacı üst üste, yanlış isim, sonradan beliren karakter, yer kayması,
   tekrarlanan cümle/ifade, yarım son, sözlükte olmayan (uydurma) kelime.
   Kuralları temiz geçen hikâyeler hakemden ort. **5.6**, geçemeyenler **3.2** aldı.

`gen.c` kullanımı:
```
./gen <model.bin> <n_token> <temp> <top_k> <seed> <rep> [-b id,id,...] [-l] <prompt token id'leri...>
   -b : yasaklı token id'leri       -l : her token'ın log-olasılığını da yaz
```

---

## Kalite ölçümü (hakem düzeni)

`degerlendirme/`:

| Dosya | Görev |
|---|---|
| `RUBRIK.md` | 10 puanlık katı rubrik (figür yanlış −4, karakter karışık −3, mantıksız −2…) |
| `uret.py` | Sabit 36 vakalık test setini üret: `python degerlendirme/uret.py hf_c1ft c1ft_t05_sec16 --aday 16 --temp 0.5 --rep 1.1` |
| `sec.py` | Aday seçici (kural cezaları + log-olasılık) |
| `izgara.py` | Üretim ayarı taraması (hakemsiz: uydurma kelime oranı + kural cezası) |
| `ozet.py` | Hakem puanlarını topla: `python degerlendirme/ozet.py <ad>` |
| `sozluk_olustur.py` | Uydurma kelime kontrolü için sözlük (`sozluk.pkl`) |
| `<ad>/hikayeler.json`, `puan_*.json` | Her deneyin hikâyeleri ve hakem puanları |

Hakemler, `parti_*.json` dosyalarını okuyup `puan_*.json` yazan bağımsız Claude ajanlarıdır.

---

## PC'de test arayüzü

```bash
.venv/bin/python server.py          # http://localhost:8765
```

- **📡 Figür okuyucu (NFC simülasyonu):** figüre tıkla = okut; bip + isim sesi; en fazla 2 figür + yer kartı;
  3 sn sonra hikâye başlar.
- **Model seçimi:** Oyuncak v2 (büyük model), Oyuncak v1, Türkçe temel model, İngilizce + çeviri.
- **Ses:** Piper `tr_TR-dfki-medium` (offline Türkçe), cümle cümle akış, okunan cümle vurgulanır,
  "oyuncak hoparlörü" filtresi (küçük 3W hoparlör simülasyonu), okuma hızı.
- **Ayarlar:** yaratıcılık (temperature), tekrar cezası, top-k, uzunluk, seed, "greedy" (kartın eski hali).
- **Eğitim sayfası:** http://localhost:8765/egitim — canlı eğitim ilerlemesi, perplexity grafiği,
  hikâye yazım sayacı, "eğitimi başlat / devam ettir" düğmesi.

Arayüzün modelleri `hf_*/` klasörlerinden okur (depoda yok; aşağıdaki komutlarla üretilir).

---

## Kurulum ve komutlar

```bash
git clone https://github.com/yusuf7855/hikaye-oyuncak && cd hikaye-oyuncak
/opt/homebrew/bin/python3.13 -m venv .venv          # Python 3.13
.venv/bin/pip install torch numpy requests pyarrow tokenizers piper-tts ctranslate2 sentencepiece
cc -O3 -o gen runtime/host_verify/gen.c -lm         # PC üretim motoru (ESP32 ile aynı C kodu)
cc -O2 -o gen_verify runtime/host_verify/verify.c -lm

# 1) Türkçe veri
mkdir -p data/tr_tinystories/raw
curl -L -o data/tr_tinystories/raw/train.arrow \
  https://huggingface.co/datasets/esat-krky/TinyStories_Turkish/resolve/main/train/data-00000-of-00001.arrow
.venv/bin/python -c "
import pyarrow as pa
t = pa.ipc.open_stream('data/tr_tinystories/raw/train.arrow').read_all()
with open('data/tr_tinystories/raw/tr-tinystories.txt','w',encoding='utf-8') as f:
    for s in t.column('text').to_pylist():
        if s and s.strip(): f.write(s.strip() + '\n<|endoftext|>\n')"
TS_DATA=data/tr_tinystories PYTHONPATH=src .venv/bin/python -m research.tinystories.prepare_tr --vocab 16384

# 2) Ön-eğitim (C1) ve ince ayar
./egit_c1.sh                      # kaldığı yerden devam eder
./ince_ayar_c1.sh c1ft            # -> hf_c1ft/model.bin + test seti

# 3) Ses (PC önizlemesi)
mkdir -p voices && cd voices && B=https://huggingface.co/rhasspy/piper-voices/resolve/main/tr/tr_TR/dfki/medium \
  && curl -LO $B/tr_TR-dfki-medium.onnx && curl -LO $B/tr_TR-dfki-medium.onnx.json && cd ..

# 4) Arayüz
.venv/bin/python server.py
```

> **Uyarı:** M3'te iki eğitimi aynı anda çalıştırmayın — MPS paylaşımında ikisi de ~10× yavaşlıyor.

---

## ESP32'ye geçiş planı ve donanım

**Hazır olanlar:** 4-bit model formatı (upstream firmware ile uyumlu, C doğrulaması geçiyor), örnekleme,
tekrar cezası, yasak isim listesi, başlık biçimi, aday seçici kuralları — hepsi PC'de, ESP32'de çalışacak
C/basit metin işlemleri olarak test edildi.

**Kart gelince:**
1. `firmware/esp32_tinystories` ile C1 modelini yükleyip **gerçek hızı ölç** (tahmin 4.1 tok/s).
2. Firmware'e ekle: rastgele örnekleme (şu an greedy), tekrar cezası, yasak token listesi, NFC → başlık,
   aday üret + seç, hikâyeleri flash/SD'de kuyrukta tut (şarjdayken üret).
3. NFC: PN532 (I2C) ya da iki yuvalı RC522 (SPI).
4. TTS: ESP32'de nöral TTS sığmıyor → SD kartta kelime + kalıp cümle bankası, cümle sonu / soru tonlaması
   varyantları, hece birleştirme yedeği (Türkçe fonetik olduğu için uygun). Banka Piper ya da seslendirme
   sanatçısıyla bir kez üretilir (**ses lisansını ticari kullanım için kontrol edin**).

**Donanım listesi (yaklaşık, 2026 TL):** ESP32-S3 N16R8 (~490), MAX98357A (~200–380), 40–50 mm hoparlör,
TP4056 + 18650/LiPo, microSD, NFC modül + NTAG213 etiketler.

---

## Önemli bulgular / dersler

1. **4-bit'te hasarın neredeyse tamamı kelime tablosundan (`tok_emb`) geliyor.** d_model ≤ 128 olduğu için
   satır başına tek ölçek var; birkaç aykırı değer diğer ağırlıkları yok ediyor (fp32 kayıp 3.43 → int4 4.67).
   Çözüm: `--qat-emb` ile ince ayar + dışa aktarmada `tok_emb` için max-abs, diğer tensörlerde MSE-optimal
   kırpma. Sonuç 4.67 → 3.75. `verify.c` bunu **yakalamaz** (golden da 4-bit); ayrı ölçün.
2. **Kelime dağarcığını 32k → 16k indirmek neredeyse bedava** (sadece %3 daha fazla token) ama çıkış
   katmanını yarıya indirip çekirdeğe bütçe açıyor.
3. **Tekrar cezası + yüksek sıcaklık = uydurma kelime.** temp 0.4–0.5 / rep 1.1 en iyisi (uydurma kelime
   %1.2 → %0.2).
4. **Sabit isimler + yasak isim listesi** isim çorbasını bitirdi; ilk cümleyi şablonla vermek ise işe
   yaramadı (figür sadakatini düşürdü).
5. **Veri 10/10, model değil:** eğitim hikâyeleri 9.83 alırken model 4.94. Kalan fark model kapasitesi ve
   taklit gücü.
6. Kartın bağlamı 256 token → hikâyeler ≤ ~150 kelime olmalı.

---

## Yol haritası

- [x] Türkçe ön-eğitim, B ve C1 modelleri
- [x] 12 figür, 2300+ sabit isimli oyuncak hikâyesi (v2 + v3)
- [x] 4-bit QAT, yasak isim listesi, aday seçici, hakem düzeni
- [x] PC test arayüzü + NFC simülasyonu + Türkçe ses
- [ ] C1 ince ayar sonuçlarının hakem puanı; "sadece oyuncak verisi" deneyi
- [ ] Gerçek ESP32-S3 hız ölçümü, firmware'e örnekleme/yasak liste/seçici
- [ ] NFC donanımı, kelime-bankası TTS
- [ ] **Hibrit seçenek:** 10/10 kalitedeki hazır hikâye kütüphanesini (~1 MB, flash'ta) modelle birlikte
      kullanmak — kalite garantisi + sınırsız yeni hikâye
- [ ] Figür isimlerini tek token yapmak (ör. "Paytak" 3 parça → üretmesi zor), yeni tokenizer ile C2

---

## Dizin yapısı

```
baslangic.py              figür → başlık, yasak isim token'ları
server.py, ui.html        test arayüzü (hikâye + NFC simülasyonu + ses)
egitim.html               eğitim ilerleme sayfası
hikaye.py                 komut satırından hikâye üret (eski İngilizce model)
tools_boyut.py            model boyutu / flash / ESP32 hız tahmini
egit*.sh, ince_ayar*.sh   eğitim ve ince ayar zincirleri (kaldığı yerden devam eder)
data/karakterler.json     figür kataloğu (NFC kimlik, isim, sıfat, açılış cümleleri)
data/oyuncak_*/           oyuncak hikâyeleri + kılavuz + kontrol + iş kuyruğu
degerlendirme/            rubrik, test seti üretimi, seçici, hakem puanları
research/tinystories/     eğitim (train.py), veri hazırlama (prepare_*.py), dışa aktarma (export.py)
runtime/                  ESP32 C çalışma zamanı (llm.h) + host_verify/ (gen.c, verify.c)
firmware/                 upstream ESP32 firmware'leri
src/                      model tanımı (PLE), kuantizasyon
docs/UPSTREAM_README.md   orijinal esp32-ai README'si
```

Depoda **olmayanlar** (büyük / yeniden üretilebilir): `.venv/`, `data/tr_*` (token dosyaları),
`runs/` (checkpoint'ler), `hf*/` (dışa aktarılmış modeller), `voices/`, `tr/`, `logs/`.

---

## Lisanslar ve teşekkür

- Temel kod: [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) — MIT ([LICENSE](LICENSE)), © Viacheslav Sierbov
- Veri: [TinyStories](https://arxiv.org/abs/2305.07759) (Eldan & Li) ve
  [TinyStories_Turkish](https://huggingface.co/datasets/esat-krky/TinyStories_Turkish) — CDLA-Sharing-1.0
- PLE fikri: Google Gemma 3n
- Ses: [Piper](https://github.com/rhasspy/piper) `tr_TR-dfki-medium` — ürün için ses lisansını kontrol edin
- Çeviri (sadece İngilizce model önizlemesi): [Argos Translate](https://github.com/argosopentech/argos-translate) en→tr
- Oyuncak hikâyeleri ve değerlendirme: Claude Code ajanlarıyla üretildi
