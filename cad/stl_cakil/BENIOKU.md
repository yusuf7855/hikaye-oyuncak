# Çakıl stand — baskıya hazır STL'ler

Hangi NFC okuyucuyu kullanacaksan o klasörü bas: `rc522/` ya da `pn5180/`. İki klasör yalnız `3_halka_nfc_tutucu.stl`'de
farklı (okuyucunun rayları); öteki parçalar aynı. Her parça **baskı yönünde, tablanın ortasında** kaydedildi: slicer'a
at, döndürme. Birim mm.

Yeniden üretmek: `python cad/cakil_ic.py --stl --onizle` (önce çarpışma denetimi; "0 sorun" yazmalı).
Ölçülerin bir kısmı TAHMİN (pil yatağı, hoparlör derinliği, KCD11, PN5180, MAX98357A); parça elinde olunca ölç,
`cad/cakil_ic.py` PARCA sözlüğünde düzelt, yeniden üret. TP4056 ve ESP32-S3 ölçüleri ürün sahibinin modellerinden.

| Dosya | Adet | Baskı yönü | Malzeme / ayar |
|---|---|---|---|
| `0_tum_stand_*_montajli.stl` | — | BASILMAZ: tüm stand monte hâlde (bakmak için) | |
| `0_tum_stand_*_elektronikli_GORSEL.stl` | — | BASILMAZ: elektronik parçalar dahil (ESP32 ve TP4056 gerçek model, ötekiler kutu) | |
| `1_kabuk.stl` | 1 | ters: üst yüz (figür çukuru) tablada | (renkli için `renkli_bambu/` bölümüne bak) **beyaz** PLA/PETG (LED ışığı figür zemininden ve çukur duvarındaki yarıklardan geçer). 0,2 mm katman, 3 duvar, %15 doluluk. **Destek: ağaç (tree), yalnız iç kısım** (vida kolonları, TP4056 kızakları, ses yakası). "eco ai" logosu için logonun başladığı katmanda filament değiştirilebilir |
| `2_taban_plakasi.stl` | 1 | düz alt yüz tablada | PLA/PETG, destek GEREKMEZ (TP4056 üstündeki 23 mm köprü dahil) |
| `3_halka_nfc_tutucu.stl` | 1 | ters: halkanın bastığı düz yüz tablada, raylar yukarı | PLA, destek gerekmez |
| `4_figur_taban.stl` + `4b_figur_kapagi.stl` | figür başına 1 + 1 | taban ters (düz üst yüz tablada), kapak alt yüzü tablada | figür adı ve numarası kazılı kapaklar `figurler/` klasöründe (figür başına tek dosya) |
| `5_ayar_karti.stl` | 1 | dik, topuz yukarı | + 1 kapak (`figurler/200_ayar_karti.stl`) |

## Ek malzeme

- M3 x 8 HAVŞA BAŞLI vida (4) + M3 ısıl gömme somun (4, Ø4,6 x 5,7; delik Ø4,0 x 6,5): taban plakası → kabuk (somunlar kabuğun 4 kolonuna havyayla gömülür)
- M2,5 x 6 sac vidası (4): halka/NFC tutucu → kabuğun 4 direği (tutucuda 3,5 mm vida tablası, direkte 3 mm kılavuz delik)
- Kablo bağı 2,5 mm (3): pil yatağı (2), hoparlör (1)
- Silikon ayak Ø10 x 1 mm (3–6)
- NTAG213 **Ø25** yuvarlak yapışkan NFC etiket (13): her figürün vidalı kapağının içine (12 figür + ayar kartı)
- Dişi-dişi jumper kablolar (ESP32 ters yatar, pinler yukarıda)

## Montaj sırası

Üst modül (kabuk ters dururken):
1. Isıl gömme somunları 4 kolona göm.
2. NeoPixel halkayı LED'ler tavandaki ışık oyuğuna girecek biçimde koy (kablosu arkada).
3. NFC okuyucuyu tutucunun raylarına kaydır; tutucuyu halkanın üstüne koy, 4 M2,5 vidayla direklere vidala.
4. KCD11 anahtarı sol yandaki deliğe dışarıdan bastır (tırnaklar içte oturur).
5. TP4056'yı içeriden arka duvardaki kızaklara kaydır; USB-C dışarıdaki deliğe girer.

Alt modül (taban plakası):
1. Ayakları yapıştır; pil yatağını cebine koy, 2 kablo bağıyla sık.
2. Hoparlörü öndeki beşiğe oturt, kablo bağıyla sık; MAX98357A'yı sağ öndeki cebine koy.
3. ESP32-S3'ü TERS tut (bileşenler aşağı): USB-C ucunu iki köşe kancasının altına kaydır, anten ucunu bastır, tırnak oturur.
4. Jumper'ları yukarıdan pinlere tak, kabloları bağla (lehim / jumper).

Birleştir: kabuğu alt modülün üstüne indir (TP4056 kartı tabandaki kaidenin üstüne, arka dayanağın önüne gelir),
alttan 4 M3 vidayla sık. Kod yüklemek için kabuk açılır (ESP32'nin USB-C uçları sol tarafta açıkta).

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
| `1_kabuk.3mf` | beyaz gövde, turkuaz "eco ai" ve çukur zemini, sarı çukur kenarı + güneş halkası, 6 mor yıldız | LED'lerin üstündeki ışık halkası beyaz kalmalı. Destek: ağaç (tree), yalnız iç kısım. Logo dikey duvarda: logo boyunca her katmanda renk değişir (en çok atık burada) |
| `2_taban_plakasi.3mf` | beyaz plaka; alt yüzde turkuaz "eco ai", sarı halka, 4 mor yıldız | renkler ilk 3 katmanda, alttan okunur; destek yok |
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

## İlk baskıdan sonra yapılan düzeltmeler (20 Ekim 2026)

- **LED halka** iç Ø55 / dış Ø70 (ürün sahibinin ölçüsü): figür çukurunun dış duvarı Ø54,9 (halkaya sıkı geçer ve
  halkayı ortalar), çukurun içi Ø52,5, ışık oyuğu r 28–34,6, çukur duvarında 36 ışık penceresi. Halka/NFC tutucusu
  halkayla birlikte büyüdü (Ø75), rayları çukurun zemininin altında kalacak biçimde kısaltıldı.
- **Figür tabanı Ø52** (kapak Ø30 dişli, içinde Ø25 etiket).
- **USB-C:** kızak kanalı kartın iki yanında 0,4 mm, dudaklar arası kart + 0,8 mm (ilk baskıda dar geldi); delik
  0,6 mm geniş; dışta fiş gövdesi için 12,8 x 7,2 mm yuvarlak köşeli cep (fiş dişinin ön yüzüne kadar oturur).
- **Hoparlör:** mıknatıs eyerinin aynısından bir tane daha, içeride; ön beşik, eyer ve ikinci eyer arası eşit (15,5 mm).
- Kabuk **ters** (üst yüz tablada) basılmalı; dik basılırsa USB-C deliğinin üstünde köprü sarkması olur.
