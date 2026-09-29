# Editör görevi (onarım): Pepee, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0001 (deneme 4 -> 5)

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
Rüzgar esiyordu ve deniz biraz dalgalıydı. Pepee annesine sürpriz yapmak için su kenarındaki kuma bir kalp çizdi. Ama küçük bir dalga geldi ve çizgileri hemen sildi. Annee arkasında oturmuş, onu izliyordu. Pepee bu kez sudan uzakta, annesinin yanındaki kuru kuma gitti. Annesi görsün diye ayaklarıyla büyük bir kalp çizmeyi denedi. Küçük adımlarla yürüdü ve her adım kumda bir iz bıraktı. Bu izler kocaman bir kalp oldu. "Anne, buraya bak, ayakla çizmeyi öğrendim!" dedi Pepee. Annee ayağa kalktı ve kumdaki kalbi gördü. "Ne güzel olmuş, bunu hiç unutmayacağım, Pepee," dedi Annee. Sonra ikisi kalbin yanına oturdu ve mutlu mutlu denizi seyretti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Annee arkasında oturmuş, onu izliyordu"
   - Cümle 4: «Annee arkasında oturmuş, onu izliyordu.»
   - Açıklama: Pepee annesine sürpriz yapmak istiyor ama annesi baştan beri onu izliyor ve sonunda kalbi yeni görmüş gibi davranıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0001` birebir aynı, ardından `@onarim: d3e47cb7849bbf965beaf2decf6e6a8a3589486c`, sonra gövde.

### Hikâye 2: tohum pepee-0007 (deneme 4 -> 5)

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
Rüzgar hafif hafif esiyordu. Pepee kumda gemi oyunu oynuyordu. Kumdan bir gemi yaptı ama kuru kum hemen dağıldı. Pepee üzülmedi, umutluydu. Kumu elleriyle biraz kazdı. Kumun altı ıslaktı. Kovasını aldı ve bu kumla doldurdu. Islak kumu sıkıca sıktı ve yeni bir gemi yaptı. Bu kez gemi hiç yıkılmadı. Pepee kovayı doldurmayı üç kez tekrarladı ve gemi büyüdü. Sonra geminin ortasına oturdu ve denize baktı. Pepee çok sevindi, çünkü ıslak kumla gemi yapmayı öğrenmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee üzülmedi, umutluydu"
   - Cümle 4: «Pepee üzülmedi, umutluydu.»
   - Açıklama: 'umutlu' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Islak kumu sıkıca sıktı"
   - Cümle 8: «Islak kumu sıkıca sıktı ve yeni bir gemi yaptı.»
   - Açıklama: 'sıkıca sıktı' gereksiz tekrar.
   - Açıklama: 'sıkıca sıktı' gereksiz tekrar içeriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0007` birebir aynı, `@degisim: şort -> kova` (tutuyorsan), ardından `@onarim: 55b74ad1f7181d208980766216e5e206563377cd`, sonra gövde.

