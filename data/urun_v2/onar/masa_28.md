# Editör görevi (onarım): Maşa, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0105
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'simit', fiil 'boyamak', sıfat 'nazik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi simidi yemedi çünkü elmayı severdi | simidi alıp üstüne elma reçeli sürdü
@tohum: masa-0105
@degisim: boyamak -> sürmek
Bir sabah Maşa ormanda yemek oyunu oynuyordu. Koca Ayı bir kütüğün üstüne iki simit koydu. Ama kirpi simidi kokladı ve yemedi, çünkü o elmayı severdi. Maşa bir an düşündü. Sonra kendi reçel kavanozunu açtı. Bir simidi alıp üstüne kalın kalın elma reçeli sürdü. "Buyur, kirpi, bu simit artık elmalı!" dedi Maşa nazik bir sesle. Kirpi hemen bir ısırık aldı ve burnunu oynattı. Koca Ayı sevinçle ellerini çırptı. Maşa da güldü ve üçü oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kendi reçel kavanozunu açtı"
   - Cümle 5: «Sonra kendi reçel kavanozunu açtı.»
   - Açıklama: Reçel kavanozu daha önce kurulmadan çözümü getirmek için sebepsizce beliriyor.
   - Açıklama: Reçel kavanozu önceden kurulmadan çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0105` birebir aynı, `@degisim: boyamak -> sürmek` (tutuyorsan), ardından `@onarim: f19c5c8f996fd8d6a4b54e60f17aae4429c52a47`, sonra gövde.

### Hikâye 2: tohum masa-0106 (deneme 1 -> 2)

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
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa orada meyveli bir ağacın yapbozunu yapıyordu. Ama bir sincap son parçayı fındık sandı ve kapıp kaçtı. Sincap sonra bir taşın üstüne oturdu. Parça olmadan yapboz bitmiyordu ve Maşa üzüldü. Maşa'nın cebinde hiç fındık yoktu, bu yüzden Daşa'dan yardım istedi. Daşa cebinden bir fındık çıkarıp Maşa'ya verdi. Maşa fındığı taşın yanına koymayı denedi. Sincap taştan indi, parçayı bıraktı ve fındığı aldı. Maşa son parçayı hemen yerine koydu ve yapbozu tamamladı. Daşa ile Maşa meyveli ağaca bakıp güldüler. Maşa bundan sonra zor bir işte hemen yardım istedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taşın yanına koymayı denedi"
   - Cümle 8: «Maşa fındığı taşın yanına koymayı denedi.»
   - Açıklama: 'Koymayı denedi' yanlış fiil seçimi; fındığı koymak zor bir iş değil, 'koydu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fındığı taşın yanına koymayı denedi"
   - Cümle 8: «Maşa fındığı taşın yanına koymayı denedi.»
   - Açıklama: Fındığı koymak denenecek bir iş değil; 'denedi' fiili yersiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0106` birebir aynı, `@degisim: saat -> yapboz` (tutuyorsan), ardından `@onarim: bc4b2c1de112b5b985e5caab3c45493bb459586f`, sonra gövde.

