# Editör görevi (onarım): Keloğlan, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0155 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0155
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çuval', fiil 'yeşermek', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşeğine çok ağır çuvallar koydu ve eşek durdu | özür diledi ve ufak çuvalı kendi taşıdı
@tohum: keloglan-0155
@degisim: yeşermek -> okşamak
Dağda serin bir rüzgar esiyordu. Keloğlan, eşeği Karakaçan'ın sırtına iki çuval odun koymuştu. Büyük çuvalın yanında ufak bir çuval da vardı. Karakaçan birkaç adım attı ve durdu, çünkü çuvallar çok ağırdı. Keloğlan eşeğine fazla odun koyduğunu hemen anladı. Keloğlan dürüst bir çocuktu ve eşeğinden özür diledi. Eşeğinin başını okşadı. Sonra ufak çuvalı indirdi ve kendi sırtına aldı. Karakaçan başını salladı ve yeniden yürüdü. Keloğlan çok sevindi, çünkü eşeği artık büyük çuvalı kolayca taşıyordu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Karakaçan birkaç adım attı ve durdu"
   - Cümle 4: «Karakaçan birkaç adım attı ve durdu, çünkü çuvallar çok ağırdı.»
   - Açıklama: Eşeğin durması sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0155` birebir aynı, `@degisim: yeşermek -> okşamak` (tutuyorsan), ardından `@onarim: f353987c7fdcf6d24a0a4fd7954c5c50d9b2ea01`, sonra gövde.

### Hikâye 2: tohum keloglan-0156 (deneme 1 -> 2)

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
Şatonun büyük bahçesinde Keloğlan ile Balkız oynuyordu. Birden rüzgar esti ve Balkız'ın mavi şeridi uçtu. Şerit bir çalıya takıldı ve Balkız somurtkan bir yüzle baktı. Keloğlan şeridi ucundan çekti. Şerit esnedi ama dallardan çıkmadı. Keloğlan biraz sakardı ve şeridi dallara daha çok sardı. Bunu görünce Balkız'dan yardım istedi. Balkız dalları iki eliyle yavaşça ayırdı. Keloğlan da şeridi dalların arasından dikkatle çıkardı. Sonra şeridi Balkız'ın sarı saçına bağladı. Balkız hemen gülümsedi. Keloğlan çok sevindi, çünkü Balkız yine gülüyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Balkız somurtkan bir yüzle"
   - Cümle 3: «Şerit bir çalıya takıldı ve Balkız somurtkan bir yüzle baktı.»
   - Açıklama: 'Somurtkan' kelimesi 3 yaşındaki bir çocuk için zor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 6: «Keloğlan biraz sakardı ve şeridi dallara daha çok sardı.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0156` birebir aynı, ardından `@onarim: 45f27e01a667736570e26187425e1ba873c920ac`, sonra gövde.

