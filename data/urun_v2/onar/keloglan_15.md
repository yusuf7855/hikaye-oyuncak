# Editör görevi (onarım): Keloğlan, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0036 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0036
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'duvar', fiil 'öğrenmek', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kar çok yumuşaktı ve duvar hep yıkılıyordu | karı sıkıca sıkıp sert toplar yaptı
@tohum: keloglan-0036
@degisim: öğrenmek -> sıkmak
Bir sabah ormana bembeyaz kar yağmıştı. Keloğlan büyük ağaçların arasında kardan bir duvar yapmak istedi. Ama kar çok yumuşaktı ve duvar hep yıkılıyordu. Dürüst Keloğlan işini bırakmadı ve yeniden denedi. Karı iki elinin arasında sıkıca sıktı. Kar sert bir top oldu. Keloğlan böyle toplardan bir sürü yaptı. Sonra kar toplarını yan yana ve üst üste koydu. Duvar yavaş yavaş yükseldi. Sonunda Keloğlan'ın boyu kadar yüksek oldu. Keloğlan duvarın arkasına oturdu ve gülümsedi. Keloğlan çok sevindi, çünkü kardan duvarı bitirmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dürüst Keloğlan işini bırakmadı"
   - Cümle 4: «Dürüst Keloğlan işini bırakmadı ve yeniden denedi.»
   - Açıklama: Dürüstlük işi bırakmamakla ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' kelimesi burada yanlış anlamda; pes etmemek dürüstlük değildir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0036` birebir aynı, `@degisim: öğrenmek -> sıkmak` (tutuyorsan), ardından `@onarim: 92a83169287a0616e93367897ff60ca044359fb0`, sonra gövde.

### Hikâye 2: tohum keloglan-0040 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0040
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mermer', fiil 'savurmak', sıfat 'süslü'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: ikisi de ipi aynı anda çekti | sırayla oynamayı söyledi ve önce arkadaşına verdi
@tohum: keloglan-0040
@degisim: mermer -> taş
Keloğlan ile Balkız şatonun bahçesinde taş bir yolda oynuyordu. Ellerinde tek bir süslü topaç vardı. İkisi de ipi aynı anda çekti ve ip karmakarışık oldu. "Balkız, sırayla oynayalım, önce sen çevir," dedi Keloğlan. Keloğlan ipi çözdü ve topacı Balkız'a verdi. Balkız ipi sardı ve topacı yere savurdu. Topaç taşın üstünde uzun uzun döndü. Sıra Keloğlan'a geldi. Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve sıkıca sardı. Sonra topacı yere attı ve topaç o da güzelce döndü. İkisi de güldü. "Sırayla oynamak çok eğlenceli, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 9: «Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve sıkıca sardı.»
   - Açıklama: 'Sakar' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve sıkıca sardı"
   - Cümle 9: «Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve sıkıca sardı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına göre sakarlık yalnız düşürmek ya da karıştırmak olarak gösterilir; burada sakarlık dikkatli sarma gerekçesi olarak kullanılıyor ve işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden ipi yavaşça"
   - Cümle 9: «Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve sıkıca sardı.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı bir şeyi düşürmek ya da karıştırmak olarak ister; burada sakarlık yalnız söyleniyor ve işe yaramıyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yere attı ve topaç o da güzelce döndü"
   - Cümle 10: «Sonra topacı yere attı ve topaç o da güzelce döndü.»
   - Açıklama: Özne 'topaç' ve 'o' ile iki kez yazılmış; cümle bozuk.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve topaç o da güzelce döndü"
   - Cümle 10: «Sonra topacı yere attı ve topaç o da güzelce döndü.»
   - Açıklama: 'topaç o da' yapısında gereksiz zamir cümleyi bozuyor; 'topaç da güzelce döndü' olmalı.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "topaç o da güzelce döndü"
   - Cümle 10: «Sonra topacı yere attı ve topaç o da güzelce döndü.»
   - Açıklama: 'Topaç' ile 'o' aynı özneyi gereksiz yere tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0040` birebir aynı, `@degisim: mermer -> taş` (tutuyorsan), ardından `@onarim: fef7820c98e2db0e231c04c76bd34d76c1c1b546`, sonra gövde.

### Hikâye 3: tohum keloglan-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0042
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yağmurluk', fiil 'boyamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: resmi boyamak için yeşil boya bitmişti | dededen yardım isteyip sarı ile maviyi karıştırdı
@tohum: keloglan-0042
@degisim: yağmurluk -> fırça
Keloğlan tepede resim yapma oyunu oynuyordu. Bilgecan Dede de yanına oturmuş, onu izliyordu. Keloğlan kağıttaki tepeyi boyamak istedi ama yeşil boyası bitmişti. Elinde yalnız sarı ile mavi boya vardı. "Dede, yeşil boyam bitti, ne yapayım?" diye sordu Keloğlan. "Sarı ile maviyi karıştır, yeşil olur," dedi Bilgecan Dede. Keloğlan biraz sakardı, bu yüzden sarı boyayı mavi boyanın içine yavaşça döktü. Sonra fırçasıyla iki rengi karıştırdı. Mavi renk yavaş yavaş yeşile döndü. Keloğlan resimdeki tepeyi yemyeşil boyadı. Bilgecan Dede resmi görünce ellerini çırptı. Keloğlan da mutlu mutlu yeni bir resme başladı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden sarı boyayı mavi boyanın içine yavaşça döktü"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden sarı boyayı mavi boyanın içine yavaşça döktü.»
   - Açıklama: Kartın özellik ve güvenli kullanım satırına göre sakarlık bir şeyi düşürmek ya da karıştırmaktır, burada sakarlık yavaş ve dikkatli dökmenin nedeni yapılarak yanlış ve işe yaramaz biçimde kullanılıyor.
   - Açıklama: Kartın güvenli kullanım satırına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilir, burada ise dikkatli dökme olarak işe yaramaz biçimde anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0042` birebir aynı, `@degisim: yağmurluk -> fırça` (tutuyorsan), ardından `@onarim: dbfcfae60b0397970846ce5c4e7122e5a457f557`, sonra gövde.

