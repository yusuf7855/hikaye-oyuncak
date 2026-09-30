# Editör görevi (onarım): Şakir, onarım partisi 51

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar51.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar51.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0261 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0261
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bezelye', fiil 'satmak', sıfat 'ahşap'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: hızlı koşarken masaya çarptı ve bezelye döküldü | özür diledi ve taneleri şapkasıyla topladı
@tohum: sakir-0261
Rüzgar hafif hafif esiyordu. Canan ahşap bir masada Şakir'e bezelye satıyordu. Şakir hızlı koşarak geldi, masaya çarptı ve bezelyeler otlara döküldü. Canan buna çok üzüldü. "Özür dilerim, Canan, çok hızlı koştum," dedi Şakir. Sonra şapkasını çıkarıp ters çevirdi. Taneleri tek tek toplayıp içine koydu. Hepsini masanın üstüne yavaşça boşalttı. "Teşekkürler, Şakir," dedi Canan ve güldü. Sonra Canan ona bir avuç bezelye sattı. İkisi de çok sevindi, çünkü bezelyeler yeniden masadaydı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Canan ahşap bir masada Şakir'e bezelye satıyordu"
   - Cümle 2: «Canan ahşap bir masada Şakir'e bezelye satıyordu.»
   - Açıklama: Orman tarifi dağda ağaçlar arasında kamp yeri diyor; hikayede kamp yeri yerine bir satış tezgahı var.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Canan ahşap bir masada Şakir'e bezelye satıyordu"
   - Cümle 2: «Canan ahşap bir masada Şakir'e bezelye satıyordu.»
   - Açıklama: Canan bezelyeyi zaten Şakir'e satıyorken Şakir sonradan koşarak geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0261` birebir aynı, ardından `@onarim: 1ac6c502b7c2cd772314539aba74b1f5a9b36a18`, sonra gövde.

### Hikâye 2: tohum sakir-0271 (deneme 3 -> 4)

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
@plan: rüzgar kumu kaldırıp sandviçlere doğru getiriyordu | şapkasını öne çekip kumdan bloklarla duvar kurdu
@tohum: sakir-0271
Rüzgar esiyordu. Şakir ile annesi Kadriye kumsalda oturmuş, sandviç yiyordu. Ama rüzgar kumu kaldırıp sandviçlere doğru getiriyordu. "Sandviçlerimize kum gelecek," dedi Kadriye. Şakir biraz düşündü. Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi. Patileriyle ıslak kumdan küçük bir blok yaptı. Şakir böyle iki blok daha yaptı ve sandviçlerin önüne dizdi. Bloklar küçük bir duvar oldu. Artık sandviçler rüzgardan korunuyordu. Kadriye yemeğini rahatça bitirdi ve Şakir'e sarıldı. "Sen çok zekisin, teşekkürler, Şakir!" dedi Kadriye.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi"
   - Cümle 6: «Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi.»
   - Açıklama: Tohumdaki şapka özelliği sorunu çözmüyor; çözüm kumdan bloklarla yapılıyor ve şapka yalnız süs gibi kalıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra şapkasını öne çekti"
   - Cümle 6: «Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi.»
   - Açıklama: Tohumdaki şapka özelliği sorunu çözmüyor, yalnız göz korumak için geçiyor; sorunu kum bloklardan duvar çözüyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra şapkasını öne çekti"
   - Cümle 6: «Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi.»
   - Açıklama: Şapkayı öne çekmek sandviçlere gelen kuma yönelmiyor ve çözüm ikiden fazla adıma yayılıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi"
   - Cümle 6: «Sonra şapkasını öne çekti, böylece gözlerine kum gelmedi.»
   - Açıklama: Şapkayı öne çekmek sandviçlere gelen kuma değil Şakir'in gözlerine yönelik, çözüm sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0271` birebir aynı, ardından `@onarim: 1a6ba3788829379f47e516634b35ab62f0850a5d`, sonra gövde.

