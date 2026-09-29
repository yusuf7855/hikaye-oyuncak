# Editör görevi (onarım): Pepee, onarım partisi 4

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar4.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar4.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Annee
@tohum: pepee-0001
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'iz', fiil 'unutmak', sıfat 'dalgalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Annee
@plan: dalga su kenarındaki kalbi sildi | kuru kumda ayaklarıyla yeni bir kalp yaptı
@tohum: pepee-0001
Rüzgar esiyordu ve deniz biraz dalgalıydı. Pepee annesine sürpriz yapmak için su kenarındaki kuma bir kalp çizdi. Ama küçük bir dalga geldi ve çizgileri hemen sildi. Annee biraz ileride oturmuş, denize bakıyordu. Pepee bu kez sudan uzakta, kuru kuma gitti. Orada ayaklarıyla çizmeyi öğrendi. Küçük adımlarla yürüdü ve her adım kumda bir iz bıraktı. Bu izler kocaman bir kalp oldu. Su oraya kadar gelemedi. "Anne, buraya bak!" dedi Pepee. Annee döndü ve kumdaki kalbi gördü. "Ne güzel olmuş, bunu hiç unutmayacağım, Pepee," dedi Annee. Sonra ikisi kalbin yanına oturdu ve mutlu mutlu denizi seyretti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Orada ayaklarıyla çizmeyi öğrendi"
   - Cümle 6: «Orada ayaklarıyla çizmeyi öğrendi.»
   - Açıklama: Pepee bir şey öğrenmiyor, sadece çiziyor; 'öğrendi' fiili yanlış anlamda.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Orada ayaklarıyla çizmeyi öğrendi"
   - Cümle 6: «Orada ayaklarıyla çizmeyi öğrendi.»
   - Açıklama: Pepee'nin neden ayaklarıyla çizmeye geçtiği söylenmiyor; yöntem sebepsizce değişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0001` birebir aynı, ardından `@onarim: 9449fbb16ff4fbb265c75fd6119b6621f44cbe40`, sonra gövde.

### Hikâye 2: tohum pepee-0002 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0002
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'köfte', fiil 'dağıtmak', sıfat 'heyecanlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: dans ederken arkadaşının topraktan köftelerini dağıttı | özür diledi ve köfteleri yeniden yaptı
@tohum: pepee-0002
Ormanda büyük bir ağacın altında Şila ile Pepee oynuyordu. Şila topraktan küçük köfteler yapmış ve bir yaprağın üstüne koymuştu. Heyecanlı Pepee dans ederken ayağıyla köfteleri dağıttı. Şila yerdeki toprak parçalarına baktı ve üzüldü. Pepee hemen durdu ve kuzeninin yanına oturdu. "Özür dilerim, Şila, köftelerin benim yüzümden düştü," dedi Pepee. Sonra topraktan yeni köfteler yapmaya başladı. Onları tek tek yuvarladı ve yaprağa koydu. Şila da ona yardım etti ve güldü. Az sonra yaprağın üstü yine doldu. "Teşekkür ederim, Pepee, yeni köfteler daha da güzel oldu!" dedi Şila.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "arkadaşının topraktan köftelerini dağıttı"
   - Cümle 0 (plan satırı): «dans ederken arkadaşının topraktan köftelerini dağıttı | özür diledi ve köfteleri yeniden yaptı»
   - Açıklama: 'topraktan köftelerini' tamlaması bozuk; 'topraktan yaptığı köfteleri' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "köftelerin benim yüzümden düştü"
   - Cümle 6: «"Özür dilerim, Şila, köftelerin benim yüzümden düştü," dedi Pepee.»
   - Açıklama: Köfteler yerdeki yaprakta dağıldı, düşmedi; ayrıca 'yüzümden' deyimsel kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0002` birebir aynı, ardından `@onarim: d7ca41173f03e378681bb21e7de0bfbc65129a7e`, sonra gövde.

### Hikâye 3: tohum pepee-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0003
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'zambak', fiil 'damlamak', sıfat 'yağmurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: yağmurdan zambağın sapı eğildi | dedesinden yardım isteyip sapı bir çubuğa bağladı
@tohum: pepee-0003
Pepee ile Dedee yağmurlu ormanda dans ediyordu. Pepee dönerken yerde beyaz bir zambak gördü. Zambağın sapı yağmurdan eğilmişti ve başı çamura değiyordu. Yapraklarından yere su damlıyordu. Pepee çiçeği kaldırdı ama sap hemen yine eğildi. "Dedeciğim, bu çiçeği dik tutmama yardım eder misin?" diye sordu Pepee. Dedee yerden düz bir çubuk buldu ve Pepee'ye verdi. Pepee çubuğu zambağın yanında toprağa batırdı. Sonra sapı uzun bir otla çubuğa bağladı. Beyaz çiçek artık dik duruyordu. Dedee sevinçle ellerini çırptı. "Teşekkürler, dedeciğim, çiçeğimiz artık çamurda değil!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yağmurlu ormanda dans ediyordu"
   - Cümle 1: «Pepee ile Dedee yağmurlu ormanda dans ediyordu.»
   - Açıklama: Tohumdaki dans özelliği yalnız açılışta geçiyor ve sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ile Dedee yağmurlu ormanda dans ediyordu"
   - Cümle 1: «Pepee ile Dedee yağmurlu ormanda dans ediyordu.»
   - Açıklama: Tohumdaki dans özelliği yalnız açılışta geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0003` birebir aynı, ardından `@onarim: 0dac560c47109fc4777db332d15f4304f7f74c89`, sonra gövde.

