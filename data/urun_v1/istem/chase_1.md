# Yazar görevi: Chase, parti 1

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 9 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v1/aday/chase_1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Chase | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v1/aday/chase_1.txt`
  İşaretlenen hikâyede EN ÇOK 1 yerel düzeltme yap ve kontrolü bir kez daha koş. Yine geçmeyen hikâyenin bütün
  bloğunu (başlık dahil) dosyadan sil; zorlama. Geçen hikâyeye dokunma (her değişiklik bir yama sayılır).

## Yazım kılavuzu

# Ürün hikayesi yazım kılavuzu

Bu hikayeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini eğitecek. Her hikaye bir tohumdan yazılır.
Yanında figürün kaynaklı kartı (data/urun_kartlari.json) ve sade sözlük (data/sade_sozluk_sik.txt) vardır.
Kart kapalı dünyadır: kartta yazmayan hiçbir şey hikayeye girmez.

1. **Uzunluk.** Gövde 70-100 kelime. Her cümle en çok 12 kelime, çoğu 5-9 kelime. Tek paragraf.
2. **Tek sahne, tek zaman.** Hikaye tohumdaki yerde başlar ve biter. 'ertesi', '... gün/hafta sonra',
   'akşama/sabaha kadar', 'bütün gün', 'o gece', 'günlerce', 'her sabah' gibi zaman atlamaları yok.
   Bekleme sahnenin içinde olur.
3. **Tek sorun.** Sorun ilk 3 cümlede sebebiyle birlikte söylenir ('Top çalıya takıldı.'). Sorunu figür kendisi
   1-2 adımda çözer; yardım istemek de figürün çözümüdür. Yan karakter en fazla yardım eder.
4. **Figür görünür ve etkin.** Figürün adı ilk 2 cümlede ve sonda geçer. Hikaye onun gözünden anlatılır.
5. **Yan karakter ve kapalı dünya.** Yalnız başlıktaki Yan alanında yazan karakterler bulunur; kartta yazan kısa
   adla ve karttaki ilişkiyle (Niloya'nın ağabeyi Murat'tır; Mete, Murat'ın arkadaşıdır). Başka ad, canlı, rol ya
   da aile üyesi yok; bebek, robot, dev, biri gibi kelimeler karakter olamaz, yalnız cansız anlamda geçer ('oyuncak
   robot', 'bir sürü yaprak'). Arka plandaki çoğul canlılar ('kuşlar') konuşmaz ve olaya katılmaz. Kartta 'konuşmaz'
   yazan karakter konuşmaz. Kartta olmayan ev, eşya ya da yetenek uydurulmaz. Yer, kartın o yer için verdiği
   tarife uyar.
6. **Figür özelliği.** Yalnız tohumdaki özellik kullanılır: bir kez, olayda işe yarar biçimde ve kartın 'güvenli
   özellik kullanımı' satırına uygun. Özellikler sıralanmaz, betimlenmez. Slogan ve kalıp replik yok.
7. **Sade kelime.** Kelimeler sade_sozluk_sik.txt'den seçilir; en çok 2 liste dışı kelime. Deyim, mecaz, soyut
   kavram ve şapkalı harf yok; 'hâlâ' yerine 'yine' ya da 'daha' yazılır. Tohumdaki isim, fiil ve sıfat geçer;
   biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik kayda yazılır.
8. **Dil.** Anlatım -dı'lı geçmiş zamanda ('yürüdü', 'bakıyordu', 'takılmıştı'). Her replikte konuşan bellidir
   ('dedi Niloya'); hitaptan önce virgül konur ('Sıra sende, Niloya'). Kimse kendi kendine konuşmaz ya da kendine adıyla seslenmez. Plan satırları da aynı dil ve
   yazım kurallarına uyar; cihazda model planı kendisi yazıyor.
9. **Son.** Hikaye tohumdaki kapanış türüyle biter: eylem, replik, görüntü, ders ya da duygu. Son güvenlidir ve
   sorun çözülmüştür. Son cümlede 'çünkü' ile açıklama ve 'gülümsedi/sevindi' kalıbı yalnız kapanış türü 'duygu'
   ise kullanılır. Ders, olaydan çıkan tek ve somut bir cümledir. Korku, yaralanma, hastalık ve taklit edilince
   tehlikeli davranış (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç) yok.
10. **Biçim ve öz-denetim.** Her hikaye dört parçadır:
    `### Figür | yer | yan` / `@plan: sorun | çözüm` / `@tohum: id` / gövde.
    Başlık tohumdaki figür, yer ve yan alanlarının birebir kopyasıdır. Planda sorun ve çözüm her biri 3-9 küçük
    harfli kelimedir, özel ad yoktur. Yazdıktan sonra her hikaye HAKEM_M.md, HAKEM_D.md ve HAKEM_K.md madde
    listelerine karşı cümle cümle okunur (çelişki, sebepsiz nesne, ikinci sorun, özne-fiil uyumu, tekrar, kart
    dışı eşya, taklit edilince tehlikeli davranış) ve kusur bulunursa kontrolden önce düzeltilir. Sonra
    `veri_hakem.py kontrol` koşulur. İşaretli hikayede en çok
    1 yerel düzeltme yapılır; yine geçmezse hikaye boş bırakılır, zorlanmaz.

