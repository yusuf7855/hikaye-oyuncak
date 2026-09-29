# Editör görevi (onarım): Keloğlan, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0001 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0001
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'yiyecek', fiil 'basmak', sıfat 'dar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: taş duvardan ince bir ıslık sesi geldi | sesi arayıp rüzgarın dar delikten geçtiğini buldu
@tohum: keloglan-0001
Rüzgar esiyordu. Keloğlan şatonun bahçesinde oturmuş, yiyeceklerini yiyordu. Birden taş duvardan ince bir ıslık sesi geldi. Keloğlan yeni şeyler öğrenmeyi severdi. Bu sesin nereden geldiğini çok merak etti. Yumuşak otlara basarak duvara yürüdü. Taşların arasında dar bir delik vardı. Rüzgar esince ses bu delikten geliyordu. Keloğlan elini deliğin önüne koydu ve ses durdu. Elini çekince ıslık yine başladı. Keloğlan güldü. Sesi yapan rüzgardı! Keloğlan duvarın dibinde rüzgarı dinledi ve yiyeceklerini mutlu mutlu bitirdi.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "oturmuş, yiyeceklerini yiyordu"
   - Cümle 2: «Keloğlan şatonun bahçesinde oturmuş, yiyeceklerini yiyordu.»
   - Açıklama: 'Yiyeceklerini yiyordu' aynı kökü gereksiz yere tekrarlıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "taş duvardan ince bir ıslık sesi geldi"
   - Cümle 3: «Birden taş duvardan ince bir ıslık sesi geldi.»
   - Açıklama: Duvardan gelen ses kimseye zarar vermeyen bir merak konusu; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden taş duvardan ince bir ıslık sesi geldi"
   - Cümle 3: «Birden taş duvardan ince bir ıslık sesi geldi.»
   - Açıklama: Duvardan gelen ıslık sesi kimseye zarar vermeyen bir merak konusu; çocuğun önemseyeceği gerçek bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0001` birebir aynı, ardından `@onarim: 608f0bd425110d72975af045b4c19399b492c36f`, sonra gövde.

### Hikâye 2: tohum keloglan-0003 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0003
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sepet', fiil 'oturmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları örmeyi gördü
@tohum: keloglan-0003
Keloğlan ile Balkız tepede yumuşak otların üstüne oturdu. Keloğlan yeni şeyler öğrenmeyi severdi ve otlardan küçük bir sepet yapmak istedi. Uzun otları üst üste koydu, ama otlar hep dağıldı. Keloğlan bir daha denedi, yine olmadı. Sonra Balkız'a döndü ve ondan yardım istedi. Balkız bir otu alıp öbür otların arasından geçirdi. Keloğlan onun gibi yaptı ve otları sıkıca ördü. Otlar artık dağılmıyordu. Az sonra Keloğlan'ın elinde küçük bir sepet vardı. Balkız sepete sarı çiçekler koydu ve güldü. Keloğlan çok sevindi, çünkü Balkız'ın yardımıyla ilk sepetini yapmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "otları örmeyi gördü"
   - Cümle 0 (plan satırı): «otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları örmeyi gördü»
   - Açıklama: Plan satırı dilbilgisel olarak bozuk; 'örmeyi öğrendi' ya da 'nasıl örüldüğünü gördü' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve otları örmeyi gördü"
   - Cümle 0 (plan satırı): «otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları örmeyi gördü»
   - Açıklama: Plan satırında 'örmeyi gördü' yanlış fiil; 'örmeyi öğrendi' olmalı.
   - Açıklama: 'Örmeyi gördü' anlamca yanlış; 'örmeyi öğrendi' ya da 'nasıl ördüğünü gördü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0003` birebir aynı, ardından `@onarim: b0927836cbeb55b19ca6b730e9c98b510c2e5813`, sonra gövde.

