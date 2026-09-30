# Editör görevi (onarım): Maşa, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar36.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0106 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0106
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'saat', fiil 'tamamlamak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: sincap yapbozun son parçasını fındık sandı ve kaçtı | yardım isteyip sincaba bir fındık verdi
@tohum: masa-0106
@degisim: saat -> yapboz
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa meyveli bir ağacın yapbozunu yapıyordu. Son parça küçük, yuvarlak ve kahverengiydi. Bir sincap onu fındık sandı ve kapıp kaçtı. Sincap sonra bir taşın üstüne oturdu. Parça olmadan yapboz bitmiyordu ve Maşa üzüldü. Maşa'nın cebinde hiç fındık yoktu, bu yüzden Daşa'dan yardım istedi. Daşa cebinden bir fındık çıkarıp Maşa'ya verdi. Maşa parçayı fındıkla değiştirmeyi denedi. Fındığı taşın yanına koydu. Sincap taştan indi, parçayı bıraktı ve fındığı aldı. Maşa son parçayı hemen yerine koydu ve yapbozu tamamladı. Daşa ile Maşa meyveli ağaca bakıp güldüler. Maşa bundan sonra zor bir işte hemen yardım istedi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Bir sincap onu fındık sandı ve kapıp kaçtı"
   - Cümle 4: «Bir sincap onu fındık sandı ve kapıp kaçtı.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor; ilk üç cümlede sorun yok.
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0106` birebir aynı, `@degisim: saat -> yapboz` (tutuyorsan), ardından `@onarim: 883d00911d56704cab92bd7fb20d214267aed75c`, sonra gövde.

### Hikâye 2: tohum masa-0112 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0112
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buz', fiil 'tamamlanmak', sıfat 'uykulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: reçel kavanozu kapının önünden kaybolmuştu | reçel damlalarını izledi ve kavanozu buldu
@tohum: masa-0112
@degisim: tamamlanmak -> damlamak
Soğuk bir rüzgar esiyordu. Maşa, Koca Ayı'nın bahçesinde oynarken reçel kavanozunu kapının önüne koymuştu. Ama geri döndüğünde kavanoz yerinde yoktu. Maşa kavanozu kimin aldığını çok merak etti. Kapının önüne kırmızı bir damla damlamıştı. Maşa eğilip kokladı ve kendi reçelini hemen tanıdı. Bahçedeki beyaz buzun üstünde başka kırmızı damlalar da vardı. Maşa damlaları izledi ve ağaç evin arkasına yürüdü. Orada uykulu Koca Ayı bir kütüğün üstünde oturuyordu. Kucağında reçel kavanozu, burnunda da reçel vardı. "Koca Ayı, reçelimi sen mi aldın?" diye sordu Maşa. Koca Ayı utandı ve kavanozu Maşa'ya uzattı. "Gel, Koca Ayı, kalanını birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kırmızı bir damla damlamıştı"
   - Cümle 5: «Kapının önüne kırmızı bir damla damlamıştı.»
   - Açıklama: 'Damla damlamıştı' gereksiz tekrar; 'kırmızı bir damla vardı' olmalı.
   - Açıklama: 'damla damlamıştı' gereksiz tekrar yapıyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Kucağında reçel kavanozu, burnunda da reçel vardı"
   - Cümle 10: «Kucağında reçel kavanozu, burnunda da reçel vardı.»
   - Açıklama: Kartın 'yanlar' alanında iyi kalpli dost olarak verilen Koca Ayı, Maşa'nın reçelini habersizce alan biri olarak gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0112` birebir aynı, `@degisim: tamamlanmak -> damlamak` (tutuyorsan), ardından `@onarim: f59d2010d2be24ceba771d3fda1ea815e2b16450`, sonra gövde.

