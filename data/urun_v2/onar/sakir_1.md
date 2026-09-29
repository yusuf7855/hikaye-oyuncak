# Editör görevi (onarım): Şakir, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 4 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0005 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: mutfaktan garip bir ses geldi | mutfağa gidip tencerede patlayan mısırı gördü
@tohum: sakir-0005
Şakir odasında oynarken garip bir ses duydu. Mutfaktan pıt pıt diye sesler geliyordu. Şakir bu sesi çok merak etti ve mutfağa koştu. Annesi Kadriye ocağın başındaydı. Ocakta devasa bir tencere vardı ve ses oradan geliyordu. "Anne, tencerede ne var?" diye sordu Şakir. Kadriye onu ocaktan uzak bir sandalyeye oturttu. "Birazdan göreceksin," dedi Kadriye. Ses bitince Kadriye tencerenin kapağını açtı. Tencere bembeyaz patlamış mısırla doluydu! Şakir şapkasını çıkarıp annesine uzattı. Kadriye kepçeyle şapkayı mısırla doldurdu. Şakir çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir bu sesi çok merak etti"
   - Cümle 3: «Şakir bu sesi çok merak etti ve mutfağa koştu.»
   - Açıklama: Garip ses gerçek bir sorun değil, yalnız bir merak; ortada çözülecek bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Ocakta devasa bir tencere"
   - Cümle 5: «Ocakta devasa bir tencere vardı ve ses oradan geliyordu.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmez; 'çok büyük' denmeli.
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kadriye tencerenin kapağını açtı"
   - Cümle 9: «Ses bitince Kadriye tencerenin kapağını açtı.»
   - Açıklama: Sesin kaynağını Şakir değil annesi ortaya çıkarıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir şapkasını çıkarıp annesine uzattı"
   - Cümle 11: «Şakir şapkasını çıkarıp annesine uzattı.»
   - Açıklama: Tohumdaki şapka özelliği sorunun (sesin kaynağını bulmanın) çözümünde işe yaramıyor, yalnız sonradan kap olarak ekleniyor.
   - Açıklama: Tohumdaki şapka özelliği sorunu (sesin kaynağını bulmak) çözmüyor, yalnız sona eklenmiş bir kap olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0005` birebir aynı, ardından `@onarim: e515ca0c2d973cd454533d8a4cd784296f6a6b06`, sonra gövde.

### Hikâye 2: tohum sakir-0006 (deneme 1 -> 2)

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
@plan: kum çok kuruydu ve kule hep yıkıldı | şapkasını ıslak kumla doldurup kaleye ters çevirdi
@tohum: sakir-0006
@degisim: sadık -> ıslak
Rüzgar esiyordu ve Şakir kumsalda Fil Necati ile kale yapıyordu. Necati küçük bir kum aletiyle kaleye kule yapıyordu. Ama kum çok kuruydu ve kule hep yıkılıyordu. "Bu kule hiç durmuyor," dedi Necati üzgün üzgün. Şakir su kenarındaki kumun ıslak olduğunu gördü. Şapkasını çıkardı ve o kumla doldurdu. Sonra şapkayı kalenin üstüne ters çevirdi. Sonra şapkayı yavaşça kaldırdı. Kum birbirine yapışmıştı ve kule şapkaya benziyordu. "Şapkalı kule harika oldu, Şakir!" dedi Necati. Şakir ile Necati bundan sonra kuleleri hep ıslak kumla yaptı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "doldurup kaleye ters çevirdi"
   - Cümle 0 (plan satırı): «kum çok kuruydu ve kule hep yıkıldı | şapkasını ıslak kumla doldurup kaleye ters çevirdi»
   - Açıklama: 'Kaleye ters çevirdi' bozuk; 'kalenin üstüne ters çevirdi' olmalı.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasını ıslak kumla doldurup kaleye ters çevirdi"
   - Cümle 0 (plan satırı): «kum çok kuruydu ve kule hep yıkıldı | şapkasını ıslak kumla doldurup kaleye ters çevirdi»
   - Açıklama: Gövdede şapka kaleye ters çevrilmiyor, yalnız doldurulup kaldırılıyor; plan çözümü gövdeden farklı söylüyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra şapkayı yavaşça kaldırdı"
   - Cümle 8: «Sonra şapkayı yavaşça kaldırdı.»
   - Açıklama: Art arda iki cümle 'Sonra şapkayı' ile başlıyor; gereksiz tekrar.
   - Açıklama: Art arda iki cümle 'Sonra şapkayı' diye başlıyor; gereksiz tekrar.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra kuleleri hep ıslak kumla yaptı"
   - Cümle 11: «Şakir ile Necati bundan sonra kuleleri hep ıslak kumla yaptı.»
   - Açıklama: Son cümle sahnenin dışına, belirsiz bir geleceğe atlıyor; tek zaman kuralı çiğneniyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra kuleleri hep ıslak kumla"
   - Cümle 11: «Şakir ile Necati bundan sonra kuleleri hep ıslak kumla yaptı.»
   - Açıklama: Son cümle tek sahneden çıkıp sonraki günlere uzanıyor; tek zaman kuralı zorlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0006` birebir aynı, `@degisim: sadık -> ıslak` (tutuyorsan), ardından `@onarim: fd110d24357ddc1e71c43e532c95cfe6c6e3fa1e`, sonra gövde.

