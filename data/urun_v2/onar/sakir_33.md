# Editör görevi (onarım): Şakir, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0070 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0070
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ruj', fiil 'dokunmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: şirin bir kabuk ağır bir kütüğün altında kaldı | yardım istedi ve fil kütüğü kenara itti
@tohum: sakir-0070
@degisim: ruj -> kütük
Denizden serin bir rüzgar esiyordu. Macerayı çok seven Şakir, Necati ile kumsalda kabuk arıyordu. Birden şirin, pembe bir kabuk gördü ama kabuk ağır bir kütüğün altındaydı. Şakir kütüğü iki eliyle çekti ama kütük hiç kıpırdamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. Necati hortumuyla kütüğü kolayca kenara itti. Şakir kabuğu aldı ve ona parmağıyla yavaşça dokundu. Kabuğun içi çok parlaktı. "Çok güzel bir kabuk buldun, Şakir," dedi Necati. "Teşekkürler, Necati, bu kabuğu hep saklayacağım!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 2: «Macerayı çok seven Şakir, Necati ile kumsalda kabuk arıyordu.»
   - Açıklama: 'Macera' soyut bir kavramdır ve 3 yaşındaki çocuk için anlaşılır değildir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir, Necati ile kumsalda kabuk arıyordu"
   - Cümle 2: «Macerayı çok seven Şakir, Necati ile kumsalda kabuk arıyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor; sorunu Necati çözüyor ve özellik işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0070` birebir aynı, `@degisim: ruj -> kütük` (tutuyorsan), ardından `@onarim: e9f5d18e80675aec4a69feaa9ea55bae43b148d9`, sonra gövde.

### Hikâye 2: tohum sakir-0083 (deneme 4 -> 5)

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
Yağmur cama vuruyordu. Şakir ile annesi Kadriye evde pul eşleştirme oyunu oynuyordu. Ama ikisi de aynı anda aynı pulu tuttu ve oyun durdu. Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi. Biraz düşündü. "Anneciğim, sırayla oynayalım, önce sen bir pul seç," dedi Şakir. Kadriye güldü ve başını salladı. Önce Kadriye iki gemi pulunu buldu ve yan yana koydu. Sonra sıra Şakir'e geçti. Şakir de iki güzel çiçek pulunu eşleştirdi. "Aferin, Şakir!" dedi Kadriye. İkisi sırayla oynadı ve bütün pulların eşini buldu. Şakir çok sevindi, çünkü oyun artık hiç durmadı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi"
   - Cümle 4: «Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi.»
   - Açıklama: Evde pul eşleştirmede macera yok; 'macerayı severdi' oyunun durmasını istememeye gerekçe olarak yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi"
   - Cümle 4: «Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi.»
   - Açıklama: Tohumdaki macera özelliği süs olarak sayılıyor, sırayla oynama çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve oyunun"
   - Cümle 4: «Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi.»
   - Açıklama: Macera özelliği pul oyununda yalnız etiket olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve oyunun durmasını hiç istemedi.»
   - Açıklama: Macerayı sevme özelliği eşleştirme oyunuyla ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0083` birebir aynı, ardından `@onarim: 0ac9d63a19c6358b1ea0169aa6548b01820d9cfe`, sonra gövde.

### Hikâye 3: tohum sakir-0084 (deneme 4 -> 5)

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
Bir sabah Şakir ile Fil Necati parktaydı. Necati ilk kez hiç durmadan koştu ve alçak bir taş küpe oturdu. Şakir onu kutlamak istedi ama yanında hiç ödül yoktu. Şakir biraz düşündü ve şapkasını çıkardı. Necati küpte oturduğu için Şakir onun başına kolayca uzandı. Şapkayı Necati'nin başına koydu. Küçük şapka filin kocaman başında çok garip durdu. İkisi de çok güldü. "Bu senin ödül şapkan, Necati!" dedi Şakir. "Teşekkürler, Şakir, bu çok güzel bir kutlama!" dedi Necati. Sonra ikisi yan yana parkta mutlu mutlu yürüdü.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Necati ilk kez hiç durmadan koştu"
   - Cümle 2: «Necati ilk kez hiç durmadan koştu ve alçak bir taş küpe oturdu.»
   - Açıklama: Kartın ilişki alanında Necati Remzi'nin yetişkin arkadaşıdır, burada Şakir'in ödüllendirdiği bir çocuk gibi geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0084` birebir aynı, ardından `@onarim: 747bb1e7b2b49cc77b64d05b5b9f3396d1be3511`, sonra gövde.

### Hikâye 4: tohum sakir-0085 (deneme 4 -> 5)

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
Şakir ile babası Remzi ormandaki kamp yerinde hazine oyunu oynuyordu. Remzi büyük bir ağacın dibine bir hazine kutusu saklamıştı. Ama yağmur yağmıştı ve ağaca giden yolda büyük bir çamur vardı. Şakir çamurdan geçerse ayakları kirli olacaktı. Çamurun kenarında düz taşlar gördü. Şakir macerayı çok severdi ve taşlardan bir yol yapmayı düşündü. Taşları tek tek topladı ve çamurun içine sıra sıra dizdi. Taşların üstüne basarak karşıya geçti. Remzi de onun arkasından geldi. Şakir ağacın dibinde hazine kutusunu buldu. Kutuyu açtı ve içinde iki kurabiye gördü. Kurabiyelerden birini babasına verdi. Sonra ikisi ağacın dibine oturdu ve kurabiyelerini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çamurun kenarında düz taşlar gördü"
   - Cümle 5: «Çamurun kenarında düz taşlar gördü.»
   - Açıklama: Çözümü sağlayan düz taşlar önceden kurulmadan, tam gerektiği anda tesadüfen beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0085` birebir aynı, `@degisim: kumbara -> kutu` (tutuyorsan), ardından `@onarim: 1bcaf5d186948c840d99703aac394d86894c617e`, sonra gövde.

