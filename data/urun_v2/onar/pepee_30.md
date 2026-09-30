# Editör görevi (onarım): Pepee, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0114
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'patik', fiil 'sallanmak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: patik kumun altında kaldı ve kayboldu | o yerde dans edip patiği ayağıyla buldu
@tohum: pepee-0114
Pepee ile Bebee deniz kıyısında kumla oynuyordu. Bebee patiğini çıkarıp yanına koymuştu. Ama Bebee kum atarken patiği kumun altında kaldı ve kayboldu. "Patiğim nerede?" diye sordu Bebee. Bebee kumu hep oraya atmıştı. "Bebee, gel, orada dans edelim!" dedi Pepee. İkisi el ele tutuştu ve küçük adımlarla dans etti. Bebee sağa sola sallandı ve güldü. Birden Pepee'nin ayağı yumuşak bir şeye değdi. Pepee kumu eliyle kazdı ve pembe patiği buldu. Patiği Bebee'nin ayağına giydirdi ve incecik ipini bağladı. İkisi kumda oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "o yerde dans edip"
   - Cümle 0 (plan satırı): «patik kumun altında kaldı ve kayboldu | o yerde dans edip patiği ayağıyla buldu»
   - Açıklama: Plan satırındaki 'o yerde' zamirinin hangi yeri gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bebee kumu hep oraya atmıştı"
   - Cümle 5: «Bebee kumu hep oraya atmıştı.»
   - Açıklama: 'oraya' zarfının hangi yeri gösterdiği belli değil; öncesinde bir yer anılmamış.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "orada dans edelim"
   - Cümle 6: «"Bebee, gel, orada dans edelim!" dedi Pepee.»
   - Açıklama: Patiği aramak yerine dans ediliyor ve patik tesadüfen ayağa değince bulunuyor; çözüm sebebe doğrudan yönelmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Birden Pepee'nin ayağı yumuşak bir şeye değdi"
   - Cümle 9: «Birden Pepee'nin ayağı yumuşak bir şeye değdi.»
   - Açıklama: Patik aramaya değil dansa yönelen çözümde patik tesadüfen bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0114` birebir aynı, ardından `@onarim: 95db9062fa00cd23c221d0dee27a9ce6fac732e3`, sonra gövde.

### Hikâye 2: tohum pepee-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0118
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: kaybolan eşya
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'taç', fiil 'serinletmek', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: taç dalın altında başından kaydı ve kayboldu | sırtındaki tacı dans ederek yere düşürdü
@tohum: pepee-0118
Hafif bir rüzgar esti ve Pepee'yi serinletti. Pepee ormanda sarı çiçeklerden yaptığı tacıyla yürüyordu. Ama alçak bir dalın altından geçerken taç başından kaydı ve kayboldu. Pepee çamurlu yola ve çiçeklerin arasına baktı. Tacını hiçbir yerde göremedi. Sonra sırtında hafif bir şey olduğunu hissetti. Pepee dansındaki gibi zıpladı ve sallandı. Sırtından yere sarı bir şey düştü. Bu onun tacıydı, sırtında takılı kalmıştı. Pepee tacı yerden aldı ve başına yeniden taktı. Sonra ormanda tacıyla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Pepee dansındaki gibi zıpladı"
   - Cümle 7: «Pepee dansındaki gibi zıpladı ve sallandı.»
   - Açıklama: 'dansındaki gibi' bozuk bir yapı; 'dans eder gibi' olmalı.
   - Açıklama: 'Dansındaki gibi' bozuk bir yapı; 'dans eder gibi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0118` birebir aynı, ardından `@onarim: 1a50f8d1809fbdf5622566ce11592d3a5904b11f`, sonra gövde.

