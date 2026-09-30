# Editör görevi (onarım): Pepee, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0121 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0121
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'piyano', fiil 'paylaşmak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: ormanda çok ağaç vardı ve dedesini bulamadı | kahvaltı kokusunu tanıdı ve kokuya doğru gitti
@tohum: pepee-0121
@degisim: piyano -> örtü
Pepee ormanda Dedee ile saklambaç oynuyordu. Dedee elinde bir sepetle saklandı. Pepee onu aradı ama ormanda çok ağaç vardı ve dedesini bulamadı. Az sonra ağaçların arasından tatlı bir koku geldi. Pepee havayı kokladı ve bu kokuyu kahvaltıdan tanıdı. Bu, tahin ile pekmezin kokusuydu! Pepee kokuya doğru yürüdü ve büyük bir ağacın arkasına baktı. Dedee orada yere bir örtü seriyordu ve çok meşguldü. Örtünün üstünde yumurta, bal ve tahin pekmez vardı. "Seni buldum, dedeciğim!" dedi Pepee. "Buldun, sana sürpriz bir kahvaltı hazırladım," dedi Dedee. Pepee dedesine sıkıca sarıldı. İkisi örtüye oturdu ve kahvaltıyı mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "seriyordu ve çok meşguldü"
   - Cümle 8: «Dedee orada yere bir örtü seriyordu ve çok meşguldü.»
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Meşgul' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0121` birebir aynı, `@degisim: piyano -> örtü` (tutuyorsan), ardından `@onarim: e86d78059e6e8e1e2e9960e6c1d6eca90d2df100`, sonra gövde.

### Hikâye 2: tohum pepee-0124 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0124
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'sünger', fiil 'dizmek', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yer düz değildi ve yumurtalardan biri kayboldu | izin yanından yürüdü ve yumurtayı ağacın dibinde buldu
@tohum: pepee-0124
@degisim: esnek -> yumuşak
Pepee ormanda kahvaltı yapmak için yere bir örtü serdi. Örtünün üstüne üç yumurtayı yan yana dizdi. Ama yer düz değildi ve yumurtalardan biri kayboldu. Pepee yumurtanın nereye gittiğini çok merak etti. Pepee kahvaltıyı çok severdi ve yumurtaların kolay yuvarlandığını bilirdi. Bu yüzden aşağıya doğru baktı. Otların arasında ince bir iz vardı. Pepee izin yanından yavaşça yürüdü. İz, büyük bir ağacın dibinde bitti. Yumurta orada, sünger gibi yumuşak bir çimenin üstünde duruyordu. Pepee yumurtayı aldı ve örtüyü ağacın yanındaki düz yere taşıdı. Pepee çok sevindi, çünkü kaybolan yumurtasını bulmuştu.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee kahvaltıyı çok severdi ve yumurtaların"
   - Cümle 5: «Pepee kahvaltıyı çok severdi ve yumurtaların kolay yuvarlandığını bilirdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunu çözmek için kullanılmıyor, yalnız söyleniyor; çözümü yumurtanın yuvarlandığını bilmek getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşak bir çimenin üstünde"
   - Cümle 10: «Yumurta orada, sünger gibi yumuşak bir çimenin üstünde duruyordu.»
   - Açıklama: 'Çimen' sayılmayan bir kelime; 'bir çimenin' yanlış kullanım, 'yumuşak çimenlerin üstünde' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sünger gibi yumuşak bir çimenin"
   - Cümle 10: «Yumurta orada, sünger gibi yumuşak bir çimenin üstünde duruyordu.»
   - Açıklama: 'Sünger gibi' benzetmesi küçük çocuk için mecazlı anlatım.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sünger gibi yumuşak bir"
   - Cümle 10: «Yumurta orada, sünger gibi yumuşak bir çimenin üstünde duruyordu.»
   - Açıklama: Benzetme 3 yaşındaki çocuk için mecazlı; sade 'yumuşak bir çimen' yeterli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0124` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: 354ac5a3b95ad9391f6efce98aee058fb898154c`, sonra gövde.

