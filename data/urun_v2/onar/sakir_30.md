# Editör görevi (onarım): Şakir, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0069 (deneme 5 -> 6)

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
@plan: parkta çok ağaç vardı ve meşe ağacını bulamadı | yapraklara bakıp resimdeki meşe yaprağını buldu
@tohum: sakir-0069
@degisim: işaretli -> resimli
Bir sabah Şakir parkta macera oyunu oynuyordu. Elindeki resimli kağıtta bir meşe yaprağı çizilmişti. Ama parkta çok ağaç vardı ve Şakir meşe ağacını hemen bulamadı. Oyunda o ağaçtan bir yaprak bulup kağıdına koyacaktı. Şakir yakındaki ağaçların yapraklarına dikkatle baktı. Sonunda kağıttaki resme benzeyen yapraklar gördü. Alçak bir dalı hafifçe salladı ve birkaç yaprak eline düştü. Bu ağaç resimdeki meşe ağacıydı. Şakir en güzel yaprağı kağıdın üstüne koydu. Sonra macera oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu ağaç resimdeki meşe ağacıydı"
   - Cümle 8: «Bu ağaç resimdeki meşe ağacıydı.»
   - Açıklama: Resimde ağaç değil yaprak çizili; 'resimdeki meşe ağacı' yanlış anlam taşıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra macera oyununa mutlu"
   - Cümle 10: «Sonra macera oyununa mutlu mutlu devam etti.»
   - Açıklama: Tohumdaki macera özelliği iki kez adı geçiyor ve sorunu çözmede işe yaramıyor, kartın özellik kullanımına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0069` birebir aynı, `@degisim: işaretli -> resimli` (tutuyorsan), ardından `@onarim: b3f5dcb5077c612eb296b37c6add2b28a56a8fb2`, sonra gövde.

### Hikâye 2: tohum sakir-0070 (deneme 4 -> 5)

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
Denizden serin bir rüzgar esiyordu. Şakir, Necati ile kumsalda en güzel kabuğu bulma macerasındaydı. Birden şirin, pembe bir kabuk gördü ama kabuk ağır bir kütüğün altındaydı. Şakir kütüğü iki eliyle çekti ama kütük hiç kıpırdamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. Necati hortumuyla kütüğü kolayca kenara itti. Şakir kabuğu aldı ve ona parmağıyla yavaşça dokundu. Kabuğun içi çok parlaktı. "Çok güzel bir kabuk buldun, Şakir," dedi Necati. "Teşekkürler, Necati, bu kabuğu hep saklayacağım!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "en güzel kabuğu bulma macerasındaydı"
   - Cümle 2: «Şakir, Necati ile kumsalda en güzel kabuğu bulma macerasındaydı.»
   - Açıklama: 'Bulma macerasındaydı' soyut ve ağır bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram ve cümle yapısı çocuğa ağır.
   - Açıklama: 'Bulma macerasındaydı' soyut ve 3 yaşındaki çocuğa uygun olmayan bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0070` birebir aynı, `@degisim: ruj -> kütük` (tutuyorsan), ardından `@onarim: c256e07b0125ce78f2cd5419e4710b931761b0df`, sonra gövde.