### Hikâye 4: tohum keloglan-0043 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0043
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yelpaze', fiil 'karşılaşmak', sıfat 'küçücük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: annenin küçücük yelpazesi ormanda düşmüştü | ağaçların altına bakıp yelpazeyi annesine geri verdi
@tohum: keloglan-0043
Keloğlan ormanda anasıyla karşılaştı. Anası üzgündü, çünkü küçücük yelpazesini ormanda düşürmüştü. "Hava çok sıcak," dedi anası. "Anneciğim, ben onu senin için bulurum," dedi Keloğlan. Keloğlan büyük ağaçların altına tek tek baktı. Sonunda bir ağacın altında yelpazeyi buldu. Yelpaze çok güzeldi ve Keloğlan onu çok beğendi. Ama dürüst Keloğlan yelpazeyi hemen anasına götürdü. Anası yelpazeyi salladı ve önce Keloğlan'ı, sonra kendini serinletti. "Teşekkür ederim, Keloğlan, sen bana çok yardım ettin!" dedi anası.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "annenin küçücük yelpazesi"
   - Cümle 0 (plan satırı): «annenin küçücük yelpazesi ormanda düşmüştü | ağaçların altına bakıp yelpazeyi annesine geri verdi»
   - Açıklama: İyelik eki eksik; kimin annesi olduğu belirtilmeli, 'annesinin' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "annenin küçücük yelpazesi ormanda"
   - Cümle 0 (plan satırı): «annenin küçücük yelpazesi ormanda düşmüştü | ağaçların altına bakıp yelpazeyi annesine geri verdi»
   - Açıklama: İyelik eksik; 'annesinin küçücük yelpazesi' olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçücük yelpazesini ormanda düşürmüştü"
   - Cümle 2: «Anası üzgündü, çünkü küçücük yelpazesini ormanda düşürmüştü.»
   - Açıklama: Yelpazenin nasıl ve nerede düştüğü söylenmiyor; Keloğlan'ın annesiyle ormanda rastlantıyla karşılaşması da akla yatkın değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "büyük ağaçların altına tek tek baktı"
   - Cümle 5: «Keloğlan büyük ağaçların altına tek tek baktı.»
   - Açıklama: Arama hiçbir ipucuna dayanmıyor; çözüm sebebe yönelmiyor, rastgele tarama.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yelpaze çok güzeldi ve Keloğlan onu çok beğendi"
   - Cümle 7: «Yelpaze çok güzeldi ve Keloğlan onu çok beğendi.»
   - Açıklama: Yelpazeyi beğenme ayrıntısı bir çatışma kuruyormuş gibi açılıyor ama hiçbir işe yaramadan kapanıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan onu çok beğendi"
   - Cümle 7: «Yelpaze çok güzeldi ve Keloğlan onu çok beğendi.»
   - Açıklama: Annesinin yelpazesini saklama isteği ima ediliyor ama bu ayrıntı olaydan çıkmıyor ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0043` birebir aynı, ardından `@onarim: e9dd3a3003b12ff58674b38aaf1c4eb3a734f951`, sonra gövde.

### Hikâye 5: tohum keloglan-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0044
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'şişe', fiil 'keşfetmek', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: şişeye üfledi ama hiç ses çıkmadı | şişenin ağzına yandan hafifçe üfledi
@tohum: keloglan-0044
@degisim: keşfetmek -> duymak
Evde pencereden rüzgar esti ve masadaki boş şişeden ince bir ses çıktı. Keloğlan da bu sesi çıkarmak istedi ve şişeye üfledi. Ama şişenin tam içine üfledi, bu yüzden hiç ses çıkmadı. Bu kez daha güçlü üfledi, ama şişe yine sessizdi. Keloğlan şişeye yakından baktı ve rüzgarı düşündü. Rüzgar şişenin içine değil, üstünden geçmişti. Keloğlan dudağını şişenin ağzına dayadı ve üstünden hafifçe üfledi. Bu kez Keloğlan şişeden aynı ince sesi duydu. Keloğlan birkaç kez daha üfledi ve güldü. Böylece şişeden ses çıkarmayı öğrendi. Keloğlan bundan sonra şişeleri hep yandan üfledi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "şişeleri hep yandan üfledi"
   - Cümle 11: «Keloğlan bundan sonra şişeleri hep yandan üfledi.»
   - Açıklama: 'Üflemek' yönelme ister; 'şişelere yandan üfledi' olmalı.
   - Açıklama: 'Üflemek' burada yönelme eki ister; 'şişelere yandan üfledi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0044` birebir aynı, `@degisim: keşfetmek -> duymak` (tutuyorsan), ardından `@onarim: eb53d4311cfecfb4238e660a5ad7169ccf458a00`, sonra gövde.

