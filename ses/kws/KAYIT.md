# Gerçek çocuk kaydı: "Merhaba Eko" ve komutlar

Şu anki model yalnız **yapay** sesle eğitildi (Supertonic 3 + WORLD ile çocuk sesi benzetimi). Gerçek 3–6 yaş çocuk
sesi tonlama, söyleyiş ve ortam bakımından ondan farklıdır; ürün çıkmadan önce gerçek kayıtla ince ayar ve ölçüm
**şarttır**. Hedef: **~20 aile**, her aileden 1–2 çocuk (3–6 yaş), ayrıca isteyen anne/baba.

## 1. İzin ve kişisel veri (önce bu)

Çocuk sesi KVKK kapsamında kişisel veridir. Kayıttan önce:

- **Veli açık rızası** (yazılı, imzalı) + **aydınlatma metni**: amaç (yalnız oyuncağın "Merhaba Eko" ve komutları
  tanıması için ses modeli eğitmek ve ölçmek), saklama süresi (ör. ürün geliştirme bitince en geç 2 yıl), kimlerin
  erişeceği (yalnız geliştirme ekibi), yurt dışına aktarım olmadığı, silme hakkı ve başvuru yolu.
- Kayıtlar **ad yerine kodla** saklanır (A01, A01-C1). Ad–kod eşlemesi ayrı, kilitli bir dosyada; ses klasöründe ad yok.
- Çocuğa kendi adını, adresini, okulunu söyletmeyin; söylerse o kaydı silin.
- Çocuğun da gönlü olmalı: oyun gibi, istemezse ya da yorulursa hemen bırakılır. Kayıt ~15 dk'yı geçmesin.
- Kayıtlar internete, ortak bulut klasörüne, yapay zekâ hizmetlerine yüklenmez; şifreli diskte tutulur.
- Veli isterse kayıtları dinleyip silebilir; silme isteğinde eğitim yeniden yapılır.
- Satış/pazarlama amaçlı kullanılmaz; modelin ağırlıkları kayıtları geri vermez ama yine de aydınlatma metninde yazın.

## 2. Donanım ve ortam

- **En iyisi: oyuncağın kendisiyle** (stand üstündeki INMP441 mikrofonu, 16 kHz). Bunun için kartta basit bir "kayıt
  modu" gerekir (mikrofonu seri porta/SD'ye yazar; kws.h'ye giden PCM'in aynısı). Yoksa telefonla kaydedin:
  WAV, mono, 16 kHz ya da 44,1/48 kHz (betik çevirir), otomatik kazanç/gürültü azaltma KAPALI (mümkünse).
- Telefon/oyuncak, çocuğun oynadığı yerde masaya konur; çocuk **0,5–2 m** uzakta, bazen yakın, bazen uzak.
- Ortamlar (her ailede en az ilk üçü):
  1. sessiz oda,
  2. **oyuncak hikâye okurken** (en önemlisi: kartın hoparlöründen ses gelirken çocuk "Merhaba Eko" der),
  3. ev gürültüsü (TV, mutfak, kardeş sesi),
  4. çocuk oyun oynarken / yürürken.

## 3. Söylenecekler (her çocuk için)

3–4 yaş okuyamaz: veli **ifadeyi söylemez**, durumu anlatır ("Oyuncak çok yüksek konuşuyor, ona ne dersin?",
"Hikâyeyi beğenmedin, ne dersin?"). Taklit tonlaması yerine çocuğun kendi sözleri gelsin; çocuk farklı bir şey derse
(ör. "Bunu istemiyorum") o da kaydedilir ve klasörüne konur (sınıfı belirsizse `KONUSMA`).

