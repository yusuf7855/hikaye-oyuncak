# Editör görevi (onarım): Niloya, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0022 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Tospik
@tohum: niloya-0022
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'sebze', fiil 'sıkmak', sıfat 'küçük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | Tospik
@plan: kaplumbağa havucun peşinden gidip kaydırağın altında sıkıştı | sesi duyunca eğildi ve onu yavaşça geri çekti
@tohum: niloya-0022
@degisim: sıkmak -> sıkışmak
Parkta Niloya, Tospik'e küçük sebze parçaları veriyordu. Bir havuç parçası yere düştü ve kaydırağın alçak ucunun altına yuvarlandı. Tospik onun peşinden girdi ama orada sıkıştı. Birden ince bir ses duyuldu. Niloya merakla eğildi ve baktı. Tospik'in kabuğu kaydırakla yer arasında kalmıştı. "Çıkamıyorum, Niloya!" dedi Tospik. "Sana yardım edeceğim, Tospik," dedi Niloya. Niloya kabuğu iki eliyle tuttu ve Tospik'i yavaşça geri çekti. Tospik kolayca dışarı çıktı. Niloya havuç parçasını da buldu ve ona verdi. Tospik havucu afiyetle yedi ve ikisi parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "girdi ama orada sıkıştı"
   - Cümle 3: «Tospik onun peşinden girdi ama orada sıkıştı.»
   - Açıklama: Kaplumbağanın kaydırağın altında sıkışıp çıkamaması küçük çocuk için ürkütücü bir öğe.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Tospik onun peşinden girdi ama orada sıkıştı"
   - Cümle 3: «Tospik onun peşinden girdi ama orada sıkıştı.»
   - Açıklama: Kaydırağın altında sıkışıp çıkamayan kaplumbağa küçük çocuk için ürkütücü olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0022` birebir aynı, `@degisim: sıkmak -> sıkışmak` (tutuyorsan), ardından `@onarim: d3126b909265ae1d427f3e1010c2def93bcd5de6`, sonra gövde.

### Hikâye 2: tohum niloya-0024 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0024
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'teneke', fiil 'şaşırtmak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: boş kutuya elle vurunca ses zayıf çıktı | dedesine sordu ve kuru çubuklarla vurdu
@tohum: niloya-0024
Bir sabah Niloya ile dedesi yeşil tepede meyveli kurabiyeleri bitirdi. Niloya boş teneke kutudan bir davul yapmak istedi. Ama eliyle vurunca kutu çok zayıf bir ses çıkardı. Niloya kutuya neyle vurabileceğini dedesine sordu. Dedesi ona kuru bir çubukla vurmasını söyledi. Niloya çimenlerin arasında iki kuru çubuk buldu. Önce kutunun kapağını sıkıca kapattı. Sonra çubuklarla kutuya sırayla vurdu. Tepede güçlü ve neşeli bir ses yayıldı. Bu ses ikisini de çok şaşırttı. Dedesi gülerek ellerini çırptı. Niloya davulunu çalarak tepede yürüdü. Niloya çok sevindi, çünkü kendi davulunu yapmıştı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce kutunun kapağını sıkıca kapattı"
   - Cümle 7: «Önce kutunun kapağını sıkıca kapattı.»
   - Açıklama: Kapağı kapatmak zayıf sesin sebebine (elle vurma) yönelmeyen fazladan bir adım ve çözümü ikiden fazla adıma çıkarıyor.
   - Açıklama: Kurulmamış kapak kapatma adımı çözüme gereksiz üçüncü bir adım ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0024` birebir aynı, ardından `@onarim: 812f31391dc4104a0c2c67b78677cc797d62377f`, sonra gövde.

