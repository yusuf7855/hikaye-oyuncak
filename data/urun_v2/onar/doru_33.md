# Editör görevi (onarım): Doru, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar33.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0132 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0132
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kalıp', fiil 'basmak', sıfat 'üzgün'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: yumuşak toprakta ayakları battı ve yavaş koştu | annesini izleyip sert ve düz yolu buldu
@tohum: doru-0132
@degisim: kalıp -> iz
Rüzgar dağda hafif hafif esiyordu. Doru ile annesi sırayla yalnız ağaca kadar koşup dönüyordu. Ama Doru'nun sırasında ayakları yumuşak toprağa battı. Doru her bastığı yerde derin bir iz bıraktı ve yavaş koştu. Doru geç döndü ve biraz üzgündü. "Sıra bende," dedi annesi ve taşların yanındaki sert yoldan koştu. Doru annesinin yolunu dikkatle izledi. "Sıra sende, Doru," dedi annesi. Doru bu kez sert ve düz yoldan hızla koştu. Bu kez çok çabuk geri döndü. "Aferin, Doru!" dedi annesi. Doru çok sevindi, çünkü sert yolu bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sırayla yalnız ağaca kadar"
   - Cümle 2: «Doru ile annesi sırayla yalnız ağaca kadar koşup dönüyordu.»
   - Açıklama: 'Yalnız' hem 'sadece' hem 'tek başına duran' anlamına gelebiliyor; kelimenin anlamı belirsiz.
   - Açıklama: 'Yalnız' hem 'tek başına duran' hem 'sadece' anlamına gelebiliyor; anlam belirsiz.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu kez çok çabuk"
   - Cümle 10: «Bu kez çok çabuk geri döndü.»
   - Açıklama: 'Bu kez' art arda iki cümlede gereksiz yere tekrarlanıyor.
   - Açıklama: 'Bu kez' art arda iki cümlede gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0132` birebir aynı, `@degisim: kalıp -> iz` (tutuyorsan), ardından `@onarim: 503d4400f4367fa58b6a7d33c81d69f1b52b75b6`, sonra gövde.

### Hikâye 2: tohum doru-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0133
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'koza', fiil 'uzamak', sıfat 'şapkalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: küçük atın sırasında uzun otlar önünü kapattı | otları burnuyla iki yana itti
@tohum: doru-0133
Doru ormanda Alaca ile sırayla bir bulma oyunu oynuyordu. Doru ilk olarak ağacın dibinde şapkalı bir mantar buldu. Ama Alaca'nın sırası gelince uzun otlar önünü kapattı. Otlar çok uzamıştı ve küçük Alaca onların üstünden bakamıyordu. "Burada hiçbir şey göremiyorum," dedi Alaca. Doru yardım etmek için burnuyla otları iki yana itti. Otların arasında alçak bir dal göründü. Dalın ucunda küçük, beyaz bir koza asılıydı. "Bir koza buldum!" dedi Alaca sevinçle. "Aferin, Alaca, şimdi sıra yine bende," dedi Doru. Doru çok sevindi, çünkü Alaca da oyunda güzel bir şey bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, beyaz bir koza"
   - Cümle 8: «Dalın ucunda küçük, beyaz bir koza asılıydı.»
   - Açıklama: 'Koza' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Koza' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0133` birebir aynı, ardından `@onarim: ae3e0a1883e76c856290fb1847f9eb4285d7d1e2`, sonra gövde.