### Hikâye 3: tohum masa-0114 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0114
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'zambak', fiil 'çizmek', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: rüzgar esti ve resim kağıdı uçtu | kağıdın köşesine reçel kavanozunu koydu
@tohum: masa-0114
Maşa ormanda resim oyunu oynuyordu ve bir zambak çizmek istiyordu. Kalemlerini ve sepetini beyaz bir zambağın yanına koydu, kağıdını da çimenlere serdi. Ama rüzgar esti ve kağıt havalanıp çalılara doğru uçtu. Maşa koştu ve kağıdı çalının dibinden aldı. Sonra sepetine baktı. Sepette en sevdiği yiyecek, bir kavanoz çilek reçeli vardı. Maşa reçel kavanozunu kağıdın bir köşesine koydu. Rüzgar yine esti ama kağıt bu kez yerinden kıpırdamadı. Maşa zambağın uzun sapını ve açık yapraklarını dikkatle çizdi. Resim çok güzel oldu ve tıpkı çiçeğe benzedi. Maşa oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçel kavanozunu kağıdın bir köşesine"
   - Cümle 7: «Maşa reçel kavanozunu kağıdın bir köşesine koydu.»
   - Açıklama: Tohumdaki reçel sevgisi işe yaramıyor; kavanoz yalnız ağırlık olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0114` birebir aynı, ardından `@onarim: a33066920eade0ccc12e2da998fc1cc1a1b16d45`, sonra gövde.

### Hikâye 4: tohum masa-0117 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi, Daşa
@tohum: masa-0117
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buket', fiil 'toplanmak', sıfat 'memnun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi, Daşa
@plan: reçel kavanozunun kapağı çok sıkıydı | kuzeninden yardım isteyip kapağı birlikte açtı
@tohum: masa-0117
@degisim: buket -> kavanoz
Bir sabah Maşa ile kirpi bahçede kahvaltı masasının başındaydı. Masada ekmek, elmalar ve bir kavanoz çilek reçeli vardı. Maşa ekmeğine reçel sürmek istedi, ama kavanozun kapağı çok sıkıydı. Tam o sırada kuzeni Daşa bahçeye geldi. "Daşa, kapak açılmıyor, bana yardım eder misin?" diye sordu Maşa. Daşa kavanozu sıkıca tuttu. Maşa kapağı çevirdi. Bu kez kapak "pıt" diye açıldı. Maşa ekmeğine bol bol reçel sürdü ve bir dilimi Daşa'ya verdi. Kirpiye de küçük bir elma verdi ve kirpi çok memnun oldu. Sonra üçü masada toplandı ve mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada kuzeni Daşa bahçeye geldi"
   - Cümle 4: «Tam o sırada kuzeni Daşa bahçeye geldi.»
   - Açıklama: Çözümü getiren Daşa tam gereken anda sebepsizce beliriyor.
   - Açıklama: Yardım edecek karakter tam gereken anda sebepsizce beliriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kirpi çok memnun oldu"
   - Cümle 10: «Kirpiye de küçük bir elma verdi ve kirpi çok memnun oldu.»
   - Açıklama: 'Memnun' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime; 'sevindi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0117` birebir aynı, `@degisim: buket -> kavanoz` (tutuyorsan), ardından `@onarim: 99d0f6ae257c62226b609377d4669e02be751019`, sonra gövde.

### Hikâye 5: tohum masa-0118 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0118
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'iplik', fiil 'yakalanmak', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: uçurtmanın ipliği bahçedeki bir çalıya takıldı | çekmeyi bırakıp ipliği dallardan yavaşça çözdü
@tohum: masa-0118
@degisim: kırılgan -> ince
Bahçede rüzgar esiyordu. Maşa ince çubuklardan yapılmış bir uçurtma uçuruyordu. Birden uçurtma dönen rüzgara yakalandı ve ipliği bir çalıya takıldı. Maşa ipliği çekti ama uçurtma çalıdan çıkmadı. Çubuklar eğildi ve kırılacak gibi oldu. Maşa hemen durdu ve çekmek yerine çözmeyi denedi. Çalının yanına yürüdü ve ipliği dallardan tek tek çözdü. Sonra uçurtmayı iki eliyle yavaşça dışarı aldı. Çubukların hiçbiri kırılmamıştı. Maşa bahçenin ortasına koştu ve uçurtmayı yeniden havaya kaldırdı. Uçurtma rüzgarla yükseldi ve Maşa sevinçle güldü. Maşa bundan sonra uçurtmasını hep çalılardan uzakta uçurdu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uçurtma dönen rüzgara yakalandı"
   - Cümle 3: «Birden uçurtma dönen rüzgara yakalandı ve ipliği bir çalıya takıldı.»
   - Açıklama: 'Dönen rüzgara yakalanmak' mecazlı bir anlatım, küçük çocuk için anlaşılmaz.
   - Açıklama: 'rüzgara yakalanmak' mecazlı bir anlatım ve 'dönen rüzgar' 3 yaşındaki çocuğa açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0118` birebir aynı, `@degisim: kırılgan -> ince` (tutuyorsan), ardından `@onarim: 3263ac32684dca2673dae244eefbb0a24acaaea6`, sonra gövde.

### Hikâye 6: tohum masa-0120 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0120
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'küp', fiil 'doldurmak', sıfat 'açık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: patikadaki çilekler yeşildi | güneşli açık yeri fark edip kırmızı çilek topladı
@tohum: masa-0120
Hafif bir rüzgar esiyordu ve güneş ormanı ısıtıyordu. Maşa elinde küçük bir küple patikada yürüyordu. Reçeli çok seven Maşa küpü çilekle doldurmak istedi, ama çilekler yeşildi. Maşa etrafa dikkatle baktı ve bir şey fark etti. Ağaçların altındaki çilekler yeşildi, ama güneşte olan çilekler kırmızıydı. Maşa ağaçların arasındaki açık bir yere koştu. Burası güneşliydi ve çimenlerde bir sürü kırmızı çilek vardı. Maşa bir kırmızı çileği tattı ve çilek reçel gibi tatlıydı. Maşa en kırmızı çilekleri tek tek topladı ve küpe koydu. Az sonra küp doldu. Maşa dolu küpü kucakladı ve mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa bir kırmızı çileği tattı"
   - Cümle 8: «Maşa bir kırmızı çileği tattı ve çilek reçel gibi tatlıydı.»
   - Açıklama: Ormanda bulunan yabani meyveyi toplayıp yemek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0120` birebir aynı, ardından `@onarim: cca53c0322890d86e93dfdddebc172e5d05105c5`, sonra gövde.

