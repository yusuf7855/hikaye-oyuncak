# Editör görevi (onarım): Şakir, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0017 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0017
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fındık', fiil 'anlamak', sıfat 'peynirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kayaların arasından bilinmeyen bir ses geldi | şapkasını öne çekip delikteki fındığı gördü
@tohum: sakir-0017
Bir sabah Şakir ile Canan kumsalda peynirli poğaça ve fındık yiyordu. Birden kayaların arasından tık tık diye bir ses geldi. Şakir bu sesin ne olduğunu anlamak istedi. "Canan, bu ses nereden geliyor?" diye sordu Şakir. "Şu küçük delikten geliyor," dedi Canan. Şakir deliğe baktı, ama güneş çok parlaktı ve içini göremedi. Hemen geniş şapkasını öne doğru çekti. Şapka gözlerine gölge yaptı ve deliğin içi göründü. İçeride bir fındık vardı ve küçük dalgalar onu taşa vuruyordu. "Ses bu fındıktan geliyormuş!" dedi Canan gülerek. "Yaşasın, Canan, sesin nereden geldiğini birlikte bulduk!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "peynirli poğaça ve fındık yiyordu"
   - Cümle 1: «Bir sabah Şakir ile Canan kumsalda peynirli poğaça ve fındık yiyordu.»
   - Açıklama: Poğaça işlevsiz bir ayrıntı; delikteki fındığın oraya nasıl girdiği de söylenmiyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Şu küçük delikten geliyor"
   - Cümle 5: «"Şu küçük delikten geliyor," dedi Canan.»
   - Açıklama: Sesin yerini Canan buluyor ve sesin fındıktan geldiğini de Canan söylüyor; çözümün önemli kısmı yan karaktere kalıyor.
3. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: ""Ses bu fındıktan geliyormuş!" dedi Canan"
   - Cümle 10: «"Ses bu fındıktan geliyormuş!" dedi Canan gülerek.»
   - Açıklama: Deliğin içini Şakir gördü; keşif repliğinin Canan'a verilmesi yanlış kişi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0017` birebir aynı, ardından `@onarim: e6efa60538960fba695826e4f2179848a0e91319`, sonra gövde.

