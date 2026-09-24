# Türkçe kadın sesi araştırması

> 24 Eylül 2026. Dört araştırmacı (hazır modeller, kendi sesini eğitmek, bulut/ticari üretim, cihaz içi seçenekler)
> 26 ajanla aday topladı; her aday için "gerçekten kadın mı, satılan oyuncakta kullanılabilir mi, internetsiz
> çalışır mı" ayrıca doğrulandı. Örnek sesler oturumun geçici dizininde üretildi (depoya alınmadı).
> ESP32 bütçesi (docs/ESP32_BUTCE.md) ses için difon + kelime + kalıp bankasını seçiyor; buradaki öneri o bankanın
> hangi kadın sesinden üretileceğine dair.

**Özet:** Önizleme için hemen Supertonic 3'ün kadın seslerine (F2 ya da F5) geçin. Oyuncağa girecek kelime bankasını da aynı sesle üretin. Yedek seçenek Amazon Polly'nin Burcu sesi. Bugün kullanılan dfki sesi hem erkek hem de ticari kullanıma kapalı, bu yüzden hiçbir kaydı oyuncağa girmemeli.

## 1) PC önizleme (server.py): şimdi en iyisi Supertonic 3, F2 ya da F5
- **Kadın olduğu ölçüldü.** Resmi belgede 5 kadın ses var. Bu makinede Türkçe denendi: F2'nin ses perdesi ~234 Hz (parlak, genç), F5'inki ~164 Hz (kadın aralığının alt ucu, daha olgun ve pes). Erkek M1 ~94 Hz çıktı. Çocuklara daha uygun görünen F2, ama seçim kulakla yapılmalı.
- **İnternetsiz çalıştığı doğrulandı.** Ağ tamamen kapalıyken ses üretildi. Tek seferlik indirme ~400 MB. Yalnızca işlemci yetiyor: tek çekirdekte, eğitim çalışırken 7,4 sn'lik ses 2,6 sn'de üretildi.
- **Dinlenecek örnekler:** `/tmp/claude-0/-home-user-hikaye-oyuncak/51a50a87-4e4c-59c8-8b0c-5316b89b1551/scratchpad/v_st3/out_F2_masal.wav`, `out_F5_masal.wav` ve `q_F2_*.wav`, `q_F5_*.wav` (soru tonu denemeleri).

## 2) ESP32 kelime/kalıp bankası (satılan oyuncak için)
**Birinci seçenek: Supertonic 3 (F2 ya da F5)**
- **Lisans** BigScience Open RAIL-M. Ticari kullanım serbest, süresiz ve geri alınamaz. Madde 6'ya göre üretilen ses üzerinde hak iddia edilmiyor.
- **Uyulması gereken koşullar:**
  - Ambalajda ya da kılavuzda "Bu oyuncaktaki ses yapay zekâ ile üretilmiştir" yazmalı (Ek A (e)).
  - Pazarlamada Supertone ya da Supertonic markası kullanılamaz (Madde 8).
  - Bu sesin çıktısıyla ileride küçük bir TTS modeli eğitilirse o model "türev" sayılır ve lisanstaki kısıtlar son kullanıcı sözleşmesine taşınmalı. Hazır ses bankası için bu gerekmez.
