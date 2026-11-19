# Ürün tanımı (ürün sahibinin kararları, 13 Ekim 2026) — bütün ajanlar için ortak

Yalnız Türkçe. İnternetsiz. Düğme YOK.

## Etkileşim
- Uyandırma sözcüğü: tek ve sabit: **"Merhaba Eko"** (çocuk söyleyişleri de tanınmalı: "Melhaba Eko", "Meraba Eko", "Merhaba Ekoo", "Eko!" tek başına DEĞİL — yanlış uyanmayı azaltmak için iki sözcük gerekli).
- Sesli komutlar ÇOCUĞA göre (3–6 yaş, kısa, doğal söyleyişler), yalnız uyandırmadan sonraki ~4 sn içinde:
  | Olay | Çocuğun diyebileceği |
  |---|---|
  | DUR | "Dur", "Dursun", "Sus" |
  | DEVAM | "Devam", "Devam et", "Hadi" |
  | BASKA | "Başka", "Başka masal", "Bunu sevmedim" (aynı oyuncağın başka hikâyesi) |
  | BIR_DAHA | "Bir daha", "Yine", "Tekrar" (son hikâyeyi baştan) |
  | SESI_AC | "Sesini aç", "Yüksek", "Duyamıyorum" |
  | SESI_KIS | "Sesini kıs", "Çok yüksek", "Yavaş konuş" |
- Uyku sesli komutla DEĞİL, gece figürüyle açılır (aşağıda "Uyku modu").
- Hiçbir komut karakter SEÇEMEZ. Hikâye yalnız standa konan oyuncağın hikâyesidir. Standda oyuncak yoksa hikâye okunmaz.
- **Hikâyeler her zaman özgün, kartın kendi yazdığı hikâyelerdir; kartta sabit hikâye yoktur** (ürün sahibinin kararı, 15 Ekim 2026):
  - İlk açılıştan itibaren kart boştayken bütün figürler için hikâye yazar: her hikâye için **5 aday**, seçici en iyisini saklar (standa konmuş oyuncaklar önce). Oyuncak konunca hazır hikâye hemen okunur.
  - Hazır hikâye yoksa (ör. Pinokyo için henüz yazılmamış): oyuncak konunca kart **hemen yazmaya başlar ve yazdıkça okur** (selam çalarken plan yazılır; her cümle biter bitmez okunur; bitmesi beklenmez, aday seçimi yok). "Dur" denirse anlatım susar, hikâye sessizce tamamlanır; "Devam" kaldığı cümleden sürer.
- Selamlama: "Merhaba Emre, şimdi sana Pamuk'un hikâyesini okuyacağım." (ad yoksa "Merhaba, şimdi sana ..."). Ek uyumu doğru olmalı (Keloğlan'ın, Pamuk Prenses'in, Pinokyo'nun, Nasreddin Hoca'nın, Bulut'un, Zıpzıp'ın, Tek Boynuzlu At'ın, Fıstık'ın ...). Açılıştan sonraki ilk selam hep bu; sonrakiler sırayla üç kalıp arasında döner ("Emre, bak kim geldi: Keloğlan! Dinlemeye hazır mısın?", "Hoş geldin Emre! Keloğlan yeni bir maceraya çıkıyor.").
- Ayarlar: "Ayar kartı" (NFC, nfc_no 200) standa konunca kart kendi Wi-Fi erişim noktasını açar (WPA2, her açılışta yeni 8 haneli şifre). Bağlanmanın iki yolu (19 Kasım 2026, ürün sahibinin isteği):
  - **Telefonla dokunma:** kart, standdaki ayar kartına o oturumun ağ adını ve şifresini NFC Wi-Fi kaydı olarak yazar (NDEF, "application/vnd.wfa.wsc"). Kart kaldırılıp telefonun arkasına dokundurulunca Android "Ağa bağlanılsın mı?" diye sorar; bağlanınca ayar sayfası kendiliğinden açılır. iPhone bu kaydı kendiliğinden işlemez.
  - **Sesli şifre:** oyuncak ağ adını ve şifreyi iki kez söyler; telefonun Wi-Fi ayarından bağlanılır (her telefonda).
  - Kart kaldırılınca ayar modu kapanmaz (telefona dokundurmak için): telefon 3 dakikada bağlanmazsa, bağlanan telefon ayrıldıktan 2 dakika sonra, sayfadan "Bitir" ile ya da en geç 10 dakikada kapanır.
