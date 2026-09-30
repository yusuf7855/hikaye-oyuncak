# Editör görevi (onarım): Niloya, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0137
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'taş', fiil 'güvenmek', sıfat 'kırmızı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: yıldız için kırmızı taş gerekiyordu ama yerde yoktu | merakla etrafa bakıp kütüğün dibinde kırmızı taşlar buldu
@tohum: niloya-0137
@degisim: güvenmek -> kapatmak
Ormanda, fındık ağaçlarının altında, Niloya ile Mete oynuyordu. Niloya, Mete'ye taşlardan sürpriz bir yıldız yapmak istedi. Mete kırmızıyı çok severdi, ama yerde hiç kırmızı taş yoktu. "Gözlerini kapat, Mete, biraz bekle," dedi Niloya. Mete gözlerini kapattı ve bir ağaca yaslandı. Niloya merakla etrafta dolaştı. Yaprakların altına ve kütüklerin yanına baktı. Bir kütüğün dibinde küçük kırmızı taşlar buldu. Niloya bu taşlarla yere büyük bir yıldız yaptı. "Şimdi aç, Mete!" dedi Niloya. Mete yıldızı gördü ve sevinçle zıpladı. "Benim için mi, çok güzel!" dedi Mete. Niloya çok sevindi, çünkü Mete yıldızı sevmişti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yerde hiç kırmızı taş yoktu"
   - Cümle 3: «Mete kırmızıyı çok severdi, ama yerde hiç kırmızı taş yoktu.»
   - Açıklama: Yerde hiç kırmızı taş olmadığı söyleniyor ama az sonra kütüğün dibinde yerde kırmızı taşlar bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0137` birebir aynı, `@degisim: güvenmek -> kapatmak` (tutuyorsan), ardından `@onarim: 1714999545bb1952c643ba1bc8ee030f88598b51`, sonra gövde.

### Hikâye 2: tohum niloya-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0138
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'ucuz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: oyuncak bebeğin ayağındaki bağ açıldı | ağabeyinden yardım isteyip bağlamayı öğrendi
@tohum: niloya-0138
@degisim: ucuz -> yumuşak
Ormanda, fındık ağaçlarının altında, Niloya oyuncak bebeğiyle oynuyordu. Oyuncak bebeğin ayağında yumuşak, küçük patikler vardı. Birden patiklerden birinin bağı açıldı ve patik yere düştü. Niloya bağı bağlamaya çalıştı, ama fiyonk yapmayı bilmiyordu. "Abi, bana fiyonk yapmayı gösterir misin?" diye sordu Niloya. Murat hemen yanına oturdu. "Önce iki halka yap, sonra onları birbirine geçir," dedi Murat. Niloya patiği oyuncak bebeğin ayağına taktı, iki halka yaptı ve sıkıca bağladı. Artık patik hiç düşmedi. "Oldu, abiciğim!" dedi Niloya. Murat gülümsedi ve Niloya'nın başını okşadı. Niloya çok sevindi, çünkü fiyonk yapmayı öğrenmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bebeğin ayağında yumuşak, küçük patikler"
   - Cümle 2: «Oyuncak bebeğin ayağında yumuşak, küçük patikler vardı.»
   - Açıklama: Tek ayakta çoğul patik uyumsuz; 'ayaklarında' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0138` birebir aynı, `@degisim: ucuz -> yumuşak` (tutuyorsan), ardından `@onarim: 7a3cdd23462aa4e97228922fe88aea4801aa5650`, sonra gövde.

