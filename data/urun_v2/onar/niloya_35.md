# Editör görevi (onarım): Niloya, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Niloya | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar35.txt --ad urun_v2`
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

## Kart: Niloya (kaynaklı, kapalı dünya)

- Ad: Niloya (okunuş: niloya; kesme eki okunuşa uyar)
- Kimlik: Niloya, nehir kenarındaki bir köyde ailesiyle yaşayan küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Niloya'nın merakı bakarak, sorarak ve bir büyüğe haber vererek gösterilir; nehre ya da dereye girmez, suya yalnız kıyıdan bakar; ağaca ya da yüksek yere tırmanmaz.
- Özellikler:
  - keşfet: Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever. (örnek biçimler: merak etti, merakla, keşfetti)
  - soru: Merak ettiği her şeyi sorar. (örnek biçimler: sordu, soruyu, sorular)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
- Yerler:
  - orman: Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.
  - dağ: Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.
  - ev: Niloya'nın nehir kenarındaki köy evi ve bahçesi.
  - park: Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Murat: Niloya'nın ağabeyi; küçük kardeşi Niloya'yı çok sever. Tür: oğlan; konuşur; huy: Top oynamayı, koşturmayı ve fındık toplamayı sever.. Yüzey biçimleri: Murat, ağabey, ağabeyi, abi, abisi, abiciğim
  - Mete: Murat'ın en yakın arkadaşı; Niloya ile aynı yaştadır ve onun da arkadaşıdır. Tür: oğlan; konuşur; huy: Oyuncaklarını dağıtır, sonra aradığını bulamaz.. Yüzey biçimleri: Mete
  - Tospik: Niloya'nın kaplumbağası ve en yakın arkadaşı. Tür: kaplumbağa; konuşur; huy: Oyun oynamayı ve uyumayı sever; Niloya'ya yetişmekte zorlanır.. Yüzey biçimleri: Tospik, kaplumbağa, kaplumbağası
  - dedesi: Niloya'nın dedesi; herkese iyi öğütler verir. Tür: dede; konuşur. Yüzey biçimleri: dede, dedesi, dedeciğim, Dede
  - babaannesi: Niloya'nın babaannesi; yemek yapmayı ve fındık toplamayı sever. Tür: babaanne; konuşur. Yüzey biçimleri: babaanne, babaannesi, babaanneciğim, Babaanne, nine, ninesi
  - annesi: Niloya'nın annesi; yemek yapmayı, ekinleri ve yaylayı sever. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
- Dünya kuralları:
  - Niloya'nın ağabeyi Murat'tır. Mete Niloya'nın ağabeyi değildir; Murat'ın arkadaşıdır.
  - Tospik yavaştır; Niloya'ya yetişmekte zorlanır, hızla koşmaz.
  - Köy nehir kenarındadır; hikayede kimse nehre ya da dereye girmez, suya kıyıdan bakılır.
- Yasak adlar: Elif, Mine, Fatoş, Cem, Ayşecik, Sarıkanat, Miniş
- Yasak: Babası kartta yok; hikayeye girmez (kapalı dünya).
- İzinli dünya kelimeleri: köy, nehir, yayla, fındık, kaplumbağa, kekik

## Onarılacak hikâyeler