### Hikâye 3: tohum sakir-0007 (deneme 1 -> 2)

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
@plan: silgi elinden kaydı ve kayboldu | aradı ve silgiyi minderlerin arasında buldu
@tohum: sakir-0007
Salonda Şakir koltukta oturmuş, resim yapıyordu. Silgisi birden elinden kaydı ve kayboldu. Şakir resmindeki fazla bir çizgiyi silmek istiyordu. Macerayı seven Şakir, silgiyi aramaya hemen başladı. Emekleyerek masanın altına baktı. Sonra halının kenarını kaldırdı. Silgi hiçbir yerde yoktu. Şakir yoruldu ve koltuğa geri oturdu. Birden altında küçük, sert bir şey hissetti. Silgi iki minderin arasına düşmüştü! Neyse ki silgi sağlamdı. Şakir fazla çizgiyi hemen sildi. Şakir çok sevindi, çünkü kayıp silgisini kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Macerayı seven Şakir"
   - Cümle 4: «Macerayı seven Şakir, silgiyi aramaya hemen başladı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuk için anlaşılır değil, silgi aramakla da uyuşmuyor.
   - Açıklama: 'Macera' soyut bir kavram ve silgi aramayla ilgisiz; 3 yaşındaki çocuk için uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı seven Şakir, silgiyi aramaya"
   - Cümle 4: «Macerayı seven Şakir, silgiyi aramaya hemen başladı.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Emekleyerek masanın altına baktı"
   - Cümle 5: «Emekleyerek masanın altına baktı.»
   - Açıklama: Arama ikiden fazla adım sürüyor ve silgi sonunda sebebe yönelen bir çözümle değil tesadüfen bulunuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Birden altında küçük, sert bir şey hissetti"
   - Cümle 9: «Birden altında küçük, sert bir şey hissetti.»
   - Açıklama: Silgi iki boşa arama adımından sonra tesadüfen bulunuyor; çözüm sebebe yönelmiyor ve 2 adımı aşıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Neyse ki silgi sağlamdı"
   - Cümle 11: «Neyse ki silgi sağlamdı.»
   - Açıklama: Silginin kırılabileceği hiç kurulmadığı için bu cümle işlevsiz bir ayrıntı.
   - Açıklama: Silginin sağlam olduğu bilgisi hiçbir kurulumla bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0007` birebir aynı, ardından `@onarim: b6c1dda65234e9cc07857e36ab4548fdca5df0ec`, sonra gövde.

### Hikâye 4: tohum sakir-0009 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar esti ve kağıt havaya kalktı | şapkasını kağıdın köşesine koydu
@tohum: sakir-0009
@degisim: jöle -> kağıt
Salonda Şakir resim oyunu oynuyordu. Büyük bir kağıda güneş yapmak istiyordu. Ama açık pencereden rüzgar esti ve kağıt havaya kalktı. Şakir kağıdı yere koydu ama rüzgar onu yine kaldırdı. Şakir biraz düşündü. Sonra şapkasını çıkarıp kağıdın köşesine koydu. Bu kez kağıt yerinden hiç kıpırdamadı. Şakir fırçasını sarı boyaya batırdı. Kağıda kocaman bir güneş yaptı. Resim bitince boyalı ellerini yıkadı ve havluyla kurulandı. Şakir bundan sonra rüzgarlı günlerde resmini pencereden uzakta yaptı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve kağıt havaya kalktı"
   - Cümle 3: «Ama açık pencereden rüzgar esti ve kağıt havaya kalktı.»
   - Açıklama: Kağıdın rüzgarla kalkması önemsiz, kolayca geçen bir olay.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "şapkasını çıkarıp kağıdın köşesine koydu"
   - Cümle 6: «Sonra şapkasını çıkarıp kağıdın köşesine koydu.»
   - Açıklama: Sebep açık pencere iken çözüm pencereye yönelmiyor; son cümledeki ders de kullanılan çözümle uyuşmuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve havluyla kurulandı"
   - Cümle 10: «Resim bitince boyalı ellerini yıkadı ve havluyla kurulandı.»
   - Açıklama: Yalnız eller yıkandığı için 'ellerini kuruladı' olmalı; 'kurulandı' bütün vücut için kullanılır.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "boyalı ellerini yıkadı ve havluyla kurulandı"
   - Cümle 10: «Resim bitince boyalı ellerini yıkadı ve havluyla kurulandı.»
   - Açıklama: El yıkama ayrıntısı olaydan çıkmıyor ve işlevsiz.
   - Açıklama: El yıkama ayrıntısı sorunla ya da çözümle ilgisiz, işlevsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0009` birebir aynı, `@degisim: jöle -> kağıt` (tutuyorsan), ardından `@onarim: 2f021d613b1968743359a8a755b1eed2d425f5bc`, sonra gövde.
