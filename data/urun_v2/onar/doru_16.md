# Editör görevi (onarım): Doru, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0026 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0026
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bulut', fiil 'giydirmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: sırası gelince rüzgar bulutun gölgesini uzağa götürdü | düz vadide hızla koşup gölgenin üstüne bastı
@tohum: doru-0026
@degisim: giydirmek -> koşmak
Doru ile annesi vadide sırayla gölgeye basma oyunu oynuyordu. Önce annesi koştu ve büyük bir bulutun gölgesine bastı. Şimdi sıra Doru'daydı, ama rüzgar bulutu uzağa götürüyordu. Bulutun gölgesi de çimenlerin üstünde vadinin öbür ucuna gidiyordu. "Acele et, Doru, gölge gidiyor!" dedi annesi. Doru gölgenin gittiği yere baktı. Orada vadi açık ve düzdü. Annesi meraklı gözlerle onu izledi. Doru hızla koştu ve az sonra gölgenin yanına vardı. Sonra dört ayağıyla gölgenin içine bastı. "Bastım, anne!" dedi Doru. Annesi de yanına geldi ve güldü. "Çok güzel oynadın, Doru!" dedi annesi. "Teşekkürler, anneciğim, şimdi yine sıra sende!" dedi Doru.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sırası gelince rüzgar bulutun"
   - Cümle 0 (plan satırı): «sırası gelince rüzgar bulutun gölgesini uzağa götürdü | düz vadide hızla koşup gölgenin üstüne bastı»
   - Açıklama: Plan satırında 'sırası' kimin sırası belli değil; özne rüzgar olduğu için rüzgarın sırası gibi okunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0026` birebir aynı, `@degisim: giydirmek -> koşmak` (tutuyorsan), ardından `@onarim: 62ffe536674b1a3b3b2474abe3bc28ef9799048d`, sonra gövde.

### Hikâye 2: tohum doru-0031 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0031
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'salatalık', fiil 'sabırsızlanmak', sıfat 'şık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: ağaçta tek elma vardı ve ikisi de acıkmıştı | hızla koşup elmayı getirdi ve yarısını arkadaşına verdi
@tohum: doru-0031
@degisim: salatalık -> elma
Dağda, vadinin öbür ucunda küçük bir elma ağacı vardı. Doru ağacın alçak dalında kırmızı, şık bir elma gördü. Elma bir taneydi, ama Doru da Karatay da acıkmıştı. Karatay sabırsızlandı ve yerinde zıpladı. "Elmayı getireyim, ikimiz paylaşalım," dedi Doru. Doru düz vadide hızla koştu. Ağaca varınca elmayı dişleriyle daldan kopardı. Sonra Karatay'ın yanına geri döndü. Elmanın yarısını yedi ve öbür yarısını Karatay'a verdi. "Teşekkürler, Doru, çok tatlıymış," dedi Karatay. Doru bundan sonra bulduğu her elmayı arkadaşıyla paylaştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kırmızı, şık bir elma"
   - Cümle 2: «Doru ağacın alçak dalında kırmızı, şık bir elma gördü.»
   - Açıklama: 'Şık' kelimesi elma için yanlış anlamda kullanılmış.
   - Açıklama: 'Şık' giysi ve görünüş için kullanılır, elmaya uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay sabırsızlandı ve yerinde"
   - Cümle 4: «Karatay sabırsızlandı ve yerinde zıpladı.»
   - Açıklama: 'Sabırsızlandı' 3 yaşındaki çocuk için soyut ve zor bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0031` birebir aynı, `@degisim: salatalık -> elma` (tutuyorsan), ardından `@onarim: d15db05c8c79d3254fb78eed8483f43cb348ccd6`, sonra gövde.