### Hikâye 3: tohum sakir-0071 (deneme 5 -> 6)

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
Şakir parkta kum havuzunda yemek oyunu oynuyordu. Ceketini bir önlük gibi beline bağlamıştı. Şakir büyük bir pasta yapmak istedi ama kalıbı yoktu. Kum elinde dağılıyor ve hiç yuvarlak olmuyordu. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı yağmurdan ıslanan kumla doldurdu ve sıkıca bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumda yuvarlak bir pasta duruyordu. Şakir onun üstüne sos gibi ince kum döktü. Böylece güzel, soslu bir kum pastası oldu. Şakir, kalıp yokken şapkanın da kalıp olabileceğini öğrendi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ceketini bir önlük gibi beline bağlamıştı"
   - Cümle 2: «Ceketini bir önlük gibi beline bağlamıştı.»
   - Açıklama: Önlük gibi bağlanan ceket kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Önlük gibi bağlanan ceket bir daha hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şapkayı yağmurdan ıslanan kumla doldurdu"
   - Cümle 6: «Şapkayı yağmurdan ıslanan kumla doldurdu ve sıkıca bastırdı.»
   - Açıklama: Kum az önce elde dağılıyorken çözümü sağlayan yağmurdan ıslanmış kum sebepsizce beliriyor.
   - Açıklama: Yağmur hikayede hiç kurulmadan ıslak kum sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0071` birebir aynı, `@degisim: bindirmek -> dökmek` (tutuyorsan), ardından `@onarim: 1618e98d06b3260162a01251adca5f07a0ea3cbe`, sonra gövde.

### Hikâye 4: tohum sakir-0072 (deneme 5 -> 6)

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
Şakir babası Remzi ile kamp yerinde bir bulmaca yapıyordu. Bulmaca bitince Remzi ona kremalı bir kek verecekti. Ama Şakir'in kalemi elinden kaydı ve kütüğün yanında kayboldu. "Baba, bu benim macera oyunum, kalemi ben bulurum!" dedi Şakir. Şakir yere eğildi ve kütüğün yanına baktı. Orada bir sürü kuru yaprak vardı. Şakir yaprakları tek tek kaldırdı. Kalem bir yaprağın altında duruyordu. Şakir kalemi aldı ve bulmacanın son kelimesini yazdı. "Bulmaca bitti, baba!" dedi Şakir. Remzi gülerek ona keki verdi. Şakir çok sevindi, çünkü kalemini kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu benim macera oyunum"
   - Cümle 4: «"Baba, bu benim macera oyunum, kalemi ben bulurum!" dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kavram ve bulmaca için yerinde değil; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0072` birebir aynı, ardından `@onarim: 2a2bf9ed69dd34714afc5076412793cc1552638b`, sonra gövde.

### Hikâye 5: tohum sakir-0073 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0073
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'başörtüsü', fiil 'buluşmak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: çiçek eğilmişti çünkü toprağı çok kuruydu | çeşmeden su getirip çiçeği suladı
@tohum: sakir-0073
@degisim: başörtüsü -> çiçek
Güneşli bir sabah Şakir parkta yürüyordu. Birden bankın yanında küçük, sarı bir çiçek gördü. Çiçek yere doğru eğilmişti, çünkü toprağı çok kuruydu. Şakir çiçeğe su vermek istedi. Şakir su bulmayı bir macera oyunu yaptı. Çiçeğe yakın, iki yolun buluştuğu yerde bir çeşme buldu. Ellerine su doldurdu. Yavaşça yürüdü ve suyu çiçeğin dibine boşalttı. Sonra bir kez daha gidip su getirdi. Toprak ıslandı ve çiçek yavaş yavaş doğruldu. Sarı yaprakları güneşte parladı. Şakir, çiçeklerin de su içtiğini öğrendi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "su bulmayı bir macera oyunu yaptı"
   - Cümle 5: «Şakir su bulmayı bir macera oyunu yaptı.»
   - Açıklama: Yapı bozuk; 'su bulmayı bir macera oyununa çevirdi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "su bulmayı bir macera oyunu yaptı"
   - Cümle 5: «Şakir su bulmayı bir macera oyunu yaptı.»
   - Açıklama: 'Bir şeyi oyun yapmak' yanlış kullanım; 'oyuna çevirdi' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir su bulmayı bir macera oyunu yaptı"
   - Cümle 5: «Şakir su bulmayı bir macera oyunu yaptı.»
   - Açıklama: Macera oyunu kuruluyor ama hiç gelişmiyor; çeşme hemen yakında bulunuyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şakir, çiçeklerin de su içtiğini öğrendi"
   - Cümle 12: «Şakir, çiçeklerin de su içtiğini öğrendi.»
   - Açıklama: Şakir çiçeğe baştan su vermek istediği halde sonda bunu yeni öğrenmiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0073` birebir aynı, `@degisim: başörtüsü -> çiçek` (tutuyorsan), ardından `@onarim: 504114ac7fcfd63014bba9b7a18b70d700e5e5dc`, sonra gövde.

### Hikâye 6: tohum sakir-0075 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0075
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'cüzdan', fiil 'köpürmek', sıfat 'yeni'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil çok hızlı üfledi ve köpükler uçtu | ondan yavaşça üflemesini istedi ve kova köpükle doldu
@tohum: sakir-0075
@degisim: cüzdan -> kova
Ormanda kamp yerinde Şakir ile Fil Necati bir kova sabunlu suyla oynuyordu. Bu yeni macera oyununda kova köpükle dolacaktı. Ama Necati hortumuyla suya çok hızlı üfledi ve köpükler havaya uçtu. Köpükler Necati'nin başına kondu ve kovada hiç köpük kalmadı. "Necati, bu kez hafifçe üfle," dedi Şakir. Necati hortumunu suya soktu ve öyle yaptı. Su yavaş yavaş köpürdü. Beyaz köpük kovanın ağzına kadar çıktı. "Bak, Şakir, kova doldu!" dedi Necati. İkisi köpüklerle oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni macera oyununda"
   - Cümle 2: «Bu yeni macera oyununda kova köpükle dolacaktı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu yeni macera oyununda"
   - Cümle 2: «Bu yeni macera oyununda kova köpükle dolacaktı.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0075` birebir aynı, `@degisim: cüzdan -> kova` (tutuyorsan), ardından `@onarim: cac2dcda77ded3a6179779c2a205c808d67731e8`, sonra gövde.