### Hikâye 1: tohum niloya-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Mete
@tohum: niloya-0151
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mete
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'yulaf', fiil 'aydınlatmak', sıfat 'faydalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | Mete
@plan: kavanozun kapağı sıkıydı ve açılmadı | arkadaşından kavanozu tutmasını istedi ve kapağı açtı
@tohum: niloya-0151
@degisim: faydalı -> sıkı
Niloya ile Mete mutfakta kahvaltı hazırlıyordu. Güneş mutfağı güzelce aydınlatıyordu. Niloya kaselere yulaf koymak istedi ama kavanozun kapağı çok sıkıydı. Niloya kapağı çevirdi ama kavanoz elinde döndü. "Mete, kavanozu tutar mısın?" diye sordu Niloya. "Tabii, sıkıca tutarım," dedi Mete. Mete kavanozu iki eliyle masada tuttu. Niloya kapağı bir kez daha çevirdi. Kapak bu kez açıldı. Niloya iki kaseye yulaf koydu ve üstüne süt döktü. İkisi masaya oturup yulaflarını yedi. Niloya çok sevindi, çünkü Mete'den yardım istemiş ve kapağı kolayca açmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "diye sordu Niloya"
   - Cümle 5: «"Mete, kavanozu tutar mısın?" diye sordu Niloya.»
   - Açıklama: Kartın özellikler alanındaki 'merak ettiği her şeyi sorar' özelliği merakla soru sormak yerine yalnız yardım istemek olarak kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0151` birebir aynı, `@degisim: faydalı -> sıkı` (tutuyorsan), ardından `@onarim: bc747c4ea792fd3a7c75ffc10d5311744ce078be`, sonra gövde.

### Hikâye 2: tohum niloya-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0152
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'değnek', fiil 'ulaşmak', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | -
@plan: kozalak bankın altında çok arkadaydı | eski bir değnek buldu ve kozalağı çekti
@tohum: niloya-0152
Bir sabah Niloya parkta yürüyordu. Bankın altında büyük, kahverengi bir kozalak gördü. Niloya onu çok beğendi ve almak istedi. Ama kozalak bankın en arkasındaydı ve eli ona ulaşmadı. Niloya etrafa merakla baktı. Parkta uzun bir şey aradı. Ağacın dibinde eski bir değnek buldu. Niloya değneği bankın altına uzattı. Kozalağı yavaşça kendine doğru çekti. Sonra onu eline aldı. Niloya kozalağı cebine koydu ve güldü. Niloya bundan sonra uzaktaki bir şeyi almak için değnek kullandı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bankın altında çok arkadaydı"
   - Cümle 0 (plan satırı): «kozalak bankın altında çok arkadaydı | eski bir değnek buldu ve kozalağı çekti»
   - Açıklama: 'Çok arkada' yanlış kullanım; 'en arkadaydı' olmalı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama kozalak bankın en arkasındaydı ve eli ona ulaşmadı.»
   - Açıklama: Kozalağa elin ulaşmaması sorunu ancak 4. cümlede söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra uzaktaki bir şeyi almak için değnek kullandı"
   - Cümle 12: «Niloya bundan sonra uzaktaki bir şeyi almak için değnek kullandı.»
   - Açıklama: 'Bundan sonra' süreklilik bildirir ama tekil 'bir şeyi ... kullandı' ile uyuşmuyor; 'uzaktaki şeyleri almak için hep değnek kullandı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0152` birebir aynı, ardından `@onarim: 557df4b542fe48a4ac0c093dca6a64859b41c3be`, sonra gövde.

### Hikâye 3: tohum niloya-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0153
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Murat
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'misket', fiil 'üzülmek', sıfat 'sabunlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: misket yaprakların arasında kayboldu | toprağın indiği yere baktı ve misketi buldu
@tohum: niloya-0153
@degisim: sabunlu -> yuvarlak
Ormanda Niloya ile Murat misket oynuyordu. İkisi sırayla atıyor ve çok eğleniyordu. Ama Murat mavi misketini hızlı atınca misket yaprakların arasında kayboldu. Murat üzüldü ve etrafa baktı ama onu bulamadı. Niloya yere merakla baktı. Toprak ileride biraz aşağı iniyordu. "Yuvarlak misket oraya gitmiş olmalı," dedi Niloya. Niloya oradaki yaprakları tek tek kaldırıp baktı. Bir taşın yanında mavi misket duruyordu. Niloya misketi alıp ağabeyine verdi. "Buldun, Niloya, teşekkürler!" dedi Murat. Sonra ikisi fındık ağaçlarının altında oyuna gülerek devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "toprağın indiği yere baktı"
   - Cümle 0 (plan satırı): «misket yaprakların arasında kayboldu | toprağın indiği yere baktı ve misketi buldu»
   - Açıklama: Toprak inmez; eğim için 'yerin alçaldığı' ya da 'yokuşun' gibi bir anlatım gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0153` birebir aynı, `@degisim: sabunlu -> yuvarlak` (tutuyorsan), ardından `@onarim: 4432b049d41e8aa29400ae7405b388843a242c29`, sonra gövde.

### Hikâye 4: tohum niloya-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0154
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'top', fiil 'inanmak', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: topu atıp tutmak istedi ama top düştü | şarkı söyleyerek topu yavaşça attı ve tuttu
@tohum: niloya-0154
Niloya ormanda dedesiyle top oynuyordu. Niloya dedesine büyük bir top gösterisi yapıyormuş gibi oynadı. Topu beş kez havaya atıp tutacaktı. Ama acele ediyordu ve top her seferinde yere düşüyordu. "Dede, bana inan, bu kez tutacağım," dedi Niloya. Sonra en sevdiği özel şarkısını söylemeye başladı. Şarkının her sözünde topu yavaşça havaya attı. Niloya bir, iki, üç, dört, beş diye saydı ve hepsini tuttu. Dedesi ellerini çırptı. "Harika bir gösteriydi, Niloya!" dedi dedesi. Niloya bundan sonra topu atıp tutarken hep şarkı söyledi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir top gösterisi yapıyormuş gibi oynadı"
   - Cümle 2: «Niloya dedesine büyük bir top gösterisi yapıyormuş gibi oynadı.»
   - Açıklama: 'gösterisi yapıyormuş gibi oynadı' soyut ve 3 yaşındaki çocuk için anlaşılması zor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Topu beş kez havaya atıp tutacaktı.»
   - Açıklama: Sorun (topun acele yüzünden düşmesi) ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0154` birebir aynı, ardından `@onarim: 2db96a0e47024c23fe0f1fe74d999dd0abac3375`, sonra gövde.