### Hikâye 3: tohum pepee-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0119
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tekne', fiil 'tanımak', sıfat 'özel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: hafif tekne dalgalar gelince hep devrildi | teknenin ortasına düz bir taş koydu
@tohum: pepee-0119
@degisim: tanımak -> denemek
Küçük dalgalar kumda hafif bir ses çıkarıyordu. Pepee su kenarında küçük oyuncak teknesiyle oynuyordu. Ama tekne çok hafifti ve dalgalar gelince hep devrildi. Pepee tekneyi üç kez düzeltmeyi denedi ama olmadı. Sonra biraz düşündü. Kumdan bunun için özel bir taş seçti. Taş düz ve ağırdı. Pepee taşı teknenin tam ortasına koydu. Bir dalga geldi ama tekne bu kez dik kaldı. Tekne dalgaların üstünde sallanarak yüzdü. Pepee taşın tekneyi sağlam tuttuğunu öğrendi. Pepee çok sevindi, çünkü teknesiyle yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee su kenarında küçük oyuncak teknesiyle oynuyordu."
   - Cümle 2: «Pepee su kenarında küçük oyuncak teknesiyle oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama burada deniz kenarında yalnız başına deniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kumdan bunun için özel"
   - Cümle 6: «Kumdan bunun için özel bir taş seçti.»
   - Açıklama: 'Bunun' zamirinin neyi gösterdiği belli değil, önceki cümlelerde bir plan anlatılmadı.
   - Açıklama: 'Bunun' zamirinin neyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0119` birebir aynı, `@degisim: tanımak -> denemek` (tutuyorsan), ardından `@onarim: 981292b60744d07d059c73a20fb75eda6d7d2faa`, sonra gövde.

### Hikâye 4: tohum pepee-0120 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | park | Annee
@tohum: pepee-0120
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'ruj', fiil 'fışkırmak', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | park | Annee
@plan: damlalar hemen düştü ve renkler kayboldu | şişeyi yukarı doğru sıkıp suyu yükseğe fışkırttı
@tohum: pepee-0120
@degisim: ruj -> damla
Bir sabah Pepee ile Annee parkta kahvaltı yapıyordu. Annee su şişesini sıktı ve su havaya fışkırdı. Güneşte damlalar renk renk parladı ama hemen yere düştü. Pepee o renkleri daha uzun görmek istedi. Çilekli ekmeğini bıraktı ve su şişesini aldı. Güneşe arkasını döndü ve şişeyi yukarı doğru güçlü sıktı. Su yükseğe fışkırdı ve damlalar havada daha uzun kaldı. Damlalar kırmızı, sarı ve mavi renklerle parladı. Annee sevinçle ellerini çırptı. Pepee şişeyi Annee'ye verdi ve o da su fışkırttı. İkisi renkli damlalar yapıp kahvaltılarına mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parkta kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Pepee ile Annee parkta kahvaltı yapıyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız arka plan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız ortam olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "renk renk parladı ama hemen yere düştü"
   - Cümle 3: «Güneşte damlalar renk renk parladı ama hemen yere düştü.»
   - Açıklama: Damlaların neden hemen düştüğüne dair bir sebep söylenmiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama hemen yere düştü"
   - Cümle 3: «Güneşte damlalar renk renk parladı ama hemen yere düştü.»
   - Açıklama: Damlaların yere düşmesi çocuğun önemseyeceği gerçek bir sorun olmaktan çok zayıf bir istek.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "şişeyi yukarı doğru güçlü sıktı"
   - Cümle 6: «Güneşe arkasını döndü ve şişeyi yukarı doğru güçlü sıktı.»
   - Açıklama: Sıfat zarf yerine kullanılmış; 'güçlüce' ya da 'kuvvetle sıktı' olmalı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şişeyi yukarı doğru güçlü sıktı"
   - Cümle 6: «Güneşe arkasını döndü ve şişeyi yukarı doğru güçlü sıktı.»
   - Açıklama: 'güçlü' sıfatı zarf yerinde yanlış kullanılmış; 'güçlüce' ya da 'kuvvetle' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0120` birebir aynı, `@degisim: ruj -> damla` (tutuyorsan), ardından `@onarim: 30ea609227c90b985c781fc931188aec24ccb19f`, sonra gövde.

