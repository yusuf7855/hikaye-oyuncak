# Editör görevi (onarım): Maşa, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0010 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0010
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'vazo', fiil 'durdurmak', sıfat 'şık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: vazoya düşen kirpi dışarı çıkamadı | vazoyu yavaşça eğdi ve kirpi dışarı kaydı
@tohum: masa-0010
@degisim: şık -> boş
Rüzgar hızlı hızlı esiyordu. Maşa evinin önünde zıplarken çimenlerdeki boş vazodan bir ses duydu. Bir kirpi vazoya bakarken içine düşmüştü. Vazonun içi kaygandı ve kirpi dışarı çıkamıyordu. Maşa hemen zıplamayı durdurdu ve vazonun yanına koştu. "Bekle, kirpi, sana yardım edeceğim," dedi Maşa. Maşa vazonun dibini yavaşça yukarı kaldırmayı denedi. Vazonun ağzı çimenlere doğru eğildi. Kirpi yavaş yavaş kaydı ve çimenlerin üstüne çıktı. Kirpi küçük burnunu kıpırdattı ve Maşa'ya baktı. "Oldu, kirpi, artık çıktın!" dedi Maşa. Sonra boş vazoyu dikkatle yerine koydu. Kirpi de çimenlerde mutlu mutlu dolaştı. Maşa çok sevindi, çünkü kirpiyi vazodan çıkarmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar hızlı hızlı esiyordu"
   - Cümle 1: «Rüzgar hızlı hızlı esiyordu.»
   - Açıklama: Hızlı esen rüzgar önemli bir şeymiş gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0010` birebir aynı, `@degisim: şık -> boş` (tutuyorsan), ardından `@onarim: ae60bcafc7da7ab4d38a8656cafd3e0d424c35f9`, sonra gövde.

### Hikâye 2: tohum masa-0011 (deneme 3 -> 4)

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
Bir sabah Maşa evinin önündeki bahçede tek bir kırmızı çilek fark etti. Maşa çilek reçelini çok severdi ve sepetini çilekle doldurmak istedi. Ama öteki çilekler görünmüyordu, çünkü büyük yaprakların altındaydı. Maşa yere eğildi ve bir yaprağı yavaşça kaldırdı. Altında kıpkırmızı bir çilek duruyordu! Böylece Maşa çileklerin yaprakların altında olduğunu öğrendi. Yapraklar ince ve narindi, Maşa onları ezmeden tek tek kaldırdı. Her seferinde yeni bir çilek buldu ve sepete koydu. Sepet kısa sürede çileklerle doldu. Maşa en büyük çileği hemen yedi ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Böylece Maşa çileklerin yaprakların altında olduğunu öğrendi"
   - Cümle 6: «Böylece Maşa çileklerin yaprakların altında olduğunu öğrendi.»
   - Açıklama: Çileklerin yaprakların altında olduğu 3. cümlede zaten söylenmişti; gereksiz tekrar.
   - Açıklama: Çileklerin yaprak altında olduğu 3. cümlede zaten söylendi; gereksiz tekrar.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yapraklar ince ve narindi"
   - Cümle 7: «Yapraklar ince ve narindi, Maşa onları ezmeden tek tek kaldırdı.»
   - Açıklama: 'Narin' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Narin' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0011` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: f2960d1813cfe3b15888ff5010497616b2c55187`, sonra gövde.

### Hikâye 3: tohum masa-0012 (deneme 2 -> 3)

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
Bir sabah Maşa ile Daşa ormanda büyük bir ağacın altında oturuyordu. Maşa reçeli çok severdi ve küçük bir kaşıkla yiyordu. Dalda küçük bir sincap reçelin kokusunu almış, aşağı bakıyordu. Birden kaşık Maşa'nın elinden kaydı ve ağacın yanındaki bir deliğe düştü. Delik Maşa'nın elinden çok daha küçüktü. Maşa çok mutsuz oldu. Daşa deliği iki parmağıyla ölçtü. "Benim elim de sığmaz, Maşa," dedi Daşa. "Sincap, kaşığımı bana getirir misin?" diye sordu Maşa. Sincap hızla indi ve deliğe girdi. Biraz sonra kaşığı ağzında tutarak dışarı çıktı. "Teşekkürler, sincap!" dedi Maşa. Maşa çok sevindi, çünkü sincap onun kaşığını geri getirmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok severdi"
   - Cümle 2: «Maşa reçeli çok severdi ve küçük bir kaşıkla yiyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız kartta yazdığı gibi söylenip geçiyor, sorunun çözümünde işe yaramıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Birden kaşık Maşa'nın elinden kaydı ve ağacın yanındaki bir deliğe düştü.»
   - Açıklama: Sorun, kaşığın deliğe düşmesi, ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0012` birebir aynı, `@degisim: tabure -> kaşık` (tutuyorsan), ardından `@onarim: 8b603abe1d2ad6db065354330b6b84019b17d679`, sonra gövde.

