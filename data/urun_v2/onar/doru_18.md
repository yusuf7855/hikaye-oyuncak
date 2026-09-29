# Editör görevi (onarım): Doru, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0067 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0067
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'resim', fiil 'ısınmak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: güneş yoktu ve iki arkadaş ısınmak istiyordu | karda koşup büyük bir güneş resmi yaptılar
@tohum: doru-0067
Soğuk bir rüzgar esiyordu ve gökyüzü bulutluydu. Doru ile Karatay dağda, karın üstünde duruyordu. Güneş yoktu ve ikisi de ısınmak istiyordu. Birden Doru, karda kendi ayak izlerini fark etti. Onlarla büyük bir resim yapmayı düşündü. Hemen koşmaya başladı ve kocaman bir güneş çizdi. Karatay da çizmek istedi ama nasıl yapacağını bilmiyordu. Doru ona yardım etti ve önünden yavaşça yürüdü. Karatay onun arkasından gidip güneşin çevresine çizgiler yaptı. Az sonra güneş resmi bitti. Bu oyunla ikisi de çok ısındı. Doru bundan sonra soğuk günlerde koşup oynamayı unutmadı.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Onlarla büyük bir resim yapmayı düşündü"
   - Cümle 5: «Onlarla büyük bir resim yapmayı düşündü.»
   - Açıklama: Güneş resmi yapmak ısınma sorununa doğrudan yönelmiyor; ısınma koşmanın yan etkisi olarak geliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen koşmaya başladı ve"
   - Cümle 6: «Hemen koşmaya başladı ve kocaman bir güneş çizdi.»
   - Açıklama: Güvenli özellik kullanımı satırı koşmayı açık ve düz yerle sınırlar; burada karlı dağda koşuluyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Karatay da çizmek istedi ama nasıl yapacağını bilmiyordu"
   - Cümle 7: «Karatay da çizmek istedi ama nasıl yapacağını bilmiyordu.»
   - Açıklama: Isınma sorununun yanında Karatay'ın çizmeyi bilmemesi ikinci bir sorun olarak açılıyor.
   - Açıklama: Karatay'ın çizmeyi bilmemesi ısınma sorununun yanına ikinci bir sorun ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0067` birebir aynı, ardından `@onarim: be46bbb7162115685a748929e7beeb0029d02e4a`, sonra gövde.

### Hikâye 2: tohum doru-0068 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0068
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'altın', fiil 'dönmek', sıfat 'değerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: koşarken annesinin sevdiği çiçekleri ezdi | cesaretle doğruyu söyleyip özür diledi
@tohum: doru-0068
Bir sabah Doru, dağda annesiyle çimen yiyordu. Sonra oynamak için koştu ve altın renkli çiçekleri ezdi. Bu çiçekler annesi için çok değerliydi. Doru geri döndü ve çiçeklere üzgün üzgün baktı. Önce annesine söylemekten çekindi. Sonra cesaretle annesinin yanına gitti. "Anneciğim, koşarken çiçeklerini ezdim, özür dilerim," dedi Doru. Annesi başını eğdi ve Doru'yu burnuyla okşadı. "Tamam, Doru, ama bir daha çiçeklerin yanında koşma," dedi annesi. Doru kalan çiçeklerin arasından yavaşça yürüdü. "Tamam, anneciğim, seni çok seviyorum," dedi Doru.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesi için çok değerliydi"
   - Cümle 3: «Bu çiçekler annesi için çok değerliydi.»
   - Açıklama: 'Değerli' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesine söylemekten çekindi"
   - Cümle 5: «Önce annesine söylemekten çekindi.»
   - Açıklama: 'Çekinmek' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Çekinmek' soyut bir kelime, küçük çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0068` birebir aynı, ardından `@onarim: 0c4ae540b546cd19565a96e34c2cc32bf75518f7`, sonra gövde.