### Hikâye 3: tohum masa-0107 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0107
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'file', fiil 'uçuşmak', sıfat 'mükemmel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: sepetin altındaki delikten yapraklar düşüyordu | deliğin üstüne büyük bir yaprak koydu
@tohum: masa-0107
@degisim: file -> sepet
Maşa ormanda rüzgarla uçuşan yaprakları bir sepetle yakalıyordu. Kirpi de onun yanında yürüyordu. Ama sepetin altında küçük bir delik vardı ve yapraklar delikten düşüyordu. Düşen yapraklar hep kirpiye takıldı ve kirpi yeşil bir top gibi oldu. Maşa kirpiye baktı ve güldü. "Bak, kirpi, sen de yaprak topluyorsun!" dedi Maşa. Sonra Maşa deliği kapatmayı denedi. Deliğin üstüne büyük bir yaprak koydu. Yeni bir yaprak yakaladı ve bu kez yaprak sepette kaldı. Maşa kirpiye takılan yaprakları da yavaşça alıp sepete koydu. Kirpi sevinçle burnunu oynattı. "Bu oyun mükemmel oldu, kirpi!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sepetin altında küçük bir delik vardı"
   - Cümle 3: «Ama sepetin altında küçük bir delik vardı ve yapraklar delikten düşüyordu.»
   - Açıklama: Rüzgarda uçuşan yaprakları yakalama oyunundaki delik çocuğun önemseyeceği bir sorun değil, önemsiz bir oyun aksaklığı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu oyun mükemmel oldu"
   - Cümle 12: «"Bu oyun mükemmel oldu, kirpi!" dedi Maşa.»
   - Açıklama: 'mükemmel' 3 yaşındaki çocuğun bilmeyebileceği soyut bir değerlendirme kelimesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0107` birebir aynı, `@degisim: file -> sepet` (tutuyorsan), ardından `@onarim: bb3352ebf84876b2a3ee02b50312f81648b4e840`, sonra gövde.

### Hikâye 4: tohum masa-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0108
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'papatya', fiil 'havalanmak', sıfat 'minik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: kuyruk papatyalarla ağır olduğu için uçurtma uçmadı | yardım isteyip kuyrukta tek papatya bıraktı
@tohum: masa-0108
Bir sabah Maşa ile kuzeni Daşa tepede uçurtma uçurmaya çalışıyordu. Bir taşın üstündeki sincap da onlara bakıyordu. Ama uçurtma yerden kalkmadı, çünkü kuyruğu papatyalarla çok ağırdı. Maşa hızlı hızlı koştu ama uçurtma yine yere düştü. "Daşa, bana yardım eder misin?" diye sordu Maşa. Daşa uçurtmanın kuyruğuna dikkatlice baktı. "Papatyaları çıkar, yalnız minik bir tane bırak," dedi Daşa. Maşa bunu hemen denedi ve yeniden koştu. Bu kez uçurtma rüzgarla havalandı ve yükseldi. Sincap da taşın üstünde sevinçle zıpladı. "Yardımın için çok teşekkürler, Daşa!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sincap da taşın üstünde sevinçle zıpladı"
   - Cümle 10: «Sincap da taşın üstünde sevinçle zıpladı.»
   - Açıklama: Sincap olayda hiçbir işe yaramıyor; yalnız bakıp zıplayan işlevsiz bir karakter.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0108` birebir aynı, ardından `@onarim: cdda4615b01466311597b396f96579fc85fef85b`, sonra gövde.

### Hikâye 5: tohum masa-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0109
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: bir şey yapmak
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'bardak', fiil 'giyinmek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: ip yere değdiği için öbür bardaktan ses gelmedi | geri geri yürüyüp ipi iyice çekti
@tohum: masa-0109
@degisim: giyinmek -> çekmek
Ormanda kuşlar ötüyordu. Maşa, Koca Ayı ile iki ahşap bardaktan ve bir ipten telefon yapmıştı. Ama kirpi öbür bardağı dinleyince hiç ses duymadı, çünkü ip yere değiyordu. "Beni duyuyor musun, kirpi?" diye sordu Maşa bardağa. Kirpi başını iki yana salladı. Maşa hemen yeni bir şey denedi. Geri geri yürüdü ve ipi iyice çekti. İp artık yere değmiyordu. "Merhaba, kirpi!" dedi Maşa. Kirpi bu kez sesi duydu ve sevinçle zıpladı. Koca Ayı da gülümsedi ve ellerini çırptı. Maşa çok sevindi, çünkü kendi yaptığı telefon artık çalışıyordu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kirpi öbür bardağı dinleyince"
   - Cümle 3: «Ama kirpi öbür bardağı dinleyince hiç ses duymadı, çünkü ip yere değiyordu.»
   - Açıklama: Bardak dinlenmez; 'bardağı kulağına tutunca' olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kirpi başını iki yana salladı"
   - Cümle 5: «Kirpi başını iki yana salladı.»
   - Açıklama: Kirpi bardaktan hiç ses duymuyorken Maşa'nın sorusunu duymuş gibi başını sallayarak cevap veriyor.
   - Açıklama: Kirpi sesi duymadığı söylenirken Maşa'nın sorusuna cevap veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0109` birebir aynı, `@degisim: giyinmek -> çekmek` (tutuyorsan), ardından `@onarim: d9fa02d901cbf8ae561b1e6e22c6e3a49a630da2`, sonra gövde.