### Hikâye 3: tohum niloya-0026 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0026
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'tabure', fiil 'uyumak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: ağaçların arasından garip bir ses geliyordu | sesi izledi ve uyuyan babaannesini buldu
@tohum: niloya-0026
Ağaçların arasından garip bir ses geliyordu. Niloya fındık toplamayı bıraktı ve sesi dinledi. Sesin nereden geldiğini bulmak istedi. Sesi izleyerek büyük bir fındık ağacına yürüdü. Ağacın arkasına baktı ve güldü. Babaannesi fındık toplarken oturduğu küçük taburede uyuyordu. Garip ses ondan geliyordu. Yanındaki sepette kremalı bir kek vardı. Niloya onu yavaşça uyandırmak için tatlı bir şarkı söyledi. Babaannesi gözlerini açtı ve Niloya'ya gülümsedi. İkisi keki birlikte yedi. Sonra fındık toplamaya mutlu mutlu devam ettiler.
```

**Hakem bulguları (6):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "garip bir ses geliyordu"
   - Cümle 1: «Ağaçların arasından garip bir ses geliyordu.»
   - Açıklama: Hikaye ağaçların arasından gelen garip bir sesle gerilimli ve ürkütücü açılıyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Ağaçların arasından garip bir ses geliyordu"
   - Cümle 1: «Ağaçların arasından garip bir ses geliyordu.»
   - Açıklama: Ormanda kaynağı bilinmeyen garip ses küçük çocuk için ürkütücü bir öğe olabilir.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sesi izleyerek büyük bir fındık ağacına yürüdü"
   - Cümle 4: «Sesi izleyerek büyük bir fındık ağacına yürüdü.»
   - Açıklama: Güvenli kullanım satırı merakın bir büyüğe haber vererek gösterilmesini istiyor; Niloya ormanda garip bir sesi tek başına izliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanındaki sepette kremalı bir kek vardı"
   - Cümle 8: «Yanındaki sepette kremalı bir kek vardı.»
   - Açıklama: Kek sebepsiz beliriyor ve sorunla ilgisi yok.
   - Açıklama: Kek sebepsiz beliriyor ve sorunla ilgisi olmadan yalnız sonda yeniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "için tatlı bir şarkı"
   - Cümle 9: «Niloya onu yavaşça uyandırmak için tatlı bir şarkı söyledi.»
   - Açıklama: 'Tatlı şarkı' mecaz bir kullanım.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Niloya onu yavaşça uyandırmak"
   - Cümle 9: «Niloya onu yavaşça uyandırmak için tatlı bir şarkı söyledi.»
   - Açıklama: 'Onu' zamiri bir önceki cümledeki keki gösteriyor gibi duruyor, babaanne olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0026` birebir aynı, ardından `@onarim: e9faea314d3b592e0d949fd030b7168dfd4baf06`, sonra gövde.