**Kural bütçesi.** Bu kılavuz tek sayfa ve 10 maddedir. Yeni bir kusur türü kılavuza değil koda ya da hakem
listesine eklenir. Kılavuza yeni madde ancak bir madde çıkarılarak girer. Kötü örnek konmaz.

**Tohum alanları (tanım, kural değil).** Açılış türü: figür adı / zaman ('Bir sabah') / yer / ses-hava;
'<Ad> adında ... yaşardı' bir açılış türü değildir. Kapanış türü: *eylem* (figür son bir şey yapar),
*replik* (son cümle bir konuşmadır), *görüntü* (sahneden son bir resim), *ders* (olaydan çıkan tek somut cümle),
*duygu* (figürün hissi). Diyalog 'yok' ise hikayede replik yoktur. Temalar tek sahneye uyarlanmıştır:
kaybolan eşya; yeni arkadaş (ilk adımı figür atar); paylaşmak; yardım istemek (çözüm figürün yardım
istemesidir); yeni bir şeyi denemek; sahne içinde beklemek (sıra, fırındaki kek, yağmurun dinmesi); özür
dilemek; sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil); bir şey yapmak;
yağmur ya da kar günü; aynı sahnede hazırlanıp verilen sürpriz; sırayla oynamak.

**İyi örnekler** (kullanıcı yetkisiyle seçildi; farklı figür ve farklı kapanış türü; ikisi de `veri_hakem.py kontrol`dan
geçer):

Tohum: deniz, yan balık, özellik kabuk, kelimeler taş/toplamak/renkli, tema yağmur, açılış yer, kapanış görüntü.

```
### Tosbi | deniz | balık
@plan: yağmur başladı ve başı ıslandı | başını kabuğuna çekip yağmurun dinmesini bekledi
@tohum: tosbi-9001
Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden yağmur başladı ve Tosbi'nin başı ıslandı. Tosbi başını ve ayaklarını kabuğuna çekti. Sudan küçük bir balık başını çıkardı. "Tosbi, neredesin?" diye sordu balık. "Buradayım, içerisi çok kuru," dedi Tosbi. Balık gülümsedi ve suya geri döndü. Tosbi içeride sessizce bekledi. Bir süre sonra yağmur dindi ve bulutların arasından güneş çıktı. Tosbi başını yavaşça dışarı çıkardı. Balık da yeniden sudan baktı. Kumdaki renkli taşlar güneşte parlıyordu.
```

Tohum: park, yan Murat, özellik soru, kelimeler uçurtma/bağlamak/uzun, tema yardım istemek, açılış figür adı,
kapanış replik.

```
### Niloya | park | Murat
@plan: uçurtma ağaçların üstüne çıkamadı çünkü ipi kısaydı | ağabeyinden ip isteyip iki ipi bağladı
@tohum: niloya-9001
Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu. "Bak Murat, uçurtma ağaçlardan yüksek!" dedi Niloya.
```

## Kart: Chase (kaynaklı, kapalı dünya)