### Hikâye 3: tohum pepee-0010 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: minder kalesinin üstündeki yastık düştü | minderleri yaklaştırdı ve yastığı yeniden koydu
@tohum: pepee-0010
@degisim: şekerleme -> tabak
Evde, salonda iki büyük minder vardı. Pepee bu minderlerden bir kale yapıp kahvaltısını içinde yemek istiyordu. İki minderi yan yana koydu ve üstlerine uzun bir yastık yerleştirdi. Ama minderler birbirinden çok uzaktı ve yastık aşağı düştü. Pepee sandalyeye oturdu ve biraz düşündü. Sonra sandalyeden indi ve minderleri birbirine yaklaştırdı. Yastığı yeniden üstlerine koydu. Bu kez yastık düşmedi ve kale sağlam durdu. Pepee masadan tabağını getirdi. Tabakta yumurta, ballı ekmek ve tahin pekmez vardı. Artık Pepee hazırlıklıydı ve kalenin içine girdi. Yumurtasını ve ekmeğini orada afiyetle yedi. Pepee çok mutluydu, çünkü kalesinde kahvaltı yapmıştı.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İki minderi yan yana koydu"
   - Cümle 3: «İki minderi yan yana koydu ve üstlerine uzun bir yastık yerleştirdi.»
   - Açıklama: Minderler yan yana konmuşken hemen ardından birbirinden çok uzak oldukları söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "yastık aşağı düştü"
   - Cümle 4: «Ama minderler birbirinden çok uzaktı ve yastık aşağı düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Artık Pepee hazırlıklıydı"
   - Cümle 11: «Artık Pepee hazırlıklıydı ve kalenin içine girdi.»
   - Açıklama: 'Hazırlıklı' 3 yaşındaki çocuk için soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0010` birebir aynı, `@degisim: şekerleme -> tabak` (tutuyorsan), ardından `@onarim: 0a4a324d73f170ab9d79e19ca4284e0377ae3f0f`, sonra gövde.

### Hikâye 4: tohum pepee-0016 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0016
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yağmur ya da kar günü
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'pankek', fiil 'köpürmek', sıfat 'kırılgan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: yağmur başladı ve şapka ıslandı | ninesinden şemsiye isteyip onu açmayı öğrendi
@tohum: pepee-0016
@degisim: pankek -> şemsiye
Deniz kıyısında küçük dalgalar köpürüyordu. Pepee ile Nenee kumda oturmuş, denize bakıyordu. Birden yağmur başladı ve Pepee'nin mavi şapkası ıslandı. "Nineciğim, şemsiye var mı?" diye sordu Pepee. Nenee çantasından katlanmış bir şemsiye çıkardı. "Şemsiyeyi ben açabilir miyim?" diye sordu Pepee. "Tabii, ama yavaş aç, telleri kırılgan," dedi Nenee. Nenee ona küçük bir düğmeyi gösterdi. Pepee düğmeye bastı ve şemsiyeyi yavaşça yukarı itti. Şemsiye kocaman açıldı. İkisi şemsiyenin altına girdi ve artık hiç ıslanmadı. Yağmur damlaları şemsiyede tık tık ses yaptı. Pepee çok mutlu oldu, çünkü şemsiye açmayı kendisi öğrenmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yavaş aç, telleri kırılgan"
   - Cümle 7: «"Tabii, ama yavaş aç, telleri kırılgan," dedi Nenee.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0016` birebir aynı, `@degisim: pankek -> şemsiye` (tutuyorsan), ardından `@onarim: a6c2f7e784d53a6fcb5a42744b8b8ba70429b20f`, sonra gövde.

