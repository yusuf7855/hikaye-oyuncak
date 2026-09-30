# Editör görevi (onarım): Keloğlan, onarım partisi 49

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar49.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <aynı tohum kimliği>
@degisim: <eski> -> <yeni>      (yalnız özgün blokta varsa ve tutuyorsan)
@onarim: <özgün bloğun sha1'i; her hikâyede verilir>
<gövde>
```

- **Yalnız bulguların gösterdiği yeri düzelt** ve tutarlılık için değişmesi gerekeni (ör. çözüm değiştiyse plan
  satırı, silinen nesnenin sonraki anılışı). Öteki cümleler olduğu gibi kalır.
- **Tohumu ve hikâyeyi koru:** figür, yer, yan, tema, açılış, kapanış türü, diyalog, özellik ve tohum kelimeleri
  (isim, fiil, sıfat) aynı kalır; sorun ve çözüm aynı kalır. Tohum kelimelerinden en çok biri değişebilir ve
  `@degisim` satırına yazılır (özgün bloktaki değişim sayılır).
- Gövde 70-100 kelime, her cümle en çok 12 kelime, tek paragraf.
- Bir bulgu sana yanlış görünse bile o cümleyi daha basit ve açık biçimde yeniden söyle: hakem orada takıldı,
  okuyan çocuk da takılabilir. İşaretlenen kelimeyi ya da yapıyı tekrarlama.
- Görevi **YENİDEN YAZ** olan hikâyede (M3: çekirdek önemsiz ya da saçma) hikâyeyi aynı tohumdan baştan yaz:
  çocuğun önemseyeceği, sebebi ilk 3 cümlede söylenen bir sorun ve figürün 1-2 adımlık çözümü; başlık, tohum
  kimliği ve `@onarim` satırı yine verilir.
- Onarılmış metin özgünden farklı olmalıdır (aynı metin aynı kayıttır ve reddedilir).
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar49.txt --ad urun_v2`
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
3. **Tek sorun, açık hedef.** Figürün açık ve küçük bir hedefi vardır (uçurtmayı yükseltmek, sesin nereden
   geldiğini bulmak) ve hikaye bu hedefe ulaşınca tatmin edici biçimde biter; 'hiçbir şey olmayan' hikaye yok.
   Hedef çocuğun önemseyeceği bir şeydir (bir arkadaşı sevindirmek, kaybolan oyuncağı bulmak, bozulan oyunu
   kurtarmak); rüzgarın yaprakları dağıtması gibi önemsiz ya da 'kurdele hamurun içine düştü' gibi saçma olay yok.
   Sorun ilk 3 cümlede sebebiyle birlikte söylenir ('Top çalıya takıldı.'). Sorun çoğunlukla dışarıdan gelir
   (hava, takılan top, merak uyandıran bir ses); figürün kendi hatası yalnız özür temasında sorundur. Sorunu figür
   kendisi 1-2 adımda çözer; yardım istemek de figürün çözümüdür. Yan karakter en fazla yardım eder.
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
   kavram ve şapkalı harf yok ('keşfetmek' değil 'bulmak'; 'top gibi' benzetmesi serbest); 'hâlâ' yerine 'yine'
   ya da 'daha' yazılır. Tohumdaki isim, fiil ve sıfat geçer;
   biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik kayda yazılır.
8. **Dil.** Anlatım -dı'lı geçmiş zamanda ('yürüdü', 'bakıyordu', 'takılmıştı'). Her replikte konuşan bellidir
   ('dedi Niloya'); hitaptan önce virgül konur ('Sıra sende, Niloya'). Kimse kendi kendine konuşmaz ya da kendine adıyla seslenmez. Plan satırları da aynı dil ve
   yazım kurallarına uyar; cihazda model planı kendisi yazıyor.