### Hikâye 6: tohum masa-0111 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0111
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: kaybolan eşya
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'zeytin', fiil 'kırpmak', sıfat 'pembe'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: koşarken pembe toka yaprakların arasına düştü | yere yattı ve yapraklara yandan baktı
@tohum: masa-0111
@degisim: zeytin -> toka
Ormanda yerler sarı yapraklarla doluydu. Maşa ile kuzeni Daşa patikada koşuyordu. Birden Daşa durdu, çünkü parlak pembe tokası düşmüştü. "Toka kayboldu, bulamıyorum," dedi Daşa. Maşa yaprakları elleriyle karıştırdı ama tokayı bulamadı. Sonra başka bir yol denedi. Yere yattı ve yaprakların arasına yandan baktı. Birden bir şey güneşte parladı ve Maşa gözlerini kırptı. Orada pembe toka duruyordu. "Buldum, Daşa!" dedi Maşa. Daşa tokasını saçına taktı ve Maşa'ya sarıldı. Maşa çok mutlu oldu, çünkü Daşa'nın tokasını bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "koşarken pembe toka yaprakların"
   - Cümle 0 (plan satırı): «koşarken pembe toka yaprakların arasına düştü | yere yattı ve yapraklara yandan baktı»
   - Açıklama: '-ken' yan cümlesinin öznesi ana cümlenin öznesi olan tokaya bağlanıyor; toka koşmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra başka bir yol denedi"
   - Cümle 6: «Sonra başka bir yol denedi.»
   - Açıklama: 'Yol' burada 'yöntem' anlamında mecaz; patikada koşan bir hikayede çocuğu şaşırtır.
   - Açıklama: 'yol' burada 'yöntem' anlamında mecazlı ve küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0111` birebir aynı, `@degisim: zeytin -> toka` (tutuyorsan), ardından `@onarim: 3c2acdf04f5c67871770983c99cb683affee56df`, sonra gövde.

### Hikâye 7: tohum masa-0112 (deneme 1 -> 2)

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
@plan: ağaç evin dışından tık tık diye bir ses geldi | reçel almaya gidince pencereden sesin yerini gördü
@tohum: masa-0112
@degisim: tamamlanmak -> damlamak
Dışarıdan tık tık diye bir ses geliyordu. Maşa, Koca Ayı'nın ağaç evindeydi ve bu sesi çok merak etti. Uykulu Koca Ayı da başını kaldırıp dinledi. Maşa önce kapıyı açıp baktı, ama orada bir şey yoktu. Sonra bir kaşık reçel yemek için pencerenin yanındaki rafa gitti. Ses orada daha yüksekti. Maşa pencereden dışarı baktı. Çatıdaki buzlar eriyordu ve damlalar boş bir kovaya damlıyordu. Her damla kovada tık diye ses yapıyordu. Koca Ayı da pencereye geldi ve gülümsedi. "Koca Ayı, sesi buldum, şimdi birlikte reçel yiyelim!" dedi Maşa.
```

**Hakem bulguları (6):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bir kaşık reçel yemek için pencerenin"
   - Cümle 5: «Sonra bir kaşık reçel yemek için pencerenin yanındaki rafa gitti.»
   - Açıklama: Maşa sesin kaynağını aramıyor, sesi reçele giderken tesadüfen buluyor; çözüm sebebe yönelmiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bir kaşık reçel yemek için"
   - Cümle 5: «Sonra bir kaşık reçel yemek için pencerenin yanındaki rafa gitti.»
   - Açıklama: Maşa sesin sebebine yönelmiyor, reçel yemeye giderken sesi tesadüfen buluyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bir kaşık reçel yemek için"
   - Cümle 5: «Sonra bir kaşık reçel yemek için pencerenin yanındaki rafa gitti.»
   - Açıklama: Çözüm, sorunla ilgisiz reçel isteğiyle sebepsizce geliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ses orada daha yüksekti"
   - Cümle 6: «Ses orada daha yüksekti.»
   - Açıklama: Sesin yeri figürün çabasından değil rastlantıdan çıkıyor; çözüm sebepsizce geliyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "damlalar boş bir kovaya damlıyordu"
   - Cümle 8: «Çatıdaki buzlar eriyordu ve damlalar boş bir kovaya damlıyordu.»
   - Açıklama: 'Damlalar damlıyordu' gereksiz tekrar.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kovada tık diye ses yapıyordu"
   - Cümle 9: «Her damla kovada tık diye ses yapıyordu.»
   - Açıklama: 'Ses yapmak' yanlış kullanım; 'ses çıkarıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0112` birebir aynı, `@degisim: tamamlanmak -> damlamak` (tutuyorsan), ardından `@onarim: 8cd6216ea94ff3b5559d76afea77ae5edeac95b8`, sonra gövde.