### Hikâye 5: tohum niloya-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0156
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'tablo', fiil 'yaklaşmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar kağıdı sallıyordu ve resim yapamadı | rüzgarın geldiği yere bakıp büyük bir kayanın arkasına oturdu
@tohum: niloya-0156
@degisim: dürüst -> büyük
Rüzgar tepede hızlı hızlı esiyordu. Niloya orada güzel bir tablo yapmak istiyordu. Kağıdına aşağıdaki köyü çizecekti. Ama rüzgar kağıdı sallıyordu ve Niloya düzgün çizemiyordu. Niloya bir soru düşündü: Bu hava nereden geliyordu? Otlara baktı. Bütün otlar aynı yana eğiliyordu. Rüzgar karşıdaki tepeden esiyordu. Niloya yakındaki büyük bir kayaya yaklaştı. Kayanın öbür yanına oturdu. Orada rüzgar yoktu ve kağıt hiç kıpırdamadı. Niloya köyü, nehri ve evleri rahatça çizdi. Niloya bundan sonra rüzgarlı günlerde resmini büyük bir kayanın arkasında yaptı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "rüzgar kağıdı sallıyordu ve resim yapamadı"
   - Cümle 0 (plan satırı): «rüzgar kağıdı sallıyordu ve resim yapamadı | rüzgarın geldiği yere bakıp büyük bir kayanın arkasına oturdu»
   - Açıklama: Bağlı iki yüklemin öznesi rüzgar görünüyor; resim yapamayan kişi dilbilgisel olarak belirtilmemiş.
   - Açıklama: İkinci yüklemin öznesi rüzgar gibi okunuyor; özne uyumu bozuk.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güzel bir tablo yapmak"
   - Cümle 2: «Niloya orada güzel bir tablo yapmak istiyordu.»
   - Açıklama: Kağıda çizilen resim için 'tablo' kelimesi uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar kağıdı sallıyordu"
   - Cümle 4: «Ama rüzgar kağıdı sallıyordu ve Niloya düzgün çizemiyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu hava nereden geliyordu"
   - Cümle 5: «Niloya bir soru düşündü: Bu hava nereden geliyordu?»
   - Açıklama: Rüzgar yerine 'hava' kullanılmış; kelime doğru anlamda değil.
   - Açıklama: Rüzgar yerine 'hava' kelimesi yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0156` birebir aynı, `@degisim: dürüst -> büyük` (tutuyorsan), ardından `@onarim: 7a2a773916e7c3c027b8f35049253792d6605364`, sonra gövde.

### Hikâye 6: tohum niloya-0157 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0157
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yeni bir şeyi denemek
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çim', fiil 'hazırlanmak', sıfat 'parlak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağa hızlı dansa yetişemedi | yavaş bir şarkı söyleyip adımlarını yavaşlattı
@tohum: niloya-0157
Bahçede kuşlar ötüyordu. Parlak güneşin altında Niloya ile Tospik çimlerin üstünde oturuyordu. "Tospik, yeni bir oyun deneyelim mi? Birlikte dans edelim!" dedi Niloya. Tospik hemen dansa hazırlandı. Niloya hızlı hızlı zıpladı ve döndü. Ama Tospik ona yetişemedi ve durdu. "Çok hızlısın, Niloya," dedi Tospik. Niloya biraz düşündü. Sonra yavaş bir şarkı söylemeye başladı. Adımlarını da şarkıya göre yavaşlattı. Tospik bu kez Niloya'ya kolayca yetişti ve sallandı. İkisi şarkı bitene kadar bahçede mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kaplumbağa hızlı dansa yetişemedi"
   - Cümle 0 (plan satırı): «kaplumbağa hızlı dansa yetişemedi | yavaş bir şarkı söyleyip adımlarını yavaşlattı»
   - Açıklama: 'Dansa yetişemedi' dansa geç kalmak anlamına gelir; 'Niloya'ya yetişemedi' kastediliyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «"Tospik, yeni bir oyun deneyelim mi?»
   - Açıklama: Sorun ilk üç cümlede söylenmiyor, Tospik'in yetişememesi ancak altıncı cümlede geliyor.
   - Açıklama: Sorun ilk üç cümlede söylenmiyor; Tospik'in dansa yetişememesi ancak altıncı cümlede geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0157` birebir aynı, ardından `@onarim: 2c61ab45547b3ddc6e5f74fb74cf2c4af0261d22`, sonra gövde.