### Hikâye 4: tohum masa-0014 (deneme 2 -> 3)

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
Tepede serin bir rüzgar esiyordu. Maşa ile Daşa kirpi için küçük bir elma fidanı dikecekti. Ama tek bir kürek vardı ve ikisi de önce kazmak istedi. Küreği aynı anda çektiler ve kürek yere düştü. "Sırayla kazalım, Daşa, sen kazarken ben reçelimden bir kaşık yiyeyim," dedi Maşa. Daşa biraz kazdı ve Maşa reçelini yedi. Sonra sıra Maşa'ya geldi ve kaşığı Daşa aldı. Böyle sırayla kazdılar ve çukur hazır oldu. Fidanı çukura koyup etrafını toprakla doldurdular. Kirpi yaklaştı ve burnuyla fidana dokundu. Maşa ile Daşa çok sevindi, çünkü sırayla kazınca fidan çabucak dikilmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben reçelimden bir kaşık yiyeyim"
   - Cümle 5: «"Sırayla kazalım, Daşa, sen kazarken ben reçelimden bir kaşık yiyeyim," dedi Maşa.»
   - Açıklama: Tohumdaki reçel özelliği iki kez süs olarak geçiyor, sorunu çözen sıraya bir katkısı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ben reçelimden bir kaşık yiyeyim"
   - Cümle 5: «"Sırayla kazalım, Daşa, sen kazarken ben reçelimden bir kaşık yiyeyim," dedi Maşa.»
   - Açıklama: Reçel ve kaşık sebepsiz beliriyor ve sorunun çözümünde hiçbir işe yaramıyor.
   - Açıklama: Reçel ve kaşık hiç kurulmadan sebepsizce beliriyor ve sorunun çözümüne hiçbir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0014` birebir aynı, `@degisim: ucuz -> küçük` (tutuyorsan), ardından `@onarim: bea2b465ee5d1d82e81bfb526a15cf647d894c94`, sonra gövde.

### Hikâye 5: tohum masa-0016 (deneme 2 -> 3)

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
Serin bir rüzgar esiyordu. Maşa reçelini gölgede yemek istedi ve kirpiyle ormanda çadır kurdu. Ama örtü hep yere kayıyordu, çünkü çadırın direği çok ince bir daldı. Maşa ince dalı yere bıraktı ve etrafa baktı. Kirpi koşup çalıların yanındaki bir dalı kokladı. Bu dal kalın ve düzdü. Maşa dalı toprağa sıkıca yerleştirdi ve örtüyü üstüne serdi. Bu kez örtü hiç kaymadı. Güzel bir çadır olmuştu. Kirpi hemen çadırın içine girdi. Maşa da reçeliyle onun yanına oturdu. "Teşekkürler, kirpi, çadırımız hazır!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "reçelini gölgede yemek istedi"
   - Cümle 2: «Maşa reçelini gölgede yemek istedi ve kirpiyle ormanda çadır kurdu.»
   - Açıklama: Serin rüzgarlı bir havada gölge arayıp çadır kurmak çelişkili bir gerekçe.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kirpi koşup çalıların yanındaki bir dalı kokladı"
   - Cümle 5: «Kirpi koşup çalıların yanındaki bir dalı kokladı.»
   - Açıklama: Çözümü getiren kalın dalı Maşa istemeden kirpi buluyor; figür yalnız yerleştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0016` birebir aynı, ardından `@onarim: 77dc88847d609e195fc8414588660a0ba0f65e53`, sonra gövde.