### Hikâye 2: tohum sakir-0021 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0021
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'simit', fiil 'sarmak', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil acıkmıştı ama yanında yiyecek yoktu | simidini ikiye böldü ve yarısını file verdi
@tohum: sakir-0021
Bir sabah Şakir ile Necati ormanda, ağaçların arasında yürüyordu. Ama Necati'nin karnı acıkmıştı ve yanında hiç yiyecek yoktu. Şakir macerayı çok severdi ve yürüyüşe yiyecek getirmişti. Çantasında bir beze sardığı ılık bir simit vardı. Şakir simidi çıkardı ve bezi açtı. Sonra simidi iki eşit parçaya böldü. "Necati, yarısı senin," dedi Şakir. Necati simidin yarısını hortumuyla aldı. "Teşekkür ederim, Şakir, çok acıkmıştım," dedi Necati. İkisi bir kütüğün üstüne oturdu ve simidi birlikte yedi. Şakir çok sevindi, çünkü simidini Necati ile paylaşmıştı.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "ormanda, ağaçların arasında yürüyordu"
   - Cümle 1: «Bir sabah Şakir ile Necati ormanda, ağaçların arasında yürüyordu.»
   - Açıklama: Kartın orman tarifi dağdaki kamp yeri; hikaye kamp yeri dışında ormanda yürüyüşte geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 3: «Şakir macerayı çok severdi ve yürüyüşe yiyecek getirmişti.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 3: «Şakir macerayı çok severdi ve yürüyüşe yiyecek getirmişti.»
   - Açıklama: Tohumdaki macera özelliği yalnız sayılıyor, sorunun çözümünde (simidi paylaşmak) işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve yürüyüşe yiyecek getirmişti"
   - Cümle 3: «Şakir macerayı çok severdi ve yürüyüşe yiyecek getirmişti.»
   - Açıklama: Macera özelliği ile yiyecek getirmek arasında bağ yok; özellik süs olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0021` birebir aynı, ardından `@onarim: 32b5b2f5599e0cb28d4ee012b6b4c039d68f4c6d`, sonra gövde.

### Hikâye 3: tohum sakir-0024 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Canan
@tohum: sakir-0024
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'sebze', fiil 'yürümek', sıfat 'pahalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Canan
@plan: hızlı yürürken sebze sepetine çarptı ve sebzeler döküldü | kardeşinden özür diledi ve sebzeleri topladı
@tohum: sakir-0024
@degisim: pahalı -> dolu
Evde Şakir ile Canan mutfaktaydı. Şakir hızlı hızlı yürürken önüne bakmadı. Canan'ın masadaki dolu sebze sepetine çarptı ve sebzeler yere döküldü. Canan onları az önce sepete koymuştu. Canan üzüldü ve yere baktı. Şakir hemen durdu. "Özür dilerim, Canan, dikkat etmedim," dedi Şakir. Bazı domatesler masanın altındaydı. Şakir macerayı çok severdi ve hemen masanın altına girdi. Havuçları ve domatesleri tek tek topladı. Canan da ona yardım etti. Kısa sürede sepet yine doldu. "Tamam, Şakir, birlikte hepsini topladık," dedi Canan ve gülümsedi. Şakir çok rahatladı, çünkü kardeşi artık üzgün değildi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 9: «Şakir macerayı çok severdi ve hemen masanın altına girdi.»
   - Açıklama: 'Macera' soyut bir kavram; küçük çocuk için somut değil.
   - Açıklama: 'Macera' soyut bir kavram ve masanın altına girmekle uyuşmuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 9: «Şakir macerayı çok severdi ve hemen masanın altına girdi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, masanın altına girmek için işe yarar biçimde kullanılmamış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve hemen masanın altına girdi"
   - Cümle 9: «Şakir macerayı çok severdi ve hemen masanın altına girdi.»
   - Açıklama: Sebze toplamak macera değil; tohumdaki özellik işe yaramadan etiket olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0024` birebir aynı, `@degisim: pahalı -> dolu` (tutuyorsan), ardından `@onarim: c35cf40c0017e8959588155b0fa2720c904dff4b`, sonra gövde.

