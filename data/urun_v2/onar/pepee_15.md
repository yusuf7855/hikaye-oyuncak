# Editör görevi (onarım): Pepee, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Pepee | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar15.txt --ad urun_v2`
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

## Kart: Pepee (kaynaklı, kapalı dünya)

- Ad: Pepee (okunuş: pepe; kesme eki okunuşa uyar)
- Kimlik: Pepee, mavi tulum ve mavi şapka giyen, dört yaşında meraklı bir oğlandır.
- Tür: oğlan
- Güvenli özellik kullanımı: Pepee yeni şeyleri bir büyüğün yanında dener; derin suya girmez, yüksek yere çıkmaz.
- Özellikler:
  - öğren: Yeni şeyler öğrenmeyi ve denemeyi sever. (örnek biçimler: öğrendi, öğrenmeyi)
  - kahvaltı: Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer. (örnek biçimler: kahvaltı, kahvaltıda)
  - dans: Oyun oynamayı ve dans etmeyi sever. (örnek biçimler: dans, dansı)
- Yerler:
  - orman: Ağaçlarla ve çiçeklerle dolu bir orman.
  - deniz: Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.
  - park: Salıncağı ve kaydırağı olan bir çocuk parkı.
  - ev: Pepee'nin ailesiyle yaşadığı ev.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Bebee: Pepee'nin küçük kız kardeşi; annesine hayrandır, Pepee ile oynamak için büyümek ister. Tür: kız; konuşur. Yüzey biçimleri: Bebee, kardeş, kardeşi
  - Şila: Pepee'nin kuzeni ve en yakın arkadaşı; çok güzel dans eder. Tür: kız; konuşur. Yüzey biçimleri: Şila, kuzen, kuzeni
  - Dedee: Pepee'nin dedesi; en az Pepee kadar hareketli bir oyun arkadaşı. Tür: dede; konuşur. Yüzey biçimleri: Dedee, dede, dedesi, dedeciğim
  - Nenee: Pepee'nin ninesi; komik ve eğlencelidir, yemek pişirmeyi sever. Tür: nine; konuşur. Yüzey biçimleri: Nenee, Ninee, nine, ninesi, nineciğim
  - Annee: Pepee'nin ve Bebee'nin annesi. Tür: anne; konuşur. Yüzey biçimleri: Annee, anne, annesi, anneciğim
- Dünya kuralları:
  - Bebee Pepee'nin küçük kız kardeşidir; Şila kuzenidir, kardeşi değildir.
  - Dizinin görünmeyen anlatıcısı hikayeye girmez; hikaye olayları kendisi anlatır.
- Yasak adlar: Şuşu, Şuşuu, Pisi, Zulu, Köpüş, Maymuş, Kaliş, Möcük, Zezee, Bibii, Kekee, Mimi, Mimii, Duduu, Tutuu, Ekee, Babaa, Zuku
- Yasak: Pepee'nin ve Bebee'nin konuşma zorluğu hikayeye konmaz; kimse konuşmasıyla alay etmez.
- Yasak: Dedee'nin uçan balonu hikayeye girmez (yükseklik).
- İzinli dünya kelimeleri: tulum, kahvaltı, pekmez, tahin, dans

## Onarılacak hikâyeler