### Hikâye 7: tohum niloya-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0160
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'etiket', fiil 'doldurmak', sıfat 'keyifli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: fındıklar yüksek dallarda kaldı | şarkı söyleyerek abisini yardıma çağırdı
@tohum: niloya-0160
@degisim: etiket -> sepet
Ormanda fındık ağaçlarının altı serin ve keyifliydi. Niloya sepetini fındıkla doldurmak istiyordu. Ama yerdeki fındıklar bitmişti ve dallar çok yüksekteydi. Murat biraz ileride top oynuyordu. "Abiciğim, abiciğim, gel bana yardım et!" diye şarkı söyledi Niloya. Murat bu sesi duyunca güldü ve koşarak geldi. "Fındıklar yukarıda kaldı, Murat," dedi Niloya. Murat alçak bir dalı tuttu ve yavaşça salladı. Fındıklar yere pıt pıt düştü. Niloya hepsini tek tek topladı ve sepet doldu. Niloya ile Murat dolu sepetin yanına oturup fındıkları mutlu mutlu saydı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "altı serin ve keyifliydi"
   - Cümle 1: «Ormanda fındık ağaçlarının altı serin ve keyifliydi.»
   - Açıklama: Bir yerin 'keyifli' olması soyut bir niteleme, küçük çocuğa uygun değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Murat alçak bir dalı tuttu"
   - Cümle 8: «Murat alçak bir dalı tuttu ve yavaşça salladı.»
   - Açıklama: Dalların çok yüksekte olduğu söylenip ardından alçak bir dalın sallanması çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0160` birebir aynı, `@degisim: etiket -> sepet` (tutuyorsan), ardından `@onarim: 644c8c7a6e94dc417e4a47d591ddf87a83a4c27a`, sonra gövde.

### Hikâye 8: tohum niloya-0161 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0161
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'eşarp', fiil 'ışıldamak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: parkta şarkıyı tekrar eden minicik bir ses duydu | sesin kaydıraktan gelen kendi sesi olduğunu buldu
@tohum: niloya-0161
@degisim: eşarp -> kaydırak
Niloya parkta salıncakta sallanıyordu. Güneş kapalı kaydırağın üstünde ışıldıyordu. Niloya en sevdiği şarkıyı söyledi. Birden minicik bir ses onun şarkısını tekrarladı. Niloya çok merak etti ve salıncaktan indi. Ses kaydırak tarafından geliyordu. Niloya kapalı kaydırağın ağzına gitti ve bir kez daha söyledi. Minicik ses bu kez kaydırağın içinden geldi. Niloya içeri baktı ama orada kimse yoktu. Kaydırak onun kendi sesini geri veriyordu. Niloya kaydırağın önünde ellerini çırptı ve sesiyle mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Birden minicik bir ses onun şarkısını tekrarladı.»
   - Açıklama: Sorun olan minicik ses ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya çok merak etti"
   - Cümle 5: «Niloya çok merak etti ve salıncaktan indi.»
   - Açıklama: Tohumdaki özellik şarkı; kartın ozellikler alanındaki merak/keşfet ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0161` birebir aynı, `@degisim: eşarp -> kaydırak` (tutuyorsan), ardından `@onarim: 055b983cdc86f6e930cad420066adb6014b3efe3`, sonra gövde.