### Hikâye 4: tohum sakir-0025 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0025
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'piyano', fiil 'küçültmek', sıfat 'şanslı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: fazla çiçek yüzünden taç çok büyük oldu | üç çiçek çıkarıp tacı şapkasına göre küçülttü
@tohum: sakir-0025
@degisim: piyano -> çiçek
Şakir, ormandaki kamp yerinde annesi Kadriye için bir sürpriz hazırlıyordu. Şakir şanslıydı, çünkü orada çok çiçek vardı. Onlardan bir taç yaptı. Ama fazla çiçek koyduğu için taç çok büyük oldu. Şakir tacı şapkasına taktı ama taç aşağı düştü. Üç çiçek çıkardı ve tacı küçülttü. Bu kez taç şapkada kaldı. Sonra şapkayı arkasına sakladı ve annesinin yanına koştu. "Anne, gözlerini kapar mısın?" diye sordu Şakir. Kadriye gülümsedi ve gözlerini kapadı. Şakir şapkayı tacıyla birlikte annesinin başına yavaşça koydu. Kadriye gözlerini açtı ve tacı eliyle tuttu. "Teşekkür ederim, Şakir, bu taç çok güzel!" dedi Kadriye.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir şanslıydı, çünkü"
   - Cümle 2: «Şakir şanslıydı, çünkü orada çok çiçek vardı.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "fazla çiçek koyduğu için taç çok büyük oldu"
   - Cümle 4: «Ama fazla çiçek koyduğu için taç çok büyük oldu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0025` birebir aynı, `@degisim: piyano -> çiçek` (tutuyorsan), ardından `@onarim: 927eb3daf6173c1bccfaf1b58dec74730e8af3ee`, sonra gövde.

### Hikâye 5: tohum sakir-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0026
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'palmiye', fiil 'tutunmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: palmiyeler arasında rüzgar güçlü değildi | açık bir yere koşup ipi sıkıca tuttu
@tohum: sakir-0026
@degisim: yeterli -> güçlü
Şakir babası Remzi ile kumsalda ilk kez uçurtma uçuracaktı. Remzi ona mavi bir uçurtma verdi. Ama palmiyeler arasında rüzgar güçlü değildi ve uçurtma hep kuma düştü. Şakir macerayı çok severdi ve bir daha denemek istedi. Etrafına baktı ve deniz kenarında açık bir yer gördü. Uçurtmayı aldı ve babasının eline tutunarak oraya koştu. Orada rüzgar daha güçlüydü. Şakir ipi iki eliyle sıkıca tuttu. Remzi de uçurtmayı havaya bıraktı. Mavi uçurtma hızla yükseldi ve ağaçların üstüne çıktı. Remzi sevinçle zıplayıp güldü. "Babacığım, ilk uçurtmam gökyüzünde uçuyor!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve bir daha denemek istedi.»
   - Açıklama: 'macera' soyut bir kavram; 3 yaşındaki çocuk için somut değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve bir daha denemek istedi"
   - Cümle 4: «Şakir macerayı çok severdi ve bir daha denemek istedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, sorunun çözümünde işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0026` birebir aynı, `@degisim: yeterli -> güçlü` (tutuyorsan), ardından `@onarim: 172cddc0bb70f31312cfe1fb2b5d5d13862118f4`, sonra gövde.

### Hikâye 6: tohum sakir-0027 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0027
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'süpürge', fiil 'çözmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kardeşi kitabını unuttuğu için oynayacak bir şeyi yoktu | çantanın ipini çözdü ve ikinci küreği paylaştı
@tohum: sakir-0027
@degisim: süpürge -> kürek
Rüzgar hafif hafif esiyordu. Şakir kumsalda küreğiyle büyük bir kale yapıyordu. Kardeşi Canan kitabını evde unuttuğu için oynayacak bir şeyi yoktu. Canan kumun üstünde sessiz oturuyordu. Şakir'in oyuncak çantasında bir kürek daha vardı. Şakir çantanın ipini çözdü ve ikinci küreği çıkardı. "Canan, bu kürek senin olsun, gel birlikte oynayalım!" dedi Şakir. "Ne yapacağız?" diye sordu Canan. Şakir macerayı çok severdi ve hemen yeni bir oyun buldu. "Kalenin etrafına uzun bir yol kazalım!" dedi Şakir. Canan küreği aldı ve gülümsedi. İkisi yan yana kumu kazdı. Sonunda yol kalenin etrafını tam sardı. Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 9: «Şakir macerayı çok severdi ve hemen yeni bir oyun buldu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve hemen yeni bir oyun buldu"
   - Cümle 9: «Şakir macerayı çok severdi ve hemen yeni bir oyun buldu.»
   - Açıklama: Tohumdaki macera özelliği işe yarar biçimde kullanılmıyor, yalnız karttaki özellik cümlesi tekrar ediliyor; çözüm küreği paylaşmakla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0027` birebir aynı, `@degisim: süpürge -> kürek` (tutuyorsan), ardından `@onarim: 98f6688bebe0aa45109ec74a9c42959a827be611`, sonra gövde.

### Hikâye 7: tohum sakir-0028 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0028
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tüy', fiil 'gülümsemek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kumdan pastanın mumu eksikti | şemsiyenin yanında beyaz bir tüy bulup pastaya dikti
@tohum: sakir-0028
Kumsalda Fil Necati büyük bir şemsiyenin altında uyuyordu. Şakir ona sürpriz olarak kumdan bir pasta yaptı ve üstüne kabuklar dizdi. Ama pastanın mumu eksikti ve kumsalda hiç mum yoktu. Şakir mum yerine başka bir şey bulmak istedi. Macerayı çok severdi ve hemen şemsiyenin yanındaki kumu aradı. Kumun üstünde uzun, beyaz bir tüy buldu. Tüyü pastanın tam ortasına dikti. Şimdi pasta tamamdı. Biraz sonra Necati uyandı ve pastayı gördü. Hortumuyla tüye yavaşça dokundu ve gülümsedi. Şakir de sevinçle ellerini çırptı. Şakir bundan sonra bir şey eksik olunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok severdi ve hemen şemsiyenin yanındaki kumu aradı"
   - Cümle 5: «Macerayı çok severdi ve hemen şemsiyenin yanındaki kumu aradı.»
   - Açıklama: Kartın özellikler alanındaki macera sevgisi kumda tüy aramaya yapıştırılmış, işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok severdi ve hemen"
   - Cümle 5: «Macerayı çok severdi ve hemen şemsiyenin yanındaki kumu aradı.»
   - Açıklama: Tohumdaki macera özelliği süs olarak söylenmiş, çözümde işe yarar biçimde kullanılmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Macerayı çok severdi"
   - Cümle 5: «Macerayı çok severdi ve hemen şemsiyenin yanındaki kumu aradı.»
   - Açıklama: Maceracılık ayrıntısı olayda hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumun üstünde uzun, beyaz bir tüy buldu"
   - Cümle 6: «Kumun üstünde uzun, beyaz bir tüy buldu.»
   - Açıklama: Çözümü getiren tüy önceden kurulmadan tesadüfen beliriyor.
   - Açıklama: Çözümü getiren tüy tesadüfen ortaya çıkıyor ve Şakir'in aramasıyla bir bağı kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0028` birebir aynı, ardından `@onarim: 41f3c30015003b1c1e23f520f9c1cd6228b9b476`, sonra gövde.

