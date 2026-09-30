# Editör görevi (onarım): Pepee, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Bebee
@tohum: pepee-0125
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kaşık', fiil 'korunmak', sıfat 'eksik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | park | Bebee
@plan: kaydıraktan kayarken çantadan bir kaşık düştü | kardeşinden yardım istedi ve kaşığı birlikte buldular
@tohum: pepee-0125
Pepee ile Bebee parkta kahvaltı yapmak istedi. Güneşten korunmak için ağacın gölgesine oturdular. Ama Pepee kaydıraktan kayarken çantadan bir kaşık düşmüştü. Bal için bir kaşık eksikti. Pepee kaydırağın yanına koştu ama kaşığı göremedi. "Bebee, gel bana yardım et, kaşığı birlikte arayalım," dedi Pepee. Bebee hemen koşarak geldi. "Ben küçüğüm, kaydırağın altına sığarım!" dedi Bebee. Bebee eğildi ve kaydırağın altına baktı. Kaşık orada, bir taşın yanında duruyordu. Bebee kaşığı alıp Pepee'ye uzattı. "Teşekkürler, Bebee!" dedi Pepee. Sonra ikisi yerlerine döndü ve ballı ekmeklerini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kaşığı birlikte buldular"
   - Cümle 0 (plan satırı): «kaydıraktan kayarken çantadan bir kaşık düştü | kardeşinden yardım istedi ve kaşığı birlikte buldular»
   - Açıklama: Planda kaşığı birlikte buldukları söyleniyor ama gövdede kaşığı yalnız Bebee buluyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bebee kaşığı alıp Pepee'ye uzattı"
   - Cümle 11: «Bebee kaşığı alıp Pepee'ye uzattı.»
   - Açıklama: Kaşığı Bebee tek başına bulup veriyor; Pepee yardım istedikten sonra çözüme hiç katılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0125` birebir aynı, ardından `@onarim: b7da714f16ee4d347fec3ba53b2968c06fe7d6df`, sonra gövde.

### Hikâye 2: tohum pepee-0126 (deneme 1 -> 2)

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
Bir sabah Pepee ormanda kaşıkta yumurta taşıma oyunu oynuyordu. Bitiş için iki ağacın arasına kırmızı bir iplik bağlamıştı. Ama yuvarlak yumurta kaşıkta durmadı ve çimlere yuvarlandı. Pepee yumurtayı yerden aldı ama yumurta yine düştü. Pepee güldü ve biraz düşündü. Sonra yanındaki kahvaltı sepetini açtı. İçinde bal ve biberli peynir vardı. Pepee kaşığa biraz bal sürdü ve yumurtayı üstüne koydu. Yumurta bala yapıştı ve artık kaymadı. Pepee yavaş yavaş yürüdü ve yumurta hiç düşmedi. Sonunda kırmızı ipliğe vardı. Oyun bitince ağacın altına oturdu ve yumurtayı biberli peynirle mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee ormanda kaşıkta yumurta taşıma oyunu oynuyordu"
   - Cümle 1: «Bir sabah Pepee ormanda kaşıkta yumurta taşıma oyunu oynuyordu.»
   - Açıklama: Dört yaşındaki Pepee ormanda büyüksüz yalnız oynuyor; kartın güvenli kullanım satırı yeni şeyleri bir büyüğün yanında denemesini ister.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bitiş için iki ağacın"
   - Cümle 2: «Bitiş için iki ağacın arasına kırmızı bir iplik bağlamıştı.»
   - Açıklama: 'Bitiş' kelimesi eksiltili ve soyut kalıyor; 3 yaşındaki çocuk için 'bitiş çizgisi' gibi somut bir ifade gerekir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yanındaki kahvaltı sepetini açtı"
   - Cümle 6: «Sonra yanındaki kahvaltı sepetini açtı.»
   - Açıklama: Daha önce kurulmamış kahvaltı sepeti çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0126` birebir aynı, `@degisim: kapanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 825ce9c213c432bdb6e77e3a2bd832a615343f81`, sonra gövde.