- Ad: Chase (okunuş: çeys; kesme eki okunuşa uyar)
- Kimlik: Chase, bir kurtarma ekibinin polis köpeği olan bir çoban köpeği yavrusudur.
- Tür: köpek
- Güvenli özellik kullanımı: Chase kaybolanı bulur ve küçük sorunları çözer; kimseyi kovalamaz, yakalamaz ya da cezalandırmaz. Kimse yabancıyla bir yere gitmez. 'Tehlike' yerine 'bir sorun var' denir. Kediler ve tüyler yüzünden hapşırması hikayeye konmaz.
- Özellikler:
  - koku: Burnuyla koku alarak çözüm bulur. (örnek biçimler: koku, kokladı, kokusunu)
  - kural: Ekibin polis köpeğidir; kurallara uyar. (örnek biçimler: kural, kurallara)
  - şapka: Mavi bir şapka takar. (örnek biçimler: şapka, şapkası)
- Yerler:
  - dağ: Kasabanın yakınındaki karlı dağ.
  - deniz: Kasabanın kıyısı; kumsal ve iskele.
  - orman: Kasabanın yakınında, ağaçların arasındaki kamp yeri.
  - park: Kasabadaki çocuk oyun parkı.
  - ev: Ekibin yüksek kulesi ve köpeklerin kulübeleri.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Ryder: On yaşında bir çocuk; ekibin başıdır. Köpeklere bakar ve işe uygun köpeği o seçer. Tür: oğlan; konuşur. Yüzey biçimleri: Ryder
  - Marshall: Ekibin itfaiyeci köpeği; altı yaşında, benekli bir köpek. Biraz sakardır ama cesur ve yardımseverdir. Tür: köpek; konuşur. Yüzey biçimleri: Marshall
  - Skye: Helikopter kullanan pilot köpek; ekibin en küçüğü, küçük hayvanları çok sever. Tür: köpek; konuşur. Yüzey biçimleri: Skye
  - Rubble: İnşaat köpeği; güçlü, şakacıdır ve yemek yemeyi sever. Tür: köpek; konuşur. Yüzey biçimleri: Rubble
- Dünya kuralları:
  - Chase slogan söylemez; kimse kendi adıyla konuşmaz.
  - Ryder bir çocuktur, köpek değildir.
  - Görevler karışmaz: Chase polis, Marshall itfaiyeci, Skye pilot, Rubble inşaat köpeğidir.
- Yasak adlar: Rocky, Zuma, Everest, Tracker, Goodway, Chickaletta, Turbot, Humdinger, Robo-Dog, Jake, Liberty, Rex
- Yasak: Araçların kovalamacası, sirenle hız ve kötü karakterler hikayeye girmez.
- İzinli dünya kelimeleri: polis, koku, şapka, itfaiye, helikopter, kule, kulübe, iskele

## Tohumlar

### Chase | park | Skye
@tohum: chase-0001
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yeni bir şeyi denemek
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çeşme', fiil 'toplamak', sıfat 'karmakarışık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle bir konuşmadır)

### Chase | park | -
@tohum: chase-0002
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bulaşık', fiil 'barışmak', sıfat 'gururlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün hissi)

### Chase | deniz | -
@tohum: chase-0003
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'madalya', fiil 'büyümek', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaydan çıkan tek ve somut bir cümle)

### Chase | deniz | -
@tohum: chase-0004
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: bir şey yapmak
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'ay', fiil 'biriktirmek', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaydan çıkan tek ve somut bir cümle)

### Chase | deniz | Marshall
@tohum: chase-0005
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: sırayla oynamak
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bisiklet', fiil 'şaşırmak', sıfat 'güçlü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle bir konuşmadır)

### Chase | ev | -
@tohum: chase-0006
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: kaybolan eşya
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'bisküvi', fiil 'kaydetmek', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: goruntu (sahneden son bir resim)

### Chase | orman | Ryder
@tohum: chase-0007
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kostüm', fiil 'tamamlamak', sıfat 'elmalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle bir konuşmadır)

### Chase | deniz | Rubble
@tohum: chase-0008
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'tabure', fiil 'yardımlaşmak', sıfat 'iyi'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: eylem (figür son bir şey yapar)

### Chase | dağ | -
@tohum: chase-0009
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: sahne içinde beklemek (sıra, fırındaki kek, yağmurun dinmesi)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'pizza', fiil 'yaklaştırmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaydan çıkan tek ve somut bir cümle)