### Hikâye 3: tohum keloglan-0004 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0004
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kemer', fiil 'getirmek', sıfat 'ıslak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kemer su birikintisine düştü ve ıslandı | kuru yapraklar getirip kemeri iyice sildi
@tohum: keloglan-0004
Bir sabah Keloğlan ormanda halka atma oyunu oynuyordu. Kemerinin iki ucunu birleştirip bir halka yapmıştı. Halkayı uzaktan küçük bir kütüğe atıyordu. Keloğlan biraz sakardı ve kemer elinden kaydı. Kemer bir su birikintisine düştü ve ıslandı. Keloğlan kemeri sudan aldı. Büyük ağaçların altından kuru yapraklar getirdi. Kemeri bu yapraklarla iyice sildi. Kemer artık ıslak değildi. Keloğlan kemeri yeniden kütüğe attı. Bu kez kemer tam kütüğün üstüne geçti! Keloğlan çok sevindi, çünkü halkayı sonunda kütüğe geçirmişti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Kemer bir su birikintisine düştü ve ıslandı"
   - Cümle 5: «Kemer bir su birikintisine düştü ve ıslandı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak beşinci cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kemer bir su birikintisine düştü ve ıslandı"
   - Cümle 5: «Kemer bir su birikintisine düştü ve ıslandı.»
   - Açıklama: Islak kemer halka atmayı engellemez; sorun önemsiz ve çözümü oyunla ilgisiz.
   - Açıklama: Kemerin ıslanması halka atma oyununu engellemiyor, sorun önemsiz kalıyor.
   - Açıklama: Islak kemer yine halka olarak atılabilir; sorun oyunu engellemeyen önemsiz bir olay.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 5. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0004` birebir aynı, ardından `@onarim: 175b9964c4b30df4a3eb839c79d28a25bca730a9`, sonra gövde.

### Hikâye 4: tohum keloglan-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0005
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kumaş', fiil 'güzelleştirmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: böğürtlen suyu kumaşa döküldü ve leke oldu | yaprakları suya batırıp lekenin çevresine bastı
@tohum: keloglan-0005
Ormanda büyük ağaçların altı serindi. Keloğlan yanına beyaz bir kumaş getirmişti. Bugün ilk kez yapraklarla kumaşa resim yapmayı deneyecekti. Tatlı böğürtlenleri bir taşın üstünde ezdi. Taşta mor bir su oldu. Keloğlan biraz sakardı ve eli taşa çarptı. Mor su kumaşın ortasına döküldü. Kumaşta büyük, yuvarlak bir leke oldu. Keloğlan lekeye baktı ve düşündü. Sonra yaprakları mor suya batırdı. Onları lekenin çevresine tek tek bastı. Leke kocaman bir çiçeğin ortası oldu. Keloğlan kumaşı mor bir çiçekle güzelleştirdi. Keloğlan çok sevindi, çünkü leke güzel bir çiçeğe dönmüştü.
```

**Hakem bulguları (8):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Bugün ilk kez yapraklarla"
   - Cümle 3: «Bugün ilk kez yapraklarla kumaşa resim yapmayı deneyecekti.»
   - Açıklama: Geçmiş anlatımda 'Bugün' şimdiki zamana kayıyor; 'O gün' olmalı.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "eli taşa çarptı"
   - Cümle 6: «Keloğlan biraz sakardı ve eli taşa çarptı.»
   - Açıklama: Sakarlık elin taşa çarpmasıyla gösteriliyor; bu acı ya da incinme çağrıştırıyor ve güvenli özellik kullanımı satırı kimsenin incinmemesini istiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve eli taşa çarptı"
   - Cümle 6: «Keloğlan biraz sakardı ve eli taşa çarptı.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak izin verir; burada el taşa çarpıyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Mor su kumaşın ortasına döküldü"
   - Cümle 7: «Mor su kumaşın ortasına döküldü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak yedinci cümlede ortaya çıkıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Leke kocaman bir çiçeğin ortası oldu"
   - Cümle 12: «Leke kocaman bir çiçeğin ortası oldu.»
   - Açıklama: Lekenin çiçeğe dönmesi 13-15. cümlelerde üç kez tekrarlanıyor.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan kumaşı mor bir çiçekle güzelleştirdi"
   - Cümle 13: «Keloğlan kumaşı mor bir çiçekle güzelleştirdi.»
   - Açıklama: Lekenin çiçeğe dönüşmesi 12., 13. ve 14. cümlelerde üç kez tekrar ediliyor.
   - Açıklama: Lekenin çiçeğe döndüğü art arda üç cümlede tekrar ediliyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "leke güzel bir çiçeğe dönmüştü"
   - Cümle 14: «Keloğlan çok sevindi, çünkü leke güzel bir çiçeğe dönmüştü.»
   - Açıklama: 'Dönmek' burada yanlış; 'dönüşmüştü' ya da 'benzemişti' olmalı.
8. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Açıklama: Leke sorunu ancak 7. ve 8. cümlede ortaya çıkıyor, ilk üç cümlede söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0005` birebir aynı, ardından `@onarim: a7afb35187e8bd59ffe3a093a5546594fe056678`, sonra gövde.

### Hikâye 5: tohum keloglan-0008 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0008
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'patates', fiil 'yakalamak', sıfat 'tedbirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: patates hızlı yuvarlandı ve çiçekleri dağıttı | özür diledi ve çiçekleri yeniden dizdi
@tohum: keloglan-0008
Şatonun bahçesinde Keloğlan ile Balkız patates oyunu oynuyordu. Balkız'ın çiçekleri çimlerin üstünde sıra sıra duruyordu. Keloğlan bakmadan patatesi çok hızlı yuvarladı ve patates çiçeklere çarptı. Çiçekler çimlere dağıldı. Balkız çiçeklere üzgün üzgün baktı. Keloğlan dürüst bir çocuktu ve hemen yanına gitti. "Özür dilerim, Balkız, patatesi çok hızlı yuvarladım," dedi Keloğlan. Sonra çiçekleri tek tek topladı ve yeniden dizdi. "Teşekkürler, Keloğlan, çiçekler yine çok güzel," dedi Balkız. Oyuna döndüler ve Balkız patatesi kolayca yakaladı. Keloğlan bundan sonra patatesle oynarken daha tedbirli oldu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "patates çiçeklere çarptı"
   - Cümle 3: «Keloğlan bakmadan patatesi çok hızlı yuvarladı ve patates çiçeklere çarptı.»
   - Açıklama: Çiçekler dağılıyor, toplanıyor ve bitiyor; sorun 'dağıldı, topladı, bitti' kalıbında önemsiz bir olay.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çiçekler çimlere dağıldı"
   - Cümle 4: «Çiçekler çimlere dağıldı.»
   - Açıklama: Çimlere dizilmiş çiçeklerin dağılıp yeniden dizilmesi, 'dağıttı, topladı, bitti' türünden önemsiz bir sorun.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "daha tedbirli oldu"
   - Cümle 11: «Keloğlan bundan sonra patatesle oynarken daha tedbirli oldu.»
   - Açıklama: 'Tedbirli' soyut ve 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Tedbirli' soyut bir kelime ve 3 yaşındaki bir çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "oynarken daha tedbirli oldu"
   - Cümle 11: «Keloğlan bundan sonra patatesle oynarken daha tedbirli oldu.»
   - Açıklama: 'Tedbirli' soyut bir kelime ve 3 yaşındaki bir çocuk bilmez.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "patatesle oynarken daha tedbirli oldu"
   - Cümle 11: «Keloğlan bundan sonra patatesle oynarken daha tedbirli oldu.»
   - Açıklama: Tohumdaki özellik dürüstlük; tedbirlilik karttaki özellik alanında olmayan ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0008` birebir aynı, ardından `@onarim: 4b803186cb4fde410cb7d88ed7c83beb5e2d1599`, sonra gövde.

### Hikâye 6: tohum keloglan-0009 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0009
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'trompet', fiil 'eğilmek', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: rüzgar açık pencereden esti ve yaprakları dağıttı | pencereyi kapattı ve yaprakları yeniden topladı
@tohum: keloglan-0009
@degisim: trompet -> çiçek
Keloğlan annesine bir sürpriz hazırlıyordu. Anası mutfakta yemek yapıyordu. Keloğlan masaya çiçek yapraklarıyla büyük bir kalp yaptı. Ama pencere açıktı ve rüzgar yaprakları yere uçurdu. Keloğlan önce pencereyi kapattı. Sonra eğildi ve yaprakları yerden tek tek topladı. Yapraklar çoktu, ama Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı. Kalbi masada yeniden yaptı. Tam o sırada anası içeri girdi. "Bu kalp benim için mi?" diye sordu anası. "Evet, anneciğim, senin için yaptım!" dedi Keloğlan. Anası Keloğlan'a sıkıca sarıldı. Keloğlan çok sevindi, çünkü sürprizi annesini mutlu etmişti.
```

**Hakem bulguları (7):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama pencere açıktı ve rüzgar"
   - Cümle 4: «Ama pencere açıktı ve rüzgar yaprakları yere uçurdu.»
   - Açıklama: Sorun ilk 3 cümlede değil ancak 4. cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar yaprakları yere uçurdu"
   - Cümle 4: «Ama pencere açıktı ve rüzgar yaprakları yere uçurdu.»
   - Açıklama: Rüzgarın yaprakları dağıtıp toplanması istemde önemsiz sayılan örnekle aynı türden bir sorun.
   - Açıklama: Rüzgarın yaprakları dağıtıp yeniden toplanması önemsiz, kalıplaşmış bir sorun.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 7: «Yapraklar çoktu, ama Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı.»
   - Açıklama: Yaprakları toplamanın dürüstlükle ilgisi yok; 'dürüst' kelimesi bu bağlamda yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' yaprakları toplamayı sürdürmekle ilgili değil; kelime yanlış anlamda kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 7: «Yapraklar çoktu, ama Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı.»
   - Açıklama: 'Azimli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 7: «Yapraklar çoktu, ama Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı.»
   - Açıklama: Dürüstlük olayda hiçbir işlev görmeyen bir ayrıntı.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kalbi masada yeniden yaptı"
   - Cümle 8: «Kalbi masada yeniden yaptı.»
   - Açıklama: Çözüm pencereyi kapatma, yaprakları toplama ve kalbi yeniden yapma olarak ikiden fazla adım sürüyor.
7. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0009` birebir aynı, `@degisim: trompet -> çiçek` (tutuyorsan), ardından `@onarim: eb66c0334af2f956d9bf0c9a34c40834b1cfb0b9`, sonra gövde.