### Hikâye 8: tohum sakir-0029 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Remzi
@tohum: sakir-0029
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kek', fiil 'gezinmek', sıfat 'tuzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Remzi
@plan: rüzgar oyunun haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu
@tohum: sakir-0029
@degisim: tuzlu -> sarı
Parkta Şakir ile babası Remzi bir macera oyunu oynuyordu. Remzi sarı bir kutuya kek koyup saklamış, bir de harita çizmişti. Ama rüzgar esti ve harita uçup gitti. Şakir hiç üzülmedi ve oyunu bırakmadı. "Baba, yaklaşınca 'sıcak', uzaklaşınca 'soğuk' der misin?" diye sordu Şakir. "Tamam, haydi başla!" dedi Remzi gülerek. Şakir parkta gezinmeye başladı. "Soğuk, çok soğuk!" dedi Remzi ve titriyormuş gibi yaptı. Şakir döndü ve banklara doğru yürüdü. "Sıcak, çok sıcak!" dedi Remzi. Şakir bankın altına baktı ve sarı kutuyu buldu. Sonra ikisi banka oturdu ve keki mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "kek koyup saklamış, bir de"
   - Cümle 2: «Remzi sarı bir kutuya kek koyup saklamış, bir de harita çizmişti.»
   - Açıklama: Anlatımda -mış'lı çekim kullanılmış; -dı'lı geçmiş zamandan kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0029` birebir aynı, `@degisim: tuzlu -> sarı` (tutuyorsan), ardından `@onarim: 84bf0af94fbc4aab8c12eec31d7c44e7def20739`, sonra gövde.

### Hikâye 9: tohum sakir-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0031
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'patates', fiil 'göstermek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: fil ağır adımlarla yoldaki çiçeğe doğru geliyordu | fili durdurup çiçeğin etrafına taş dizdi
@tohum: sakir-0031
@degisim: patates -> çiçek
Bir sabah Şakir ile Fil Necati parkta yürüyordu. Şakir yolun ortasında ince saplı, kırılgan bir çiçek gördü. Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu. "Dur, Necati, sana bir çiçek göstermek istiyorum!" dedi Şakir. Necati durdu ve eğilip çiçeğe baktı. "Onu hiç görmemiştim," dedi Necati. Şakir çiçeği korumak istedi. Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı. Taşları çiçeğin etrafına dizdi. Şimdi çiçek uzaktan kolayca görünüyordu. Necati ayak uçlarında yürüdü ve çiçeğin yanından dikkatle geçti. "Artık çiçeğe kimse basmaz, Necati!" dedi Şakir sevinçle.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ince saplı, kırılgan bir çiçek"
   - Cümle 2: «Şakir yolun ortasında ince saplı, kırılgan bir çiçek gördü.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 8: «Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı.»
   - Açıklama: 'Macera' soyut bir kavramdır ve cümleye gereksiz bir özellik olarak eklenmiş.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Macerayı çok seven Şakir, çalıların arasından"
   - Cümle 8: «Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı.»
   - Açıklama: Zaten tanıtılmış olan Şakir hikayenin ortasında sıfatla yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı"
   - Cümle 8: «Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı.»
   - Açıklama: Kartın özellikler alanındaki macera sevgisi taş toplamaya etiket olarak eklenmiş, çözümde işe yarar biçimde kullanılmıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 8: «Macerayı çok seven Şakir, çalıların arasından dört büyük taş topladı.»
   - Açıklama: Tohumdaki macera özelliği yalnız sıfat olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0031` birebir aynı, `@degisim: patates -> çiçek` (tutuyorsan), ardından `@onarim: 677122371d659ea1de934e9a9e303cd9aaf7990e`, sonra gövde.