9. **Son.** Son 1-2 cümle hikayeyi kapatır: sorunun çözüldüğü görünür ve son cümle sıcak, doyurucu bir kapanış
   verir ('İkisi oyunlarına mutlu mutlu devam etti.'). Hikaye hiçbir zaman çıplak bir eylemle ya da durgun bir
   resimle bitmez; okur 'sonra ne oldu?' diye sormaz. Son, tohumdaki kapanış türüyle yazılır: duygu, sonuç, replik ya
   da ders; 'çünkü' ile açıklama yalnız 'duygu' türünde kullanılır. Son güvenlidir. Korku, yaralanma, hastalık ve
   taklit edilince tehlikeli davranış (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç) yok.
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
'<Ad> adında ... yaşardı' bir açılış türü değildir. Kapanış türü: *duygu* (figürün ya da karakterlerin yaşanan
olaya bağlı hissi; 'çünkü' kullanılabilir: 'Tosbi çok sevindi, çünkü sesin nereden geldiğini bulmuştu.'),
*sonuç* (ardından mutlulukla ne yaptıkları ya da olayın sonucu: 'oyunlarına mutlu mutlu devam ettiler'),
*replik* (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle gelmez), *ders* (olaya
bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir: 'Niloya bundan sonra zorda kalınca büyüklerinden yardım
istedi.'). Diyalog 'yok' ise hikayede replik yoktur. Temalar tek sahneye uyarlanmıştır: merak edip bulmak (bir
ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar); eğlenceli ya da komik bir oyun ve oyunda küçük bir
aksilik; figür başkasına yardım eder (hasta ya da yaralı hayvan değil); aynı sahnede küçük bir kutlama ya da
sürpriz hazırlamak; doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef; hayali
oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef; kaybolan eşya; yeni bir şeyi denemek; bir şey
yapmak; yağmur ya da kar günü; sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil);
yeni arkadaş (ilk adımı figür atar); ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek;
yalnız yağmurun dinmesi değil); paylaşmak; yardım istemek (çözüm figürün yardım istemesidir); özür dilemek (figürün
kendi hatası yalnız bu temada olur); sırayla oynamak.

**İyi örnekler** (kullanıcı yetkisiyle seçildi; farklı figür ve farklı kapanış türü; ikisi de `veri_hakem.py kontrol`dan
geçer):

Tohum: deniz, yan balık, özellik sabır, kelimeler taş/toplamak/renkli, tema merak edip bulmak, açılış yer,
kapanış duygu.

```
### Tosbi | deniz | balık
@plan: sığ sudan bilinmeyen bir ses geldi | sabırla bekledi ve sesi yapan balığı gördü
@tohum: tosbi-9001
Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden sığ sudan garip bir ses geldi. Tosbi bu sesi çok merak etti. Suyun kenarına yavaşça yürüdü ve baktı. Ama suda hiçbir şey göremedi. Tosbi acele etmedi ve sabırla bekledi. Sonunda küçük bir balık sudan zıpladı ve suya geri düştü. "Bu sesi sen mi yapıyorsun?" diye sordu Tosbi. "Evet, bu benim zıplama oyunum," dedi balık. Balık üç kez daha zıpladı ve Tosbi hepsini saydı. Tosbi çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

Tohum: park, yan Murat, özellik soru, kelimeler uçurtma/bağlamak/uzun, tema yardım istemek, açılış figür adı,
kapanış replik.

```
### Niloya | park | Murat
@plan: uçurtma ağaçların üstüne çıkamadı çünkü ipi kısaydı | ağabeyinden ip isteyip iki ipi bağladı
@tohum: niloya-9001
Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu ve güldü. "Teşekkürler, Murat, uçurtmamız artık en yüksekte!" dedi Niloya.
```

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0095
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'süt', fiil 'kapamak', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: gözü kapalıyken kabarık şeyin ne olduğunu bilemedi | yavaşça dokundu ve ortasındaki sert sapı buldu
@tohum: keloglan-0095
@degisim: süt -> tüy
Ormanda Bilgecan Dede ile Keloğlan bir oyun oynuyordu. Keloğlan gözlerini kapadı ve dede onun avucuna bir şey koydu. Keloğlan bu kabarık şeyin ne olduğunu bilemedi, çünkü çok yumuşaktı. "Bu pamuk mu?" diye sordu Keloğlan. Bilgecan Dede güldü. "Hayır, bir daha dokun," dedi Bilgecan Dede. Keloğlan parmaklarını yavaşça gezdirdi. Ortasında ince ve sert bir sap vardı. "Bu bir tüy!" dedi Keloğlan. Keloğlan gözlerini açtı ve avucundaki beyaz tüye baktı. Böylece tüylerin ortasında sert bir sap olduğunu öğrendi. Bilgecan Dede onu alkışladı. Keloğlan çok sevindi, çünkü tüyü kendi başına bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Böylece tüylerin ortasında sert bir sap olduğunu öğrendi"
   - Cümle 11: «Böylece tüylerin ortasında sert bir sap olduğunu öğrendi.»
   - Açıklama: Keloğlan tüyü zaten sert sapından tanımıştı, sonra bunu yeni öğrenmiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0095` birebir aynı, `@degisim: süt -> tüy` (tutuyorsan), ardından `@onarim: 011e35bd25d1c5e0e4af15a4cf845af41542307c`, sonra gövde.