### Hikâye 3: tohum pepee-0126 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0126
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'iplik', fiil 'kapanmak', sıfat 'biberli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yuvarlak yumurta kaşıkta durmadı ve düştü | kaşığa bal sürdü ve yumurtayı ipliğe kadar taşıdı
@tohum: pepee-0126
@degisim: kapanmak -> bağlamak
Bir sabah Pepee ormanda kaşıkla yumurta taşıma oyunu oynuyordu. Yumurtayı iki ağaca bağladığı kırmızı ipliğe kadar taşıyacaktı. Ama yuvarlak yumurta kaşıkta durmadı ve çimlere yuvarlandı. Pepee yumurtayı yerden aldı ama yumurta yine düştü. Sonra yanındaki kahvaltı sepetini açtı. İçinde bal ve biberli peynir vardı. Pepee kaşığa biraz bal sürdü ve yumurtayı üstüne koydu. Yumurta bala yapıştı ve artık kaymadı. Pepee yavaş yavaş yürüdü ve yumurta hiç düşmedi. Sonunda kırmızı ipliğe vardı. Oyun bitince ağacın altına oturdu ve yumurtayı biberli peynirle mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yanındaki kahvaltı sepetini açtı"
   - Cümle 5: «Sonra yanındaki kahvaltı sepetini açtı.»
   - Açıklama: Kahvaltı sepeti önceden kurulmadan tam çözüm gerektiğinde beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0126` birebir aynı, `@degisim: kapanmak -> bağlamak` (tutuyorsan), ardından `@onarim: dcc3bac7d004d05a7c6d0e13801664dbe027343c`, sonra gövde.

### Hikâye 4: tohum pepee-0128 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0128
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'battaniye', fiil 'satmak', sıfat 'çabuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: kum çok kuru olduğu için kuleler çabuk dağıldı | küçük kabı ıslak kumla doldurup ters çevirdi
@tohum: pepee-0128
@degisim: satmak -> doldurmak
Bir sabah Pepee ile Bebee deniz kıyısında bir battaniyenin üstünde oturuyordu. Pepee kumdan kuleler yapmak istedi. Ama kum çok kuruydu ve kuleler çabuk dağıldı. Pepee kahvaltıda yumurtasını yediği küçük kabı battaniyeden aldı. Kabı dalgaların ıslattığı kumla doldurdu. Sonra kabı ters çevirdi ve yavaşça kaldırdı. Kumda yumurta gibi yuvarlak bir kule duruyordu. "Bak, Bebee, bu kule dağılmadı!" dedi Pepee. "Ben de yapmak istiyorum!" dedi Bebee. Pepee kabı ona verdi ve Bebee de bir kule yaptı. Pepee çok sevindi, çünkü kumdan sağlam bir kule yapmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltıda yumurtasını yediği küçük kabı"
   - Cümle 4: «Pepee kahvaltıda yumurtasını yediği küçük kabı battaniyeden aldı.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız kabın nereden geldiğini söyleyen süs olarak geçiyor, çözüme işe yarar biçimde katılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0128` birebir aynı, `@degisim: satmak -> doldurmak` (tutuyorsan), ardından `@onarim: b68cac926fb94c965049f28250595a041b3083b7`, sonra gövde.