### Hikâye 1: tohum pepee-0031 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0031
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'boru', fiil 'ıslanmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: kayanın altındaki kuru yer küçüktü ve annesi ıslanıyordu | kayaya iyice yaslandı ve annesiyle dans etti
@tohum: pepee-0031
@degisim: boru -> kaya
Yağmur yapraklara hafifçe vuruyordu. Pepee ile Annee ormanda büyük bir kayanın altına koştu. Ama kayanın altındaki kuru yer küçüktü ve Annee'nin omzu ıslanıyordu. Pepee annesine yer açmak istedi. Hemen kayaya iyice yaslandı. Sonra annesinin iki elini tuttu. İkisi birbirine yakın durup küçük adımlarla dans etti. Böylece Annee de kuru yere sığdı. Annee huzurlu bir yüzle gülümsedi. Yağmur bir süre daha yağdı, sonra durdu. Pepee çok mutluydu, çünkü kuru yerini annesiyle paylaşmıştı.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "küçük adımlarla dans etti"
   - Cümle 7: «İkisi birbirine yakın durup küçük adımlarla dans etti.»
   - Açıklama: Tohumdaki dans özelliği sorunu gerçekten çözmüyor; yer açan şey kayaya yaslanıp yakın durmak.
   - Açıklama: Tohumdaki dans özelliği sorunu gerçekten çözmüyor; yer açan şey kayaya yaslanmak, dans işe yarar biçimde kullanılmamış.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "küçük adımlarla dans etti"
   - Cümle 7: «İkisi birbirine yakın durup küçük adımlarla dans etti.»
   - Açıklama: Dans etmek kuru yerin küçüklüğüne doğrudan yönelen bir çözüm değil ve Annee'nin sığmasını akla yatkın biçimde açıklamıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Böylece Annee de kuru yere sığdı"
   - Cümle 8: «Böylece Annee de kuru yere sığdı.»
   - Açıklama: Dans etmek kuru yeri büyütmez; çözüm dar yer sorununa doğrudan yönelmiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Annee huzurlu bir yüzle gülümsedi"
   - Cümle 9: «Annee huzurlu bir yüzle gülümsedi.»
   - Açıklama: 'Huzurlu' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "huzurlu bir yüzle"
   - Cümle 9: «Annee huzurlu bir yüzle gülümsedi.»
   - Açıklama: 'Huzurlu bir yüz' soyut bir ifade, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0031` birebir aynı, `@degisim: boru -> kaya` (tutuyorsan), ardından `@onarim: 193ce77c6eaf8c8cf310d16fdb9ea327effb3557`, sonra gövde.

### Hikâye 2: tohum pepee-0035 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0035
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'krem', fiil 'uzamak', sıfat 'sabunlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: baloncuk uçurmak istedi ama halka evde kalmıştı | otu yuvarlak bal kabına sardı ve halka yaptı
@tohum: pepee-0035
@degisim: krem -> halka
Bir sabah Pepee ile Bebee ormanda kahvaltı yapıyordu. "Bak, Pepee, boyum uzadı, çiçekli dala dokunabiliyorum!" dedi Bebee. Pepee bunu baloncukla kutlamak istedi. Çantada bir şişe sabunlu su vardı, ama halka evde kalmıştı. Pepee yerde ince ve uzun bir ot buldu. Otu kahvaltıdaki yuvarlak bal kabına sardı. Böylece küçük bir halka yaptı. Halkayı suya batırdı ve yavaşça üfledi. Ağaçların arasına bir sürü baloncuk uçtu. Bebee onların arkasından koştu ve ellerini çırptı. "Bunlar senin için, Bebee!" dedi Pepee. Sonra ikisi sırayla baloncuk uçurdu ve mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama halka evde kalmıştı"
   - Cümle 4: «Çantada bir şişe sabunlu su vardı, ama halka evde kalmıştı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0035` birebir aynı, `@degisim: krem -> halka` (tutuyorsan), ardından `@onarim: 50bb056e85e85fc8b8b80884e1155cfa446e5da2`, sonra gövde.