### Hikâye 2: tohum keloglan-0109 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0109
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'saksı', fiil 'seçmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: cevizler saksının sert kenarına çarpıp dışarı düşüyordu | saksıyı yere yatırdı ve cevizleri yerden yuvarladı
@tohum: keloglan-0109
Keloğlan evde eğlenceli bir oyun oynuyordu. En büyük boş saksıyı seçti ve duvarın dibine koydu. Ama attığı cevizler saksının sert kenarına çarpıp dışarı düşüyordu. Keloğlan yere bir ip koymuştu ve cevizleri ipin arkasından atıyordu. Saksıya yaklaşsa cevizler kolayca girerdi. Keloğlan yine de dürüst davrandı, ipin arkasında kaldı ve biraz düşündü. Sonra saksıyı yere yan yatırdı. Bu sefer cevizi atmadı, yerden yavaşça yuvarladı. Ceviz yerde ilerledi ve içeri girdi. Keloğlan öteki cevizleri de tek tek yuvarladı. Hepsi saksının içinde toplandı. Keloğlan çok sevindi, çünkü bütün cevizleri ipin arkasından saksıya sokmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Saksıya yaklaşsa cevizler kolayca"
   - Cümle 5: «Saksıya yaklaşsa cevizler kolayca girerdi.»
   - Açıklama: Yaklaşsa fiilinin öznesi eksik; cümle cevizler saksıya yaklaşsa diye okunuyor, 'Keloğlan saksıya yaklaşsa' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yine de dürüst davrandı"
   - Cümle 6: «Keloğlan yine de dürüst davrandı, ipin arkasında kaldı ve biraz düşündü.»
   - Açıklama: 'Dürüst davranmak' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0109` birebir aynı, ardından `@onarim: 55bc485be143e357c06e5f9849cdf82b47abec6e`, sonra gövde.

### Hikâye 3: tohum keloglan-0111 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0111
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kaşık', fiil 'hazırlanmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda nereden geldiği bilinmeyen bir ses vardı | aramayı bırakmadı ve sesin kendi çantasından geldiğini buldu
@tohum: keloglan-0111
Hafif bir rüzgar esiyordu. Keloğlan çantasını alçak bir dala astı ve yemeğe hazırlandı. Birden yakından ince bir ses geldi. Keloğlan bu sesin nereden geldiğini çok merak etti. Büyük bir kayanın arkasına baktı ama hiçbir şey göremedi. Biraz mutsuz oldu. Ama Keloğlan dürüsttü ve sesi duymamış gibi yapmadı. Durdu ve sesi dikkatle dinledi. Sonunda sesin kendi çantasından geldiğini buldu. Rüzgar çantayı sallıyordu. İçindeki kaşık da bardağa çarpıp ses çıkarıyordu. Keloğlan güldü ve kaşığı çıkardı. Ses hemen kesildi. Keloğlan bundan sonra bir sesi merak edince onu bulana kadar aradı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüsttü ve sesi duymamış gibi yapmadı"
   - Cümle 7: «Ama Keloğlan dürüsttü ve sesi duymamış gibi yapmadı.»
   - Açıklama: 'Dürüst' kelimesi sesi aramaya zorlama biçimde bağlanmış, anlamına uygun kullanılmamış.
   - Açıklama: 'Dürüst' kelimesi sesi aramaya devam etmekle ilgili değil; yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüsttü ve sesi duymamış gibi yapmadı"
   - Cümle 7: «Ama Keloğlan dürüsttü ve sesi duymamış gibi yapmadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği karttaki anlamıyla değil, sesi duymazdan gelmemek gibi zorlama bir biçimde kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüsttü ve sesi duymamış gibi yapmadı"
   - Cümle 7: «Ama Keloğlan dürüsttü ve sesi duymamış gibi yapmadı.»
   - Açıklama: Dürüstlük sesi aramakla ilgisiz; cümle olaydan çıkmıyor, işlevsiz bir ayrıntı.
   - Açıklama: Dürüstlük sesi aramakla ilgisiz; cümle olaydan çıkmıyor ve sebepsiz bir bağ kuruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0111` birebir aynı, ardından `@onarim: 65ae7f53997ac262e2cacb6a5e6db60146220e3a`, sonra gövde.

