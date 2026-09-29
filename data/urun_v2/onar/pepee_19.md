# Editör görevi (onarım): Pepee, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0068 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0068
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çan', fiil 'sıralamak', sıfat 'somurtkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kuru kum kovadan çıkınca dağıldı | kovayı ıslak kumla doldurup kale yaptı
@tohum: pepee-0068
@degisim: çan -> kova
Deniz kıyısında serin bir rüzgar esiyordu. Pepee kovayla kumdan bir kale yapıyordu. Ama kuru kum kovadan çıkınca hemen dağıldı. Pepee üzüldü ve yüzü somurtkan oldu. "Ne oldu, Pepee?" diye sordu Şila. "Kum hep dağılıyor," dedi Pepee. Pepee sonra su kenarına baktı. Oradaki ıslak kumda Şila'nın ayak izleri duruyordu. Pepee kovayı ıslak kumla doldurdu ve ters çevirdi. Bu kez güzel bir kale çıktı. Şila küçük taşlar getirdi. Pepee taşları kalenin üstüne tek tek sıraladı. "Ne güzel bir kale, Pepee!" dedi Şila. Pepee o gün kaleyi ıslak kumla yapmayı öğrendi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve yüzü somurtkan oldu"
   - Cümle 4: «Pepee üzüldü ve yüzü somurtkan oldu.»
   - Açıklama: 'Somurtkan' 3 yaşındaki çocuğun bilmeyeceği bir kelime ve 'yüzü somurtkan oldu' kuruluşu doğal değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0068` birebir aynı, `@degisim: çan -> kova` (tutuyorsan), ardından `@onarim: f85ebd8681c3745932256bd35eb57a90995181af`, sonra gövde.

### Hikâye 2: tohum pepee-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0070
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'ayakkabı', fiil 'yaklaşmak', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: küçük dalgalar örtüye yaklaştı | örtüyü ayakkabının yanındaki kuru kuma taşıdı
@tohum: pepee-0070
Güneş parlıyordu ve deniz ışıltılıydı. Pepee su kenarında dedesine sürpriz bir kahvaltı hazırlıyordu. Ama küçük dalgalar gelip örtüye yaklaştı. Örtünün ucu ıslandı. Pepee etrafına baktı. Dedee yakında, kuru kumda gözleri kapalı bekliyordu. Ayakkabısı da yanında duruyordu. Pepee örtüyü ve her şeyi oraya taşıdı. Balı, yumurtayı ve ekmeği ayakkabının yanına koydu. Dalgalar artık oraya gelemedi. Sonra Dedee gözlerini açtı. Sürprizi görünce güldü ve Pepee'ye sarıldı. İkisi kumda oturup balı ve yumurtayı paylaştı. Pepee bundan sonra sofrayı hep kuru kumda kurdu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ayakkabısı da yanında duruyordu"
   - Cümle 7: «Ayakkabısı da yanında duruyordu.»
   - Açıklama: Ayakkabının ve 'yanında' zamirinin kimi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ayakkabısı da yanında duruyordu"
   - Cümle 7: «Ayakkabısı da yanında duruyordu.»
   - Açıklama: Ayakkabı sebepsiz kuruluyor ve yalnız yer işareti olarak geçiyor, olayda işlevi yok.
   - Açıklama: Ayakkabı işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok, yiyecekler yalnızca yanına konuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0070` birebir aynı, ardından `@onarim: 72bfa6a0a2c2d463d38864a9c2d463f98930a67c`, sonra gövde.