### Hikâye 5: tohum pepee-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Annee
@tohum: pepee-0129
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'salata', fiil 'homurdanmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Annee
@plan: yakında komik bir şey homurdanıyordu | dans ederek dolaştı ve sesin kendi karnından geldiğini buldu
@tohum: pepee-0129
Deniz kıyısında küçük dalgalar kuma vuruyordu. Pepee annesiyle kumda otururken yakında bir ses duydu. Bir şey komik komik homurdanıyordu. "Anneciğim, bu ses nereden geliyor?" diye sordu Pepee. "Bilmiyorum, sen bul bakalım," dedi Annee. Pepee sesi bulmak için kalktı ve dans etmeye başladı. Sağa dans edince ses de sağa, sola dans edince sola gitti. Pepee durdu ve elini karnına koydu. "Anneciğim, homurdanan benim karnım!" dedi Pepee ve güldü. Annee de güldü ve çantadan bir kap salata çıkardı. Sonra ikisi kumda oturdu ve salatayı memnun memnun yedi.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bir şey komik komik homurdanıyordu"
   - Cümle 3: «Bir şey komik komik homurdanıyordu.»
   - Açıklama: 'Komik komik' ikilemesi homurdanma fiiline uygun ve doğal değil.
   - Açıklama: 'Komik komik' Türkçede kullanılan bir ikileme değil ve homurdanmaya uymuyor.
   - Açıklama: 'Komik komik' ikilemesi homurdanmayı niteleyen doğal bir zarf değil; kelime yanlış kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bir şey komik komik homurdanıyordu"
   - Cümle 3: «Bir şey komik komik homurdanıyordu.»
   - Açıklama: Pepee'nin kendi karnının sesini yakındaki başka bir şey sanması akla yatkın değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee sesi bulmak için kalktı ve dans etmeye başladı"
   - Cümle 6: «Pepee sesi bulmak için kalktı ve dans etmeye başladı.»
   - Açıklama: Dans etmek sesin sebebine doğrudan yönelen bir çözüm değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "salatayı memnun memnun yedi"
   - Cümle 11: «Sonra ikisi kumda oturdu ve salatayı memnun memnun yedi.»
   - Açıklama: 'Memnun memnun' doğal bir ikileme değil; 'mutlu mutlu' olmalı.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "salatayı memnun memnun yedi"
   - Cümle 11: «Sonra ikisi kumda oturdu ve salatayı memnun memnun yedi.»
   - Açıklama: 'Memnun' 3 yaşındaki çocuğun bildiği bir kelime değil ve ikileme doğal değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0129` birebir aynı, ardından `@onarim: 6839d4ff8a60f8805bd1204e0fd2c7cf064e7929`, sonra gövde.

### Hikâye 6: tohum pepee-0130 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0130
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: bir şey yapmak
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çilek', fiil 'takmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: çiçekler şapkadan hep kaydı çünkü çok kısaydı | çiçekleri birbirine bağlamayı öğrendi ve halka yaptı
@tohum: pepee-0130
@degisim: düşünceli -> kırmızı
Pepee ormanda kırmızı çiçekler ve çilekler topluyordu. Mavi şapkasını çiçeklerle süslemek istedi. Ama çiçekler şapkadan hep kaydı, çünkü çok kısaydı. Pepee bir çiçeği başka bir çiçeğe sardı. İlk seferde olmadı ve çiçek yere düştü. Pepee bir daha sardı ve bu işi öğrendi. Sonra bütün çiçekleri tek tek birbirine bağladı. Böylece uzun bir çiçek halkası yaptı. Pepee halkayı şapkasının çevresine taktı. Pepee başını salladı ama çiçekler hiç düşmedi. Sonra çileklerini yedi ve çiçekli şapkasıyla ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kırmızı çiçekler ve çilekler topluyordu"
   - Cümle 1: «Pepee ormanda kırmızı çiçekler ve çilekler topluyordu.»
   - Açıklama: Çilekler olayda hiçbir işe yaramıyor; yalnız sonda yenmek için kurulmuş işlevsiz bir ayrıntı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çünkü çok kısaydı"
   - Cümle 3: «Ama çiçekler şapkadan hep kaydı, çünkü çok kısaydı.»
   - Açıklama: Çiçeklerin kendisi değil sapları kısadır; kelime öznesine tam uymuyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra çileklerini yedi"
   - Cümle 11: «Sonra çileklerini yedi ve çiçekli şapkasıyla ormanda mutlu mutlu yürümeye devam etti.»
   - Açıklama: Ormanda kendi topladığı yabani çilekleri yemek taklit edilince tehlikeli bir davranıştır.
   - Açıklama: Ormanda kendi topladığı çilekleri bir büyük olmadan yemesi çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0130` birebir aynı, `@degisim: düşünceli -> kırmızı` (tutuyorsan), ardından `@onarim: 252b5afc78596cb078e2ea555dd5a47709483a53`, sonra gövde.

### Hikâye 7: tohum pepee-0134 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0134
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'scooter', fiil 'belirmek', sıfat 'farklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yağmur başladı ve damlalar şapkasına düştü | kahvaltı örtüsünü başının üstüne tuttu ve kuru kaldı
@tohum: pepee-0134
@degisim: scooter -> bisiklet
Pepee ormanda kahvaltı yapmak için bisikletini itiyordu. Bisikletin sepetinde yumurta, bal ve bir kahvaltı örtüsü vardı. Birden yağmur başladı ve damlalar Pepee'nin mavi şapkasına düştü. Pepee hiç ıslanmak istemedi. Hemen durdu ve örtüyü sepetten çıkardı. Örtüyü başının üstüne tuttu. Sonra bir ağacın yanında sessizce bekledi. Yağmur örtünün üstüne tıp tıp damladı ama Pepee kuru kaldı. Az sonra yağmur dindi. Bulutların arasından sıcak güneş belirdi. Yapraklardaki damlalar farklı renklerde parlıyordu. Pepee ağacın altına oturdu ve yumurtasını ve balını yedi. Pepee çok sevindi, çünkü yağmurda hiç ıslanmamıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yapraklardaki damlalar farklı renklerde parlıyordu"
   - Cümle 11: «Yapraklardaki damlalar farklı renklerde parlıyordu.»
   - Açıklama: Yapraklardaki renkli damlalar olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "oturdu ve yumurtasını ve balını yedi"
   - Cümle 12: «Pepee ağacın altına oturdu ve yumurtasını ve balını yedi.»
   - Açıklama: 'Ve' bağlacı aynı cümlede gereksiz yere iki kez tekrarlanıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yağmurda hiç ıslanmamıştı"
   - Cümle 13: «Pepee çok sevindi, çünkü yağmurda hiç ıslanmamıştı.»
   - Açıklama: Damlalar Pepee'nin şapkasına düşmüşken sonda hiç ıslanmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0134` birebir aynı, `@degisim: scooter -> bisiklet` (tutuyorsan), ardından `@onarim: 643df68bb602ce36bc287eef66a268b79856fd59`, sonra gövde.

