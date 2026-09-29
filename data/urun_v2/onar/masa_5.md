# Editör görevi (onarım): Maşa, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0002 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0002
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'silgi', fiil 'hazırlamak', sıfat 'gizemli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: sepet dala takıldı ve reçel kavanozu kayboldu | yerdeki mor damlaları takip edip kavanozu buldu
@tohum: masa-0002
@degisim: silgi -> kavanoz
Ormanda Koca Ayı, Maşa ile kirpi için kahvaltı hazırlıyordu. Ama sepet bir dala takıldı ve reçel kavanozu düşüp yuvarlandı. Koca Ayı her yere baktı ama kavanozu bulamadı. Maşa, Koca Ayı'ya yardım etmek istedi. Yerde küçük, gizemli, mor damlalar gördü. Maşa reçeli çok severdi ve bu damlaları hemen tanıdı. Kavanozun kapağı açılmıştı ve reçel yere dökülmüştü. Maşa damlaları takip etti ve çalılara vardı. Kavanoz orada, çimenlerin üstünde duruyordu. "Buldum, Koca Ayı, işte reçel!" dedi Maşa. Koca Ayı sevinçle kavanozu aldı ve ekmeklere reçel sürdü. Kirpi de burnunu kavanoza uzattı. "Kahvaltı hazır, hadi hep birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sepet bir dala takıldı"
   - Cümle 2: «Ama sepet bir dala takıldı ve reçel kavanozu düşüp yuvarlandı.»
   - Açıklama: Kahvaltı hazırlanırken sepetin nasıl dala takıldığı ve kavanozun neden uzağa gittiği akla yatkın biçimde söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, gizemli, mor damlalar"
   - Cümle 5: «Yerde küçük, gizemli, mor damlalar gördü.»
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yerde küçük, gizemli, mor damlalar"
   - Cümle 5: «Yerde küçük, gizemli, mor damlalar gördü.»
   - Açıklama: 'Gizemli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0002` birebir aynı, `@degisim: silgi -> kavanoz` (tutuyorsan), ardından `@onarim: ed818b2486b4af0c2e7288e7ca7ef648891e16ff`, sonra gövde.

### Hikâye 2: tohum masa-0005 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0005
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'mermer', fiil 'uyutmak', sıfat 'değerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: kirpi sert taşın üstünde uyuyamadı | yapraktan yumuşak bir yatak yaptı
@tohum: masa-0005
@degisim: değerli -> yumuşak
Bir sabah Maşa ormanda bir kirpi gördü. Kirpi büyük bir taşın üstünde uyumaya çalışıyordu. Ama bu beyaz mermer taş çok sertti ve kirpi uyuyamadı. Maşa daha önce hiç yapraktan yatak yapmamıştı. Ama bu yeni işi hemen denedi. Ağaçların altından yumuşak yapraklar topladı. Yaprakları taşın yanına koydu ve küçük bir yatak yaptı. Kirpi taştan indi ve yaprakları kokladı. "Bu senin yeni yatağın, kirpi," dedi Maşa. Kirpi yumuşak yatağa kıvrıldı ve hemen uyudu. Maşa çok sevindi, çünkü yaptığı ilk yatakla kirpiyi uyutmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu beyaz mermer taş"
   - Cümle 3: «Ama bu beyaz mermer taş çok sertti ve kirpi uyuyamadı.»
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "bu beyaz mermer taş çok sertti"
   - Cümle 3: «Ama bu beyaz mermer taş çok sertti ve kirpi uyuyamadı.»
   - Açıklama: Kartın orman tarifi ağaçlar ve patikalardan söz ediyor; mermer taş bu tarife yabancı bir öğe.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0005` birebir aynı, `@degisim: değerli -> yumuşak` (tutuyorsan), ardından `@onarim: 133507610b884226d22735890330ef1574ad7d21`, sonra gövde.

### Hikâye 3: tohum masa-0009 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0009
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'ay', fiil 'buruşturmak', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: kurabiye sertti ve elle kırılmadı | kurabiyeyi kağıda sardı ve kağıdı kütükte buruşturdu
@tohum: masa-0009
@degisim: kararlı -> yuvarlak
Maşa ormanda bir kütüğe oturdu ve kağıda sarılı kurabiyesini açtı. Bir sincap kütüğe zıpladı ve yuvarlak, ay şeklindeki kurabiyeye baktı. Maşa kurabiyeyi sincapla paylaşmak istedi, ama kurabiye sertti. Maşa onu elleriyle kıramadı. Maşa hemen yeni bir şey denedi. Kurabiyeyi yeniden kağıda sardı. Sonra kağıdı kütüğe koydu ve iki eliyle sıkıca buruşturdu. Kağıdın içinde kurabiye çıt diye kırıldı. Maşa kağıdı açtı ve parçaların yarısını sincaba verdi. Sincap parçaları patileriyle tuttu ve hızlı hızlı yedi. Maşa da kendi parçalarını yedi. "Birlikte yemek daha güzel, sincap!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa onu elleriyle kıramadı"
   - Cümle 4: «Maşa onu elleriyle kıramadı.»
   - Açıklama: Kurabiyeyi elleriyle kıramayan Maşa aynı kurabiyeyi kağıt içinde yine elleriyle sıkarak kolayca kırıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kağıdın içinde kurabiye çıt diye kırıldı"
   - Cümle 8: «Kağıdın içinde kurabiye çıt diye kırıldı.»
   - Açıklama: Elleriyle kıramadığı sert kurabiye yine elleriyle kağıdı buruşturunca kırılıyor; çözüm akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0009` birebir aynı, `@degisim: kararlı -> yuvarlak` (tutuyorsan), ardından `@onarim: 7776d077ea1bba4661141bfc6ff1b7e124ec0f83`, sonra gövde.