### Hikâye 3: tohum keloglan-0157 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0157
- yer: dağ (Köyün yakınındaki tepe.)
- tema: kaybolan eşya
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yulaf', fiil 'değiştirmek', sıfat 'boyalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: rüzgar boyalı topu yokuştan aşağı yuvarladı | büyük taşın arkasına da bakıp topu buldu
@tohum: keloglan-0157
Bir sabah Keloğlan ile anası köyün yanındaki tepede oturuyordu. Anası kahvaltı için bir torba yulaf ve süt getirmişti. Birden rüzgar esti ve Keloğlan'ın boyalı topu yokuştan aşağı yuvarlandı. Keloğlan topun arkasından gitti ama onu otların arasında göremedi. "Anneciğim, topum kayboldu!" dedi Keloğlan. "Her yere baktın mı?" diye sordu anası. "Hayır, büyük taşın arkasına bakmadım," dedi Keloğlan dürüst bir şekilde. "O zaman orayı da ara," dedi anası. Keloğlan taşın arkasına baktı ve topunu buldu. Bu sefer yerlerini değiştirdiler ve düz bir yere oturdular. Sonra Keloğlan ile anası yulaflarını yiyip mutlu mutlu top oynadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "topu yokuştan aşağı yuvarlandı"
   - Cümle 3: «Birden rüzgar esti ve Keloğlan'ın boyalı topu yokuştan aşağı yuvarlandı.»
   - Açıklama: Top yuvarlanıyor, taşın arkasına bakılıp bulunuyor; sorun 'dağıldı, topladı, bitti' türünde önemsiz bir olay.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Keloğlan dürüst bir şekilde"
   - Cümle 7: «"Hayır, büyük taşın arkasına bakmadım," dedi Keloğlan dürüst bir şekilde.»
   - Açıklama: 'dürüst bir şekilde' soyut ve küçük çocuğa ağır bir anlatım.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu sefer yerlerini değiştirdiler"
   - Cümle 10: «Bu sefer yerlerini değiştirdiler ve düz bir yere oturdular.»
   - Açıklama: Daha önce yer değiştirme olmadığı için 'Bu sefer' yanlış anlamda.
   - Açıklama: 'Bu sefer' yanlış anlamda; daha önce yer değiştirme olmadığı için ifade anlamsız.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu sefer yerlerini değiştirdiler"
   - Cümle 10: «Bu sefer yerlerini değiştirdiler ve düz bir yere oturdular.»
   - Açıklama: 'Bu sefer' daha önce yaşanmamış bir olaya gönderme yapıyor ve yer değiştirme önceki olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0157` birebir aynı, ardından `@onarim: c9f2a1278bd8f6e000b0216eebd8edf5829e1ec1`, sonra gövde.

### Hikâye 4: tohum keloglan-0158 (deneme 1 -> 2)

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
Keloğlan eşeğiyle ormandan eve dönüyordu. Eşek sırtında odunlarla ormanda çok koşuşturdu. Çok acıkmıştı ve büyük bir ağacın altında durdu. Keloğlan eşeği ipinden çekti ama eşek yerinden kıpırdamadı. Keloğlan'ın çantasında bir kap çorba ve iki elma vardı. Elmayı yalnız gösterip eşeği kandırmak kolaydı. Ama Keloğlan dürüst davrandı ve elmalardan birini eşeğe verdi. Eşek elmayı çıtır çıtır yedi. Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti. Sonra eşek başını salladı ve yeniden yürümeye başladı. Keloğlan çok sevindi, çünkü elmasını paylaşınca eşeği neşeyle yola devam etmişti.
```