### Hikâye 6: tohum masa-0017 (deneme 2 -> 3)

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
@plan: kirpi kütüğe çıkarken ekmeği itti ve ekmek toprağa düştü | kendi ekmeğini kuzeniyle paylaştı
@tohum: masa-0017
@degisim: taç -> kütük
Ormanda serin bir rüzgar esiyordu. Maşa, Daşa ve kirpi bir kütüğün yanında oturuyordu. Kirpi kütüğe çıkarken, orada duran Daşa'nın ekmeğini itti. Ekmek toprağa düştü ve kirlendi, Daşa çok üzüldü. Maşa'nın elinde en sevdiği reçelli ekmek vardı. Maşa onu ikiye böldü ve büyük parçayı Daşa'ya uzattı. "Al, Daşa, birlikte yiyelim," dedi Maşa. Daşa hemen bir ısırık aldı. "Harika, çok tatlı olmuş!" dedi Daşa. Maşa çok sevindi, çünkü paylaşınca ikisinin de yiyeceği olmuştu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ekmek toprağa düştü ve kirlendi"
   - Cümle 4: «Ekmek toprağa düştü ve kirlendi, Daşa çok üzüldü.»
   - Açıklama: Asıl sorun olan ekmeğin toprağa düşüp kirlenmesi ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0017` birebir aynı, `@degisim: taç -> kütük` (tutuyorsan), ardından `@onarim: 92f4bfd770b9f2a2540ddad3ff4e3feb336d2e4c`, sonra gövde.

### Hikâye 7: tohum masa-0019 (deneme 2 -> 3)

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
@plan: karda yıldız çizmek istedi ama ince çubuk kırıldı | kalın bir çubuk bulup yıldızı çizdi
@tohum: masa-0019
@degisim: utanmak -> çizmek
Ormanda her yer karla kaplıydı. Maşa karda yıldıza benzeyen kırmızı bir yaprak fark etti. Maşa karda ince bir çubukla yıldız çizmek istedi, ama çubuk kırıldı. Maşa ağaçların altında yeni bir çubuk aradı. Yaprağı ezmemek için yavaş ve temkinli yürüdü. Sonunda kalın ve sağlam bir çubuk buldu. Maşa bu çubukla yeniden denedi. Çubuğu karda yavaşça çekti ve yıldızın beş ucunu çizdi. Çubuk bu kez hiç kırılmadı. Karda yaprağın yanında büyük bir yıldız vardı. Maşa çok sevindi, çünkü kocaman yıldızını sonunda çizmişti.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yıldıza benzeyen kırmızı bir yaprak"
   - Cümle 2: «Maşa karda yıldıza benzeyen kırmızı bir yaprak fark etti.»
   - Açıklama: Karın ortasında kırmızı yaprak sebepsiz beliriyor ve çözümde hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yavaş ve temkinli yürüdü"
   - Cümle 5: «Yaprağı ezmemek için yavaş ve temkinli yürüdü.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmediği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yaprağı ezmemek için yavaş ve temkinli yürüdü"
   - Cümle 5: «Yaprağı ezmemek için yavaş ve temkinli yürüdü.»
   - Açıklama: Kırmızı yaprak önemliymiş gibi kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Yıldıza benzeyen kırmızı yaprak önemliymiş gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0019` birebir aynı, `@degisim: utanmak -> çizmek` (tutuyorsan), ardından `@onarim: 3c71131ab4bb14a1e1abc50fcbc8ef4a32cafff0`, sonra gövde.