### Hikâye 6: tohum keloglan-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0045
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'boya', fiil 'duymak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: boya kabını düşürdü ve boya yere döküldü | dededen özür diledi ve evi birlikte boyadılar
@tohum: keloglan-0045
Ormanda Bilgecan Dede kuşlar için tahta bir ev boyuyordu. Keloğlan hazırlıklı gelmişti ve çantasına iki kap kırmızı boya koymuştu. Keloğlan bir kabı tutarak dedeye yardım ediyordu. Ama sakar Keloğlan kabı düşürdü ve boya yere döküldü. Bilgecan Dede sesi duydu ve arkasına döndü. Keloğlan yerdeki kırmızı lekeye baktı ve başını eğdi. "Özür dilerim, dede, boyayı ben düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede ve gülümsedi. Keloğlan çantasından ikinci kabı çıkardı ve onu iki eliyle sıkıca tuttu. İkisi evi birlikte boyadı ve bitirdi. Keloğlan çok sevindi, çünkü dede ona kızmamıştı ve kuşların evi hazırdı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan hazırlıklı gelmişti ve çantasına iki kap kırmızı boya koymuştu"
   - Cümle 2: «Keloğlan hazırlıklı gelmişti ve çantasına iki kap kırmızı boya koymuştu.»
   - Açıklama: Tohumdaki özellik sakarlık; kartın özellikler alanında olmayan hazırlıklılık sorunu çözen ikinci bir özellik olarak ekleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama sakar Keloğlan kabı"
   - Cümle 4: «Ama sakar Keloğlan kabı düşürdü ve boya yere döküldü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0045` birebir aynı, ardından `@onarim: b1777926fddbaa6fe54d2a1fec0a8f4f51f76bcf`, sonra gövde.

### Hikâye 7: tohum keloglan-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0047
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kiraz', fiil 'koklamak', sıfat 'meraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: bahçedeki tatlı kokunun nereden geldiğini bilmiyordu | gözlerini kapatıp kokladı ve kiraz ağacını buldu
@tohum: keloglan-0047
@degisim: meraklı -> tatlı
Şatonun büyük bahçesinde tatlı bir koku vardı. Keloğlan kokunun nereden geldiğini bulmak istedi. Ama bahçede bir sürü ağaç ve çiçek vardı. "Balkız, gözlerimi kapatıp kokuyu bulacağım," dedi Keloğlan. Dürüst Keloğlan gözlerini kapattı ve hiç açmadı. Sonra yavaşça döndü ve havayı kokladı. Sonunda eliyle kapının yanını gösterdi. "Koku oradan geliyor, Balkız!" dedi Keloğlan. Keloğlan gözlerini açtı ve ikisi o tarafa yürüdü. Kapının yanında beyaz çiçekli bir kiraz ağacı vardı. "İşte, kiraz çiçekleri!" dedi Balkız sevinçle. Keloğlan çok sevindi, çünkü kokuyu yalnız burnuyla bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gözlerini kapattı ve hiç açmadı"
   - Cümle 5: «Dürüst Keloğlan gözlerini kapattı ve hiç açmadı.»
   - Açıklama: 'Hiç açmadı' yanlış, çünkü Keloğlan sonra gözlerini açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0047` birebir aynı, `@degisim: meraklı -> tatlı` (tutuyorsan), ardından `@onarim: e5bcfb2b43e49879f88276a1d99f828026424ec4`, sonra gövde.