### Hikâye 4: tohum pepee-0004 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0004
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kilit', fiil 'serinlemek', sıfat 'sevinçli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: kardeşi hızlı dansı yapamadı ve üzüldü | ona yavaş adımları gösterdi ve birlikte döndüler
@tohum: pepee-0004
@degisim: kilit -> gölge
Pepee ile Bebee ormanda çiçeklerin arasında oynuyordu. Pepee hızlı hızlı dönerek dans etti. Bebee de dönmek istedi, ama küçüktü ve bunu yapamadı. Bebee çimlere oturdu ve üzüldü. Pepee kardeşinin yanına geldi ve ona elini uzattı. "Gel, Bebee, önce yavaş yavaş yapalım," dedi Pepee. Pepee bir adım sağa, bir adım sola gitti. Bebee de Pepee'ye bakıp aynı adımları attı. Sonra ikisi el ele yavaşça döndü. "Bak, ben de dönüyorum!" dedi Bebee. Biraz sonra ikisi büyük bir ağacın gölgesine oturup serinledi. Bebee çok sevinçliydi, çünkü Pepee ona yardım etmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sonra ikisi büyük bir ağacın gölgesine oturup serinledi"
   - Cümle 11: «Biraz sonra ikisi büyük bir ağacın gölgesine oturup serinledi.»
   - Açıklama: Gölgede serinleme olaydan çıkmıyor ve dans sorununa hiçbir katkısı olmayan işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ikisi büyük bir ağacın gölgesine oturup serinledi"
   - Cümle 11: «Biraz sonra ikisi büyük bir ağacın gölgesine oturup serinledi.»
   - Açıklama: Gölgede serinleme olaydan çıkmıyor ve hikayede hiçbir işe yaramayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0004` birebir aynı, `@degisim: kilit -> gölge` (tutuyorsan), ardından `@onarim: 753aac17aac71b8123c3dd8178f70aec09b3413a`, sonra gövde.

### Hikâye 5: tohum pepee-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0006
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kanepe', fiil 'sulamak', sıfat 'yüksek'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: toprak kuruydu ve küçük çiçekler susuz kalmıştı | ninesinden su isteyip çiçekleri dans ederek suladı
@tohum: pepee-0006
@degisim: kanepe -> şişe
Ormanda Pepee ile Nenee yüksek ağaçların altında yürüyordu. Pepee yerde başı eğik küçük mor çiçekler gördü. Toprak çok kuruydu ve çiçekler susuz kalmıştı. Pepee çiçekleri sulamak istedi ama yanında hiç su yoktu. "Nineciğim, çiçekler için biraz su verir misin?" diye sordu Pepee. Nenee çantasından bir şişe su çıkardı ve Pepee'ye verdi. Pepee şişeyi iki eliyle tuttu ve dans ederek döndü. Şişeden küçük damlalar çıktı ve bütün çiçeklerin üstüne düştü. Nenee bunu görünce kahkahayla güldü. Az sonra çiçeklerin altındaki toprak ıslandı. Pepee çok sevindi, çünkü çiçeklere su vermişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerde başı eğik küçük mor çiçekler"
   - Cümle 2: «Pepee yerde başı eğik küçük mor çiçekler gördü.»
   - Açıklama: Çiçeğe 'başı eğik' demek küçük çocuk için mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerde başı eğik küçük"
   - Cümle 2: «Pepee yerde başı eğik küçük mor çiçekler gördü.»
   - Açıklama: Çiçeklerin 'başı eğik' olması mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0006` birebir aynı, `@degisim: kanepe -> şişe` (tutuyorsan), ardından `@onarim: 966fb2d7951ab5cfdde99fa0718aec296619f8eb`, sonra gövde.