### Hikâye 7: tohum sakir-0076 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0076
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tost', fiil 'koşuşturmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kumdan nereden geldiği belli olmayan ince bir ses duyuldu | kum tepesinin arkasına bakıp sesi yapan kabuğu buldu
@tohum: sakir-0076
@degisim: sevecen -> neşeli
Şakir babası Remzi ile kumsalda tost yiyordu. Birden kumdan ince bir ses geldi. Şakir bu sesin nereden geldiğini çok merak etti. Şakir macerayı çok severdi ve sesi bulmak istedi. Tostunu bitirdi ve kumda yavaş yavaş yürüdü. Ses yakındaki bir kum tepesinin arkasından geliyordu. Şakir oraya baktı ve kumda büyük bir kabuk gördü. Rüzgar kabuğun deliğine esince ince bir ses çıkıyordu. "Baba, gel, sesi bu kabuk yapıyor!" dedi Şakir. Remzi geldi ve kabuğu dinledi. "Ne güzel buldun, Şakir," dedi Remzi neşeli bir sesle. Sonra ikisi kumda koşuşturdu ve güldü. Şakir çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Tostunu bitirdi ve kumda yavaş yavaş yürüdü"
   - Cümle 5: «Tostunu bitirdi ve kumda yavaş yavaş yürüdü.»
   - Açıklama: Şakir bilinmeyen bir sesin peşinden babasından ayrılıp kum tepesinin arkasına tek başına gidiyor; güvenli kullanım satırındaki tek başına uzağa gitmez kuralına aykırı.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "sesin nereden geldiğini bulmuştu"
   - Cümle 13: «Şakir çok sevindi, çünkü sesin nereden geldiğini bulmuştu.»
   - Açıklama: 3. cümledeki 'sesin nereden geldiğini' ifadesi sonda gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0076` birebir aynı, `@degisim: sevecen -> neşeli` (tutuyorsan), ardından `@onarim: 974c2f1d70c1db61e21c0450bb979304c33c5991`, sonra gövde.

### Hikâye 8: tohum sakir-0078 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0078
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karton', fiil 'çağırmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: rüzgar karton evin çatısını uçurdu ve yırttı | şapkasını çıkarıp evin üstüne çatı yaptı
@tohum: sakir-0078
@degisim: cömert -> komik
Şakir kamp yerinde, çadırın hemen önünde oynuyordu. Oyuncak aslanı için karton bir kutudan komik bir ev yapmıştı. Ama rüzgar esti ve evin karton çatısını uçurdu. Çatı çalılara takıldı ve yırtıldı. Evin tepesi açık kaldı ve oyun durdu. Şakir biraz düşündü ve şapkasını çıkardı. Şapka genişti ve kutunun üstünü tam örttü. Böylece eve yeni ve güzel bir çatı oldu. Sonra Şakir oyunda aslanını yeni evine çağırdı. Oyuncak aslanı evin içine koydu ve güldü. Şakir çok sevindi, çünkü aslanının evinin yine bir çatısı vardı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "eve yeni ve güzel bir çatı oldu"
   - Cümle 8: «Böylece eve yeni ve güzel bir çatı oldu.»
   - Açıklama: Yapı bozuk; 'evin yeni ve güzel bir çatısı oldu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0078` birebir aynı, `@degisim: cömert -> komik` (tutuyorsan), ardından `@onarim: 4a0e59dd87c19913ca42cde8c7008f4e50231d0c`, sonra gövde.