### Hikâye 5: tohum pepee-0017 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Şila
@tohum: pepee-0017
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'baharat', fiil 'sürmek', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Şila
@plan: salıncak gitmedi çünkü kuzeni ayaklarını sallamıyordu | dans ederek ayak hareketini ona gösterdi
@tohum: pepee-0017
@degisim: baharat -> salıncak
Hafif bir rüzgar esiyordu. Pepee ile Şila parkta salıncağa koştu. Şila salıncağa oturdu ama salıncak gitmedi, çünkü küçük ayaklarını hiç sallamıyordu. Pepee Şila'ya yardım etmek istedi. Salıncağın yanında dans etmeye başladı. Bir adım öne attı ve ayağını uzattı. Sonra geri çekildi ve ayağını büktü. Şila onu dikkatle izledi. Salıncakta o da aynısını yaptı. Salıncak bu kez durmadı ve sallanma uzun sürdü. Şila neşeyle güldü. Pepee bundan sonra Şila'ya yeni hareketleri hep önce kendisi gösterdi.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "salıncak gitmedi çünkü kuzeni"
   - Cümle 0 (plan satırı): «salıncak gitmedi çünkü kuzeni ayaklarını sallamıyordu | dans ederek ayak hareketini ona gösterdi»
   - Açıklama: Salıncak 'gitmez'; 'sallanmadı' olmalı.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kuzeni ayaklarını sallamıyordu"
   - Cümle 0 (plan satırı): «salıncak gitmedi çünkü kuzeni ayaklarını sallamıyordu | dans ederek ayak hareketini ona gösterdi»
   - Açıklama: Plan Şila'yı kuzen olarak anıyor ama gövdede böyle bir bağ hiç söylenmiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama salıncak gitmedi"
   - Cümle 3: «Şila salıncağa oturdu ama salıncak gitmedi, çünkü küçük ayaklarını hiç sallamıyordu.»
   - Açıklama: Salıncak gitmez, sallanır; fiil öznesine uymuyor.
   - Açıklama: Salıncak 'gitmez'; fiil öznesine uymuyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü küçük ayaklarını hiç sallamıyordu"
   - Cümle 3: «Şila salıncağa oturdu ama salıncak gitmedi, çünkü küçük ayaklarını hiç sallamıyordu.»
   - Açıklama: Son özne salıncak olduğu için ayaklarını kimin sallamadığı dilbilgisel olarak belirsiz.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "küçük ayaklarını hiç sallamıyordu"
   - Cümle 3: «Şila salıncağa oturdu ama salıncak gitmedi, çünkü küçük ayaklarını hiç sallamıyordu.»
   - Açıklama: Son özne salıncak olduğu için ayakları sallamayanın kim olduğu belirsiz.
6. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Pepee bundan sonra Şila'ya yeni hareketleri hep önce kendisi gösterdi"
   - Cümle 12: «Pepee bundan sonra Şila'ya yeni hareketleri hep önce kendisi gösterdi.»
   - Açıklama: Kartın yanlar alanında Şila çok güzel dans eden kuzen olarak geçiyor; ona hareket öğretilen, ayağını sallamayı bilmeyen küçük biri gibi gösterilmesi yanlış bilgi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0017` birebir aynı, `@degisim: baharat -> salıncak` (tutuyorsan), ardından `@onarim: 73d8c2bb4bc31d424f980587a33a9c69b38e13b8`, sonra gövde.

### Hikâye 6: tohum pepee-0019 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Bebee
@tohum: pepee-0019
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'yama', fiil 'bağlamak', sıfat 'sevecen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Bebee
@plan: sepetin kapağı açılıyordu çünkü ipi çözüldü | kardeşinden kapağı tutmasını isteyip ipi bağladı
@tohum: pepee-0019
@degisim: yama -> sepet
Parkta güneş parlıyordu. Pepee kahvaltı sepetini taşıyordu, Bebee de yanında yürüyordu. Ama sepet çok doluydu ve kapağın ipi çözüldü. Kapak hep açılıyordu ve Pepee ipi tek başına bağlayamadı. "Bebee, kapağı tutar mısın?" diye sordu Pepee. Sevecen kardeşi hemen geldi ve kapağı iki eliyle tuttu. Pepee ipi sıkıca bağladı. Kapak bir daha açılmadı. İkisi sepeti kaydırağın yanına götürdü. Orada Pepee ipi çözdü ve yumurta ile balı çıkardı. Bebee ekmeğini bala batırdı ve güldü. "Teşekkürler, Bebee, sen çok iyi bir kardeşsin!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "açılıyordu çünkü ipi çözüldü"
   - Cümle 0 (plan satırı): «sepetin kapağı açılıyordu çünkü ipi çözüldü | kardeşinden kapağı tutmasını isteyip ipi bağladı»
   - Açıklama: Plan satırında zaman uyumu bozuk; 'ipi çözülmüştü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0019` birebir aynı, `@degisim: yama -> sepet` (tutuyorsan), ardından `@onarim: aa78c04aa19e7972df933f357f1bcd77c69b5b1e`, sonra gövde.

