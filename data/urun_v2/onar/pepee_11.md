# Editör görevi (onarım): Pepee, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0041 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0041
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kök', fiil 'ovuşturmak', sıfat 'bembeyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: ağacın kökü dışarı çıkmıştı ve turunu durduruyordu | köke dikkatle bakıp üstünden zıpladı
@tohum: pepee-0041
Bir sabah Pepee ormanda bembeyaz çiçeklerin arasında dans ediyordu. Pepee büyük bir ağacın etrafında dönerek bir tur atmak istedi. Ama ağacın kalın bir kökü dışarı çıkmıştı. Pepee köke basmak istemedi ve her seferinde orada durdu. Böylece turunu bir türlü bitiremedi. Pepee ellerini ovuşturdu ve köke dikkatle baktı. Sonra yeniden dönmeye başladı. Bu kez kökün yanına gelince üstünden zıpladı. Zıplamak dönmekten de eğlenceliydi. Pepee çok sevindi, çünkü turunu bu kez hiç durmadan bitirmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dışarı çıkmıştı ve turunu durduruyordu"
   - Cümle 0 (plan satırı): «ağacın kökü dışarı çıkmıştı ve turunu durduruyordu | köke dikkatle bakıp üstünden zıpladı»
   - Açıklama: Kök turu durdurmaz; Pepee kendisi duruyor, fiil öznesine uymuyor.
   - Açıklama: Kök turu durdurmaz; fiil öznesine uymuyor ve plan satırında 'turunu' kökün turu gibi okunuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Pepee köke basmak istemedi"
   - Cümle 4: «Pepee köke basmak istemedi ve her seferinde orada durdu.»
   - Açıklama: Pepee'nin neden köke basmak istemediği söylenmiyor ve sorun önemsiz bir oyun aksaklığı olarak kalıyor.
   - Açıklama: Pepee'nin köke basmak istememesinin sebebi söylenmiyor ve sorun çok önemsiz kalıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "turunu bir türlü bitiremedi"
   - Cümle 5: «Böylece turunu bir türlü bitiremedi.»
   - Açıklama: 'Bir türlü' deyimsel bir kalıp, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0041` birebir aynı, ardından `@onarim: 1b863de4d2007a374bd4082d8caf3ec3441ca5d7`, sonra gövde.

### Hikâye 2: tohum pepee-0042 (deneme 2 -> 3)

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
Deniz kıyısında kumlar sıcak ve kuruydu. Pepee küçük teneke kovasıyla bir kum kulesi yapmak istiyordu. Ama kovayı kaldırınca kuru kum hemen dağıldı. Pepee bir kez daha denedi, ama kule yine olmadı. Sonra kumu biraz kazdı ve altında ıslak kum buldu. Küçük dalgalar bu kumu ıslatmıştı. Kovayı ıslak kumla doldurdu ve elleriyle bastırdı. Kovayı yavaşça ters çevirip kaldırdı. Kumda dimdik bir kule duruyordu! Pepee ıslak kumun daha iyi olduğunu öğrendi. Hemen yanına üç tane daha yaptı. Pepee yorgundu ama çok mutluydu, çünkü artık dört kulesi vardı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee küçük teneke kovasıyla"
   - Cümle 2: «Pepee küçük teneke kovasıyla bir kum kulesi yapmak istiyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında hiçbir büyük olmadan yalnız başına deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0042` birebir aynı, `@degisim: yıkanmak -> ıslatmak` (tutuyorsan), ardından `@onarim: c0629f40d1f928a75a7dd9e0313eb2bfe9782bd3`, sonra gövde.