**Hakem bulguları (8):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Eşek sırtında odunlarla ormanda çok koşuşturdu"
   - Cümle 2: «Eşek sırtında odunlarla ormanda çok koşuşturdu.»
   - Açıklama: Önceki olay anlatıldığı için '-mıştı' olmalı; zaman uyumu bozuk.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "ormanda çok koşuşturdu"
   - Cümle 2: «Eşek sırtında odunlarla ormanda çok koşuşturdu.»
   - Açıklama: Önceden olmuş iş düz geçmişle anlatılıp zaman sırası kayıyor; 'koşuşturmuştu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "eşeği kandırmak kolaydı"
   - Cümle 6: «Elmayı yalnız gösterip eşeği kandırmak kolaydı.»
   - Açıklama: Varsayımsal 'kandırmak kolaydı' ifadesi 3 yaş için soyut.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama Keloğlan dürüst davrandı"
   - Cümle 7: «Ama Keloğlan dürüst davrandı ve elmalardan birini eşeğe verdi.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunu çözmüyor; eşek paylaşılan elmayla yürüyor, dürüstlük karttaki anlamıyla işe yaramıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sağlıklı çorbasını içti"
   - Cümle 9: «Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti.»
   - Açıklama: 'Sağlıklı' soyut ve bağlamda gereksiz bir niteleme.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oturdu ve sağlıklı çorbasını içti"
   - Cümle 9: «Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti.»
   - Açıklama: 'Sağlıklı' soyut bir sıfat ve burada gereksiz; küçük çocuğa uygun değil.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti"
   - Cümle 9: «Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti.»
   - Açıklama: Çorba sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sağlıklı çorbasını içti"
   - Cümle 9: «Keloğlan da ağacın altına oturdu ve sağlıklı çorbasını içti.»
   - Açıklama: Çorba kurulup sorunla hiç ilgisi olmayan işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0158` birebir aynı, ardından `@onarim: 4eacedb88871646c9cf4c1ee6e3154ea698e7ad1`, sonra gövde.

### Hikâye 5: tohum keloglan-0159 (deneme 1 -> 2)

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
@plan: yeni paltonun düğmeleri çok sıkıydı ve kapanmadı | anasından yardım isteyip düğmeleri kapatmayı öğrendi
@tohum: keloglan-0159
Bir sabah her yer karla kaplıydı. Keloğlan evin önünde kar topu oynamak için yeni kahverengi paltosunu giydi. Ama düğmeler çok sıkıydı ve deliklerden geçmiyordu. Keloğlan kapıya yaslandı ve biraz düşündü. Sonra pencerenin yanında oturan anasından yardım istedi. Anası düğmeyi deliğe yandan sokmayı gösterdi. Keloğlan dikkatle baktı ve bunu hemen öğrendi. Öteki düğmeleri tek tek kendisi kapattı. Palto sımsıkı kapandı ve Keloğlan'ı sıcacık tuttu. Keloğlan ile anası evin önünde mutlu mutlu kar topu oynadı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "paltonun düğmeleri çok sıkıydı ve kapanmadı"
   - Cümle 0 (plan satırı): «yeni paltonun düğmeleri çok sıkıydı ve kapanmadı | anasından yardım isteyip düğmeleri kapatmayı öğrendi»
   - Açıklama: Düğme sıkı olmaz ve kendisi kapanmaz; delikler dar olur, palto kapanmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0159` birebir aynı, ardından `@onarim: 9b8026dde7e12faa90f6a0e804cecde387419bb3`, sonra gövde.

