# Çakıl stand — baskıya hazır STL'ler

Hangi NFC okuyucuyu kullanacaksan o klasörü bas: `rc522/` ya da `pn5180/`. İki klasör yalnız `3_halka_nfc_tutucu.stl`'de
farklı (okuyucunun rayları); öteki parçalar aynı. Her parça **baskı yönünde, tablanın ortasında** kaydedildi: slicer'a
at, döndürme. Birim mm.

Yeniden üretmek: `python cad/cakil_ic.py --stl --onizle` (önce çarpışma denetimi; "0 sorun" yazmalı).
Ölçülerin bir kısmı TAHMİN (4'lü AA yatağı, hoparlör derinliği, KCD11, PN5180, MAX98357A, 5 V düzenleyici); parça
elinde olunca ölç, `cad/cakil_ic.py` PARCA sözlüğünde düzelt, yeniden üret. ESP32-S3 ölçüsü ürün sahibinin modelinden.

| Dosya | Adet | Baskı yönü | Malzeme / ayar |
|---|---|---|---|
| `0_tum_stand_*_montajli.stl` | — | BASILMAZ: tüm stand monte hâlde (bakmak için) | |
| `0_tum_stand_*_elektronikli_GORSEL.stl` | — | BASILMAZ: elektronik parçalar dahil (ESP32 gerçek model, ötekiler kutu) | |
| `1_kabuk.stl` | 1 | ters: üst yüz (figür çukuru) tablada | (renkli için `renkli_bambu/` bölümüne bak) **beyaz** PLA/PETG (LED ışığı figür zemininden ve çukur duvarındaki yarıklardan geçer). 0,2 mm katman, 3 duvar, %15 doluluk. **Destek: ağaç (tree), yalnız iç kısım** (vida kolonları, ses yakası). "eco ai" logosu için logonun başladığı katmanda filament değiştirilebilir |
| `2_taban_plakasi.stl` | 1 | düz alt yüz tablada | PLA/PETG. **Destek: yalnız tablaya değen (on build plate only)**: pil kutusunun tavanı ~60 mm köprü; destek kutunun içinde kalır, kapak deliğinden alttan sökülür |
| `2b_pil_kapagi.stl` | 1 | dış yüz (yazılı) tablada | PLA/PETG, destek gerekmez (dillerin altı 45° pahlı) |
| `3_halka_nfc_tutucu.stl` | 1 | ters: halkanın bastığı düz yüz tablada, raylar yukarı | PLA, destek gerekmez |
| `4_figur_taban.stl` + `4b_figur_kapagi.stl` | figür başına 1 + 1 | taban ters (düz üst yüz tablada), kapak alt yüzü tablada | figür adı ve numarası kazılı kapaklar `figurler/` klasöründe (figür başına tek dosya) |
| `5_ayar_karti.stl` | 1 | dik, topuz yukarı | + 1 kapak (`figurler/200_ayar_karti.stl`) |

## Ek malzeme

- M3 x 8 HAVŞA BAŞLI vida (4) + M3 ısıl gömme somun (4, Ø4,6 x 5,7; delik Ø4,0 x 6,5): taban plakası → kabuk (somunlar kabuğun 4 kolonuna havyayla gömülür)
- Halka/NFC tutucu VİDASIZ: kabuğun 4 direğinin ucundaki Ø5 pimler tutucunun tablalarına sıkı geçer (3 ezilen kaburga)
- Pil kapağı: M3 x 8 HAVŞA vida (1) + M3 ısıl gömme somun (1; taban plakasındaki kolona ALTTAN gömülür)
- 4'lü AA pil yatağı (yan yana 4 pil, kablolu) + ince çift taraflı bant (yatağın sırtı kutunun tavanına)
- 5 V düzenleyici: **Pololu S9V11F5** (5 V, düşürür-yükseltir; alkalin 6,4 V'tan şarjlı NiMH 4,4 V'a kadar sabit 5 V)
- Kablo bağı 2,5 mm (1): hoparlör
- Silikon ayak Ø10 x 1 mm (4)
- NTAG213 **Ø25** yuvarlak yapışkan NFC etiket (13): her figürün vidalı kapağının içine (12 figür + ayar kartı)
- Dişi-dişi jumper kablolar (ESP32 ters yatar, pinler yukarıda)

## Montaj sırası

Üst modül (kabuk ters dururken):
1. Isıl gömme somunları 4 kolona göm.
2. NeoPixel halkayı LED'ler tavandaki ışık oyuğuna girecek biçimde koy (kablosu arkada).
3. NFC okuyucuyu tutucunun raylarına kaydır; tutucuyu halkanın üstüne koy, 4 tablayı kabuğun 4 pimine hizala ve
   bastır (sıkı geçer; çıkarmak için tablaların yanından eşit çek). Pimler 10 mm: tutucu halkaya tam basmasa da tutar.
4. KCD11 anahtarı sol yandaki deliğe dışarıdan bastır (tırnaklar içte oturur).

Alt modül (taban plakası):
1. Ayakları yapıştır. Plakayı ters çevir, pil kapağı kolonuna M3 ısıl gömme somunu **alttan** havyayla göm.
2. 4'lü AA yatağını pilsiz, **açık yüzü aşağı** bakacak biçimde alttan kutuya sok; sırtını tavana ince çift taraflı
   bantla yapıştır. Kabloları tavandaki kablo deliğinden (önde, solda ya da sağda) yukarı çıkar.
3. Hoparlörü öndeki beşiğe oturt, kablo bağıyla sık. Kutunun tavanında: MAX98357A sağdaki, 5 V düzenleyici soldaki
   çerçeveye (bantla).
4. ESP32-S3'ü TERS tut (bileşenler aşağı, J1 sırası öne): USB-C ucunu (sağda) iki köşe kancasının altına kaydır, anten
   ucunu (solda) bastır, tırnak oturur.
5. Jumper'ları yukarıdan J1 pinlerine tak, kabloları bağla. Güç: pil + (kırmızı) → anahtar → düzenleyici VIN;
   düzenleyici VOUT → 5 V (ESP32 5V, MAX98357A VIN, halka 5V); bütün GND'ler ortak.

Birleştir: kabuğu alt modülün üstüne indir, alttan 4 M3 vidayla sık. Pilleri tak: kapağın iki dilini soldaki yuvalara
sok, kapağı kapat, sağdaki M3 havşa vidayı sık. Kod yüklemek için taban açılır (ESP32'nin USB-C ucu sağda açıkta);
bu sırada anahtar KAPALI olsun.

## Renkli baskı (Bambu Lab P2S Combo / AMS, 4 renk) — `renkli_bambu/`

Her `.3mf`'yi Bambu Studio'da aç: parçalar filament 1–4'e atanmış, tablaya yerleşmiş gelir. AMS'e şu sırayla tak:

| AMS | Renk |
|---|---|
| 1 | **beyaz** |
| 2 | turkuaz |
| 3 | sarı |
| 4 | mor |

| Dosya | Renkler | Not |
|---|---|---|
| `1_kabuk.3mf` | beyaz gövde, turkuaz "eco ai" ve çukur zemini, sarı çukur kenarı, üst yüzde 8 mor yıldız (dış sarı halkanın yerinde) | LED'lerin üstündeki ışık halkası beyaz kalmalı. Destek: ağaç (tree), yalnız iç kısım. Logo dikey duvarda: logo boyunca her katmanda renk değişir (en çok atık burada) |
| `2_taban_plakasi.3mf` | beyaz plaka; alt yüzde (pil kapağının önünde) turkuaz "eco ai" | renkler ilk 3 katmanda, alttan okunur; destek: yalnız tablaya değen (pil kutusu tavanı) |
| `2b_pil_kapagi.3mf` | beyaz kapak; dış yüzde turkuaz "4 x AA / 1,5 V" | destek yok |
| `3_halka_nfc_tutucu_rc522.3mf` / `_pn5180.3mf` | beyaz (LED ışığını yansıtır), turkuaz "ÖN" ve ok | yalnız birini bas; montajda ok kabuğun ÖNÜNE (logo tarafına) bakar |
| `4a_figur_tabanlari_ay_dede_ayar_karti.3mf` | 11 turkuaz figür tabanı Ø52 (üstte sarı halka), Ay Dede (turkuaz taban, sarı hilal), mor ayar kartı (topuzda beyaz çark) | tek tablada 13 parça |
| `4b_nfc_kapaklari.3mf` | 13 sarı adlı vidalı NFC kapağı | tek tablada 13 parça |

Atık kulesi (prime tower) açık kalsın. 3MF açılmazsa ya da renkler gelmezse: aynı parçanın renk STL'lerini
(ör. `1_kabuk_1_beyaz.stl` … `1_kabuk_4_mor.stl`) birlikte seçip Bambu Studio'ya sürükle, "tek nesne, çok parça
olarak yükle?" sorusuna **Evet** de, sonra her parçaya sağ tık → filament seç. Dosya adının sonundaki numara AMS yuvasıdır.

## Figür tabanları ve vidalı NFC kapağı — `figurler/`

Her figür için tek dosya (iki parça yan yana, baskı yönünde): **taban** Ø52 x 8 (5 mm standın çukurunda, 3 mm üstte;
düz üst yüzüne oyuncak figür yapıştırılır) + **kapak** (şişe kapağı gibi tabanın altına vidalanır, 1,5 tur).
Kapağın içine Ø25 NTAG213 yapışkan etiket yapıştırılır; etiket antene ≈ 2,9 mm. Kapağın alt yüzünde bozuk para
yarığı, figürün adı ve NFC numarası (etikete yazılacak numara) kazılı. Ay Dede tabanla tek parça hilal ay (dik basılır).

| No | Figür | Dosya |
|---|---|---|
| 1 | Niloya | `figurler/01_niloya.stl` |
| 2 | Maşa | `figurler/02_masa.stl` |
| 3 | Pepee | `figurler/03_pepee.stl` |
| 4 | Keloğlan | `figurler/04_keloglan.stl` |
| 5 | Doru | `figurler/05_doru.stl` |
| 6 | Hayri | `figurler/06_hayri.stl` |
| 7 | Şakir | `figurler/07_sakir.stl` |
| 8 | Elsa | `figurler/08_elsa.stl` |
| 9 | Chase | `figurler/09_chase.stl` |
| 10 | Örümcek Adam | `figurler/10_orumcek_adam.stl` |
| 11 | Hello Kitty | `figurler/11_hello_kitty.stl` |
| 12 | Ay Dede | `figurler/12_gece.stl` |
| 200 | Ayar kartı | `figurler/200_ayar_karti.stl` |

Diş: adım 2 mm, erkek Ø30/Ø28, dişi oyuk 0,35 mm yarıçap ve 0,25 mm yanak boşluklu (FDM). Sıkı gelirse kapağı
%100,5 ölçekle değil, `cakil_ic.py` VIDA_PAY'ı 0,45 yapıp yeniden üret. Boş taban/kapak: `bos_figur_taban.stl`,
`bos_kapak.stl`. Lisanslı karakterlerin kendisi çizilmez; hazır oyuncak figür yapıştırılır.

## v5 (21 Ekim 2026, baskıdan sonra)

- **Hoparlör beşiğinin kolları** (ve alt modüldeki her şey) kabuğun alt ağzından geçecek kadar içeri alındı (r ≤ 55,0):
  kabuk indirilirken 1-SAĞ kolunun köşesi kabuğun alt kenarına takılıyordu. Çarpışma denetimi artık kabuğu alt modülün
  üstüne indirmeyi de dener.
- **Tutucu direkleri** 45°/135° → 38°/142° (öndekiler hoparlörden ~3 mm uzakta, okuyucunun köşesine de değmez).
- **Tutucu vidasız, pimli:** direklerin ucunda Ø5 x 10 pim, tutucunun tablalarında 3 kaburgalı delik (0,12 mm sıkı).
- **ESP32** y −34,5 → −32,7 (köşeleri kabuğun alt ağzından geçer); jumper payı 14 + 2 mm: kabloları yana yatır ya da
  90° açılı jumper / lehim kullan.

## Pil kutusu (21 Ekim 2026): USB-C ve şarj kalktı, 4'lü AA geldi

- **Kalkanlar:** USB-C deliği ve fiş cebi (kabuk arkası artık düz), TP4056 kaidesi, 18650 cebi, ikinci hoparlör eyeri
  (pil kutusu oraya geldi; kutunun ön duvarı hoparlörün 5 mm arkasında).
- **Pil kutusu** taban plakasının ortasında: iç 63,3 x 58,8 mm, duvar 2,4, tavan 1,6 (z 18,7–20,3). 4'lü AA yatağı
  (tahmin 62,5 x 58 x 15,5) ters durur, piller alttan takılır.
- **Pil kapağı** taban plakasıyla aynı hizada (2,4 mm): solda iki dil plakadaki yuvalara girer, sağda tek M3 havşa
  vida (tornavidasız açılmaz: 3–6 yaş için oyuncak güvenliği). Vidanın yanında tırnak çentiği. Dış yüzde "4 x AA 1,5 V".
- **Ayaklar** kapağın dışına alındı (4 ayak: önde, iki yanda, arkada). Taban vidası 230° → 210° (kutunun dışı).
- **ESP32-S3** kutunun tavanının üstüne çıktı (bileşen yüzü z 24,3) ve 180° döndü: J1 (kullanılan bütün uçlar) öne,
  USB-C sağda. Jumper payı 14 + 3 mm (üstte okuyucunun rayı).
- **MAX98357A** ve **5 V düzenleyici** kutunun tavanında (sağ ön / sol ön). **Anahtar** z 17 → 28 (kutunun üstü).

## İlk baskıdan sonra yapılan düzeltmeler (20 Ekim 2026)

- **LED halka** iç Ø55 / dış Ø70 (ürün sahibinin ölçüsü): figür çukurunun dış duvarı Ø54,9 (halkaya sıkı geçer ve
  halkayı ortalar), çukurun içi Ø52,5, ışık oyuğu r 28–34,6, çukur duvarında 36 ışık penceresi. Halka/NFC tutucusu
  halkayla birlikte büyüdü (Ø75), rayları çukurun zemininin altında kalacak biçimde kısaltıldı.
- **Figür tabanı Ø52** (kapak Ø30 dişli, içinde Ø25 etiket).
- **USB-C:** kabuktaki kızaklar KALDIRILDI (ters baskıda havada kaldıkları için destekle dolup kapanıyordu) ve içteki
  geniş inceltme cebi kaldırıldı (duvarı 1,1 mm'ye indirip dış yüzde pürüz yapıyordu). Şimdi: USB-C deliği dişiden
  0,8 mm büyük; kartın ön kenarı duvarın içindeki ince düz banda dayanır (bantta duvar en az 1,4 mm); dışta fiş gövdesi
  için 12,8 x 7,2 mm cep (dişinin ön yüzüne kadar iner, fiş sonuna kadar oturur). Kart tabandaki kaideye oturur,
  arkadaki esnek dayanağın tırnağı kartın arka kenarına üstten biner. Montaj: kartı kabuğa içeriden tak (USB-C deliğe),
  sonra tabanı kapat.
- **Hoparlör:** mıknatıs eyerinin aynısından bir tane daha, içeride; ön beşik, eyer ve ikinci eyer arası eşit (15,5 mm).
- Kabuk **ters** (üst yüz tablada) basılmalı; dik basılırsa USB-C deliğinin üstünde köprü sarkması olur.
