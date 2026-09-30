# Editör görevi (onarım): Pepee, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0126 (deneme 4 -> 5)

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
Bir sabah Pepee ormanda kaşıkla yumurta taşıma oyunu oynuyordu. Yanında kahvaltı için getirdiği bir sepet vardı. Yumurtayı iki ağaca bağladığı kırmızı ipliğe kadar taşıyacaktı. Ama yuvarlak yumurta kaşıkta durmadı ve çimlere yuvarlandı. Pepee yumurtayı yerden aldı ama yumurta yine düştü. Sonra kahvaltı sepetini açtı. İçinde bal ve biberli peynir vardı. Pepee kaşığa biraz bal sürdü ve yumurtayı üstüne koydu. Yumurta bala yapıştı ve artık kaymadı. Pepee yavaş yavaş yürüdü ve yumurta hiç düşmedi. Sonunda kırmızı ipliğe vardı. Oyun bitince ağacın altına oturdu ve yumurtayı biberli peynirle mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee ormanda"
   - Cümle 1: «Bir sabah Pepee ormanda kaşıkla yumurta taşıma oyunu oynuyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama ormanda tek başına yeni bir yol deniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama yuvarlak yumurta kaşıkta durmadı"
   - Cümle 4: «Ama yuvarlak yumurta kaşıkta durmadı ve çimlere yuvarlandı.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0126` birebir aynı, `@degisim: kapanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 0c42dd68ce6966a8d5088e89adb633a093438cd0`, sonra gövde.

### Hikâye 2: tohum pepee-0128 (deneme 4 -> 5)

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
Bir sabah Pepee ile Bebee deniz kıyısında bir battaniyenin üstünde oturuyordu. Pepee kumdan kuleler yapmak istedi. Ama kum çok kuruydu ve kuleler çabuk dağıldı. Pepee kahvaltıda yumurtasını yediği küçük kabı hatırladı. Kabı battaniyeden aldı ve dalgaların ıslattığı kumla doldurdu. Sonra kabı ters çevirdi ve yavaşça kaldırdı. Kumda yumurta gibi yuvarlak bir kule duruyordu. "Bak, Bebee, bu kule dağılmadı!" dedi Pepee. "Ben de yapmak istiyorum!" dedi Bebee. Pepee kabı ona verdi ve Bebee de bir kule yaptı. Pepee çok sevindi, çünkü kumdan sağlam bir kule yapmıştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee ile Bebee deniz kıyısında"
   - Cümle 1: «Bir sabah Pepee ile Bebee deniz kıyısında bir battaniyenin üstünde oturuyordu.»
   - Açıklama: Pepee ve bebek kardeşi deniz kıyısında yanlarında hiçbir büyük olmadan yalnız bulunuyor; kartın güvenli kullanım satırı büyüğün yanında olmayı ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0128` birebir aynı, `@degisim: satmak -> doldurmak` (tutuyorsan), ardından `@onarim: 61a2038f2ae5b04c624f4d3efc1ef54f95ade6bf`, sonra gövde.

### Hikâye 3: tohum pepee-0129 (deneme 4 -> 5)

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
@plan: yakında bir şey homurdanıyordu ama görünmüyordu | dans ederek dolaştı ve sesin kendi karnından geldiğini buldu
@tohum: pepee-0129
@degisim: memnun -> mutlu
Deniz kıyısında küçük dalgalar kuma vuruyordu. Pepee annesiyle kumda otururken yakında bir ses duydu. Bir şey homurdanıyordu, ama ne olduğu görünmüyordu. "Anneciğim, bu ses nereden geliyor?" diye sordu Pepee. "Bilmiyorum, sen bul bakalım," dedi Annee. Ses, annesinin çantasının yanından geliyor gibiydi. Pepee kalktı ve dans ederek çantadan uzaklaştı. Sağa dans edince ses de sağa, sola dans edince sola gitti. Pepee durdu ve elini karnına koydu. "Anne, homurdanan benim karnım!" dedi Pepee ve güldü. Annee de güldü ve çantadan bir kap salata çıkardı. Sonra ikisi salatayı mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Bir şey homurdanıyordu, ama ne olduğu görünmüyordu"
   - Cümle 3: «Bir şey homurdanıyordu, ama ne olduğu görünmüyordu.»
   - Açıklama: Görünmeyen, homurdanan bilinmeyen bir şey küçük çocuk için korkutucu bir öğe olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0129` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: bd97dd8926fda5b61f8bc90efb8c870b860727e2`, sonra gövde.