### Hikâye 6: tohum keloglan-0160 (deneme 1 -> 2)

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
@plan: sürpriz düdüğü boyamak için yeşil boya yoktu | sarıyı maviye döktü ve yeşil boyayla düdüğü boyadı
@tohum: keloglan-0160
Ormanda kuşlar ötüyordu. Keloğlan büyük bir ağacın altında Bilgecan Dede için bir düdük boyuyordu. Düdüğün üstüne yeşil çizgiler çekmek istiyordu ama yanında yeşil boya yoktu. Elinde yalnız sarı ve mavi boya vardı. Dede biraz ileride odun topluyordu. Keloğlan biraz sakardı ve fırçayı alırken sarı boya kabını devirdi. Sarı boya mavi boyanın içine aktı ve yemyeşil bir renk oldu! Keloğlan yeni boyayla düdüğü çizgi çizgi boyadı. Tam o sırada Dede elindeki odunları yere indirdi ve Keloğlan'ın yanına geldi. "Sürpriz, dede! Bu çizgili düdük senin," dedi Keloğlan. Dede düdüğü alıp güldü. "Ne güzel bir düdük, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sarıyı maviye döktü ve yeşil"
   - Cümle 0 (plan satırı): «sürpriz düdüğü boyamak için yeşil boya yoktu | sarıyı maviye döktü ve yeşil boyayla düdüğü boyadı»
   - Açıklama: Plan boyayı bilerek döktüğünü söylüyor ama gövdede boya kap devrilerek kazayla karışıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "fırçayı alırken sarı boya kabını devirdi"
   - Cümle 6: «Keloğlan biraz sakardı ve fırçayı alırken sarı boya kabını devirdi.»
   - Açıklama: Yeşil boya Keloğlan'ın çözümüyle değil bir kazayla, tesadüfen elde ediliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "fırçayı alırken sarı boya kabını devirdi"
   - Cümle 6: «Keloğlan biraz sakardı ve fırçayı alırken sarı boya kabını devirdi.»
   - Açıklama: Yeşil boya bir kaza sonucu tesadüfen oluşuyor; çözüm sebepsizce, şansla geliyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve yemyeşil bir renk oldu"
   - Cümle 7: «Sarı boya mavi boyanın içine aktı ve yemyeşil bir renk oldu!»
   - Açıklama: Cümlenin öznesi sarı boya kalıyor; yeşil olanın karışım olduğu dilbilgisel olarak kurulmamış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aktı ve yemyeşil bir renk oldu"
   - Cümle 7: «Sarı boya mavi boyanın içine aktı ve yemyeşil bir renk oldu!»
   - Açıklama: Öznesi 'sarı boya' olan cümlede 'bir renk oldu' yanlış kullanım; boyalar karışıp yeşil oldu denmeli.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sarı boya mavi boyanın içine aktı"
   - Cümle 7: «Sarı boya mavi boyanın içine aktı ve yemyeşil bir renk oldu!»
   - Açıklama: Keloğlan sorunu bilerek çözmeye yönelmiyor, renkler kendiliğinden karışıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sarı boya mavi boyanın içine aktı"
   - Cümle 7: «Sarı boya mavi boyanın içine aktı ve yemyeşil bir renk oldu!»
   - Açıklama: Çözüm figürün eyleminden değil sebepsiz bir kazadan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0160` birebir aynı, ardından `@onarim: 9a40c3d47a56d766b9a524ccae7651f5481e5ce2`, sonra gövde.

### Hikâye 7: tohum keloglan-0161 (deneme 1 -> 2)

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
@plan: ikisi ipi aynı anda çekince uçurtma aşağı indi | ipi tek başına tutunca uçtuğunu görüp sırayla uçurdular
@tohum: keloglan-0161
@degisim: konmak -> beklemek
Tepede serin bir rüzgar esiyordu ve gökyüzü masmaviydi. Keloğlan ile Balkız bir uçurtma uçuruyordu. Ama ikisi de ipi aynı anda çekiyordu ve uçurtma aşağı iniyordu. Keloğlan biraz sakardı ve ipi elinden düşürdü. İp yalnız Balkız'da kaldı ve uçurtma hemen yükseldi. "Önce sen tut, Balkız, sonra ben," dedi Keloğlan. Balkız başını salladı ve ipi sıkıca tuttu. Keloğlan beklerken sürahiden biraz su içti. Sonra Balkız ipi Keloğlan'a verdi. Keloğlan ipi tek başına tuttu ve uçurtma yine yükseldi. "Sırayla oynamak çok güzel, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi de ipi aynı anda çekiyordu ve uçurtma aşağı iniyordu"
   - Cümle 3: «Ama ikisi de ipi aynı anda çekiyordu ve uçurtma aşağı iniyordu.»
   - Açıklama: İki kişinin ipi birlikte çekmesi ipi gerer, uçurtmanın aşağı inmesi için akla yatkın bir sebep değildir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "beklerken sürahiden biraz su"
   - Cümle 8: «Keloğlan beklerken sürahiden biraz su içti.»
   - Açıklama: 'Sürahi' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "beklerken sürahiden biraz su içti"
   - Cümle 8: «Keloğlan beklerken sürahiden biraz su içti.»
   - Açıklama: Sürahi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan beklerken sürahiden biraz su içti"
   - Cümle 8: «Keloğlan beklerken sürahiden biraz su içti.»
   - Açıklama: Sürahi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0161` birebir aynı, `@degisim: konmak -> beklemek` (tutuyorsan), ardından `@onarim: 40a296b6006b8bba0528610e18e292427cd6c8a2`, sonra gövde.