### Hikâye 8: tohum masa-0021 (deneme 2 -> 3)

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
@degisim: devasa -> kocaman
Maşa reçelini kocaman bir ağacın dibine koydu ve top sektirmeye başladı. Koca Ayı ile sincap da yakında bir sepete fındık topluyordu. Maşa topa ayakkabısıyla çok sert vurdu ve top sepeti devirdi. Fındıklar yere döküldü ve sincap üzüldü. "Özür dilerim, sincap, dikkat etmedim," dedi Maşa. Sonra Maşa yere eğildi ve fındıkları tek tek topladı. Koca Ayı da ona yardım etti. Kısa sürede sepet yine fındıkla doldu. Sincap sevinçle kuyruğunu salladı. Maşa en sevdiği reçeli getirdi ve üçü onu mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "da yakında bir sepete"
   - Cümle 2: «Koca Ayı ile sincap da yakında bir sepete fındık topluyordu.»
   - Açıklama: 'Yakında' zaman anlamıyla karışıyor; yer için 'yakınlarda' ya da 'yanda' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa en sevdiği reçeli getirdi"
   - Cümle 10: «Maşa en sevdiği reçeli getirdi ve üçü onu mutlu mutlu paylaştı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız başta ve sonda süs olarak iki kez geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0021` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: 1d0fbf012aad382d22e21517dc49ce148842d7f0`, sonra gövde.

### Hikâye 9: tohum masa-0022 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0022
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'mobilya', fiil 'girmek', sıfat 'keyifli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kulübenin kapısı çok küçüktü ve içeri giremedi | kapının iki yanındaki dalları kenara çekmeyi denedi
@tohum: masa-0022
@degisim: mobilya -> dal
Bir sabah Maşa ormanda kuru dallardan küçük bir kulübe yaptı. Maşa kulübenin içinde oynamak istiyordu. Ama kapı çok küçüktü ve Maşa içeri giremedi. Maşa kapıya baktı ve biraz düşündü. Sonra kapının iki yanındaki dalları yavaşça kenara çekmeyi denedi. Dallar kolayca kenara gitti. Kapı şimdi daha büyüktü. Maşa bu kez rahatça içeri girdi. İçerisi serin ve çok keyifliydi. Maşa yumuşak yaprakların üstüne oturdu. Maşa çok sevindi, çünkü kendi yaptığı kulübeye sonunda girmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dallar kolayca kenara gitti"
   - Cümle 6: «Dallar kolayca kenara gitti.»
   - Açıklama: Dallar kendiliğinden gitmez; 'kenara çekildi/kaydı' olmalı.
   - Açıklama: Dallar kendiliğinden gitmez; 'kenara açıldı/çekildi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0022` birebir aynı, `@degisim: mobilya -> dal` (tutuyorsan), ardından `@onarim: f036241e8be6b00d51dc1abdf7242ece2463eb26`, sonra gövde.

### Hikâye 10: tohum masa-0023 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap, Daşa
@tohum: masa-0023
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'düdük', fiil 'yorulmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | sincap, Daşa
@plan: yorulunca kuzeninin ekmeğini sormadan yedi | özür diledi ve ona reçelli yeni bir ekmek getirdi
@tohum: masa-0023
Bahçede bir düdük ötüyordu. Maşa düdük çalarak sincapla ağaçların arasında yarışıyordu. Maşa çok yoruldu ve Daşa'nın masadaki reçelli ekmeğini sormadan yedi. Biraz sonra Daşa bahçeye geldi ve boş tabağa baktı. "Ekmeğim nerede, Maşa?" diye sordu Daşa. Maşa'nın yüzü kıpkırmızı oldu. "Özür dilerim, Daşa, ekmeğini ben yedim," dedi Maşa. Maşa hemen mutfağa koştu. Yeni bir ekmek aldı ve en sevdiği çilek reçelinden bol bol sürdü. Ekmeği iki eliyle Daşa'ya getirdi. "Teşekkür ederim, Maşa," dedi Daşa ve gülümsedi. Sonra Maşa, Daşa ve sincap bahçede hep birlikte mutlu mutlu yarıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bahçede bir düdük ötüyordu"
   - Cümle 1: «Bahçede bir düdük ötüyordu.»
   - Açıklama: Düdük kendiliğinden ötüyormuş gibi kuruluyor ve olayda hiçbir işe yaramıyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede bir düdük ötüyordu"
   - Cümle 1: «Bahçede bir düdük ötüyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve mutfağa geçiyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa hemen mutfağa koştu"
   - Cümle 8: «Maşa hemen mutfağa koştu.»
   - Açıklama: Sahne bahçeden mutfağa değişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0023` birebir aynı, ardından `@onarim: 233e5f84db4c22f5c3f33d0f01ed82899f06263f`, sonra gövde.

### Hikâye 11: tohum masa-0029 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0029
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'fırça', fiil 'aramak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: yağmur dinmişti ama fırça yine ıslanıyordu | yukarı bakıp damlayan dalı buldu ve fırçayı taşıdı
@tohum: masa-0029
Bir sabah Maşa bahçede resim yapmak istedi. Ama masadaki fırçası sırılsıklamdı. Yağmur çoktan dinmişti ama fırça yine ıslanıyordu. Maşa bu suyun nereden geldiğini merak etti ve aramaya başladı. Önce masanın altına baktı ama orada bir şey yoktu. Sonra masanın yanına uzandı ve yukarıya bakmayı denedi. Masanın üstünde ağacın yapraklı bir dalı vardı. Rüzgar esince yapraklardan fırçanın üstüne damlalar düştü. Su, yapraklarda kalan yağmurdan geliyordu. Maşa kağıdını ve fırçasını güneşli bir köşeye taşıdı. Fırça güneşte kurudu ve Maşa resmine başladı. Maşa bundan sonra ıslak bir şey görünce önce yukarıya baktı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce masanın altına baktı"
   - Cümle 5: «Önce masanın altına baktı ama orada bir şey yoktu.»
   - Açıklama: Çözüm masanın altına bakma, yukarı bakma ve eşyaları taşıma olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0029` birebir aynı, ardından `@onarim: 0090855102209ce7447ba1a2fb2be118446fe119`, sonra gövde.