### Hikâye 3: tohum pepee-0127 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0127
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'nota', fiil 'tamamlamak', sıfat 'parlak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: ikisi aynı anda vurunca notalar karıştı | sırayla çalmayı önerdi ve şarkıyı tamamladılar
@tohum: pepee-0127
Ormanda, çiçeklerin yanında Pepee ile Annee kahvaltı yapıyordu. Kaşıklarla parlak bardaklara vurup nota çıkarıyorlardı. Ama ikisi aynı anda vurunca sesler birbirine karıştı. Pepee'nin sevdiği şarkı hiç anlaşılmadı. "Anneciğim, sırayla çalalım, bir nota sen, bir nota ben!" dedi Pepee. "Olur, önce sen başla," dedi Annee. Pepee ilk bardağa vurdu. Sonra Annee ikinci bardağa vurdu. Böylece şarkıyı nota nota tamamladılar. Bu kez şarkı çok güzel çıktı. Annee gülümsedi ve Pepee'ye sarıldı. Pepee bundan sonra annesiyle şarkıları hep sırayla çaldı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ile Annee kahvaltı yapıyordu"
   - Cümle 1: «Ormanda, çiçeklerin yanında Pepee ile Annee kahvaltı yapıyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız dekor olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bardaklara vurup nota çıkarıyorlardı"
   - Cümle 2: «Kaşıklarla parlak bardaklara vurup nota çıkarıyorlardı.»
   - Açıklama: 'Nota' soyut bir müzik terimi ve 3 yaşındaki bir çocuk bunu bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir nota sen, bir nota ben"
   - Cümle 5: «"Anneciğim, sırayla çalalım, bir nota sen, bir nota ben!" dedi Pepee.»
   - Açıklama: 'Nota' 3 yaşındaki çocuğun bilmeyebileceği soyut bir müzik kavramı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0127` birebir aynı, ardından `@onarim: 04a24dadd908630703eb7e76d7560bacd65dc144`, sonra gövde.

### Hikâye 4: tohum pepee-0129 (deneme 1 -> 2)

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
@plan: yakında bilinmeyen bir şey homurdanıyordu | dans ederek dolaştı ve sesin karnından geldiğini buldu
@tohum: pepee-0129
Deniz kıyısında küçük dalgalar kuma vuruyordu. Pepee annesiyle kumda otururken garip bir ses duydu. Yakında bir şey homurdanıyordu. "Anneciğim, bu ses nereden geliyor?" diye sordu Pepee. "Bilmiyorum, sen bul bakalım," dedi Annee. Pepee kalktı ve kumda dans ederek dolaştı. Sağa döndü, sola zıpladı. Ama ses her yerde onunla birlikte geldi. Pepee durdu ve karnına baktı. "Ses benim karnımdan geliyor, anneciğim!" dedi Pepee ve güldü. Annee de güldü ve çantadan bir kap salata çıkardı. Sonra ikisi kumda oturdu ve salatayı memnun memnun yedi.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sesin karnından geldiğini buldu"
   - Cümle 0 (plan satırı): «yakında bilinmeyen bir şey homurdanıyordu | dans ederek dolaştı ve sesin karnından geldiğini buldu»
   - Açıklama: Plan satırında 'karnından' kimin karnı olduğu belirsiz; 'sesin karnı' gibi de okunabiliyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Yakında bir şey homurdanıyordu"
   - Cümle 3: «Yakında bir şey homurdanıyordu.»
   - Açıklama: Yakında homurdanan bilinmeyen bir şey küçük çocuk için korkutucu olabilir.
   - Açıklama: Bilinmeyen bir şeyin homurdanması küçük çocuk için korkutucu bir öğe olabilir.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee kalktı ve kumda dans ederek dolaştı"
   - Cümle 6: «Pepee kalktı ve kumda dans ederek dolaştı.»
   - Açıklama: Dans ederek dolaşmak sesin sebebine yönelmiyor; ses ancak durup karnına bakınca bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0129` birebir aynı, ardından `@onarim: 9d67fcce02d5d2a0b66a63430c46173200b845b0`, sonra gövde.

