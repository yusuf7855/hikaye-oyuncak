# Editör görevi (onarım): Maşa, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0054 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0054
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'paspas', fiil 'boşaltmak', sıfat 'cömert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: sebzeleri sulamak istedi ama su dolu kova çok ağırdı | suyun yarısını boşalttı ve kovayı rahatça taşıdı
@tohum: masa-0054
@degisim: paspas -> kova
Ormandaki ağaç evin bahçesinde Koca Ayı bir ağacın altında uyuyordu. Cömert Maşa, Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi. Ama su dolu büyük kova çok ağırdı. Maşa kovayı iki eliyle çekti ama kova yerinden oynamadı. Maşa biraz düşündü ve suyun yarısını domateslere boşaltmayı denedi. Kova hafifledi ve Maşa onu rahatça taşıdı. Kalan suyu da havuçlara döktü. Sonra Koca Ayı uyandı ve ıslak bahçeyi gördü. Şaşırdı ve kocaman gülümsedi. Maşa'ya koştu ve ona sıkıca sarıldı. "Sürpriz, Koca Ayı! Bugün bahçeni ben suladım!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Cömert Maşa, Koca Ayı'ya"
   - Cümle 2: «Cömert Maşa, Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi.»
   - Açıklama: Tohumdaki özellik denemek; kartın özellikler alanında olmayan cömertlik ikinci bir özellik olarak ekleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Cömert Maşa, Koca Ayı'ya sürpriz"
   - Cümle 2: «Cömert Maşa, Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi.»
   - Açıklama: Tohumdaki özellik denemek; kartın özellikler alanında olmayan cömertlik ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0054` birebir aynı, `@degisim: paspas -> kova` (tutuyorsan), ardından `@onarim: 8b8d77c51844c9ca6719182ddd2312cf834c5370`, sonra gövde.

### Hikâye 2: tohum masa-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0056
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: yaprakların arasından gelen sesi merak etti | sakinleşti ve yere elma koyunca kirpiyi gördü
@tohum: masa-0056
@degisim: yağ -> elma
Maşa ormanda elinde bir elmayla yürüyordu. Birden yaprakların arasından hışır hışır bir ses geldi. Maşa bu sesi çok merak etti. Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu. Ama ses kesildi ve hiçbir şey kıpırdamadı. Maşa biraz bekledi ve sakinleşti. Sonra yeni bir şey denedi ve elmasını yere koydu. Yavaşça geri çekildi ve sessizce oturdu. Az sonra yaprakların arasından küçük bir burun çıktı. Ardından dikenli bir kirpi göründü. Kirpi elmayı kokladı ve mutlu mutlu yemeye başladı. Maşa çok sevindi, çünkü sesi yapan kirpiyi sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Maşa çok sabırsızdı ve"
   - Cümle 4: «Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu.»
   - Açıklama: Art arda iki cümle gereksiz yere 'Maşa' adıyla başlıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa çok sabırsızdı"
   - Cümle 4: «Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu.»
   - Açıklama: Tohumdaki özellik denemek; sabırsızlık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0056` birebir aynı, `@degisim: yağ -> elma` (tutuyorsan), ardından `@onarim: 54a993d80ba12a8262dd0a2ffd12346a3eb368cf`, sonra gövde.