### Hikâye 8: tohum keloglan-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0165
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yorgan', fiil 'ilgilenmek', sıfat 'gri'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: yağmurda evde saklanacak yer yoktu | yorganı düşürdü ve saklanma yeri oldu
@tohum: keloglan-0165
Yağmur cama tık tık vuruyordu. Keloğlan evde anasıyla saklambaç oynamak istedi. Ama ev küçüktü ve saklanacak hiç yer yoktu. Anası elindeki işi bıraktı ve Keloğlan'la ilgilendi. Keloğlan yer ararken sakarlık yaptı ve gri yorganı raftan düşürdü. Yorgan yan yana duran iki sandalyenin üstüne serildi. Sandalyelerin altında çadır gibi bir yer oldu. "Anneciğim, işte saklanacak yer!" dedi Keloğlan. "Önce sen saklan, sonra ben," dedi anası. Keloğlan yorganın altına girdi ve anası onu buldu. Sonra sıra anasına geldi. Anası da çadıra saklandı ve Keloğlan onu hemen buldu. Keloğlan ile anası sırayla saklanmaya mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yorganı düşürdü ve saklanma yeri oldu"
   - Cümle 0 (plan satırı): «yağmurda evde saklanacak yer yoktu | yorganı düşürdü ve saklanma yeri oldu»
   - Açıklama: İki yüklemin öznesi farklı ama ikinci özne yazılmamış, cümle Keloğlan saklanma yeri oldu diye okunuyor.
   - Açıklama: İki yüklemin öznesi uyuşmuyor; düşüren Keloğlan, saklanma yeri olan yorgan.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ararken sakarlık yaptı ve"
   - Cümle 5: «Keloğlan yer ararken sakarlık yaptı ve gri yorganı raftan düşürdü.»
   - Açıklama: 'Sakarlık yaptı' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Keloğlan yer ararken sakarlık yaptı"
   - Cümle 5: «Keloğlan yer ararken sakarlık yaptı ve gri yorganı raftan düşürdü.»
   - Açıklama: Sorunu Keloğlan'ın bilinçli bir eylemi değil, bir kaza çözüyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "gri yorganı raftan düşürdü"
   - Cümle 5: «Keloğlan yer ararken sakarlık yaptı ve gri yorganı raftan düşürdü.»
   - Açıklama: Çözüm sebebe yönelik bir adım değil, rastlantı.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yaptı ve gri yorganı raftan düşürdü"
   - Cümle 5: «Keloğlan yer ararken sakarlık yaptı ve gri yorganı raftan düşürdü.»
   - Açıklama: Çözüm figürün sebebe yönelik bilinçli bir adımı değil, rastlantı sonucu bir kaza.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yorgan yan yana duran iki sandalyenin üstüne serildi"
   - Cümle 6: «Yorgan yan yana duran iki sandalyenin üstüne serildi.»
   - Açıklama: Düşen yorganın tesadüfen sandalyelere serilip çadır olması çözümü sebepsizce getiriyor.
   - Açıklama: Düşen yorganın tesadüfen iki sandalyenin üstüne serilmesi çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0165` birebir aynı, ardından `@onarim: 34907facf78f989e0ad699eb536203adeb0a946b`, sonra gövde.

### Hikâye 9: tohum keloglan-0167 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0167
- yer: dağ (Köyün yakınındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'un', fiil 'süslenmek', sıfat 'geniş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: anası tabağı süslemek istedi ama yakında çiçek yoktu | elmayı düşürdü ve taşın arkasında çiçek buldu
@tohum: keloglan-0167
@degisim: un -> kek
Tepenin üstü geniş ve düzdü. Keloğlan ile anası orada piknik yapıyordu. Anası kekin tabağını çiçeklerle süslemek istiyordu ama yakında hiç çiçek yoktu. "Ben sana çiçek bulurum, anneciğim," dedi Keloğlan. Keloğlan ayağa kalkarken sakarlık yaptı ve elindeki elmayı düşürdü. Elma yuvarlandı ve büyük bir taşın arkasında durdu. Keloğlan elmayı almak için taşın arkasına gitti. Orada bir sürü sarı çiçek vardı! Keloğlan birkaç çiçek topladı ve anasına götürdü. "Çiçekler taşın arkasındaymış, anneciğim!" dedi Keloğlan. Anası çiçekleri tabağın kenarına dizdi ve kekin tabağı güzelce süslendi. Keloğlan ile anası kekten birer dilim alıp mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ayağa kalkarken sakarlık yaptı"
   - Cümle 5: «Keloğlan ayağa kalkarken sakarlık yaptı ve elindeki elmayı düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "elindeki elmayı düşürdü"
   - Cümle 5: «Keloğlan ayağa kalkarken sakarlık yaptı ve elindeki elmayı düşürdü.»
   - Açıklama: Çözüm sebebe yönelmiyor; çiçekler elma rastlantıyla yuvarlanınca bulunuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yaptı ve elindeki elmayı düşürdü"
   - Cümle 5: «Keloğlan ayağa kalkarken sakarlık yaptı ve elindeki elmayı düşürdü.»
   - Açıklama: Çiçekler aranarak değil tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma yuvarlandı ve büyük bir taşın arkasında durdu"
   - Cümle 6: «Elma yuvarlandı ve büyük bir taşın arkasında durdu.»
   - Açıklama: Çözümü figürün eylemi değil sebepsiz bir rastlantı getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0167` birebir aynı, `@degisim: un -> kek` (tutuyorsan), ardından `@onarim: 58dc5b62d835d2ca6959f06c87d96ccb51c3971a`, sonra gövde.