### Hikâye 8: tohum masa-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0113
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'armut', fiil 'durmak', sıfat 'soslu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: sincap armutları sevmedi ve kütükte durmadı | fındık toplayıp yeni bir yemek denedi
@tohum: masa-0113
Bir sabah Maşa ile Daşa ormanda yemek oyunu oynuyordu. Kütüğün üstünde evden getirdikleri armutlar ve bir kase bal vardı. İlk yemeği sincaba verdiler, ama sincap armutları sevmedi ve kütükte durmadı. Hemen ağaca geri kaçtı. "Sincap armut değil, fındık sever," dedi Daşa. Maşa yeni bir yemek denedi. Ağacın altından birkaç fındık topladı ve armutları fındıkla süsledi. Sonra hepsinin üstüne biraz bal döktü. "Gel, sincap, işte soslu fındıklı armut!" dedi Maşa. Sincap fındıkları gördü ve ağaçtan hızla indi. Bu kez kütükte durdu ve fındıkları tek tek yedi. "Bak, Maşa, sincap hepsini bitirdi," dedi Daşa. Maşa çok sevindi, çünkü küçük sincap sonunda doymuştu.
```

**Hakem bulguları (4):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sincap armut değil, fındık sever"
   - Cümle 5: «"Sincap armut değil, fındık sever," dedi Daşa.»
   - Açıklama: Çözümün anahtarını Maşa değil Daşa buluyor; Maşa yalnız söyleneni uyguluyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "hepsinin üstüne biraz bal döktü"
   - Cümle 8: «Sonra hepsinin üstüne biraz bal döktü.»
   - Açıklama: Sincaba fındık vermek yeterliyken çözüm fındık toplama, armutları süsleme ve bal dökme ile iki adımı aşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hepsinin üstüne biraz bal döktü"
   - Cümle 8: «Sonra hepsinin üstüne biraz bal döktü.»
   - Açıklama: Kurulan bal hiçbir işe yaramıyor; sincap yalnız fındıkları yiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sincap hepsini bitirdi"
   - Cümle 12: «"Bak, Maşa, sincap hepsini bitirdi," dedi Daşa.»
   - Açıklama: Sincap yalnız fındıkları yiyor ama armutlu yemeğin hepsini bitirmiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0113` birebir aynı, ardından `@onarim: f1abdfadeb0881d68812d90a8a9b0ea9ece88f45`, sonra gövde.

### Hikâye 9: tohum masa-0114 (deneme 1 -> 2)

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
Maşa ormanda resim oyunu oynuyordu ve bir zambak çizmek istiyordu. Kalemlerini ve sepetini beyaz bir zambağın yanına koydu, kağıdını da çimenlere serdi. Ama rüzgar esti ve kağıt havalanıp çalılara doğru uçtu. Maşa koştu ve kağıdı çalının dibinden aldı. Sonra sepetine baktı. Sepette en sevdiği yiyecek, bir kavanoz çilek reçeli vardı. Maşa reçel kavanozunu kağıdın bir köşesine koydu. Artık rüzgar esse de kağıt yerinden kıpırdamadı. Maşa zambağın uzun sapını ve açık yapraklarını dikkatle çizdi. Resim çok güzel oldu ve tıpkı çiçeğe benzedi. Sonra Maşa kağıdın boş köşesine mutlu mutlu küçük bir zambak daha çizdi.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra Maşa kağıdın boş köşesine mutlu mutlu küçük bir zambak daha çizdi"
   - Cümle 11: «Sonra Maşa kağıdın boş köşesine mutlu mutlu küçük bir zambak daha çizdi.»
   - Açıklama: Hikaye sıcak bir kapanış yerine 'Sonra' ile başlayan çıplak bir eylemle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0114` birebir aynı, ardından `@onarim: 4eecf3bdabb6d4f565589c051451a2dd57ad892c`, sonra gövde.

### Hikâye 10: tohum masa-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0115
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'karabiber', fiil 'sormak', sıfat 'kalın'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: kar çok kuruydu ve kar topları dağıldı | tepenin güneşli yanındaki ıslak karı denedi
@tohum: masa-0115
@degisim: karabiber -> dal
Bir sabah tepede kalın bir kar vardı. Maşa ile Koca Ayı kardan bir ayı yapmak istedi. Ama kar çok kuruydu ve kar topları elde hep dağıldı. Maşa hemen başka bir yer denedi. Tepenin güneşli yanına koştu ve bir avuç kar aldı. Bu kar biraz ıslaktı ve kolayca top oldu. "Koca Ayı, bu karla büyük toplar yapalım mı?" diye sordu Maşa. Koca Ayı başını salladı. İkisi birlikte büyük kar topları yuvarladı ve üst üste koydu. Bu kez kardan ayı hiç dağılmadı. Sonra Koca Ayı yerden iki dal aldı ve kardan ayıya kol yaptı. Maşa çok sevindi, çünkü kardan ayıyı sonunda yapabilmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kar topları elde hep dağıldı"
   - Cümle 3: «Ama kar çok kuruydu ve kar topları elde hep dağıldı.»
   - Açıklama: 'elde' iyelik eki eksik ve kulağa bozuk geliyor; 'ellerinde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0115` birebir aynı, `@degisim: karabiber -> dal` (tutuyorsan), ardından `@onarim: cfaebae2717e103028160dde01384f1d50994e10`, sonra gövde.

