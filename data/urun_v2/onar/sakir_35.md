# Editör görevi (onarım): Şakir, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Şakir | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar35.txt --ad urun_v2`
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

## Kart: Şakir (kaynaklı, kapalı dünya)

- Ad: Şakir (okunuş: şakir; kesme eki okunuşa uyar)
- Kimlik: Şakir, ailesiyle bir apartmanda yaşayan, okula giden yavru bir aslandır.
- Tür: aslan
- Güvenli özellik kullanımı: Şakir'in macerası güvenli bir oyun olarak kalır; yüksekten atlamaz, ateşle oynamaz, tek başına uzağa gitmez.
- Özellikler:
  - şapka: Hep şapka takar; şapkası yerden yere değişir. (örnek biçimler: şapka, şapkasını)
  - macera: Macerayı çok sever. (örnek biçimler: macera, macerayı)
- Yerler:
  - deniz: Deniz kıyısı ve kumsal.
  - orman: Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.
  - park: Şehirdeki park.
  - ev: Şakir'in ailesiyle yaşadığı apartman dairesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Remzi: Şakir'in ve Canan'ın babası; kırmızı kazak giyer, bankada çalışır, çocuk gibi eğlenir. Tür: aslan; konuşur. Yüzey biçimleri: Remzi, baba, babası, babacığım
  - Kadriye: Şakir'in ve Canan'ın annesi. Tür: kedi; konuşur. Yüzey biçimleri: Kadriye, anne, annesi, anneciğim
  - Canan: Şakir'in kız kardeşi; çok akıllıdır, kitap okumayı sever. Tür: kedi; konuşur. Yüzey biçimleri: Canan, kardeş, kardeşi
  - Necati: Remzi'nin en iyi arkadaşı; sık sık Şakir'lerin evine gelir, yemek yer ve oyun oynar. Tür: fil; konuşur. Yüzey biçimleri: Necati, Fil Necati, fil
- Dünya kuralları:
  - Remzi ve Şakir aslandır; Kadriye ve Canan beyaz kedidir; Necati mor bir fildir.
  - Necati Şakir'in akrabası değil, babasının arkadaşıdır; Şakir'in dedesi ve başka akrabası kartta yoktur.
- Yasak adlar: Peyami, Filsu, Tanju, Mirket, Kürşat, Ercan, Necmi, Cüneyt, Polat, Kumpir, Cemşit, Arif, Vedat, Refik
- Yasak: Video oyunu ve ekran başında oyun hikayeye girmez.
- İzinli dünya kelimeleri: şapka, aslan, apartman, macera, fil

## Onarılacak hikâyeler

