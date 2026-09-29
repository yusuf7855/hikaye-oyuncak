# Editör görevi (onarım): Şakir, onarım partisi 24

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar24.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0032 (deneme 5 -> 6)

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
@plan: oyunda geminin yelkeni yoktu | annesinden havlu istedi ve havluyu sopaya bağladı
@tohum: sakir-0032
@degisim: bilgili -> büyük
Şakir, kamp yerinde yere düşmüş kalın bir ağaca oturdu. Oyunda bu ağaç bir gemi oldu ve annesi Kadriye de arkasına oturdu. Ama geminin yelkeni yoktu ve yola çıkamıyordu. Şakir macerayı çok severdi, bu yüzden oyunu bırakmadı ve bir yelken aradı. "Anneciğim, büyük mavi havluyu alabilir miyim?" diye sordu Şakir. "Tabii, al," dedi Kadriye ve havluyu ona verdi. Şakir havluyu yerdeki uzun bir sopaya sıkıca bağladı. Sonra sopayı iki eliyle havaya kaldırdı. Rüzgar esti ve havlu bir yelken gibi şişti. "Bak, anneciğim, yelkenlimiz uzaklaşıyor!" dedi Şakir. Kadriye güldü ve ellerini çırptı. Şakir çok mutlu oldu, çünkü gemisi sonunda yola çıkmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yelkenlimiz uzaklaşıyor"
   - Cümle 10: «"Bak, anneciğim, yelkenlimiz uzaklaşıyor!" dedi Şakir.»
   - Açıklama: Konuşanlar geminin üstünde oturduğu için gemi onlardan uzaklaşamaz; 'uzaklaşıyor' yanlış anlamda.
   - Açıklama: Üstünde oturdukları gemi onlardan uzaklaşamaz; 'gidiyor' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0032` birebir aynı, `@degisim: bilgili -> büyük` (tutuyorsan), ardından `@onarim: 808a9eaae4fe8e3e0c710e6fd10e687d85a0b979`, sonra gövde.

### Hikâye 2: tohum sakir-0046 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0046
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'zincir', fiil 'seslenmek', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: ikisi de önce zinciri saklamak istedi | sırayla oynamayı söyleyip ilk sırayı annesine verdi
@tohum: sakir-0046
@degisim: temkinli -> yavaş
Ormanda, kamp yerinde Şakir ile annesi Kadriye bir oyun oynayacaktı. Ama ikisi de parlak zinciri önce saklamak istedi, çünkü çok eğlenceliydi. Şakir bu macera oyununu çok severdi. "Anneciğim, sırayla oynayalım, önce sen sakla," dedi Şakir. Kadriye gülümsedi ve zinciri büyük bir taşın altına koydu. "Bul bakalım, Şakir!" diye seslendi Kadriye. Şakir yavaş adımlarla yürüdü ve taşları tek tek kaldırdı. Zincir üçüncü taşın altındaydı. "Buldum!" dedi Şakir sevinçle. Sonra sıra Şakir'e geldi. Şakir zinciri çalıların arasına sakladı. Kadriye etrafa baktı ve zinciri buldu. Şakir ile annesi oyunlarına sırayla, mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir bu macera oyununu"
   - Cümle 3: «Şakir bu macera oyununu çok severdi.»
   - Açıklama: 'Macera' soyut bir kavram ve küçük çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir bu macera oyununu çok severdi"
   - Cümle 3: «Şakir bu macera oyununu çok severdi.»
   - Açıklama: Tohum özelliği macera yalnız söylenmiş, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0046` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: eb1fb55cddbf9958f9e8eab4ea0e23f86c682789`, sonra gövde.

### Hikâye 3: tohum sakir-0054 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0054
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'gölge', fiil 'somurtmak', sıfat 'kırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: ipi sıkı tutunca uçurtma hep yere düştü | yeniden koştu ve ipi yavaş yavaş bıraktı
@tohum: sakir-0054
Şakir kumsalda ilk kez kırmızı bir uçurtma uçurmayı denedi. Ama uçurtma hep yere düştü, çünkü Şakir ipi hiç bırakmıyordu. Sonra şemsiyenin gölgesine oturdu ve biraz somurttu. Şakir bu macera oyununu bırakmak istemedi. Uçurtmaya ve ipe uzun uzun baktı. Denizden hafif bir rüzgar esiyordu. Şakir kalktı ve kumda yeniden koştu. Bu kez ipi yavaş yavaş bıraktı. Kırmızı uçurtma rüzgarla yükseldi ve havada kaldı. Şakir sevinçle zıpladı ve ipi biraz daha bıraktı. Sonra kumsalda uçurtmasını mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir bu macera oyununu"
   - Cümle 4: «Şakir bu macera oyununu bırakmak istemedi.»
   - Açıklama: Kumsalda uçurtma uçurmak bir macera oyunu değil; kelime yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu macera oyununu bırakmak"
   - Cümle 4: «Şakir bu macera oyununu bırakmak istemedi.»
   - Açıklama: Uçurtma uçurmaya 'macera oyunu' demek soyut ve yersiz bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0054` birebir aynı, ardından `@onarim: a454a44f1ea7519eeaafc2b81aca1d575a357fb2`, sonra gövde.

