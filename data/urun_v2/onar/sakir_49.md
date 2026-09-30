# Editör görevi (onarım): Şakir, onarım partisi 49

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar49.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar49.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0271 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0271
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'blok', fiil 'korunmak', sıfat 'zeki'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: rüzgar kumu kaldırıp sandviçlere doğru getiriyordu | şapkasıyla kumdan bloklar yapıp duvar kurdu
@tohum: sakir-0271
Rüzgar esiyordu. Şakir ile annesi Kadriye kumsalda oturmuş, sandviç yiyordu. Ama rüzgar kumu kaldırıp sandviçlere doğru getiriyordu. "Sandviçlerimize kum gelecek," dedi Kadriye. Şakir biraz düşündü. Sonra şapkasını ıslak kumla doldurup yere ters çevirdi. Yerde kumdan küçük bir blok kaldı. Şakir böyle iki blok daha yaptı ve sandviçlerin önüne dizdi. Bloklar küçük bir duvar oldu. Artık sandviçler rüzgardan korunuyordu. Kadriye yemeğini rahatça bitirdi ve Şakir'e sarıldı. "Sen çok zekisin, teşekkürler, Şakir!" dedi Kadriye.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "şapkasını ıslak kumla doldurup yere ters çevirdi"
   - Cümle 6: «Sonra şapkasını ıslak kumla doldurup yere ters çevirdi.»
   - Açıklama: Kartın özellik alanı Şakir'in hep şapka taktığını söylüyor; şapkanın kum kalıbı olarak kullanılması karttaki özelliğin kullanımı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0271` birebir aynı, ardından `@onarim: dce110e72c92f1fea804be5bf3a33ec24f06b22f`, sonra gövde.

### Hikâye 2: tohum sakir-0273 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0273
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: bir şey yapmak
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'güneş', fiil 'binmek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: karton kutudan araba yapmak istedi ama direksiyon yoktu | şapkasını direksiyon gibi tuttu ve arabaya bindi
@tohum: sakir-0273
@degisim: sıcacık -> büyük
Güneş parlıyordu. Şakir kamp yerinde boş ve büyük bir karton kutu buldu. Ondan bir araba yapmak istedi ama arabanın direksiyonu yoktu. Şakir kutuya baktı ve biraz düşündü. Sonra yuvarlak şapkasını çıkardı. Onu iki eliyle direksiyon gibi tuttu. Şakir kutunun içine yavaşça oturdu ve hemen arabasına bindi. Şakir şapkayı bir sağa bir sola çevirdi. Ağzıyla vın vın diye araba sesi çıkardı. Şakir karton arabasıyla kamp yerinde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yavaşça oturdu ve hemen arabasına bindi"
   - Cümle 7: «Şakir kutunun içine yavaşça oturdu ve hemen arabasına bindi.»
   - Açıklama: Kutuya oturmak ile arabaya binmek aynı eylem; gereksiz tekrar.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir kutunun içine yavaşça oturdu ve hemen arabasına bindi"
   - Cümle 7: «Şakir kutunun içine yavaşça oturdu ve hemen arabasına bindi.»
   - Açıklama: Kutuya oturmak ile arabaya binmek aynı eylem, gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0273` birebir aynı, `@degisim: sıcacık -> büyük` (tutuyorsan), ardından `@onarim: 2abda68dd9abe69956d4753f6ad8b5fda39e0688`, sonra gövde.

### Hikâye 3: tohum sakir-0274 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0274
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'nilüfer', fiil 'şakalaşmak', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: benekli kabuklar kumun içine karışmıştı | şapkasıyla kumu salladı ve kabukları ayırdı
@tohum: sakir-0274
@degisim: şakalaşmak -> sallamak
Dalgaların sesi geliyordu. Şakir sudan uzakta, kumda benekli kabuklar gördü ve çiçek yapmak istedi. Ama kabuklar kumun içine karışmıştı. Şakir onları patileriyle kumdan ayıramadı. Şakir hasır şapkasını çıkardı. Onunla biraz kum aldı ve yavaşça salladı. Kum şapkanın küçük deliklerinden aşağı aktı. Kabuklar ise içeride kaldı. Şakir onları yere tek tek koydu. Ortaya bir daire, etrafına da çiçek yaprakları yaptı. Sonunda güzel bir nilüfer çiçeği oldu. Şakir çiçeğinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güzel bir nilüfer çiçeği oldu"
   - Cümle 11: «Sonunda güzel bir nilüfer çiçeği oldu.»
   - Açıklama: 'Nilüfer' 3 yaşındaki bir çocuğun bilmeyeceği bir kelimedir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mutlu mutlu oynamaya devam etti"
   - Cümle 12: «Şakir çiçeğinin yanında mutlu mutlu oynamaya devam etti.»
   - Açıklama: Şakir daha önce oynamıyordu; 'devam etti' anlamca uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0274` birebir aynı, `@degisim: şakalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: 89352a5f5fde312c4c637cec5814e4e582b10aba`, sonra gövde.

