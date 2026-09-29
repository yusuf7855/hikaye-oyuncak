# Editör görevi (onarım): Şakir, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar29.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0100
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yün', fiil 'sunmak', sıfat 'çilekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: kavanozun kapağı çok sıkıydı ve açılmadı | babasından yardım isteyip kapağı yün şapkayla çevirdi
@tohum: sakir-0100
Şakir kamp yerinde babasına çilekli bisküvi sunmak istedi. Ama kavanozun kapağı çok sıkıydı. Şakir kapağı çevirdi ama elleri kaydı ve kapak açılmadı. "Baba, kavanozu tutar mısın?" diye sordu Şakir. Remzi kavanozu iki eliyle sıkıca tuttu. Şakir de yün şapkasıyla kapağı tuttu ve çevirdi. Yün kaymadı ve kapak bu kez döndü. Kavanoz sonunda açıldı. Şakir babasına bir bisküvi uzattı. "Teşekkürler, Şakir, bisküvi çok güzel kokuyor!" dedi Remzi. İkisi çadırın önünde oturup bisküvileri yedi. Şakir çok sevindi, çünkü kavanozu babasıyla birlikte açmıştı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi kavanozu iki eliyle"
   - Cümle 5: «Remzi kavanozu iki eliyle sıkıca tuttu.»
   - Açıklama: Remzi adı babayla ilişkilendirilmeden birden kullanılıyor; kimi gösterdiği belli değil.
   - Açıklama: Remzi adı babanın adı olduğu söylenmeden birden geçiyor; kimin kastedildiği çocuk için belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0100` birebir aynı, ardından `@onarim: d2c1507b4a528bf7e7ec89593d412c5e8b7fc760`, sonra gövde.

### Hikâye 2: tohum sakir-0101 (deneme 1 -> 2)

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
Şakir ile Canan kamp yerinde küçük bir ev yapıyordu. Evi bir ağacın dibine kurmuşlardı. Evin duvarları dallardan yapılmıştı, çatısı da büyük bir yapraktı. Ama birden rüzgar esti ve çatı havada süzüldü, uzağa gitti. "Evimizin çatısı gitti, Şakir," dedi Canan. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı evin üstüne yavaşça yerleştirdi. Şapka yapraktan ağırdı ve rüzgarda uçmadı. Yeni çatı evi tam kapattı. Canan çok hevesliydi ve evin önüne küçük taşlar dizdi. "Şapkalı evimiz çok güzel oldu, Şakir!" dedi Canan.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama birden rüzgar esti ve çatı havada süzüldü, uzağa gitti.»
   - Açıklama: Çatının uçması sorunu ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0101` birebir aynı, ardından `@onarim: 41882ff5cfeea90612bd63afd8b60e1c7eec2e34`, sonra gövde.

### Hikâye 3: tohum sakir-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0104
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'külah', fiil 'gülmek', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar düşen yaprakları hep elinden götürdü | şapkasını ters çevirip yaprakları içine yakaladı
@tohum: sakir-0104
Park ferah ve serindi. Şakir ağaçtan sarı yaprakların yavaş yavaş düştüğünü fark etti. Bir yaprağı yere düşmeden yakalamak istedi ama rüzgar yaprakları hep götürdü. Şakir ellerine baktı ve şapkasını çıkardı. Şapkayı ters çevirip bir dondurma külahı gibi tuttu. Sonra ağacın altında sessizce bekledi. Bir yaprak süzülerek şapkanın içine düştü. Şakir sevinçle güldü. Az sonra şapkaya iki sarı yaprak daha girdi. Sonra üç yaprağı dikkatle çimenlerin üstüne dizdi. Şakir bundan sonra yaprak yakalarken şapkasını ters tuttu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yaprakları hep elinden götürdü"
   - Cümle 0 (plan satırı): «rüzgar düşen yaprakları hep elinden götürdü | şapkasını ters çevirip yaprakları içine yakaladı»
   - Açıklama: Yapraklar hiç Şakir'in elinde olmadığı için 'elinden götürdü' yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Park ferah ve serindi."
   - Cümle 1: «Park ferah ve serindi.»
   - Açıklama: 'Ferah' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0104` birebir aynı, ardından `@onarim: c47aa08e6269bcc06a2e55e814b1e851608a36ab`, sonra gövde.

### Hikâye 4: tohum sakir-0108 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kumun bir yeri kabarmıştı ve altında bir şey vardı | şapkasını kürek gibi kullanıp kumu kenara itti
@tohum: sakir-0108
Şakir deniz kıyısında oturmuş, erik yiyordu. Önündeki kumun bir yeri küçük bir tepe gibi kabarmıştı. Şakir düşünceli düşünceli oraya baktı ve altında ne olduğunu merak etti. Yanında hiç kürek yoktu. Şakir şapkasını çıkardı ve onu bir kürek gibi kullandı. Kumu yavaş yavaş kenara itti. Kumun altından büyük, beyaz bir deniz kabuğu çıktı. Kabuğun içi pembeydi ve güneşte parlıyordu. Şakir kabuğu kulağına tuttu. İçinden denize benzeyen hafif bir ses geldi. Şapkasındaki kumu silkeledi ve şapkayı yeniden taktı. Sonra Şakir kabuğu dinleyerek eriklerini mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "altında ne olduğunu merak etti"
   - Cümle 3: «Şakir düşünceli düşünceli oraya baktı ve altında ne olduğunu merak etti.»
   - Açıklama: Kabarık kum gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir sorun ve sebebi kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İçinden denize benzeyen hafif bir ses geldi"
   - Cümle 10: «İçinden denize benzeyen hafif bir ses geldi.»
   - Açıklama: Ses denize benzemez; 'deniz sesine benzeyen' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0108` birebir aynı, ardından `@onarim: e78f5dfda465cbe38df88caf00fa14c19eb56276`, sonra gövde.