### Hikâye 5: tohum pepee-0131 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0131
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çubuk', fiil 'güzelleştirmek', sıfat 'harika'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: çubuk çok düzdü ve çiçekler aşağı kaydı | otla çiçekleri çubuğa bağlamayı öğrendi
@tohum: pepee-0131
Pepee ormanda kuzeni Şila için bir sürpriz hazırlıyordu. Şila dans edecekti ve Pepee düz bir çubuğu çiçeklerle güzelleştirmek istedi. Ama çubuk çok düzdü ve çiçekler hep aşağı kaydı. Uzun ve ince bir ot aldı ve bir çiçeğin sapına sardı. Sonra otu çubuğa da sardı ve sıkıca bağladı. Çiçek artık kaymadı ve Pepee çiçek bağlamayı öğrendi. Öbür çiçekleri de aynı biçimde bağladı. Az sonra Şila ağaçların arasından geldi. "Sürpriz, Şila, bu çubuk senin dansın için!" dedi Pepee. "Bu harika bir çubuk, teşekkürler, Pepee!" dedi Şila. Sonra Şila çubukla dans etti ve Pepee mutlu mutlu el çırptı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çiçekler hep aşağı kaydı"
   - Cümle 3: «Ama çubuk çok düzdü ve çiçekler hep aşağı kaydı.»
   - Açıklama: 'Hep' ile süreklilik anlatılıyor; 'hep aşağı kayıyordu' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama çubuk çok düzdü ve çiçekler hep aşağı kaydı"
   - Cümle 3: «Ama çubuk çok düzdü ve çiçekler hep aşağı kaydı.»
   - Açıklama: Çiçeklerin kaymasının sebebi çubuğun düz olması olarak veriliyor, bu akla yatkın bir sebep değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Uzun ve ince bir ot aldı"
   - Cümle 4: «Uzun ve ince bir ot aldı ve bir çiçeğin sapına sardı.»
   - Açıklama: Son özne 'çiçekler'; otu kimin aldığı belli değil.
   - Açıklama: Önceki cümlenin öznesi 'çiçekler' olduğu için otu kimin aldığı belli değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee çiçek bağlamayı öğrendi"
   - Cümle 6: «Çiçek artık kaymadı ve Pepee çiçek bağlamayı öğrendi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada ormanda yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0131` birebir aynı, ardından `@onarim: e578d12d4f12318fd4fc00e326857a6ca9faf3fb`, sonra gövde.

### Hikâye 6: tohum pepee-0132 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | park | Nenee
@tohum: pepee-0132
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'atkı', fiil 'süslemek', sıfat 'kaygan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Nenee
@plan: parkta nereden geldiği bilinmeyen güzel bir koku vardı | kokuyu tanıdı ve ağacın altında ninesini buldu
@tohum: pepee-0132
Bir sabah Pepee parkta kaydırakta oynuyordu. Birden çok güzel bir koku geldi. Pepee bu kokunun nereden geldiğini merak etti. Kaygan kaydıraktan aşağı kaydı ve havayı kokladı. Pepee kokuyu hemen tanıdı. Bu, kahvaltıda en sevdiği yumurtanın kokusuydu. Koku salıncakların arkasındaki büyük ağaçtan geliyordu. Pepee oraya yürüdü. Ağacın altında Nenee yere renkli atkısını sermişti. Atkının üstünde sıcak yumurta, bal ve tahin pekmez vardı. Nenee tabakları küçük çiçeklerle süslüyordu. Nenee Pepee'yi görünce güldü ve ona bir tabak uzattı. Pepee çok sevindi, çünkü o güzel kokuyu yapan sıcak yumurtaları bulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Birden çok güzel bir koku geldi"
   - Cümle 2: «Birden çok güzel bir koku geldi.»
   - Açıklama: 'Birden çok' yan yana gelince 'birçok' anlamına okunabiliyor; anlam belirsiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çok güzel bir koku geldi"
   - Cümle 2: «Birden çok güzel bir koku geldi.»
   - Açıklama: Güzel bir koku çocuğun çözmesi gereken bir sorun değil, yalnız bir merak.
   - Açıklama: Güzel bir koku sorun değil; çocuğun önemseyeceği bir sorun yok.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bal ve tahin pekmez"
   - Cümle 10: «Atkının üstünde sıcak yumurta, bal ve tahin pekmez vardı.»
   - Açıklama: Tamlama eki eksik; 'tahin pekmezi' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Nenee tabakları küçük çiçeklerle süslüyordu"
   - Cümle 11: «Nenee tabakları küçük çiçeklerle süslüyordu.»
   - Açıklama: Çiçekle süsleme olayda işlevsiz bir ayrıntı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o güzel kokuyu yapan"
   - Cümle 13: «Pepee çok sevindi, çünkü o güzel kokuyu yapan sıcak yumurtaları bulmuştu.»
   - Açıklama: Koku 'yapılmaz'; 'kokuyu çıkaran' olmalı.
   - Açıklama: Koku yapılmaz; 'kokuyu çıkaran' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0132` birebir aynı, ardından `@onarim: be3b006040996c837ea522d7e4361b7a1f3898e1`, sonra gövde.