### Hikâye 4: tohum sakir-0275 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0275
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'salatalık', fiil 'kaldırmak', sıfat 'şapkalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: salatalık ıslak kuma yuvarlandı ve dalga ona geliyordu | şapkasıyla salatalığı dalgadan önce aldı ve kaldırdı
@tohum: sakir-0275
@degisim: şapkalı -> yeşil
Deniz kıyısında Şakir ile Canan yeşil salatalık yiyecekti. Canan çok acıkmıştı. Ama salatalık Canan'ın elinden kaydı ve ıslak kuma yuvarlandı. Küçük bir dalga ona doğru geliyordu. "Dalga salatalığımı alacak!" dedi Canan. Şakir hemen şapkasını çıkardı. Dalga gelmeden salatalığı şapkasına aldı ve yukarı kaldırdı. Dalga geldi ama yalnız boş kumu ıslattı. Salatalık şapkanın içinde kuru kaldı. Şakir salatalığı Canan'a verdi. "Teşekkürler, Şakir," dedi Canan. İkisi kumda oturup salatalığı mutlu mutlu paylaştı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dalga ona geliyordu"
   - Cümle 0 (plan satırı): «salatalık ıslak kuma yuvarlandı ve dalga ona geliyordu | şapkasıyla salatalığı dalgadan önce aldı ve kaldırdı»
   - Açıklama: Plandaki 'ona' zamirinin kimi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Küçük bir dalga ona doğru geliyordu."
   - Cümle 4: «Küçük bir dalga ona doğru geliyordu.»
   - Açıklama: 'ona' zamirinin salatalığı mı Canan'ı mı gösterdiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Küçük bir dalga ona doğru"
   - Cümle 4: «Küçük bir dalga ona doğru geliyordu.»
   - Açıklama: 'Ona' zamirinin salatalığı mı Canan'ı mı gösterdiği belli değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Dalga gelmeden salatalığı şapkasına aldı"
   - Cümle 7: «Dalga gelmeden salatalığı şapkasına aldı ve yukarı kaldırdı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde gelen dalgaya doğru koşup eşya kurtarılıyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Salatalık şapkanın içinde kuru kaldı"
   - Cümle 9: «Salatalık şapkanın içinde kuru kaldı.»
   - Açıklama: Salatalık zaten ıslak kuma yuvarlanmışken kuru kaldığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0275` birebir aynı, `@degisim: şapkalı -> yeşil` (tutuyorsan), ardından `@onarim: c38eb31fd22cf39c76dc913da99f121d6e0ecb9e`, sonra gövde.

### Hikâye 5: tohum sakir-0282 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0282
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çekirdek', fiil 'keşfetmek', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: oyuncak fırının kapağı eskiydi ve kapanmadı | şapkasını fırının önüne kapak gibi kapattı
@tohum: sakir-0282
@degisim: keşfetmek -> bulmak
Şakir evde soslu bir oyun pizzası yapıyordu. Mutfakta bulduğu çekirdekleri pizzanın üstüne dizdi. Ama oyuncak fırının kapağı çok eskiydi ve kapanmıyordu. Şakir kapağı iki kez itti, yine olmadı. Sonra büyük beyaz şapkasını çıkardı. Pizzayı fırına koydu ve önünü şapkayla kapattı. Şapka, fırının yeni kapağı oldu. Şakir yavaşça bir, iki, üç diye saydı. Sonra şapkayı kaldırdı ve pizzayı bir tabağa aldı. Oyunda pizza artık pişmişti. Şakir çok sevindi, çünkü şapkası oyununu kurtarmıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fırının önüne kapak gibi kapattı"
   - Cümle 0 (plan satırı): «oyuncak fırının kapağı eskiydi ve kapanmadı | şapkasını fırının önüne kapak gibi kapattı»
   - Açıklama: Şapka kapatılmaz, fırın şapkayla kapatılır; fiil nesnesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasını fırının önüne kapak gibi kapattı"
   - Cümle 0 (plan satırı): «oyuncak fırının kapağı eskiydi ve kapanmadı | şapkasını fırının önüne kapak gibi kapattı»
   - Açıklama: Şapka kapatılmaz; fırının önü şapkayla kapatılır, fiil nesnesine uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mutfakta bulduğu çekirdekleri pizzanın üstüne dizdi"
   - Cümle 2: «Mutfakta bulduğu çekirdekleri pizzanın üstüne dizdi.»
   - Açıklama: Çekirdekler kuruluyor ama olayda hiçbir işe yaramıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şapkası oyununu kurtarmıştı"
   - Cümle 11: «Şakir çok sevindi, çünkü şapkası oyununu kurtarmıştı.»
   - Açıklama: 'Oyunu kurtarmak' mecazdır ve 3 yaşındaki çocuk için soyuttur.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü şapkası oyununu kurtarmıştı"
   - Cümle 11: «Şakir çok sevindi, çünkü şapkası oyununu kurtarmıştı.»
   - Açıklama: Şapkanın oyunu kurtarması mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0282` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 300acd743ffd9ddca5698f57d674594ab29ecdb0`, sonra gövde.

### Hikâye 6: tohum sakir-0284 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0284
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'tekne', fiil 'vermek', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: havuzdan garip bir tık tık sesi geldi | şapkasıyla gölge yaptı ve sesi yapan kabuğu gördü
@tohum: sakir-0284
Rüzgar esiyordu. Şakir parktaki havuzun yanından geçerken tık tık diye bir ses duydu. Ses suyun ortasından geliyordu. Şakir bu sesi çok merak etti. Ama güneş suda çok parlıyordu. Bu yüzden Şakir iyi göremedi. Hemen şapkasını gözlerinin üstüne indirdi. Şapka ona serin bir gölge verdi. Şimdi suyun ortasını iyice gördü. Orada küçük bir ağaç kabuğu yüzüyordu. Kabuk yamuk bir tekne gibi sallanıyordu. Rüzgar kabuğu itiyordu ve kabuk bir taşa vuruyordu. Sesi bu kabuk yapıyordu. Şakir her tık sesini tek tek saydı ve güldü. Şakir çok sevindi, çünkü tık tık sesini yapan kabuğu bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir bu sesi çok merak etti"
   - Cümle 4: «Şakir bu sesi çok merak etti.»
   - Açıklama: Sorun yalnız merak uyandıran bir ses; çocuğun önemseyeceği gerçek bir sorun zayıf ve asıl engel olan parlamayla karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0284` birebir aynı, ardından `@onarim: 476d55dc0c3ad295b060febb41b6fc117a6db268`, sonra gövde.