### Hikâye 4: tohum sakir-0056 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0056
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'taç', fiil 'düşürmek', sıfat 'ufak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: koşarken babasına çarptı ve tacı yere düşürdü | özür diledi ve yaprakları toplayıp tacı düzeltti
@tohum: sakir-0056
Şakir ormandaki kamp yerinde ağaçların arasında koşuyordu. Babası Remzi bir taşın üstünde oturmuş, yapraklardan ufak bir taç yapıyordu. Şakir koşarken babasının koluna çarptı ve tacı yere düşürdü. Tacın yaprakları otların arasına dağıldı. Şakir hemen durdu ve dağılan yapraklara baktı. "Özür dilerim, baba, seni görmedim," dedi Şakir. "Tamam, Şakir, birlikte düzeltelim," dedi Remzi ve gülümsedi. Şakir macerayı çok severdi ve yaprakları taşın arkasında bile aradı. Hepsini tek tek buldu. Sonra babasıyla birlikte onları taca taktı. Remzi tacı Şakir'in başına koydu ve ikisi de güldü. Şakir çok sevindi, çünkü özür dilemiş ve tacı babasıyla yeniden yapmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 8: «Şakir macerayı çok severdi ve yaprakları taşın arkasında bile aradı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Macera' soyut bir kavramdır ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0056` birebir aynı, ardından `@onarim: f328660af6096fb6a15abb797074600dbf7d17ff`, sonra gövde.

### Hikâye 5: tohum sakir-0057 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0057
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pirinç', fiil 'giydirmek', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: koşarken ayağı elbiseye takıldı ve elbise rüzgarla uçtu | özür diledi ve çalılarda elbiseyi bulup getirdi
@tohum: sakir-0057
@degisim: pirinç -> elbise
Rüzgar esiyordu ve Şakir kamp yerinde koşuyordu. Kardeşi Canan örtüde oyuncak bebeğine bir elbise hazırlıyordu. Koşarken Şakir'in ayağı elbiseye takıldı ve elbise rüzgarla uçup kayboldu. Canan çok üzüldü, çünkü oyuncak bebeğinin başka elbisesi yoktu. Şakir hemen durdu ve kardeşinden özür diledi. Macerayı çok seven Şakir yakındaki karmakarışık çalılara eğilip baktı. Küçük elbise bir dala takılmıştı. Şakir elbiseyi dikkatle aldı ve Canan'a götürdü. İkisi oyuncak bebeğe elbiseyi birlikte giydirdi. Canan gülümsedi ve Şakir'e sarıldı. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C6** (K merceği) — Kalıp yargı yok.
   - Alıntı: "oyuncak bebeğine bir elbise hazırlıyordu"
   - Cümle 2: «Kardeşi Canan örtüde oyuncak bebeğine bir elbise hazırlıyordu.»
   - Açıklama: Kız karakter bebeğe elbise hazırlarken erkek koşuyor; cinsiyet kalıp yargısı sezdiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 6: «Macerayı çok seven Şakir yakındaki karmakarışık çalılara eğilip baktı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0057` birebir aynı, `@degisim: pirinç -> elbise` (tutuyorsan), ardından `@onarim: 308d646fa5348a5af84bdebae3d550528fff403a`, sonra gövde.