### Hikâye 4: tohum masa-0011 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0011
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'beşik', fiil 'öğrenmek', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: çilekler büyük yaprakların altında görünmüyordu | yaprakları yavaşça kaldırıp çilekleri buldu
@tohum: masa-0011
@degisim: beşik -> sepet
Bir sabah Maşa bahçede tek bir kırmızı çilek fark etti. Maşa çilek reçelini çok severdi ve sepetini çilekle doldurmak istedi. Ama öteki çilekler görünmüyordu, çünkü büyük yaprakların altındaydı. Maşa yere eğildi ve bir yaprağı yavaşça kaldırdı. Altında kıpkırmızı bir çilek duruyordu! Böylece Maşa çileklerin nerede saklandığını öğrendi. Narin yaprakları ezmeden tek tek kaldırdı. Her seferinde yeni bir çilek buldu ve sepete koydu. Sepet kısa sürede çileklerle doldu. Maşa en büyük çileği hemen yedi ve mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah Maşa bahçede"
   - Cümle 1: «Bir sabah Maşa bahçede tek bir kırmızı çilek fark etti.»
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çileklerin nerede saklandığını öğrendi"
   - Cümle 6: «Böylece Maşa çileklerin nerede saklandığını öğrendi.»
   - Açıklama: Çilekler saklanmaz; fiil öznesine uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çileklerin nerede saklandığını öğrendi"
   - Cümle 6: «Böylece Maşa çileklerin nerede saklandığını öğrendi.»
   - Açıklama: Çileklerin saklanması kişileştirme ve mecaz bir kullanım.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Narin yaprakları ezmeden tek"
   - Cümle 7: «Narin yaprakları ezmeden tek tek kaldırdı.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Narin yaprakları ezmeden"
   - Cümle 7: «Narin yaprakları ezmeden tek tek kaldırdı.»
   - Açıklama: 'Narin' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0011` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: 1e5f2f02fca3cbb6869ab9935b68ea2a5c53cdd7`, sonra gövde.