### Hikâye 10: tohum sakir-0032 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0032
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yelkenli', fiil 'uzaklaşmak', sıfat 'bilgili'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: oyunda geminin yelkeni yoktu | annesinden havlu isteyip bir dala bağladı
@tohum: sakir-0032
@degisim: bilgili -> büyük
Şakir, kamp yerinde yere düşmüş kalın bir ağaca oturdu. Oyunda bu ağaç bir gemi oldu ve annesi Kadriye de arkasına oturdu. Ama geminin yelkeni yoktu ve yola çıkamıyordu. Şakir macera oyununu bırakmadı ve hemen bir yelken aradı. "Anneciğim, büyük mavi havluyu alabilir miyim?" diye sordu Şakir. "Tabii, al," dedi Kadriye ve havluyu ona verdi. Şakir havluyu uzun bir dala bağladı. Sonra dalı iki eliyle havaya kaldırdı. Rüzgar esti ve havlu bir yelken gibi şişti. "Bak, anneciğim, yelkenlimiz limandan uzaklaşıyor!" dedi Şakir. Kadriye güldü ve ellerini çırptı. Şakir çok mutlu oldu, çünkü gemisi sonunda yola çıkmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyununu bırakmadı"
   - Cümle 4: «Şakir macera oyununu bırakmadı ve hemen bir yelken aradı.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki bir çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yelkenlimiz limandan uzaklaşıyor"
   - Cümle 10: «"Bak, anneciğim, yelkenlimiz limandan uzaklaşıyor!" dedi Şakir.»
   - Açıklama: Sahnede liman yok ve 'liman' kelimesi 3 yaşındaki çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0032` birebir aynı, `@degisim: bilgili -> büyük` (tutuyorsan), ardından `@onarim: 37db6a78abfb5e21ca30c227cd315facea635aba`, sonra gövde.

### Hikâye 11: tohum sakir-0033 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0033
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pota', fiil 'üflemek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: üflerken topun havası geri kaçıyordu | kardeşinden topun ağzını tutmasını istedi
@tohum: sakir-0033
@degisim: pota -> top
Kumsalda Şakir ile Canan ahşap oyuncak kutusunu açtı. İçinden havası inmiş mavi bir deniz topu çıktı. Şakir topa üfledi, ama nefes alırken hava hep geri kaçtı. Şakir topla bir macera oyunu oynamak istiyordu, bu yüzden vazgeçmedi. "Canan, ben nefes alırken topun ağzını tutar mısın?" diye sordu Şakir. "Tabii, tutarım," dedi Canan. Şakir yine üfledi. Şakir nefes alırken Canan topun ağzını parmağıyla kapattı. Böylece hava hiç kaçmadı. Top yavaş yavaş büyüdü ve yuvarlak oldu. Sonunda Şakir topun ağzını sıkıca kapattı. "Teşekkürler, Canan, şimdi birlikte oynayabiliriz!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynamak"
   - Cümle 4: «Şakir topla bir macera oyunu oynamak istiyordu, bu yüzden vazgeçmedi.»
   - Açıklama: 'Macera' soyut bir kelimedir, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "topla bir macera oyunu"
   - Cümle 4: «Şakir topla bir macera oyunu oynamak istiyordu, bu yüzden vazgeçmedi.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir topla bir macera oyunu oynamak istiyordu"
   - Cümle 4: «Şakir topla bir macera oyunu oynamak istiyordu, bu yüzden vazgeçmedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, çözümde işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0033` birebir aynı, `@degisim: pota -> top` (tutuyorsan), ardından `@onarim: 64830afc02a265a230ed480c1282f18ebef7eb77`, sonra gövde.