- **Artısı:** Model ağırlıkları sabit ve yerelde duruyor. Yıllar sonra çıkacak ek figür paketleri için eklenen kelimeler de aynı sesle üretilebilir.
- **Eksileri:**
  - Depo arşivlendi, güncelleme gelmeyecek.
  - Aynı metin her seferinde biraz farklı çıkıyor. "?" ile bitirmek soru tonunu garanti etmiyor (F2 "tavşan?" 3 denemenin 2'sinde yükseldi). Her varyant için birkaç deneme üretip otomatik seçmek gerekiyor.
  - Her klibin başında ve sonunda sessizlik var, kırpılmalı.

**İkinci seçenek: Amazon Polly, Burcu (nöral kadın ses)**
- Kadın olduğu AWS'nin ses tablosundan doğrulandı.
- Ticari koşulları en net olan seçenek. SSS'de "static voice prompts replayed multiple times" kullanımına açıkça izin veriliyor, çıktı müşteriye ait ve 13 yaş altı uygulamalara izin var.
- Maliyet: 1–2 milyon karakter için tahminen ~16–32 USD. İnternet yalnızca üretim sırasında gerekiyor.
- Kısıtlar:
  - Polly çıktısıyla model eğitmek yasak (Service Terms 50.5 ve 50.11).
  - Burcu'da perde (pitch) ayarı yok.
  - Burcu herkese açık bir ses, oyuncağa özgü olmaz.
  - Hece yedeğinin "benzer hizmet" sayılmaması için AWS'den yazılı teyit alınmalı.

**Diğer seçenekler**
- **VoxCPM2:** Apache-2.0, yani lisansı en serbest olan. Metinle tarif edilen kadın ses üç denemede 228–239 Hz ölçüldü. Ancak ekran kartı (GPU) gerekiyor ve her çalıştırmada ses değişiyor. Oyuncağa özgü bir ses isteniyorsa değerlendirilebilir. Örnekler aynı scratchpad klasöründe: `vd_tr_0.mp3`, `vd_tr_1.mp3`, `vd_tr_2.mp3`.
- **Uzun vadede en kaliteli yol:** Kadın seslendirme sanatçısı kaydı, yazılı hak devri ve KVKK açık rızasıyla. Maliyeti tahminen 70–200 bin TL veya üzeri. Sendika tarifesinin yapay zekâ notu yüzünden süreli lisans ve tekrarlayan ödeme istenebilir.

## 3) Kaçınılacaklar ve nedenleri
- **tr_TR-dfki-medium (şu anki ses):**
  - Erkek.
  - Eğitim verisinin lisansı CC BY-NC-SA 4.0, yani ticari kullanım yasak.
  - İngilizce lessac sesinden türetilmiş; lessac lisansı yalnızca araştırmaya izin veriyor.
  - Bu sesle üretilen hiçbir şey SD karta girmemeli ve bu sesten ince ayar yapılmamalı. Aynı lessac kökü amy ve hfc_female seslerinde de var.
- **Ticari kullanıma kapalı modeller:**
  - XTTS-v2: lisansı çıktıyı da ticari kullanıma kapatıyor.
  - MMS-TTS-tur: NC lisanslı, ölçümde erkek çıktı.
  - F5-TTS ve Türkçe ince ayarları, OmniVoice: NC lisanslı.
- **Erkek çıkan ya da hak zinciri belirsiz olanlar:**
  - Antalia verisi: kartta "she" yazıyor ama ölçülen perde ~108 Hz, yani erkek aralığında. Hak zinciri de doğrulanamadı.
  - 99eren99 Piper sesi: erkek ve lisanssız.
  - Coqui glow-tts: erkek (Talent_TR_Male verisiyle eğitilmiş).
  - sanoTTS'in Türkçe modeli: dfki'den türemiş, dolayısıyla erkek ve NC.
- **Ek koşulları sorunlu bulut hizmetleri:**
  - ElevenLabs: önerilen "Doga" sesi aslında erkek. Kullanım politikası 9(r) 13 yaş altını hedefleyen çözümleri kısıtlıyor.
  - Google Chirp 3 HD: koşullarda 18 yaş altı kısıtı (20(d)) ve "Google modelinin yerine geçme" yasağı (17(b)) var.
  - Azure: "benzer veya rakip ürün" yasağı geniş; Elif sesi henüz önizleme aşamasında.
  - Voiser: Google ve OpenAI seslerini yeniden satıyor, onların kısıtları zincirleme geçerli olabilir.
- **Kullanılamayacak diğerleri:**
  - MBROLA tr2: satılan üründe izinsiz kullanım yasak, izin adresi e-posta almıyor.
  - Commencis: veriye erişilemiyor, lisans yok.
  - Common Voice'tan tek bir konuşmacının sesini ürün sesi yapmak: kişilik hakları ve MDC koşulları açısından riskli.
  - Chatterbox: bu işlemcide gerçek zamandan ~107 kat yavaş.
  - MOSS-Nano'nun hazır sesleri: aralarında Trump ve anime karakteri sesleri var.
  - espeak-ng tr+f3: robotik ses.

## 4) Somut adımlar ve maliyet
1. Kurulum:
   `.venv/bin/pip install supertonic==1.3.1 "huggingface_hub[cli]"`
   `.venv/bin/hf download supertone-oss-archive/supertonic-3 --revision aafc6e32416a594460b32413efc49d7fe4ce6d46 --local-dir voices/supertonic-3`
   (Bu sabit sürümle indirme test edildi. `auto_download=True` kullanılırsa kod hâlâ eski depodan indiriyor.)
2. `server.py` değişikliği (taslak; kullanılan API çağrıları doğrulama testinde çalıştı):
   - Satır 13'e ekle: `from supertonic import TTS as STTS` ve `import tempfile`
   - Satır 42'deki Piper yüklemesinin yerine:
     `st = STTS(model_dir=os.path.join(HERE,"voices/supertonic-3"), auto_download=False, intra_op_num_threads=1, inter_op_num_threads=1)`
     `SESLER = {v: st.get_voice_style(voice_name=v) for v in ("F2","F5")}`
   - `tts()` içinde (satır ~138–148):
     `ses = q.get("ses") if q.get("ses") in SESLER else "F2"`
     `hiz = min(2.0, max(0.7, 1/float(q.get("length",1.0))))`
     `wav,_ = st.synthesize(text, voice_style=SESLER[ses], lang="tr", speed=hiz, total_steps=8)`
     Ardından `st.save_audio(wav, geçici_dosya)` ile yazıp dosyayı okuyun ve mevcut `reply(200,"audio/wav",...)` ile gönderin.
   - Piper satırlarını kaldırın ya da yalnızca A/B karşılaştırması için tutun.
   - Web arayüzüne `&ses=F2/F5` seçici eklenebilir.
3. Ürün sahibi F2 ve F5'i gerçek 3 W hoparlör ve MAX98357A üzerinden, çocuklarla birlikte dinleyip bir ses seçsin.
4. Banka için yeni bir betik yazılmalı (ör. `ses_bankasi_uret.py`):
   - Kelime listesi olarak `web/sozluk.txt` kullanılabilir, ama önce "aaa", "anneee" gibi 306 bozuk giriş temizlenmeli. Başlangıç için en sık 5–8 bin kelime yeterli; bunlar eğitim hikâyelerindeki kelimelerin %96,3–98,6'sını kapsıyor.
   - Her kelime için üç varyant: "kelime,", "kelime." ve "kelime?". Her varyanttan 3 deneme, sabit seed ile.
   - En iyi denemeyi otomatik seçin: Whisper ile doğru okunmuş mu, "?" varyantında perde yükseliyor mu.
   - Ardından: sessizlik kırpma, ses yüksekliğini eşitleme, 16 veya 22,05 kHz mono'ya indirme, IMA-ADPCM, tek büyük banka dosyası ve indeks.
   - Süre tahmini: bu makinede tek çekirdekle ~14 saat (yük altında ölçülen kelime başına ~0,7 sn'den hesaplandı).
5. Hukuk:
   - "Yapay zekâ ile üretilmiştir" ibaresinin ambalajdaki biçimini hukukçuya onaylatın.
   - Supertonic LICENSE dosyasının bir kopyasını ve ses bankasını arşivleyin.
   - Hazır seslerin lisans kapsamında olduğunu teyit etmek için contact@supertone.ai'ya yazın (yanıt gelmeyebilir).
   - Polly'ye geçilirse AWS'den hece yedeği için yazılı teyit alın.

**Maliyet**
| Kalem | Tutar |
|---|---|
| Supertonic | 0 TL. Emek: server.py yarım gün, banka betiği ve dinleme kontrolü 1–2 gün |
| Polly (yedek) | ~16–32 USD. Yeni AWS hesaplarına 200 USD'ye kadar kredi veriliyor |
| VoxCPM2 | GPU kiralama birkaç–10 USD (doğrulanmamış tahmin) |
| Hukukçu | bilinmiyor |
| Seslendirme sanatçısı | 70–200 bin TL veya üzeri (tahmin) |

**Doğrulanmamış noktalar:**
- Hiçbir sesi bir insan kulakla dinlemedi. Sıcaklık, Türkçe aksan ve çocuğa uygunluk ölçülmedi; bunu ürün sahibinin dinleme testi gösterecek.
- Banka üretim süreleri tahmin.
- Supertonic'in hazır seslerinin lisans kapsamında olduğu yalnızca çıkarım (ayrı bir ses lisansı yok, ama yazılı teyit de yok).
- Polly'de hece yedeğine ne kadar izin verildiği yoruma açık.