### Hikâye 1: tohum sakir-0013 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0013
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'mermer', fiil 'sallanmak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kova sallanınca kabuklar kuma düşüyordu | kovayı iki eliyle tuttu ve yavaşça yürüdü
@tohum: sakir-0013
@degisim: mermer -> kova
Şakir kumsalda hazine oyunu oynuyordu. Minicik deniz kabuklarını kovayla kumdaki çukura taşıyordu. Ama kova elinde sallanınca kabuklar kuma düşüyordu. Şakir macerayı çok severdi ve oyunu bırakmadı. Eğildi ve düşen kabukları tek tek topladı. Sonra kovayı iki eliyle önünde tuttu. Yavaş yavaş yürüdü ve kova hiç sallanmadı. Çukura vardığında bütün hazinesi kovanın içindeydi. Şakir kabukları çukura döktü ve üstlerini kumla örttü. Yerini unutmamak için üstüne büyük bir taş koydu. Hazine oyunu tam istediği gibi olmuştu. Şakir bundan sonra dolu kovayı hep iki eliyle taşıdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve oyunu bırakmadı"
   - Cümle 4: «Şakir macerayı çok severdi ve oyunu bırakmadı.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiliyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0013` birebir aynı, `@degisim: mermer -> kova` (tutuyorsan), ardından `@onarim: eeebfaf01b04b5b6164530378780ba901e458d3f`, sonra gövde.

### Hikâye 2: tohum sakir-0083 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0083
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pul', fiil 'eşleştirmek', sıfat 'güzel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: ikisi de aynı anda aynı pulu tuttu | sırayla oynamayı önerdi ve oyun devam etti
@tohum: sakir-0083
Yağmur cama vuruyordu. Şakir ile annesi Kadriye evde pul eşleştirme oyunu oynuyordu. Ama ikisi de aynı anda aynı gemi pulunu tuttu ve oyun durdu. Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi. Biraz düşündü. "Anneciğim, sırayla oynayalım, önce sen bir pul seç," dedi Şakir. Kadriye güldü ve başını salladı. Önce Kadriye iki çiçek pulunu buldu ve yan yana koydu. Sonra sıra Şakir'e geçti. Şakir de iki güzel gemi pulunu eşleştirdi. "Aferin, Şakir!" dedi Kadriye. İkisi sırayla oynadı ve bütün pulların eşini buldu. Şakir çok sevindi, çünkü oyun artık hiç durmadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' soyut bir kavramdır ve 3 yaşındaki çocuğa uygun değildir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi"
   - Cümle 4: «Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor, pulu isteme davranışıyla ilgisi yok ve sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve gemi pulunu"
   - Cümle 4: «Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiliyor ve sorunun çözümünde hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi"
   - Cümle 4: «Şakir macerayı çok severdi ve gemi pulunu kendisi almak istedi.»
   - Açıklama: Macera sevgisi gemi pulunu isteme sebebi olarak zorlama ve işlevsiz biçimde ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0083` birebir aynı, ardından `@onarim: 275ecdf27509f63a5c0c529c41bf5f236994a8c4`, sonra gövde.