### Hikâye 5: tohum pepee-0121 (deneme 2 -> 3)

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
Pepee ormanda Dedee ile saklambaç oynuyordu. Dedee saklandı ve Pepee onu aramaya başladı. Ama ormanda çok ağaç vardı ve Pepee dedesini bulamadı. Birden rüzgarla tatlı bir koku geldi. Pepee havayı kokladı ve bu kokuyu kahvaltıdan tanıdı. Bu, tahin ile pekmezin kokusuydu! Pepee kokuya doğru yürüdü ve büyük bir ağacın arkasına baktı. Dedee orada yere bir örtü sermekle meşguldü. Örtünün üstünde yumurta, bal ve tahin pekmez vardı. "Seni buldum, dedeciğim!" dedi Pepee. "Buldun, sana sürpriz bir kahvaltı hazırladım," dedi Dedee. Pepee dedesine sıkıca sarıldı. İkisi örtüye oturdu ve kahvaltıyı mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden rüzgarla tatlı bir koku geldi"
   - Cümle 4: «Birden rüzgarla tatlı bir koku geldi.»
   - Açıklama: Çözümü getiren koku rüzgarla tesadüfen geliyor ve saklanan dedenin aynı anda kahvaltı sermesi sebepsizce çözümü hazırlıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir örtü sermekle meşguldü"
   - Cümle 8: «Dedee orada yere bir örtü sermekle meşguldü.»
   - Açıklama: 'Meşguldü' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yere bir örtü sermekle meşguldü"
   - Cümle 8: «Dedee orada yere bir örtü sermekle meşguldü.»
   - Açıklama: 'Meşgul' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0121` birebir aynı, `@degisim: piyano -> örtü` (tutuyorsan), ardından `@onarim: 7b5449b82fa46a54135652563581e675ed491102`, sonra gövde.

### Hikâye 6: tohum pepee-0124 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ormanda tatlı bir kokunun nereden geldiğini merak etti | kokuyu baldan tanıdı ve sarı çiçekleri buldu
@tohum: pepee-0124
@degisim: dizmek -> koklamak
Pepee ormanda ağaçların arasında yürüyordu. Birden havada tatlı bir koku duydu. Pepee bu kokunun nereden geldiğini çok merak etti. Kahvaltıda yediği bal da tam böyle kokuyordu. Bu yüzden Pepee çevrede bal gibi kokan bir çiçek aradı. Bir çalının esnek dallarını elleriyle yavaşça açtı. Dalların arkasında küçük, sarı çiçekler vardı. Pepee sünger gibi yumuşak çiçeklerden birini kokladı. Güzel koku bu çiçeklerden geliyordu. Pepee çiçeklere uzun uzun baktı ve gülümsedi. Pepee çok sevindi, çünkü kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Pepee bu kokunun nereden geldiğini çok merak etti"
   - Cümle 3: «Pepee bu kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Yalnız bir merak var; çözülmesi gereken gerçek bir sorun kurulmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden Pepee çevrede bal gibi kokan bir çiçek aradı"
   - Cümle 5: «Bu yüzden Pepee çevrede bal gibi kokan bir çiçek aradı.»
   - Açıklama: Bal kokusundan çiçek aramaya geçiş sebepsiz; çözüm açıklanmadan geliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çalının esnek dallarını"
   - Cümle 6: «Bir çalının esnek dallarını elleriyle yavaşça açtı.»
   - Açıklama: 'Esnek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki bir çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0124` birebir aynı, `@degisim: dizmek -> koklamak` (tutuyorsan), ardından `@onarim: 1348e0b7a27cef9c4d73ab8ebbfd4c4f4575fe6c`, sonra gövde.