### Hikâye 11: tohum masa-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0116
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'misket', fiil 'serinletmek', sıfat 'dağınık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: yer düz değildi ve misketler aşağı yuvarlandı | ağacın gölgesinde düz bir yer denedi
@tohum: masa-0116
Güneş tepede sıcak sıcak parlıyordu. Maşa kirpiyle ilk kez misket oynuyordu. Ama yer düz değildi ve misketler hep aşağı kaçıp çimenlere dağıldı. Kirpi dağınık misketleri burnuyla itip tek tek geri getirdi. Maşa hemen başka bir yer denedi ve bir ağacın gölgesine koştu. Orada yer düzdü ve hafif bir rüzgar Maşa'nın sıcak yüzünü serinletti. Maşa misketleri toprağa bir halka gibi dizdi. Sonra parmağıyla bir misketi itti. Misket öbür misketlere tık diye çarptı, ama bu kez hiçbiri uzağa gitmedi. "Sıra sende, kirpi!" dedi Maşa. Kirpi de burnuyla küçük bir misketi itti. Maşa çok sevindi, çünkü misketler artık kaçmıyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hafif bir rüzgar Maşa'nın sıcak yüzünü serinletti"
   - Cümle 6: «Orada yer düzdü ve hafif bir rüzgar Maşa'nın sıcak yüzünü serinletti.»
   - Açıklama: Serinleten rüzgar sorunla ve çözümle ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Serinleten rüzgar misket sorunuyla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0116` birebir aynı, ardından `@onarim: 67f7613b85ec63d33c9959d2ec369821773274bc`, sonra gövde.

### Hikâye 12: tohum masa-0117 (deneme 1 -> 2)

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
Bir sabah Maşa evin bahçesinde kahvaltı masası hazırlıyordu. Masada ekmek, elmalar ve bir kavanoz çilek reçeli vardı. Maşa ekmeğine reçel sürmek istedi, ama kavanozun kapağı çok sıkıydı. Tam o sırada kuzeni Daşa bahçeye geldi. Elinde Maşa için bir buket vardı. "Daşa, kapak açılmıyor, bana yardım eder misin?" diye sordu Maşa. Daşa buketi masaya koydu ve kavanozu sıkıca tuttu. Maşa kapağı çevirdi. Bu kez kapak "pıt" diye açıldı. Elma kokusunu alan kirpi de çitin altından masaya geldi. Maşa ona küçük bir elma verdi ve kirpi çok memnun oldu. Sonra hepsi masanın başında toplandı ve mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa için bir buket"
   - Cümle 5: «Elinde Maşa için bir buket vardı.»
   - Açıklama: 'buket' 3 yaşındaki çocuğun bilmeyebileceği bir kelime; 'çiçek demeti' ya da 'çiçekler' daha uygun.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa için bir buket vardı"
   - Cümle 5: «Elinde Maşa için bir buket vardı.»
   - Açıklama: 'buket' 3 yaşındaki çocuğun bilmeyebileceği bir kelime ve neyin buketi olduğu da belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elinde Maşa için bir buket vardı"
   - Cümle 5: «Elinde Maşa için bir buket vardı.»
   - Açıklama: Buket sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Buket olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma kokusunu alan kirpi"
   - Cümle 10: «Elma kokusunu alan kirpi de çitin altından masaya geldi.»
   - Açıklama: Kirpi sorun çözüldükten sonra sebepsizce geliyor ve olaya katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0117` birebir aynı, ardından `@onarim: cf3e13c315bd4921821dd344c52d580620965d16`, sonra gövde.