### Hikâye 3: tohum sakir-0084 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0084
- yer: park (Şehirdeki park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'küp', fiil 'koşmak', sıfat 'garip'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: kutlama için yanında hiç ödül yoktu | şapkasını ödül olarak filin başına koydu
@tohum: sakir-0084
Bir sabah Şakir ile Fil Necati parkta yarış için koştu. Necati alçak bir taş küpe ilk vardı ve üstüne oturdu. Şakir onu kutlamak istedi ama yanında hiç ödül yoktu. Şakir biraz düşündü ve şapkasını çıkardı. Necati küpte oturduğu için Şakir onun başına kolayca uzandı. Şapkayı Necati'nin başına koydu. Küçük şapka filin kocaman başında çok garip durdu. İkisi de çok güldü. "Bu senin ödül şapkan, Necati!" dedi Şakir. "Teşekkürler, Şakir, bu çok güzel bir kutlama!" dedi Necati. Sonra ikisi yan yana parkta mutlu mutlu yürüdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Necati alçak bir taş küpe ilk vardı"
   - Cümle 2: «Necati alçak bir taş küpe ilk vardı ve üstüne oturdu.»
   - Açıklama: 'Küp' 3 yaşındaki çocuğun bilmediği bir kelime ve 'küpe' biçimi takı ile karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0084` birebir aynı, ardından `@onarim: e47249f904ca1fbffb4903df9a63cfdbaf920e65`, sonra gövde.

### Hikâye 4: tohum sakir-0085 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0085
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumbara', fiil 'geçmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: yağmur yağmıştı ve ağaca giden yolda çamur vardı | düz taşları çamura koyup karşıya geçti
@tohum: sakir-0085
@degisim: kumbara -> kutu
Şakir ile babası Remzi ormandaki kamp yerinde hazine oyunu oynuyordu. Remzi büyük bir ağacın dibine bir hazine kutusu saklamıştı. Ama yağmur yağmıştı ve ağaca giden yolda büyük bir çamur vardı. Şakir çamurdan geçerse ayakları kirli olacaktı. Kamp yerinde oturmak için düz taşlar vardı. Şakir macerayı çok severdi ve taşlardan bir yol yapmayı düşündü. Taşları tek tek topladı ve çamurun içine sıra sıra dizdi. Taşların üstüne basarak karşıya geçti. Remzi de onun arkasından geldi. Şakir ağacın dibinde hazine kutusunu buldu. Kutuyu açtı ve içinde iki kurabiye gördü. Kurabiyelerden birini babasına verdi. Sonra ikisi ağacın dibine oturdu ve kurabiyelerini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yolda büyük bir çamur"
   - Cümle 3: «Ama yağmur yağmıştı ve ağaca giden yolda büyük bir çamur vardı.»
   - Açıklama: Çamur sayılamaz; 'büyük bir çamur' yerine 'çamur birikintisi' ya da 'çok çamur' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 6: «Şakir macerayı çok severdi ve taşlardan bir yol yapmayı düşündü.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.
   - Açıklama: 'Macera' soyut bir kavram ve küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0085` birebir aynı, `@degisim: kumbara -> kutu` (tutuyorsan), ardından `@onarim: 2a9e9f337976a16575b06bdcf0c7e22d3ba3f26a`, sonra gövde.

### Hikâye 5: tohum sakir-0086 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0086
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumaş', fiil 'çiğnemek', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: güneş çok parlaktı ve kardeşi okuyamadı | kumaştan gölgeli küçük bir çadır kurdu
@tohum: sakir-0086
@degisim: çiğnemek -> okumak
Ormandaki kamp yerinde güneşli bir gündü. Şakir geniş bir kumaşın üstünde oturuyordu, kardeşi Canan da paslı bir sandalyedeydi. Canan kitap okumak istedi ama güneş çok parlaktı ve yazıları göremedi. Şakir macera oyunlarında hep çadır kurardı. Hemen kalktı ve kumaşın iki ucunu iki alçak dala sıkıca bağladı. Böylece sandalyenin üstüne küçük bir çadır kurdu. Çadırın içi serin oldu. Canan kitabını rahatça okudu. Şakir de çadıra girdi ve kardeşinin yanına oturdu. İkisi kitaptaki resimlere birlikte baktı. Kumaşını paylaşınca ikisi de gölgede rahat etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunlarında hep"
   - Cümle 4: «Şakir macera oyunlarında hep çadır kurardı.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmeyebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macera oyunlarında hep çadır kurardı"
   - Cümle 4: «Şakir macera oyunlarında hep çadır kurardı.»
   - Açıklama: Kartın özellikler alanındaki macera sevgisi işe yarar biçimde kullanılmıyor, yerine kartta olmayan bir çadır kurma alışkanlığı ekleniyor.
   - Açıklama: Karttaki macera özelliğine kartta olmayan bir alışkanlık (hep çadır kurma) ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0086` birebir aynı, `@degisim: çiğnemek -> okumak` (tutuyorsan), ardından `@onarim: f27f8be588cf582c6fe7f515976021f94218eff9`, sonra gövde.

### Hikâye 6: tohum sakir-0088 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0088
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tebeşir', fiil 'sıçratmak', sıfat 'plastik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: rüzgar plastik kovayı yuvarladı ve kova kayboldu | babasıyla sesin geldiği yere gidip kovayı buldu
@tohum: sakir-0088
Rüzgar hızlı esiyordu. Şakir kumsalda babası Remzi'yle bir taşa tebeşirle resim çiziyordu. Birden rüzgar Şakir'in plastik kovasını yuvarladı ve kova kayboldu. Sonra büyük bir kayanın arkasından "tak tak" diye bir ses geldi. Şakir macerayı çok severdi ve bu sesi merak etti. "Baba, birlikte gidip bakalım mı?" diye sordu Şakir. Remzi güldü ve Şakir'in elini tuttu. İkisi kumda yürüdü ve kayanın arkasına baktı. Orada dalgalar kovaya su sıçratıyordu ve kova kayaya çarpıyordu. Ses kovadan geliyordu. Şakir kovayı aldı ve içindeki suyu döktü. "Kovayı bulduk, baba, şimdi taşa bir kova da çizelim!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve bu sesi merak etti.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şakir macerayı çok severdi ve bu sesi merak etti"
   - Cümle 5: «Şakir macerayı çok severdi ve bu sesi merak etti.»
   - Açıklama: Şakir kovayı aramaya değil merak ettiği sese gidiyor; çözüm kovayı bulma hedefine doğrudan yönelmiyor, kova tesadüfen bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0088` birebir aynı, ardından `@onarim: 3897cba802a4b5d23ddcb6ad03a5e49119b0b368`, sonra gövde.

### Hikâye 7: tohum sakir-0092 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0092
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ip', fiil 'savrulmak', sıfat 'çevik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: perde savruldu ve yumağı koltuğun altına düşürdü | yere uzanıp ipi çekti ve yumağı çıkardı
@tohum: sakir-0092
@degisim: çevik -> uzun
Şakir evde annesi Kadriye'nin yanında oturuyordu. Kadriye, Şakir için mavi bir atkı örüyordu. Birden rüzgar esti, perde savruldu ve yumağı koltuğun altına düşürdü. "Şakir, yumak olmadan atkı bitmez," dedi Kadriye. Şakir hemen yere uzandı ve koltuğun altına baktı. Yumak görünmüyordu ama uzun bir ip dışarıda duruyordu. Şakir macerayı çok severdi ve ipi bir hazine yolu gibi izledi. İpi yavaşça çekti ve yumak önüne yuvarlandı. "İşte buldum, anneciğim!" dedi Şakir. Kadriye yumağı aldı ve güldü. "Teşekkürler, Şakir, şimdi örmeye devam edebilirim," dedi Kadriye. Şakir çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ipi bir hazine yolu gibi izledi"
   - Cümle 7: «Şakir macerayı çok severdi ve ipi bir hazine yolu gibi izledi.»
   - Açıklama: 'Hazine yolu gibi' benzetmesi ve 'macera' soyut kavramı 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' ve 'hazine yolu gibi' benzetmesi soyut ve mecazlı, 3 yaşa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0092` birebir aynı, `@degisim: çevik -> uzun` (tutuyorsan), ardından `@onarim: 8ac48b009b8ee3a1a3dce861ab68b5a4e2ec5a2f`, sonra gövde.

### Hikâye 8: tohum sakir-0101 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0101
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: bir şey yapmak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ağaç', fiil 'süzülmek', sıfat 'hevesli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: rüzgar esti ve küçük evin çatısı uçtu | şapkasını evin üstüne yeni çatı olarak koydu
@tohum: sakir-0101
@degisim: hevesli -> sevinçli
Şakir ile Canan kamp yerinde bir ağacın dibine küçük bir ev yapıyordu. Evin duvarları dallardan yapılmıştı, çatısı da büyük bir yapraktı. Ama birden rüzgar esti ve çatı havada süzüldü. "Evimizin çatısı gitti, Şakir," dedi Canan. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı evin üstüne yavaşça yerleştirdi. Şapka yapraktan ağırdı ve rüzgarda uçmadı. Yeni çatı evi tam kapattı. Canan sevinçli sevinçli ellerini çırptı. "Şapkalı evimiz çok güzel oldu, Şakir!" dedi Canan.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Canan sevinçli sevinçli ellerini"
   - Cümle 9: «Canan sevinçli sevinçli ellerini çırptı.»
   - Açıklama: 'Sevinçli sevinçli' yanlış ikileme; 'sevinçle' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0101` birebir aynı, `@degisim: hevesli -> sevinçli` (tutuyorsan), ardından `@onarim: 44c57425d725b80c10ebab397f70c4bd4e13c2db`, sonra gövde.

### Hikâye 9: tohum sakir-0108 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0108
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'erik', fiil 'kabarmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kum kaydı ve eriği örttü | şapkasıyla kabarık kumu itip eriği buldu
@tohum: sakir-0108
Şakir kumsalda oturuyordu ve elinde son bir erik vardı. Ama erik elinden düştü ve kumdaki küçük bir çukura yuvarlandı. Çukurun kenarından kum kaydı ve eriği örttü. Artık erik görünmüyordu. Şakir hemen yanına eğildi. Kumun bir yeri küçük bir tepe gibi kabarmıştı. Şakir düşünceli düşünceli kabarık yere baktı. Erik bu kumun altında olabilirdi. Şakir şapkasını çıkardı ve onu küçük bir kürek gibi tuttu. Şapkayla kumu yavaş yavaş kenara itti. Kumun altından mor erik çıktı. Şakir onun üstündeki kumu sildi. Sonra şapkasını yeniden taktı ve eriği mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şakir hemen yanına eğildi"
   - Cümle 5: «Şakir hemen yanına eğildi.»
   - Açıklama: 'yanına' zamirinin kimin ya da neyin yanını gösterdiği belli değil; son özne görünmeyen erik.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "eriği mutlu mutlu yedi"
   - Cümle 13: «Sonra şapkasını yeniden taktı ve eriği mutlu mutlu yedi.»
   - Açıklama: Kuma düşüp yalnız silinen erik yıkanmadan yeniyor; çocuk taklit ederse sağlıksız bir davranış örneği olur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0108` birebir aynı, ardından `@onarim: a74da3f75900c6a56701afcf501c8d8e707dad32`, sonra gövde.

### Hikâye 10: tohum sakir-0109 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0109
- yer: park (Şehirdeki park.)
- tema: kaybolan eşya
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karpuz', fiil 'büyütmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: top bankın altına yuvarlandı ve çok uzaktaydı | şapkasını bankın altına uzatıp topu kendine çekti
@tohum: sakir-0109
@degisim: zarif -> geniş
Parkta güneşli bir gündü. Şakir karpuz desenli topuna hava üfledi ve onu büyüttü. Sonra topla oynamaya başladı. Top bir taşa çarptı ve bankın altına yuvarlandı. Şakir eğildi ve topu bankın altında gördü. Kolunu uzattı ama top çok uzaktaydı. Sonra başındaki geniş, beyaz şapkayı çıkardı. Şapkayı bankın altına uzattı. Şapkanın kenarı topun arkasına ulaştı. Şakir şapkayı yavaşça kendine doğru çekti. Top şapkanın önünden dışarı yuvarlandı. Şakir topu iki eliyle sıkıca tuttu. Şapkanın tozunu silkeledi ve onu yeniden taktı. Sonra Şakir topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "topuna hava üfledi ve onu büyüttü"
   - Cümle 2: «Şakir karpuz desenli topuna hava üfledi ve onu büyüttü.»
   - Açıklama: Topu şişirme ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "karpuz desenli topuna hava üfledi ve onu büyüttü"
   - Cümle 2: «Şakir karpuz desenli topuna hava üfledi ve onu büyüttü.»
   - Açıklama: Topu üfleyerek şişirme ayrıntısı olayda hiçbir işe yaramıyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Top bir taşa çarptı ve bankın altına yuvarlandı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Top bir taşa çarptı ve bankın altına yuvarlandı"
   - Cümle 4: «Top bir taşa çarptı ve bankın altına yuvarlandı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0109` birebir aynı, `@degisim: zarif -> geniş` (tutuyorsan), ardından `@onarim: 82da0ebc6373428676c8e513391d997bbd9ef9dd`, sonra gövde.

### Hikâye 11: tohum sakir-0127 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0127
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'lastik', fiil 'sulamak', sıfat 'sıkı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: topunu kaleye yakın attı ve kuleyi yıktı | özür diledi ve şapkasıyla yeni bir kule yaptı
@tohum: sakir-0127
@degisim: sulamak -> ıslatmak
Dalgalar kıyıya vuruyordu. Şakir'in babası Remzi kumda büyük bir kale yapmıştı. Şakir lastik topunu hızlı attı ve top kalenin kulesini yıktı. Remzi çok üzüldü. Şakir babasının yanına koştu. "Özür dilerim, baba, topu kaleye çok yakın attım," dedi Şakir. Şakir elleriyle deniz suyu getirdi ve kumu ıslattı. Şapkasının içine ıslak kum koydu ve sıkı bastırdı. Sonra onu kalenin üstüne ters çevirdi ve yavaşça kaldırdı. Yuvarlak, yeni bir kule ortaya çıktı. Remzi güldü ve ellerini çırptı. "Bu kule eskisinden de güzel, Şakir!" dedi Remzi. Şakir bundan sonra topunu hep kalelerden uzağa attı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şakir elleriyle deniz suyu getirdi ve kumu ıslattı"
   - Cümle 7: «Şakir elleriyle deniz suyu getirdi ve kumu ıslattı.»
   - Açıklama: Çözüm özür, su taşıma, kumu ıslatma, şapkaya doldurma ve ters çevirme gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0127` birebir aynı, `@degisim: sulamak -> ıslatmak` (tutuyorsan), ardından `@onarim: fe412d4df53bbd468716f483237e7915021ab4e6`, sonra gövde.

### Hikâye 12: tohum sakir-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0133
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bisküvi', fiil 'uzatmak', sıfat 'kolay'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: annesi güneş yüzünden buluta bakamadı | şapkasını annesine uzattı ve gözlerine gölge yaptı
@tohum: sakir-0133
Deniz kıyısında güneşli bir öğle vaktiydi. Şakir kumda oturmuş yuvarlak bir bisküvi yiyordu. Birden güneşin yanında tıpkı bisküvisine benzeyen bir bulut gördü. "Anne, bak, gökyüzünde bir bisküvi var!" dedi Şakir. Annesi Kadriye yukarı baktı. "Güneş çok parlak, bulutu göremiyorum," dedi Kadriye. Şakir başından geniş şapkasını çıkardı ve annesine uzattı. Kadriye şapkayı taktı ve gözleri gölgede kaldı. Şimdi bulutu görmek çok kolaydı. Kadriye bulutu gördü ve güldü. "Teşekkürler, Şakir, bu gerçekten kocaman bir bisküvi!" dedi Kadriye.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Birden güneşin yanında tıpkı bisküvisine benzeyen bir bulut gördü"
   - Cümle 3: «Birden güneşin yanında tıpkı bisküvisine benzeyen bir bulut gördü.»
   - Açıklama: Çocuğun taklit edebileceği biçimde güneşin hemen yanına, parlak gökyüzüne bakmak özendiriliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "güneşin yanında tıpkı bisküvisine"
   - Cümle 3: «Birden güneşin yanında tıpkı bisküvisine benzeyen bir bulut gördü.»
   - Açıklama: Çocuğun taklit edebileceği biçimde güneşin hemen yanına bakılıyor, bu göz için tehlikeli bir davranış.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Güneş çok parlak, bulutu göremiyorum"
   - Cümle 6: «"Güneş çok parlak, bulutu göremiyorum," dedi Kadriye.»
   - Açıklama: Sorun ilk üç cümlede değil ancak altıncı cümlede söyleniyor.
   - Açıklama: Annenin bulutu görememe sorunu ilk üç cümlede değil ancak altıncı cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0133` birebir aynı, ardından `@onarim: 7eae6f9e30e1f6169e3fddf5c3fb58d8f13b196f`, sonra gövde.
