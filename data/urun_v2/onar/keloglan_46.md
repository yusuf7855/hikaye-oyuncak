# Editör görevi (onarım): Keloğlan, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar46.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0149 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0149
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'şal', fiil 'şekillendirmek', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kar çok kuru olduğu için elinde dağılıyordu | güneşte ıslak kar bulup onunla kale yaptı
@tohum: keloglan-0149
@degisim: gizemli -> ıslak
Ormanda Keloğlan kardan bir kale yapmak istiyordu. Yanına bayrak için eski bir şal almıştı. Ama kar çok kuruydu ve elinde hemen dağılıyordu. Keloğlan büyük ağaçların arasında dikkatle baktı. Güneşin vurduğu bir yerde kar parlıyordu ve biraz ıslaktı. Oradan bir avuç kar aldı ve sıktı. Bu kar hemen top oldu. Keloğlan böylece ıslak karın daha iyi olduğunu öğrendi. Sonra o karı elleriyle şekillendirdi ve küçük bir kale yaptı. Eski şalı bir dala bağladı ve kalenin üstüne dikti. Keloğlan kalesinin yanında mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Keloğlan büyük ağaçların arasında dikkatle baktı"
   - Cümle 4: «Keloğlan büyük ağaçların arasında dikkatle baktı.»
   - Açıklama: 'Baktı' fiilinin yönelme tümleci eksik ve 'arasında baktı' kuruluşu bozuk; 'ağaçların arasına dikkatle baktı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "o karı elleriyle şekillendirdi"
   - Cümle 9: «Sonra o karı elleriyle şekillendirdi ve küçük bir kale yaptı.»
   - Açıklama: 'Şekillendirdi' 3 yaşındaki çocuğun bilmediği soyut bir fiil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0149` birebir aynı, `@degisim: gizemli -> ıslak` (tutuyorsan), ardından `@onarim: 285c90b8e84ddf71db454048640a5f7578e65282`, sonra gövde.

### Hikâye 2: tohum keloglan-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0150
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'tüy', fiil 'havalanmak', sıfat 'yardımsever'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: eşek de oynamak istedi ama tüyü tutamıyordu | tüyü eşeğin burnuna uzatıp sırayla oynadılar
@tohum: keloglan-0150
@degisim: yardımsever -> beyaz
Evin önünde Keloğlan yerde beyaz bir tüy buldu. Tüyü avucuna koyup üfledi ve tüy havalandı. Eşeği Karakaçan da oynamak istedi, ama tüyü tutacak eli yoktu. Keloğlan tüyü yerden aldı ve biraz düşündü. Keloğlan biraz sakardı, bu yüzden tüy düşmesin diye onu avucunun ortasına koydu. Sonra avucunu Karakaçan'ın burnunun önüne tuttu. Karakaçan burnundan hızla üfledi ve tüy yukarı uçtu. Keloğlan güldü, tüyü yakaladı ve yine eşeğin burnuna tuttu. Karakaçan bir daha üfledi ve tüy tekrar havalandı. Sonra sıra Keloğlan'a geldi. Keloğlan ile eşeği tüyle sırayla oynayarak çok eğlendi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden"
   - Cümle 5: «Keloğlan biraz sakardı, bu yüzden tüy düşmesin diye onu avucunun ortasına koydu.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı bir şeyi düşürmek ya da karıştırmak olarak göstermeyi istiyor; burada sakarlık yalnız söyleniyor, gösterilmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden tüy düşmesin"
   - Cümle 5: «Keloğlan biraz sakardı, bu yüzden tüy düşmesin diye onu avucunun ortasına koydu.»
   - Açıklama: Sakarlık işe yarayacakmış gibi kuruluyor ama olayda hiçbir sonucu yok, Keloğlan tüyü sorunsuz yakalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden"
   - Cümle 5: «Keloğlan biraz sakardı, bu yüzden tüy düşmesin diye onu avucunun ortasına koydu.»
   - Açıklama: Sakarlık işe yarayacakmış gibi kuruluyor ama hikayede hiçbir sonucu olmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0150` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 032f9f5ddcc7e76bd5069c3ce0291846481c10c3`, sonra gövde.

### Hikâye 3: tohum keloglan-0153 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0153
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'şemsiye', fiil 'ekmek', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: rüzgar esti ve tohumları avucundan uçurmaya başladı | şemsiyeyi açtı ve arkasında tohumları ekti
@tohum: keloglan-0153
Dağda Keloğlan bahçe oyunu oynuyordu. Elinde ilginç, çizgili ayçiçeği tohumları vardı. Ama rüzgar esti ve tohumları avucundan uçurmaya başladı. Keloğlan tohumları sıkıca tuttu. Yanında bir şemsiye vardı, çünkü hava bulutluydu. Keloğlan dürüst bir çocuktu ve işini bırakmazdı. Şemsiyeyi açtı ve rüzgara karşı yere koydu. Şemsiyenin arkasında hiç rüzgar yoktu. Keloğlan toprağı parmağıyla kazdı. Tohumları tek tek ekti ve üstlerini örttü. Tohumlar artık uçmadı ve bahçe hazır oldu. Keloğlan bundan sonra rüzgarlı havada tohumlarını şemsiyenin arkasında ekti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elinde ilginç, çizgili"
   - Cümle 2: «Elinde ilginç, çizgili ayçiçeği tohumları vardı.»
   - Açıklama: 'İlginç' soyut bir değerlendirme kelimesi, 3 yaşındaki çocuk için uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elinde ilginç, çizgili ayçiçeği"
   - Cümle 2: «Elinde ilginç, çizgili ayçiçeği tohumları vardı.»
   - Açıklama: 'İlginç' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında bir şemsiye vardı, çünkü hava bulutluydu"
   - Cümle 5: «Yanında bir şemsiye vardı, çünkü hava bulutluydu.»
   - Açıklama: Şemsiye sorun çıktıktan sonra sebepsizce beliriyor ve çözümü hazır getiriyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmazdı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmazdı.»
   - Açıklama: 'Dürüst' kelimesi işini bırakmamakla ilgili değil; yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' kelimesi işini bırakmamakla ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmazdı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmazdı.»
   - Açıklama: Tohumdaki dürüstlük özelliği hikayede hiçbir işe yaramıyor, yalnız etiket olarak söyleniyor.
   - Açıklama: Tohumdaki özellik iş görmeden bir liste cümlesi olarak söyleniyor ve dürüstlük hikayede hiç kullanılmıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmazdı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmazdı.»
   - Açıklama: Dürüstlük olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Dürüstlük olayla ilgisiz, işlevsiz bir ayrıntı olarak araya giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0153` birebir aynı, ardından `@onarim: f4cff73b549f3aee71f395e1f7f01334d164884a`, sonra gövde.