### Hikâye 7: tohum keloglan-0010 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0010
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'odun', fiil 'süpürmek', sıfat 'kırık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: kırık dal yaprakları toplamıyordu | eşeğin kuyruğuna bakıp dallardan bir demet yaptı
@tohum: keloglan-0010
@degisim: odun -> yaprak
Bir sabah Keloğlan ile eşeği Karakaçan ormanda oyun oynuyordu. Keloğlan yapraklardan büyük bir yığın yapıp içine atlamak istedi. Ama elinde yalnız kırık bir dal vardı ve dal yaprakları toplamıyordu. Keloğlan yeni şeyler öğrenmeyi severdi ve etrafına baktı. Karakaçan kuyruğunu sallıyordu. Kuyruk yerdeki yaprakları bir yana itiyordu. Keloğlan ince dallardan kuyruk gibi bir demet yaptı. Demeti tuttu ve yaprakları kolayca süpürdü. "Bak, Karakaçan, senin kuyruğun gibi!" dedi Keloğlan. Karakaçan başını salladı. Az sonra büyük bir yaprak yığını oldu. Keloğlan yığına atladı ve yapraklar havaya uçtu. Keloğlan çok sevindi, çünkü oyunları çok eğlenceli olmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kırık dal yaprakları toplamıyordu"
   - Cümle 0 (plan satırı): «kırık dal yaprakları toplamıyordu | eşeğin kuyruğuna bakıp dallardan bir demet yaptı»
   - Açıklama: Dal kendi başına yaprak toplamaz; fiil öznesine uymuyor.
   - Açıklama: Plan satırında da dal yaprak toplayan özne olarak kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dal yaprakları toplamıyordu"
   - Cümle 3: «Ama elinde yalnız kırık bir dal vardı ve dal yaprakları toplamıyordu.»
   - Açıklama: Dal yaprak toplamaz; 'dalla yaprakları toplayamıyordu' gibi olmalı.
   - Açıklama: Dal kendi başına yaprak toplamaz; fiil öznesine uymuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "dal yaprakları toplamıyordu"
   - Cümle 3: «Ama elinde yalnız kırık bir dal vardı ve dal yaprakları toplamıyordu.»
   - Açıklama: Kırık dalın neden yaprak toplamadığı söylenmiyor ve Keloğlan yaprakları eliyle de toplayabilecekken sorun zorlama duruyor.
   - Açıklama: Keloğlan yaprakları eliyle de toplayabileceği için kırık dalın işe yaramaması akla yatkın bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0010` birebir aynı, `@degisim: odun -> yaprak` (tutuyorsan), ardından `@onarim: 5e424f9a92b68fdc503c9038dfb9417fafe1d313`, sonra gövde.

### Hikâye 8: tohum keloglan-0011 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0011
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tarak', fiil 'yeşillenmek', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin tarağı yolda cebinden düştü | aramayı bırakmadı ve tarağı bulup dedeye verdi
@tohum: keloglan-0011
Keloğlan ormanda Bilgecan Dede ile yürüyordu. Büyük ağaçlar yeni yeşillenmişti. Birden Dede durdu ve cebine baktı. Tahta tarağı cebinden düşmüştü. "Keloğlan, tarağı birlikte arayalım mı?" diye sordu Bilgecan Dede. Keloğlan yerdeki yeşil otlara baktı, ama tarak görünmüyordu. Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı. Yolda biraz geri yürüdü ve her yere baktı. Büyük bir ağacın dibinde tarağı buldu. Tarağı koşarak Dede'ye götürdü. "Teşekkür ederim, Keloğlan, ne nazik bir çocuksun," dedi Bilgecan Dede. Dede tarağı cebine koydu ve gülümsedi. Sonra Keloğlan ile Bilgecan Dede ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Tahta tarağı cebinden düşmüştü"
   - Cümle 4: «Tahta tarağı cebinden düşmüştü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 7: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler 3 yaşındaki çocuğa uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Açıklama: Tarağın düştüğü ancak 4. cümlede söyleniyor; ilk 3 cümlede sorun açıkça yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0011` birebir aynı, ardından `@onarim: d9dbc3950365004292710f5d4747777c1e911f08`, sonra gövde.