### Hikâye 3: tohum masa-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0057
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yosun', fiil 'içmek', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: sincap saklanan kavanozun üstüne yosun koydu | sincabın ağzında yosun görüp yosunların altına baktı
@tohum: masa-0057
@degisim: içmek -> saklamak
Maşa tepede Koca Ayı ve sincapla bir arama oyunu oynuyordu. Koca Ayı, Maşa'nın özel reçel kavanozunu bir taşın arkasına sakladı. Ama sincap kavanozun üstüne yosun koydu. Maşa taşların arkasına baktı ama kavanozu göremedi. Sonra sincabın ağzında biraz yosun gördü. Maşa kavanozun yosunun altında olduğunu anladı. Büyük bir taşın yanında kabarık bir yosun yığını vardı. Maşa hemen o taşa koştu ve yosunları kaldırdı. Reçel kavanozu tam oradaydı! "Buldum, sincap, sen çok komiksin!" dedi Maşa. Koca Ayı güldü ve ellerini çırptı. Sincap da kuyruğunu salladı. Maşa çok sevindi, çünkü sevdiği reçeli oyunun sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sincap kavanozun üstüne yosun koydu"
   - Cümle 3: «Ama sincap kavanozun üstüne yosun koydu.»
   - Açıklama: Sincabın kavanozu neden yosunla örttüğü söylenmiyor, sorunun sebebi açıklanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0057` birebir aynı, `@degisim: içmek -> saklamak` (tutuyorsan), ardından `@onarim: df024019af2caad671f21694f77cae967198a017`, sonra gövde.

### Hikâye 4: tohum masa-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0058
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'basamak', fiil 'şişirmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: parmakları reçelli olunca balon elinden kaydı | parmaklarını temizleyip balonu yeniden şişirdi
@tohum: masa-0058
@degisim: düzenli -> sıkı
Güneş parlıyordu. Maşa tepede ekmeğini bitirdi ve kırmızı bir balon şişirdi. Ama reçelli parmakları kaydı ve balon elinden kaçtı. Balon komik bir sesle tepede sağa sola uçtu. Sonra söndü ve taş bir basamağın üstüne düştü. Maşa balonuna baktı ve üzüldü. Maşa tatlıyı çok severdi ve parmaklarını tek tek yaladı. Balonu yeniden şişirdi ve ucuna sıkı bir düğüm attı. Bu kez balon hiç kaçmadı. Maşa balonu havaya attı ve yakaladı. Maşa balonuyla tepede mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "parmaklarını temizleyip balonu yeniden şişirdi"
   - Cümle 0 (plan satırı): «parmakları reçelli olunca balon elinden kaydı | parmaklarını temizleyip balonu yeniden şişirdi»
   - Açıklama: Plan asıl işe yarayan düğümü söylemiyor ve gövdede parmaklar temizlenmiyor, yalanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "reçelli parmakları kaydı"
   - Cümle 3: «Ama reçelli parmakları kaydı ve balon elinden kaçtı.»
   - Açıklama: Parmaklar kaymaz, balon parmaklardan kayar; fiil öznesine uymuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama reçelli parmakları kaydı"
   - Cümle 3: «Ama reçelli parmakları kaydı ve balon elinden kaçtı.»
   - Açıklama: Reçelli parmaklar yapışkan olur, kaymaz; sebep akla yatkın değil ve reçel hiç kurulmuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "ucuna sıkı bir düğüm attı"
   - Cümle 8: «Balonu yeniden şişirdi ve ucuna sıkı bir düğüm attı.»
   - Açıklama: Balonu asıl tutan düğüm; çözüm parmak sebebine değil başka bir şeye yöneliyor.
   - Açıklama: Çözüm parmakları yalamak, balonu yeniden şişirmek ve düğüm atmak olarak üç adıma yayılıyor; düğüm sebebe (reçelli parmaklar) yönelmiyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "balonuyla tepede mutlu mutlu"
   - Cümle 11: «Maşa balonuyla tepede mutlu mutlu oynamaya devam etti.»
   - Açıklama: 'Tepede' kelimesi hikayede gereksiz yere üç kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0058` birebir aynı, `@degisim: düzenli -> sıkı` (tutuyorsan), ardından `@onarim: 8012feede58f813c230a4f6b58436b07120c9f28`, sonra gövde.