### Hikâye 4: tohum keloglan-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0156
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'şerit', fiil 'esnemek', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: rüzgar mavi şeridi uçurdu ve şerit çalıya takıldı | arkadaşından yardım istedi ve şeridi birlikte çıkardılar
@tohum: keloglan-0156
@degisim: somurtkan -> üzgün
Şatonun büyük bahçesinde Keloğlan ile Balkız oynuyordu. Birden rüzgar esti ve Balkız'ın mavi şeridi uçtu. Şerit bir çalıya takıldı ve Balkız üzgün üzgün baktı. Keloğlan şeridi ucundan çekti. Şerit esnedi ama dallardan çıkmadı. Ama Keloğlan sakardı ve şeridi yanlışlıkla dallara daha çok doladı. Bunu görünce Balkız'dan yardım istedi. Balkız dalları iki eliyle yavaşça ayırdı. Keloğlan da şeridi dalların arasından dikkatle çıkardı. Sonra şeridi Balkız'ın sarı saçına bağladı. Balkız hemen gülümsedi. Keloğlan çok sevindi, çünkü Balkız yine gülüyordu.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şerit esnedi ama dallardan çıkmadı"
   - Cümle 5: «Şerit esnedi ama dallardan çıkmadı.»
   - Açıklama: 'ama' ile biten cümleden hemen sonra yeni cümle yine 'Ama' ile başlıyor; gereksiz tekrar.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Keloğlan sakardı"
   - Cümle 6: «Ama Keloğlan sakardı ve şeridi yanlışlıkla dallara daha çok doladı.»
   - Açıklama: Karşıtlık yokken 'Ama' kullanılmış ve bir önceki cümledeki 'ama'dan hemen sonra tekrar ediyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "şeridi yanlışlıkla dallara daha çok doladı"
   - Cümle 6: «Ama Keloğlan sakardı ve şeridi yanlışlıkla dallara daha çok doladı.»
   - Açıklama: Keloğlan'ın sakarlığı şeridin takılmasının üstüne ikinci bir sorun ekliyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bunu görünce Balkız'dan yardım"
   - Cümle 7: «Bunu görünce Balkız'dan yardım istedi.»
   - Açıklama: Yardım isteyenin kim olduğu belli değil; 'Bunu görünce' başka birinin gördüğünü düşündürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0156` birebir aynı, `@degisim: somurtkan -> üzgün` (tutuyorsan), ardından `@onarim: 8a4e177be03ec9bb2d906b110d5153f90c33eaab`, sonra gövde.

### Hikâye 5: tohum keloglan-0158 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0158
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çorba', fiil 'koşuşturmak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: yorgun ve aç eşek ağacın altında durdu | elmasını eşeğiyle paylaşınca eşek yeniden yürüdü
@tohum: keloglan-0158
@degisim: sağlıklı -> sıcak
Keloğlan eşeğiyle ormandan eve dönüyordu. Eşek sırtında odunlarla ormanda çok koşuşturmuştu. Çok acıkmıştı ve büyük bir ağacın altında durdu. Keloğlan eve gidip sıcak çorba içmek istiyordu. Eşeği ipinden çekti ama eşek hiç yürümedi. Keloğlan'ın çantasında iki elma vardı. Ormana gelirken eşeğine bir elma vereceğini söylemişti. Keloğlan dürüst bir çocuktu ve söylediğini yaptı. Elmalardan birini eşeğine verdi. Eşek elmayı çıtır çıtır yedi. Sonra eşek başını salladı ve yeniden yürüdü. Keloğlan çok sevindi, çünkü elmasını eşeğiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ormanda çok koşuşturmuştu"
   - Cümle 2: «Eşek sırtında odunlarla ormanda çok koşuşturmuştu.»
   - Açıklama: Sırtında odun taşıyan eşek için 'koşuşturmak' fiili uygun değil; 'çok yürümüştü' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ormana gelirken eşeğine bir elma vereceğini söylemişti"
   - Cümle 7: «Ormana gelirken eşeğine bir elma vereceğini söylemişti.»
   - Açıklama: Daha önce hiç geçmeyen bir söz çözümü sebepsizce getiriyor; Keloğlan eşeğin aç olduğunu fark ettiği için değil, söz verdiği için elma veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0158` birebir aynı, `@degisim: sağlıklı -> sıcak` (tutuyorsan), ardından `@onarim: 7ea5b0f69ae01fcdbd1b0f0903180a0a98a9c89c`, sonra gövde.