### Hikâye 3: tohum doru-0134 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0134
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'örgü', fiil 'gitmek', sıfat 'uzak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: küçük at saklanırken yolunu kaybetti | sesini duyup koştu ve onu geri getirdi
@tohum: doru-0134
@degisim: örgü -> ağaç
Ormanda Doru ile Alaca saklambaç oynuyordu. Alaca saklanmak için ağaçların arasında ileri gitti. Sonra geri dönmek istedi ama yolu bulamadı. "Doru, neredesin?" diye seslendi Alaca. Doru bu sesi uzaktan duydu. Hemen ağaçların arasındaki düz yolda hızla koştu. Az sonra Alaca'yı büyük bir ağacın altında buldu. "Seni buldum, Alaca!" dedi Doru. "İyi ki geldin, Doru," dedi Alaca. "Benim arkamdan gel," dedi Doru. Alaca onun arkasından yürüdü ve oyun yerine döndüler. Sonra Doru ile Alaca, yakın ağaçların arasında oyunlarına devam etti.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "geri dönmek istedi ama yolu bulamadı"
   - Cümle 3: «Sonra geri dönmek istedi ama yolu bulamadı.»
   - Açıklama: Küçük Alaca'nın ormanda kaybolması 3-6 yaş için korkutucu bir öğe olabilir.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ağaçların arasındaki düz yolda hızla koştu"
   - Cümle 6: «Hemen ağaçların arasındaki düz yolda hızla koştu.»
   - Açıklama: Güvenli kullanım satırı hızı açık ve düz yerde gösterir; ağaçlar arasında koşuluyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra Doru ile Alaca, yakın ağaçların arasında oyunlarına devam etti"
   - Cümle 12: «Sonra Doru ile Alaca, yakın ağaçların arasında oyunlarına devam etti.»
   - Açıklama: Son cümle his ya da sıcak bir kapanış taşımayan çıplak bir eylemle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0134` birebir aynı, `@degisim: örgü -> ağaç` (tutuyorsan), ardından `@onarim: 44f8e976891af7d843e72bbecd17b93309c705ac`, sonra gövde.

### Hikâye 4: tohum doru-0136 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0136
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'su', fiil 'yapışmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: yuvarlanırken başkasının yiyeceği yonca yapraklarını ezdi | özür diledi ve hızla koşup yeni yonca getirdi
@tohum: doru-0136
@degisim: su -> yonca
Çayırda Kırat taze yonca yaprakları yiyordu. Doru oyun oynarken yaprakların üstünde yuvarlandı. Yapraklar ezildi ve Kırat onları yiyemedi. Birkaç yaprak Doru'nun sırtına yapışmıştı. Kırat sessizce Doru'ya baktı. Doru bunu görünce çok üzüldü. "Özür dilerim, Kırat, sana yeni yonca getireceğim," dedi Doru. Doru çayırın öbür ucuna hızla koştu. Orada ağzını taze yonca ile doldurdu. Sonra geri gelip yaprakları Kırat'ın önüne bıraktı. Kırat yaprakları yedi ve çok memnun oldu. "Teşekkürler, Doru, bu yonca çok tatlı!" dedi Kırat.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda Kırat taze yonca"
   - Cümle 1: «Çayırda Kırat taze yonca yaprakları yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birkaç yaprak Doru'nun sırtına yapışmıştı"
   - Cümle 4: «Birkaç yaprak Doru'nun sırtına yapışmıştı.»
   - Açıklama: Sırta yapışan yapraklar bir daha kullanılmayan işlevsiz bir ayrıntı.
   - Açıklama: Sırta yapışan yapraklar kuruluyor ama olayda hiçbir işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yedi ve çok memnun oldu"
   - Cümle 11: «Kırat yaprakları yedi ve çok memnun oldu.»
   - Açıklama: 'Memnun' 3 yaşındaki çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0136` birebir aynı, `@degisim: su -> yonca` (tutuyorsan), ardından `@onarim: 99c0c2f2ea63d2eb1852778b15efaef07142ae90`, sonra gövde.