### Hikâye 6: tohum pepee-0007 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0007
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'şort', fiil 'tekrarlamak', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kuru kumdan yapılan gemi hemen dağıldı | ıslak kumla sağlam bir gemi yaptı
@tohum: pepee-0007
@degisim: şort -> kova
Rüzgar hafif hafif esiyordu. Pepee kumda gemi oyunu oynuyordu. Kumdan bir gemi yaptı ama kuru kum hemen dağıldı. Pepee yine umutluydu ve yeni bir şey öğrenmek istedi. Kovasını aldı ve su kenarındaki ıslak kumla doldurdu. Islak kumu elleriyle sıktı ve yeni bir gemi yaptı. Bu kez gemi hiç yıkılmadı. Pepee bunu üç kez tekrarladı ve gemi büyüdü. Sonra geminin ortasına oturdu ve denize baktı. Pepee çok sevindi, çünkü artık sağlam bir gemisi vardı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yeni bir şey öğrenmek istedi"
   - Cümle 4: «Pepee yine umutluydu ve yeni bir şey öğrenmek istedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız deniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee yine umutluydu"
   - Cümle 4: «Pepee yine umutluydu ve yeni bir şey öğrenmek istedi.»
   - Açıklama: 'Umutlu' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Pepee bunu üç kez tekrarladı"
   - Cümle 8: «Pepee bunu üç kez tekrarladı ve gemi büyüdü.»
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği belli değil.
   - Açıklama: 'Bunu' zamirinin hangi eylemi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0007` birebir aynı, `@degisim: şort -> kova` (tutuyorsan), ardından `@onarim: 43a43b2e2c181795ed260d9b1ba16112ca935791`, sonra gövde.

### Hikâye 7: tohum pepee-0010 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0010
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'şekerleme', fiil 'inmek', sıfat 'hazırlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: zıplayan yumurta masanın altına yuvarlandı | yumurtayı bulup kaşığın altına tabak tuttu
@tohum: pepee-0010
@degisim: şekerleme -> tabak
Evde kahvaltı masası hazırdı ve Pepee yerine oturmuştu. Pepee haşlanmış yumurtasını kaşığa koydu ve onu yavaşça zıplattı. Ama yumurta çok yükseğe zıpladı ve masanın altına yuvarlandı. Pepee hemen sandalyesinden indi ve masanın altına baktı. Pepee onu bir masa ayağının yanında buldu. Sonra yerine geri oturdu. Bu kez Pepee daha hazırlıklıydı. Kaşığın altına büyük bir tabak tuttu. Yumurta yine zıpladı, ama bu sefer tabağa düştü. Pepee oyunu üç kez daha oynadı ve güldü. Sonra yumurtasını soydu ve afiyetle yedi. Pepee çok mutluydu, çünkü tabakla oyununu kurtarmıştı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yumurtasını kaşığa koydu ve onu yavaşça zıplattı"
   - Cümle 2: «Pepee haşlanmış yumurtasını kaşığa koydu ve onu yavaşça zıplattı.»
   - Açıklama: Haşlanmış yumurtanın kaşıkta zıplatılması akla yatkın değil; sorun saçma bir oyundan doğuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yumurta çok yükseğe zıpladı"
   - Cümle 3: «Ama yumurta çok yükseğe zıpladı ve masanın altına yuvarlandı.»
   - Açıklama: Haşlanmış yumurtanın kaşıktan yavaşça zıplatılıp çok yükseğe fırlaması akla yatkın olmayan, önemsiz bir sorun.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee daha hazırlıklıydı"
   - Cümle 7: «Bu kez Pepee daha hazırlıklıydı.»
   - Açıklama: 'Hazırlıklı' soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tabakla oyununu kurtarmıştı"
   - Cümle 12: «Pepee çok mutluydu, çünkü tabakla oyununu kurtarmıştı.»
   - Açıklama: 'Oyunu kurtarmak' mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Oyunu kurtarmak' mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0010` birebir aynı, `@degisim: şekerleme -> tabak` (tutuyorsan), ardından `@onarim: 690ed4748240ef93111e33a9992c64206dc96b6c`, sonra gövde.