### Hikâye 6: tohum keloglan-0159 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0159
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'palto', fiil 'yaslanmak', sıfat 'kahverengi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: paltonun delikleri dardı ve düğmeler geçmedi | anasından yardım isteyip düğmeleri geçirmeyi öğrendi
@tohum: keloglan-0159
Bir sabah her yer karla kaplıydı. Keloğlan evin önünde kar topu oynamak için yeni kahverengi paltosunu giydi. Ama delikler çok dardı ve düğmeler geçmiyordu. Keloğlan kapıya yaslandı ve biraz düşündü. Sonra pencerenin yanında oturan anasından yardım istedi. Anası düğmeyi deliğe yandan sokmayı gösterdi. Keloğlan dikkatle baktı ve bunu hemen öğrendi. Öteki düğmeleri tek tek kendisi kapattı. Palto sımsıkı kapandı ve Keloğlan'ı sıcacık tuttu. Keloğlan ile anası evin önünde mutlu mutlu kar topu oynadı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "kar topu oynamak için"
   - Cümle 2: «Keloğlan evin önünde kar topu oynamak için yeni kahverengi paltosunu giydi.»
   - Açıklama: Oyun adı 'kartopu' bitişik yazılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0159` birebir aynı, ardından `@onarim: 124d37c4972a900835379cde22d1e7cd67757878`, sonra gövde.

### Hikâye 7: tohum keloglan-0160 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0160
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'düdük', fiil 'indirmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yeşil boya kabı devrildi ve yeşil boya kalmadı | sarı ve mavi boyayı karıştırıp yeşil yaptı
@tohum: keloglan-0160
Ormanda kuşlar ötüyordu. Keloğlan, Bilgecan Dede için bir düdük boyuyordu. Ama biraz sakardı ve yeşil boya kabını devirdi. Yeşil boyanın hepsi toprağa aktı. Elinde yalnız sarı ve mavi boya kaldı. Dede biraz ileride odun topluyordu. Keloğlan, sarı ile mavinin yeşil yaptığını biliyordu. Sarıyı ve maviyi boş kaba döktü ve karıştırdı. Boya yemyeşil oldu! Keloğlan yeni boyayla düdüğü çizgi çizgi boyadı. Tam o sırada Dede elindeki odunları yere indirdi ve yanına geldi. "Sürpriz, dede! Bu çizgili düdük senin," dedi Keloğlan. Dede düdüğü alıp güldü. "Ne güzel bir düdük, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama biraz sakardı"
   - Cümle 3: «Ama biraz sakardı ve yeşil boya kabını devirdi.»
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir nitelik kelimesidir.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: ""Sürpriz, dede! Bu"
   - Cümle 12: «"Sürpriz, dede!»
   - Açıklama: Anlatımda ad gibi büyük harfle 'Dede' yazılan kişiye replikte küçük harfle 'dede' deniyor; yazım tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0160` birebir aynı, ardından `@onarim: e3d68bea1e7de4c01d0e6be5f4f149b26d508404`, sonra gövde.