### Hikâye 7: tohum pepee-0125 (deneme 2 -> 3)

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
@plan: kaydıraktan kayarken çantadan bir kaşık düştü | kardeşinden yardım istedi ve kaşığı kaydırağın altında buldu
@tohum: pepee-0125
Pepee ile Bebee parkta kahvaltı yapmak istedi. Güneşten korunmak için ağacın gölgesine oturdular. Ama Pepee kaydıraktan kayarken çantadan bir kaşık düşmüştü. Bal için bir kaşık eksikti. Pepee kaydırağın yanına koştu ama kaşığı göremedi. "Bebee, gel bana yardım et, kaşığı birlikte arayalım," dedi Pepee. Bebee hemen koşarak geldi. "Ben küçüğüm, kaydırağın altına sığarım!" dedi Bebee. Bebee eğildi ve kaydırağın altına baktı. "Kaşık burada, taşın yanında!" dedi Bebee. Pepee elini uzattı ve kaşığı aldı. "Teşekkürler, Bebee!" dedi Pepee. Sonra ikisi yerlerine döndü ve ballı ekmeklerini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kaşığı kaydırağın altında buldu"
   - Cümle 0 (plan satırı): «kaydıraktan kayarken çantadan bir kaşık düştü | kardeşinden yardım istedi ve kaşığı kaydırağın altında buldu»
   - Açıklama: Planda kaşığı Pepee buluyor ama gövdede Bebee buluyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bebee eğildi ve kaydırağın altına baktı"
   - Cümle 9: «Bebee eğildi ve kaydırağın altına baktı.»
   - Açıklama: Kaşığı Pepee değil Bebee bulup sorunu çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0125` birebir aynı, ardından `@onarim: bdcbaeb7cb0f530d1e9f58ae21bf8148e2187f2e`, sonra gövde.

### Hikâye 8: tohum pepee-0126 (deneme 2 -> 3)

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
Bir sabah Pepee kahvaltı sepetiyle ormana geldi. Sepetten bir yumurta ve bir kaşık aldı. Kaşıkta yumurta taşıma oyunu oynamak istedi. Önce iki ağacın arasına kırmızı bir iplik bağladı. Yumurtayı o ipliğe kadar taşıyacaktı. Ama yuvarlak yumurta kaşıkta durmadı ve çimlere yuvarlandı. Pepee yumurtayı yerden aldı ama yumurta yine düştü. Sonra kahvaltı sepetini yeniden açtı. İçinde bal ve biberli peynir vardı. Pepee kaşığa biraz bal sürdü ve yumurtayı üstüne koydu. Yumurta bala yapıştı ve artık kaymadı. Pepee yavaş yavaş yürüdü ve yumurta hiç düşmedi. Sonunda kırmızı ipliğe vardı. Oyun bitince ağacın altına oturdu ve yumurtayı biberli peynirle mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee kahvaltı sepetiyle ormana geldi"
   - Cümle 1: «Bir sabah Pepee kahvaltı sepetiyle ormana geldi.»
   - Açıklama: Dört yaşındaki Pepee ormana tek başına gidiyor ve oyunu büyüksüz deniyor; güvenli kullanım satırına aykırı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kahvaltı sepetiyle ormana geldi"
   - Cümle 1: «Bir sabah Pepee kahvaltı sepetiyle ormana geldi.»
   - Açıklama: Güvenli özellik kullanımı satırı Pepee'nin yeni şeyleri bir büyüğün yanında denemesini ister; burada dört yaşındaki Pepee ormanda yalnız başına yeni bir oyun deniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kaşıkta yumurta taşıma oyunu oynamak istedi.»
   - Açıklama: Sorun (yumurtanın kaşıkta durmaması) ancak 6. cümlede söyleniyor, ilk 3 cümlede değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0126` birebir aynı, `@degisim: kapanmak -> bağlamak` (tutuyorsan), ardından `@onarim: c940d41cf754971d70b465ef639d7f46c15a3012`, sonra gövde.

### Hikâye 9: tohum pepee-0128 (deneme 2 -> 3)

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
Bir sabah Pepee ile Bebee deniz kıyısında bir battaniyenin üstünde oturuyordu. Pepee ilk kez kumdan kuleler yapmayı denedi. Ama kum çok kuruydu ve kuleler çabuk dağıldı. Pepee kahvaltıda yumurtasını yediği küçük kabı battaniyeden aldı. Su kenarına gitti ve kabı ıslak kumla doldurdu. Sonra kabı ters çevirdi ve yavaşça kaldırdı. Kumda yumurta gibi yuvarlak bir kule duruyordu. "Bak, Bebee, bu kule dağılmadı!" dedi Pepee. "Ben de yapmak istiyorum!" dedi Bebee. Pepee kabı ona verdi ve Bebee de bir kule yaptı. Pepee çok sevindi, çünkü ilk kez kumdan sağlam bir kule yapmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ilk kez kumdan kuleler yapmayı denedi"
   - Cümle 2: «Pepee ilk kez kumdan kuleler yapmayı denedi.»
   - Açıklama: Tohumdaki özellik kahvaltı iken hikaye 'yeni şeyler denemeyi sever' özelliğini de ekliyor ve kahvaltı yalnız kabın kaynağı olarak geçiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Su kenarına gitti ve kabı ıslak kumla doldurdu"
   - Cümle 5: «Su kenarına gitti ve kabı ıslak kumla doldurdu.»
   - Açıklama: Güvenli kullanım satırı yeni şeyleri bir büyüğün yanında denemeyi istiyor, oysa iki küçük çocuk yanlarında büyük olmadan deniz kıyısında su kenarına gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0128` birebir aynı, `@degisim: satmak -> doldurmak` (tutuyorsan), ardından `@onarim: 31372a2a8e0270d321e5b9dd70a8912ebe4a3d1f`, sonra gövde.

### Hikâye 10: tohum pepee-0129 (deneme 2 -> 3)

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
Deniz kıyısında küçük dalgalar kuma vuruyordu. Pepee annesiyle kumda otururken yakında bir ses duydu. Bir şey komik komik homurdanıyordu. "Anneciğim, bu ses nereden geliyor?" diye sordu Pepee. "Bilmiyorum, sen bul bakalım," dedi Annee. Pepee sesi bulmak için kalktı ve dans ederek sağa sola gitti. Ama nereye gitse ses de onunla gidiyordu. Pepee durdu ve elini karnına koydu. "Anneciğim, homurdanan benim karnım!" dedi Pepee ve güldü. Annee de güldü ve çantadan bir kap salata çıkardı. Sonra ikisi kumda oturdu ve salatayı memnun memnun yedi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dans ederek sağa sola gitti"
   - Cümle 6: «Pepee sesi bulmak için kalktı ve dans ederek sağa sola gitti.»
   - Açıklama: Tohumdaki dans özelliği sorunu çözmüyor; sesin karından geldiğini durup elini karnına koyunca buluyor, dans süs olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0129` birebir aynı, ardından `@onarim: 5cb72b538436d7226a439403279dbbff0e8f0e8e`, sonra gövde.