### Hikâye 6: tohum sakir-0059 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0059
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'giysi', fiil 'soğumak', sıfat 'sabırlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: rüzgarla birlikte ıslık gibi bir ses geldi | şapkasıyla kabuğun ağzını kapatıp sesin yerini buldu
@tohum: sakir-0059
Deniz kıyısında hava biraz soğumuştu. Şakir ile Canan kalın giysiler içinde kumda oturuyordu. Birden rüzgarla birlikte ıslık gibi ince bir ses geldi. "Bu ses nereden geliyor?" diye sordu Şakir. "Sabırlı olalım ve dikkatle dinleyelim," dedi Canan. İkisi sessizce bekledi. Rüzgar yine esti ve ses büyük bir kabuğun yanından geldi. Şakir şapkasını çıkardı ve kabuğun ağzını kapattı. Islık hemen kesildi. Şapkayı kaldırınca ıslık tekrar başladı. "Rüzgar kabuğun içine esince bu ses çıkıyor!" dedi Şakir. Sonra kabuğu kulağına tuttu ve güldü. İkisi de çok sevindi, çünkü sesin nereden geldiğini bulmuşlardı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarla birlikte ıslık gibi ince bir ses"
   - Cümle 3: «Birden rüzgarla birlikte ıslık gibi ince bir ses geldi.»
   - Açıklama: Duyulan bir ses çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak konusu.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ıslık gibi ince bir ses geldi"
   - Cümle 3: «Birden rüzgarla birlikte ıslık gibi ince bir ses geldi.»
   - Açıklama: Tuhaf bir ses kimseye zarar vermiyor; çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak konusu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0059` birebir aynı, ardından `@onarim: 7976417f585ce9d31366d92d3161f09013b76236`, sonra gövde.

### Hikâye 7: tohum sakir-0060 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0060
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'altın', fiil 'birleşmek', sıfat 'turuncu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: tek bir turuncu kova vardı ve ikisi de istedi | kovayı sırayla kullanmayı önerdi
@tohum: sakir-0060
Şakir kumsalda Necati ile macera oyunu oynuyordu. Oyuncak altın için kumdan büyük bir kale yapacaklardı. Ama tek bir turuncu kova vardı ve ikisi de onu istedi. "Necati, kovayı sırayla dolduralım mı?" diye sordu Şakir. "Olur, önce sen başla," dedi Necati. Şakir kovayı kumla doldurdu ve sol yanda bir kule yaptı. Sonra Necati kovayı aldı ve sağ yana ikinci bir kule dikti. Kuleler büyüdükçe duvarları ortada birleşti. Şakir oyuncak altını kalenin ortasına koydu. "Ne güzel bir kale oldu, Şakir!" dedi Necati. Şakir çok sevindi, çünkü birlikte kocaman bir kale yapmışlardı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Necati ile macera oyunu"
   - Cümle 1: «Şakir kumsalda Necati ile macera oyunu oynuyordu.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Necati ile macera oyunu"
   - Cümle 1: «Şakir kumsalda Necati ile macera oyunu oynuyordu.»
   - Açıklama: Kartın 'Macerayı çok sever' özelliği yalnız oyunun adı olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0060` birebir aynı, ardından `@onarim: 99275f2b0661f0c5eb6c0ccbacd49330b4eeaa58`, sonra gövde.