### Hikâye 5: tohum sakir-0086 (deneme 4 -> 5)

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
Ormandaki kamp yerinde Şakir ile kardeşi Canan aileleriyle birlikteydi. Şakir geniş bir kumaşın üstünde oturuyordu, Canan da paslı bir sandalyedeydi. Canan kitap okumak istedi ama güneş çok parlaktı ve yazıları göremedi. Şakir macerayı çok severdi ve kumaşından bir çadır yapmayı düşündü. Kalktı ve kumaşın iki ucunu iki alçak dala sıkıca bağladı. Böylece sandalyenin üstüne küçük bir çadır kurdu. Çadırın içi serin oldu. Canan kitabını rahatça okudu. Şakir de çadıra girdi ve kardeşinin yanına oturdu. İkisi kitaptaki resimlere birlikte baktı. Şakir bundan sonra kumaşını hep kardeşiyle paylaştı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kardeşi Canan aileleriyle birlikteydi"
   - Cümle 1: «Ormandaki kamp yerinde Şakir ile kardeşi Canan aileleriyle birlikteydi.»
   - Açıklama: İki kardeşin tek ailesi var; çoğul 'aileleriyle' yerine 'ailesiyle' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve kumaşından bir çadır yapmayı düşündü.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve kumaşından"
   - Cümle 4: «Şakir macerayı çok severdi ve kumaşından bir çadır yapmayı düşündü.»
   - Açıklama: Macera özelliği çadır kurma çözümüne yalnız etiket olarak bağlanıyor, kartın özelliği işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi ve kumaşından bir çadır yapmayı düşündü"
   - Cümle 4: «Şakir macerayı çok severdi ve kumaşından bir çadır yapmayı düşündü.»
   - Açıklama: Macerayı sevmesi çadır kurma fikrini sebeplendirmiyor; özellik çözüme bağsız ekleniyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Şakir bundan sonra kumaşını hep kardeşiyle paylaştı"
   - Cümle 11: «Şakir bundan sonra kumaşını hep kardeşiyle paylaştı.»
   - Açıklama: Son ders paylaşmama gibi bir sorundan çıkmıyor; yaşanan olaya bağlı değil.
   - Açıklama: Son ders cümlesi paylaşmayla ilgili ama hikayede paylaşmama sorunu yok; ders olaydan doğrudan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0086` birebir aynı, `@degisim: çiğnemek -> okumak` (tutuyorsan), ardından `@onarim: 748b8eadb810ba2681282c016865bce1dee7241b`, sonra gövde.

### Hikâye 6: tohum sakir-0088 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kayanın arkasından garip bir ses geldi | babasıyla kayanın arkasına gidip sesi yapan kovayı buldu
@tohum: sakir-0088
Rüzgar esiyordu ve dalgalar kıyıya vuruyordu. Şakir kumsalda babası Remzi'yle taşlara tebeşirle resim çiziyordu. Birden büyük kayanın arkasından "tak tak" diye garip bir ses geldi. Şakir bu sesi çok merak etti. "Baba, ben macerayı çok severim, sesi bulalım mı?" diye sordu Şakir. Remzi güldü ve Şakir'in elini tuttu. İkisi birlikte kayanın arkasına yürüdü. Orada mavi, plastik bir kova vardı. Dalgalar kovaya su sıçratıyordu ve kova kayaya çarpıyordu. "Bu kova bizim, rüzgar onu buraya getirmiş!" dedi Remzi. Şakir kovayı aldı ve ikisi resimlerin yanına geri döndü. "Kovayı bulduk, baba, şimdi kumdan kale yapalım!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip bir ses geldi"
   - Cümle 3: «Birden büyük kayanın arkasından "tak tak" diye garip bir ses geldi.»
   - Açıklama: Garip ses gerçek bir sorun değil; ortada çözülmesi gereken bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben macerayı çok severim"
   - Cümle 5: «"Baba, ben macerayı çok severim, sesi bulalım mı?" diye sordu Şakir.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuk bu kelimeyi bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kova bizim, rüzgar onu buraya getirmiş"
   - Cümle 10: «"Bu kova bizim, rüzgar onu buraya getirmiş!" dedi Remzi.»
   - Açıklama: Kovanın onlara ait olduğu ve kaybolduğu daha önce hiç kurulmuyor; kova sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0088` birebir aynı, ardından `@onarim: 9777fc09d244ff2b1cf42567a89cd1868607c3c7`, sonra gövde.