### Hikâye 8: tohum keloglan-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0048
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'gölge', fiil 'alışmak', sıfat 'plastik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşek acıktı ama tepedeki otlar kuruydu | kayanın gölgesinde taze ot bulup eşeği çağırdı
@tohum: keloglan-0048
@degisim: plastik -> taze
Tepede sıcak bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan yavaşça yürüyordu. Birden Karakaçan durdu ve yüksek sesle anırdı. Eşek çok acıkmıştı ama buradaki otlar kuruydu. Karakaçan yeşil otlara alışmıştı ve sarı otları yemedi. "Üzülme, sana taze ot bulacağım," dedi Keloğlan. Taşların arasına baktı ama hiç ot göremedi. Yorulmuştu ama dürüst Keloğlan verdiği sözü unutmadı. Sonra büyük bir kayanın gölgesine baktı. Gölgede taze ve yeşil otlar vardı. Keloğlan ıslık çaldı ve Karakaçan hemen yanına geldi. Eşek otları yedi ve başını salladı. Karakaçan ile Keloğlan serin gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden Karakaçan durdu ve yüksek sesle anırdı.»
   - Açıklama: İlk üç cümlede yalnız eşeğin durup anırdığı söyleniyor; acıkma ve kuru otlar sorunu ancak 4. cümlede açıklanıyor.
   - Açıklama: İlk üç cümlede yalnız eşeğin durup anırdığı söyleniyor; açlık ve kuru ot sorunu ancak 4. cümlede açıkça söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst Keloğlan verdiği sözü unutmadı"
   - Cümle 8: «Yorulmuştu ama dürüst Keloğlan verdiği sözü unutmadı.»
   - Açıklama: 'Verdiği sözü unutmamak' soyut bir deyimsel anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0048` birebir aynı, `@degisim: plastik -> taze` (tutuyorsan), ardından `@onarim: 02cf4e4f5499f5b5a0617bb437260555aee0e5f2`, sonra gövde.

### Hikâye 9: tohum keloglan-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0049
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'balon', fiil 'şişirmek', sıfat 'elmalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: kırmızı balon çok sert olduğu için büyümedi | balonu önce çekip yumuşattı sonra şişirdi
@tohum: keloglan-0049
@degisim: elmalı -> kırmızı
Ormanda kuşlar neşeyle ötüyordu. Keloğlan ile Balkız ağaçların altında balon dükkanı oyunu oynuyordu. Balkız kırmızı bir balon istedi ama balon çok sertti ve hiç büyümüyordu. Sakar Keloğlan balonu elinden düşürdü ve ucuna bastı. Balonu ayağının altından çekince balon uzadı. Keloğlan bunu görünce balonu iki eliyle birkaç kez çekip gerdi. Balon biraz yumuşadı. Sonra Keloğlan derin bir nefes aldı ve balonu şişirdi. Kırmızı balon yavaş yavaş büyüdü. "İşte kırmızı balonun, Balkız!" dedi Keloğlan. Balkız balonu aldı ve sevinçle güldü. Sonra ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan balonu elinden düşürdü ve ucuna bastı"
   - Cümle 4: «Sakar Keloğlan balonu elinden düşürdü ve ucuna bastı.»
   - Açıklama: Çözüm fikri Keloğlan'ın düşünmesinden değil, balonu kazara düşürüp basmasından sebepsizce geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan balonu elinden düşürdü"
   - Cümle 4: «Sakar Keloğlan balonu elinden düşürdü ve ucuna bastı.»
   - Açıklama: Çözüm Keloğlan'ın düşünmesinden değil, balonu kazara düşürüp üstüne basmasından tesadüfen çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0049` birebir aynı, `@degisim: elmalı -> kırmızı` (tutuyorsan), ardından `@onarim: 9e186bd4fee43d74c56543c8fd89ad47e93bdd70`, sonra gövde.