### Hikâye 7: tohum masa-0121 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0121
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: paylaşmak
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çekmece', fiil 'eğilmek', sıfat 'sarı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: ayının büyük elleri ince kalemleri tutamadı | çekmeceden kalın bir boya çıkarıp ayıya verdi
@tohum: masa-0121
Koca Ayı'nın ağaç evinde Maşa kalem kutusunu açıp resim yapıyordu. Maşa kalemlerini Koca Ayı ile paylaşmak istedi. Ama ayının kocaman elleri ince kalemleri tutamıyordu. Kalemler hep elinden kayıp yere düştü. Koca Ayı her seferinde yere eğildi ve kalemi aldı. Maşa hemen başka bir şey denedi. Kalem kutusunun küçük çekmecesini açtı ve içinden kalın bir mum boya çıkardı. Koca Ayı bu boyayı kolayca tuttu. Kağıda büyük, sarı bir güneş çizdi. Maşa da güneşin altına küçük bir ağaç ev çizdi. Koca Ayı resme baktı ve mutlulukla başını salladı. Maşa çok sevindi, çünkü artık ikisi birlikte resim yapıyordu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kağıda büyük, sarı bir güneş çizdi"
   - Cümle 9: «Kağıda büyük, sarı bir güneş çizdi.»
   - Açıklama: Kağıt kaybolmuştu ama Koca Ayı sonra kağıda resim çiziyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0121` birebir aynı, ardından `@onarim: 9fc9c222a85f3b9cd1299a1fc1bf54fd70d80735`, sonra gövde.

### Hikâye 8: tohum masa-0126 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0126
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'hediye', fiil 'saklamak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: ayı hediyeyi saklamak istedi ama kirpi hep peşindeydi | kozalak yuvarladı ve kirpiyle oynadı
@tohum: masa-0126
Bir sabah Maşa ormanda Koca Ayı'yı gördü. Koca Ayı'nın elinde kirpi için bir hediye vardı, kırmızı bir elma. Ayı elmayı saklayıp kirpiye sürpriz yapmak istiyordu, ama oynak kirpi hep peşindeydi. Koca Ayı durdu ve üzgün üzgün Maşa'ya baktı. Maşa hemen yeni bir oyun denedi. Yerden bir kozalak aldı ve patikada yavaşça yuvarladı. Kirpi sevinçle kozalağı kovaladı. O sırada Koca Ayı elmayı yaprakların altına sakladı. Biraz sonra kirpi geri geldi ve burnuyla yaprakları kokladı. Kırmızı elmayı buldu ve mutlu mutlu yemeye başladı. Koca Ayı da Maşa'ya sarıldı. Maşa bundan sonra Koca Ayı sürpriz hazırlarken ona hep böyle yardım etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kozalak yuvarladı ve kirpiyle oynadı"
   - Cümle 0 (plan satırı): «ayı hediyeyi saklamak istedi ama kirpi hep peşindeydi | kozalak yuvarladı ve kirpiyle oynadı»
   - Açıklama: Plan satırında öznesiz çözümün öznesi sorundaki 'ayı' gibi okunuyor, oysa kozalağı Maşa yuvarladı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Koca Ayı da Maşa'ya"
   - Cümle 11: «Koca Ayı da Maşa'ya sarıldı.»
   - Açıklama: 'da' başka birinin de sarıldığını anlatıyor ama başka kimse sarılmadı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0126` birebir aynı, ardından `@onarim: f60b916d72c048223b93a9994ff33f4d3f986e00`, sonra gövde.