### Hikâye 7: tohum pepee-0021 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0021
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çit', fiil 'rahatlatmak', sıfat 'şanslı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: rüzgar esti ve çitin iki dalı düştü | kalın dallar bulup toprağa sıkıca dikti
@tohum: pepee-0021
@degisim: rahatlatmak -> dikmek
Bir sabah Pepee ormanda evcilik oynuyordu. Dallardan küçük bir çit yaptı ve içine taştan bir masa kurdu. Ama rüzgar esti ve çitin iki dalı yere düştü. Artık çitin bir yanı açık kaldı. Pepee kahvaltıyı çok severdi ve bu masada yemek yiyecekti. Bu yüzden çitin tam olmasını istedi. Pepee şanslıydı, çünkü ağacın altında kalın dallar vardı. İki dal seçti ve onları toprağa sıkıca dikti. Bu kez rüzgar esti ama dallar düşmedi. Pepee masaya yaprak tabaklar koydu. Beyaz taşlar yumurta, sarı çiçekler bal oldu. Sonra Pepee kahvaltısını yer gibi yaptı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee ormanda evcilik oynuyordu"
   - Cümle 1: «Bir sabah Pepee ormanda evcilik oynuyordu.»
   - Açıklama: Dört yaşındaki Pepee ormanda yanında hiçbir büyük olmadan tek başına oynuyor; güvenli kullanım satırı bir büyüğün yanında olmayı öngörüyor ve çocuk bunu taklit edebilir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve çitin iki dalı yere düştü"
   - Cümle 3: «Ama rüzgar esti ve çitin iki dalı yere düştü.»
   - Açıklama: İki dalın düşüp yeniden dikilmesi önemsiz bir sorun; kahvaltı için çitin tam olması gerektiği de akla yatkın değil.
   - Açıklama: İki dalın düşüp yeniden dikilmesi önemsiz bir olay; 'rüzgar dağıttı, topladı, bitti' türünde bir sorun.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden çitin tam olmasını istedi"
   - Cümle 6: «Bu yüzden çitin tam olmasını istedi.»
   - Açıklama: Kahvaltıyı sevmesinden çitin tam olması gerektiği sonucu çıkmıyor; bağ sebepsiz kuruluyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee şanslıydı, çünkü ağacın altında kalın dallar vardı"
   - Cümle 7: «Pepee şanslıydı, çünkü ağacın altında kalın dallar vardı.»
   - Açıklama: Çözümü getiren kalın dallar şans eseri, sebepsizce beliriyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sarı çiçekler bal oldu"
   - Cümle 11: «Beyaz taşlar yumurta, sarı çiçekler bal oldu.»
   - Açıklama: Çiçeklerin bal olması oyun mecazı; 3 yaşındaki çocuk gerçek dönüşüm sanabilir.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Beyaz taşlar yumurta, sarı çiçekler bal oldu"
   - Cümle 11: «Beyaz taşlar yumurta, sarı çiçekler bal oldu.»
   - Açıklama: Taşların yumurta, çiçeklerin bal olması mecazlı bir anlatım; küçük çocuk için kafa karıştırıcı.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Pepee kahvaltısını yer gibi yaptı"
   - Cümle 12: «Sonra Pepee kahvaltısını yer gibi yaptı ve oyununa mutlu mutlu devam etti.»
   - Açıklama: Tohumdaki kahvaltı özelliği iki kez geçiyor ve sorunun çözümünde işe yaramıyor, yalnız gerekçe ve süs olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0021` birebir aynı, `@degisim: rahatlatmak -> dikmek` (tutuyorsan), ardından `@onarim: 18e01c9bde1f1df64791d6ccc8b73ed43b175491`, sonra gövde.

### Hikâye 8: tohum pepee-0022 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0022
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'yemek', fiil 'oynatmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: ağacın altına girince gölgesi kayboldu | güneşli bir yere yürüdü ve gölgesiyle dans etti
@tohum: pepee-0022
@degisim: yemek -> gölge
Ormanda, Pepee mavi şapkasına çiçek takmıştı ve şapkası çok süslüydü. Pepee çiçeklerin yanında, yerde kendi gölgesini fark etti. Gölgesiyle dans etmek istedi ama büyük bir ağacın altına girince gölgesi kayboldu. Pepee biraz düşündü ve çevresine baktı. İleride güneşin vurduğu açık bir yer vardı. Pepee oraya yürüdü ve gölgesi yeniden göründü. Sonra kollarını oynattı ve dans etti. Gölgedeki çiçekli şapka da onunla birlikte sallandı. Pepee tek ayağının üstünde döndü, gölge de döndü. Sonra kahkahalarla güldü. Pepee bundan sonra gölgesiyle oynamak için güneşli yerleri seçti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Gölgedeki çiçekli şapka da"
   - Cümle 8: «Gölgedeki çiçekli şapka da onunla birlikte sallandı.»
   - Açıklama: 'Gölgedeki' hem gölgelik yer hem şapkanın gölgesi anlamına gelebiliyor; kastedilen şapkanın gölgesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0022` birebir aynı, `@degisim: yemek -> gölge` (tutuyorsan), ardından `@onarim: a98e83edda3badb7566001c0747c87d16100fa79`, sonra gövde.