### Hikâye 3: tohum pepee-0036 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0036
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çekmece', fiil 'yapıştırmak', sıfat 'akıllı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: koşarken ninesinin kumdan pastasına bastı | özür diledi ve kabukları yeniden yapıştırdı
@tohum: pepee-0036
@degisim: çekmece -> kabuk
Pepee deniz kıyısında hızlı hızlı koşuyordu. Koşarken Nenee'nin kumdan yaptığı pastaya bastı. Pasta dağıldı ve üstündeki deniz kabukları kuma saçıldı. Nenee buna çok üzüldü. Pepee durdu ve hemen ninesinden özür diledi. Sonra pastayı Nenee ile birlikte yeniden yaptı. Beyaz kabukları ıslak kumla yapıştırdı ve kahvaltıdaki gibi bir yumurta yaptı. Nenee kumdan yumurtayı görünce kahkaha attı. Sonra Pepee'ye sarıldı ve onun akıllı bir çocuk olduğunu söyledi. Pepee çok sevindi, çünkü ninesi artık üzgün değildi ve pasta yine güzeldi.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kahvaltıdaki gibi bir yumurta yaptı"
   - Cümle 7: «Beyaz kabukları ıslak kumla yapıştırdı ve kahvaltıdaki gibi bir yumurta yaptı.»
   - Açıklama: Pastayı yeniden yaparken birden yumurta yapması kelimeyi yanlış anlamda kullanıyor ve kafa karıştırıyor.
   - Açıklama: Hikayede kahvaltı geçmediği için 'kahvaltıdaki gibi' ifadesinin anlamı belirsiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltıdaki gibi bir yumurta yaptı"
   - Cümle 7: «Beyaz kabukları ıslak kumla yapıştırdı ve kahvaltıdaki gibi bir yumurta yaptı.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunu çözmeye yaramıyor, yalnız süs olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kahvaltıdaki gibi bir yumurta yaptı"
   - Cümle 7: «Beyaz kabukları ıslak kumla yapıştırdı ve kahvaltıdaki gibi bir yumurta yaptı.»
   - Açıklama: Pastayı yeniden yaparken sebepsizce kumdan bir yumurta ortaya çıkıyor ve pasta onarımıyla bağı kurulmuyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kahvaltıdaki gibi bir yumurta yaptı"
   - Cümle 7: «Beyaz kabukları ıslak kumla yapıştırdı ve kahvaltıdaki gibi bir yumurta yaptı.»
   - Açıklama: Pepee pastayı yeniden yapıyor ama kabuklarla yumurta yapıyor, sonra yine pastanın güzel olduğu söyleniyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "pasta yine güzeldi"
   - Cümle 10: «Pepee çok sevindi, çünkü ninesi artık üzgün değildi ve pasta yine güzeldi.»
   - Açıklama: Kabuklarla yumurta yapıldığı anlatılırken sonda pastanın yeniden güzel olduğu söyleniyor, iki anlatım çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0036` birebir aynı, `@degisim: çekmece -> kabuk` (tutuyorsan), ardından `@onarim: c1a8d7e91d302c79d6d8dad2d522f72b481d6bd7`, sonra gövde.

### Hikâye 4: tohum pepee-0040 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0040
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kolye', fiil 'dinlemek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yumurta yuvarlak olduğu için kaşıktan düştü | peçeteyi katlayıp kaşığın içine koydu
@tohum: pepee-0040
@degisim: kolye -> peçete
Bir sabah Pepee ormanda kuşları dinleyerek kahvaltı yapıyordu. Sonra sıcacık yumurtasını kaşığa koydu ve ağaca kadar taşıma oyunu oynadı. Ama yumurta yuvarlaktı ve ilk adımda yumuşak otların üstüne düştü. Pepee bir kez daha denedi, ama yumurta yine düştü. Pepee kaşığa baktı ve düşündü. Sonra peçetesini katladı ve kaşığın içine koydu. Yumurtayı peçetenin üstüne yerleştirdi. Yumurta peçetenin üstünde güzelce durdu. Pepee yavaş adımlarla büyük ağaca kadar yürüdü. Yumurta bir kez bile düşmedi. Pepee sevinçle zıpladı ve oyunu mutlu mutlu bir kez daha oynadı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kuşları dinleyerek kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Pepee ormanda kuşları dinleyerek kahvaltı yapıyordu.»
   - Açıklama: Kartın kahvaltı özelliği yalnız sahne olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0040` birebir aynı, `@degisim: kolye -> peçete` (tutuyorsan), ardından `@onarim: aed7aa16cb74d86bbba4e62e584a0a5ab8e2c81a`, sonra gövde.