### Hikâye 3: tohum niloya-0139 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0139
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'yoğurt', fiil 'yorulmak', sıfat 'hareketli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: oyunda otların arasında kekiği tanıyamadı | kekiğin kokusunu düşündü ve otları kokladı
@tohum: niloya-0139
Dağda Niloya yemek oyunu oynuyordu. Yanında küçük bir kap yoğurt vardı ve üstüne kekik koyacaktı. Ama çimenlerde çok yeşil ot vardı ve Niloya kekiği tanıyamadı. Oyun çok hareketliydi ve Niloya otların arasında koşup yoruldu. Bir taşa oturdu ve bir soru düşündü: Kekiğin kokusu nasıldı? Niloya kekiğin güzel koktuğunu biliyordu. Yakındaki otları tek tek kokladı. Küçük yapraklı bir ot çok güzel kokuyordu. Bu kekikti! Niloya kekiği yoğurdun üstüne koydu ve yemeği hazır oldu. Niloya bundan sonra otları kokusundan tanıdı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyun çok hareketliydi ve Niloya otların arasında koşup yoruldu"
   - Cümle 4: «Oyun çok hareketliydi ve Niloya otların arasında koşup yoruldu.»
   - Açıklama: Yemek oyunu sırasında koşup yorulma sebepsiz ve işlevsiz bir ayrıntı.
   - Açıklama: Koşup yorulma olaydan çıkmıyor ve çözüme hiçbir katkı sağlamıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve bir soru düşündü"
   - Cümle 5: «Bir taşa oturdu ve bir soru düşündü: Kekiğin kokusu nasıldı?»
   - Açıklama: 'Soru düşünmek' doğal bir kullanım değil; 'kendine bir soru sordu' olmalı.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya kekiği yoğurdun üstüne koydu"
   - Cümle 10: «Niloya kekiği yoğurdun üstüne koydu ve yemeği hazır oldu.»
   - Açıklama: Çocuk dağdaki otları kokusundan tanıyıp bir büyüğe sormadan yiyeceğe katıyor; taklit edilince yabani bitki yeme tehlikesi var.
   - Açıklama: Çocuk büyüğe sormadan dağdaki bir otu yalnız kokusuyla tanıyıp yiyeceğe koyuyor; taklit edilince zehirli ot riski taşır.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve yemeği hazır oldu"
   - Cümle 10: «Niloya kekiği yoğurdun üstüne koydu ve yemeği hazır oldu.»
   - Açıklama: İyelik eki uyumsuz; 'yemek hazır oldu' ya da 'yemeğini hazırladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0139` birebir aynı, ardından `@onarim: f4e31db4fcfc050f69dabc73dc46dc75cd2bf208`, sonra gövde.

### Hikâye 4: tohum niloya-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0141
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kilit', fiil 'hatırlamak', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: koşarken sepete çarptı ve kekikler döküldü | özür diledi ve kayanın arkasında yeni kekik buldu
@tohum: niloya-0141
@degisim: kilit -> kapak
Niloya babaannesiyle dağda kekik topluyordu. Ama Niloya koşarken sepete çarptı ve kekikler yere döküldü. Kekiklerin çoğu ayağının altında ezildi. Babaannesi üzgün üzgün baktı. "Özür dilerim, babaanne, sepeti görmedim," dedi Niloya. "Olsun, güzel kızım," dedi babaannesi. Niloya koşarken gördüğü büyük kayayı hatırladı. Kayanın arkasına merakla baktı. Orada çok kekik vardı! "Babaanne, gel, burada çok kekik var!" dedi Niloya. İkisi sepeti hemen doldurdu. Babaannesi sepetin kapağını kapattı ve "Sepet hazır," dedi. Sonra ikisi mutlu mutlu kekik toplamaya devam etti.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya koşarken gördüğü büyük kayayı hatırladı"
   - Cümle 7: «Niloya koşarken gördüğü büyük kayayı hatırladı.»
   - Açıklama: Kaya önceden hiç kurulmadan çözümü getirmek için sebepsizce beliriyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "burada çok kekik var!"
   - Cümle 10: «"Babaanne, gel, burada çok kekik var!" dedi Niloya.»
   - Açıklama: Bir önceki cümledeki 'Orada çok kekik vardı!' bilgisi replikte gereksizce tekrarlanıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra ikisi mutlu mutlu kekik toplamaya devam etti"
   - Cümle 13: «Sonra ikisi mutlu mutlu kekik toplamaya devam etti.»
   - Açıklama: Sepet doldurulup kapağı kapatılmış ve hazır denmişken kekik toplamaya devam ediyorlar.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ikisi mutlu mutlu kekik toplamaya devam etti"
   - Cümle 13: «Sonra ikisi mutlu mutlu kekik toplamaya devam etti.»
   - Açıklama: Sepet doldurulup kapatılmış ve hazır denmişken kekik toplamaya devam ediyorlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0141` birebir aynı, `@degisim: kilit -> kapak` (tutuyorsan), ardından `@onarim: 5581d878b0eddab8da5c5f43c71d05cfa2119c20`, sonra gövde.

### Hikâye 5: tohum niloya-0142 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0142
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'armut', fiil 'saymak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: armutlar yaprakların arkasında kaldı | ağacın öbür tarafına gidip kalan armutları saydı
@tohum: niloya-0142
Ormanda Niloya çok yorgundu ve bir armut ağacının altına oturdu. Dallarda sarı armutlar vardı ve Niloya onları saymak istedi. Ama armutlar yaprakların arkasında kalıyordu. Niloya ancak beş armut görebildi. Sonra bir soru düşündü: Ağacın öbür tarafında da armut var mıydı? Biraz sonra kalktı ve ağacın öbür tarafına yürüdü. Oradan başka armutlar da görünüyordu. Niloya onları tek tek saydı. Orada yedi armut daha vardı! Ağaçta tam on iki armut vardı. Niloya çok sevindi, çünkü ağaçtaki bütün armutları bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra bir soru düşündü"
   - Cümle 5: «Sonra bir soru düşündü: Ağacın öbür tarafında da armut var mıydı?»
   - Açıklama: 'Soru düşünmek' doğal değil; 'aklına bir soru geldi' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra bir soru düşündü"
   - Cümle 5: «Sonra bir soru düşündü: Ağacın öbür tarafında da armut var mıydı?»
   - Açıklama: Kartın özellikler alanındaki 'sorar' özelliği kimseye soru sorulmadan yalnız içten düşünülen bir soruya indirgenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0142` birebir aynı, ardından `@onarim: 6f606d2aeff7056316778f457fb9b5a269ee6af2`, sonra gövde.