### Hikâye 4: tohum keloglan-0114 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0114
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'taç', fiil 'serinletmek', sıfat 'bulutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: sıcaktan tacın çiçekleri aşağı eğildi | arkadaşına sordu ve tacı soğuk suya koydu
@tohum: keloglan-0114
Hava bulutluydu ama çok sıcaktı. Keloğlan evde Balkız için çiçeklerden bir taç yapmıştı. Ama sıcaktan tacın çiçekleri aşağı eğildi. O sırada Balkız kapıdan içeri girdi ve tacı gördü. Keloğlan dürüst davrandı ve tacı ona gösterdi. "Senin için yaptım, sıcakta bozuldu, ne yapalım?" diye sordu Keloğlan. "Çiçekler soğuk suda kalkar," dedi Balkız. Keloğlan bir kova su getirdi. Tacı suya koydu ve çiçekleri serinletti. Biraz sonra çiçekler yeniden yukarı kalktı. Keloğlan tacı Balkız'a verdi ve Balkız onu başına taktı. "Çok güzel bir taç, teşekkür ederim, Keloğlan!" dedi Balkız.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı ve tacı ona gösterdi"
   - Cümle 5: «Keloğlan dürüst davrandı ve tacı ona gösterdi.»
   - Açıklama: Balkız tacı zaten görmüştü; 'dürüst davrandı' burada anlamına uygun kullanılmamış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çiçekler soğuk suda kalkar"
   - Cümle 7: «"Çiçekler soğuk suda kalkar," dedi Balkız.»
   - Açıklama: Eğilen çiçekler için 'kalkmak' fiili öznesine uygun değil; 'dikleşir' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0114` birebir aynı, ardından `@onarim: 8c7a398e699e0b151ffe8cf119b9e71b172b3e42`, sonra gövde.

### Hikâye 5: tohum keloglan-0116 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0116
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kereviz', fiil 'küçültmek', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: anası acıkmıştı ve sert kereviz ikiye kırılmadı | kerevizi taşa vurdu ve ikiye ayırdı
@tohum: keloglan-0116
@degisim: küçültmek -> bölmek
Keloğlan anasıyla ormanda ferah bir yerde, büyük ve düz bir taşa oturdu. Anası çok acıkmıştı ve çantada yalnız bir kereviz vardı. Keloğlan onu paylaşmak istedi, ama kereviz çok sertti. Kerevizi bölmek için iki eliyle bükmeye çalıştı. Kereviz kırılmadı ve sakar Keloğlan onu elinden düşürdü. Kereviz taşa çarptı ve biraz çatladı. Keloğlan bunu gördü ve kerevizi taşın kenarına bir kez vurdu. Kereviz hemen ikiye ayrıldı. "Anneciğim, bu parça senin, bu da benim," dedi Keloğlan. Anası parçasını aldı ve Keloğlan'ı öptü. İkisi kerevizi mutlu mutlu yedi. "Teşekkürler, Keloğlan, birlikte yemek çok güzel!" dedi anası.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormanda ferah bir yerde"
   - Cümle 1: «Keloğlan anasıyla ormanda ferah bir yerde, büyük ve düz bir taşa oturdu.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Ferah' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kereviz taşa çarptı ve biraz çatladı"
   - Cümle 6: «Kereviz taşa çarptı ve biraz çatladı.»
   - Açıklama: Çözümün yolu Keloğlan'ın kerevizi kazara düşürmesiyle şans eseri açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0116` birebir aynı, `@degisim: küçültmek -> bölmek` (tutuyorsan), ardından `@onarim: a0c84a09943baabdc2cccd24bce4266fd637a450`, sonra gövde.