### Hikâye 5: tohum doru-0137 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0137
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fener', fiil 'tasarlamak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar son dalı dereye düşürdü ve oyun bozuldu | cesurca dereye girip dalı ağzıyla geri getirdi
@tohum: doru-0137
@degisim: fener -> dal
Vadide Doru yeni bir atlama oyunu tasarladı. Kuru dalları derenin yanına dalgalı bir çizgi gibi dizdi. Ama birden rüzgar esti ve son dal dereye düştü. Dal suyun ortasında bir taşa takıldı. Doru suya girmeye önce biraz çekindi. Dere derin değildi ama suyu çok soğuktu. Doru cesur davrandı ve yavaşça suya girdi. Dalı ağzıyla tuttu ve kıyıya getirdi. Sonra dalı çizginin sonuna geri koydu. Doru dalların üstünden tek tek atladı. Hiçbir dala çarpmadı ve oyunu bitirdi. Doru çok sevindi, çünkü kendi oyununu sonuna kadar oynamıştı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir atlama oyunu tasarladı"
   - Cümle 1: «Vadide Doru yeni bir atlama oyunu tasarladı.»
   - Açıklama: 'Tasarlamak' 3 yaşındaki bir çocuğun bildiği bir kelime değil.
   - Açıklama: 'Tasarladı' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve son dal dereye düştü"
   - Cümle 3: «Ama birden rüzgar esti ve son dal dereye düştü.»
   - Açıklama: Rüzgarın oyun dalını dağıtması önemsiz bir olay; dal geri getirilip bitiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru suya girmeye önce biraz çekindi"
   - Cümle 5: «Doru suya girmeye önce biraz çekindi.»
   - Açıklama: 'Çekinmek' ayrılma hali ister; 'suya girmekten çekindi' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "suya girmeye önce biraz çekindi"
   - Cümle 5: «Doru suya girmeye önce biraz çekindi.»
   - Açıklama: 'Çekinmek' 3 yaşındaki çocuk için ağır bir kelime.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yavaşça suya girdi"
   - Cümle 7: «Doru cesur davrandı ve yavaşça suya girdi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde soğuk dereye giriliyor.
   - Açıklama: Doru soğuk dere suyuna giriyor; çocuğun taklit edebileceği biçimde suya girme davranışı var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0137` birebir aynı, `@degisim: fener -> dal` (tutuyorsan), ardından `@onarim: 53a62f1dd69c3de3d58140ce9b482da07b202aa0`, sonra gövde.

### Hikâye 6: tohum doru-0139 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0139
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kartopu', fiil 'saklamak', sıfat 'sisli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: kartopu sisli vadide bir taşın arkasında kayboldu | hızla her taşın arkasına bakıp kartopu buldu
@tohum: doru-0139
Bir sabah Doru ile Karatay sisli vadide oyun oynuyordu. Karatay büyük bir kartopu yaptı ve bir taşın arkasına sakladı. Ama sis yüzünden hangi taş olduğunu unuttu. Vadide çok taş vardı. "Doru, kartopu kayboldu!" dedi Karatay. "Sen burada bekle, ben bakarım," dedi Doru. Doru düz vadide taştan taşa hızla koştu. Her taşın arkasına baktı. Beşinci taşın arkasında beyaz bir kartopu duruyordu. "Buldum, Karatay, buraya gel!" dedi Doru. Karatay sevinçle yanına geldi. Sonra iki arkadaş kartopu ile mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "her taşın arkasına bakıp kartopu buldu"
   - Cümle 0 (plan satırı): «kartopu sisli vadide bir taşın arkasında kayboldu | hızla her taşın arkasına bakıp kartopu buldu»
   - Açıklama: Belirli nesne belirtme eki eksik; 'kartopunu buldu' olmalı.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Karatay büyük bir kartopu yaptı"
   - Cümle 2: «Karatay büyük bir kartopu yaptı ve bir taşın arkasına sakladı.»
   - Açıklama: Bir at kartopu yapamaz; kartın tür alanına aykırı yanlış bilgi.
   - Açıklama: Kartta atların kartopu yapıp saklama yeteneği yok; diziyi izleyen çocuğun tanıdığı dünyaya uymuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Karatay büyük bir kartopu yaptı ve bir taşın arkasına sakladı"
   - Cümle 2: «Karatay büyük bir kartopu yaptı ve bir taşın arkasına sakladı.»
   - Açıklama: Kartopu kolayca yeniden yapılabileceğinden kaybolması çocuk için önemsiz bir sorun.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Karatay büyük bir kartopu yaptı"
   - Cümle 2: «Karatay büyük bir kartopu yaptı ve bir taşın arkasına sakladı.»
   - Açıklama: Karlı vadide bir kartopunun kaybolması önemsiz bir sorun; yenisi hemen yapılabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0139` birebir aynı, ardından `@onarim: e355c6152fc552a00f22ff89ebfaad82b3aaff6c`, sonra gövde.