### Hikâye 6: tohum niloya-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0143
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'mürekkep', fiil 'seçmek', sıfat 'bomboş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: kağıt boştu çünkü hangi çiçeği çizeceğini bilmiyordu | şarkı söyleyip bir çiçek seçti
@tohum: niloya-0143
@degisim: mürekkep -> kalem
Dağda yeşil tepelerin üstünde kekik çiçekleri açmıştı. Niloya ile Mete çimenlere oturmuş, resim yapıyordu. Ama Mete'nin kağıdı bomboştu, çünkü hangi çiçeği çizeceğini bilmiyordu. "Hepsi çok güzel, ben hangisini çizeceğim?" diye sordu Mete. Niloya çiçeklere baktı. "Gel, bir şarkı söyleyip seçelim, Mete," dedi Niloya. Niloya şarkı söylerken sırayla çiçekleri gösterdi. Şarkı mor bir çiçekte bitti. "İşte senin çiçeğin!" dedi Niloya. Mete kalemini aldı ve mor çiçeği çizdi. "Teşekkürler, Niloya, çok güzel oldu!" dedi Mete. Niloya çok sevindi, çünkü Mete'ye yardım etmişti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kağıt boştu çünkü hangi çiçeği çizeceğini bilmiyordu"
   - Cümle 0 (plan satırı): «kağıt boştu çünkü hangi çiçeği çizeceğini bilmiyordu | şarkı söyleyip bir çiçek seçti»
   - Açıklama: Plan satırında 'bilmiyordu' fiilinin öznesi belli değil; kağıt bilmiyormuş gibi okunuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kağıt boştu çünkü hangi"
   - Cümle 0 (plan satırı): «kağıt boştu çünkü hangi çiçeği çizeceğini bilmiyordu | şarkı söyleyip bir çiçek seçti»
   - Açıklama: Plan satırında 'bilmiyordu' fiilinin öznesi belli değil; cümle kağıdın bilmediğini söylüyor gibi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0143` birebir aynı, `@degisim: mürekkep -> kalem` (tutuyorsan), ardından `@onarim: f2846d831478652f56f0eb2055fa90a0260468b3`, sonra gövde.

### Hikâye 7: tohum niloya-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Murat
@tohum: niloya-0144
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'dolap', fiil 'esnemek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | Murat
@plan: ağabeyi yeni uyandı ve topunu bulamadı | bir soru sordu ve topu dolapta buldu
@tohum: niloya-0144
Rüzgar hafifçe esiyordu. Niloya bahçede ağabeyi Murat'ı gördü. Murat top oynamak istiyordu ama topunu bulamıyordu. Murat yeni uyanmıştı ve uzun uzun esnedi. "Topumu nereye koydum, hiç hatırlamıyorum," dedi Murat. Niloya ona yardım etmek istedi. "Eve girince ilk nereye gittin?" diye sordu Niloya. Murat biraz düşündü. "Odama gittim ve dolabı açtım," dedi Murat. İkisi hemen odaya koştu. Dolap oyuncaklarla doluydu. Niloya kapağını temkinli bir şekilde açtı ve hiçbir oyuncak düşmedi. Kırmızı top en arkadaydı. Niloya topu çıkarıp ağabeyine verdi. "Teşekkürler, Niloya, şimdi bahçede birlikte oynayalım!" dedi Murat.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Murat yeni uyanmıştı ve uzun uzun esnedi"
   - Cümle 4: «Murat yeni uyanmıştı ve uzun uzun esnedi.»
   - Açıklama: Topun kaybolma sebebi söylenmiyor; yeni uyanmış olmak topun nerede olduğunu unutmayı açıklamıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Eve girince ilk nereye gittin?"
   - Cümle 7: «"Eve girince ilk nereye gittin?" diye sordu Niloya.»
   - Açıklama: Murat yeni uyanmışken ve bahçedeyken eve girdiği anın sorulması zaman sırasıyla çelişiyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "İkisi hemen odaya koştu"
   - Cümle 10: «İkisi hemen odaya koştu.»
   - Açıklama: Hikaye bahçede başlıyor ve odada bitiyor; sahne değişiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kapağını temkinli bir şekilde"
   - Cümle 12: «Niloya kapağını temkinli bir şekilde açtı ve hiçbir oyuncak düşmedi.»
   - Açıklama: 'Temkinli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya kapağını temkinli bir şekilde açtı ve hiçbir oyuncak düşmedi"
   - Cümle 12: «Niloya kapağını temkinli bir şekilde açtı ve hiçbir oyuncak düşmedi.»
   - Açıklama: Dolu dolap bir tehlike gibi kuruluyor ama hiçbir işe yaramıyor.
   - Açıklama: Oyuncakla dolu dolap bir tehlike gibi kuruluyor ama hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0144` birebir aynı, ardından `@onarim: 04f57bdea47c6532af2a97a6c78fdc3122483e85`, sonra gövde.