### Hikâye 12: tohum masa-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0030
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'gözlük', fiil 'köpürmek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: çimenlerde bir şey parladı ve sonra kayboldu | ilk durduğu yere dönüp oradan baktı ve yürüdü
@tohum: masa-0030
@degisim: köpürmek -> parlamak
Maşa tepede koşup oynuyordu. Birden çimenlerin arasında bir şey parladı. Maşa bu parlayan şeyin ne olduğunu çok merak etti. Hemen ışığa doğru koştu ama ışık kayboldu. Maşa ilk durduğu yere döndü ve oradan bakmayı denedi. Işık yine parladı. Maşa bu kez ışığa bakarak yavaş yavaş yürüdü. Çimenlerin arasında Maşa'nın kayıp pembe oyuncak gözlüğü vardı. Gözlüğün bir camı eksikti ve öbür camı güneşte parlıyordu. Maşa gözlüğü hemen taktı ve güldü. Maşa çok sevindi, çünkü hem ışığı hem de gözlüğünü bulmuştu.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama ışık kayboldu"
   - Cümle 4: «Hemen ışığa doğru koştu ama ışık kayboldu.»
   - Açıklama: Işığın kaybolması sorunu ilk 3 cümlede değil 4. cümlede ortaya çıkıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hemen ışığa doğru koştu ama ışık kayboldu"
   - Cümle 4: «Hemen ışığa doğru koştu ama ışık kayboldu.»
   - Açıklama: Işığın neden kaybolduğu hiç söylenmiyor.
   - Açıklama: Işığın neden kaybolduğu ve ilk yerden neden yeniden göründüğü hiç söylenmiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa gözlüğü hemen taktı"
   - Cümle 10: «Maşa gözlüğü hemen taktı ve güldü.»
   - Açıklama: Bir camı eksik, kırık olabilecek gözlüğü hemen takmak çocuğun taklit edebileceği, kesilme riski taşıyan bir davranış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hem ışığı hem de gözlüğünü bulmuştu"
   - Cümle 11: «Maşa çok sevindi, çünkü hem ışığı hem de gözlüğünü bulmuştu.»
   - Açıklama: Işık ayrı bir şey değil, camın parıltısıdır; 'ışığı bulmak' kelimeyi yanlış anlamda kullanıyor.
   - Açıklama: Işık bulunacak bir nesne değil; 'ışığı bulmak' yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0030` birebir aynı, `@degisim: köpürmek -> parlamak` (tutuyorsan), ardından `@onarim: e366ee844ce9210bb68867ae35c730bcdc30cd9b`, sonra gövde.