### Hikâye 4: tohum pepee-0130 (deneme 4 -> 5)

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
@plan: çiçekler şapkada durmadı ve hep kaydı | çiçekleri birbirine bağlamayı öğrendi ve halka yaptı
@tohum: pepee-0130
@degisim: düşünceli -> kırmızı
Pepee ormanda kırmızı çiçekler ve küçük çilekler topluyordu. Mavi şapkasını onlarla süslemek istedi. Ama çiçekler şapkadan hep kaydı, çünkü sapları çok kısaydı. Pepee bir çiçeği başka bir çiçeğe sardı. İlk seferde olmadı ve çiçek yere düştü. Pepee bir daha sardı ve bu işi öğrendi. Sonra bütün çiçekleri tek tek birbirine bağladı. Böylece uzun bir çiçek halkası yaptı. Pepee halkayı şapkasının çevresine taktı. Çilekleri de çiçeklerin arasına sıkıştırdı. Pepee başını salladı ama hiçbiri düşmedi. Sonra çiçekli şapkasıyla ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ormanda kırmızı çiçekler ve küçük çilekler topluyordu"
   - Cümle 1: «Pepee ormanda kırmızı çiçekler ve küçük çilekler topluyordu.»
   - Açıklama: Pepee ormanda büyük olmadan yabani çilek topluyor ve yeni şey deniyor; kartın güvenli kullanım satırına aykırı ve taklit edilince tehlikeli.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ormanda kırmızı çiçekler ve küçük çilekler topluyordu"
   - Cümle 1: «Pepee ormanda kırmızı çiçekler ve küçük çilekler topluyordu.»
   - Açıklama: Ormanda yalnız başına yabani çilek toplamak taklit edilince tehlikelidir ve güvenli kullanım satırındaki büyüğün yanında deneme kuralına uymaz.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çünkü sapları çok kısaydı"
   - Cümle 3: «Ama çiçekler şapkadan hep kaydı, çünkü sapları çok kısaydı.»
   - Açıklama: Sapları çok kısa denen çiçekler sonra birbirine sarılıp bağlanarak uzun bir halka yapılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0130` birebir aynı, `@degisim: düşünceli -> kırmızı` (tutuyorsan), ardından `@onarim: 26d77c1c7d548b2fccb9d40ea10e0a04f56227f7`, sonra gövde.

### Hikâye 5: tohum pepee-0131 (deneme 2 -> 3)

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
@plan: çiçekleri tutan bir şey yoktu ve çiçekler düştü | otla çiçekleri çubuğa bağlamayı öğrendi
@tohum: pepee-0131
Pepee ormanda kuzeni Şila için bir sürpriz hazırlıyordu. Şila dans edecekti ve Pepee bir çubuğu çiçeklerle güzelleştirmek istedi. Ama çiçekler çubukta durmadı, çünkü onları tutan bir şey yoktu. Pepee uzun ve ince bir ot buldu. Otu bir çiçeğin sapına ve çubuğa sıkıca sardı. Çiçek artık düşmedi ve Pepee otla çiçek bağlamayı öğrendi. Öbür çiçekleri de aynı biçimde bağladı. Az sonra Şila ağaçların arasından geldi. "Sürpriz, Şila, bu çubuk senin dansın için!" dedi Pepee. "Bu harika bir çubuk, teşekkürler, Pepee!" dedi Şila. Sonra Şila çubukla dans etti ve Pepee mutlu mutlu el çırptı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çiçekleri tutan bir şey yoktu ve çiçekler düştü"
   - Cümle 0 (plan satırı): «çiçekleri tutan bir şey yoktu ve çiçekler düştü | otla çiçekleri çubuğa bağlamayı öğrendi»
   - Açıklama: Gövde sebebi bağlayıcı eksikliği olarak değil taşların rengi olarak veriyor, plan gövdeyle örtüşmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0131` birebir aynı, ardından `@onarim: 0e2aab399833243243232344b8307cf4a264f151`, sonra gövde.