### Hikâye 3: tohum doru-0032 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0032
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kaktüs', fiil 'fısıldamak', sıfat 'gizemli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: çalının üstündeki çiçek açılıyordu ama annesi uzaktaydı | hızla koşup annesini çiçeğin yanına getirdi
@tohum: doru-0032
@degisim: kaktüs -> çalı
Dağda, geniş ve düz bir çimenlikte büyük bir çalı vardı. Doru çalının üstünde pembe bir tomurcuk gördü. Tomurcuk açılıyordu, ama Doru'nun annesi uzakta çimen yiyordu. Doru bu çiçeği annesine göstermek istedi. Çimenlikte hızla koştu ve annesinin yanına vardı. Sonra annesinin kulağına eğildi. "Anne, benimle gel, sana bir sürpriz var," diye fısıldadı Doru. Annesi bu gizemli sürprizi merak etti ve Doru'nun yanında çalıya yürüdü. Çalının üstündeki pembe çiçek tam açılmıştı. Annesi çiçeğe uzun uzun baktı. Doru sevinçle annesine sokuldu. "Ne güzel bir sürpriz, teşekkür ederim, Doru!" dedi annesi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tomurcuk açılıyordu, ama Doru'nun annesi uzakta çimen yiyordu"
   - Cümle 3: «Tomurcuk açılıyordu, ama Doru'nun annesi uzakta çimen yiyordu.»
   - Açıklama: Çiçek açık kalacağı için annenin uzakta olması gerçek bir sorun değil; acele için sebep yok.
   - Açıklama: Annenin uzakta olması belirgin bir sorun oluşturmuyor ve sorun açıkça konmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu gizemli sürprizi merak"
   - Cümle 8: «Annesi bu gizemli sürprizi merak etti ve Doru'nun yanında çalıya yürüdü.»
   - Açıklama: 'Gizemli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu gizemli sürprizi merak etti"
   - Cümle 8: «Annesi bu gizemli sürprizi merak etti ve Doru'nun yanında çalıya yürüdü.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0032` birebir aynı, `@degisim: kaktüs -> çalı` (tutuyorsan), ardından `@onarim: 0dd6c9e260d95321bab3fdc3f1dc4191a9ceee77`, sonra gövde.