### Hikâye 11: tohum pepee-0130 (deneme 2 -> 3)

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
Pepee ormanda çiçek topluyordu. Mavi şapkasını çiçeklerle süslemek istedi. Ama çiçekler şapkadan hep kaydı, çünkü çok kısaydı. Pepee bir çiçeği başka bir çiçeğe sarmayı denedi. İlk seferde olmadı ve çiçek yere düştü. Pepee yeniden denedi ve bu işi öğrendi. Sonra bütün çiçekleri tek tek birbirine bağladı. Böylece uzun bir çiçek halkası yaptı. Pepee halkayı şapkasının çevresine taktı. Pepee başını salladı ama çilek gibi kırmızı çiçekler hiç düşmedi. Pepee çiçekli şapkasıyla ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee bir çiçeği başka bir çiçeğe sarmayı denedi"
   - Cümle 4: «Pepee bir çiçeği başka bir çiçeğe sarmayı denedi.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada ormanda tek başına deniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çilek gibi kırmızı çiçekler"
   - Cümle 10: «Pepee başını salladı ama çilek gibi kırmızı çiçekler hiç düşmedi.»
   - Açıklama: Benzetme (çilek gibi) mecazlı anlatım; sade 'kırmızı çiçekler' yeterli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0130` birebir aynı, `@degisim: düşünceli -> kırmızı` (tutuyorsan), ardından `@onarim: f4d6ba7546ec0ace14b93bc354c5814eaf3ec877`, sonra gövde.

### Hikâye 12: tohum pepee-0134 (deneme 2 -> 3)

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
Pepee ormanda kahvaltı yapmak için bisikletini itiyordu. Bisikletin sepetinde yumurta, bal ve bir kahvaltı örtüsü vardı. Birden yağmur başladı ve damlalar Pepee'nin mavi şapkasına düştü. Pepee hiç ıslanmak istemedi. Hemen durdu ve örtüyü sepetten çıkardı. Örtüyü başının üstüne tuttu. Sonra bir ağacın yanında sessizce bekledi. Yağmur örtünün üstüne tıp tıp damladı ama Pepee kuru kaldı. Az sonra yağmur dindi. Bulutların arasında sıcak güneş belirdi. Yapraklardaki damlalar farklı renklerde parlıyordu. Pepee çok sevindi, çünkü yağmurda hiç ıslanmamıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepetinde yumurta, bal ve bir kahvaltı örtüsü"
   - Cümle 2: «Bisikletin sepetinde yumurta, bal ve bir kahvaltı örtüsü vardı.»
   - Açıklama: Kahvaltı için kurulan yumurta ve bal hiç kullanılmıyor, kahvaltı da yapılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bisikletin sepetinde yumurta, bal ve"
   - Cümle 2: «Bisikletin sepetinde yumurta, bal ve bir kahvaltı örtüsü vardı.»
   - Açıklama: Kahvaltı, bisiklet, yumurta ve bal işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0134` birebir aynı, `@degisim: scooter -> bisiklet` (tutuyorsan), ardından `@onarim: 2fda1d63b1f3905f0b7532c854b110fa50d84566`, sonra gövde.