### Hikâye 3: tohum pepee-0043 (deneme 2 -> 3)

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
Bir sabah Pepee parkta bahçe oyunu oynuyordu. Elinde küçük, kırmızı bir kova vardı. Kaydırağın yanındaki ayçiçeği yere doğru eğilmişti, çünkü toprağı çok kuruydu. Pepee çiçeğe hemen su vermek istedi. Parkta çeşmeyi aradı ve onu salıncakların arkasında buldu. Kovasını doldurdu ve çiçeğe geri koştu. Suyu dikkatle toprağa döktü. Sonra çiçeğin yanına oturdu ve bekledi. Biraz sonra ayçiçeği yavaş yavaş yukarı kalktı. Pepee böylece kuru toprağa su vermek gerektiğini öğrendi. Pepee çok sevindi, çünkü ayçiçeği artık dik duruyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ayçiçeği yavaş yavaş yukarı kalktı"
   - Cümle 9: «Biraz sonra ayçiçeği yavaş yavaş yukarı kalktı.»
   - Açıklama: Çiçek için 'kalkmak' uygun değil; 'doğruldu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0043` birebir aynı, `@degisim: sulu -> kuru` (tutuyorsan), ardından `@onarim: adfb5141ef1eaafde5f9a62a9a5c801bcf794688`, sonra gövde.

### Hikâye 4: tohum pepee-0044 (deneme 1 -> 2)

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
Pepee deniz kıyısında kovasıyla kumdan bir kule yapıyordu. Birden yağmur başladı. Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı. Pepee kulesini kurtarmak istedi. Kovayı kaldırdı ve kulenin üstüne ters kapattı. Artık damlalar kovanın üstüne düşüyordu. Pepee de yanına çömeldi ve bekledi. Yağmur kısa sürdü ve biraz sonra dindi. Pepee kovayı yavaşça çekti. Kule yerinde duruyordu. Yanındaki kum ıslanmış ve yapışkan olmuştu. Pepee böylece ıslak kumun daha iyi tuttuğunu öğrendi. Hemen bu kumla kuleye yeni bir kat ekledi. Pepee çok sevindi, çünkü kulesini yağmurdan korumuştu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee deniz kıyısında kovasıyla"
   - Cümle 1: «Pepee deniz kıyısında kovasıyla kumdan bir kule yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yağmurda büyüksüz yalnız kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee de yanına çömeldi"
   - Cümle 7: «Pepee de yanına çömeldi ve bekledi.»
   - Açıklama: 'de' başka birinin de çömeldiğini ima ediyor ama sahnede Pepee yalnız.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee böylece ıslak kumun daha iyi tuttuğunu öğrendi"
   - Cümle 12: «Pepee böylece ıslak kumun daha iyi tuttuğunu öğrendi.»
   - Açıklama: Sorun çözüldükten sonra ıslak kum dersi ve yeni kat ekleme, ana olaya bağlı olmayan fazladan bir yan olay getiriyor.
   - Açıklama: Islak kum dersi sorunla ilgisiz ikinci bir iş açıyor ve yağmurun kuleyi dağıtmasıyla çelişir gibi duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0044` birebir aynı, `@degisim: çikolata -> kova` (tutuyorsan), ardından `@onarim: 68580f2db5df2fbc2784458431a2345af8e356ea`, sonra gövde.

### Hikâye 5: tohum pepee-0045 (deneme 1 -> 2)

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
@plan: kağıt zincir iki sandalyenin arasına yetmedi | üç halka daha yapıp zinciri uzattı
@tohum: pepee-0045
@degisim: kamera -> kağıt
Yağmur cama tık tık vuruyordu. Pepee odasında kardeşi Bebee için bir sürpriz hazırlıyordu. Kağıttan renkli bir zincir yapmıştı. Zinciri iki sandalyenin arasına asmak istiyordu. Ama zincir kısaydı ve öbür sandalyeye yetmedi. Pepee masadaki kağıtlara baktı. Halka yapmayı yeni öğrenmişti. Hemen üç halka daha yaptı ve zincire ekledi. Şimdi zincir iki sandalyeye de yetti. Pepee zinciri astı ve Bebee'yi çağırmak için oynak bir şarkı söyledi. Bebee koşarak odaya girdi. "Bu zincir benim için mi?" diye sordu Bebee. "Evet, Bebee, senin için yaptım," dedi Pepee. "Çok güzel olmuş, teşekkür ederim, Pepee!" dedi Bebee.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki sandalyenin arasına yetmedi"
   - Cümle 0 (plan satırı): «kağıt zincir iki sandalyenin arasına yetmedi | üç halka daha yapıp zinciri uzattı»
   - Açıklama: Zincir iki sandalyenin arasına yetmez, arasındaki boşluğa ya da öbür sandalyeye yetmez; fiil tümleciyle uyuşmuyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kağıttan renkli bir zincir yapmıştı.»
   - Açıklama: Zincirin kısa kalma sorunu ilk üç cümlede değil ancak beşinci cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "için oynak bir şarkı"
   - Cümle 10: «Pepee zinciri astı ve Bebee'yi çağırmak için oynak bir şarkı söyledi.»
   - Açıklama: 'Oynak' kelimesi şarkı için 3 yaşındaki çocuğun bilmeyeceği bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0045` birebir aynı, `@degisim: kamera -> kağıt` (tutuyorsan), ardından `@onarim: 28c49a8f2dbc53015188efaa18df1fcdc1d1b611`, sonra gövde.