### Hikâye 4: tohum doru-0034 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0034
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çit', fiil 'doğmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: bir kayanın arkasından garip bir ses geliyordu | sesi bulup fidanın üstündeki kuru dalı çekti
@tohum: doru-0034
@degisim: çit -> fidan
Bir sabah güneş dağın arkasından doğdu. Doru çimen yerken garip bir tak tak sesi duydu. Ses hiç durmadı ve Doru rahatça yiyemediği için mutsuz oldu. Ses büyük bir kayanın arkasından geliyordu ve Doru onu çok merak etti. Kayanın arkasına yavaşça yürüdü ve baktı. Orada küçük bir fidan vardı. Fidanın üstüne kuru ve uzun bir dal düşmüştü. Rüzgar esince dal kayaya çarpıyor ve ses çıkarıyordu. Doru sesi durdurmak ve fidana yardım etmek istedi. Kuru dalı dişleriyle tuttu ve kenara çekti. Dal artık kayaya çarpmadı ve ses de bitti. Doru orada çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Orada küçük bir fidan vardı."
   - Cümle 6: «Orada küçük bir fidan vardı.»
   - Açıklama: 'Fidan' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0034` birebir aynı, `@degisim: çit -> fidan` (tutuyorsan), ardından `@onarim: 682ec8ba5844ebed3c190011b82d66f275acd95f`, sonra gövde.

### Hikâye 5: tohum doru-0036 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0036
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'bambu', fiil 'seslenmek', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar en sevdiği dalı yokuştan aşağı yuvarladı | sürüye seslenip indi ve dalı çalıların arasında buldu
@tohum: doru-0036
@degisim: bambu -> dal
Rüzgar dağın üstünde esiyordu. Doru sürünün yanında en sevdiği uzun dalla oynuyordu. Birden rüzgar güçlendi ve dalı yokuştan aşağı yuvarladı. Doru dalı artık göremiyordu. Gitmeden önce sürüye seslendi ve sürü onu bekledi. Sonra yokuştan yavaş yavaş aşağı yürüdü. Dal, yokuşun dibindeki çalıların arasına girmişti. Çalılar çok sıktı, ama Doru cesaretle başını içeri uzattı. Dalı dişleriyle tuttu ve dışarı çekti. Dal çok sağlamdı ve hiç kırılmamıştı. Doru onu ağzında sürünün yanına taşıdı. Doru çok sevindi, çünkü en sevdiği oyuncağını yeniden bulmuştu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "rüzgar en sevdiği dalı"
   - Cümle 0 (plan satırı): «rüzgar en sevdiği dalı yokuştan aşağı yuvarladı | sürüye seslenip indi ve dalı çalıların arasında buldu»
   - Açıklama: Plan satırında öznesi rüzgar olduğu için 'en sevdiği' rüzgarı gösteriyor gibi okunuyor, dalın Doru'nun olduğu belli değil.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "sürüye seslendi ve sürü onu bekledi"
   - Cümle 5: «Gitmeden önce sürüye seslendi ve sürü onu bekledi.»
   - Açıklama: Arka plandaki çoğul canlı sürü Doru'yu bekleyerek olaya katılıyor.
   - Açıklama: Arka plandaki çoğul canlı olan sürü Doru'yu bekleyerek olaya katılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürüye seslendi ve sürü onu bekledi"
   - Cümle 5: «Gitmeden önce sürüye seslendi ve sürü onu bekledi.»
   - Açıklama: Belirsiz kelime sürü canlı bir rol olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0036` birebir aynı, `@degisim: bambu -> dal` (tutuyorsan), ardından `@onarim: 5aadb2ee73c5e5591d5ea7ca540838b63a4c1d1a`, sonra gövde.