### Hikâye 6: tohum keloglan-0120 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0120
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ip', fiil 'kırpmak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: gürültülü bir ses geldi ve uçurtma yukarı çıkamadı | uçurtmayı indirdi ve fazla ipi sardı
@tohum: keloglan-0120
@degisim: kırpmak -> sarmak
Bir sabah Keloğlan ile Bilgecan Dede tepede uçurtma uçuruyordu. Birden yukarıdan gürültülü bir ses geldi. Uçurtma hep sallanıyordu ve yukarı çıkamıyordu. "Bu ses ne, Keloğlan?" diye sordu Dede. Keloğlan dürüst davrandı ve "Bilmiyorum, Dede, ama bulacağım," dedi. Keloğlan uçurtmayı yavaşça indirdi ve her yerine dikkatle baktı. Uçurtmanın altında uzun bir ip parçası vardı. Rüzgar esince bu ip uçurtmaya çarpıyor ve ses çıkarıyordu. Keloğlan ipin fazla kalan ucunu uçurtmaya sıkıca sardı. Sonra uçurtmayı yeniden uçurdu. Uçurtma bu kez sessizce yükseldi. Keloğlan çok sevindi, çünkü sesin nereden geldiğini kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: ""Bu ses ne, Keloğlan?" diye sordu Dede"
   - Cümle 4: «"Bu ses ne, Keloğlan?" diye sordu Dede.»
   - Açıklama: Kartın ilişki alanında Bilgecan Dede köyün en bilgesi ve çocuklara bilmediklerini öğreten kişidir; burada bilmeyip çocuğa soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0120` birebir aynı, `@degisim: kırpmak -> sarmak` (tutuyorsan), ardından `@onarim: 614d498c469df30798629c810289b589cc15103e`, sonra gövde.

### Hikâye 7: tohum keloglan-0121 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0121
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'etiket', fiil 'dinlenmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar sert sepetten hep dışarı zıplıyordu | sepetin içine yumuşak yosun koydu
@tohum: keloglan-0121
@degisim: etiket -> kozalak
Keloğlan ormanda eğlenceli bir oyun oynuyordu. Kozalakları uzaktan sepetine atıyordu. Ama sepet çok sertti ve kozalaklar hep dışarı zıplıyordu. Keloğlan birkaç kez daha denedi ama olmadı. Sonra yoruldu ve bir kütüğün üstüne oturup dinlendi. Zıplayan bir kozalak kütüğün yanındaki sulu ve yumuşak yosunların üstüne düşmüştü. Keloğlan merak etti ve bir kozalak daha oraya attı. Kozalak hiç zıplamadı. Böylece kozalağın yumuşak yerde durduğunu öğrendi. Hemen sepetin dibine biraz yosun koydu. Sonra kozalakları yine attı. Bu kez hepsi sepette kaldı ve Keloğlan sevinçle el çırptı. Keloğlan bundan sonra oyunda hep sepete yosun koydu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sulu ve yumuşak yosunların"
   - Cümle 6: «Zıplayan bir kozalak kütüğün yanındaki sulu ve yumuşak yosunların üstüne düşmüştü.»
   - Açıklama: Yosun için 'sulu' uygun değil; 'ıslak' olmalı.
   - Açıklama: Yosun için 'sulu' yanlış kelime; 'ıslak' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan merak etti ve bir kozalak daha oraya attı"
   - Cümle 7: «Keloğlan merak etti ve bir kozalak daha oraya attı.»
   - Açıklama: Çözüm denemeler, dinlenme, tesadüfi gözlem ve test üzerinden ikiden fazla adımda geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0121` birebir aynı, `@degisim: etiket -> kozalak` (tutuyorsan), ardından `@onarim: 463b0fb6bc9ee91e985854481e638a331e73933f`, sonra gövde.