### Hikâye 12: tohum sakir-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Canan
@tohum: sakir-0034
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tartı', fiil 'ısınmak', sıfat 'şekerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | ev | Canan
@plan: böcekler soğuk tartıya ters düştü ve dönemedi | yaprak uzatıp böcekleri güneşe taşıdı
@tohum: sakir-0034
@degisim: şekerli -> yeşil
Şakir mutfakta kardeşi Canan ile macera oyunu oynuyordu. İkisi her köşeye dikkatle bakıyordu. Birden Şakir tartının üstünde ters dönmüş minik uğur böcekleri gördü. Böcekler pencerenin önündeki çiçekten uçup gelmiş ve soğuk tartıya düşmüştü. "Canan, onlara nasıl yardım ederiz?" diye sordu Şakir. "Onlara bir yaprak uzat, yaprağı tutarlar," dedi Canan. Şakir o çiçekten yeşil bir yaprak kopardı. Yaprağı böceklerin ayaklarına yavaşça yaklaştırdı. Böcekler yaprağa tutundu ve döndü. Şakir yaprağı güneşli pencerenin önüne koydu. Uğur böcekleri güneşte ısındı ve kanatlarını açtı. Sonra uçup yine çiçeğe kondular. "Teşekkürler, Canan, böcekleri birlikte kurtardık!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Canan ile macera oyunu"
   - Cümle 1: «Şakir mutfakta kardeşi Canan ile macera oyunu oynuyordu.»
   - Açıklama: 'Macera' soyut bir kelimedir, 3 yaşındaki çocuk bilmeyebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "macera oyunu oynuyordu"
   - Cümle 1: «Şakir mutfakta kardeşi Canan ile macera oyunu oynuyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılmış, çözümde işe yarar biçimde kullanılmamış.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler yaprağa tutundu ve döndü"
   - Cümle 9: «Böcekler yaprağa tutundu ve döndü.»
   - Açıklama: Notlanan çoğul canlı uğur böcekleri arka planda kalmıyor, olayın merkezine katılıyor.
   - Açıklama: Çoğul canlı uğur böcekleri arka planda kalmıyor, olayın merkezinde yer alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0034` birebir aynı, `@degisim: şekerli -> yeşil` (tutuyorsan), ardından `@onarim: 1bf45973f09cabbe87e5e086cd9ef0d898e6d067`, sonra gövde.