### Hikâye 7: tohum sakir-0288 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Canan
@tohum: sakir-0288
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'krema', fiil 'uyandırmak', sıfat 'bozuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Canan
@plan: oyuncak saat bozuktu ve çalmadı | şapkasını salladı ve kardeşini uyandırdı
@tohum: sakir-0288
Parkta Şakir ile Canan komik bir oyun oynuyordu. Kazanan, kremalı kekin ilk dilimini alacaktı. Canan çimlere uzandı ve uyuyor gibi yaptı. Şakir onu oyuncak saatle uyandırmak istedi, ama saat bozuktu ve çalmadı. Şakir düğmeye iki kez bastı, yine ses çıkmadı. Canan gözlerini kapalı tuttu ve hiç kıpırdamadı. Sonra Şakir şapkasını çıkardı. Şapkayı Canan'ın yüzüne doğru yavaşça salladı. Şapkadan gelen serin hava Canan'ın yüzüne değdi. Canan güldü ve gözlerini açtı. "Uyandım, uyandım, yüzüm serinledi!" dedi Canan. "Kazandım, ama ilk dilimi birlikte yiyelim, Canan!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasını salladı ve kardeşini uyandırdı"
   - Cümle 0 (plan satırı): «oyuncak saat bozuktu ve çalmadı | şapkasını salladı ve kardeşini uyandırdı»
   - Açıklama: Gövdede Canan'ın Şakir'in kardeşi olduğu hiç söylenmiyor; plan gövdeyi doğru aktarmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kazanan, kremalı kekin ilk dilimini alacaktı"
   - Cümle 2: «Kazanan, kremalı kekin ilk dilimini alacaktı.»
   - Açıklama: Oyunun kuralı ve neyin kazanmak sayıldığı söylenmiyor, bu yüzden sorunun ne olduğu ve neden önemli olduğu belirsiz kalıyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "saat bozuktu ve çalmadı"
   - Cümle 4: «Şakir onu oyuncak saatle uyandırmak istedi, ama saat bozuktu ve çalmadı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0288` birebir aynı, ardından `@onarim: 9a5174af94b2a797bb57e56d50416150eefd48d6`, sonra gövde.

### Hikâye 8: tohum sakir-0291 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0291
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'demet', fiil 'öğretmek', sıfat 'esnek'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: esnek top her seferinde ellerinden kaçtı | şapkasını ters tuttu ve topu içine yakaladı
@tohum: sakir-0291
@degisim: demet -> hortum
Bir sabah Şakir, Necati'ye kumsalda top yakalama oyununu öğretiyordu. Necati topu hortumuyla atıyor, Şakir yakalıyordu. Ama top çok esnekti ve Şakir'in ellerine çarpınca hop diye geri zıpladı. Top kumda yuvarlanarak uzağa gitti. Necati kulaklarını salladı ve güldü. Şakir de güldü ve biraz düşündü. Sonra şapkasını çıkardı ve ters çevirip iki eliyle tuttu. "Hadi, Necati, şimdi at!" dedi Şakir. Necati topu yavaşça attı. Top şapkanın içine düştü ve dışarı çıkmadı. "Yakaladın, aferin!" dedi Necati. Sonra oyunu birçok kez daha oynadılar. Şakir çok mutluydu, çünkü artık topu hiç kaçırmıyordu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama top çok esnekti"
   - Cümle 3: «Ama top çok esnekti ve Şakir'in ellerine çarpınca hop diye geri zıpladı.»
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "top çok esnekti"
   - Cümle 3: «Ama top çok esnekti ve Şakir'in ellerine çarpınca hop diye geri zıpladı.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Top kumda yuvarlanarak uzağa gitti"
   - Cümle 4: «Top kumda yuvarlanarak uzağa gitti.»
   - Açıklama: Top uzağa gidiyor ama geri getirilmeden Necati onu yeniden atıyor; olaylar birbirinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0291` birebir aynı, `@degisim: demet -> hortum` (tutuyorsan), ardından `@onarim: 8489af8af4c378b950207f4302580cba04350e90`, sonra gövde.