### Hikâye 9: tohum sakir-0079 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0079
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yonca', fiil 'mırıldanmak', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: top yuvarlandı ve otların arasında kayboldu | zilin sesini dinleyip otlara bakınca topu buldu
@tohum: sakir-0079
@degisim: kibar -> yavaş
Bir sabah Şakir kamp yerinde bir şarkı mırıldanıyordu. Elindeki küçük zilli top birden yere düştü ve yuvarlandı. Şakir topunu çok seviyordu ama onu göremedi ve üzüldü. O sırada hemen yanındaki otların arasından ince bir zil sesi geldi. Şakir bu sesin topun zili olduğunu düşündü. Sonra macera oyunlarındaki gibi otlara sessizce eğildi. Rüzgar esti ve ses yine geldi. Şakir otları yavaşça iki yana açtı. Top orada, yeşil yonca yapraklarının arasında duruyordu. Rüzgar esince top sallanıyor ve zili çalıyordu. Şakir çok sevindi, çünkü topunu bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elindeki küçük zilli top birden yere düştü"
   - Cümle 2: «Elindeki küçük zilli top birden yere düştü ve yuvarlandı.»
   - Açıklama: Top hemen yandaki otlara düşüp kendi sesiyle hemen bulunuyor; sorun neredeyse yok ve çocuk için önemsiz kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu sesin topun zili olduğunu"
   - Cümle 5: «Şakir bu sesin topun zili olduğunu düşündü.»
   - Açıklama: Ses zil değildir; 'topun zilinin sesi' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunlarındaki gibi otlara"
   - Cümle 6: «Sonra macera oyunlarındaki gibi otlara sessizce eğildi.»
   - Açıklama: 'Macera oyunlarındaki gibi' soyut bir benzetme, küçük çocuğa uygun değil.
   - Açıklama: 'Macera oyunları' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0079` birebir aynı, `@degisim: kibar -> yavaş` (tutuyorsan), ardından `@onarim: 488979d95e804571a8c37f00e6d2fd6bce72b1bd`, sonra gövde.

### Hikâye 10: tohum sakir-0081 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0081
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kazak', fiil 'ilgilenmek', sıfat 'gizli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: rüzgar kuru kumu savurdu ve kule yıkıldı | kardeşinden yardım isteyip ıslak kumla kule yaptı
@tohum: sakir-0081
@degisim: ilgilenmek -> dinlemek
Rüzgar esiyordu. Şakir ile kardeşi Canan kazaklarını giymiş, kumsalda oturuyordu. Şakir kuru kumdan bir kule yaptı ama rüzgar onu yıktı. Canan yanında kitap okuyordu. "Canan, bana yardım eder misin?" diye sordu Şakir. Canan kitabını kapattı ve kardeşini dinledi. "Kumun altına bak, ıslak kum rüzgarda savrulmaz," dedi Canan. Şakir oturduğu yerde kumu kazdı ve altta gizli ıslak kumu buldu. Şapkasını bu ıslak kumla doldurdu. Sonra şapkayı kulenin yerine ters çevirdi ve kumu sıkıca bastırdı. Bu kez rüzgar kuleyi yıkamadı. "Teşekkürler, Canan, kulem artık çok sağlam!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kulenin yerine ters çevirdi"
   - Cümle 10: «Sonra şapkayı kulenin yerine ters çevirdi ve kumu sıkıca bastırdı.»
   - Açıklama: 'Kulenin yerine' burada 'kule yerine' anlamına da gelip belirsiz; 'kulenin olduğu yere' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0081` birebir aynı, `@degisim: ilgilenmek -> dinlemek` (tutuyorsan), ardından `@onarim: 6614bb9cee6ddae8dbcdf9f24c13ea65e9c17445`, sonra gövde.

