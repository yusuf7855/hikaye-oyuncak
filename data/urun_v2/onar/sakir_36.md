# Editör görevi (onarım): Şakir, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0135 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0135
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'topaç', fiil 'dalgalanmak', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: babası gelirken sürpriz topaç kumda görünüyordu | topacı şapkasıyla kapatıp sonra babasına gösterdi
@tohum: sakir-0135
Kumsalda deniz hafif hafif dalgalanıyordu. Şakir babası Remzi için renkli bir topaç getirmişti. Topacı babasına gizlice vermek istiyordu. Ama Remzi kıyıdan ona doğru geliyordu ve topaç kumda duruyordu. Babası topacı uzaktan görebilirdi. Şakir hemen başından mavi şapkasını çıkardı. Topacı şapkanın altına sakladı. Remzi geldi ve kumdaki şapkaya merakla baktı. Şakir şapkayı yavaşça kaldırdı ve renkli topaç ortaya çıktı. Remzi çok sevindi ve topacı düz bir taşın üstünde çevirdi. Topaç uzun uzun döndü ve Remzi neşeyle güldü. Şakir çok mutlu oldu, çünkü babasına güzel bir sürpriz yapmıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Topacı babasına gizlice vermek istiyordu.»
   - Açıklama: Topacın babası tarafından görülme sorunu ilk üç cümlede değil ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0135` birebir aynı, ardından `@onarim: 7c5afad89b313de2f2c8a39a27b2d7dac678ab55`, sonra gövde.

### Hikâye 2: tohum sakir-0136 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0136
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'biber', fiil 'dinmek', sıfat 'hareketsiz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: güneş filin başını ısıttı ve hiç gölge yoktu | şapkasını ona verdi ve onun gölgesinde oturdu
@tohum: sakir-0136
@degisim: biber -> gölge
Şakir ile Necati kumsalda oturuyordu. Yağmur az önce dinmişti ve güneş çıkmıştı. Rüzgar yoktu, deniz de hareketsizdi. Güneş Necati'nin büyük başını çok ısıttı. "Başım çok sıcak, burada hiç gölge yok," dedi Necati. Şakir başındaki şapkasını hemen çıkardı. Şapkayı Necati'nin başının üstüne koydu. Şapka küçüktü ama Necati'nin başını güneşten korudu. Necati güldü ve Şakir'i yanına çağırdı. Şakir de Necati'nin gölgesinde oturdu. Artık ikisi de serindi. "Teşekkürler, Şakir, şapkanı benimle paylaştın!" dedi Necati.
```

**Hakem bulguları (8):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yağmur az önce dinmişti"
   - Cümle 2: «Yağmur az önce dinmişti ve güneş çıkmıştı.»
   - Açıklama: Az önce dinen yağmur hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yağmur az önce dinmişti ve güneş çıkmıştı"
   - Cümle 2: «Yağmur az önce dinmişti ve güneş çıkmıştı.»
   - Açıklama: Yeni dinen yağmur ve durgun deniz ayrıntıları olayda hiçbir işe yaramıyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Rüzgar yoktu, deniz de hareketsizdi.»
   - Açıklama: İlk üç cümle yağmur, güneş ve rüzgardan söz ediyor; sorun ancak 4. ve 5. cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Güneş Necati'nin büyük başını çok ısıttı"
   - Cümle 4: «Güneş Necati'nin büyük başını çok ısıttı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "burada hiç gölge yok"
   - Cümle 5: «"Başım çok sıcak, burada hiç gölge yok," dedi Necati.»
   - Açıklama: Necati hiç gölge olmadığını söylüyor ama sonra Şakir Necati'nin gölgesinde oturuyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şapka küçüktü ama Necati'nin başını güneşten korudu"
   - Cümle 8: «Şapka küçüktü ama Necati'nin başını güneşten korudu.»
   - Açıklama: Küçük bir şapkanın bir filin büyük başını güneşten koruması kendi söylediğiyle çelişiyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir de Necati'nin gölgesinde oturdu"
   - Cümle 10: «Şakir de Necati'nin gölgesinde oturdu.»
   - Açıklama: 'de' bağlacı yanlış anlamda; Necati kendi gölgesinde oturmadığı için eklenecek kimse yok.
8. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkanı benimle paylaştın"
   - Cümle 12: «"Teşekkürler, Şakir, şapkanı benimle paylaştın!" dedi Necati.»
   - Açıklama: Şakir şapkayı verdi, paylaşmadı; 'paylaşmak' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0136` birebir aynı, `@degisim: biber -> gölge` (tutuyorsan), ardından `@onarim: 61be28e62e243db41dbbf4a8ddf91b35d8cb7e5a`, sonra gövde.

### Hikâye 3: tohum sakir-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0138
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'börek', fiil 'değiştirmek', sıfat 'mutsuz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: kozalaklar tabaktan dışarı zıplıyordu ve kardeşi üzüldü | tabağı derin şapkasıyla değiştirdi
@tohum: sakir-0138
Ormandaki kamp yerinde çam ağaçları vardı. Şakir ile kardeşi Canan börek yedikten sonra kozalak topladı. Boş börek tabağını yere koydular ve içine kozalak atmaya başladılar. Ama kozalaklar tabağa düşünce hep dışarı zıplıyordu. Canan hiç sayı alamadı ve mutsuz oldu. Şakir tabağa baktı ve biraz düşündü. Sonra başından derin şapkasını çıkardı. Tabağı hemen şapkayla değiştirdi. "Canan, şimdi bir daha dene," dedi Şakir. Canan bir kozalak attı. Kozalak şapkanın içine düştü ve orada kaldı. Canan sevinçle ellerini çırptı. "Teşekkürler, Şakir, artık hepsi içeride kalıyor!" dedi Canan.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Boş börek tabağını yere koydular ve içine kozalak atmaya başladılar.»
   - Açıklama: Kozalakların tabaktan zıplaması sorunu ilk üç cümlede değil ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kozalaklar tabağa düşünce hep dışarı zıplıyordu"
   - Cümle 4: «Ama kozalaklar tabağa düşünce hep dışarı zıplıyordu.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Canan hiç sayı alamadı"
   - Cümle 5: «Canan hiç sayı alamadı ve mutsuz oldu.»
   - Açıklama: 'Sayı almak' oyun terimi olarak 3 yaşındaki çocuğa soyut ve daha önce kurulmamış bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0138` birebir aynı, ardından `@onarim: fcd040f15e3746a931d8a2f03a5c473be6deb8c7`, sonra gövde.