### Hikâye 6: tohum doru-0037 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0037
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çam', fiil 'bozulmak', sıfat 'zarif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: rüzgar esti ve çiçek yığını bozuldu | hızla koşup yeni papatyalar getirdi
@tohum: doru-0037
@degisim: zarif -> beyaz
Doru, parktaki geniş çayırda, büyük bir çam ağacının altındaydı. Doru ağacın altında Alaca için çiçeklerden bir yığın yapmıştı. Ama birden rüzgar esti, yığın bozuldu ve çiçekler uçtu. Alaca da uzaktan ağaca doğru geliyordu. Çayırın öbür ucunda papatyalar vardı. Doru düz çayırda hızla koştu. Ağzıyla birçok papatya kopardı ve ağaca geri döndü. Tam o sırada Alaca geldi ve beyaz çiçeklere baktı. "Bunlar benim için mi, Doru?" diye sordu Alaca. "Evet, Alaca, hepsi senin," dedi Doru. Alaca sevinçle zıpladı. Doru da çok sevindi, çünkü sürprizini tam zamanında yeniden hazırlamıştı.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parktaki geniş çayırda"
   - Cümle 1: «Doru, parktaki geniş çayırda, büyük bir çam ağacının altındaydı.»
   - Açıklama: Kartın park tarifi sürünün otladığı çayırdır; dizide olmayan 'park' adı yeri insan yapımı bir park gibi gösteriyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru ağacın altında Alaca"
   - Cümle 2: «Doru ağacın altında Alaca için çiçeklerden bir yığın yapmıştı.»
   - Açıklama: Doru ve ağacın altında olduğu bir önceki cümlenin hemen ardından gereksizce tekrarlanıyor.
   - Açıklama: Bir önceki cümlede söylenen 'ağacın altında' yeri gereksiz yere tekrarlanıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "birden rüzgar esti, yığın bozuldu"
   - Cümle 3: «Ama birden rüzgar esti, yığın bozuldu ve çiçekler uçtu.»
   - Açıklama: Rüzgarın çiçek yığınını dağıtıp yenisinin toplanması istemdeki önemsiz 'rüzgar dağıttı, topladı, bitti' kalıbına düşüyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Alaca da uzaktan ağaca"
   - Cümle 4: «Alaca da uzaktan ağaca doğru geliyordu.»
   - Açıklama: 'da' bağlacı 'de' anlamı taşıyor ama başka gelen kimse yok; yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0037` birebir aynı, `@degisim: zarif -> beyaz` (tutuyorsan), ardından `@onarim: 88b6383d17896895862977bb41bb49852785fa5a`, sonra gövde.

### Hikâye 7: tohum doru-0038 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0038
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'paket', fiil 'rahatlatmak', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi | kozalağı dişleriyle çekip fidanı kurtardı
@tohum: doru-0038
@degisim: paket -> kozalak
Bir sabah gökyüzü mavi ve açıktı. Doru, parktaki geniş çayırda bir kozalağı burnuyla itip peşinden koşuyordu. Birden kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi. Doru fidana yardım etmek istedi. Kozalağı dişleriyle yavaşça tuttu ve dalların arasından çekti. Dallar kırılmadı ve fidan yeniden dik durdu. Fidanın yeniden dik durması Doru'yu çok rahatlattı. Doru kozalağı dikkatlice çayırın ortasına götürdü. Oyununa açık çimenlerde yine neşeyle devam etti. Doru bundan sonra kozalağı fidanlardan uzakta itti.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parktaki geniş çayırda bir kozalağı"
   - Cümle 2: «Doru, parktaki geniş çayırda bir kozalağı burnuyla itip peşinden koşuyordu.»
   - Açıklama: Kartın park tarifi yalnız sürünün çimen yediği çayırdır; dizide park yok ama metin parkı açıkça anıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Fidanın yeniden dik durması Doru'yu çok rahatlattı"
   - Cümle 7: «Fidanın yeniden dik durması Doru'yu çok rahatlattı.»
   - Açıklama: Soyut adlaşmış yapı ve 'rahatlattı' 3 yaşındaki çocuğa uygun değil.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Fidanın yeniden dik durması Doru'yu çok rahatlattı"
   - Cümle 7: «Fidanın yeniden dik durması Doru'yu çok rahatlattı.»
   - Açıklama: Önceki cümledeki 'fidan yeniden dik durdu' bilgisi gereksiz yere tekrarlanıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Fidanın yeniden dik durması"
   - Cümle 7: «Fidanın yeniden dik durması Doru'yu çok rahatlattı.»
   - Açıklama: Bir önceki cümledeki 'fidan yeniden dik durdu' gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0038` birebir aynı, `@degisim: paket -> kozalak` (tutuyorsan), ardından `@onarim: 4fd098304bd3a3b1e63f76f07a5dd851a447e17c`, sonra gövde.