### Hikâye 5: tohum masa-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0012
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tabure', fiil 'ölçmek', sıfat 'mutsuz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: kaşık ağacın yanındaki küçük bir deliğe düştü | sincaptan yardım istedi ve sincap kaşığı getirdi
@tohum: masa-0012
@degisim: tabure -> kaşık
Bir sabah Maşa ile Daşa ormanda büyük bir ağacın altında oturuyordu. Maşa reçeli çok severdi ve küçük bir kaşıkla yiyordu. Birden kaşık elinden kaydı ve ağacın yanındaki bir deliğe düştü. Delik Maşa'nın elinden çok daha küçüktü. Maşa çok mutsuz oldu. Daşa deliği iki parmağıyla ölçtü. "Benim elim de sığmaz, Maşa," dedi Daşa. O sırada ağaçtan küçük bir sincap indi. "Sincap, kaşığımı bana getirir misin?" diye sordu Maşa. Sincap hızla deliğe girdi. Biraz sonra kaşığı ağzında tutarak dışarı çıktı. "Teşekkürler, sincap!" dedi Maşa. Maşa çok sevindi, çünkü sincap kaşığını geri getirmişti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok severdi ve küçük bir kaşıkla yiyordu"
   - Cümle 2: «Maşa reçeli çok severdi ve küçük bir kaşıkla yiyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada ağaçtan küçük bir sincap indi"
   - Cümle 8: «O sırada ağaçtan küçük bir sincap indi.»
   - Açıklama: Çözümü getiren sincap tam gereken anda sebepsizce beliriyor.
   - Açıklama: Sincap tam gerektiği anda sebepsiz beliriyor ve çözümü getiriyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sincap kaşığını geri getirmişti"
   - Cümle 13: «Maşa çok sevindi, çünkü sincap kaşığını geri getirmişti.»
   - Açıklama: 'Kaşığını' sincabın kendi kaşığı gibi de okunabiliyor; kimin kaşığı olduğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0012` birebir aynı, `@degisim: tabure -> kaşık` (tutuyorsan), ardından `@onarim: 8eacc93db667b2cd3cf3b49467594f27c7f91399`, sonra gövde.

### Hikâye 6: tohum masa-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi, Daşa
@tohum: masa-0014
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kürek', fiil 'dokunmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi, Daşa
@plan: tek bir kürek vardı ve ikisi de kazmak istedi | sırayla kazdılar ve fidanı diktiler
@tohum: masa-0014
@degisim: ucuz -> küçük
Tepede serin bir rüzgar esiyordu. Maşa ile Daşa kirpiye küçük bir elma fidanı dikecekti. Ama tek bir kürek vardı ve ikisi de önce kazmak istedi. Küreği aynı anda çektiler ve kürek yere düştü. Maşa'nın yanında bir kavanoz reçel vardı. "Sırayla kazalım, Daşa, sen kazarken ben bir kaşık yiyeyim," dedi Maşa. Daşa biraz kazdı. Sonra sıra Maşa'ya geldi ve kaşığı Daşa aldı. Böyle sırayla kazdılar ve çukur hazır oldu. Fidanı çukura koyup etrafını toprakla doldurdular. Kirpi yaklaştı ve burnuyla fidana dokundu. Maşa ile Daşa çok sevindi, çünkü sırayla kazınca fidan çabucak dikilmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Daşa kirpiye küçük bir elma fidanı dikecekti"
   - Cümle 2: «Maşa ile Daşa kirpiye küçük bir elma fidanı dikecekti.»
   - Açıklama: Yönelme eki yerinde değil; 'kirpi için' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın yanında bir kavanoz reçel vardı"
   - Cümle 5: «Maşa'nın yanında bir kavanoz reçel vardı.»
   - Açıklama: Reçel kavanozu sebepsiz beliriyor ve sorunun çözümüne bir katkısı yok.
   - Açıklama: Reçel sebepsiz beliriyor ve sırayla kazma çözümü için gerekli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0014` birebir aynı, `@degisim: ucuz -> küçük` (tutuyorsan), ardından `@onarim: e7b616ee736662fa8d9a89434d17b4d34e693534`, sonra gövde.

