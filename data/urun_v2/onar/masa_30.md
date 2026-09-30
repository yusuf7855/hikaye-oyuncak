# Editör görevi (onarım): Maşa, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0038 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0038
- yer: dağ (Ormanın yanındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bilezik', fiil 'dağılmak', sıfat 'değişik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: sepet devrildi ve elmalar tepeden aşağı dağıldı | sepete ağır reçel kavanozu koydu ve elmaları topladı
@tohum: masa-0038
@degisim: bilezik -> sepet
Tepede güneş parlıyordu. Maşa, Koca Ayı ve kirpi çimenlerde elma ile reçel yiyordu. Ama kirpi elma sepetine dayandı ve sepet devrildi. Değişik renkli elmalar tepeden aşağı yuvarlandı ve çimenlere dağıldı. Kirpi üzgün üzgün başını eğdi. "Üzülme, kirpi, elmaları birlikte toplarız!" dedi Maşa. Maşa önce ağır reçel kavanozunu sepetin dibine koydu. Sonra elmaları tek tek topladı ve sepete koydu. Koca Ayı da ona yardım etti. Kirpi sepete yine dayandı ama sepet bu kez devrilmedi. Kirpi bir elma aldı ve mutlu mutlu yedi. Maşa çok sevindi, çünkü bütün elmalar yine sepetteydi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa önce ağır reçel kavanozunu sepetin dibine koydu"
   - Cümle 7: «Maşa önce ağır reçel kavanozunu sepetin dibine koydu.»
   - Açıklama: Tohum özelliği 'tatlıları ve reçeli çok sever' iken reçel yalnız ağırlık olarak kullanılıyor, özellik işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0038` birebir aynı, `@degisim: bilezik -> sepet` (tutuyorsan), ardından `@onarim: 2c1b7e985cfe3f7950953ad7939546693cc2fab4`, sonra gövde.

### Hikâye 2: tohum masa-0043 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0043
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'güneş', fiil 'çalıştırmak', sıfat 'resimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: müzik kutusu çalmadı ve içinden tık tık sesi geldi | kutunun kapağını açıp içindeki taşı çıkardı
@tohum: masa-0043
Maşa güneşli bir sabah Koca Ayı'nın evinin önündeki bahçedeydi. Resimli müzik kutusuyla Koca Ayı ile dans etmek istiyordu. Ama Maşa kutunun kolunu çevirince müzik çalmadı. İçinden tık tık diye bir ses geldi. Maşa bu sesi çok merak etti. Kutunun altındaki küçük kapağı açmayı denedi. Kapak açıldı ve içinden küçük bir taş düştü. "Koca Ayı, bak, kutunun içine taş girmiş!" dedi Maşa. Koca Ayı taşa baktı ve başını salladı. Maşa kolu yeniden çevirdi ve kutuyu çalıştırdı. Bu kez güzel bir şarkı başladı. Maşa ile Koca Ayı bahçede mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Koca Ayı'nın evinin önündeki bahçedeydi"
   - Cümle 1: «Maşa güneşli bir sabah Koca Ayı'nın evinin önündeki bahçedeydi.»
   - Açıklama: Başlıktaki yer ev ama hikaye evin dışındaki bahçede geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0043` birebir aynı, ardından `@onarim: efad3e716e5ee8cc17da4c1dca35bb248747d515`, sonra gövde.

### Hikâye 3: tohum masa-0077 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi, Daşa
@tohum: masa-0077
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'reçel', fiil 'parıldamak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi, Daşa
@plan: reçel kavanozunun kapağı çok sıkıydı ve açılmadı | kuzeninden yardım isteyip kapağı birlikte açtı
@tohum: masa-0077
@degisim: meşgul -> kalın
Maşa evinin önünde kirpiye bir elma getirmişti. Elmanın üstüne en sevdiği reçelden koymak istedi. Ama kavanozun kapağı çok sıkıydı ve açılmadı. Maşa kapağı iki eliyle çevirdi ama kapak dönmedi. Daşa yakında oturmuş, kalın bir kitap okuyordu. "Daşa, bu kapağı açmama yardım eder misin?" diye sordu Maşa. Daşa kitabını bıraktı ve kavanozu sıkıca tuttu. Maşa kapağı bir kez daha çevirdi. Kapak birden açıldı. Kırmızı reçel güneşte parıldadı. Maşa elmanın üstüne biraz reçel koydu ve kirpiye verdi. Kirpi elmayı yedi ve sevinçle burnunu oynattı. "Teşekkürler, Daşa!" dedi Maşa. Maşa bundan sonra kapak açılmayınca Daşa'dan yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra kapak açılmayınca Daşa'dan yardım istedi"
   - Cümle 14: «Maşa bundan sonra kapak açılmayınca Daşa'dan yardım istedi.»
   - Açıklama: Alışkanlık anlatan cümlede '-dı' kullanımı bozuk; 'yardım isterdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0077` birebir aynı, `@degisim: meşgul -> kalın` (tutuyorsan), ardından `@onarim: 85d2c477660d8001597ec43bed17e375f75daaee`, sonra gövde.

### Hikâye 4: tohum masa-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0079
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pilav', fiil 'kucaklamak', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: pilavı koyduğu ince yaprak yırtıldı ve pilav döküldü | pilavı boş reçel kavanozuna doldurup sofraya taşıdı
@tohum: masa-0079
Maşa ormanda yemek oyunu oynuyordu ve bir kütüğe sofra kurmuştu. Beyaz taşlardan pilav yaptı ve pilavı temiz bir yaprağa koydu. Ama yaprak çok inceydi, yırtıldı ve pilav yere döküldü. Maşa taşları tek tek topladı. Sonra yanındaki boş reçel kavanozunu gördü. Maşa en sevdiği reçeli az önce bitirmişti. Taşları bu kavanoza doldurdu. Kavanoz sağlamdı ve hiçbir taş dökülmedi. Maşa kavanozu sevinçle kucakladı ve kütüğe taşıdı. Kavanozu sofranın ortasına koydu. Sofra artık hazırdı. Maşa bundan sonra pilavını hep kavanoza koydu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yanındaki boş reçel kavanozunu gördü"
   - Cümle 5: «Sonra yanındaki boş reçel kavanozunu gördü.»
   - Açıklama: Kavanoz daha önce kurulmadan tam çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0079` birebir aynı, ardından `@onarim: 45e002551badf98a2b1bb24d106ccaf1c8878812`, sonra gövde.

### Hikâye 5: tohum masa-0080 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0080
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'süs', fiil 'kurulamak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: reçel kavanozu ıslak çimenlerde kayboldu | reçelin kokusunu alıp kavanozu çalının altında buldu
@tohum: masa-0080
@degisim: süs -> örtü
Bir sabah Maşa ile kuzeni Daşa tepede piknik yapıyordu. Daşa tuzlu ekmekleri örtünün üstüne koydu. Ama Maşa'nın reçel kavanozu örtüden kaymış ve ıslak çimenlerde kaybolmuştu. "Reçelim nerede?" diye sordu Maşa. Daşa çimenlere uzun uzun baktı ama kavanozu göremedi. O sırada küçük bir sincap bir çalının yanında burnunu oynatıyordu. Maşa oraya koştu ve havayı derin derin kokladı. Reçeli çok severdi ve tatlı kokusunu hemen tanıdı. Koku çalının altından geliyordu. Maşa eğildi ve kavanozu orada buldu. Kavanoz çimenlerde ıslanmıştı, Daşa onu örtünün ucuyla kuruladı. "Teşekkürler, sincap!" dedi Maşa. Maşa ile Daşa çok sevindi, çünkü kaybolan reçeli sincabın yardımıyla bulmuşlardı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "küçük bir sincap bir çalının yanında burnunu oynatıyordu"
   - Cümle 6: «O sırada küçük bir sincap bir çalının yanında burnunu oynatıyordu.»
   - Açıklama: Sincap sebepsizce beliriyor ve çözümde açık bir işlevi olmadığı halde ona teşekkür ediliyor.
   - Açıklama: Sincap sebepsizce tam kavanozun yanında beliriyor ve sona sincabın yardımı diye bağlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tatlı kokusunu hemen tanıdı"
   - Cümle 8: «Reçeli çok severdi ve tatlı kokusunu hemen tanıdı.»
   - Açıklama: Çimende kaybolan kavanozun kokusunun sezilmesi ve yanında beliren sincap çözümü sebepsizce getiriyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kaybolan reçeli sincabın yardımıyla bulmuşlardı"
   - Cümle 13: «Maşa ile Daşa çok sevindi, çünkü kaybolan reçeli sincabın yardımıyla bulmuşlardı.»
   - Açıklama: Maşa kavanozu kendi burnuyla kokuyu izleyerek buluyor, ama son cümle bulmayı hiçbir şey yapmayan sincabın yardımına bağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0080` birebir aynı, `@degisim: süs -> örtü` (tutuyorsan), ardından `@onarim: a2aba0914c9f39635f8099cdc688212ad3819efa`, sonra gövde.

### Hikâye 6: tohum masa-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap
@tohum: masa-0081
- yer: dağ (Ormanın yanındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'ekmek', fiil 'guruldamak', sıfat 'renkli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | sincap
@plan: sofra taşın arkasındaydı ve sincap onu bulamadı | fındıkları yere koyup sincaba yol yaptı
@tohum: masa-0081
@degisim: ekmek -> fındık
Tepede rüzgar hafif hafif esiyordu. Maşa sincaba bir taşın arkasında sürpriz bir sofra hazırlamıştı. Ama sincap taşın arkasını göremedi ve sofrayı bulamadı. Sincabın karnı yüksek sesle guruldadı. Maşa hemen yeni bir şey denedi. Birkaç fındık aldı ve onları yere tek tek koydu. Fındıklar sincabın önünden taşın arkasına kadar uzandı. Sincap ilk fındığı buldu ve yedi. Sonra öbür fındıkları da yiyerek taşa doğru gitti. Taşın arkasında renkli yapraklarla süslü sofrayı gördü. "Sürpriz, sincap, bu sofra senin için!" dedi Maşa. Sincap sevinçle kuyruğunu salladı. Maşa ile sincap sofrada mutlu mutlu yemek yedi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Fındıklar sincabın önünden taşın"
   - Cümle 7: «Fındıklar sincabın önünden taşın arkasına kadar uzandı.»
   - Açıklama: Tek tek konmuş fındıklar için 'uzandı' fiili öznesine tam uymuyor; 'fındık sırası uzandı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0081` birebir aynı, `@degisim: ekmek -> fındık` (tutuyorsan), ardından `@onarim: b2371de21c711a3208e017973cab3bba17481394`, sonra gövde.

### Hikâye 7: tohum masa-0083 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0083
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kemer', fiil 'sallamak', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: kavanozdaki çiçek gölgede kaldı ve açılmadı | kavanozu sepetle güneşli bir yere taşıdı
@tohum: masa-0083
@degisim: kemer -> sepet
Hava aydınlıktı ve evin önünde kuşlar ötüyordu. Maşa ile kirpi kavanozdaki kırmızı çiçeğin açılmasını bekliyordu. Ama kavanoz ağacın gölgesinde kalmıştı ve çiçek açılmıyordu. Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu. Kavanoz küçük ve hafifti. Maşa kavanozu sepetine koydu. Sonra sepeti güneşli bir yere taşıdı. İkisi kavanozun yanına oturup sessizce bekledi. Güneş çiçeği ısıttı. Kırmızı çiçek yavaş yavaş açıldı. "Bak, kirpi, çiçek açıldı!" dedi Maşa. Kirpi çiçeği kokladı ve sevinçle başını salladı. Maşa ile kirpi çiçeğin yanında mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu"
   - Cümle 4: «Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa'nın en sevdiği reçelin boş kavanozuydu"
   - Cümle 4: «Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu"
   - Cümle 4: «Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu.»
   - Açıklama: Reçel kavanozu ayrıntısı işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın en sevdiği reçelin boş kavanozuydu"
   - Cümle 4: «Bu, Maşa'nın en sevdiği reçelin boş kavanozuydu.»
   - Açıklama: Kavanozun reçel kavanozu olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0083` birebir aynı, `@degisim: kemer -> sepet` (tutuyorsan), ardından `@onarim: eb613a9a3461500a6d92249195b203692fb6ec76`, sonra gövde.

### Hikâye 8: tohum masa-0085 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0085
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kütük', fiil 'örtmek', sıfat 'yeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: sepetteki elmalar tek tek kayboldu | küçük izlere bakıp kirpiyi buldu
@tohum: masa-0085
Maşa ile Koca Ayı ormanda elma topluyordu. Ama sepetteki elmalar tek tek kayboluyordu. "Koca Ayı, elmalar nereye gidiyor?" diye sordu Maşa. Koca Ayı başını iki yana salladı. Maşa yerde küçük izler gördü ve peşinden koştu. İzler eski bir kütükte bitiyordu. Yeşil yapraklar kütüğün deliğini örtmüştü. Maşa deliğe baktı ama içini göremedi. Sonra yeni bir şey denedi ve yaprakları tek tek kaldırdı. Deliğin içinde küçük bir kirpi vardı. Kirpinin yanında kayıp elmalar duruyordu. "Elmaları sen aldın, kirpi!" dedi Maşa ve güldü. Koca Ayı kirpiye bir elma verdi. Maşa çok sevindi, çünkü elmaların nereye gittiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "izler gördü ve peşinden koştu"
   - Cümle 5: «Maşa yerde küçük izler gördü ve peşinden koştu.»
   - Açıklama: Tamlayan eksik; çoğul 'izler' için 'izlerin peşinden' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0085` birebir aynı, ardından `@onarim: d1c53a2c589d8e1ff094ce124fc4c13be7f21baf`, sonra gövde.

### Hikâye 9: tohum masa-0086 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0086
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'düğüm', fiil 'uzaklaşmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: atlama ipi ayağına dolandı ve düğüm oldu | kuzeninin arkasından koşup ondan yardım istedi
@tohum: masa-0086
Bir sabah Maşa evin önünde ip atlıyordu. Birden ip ayağına dolandı ve ortasında sıkı bir düğüm oldu. Maşa iki ucu da çekti ama düğüm daha çok sıkıştı. O sırada Daşa kitabını alıp eve doğru uzaklaşıyordu. Maşa yeni bir şey denedi ve Daşa'nın arkasından koştu. Ondan yardım istedi ve düğümü gösterdi. Daşa ipi elinde dikkatle çevirdi. Sonra düğümün içinde gizli kalmış küçük bir ucu gösterdi. Maşa o ucu yavaşça çekti ve düğüm çözüldü. Maşa sevinçle zıpladı ve Daşa'ya sarıldı. Daşa da kitabını bir kenara bıraktı. İkisi sırayla ip atlayıp mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "düğümün içinde gizli kalmış küçük bir ucu"
   - Cümle 8: «Sonra düğümün içinde gizli kalmış küçük bir ucu gösterdi.»
   - Açıklama: Maşa ipin iki ucunu da elinde tutup çekmişken düğümün içinde gizli bir uç bulunması çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0086` birebir aynı, ardından `@onarim: fe0821923fb664d6a45de73d7d167b93bb55a40c`, sonra gövde.

### Hikâye 10: tohum masa-0090 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0090
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çarşaf', fiil 'sarılmak', sıfat 'ilginç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: rüzgar yere serilen çarşafı havaya kaldırdı | çarşafın dört ucuna reçel kavanozu koydu
@tohum: masa-0090
@degisim: ilginç -> beyaz
Ormanda Maşa ile Daşa sincap için bir sürpriz hazırlıyordu. Maşa'nın sepetinde fındık ve en sevdiği reçelden dört kavanoz vardı. Bir ağacın altına beyaz bir çarşaf serdiler ama rüzgar onu havaya kaldırdı. "Maşa, rüzgar çarşafı uçuruyor!" dedi Daşa. Maşa çarşafı yeniden serdi. Sonra reçel kavanozlarını çarşafın dört ucuna koydu. Rüzgar yine esti ama çarşaf artık kalkmadı. İki kız fındıkları çarşafın ortasına koydu. "Bak, Maşa, kavanozlar çarşafı tuttu!" dedi Daşa. Tam o sırada sincap ağaçtan hızla indi. Fındıkları görünce sevinçle bir tanesine sarıldı. Maşa çok sevindi, çünkü sürprizleri sincabı mutlu etmişti.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çarşafın dört ucuna reçel kavanozu koydu"
   - Cümle 0 (plan satırı): «rüzgar yere serilen çarşafı havaya kaldırdı | çarşafın dört ucuna reçel kavanozu koydu»
   - Açıklama: Plandaki kavanozları koyma eylemi gövdede anlatılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0090` birebir aynı, `@degisim: ilginç -> beyaz` (tutuyorsan), ardından `@onarim: 12d51c2e85a632e6598caaa42a194d658c049592`, sonra gövde.

### Hikâye 11: tohum masa-0091 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0091
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: kaybolan eşya
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'baston', fiil 'sığınmak', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: koşarken çikolatalı baston şeker elinden düştü | yerdeki reçel izine bakarak şekeri buldu
@tohum: masa-0091
@degisim: sığınmak -> koşmak
Koca Ayı'nın evinin önünde Maşa çikolatalı baston şekerini reçele batırıp yiyordu. Sonra Koca Ayı ile koşmaya başladı. Ama koşarken şeker elinden düştü. Maşa şekeri otların arasında hiçbir yerde göremedi. Sonra reçel yediği yere döndü. Otların üstünde küçük, parlak reçel damlaları vardı. Maşa koşarken şekerden yere reçel düşmüştü. Maşa bu damlalara bakarak yürüdü. Son damla bir çalının dibindeydi. Çikolatalı şeker de orada, yaprakların arasında duruyordu. Maşa şekeri aldı ve sevinçle Koca Ayı'ya gösterdi. Koca Ayı gülümseyip başını salladı. Maşa bundan sonra koşarken şekerini sıkıca tuttu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çikolatalı baston şeker elinden"
   - Cümle 0 (plan satırı): «koşarken çikolatalı baston şeker elinden düştü | yerdeki reçel izine bakarak şekeri buldu»
   - Açıklama: Tamlama eki eksik; 'baston şekeri' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa bundan sonra koşarken şekerini sıkıca tuttu"
   - Cümle 13: «Maşa bundan sonra koşarken şekerini sıkıca tuttu.»
   - Açıklama: Baston şekerle koşmak taklit edilince tehlikeli bir davranış olarak ders gibi sunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0091` birebir aynı, `@degisim: sığınmak -> koşmak` (tutuyorsan), ardından `@onarim: 556de9a6c58c57ccfe9647314372b21ed4d3925c`, sonra gövde.

### Hikâye 12: tohum masa-0092 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0092
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'bot', fiil 'duymak', sıfat 'incecik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: sincap yuvasındaydı ve onları duymuyordu | incecik bir dalla botun altına vurdu
@tohum: masa-0092
Rüzgar hafif hafif esiyordu. Maşa ile Koca Ayı, sincabın ağacının dibine fındık dolu bir bot koydu. Bu bir sürprizdi ama sincap yuvasındaydı ve onları duymuyordu. Maşa önce ellerini çırptı ama sincap dışarı çıkmadı. Sonra yerden incecik bir dal aldı. Dalla botun altına tak tak vurmayı denedi. Bot yüksek ve komik bir ses çıkardı. Sincap sesi duydu ve ağaçtan hızla indi. Botun içindeki fındıkları görünce kuyruğunu salladı. Sonra fındıkları birer birer yuvasına taşıdı. Koca Ayı sevinçle Maşa'ya sarıldı. Maşa bundan sonra sincaba sürpriz yapınca onu botun komik sesiyle çağırdı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sürpriz yapınca onu botun komik sesiyle çağırdı"
   - Cümle 12: «Maşa bundan sonra sincaba sürpriz yapınca onu botun komik sesiyle çağırdı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor, fiil 'çağırırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0092` birebir aynı, ardından `@onarim: 3f421245029f687722eec7afb11b32d3e8fd09d3`, sonra gövde.