### Hikâye 4: tohum sakir-0141 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0141
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'delik', fiil 'düzelmek', sıfat 'harika'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: rüzgarda bir yerden ıslık sesi geliyordu | şapkasıyla delikli kabuğu kapatıp sesi buldu
@tohum: sakir-0141
@degisim: düzelmek -> dinlemek
Bir sabah Şakir kumsalda yürüyordu. Rüzgar esiyordu ve bir yerden ince bir ıslık sesi geliyordu. Şakir bu sesi çok merak etti. Etrafa baktı ama sesin nereden geldiğini bulamadı. Kumda büyük beyaz bir kabuk gördü. Kabuğun üstünde küçük bir delik vardı. Şakir şapkasını çıkardı ve kabuğun üstüne kapattı. Islık hemen durdu. Şapkayı kaldırınca ıslık yeniden başladı. Rüzgar deliğin içinden geçiyor ve ıslık çalıyordu. Şakir kabuğu kulağına tuttu ve dikkatle dinledi. Sonra harika kabuğuyla kumsalda mutlu mutlu oynadı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bir yerden ince bir ıslık sesi geliyordu"
   - Cümle 2: «Rüzgar esiyordu ve bir yerden ince bir ıslık sesi geliyordu.»
   - Açıklama: Sorun yalnızca bir sesi merak etmek; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çıkardı ve kabuğun üstüne kapattı"
   - Cümle 7: «Şakir şapkasını çıkardı ve kabuğun üstüne kapattı.»
   - Açıklama: 'Kapatmak' fiili yönelme ekli 'kabuğun üstüne' ile uyumsuz; 'kabuğun üstüne koydu' ya da 'deliği kapattı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir şapkasını çıkardı ve kabuğun üstüne kapattı"
   - Cümle 7: «Şakir şapkasını çıkardı ve kabuğun üstüne kapattı.»
   - Açıklama: Şakir kabuktan şüphelendiğine dair hiçbir ipucu yokken kabuğu kapatıyor; çözüm şans eseri, sebepsizce geliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geçiyor ve ıslık çalıyordu"
   - Cümle 10: «Rüzgar deliğin içinden geçiyor ve ıslık çalıyordu.»
   - Açıklama: Rüzgarın ıslık çalması mecazlı bir anlatım.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve ıslık çalıyordu"
   - Cümle 10: «Rüzgar deliğin içinden geçiyor ve ıslık çalıyordu.»
   - Açıklama: Rüzgarın ıslık çalması kişileştirme ve mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0141` birebir aynı, `@degisim: düzelmek -> dinlemek` (tutuyorsan), ardından `@onarim: 8a68192a6da414df6f17617ca8a23704bb956e7c`, sonra gövde.

### Hikâye 5: tohum sakir-0145 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0145
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'zeytin', fiil 'öğrenmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: rüzgarda siyah küçük bir şey kumda kaçıyordu | şapkasıyla üstünü kapattı ve annesine sordu
@tohum: sakir-0145
Şakir annesi Kadriye ile kumsalda oturuyordu. Rüzgar hızlı hızlı esiyordu. Birden kumda zeytin gibi siyah küçük bir şey yuvarlandı. Meraklı Şakir hemen arkasından koştu. Ama o şey rüzgarla hep ileri kaçıyordu. Şakir başından şapkasını çıkardı ve onun üstüne kapattı. Şapkanın altında kapalı, küçük bir kabuk vardı. "Anne, bu ne?" diye sordu Şakir. "Bu bir deniz kabuğu, rüzgar onu yuvarladı," dedi Kadriye. Şakir kabuğu eline aldı ve dikkatle baktı. "Yaşasın, anneciğim, zeytin sandığım şeyin ne olduğunu öğrendim!" dedi Şakir.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "siyah küçük bir şey kumda kaçıyordu"
   - Cümle 0 (plan satırı): «rüzgarda siyah küçük bir şey kumda kaçıyordu | şapkasıyla üstünü kapattı ve annesine sordu»
   - Açıklama: Planda da cansız şey için 'kaçmak' kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarda siyah küçük bir şey kumda kaçıyordu"
   - Cümle 0 (plan satırı): «rüzgarda siyah küçük bir şey kumda kaçıyordu | şapkasıyla üstünü kapattı ve annesine sordu»
   - Açıklama: Rüzgarda yuvarlanan bir kabuk çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak anı.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Meraklı Şakir hemen arkasından koştu"
   - Cümle 4: «Meraklı Şakir hemen arkasından koştu.»
   - Açıklama: Rüzgarla hep ileri kaçan bir şeyin peşinden annesinden uzaklaşarak koşmak, güvenli kullanım satırındaki tek başına uzağa gitmez kuralına aykırı ve taklit edilebilir.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Meraklı Şakir hemen arkasından koştu"
   - Cümle 4: «Meraklı Şakir hemen arkasından koştu.»
   - Açıklama: Tohumdaki özellik şapka; merak kartta olmayan ikinci bir özellik olarak ekleniyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o şey rüzgarla hep ileri kaçıyordu"
   - Cümle 5: «Ama o şey rüzgarla hep ileri kaçıyordu.»
   - Açıklama: Cansız bir şey kaçmaz; fiil öznesine uymuyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şey rüzgarla hep ileri kaçıyordu"
   - Cümle 5: «Ama o şey rüzgarla hep ileri kaçıyordu.»
   - Açıklama: Cansız bir kabuk için 'kaçmak' fiili öznesine uymuyor; 'yuvarlanıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0145` birebir aynı, ardından `@onarim: 0b2cef958574118676141ed9c37e6c67f3266985`, sonra gövde.