### Hikâye 9: tohum niloya-0162 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | dedesi
@tohum: niloya-0162
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'beşik', fiil 'yeşillenmek', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | dedesi
@plan: oyuncak beşik saksıya çarptı ve saksı devrildi | dedesinden özür diledi ve ne yapacağını sordu
@tohum: niloya-0162
@degisim: kararlı -> küçük
Niloya bahçede oyuncak beşiği ile oynuyordu. Yanında dedesinin küçük saksısı duruyordu. Saksıdaki toprak yeni yeşillendi. Niloya beşiği hızlı hızlı salladı ve beşik saksıya çarptı. Saksı devrildi ve toprak yere döküldü. Dedesi hemen yanına geldi. "Dedeciğim, özür dilerim. Şimdi ne yapalım?" diye sordu Niloya. "Toprağı geri koyalım ve biraz su verelim," dedi dedesi. Niloya toprağı elleriyle saksıya doldurdu. Filizleri toprağa yavaşça yerleştirdi. Sonra onları suladı. Filizler yeniden dik durdu. Niloya çok sevindi, çünkü dedesinin saksısı yine yeşildi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya bahçede oyuncak beşiği ile oynuyordu"
   - Cümle 1: «Niloya bahçede oyuncak beşiği ile oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Saksıdaki toprak yeni yeşillendi"
   - Cümle 3: «Saksıdaki toprak yeni yeşillendi.»
   - Açıklama: Arka plan bilgisi '-mişti' ile verilmeliydi; 'yeni yeşillendi' zaman kaymasıdır.
   - Açıklama: Arka plan durumu için -mişti gerekirken -dı kullanılmış; 'yeni yeşillenmişti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0162` birebir aynı, `@degisim: kararlı -> küçük` (tutuyorsan), ardından `@onarim: 6138225b07b2a11f33e70cc5660b99096e674483`, sonra gövde.