### Hikâye 6: tohum pepee-0046 (deneme 1 -> 2)

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
Mutfakta Pepee ile Annee tren oyunu oynuyordu. Sandalyeler trenin vagonları olmuştu. Ama tek bir düdük vardı ve ikisi de onu çalmak istiyordu. Pepee biraz düşündü. "Anneciğim, düdüğü sırayla çalalım mı?" diye sordu Pepee. "Olur, önce sen çal," dedi Annee. Pepee düdüğü çaldı ve annesine kağıttan bir bilet verdi. "Bu bilet çok pahalı, bir öpücük!" dedi Pepee. Annee güldü ve Pepee'yi öptü. Sonra düdük Annee'ye geçti. Pepee bu kez sandalyeye oturdu ve bekledi. "Nereye gidiyorsunuz?" diye sordu Annee. "Kahvaltı masasına, bal ve yumurta yemeye!" dedi Pepee. Pepee çok mutluydu, çünkü sırayla oynadıkları için ikisi de düdüğü çalmıştı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesine kağıttan bir bilet verdi"
   - Cümle 7: «Pepee düdüğü çaldı ve annesine kağıttan bir bilet verdi.»
   - Açıklama: Kağıttan bilet sebepsizce beliriyor ve düdük sorunuyla ilgisi yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Bu bilet çok pahalı, bir öpücük!""
   - Cümle 8: «"Bu bilet çok pahalı, bir öpücük!" dedi Pepee.»
   - Açıklama: 'Pahalı' fiyat kavramı ve öpücükle ödeme mecazı küçük çocuğa soyut.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kahvaltı masasına, bal ve yumurta"
   - Cümle 13: «"Kahvaltı masasına, bal ve yumurta yemeye!" dedi Pepee.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor; kartın özellikler alanındaki kullanım beklentisini karşılamıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Kahvaltı masasına, bal ve yumurta yemeye!" dedi Pepee"
   - Cümle 13: «"Kahvaltı masasına, bal ve yumurta yemeye!" dedi Pepee.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız oyunun süsü olarak geçiyor, sırayla çalma çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0046` birebir aynı, `@degisim: sığınmak -> beklemek` (tutuyorsan), ardından `@onarim: 60784ffbd7b01f089ffefde176e195156408c75e`, sonra gövde.

### Hikâye 7: tohum pepee-0048 (deneme 1 -> 2)

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
Parkta Pepee ile Nenee saray oyunu oynuyordu. Pepee kağıttan bir taç takıp süslenmişti. Ama taç çok hafifti ve rüzgar esince hep yere düşüyordu. Pepee ninesine bir gösteri yapmak istiyordu. Pepee tacı yerden aldı ve biraz düşündü. Sonra tacı mavi şapkasının üstüne sıkıca geçirdi. Rüzgar yine esti ama taç bu kez düşmedi. "Nineciğim, şimdi beni izle!" dedi Pepee. Pepee salıncakların önünde güzelce dans etti. Nenee ellerini çırptı ve güldü. "Ne güzel bir gösteri, bravo!" dedi Nenee. "Teşekkürler, nineciğim, seninle oynamak çok güzel!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tacı mavi şapkasının üstüne sıkıca geçirdi"
   - Cümle 6: «Sonra tacı mavi şapkasının üstüne sıkıca geçirdi.»
   - Açıklama: Mavi şapka daha önce hiç kurulmadan çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0048` birebir aynı, `@degisim: gevrek -> taç` (tutuyorsan), ardından `@onarim: 78a3bb80883db5be497aa7a9ce024e592306b9b1`, sonra gövde.