### Hikâye 3: tohum pepee-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0072
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: sırayla oynamak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'yoğurt', fiil 'çalışmak', sıfat 'ilginç'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: sesle dans etmek istedi ama yapamadı | annesiyle sırayla kaba vurdular
@tohum: pepee-0072
Dışarıdan yağmur sesi geliyordu. Pepee evde boş bir yoğurt kabına kaşıkla vurunca ilginç bir ses çıktı. Bu sesle dans etmeye çalıştı ama iki işi birden yapamadı. "Anne, sırayla oynayalım mı?" diye sordu Pepee. "Olur, önce ben çalarım," dedi Annee. Annee kaşıkla kaba vurdu. Pepee bu sese göre döndü ve zıpladı. Sonra sıra Pepee'ye geldi. Pepee kaba vurdu, Annee de kollarını açıp döndü. "Çok güzel, anne!" dedi Pepee. "Şimdi dönme sırası sende, Pepee," dedi Annee. Pepee ile Annee sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Pepee evde boş bir yoğurt kabına kaşıkla vurunca ilginç bir ses çıktı"
   - Cümle 2: «Pepee evde boş bir yoğurt kabına kaşıkla vurunca ilginç bir ses çıktı.»
   - Açıklama: 'Pepee' öznesi ana cümlenin yüklemi 'çıktı' ile uyumsuz; özne kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0072` birebir aynı, ardından `@onarim: 63bf7dcf84dc921b16062a6fdc5eee02dac4b631`, sonra gövde.

### Hikâye 4: tohum pepee-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0073
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çekirdek', fiil 'eğlenmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: oynayacakları yer kuru dallarla doluydu | dalları kenara taşıyıp çiçekler koydu
@tohum: pepee-0073
@degisim: çekirdek -> çiçek
Pepee ormanda kardeşi Bebee için bir sürpriz hazırlıyordu. Bebee bir ağacın arkasında gözlerini kapatıp bekliyordu. Ama oynayacakları yer kuru dallarla doluydu ve güvenli değildi. Pepee dalları tek tek topladı ve kenara taşıdı. Yerde yumuşak çimenler kaldı. Pepee yakındaki renkli çiçeklerden birkaç tane kopardı. Onları çimenlerin etrafına koydu. "Şimdi gözlerini aç, Bebee!" dedi Pepee. Bebee gözlerini açtı ve çiçekleri gördü. "Ne güzel bir yer!" dedi Bebee. Pepee kardeşinin elini tuttu ve ikisi çimenlerde dans etti. Döndüler, zıpladılar ve çok eğlendiler. Pepee çok mutluydu, çünkü sürprizi kardeşini sevindirmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve güvenli değildi"
   - Cümle 3: «Ama oynayacakları yer kuru dallarla doluydu ve güvenli değildi.»
   - Açıklama: 'Güvenli' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee yakındaki renkli çiçeklerden birkaç tane kopardı"
   - Cümle 6: «Pepee yakındaki renkli çiçeklerden birkaç tane kopardı.»
   - Açıklama: Dallar kaldırılınca sorun çözülmüşken çiçek koparıp dizmek sebebe yönelmeyen ek adımlar olarak çözümü uzatıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ikisi çimenlerde dans etti"
   - Cümle 11: «Pepee kardeşinin elini tuttu ve ikisi çimenlerde dans etti.»
   - Açıklama: Tohumdaki dans özelliği sorunun çözümünde işe yaramıyor, yalnız sonda süs olarak geçiyor.
   - Açıklama: Tohumdaki dans özelliği sorunu çözmeye yaramıyor, yalnız kutlama olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0073` birebir aynı, `@degisim: çekirdek -> çiçek` (tutuyorsan), ardından `@onarim: 28fc8d5b646f414b0439246149495872828448b8`, sonra gövde.

### Hikâye 5: tohum pepee-0074 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0074
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'bant', fiil 'yumuşamak', sıfat 'şapkalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: tek bir bant vardı ve ikisi aynı anda istedi | sırayla yapıştırmayı önerdi ve resmi birlikte bitirdiler
@tohum: pepee-0074
@degisim: yumuşamak -> yapıştırmak
Pepee ile Nenee ormanda bir kağıda yapraklardan şapkalı bir mantar yapıyordu. Pepee yapraklarla resim yapmayı yeni öğreniyordu. Ama tek bir bant vardı ve ikisi de aynı anda banda uzandı. İkisi bandı birden çekti ve hiçbir yaprak yapışmadı. Pepee biraz düşündü. "Nenee, sırayla yapıştıralım mı? Önce sen, sonra ben," dedi Pepee. "Tamam, önce ben," dedi Nenee ve güldü. Nenee kağıda büyük sarı bir yaprak koydu. Sonra bandı Pepee'ye verdi. Pepee küçük kırmızı bir yaprağı mantarın başına şapka gibi yapıştırdı. Sırayla çalışınca mantar çabucak bitti. Pepee ile Nenee bitmiş resme bakıp sevinçle birbirine sarıldı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee yapraklarla resim yapmayı yeni öğreniyordu"
   - Cümle 2: «Pepee yapraklarla resim yapmayı yeni öğreniyordu.»
   - Açıklama: Tohumdaki öğrenme özelliği yalnız anılıyor, sorunun çözümünde (sırayla yapıştırma) işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee yapraklarla resim yapmayı yeni öğreniyordu"
   - Cümle 2: «Pepee yapraklarla resim yapmayı yeni öğreniyordu.»
   - Açıklama: Pepee'nin yeni öğrendiği bilgisi olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0074` birebir aynı, `@degisim: yumuşamak -> yapıştırmak` (tutuyorsan), ardından `@onarim: 83fbd15784b46e97ac9ad4c5a7c2593e039e5bf6`, sonra gövde.