### Hikâye 10: tohum niloya-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0163
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'mermer', fiil 'korumak', sıfat 'büyük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: alttaki küçük taşlar yüzünden kale hep yıkıldı | büyük bir mermer taşı en alta koydu
@tohum: niloya-0163
Tepede kuşlar ötüyordu. Niloya orada kale oyunu oynuyordu. Önce taşlardan bir kale yapacak, sonra onu koruyacaktı. Ama altta küçük taşlar vardı ve kale hep yıkılıyordu. Niloya kaleye baktı ve bir soru düşündü: Kale neden duramıyordu? Alttaki taşlar küçük ve yuvarlaktı. Üstteki taşları hiç tutamıyordu. Niloya otların arasında büyük, düz bir mermer taşı buldu. Onu kalenin en altına koydu. Küçük taşları da üstüne dizdi. Kale bu kez yıkılmadı. Niloya kalesinin önüne oturdu ve onu korudu. Niloya bundan sonra kale yaparken büyük taşları hep en alta koydu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kaleye baktı ve bir soru düşündü"
   - Cümle 5: «Niloya kaleye baktı ve bir soru düşündü: Kale neden duramıyordu?»
   - Açıklama: 'Bir soru düşünmek' doğal bir kullanım değil; 'kendine sordu' ya da 'merak etti' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "baktı ve bir soru düşündü"
   - Cümle 5: «Niloya kaleye baktı ve bir soru düşündü: Kale neden duramıyordu?»
   - Açıklama: 'Soru düşünmek' doğru bir kullanım değil; 'kendine sordu' ya da 'merak etti' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir soru düşündü"
   - Cümle 5: «Niloya kaleye baktı ve bir soru düşündü: Kale neden duramıyordu?»
   - Açıklama: Kartın özellikler alanında Niloya merak ettiğini sorar; burada kimseye sormuyor, yalnız içinden düşünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0163` birebir aynı, ardından `@onarim: 8053d263a24b0adb0520924a88683ce0420ccb7b`, sonra gövde.

### Hikâye 11: tohum niloya-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | annesi
@tohum: niloya-0164
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'basamak', fiil 'utanmak', sıfat 'rahat'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | annesi
@plan: son basamak çok yüksekti ve çıkamadı | annesinden yardım istedi
@tohum: niloya-0164
Bir sabah Niloya ile annesi ormanda fındık topluyordu. Niloya ağaçların arasına merakla baktı ve dar bir yol buldu. Yolda yukarı giden taş basamaklar vardı. Niloya ilk basamakları kolayca çıktı. Ama son basamak çok yüksekti ve Niloya ona yetişemedi. Niloya yardım istemekten biraz utandı. Sonra annesine döndü. "Anneciğim, bana elini verir misin?" diye sordu Niloya. Annesi yanına geldi ve elini uzattı. Niloya o eli tuttu ve son basamağa rahatça çıktı. Yukarıda fındık dolu büyük bir ağaç vardı. Niloya çok sevindi, çünkü annesinin yardımıyla bu güzel yeri bulmuştu.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "son basamak çok yüksekti ve çıkamadı"
   - Cümle 0 (plan satırı): «son basamak çok yüksekti ve çıkamadı | annesinden yardım istedi»
   - Açıklama: Plan satırında 've' ile bağlanan 'çıkamadı' fiilinin öznesi 'basamak' gibi okunuyor; özne uyumu bozuk.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "yukarı giden taş basamaklar"
   - Cümle 3: «Yolda yukarı giden taş basamaklar vardı.»
   - Açıklama: Kartın orman tarifi meyve ve fındık ağaçlarıyla sınırlı; taş basamaklı yol tarifte yok.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Yolda yukarı giden taş basamaklar vardı.»
   - Açıklama: Sorun ancak 5. cümlede ortaya çıkıyor; ilk üç cümle fındık toplama ve yol bulmayı anlatıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya ilk basamakları kolayca çıktı"
   - Cümle 4: «Niloya ilk basamakları kolayca çıktı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Niloya yüksek yere tırmanmaz, ama yukarı giden basamakları tırmanıyor.
   - Açıklama: Güvenli kullanım satırına göre Niloya yüksek yere tırmanmaz, burada annesinden ayrılıp yukarı giden taş basamaklara tek başına çıkıyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama son basamak çok yüksekti"
   - Cümle 5: «Ama son basamak çok yüksekti ve Niloya ona yetişemedi.»
   - Açıklama: Sorun ancak beşinci cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0164` birebir aynı, ardından `@onarim: a0eb67fd2247ec2a1c8f4ab7fce5ae825251e45b`, sonra gövde.

### Hikâye 12: tohum niloya-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0165
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'resim', fiil 'kaplamak', sıfat 'gizli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: ağabeyinin resim yapacak kağıdı yoktu | kağıdını ikiye bölüp ağabeyiyle paylaştı
@tohum: niloya-0165
@degisim: kaplamak -> boyamak
Niloya ormanda, fındık ağacının altındaki gizli köşede resim yapıyordu. Murat da gelip yanına oturdu ama hiç kağıdı yoktu. Murat onun resmine bakıp sessizce bekledi. "Abi, sen de resim yapmak ister misin?" diye sordu Niloya. "Çok isterim ama kağıdım yok," dedi Murat. Niloya büyük kağıdına baktı. Kağıdı ikiye katladı ve dikkatle yırttı. "Yarısı senin, abi," dedi Niloya. Kalemlerini de ortaya koydu. Murat fındık ağaçlarını yeşile boyadı. Niloya da kırmızı elmaları boyadı. İkisi resimlerini bitirip birbirine mutlu mutlu gösterdi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen de resim yapmak ister misin"
   - Cümle 4: «"Abi, sen de resim yapmak ister misin?" diye sordu Niloya.»
   - Açıklama: Tohumdaki özellik merak ettiğini sormak iken buradaki soru merak değil bir teklif ve sorunu çözen şey soru değil paylaşmak; özellik karttaki gibi işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0165` birebir aynı, `@degisim: kaplamak -> boyamak` (tutuyorsan), ardından `@onarim: 2cdea887d6c39d696fa59a70ae700d82a5d93ec5`, sonra gövde.