### Hikâye 7: tohum doru-0140 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0140
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gökkuşağı', fiil 'taşınmak', sıfat 'garip'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: renkli tüy rüzgarla uzun otların arasına taşındı | cesurca sık otlara girip tüyü buldu
@tohum: doru-0140
@degisim: gökkuşağı -> tüy
Bir sabah Kırat dağda garip, renkli bir tüy buldu. Tüyü Doru'ya göstermek için bir taşın üstüne koydu. Ama birden rüzgar esti ve tüy uzun otların arasına taşındı. Otlar çok sık ve uzundu. Doru önce durdu, çünkü otların içi görünmüyordu. Sonra cesur davrandı ve otların arasına girdi. Burnuyla otları iki yana itti ve yere baktı. Renkli tüy bir otun dibinde duruyordu. Doru tüyü dişleriyle tuttu ve Kırat'a getirdi. "İşte tüyün, Kırat," dedi Doru. "Teşekkürler, Doru, onu çok seviyorum," dedi Kırat. Doru çok sevindi, çünkü Kırat'ın tüyünü geri getirmişti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesur davrandı ve otların arasına girdi"
   - Cümle 6: «Sonra cesur davrandı ve otların arasına girdi.»
   - Açıklama: İçi görünmeyen sık otlara girmek cesaret olarak övülüyor ve çocuk için taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0140` birebir aynı, `@degisim: gökkuşağı -> tüy` (tutuyorsan), ardından `@onarim: e7e486ebed884db7d7da6e55f4b03d33f257c930`, sonra gövde.

### Hikâye 8: tohum doru-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0143
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'torba', fiil 'yaslanmak', sıfat 'çabuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşının kuyruğu sık bir çalıya takıldı | dişleriyle dalları ayırıp arkadaşını kurtardı
@tohum: doru-0143
@degisim: torba -> çalı
Bir sabah Doru ile Karatay dağda yürüyordu. Karatay dinlenmek için sık bir çalıya yaslandı. Ama uzun kuyruğu dallara takıldı ve çıkamadı. "Doru, kuyruğum sıkıştı!" dedi Karatay. Karatay kuyruğunu çekip kurtarmak istedi. "Dur, Karatay, ben sana yardım ederim," dedi Doru. Doru dişleriyle dalları tek tek tuttu ve yana çekti. Dalların arasında bir boşluk açıldı. Karatay çabuk bir adım attı ve kuyruğu dışarı çıktı. "Teşekkürler, Doru, kuyruğum yine serbest!" dedi Karatay. Doru çok sevindi, çünkü arkadaşı çalıdan kurtulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuyruğum yine serbest!"
   - Cümle 10: «"Teşekkürler, Doru, kuyruğum yine serbest!" dedi Karatay.»
   - Açıklama: 'Serbest' soyut bir kelime ve 3 yaşındaki bir çocuk bunu bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0143` birebir aynı, `@degisim: torba -> çalı` (tutuyorsan), ardından `@onarim: 197b0610637201a06356530146409fc69ece81ee`, sonra gövde.

### Hikâye 9: tohum doru-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0144
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kürek', fiil 'açmak', sıfat 'soğuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: büyük bir kütük dar yolu kapattı | cesaretle küçük arkadaşından yardım istedi ve kütüğü birlikte ittiler
@tohum: doru-0144
@degisim: kürek -> kütük
Ormanda soğuk bir rüzgar esiyordu. Doru ile Alaca ormandaki güneşli açıklığa gitmek istiyordu. Ama dar yola büyük bir kütük düşmüştü ve yol kapanmıştı. Doru kütüğü tek başına itti ama kütük kıpırdamadı. Alaca çok küçüktü ve Doru ondan yardım istemeye çekindi. Sonra cesur davrandı ve Alaca'ya döndü. "Alaca, bana yardım eder misin?" diye sordu Doru. "Tabii, Doru, birlikte itelim," dedi Alaca. İkisi yan yana durdu ve kütüğü itti. Kütük yavaşça yuvarlandı ve yolun kenarına düştü. İkisi hemen güneşli açıklığa koştu. Doru çok sevindi, çünkü Alaca'dan yardım isteyip yolu açmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yardım istemeye çekindi"
   - Cümle 5: «Alaca çok küçüktü ve Doru ondan yardım istemeye çekindi.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0144` birebir aynı, `@degisim: kürek -> kütük` (tutuyorsan), ardından `@onarim: 74f853ae31c4d580c1bcfcc144dd815be7a1c617`, sonra gövde.