### Hikâye 5: tohum sakir-0109 (deneme 1 -> 2)

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
@degisim: büyütmek -> çekmek
Parkta güneşli bir gündü. Şakir karpuz desenli küçük topuyla oynuyordu. Top bir taşa çarptı ve bankın altına yuvarlandı. Şakir eğilip baktı ama bankın altı karanlıktı ve top görünmüyordu. Kolunu uzattı ama top çok uzaktaydı. Sonra zarif, beyaz şapkasını çıkardı. Şapkayı topun arkasına uzattı ve yavaşça kendine doğru çekti. Top şapkanın önünde dışarı yuvarlandı. Şakir topu iki eliyle sıkıca tuttu. Şapkanın tozunu silkeledi ve onu yeniden taktı. Sonra Şakir topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bankın altı karanlıktı ve top görünmüyordu"
   - Cümle 4: «Şakir eğilip baktı ama bankın altı karanlıktı ve top görünmüyordu.»
   - Açıklama: Top görünmüyor denirken Şakir topun uzakta olduğunu biliyor ve şapkayı tam topun arkasına uzatıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra zarif, beyaz şapkasını"
   - Cümle 6: «Sonra zarif, beyaz şapkasını çıkardı.»
   - Açıklama: 'Zarif' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şapkayı topun arkasına uzattı"
   - Cümle 7: «Şapkayı topun arkasına uzattı ve yavaşça kendine doğru çekti.»
   - Açıklama: Top görünmüyor ve kol yetişmiyorken Şakir şapkayı topun arkasına uzatabiliyor; bu önceki cümlelerle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0109` birebir aynı, `@degisim: büyütmek -> çekmek` (tutuyorsan), ardından `@onarim: 03203db1985b553c2f0ed8e27da7c394559abe34`, sonra gövde.

### Hikâye 6: tohum sakir-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0115
- yer: park (Şehirdeki park.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'turp', fiil 'dağılmak', sıfat 'sevimli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: kar çok kuruydu ve topladığı kar dağıldı | karı şapkasına doldurup sıkıca bastırdı
@tohum: sakir-0115
Kar sessizce yağıyordu. Şakir parkta kardan küçük bir kule yapmak istedi. Ama kar çok kuruydu ve topladığı kar hemen dağıldı. Şakir biraz düşündü ve şapkasını çıkardı. Şapkanın içini karla doldurdu ve iki eliyle sıkıca bastırdı. Sonra şapkayı ters çevirip karı yere bıraktı. Yerde sağlam, yuvarlak bir kar parçası duruyordu. Şakir aynı şeyi iki kez daha yaptı ve parçaları üst üste koydu. En üste getirdiği kırmızı turpu bayrak gibi taktı. Kule çok sevimli oldu ve hiç yıkılmadı. Şakir bundan sonra kuru karı hep bir kalıba doldurup bastırdı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "En üste getirdiği kırmızı turpu bayrak gibi taktı"
   - Cümle 9: «En üste getirdiği kırmızı turpu bayrak gibi taktı.»
   - Açıklama: Kırmızı turp daha önce hiç anılmadan sebepsiz beliriyor.
   - Açıklama: Kırmızı turp daha önce hiç kurulmadan sebepsizce beliriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hep bir kalıba doldurup"
   - Cümle 11: «Şakir bundan sonra kuru karı hep bir kalıba doldurup bastırdı.»
   - Açıklama: 'Kalıp' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0115` birebir aynı, ardından `@onarim: dcb14ec77f650dd07efbf5df5be8b87ffbf42f6d`, sonra gövde.