### Hikâye 8: tohum sakir-0061 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0061
- yer: park (Şehirdeki park.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'buz', fiil 'güneşlenmek', sıfat 'yağmurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar olmadığı için gemi suyun ortasında durdu | şapkasını salladı, rüzgar yaptı ve gemiyi kenara getirdi
@tohum: sakir-0061
@degisim: buz -> gemi
Şakir yağmurlu bir sabahın sonunda evinin önündeki parkta güneşleniyordu. Oyuncak gemisini büyük bir su birikintisine bıraktı. Ama gemi suyun ortasında durdu, çünkü hiç rüzgar yoktu. Şakir suya girmek istemedi, çünkü ayakkabıları kuru kalmalıydı. Biraz düşündü ve sarı yağmur şapkasını başından çıkardı. Şapkayı suyun üstünde hızlı hızlı salladı. Şapkadan hafif bir rüzgar çıktı ve su kıpırdadı. Gemi yavaş yavaş suyun öbür kenarına yüzdü. Şakir öbür kenara yürüdü ve gemiyi aldı. Sonra şapkasını yeniden başına taktı. Şakir çok mutluydu, çünkü gemisini suya girmeden kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "gemi suyun ortasında durdu"
   - Cümle 3: «Ama gemi suyun ortasında durdu, çünkü hiç rüzgar yoktu.»
   - Açıklama: Hiç rüzgar yokken kenara bırakılan geminin suyun ortasına nasıl gittiği çelişkili kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0061` birebir aynı, `@degisim: buz -> gemi` (tutuyorsan), ardından `@onarim: 4e6a1ba0d3e66d7fa4604babfaef5b784a0bf5c9`, sonra gövde.

### Hikâye 9: tohum sakir-0066 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0066
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kanepe', fiil 'konuşmak', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: gemi oyununda geminin bayrağı yoktu | şapkasını bir dalın ucuna takıp bayrak yaptı
@tohum: sakir-0066
Bir sabah Şakir ile annesi Kadriye kamp yerindeydi. Şakir yerdeki kalın bir kütüğü gemi yaptı ve gemi oyunu kurdu. Ama gemisinin bayrağı yoktu ve ağaçların arasında hiç bayrak bulamadı. Şakir biraz düşündü ve başındaki şapkaya dokundu. Sonra yerden uzun bir dal aldı. Şapkasını dalın ucuna taktı ve dalı kütüğün yanında toprağa dikti. Şapka rüzgarda bayrak gibi sallandı. Kadriye de gelip gemiye bindi. Kütük evdeki kanepe kadar uzundu ve ikisi de üstüne sığdı. Şakir sevinçle annesiyle konuştu: "Bayrağımız hazır, anne!" "Sen çok akıllısın, Şakir," dedi Kadriye. Şakir çok sevindi, çünkü gemisinin artık güzel bir bayrağı vardı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kütük evdeki kanepe kadar uzundu"
   - Cümle 9: «Kütük evdeki kanepe kadar uzundu ve ikisi de üstüne sığdı.»
   - Açıklama: Kanepe karşılaştırması olaydan çıkmıyor ve bayrak sorununa hiçbir katkısı yok.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir sevinçle annesiyle konuştu"
   - Cümle 10: «Şakir sevinçle annesiyle konuştu: "Bayrağımız hazır, anne!"»
   - Açıklama: 'Annesiyle konuştu' ardından replikte yine 'anne' deniyor ve iki cümle sonra 'çok sevindi' tekrar ediliyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0066` birebir aynı, ardından `@onarim: f395436fdd84a3aa427719d98a7d5b33bf061356`, sonra gövde.

### Hikâye 10: tohum sakir-0069 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0069
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'meşe', fiil 'sallamak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: parkta çok ağaç vardı ve kağıttaki ağacı bulamadı | yapraklara bakıp kağıttaki meşe ağacını buldu
@tohum: sakir-0069
Bir sabah Şakir parkta macera oyunu oynuyordu. Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı. Ama parkta çok ağaç vardı ve Şakir o ağacı hemen bulamadı. Şakir hemen aramaya başladı. Ağaçların yapraklarına tek tek baktı. Sonunda kağıttaki yapraklara benzeyen bir ağaç gördü. Alçak bir dalı hafifçe salladı ve birkaç yaprak eline düştü. Yapraklar kağıttaki resmin aynısıydı ve bu ağaç bir meşe ağacıydı. Şakir yaprakları kağıdın yanına koydu ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı"
   - Cümle 2: «Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı.»
   - Açıklama: İşaretli kağıt ağaçta bir şey bulunacakmış gibi kuruluyor ama ağaç bulununca hiçbir şey olmuyor ve okur ağacın neden arandığını merak ederek kalıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir hemen aramaya başladı"
   - Cümle 4: «Şakir hemen aramaya başladı.»
   - Açıklama: 'Hemen' bir önceki cümlede de geçiyor ve gereksiz tekrar ediliyor.
   - Açıklama: 'Hemen' bir önceki cümlede de geçiyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0069` birebir aynı, ardından `@onarim: 14346a271b6af4e13cc7e81171ace7030a4bd97d`, sonra gövde.

### Hikâye 11: tohum sakir-0071 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0071
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ceket', fiil 'bindirmek', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: kumdan pasta yapmak için kalıbı yoktu | şapkasını kalıp olarak kullandı
@tohum: sakir-0071
@degisim: bindirmek -> dökmek
Şakir parkta kum havuzunda yemek oyunu oynuyordu. Kum yağmurdan ıslaktı, bu yüzden ceketini çıkarıp kenara koydu. Şakir büyük bir pasta yapmak istedi ama kalıbı yoktu. Kum elinde dağılıyor ve hiç yuvarlak olmuyordu. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı ıslak kumla doldurdu ve sıkıca bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumda yuvarlak bir pasta duruyordu. Şakir onun üstüne sos gibi ince kum döktü. Böylece güzel, soslu bir kum pastası oldu. Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara bakardı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ıslaktı, bu yüzden ceketini çıkarıp kenara koydu"
   - Cümle 2: «Kum yağmurdan ıslaktı, bu yüzden ceketini çıkarıp kenara koydu.»
   - Açıklama: Cümlenin öznesi 'kum' olduğu için 'ceketini çıkarıp koydu' fiili yanlış özneye bağlanıyor; Şakir adı gerekli.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ıslaktı, bu yüzden ceketini"
   - Cümle 2: «Kum yağmurdan ıslaktı, bu yüzden ceketini çıkarıp kenara koydu.»
   - Açıklama: 'Bu yüzden' bağlacı yanlış kullanılmış; kumun ıslak olması ceketi çıkarmanın nedeni değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bu yüzden ceketini çıkarıp kenara koydu"
   - Cümle 2: «Kum yağmurdan ıslaktı, bu yüzden ceketini çıkarıp kenara koydu.»
   - Açıklama: Kumun ıslak olması ceketi çıkarmayı açıklamıyor ve ceket bir daha işe yaramıyor.
   - Açıklama: Kumun ıslak olması ceketi çıkarmanın sebebi değil ve ceket bir daha hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0071` birebir aynı, `@degisim: bindirmek -> dökmek` (tutuyorsan), ardından `@onarim: 28dbed5398a16aa097e1dbe67d23196ddba09595`, sonra gövde.

### Hikâye 12: tohum sakir-0072 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0072
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: kaybolan eşya
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bulmaca', fiil 'eğilmek', sıfat 'kremalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: kalem kütüğün yanında yaprakların arasında kayboldu | yere eğilip yaprakları kaldırdı ve kalemi buldu
@tohum: sakir-0072
Şakir babası Remzi ile kamp yerinde bir macera bulmacası yapıyordu. Bulmaca bitince Remzi ona kremalı bir kek verecekti. Ama Şakir'in kalemi elinden kaydı ve kütüğün yanında kayboldu. "Baba, kalemimi ben bulurum!" dedi Şakir. Şakir yere eğildi ve kütüğün yanına baktı. Orada bir sürü kuru yaprak vardı. Şakir yaprakları tek tek kaldırdı. Kalem bir yaprağın altında duruyordu. Şakir kalemi aldı ve bulmacanın son kelimesini yazdı. "Bulmaca bitti, baba!" dedi Şakir. Remzi gülerek ona keki verdi. Şakir çok sevindi, çünkü kalemini kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir macera bulmacası yapıyordu"
   - Cümle 1: «Şakir babası Remzi ile kamp yerinde bir macera bulmacası yapıyordu.»
   - Açıklama: Kartın 'Macerayı çok sever' özelliği yalnız bir etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki macera özelliği yalnız bulmacanın sıfatı olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0072` birebir aynı, ardından `@onarim: b24b90f5523f83b5f80a8e9093b3a7e330bad786`, sonra gövde.