### Hikâye 5: tohum masa-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0062
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'külah', fiil 'çırpmak', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: tanımadığı sincap utandı ve yaprakların arasına saklandı | yapraktan külah yapıp içine fındık koydu
@tohum: masa-0062
Maşa ormanda reçel yiyerek yürüyordu. Bir ağacın dalında daha önce görmediği bir sincap gördü. Sincap onu görünce utandı ve yaprakların arasına saklandı. "Merhaba, sincap, benimle arkadaş olur musun?" diye sordu Maşa. Ama sincap saklandığı yerden çıkmadı. Maşa etrafına baktı ve yerde fındıklar gördü. Büyük bir yapraktan yamuk bir külah yaptı. Sonra külahın kenarını parmağındaki reçelle yapıştırdı. Külahı fındıkla doldurdu ve ağacın dibine koydu. Sincap hemen aşağı indi ve bir fındık aldı. Sonra Maşa'nın yanına geldi ve kuyruğunu salladı. Maşa sevinçle ellerini yavaşça çırptı. Maşa çok mutluydu, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra külahın kenarını parmağındaki reçelle yapıştırdı"
   - Cümle 8: «Sonra külahın kenarını parmağındaki reçelle yapıştırdı.»
   - Açıklama: Çözüm yaprak külah yapma, reçelle yapıştırma, doldurma ve koyma gibi ikiden fazla dolambaçlı adıma yayılıyor.
   - Açıklama: Çözüm külah yapma, reçelle yapıştırma, doldurma ve koyma gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0062` birebir aynı, ardından `@onarim: 36a5886806a5fb1391c85bd8f97ae995801666d7`, sonra gövde.

### Hikâye 6: tohum masa-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0064
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'mendil', fiil 'aydınlanmak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi uzun otların arasından kelebekleri göremedi | taşın üstüne reçel koydu ve kirpi taşa çıktı
@tohum: masa-0064
Yağmur dindi ve orman birden aydınlandı. Maşa ile Koca Ayı çiçeklerin üstünde uçan renkli kelebekler gördü. Ama küçük kirpi uzun otların arasından onları göremedi. "Kirpi, sen de görmelisin!" dedi Maşa. Koca Ayı yakındaki kuru ve düz bir taşı gösterdi. Maşa cebinden küçük bir kavanoz çıkardı. Taşın üstüne biraz elma reçeli koydu. Kirpi kokuyu aldı ve hemen taşa çıktı. Reçeli yedi ve başını kaldırdı. Kirpi kelebekleri görünce sevinçle burnunu oynattı. Maşa kirpiye eğildi ve onun reçelli burnunu mendiliyle sildi. Maşa, Koca Ayı ve kirpi yan yana oturup kelebekleri mutlu mutlu seyretti.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Koca Ayı yakındaki kuru ve düz bir taşı gösterdi"
   - Cümle 5: «Koca Ayı yakındaki kuru ve düz bir taşı gösterdi.»
   - Açıklama: Çözümün ana fikri olan taşı yan karakter Koca Ayı buluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa cebinden küçük bir kavanoz çıkardı"
   - Cümle 6: «Maşa cebinden küçük bir kavanoz çıkardı.»
   - Açıklama: Reçel kavanozu sebepsizce beliriyor ve çözümü dolaylı getiriyor; kirpinin taşa çıkması için reçele gerek yok.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Taşın üstüne biraz elma reçeli koydu"
   - Cümle 7: «Taşın üstüne biraz elma reçeli koydu.»
   - Açıklama: Kartın özelliği Maşa'nın reçeli sevmesi; burada reçel yalnız kirpiyi çekmek için yem olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0064` birebir aynı, ardından `@onarim: e189d5a4e090e8c267283f1c17361bbd22516dd6`, sonra gövde.

### Hikâye 7: tohum masa-0065 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0065
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'havlu', fiil 'yedirmek', sıfat 'küçücük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kuru toprak dağıldı ve pasta olmadı | toprağa su dökmeyi denedi ve pastayı yaptı
@tohum: masa-0065
@degisim: yedirmek -> süslemek
Kuşlar ağaçların arasında ötüyordu. Maşa beline bir havlu bağlamış, pasta yapma oyunu oynuyordu. Çamurdan pasta yapmak istedi ama toprak kuruydu ve hep dağılıyordu. Maşa hemen başka bir yol denedi. Yanındaki su şişesini açtı ve toprağa biraz su döktü. Sonra toprağı elleriyle karıştırdı. Toprak yumuşadı ve yapış yapış oldu. Maşa yuvarlak bir pasta yaptı ve pasta bu kez sağlam durdu. Pastanın üstünü küçücük çiçeklerle süsledi. Sonra çamurlu ellerini havluya sildi. Maşa çok sevindi, çünkü çamur pastasını sonunda yapmıştı.
```

**Hakem bulguları (2):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Maşa beline bir havlu bağlamış"
   - Cümle 2: «Maşa beline bir havlu bağlamış, pasta yapma oyunu oynuyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen başka bir yol denedi"
   - Cümle 4: «Maşa hemen başka bir yol denedi.»
   - Açıklama: 'Yol denemek' mecazlı kullanım; küçük çocuk yolu somut anlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0065` birebir aynı, `@degisim: yedirmek -> süslemek` (tutuyorsan), ardından `@onarim: 8c47d10489cddcaccbab3f46d053283b03b1b888`, sonra gövde.