### Hikâye 8: tohum niloya-0145 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | dedesi
@tohum: niloya-0145
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'salatalık', fiil 'birikmek', sıfat 'zarif'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | dedesi
@plan: kaydırağın yanından garip bir ses geldi | dedesine yağmuru sordu ve damlayan suyu buldu
@tohum: niloya-0145
Bir sabah Niloya ile dedesi parktaki bankta oturuyordu. Dedesi ona dilim dilim salatalık verdi. Birden kaydırağın yanından "tıp, tıp" diye bir ses geldi. Niloya bu sesin ne olduğunu çok merak etti. "Dede, dün yağmur yağdı mı?" diye sordu Niloya. "Evet, çok yağdı," dedi dedesi. Niloya hemen anladı ve salatalığını bitirip kaydırağa koştu. Kaydırağın tepesinde yağmur suyu birikmişti. Su oradan yavaş yavaş aşağı damlıyordu. Her damla yerdeki suya düşünce "tıp" diye ses çıkarıyordu. Suyun üstünde küçük, zarif halkalar oluşuyordu. Dedesi de gelip baktı ve gülümsedi. Niloya çok sevindi, çünkü sesi yapan damlaları kendisi bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dedesi ona dilim dilim salatalık verdi"
   - Cümle 2: «Dedesi ona dilim dilim salatalık verdi.»
   - Açıklama: Salatalık olayda hiçbir işe yaramayan işlevsiz bir ayrıntı olarak kuruluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dede, dün yağmur yağdı mı"
   - Cümle 5: «"Dede, dün yağmur yağdı mı?" diye sordu Niloya.»
   - Açıklama: Niloya'nın sesi duyunca birden dünkü yağmuru sorması önceki olaydan çıkmıyor, çözüme sebepsiz bir sıçrama.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, zarif halkalar oluşuyordu"
   - Cümle 11: «Suyun üstünde küçük, zarif halkalar oluşuyordu.»
   - Açıklama: 'Zarif' kelimesini 3 yaşındaki bir çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, zarif halkalar"
   - Cümle 11: «Suyun üstünde küçük, zarif halkalar oluşuyordu.»
   - Açıklama: 'Zarif' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0145` birebir aynı, ardından `@onarim: 6ce37f0818a5c184fd6d45dcaa4b8ac95cf9a528`, sonra gövde.

### Hikâye 9: tohum niloya-0146 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0146
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'brokoli', fiil 'takmak', sıfat 'iyi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: babaannesi eşarbını koyduğu ağacı hatırlamadı | bir soru sordu ve taşın yanındaki ağacı buldu
@tohum: niloya-0146
@degisim: brokoli -> fındık
Niloya babaannesiyle ormanda fındık topluyordu. Hava sıcaktı ve babaannesi eşarbını alçak bir dala asmıştı. Sepet dolunca eşarbını almak istedi ama hangi ağaçta olduğunu hatırlamadı. Etraftaki ağaçlar birbirine çok benziyordu. "Babaanne, o ağacın yanında ne vardı?" diye sordu Niloya. "Dibinde büyük, gri bir taş vardı," dedi babaannesi. Niloya etrafa dikkatle baktı. İleride o taşı gördü ve oraya koştu. Taşın yanındaki ağacın dalında mavi eşarp duruyordu. Niloya eşarbı alıp babaannesine götürdü. Babaannesi eşarbını başına taktı ve Niloya'ya sarıldı. "Sağ ol, Niloya, sen çok iyi bir kızsın," dedi babaannesi. Niloya bundan sonra kaybolan bir şeyi ararken önce sorular sordu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sepet dolunca eşarbını almak istedi"
   - Cümle 3: «Sepet dolunca eşarbını almak istedi ama hangi ağaçta olduğunu hatırlamadı.»
   - Açıklama: Öznesiz cümlede eşarbı almak isteyenin babaanne mi Niloya mı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0146` birebir aynı, `@degisim: brokoli -> fındık` (tutuyorsan), ardından `@onarim: 797a847c183178da65bd12797f2c0febc0d85c63`, sonra gövde.