### Hikâye 8: tohum keloglan-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0161
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'sürahi', fiil 'konmak', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: ikisi ipi kendi yanına çekince uçurtma aşağı indi | ipi tek başına tutunca uçtuğunu görüp sırayla uçurdular
@tohum: keloglan-0161
@degisim: konmak -> beklemek
Tepede serin bir rüzgar esiyordu ve gökyüzü masmaviydi. Keloğlan ile Balkız bir uçurtma uçuruyordu. Ama ikisi de ipi kendi yanına çekiyordu ve uçurtma sallanıp aşağı iniyordu. Keloğlan biraz sakardı ve ipi elinden düşürdü. İp yalnız Balkız'da kaldı ve uçurtma hemen yükseldi. "Önce sen tut, Balkız, sonra ben," dedi Keloğlan. Balkız başını salladı ve ipi sıkıca tuttu. Keloğlan beklerken sürahiden Balkız'a bir bardak su doldurdu. Sonra Balkız ipi Keloğlan'a verdi ve suyu içti. Keloğlan ipi tek başına tuttu ve uçurtma yine yükseldi. "Sırayla oynamak çok güzel, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "tek başına tutunca uçtuğunu görüp"
   - Cümle 0 (plan satırı): «ikisi ipi kendi yanına çekince uçurtma aşağı indi | ipi tek başına tutunca uçtuğunu görüp sırayla uçurdular»
   - Açıklama: Plan satırında ipi kimin tuttuğu ve 'uçtuğunu' sözünün neyi gösterdiği belli değil, çünkü uçurtma hiç anılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve ipi elinden düşürdü"
   - Cümle 4: «Keloğlan biraz sakardı ve ipi elinden düşürdü.»
   - Açıklama: Çözüm figürün düşünmesinden değil, rastlantıyla ipin düşmesinden sebepsizce geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sürahiden Balkız'a bir bardak su doldurdu"
   - Cümle 8: «Keloğlan beklerken sürahiden Balkız'a bir bardak su doldurdu.»
   - Açıklama: Tepede sürahi ve bardak sebepsiz beliriyor ve sorunla ilgisi olmayan işlevsiz bir ayrıntı oluyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan beklerken sürahiden Balkız'a bir bardak su doldurdu"
   - Cümle 8: «Keloğlan beklerken sürahiden Balkız'a bir bardak su doldurdu.»
   - Açıklama: Sürahi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor; ayrıca çözüm Keloğlan'ın ipi kazayla düşürmesiyle sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0161` birebir aynı, `@degisim: konmak -> beklemek` (tutuyorsan), ardından `@onarim: 4112331459ed88cd45107f4e01e2b9fadf82446f`, sonra gövde.

### Hikâye 9: tohum keloglan-0162 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0162
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bisküvi', fiil 'uyumak', sıfat 'sıcak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: üç bisküvi iki arkadaşa eşit olmuyordu | arkadaşından öğrendi ve son bisküviyi ikiye böldü
@tohum: keloglan-0162
@degisim: uyumak -> bölmek
Köy evinde masanın üstünde üç sıcak bisküvi vardı. Keloğlan ile Balkız onları eşit paylaşmak istedi. Ama üç bisküvi iki arkadaşa eşit olmuyordu. Keloğlan bunu nasıl yapacağını bilmiyordu. "Balkız, eşit paylaşmayı bana öğretir misin?" diye sordu Keloğlan. "Önce birer tane alalım, sonra kalanı ortadan bölelim," dedi Balkız. Keloğlan bir bisküviyi Balkız'a verdi, bir tane de kendisi aldı. Sonra son bisküviyi dikkatle tam ortasından böldü. İki parça aynı boydaydı. Keloğlan bir parçayı arkadaşına uzattı. İkisi bisküvilerini gülerek yedi. "Teşekkürler, Balkız, bugün yeni bir şey öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üç bisküvi iki arkadaşa eşit olmuyordu"
   - Cümle 3: «Ama üç bisküvi iki arkadaşa eşit olmuyordu.»
   - Açıklama: Bisküvi arkadaşa eşit olmaz; 'eşit bölünmüyordu' olmalı.
   - Açıklama: Plan satırında da fiil öznesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama üç bisküvi iki arkadaşa eşit olmuyordu"
   - Cümle 3: «Ama üç bisküvi iki arkadaşa eşit olmuyordu.»
   - Açıklama: Bisküvi arkadaşa eşit olmaz; 'eşit bölünmüyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0162` birebir aynı, `@degisim: uyumak -> bölmek` (tutuyorsan), ardından `@onarim: 91133b7fb4841f11c62574cbab1dfffee2a6a857`, sonra gövde.