- Ayar sayfası: çocuğun adı ve **okunuşu** ("Adı dinle" ile oyuncak "Merhaba Emre! Adını doğru söylüyor muyum?" der), **alarm**, **alarm sesi yükleme**, **yatma vakti** ve **gece kilidi**, **sürpriz mesaj**, en yüksek ses, uyku zamanlayıcısı (10/20/30 dk), ninnide müzik kutusu, halka parlaklığı, oyuncak çekilince ne olsun, oyuncak tanıt (NFC etiketine figür yazma), hikâyeleri sil. Wi-Fi yalnız ayar modunda açık; internet hiç kullanılmaz.
- **Saat:** oyuncakta pil destekli saat yok. Ayar sayfası her açıldığında telefonun saati (ve saat dilimi) karta gönderilir; oyuncak açık kaldıkça kendi zamanlayıcısıyla sayar. Piller çıkarılırsa saat kaybolur ve alarm, yatma vakti, gece kilidi ayar sayfası yeniden açılana kadar çalışmaz.
- **Alarm (sabah):** saat, günler (hafta içi, her gün ya da seçilen günler), ne çalacağı: **Eko'nun sesi** ("Günaydın Emre! Kalkma vakti geldi." + ebeveynin yazdığı mesaj; rakamlar yazıyla okunur: "8'de" → "sekizde"), **müzik kutusu ezgisi** ya da **yüklenen ses** (müzik ve yüklenen seste günaydın bir kez söylenir). En çok 3 dakika çalar; standa oyuncak koyunca ya da kaldırınca, ya da "Merhaba Eko, dur" denince susar. Alarmı oyuncak koyarak susturan çocuk o oyuncağın hikâyesini dinler. Ses seviyesi alarmda en az 4 (en yüksek ses ayarını aşmadan).
- **Gün doğumu ışığı:** alarmdan 5–30 dakika önce (ayarlanır) halka koyu kırmızıdan sıcak beyaza yavaşça aydınlanır. Halka parlaklığı "kapalı" ise yanmaz.
- **Alarm sesi yükleme:** telefonda seçilen ses dosyası (mp3, m4a, wav ...) sayfada çözülür, tek kanala ve 8 kHz'e indirilir, istenen saniyeden başlayarak en çok 10 saniyesi alınır ve küçültülerek (IMA ADPCM, 40 KB) karta yüklenir. "Dinle" ve "Sil" düğmeleri var. Yer: flash'taki "alarm" bölümü (44 KB; ses bölümünün boşalan sonu, hikâye kuyruğundan yer alınmadı).
- **Yatma vakti:** seçilen saatte oyuncak "Emre, uyku vakti geldi. Ay Dede'yi standa koyarsan sana ninni söylerim." der (ninni çalıyorsa söylemez). **Gece kilidi** (isteğe bağlı): yatma vaktinden sabah saatine kadar hikâye figürü konunca hikâye yerine "Emre, şimdi uyku vakti. Hikâyeler sabah devam edecek. İstersen Ay Dede'yi koy, sana ninni söyleyeyim." der; Ay Dede (ninni) serbesttir.
- **Sürpriz mesaj:** ebeveyn sayfadan bir mesaj bırakır; çocuk oyuncağı bir dahaki sefere standa koyduğunda selamdan sonra bir kez söylenir ("Emre, sana bir mesaj var: Annen seni çok seviyor") ve silinir.
- Figür listesi ve halka renkleri: `data/figur_donanim.json` (nfc_no + renk; 26 Ekim 2026'dan beri Keloğlan 4, Ay Dede 12 ve lisanssız 12 figür 13–24; çıkan lisanslı figürlerin numaraları `cikarildi` ile durur, yeniden kullanılmaz). NFC etiketine figür numarası yazılır (NTAG213 kullanıcı belleği, sayfa 4+: sihir + sürüm + nfc_no + CRC).

## Uyku modu: gece figürü ("Ay Dede", nfc_no 12)
- Standa gece figürü konunca oyuncak **ninni moduna** geçer: ninni okur. Bu figür bir hikâye karakteri değil, bir mod figürüdür (bir geceyi temsil eder: ay, yıldızlar).
- **Ninniler sabittir (ürün sahibinin kararı, 15 Ekim 2026):** kartta **100 anonim halk ninnisi** durur; en bilinenler başta ("Dandini dandini dastana", "Uyusun da büyüsün", "Fış fış kayıkçı", "E bebeğim", "Ninni ninni ninnice" ...), gerisi halk derlemelerinden (Çelebioğlu, Demir, yöre derlemeleri; kaynaklar `firmware/hikaye_oyuncak/ninni_kaynaklar.tsv`). Metin uydurulmadı; model bu modda hiç yazmaz. Toplam ≈12,5 KB. Çocuğa uygun olmayan dizeler çıkarıldı, "oğlum/kızım" → "yavrum". Kaynak `firmware/hikaye_oyuncak/ninniler.txt`; `tools/ninniler.py` biçim denetimi yapıp `yerlesik.h`'yi üretir. Sırayla okunur, aynı ninni art arda gelmez; uyku zamanlayıcısı dolana dek ninniler sürer. Hiçbir ninnide ya da hikâyede kullanıcı yer seçmez: çocuk yalnız oyuncağı koyar.
- **Ses tonu değişir:** kartın ses modeli daha yavaş (≈%75 hız), daha alçak perde (≈−2 yarım ton), daha kısık ve cümle aralarında daha uzun duraklarla okur; isteğe bağlı çok kısık bir müzik kutusu melodisi (kartta sentezlenir, dosya gerekmez). Gerçek şarkı (melodili ninni) bu ses modeliyle mümkün değil: "ninni okur", söylemez.
- **Halka:** gece mavisi, yıldız gibi rastgele yavaş parıldayan birkaç LED; okuma bitince 60 sn'de söner; ardından oyuncak uyku zamanlayıcısıyla kapanır.
- Selamlama: "İyi geceler Emre, şimdi sana bir ninni söyleyeceğim." (ad yoksa "İyi geceler, ...").

## Halka (NeoPixel, WS2812B uyumlu) — standın üstünde, figürün çevresinde
- Ölçü (16 Ekim 2026, ürün sahibi): **NeoPixel 16'lı halka, dış Ø44,5 mm, iç Ø31,75 mm**, figürün hemen altında (ışık figürün altından yansır). Yazılımda `HALKA_LED_SAYISI 16`. (Önceki taslak: Ø104/Ø90 mm büyük halka.)
- 5 V beslenir; veri hattı 3,3 V → 5 V seviye çevirici (74AHCT1G125) + 330 Ω seri direnç; halka girişinde 1000 µF kondansatör. Yazılımda parlaklık üst sınırı (varsayılan %25) ve toplam akım sınırı (≤ 600 mA).
- Davranışlar:
  | Durum | Halka |
  |---|---|
  | Açılış | Gökkuşağı tek tur, sonra söner |
  | Boşta, oyuncak yok | Çok sönük "nefes alan" beyaz (ya da kapalı, ayardan) |
  | Oyuncak kondu | Figürün rengiyle halkanın dolması (≈0,6 sn) |
  | Selamlama / okuma | Figür renginde; ilerleme: hikâyenin okunan kısmı kadar LED dolu, kalan sönük (cümle cümle ilerler) |
  | Konuşma sesi | Okurken parlaklık sesin yüksekliğiyle hafifçe dalgalanır |
  | "Merhaba Eko" duyuldu | Beyaz dönen nokta = dinliyorum |
  | Komut anlaşıldı | Kısa yeşil yanıp sönme; anlaşılmadı: kısa turuncu |
  | Ses aç/kıs | Halka ses düzeyini gösterir (0..maks dolu LED, beyaz), 2 sn sonra eski haline döner |
  | Arka planda hikâye hazırlanıyor | Çok sönük, yavaş dönen figür rengi noktası (ayardan kapatılabilir) |
  | Uyku modu (gece figürü) | Gece mavisi, yavaş parıldayan yıldızlar, okuma bitince 60 sn'de söner |
  | Ayar modu | Turkuaz nefes |
  | Hata (model yok vb.) | Kırmızı yanıp sönme |

## Pin haritası (ESP32-S3-DevKitC-1 N16R8) — kesin, değiştirilecekse bütün belgeler birlikte
| Parça | Sinyal | GPIO |
|---|---|---|
| MAX98357A hoparlör yükselteci (I2S0) | BCLK / LRC / DIN / SD | 4 / 5 / 6 / 7 |
| INMP441 mikrofon (I2S1) | SCK / WS / SD (L/R → GND) | 15 / 16 / 17 |
| RC522 NFC okuyucu (SPI, 3,3 V) | SCK / MISO / MOSI / SDA(SS) / RST | 12 / 13 / 11 / 10 / 9 |
| NeoPixel halka | DIN (seviye çevirici üzerinden) | 18 |
| Kart üstü RGB LED | kullanılmaz | 48 (ya da 38) |
Kullanılmayacak uçlar: 0, 3, 45, 46 (açılış), 19/20 (USB), 26–37 (flash/PSRAM), 43/44 (UART).
Güç (ürün sahibi, 21 Ekim 2026): **4 x AA pil** (alttan vidalı pil kapağı) → açma-kapama anahtarı → 5 V düzenleyici
(Pololu S9V11F5, düşürür-yükseltir) → ESP32 5V, ses kartı, halka. USB-C girişi ve şarj devresi yok; kod yüklerken
taban açılır, ESP32'nin kendi USB-C'si kullanılır (anahtar kapalı).