### Hikâye 6: tohum pepee-0134 (deneme 4 -> 5)

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
@plan: yağmur birden başladı ve ıslanmak istemedi | kahvaltı örtüsünü başının üstüne tuttu ve kuru kaldı
@tohum: pepee-0134
@degisim: scooter -> bisiklet
Pepee ormanda kahvaltı yapmak için bisikletini itiyordu. Bisikletin sepetinde yumurta, bal ve bir kahvaltı örtüsü vardı. Birden yağmur başladı. Pepee hiç ıslanmak istemedi. Hemen durdu ve örtüyü sepetten çıkardı. Örtüyü başının üstüne tuttu. Sonra bir ağacın yanında sessizce bekledi. Yağmur örtünün üstüne tıp tıp damladı ama Pepee kuru kaldı. Az sonra yağmur dindi. Bulutların arasından sıcak güneş belirdi. Pepee ağacın altına oturdu ve yumurtayla balı yedi. Pepee çok sevindi, çünkü örtüyü farklı bir iş için kullanmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yağmur birden başladı ve ıslanmak istemedi"
   - Cümle 0 (plan satırı): «yağmur birden başladı ve ıslanmak istemedi | kahvaltı örtüsünü başının üstüne tuttu ve kuru kaldı»
   - Açıklama: Plan cümlesinde ikinci yüklemin öznesi de 'yağmur' gibi okunuyor; özne eksik ve uyum bozuk.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ormanda kahvaltı yapmak için bisikletini itiyordu"
   - Cümle 1: «Pepee ormanda kahvaltı yapmak için bisikletini itiyordu.»
   - Açıklama: Dört yaşındaki Pepee büyük olmadan tek başına ormana gidiyor; güvenli kullanım satırı yeni şeyleri bir büyüğün yanında denemesini ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0134` birebir aynı, `@degisim: scooter -> bisiklet` (tutuyorsan), ardından `@onarim: e07389ef1bdf1539c0bee2df7755249f9e5178f1`, sonra gövde.

### Hikâye 7: tohum pepee-0136 (deneme 3 -> 4)

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
@plan: annenin tabağı boştu, çünkü evde yumurta kalmamıştı | kendi yumurtasını ikiye bölüp annesiyle paylaştı
@tohum: pepee-0136
@degisim: bot -> tabak
Bir sabah Pepee ile Annee mutfakta masaya oturdu. Pepee'nin tabağında bir yumurta vardı. Ama Annee'nin yeşil tabağı boştu, çünkü evde başka yumurta yoktu. Pepee annesinin boş tabağına baktı. Kahvaltısındaki yumurtayı çatalıyla dikkatle ikiye böldü. Büyük parçayı annesinin tabağına koydu. Artık iki tabakta da birer parça yumurta vardı. Annee önce çok şaşırdı. Sonra Pepee'ye sarıldı ve onu öptü. İkisi yumurtayı yan yana yedi. Annee çok sevindi, çünkü Pepee en çok sevdiği yiyeceği onunla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en çok sevdiği yiyeceği"
   - Cümle 11: «Annee çok sevindi, çünkü Pepee en çok sevdiği yiyeceği onunla paylaşmıştı.»
   - Açıklama: Yiyeceği en çok kimin sevdiği, Pepee mi Annee mi, belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0136` birebir aynı, `@degisim: bot -> tabak` (tutuyorsan), ardından `@onarim: a481ee543c54f227c2ed6c20c0020d76ee304acd`, sonra gövde.