### Hikâye 5: tohum pepee-0042 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0042
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: bir şey yapmak
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'teneke', fiil 'yıkanmak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kuru kum kovadan çıkınca hemen dağıldı | kumu kazdı ve ıslak kumu kovaya bastırdı
@tohum: pepee-0042
@degisim: yıkanmak -> ıslatmak
Deniz kıyısında kumlar sıcak ve kuruydu. Pepee küçük teneke kovasıyla bir kum kulesi yapmak istiyordu. Ama kovayı kaldırınca kuru kum hemen dağıldı. Pepee bir kez daha denedi, ama kule yine olmadı. Sonra kumu biraz kazdı ve altında ıslak kum buldu. Deniz suyu bu kumu altından ıslatmıştı. Kovayı ıslak kumla doldurdu ve elleriyle bastırdı. Kovayı yavaşça ters çevirip kaldırdı. Kumda dimdik bir kule duruyordu! Pepee ıslak kumun daha iyi olduğunu öğrendi. Hemen yanına üç tane daha yaptı. Pepee yorgundu ama çok mutluydu, çünkü artık dört kulesi vardı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee bir kez daha denedi"
   - Cümle 4: «Pepee bir kez daha denedi, ama kule yine olmadı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada deniz kıyısında büyük olmadan yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0042` birebir aynı, `@degisim: yıkanmak -> ıslatmak` (tutuyorsan), ardından `@onarim: a8d26996bf19cbf46fba80f4b0e37d6dfd5ab8f2`, sonra gövde.

### Hikâye 6: tohum pepee-0043 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0043
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'ayçiçeği', fiil 'aramak', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: ayçiçeğinin toprağı çok kuruydu ve çiçek eğilmişti | çeşmeyi arayıp kovasıyla çiçeğe su taşıdı
@tohum: pepee-0043
@degisim: sulu -> kuru
Bir sabah Pepee parkta bahçe oyunu oynuyordu. Elinde küçük, kırmızı bir kova vardı. Kaydırağın yanındaki ayçiçeği yere doğru eğilmişti, çünkü toprağı çok kuruydu. Pepee çiçeğe hemen su vermek istedi. Çeşmeyi aradı ve onu hemen yakında buldu. Kovasını doldurdu ve çiçeğe geri yürüdü. Suyu dikkatle toprağa döktü. Sonra çiçeğin yanına oturdu ve bekledi. Biraz sonra ayçiçeği yavaş yavaş doğruldu. Pepee böylece kuru toprağa su vermek gerektiğini öğrendi. Pepee çok sevindi, çünkü ayçiçeği artık dik duruyordu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Çeşmeyi aradı ve onu hemen yakında buldu"
   - Cümle 5: «Çeşmeyi aradı ve onu hemen yakında buldu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada parkta yalnız dolaşıp deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0043` birebir aynı, `@degisim: sulu -> kuru` (tutuyorsan), ardından `@onarim: acd25974afc1a57b52624e76f516ae45eea109f1`, sonra gövde.

### Hikâye 7: tohum pepee-0044 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0044
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çikolata', fiil 'kaldırmak', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: yağmur başladı ve kulenin tepesi dağıldı | kovasını kulenin üstüne kapatıp yağmurun dinmesini bekledi
@tohum: pepee-0044
@degisim: çikolata -> kova
Pepee deniz kıyısında, sudan uzakta kovasıyla ıslak kumdan bir kule yapıyordu. Elleri kumdan yapışkan olmuştu. Birden yağmur başladı. Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı. Pepee kulesini yağmurdan korumak istedi. Kovayı kaldırdı ve kulenin üstüne ters kapattı. Artık damlalar kovanın üstüne düşüyordu. Pepee kovanın yanına çömeldi ve bekledi. Yağmur kısa sürdü ve biraz sonra dindi. Pepee kovayı yavaşça çekti. Kule yerinde sağlam duruyordu ve daha fazla dağılmamıştı. Pepee çok sevindi, çünkü kovayla kulesini korumayı öğrenmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elleri kumdan yapışkan olmuştu"
   - Cümle 2: «Elleri kumdan yapışkan olmuştu.»
   - Açıklama: Kum elleri yapışkan yapmaz; 'yapışkan' kelimesi burada doğru anlamda değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elleri kumdan yapışkan olmuştu"
   - Cümle 2: «Elleri kumdan yapışkan olmuştu.»
   - Açıklama: Yapışkan eller ayrıntısı kuruluyor ama olayda hiç kullanılmıyor.
   - Açıklama: Yapışkan eller ayrıntısı kurulup hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0044` birebir aynı, `@degisim: çikolata -> kova` (tutuyorsan), ardından `@onarim: ad378e49980011e711ca550c7a1addd61f7f8d45`, sonra gövde.

### Hikâye 8: tohum pepee-0045 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Bebee
@tohum: pepee-0045
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kamera', fiil 'asmak', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Bebee
@plan: kağıt zincir öbür sandalyeye yetmedi | üç halka daha yapıp zinciri uzattı
@tohum: pepee-0045
@degisim: kamera -> kağıt
Yağmur cama tık tık vuruyordu. Pepee odasında kardeşi Bebee için kağıttan renkli bir zincir yapmıştı. Zinciri iki sandalyenin arasına asmak istedi ama zincir öbür sandalyeye yetmedi. Pepee masadaki kağıtlara baktı. Zinciri uzatmayı öğrenmek istedi. Hemen üç halka daha yaptı ve zincire ekledi. Şimdi zincir iki sandalyeye de yetti. Pepee zinciri astı ve Bebee'yi çağırdı. Bebee odaya geldi ve zincirin altında oynak bir dans yaptı. "Bu zincir benim için mi?" diye sordu Bebee. "Evet, Bebee, senin için yaptım," dedi Pepee. "Çok güzel olmuş, teşekkür ederim, Pepee!" dedi Bebee.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Zinciri uzatmayı öğrenmek istedi"
   - Cümle 5: «Zinciri uzatmayı öğrenmek istedi.»
   - Açıklama: 'Öğrenmek' yanlış anlamda; Pepee zinciri uzatmak istiyor, öğrenmek değil.
   - Açıklama: Pepee zinciri uzatmak istiyor, öğrenmek değil; 'öğrenmek' yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Zinciri uzatmayı öğrenmek istedi"
   - Cümle 5: «Zinciri uzatmayı öğrenmek istedi.»
   - Açıklama: Tohumdaki öğrenme özelliği yalnız adı anılarak ekleniyor, çözümde bir şey öğrenilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0045` birebir aynı, `@degisim: kamera -> kağıt` (tutuyorsan), ardından `@onarim: 876b95fcbbfb312a0fcc43fc1b31d40c26cc17ef`, sonra gövde.