### Hikâye 7: tohum pepee-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0133
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'uçurtma', fiil 'güzelleşmek', sıfat 'uslu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: uçurtmayı ilk kez uçuruyordu ve uçurtma hep düştü | dedesinden yardım istedi ve uçurmayı öğrendi
@tohum: pepee-0133
Pepee dedesiyle kumsala uçurtma uçurmaya gelmişti. Hava güzelleşmişti ve denizden hafif bir rüzgar esiyordu. Ama Pepee uçurtmayı ilk kez uçuruyordu ve uçurtma hep kuma düştü. Pepee dedesinin yanına koştu. "Dedeciğim, bana uçurtma uçurmayı öğretir misin?" diye sordu Pepee. "Sırtını rüzgara dön ve ipi yavaş yavaş bırak," dedi Dedee. Pepee uslu uslu dedesini dinledi. Sırtını rüzgara döndü ve ipi azar azar bıraktı. Uçurtma yükseldi ve gökyüzünde uçmaya başladı. Dedee gülümsedi ve ellerini çırptı. Pepee çok sevindi, çünkü artık uçurtma uçurmayı öğrenmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "uçurtma hep kuma düştü"
   - Cümle 3: «Ama Pepee uçurtmayı ilk kez uçuruyordu ve uçurtma hep kuma düştü.»
   - Açıklama: 'Hep' süreklilik bildirir ama fiil tek seferlik -dı ile çekimlenmiş; 'hep düşüyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0133` birebir aynı, ardından `@onarim: 6241121fed1137c92d03f424f21e2b501733b4a4`, sonra gövde.

### Hikâye 8: tohum pepee-0134 (deneme 1 -> 2)

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
Pepee ormanda bisikletle çiçeklerin arasında dolaşıyordu. Önünde bir sepet taşıyordu. Birden yağmur başladı ve damlalar Pepee'nin mavi şapkasına düştü. Pepee hiç ıslanmak istemedi. Hemen durdu ve sepetten kahvaltı örtüsünü çıkardı. Örtüyü başının üstüne tuttu. Sonra bir ağacın yanında sessizce bekledi. Yağmur örtünün üstüne tıp tıp damladı ama Pepee kuru kaldı. Az sonra yağmur dindi. Bulutların arasında sıcak güneş belirdi. Yapraklardaki damlalar farklı renklerde parlıyordu. Pepee çok sevindi, çünkü yağmurda hiç ıslanmamıştı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ormanda bisikletle çiçeklerin"
   - Cümle 1: «Pepee ormanda bisikletle çiçeklerin arasında dolaşıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee bir büyüğün yanında olmalı, burada ormanda yalnız bisiklet sürüyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sepetten kahvaltı örtüsünü çıkardı"
   - Cümle 5: «Hemen durdu ve sepetten kahvaltı örtüsünü çıkardı.»
   - Açıklama: Tohumdaki özellik kahvaltıyı sevmek; hikayede yalnız örtünün adı geçiyor, özellik işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0134` birebir aynı, `@degisim: scooter -> bisiklet` (tutuyorsan), ardından `@onarim: 7d344bd4bc5d08619b3c8f56bab81cfe76932ac8`, sonra gövde.

### Hikâye 9: tohum pepee-0135 (deneme 1 -> 2)

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
@plan: kelebekler hiç durmadığı için sayı karıştı | yumurta kabuğuna bal koydu ve kelebekleri saydı
@tohum: pepee-0135
Kuşlar ötüyordu ve Pepee ağacın altında sağlıklı bir kahvaltı yapıyordu. Birden çiçeklerin üstünde uçan kelebekleri gördü ve saymak istedi. Ama kelebekler hiç durmuyordu ve Pepee sayıyı hep karıştırdı. Pepee yumurtanın kabuğundan küçük bir kap yaptı. Kabuğun içine tabağındaki baldan biraz koydu. Sonra onu çiçeklerin arasına bıraktı ve biraz uzağa oturdu. Az sonra kelebekler bala kondu ve kanatlarını yavaşça açıp kapadı. Pepee onları tek tek saydı. Tam beş tane vardı. Pepee çok sevindi, çünkü sonunda bütün kelebekleri saymıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sağlıklı bir kahvaltı yapıyordu"
   - Cümle 1: «Kuşlar ötüyordu ve Pepee ağacın altında sağlıklı bir kahvaltı yapıyordu.»
   - Açıklama: 'Sağlıklı' soyut bir kavram, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağacın altında sağlıklı bir kahvaltı"
   - Cümle 1: «Kuşlar ötüyordu ve Pepee ağacın altında sağlıklı bir kahvaltı yapıyordu.»
   - Açıklama: 'Sağlıklı' 3 yaşındaki bir çocuk için soyut bir kavram.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Az sonra kelebekler bala kondu"
   - Cümle 7: «Az sonra kelebekler bala kondu ve kanatlarını yavaşça açıp kapadı.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmayıp çözüme katılıyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kelebekler bala kondu"
   - Cümle 7: «Az sonra kelebekler bala kondu ve kanatlarını yavaşça açıp kapadı.»
   - Açıklama: Arka planda kalması gereken çoğul canlı kelebekler yeme gelip sayılarak olayın çözümüne katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0135` birebir aynı, ardından `@onarim: bcd042977bd8092adce5310842d502875a71004f`, sonra gövde.