### Hikâye 8: tohum pepee-0137 (deneme 3 -> 4)

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
@plan: kolları aşağıda olunca tek ayakla hep bir yana eğildi | kollarını iki yana açıp yeniden hopladı
@tohum: pepee-0137
@degisim: nefis -> tatlı
Deniz kıyısında Pepee'nin bisikleti kumun kenarında duruyordu. Bisikletin sepetinde tatlı bir dilim karpuz vardı. Pepee sudan uzakta, bisiklete kadar tek ayakla hoplamak istedi. Ama kolları aşağıdaydı ve bu yüzden hep bir yana eğildi. Öbür ayağı da her seferinde kuma değdi. Pepee biraz düşündü. Dans ederken kollarını iki yana açtığını hatırladı. Kollarını yine öyle açtı ve tek ayakla hopladı. Bu kez öbür ayağı kuma hiç değmedi. Pepee küçük küçük zıpladı ve bisiklete kadar gitti. Sonra bisikletin yanına oturdu ve karpuzunu yedi. Pepee çok sevindi, çünkü ilk kez tek ayakla oraya varmıştı.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Pepee'nin bisikleti kumun kenarında duruyordu"
   - Cümle 1: «Deniz kıyısında Pepee'nin bisikleti kumun kenarında duruyordu.»
   - Açıklama: Kartta Pepee'ye ait bir bisiklet eşyası yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bisiklete kadar tek ayakla hoplamak istedi"
   - Cümle 3: «Pepee sudan uzakta, bisiklete kadar tek ayakla hoplamak istedi.»
   - Açıklama: Pepee deniz kıyısında yanında bir büyük olmadan yeni bir şey deniyor; güvenli özellik kullanımı satırı yeni şeylerin bir büyüğün yanında denenmesini ister.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kolları aşağıdaydı ve bu yüzden hep bir yana eğildi"
   - Cümle 4: «Ama kolları aşağıdaydı ve bu yüzden hep bir yana eğildi.»
   - Açıklama: Cümlede özne 'kolları' olduğu için eğilen kollar gibi okunuyor; fiil kastedilen özneye uymuyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kolları aşağıdaydı ve bu yüzden hep bir yana eğildi"
   - Cümle 4: «Ama kolları aşağıdaydı ve bu yüzden hep bir yana eğildi.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0137` birebir aynı, `@degisim: nefis -> tatlı` (tutuyorsan), ardından `@onarim: 60c85f3c22ed5de2590e0ec9cf99a2956734b1a8`, sonra gövde.

### Hikâye 9: tohum pepee-0138 (deneme 3 -> 4)

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
Deniz kıyısında Şila kumda oturmuş, kovasıyla bir kale yapıyordu. Pepee de onun yanında deniz kabukları topluyordu. Ama kale suya çok yakındı ve küçük dalgalar dibini dağıttı. Şila üzüldü. Pepee ona yardım etmek istedi. Önce kumda durdu ve dalgaları uzaktan izledi. Dalgaların yalnız ıslak kuma kadar geldiğini öğrendi. Pepee kovayı kuru kumla doldurdu ve ters çevirdi. Dalgalardan uzakta yeni ve büyük bir kale çıktı. Şila da kalenin tepesini Pepee'nin kabuklarıyla örttü. Dalgalar yine geldi ama yeni kaleye hiç değmedi. Şila sevinçle ellerini çırptı. Pepee bundan sonra kaleleri hep kuru kumda yaptı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Dalgaların yalnız ıslak kuma"
   - Cümle 7: «Dalgaların yalnız ıslak kuma kadar geldiğini öğrendi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yanında büyük yokken öğreniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0138` birebir aynı, `@degisim: mısır -> kova` (tutuyorsan), ardından `@onarim: 8a38190573edd6bb4c0f38fb353e853b288c6da0`, sonra gövde.