### Hikâye 10: tohum keloglan-0163 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0163
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'nota', fiil 'çevirmek', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğin uzun ipi büyük bir ağaca takıldı | ipe bakıp öğrendi ve eşeği öbür yana çevirdi
@tohum: keloglan-0163
Ormanda büyük ağaçların arasında kuşlar ötüyordu. Keloğlan ıslıkla güzel notalar çaldı ve eşeğini çağırdı. Karakaçan koşarak geldi, ama uzun ipi bir ağaca takıldı. Eşek ileri gidemedi. Keloğlan ipi çekti ama ip çıkmadı. "Dur, Karakaçan, önce ipe bakayım," dedi Keloğlan. Keloğlan ağacın arkasına baktı ve yeni bir şey öğrendi. İp ağacın arkasından dönüp geri geliyordu. Keloğlan eşeğin başını öbür yana çevirdi ve onu geri götürdü. İp ağaçtan hemen çıktı. Karakaçan başını salladı ve yanına geldi. "Önce bakmak çok faydalı oldu," dedi Keloğlan. Keloğlan bundan sonra ip takılınca önce dikkatle baktı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ipe bakıp öğrendi ve"
   - Cümle 0 (plan satırı): «eşeğin uzun ipi büyük bir ağaca takıldı | ipe bakıp öğrendi ve eşeği öbür yana çevirdi»
   - Açıklama: Plan satırında 'öğrendi' fiilinin nesnesi yok, cümle eksik kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ıslıkla güzel notalar çaldı"
   - Cümle 2: «Keloğlan ıslıkla güzel notalar çaldı ve eşeğini çağırdı.»
   - Açıklama: Islıkla nota çalınmaz; 'ıslık çaldı' olmalı, fiil ve nesne uyumsuz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ıslıkla güzel notalar çaldı"
   - Cümle 2: «Keloğlan ıslıkla güzel notalar çaldı ve eşeğini çağırdı.»
   - Açıklama: 'Nota' 3 yaşındaki çocuğun bilmediği soyut bir kelime ve ıslıkla nota çalmak doğal bir anlatım değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "başını salladı ve yanına geldi"
   - Cümle 11: «Karakaçan başını salladı ve yanına geldi.»
   - Açıklama: 'yanına' zamirinin Keloğlan'ı mı ağacı mı gösterdiği belli değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Önce bakmak çok faydalı oldu"
   - Cümle 12: «"Önce bakmak çok faydalı oldu," dedi Keloğlan.»
   - Açıklama: 'Faydalı' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0163` birebir aynı, ardından `@onarim: 87efb175faa069cb9e21269c23e3cac04389a320`, sonra gövde.

### Hikâye 11: tohum keloglan-0164 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0164
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kapak', fiil 'değişmek', sıfat 'iyi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: kurabiye kutusunun kapağı çok sıkıydı ve açılmadı | doğruyu söyledi ve dedenin dediği gibi kapağı açtı
@tohum: keloglan-0164
@degisim: değişmek -> açılmak
Ormanda büyük bir ağacın altında Keloğlan, Bilgecan Dede için bir kutlama hazırlıyordu. Bugün Dede'nin doğum günüydü ve Keloğlan kurabiye getirmişti. Ama kurabiye kutusunun kapağı çok sıkıydı ve açılmadı. Keloğlan kapağı çekti, ama kapak kıpırdamadı. Keloğlan dürüst davrandı ve Dede'ye söyledi: "Sana kurabiye getirdim, ama kutuyu açamıyorum." Dede güldü ve "Kapağın kenarına üç kez vur, sonra çek," dedi. Keloğlan kenara üç kez vurdu ve çekti. Kapak "tık" diye açıldı. Keloğlan kurabiyeleri büyük bir yaprağa dizdi. "İyi ki doğdun, Dede!" dedi Keloğlan. "Ne iyi bir kutlama bu!" dedi Dede. Keloğlan bundan sonra bir işi yapamayınca hemen yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra bir işi yapamayınca hemen yardım istedi"
   - Cümle 12: «Keloğlan bundan sonra bir işi yapamayınca hemen yardım istedi.»
   - Açıklama: 'Bundan sonra' süreklilik bildirdiği için fiil geniş zamanın hikayesi olmalı: 'yardım isterdi'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0164` birebir aynı, `@degisim: değişmek -> açılmak` (tutuyorsan), ardından `@onarim: b4d95ba5c468231cb20b5ec8e8155df0cd997adb`, sonra gövde.