### Hikâye 9: tohum pepee-0023 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0023
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'eşarp', fiil 'hazırlamak', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: dans ederken nereden geldiği bilinmeyen bir ses duydu | kovasına ve cebine baktı ve kabukları buldu
@tohum: pepee-0023
@degisim: eşarp -> kabuk
Bir sabah Pepee deniz kıyısında yeni bir dans hazırlıyordu. Kumda her zıpladığında küçük bir ses duyuldu. Pepee bu sesin nereden geldiğini çok merak etti. Önce kovasına baktı ama kova bomboştu. Ses ona çok yakından geliyordu. Pepee elini tulumunun cebine soktu ve iki küçük kabuk çıkardı. Onları dansa başlamadan önce kıyıda toplamıştı. Zıplayınca kabuklar birbirine çarpıyor ve ses yapıyordu. Pepee kabukları avucunda salladı ve güldü. Pepee çok sevindi, çünkü dansı için güzel bir ses bulmuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "her zıpladığında küçük bir ses duyuldu"
   - Cümle 2: «Kumda her zıpladığında küçük bir ses duyuldu.»
   - Açıklama: 'Her zıpladığında' tekrar bildirir; fiil 'duyuluyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0023` birebir aynı, `@degisim: eşarp -> kabuk` (tutuyorsan), ardından `@onarim: adcdd6720008cebbe8c2a7d39eb1ead8aa3cca5d`, sonra gövde.