### Hikâye 8: tohum doru-0040 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0040
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'misket', fiil 'karışmak', sıfat 'kolay'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: sürü gitmişti ve yerdeki izler karışmıştı | küçük arkadaşına yolu sordu ve hızla sürüye yetişti
@tohum: doru-0040
@degisim: misket -> iz
Dağda serin bir rüzgar esiyordu. Doru ile Alaca büyük bir kayanın yanında saklambaç oynuyordu. Oyun bitince Doru etrafına baktı ama sürü gitmişti. Yerde çok iz vardı ve bütün izler birbirine karışmıştı. Doru nereye gideceğini bilemedi. "Alaca, sürü hangi yoldan gitti, gördün mü?" diye sordu Doru. "Evet, saklanırken gördüm, sarı çiçekli yoldan gittiler," dedi Alaca. O yolu bulmak kolaydı. Sürü uzakta yürüyordu. Doru düz yolda hızla koştu, Alaca da arkasından geldi. Az sonra ikisi de sürünün yanındaydı. "Teşekkürler, Alaca, iyi ki sana sordum!" dedi Doru.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "baktı ama sürü gitmişti"
   - Cümle 3: «Oyun bitince Doru etrafına baktı ama sürü gitmişti.»
   - Açıklama: Genç atın sürüden ayrı kalıp yolunu bilememesi küçük çocuk için kaybolma korkusu yaratabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0040` birebir aynı, `@degisim: misket -> iz` (tutuyorsan), ardından `@onarim: e3dd1d67382e265af1dea8afc72d0fe00f09de19`, sonra gövde.

### Hikâye 9: tohum doru-0044 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0044
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gümüş', fiil 'kalmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: rüzgar küçük çiçeğe çok sert esiyordu | cesaretle çiçeğin önünde durup onu korudu
@tohum: doru-0044
@degisim: narin -> ince
Ormanda güçlü bir rüzgar esiyordu. Doru annesiyle ağaçların arasında yürüyordu. Birden yerde küçük bir çiçek gördü ve çiçek rüzgarda kırılmak üzereydi. Çiçek gümüş renkliydi ve sapı çok inceydi. "Anne, bak, rüzgar bu çiçeği sallıyor!" dedi Doru. "Evet, rüzgar çok sert," dedi annesi. "Ben onun önünde dururum, anne," dedi Doru. Rüzgar Doru'ya sert sert esti, ama Doru cesaretle yerinden ayrılmadı. Rüzgar artık çiçeğe gelmedi. Az sonra rüzgar yavaşladı. Annesi yanına geldi ve başını Doru'nun başına sürttü. Doru çok sevindi, çünkü küçük çiçek dik kalmıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çiçek gümüş renkliydi"
   - Cümle 4: «Çiçek gümüş renkliydi ve sapı çok inceydi.»
   - Açıklama: Çiçeğin gümüş rengi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ben onun önünde dururum"
   - Cümle 7: «"Ben onun önünde dururum, anne," dedi Doru.»
   - Açıklama: 'Onun' zamiri son anılan rüzgarı mı çiçeği mi gösteriyor belli değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rüzgar artık çiçeğe gelmedi"
   - Cümle 9: «Rüzgar artık çiçeğe gelmedi.»
   - Açıklama: 'Rüzgar çiçeğe gelmedi' fiili öznesine uygun değil; 'ulaşmadı' anlamı kastediliyor.
   - Açıklama: 'Rüzgar çiçeğe gelmedi' fiil öznesine uygun değil; 'çiçeğe ulaşmadı/değmedi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0044` birebir aynı, `@degisim: narin -> ince` (tutuyorsan), ardından `@onarim: eac674fb23d96aef73b795a3830bf76c6775d697`, sonra gövde.