### Hikâye 3: tohum doru-0069 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0069
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'tomurcuk', fiil 'özlemek', sıfat 'kırık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: tomurcuklar gölgede açmamıştı | güneşli yere hızla koşup çiçekleri buldu
@tohum: doru-0069
Ormanda Doru, ağaçların dallarında küçük tomurcuklar gördü. Doru çiçekleri çok özlemişti ama tomurcukların hiçbiri açmamıştı. Ağaçlar çok sıktı, bu yüzden tomurcuklar güneş alamıyordu. Birden uzakta parlak bir yer fark etti. Orada kırık bir ağaç yere düşmüştü ve her yer güneşliydi. Doru ağaçların arasındaki düz, açık yolda hızla koştu. Kısa sürede oraya vardı. Düşen ağacın yanında sarı çiçekler vardı. Doru başını eğdi ve çiçekleri yavaşça kokladı. Doru çok sevindi, çünkü sonunda açmış çiçekler bulmuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağaçlar çok sıktı"
   - Cümle 3: «Ağaçlar çok sıktı, bu yüzden tomurcuklar güneş alamıyordu.»
   - Açıklama: 'Sık' kelimesi küçük çocuk için bilinmez ve 'sıkmak' fiiliyle karışan belirsiz bir biçim.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bu yüzden tomurcuklar güneş alamıyordu"
   - Cümle 3: «Ağaçlar çok sıktı, bu yüzden tomurcuklar güneş alamıyordu.»
   - Açıklama: Önce sebep beyaz bulutlar deniyor, hemen sonra sık ağaçlar deniyor; iki sebep çelişiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden uzakta parlak bir yer fark etti"
   - Cümle 4: «Birden uzakta parlak bir yer fark etti.»
   - Açıklama: Güneşli yer ve açmış çiçekler çözümü sebepsizce, tesadüfle getiriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru ağaçların arasındaki düz, açık yolda hızla koştu"
   - Cümle 6: «Doru ağaçların arasındaki düz, açık yolda hızla koştu.»
   - Açıklama: Sebep tomurcukların güneş almaması ama çözüm tomurcuklara yönelmiyor, başka yerde hazır çiçek bulunuyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Düşen ağacın yanında sarı çiçekler vardı"
   - Cümle 8: «Düşen ağacın yanında sarı çiçekler vardı.»
   - Açıklama: Çözüm tomurcukların açmamasına yönelmiyor; Doru başka yerde hazır çiçek buluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0069` birebir aynı, ardından `@onarim: d873e14fc31ed8bb6285f5bf5248065e8946bfe5`, sonra gövde.

### Hikâye 4: tohum doru-0070 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0070
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gölge', fiil 'anlatmak', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yağmur başladı ve yakında hiç ağaç yoktu | cesaretle büyük kayanın altına girdi
@tohum: doru-0070
@degisim: anlatmak -> saklanmak
Dağda Doru tek başına çimen yiyordu. Birden bulutlar geldi ve yağmur başladı. Doru'nun sırtı ıslandı ve yakında hiç ağaç yoktu. Biraz ileride kocaman bir kaya vardı. Kayanın altında karanlık bir gölge duruyordu. Doru önce durdu, ama sonra cesaretle gölgeye girdi. İçerisi kuruydu. Doru yerdeki eskimiş yaprakların üstüne rahatça yattı. Orada hiç ıslanmadı. Bir süre sonra bulutlar gitti ve güneş çıktı. Doru kayanın altından ayrıldı ve yeniden çimen yemeye başladı. Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.
```