### Hikâye 10: tohum pepee-0139 (deneme 3 -> 4)

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
Yağmur yeni dinmişti. Pepee ile Dedee ormanda sırayla önden yürüme oyunu oynuyordu. Sıra Pepee'deydi ama tabela çamurla kaplıydı. Pepee tabeladaki okun yolu gösterdiğini dedesinden öğrenmişti. Çamurdan oku göremedi ve nereye gideceğini bilemedi. "Dede, bana biraz su verir misin?" diye sordu Pepee. Dedee su şişesini hemen ona verdi. Pepee suyla tabelayı güzelce yıkadı. Çamurun altından siyah bir ok çıktı. Pepee okun gösterdiği tarafa önden yürüdü. Dedee de gülerek arkasından geldi. "Aferin, Pepee, yolu sen buldun!" dedi Dedee. Pepee bundan sonra çamurlu bir tabela görünce onu hep suyla temizledi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee tabeladaki okun yolu gösterdiğini dedesinden öğrenmişti"
   - Cümle 4: «Pepee tabeladaki okun yolu gösterdiğini dedesinden öğrenmişti.»
   - Açıklama: Tohumdaki öğrenme özelliği yalnız geçmişte olmuş bir bilgi olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0139` birebir aynı, ardından `@onarim: d48869bb4cc947f7e2d97762298e495c447db148`, sonra gövde.

### Hikâye 11: tohum pepee-0141 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Nenee
@tohum: pepee-0141
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yağmur ya da kar günü
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çömlek', fiil 'bindirmek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Nenee
@plan: yağmur yağdı ve salıncak oyunu bozuldu | şemsiye isteyip altında dans etti
@tohum: pepee-0141
@degisim: çömlek -> şemsiye
Parkta hafif bir yağmur başladı. Nenee Pepee'yi ahşap salıncağa bindirmek istiyordu. Ama salıncak yağmurdan ıslanmıştı. "Salıncak ıslak, şimdi ne oynayalım?" dedi Nenee üzgün bir sesle. "Nenee, çantanda şemsiye var mı?" diye sordu Pepee. Nenee çantasından büyük bir şemsiye çıkardı. İkisi şemsiyenin altına girdi. Damlalar şemsiyeye tık tık vurdu. Pepee bu sesle dans etmeye başladı. Bir sağa, bir sola zıpladı ve ellerini çırptı. "Nenee, sen de gel!" dedi Pepee. Nenee çok güldü ve Pepee'nin elini tuttu. İkisi el ele yavaşça döndü. "Pepee, bu yağmur oyunu salıncaktan da güzel!" dedi Nenee.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi şemsiyenin altına girdi"
   - Cümle 7: «İkisi şemsiyenin altına girdi.»
   - Açıklama: Çözüm ıslak salıncağa yönelmiyor, salıncak oyunu yerine başka bir oyun konuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0141` birebir aynı, `@degisim: çömlek -> şemsiye` (tutuyorsan), ardından `@onarim: b9d10686070d2c20efc8dce265b9e4caee227f8d`, sonra gövde.

### Hikâye 12: tohum pepee-0142 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0142
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'fincan', fiil 'tatmak', sıfat 'üzgün'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: fincanı olmadığı için kumdan kulesi yıkıldı | kuzeninden kule yapmayı öğrendi ve kendisi denedi
@tohum: pepee-0142
@degisim: tatmak -> doldurmak
Pepee ile kuzeni Şila sudan uzakta kumdan kule yapıyordu. Şila küçük bir fincanla güzel kuleler yaptı. Ama Pepee'nin fincanı yoktu, elle yaptığı kule hemen yıkıldı. Pepee yıkılan kuleye üzgün üzgün baktı. "Şila, ben de kule yapmayı öğrenmek istiyorum," dedi Pepee. "Tabii, fincanı seninle paylaşırım," dedi Şila. Şila fincanı kumla doldurdu, sıkıca bastırdı ve ters çevirdi. Pepee Şila'yı dikkatle izledi. Sonra fincanı aldı ve aynısını yaptı. Pepee fincanı kaldırdı ve kum yıkılmadı. Kumda küçük, yuvarlak bir kule duruyordu. Pepee sevinçle ellerini çırptı. Pepee ile Şila fincanı sırayla kullandı ve mutlu mutlu yeni kuleler yaptı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ile kuzeni Şila sudan uzakta kumdan kule yapıyordu"
   - Cümle 1: «Pepee ile kuzeni Şila sudan uzakta kumdan kule yapıyordu.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına aykırı olarak iki küçük çocuk deniz kıyısında büyük olmadan yeni bir şey deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0142` birebir aynı, `@degisim: tatmak -> doldurmak` (tutuyorsan), ardından `@onarim: 2106b644fc21c303e979769ee123eb8943414d48`, sonra gövde.