### Hikâye 7: tohum sakir-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0117
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yumurta', fiil 'koklamak', sıfat 'gri'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: güneş kitabın sayfalarına vurdu ve kardeşi okuyamadı | şapkasını kardeşinin başına takıp gölge yaptı
@tohum: sakir-0117
Bir sabah Şakir ile Canan kumsalda oturuyordu. Canan gri kapaklı kitabını açtı ve yeni sayfalarını kokladı. Ama güneş sayfalara çok parlak vuruyordu ve Canan okuyamıyordu. Şakir kardeşine yardım etmek istedi. Şapkasını çıkarıp Canan'ın başına taktı. Şapkanın geniş kenarı sayfalara gölge yaptı. Canan artık kitabını rahatça okudu. Kitapta büyük, benekli bir yumurta resmi vardı. Canan resmi parmağıyla Şakir'e gösterdi. Şakir de resme baktı ve gülümsedi. Şakir çok sevindi, çünkü kardeşi gölgede kitabını okuyabiliyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kitapta büyük, benekli bir yumurta resmi vardı"
   - Cümle 8: «Kitapta büyük, benekli bir yumurta resmi vardı.»
   - Açıklama: Yumurta resmi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Yumurta resmi sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0117` birebir aynı, ardından `@onarim: f755b6d3f0d342c9fb5b0e62c02bc0828365018d`, sonra gövde.

### Hikâye 8: tohum sakir-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0122
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'elmas', fiil 'katlamak', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: kurabiyeleri koymak için tabak yoktu | şapkasının kenarını katlayıp ondan tabak yaptı
@tohum: sakir-0122
Şakir kampta annesiyle kurabiye paylaşmak istedi. Kurabiyeler elmas gibi dört köşeydi. Ama hiç tabak yoktu ve yer tozluydu. Annesi Kadriye uykuluydu ve çadırın önünde oturdu. Şakir şapkasına baktı. Onu çıkardı ve kenarını yukarı katladı. Şapka küçük bir tabak gibi oldu. Şakir kurabiyeleri şapkaya dizdi ve annesine götürdü. Kadriye onları görünce güldü. Şakir yarısını annesine verdi, yarısını da kendine aldı. İkisi yan yana oturup yedi. Annesi ona sarıldı. Şakir çok sevindi, çünkü kurabiyeleri annesiyle birlikte yemişti.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "elmas gibi dört köşeydi"
   - Cümle 2: «Kurabiyeler elmas gibi dört köşeydi.»
   - Açıklama: Sıfat eki eksik; 'dört köşeliydi' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurabiyeler elmas gibi"
   - Cümle 2: «Kurabiyeler elmas gibi dört köşeydi.»
   - Açıklama: 'Elmas gibi' benzetmesi 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurabiyeler elmas gibi dört köşeydi."
   - Cümle 2: «Kurabiyeler elmas gibi dört köşeydi.»
   - Açıklama: 'Elmas gibi dört köşe' benzetmesini 3 yaşındaki bir çocuk anlamaz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurabiyeler elmas gibi dört köşeydi"
   - Cümle 2: «Kurabiyeler elmas gibi dört köşeydi.»
   - Açıklama: Kurabiyelerin biçimi kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Kurabiyelerin şekli olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama hiç tabak yoktu"
   - Cümle 3: «Ama hiç tabak yoktu ve yer tozluydu.»
   - Açıklama: Kampta neden tabak olmadığı söylenmiyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi Kadriye uykuluydu"
   - Cümle 4: «Annesi Kadriye uykuluydu ve çadırın önünde oturdu.»
   - Açıklama: Annenin uykulu olması kuruluyor ama olayda hiçbir işlevi yok.
   - Açıklama: Annenin uykulu olması kuruluyor ama hikayede hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0122` birebir aynı, ardından `@onarim: 2ea2cf63e16f880e45b09db2214a51382b2874ac`, sonra gövde.

### Hikâye 9: tohum sakir-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0123
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'gardırop', fiil 'gülüşmek', sıfat 'koyu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: balon gardırobun üstünde kaldı ve oyun durdu | şapkasını balona atıp onu aşağı düşürdü
@tohum: sakir-0123
Dışarıda yağmur cama tık tık vuruyordu. Şakir ile annesi Kadriye evde balonu yere düşürmeden havaya atıyordu. Ama Kadriye balona çok güçlü vurdu ve balon gardırobun üstünde kaldı. Koyu kahverengi gardırop çok yüksekti. "Balonumuz orada kaldı, anneciğim!" dedi Şakir. Sonra şapkasını çıkardı ve balona doğru yavaşça attı. Şapka balona değdi ve balon aşağı süzüldü. Şapka da halının üstüne düştü. "Harika bir atış, Şakir!" dedi Kadriye. İkisi birlikte gülüştü. Şakir çok sevindi, çünkü balon oyunları yeniden başlayabilirdi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "İkisi birlikte gülüştü"
   - Cümle 10: «İkisi birlikte gülüştü.»
   - Açıklama: 'Gülüştü' zaten birlikteliği anlatır; 'birlikte' gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0123` birebir aynı, ardından `@onarim: 62576cfc0c484742b5131b7c1cc53708257ff79f`, sonra gövde.