### Hikâye 10: tohum keloglan-0169 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0169
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bardak', fiil 'uzanmak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: ağacın altındaki çiçekler yağmurda ıslanmadı | yapraklardaki damlaları bardağa toplayıp çiçekleri suladı
@tohum: keloglan-0169
@degisim: umutlu -> kuru
Keloğlan ormanda çiçek sulama oyunu oynuyordu. Bir bardağı sulama kabı yapmıştı ve Bilgecan Dede de yanındaydı. Az önce yağmur yağmıştı ama büyük ağacın altındaki çiçeklerin toprağı kuruydu. "Dede, bu çiçekler neden ıslanmadı?" diye sordu Keloğlan. "Ağacın dalları onları örttü, yağmur suyu yapraklarda kaldı," dedi Bilgecan Dede. Keloğlan bunu yeni öğrenmişti ve hemen bir şey düşündü. Alçak bir dala uzandı ve bardağı yaprakların altına tuttu. Dalı hafifçe salladı. Damlalar bardağa şıp şıp düştü. Keloğlan birkaç dalı daha salladı ve bardak doldu. Sonra suyu çiçeklerin dibine döktü. "Teşekkürler, Dede, çiçeklerim de sonunda su içti!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çiçeklerim de sonunda su içti"
   - Cümle 12: «"Teşekkürler, Dede, çiçeklerim de sonunda su içti!" dedi Keloğlan.»
   - Açıklama: Çiçeklerin su içmesi kişileştirme ve mecaz.
   - Açıklama: Çiçeklerin su içmesi kişileştirme ve mecazdır; 3 yaş için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0169` birebir aynı, `@degisim: umutlu -> kuru` (tutuyorsan), ardından `@onarim: cfd3da1412fbbe6a1c951223b8b9afaaeaeb376b`, sonra gövde.

### Hikâye 11: tohum keloglan-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0170
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tepsi', fiil 'uçuşmak', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: havada uçuşan beyaz tüylerin nereden geldiğini merak etti | çiçeği üfledi ve tüylerin tohum olduğunu öğrendi
@tohum: keloglan-0170
Rüzgar yavaşça esiyordu. Keloğlan ormanda küçük bir tepsiye çilek topluyordu. Birden havada beyaz tüyler uçuşmaya başladı. Birkaçı tepsideki çileklerin üstüne kondu. Keloğlan bu tüylerin nereden geldiğini çok merak etti. Rüzgarın geldiği yöne doğru yürüdü. Büyük bir ağacın dibinde top gibi beyaz çiçekler gördü. Keloğlan bir çiçeği eline aldı ve üfledi. Çiçekten bir sürü beyaz tüy havaya uçtu! Her tüyün ucunda küçük bir tohum vardı. Keloğlan böylece bu hafif tüylerin rüzgarla uçan çiçek tohumları olduğunu öğrendi.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden havada beyaz tüyler uçuşmaya başladı.»
   - Açıklama: Merak edilen sorun ancak 5. cümlede söyleniyor; ilk 3 cümlede açık bir sorun yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birkaçı tepsideki çileklerin üstüne kondu"
   - Cümle 4: «Birkaçı tepsideki çileklerin üstüne kondu.»
   - Açıklama: Tepsideki çilekler işe yarayacakmış gibi kuruluyor ama bir daha kullanılmıyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Keloğlan böylece bu hafif tüylerin rüzgarla uçan çiçek tohumları olduğunu öğrendi"
   - Cümle 11: «Keloğlan böylece bu hafif tüylerin rüzgarla uçan çiçek tohumları olduğunu öğrendi.»
   - Açıklama: Son cümle yalnız bilgiyi özetleyen çıplak bir sonuç; olaya bağlı bir his ya da sıcak bir kapanış yok.
   - Açıklama: Son cümle yalnız bir bilgi tespiti; his ya da sıcak bir kapanış yok ve çilek toplamaya dönülmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0170` birebir aynı, ardından `@onarim: 8bb7a15f833d7c2d63ad77c4f9b1ff89f9c89538`, sonra gövde.