### Hikâye 8: tohum masa-0066 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0066
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'altın', fiil 'yavaşlamak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: çalıların arasından garip bir ses geldi | dalları açtı ve sesi yapan kağıdı buldu
@tohum: masa-0066
Maşa tepede neşeyle koşuyordu. Birden çalıların arasından garip bir ses geldi. Maşa yavaşladı ve sesin nereden geldiğini merak etti. Çalıya eğildi ama bir şey göremedi. Sonra dalları eliyle dikkatle açmayı denedi. Dalların arasında parlak bir şey vardı. Maşa hemen onu aldı. Bu, altın renkli plastik bir şeker kağıdıydı. Rüzgar esince bu kağıt hışır hışır ses çıkarıyordu. Maşa garip sesi bulduğu için güldü. Kağıdı katlayıp cebine koydu. Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çalıların arasından garip bir ses geldi"
   - Cümle 2: «Birden çalıların arasından garip bir ses geldi.»
   - Açıklama: Garip bir ses gerçek bir sorun değil, önemsiz bir merak olayı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı"
   - Cümle 12: «Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı.»
   - Açıklama: 'Bundan sonra' süreklilik bildirir, tek seferlik 'attı' ile uyuşmuyor; 'atardı' olmalı.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bulduğu çöpleri toplayıp çöpe attı"
   - Cümle 12: «Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı.»
   - Açıklama: Çöp toplama dersi garip sesi bulma olayından çıkmıyor, sonradan eklenmiş bir öğüt gibi duruyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı"
   - Cümle 12: «Maşa bundan sonra tepede bulduğu çöpleri toplayıp çöpe attı.»
   - Açıklama: Çöp toplama dersi yaşanan olaydan çıkmıyor; Maşa kağıdı bile çöpe değil cebine koyuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0066` birebir aynı, ardından `@onarim: 77d77b15d544fe211dddf56e459680c201041b1d`, sonra gövde.

### Hikâye 9: tohum masa-0068 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0068
- yer: dağ (Ormanın yanındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'ayna', fiil 'sokulmak', sıfat 'biberli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: bıyık çizecek boyaları evde kalmıştı | parmağıyla yüzüne reçelden bıyık çizdi
@tohum: masa-0068
@degisim: biberli -> tatlı
Tepede güneş ılık ılık parlıyordu. Maşa kediler gibi bıyıklı olmak istiyordu. Ama bıyık çizecek boyaları evde kalmıştı. Maşa yanındaki reçelli ekmeğine baktı ve güldü. Parmağını reçele batırdı ve yanaklarına ince bıyıklar çizdi. Sonra cebindeki küçük aynaya baktı. Kırmızı bıyıklar çok tatlı görünüyordu. Maşa parmağındaki reçeli de afiyetle yaladı. Sonra elleri ve dizleriyle çimenlerde yürüdü ve miyav diye ses çıkardı. Güneşli bir taşın yanına sokuldu ve kıvrıldı. Maşa oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güneş ılık ılık parlıyordu"
   - Cümle 1: «Tepede güneş ılık ılık parlıyordu.»
   - Açıklama: 'Ilık' sıcaklık bildirir, 'parlamak' fiiline uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0068` birebir aynı, `@degisim: biberli -> tatlı` (tutuyorsan), ardından `@onarim: fad365838164a8394c67f89ae1f4b6d9789486ec`, sonra gövde.