### Hikâye 8: tohum keloglan-0122 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0122
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yonca', fiil 'götürmek', sıfat 'sert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: rüzgar otları sallıyordu ve yaprakları saymak zordu | otları eliyle tuttu ve birer birer saydı
@tohum: keloglan-0122
Rüzgar ormanda sert esiyordu. Keloğlan ilk kez dört yapraklı bir yonca aramayı denedi. Ama rüzgar yüzünden otlar hep sallanıyordu ve yaprakları saymak zordu. Sallanan bir yonca ona dört yapraklı gibi göründü. Keloğlan onu hemen cebine koymadı, çünkü dürüsttü. Önce yoncayı eliyle tuttu ve yapraklarını saydı. Yonca artık sallanmadı ve yalnız üç yaprağı vardı. Sonra öteki otları da birer birer eliyle tuttu ve saydı. Sonunda gerçek bir dört yapraklı yonca buldu. Keloğlan onu eve götürmek için dikkatle cebine koydu ve sevinçle güldü.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hemen cebine koymadı, çünkü dürüsttü"
   - Cümle 5: «Keloğlan onu hemen cebine koymadı, çünkü dürüsttü.»
   - Açıklama: Yoncayı saymadan cebine koymamanın sebebi olarak dürüstlük gösterilmesi olaydan çıkmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan onu hemen cebine koymadı, çünkü dürüsttü"
   - Cümle 5: «Keloğlan onu hemen cebine koymadı, çünkü dürüsttü.»
   - Açıklama: Yoncayı saymadan cebe koymamanın sebebi olarak dürüstlük gösteriliyor; olay bu özellikten mantıklı biçimde çıkmıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "öteki otları da birer birer eliyle tuttu ve saydı"
   - Cümle 8: «Sonra öteki otları da birer birer eliyle tuttu ve saydı.»
   - Açıklama: Sayılan şey yaprak olmalıyken cümle otları saymış gibi kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0122` birebir aynı, ardından `@onarim: 2caef7f508c0dc94501275a5ee3c3bd21da5d172`, sonra gövde.

### Hikâye 9: tohum keloglan-0123 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0123
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bitki', fiil 'şaşırtmak', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: bahçede bir sürü bitki vardı ve naneyi tanımıyordu | kitaptaki resimden naneyi tanıyıp bir demet topladı
@tohum: keloglan-0123
@degisim: hevesli -> yeşil
Şatonun bahçesinde hafif bir rüzgar esiyordu. Keloğlan, naneyi çok seven Bilgecan Dede'yi bir demet nane ile şaşırtmak istiyordu. Ama bahçede bir sürü yeşil bitki vardı ve Keloğlan naneyi tanımıyordu. Dede o sırada şatonun içinde uyuyordu. Keloğlan, Dede'nin bitki kitabını hatırladı ve kitabı içeriden getirdi. Keloğlan kitabın sayfalarını çevirdi ve bir nane resmi buldu. Resme bakıp nane yaprağını tanımayı öğrendi. Keloğlan hemen bahçede dolaştı. Aynı yaprakları duvarın dibinde buldu ve küçük bir demet topladı. Dede uyanınca Keloğlan demeti ona uzattı. Dede çok şaşırdı ve naneyi sevinçle kokladı. Keloğlan çok sevindi, çünkü naneyi tek başına bulmuştu.
```