### Hikâye 8: tohum pepee-0135 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0135
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kabuk', fiil 'saymak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: çiçekler aynı olduğu için sayıyı karıştırdı | her çiçeğin yanına yumurta kabuğu koydu
@tohum: pepee-0135
@degisim: sağlıklı -> güzel
Kuşlar ötüyordu ve Pepee ormanda kahvaltı yapıyordu. Birden ağacın altında bir sürü güzel sarı çiçek gördü. Pepee çiçekleri saymak istedi ama sayıyı hep karıştırdı, çünkü hepsi aynıydı. Pepee tabağındaki yumurtanın kabuğunu küçük parçalara ayırdı. Her çiçeğin yanına bir kabuk parçası koydu ve bir sayı söyledi. Kabuğu olan çiçeğe bir daha bakmadı. Tam on iki çiçek vardı. Sonra parçaları tek tek topladı ve tabağına geri koydu. Pepee çok sevindi, çünkü sonunda kaç çiçek olduğunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kabuğu olan çiçeğe bir"
   - Cümle 6: «Kabuğu olan çiçeğe bir daha bakmadı.»
   - Açıklama: Çiçeğin kabuğu olmaz; 'yanında kabuk olan çiçeğe' denmeli.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kabuğu olan çiçeğe bir daha bakmadı"
   - Cümle 6: «Kabuğu olan çiçeğe bir daha bakmadı.»
   - Açıklama: Çiçeğin kabuğu olmaz; 'yanında kabuk olan çiçek' anlamı yanlış kurulmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0135` birebir aynı, `@degisim: sağlıklı -> güzel` (tutuyorsan), ardından `@onarim: a1888f26f7b4d1707555ea7a8c6cb8738fdaf285`, sonra gövde.

### Hikâye 9: tohum pepee-0136 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0136
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: paylaşmak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bot', fiil 'oturmak', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: annenin tabağı boştu çünkü evde yumurta kalmamıştı | kendi yumurtasını ikiye bölüp annesiyle paylaştı
@tohum: pepee-0136
@degisim: bot -> tabak
Bir sabah Pepee ile Annee mutfakta masaya oturdu. Pepee'nin tabağında bir yumurta vardı. Ama Annee'nin yeşil tabağı boştu, çünkü evde başka yumurta yoktu. Pepee annesinin boş tabağına baktı. Kahvaltısındaki yumurtayı çatalıyla dikkatle ikiye böldü. Büyük parçayı annesinin tabağına koydu. Artık iki tabakta da birer parça yumurta vardı. Annee önce çok şaşırdı. Sonra Pepee'ye sarıldı ve onu öptü. İkisi yumurtayı yan yana yedi. Annee çok sevindi, çünkü Pepee en sevdiği yumurtayı onunla paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "annenin tabağı boştu çünkü evde"
   - Cümle 0 (plan satırı): «annenin tabağı boştu çünkü evde yumurta kalmamıştı | kendi yumurtasını ikiye bölüp annesiyle paylaştı»
   - Açıklama: 'Çünkü' öncesinde virgül eksik; gövdede virgül kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee en sevdiği yumurtayı onunla paylaşmıştı"
   - Cümle 11: «Annee çok sevindi, çünkü Pepee en sevdiği yumurtayı onunla paylaşmıştı.»
   - Açıklama: Tek bir yumurta için 'en sevdiği' uygun değil ve kimin sevdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0136` birebir aynı, `@degisim: bot -> tabak` (tutuyorsan), ardından `@onarim: da4bc48b07395adefa5e67987392aee181d4ab0b`, sonra gövde.