### Hikâye 6: tohum pepee-0076 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0076
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'baston', fiil 'silmek', sıfat 'mutsuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kuzeninin şapkası ıslak kuma düştü | şapkayı elindeki mendille yavaşça sildi
@tohum: pepee-0076
@degisim: baston -> şapka
Güneş sıcaktı ve dalgalar kıyıya vuruyordu. Pepee bir mendil sallayarak Şila ile dans ediyordu. Ama Şila hızlı dönünce şapkası ıslak kuma düştü. Şila mutsuz oldu, çünkü şapkasının her yerine kum bulaşmıştı. "Pepee, şapkam çok kirlendi," dedi Şila. "Dur, Şila, bana ver," dedi Pepee. Pepee şapkayı elindeki mendille yavaşça sildi. Şapkanın üstünde hiç kum kalmadı. Şila şapkasını taktı ve gülümsedi. İkisi dalgaların yanında mutlu mutlu zıpladı. "Teşekkürler, Pepee, sen çok iyi bir kuzensin!" dedi Şila.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şila ile dans ediyordu"
   - Cümle 2: «Pepee bir mendil sallayarak Şila ile dans ediyordu.»
   - Açıklama: Tohumdaki dans özelliği yalnız sorunu başlatan arka planda kalıyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0076` birebir aynı, `@degisim: baston -> şapka` (tutuyorsan), ardından `@onarim: a67cd86d680fccd3634586d0edbbfc66d139286c`, sonra gövde.

### Hikâye 7: tohum pepee-0077 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0077
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kızartma', fiil 'yeşermek', sıfat 'yeterli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: dedenin kutusu boştu çünkü yemeğini evde unutmuştu | kızartmaları saydı ve yarısını dedesine verdi
@tohum: pepee-0077
Bir bahar sabahı Pepee ile Dedee ormanda piknik yapıyordu. Pepee'nin kutusunda sıcak patates kızartması vardı. Ama Dedee'nin kutusu boştu, çünkü yemeğini evde unutmuştu. Dedee'nin karnı acıkmıştı. Pepee saymayı yeni öğrenmişti ve kızartmaları dikkatle saydı. Tam on tane vardı. Pepee beş tanesini Dedee'nin kutusuna koydu. "Dedeciğim, bu kızartma ikimiz için yeterli," dedi Pepee. Dedee çok sevindi ve Pepee'ye sarıldı. İkisi yeni yeşermiş ağaçların altında yemeklerini yedi. "Çok teşekkürler, Pepee, bu en güzel piknik!" dedi Dedee.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni yeşermiş ağaçların altında"
   - Cümle 10: «İkisi yeni yeşermiş ağaçların altında yemeklerini yedi.»
   - Açıklama: 'Yeşermiş' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0077` birebir aynı, ardından `@onarim: 8d64a0001c5a663d0b66a7825b50494808f21d78`, sonra gövde.

### Hikâye 8: tohum pepee-0078 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0078
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'minder', fiil 'savurmak', sıfat 'yapraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yapraklar küçük elinden hemen yere düştü | şapkasını yaprakla doldurup yaprakları havaya savurdu
@tohum: pepee-0078
@degisim: minder -> şapka
Ormanda yere bir sürü sarı yaprak düşmüştü. Pepee yaprakları havaya atıp kendi üstüne yağdırmak istedi. Ama küçük eline iki üç yaprak sığdı ve hepsi hemen düştü. Pepee durdu ve biraz düşündü. Sonra mavi şapkasını çıkardı ve onu yapraklarla doldurdu. Yaprakları şapkadan havaya doğru savurdu. Sarı yapraklar yağmur gibi başına döküldü. Pepee sevinçle zıpladı ve şapkayı yine doldurdu. Yapraklar bu sefer daha yükseğe uçtu. Sonunda Pepee'nin mavi tulumu yapraklı olmuştu. Pepee çok mutluydu, çünkü yaprakları şapkayla uçurmayı kendisi öğrenmişti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yapraklar yağmur gibi başına döküldü"
   - Cümle 7: «Sarı yapraklar yağmur gibi başına döküldü.»
   - Açıklama: Benzetme ('yağmur gibi') mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yapraklar yağmur gibi başına"
   - Cümle 7: «Sarı yapraklar yağmur gibi başına döküldü.»
   - Açıklama: 'Yağmur gibi' benzetmesi mecazlı bir anlatım.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mavi tulumu yapraklı olmuştu"
   - Cümle 10: «Sonunda Pepee'nin mavi tulumu yapraklı olmuştu.»
   - Açıklama: 'Yapraklı olmak' tuluma uymuyor; 'yapraklarla kaplanmıştı' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tulumu yapraklı olmuştu"
   - Cümle 10: «Sonunda Pepee'nin mavi tulumu yapraklı olmuştu.»
   - Açıklama: 'Yapraklı olmak' tulum için doğru anlamda değil; 'yaprakla kaplanmıştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0078` birebir aynı, `@degisim: minder -> şapka` (tutuyorsan), ardından `@onarim: cca3678afdd9e62c4ce0ad0831e79746395b39e8`, sonra gövde.