**Hakem bulguları (3):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "naneyi çok seven Bilgecan Dede'yi"
   - Cümle 2: «Keloğlan, naneyi çok seven Bilgecan Dede'yi bir demet nane ile şaşırtmak istiyordu.»
   - Açıklama: Kartta Bilgecan Dede'nin naneyi sevdiğine dair bilgi yok, uydurulmuş bir özellik ekleniyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Dede o sırada şatonun içinde uyuyordu"
   - Cümle 4: «Dede o sırada şatonun içinde uyuyordu.»
   - Açıklama: Kartta Bilgecan Dede'nin şatoda yaşadığı ya da uyuduğu bir yer bilgisi yok; şato tarifi sahipsiz taş saraydır.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Dede o sırada şatonun içinde uyuyordu"
   - Cümle 4: «Dede o sırada şatonun içinde uyuyordu.»
   - Açıklama: Kartın ilişki alanında Bilgecan Dede köyün bilge kişisidir; köyün uzağındaki şatoda uyuması yanlış bilgi veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0123` birebir aynı, `@degisim: hevesli -> yeşil` (tutuyorsan), ardından `@onarim: d782ead90e3c05c9cc98f3fc3af8987959311cc9`, sonra gövde.

### Hikâye 10: tohum keloglan-0126 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0126
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'bambu', fiil 'silmek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kütük tozluydu ve halkalar iyi görünmüyordu | kütüğü suyla ıslatıp mendille sildi
@tohum: keloglan-0126
@degisim: bambu -> kütük
Keloğlan ile anası ormanda kesilmiş büyük bir kütüğün yanına geldi. Keloğlan kütüğün üstünde ince halkalar fark etti. Halkaları saymak istedi ama kütük tozluydu ve halkalar iyi görünmüyordu. Keloğlan tozu ıslatmak için su şişesini açtı. Suyu kütüğün üstüne yavaşça döktü. Sonra cebinden mendilini çıkardı ama sakar Keloğlan mendili ıslak toprağa düşürdü. Keloğlan anasından bir mendil istedi. Anası ona yepyeni bir mendil verdi. Keloğlan ıslak kütüğü mendille sildi. Kütüğün üstünde hiç toz kalmadı ve bütün halkalar göründü. Keloğlan halkaları tek tek saydı ve tam yirmi halka buldu. Sonra ikisi ormanda başka kütükler aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sakar Keloğlan mendili ıslak toprağa düşürdü"
   - Cümle 6: «Sonra cebinden mendilini çıkardı ama sakar Keloğlan mendili ıslak toprağa düşürdü.»
   - Açıklama: Sakarlık yalnız ara olay; çözüme katkısı yok, özellik işe yarar biçimde kullanılmamış.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sakar Keloğlan mendili ıslak toprağa düşürdü"
   - Cümle 6: «Sonra cebinden mendilini çıkardı ama sakar Keloğlan mendili ıslak toprağa düşürdü.»
   - Açıklama: Tozlu kütük sorununun yanına mendilin düşmesiyle ikinci bir sorun ekleniyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "mendili ıslak toprağa düşürdü"
   - Cümle 6: «Sonra cebinden mendilini çıkardı ama sakar Keloğlan mendili ıslak toprağa düşürdü.»
   - Açıklama: Tozlu kütük sorununun yanına mendilin düşmesiyle ikinci bir sorun ekleniyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan anasından bir mendil istedi"
   - Cümle 7: «Keloğlan anasından bir mendil istedi.»
   - Açıklama: Çözüm su dökme, mendil düşürme, yeni mendil isteme ve silme ile iki adımı aşıyor.
   - Açıklama: Çözüm ıslatma, yeni mendil isteme ve silme olarak ikiden fazla adım sürüyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "başka kütükler aramaya mutlu mutlu devam etti"
   - Cümle 12: «Sonra ikisi ormanda başka kütükler aramaya mutlu mutlu devam etti.»
   - Açıklama: Daha önce kütük aramıyorlardı, 'devam etti' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0126` birebir aynı, `@degisim: bambu -> kütük` (tutuyorsan), ardından `@onarim: e830a27064d5b793c5451f186631513f023a9c22`, sonra gövde.