### Hikâye 10: tohum masa-0070 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0070
- yer: dağ (Ormanın yanındaki tepe.)
- tema: bir şey yapmak
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'sabun', fiil 'yerleşmek', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: sabunlu su yapacak bir kabı yoktu | reçeli yiyip boş kavanozda sabunlu su yaptı
@tohum: masa-0070
@degisim: sakar -> kocaman
Tepede hafif bir rüzgar esiyordu. Maşa köpük uçurmak için sabun ve bir şişe su getirmişti. Ama sabunlu su yapacak bir kabı yoktu. Maşa yanındaki reçel kavanozuna baktı. Kavanozun dibinde biraz reçel kalmıştı. Maşa reçeli afiyetle yedi ve kavanozu boşalttı. Sonra kavanoza su doldurdu, sabunu koydu ve karıştırdı. Su köpük köpük oldu. Maşa ince bir dalı bükerek küçük bir halka yaptı. Çimenlere yerleşti ve halkayı suya batırıp üfledi. Kocaman köpükler rüzgarla havaya uçtu. Maşa çok sevindi, çünkü sabunlu suyu kendisi hazırlamıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "köpük uçurmak için"
   - Cümle 2: «Maşa köpük uçurmak için sabun ve bir şişe su getirmişti.»
   - Açıklama: Havada uçan sabun kabarcıkları 'baloncuk' olur; 'köpük' bu anlamda yanlış kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sabunlu su yapacak bir kabı yoktu"
   - Cümle 3: «Ama sabunlu su yapacak bir kabı yoktu.»
   - Açıklama: Maşa'nın neden kap getirmediği, yani sorunun sebebi söylenmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa yanındaki reçel kavanozuna baktı"
   - Cümle 4: «Maşa yanındaki reçel kavanozuna baktı.»
   - Açıklama: Reçel kavanozu önceden kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "ince bir dalı bükerek küçük bir halka"
   - Cümle 9: «Maşa ince bir dalı bükerek küçük bir halka yaptı.»
   - Açıklama: Çözüm reçeli yeme, sabunlu su hazırlama ve daldan halka yapma diye ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0070` birebir aynı, `@degisim: sakar -> kocaman` (tutuyorsan), ardından `@onarim: d299a2194442b218486c20a285146991cdab2c10`, sonra gövde.

### Hikâye 11: tohum masa-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0071
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'turşu', fiil 'kutlamak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: ikisi elmayı aynı anda itti ve elma çalıya yuvarlandı | sırayla oynamayı denedi ve önce kirpiye sıra verdi
@tohum: masa-0071
@degisim: turşu -> elma
Ormanda serin bir rüzgar esiyordu. Maşa ile şirin kirpi elmayı iki taşın arasından geçiriyordu. Ama ikisi elmayı aynı anda itti ve elma çalıya yuvarlandı. Maşa elmayı çalıdan aldı ve yeni bir yol denedi. "Sırayla oynayalım, kirpi, önce sen!" dedi Maşa. Kirpi elmayı burnuyla itti ve elma taşların arasından geçti. Maşa ile kirpi bunu zıplayarak kutladı. "Şimdi sıra bende," dedi Maşa. Maşa da elmayı itti ve elma yine geçti. Kirpi sevinçle yerinde döndü. Maşa çok mutluydu, çünkü sırayla oynayınca ikisi de elmayı geçirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aldı ve yeni bir yol denedi"
   - Cümle 4: «Maşa elmayı çalıdan aldı ve yeni bir yol denedi.»
   - Açıklama: 'Yeni bir yol denemek' yöntem anlamında mecaz, küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0071` birebir aynı, `@degisim: turşu -> elma` (tutuyorsan), ardından `@onarim: 01121d2d115f7332f7f619a2fac1f99443dba33b`, sonra gövde.

### Hikâye 12: tohum masa-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0072
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'delik', fiil 'getirmek', sıfat 'hazır'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: cebindeki delikten kozalaklar yere düşüyordu | reçeli yiyip boş kavanozu kuzenine verdi
@tohum: masa-0072
Ormanda yapraklar rüzgarda sallanıyordu. Maşa'nın kuzeni Daşa şehre götürmek için küçük kozalaklar topluyordu. Ama cebinde bir delik vardı ve kozalaklar yere düşüyordu. "Maşa, bunları nasıl taşıyacağım?" dedi Daşa. Maşa'nın elinde küçük bir reçel kavanozu vardı. Maşa içindeki son reçeli afiyetle yedi. Sonra boş kavanozu hemen Daşa'ya getirdi. "Onları buna koy, Daşa," dedi Maşa. Daşa yerdeki kozalakları tek tek kavanoza koydu. Maşa kapağı sıkıca kapattı. "Artık hepsi şehre gitmeye hazır!" dedi Daşa. Maşa çok sevindi, çünkü kuzenine yardım etmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın elinde küçük bir reçel kavanozu vardı"
   - Cümle 5: «Maşa'nın elinde küçük bir reçel kavanozu vardı.»
   - Açıklama: Reçel kavanozu sorun çıktıktan hemen sonra sebepsizce beliriyor ve çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0072` birebir aynı, ardından `@onarim: 7c70936c91c33cb6a8e00f4ca40efca1d988f918`, sonra gövde.