### Hikâye 9: tohum pepee-0080 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Bebee
@tohum: pepee-0080
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'şerit', fiil 'kurtulmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Bebee
@plan: her adımda arkasından garip bir ses geldi | zıplayıp sesi dinledi ve arkasındaki şeridi çıkardı
@tohum: pepee-0080
Bir sabah Pepee ile Bebee parkta oynuyordu. Pepee kaydıraktan indi ve dans etmeye başladı. Ama her adımda arkasından hışır hışır bir ses geliyordu. Pepee durunca ses de duruyordu. Pepee bu sesi çok merak etti. Bir kez daha zıpladı ve ses geri geldi. Bebee, Pepee'nin arkasına baktı ve eliyle gösterdi. Yerdeki plastik bir şerit Pepee'nin tulumuna takılmıştı. Pepee şeridi çekip çıkardı ve sesten kurtuldu. Sonra şeridi çöpe attı. Yine zıpladı ve bu kez hiç ses gelmedi. Pepee ile Bebee çok sevindi, çünkü garip sesi yapan şeyi bulmuşlardı.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bebee, Pepee'nin arkasına baktı ve eliyle gösterdi"
   - Cümle 7: «Bebee, Pepee'nin arkasına baktı ve eliyle gösterdi.»
   - Açıklama: Sesin sebebini Pepee değil Bebee buluyor; Pepee yalnız şeridi çekiyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Pepee'nin arkasına baktı ve eliyle gösterdi"
   - Cümle 7: «Bebee, Pepee'nin arkasına baktı ve eliyle gösterdi.»
   - Açıklama: Sesin sebebini Pepee değil Bebee buluyor; figür yardım istemeden çözümün anahtarını yan karakter veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0080` birebir aynı, ardından `@onarim: 3ccdc12aab72c3cbbd4337c7cb76f67350cc3266`, sonra gövde.

### Hikâye 10: tohum pepee-0081 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0081
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kızak', fiil 'güneşlenmek', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: yerde hareket eden siyah bir şekil gördü | dans etti ve şeklin kendi gölgesi olduğunu buldu
@tohum: pepee-0081
@degisim: kızak -> gölge
Parkta güneş parlıyordu. Pepee bir bankta oturmuş güneşleniyordu. Birden bankın yanında, yerde hareket eden siyah bir şekil gördü. Pepee bu şekli çok merak etti. Pepee aceleci davranmadı ve bir süre sessizce baktı. Pepee ayağa kalkınca şekil de kalktı. Pepee biraz düşündü ve dans etmeye başladı. Siyah şekil de onunla birlikte zıpladı ve döndü. Pepee bir kolunu kaldırdı ve şekil de kolunu kaldırdı. O zaman Pepee anladı. Şekil, Pepee'nin kendi gölgesiydi. Pepee çok güldü, çünkü siyah şeklin ne olduğunu kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Pepee bir bankta oturmuş güneşleniyordu"
   - Cümle 2: «Pepee bir bankta oturmuş güneşleniyordu.»
   - Açıklama: Pepee kıpırdamadan oturuyorken gölgesinin hareket ettiği söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerde hareket eden siyah bir şekil gördü"
   - Cümle 3: «Birden bankın yanında, yerde hareket eden siyah bir şekil gördü.»
   - Açıklama: Gerçek bir sorun yok, yalnız bir merak var; çocuğun önemseyeceği bir sorun kurulmuyor.
   - Açıklama: Pepee oturup dururken şeklin hareket etmesinin sebebi yok ve bu gerçek bir sorun değil, yalnız bir merak.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee aceleci davranmadı"
   - Cümle 5: «Pepee aceleci davranmadı ve bir süre sessizce baktı.»
   - Açıklama: 'Aceleci davranmak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Aceleci davranmak' soyut bir anlatım ve 3 yaşındaki çocuğa uygun değil.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Pepee ayağa kalkınca şekil"
   - Cümle 6: «Pepee ayağa kalkınca şekil de kalktı.»
   - Açıklama: Art arda cümlelerin çoğu 'Pepee' adıyla başlıyor; ad gereksiz yere tekrar ediliyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Pepee bir kolunu kaldırdı"
   - Cümle 9: «Pepee bir kolunu kaldırdı ve şekil de kolunu kaldırdı.»
   - Açıklama: Pepee adı neredeyse her cümlede gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0081` birebir aynı, `@degisim: kızak -> gölge` (tutuyorsan), ardından `@onarim: a690d230136f15215f535974d8abd5f1657efc8d`, sonra gövde.