**Hakem bulguları (5):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Kayanın altında karanlık bir gölge duruyordu"
   - Cümle 5: «Kayanın altında karanlık bir gölge duruyordu.»
   - Açıklama: Karanlık, bekleyen bir gölge küçük çocuk için korkutucu bir öğe olarak sunuluyor.
   - Açıklama: Karanlık gölgeye tek başına girme küçük çocuk için korkutucu bir öğe olabilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karanlık bir gölge duruyordu"
   - Cümle 5: «Kayanın altında karanlık bir gölge duruyordu.»
   - Açıklama: Yağmurdan korunulan kaya altı için 'gölge' kelimesi yanlış anlamda kullanılmış.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sonra cesaretle gölgeye girdi"
   - Cümle 6: «Doru önce durdu, ama sonra cesaretle gölgeye girdi.»
   - Açıklama: Büyük bir kayanın altındaki karanlık boşluğa girmek çocuğun taklit edebileceği riskli bir davranış olarak övülüyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerdeki eskimiş yaprakların"
   - Cümle 8: «Doru yerdeki eskimiş yaprakların üstüne rahatça yattı.»
   - Açıklama: Yapraklar için 'eskimiş' uygun değil; 'kuru yaprakların' olmalı.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yerdeki eskimiş yaprakların üstüne"
   - Cümle 8: «Doru yerdeki eskimiş yaprakların üstüne rahatça yattı.»
   - Açıklama: Yakında hiç ağaç yokken kayanın altında sebepsizce yapraklar beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0070` birebir aynı, `@degisim: anlatmak -> saklanmak` (tutuyorsan), ardından `@onarim: 0f153a1bcfd80a6b5417060106318af665a9bfec`, sonra gövde.

### Hikâye 5: tohum doru-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0071
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kese', fiil 'yerleştirmek', sıfat 'farklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: koşarken bakmadı ve küçük arkadaşının taşlarını dağıttı | özür diledi ve taşları yeniden dizdi
@tohum: doru-0071
@degisim: kese -> taş
Doru vadinin düz yerinde bir aşağı bir yukarı koşuyordu. Alaca ise çimenin üstüne farklı renkte taşlar yerleştiriyordu. Doru bakmadan koştu ve Alaca'nın taşlarını dağıttı. Alaca taşlara baktı ve üzüldü. Doru hemen durdu ve Alaca'nın yanına gitti. "Özür dilerim, Alaca, taşları yeniden dizmene yardım edeyim mi?" diye sordu Doru. "Evet, bir çiçek resmi yapıyordum," dedi Alaca. Alaca taşların yerini gösterdi, Doru da burnuyla onları itti. Az sonra taşlardan renkli bir çiçek oldu. Doru çok sevindi, çünkü Alaca yine gülüyordu ve çiçek resmi bitmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düz yerinde bir aşağı bir yukarı"
   - Cümle 1: «Doru vadinin düz yerinde bir aşağı bir yukarı koşuyordu.»
   - Açıklama: Düz yerde 'aşağı yukarı' koşmak kelime anlamıyla çelişiyor ve deyimsel bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0071` birebir aynı, `@degisim: kese -> taş` (tutuyorsan), ardından `@onarim: fbaa31bfa29fdcae2e967f1f067885e275d172c6`, sonra gövde.

### Hikâye 6: tohum doru-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0072
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'taş', fiil 'sıkılmak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: çalıların arkasından garip bir ses geldi | cesaretle geçip taşa damlayan suyu buldu
@tohum: doru-0072
Garip bir ses geliyordu: tık, tık. Doru ormanda tek başına sıkılmıştı ve bu sesi hemen duydu. Ses sık çalıların arkasından geliyordu ve Doru onu çok merak etti. Çalıların arkası karanlık görünüyordu. Ama Doru cesaretle çalıların arasından geçti. Arkada büyük, düz bir taş vardı. Yukarıdaki kayalardan ince bir su iniyordu. Her damla taşa düşünce tık diye ses çıkarıyordu. Doru suyun altında oynadı ve az sonra sırılsıklam oldu. Serin su Doru'yu çok güldürdü. Doru çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalıların arkası karanlık görünüyordu"
   - Cümle 4: «Çalıların arkası karanlık görünüyordu.»
   - Açıklama: Garip ses ve karanlık çalılar küçük çocuk için ürkütücü bir öğe olabilir.
   - Açıklama: Tek başına kalan Doru'nun garip bir ses için karanlık çalılara girmesi küçük çocuk için korkutucu bir öğe taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0072` birebir aynı, ardından `@onarim: 5e19c3b1289fbd8d09526217287e7065188479f5`, sonra gövde.

### Hikâye 7: tohum doru-0073 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0073
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'ceviz', fiil 'keşfetmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: ceviz yuvarlandı ve içi boş bir kütüğe girdi | cesaretle kütüğün öbür ucundan bakıp cevizi çıkardı
@tohum: doru-0073
@degisim: keşfetmek -> bulmak
Bir sabah Doru ile Kırat, çayırdaki ceviz ağacının altında oynuyordu. Kırat bir cevizi saklıyor, Doru da onu buluyordu. Ama bu kez ceviz yuvarlandı ve içi boş bir kütüğe girdi. Kütüğün içi karanlıktı ve hiçbir şey görünmüyordu. "Ceviz içeride kaldı, Doru," dedi Kırat. Doru biraz çekindi ama sonra cesaretle kütüğün öbür ucuna gitti. Oradan içeri baktı ve cevizi gördü. Ceviz bu tarafa çok yakındı. Doru ağzıyla onu tuttu ve dışarı çıkardı. "Aferin, Doru, cevizi yine buldun!" dedi Kırat. Kırat bu kez cevizi çizgili bir taşın arkasına sakladı. Doru onu hemen buldu ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "çayırdaki ceviz ağacının altında oynuyordu"
   - Cümle 1: «Bir sabah Doru ile Kırat, çayırdaki ceviz ağacının altında oynuyordu.»
   - Açıklama: Başlıktaki yer park olduğu hâlde hikaye çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0073` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 85fe8eb046ef0975991ccf440dece3876769777e`, sonra gövde.