### Hikâye 7: tohum sakir-0091 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0091
- yer: park (Şehirdeki park.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fermuar', fiil 'sakinleşmek', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: bir yaprak fermuara sıkıştı ve çanta kapanmadı | annesinden yardım isteyip büyük yaprağı şapkasına koydu
@tohum: sakir-0091
Şakir parkta annesi Kadriye'yle renkli yapraklar topluyordu. Yaprakları çantasına tek tek, düzenli diziyordu. Ama büyük bir yaprak fermuara sıkıştı ve çanta kapanmadı. Şakir önce kızdı, sonra derin bir nefes alıp sakinleşti. "Anneciğim, fermuar sıkıştı, yardım eder misin?" diye sordu Şakir. "Tabii, Şakir," dedi Kadriye. Kadriye yaprağı yavaşça çekip çıkardı. Yaprak çantaya sığmıyordu, bu yüzden Şakir onu şapkasının içine koydu. Sonra çantayı kolayca kapattı. "Teşekkürler, anneciğim, bütün yapraklar burada!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kadriye yaprağı yavaşça çekip çıkardı"
   - Cümle 7: «Kadriye yaprağı yavaşça çekip çıkardı.»
   - Açıklama: Fermuara sıkışan yaprağı Şakir değil annesi Kadriye çıkarıyor; sorunun asıl çözümünü yan karakter yapıyor.
   - Açıklama: Sıkışan yaprağı fermuardan Şakir değil annesi çıkarıyor; asıl çözümü yan karakter yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0091` birebir aynı, ardından `@onarim: fe55e20ebc54c665c593570fe0c4c7e16aa56056`, sonra gövde.

### Hikâye 8: tohum sakir-0092 (deneme 4 -> 5)

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
Şakir evde annesi Kadriye'nin yanında oturuyordu. Kadriye, Şakir için mavi bir atkı örüyordu. Birden rüzgar esti, perde savruldu ve yumağı koltuğun altına düşürdü. "Şakir, yumak olmadan atkı bitmez," dedi Kadriye. Macerayı çok seven Şakir hemen yere uzandı ve koltuğun altına baktı. Yumak çok içerideydi ama uzun bir ip dışarıda duruyordu. Şakir ipi yavaşça çekti ve yumak önüne yuvarlandı. "İşte buldum, anneciğim!" dedi Şakir. Kadriye yumağı aldı ve güldü. "Teşekkürler, Şakir, şimdi örmeye devam edebilirim," dedi Kadriye. Şakir çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir hemen yere uzandı"
   - Cümle 5: «Macerayı çok seven Şakir hemen yere uzandı ve koltuğun altına baktı.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 5: «Macerayı çok seven Şakir hemen yere uzandı ve koltuğun altına baktı.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor; koltuğun altına uzanmak kartın 'Macerayı çok sever' özelliğini işe yarar biçimde kullanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0092` birebir aynı, `@degisim: çevik -> uzun` (tutuyorsan), ardından `@onarim: b4e991f64eac51752c420c9526421bc9e5fe993a`, sonra gövde.

### Hikâye 9: tohum sakir-0101 (deneme 3 -> 4)

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
Şakir ile Canan kamp yerinde bir ağacın dibine küçük bir ev yapıyordu. Evin duvarları dallardan yapılmıştı, çatısı da büyük bir yapraktı. Ama birden rüzgar esti ve çatı havada süzüldü. "Evimizin çatısı gitti, Şakir," dedi Canan. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı evin üstüne yavaşça yerleştirdi. Şapka yapraktan ağırdı ve rüzgarda uçmadı. Yeni çatı evi tam kapattı. Canan yeniden oynamaya çok hevesliydi. "Şapkalı evimiz çok güzel oldu, Şakir!" dedi Canan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeniden oynamaya çok hevesliydi"
   - Cümle 9: «Canan yeniden oynamaya çok hevesliydi.»
   - Açıklama: 'Hevesli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Canan yeniden oynamaya çok hevesliydi"
   - Cümle 9: «Canan yeniden oynamaya çok hevesliydi.»
   - Açıklama: 'Hevesliydi' 3 yaşındaki çocuk için soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0101` birebir aynı, ardından `@onarim: a60cc79716b66ba1d806596221a835c4d0486768`, sonra gövde.

### Hikâye 10: tohum sakir-0108 (deneme 3 -> 4)

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
@plan: rüzgar eriği kumla örttü ve erik görünmedi | şapkasıyla kabarık kumu itip eriği buldu
@tohum: sakir-0108
Şakir kumsalda oturuyordu ve elinde son bir erik vardı. Ama erik elinden kaydı ve kumun üstünde biraz yuvarlandı. Birden rüzgar esti ve eriğin üstünü kumla örttü. Rüzgar durdu ama erik görünmüyordu. Şakir hemen yanına eğildi. Kumun bir yeri küçük bir tepe gibi kabarmıştı. Şakir düşünceli düşünceli kabarık yere baktı. Erik bu kumun altında olabilirdi. Şakir şapkasını çıkardı ve onu küçük bir kürek gibi tuttu. Şapkayla kumu yavaş yavaş kenara itti. Kumun altından mor erik çıktı. Şakir onun üstündeki kumu sildi. Sonra şapkasını yeniden taktı ve eriği mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve eriğin üstünü kumla örttü"
   - Cümle 3: «Birden rüzgar esti ve eriğin üstünü kumla örttü.»
   - Açıklama: Tek bir rüzgarın yuvarlanan eriği bir anda kumla tamamen gömmesi akla yatkın bir sebep değil.
   - Açıklama: Kısa bir rüzgarın bir anda eriği kumla tamamen gömmesi akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0108` birebir aynı, ardından `@onarim: e1c4d83b31ddb3ab32b88da255f0bcfd11dfea1e`, sonra gövde.

### Hikâye 11: tohum sakir-0109 (deneme 3 -> 4)

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
Parkta güneşli bir gündü. Şakir karpuz desenli küçük topuyla oynuyordu. Top bir taşa çarptı ve bankın altına yuvarlandı. Şakir eğildi, gözlerini büyüterek baktı ve topu bankın altında gördü. Kolunu uzattı ama top çok uzaktaydı. Sonra başındaki geniş, beyaz şapkayı çıkardı. Şapkayı bankın altına uzattı. Şapkanın kenarı topun arkasına ulaştı. Şakir şapkayı yavaşça kendine doğru çekti. Top şapkanın önünden dışarı yuvarlandı. Şakir topu iki eliyle sıkıca tuttu. Şapkanın tozunu silkeledi ve onu yeniden taktı. Sonra Şakir topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gözlerini büyüterek baktı"
   - Cümle 4: «Şakir eğildi, gözlerini büyüterek baktı ve topu bankın altında gördü.»
   - Açıklama: 'Gözlerini büyütmek' deyimsi bir anlatım; küçük çocuk için 'gözlerini kocaman açtı' daha somut olur.
   - Açıklama: 'Gözlerini büyüterek' deyimsel bir kullanım, küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0109` birebir aynı, `@degisim: zarif -> geniş` (tutuyorsan), ardından `@onarim: 968156f64f5ef0297beb790dfc62f4987337fb4b`, sonra gövde.

### Hikâye 12: tohum sakir-0127 (deneme 2 -> 3)

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
Dalgalar kıyıya vuruyordu. Şakir'in babası Remzi kumda büyük bir kale yapmıştı. Şakir lastik topunu hızlı attı ve top kalenin kulesini yıktı. Remzi çok üzüldü. Şakir babasının yanına koştu. "Özür dilerim, baba, topu kaleye çok yakın attım," dedi Şakir. Şakir kovasını su kenarında doldurdu ve kumu ıslattı. Şapkasının içine ıslak kum koydu ve sıkı bastırdı. Sonra onu kalenin üstüne ters çevirdi ve yavaşça kaldırdı. Yuvarlak, yeni bir kule ortaya çıktı. Remzi güldü ve ellerini çırptı. "Bu kule eskisinden de güzel, Şakir!" dedi Remzi. Şakir bundan sonra topunu hep kalelerden uzağa attı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir kovasını su kenarında doldurdu"
   - Cümle 7: «Şakir kovasını su kenarında doldurdu ve kumu ıslattı.»
   - Açıklama: Kova sebepsiz beliriyor ve kalıp olarak kova varken kulenin şapkayla yapılması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0127` birebir aynı, `@degisim: sulamak -> ıslatmak` (tutuyorsan), ardından `@onarim: ec1561983c71f8e3f972e6d1a02604445f924397`, sonra gövde.