### Hikâye 10: tohum doru-0045 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0045
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'havuç', fiil 'takmak', sıfat 'buzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: elma buzlu dallara takılmıştı ve dallar ses çıkarıyordu | cesaretle gidip elmayı aldı ve paylaştı
@tohum: doru-0045
@degisim: havuç -> elma
Bir sabah orman çok soğuktu ve Doru ile Karatay acıkmıştı. Rüzgar kırmızı bir elmayı buzlu bir çalının dallarına takmıştı. Ama çalının dalları rüzgarda çıt çıt ses çıkarıyordu ve Karatay yaklaşmadı. Doru cesaretle çalıya yürüdü ve dallara baktı. Sesi yalnız ince buzlar çıkarıyordu. Doru elmayı dişleriyle tuttu ve dışarı çekti. "Karatay, bunu birlikte yiyelim," dedi Doru. Doru elmayı ısırdı ve ikiye böldü. İkisi elmayı yavaş yavaş yedi. Doru çok mutlu oldu, çünkü elmayı en yakın arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rüzgar kırmızı bir elmayı"
   - Cümle 2: «Rüzgar kırmızı bir elmayı buzlu bir çalının dallarına takmıştı.»
   - Açıklama: 'Takmak' bilinçli bir eylemdir; rüzgar öznesine uymuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar kırmızı bir elmayı buzlu bir çalının dallarına takmıştı"
   - Cümle 2: «Rüzgar kırmızı bir elmayı buzlu bir çalının dallarına takmıştı.»
   - Açıklama: Rüzgarın bir elmayı taşıyıp çalı dallarına takması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0045` birebir aynı, `@degisim: havuç -> elma` (tutuyorsan), ardından `@onarim: 1032303a14c4af8db9a3b2b38a02f11d95575df0`, sonra gövde.

### Hikâye 11: tohum doru-0046 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0046
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'üzüm', fiil 'sığmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kar çimenlerin üstünü kapladı ve yiyecek yoktu | cesaretle karda yürüyüp kayanın dibinde kuru ot buldu
@tohum: doru-0046
@degisim: üzüm -> ot
Dağda lapa lapa kar yağıyordu. Kar bütün çimenlerin üstündeydi ve Doru yiyecek bulamıyordu. Uzakta büyük bir kaya gördü ve altında kar yoktu. Doru orada yiyecek bulmak istedi. Ama arada yumuşak ve soğuk kar vardı. Doru cesaretle karın içine adım attı. Ayakları karda küçük izler bıraktı. Yavaş yavaş kayanın yanına vardı. Kayanın dibinde kuru otlar duruyordu. Doru ağzına sığdığı kadar ot aldı ve afiyetle yedi. Kayanın yanı sessiz ve huzurluydu. Doru orada karnı tok, mutlu mutlu dinlendi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sessiz ve huzurluydu"
   - Cümle 11: «Kayanın yanı sessiz ve huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kavram, küçük çocuğa uygun değil.
   - Açıklama: 'Huzurlu' soyut bir kavram ve 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0046` birebir aynı, `@degisim: üzüm -> ot` (tutuyorsan), ardından `@onarim: 8c990a4746a474baf6a9cdf33aca1493d123e198`, sonra gövde.

### Hikâye 12: tohum doru-0047 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0047
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'marul', fiil 'barışmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar esti ve marul yokuştan yuvarlandı | yamuk ağacın arkasına cesaretle gidip marulu buldu
@tohum: doru-0047
@degisim: barışmak -> yuvarlanmak
Dağda sert bir rüzgar esiyordu. Doru kayaların arasında bulduğu küçük bir marulu yiyordu. Birden rüzgar yine esti ve marul yokuştan aşağı yuvarlandı. Rüzgar durunca Doru marulu aramak için yokuştan yavaşça indi. Aşağıda yamuk bir ağaç vardı. Ağacın arkasından yeşil bir yaprak görünüyordu. Ağacın dalları çok garipti, ama Doru cesaretle arkasına yürüdü. Marul orada, iki kökün arasında duruyordu. Doru marulu dişleriyle aldı ve çok sevindi. Doru bundan sonra rüzgarlı havada yemeğini bir kayanın dibinde yerdi.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "küçük bir marulu yiyordu"
   - Cümle 2: «Doru kayaların arasında bulduğu küçük bir marulu yiyordu.»
   - Açıklama: Marul bahçe sebzesidir; kartın özgür at sürüsü dünyasında ve dağ tarifinde böyle bir yiyecek yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "marul yokuştan aşağı yuvarlandı"
   - Cümle 3: «Birden rüzgar yine esti ve marul yokuştan aşağı yuvarlandı.»
   - Açıklama: Rüzgarın dağıttığı şeyi gidip toplamak önemsiz bir sorun kalıbı; sorun kurulur kurulmaz kendiliğinden bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0047` birebir aynı, `@degisim: barışmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 7a0106544363aedca9a2cd18dba86eb1552d6e70`, sonra gövde.