### Hikâye 10: tohum pepee-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0137
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'bisiklet', fiil 'hoplamak', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: tek ayakla giderken hep bir yana eğildi | kollarını iki yana açıp yeniden hopladı
@tohum: pepee-0137
@degisim: bisiklet -> taş
Deniz kıyısında Pepee'nin nefis karpuzu bir taşın üstünde duruyordu. Pepee o taşa kadar tek ayakla gitmek istedi. Ama her seferinde bir yana eğildi ve öbür ayağı kuma değdi. Pepee biraz düşündü. Dans ederken kollarını iki yana açtığını hatırladı. Kollarını yine öyle açtı ve tek ayakla hopladı. Bu kez öbür ayağı kuma hiç değmedi. Pepee küçük küçük zıpladı ve taşa kadar gitti. Sonra taşın yanına oturdu ve karpuzunu yedi. Pepee çok sevindi, çünkü ilk kez tek ayakla oraya varmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee'nin nefis karpuzu bir"
   - Cümle 1: «Deniz kıyısında Pepee'nin nefis karpuzu bir taşın üstünde duruyordu.»
   - Açıklama: 'Nefis' 3 yaşındaki çocuğun bilmeyebileceği bir kelime.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee o taşa kadar tek ayakla gitmek istedi"
   - Cümle 2: «Pepee o taşa kadar tek ayakla gitmek istedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız başına yeni bir şey deniyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama her seferinde bir yana eğildi"
   - Cümle 3: «Ama her seferinde bir yana eğildi ve öbür ayağı kuma değdi.»
   - Açıklama: Pepee'nin neden bir yana eğildiği, yani sorunun sebebi söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0137` birebir aynı, `@degisim: bisiklet -> taş` (tutuyorsan), ardından `@onarim: fddbee3b3ae9c37d96891961395439d7f395764e`, sonra gövde.

### Hikâye 11: tohum pepee-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0138
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mısır', fiil 'örtmek', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kale suya çok yakındı ve dalgalar onu dağıttı | dalgaların nereye geldiğini öğrendi ve kuru kumda kale yaptı
@tohum: pepee-0138
@degisim: mısır -> kova
Deniz kıyısında Şila kovasıyla kumdan bir kale yapıyordu. Pepee de onun yanında deniz kabukları topluyordu. Ama kale suya çok yakındı ve küçük dalgalar dibini dağıttı. Şila üzüldü. Pepee ona yardım etmek istedi. Önce dalgaları dikkatle izledi. Dalgaların yalnız ıslak kuma kadar geldiğini öğrendi. Pepee kovayı kuru kumla doldurdu ve ters çevirdi. Dalgalardan uzakta yeni ve büyük bir kale çıktı. Şila da kalenin tepesini Pepee'nin kabuklarıyla örttü. Dalgalar yine geldi ama yeni kaleye hiç değmedi. Şila sevinçle ellerini çırptı. Pepee bundan sonra kaleleri hep kuru kumda yaptı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Deniz kıyısında Şila kovasıyla kumdan"
   - Cümle 1: «Deniz kıyısında Şila kovasıyla kumdan bir kale yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, oysa iki küçük çocuk deniz kıyısında büyük olmadan yalnız oynuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0138` birebir aynı, `@degisim: mısır -> kova` (tutuyorsan), ardından `@onarim: f62ac72455b543622e90c086b331d07eb048b557`, sonra gövde.

### Hikâye 12: tohum pepee-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0139
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tabela', fiil 'yıkamak', sıfat 'siyah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: tabela çamurla kaplıydı ve ok görünmüyordu | dedesinden su isteyip tabelayı yıkadı
@tohum: pepee-0139
Yağmur yeni dinmişti. Pepee ile Dedee ormanda sırayla önden yürüme oyunu oynuyordu. Sıra Pepee'deydi ama tabela çamurla kaplıydı. Pepee tabeladaki okun yolu gösterdiğini dedesinden öğrenmişti. Çamurdan oku göremedi ve nereye gideceğini bilemedi. "Dede, bana biraz su verir misin?" diye sordu Pepee. Dedee su şişesini hemen ona verdi. Pepee suyla tabelayı güzelce yıkadı. Çamurun altından siyah bir ok çıktı. Pepee okun gösterdiği tarafa önden yürüdü. Dedee de gülerek arkasından geldi. "Aferin, Pepee, yolu sen buldun!" dedi Dedee. Pepee bundan sonra ormanda hep tabeladaki oka baktı.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Pepee bundan sonra ormanda hep tabeladaki oka baktı"
   - Cümle 13: «Pepee bundan sonra ormanda hep tabeladaki oka baktı.»
   - Açıklama: Pepee oka bakmayı zaten biliyordu; son ders cümlesi yaşanan çamur sorunundan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0139` birebir aynı, ardından `@onarim: 84e61f8e2f66b427073eca0784ecb24e853bded2`, sonra gövde.