### Hikâye 7: tohum masa-0015 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0015
- yer: dağ (Ormanın yanındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'davetiye', fiil 'yetiştirmek', sıfat 'dalgalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: rüzgar ikinci yaprağı uçurdu | yaprağın peşinden koşup onu yakaladı
@tohum: masa-0015
@degisim: yetiştirmek -> yakalamak
Tepede güneşli bir gündü. Maşa oyunda dalgalı yaprakları piknik için davetiye yapmıştı. Koca Ayı yaprağını hemen aldı, ama rüzgar ikinci yaprağı uçurdu. Yaprak otların üstünde uçup gidiyordu. Maşa önce yaprağın üstüne atlamayı denedi, ama yaprak yine uçtu. Sonra Maşa rüzgarla birlikte koştu ve yaprağı iki eliyle yakaladı. "Yakaladım!" diye bağırdı Maşa. Maşa yaprağı sincaba verdi. Sincap onu aldı ve sevinçle zıpladı. Koca Ayı da alkışladı. "Haydi, piknik başlıyor!" dedi Maşa. Sonra üçü tepede pikniğe mutlu mutlu başladı.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa oyunda dalgalı yaprakları"
   - Cümle 2: «Maşa oyunda dalgalı yaprakları piknik için davetiye yapmıştı.»
   - Açıklama: 'Oyunda' ve 'dalgalı yaprakları' bu cümlede anlamı belirsiz ve yerinde olmayan kelimeler.
   - Açıklama: 'Oyunda' burada anlamsız ve yanlış kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yaprakları piknik için davetiye yapmıştı"
   - Cümle 2: «Maşa oyunda dalgalı yaprakları piknik için davetiye yapmıştı.»
   - Açıklama: 'Davetiye' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "piknik için davetiye yapmıştı"
   - Cümle 2: «Maşa oyunda dalgalı yaprakları piknik için davetiye yapmıştı.»
   - Açıklama: 'Davetiye' 3 yaşındaki bir çocuğun bilmediği bir kelime.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar ikinci yaprağı uçurdu"
   - Cümle 3: «Koca Ayı yaprağını hemen aldı, ama rüzgar ikinci yaprağı uçurdu.»
   - Açıklama: Rüzgarın yaprağı uçurması ve hemen yakalanması önemsiz bir olay; 'dağıttı, topladı, bitti' kalıbına düşüyor.
   - Açıklama: Rüzgarın oyun yaprağını uçurup geri yakalanması önemsiz bir olay.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa önce yaprağın üstüne atlamayı denedi"
   - Cümle 5: «Maşa önce yaprağın üstüne atlamayı denedi, ama yaprak yine uçtu.»
   - Açıklama: Tohumdaki deneme özelliği işe yaramayan bir girişimde kullanılıyor; çözüm denemeyle gelmiyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa yaprağı sincaba verdi"
   - Cümle 8: «Maşa yaprağı sincaba verdi.»
   - Açıklama: Sincap hikayede hiç tanıtılmadan sebepsizce beliriyor.
   - Açıklama: Sincap daha önce hiç anılmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0015` birebir aynı, `@degisim: yetiştirmek -> yakalamak` (tutuyorsan), ardından `@onarim: dfb21e8b1b207cc792bd3c880f9317db983b6f55`, sonra gövde.

### Hikâye 8: tohum masa-0016 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0016
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'direk', fiil 'yerleştirmek', sıfat 'düz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: örtü hep kayıyordu çünkü çadırın direği çok inceydi | kalın ve düz bir dalı toprağa yerleştirdi
@tohum: masa-0016
Serin bir rüzgar esiyordu. Maşa ile kirpi ormanda reçel pikniği için çadır kuruyordu. Ama örtü hep yere kayıyordu, çünkü çadırın direği çok ince bir daldı. Maşa ince dalı yere bıraktı ve etrafa baktı. Kirpi koşup çalıların yanındaki bir dalı kokladı. Bu dal kalın ve düzdü. Maşa dalı toprağa sıkıca yerleştirdi ve örtüyü üstüne serdi. Bu kez örtü hiç kaymadı. Güzel bir çadır olmuştu. Kirpi hemen çadırın içine girdi. Maşa da onun yanına oturdu. "Teşekkürler, kirpi, çadırımız hazır!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "reçel pikniği için çadır kuruyordu"
   - Cümle 2: «Maşa ile kirpi ormanda reçel pikniği için çadır kuruyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız adı geçen bir süs olarak kalıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ormanda reçel pikniği için"
   - Cümle 2: «Maşa ile kirpi ormanda reçel pikniği için çadır kuruyordu.»
   - Açıklama: Tohumdaki reçel sevgisi yalnız adı geçen bir süs olarak kalıyor, sorunun çözümünde işe yaramıyor (kartın özellikler alanı).

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0016` birebir aynı, ardından `@onarim: 9b9575839d45e56596975449785bcc54ccf2b502`, sonra gövde.

### Hikâye 9: tohum masa-0017 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi, Daşa
@tohum: masa-0017
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'taç', fiil 'oturmak', sıfat 'harika'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi, Daşa
@plan: kirpi kütüğe çarptı ve kuzenin ekmeği toprağa düştü | kendi ekmeğini ikiye bölüp kuzeniyle paylaştı
@tohum: masa-0017
@degisim: taç -> kütük
Ormanda serin bir rüzgar esiyordu. Maşa, Daşa ve kirpi bir kütüğün yanında oturuyordu. Birden kirpi kütüğe çarptı ve Daşa'nın ekmeği toprağa düştü. Ekmek kirlendi ve Daşa çok üzüldü. Maşa'nın elinde en sevdiği reçelli ekmek vardı. Maşa onu ikiye böldü ve büyük parçayı Daşa'ya uzattı. "Al, Daşa, birlikte yiyelim," dedi Maşa. Daşa hemen bir ısırık aldı. "Harika, çok tatlı olmuş!" dedi Daşa. Kirpi de yavaşça yanlarına geldi. Maşa çok sevindi, çünkü paylaşınca ikisinin de yiyeceği olmuştu.
```

**Hakem bulguları (3):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Birden kirpi kütüğe çarptı"
   - Cümle 3: «Birden kirpi kütüğe çarptı ve Daşa'nın ekmeği toprağa düştü.»
   - Açıklama: Kirpinin kütüğe çarpması yaralanma ya da acı çağrışımı taşıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kirpi kütüğe çarptı ve Daşa'nın ekmeği toprağa düştü"
   - Cümle 3: «Birden kirpi kütüğe çarptı ve Daşa'nın ekmeği toprağa düştü.»
   - Açıklama: Kirpinin kütüğe çarpması Daşa'nın elindeki ekmeğin neden düştüğünü akla yatkın biçimde açıklamıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kirpi de yavaşça yanlarına geldi"
   - Cümle 10: «Kirpi de yavaşça yanlarına geldi.»
   - Açıklama: Kirpi zaten onlarla oturuyordu; bu cümle işlevsiz ve sebepsiz.
   - Açıklama: Kirpi zaten yanlarında oturuyordu; yeniden yanlarına gelmesi işlevsiz ve tutarsız bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0017` birebir aynı, `@degisim: taç -> kütük` (tutuyorsan), ardından `@onarim: 6ff8355484c1ec87115ec3dfbcb381b2a9732c24`, sonra gövde.

### Hikâye 10: tohum masa-0018 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0018
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'lamba', fiil 'sıkılmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: uçurtma her seferinde yere düştü çünkü kuyruğu kısaydı | kavanozdaki kurdeleyi kuyruğa bağladı
@tohum: masa-0018
@degisim: lamba -> uçurtma
Tepede güçlü bir rüzgar esiyordu. Maşa süslü uçurtmasını uçurmak istiyordu. Ama uçurtma her seferinde dönüp yere düştü, çünkü kuyruğu çok kısaydı. Maşa hiç sıkılmadı ve uçurtmaya dikkatle baktı. Maşa reçeli çok severdi ve kavanozunu tepeye de getirmişti. Kavanozun kapağına uzun, kırmızı bir kurdele bağlıydı. Maşa kurdeleyi çözdü ve uçurtmanın kuyruğuna bağladı. Uçurtma bu kez dönmedi ve yavaş yavaş yükseldi. Maşa ipi sıkıca tuttu ve sevinçle zıpladı. Kırmızı kuyruk rüzgarda sallandı. Maşa uçurtmasını tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa reçeli çok severdi ve kavanozunu tepeye de getirmişti"
   - Cümle 5: «Maşa reçeli çok severdi ve kavanozunu tepeye de getirmişti.»
   - Açıklama: Kurdeleli reçel kavanozu tam çözüm gerektiğinde sebepsizce ortaya çıkıyor ve çözümü getiriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kavanozun kapağına uzun, kırmızı bir kurdele bağlıydı"
   - Cümle 6: «Kavanozun kapağına uzun, kırmızı bir kurdele bağlıydı.»
   - Açıklama: Çözümü getiren kurdele tam gerektiği anda sebepsizce reçel kavanozunda beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0018` birebir aynı, `@degisim: lamba -> uçurtma` (tutuyorsan), ardından `@onarim: 21570f61e315c3a309442a15438e37b9c8a400f6`, sonra gövde.

### Hikâye 11: tohum masa-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0019
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çubuk', fiil 'utanmak', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ince çubuk karda yıldız çizerken kırıldı | kalın bir çubuk bulup yıldızı çizdi
@tohum: masa-0019
@degisim: utanmak -> çizmek
Ormanda her yer karla kaplıydı. Maşa karda yıldıza benzeyen kırmızı bir yaprak fark etti. Maşa da ince bir çubukla yıldız çizmek istedi, ama çubuk kırıldı. Maşa ağaçların altında yeni bir çubuk aradı. Temkinli adımlarla yürüdü, çünkü yaprağı ezmek istemiyordu. Sonunda kalın ve sağlam bir çubuk buldu. Maşa bu çubukla yeniden denedi. Çubuğu karda yavaşça çekti ve yıldızın beş ucunu çizdi. Çubuk bu kez hiç kırılmadı. Karda yaprağın yanında büyük bir yıldız vardı. Maşa çok sevindi, çünkü kocaman yıldızını sonunda çizmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çubuk karda yıldız çizerken kırıldı"
   - Cümle 0 (plan satırı): «ince çubuk karda yıldız çizerken kırıldı | kalın bir çubuk bulup yıldızı çizdi»
   - Açıklama: Plan satırında '-ken' yan cümlesinin öznesi çubuk oluyor; çubuk kendi başına yıldız çizmez.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa da ince bir çubukla"
   - Cümle 3: «Maşa da ince bir çubukla yıldız çizmek istedi, ama çubuk kırıldı.»
   - Açıklama: 'da' bağlacının bağladığı başka bir kişi ya da eylem yok; yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Temkinli adımlarla yürüdü"
   - Cümle 5: «Temkinli adımlarla yürüdü, çünkü yaprağı ezmek istemiyordu.»
   - Açıklama: 'Temkinli' kelimesini 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0019` birebir aynı, `@degisim: utanmak -> çizmek` (tutuyorsan), ardından `@onarim: efdc8cd7b718823ea8eadd73198af0447304a8af`, sonra gövde.

### Hikâye 12: tohum masa-0021 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0021
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'ayakkabı', fiil 'sektirmek', sıfat 'devasa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: top fındık sepetini devirdi ve fındıklar döküldü | özür diledi ve fındıkları yeniden topladı
@tohum: masa-0021
@degisim: ayakkabı -> top
Maşa ormanda devasa bir ağacın yanında top sektiriyordu. Koca Ayı ile sincap da yakında bir sepete fındık topluyordu. Maşa topa çok sert vurdu ve top gidip fındık sepetini devirdi. Fındıklar yere döküldü ve sincap üzüldü. "Özür dilerim, sincap, dikkat etmedim," dedi Maşa. Sonra Maşa yere eğildi ve fındıkları tek tek topladı. Koca Ayı da ona yardım etti. Kısa sürede sepet yine fındıkla doldu. Sincap sevinçle kuyruğunu salladı. Sonra üçü Maşa'nın reçelini mutlu mutlu paylaştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormanda devasa bir ağacın"
   - Cümle 1: «Maşa ormanda devasa bir ağacın yanında top sektiriyordu.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmediği bir kelime; 'kocaman' olmalı.
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra üçü Maşa'nın reçelini mutlu mutlu paylaştı"
   - Cümle 10: «Sonra üçü Maşa'nın reçelini mutlu mutlu paylaştı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız sona eklenmiş.
   - Açıklama: Tohumdaki reçel özelliği yalnız sonda anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın reçelini mutlu mutlu paylaştı"
   - Cümle 10: «Sonra üçü Maşa'nın reçelini mutlu mutlu paylaştı.»
   - Açıklama: Reçel daha önce hiç kurulmadan sebepsizce beliriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "üçü Maşa'nın reçelini mutlu mutlu paylaştı"
   - Cümle 10: «Sonra üçü Maşa'nın reçelini mutlu mutlu paylaştı.»
   - Açıklama: Reçel hikayede hiç kurulmadan son cümlede sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0021` birebir aynı, `@degisim: ayakkabı -> top` (tutuyorsan), ardından `@onarim: 28573af19a31db7d90cb5691e40ebd7bb0074952`, sonra gövde.