### Hikâye 12: tohum keloglan-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0173
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tablo', fiil 'sıçratmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek de boyamak istedi ama fırçayı tutamıyordu | dalla boya sıçratmayı öğrendi ve dalı eşeğe verdi
@tohum: keloglan-0173
@degisim: ucuz -> mavi
Ormanda rüzgar serin serin esiyordu. Keloğlan büyük bir ağacın dibinde tahtaya mavi boyayla bir tablo yapıyordu. Karakaçan da boyamak istedi ama fırçayı tutamıyordu. Keloğlan yeni bir yol denemek için bir dal buldu. Dalı boyaya batırdı ve hafifçe salladı. Boya tabloya küçük noktalar halinde sıçradı. Keloğlan böylece dalla boya sıçratmayı öğrendi. Dalın kuru ucunu Karakaçan'ın ağzına verdi. "Sıra sende, Karakaçan," dedi Keloğlan. Karakaçan başını salladı ve tabloya mavi noktalar sıçrattı. Sonra sıra yine Keloğlan'a geldi. Keloğlan ile Karakaçan sırayla boyamaya mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Karakaçan da boyamak istedi"
   - Cümle 3: «Karakaçan da boyamak istedi ama fırçayı tutamıyordu.»
   - Açıklama: Kartın yanlar ve dünya kuralları alanında Karakaçan yük taşır, başını sallar, anırır; resim yapan eşek diziye yabancı bir bilgi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan da boyamak istedi"
   - Cümle 3: «Karakaçan da boyamak istedi ama fırçayı tutamıyordu.»
   - Açıklama: Karakaçan adı tanıtılmadan beliriyor ve okur onun eşek olduğunu anlayamıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir yol denemek"
   - Cümle 4: «Keloğlan yeni bir yol denemek için bir dal buldu.»
   - Açıklama: 'yol' burada 'yöntem' anlamında mecazdır ve küçük çocuk için soyuttur.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ucunu Karakaçan'ın ağzına verdi"
   - Cümle 8: «Dalın kuru ucunu Karakaçan'ın ağzına verdi.»
   - Açıklama: 'Ağzına verdi' yanlış fiil seçimi; 'ağzına tutturdu' ya da 'uzattı' olmalı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Karakaçan'ın ağzına verdi"
   - Cümle 8: «Dalın kuru ucunu Karakaçan'ın ağzına verdi.»
   - Açıklama: Bir şey ağza verilmez; 'ağzına tutturdu' ya da 'ağzına koydu' olmalı.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dalın kuru ucunu Karakaçan'ın ağzına verdi"
   - Cümle 8: «Dalın kuru ucunu Karakaçan'ın ağzına verdi.»
   - Açıklama: Eşek dalı ağzıyla tutabiliyorsa fırçayı da tutabilirdi; sorunla çözüm çelişiyor.
7. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "tabloya mavi noktalar sıçrattı"
   - Cümle 10: «Karakaçan başını salladı ve tabloya mavi noktalar sıçrattı.»
   - Açıklama: Kartın yanlar bölümünde eşeğe yalnız yük taşıma ve ıslıkla gelme verilmiş; boya yapma yeteneği kartta yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0173` birebir aynı, `@degisim: ucuz -> mavi` (tutuyorsan), ardından `@onarim: 00fb34353f1039df1919a6e49a32a6ed0f8fd5d7`, sonra gövde.