### Hikâye 8: tohum doru-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0074
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'küp', fiil 'selamlamak', sıfat 'uslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaşı çok sessiz konuşunca ses geri gelmedi | cesaretle önce kendisi bağırıp ona gösterdi
@tohum: doru-0074
@degisim: küp -> kaya
Dağda Doru ile Alaca bir ses oyunu oynuyordu. Sırayla kayaya "Merhaba!" diye bağırıyor, ses geri geliyordu. Sıra Alaca'ya gelince o çok sessiz konuştu ve ses gelmedi. Alaca başını eğdi ve üzüldü. Doru cesaretle en yüksek sesiyle kayayı selamladı. Ses hemen kayadan döndü ve ikisi güldü. "Şimdi sen dene, Alaca, ben yanındayım," dedi Doru. Alaca derin bir nefes aldı ve bağırdı. Bu kez onun sesi de döndü. Sonra Alaca uslu durdu ve Doru'nun sırasını bekledi. "Sıra sende, Doru, bu oyun çok güzel!" dedi Alaca.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru cesaretle en yüksek sesiyle kayayı selamladı"
   - Cümle 5: «Doru cesaretle en yüksek sesiyle kayayı selamladı.»
   - Açıklama: Alaca yüksek sesle bağırmayı oyunda zaten görmüştü; Doru'nun yeniden bağırması sorunun sebebine doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0074` birebir aynı, `@degisim: küp -> kaya` (tutuyorsan), ardından `@onarim: 8965f007df33bd9c4d21d7e337f5723409b55c38`, sonra gövde.

### Hikâye 9: tohum doru-0076 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0076
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'salıncak', fiil 'tartmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yolun ortasına kuru bir dal düşmüştü | dalı kenara bırakıp yolda hızla koştu
@tohum: doru-0076
@degisim: salıncak -> çiçek
Doru ormanda çiçeklerle süslü, uzun ve düz bir yol buldu. Burada daha önce hiç koşmamıştı ve hemen denemek istedi. Ama rüzgar kuru bir dalı yolun ortasına düşürmüştü. Doru dalı dişleriyle kaldırıp tarttı. Dal çok hafifti. Doru onu kenardaki çalıların yanına bıraktı. Artık önünde hiçbir şey yoktu. Sonra en başa geçti ve hızla koşmaya başladı. Çiçekler iki yanında renk renk parlıyordu. Kısa sürede sonuna ulaştı. Durdu ve arkasındaki çiçeklere baktı. Doru çok sevindi, çünkü bu güzel yolda ilk kez koşmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalı dişleriyle kaldırıp tarttı"
   - Cümle 4: «Doru dalı dişleriyle kaldırıp tarttı.»
   - Açıklama: 'Tartmak' fiili bir atın dalı dişleriyle kaldırmasına uygun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Dal çok hafifti"
   - Cümle 5: «Dal çok hafifti.»
   - Açıklama: Yoldaki hafif bir dal hiç zorluk çıkarmayan önemsiz bir sorun; kaldırıp bırakınca bitiyor.
   - Açıklama: Hafif bir dalı kenara koymak önemsiz bir engel; sorun çocuğun önemseyeceği bir sorun değil, kaldır-bitti olayı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "renk renk parlıyordu"
   - Cümle 9: «Çiçekler iki yanında renk renk parlıyordu.»
   - Açıklama: Çiçekler parlamaz; mecazlı anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0076` birebir aynı, `@degisim: salıncak -> çiçek` (tutuyorsan), ardından `@onarim: 86e3c8b70fd986622dd5e4a32010e306be4d33f2`, sonra gövde.