### Hikâye 9: tohum pepee-0046 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0046
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: sırayla oynamak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bilet', fiil 'sığınmak', sıfat 'pahalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: tek düdük vardı ve ikisi de onu çalmak istedi | düdüğü sırayla çalmayı önerdi
@tohum: pepee-0046
@degisim: sığınmak -> beklemek
Mutfakta Pepee ile Annee tren oyunu oynuyordu. Sandalyeler trenin vagonları olmuştu. Ama tek bir düdük vardı ve ikisi de onu çalmak istiyordu. Pepee masadaki yumurtaya baktı ve biraz düşündü. "Anneciğim, önce sen çal, ben kahvaltı yapayım," dedi Pepee. "Olur," dedi Annee ve düdüğü çaldı. Pepee vagona oturdu ve annesine kağıttan bir bilet uzattı. "Bu bilet pahalı, bir öpücük tutar!" dedi Annee. Pepee annesini öptü ve yumurtasını yiyerek bekledi. Sonra düdük Pepee'ye geçti ve bu kez o çaldı. Pepee çok mutluydu, çünkü sırayla oynadıkları için ikisi de düdüğü çalmıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesine kağıttan bir bilet uzattı"
   - Cümle 7: «Pepee vagona oturdu ve annesine kağıttan bir bilet uzattı.»
   - Açıklama: Bilet ve öpücük sahnesi sebepsiz beliriyor ve düdük sorununun çözümüne hiçbir katkı yapmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir öpücük tutar"
   - Cümle 8: «"Bu bilet pahalı, bir öpücük tutar!" dedi Annee.»
   - Açıklama: 'Pahalı' ve 'bir öpücük tutar' fiyat kavramı içeren soyut bir anlatım; 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu bilet pahalı, bir öpücük tutar!"
   - Cümle 8: «"Bu bilet pahalı, bir öpücük tutar!" dedi Annee.»
   - Açıklama: 'Pahalı' ve 'tutar' fiyat kavramı soyut ve mecazlı, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0046` birebir aynı, `@degisim: sığınmak -> beklemek` (tutuyorsan), ardından `@onarim: 2b17ef4932e59b09b439e226e47d3e18e984a5ff`, sonra gövde.

### Hikâye 10: tohum pepee-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Nenee
@tohum: pepee-0048
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'gevrek', fiil 'süslenmek', sıfat 'hafif'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Nenee
@plan: kağıt taç çok hafifti ve rüzgarda hep düşüyordu | tacı mavi şapkasının üstüne sıkıca geçirdi
@tohum: pepee-0048
@degisim: gevrek -> taç
Parkta Pepee ile Nenee saray oyunu oynuyordu. Pepee mavi şapkasını çıkarmış ve kağıttan bir taç takıp süslenmişti. Ama taç çok hafifti ve rüzgar esince hep yere düşüyordu. Pepee ninesine bir gösteri yapmak istiyordu. Pepee tacı yerden aldı ve biraz düşündü. Sonra şapkasını yeniden taktı ve tacı şapkanın üstüne sıkıca geçirdi. Rüzgar yine esti ama taç bu kez düşmedi. "Nineciğim, şimdi beni izle!" dedi Pepee. Pepee salıncakların önünde güzelce dans etti. Nenee ellerini çırptı ve güldü. "Ne güzel bir gösteri, bravo!" dedi Nenee. "Teşekkürler, nineciğim, seninle oynamak çok güzel!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Pepee salıncakların önünde güzelce dans etti"
   - Cümle 9: «Pepee salıncakların önünde güzelce dans etti.»
   - Açıklama: Kaybolduğu söylenen salıncak sonra yerinde duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0048` birebir aynı, `@degisim: gevrek -> taç` (tutuyorsan), ardından `@onarim: 3efc26d73c6f3fb2af8b7e7a7762b38ef5194659`, sonra gövde.