### Hikâye 9: tohum masa-0127 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | sincap
@tohum: masa-0127
- yer: dağ (Ormanın yanındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'elmas', fiil 'asmak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap
@plan: fındıklar kuru ekmekten yere kaydı | ekmeğe reçel sürdü ve fındıkları yapıştırdı
@tohum: masa-0127
@degisim: elmas -> kurdele
Maşa tepede hareketli sincap için bir sürpriz hazırlıyordu. Bir dilim ekmeğin üstüne fındık koymak istedi. Ama ekmek kuruydu ve yuvarlak fındıklar hemen yere kaydı. Maşa fındıkları topladı ve biraz düşündü. Sonra çantasından sevdiği reçel kavanozunu çıkardı. Ekmeğe kalın bir kat reçel sürdü ve fındıkları üstüne bastırdı. Fındıklar bu kez yapıştı ve hiç düşmedi. Maşa, sincap ekmeği kolay bulsun diye yakındaki bir dala kırmızı kurdele astı. Sincap kurdeleyi görünce hemen ekmeğin yanına koştu. "Bu senin için, sincap!" dedi Maşa. Sincap fındıkları tek tek yedi ve kuyruğunu salladı. Maşa bundan sonra fındıkları ekmeğe hep reçelle yapıştırdı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ekmek kuruydu ve yuvarlak fındıklar hemen yere kaydı"
   - Cümle 3: «Ama ekmek kuruydu ve yuvarlak fındıklar hemen yere kaydı.»
   - Açıklama: Sincap fındıkları yerden de yiyebilir; fındıkların ekmekten kayması önemsiz, yapay bir sorun.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yakındaki bir dala kırmızı kurdele astı"
   - Cümle 8: «Maşa, sincap ekmeği kolay bulsun diye yakındaki bir dala kırmızı kurdele astı.»
   - Açıklama: Maşa sincabın yanındayken kurdele gereksiz; sorunla ilgisi olmayan işlevsiz bir ek olay.
   - Açıklama: Kurdele sebepsiz beliriyor ve sorundan çıkmayan yeni bir iş ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0127` birebir aynı, `@degisim: elmas -> kurdele` (tutuyorsan), ardından `@onarim: 3f7a40f159349d89bd724e48b5b9c62b08c0a193`, sonra gövde.

### Hikâye 10: tohum masa-0129 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0129
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'topaç', fiil 'kopmak', sıfat 'ıslak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: kopan bir dal sincabın yuvasını kapattı | ipi dala bağladı ve dalı birlikte çektiler
@tohum: masa-0129
Bir sabah Maşa ile kuzeni Daşa ormanda topaç çeviriyordu. Birden rüzgarda büyük bir dal koptu ve bir ağacın dibine düştü. Dal, bir sincabın yuvasının önünü kapattı ve sincap dışarı çıkamadı. Sincabın ıslak burnu dalın arkasından görünüyordu. Maşa ile Daşa dalı çekmeye çalıştı. "Dal çok kalın, ellerimle tutamıyorum," dedi Daşa. Maşa hemen yeni bir şey denedi. Cebinden topaç ipini çıkardı ve dalın ucuna sıkıca bağladı. İki kız ipi birlikte çekti ve dal yavaş yavaş kaydı. Yuvanın önü açıldı ve sincap zıplayarak dışarı çıktı. Sincap kuyruğunu salladı ve bir ağacın dalına koştu. "Yaşasın, Daşa, sincap artık dışarıda!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "rüzgarda büyük bir dal koptu"
   - Cümle 2: «Birden rüzgarda büyük bir dal koptu ve bir ağacın dibine düştü.»
   - Açıklama: Rüzgarda kopup düşen büyük dal ve yuvasında kapana kısılan sincap küçük çocuk için korkutucu olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0129` birebir aynı, ardından `@onarim: 621dcaaf4ce7b4f9b123ca1fc5372a340e6b9bcf`, sonra gövde.

### Hikâye 11: tohum masa-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0130
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şapka', fiil 'gitmek', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kız koşarken kelebekler uçup gitti | şapkaya çiçek koydu ve sessizce bekledi
@tohum: masa-0130
Maşa şapkasıyla ormandaki patikada yürüyordu. Birden küçük sarı kelebekler gördü ve onlara yakından bakmak istedi. Ama Maşa yanlarına koşarken kelebekler hemen uçup gitti. Maşa durdu ve yeni bir şey denedi. Patikanın kenarından birkaç çiçek topladı ve şapkasına koydu. Sonra şapkayı çimenlere bıraktı ve yanına sessizce oturdu. Maşa hiç kıpırdamadan bekledi. Biraz sonra şapkadaki çiçeklerin üstünde yine küçük kelebekler vardı. Maşa onları bu kez çok yakından gördü. Maşa kelebekleri uzun uzun izledi ve mutlu mutlu gülümsedi.
```

**Hakem bulguları (1):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kelebekler hemen uçup gitti"
   - Cümle 3: «Ama Maşa yanlarına koşarken kelebekler hemen uçup gitti.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün merkezinde olaya katılıyor.
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0130` birebir aynı, ardından `@onarim: 9d01a101342689ccbbe428e78824eb9d096fd675`, sonra gövde.

### Hikâye 12: tohum masa-0131 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0131
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fasulye', fiil 'planlamak', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: ayı ile kirpi aşağıda çiçek topluyordu ve bulutu görmedi | ekmeğe reçel sürdü ve onları tepeye çağırdı
@tohum: masa-0131
@degisim: fasulye -> çiçek
Maşa tepede, geniş ve ferah bir çimenlikte piknik yapıyordu. Birden gökyüzünde kalp şeklinde kocaman bir bulut fark etti. Ama Koca Ayı ile kirpi aşağıda çiçek topluyordu ve gökyüzüne hiç bakmıyordu. Maşa "Yukarı bakın!" diye seslendi, ama onlar duymadı. Maşa onları reçelli ekmekle yukarı çağırmayı planladı. Kavanozunu açtı ve üç dilim ekmeğe bol bol reçel sürdü. "Ekmekler hazır, haydi gelin!" dedi Maşa yüksek sesle. Koca Ayı çiçekleri bıraktı ve kirpiyle birlikte tepeye geldi. "Bakın, kalp şeklinde bir bulut!" dedi Maşa ve gökyüzünü gösterdi. Koca Ayı ile kirpi yukarı baktı ve sevinçle ses çıkardı. Üçü çimenlikte ekmeklerini yiyip bulutu mutlu mutlu izledi.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geniş ve ferah bir çimenlikte"
   - Cümle 1: «Maşa tepede, geniş ve ferah bir çimenlikte piknik yapıyordu.»
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yukarı çağırmayı planladı"
   - Cümle 5: «Maşa onları reçelli ekmekle yukarı çağırmayı planladı.»
   - Açıklama: 'Planlamak' soyut bir kelime, küçük çocuğa uygun değil.
   - Açıklama: 'Planlamak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "onları reçelli ekmekle yukarı çağırmayı planladı"
   - Cümle 5: «Maşa onları reçelli ekmekle yukarı çağırmayı planladı.»
   - Açıklama: Sorunun sebebi arkadaşların sesi duymaması; reçelli ekmek hazırlamak bu sebebe doğrudan yönelmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa onları reçelli ekmekle yukarı çağırmayı planladı"
   - Cümle 5: «Maşa onları reçelli ekmekle yukarı çağırmayı planladı.»
   - Açıklama: Bulut aşağıdan da görülebilirken çözüm dolambaçlı; ekmek hazırlayıp tepeye çağırmak sebebe (bakmamaları) doğrudan yönelmiyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "dedi Maşa yüksek sesle"
   - Cümle 7: «"Ekmekler hazır, haydi gelin!" dedi Maşa yüksek sesle.»
   - Açıklama: Az önce seslenişini duymayan arkadaşlar, aynı biçimdeki ikinci seslenişi hemen duyuyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ekmekler hazır, haydi gelin!"
   - Cümle 7: «"Ekmekler hazır, haydi gelin!" dedi Maşa yüksek sesle.»
   - Açıklama: Aşağıdakiler Maşa'nın ilk bağırışını duymuyor ama ikinci bağırışını sebepsizce duyuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0131` birebir aynı, `@degisim: fasulye -> çiçek` (tutuyorsan), ardından `@onarim: 463cc44d9d1bf819fe0710e347c3c50f0bdaffa7`, sonra gövde.