### Hikâye 8: tohum pepee-0050 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0050
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'televizyon', fiil 'işaretlemek', sıfat 'serin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kumdan ince ve garip bir ses geliyordu | sesi duyduğu yerleri işaretledi ve boş şişeyi buldu
@tohum: pepee-0050
@degisim: televizyon -> şişe
Serin bir rüzgar esiyordu. Pepee deniz kıyısında kumdan bir yol yapıyordu. Birden yakından ince bir ıslık sesi geldi. Pepee sesin nereden geldiğini çok merak etti. Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi. Çizgilerin hepsi büyük bir taşın yanındaydı. Pepee taşın arkasına baktı. Orada boş bir şişe yatıyordu. Bu, Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi. Rüzgar şişenin ağzından geçince o ses çıkıyordu. Pepee şişeyi çöpe atmak için yanına aldı. Pepee çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kumdan ince ve garip bir ses geliyordu"
   - Cümle 0 (plan satırı): «kumdan ince ve garip bir ses geliyordu | sesi duyduğu yerleri işaretledi ve boş şişeyi buldu»
   - Açıklama: Gövdede ses kumdan değil taşın arkasındaki şişeden geliyor; plan sorunu yanlış söylüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee deniz kıyısında kumdan"
   - Cümle 2: «Pepee deniz kıyısında kumdan bir yol yapıyordu.»
   - Açıklama: Güvenli özellik kullanımı satırı Pepee'nin yeni şeyleri bir büyüğün yanında denediğini söylüyor, ama dört yaşındaki Pepee deniz kıyısında yalnız.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tahin pekmezin şişesiydi"
   - Cümle 9: «Bu, Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi.»
   - Açıklama: Tamlama eki eksik; 'tahin pekmezinin şişesiydi' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltıda çok sevdiği tahin pekmezin şişesiydi"
   - Cümle 9: «Bu, Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi.»
   - Açıklama: Tohumdaki kahvaltı özelliği çözümde işe yaramıyor, yalnız şişeyi tanıtmak için anılıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi"
   - Cümle 9: «Bu, Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak anılıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi"
   - Cümle 9: «Bu, Pepee'nin kahvaltıda çok sevdiği tahin pekmezin şişesiydi.»
   - Açıklama: Şişenin tahin pekmez şişesi olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee şişeyi çöpe atmak için yanına aldı"
   - Cümle 11: «Pepee şişeyi çöpe atmak için yanına aldı.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak Pepee bir büyük olmadan kıyıda bulduğu yabancı şişeyi eline alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0050` birebir aynı, `@degisim: televizyon -> şişe` (tutuyorsan), ardından `@onarim: 713b4a4a49eb50e775fd8a56f8c6ba0958034cee`, sonra gövde.

### Hikâye 9: tohum pepee-0051 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0051
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'harita', fiil 'dönmek', sıfat 'tekerlekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: kardeşinin oyuncağı yoktu ve o da oynamak istiyordu | tekerlekli arabasını kardeşiyle paylaştı
@tohum: pepee-0051
@degisim: harita -> araba
Deniz kıyısında Pepee tekerlekli arabasıyla kum taşıyordu. Kardeşi Bebee yanına geldi ama elinde hiç oyuncak yoktu. Bebee arabaya üzgün üzgün baktı, çünkü o da oynamak istiyordu. "Bebee, arabayı birlikte kullanalım mı?" diye sordu Pepee. "Olur, ama nasıl?" dedi Bebee. "Sen kumu doldur, ben arabayı çekerim," dedi Pepee. Bebee elleriyle arabaya kum doldurdu. Pepee arabayı çekti ve kumun üstünde bir tur döndü. Sonra yer değiştirdiler ve arabayı Bebee çekti. Pepee de arabanın yanında neşeyle dans etti. Bebee ona bakıp çok güldü. "Arabanı paylaştığın için teşekkürler, Pepee!" dedi Bebee.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee de arabanın yanında neşeyle dans etti"
   - Cümle 10: «Pepee de arabanın yanında neşeyle dans etti.»
   - Açıklama: Tohumdaki dans özelliği sorun çözüldükten sonra süs olarak geçiyor, çözüme işe yarar biçimde katılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0051` birebir aynı, `@degisim: harita -> araba` (tutuyorsan), ardından `@onarim: 6df095157a3a2479ff76c368a31093cf4045a9e8`, sonra gövde.