### Hikâye 11: tohum pepee-0053 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0053
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'duvar', fiil 'takılmak', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: rüzgar esti ve kurdele yüksek bir dala takıldı | ninesinden yardım istedi ve kurdelesini geri aldı
@tohum: pepee-0053
@degisim: duvar -> dal
Ormanda Pepee ile Nenee çiçeklerin arasında oynuyordu. Pepee ninesine mavi bir kurdeleyle yeni bir dans göstermek istiyordu. Birden rüzgar esti ve kurdele bir dala takıldı. Dal, Pepee'nin başının çok üstündeydi. Pepee zıpladı ama kurdeleye yetişemedi. "Nineciğim, kurdeleyi alır mısın?" diye sordu Pepee. Nenee güldü ve parmaklarının ucunda yükseldi. Kurdeleyi daldan yavaş yavaş çekti. Kurdele Pepee'nin eline düştü. "Teşekkürler, nineciğim!" dedi Pepee. "Bu kez kurdeleyi sıkıca tut," dedi Nenee. Pepee kurdeleyi iki eliyle tuttu ve ninesine dansını gösterdi. Nenee ellerini çırptı ve ikisi mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "parmaklarının ucunda yükseldi"
   - Cümle 7: «Nenee güldü ve parmaklarının ucunda yükseldi.»
   - Açıklama: Kalıp yanlış kurulmuş; 'ayak parmaklarının ucuna kalktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0053` birebir aynı, `@degisim: duvar -> dal` (tutuyorsan), ardından `@onarim: 583c577d6e294ec650f1aff6f87c8f192fa4cd5a`, sonra gövde.

### Hikâye 12: tohum pepee-0054 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0054
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'tuz', fiil 'döndürmek', sıfat 'konuşkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: dede de oynamak istedi ama tek çember vardı | çemberi dedesiyle paylaştı ve dansla döndürmeyi gösterdi
@tohum: pepee-0054
@degisim: tuz -> çember
Bir sabah Pepee ile dedesi kumda oynuyordu. Pepee'nin elinde kırmızı bir çember vardı. Dedee de çemberle oynamak istedi ama başka çember yoktu. "Pepee, ben de çemberini çevirebilir miyim?" diye sordu Dedee. "Tabii, dedeciğim, önce sana göstereyim," dedi Pepee. Pepee çemberi beline geçirdi ve dans ederek döndürdü. Sonra onu dedesine verdi. Dedee de belini salladı ve çemberi döndürdü. Çember hiç düşmeden dönüyordu. İkisi sırayla oynadı ve çok güldü. Dedee çok sevindi ve konuşkan oldu. "Pepee, çemberini benimle paylaştığın için teşekkür ederim!" dedi Dedee.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dedee çok sevindi ve konuşkan oldu"
   - Cümle 11: «Dedee çok sevindi ve konuşkan oldu.»
   - Açıklama: 'Konuşkan oldu' bu bağlamda yanlış ve anlamsız bir kullanım.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çok sevindi ve konuşkan oldu"
   - Cümle 11: «Dedee çok sevindi ve konuşkan oldu.»
   - Açıklama: 'Konuşkan' kalıcı bir özelliktir, bir anda olunan bir durum gibi yanlış kullanılmış.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Dedee çok sevindi ve konuşkan oldu"
   - Cümle 11: «Dedee çok sevindi ve konuşkan oldu.»
   - Açıklama: Kartta Dedee'nin ilişki alanı onu hareketli bir oyun arkadaşı olarak tanıtıyor; sonradan konuşkan olması dizideki kimliğiyle ilgili yanlış bilgi veriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dedee çok sevindi ve konuşkan oldu"
   - Cümle 11: «Dedee çok sevindi ve konuşkan oldu.»
   - Açıklama: Dedenin konuşkan olması olaydan çıkmıyor ve hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Konuşkan olma ayrıntısı olaydan çıkmıyor ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0054` birebir aynı, `@degisim: tuz -> çember` (tutuyorsan), ardından `@onarim: 9c2c0207838cbdf80504a670ce0c45b3ca1adbe0`, sonra gövde.