### Hikâye 8: tohum pepee-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0012
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'davul', fiil 'havalanmak', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kovaya vurunca kumlar tabağa uçtu | kovayı tabaktan uzağa koyup öyle vurdu
@tohum: pepee-0012
@degisim: havalı -> gürültülü
Pepee kumda oturmuş, kahvaltıda bal ve ekmek yiyordu. Bir yandan da boş kovasına davul gibi vuruyordu. Ama gürültülü sesle birlikte kumlar havalandı ve tabağın kenarına düştü. Pepee ekmeğine kum gelmesini hiç istemedi. Hemen kovasını aldı ve birkaç adım öteye koydu. Sonra yine kovaya vurdu ve komik bir şarkı söyledi. Kovadan güm güm diye sesler çıktı. Kumlar yine uçuştu ama tabağa kadar gelemedi. Pepee mutlu mutlu ekmeğini bitirdi. Pepee bundan sonra kumda kovasına hep tabaktan uzakta vurdu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "gürültülü sesle birlikte kumlar havalandı"
   - Cümle 3: «Ama gürültülü sesle birlikte kumlar havalandı ve tabağın kenarına düştü.»
   - Açıklama: Boş kovaya vurmanın sesle kumu tabağa uçurması akla yatkın bir sebep değil.
   - Açıklama: Boş kovaya vurmanın sesiyle kumların tabağa uçması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0012` birebir aynı, `@degisim: havalı -> gürültülü` (tutuyorsan), ardından `@onarim: 4a83fa764dd038387ee8d6582f8152026ac5c32d`, sonra gövde.

### Hikâye 9: tohum pepee-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0013
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'toka', fiil 'kurulamak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: ağaçlar renkli yayı kapattı ve kardeşi göremedi | kardeşini açıklığa götürdü ve renkleri saydı
@tohum: pepee-0013
@degisim: kurulamak -> saymak
Pepee ile Bebee yağmurdan sonra ormanda yürüyordu. Pepee ağaçların arasından gökyüzünde renkli bir yay gördü. Ama küçük Bebee ağaçlar yüzünden onu göremedi. Pepee biraz ileride geniş bir açıklık fark etti. "Gel, Bebee, oradan daha iyi görünür," dedi Pepee. Kardeşinin elinden tuttu ve oraya yürüdüler. Orada renkli yay kocaman görünüyordu. Hareketli Bebee sevinçle zıpladı ve el çırptı. Pepee yeni bir şey öğrenmek istedi ve renkleri tek tek saydı. Tam yedi renk vardı. "Benim tokamda da bu renkler var!" dedi Bebee. Pepee çok sevindi, çünkü kardeşi de renkleri görmüştü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gökyüzünde renkli bir yay gördü"
   - Cümle 2: «Pepee ağaçların arasından gökyüzünde renkli bir yay gördü.»
   - Açıklama: Gökkuşağı için 'renkli yay' denmiş; kelime doğru anlamda değil ve çocuk için belirsiz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Benim tokamda da bu renkler var"
   - Cümle 11: «"Benim tokamda da bu renkler var!" dedi Bebee.»
   - Açıklama: Toka sebepsiz beliriyor ve renk sayma sorunun çözümüne hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0013` birebir aynı, `@degisim: kurulamak -> saymak` (tutuyorsan), ardından `@onarim: 83de55b14ea60ba0ef239b1af0071e19d4c5d744`, sonra gövde.