### Hikâye 11: tohum pepee-0082 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0082
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'takvim', fiil 'taşımak', sıfat 'rahat'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kuru kum dağıldı ve pasta olmadı | su kenarından ıslak kum taşıdı ve pastayı yaptı
@tohum: pepee-0082
@degisim: takvim -> pasta
Güneş parlıyordu ve küçük dalgalar kıyıya vuruyordu. Bugün Şila'nın doğum günüydü ve Pepee ona kumdan bir pasta yapmak istedi. Ama kuru kum hemen dağıldı ve pasta olmadı. Şila uzakta taş topluyordu. Pepee su kenarına gitti ve iki eline ıslak kum aldı. Islak kum elinden akmadı ve Pepee onu rahatça taşıdı. Kumu üst üste koydu ve yuvarlak bir pasta yaptı. Sonra beyaz kabuklar topladı ve üstüne mum gibi dizdi. "Şila, gel, sana bir sürprizim var!" dedi Pepee. Şila koşup geldi ve pastayı gördü. "Ne güzel bir pasta, çok teşekkürler!" dedi Şila. Sonra Pepee ile Şila pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "pastanın etrafında mutlu mutlu dans etti"
   - Cümle 12: «Sonra Pepee ile Şila pastanın etrafında mutlu mutlu dans etti.»
   - Açıklama: Tohumdaki dans özelliği çözümde işe yaramıyor, yalnız sonda süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0082` birebir aynı, `@degisim: takvim -> pasta` (tutuyorsan), ardından `@onarim: c116d8fd2337a99bf6b8ac7471ef882b6c14b2c3`, sonra gövde.

### Hikâye 12: tohum pepee-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0083
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çörek', fiil 'kirletmek', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: rüzgar esti ve mavi şapkayı uçurdu | dedesiyle dönerek dans edip her yere baktı
@tohum: pepee-0083
@degisim: soslu -> şekerli
Deniz kıyısında Pepee ile Dedee kumda şekerli çörek yiyordu. Pepee mavi şapkasını yanına koymuştu. Birden rüzgar esti ve şapkayı uçurdu. Pepee etrafına baktı ama şapkasını göremedi. "Dedeciğim, gel, birlikte dönelim ve her yere bakalım!" dedi Pepee. Dedee güldü ve hemen ayağa kalktı. İkisi kumda dönerek dans etti ve etrafa baktı. Pepee su kenarında, kumun üstünde mavi bir şey gördü. Bu onun şapkasıydı! Pepee'nin elleri şekerliydi ve şapkayı kirletmek istemedi. Ellerini su kenarında yıkadı ve şapkasını başına taktı. Pepee ile Dedee çörek yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi kumda dönerek dans etti ve etrafa baktı"
   - Cümle 7: «İkisi kumda dönerek dans etti ve etrafa baktı.»
   - Açıklama: Dönerek dans etmek şapkayı bulmaya doğrudan yönelmiyor, sebebe yönelik değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi kumda dönerek dans etti"
   - Cümle 7: «İkisi kumda dönerek dans etti ve etrafa baktı.»
   - Açıklama: Dönerek dans etmek kaybolan şapkayı aramaya doğrudan yönelmiyor; çözüm dolambaçlı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee'nin elleri şekerliydi ve şapkayı kirletmek istemedi"
   - Cümle 10: «Pepee'nin elleri şekerliydi ve şapkayı kirletmek istemedi.»
   - Açıklama: Şekerli eller ve el yıkama çözüm bittikten sonra sebepsizce eklenen işlevsiz bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0083` birebir aynı, `@degisim: soslu -> şekerli` (tutuyorsan), ardından `@onarim: a5f78d9a0d9212a6353f45b85ee2836c22911118`, sonra gövde.