### Hikâye 10: tohum pepee-0024 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0024
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kırıntı', fiil 'ışıldamak', sıfat 'çalışkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: dedenin anahtarı yaprakların arasına düştü | güneşte parlayan yere bakıp anahtarı buldu
@tohum: pepee-0024
@degisim: kırıntı -> anahtar
Ormanda serin bir rüzgar esiyordu. Pepee ile Dedee ağaçların arasında yürüyordu. Birden Dedee durdu, çünkü ev anahtarı cebinden düşmüştü. "Anahtar bu yaprakların arasında olmalı," dedi Dedee. Ama yerde çok yaprak vardı. "Dedeciğim, anahtarı nasıl buluruz?" diye sordu Pepee. "Güneş vurunca anahtar parlar," dedi Dedee. Pepee yeni şeyler öğrenmeyi çok severdi ve bunu hemen denedi. Eğildi ve güneşli yerlere dikkatle baktı. Bir çalının dibinde küçük bir şey ışıldadı. Pepee yaprağı kaldırdı ve anahtarı buldu. "Sen çok çalışkansın, Pepee," dedi Dedee. Pepee çok sevindi, çünkü dedesine yardım etmişti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bunu hemen denedi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi çok severdi ve bunu hemen denedi.»
   - Açıklama: 'Bunu' zamirinin dedenin önerisini mi öğrenmeyi mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0024` birebir aynı, `@degisim: kırıntı -> anahtar` (tutuyorsan), ardından `@onarim: fd414da109b951f6446f3fc156fced4f58132e22`, sonra gövde.

### Hikâye 11: tohum pepee-0025 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0025
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'yelken', fiil 'yağmak', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: yağmur başladı ve örtünün üstüne damlalar düştü | örtüyü sık yapraklı ağacın altına taşıdı
@tohum: pepee-0025
@degisim: yelken -> örtü
Pepee ormanda kardeşi Bebee için sürpriz bir kahvaltı kuruyordu. Bebee gözlerini kapatmış, bir taşın üstünde bekliyordu. Ama yağmur yağmaya başladı ve örtünün üstüne damlalar düştü. Yakında yaprakları sık, büyük bir ağaç vardı. Pepee örtüyü dört ucundan topladı ve ağacın altına taşıdı. Sonra Bebee'nin elinden tuttu ve onu da oraya götürdü. Orada hiç damla düşmüyordu. Pepee örtüyü yeniden serdi ve yumurtayla balı dizdi. "Gözlerini aç, Bebee, sofra hazır!" dedi Pepee. Bebee baktı ve sevinçle el çırptı. "Bana tahin pekmez de getirdin mi?" diye sordu Bebee. "Evet, senin için getirdim," dedi Pepee. Pepee ile Bebee ağacın altında mutlu mutlu yemeğe başladı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sürpriz bir kahvaltı kuruyordu"
   - Cümle 1: «Pepee ormanda kardeşi Bebee için sürpriz bir kahvaltı kuruyordu.»
   - Açıklama: Kahvaltı kurulmaz; 'sofra kurmak' ya da 'kahvaltı hazırlamak' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bana tahin pekmez de getirdin mi?"
   - Cümle 11: «"Bana tahin pekmez de getirdin mi?" diye sordu Bebee.»
   - Açıklama: Sofraya konmayan tahin pekmez sonradan sebepsiz beliriyor ve olayda işlevi yok.
   - Açıklama: Tahin pekmez daha önce hiç kurulmadan sorun çözüldükten sonra sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0025` birebir aynı, `@degisim: yelken -> örtü` (tutuyorsan), ardından `@onarim: acbb44169529a16e7df5b5bfc974f46efaf5e14d`, sonra gövde.

### Hikâye 12: tohum pepee-0026 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Şila
@tohum: pepee-0026
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mobilya', fiil 'değişmek', sıfat 'gri'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Şila
@plan: kar tanesi sıcak elde hemen su oldu | kar tanesini soğuk kolunda yakaladı
@tohum: pepee-0026
@degisim: mobilya -> kapı
Evde, kapının önünde Pepee ile Şila karı izliyordu. Pepee bir kar tanesini yakından görmek istedi. Ama kar tanesi sıcak eline düşünce hemen değişti ve su oldu. Gri bulutlardan yine kar yağıyordu. "Kolun soğuk, Pepee, kar orada hemen su olmaz," dedi Şila. Pepee yeni şeyler öğrenmeyi severdi ve kolunu hemen uzattı. Mavi koluna bir kar tanesi kondu. Bu kez kar tanesi erimedi. Pepee yakından baktı ve minik bir yıldız gördü. "Şila, bak, kar tanesi yıldız gibi!" dedi Pepee. Şila da yanına gelip baktı ve güldü. Pepee çok sevindi, çünkü kar tanesini sonunda yakından görmüştü.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kolun soğuk, Pepee, kar orada hemen su olmaz"
   - Cümle 5: «"Kolun soğuk, Pepee, kar orada hemen su olmaz," dedi Şila.»
   - Açıklama: Çözüm fikrini Pepee değil Şila buluyor.
   - Açıklama: Çözüm fikrini Pepee değil Şila buluyor; Pepee yalnız söyleneni uyguluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0026` birebir aynı, `@degisim: mobilya -> kapı` (tutuyorsan), ardından `@onarim: cfbda249ef39215978da9816ddcbbd7d57a76766`, sonra gövde.