### Hikâye 10: tohum niloya-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0147
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'bluz', fiil 'birleştirmek', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: kulenin küçük topu hep kayıp düştü | büyük topun üstünü düz yaptı ve topları birleştirdi
@tohum: niloya-0147
@degisim: bluz -> eldiven
Bir sabah yaylaya kar yağmıştı. Niloya kıpkırmızı eldivenlerini giydi ve karda yürüdü. Niloya kardan bir kule yapmak istiyordu. Önce büyük bir kar topu yuvarladı. Sonra küçük bir top yapıp onun üstüne koydu. Ama küçük top her seferinde kayıp yere düştü. Niloya kendine bir soru sordu: Küçük top neden kayıyordu? Büyük topun üstü çok yuvarlaktı. Niloya onun üstüne elleriyle bastırdı ve düz yaptı. Sonra iki topu sıkıca birleştirdi. Bu kez küçük top hiç kaymadı ve kule bitti. Niloya bundan sonra kule yaparken önce büyük topun üstünü düz yaptı.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Bir sabah yaylaya kar yağmıştı"
   - Cümle 1: «Bir sabah yaylaya kar yağmıştı.»
   - Açıklama: Kartın dağ tarifi kekik toplanan yeşil tepeler diyor; karla kaplı yayla bu tarife uymuyor.
   - Açıklama: Kartın dağ tarifi kekik toplanan yeşil tepeler der; karla kaplı yayla bu tarife tam uymuyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama küçük top her seferinde kayıp yere düştü"
   - Cümle 6: «Ama küçük top her seferinde kayıp yere düştü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak altıncı cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "küçük top her seferinde kayıp yere düştü"
   - Cümle 6: «Ama küçük top her seferinde kayıp yere düştü.»
   - Açıklama: Sorun ilk 3 cümlede değil ancak 6. cümlede söyleniyor.
4. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya kendine bir soru sordu"
   - Cümle 7: «Niloya kendine bir soru sordu: Küçük top neden kayıyordu?»
   - Açıklama: Niloya kendi kendine soru soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0147` birebir aynı, `@degisim: bluz -> eldiven` (tutuyorsan), ardından `@onarim: bcbbe65c44a3e554b84700b85e7e57efabcdb528`, sonra gövde.

### Hikâye 11: tohum niloya-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | annesi
@tohum: niloya-0148
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'davul', fiil 'yağmak', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | annesi
@plan: tencerenin mavi kapağı yuvarlandı ve kayboldu | her köşeye baktı ve kapağı davulun arkasında buldu
@tohum: niloya-0148
Evin mutfağında annesi çorba yapıyordu. Dışarıda yağmur yağıyordu ve Niloya davul çalıyordu. Birden tencerenin mavi kapağı yere düştü ve yuvarlandı. Kapak bir yere gitti ve kayboldu. Annesi kapağı her yerde aradı ama bulamadı. Niloya davulu bıraktı ve merakla aramaya başladı. Önce dolabın altına, sonra sandalyelerin arkasına baktı. En son davulunun arkasına da baktı. Mavi kapak orada duruyordu. Niloya kapağı alıp annesine verdi. Annesi kapağı tencereye koydu ve Niloya'ya sarıldı. Niloya çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Evin mutfağında annesi çorba"
   - Cümle 1: «Evin mutfağında annesi çorba yapıyordu.»
   - Açıklama: Niloya tanıtılmadan 'annesi' geçiyor; kimin annesi olduğu belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Evin mutfağında annesi"
   - Cümle 1: «Evin mutfağında annesi çorba yapıyordu.»
   - Açıklama: 'annesi' iyelik eki, Niloya henüz anılmadan kullanılmış; kimin annesi olduğu belli değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tencerenin mavi kapağı yere düştü"
   - Cümle 3: «Birden tencerenin mavi kapağı yere düştü ve yuvarlandı.»
   - Açıklama: Kapağın neden düştüğü hiç söylenmiyor; sorunun sebebi yok.
   - Açıklama: Kapağın neden düştüğü söylenmiyor; sorun sebepsiz başlıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kapak bir yere gitti"
   - Cümle 4: «Kapak bir yere gitti ve kayboldu.»
   - Açıklama: Kapak kendi başına gitmez; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0148` birebir aynı, ardından `@onarim: 7b948c2563de6d818e25df4ba106d1d37c9a3297`, sonra gövde.

### Hikâye 12: tohum niloya-0150 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | annesi
@tohum: niloya-0150
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'fincan', fiil 'eğlenmek', sıfat 'kıvrımlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | annesi
@plan: annesi kek için fındık istedi ama ağaçların altı boştu | kıvrımlı bir yol buldu ve dolu bir ağaç gördü
@tohum: niloya-0150
Niloya annesiyle ormanda fındık arıyordu. Annesi kek yapmak için bir fincan dolusu istiyordu. Ama yakındaki ağaçların altı bomboştu. Niloya etrafa merakla baktı ve ileride kıvrımlı bir yol gördü. "Anne, gel, bu yolun sonuna bakalım," dedi Niloya. İkisi yolda birlikte yürüdü. Yolun sonunda büyük bir fındık ağacı vardı. Altı fındıkla doluydu. İkisi toplarken çok eğlendi. Fincan kısa sürede doldu. "Aferin, Niloya, kek için bu kadar yeter," dedi annesi. Niloya çok sevindi, çünkü o yolu kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakındaki ağaçların altı bomboştu"
   - Cümle 3: «Ama yakındaki ağaçların altı bomboştu.»
   - Açıklama: Ağaçların altının neden boş olduğu hiç söylenmiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yolun sonunda büyük bir fındık ağacı vardı"
   - Cümle 7: «Yolun sonunda büyük bir fındık ağacı vardı.»
   - Açıklama: Çözüm bir sebebe yönelmiyor; dolu ağaç şans eseri bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0150` birebir aynı, ardından `@onarim: 4267b9ad2cd0c849290947460b331786bc77be6e`, sonra gövde.