| Sınıf (klasör) | İfadeler | Adet (çocuk başına) |
|---|---|---|
| `UYANDIRMA` | "Merhaba Eko" (normal, bağırarak, fısıltıyla, uzatarak "Merhaba Ekooo", hızlı) | 15–20 |
| `DUR` | "Dur", "Dursun", "Sus" | her biri 3–4 |
| `DEVAM` | "Devam", "Devam et", "Hadi" | her biri 3–4 |
| `BASKA` | "Başka", "Başka masal", "Bunu sevmedim" | her biri 3–4 |
| `BIR_DAHA` | "Bir daha", "Yine", "Tekrar" | her biri 3–4 |
| `SESI_AC` | "Sesini aç", "Yüksek", "Duyamıyorum" | her biri 3–4 |
| `SESI_KIS` | "Sesini kıs", "Çok yüksek", "Yavaş konuş" | her biri 3–4 |
| `KONUSMA` (olumsuz) | "Merhaba", "Eko" (tek başına), "Merhaba anne", "Merhaba" + bir arkadaş adı, "Eko gel", "Uykum geldi", "İyi geceler", "Su istiyorum", 1–2 dk serbest konuşma (oyun sırasında) | 20+ |
| `ARKA` (aile başına) | oyuncak hikâye okurken hiç konuşulmayan 5–10 dk; TV/mutfak sesi 5 dk | uzun dosya |

Komutların yarısı "Merhaba Eko"dan hemen sonra (1–2 sn içinde, gerçek kullanım gibi) söylenmeli: o zaman tek dosyada
"Merhaba Eko ... dur" olur — **iki ayrı dosyaya kesin** (UYANDIRMA/ ve DUR/), aradaki sessizlik iki dosyada da kalsın.
Anne/baba da 5–10 kez "Merhaba Eko" ve birkaç komut söylesin (`<aile>/V1/...`).

## 4. Dosya düzeni

```
kws_kayit/
  A01/
    C1/UYANDIRMA/001.wav  002.wav ...      # her dosyada TEK söyleyiş (başta/sonda biraz sessizlik olabilir)
    C1/DUR/001.wav ...
    C1/KONUSMA/001.wav ...
    V1/UYANDIRMA/001.wav ...               # veli
    ARKA/hikaye_okurken.wav  tv.wav        # uzun arka plan kayıtları
  A02/ ...
  bilgi.csv     # aile,kisi,yas,cihaz(telefon/oyuncak),ortam,not   (AD YOK)
```

Uzun kayıttan kesmek için Audacity: "Analiz > Sesi etiketle" (ya da elle etiket), sonra "Dışa aktar > Çoklu dosya"
(etikete göre). Söyleyişin tamamı dosyada olsun, başa/sona ~0,2 sn sessizlik bırakın. `kws_kayit/` depoya girmez.

## 5. İnce ayar ve ölçüm

```bash
.venv/bin/python ses/kws/ince_ayar.py --kayit kws_kayit --sinama-aile A04 A11 A17 A20   # ~4 aile sınama için ayrılır
.venv/bin/python ses/kws/degerlendir.py --model ses_kws_veri/calisma/ince.pt --yaz          # eşikler (yapay dev akışı)
.venv/bin/python ses/kws/disa_aktar.py --model ses_kws_veri/calisma/ince.pt                 # generated/kws_model.h
.venv/bin/python firmware/hikaye_oyuncak/tools/kws_test.py --model ses_kws_veri/calisma/ince.pt   # C = PyTorch
```

- Sınama aileleri eğitimde **hiç** kullanılmaz (aynı çocuğun sesi iki tarafta olursa sonuç yanıltır).
- Kabul için öneri (sınama ailelerinde): sessiz odada uyanma ≥ %95, hikâye okunurken ≥ %85, uyanınca komut doğru
  ≥ %90; ARKA kayıtlarında (hikâye okunurken) yanlış uyanma saatte ≤ 0,2.
- Gerçek kayıt çoğaldıkça (≥ 40 çocuk) eşikler de gerçek sınama aileleriyle seçilmeli (şimdilik yapay dev akışıyla).
- Kartın kendi kaydı en değerlisidir: telefonla kaydedilen veriyle eğitilip oyuncakta denenince fark görülürse, birkaç
  aileyi oyuncağın mikrofonuyla yeniden kaydedin.