### Hikâye 12: tohum keloglan-0166 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0166
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kitap', fiil 'doymak', sıfat 'yeterli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: rüzgar kitabı pencereden düşürdü ve kitap kayboldu | sepete çarpıp devirdi ve kitabı samanın içinde buldu
@tohum: keloglan-0166
Köy evinde Keloğlan kitabını pencerenin önüne koymuştu. Birden rüzgar esti. Kitap pencereden bahçeye düştü. Keloğlan koşup bahçeye çıktı, ama kitabı göremedi. Pencerenin altında Karakaçan duruyordu. Yanında bir saman sepeti vardı. "Karakaçan, kitabımı gördün mü?" diye sordu Keloğlan. Karakaçan yalnız başını salladı. Keloğlan kapının önüne ve taşların arasına baktı. Sakar Keloğlan acele edip ayağıyla sepete çarptı. Sepet devrildi ve samanın içinden kitap çıktı! Kitap sepete düşmüştü. Karakaçan yeterli saman yiyip doymuştu. Kitaba hiç dokunmamıştı. Keloğlan samanı sepete geri koydu. Keloğlan çok sevindi, çünkü kitabını sağlam bulmuştu.
```

**Hakem bulguları (7):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kitap pencereden bahçeye düştü.»
   - Açıklama: Kitabın kaybolduğu sorun ancak 4. cümlede söyleniyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sakar Keloğlan acele edip ayağıyla sepete çarptı"
   - Cümle 10: «Sakar Keloğlan acele edip ayağıyla sepete çarptı.»
   - Açıklama: Kitap Keloğlan'ın bir çözüm eylemiyle değil, kazara sepete çarpmasıyla bulunuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sakar Keloğlan acele edip ayağıyla sepete çarptı"
   - Cümle 10: «Sakar Keloğlan acele edip ayağıyla sepete çarptı.»
   - Açıklama: Kitap kazayla bulunuyor; çözüm sebebe yönelmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "acele edip ayağıyla sepete çarptı"
   - Cümle 10: «Sakar Keloğlan acele edip ayağıyla sepete çarptı.»
   - Açıklama: Kitap aramaya yönelik bir çözümle değil tesadüfen sepete çarparak bulunuyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sepet devrildi ve samanın içinden kitap çıktı"
   - Cümle 11: «Sepet devrildi ve samanın içinden kitap çıktı!»
   - Açıklama: Çözüm sebebe yönelmiyor; kitap tesadüfen ortaya çıkıyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karakaçan yeterli saman yiyip doymuştu"
   - Cümle 13: «Karakaçan yeterli saman yiyip doymuştu.»
   - Açıklama: 'Yeterli' soyut bir kelime; 3 yaşındaki çocuk için 'bol bol saman yiyip' gibi somut olmalı.
   - Açıklama: 'Yeterli' 3 yaşındaki çocuk için soyut bir kelime ve cümle doğal değil.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan yeterli saman yiyip doymuştu"
   - Cümle 13: «Karakaçan yeterli saman yiyip doymuştu.»
   - Açıklama: Eşeğin doymuş olması ve kitaba dokunmaması olayda hiçbir işe yaramayan ayrıntı.
   - Açıklama: Eşeğin doymuş olması olayda hiçbir işe yaramayan ayrıntı.
   - Açıklama: Eşeğin doyduğu ayrıntısı işlevsiz, çözüm ise sebepsiz bir kazayla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0166` birebir aynı, ardından `@onarim: c9ff2e6fc95310bec4f5faa492d84856b4313b90`, sonra gövde.