### Hikâye 4: tohum niloya-0027 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0027
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'perde', fiil 'ıslanmak', sıfat 'boş'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yağmur başladı ama şapkası yolda bir dala takılmıştı | şarkısını yeniden söyleyip geldiği yoldan geri yürüdü
@tohum: niloya-0027
@degisim: perde -> şapka
Niloya boş sepetiyle fındık ağaçlarına yürüyordu. Hafif bir yağmur başladı ve Niloya şapkasını aradı. Ama şapka başında yoktu, yolda bir dala takılmıştı. Niloya buraya gelirken en sevdiği şarkıyı söylemişti. Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü. Böylece nereden geçtiğini kolayca hatırladı. Şarkının sonunda alçak bir dalın altına geldi. Sarı şapkası o dalın ucunda sallanıyordu. Niloya elini uzattı ve şapkasını aldı. Onu hemen başına taktı ve yağmurda ıslanmadı. Sonra boş sepetini fındıkla doldurmaya başladı. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Böylece nereden geçtiğini kolayca hatırladı"
   - Cümle 6: «Böylece nereden geçtiğini kolayca hatırladı.»
   - Açıklama: Şarkı söylemenin yolu hatırlatması çözümü sebepsizce getiriyor; geri yürümek zaten yeterli.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra boş sepetini fındıkla doldurmaya başladı"
   - Cümle 11: «Sonra boş sepetini fındıkla doldurmaya başladı.»
   - Açıklama: Niloya fındık ağaçlarından geri yürüyüp yoldaki dala dönmüşken fındık toplamaya sebepsizce başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0027` birebir aynı, `@degisim: perde -> şapka` (tutuyorsan), ardından `@onarim: 88aaf9eeeef0314c91aa437d8baba0630b9bdbe1`, sonra gövde.

### Hikâye 5: tohum niloya-0029 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | annesi
@tohum: niloya-0029
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: paylaşmak
- yan: annesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'muz', fiil 'boyamak', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | annesi
@plan: annesi çiti boyarken yorulmuş ve acıkmıştı | saklı muzunu onunla paylaştı ve şarkı söyledi
@tohum: niloya-0029
Bahçede rüzgar hafif hafif esiyordu. Niloya, annesinin çiti boyamasını izliyordu. Annesi çok çalışmıştı, bu yüzden yorulmuş ve acıkmıştı. Niloya'nın mutfakta saklı bir muzu vardı. Niloya koştu, muzu getirdi ve ikiye böldü. "Al, anne, yarısı senin," dedi Niloya. "Teşekkürler, kızım, sen çok tatlısın," dedi annesi. İkisi çitin önüne oturdu ve muzu yedi. Niloya annesi için neşeli bir şarkı da söyledi. Annesi şarkıyı dinledi ve keyifle güldü. Sonra fırçayı yeniden eline aldı. Niloya bundan sonra sevdiği yiyecekleri annesiyle paylaştı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede rüzgar hafif hafif esiyordu"
   - Cümle 1: «Bahçede rüzgar hafif hafif esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bitiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sen çok tatlısın"
   - Cümle 7: «"Teşekkürler, kızım, sen çok tatlısın," dedi annesi.»
   - Açıklama: 'Tatlı' insan için mecaz anlamda kullanılmış.
   - Açıklama: Kişi için 'tatlı' mecazlı bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0029` birebir aynı, ardından `@onarim: 87de413f6f16b947b7e959c1274f9d46cfdda95e`, sonra gövde.

### Hikâye 6: tohum niloya-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0031
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kızak', fiil 'katılmak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: rüzgar ağabeyinin sepetindeki kekikleri uçurdu | kendi kekiklerinin yarısını ona verdi
@tohum: niloya-0031
@degisim: kızak -> sepet
Niloya ile Murat yeşil tepede kekik topluyordu. Birden güçlü bir rüzgar esti ve Murat'ın sepeti devrildi. Sepetteki kekikler rüzgarla uçup gitti. Murat boş sepetine baktı ve üzüldü. Niloya kendi dolu sepetine baktı. Sonra kekiklerinin yarısını Murat'ın sepetine koydu. "Al, abi, yarısı senin," dedi Niloya. "Sen çok yardımseversin, Niloya!" dedi Murat. Sonra Niloya neşeli bir şarkı söylemeye başladı. Murat da hemen ona katıldı. İkisi birlikte yeni kekikler topladı ve az sonra iki sepet de doldu. Niloya ile Murat tepede mutlu mutlu şarkı söylemeye devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Niloya neşeli bir şarkı söylemeye başladı"
   - Cümle 9: «Sonra Niloya neşeli bir şarkı söylemeye başladı.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümünde işe yaramıyor, çözüm yalnız paylaşmakla geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Niloya neşeli bir şarkı söylemeye başladı"
   - Cümle 9: «Sonra Niloya neşeli bir şarkı söylemeye başladı.»
   - Açıklama: Şarkı sorunla ilgisiz, sonradan eklenmiş işlevsiz bir ayrıntı ve ardından gelen yeni toplama verilen yarı kekiği gereksiz kılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0031` birebir aynı, `@degisim: kızak -> sepet` (tutuyorsan), ardından `@onarim: f40cdb0327d72da7f15e841885a7f2cd04dbdd9b`, sonra gövde.