### Hikâye 3: tohum sakir-0273 (deneme 3 -> 4)

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
Güneş ağaçların arasından parlıyordu. Şakir kamp yerinde boş ve büyük bir karton kutu buldu. Ondan bir araba yapmak istedi ama arabanın direksiyonu yoktu. Şakir kutuya baktı ve biraz düşündü. Sonra yuvarlak şapkasını çıkardı. Onu iki eliyle sıkıca direksiyon gibi tuttu. Şakir yeni karton arabasına yavaşça bindi. Şakir şapkayı bir sağa bir sola çevirdi. Ağzıyla vın vın diye yüksek bir araba sesi çıkardı. Şakir karton arabasıyla kamp yerinde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir şapkayı bir sağa"
   - Cümle 8: «Şakir şapkayı bir sağa bir sola çevirdi.»
   - Açıklama: Art arda cümleler gereksiz yere 'Şakir' adıyla başlıyor; zamir yeterli.
   - Açıklama: Art arda cümleler gereksiz yere hep 'Şakir' adıyla başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0273` birebir aynı, `@degisim: sıcacık -> büyük` (tutuyorsan), ardından `@onarim: 0f5d8624807919fa0d8796b6dfeb34408958ba4b`, sonra gövde.

### Hikâye 4: tohum sakir-0282 (deneme 3 -> 4)

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
@plan: oyuncak fırının kapağı eskiydi ve kapanmadı | fırının önünü şapkasıyla kapattı
@tohum: sakir-0282
@degisim: keşfetmek -> bulmak
Şakir evde soslu bir oyun pizzası yapıyordu. Mutfakta bulduğu çekirdekleri pizzanın üstüne dizdi ve pizzayı fırına koymak istedi. Ama oyuncak fırının kapağı çok eskiydi ve kapanmıyordu. Şakir kapağı iki kez itti, yine olmadı. Sonra büyük beyaz şapkasını çıkardı. Pizzayı fırına koydu ve önünü şapkayla kapattı. Şapka, fırının yeni kapağı oldu. Şakir yavaşça bir, iki, üç diye saydı. Sonra şapkayı kaldırdı ve pizzayı bir tabağa aldı. Oyunda çekirdekli pizza artık hazırdı. Şakir çok sevindi, çünkü pizzasını fırında pişirmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Oyunda çekirdekli pizza artık hazırdı."
   - Cümle 10: «Oyunda çekirdekli pizza artık hazırdı.»
   - Açıklama: 'Oyunda' başta asılı kalıyor ve cümle bozuk kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0282` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 5b07c922726e7b15e5395e21bcec36552d45c8d1`, sonra gövde.

### Hikâye 5: tohum sakir-0288 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Parkta Şakir ile kardeşi Canan komik bir oyun oynuyordu. Canan uyur gibi yapacak, Şakir onu uyandırırsa kremalı kekin ilk dilimini alacaktı. Canan çimlere uzandı, ama Şakir'in oyuncak saati bozuktu ve çalmadı. Şakir düğmeye iki kez bastı, yine ses çıkmadı. Canan gözlerini kapalı tuttu ve hiç kıpırdamadı. Sonra Şakir şapkasını çıkardı. Şapkayı Canan'ın yüzüne doğru yavaşça salladı. Şapkadan gelen serin hava Canan'ın yüzüne değdi. Canan güldü ve gözlerini açtı. "Uyandım, uyandım, yüzüm serinledi!" dedi Canan. "Kazandım, ama ilk dilimi birlikte yiyelim, Canan!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir'in oyuncak saati bozuktu ve çalmadı"
   - Cümle 3: «Canan çimlere uzandı, ama Şakir'in oyuncak saati bozuktu ve çalmadı.»
   - Açıklama: Uyur gibi yapan kardeşi uyandırmak için saate gerek yok; bozuk saat çocuğun önemseyeceği gerçek bir sorun oluşturmuyor.
   - Açıklama: Uyur gibi yapan kardeşi oyuncak saatle uyandırma kurgusu yapay ve sorunun önemi zayıf.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şapkayı Canan'ın yüzüne doğru yavaşça salladı"
   - Cümle 7: «Şapkayı Canan'ın yüzüne doğru yavaşça salladı.»
   - Açıklama: Çözüm bozuk saate yönelmiyor, sebebi bir kenara bırakıp başka bir yolla sonuca gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0288` birebir aynı, ardından `@onarim: 8b8135969c2e29d5f914f5092c42ea6ffe0ac645`, sonra gövde.