### Hikâye 11: tohum sakir-0083 (deneme 3 -> 4)

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
Yağmur cama vuruyordu. Şakir ile annesi Kadriye evde pul eşleştirme oyunu oynuyordu. Ama ikisi de aynı anda aynı pulu tuttu ve oyun durdu. Şakir biraz düşündü ve macera oyunlarını hatırladı. Orada herkes sırayla yürürdü. "Anneciğim, sırayla oynayalım, önce sen bir pul seç," dedi Şakir. Kadriye güldü ve başını salladı. Önce Kadriye iki gemi pulunu buldu ve yan yana koydu. Sonra sıra Şakir'e geçti. Şakir de iki güzel çiçek pulunu eşleştirdi. "Aferin, Şakir!" dedi Kadriye. İkisi sırayla oynadı ve bütün pulların eşini buldu. Şakir çok sevindi, çünkü oyun artık hiç durmadı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düşündü ve macera oyunlarını hatırladı"
   - Cümle 4: «Şakir biraz düşündü ve macera oyunlarını hatırladı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "macera oyunlarını hatırladı"
   - Cümle 4: «Şakir biraz düşündü ve macera oyunlarını hatırladı.»
   - Açıklama: Tohumdaki macera sevgisi işe yarar biçimde kullanılmıyor, yalnız sırayla oynamayı hatırlatan uydurma bir bağ olarak geçiyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Orada herkes sırayla yürürdü"
   - Cümle 5: «Orada herkes sırayla yürürdü.»
   - Açıklama: 'Orada' zamirinin macera oyunlarını mı bir yeri mi gösterdiği belli değil ve 'herkes' kimseyi göstermiyor.
   - Açıklama: 'Orada' zamirinin neyi gösterdiği belli değil; oyunlar bir yer değildir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0083` birebir aynı, ardından `@onarim: 07a4f468db1584099edd3e0a5812fe05204a2bc1`, sonra gövde.

### Hikâye 12: tohum sakir-0084 (deneme 3 -> 4)

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
Bir sabah Şakir ile Fil Necati parktaydı. Necati ilk kez hiç durmadan koştu. Şakir onu kutlamak istedi ama yanında hiç ödül yoktu. Şakir şapkasını ödül yapmayı düşündü ama Necati'nin başı çok yüksekti. Sonra yerde alçak bir taş küp gördü. "Necati, küpün üstüne otur," dedi Şakir. Necati küpe oturdu ve başı aşağı indi. Şakir şapkasını çıkardı ve Necati'nin başına koydu. Küçük şapka filin kocaman başında çok garip durdu. İkisi de çok güldü. "Bu senin ödül şapkan, Necati!" dedi Şakir. "Teşekkürler, Şakir, bu çok güzel bir kutlama!" dedi Necati. Sonra ikisi yan yana parkta mutlu mutlu yürüdü.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "ama Necati'nin başı çok yüksekti"
   - Cümle 4: «Şakir şapkasını ödül yapmayı düşündü ama Necati'nin başı çok yüksekti.»
   - Açıklama: Ödül yokluğunun yanına ikinci bir sorun olarak başın yüksekliği ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yerde alçak bir taş küp gördü"
   - Cümle 5: «Sonra yerde alçak bir taş küp gördü.»
   - Açıklama: Taş küp çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0084` birebir aynı, ardından `@onarim: f6eae4fa6b9f9c1ba0b432fc032c1fc2da61b3c7`, sonra gövde.