### Hikâye 10: tohum keloglan-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0050
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'toprak', fiil 'uzamak', sıfat 'sevimli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: filiz çok uzadığı için yana eğilmişti | filizi iple ince bir çubuğa bağladı
@tohum: keloglan-0050
Keloğlan evde bahçe oyunu oynuyordu. Pencerenin önünde bir saksıda sevimli bir filiz vardı. Filiz çok uzamıştı ve yana doğru eğilmişti. Keloğlan filizi düz tutmak istedi. Önce filizi eliyle kaldırdı, ama elini çekince filiz yine eğildi. Dürüst ve çalışkan Keloğlan bu işi bırakmadı. Mutfaktan ince bir çubuk ve bir parça ip getirdi. Çubuğu filizin yanında toprağa yavaşça soktu. Sonra filizi iple çubuğa hafifçe bağladı. Filiz artık düz duruyordu. Keloğlan saksıyı suladı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "evde bahçe oyunu oynuyordu"
   - Cümle 1: «Keloğlan evde bahçe oyunu oynuyordu.»
   - Açıklama: Evde 'bahçe oyunu' oynamak anlamca tutarsız bir kelime seçimi.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dürüst ve çalışkan Keloğlan"
   - Cümle 6: «Dürüst ve çalışkan Keloğlan bu işi bırakmadı.»
   - Açıklama: Tohumdaki özellik dürüst/azimli; kartın özellikler alanında olmayan 'çalışkan' ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0050` birebir aynı, ardından `@onarim: 6d999088a0f9a3b43240f019524f9e107e0dafdd`, sonra gövde.

### Hikâye 11: tohum keloglan-0052 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0052
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'poğaça', fiil 'bükmek', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annenin hamuru çoktu ve kolları yorulmuştu | poğaça yapmayı öğrendi ve annesine yardım etti
@tohum: keloglan-0052
@degisim: narin -> yumuşak
Dışarıda yağmur yağıyordu. Keloğlan mutfakta anasının yanına geldi. Anası poğaça yapıyordu ama hamur çok fazlaydı ve kolları yorulmuştu. "Anneciğim, ben de poğaça yapmayı öğrenmek istiyorum," dedi Keloğlan. Anası küçük bir hamur parçasını açtı ve ay gibi büktü. "Hamur yumuşak, yavaşça bük," dedi anası. Keloğlan ilk poğaçayı biraz yamuk yaptı ve ikisi de güldü. İkinci poğaçayı ise çok güzel yaptı. Sonra Keloğlan ile anası bütün hamuru birlikte bükerek tepsiye dizdi. Kısa sürede tepsi doldu. "Teşekkür ederim, Keloğlan, işimiz ne çabuk bitti!" dedi anası.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "annenin hamuru çoktu"
   - Cümle 0 (plan satırı): «annenin hamuru çoktu ve kolları yorulmuştu | poğaça yapmayı öğrendi ve annesine yardım etti»
   - Açıklama: Plan satırında iyelik eksik; 'annesinin hamuru' olmalı.
   - Açıklama: İyelik eki yanlış; 'annesinin hamuru' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0052` birebir aynı, `@degisim: narin -> yumuşak` (tutuyorsan), ardından `@onarim: b408e50c59514846a3b526052b74051c9b4c127b`, sonra gövde.