### Hikâye 6: tohum sakir-0291 (deneme 3 -> 4)

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
Bir sabah Şakir, Necati'ye kumsalda top yakalama oyununu öğretiyordu. Necati topu hortumuyla atıyor, Şakir yakalıyordu. Ama lastik top çok esnekti ve Şakir'in ellerine çarpıp geri zıpladı. Şakir kumda yuvarlanan topu alıp Necati'ye geri verdi. Necati kulaklarını salladı ve güldü. Şakir de güldü ve biraz düşündü. Sonra şapkasını çıkardı ve ters çevirip iki eliyle tuttu. "Hadi, Necati, şimdi at!" dedi Şakir. Necati topu yavaşça attı. Top şapkanın içine düştü ve dışarı çıkmadı. "Yakaladın, aferin!" dedi Necati. Sonra oyunu birçok kez daha oynadılar. Şakir çok mutluydu, çünkü artık topu hiç kaçırmıyordu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "esnek top her seferinde ellerinden kaçtı"
   - Cümle 0 (plan satırı): «esnek top her seferinde ellerinden kaçtı | şapkasını ters tuttu ve topu içine yakaladı»
   - Açıklama: Top kaçmaz; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "lastik top çok esnekti"
   - Cümle 3: «Ama lastik top çok esnekti ve Şakir'in ellerine çarpıp geri zıpladı.»
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0291` birebir aynı, `@degisim: demet -> hortum` (tutuyorsan), ardından `@onarim: f291cf4e2a57e182028d80b68ad181bae1e29f04`, sonra gövde.

### Hikâye 7: tohum sakir-0293 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar şapkayı uçurdu ve karanlıkta şapka görünmedi | bulutların arkasında ay olduğunu fark etti ve bekledi
@tohum: sakir-0293
Rüzgar esiyordu. Birden rüzgar, çadırın önündeki Şakir'in beyaz şapkasını uçurdu. Şapka yakındaki çimlere düştü, ama hava bulutlu ve karanlıktı. Şakir şapkasını göremedi. Patileriyle çimlere dokundu, ama şapkayı bulamadı. Sonra gökyüzüne baktı ve bulutların arkasında parlak bir ay fark etti. Şakir orada durdu ve bekledi. Rüzgar bulutları yavaşça itti ve ay çıktı. Ay ışığı çimlere değdi. Beyaz şapka çimlerde parladı. Şakir şapkasını hemen aldı ve başına taktı. Sonra çadırının önüne oturdu ve aya mutlu mutlu baktı.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "hava bulutlu ve karanlıktı"
   - Cümle 3: «Şapka yakındaki çimlere düştü, ama hava bulutlu ve karanlıktı.»
   - Açıklama: Şakir gece karanlıkta ormandaki kamp yerinde tek başına şapkasını arıyor; 3-6 yaş için ürkütücü bir ortam.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "hava bulutlu ve karanlıktı"
   - Cümle 3: «Şapka yakındaki çimlere düştü, ama hava bulutlu ve karanlıktı.»
   - Açıklama: Şakir gece karanlıkta ormandaki kamp yerinde yalnız kalıyor; güvenli kullanım satırının tek başına kalmama ruhuna aykırı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bulutların arkasında parlak bir ay fark etti"
   - Cümle 6: «Sonra gökyüzüne baktı ve bulutların arkasında parlak bir ay fark etti.»
   - Açıklama: Tohumdaki şapka özelliği sorunu çözmekte işe yaramıyor; çözümü ay ve bekleme getiriyor, özellik yalnız kaybolan eşya olarak geçiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ay ışığı çimlere değdi"
   - Cümle 9: «Ay ışığı çimlere değdi.»
   - Açıklama: Işığın çimlere 'değmesi' küçük çocuk için mecazlı bir anlatım.
   - Açıklama: Işığın çimlere 'değmesi' mecazlı bir anlatım, küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0293` birebir aynı, ardından `@onarim: 0be43b4e5a70966e7525588f8a3e4c36b6955f57`, sonra gövde.

### Hikâye 8: tohum sakir-0299 (deneme 3 -> 4)

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
Şakir ile annesi Kadriye parkta bir bankta oturuyordu. Şakir'in şapkasında, yemek için saklı iki kurabiye vardı. Birden sert bir rüzgar esti ve Kadriye'nin peçetesindeki kurabiye yere düştü. Kurabiye kirlendi ve Kadriye biraz üzüldü. Şakir hemen başındaki şapkasını çıkardı ve bir kurabiye aldı. "Anneciğim, al, bu senin," dedi Şakir. Kadriye kurabiyeyi aldı ve gülümsedi. "Şapkanda yiyecek mi saklıyorsun?" diye sordu Kadriye ve güldü. Sonra şapkayı Şakir'in başına taktı ve düzeltti. Şakir ile annesi bankta mutlu mutlu kurabiye yedi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra şapkayı Şakir'in başına taktı"
   - Cümle 9: «Sonra şapkayı Şakir'in başına taktı ve düzeltti.»
   - Açıklama: Şapkayı Şakir çıkarmıştı; Kadriye'nin elinde olmayan şapkayı takması tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0299` birebir aynı, ardından `@onarim: 72636177126ad6b3473bda001fc3844148623f37`, sonra gövde.