### Hikâye 11: tohum keloglan-0127 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0127
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'cetvel', fiil 'katmak', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: çatıdan garip bir tık sesi geldi | bekledi ve düşen kozalağı gördü
@tohum: keloglan-0127
@degisim: yaratıcı -> küçük
Rüzgar ormanda hafif hafif esiyordu. Keloğlan büyük bir ağacın altında dallardan küçük bir ev yapıyordu. Dalları tahta cetveliyle ölçüyor ve aynı boyda olanları seçiyordu. Birden çatıdan bir "tık" sesi geldi. Keloğlan bu sesi çok merak etti. Etrafına baktı ama hiçbir şey göremedi. Sonra evin yanına oturdu ve dikkatle bekledi. Ses bir süre gelmedi, ama dürüst ve azimli Keloğlan beklemeyi bırakmadı. Biraz sonra yukarıdaki daldan bir kozalak düştü. Kozalak çatıya çarptı ve aynı "tık" sesi geldi. Keloğlan kozalağı aldı ve çatıya bir dal daha kattı. Keloğlan çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (6):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Dalları tahta cetveliyle ölçüyor ve aynı boyda olanları seçiyordu.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede ortaya çıkıyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tahta cetveliyle ölçüyor"
   - Cümle 3: «Dalları tahta cetveliyle ölçüyor ve aynı boyda olanları seçiyordu.»
   - Açıklama: Cetvelle ölçme ayrıntısı işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalları tahta cetveliyle ölçüyor"
   - Cümle 3: «Dalları tahta cetveliyle ölçüyor ve aynı boyda olanları seçiyordu.»
   - Açıklama: Cetvelle ölçme ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çatıdan bir"
   - Cümle 4: «Birden çatıdan bir "tık" sesi geldi.»
   - Açıklama: Çatıya düşen bir sesin merak edilmesi çocuğun önemseyeceği gerçek bir sorun değil, önemsiz bir olay.
   - Açıklama: Çatıdan gelen bir ses gerçek bir sorun değil, önemsiz bir olay.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst ve azimli Keloğlan beklemeyi"
   - Cümle 8: «Ses bir süre gelmedi, ama dürüst ve azimli Keloğlan beklemeyi bırakmadı.»
   - Açıklama: 'Dürüst' beklemekle ilgisiz, bağlamına uymayan anlamda kullanılmış.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst ve azimli Keloğlan"
   - Cümle 8: «Ses bir süre gelmedi, ama dürüst ve azimli Keloğlan beklemeyi bırakmadı.»
   - Açıklama: Beklemeyi bırakmamakla dürüstlüğün ilgisi yok; 'dürüst' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0127` birebir aynı, `@degisim: yaratıcı -> küçük` (tutuyorsan), ardından `@onarim: b2bd79c23b1fd43ad623550e205500be08996df3`, sonra gövde.

### Hikâye 12: tohum keloglan-0128 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0128
- yer: dağ (Köyün yakınındaki tepe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fındık', fiil 'sıkışmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ıslak otlardaki ahşap kutunun kapağı sıkışmıştı | kutuyu taşa hafif hafif vurdu ve kapak açıldı
@tohum: keloglan-0128
Tepede hava serin ve sessizdi. Keloğlan orada oturmuş güneşin doğmasını bekliyordu. Yanındaki ahşap kutu ıslak otlarda duruyordu ve kapağı sıkışmıştı. Kutunun içinde Keloğlan'ın fındıkları vardı. Keloğlan kapağı çekti ama açamadı. Kutuyu kaldırırken sakar Keloğlan onu düz bir taşa düşürdü. Kapak biraz yukarı kalktı. Keloğlan bunu gördü ve biraz düşündü. Sonra kutuyu taşa kendisi hafif hafif vurdu. Kapak sonunda tam açıldı. Tam o sırada güneş tepenin arkasından doğdu. Keloğlan fındıklarını yiyerek güneşi mutlu mutlu seyretti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutuyu kaldırırken sakar Keloğlan onu düz bir taşa düşürdü"
   - Cümle 6: «Kutuyu kaldırırken sakar Keloğlan onu düz bir taşa düşürdü.»
   - Açıklama: Çözüm Keloğlan'ın düşüncesinden değil, sebepsiz bir kazadan geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0128` birebir aynı, ardından `@onarim: 2785bb9cdea3f2f02cf3cb75846dfe936f814606`, sonra gövde.