### Hikâye 10: tohum pepee-0052 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0052
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'fide', fiil 'dalgalanmak', sıfat 'beyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: rüzgar esince ince ağaç hep yana eğiliyordu | ağacı kurdeleyle bir dala bağladı
@tohum: pepee-0052
@degisim: fide -> ağaç
Serin bir rüzgar esiyordu. Pepee ile Annee ormanda beyaz çiçekli küçük bir ağaç dikmişti. Pepee bu yeni ağaç için bir kutlama yapmak istiyordu. Ama rüzgar esince ince ağaç hep yana eğiliyordu. Pepee yerden düz ve sağlam bir dal buldu. Dalı onun yanında toprağa soktu. "Anneciğim, çantada ip var mı?" diye sordu Pepee. Annee çantasından uzun bir kurdele çıkardı. Pepee ağacı kurdeleyle dala yavaşça bağladı. Rüzgar yine esti ama ağaç artık dik duruyordu. Kurdele rüzgarda dalgalandı. Pepee ağacın etrafında sevinçle dans etti. Annee de gülerek ellerini çırptı. Pepee çok mutluydu, çünkü küçük ağaç artık hiç eğilmiyordu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Pepee bu yeni ağaç için bir kutlama yapmak istiyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dalı onun yanında toprağa"
   - Cümle 6: «Dalı onun yanında toprağa soktu.»
   - Açıklama: 'onun' zamirinin ağacı mı Pepee'yi mi gösterdiği belli değil.
   - Açıklama: 'Onun' zamirinin ağacı mı Pepee'yi mi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ağacın etrafında sevinçle dans etti"
   - Cümle 12: «Pepee ağacın etrafında sevinçle dans etti.»
   - Açıklama: Tohumdaki dans özelliği sorunun çözümünde işe yaramıyor, yalnız sonda süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0052` birebir aynı, `@degisim: fide -> ağaç` (tutuyorsan), ardından `@onarim: 9f69eac53ae3dc4f556ee8a819c558227f264302`, sonra gövde.

### Hikâye 11: tohum pepee-0053 (deneme 1 -> 2)

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
Ormanda Pepee ile Nenee çiçeklerin arasında oynuyordu. Pepee uzun, mavi bir kurdeleyle dans ediyordu. Birden rüzgar esti ve kurdele bir dala takıldı. Dal, Pepee'nin başının çok üstündeydi. Pepee zıpladı ama kurdeleye yetişemedi. "Nineciğim, kurdeleyi alır mısın?" diye sordu Pepee. Nenee güldü ve parmaklarının ucunda yükseldi. Kurdeleyi daldan yavaş yavaş çekti. Kurdele Pepee'nin eline düştü. "Teşekkürler, nineciğim!" dedi Pepee. "Şimdi ben de seninle oynayayım," dedi Nenee. Pepee ile Nenee kurdeleyi birlikte tuttu ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şimdi ben de seninle oynayayım"
   - Cümle 11: «"Şimdi ben de seninle oynayayım," dedi Nenee.»
   - Açıklama: Nenee ile Pepee baştan beri birlikte oynarken Nenee şimdi oynamaya başlayacakmış gibi konuşuyor.
   - Açıklama: Pepee ile Nenee baştan beri birlikte oynarken Nenee sanki yeni katılıyormuş gibi konuşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0053` birebir aynı, `@degisim: duvar -> dal` (tutuyorsan), ardından `@onarim: ce1c3af020b5b543030aaa9fc2c9d8ca7fc57170`, sonra gövde.