### Hikâye 12: tohum keloglan-0054 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0054
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'giysi', fiil 'vermek', sıfat 'konuşkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: kayaların arkasından garip bir ses geldi | sesin peşinden gidip dedenin yeni icadını buldu
@tohum: keloglan-0054
@degisim: konuşkan -> garip
Tepede serin bir rüzgar esiyordu. Keloğlan kayaların arkasından garip bir tık tık sesi duydu. Bu sesin ne olduğunu çok merak etti. Kayaların arkasına gitti ve orada Bilgecan Dede'yi gördü. Yanında büyük bir şeyin üstünde eski bir giysi duruyordu. Ses bu giysinin altından geliyordu. "Bilgecan Dede, bu ses nedir?" diye sordu Keloğlan. "Kendin bak," dedi dede ve gülümsedi. Keloğlan yaklaşırken sakar davrandı ve eski giysi yere düştü. Altında rüzgarla dönen tahta bir çark vardı. Çark dönünce küçük tahtalar birbirine çarpıyordu. Keloğlan çarkı eliyle çevirmek istedi ve dede ona izin verdi. Sonra ikisi dönen çarkı mutlu mutlu seyretti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedenin yeni icadını buldu"
   - Cümle 0 (plan satırı): «kayaların arkasından garip bir ses geldi | sesin peşinden gidip dedenin yeni icadını buldu»
   - Açıklama: 'İcat' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip bir tık tık sesi duydu"
   - Cümle 2: «Keloğlan kayaların arkasından garip bir tık tık sesi duydu.»
   - Açıklama: Merak edilen bir ses gerçek bir sorun değil; çözülecek bir dert yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan yaklaşırken sakar davrandı ve eski giysi yere düştü"
   - Cümle 9: «Keloğlan yaklaşırken sakar davrandı ve eski giysi yere düştü.»
   - Açıklama: Çözüm Keloğlan'ın bilinçli bir adımıyla değil sebepsiz bir kazayla geliyor.
   - Açıklama: Gizem Keloğlan'ın bilinçli bir hamlesiyle değil kazayla, sebepsizce çözülüyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Altında rüzgarla dönen tahta bir çark vardı"
   - Cümle 10: «Altında rüzgarla dönen tahta bir çark vardı.»
   - Açıklama: Çark giysinin altında örtülüyken rüzgarla dönüp ses çıkarıyor, bu çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0054` birebir aynı, `@degisim: konuşkan -> garip` (tutuyorsan), ardından `@onarim: 8c9a42e4f20488d1ee7d7cb05ddfa9fcb6cd9791`, sonra gövde.