### Hikâye 9: tohum sakir-0292 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0292
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'şemsiye', fiil 'başlamak', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: oyun evinden garip bir tık tık sesi geldi | şapkasını ıslak yerin üstüne tuttu ve sesi buldu
@tohum: sakir-0292
Bir sabah Şakir parkta oynarken hafif bir yağmur başladı. Şakir şemsiyesi olmadığı için küçük oyun evine koştu. Ama içeriden garip bir tık tık sesi geldi ve Şakir durdu. Şakir, içeride ne var diye çok merak etti. Kapıdan baktı ve yerde ıslak bir yer gördü. Ses tam oradan geliyordu. Şakir şapkasını çıkardı ve ıslak yerin üstüne tuttu. Tık tık sesi şimdi şapkanın üstünden geldi. Şakir yukarı baktı ve tavanda küçük bir delik gördü. Yağmur damlaları o delikten içeri düşüyordu. Oyun evi güvenliydi. Şakir şapkasını taktı ve kuru bir köşeye oturdu. Şakir bundan sonra garip bir ses duyunca önce nereden geldiğine baktı.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yerde ıslak bir yer gördü"
   - Cümle 5: «Kapıdan baktı ve yerde ıslak bir yer gördü.»
   - Açıklama: 'Yer' kelimesi aynı cümlede gereksiz tekrarlanıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yerde ıslak bir yer"
   - Cümle 5: «Kapıdan baktı ve yerde ıslak bir yer gördü.»
   - Açıklama: 'Yerde' ve 'yer' aynı cümlede gereksiz tekrar ediliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyun evi güvenliydi."
   - Cümle 11: «Oyun evi güvenliydi.»
   - Açıklama: 'Güvenli' soyut bir kavram; 3 yaşındaki çocuk için somut değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir bundan sonra garip"
   - Cümle 13: «Şakir bundan sonra garip bir ses duyunca önce nereden geldiğine baktı.»
   - Açıklama: 'Bundan sonra' ile '-dı' uyumsuz; 'bakardı' ya da 'bakacaktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0292` birebir aynı, ardından `@onarim: 2e5e1cd9a34a59221626992bc47a724194a06db9`, sonra gövde.

