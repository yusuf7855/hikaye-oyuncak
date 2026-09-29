# Editör görevi (onarım): Şakir, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 4 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0005 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0005
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kepçe', fiil 'oturtmak', sıfat 'devasa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: mutfaktaki bir ses yüzünden masal duyulmuyordu | şapkasını çıkarıp sesi dinledi ve kepçeyi kaldırdı
@tohum: sakir-0005
@degisim: devasa -> kocaman
Şakir salonda annesi Kadriye'nin yanına geldi. Kadriye onu koltukta yanına oturttu ve masal okumaya başladı. Ama mutfaktan garip bir ses geliyordu. Ses yüzünden Şakir masalı iyi duyamıyordu. "Anne, bu ses nereden geliyor?" diye sordu Şakir. "Bilmiyorum, Şakir. Bakar mısın?" dedi Kadriye. Şakir mutfağa yürüdü ve şapkasını çıkardı. Böylece kulakları sesi daha iyi duydu. Ses açık pencerenin yanından geliyordu. Rüzgar esince duvardaki kepçe kocaman bir tencereye vuruyordu. Şakir kepçeyi çekmeceye koydu ve ses durdu. Şakir çok sevindi, çünkü artık masalı rahatça dinleyebilecekti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ses yüzünden Şakir masalı iyi duyamıyordu"
   - Cümle 4: «Ses yüzünden Şakir masalı iyi duyamıyordu.»
   - Açıklama: Masalın duyulmaması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir mutfağa yürüdü ve şapkasını çıkardı"
   - Cümle 8: «Şakir mutfağa yürüdü ve şapkasını çıkardı.»
   - Açıklama: Karttaki özellik Şakir'in hep şapka taktığını söylüyor; hikaye özelliği şapkayı çıkararak tersine çeviriyor ve kulakların daha iyi duyması kartta olmayan bir işlev ekliyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Böylece kulakları sesi daha iyi duydu"
   - Cümle 9: «Böylece kulakları sesi daha iyi duydu.»
   - Açıklama: Duyan Şakir'dir; 'kulakları duydu' özneye uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0005` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: 16ce27592683ccd09bdd20736b0f7a37b046c851`, sonra gövde.

### Hikâye 2: tohum sakir-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0006
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'alet', fiil 'yapışmak', sıfat 'sadık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kum çok kuruydu ve kule hep yıkıldı | şapkasını ıslak kumla doldurup kalenin üstüne ters çevirdi
@tohum: sakir-0006
@degisim: sadık -> ıslak
Rüzgar esiyordu ve Şakir kumsalda Fil Necati ile kale yapıyordu. Necati küçük bir kum aletiyle kaleye kule yapıyordu. Ama kum çok kuruydu ve kule hep yıkılıyordu. "Bu kule hiç durmuyor," dedi Necati üzgün üzgün. Şakir su kenarındaki kumun ıslak olduğunu gördü. Şapkasını çıkardı ve o kumla doldurdu. Sonra şapkayı kalenin üstüne ters çevirdi. Ardından onu yavaşça yukarı kaldırdı. Kum birbirine yapışmıştı ve kule şapkaya benziyordu. "Şapkalı kule harika oldu, Şakir!" dedi Necati. Şakir ile Necati, ıslak kumla yapılan kulenin yıkılmadığını öğrendi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkalı kule harika oldu"
   - Cümle 10: «"Şapkalı kule harika oldu, Şakir!" dedi Necati.»
   - Açıklama: Kule şapkaya benziyor, üstünde şapka yok; 'şapkalı' yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: ""Şapkalı kule harika oldu, Şakir!""
   - Cümle 10: «"Şapkalı kule harika oldu, Şakir!" dedi Necati.»
   - Açıklama: 'Şapkalı' şapka takan demek; kule şapka biçiminde olduğu için kelime yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0006` birebir aynı, `@degisim: sadık -> ıslak` (tutuyorsan), ardından `@onarim: d95716ffcb1f27113b6522b76aee628dc4ec8c7a`, sonra gövde.

### Hikâye 3: tohum sakir-0007 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0007
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: kaybolan eşya
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'silgi', fiil 'yorulmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: silgi elinden kaydı ve kayboldu | koltuğun altına ve yastıkların arasına baktı
@tohum: sakir-0007
@degisim: sağlam -> yumuşak
Salonda Şakir koltukta oturmuş, resim yapıyordu. Silgisi birden elinden kaydı ve kayboldu. Şakir kağıttaki fazla bir çizgiyi silmek istiyordu. Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı. Silgi koltukta otururken elinden düşmüştü. Bu yüzden önce koltuğun altına baktı ama silgi orada yoktu. Sonra koltuğun yumuşak yastıklarını tek tek kaldırdı. Silgi iki yastığın arasına düşmüştü! Şakir silgiyi aldı ve fazla çizgiyi hemen sildi. Resmi yine tertemiz oldu. Şakir çok sevindi, çünkü kayıp silgisini kendisi bulmuştu.
```