### Hikâye 10: tohum sakir-0293 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0293
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ay', fiil 'değmek', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: güneş çok parlaktı ve beyaz aya bakamadı | şapkasıyla gölge yaptı ve aya rahatça baktı
@tohum: sakir-0293
@degisim: bulutlu -> mavi
Ormanda serin bir rüzgar esiyordu. Şakir çadırın önünde otururken gökyüzünde beyaz bir ay gördü. Aya iyice bakmak istedi, ama güneş çok parlaktı. Şakir elini gözlerinin üstüne koydu, ama eli küçüktü. Sonra şapkasını öne çekti ve şapkanın kenarı alnına değdi. Şapka güneşi kapattı ve gözlerine gölge yaptı. Şimdi ay mavi gökyüzünde rahatça görünüyordu. Ay yuvarlak değildi, bir yanı eksikti. Şakir ona uzun uzun baktı ve hiç sıkılmadı. Sonra Şakir aya mutlu mutlu el salladı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama güneş çok parlaktı"
   - Cümle 3: «Aya iyice bakmak istedi, ama güneş çok parlaktı.»
   - Açıklama: Gündüz aya bakamamak çocuğun önemseyeceği zayıf bir sorun ve elin küçük olduğu için gölge yapamaması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0293` birebir aynı, `@degisim: bulutlu -> mavi` (tutuyorsan), ardından `@onarim: f4377b03277ca436c9df04806b52a21d88efc3ae`, sonra gövde.

### Hikâye 11: tohum sakir-0299 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0299
- yer: park (Şehirdeki park.)
- tema: paylaşmak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'rüzgar', fiil 'düzeltmek', sıfat 'saklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: rüzgar esti ve annesinin kurabiyesi yere düştü | şapkasında saklı kurabiyeyi annesiyle paylaştı
@tohum: sakir-0299
Şakir ile annesi Kadriye parkta bir bankta oturuyordu. Şakir'in şapkasında, parkta yemek için saklı iki kurabiye vardı. Birden sert bir rüzgar esti ve Kadriye'nin peçetesindeki kurabiye yere düştü. Kurabiye kirlendi ve Kadriye biraz üzüldü. Şakir hemen başındaki şapkasını çıkardı ve bir kurabiye aldı. "Anneciğim, al, bu senin," dedi Şakir. Kadriye kurabiyeyi aldı ve gülümsedi. "Şapkanda yiyecek mi saklıyorsun?" diye sordu Kadriye ve güldü. Sonra şapkayı Şakir'in başına taktı ve düzeltti. Şakir ile annesi bankta mutlu mutlu kurabiye yedi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "parkta yemek için saklı"
   - Cümle 2: «Şakir'in şapkasında, parkta yemek için saklı iki kurabiye vardı.»
   - Açıklama: 'Parkta' bir önceki cümlede geçtiği halde gereksizce tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0299` birebir aynı, ardından `@onarim: 4a4bdc681cfcdc1509e152b711735380f504b351`, sonra gövde.