**Hakem bulguları (9):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarını çok severdi"
   - Cümle 4: «Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunlarını çok severdi"
   - Cümle 4: «Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı"
   - Cümle 4: «Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiliyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macera oyunlarını çok severdi"
   - Cümle 4: «Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, silgiyi bulmada işe yarar biçimde kullanılmamış.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı"
   - Cümle 4: «Şakir macera oyunlarını çok severdi, bu yüzden aramaktan hiç yorulmadı.»
   - Açıklama: Macera sevgisi aramaya zorlama bir sebep olarak ekleniyor ve kısa aramada yorulma söz konusu olmadığı için işlevsiz bir ayrıntı kalıyor.
   - Açıklama: Arama henüz başlamadan yorulmadığı söyleniyor ve macera sevgisi olaydan çıkmayan, işlevsiz bir ayrıntı olarak araya giriyor.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Silgi koltukta otururken elinden düşmüştü"
   - Cümle 5: «Silgi koltukta otururken elinden düşmüştü.»
   - Açıklama: 'Otururken' zarf-fiilinin öznesi cümlenin öznesi olan silgiye bağlanıyor; 'Şakir koltukta otururken silgi elinden düşmüştü' olmalı.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Silgi koltukta otururken elinden düşmüştü"
   - Cümle 5: «Silgi koltukta otururken elinden düşmüştü.»
   - Açıklama: Cümlede oturan özne silgi gibi okunuyor; silgi oturmaz.
8. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Silgi koltukta otururken elinden düşmüştü"
   - Cümle 5: «Silgi koltukta otururken elinden düşmüştü.»
   - Açıklama: Silginin elinden düştüğü 2. cümlede zaten söylenmişti; gereksiz tekrar.
9. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "koltukta otururken elinden düşmüştü"
   - Cümle 5: «Silgi koltukta otururken elinden düşmüştü.»
   - Açıklama: Silginin elinden düştüğü 2. cümlede zaten söylenmişti; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0007` birebir aynı, `@degisim: sağlam -> yumuşak` (tutuyorsan), ardından `@onarim: 38ddc996d91ba69a305f3dd2f36d0e9e05b22bdf`, sonra gövde.

### Hikâye 4: tohum sakir-0009 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0009
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'jöle', fiil 'kurulanmak', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: oyun için taç gerekiyordu ama evde taç yoktu | kağıdı sarıya boyayıp şapkasının çevresine sardı
@tohum: sakir-0009
@degisim: jöle -> kağıt
Banyoda Şakir yumuşak bir havluyla kurulandı. Sonra şapkasını taktı ve salona koştu. Şakir, ormanın en büyük aslanı olma oyunu oynamak istiyordu. Ama oyunda başına bir taç gerekiyordu ve evde hiç taç yoktu. Şakir biraz düşündü ve şapkasına baktı. Masadan uzun bir kağıt aldı. Kağıdı sarı boya kalemiyle baştan sona boyadı. Şapkasını çıkardı ve boyalı kağıdı onun çevresine sardı. Şapka artık sarı bir taç gibi olmuştu. Şakir şapkayı yine başına taktı ve aynaya baktı. Koltuğa oturdu ve oyununu mutlu mutlu oynadı. Şakir, eksik bir şeyi kendisinin de yapabileceğini öğrendi.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Banyoda Şakir yumuşak bir havluyla kurulandı"
   - Cümle 1: «Banyoda Şakir yumuşak bir havluyla kurulandı.»
   - Açıklama: Banyoda kurulanma olayı hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Banyoda kurulanma olayla ilgisiz, işlevsiz bir ayrıntı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Şakir, ormanın en büyük aslanı olma oyunu oynamak istiyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama oyunda başına bir taç gerekiyordu"
   - Cümle 4: «Ama oyunda başına bir taç gerekiyordu ve evde hiç taç yoktu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "eksik bir şeyi kendisinin de yapabileceğini öğrendi"
   - Cümle 12: «Şakir, eksik bir şeyi kendisinin de yapabileceğini öğrendi.»
   - Açıklama: Ders cümlesi soyut ve 3 yaşındaki çocuk için anlaşılması güç; olaydan çıkan somut bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0009` birebir aynı, `@degisim: jöle -> kağıt` (tutuyorsan), ardından `@onarim: f027eaf5a89df643b38eb5c2d701988bb28b4a64`, sonra gövde.
