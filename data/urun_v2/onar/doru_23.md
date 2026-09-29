# Editör görevi (onarım): Doru, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0078
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'buz', fiil 'katmak', sıfat 'puantiyeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: gölet buzla kaplıydı ve su yoktu | ağacın altına gidip düşen damlaları buldu
@tohum: doru-0078
Bir sabah ormandaki küçük gölet buzla kaplıydı. Karatay çok susamıştı ve Doru ona yardım etmek istedi. Birden Doru uzaktaki bir ağacın altında, karda puantiyeli küçük izler gördü. İzler sadece o ağacın altındaydı. Doru merak etti ve Karatay'ı da yanına kattı. İkisi izlere bakarak ağaca kadar yürüdü. Ağacın dallarında buzlar vardı ve güneşte eriyordu. Damlalar tek tek aşağı düşüyor ve karda delikler açıyordu. İzleri bu damlalar yapmıştı. Karatay ağzını açtı ve soğuk damlaları içti. Doru da biraz içti. Doru çok sevindi, çünkü izleri yapan şeyi bulmuştu.
```

**Hakem bulguları (7):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karda puantiyeli küçük izler"
   - Cümle 3: «Birden Doru uzaktaki bir ağacın altında, karda puantiyeli küçük izler gördü.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki çocuğun bilmeyeceği bir kelime ve izler için yerinde değil.
   - Açıklama: 'Puantiyeli' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "karda puantiyeli küçük izler gördü"
   - Cümle 3: «Birden Doru uzaktaki bir ağacın altında, karda puantiyeli küçük izler gördü.»
   - Açıklama: Susuzluk sorununun yanına izlerin gizemi ikinci bir sorun olarak ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden Doru uzaktaki bir ağacın altında"
   - Cümle 3: «Birden Doru uzaktaki bir ağacın altında, karda puantiyeli küçük izler gördü.»
   - Açıklama: İzler sebepsizce beliriyor ve çözümü tesadüfle getiriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay'ı da yanına kattı"
   - Cümle 5: «Doru merak etti ve Karatay'ı da yanına kattı.»
   - Açıklama: 'Yanına katmak' deyimsel bir anlatım, küçük çocuk için uygun değil.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru merak etti ve Karatay'ı da yanına kattı"
   - Cümle 5: «Doru merak etti ve Karatay'ı da yanına kattı.»
   - Açıklama: Çözüm susuzluğa yönelmiyor, Doru merakla izlerin peşine düşüyor ve suyu tesadüfen buluyor.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru çok sevindi, çünkü izleri yapan şeyi bulmuştu"
   - Cümle 12: «Doru çok sevindi, çünkü izleri yapan şeyi bulmuştu.»
   - Açıklama: Son cümle su bulma hedefine değil izlerin gizemine bağlanıyor.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "çünkü izleri yapan şeyi bulmuştu"
   - Cümle 12: «Doru çok sevindi, çünkü izleri yapan şeyi bulmuştu.»
   - Açıklama: Son, Karatay'ın susuzluğu hedefine değil izlerin gizemine bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0078` birebir aynı, ardından `@onarim: 65f9bc1ff50f34151b95c7344d6afbac6b71b403`, sonra gövde.

### Hikâye 2: tohum doru-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0081
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'oyuncak', fiil 'tatmak', sıfat 'düzenli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yakındaki çalıda yalnız üç çilek vardı | açıklığa hızla koştu ve bol çilek getirdi
@tohum: doru-0081
@degisim: oyuncak -> çilek
Bir sabah Kırat ormanda bir ağacın altında uyuyordu. Doru onu sevindirmek için çilek toplamak istedi. Ama yakındaki çalıda yalnız üç çilek vardı ve bu çok azdı. Çok çilek ise ormanın öbür ucundaki açıklıktaydı. Doru düz yolda hızla koştu ve oraya çabucak vardı. Çilekli bir dalı ağzıyla kopardı ve geri döndü. Çilekleri düz bir taşın üstüne düzenli bir sırayla dizdi. Kırat gözlerini açtı ve taşa baktı. "Bunlar benim için mi, Doru?" diye sordu Kırat. "Hepsi senin için!" dedi Doru. Kırat bir çilek tattı ve gülümsedi. "Çok tatlı, teşekkürler, Doru," dedi Kırat. Doru bundan sonra sevdiklerine sık sık küçük sürprizler hazırladı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru düz yolda hızla koştu"
   - Cümle 5: «Doru düz yolda hızla koştu ve oraya çabucak vardı.»
   - Açıklama: Güvenli kullanım satırı hızı açık ve düz yerde gösterir; burada hız ağaçlı ormanın içinde kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0081` birebir aynı, `@degisim: oyuncak -> çilek` (tutuyorsan), ardından `@onarim: e68b57eedc205d0757dfb9373985886c93b07bf0`, sonra gövde.

### Hikâye 3: tohum doru-0082 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0082
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'mercan', fiil 'tanımak', sıfat 'kırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşının hiç elması yoktu | iki elmadan birini arkadaşıyla paylaştı
@tohum: doru-0082
@degisim: mercan -> elma
Parktaki geniş çayırda kuşlar ötüyordu. Doru bir ağacın altında iki kırmızı elma buldu. Küçük Alaca da geldi ama ağaçta başka elma kalmamıştı. Alaca kırmızı elmaları tanımıyordu ve merakla baktı. "Doru, bunlar ne?" diye sordu Alaca. "Bunlar elma, çok tatlıdır," dedi Doru. Doru Alaca'ya yardım etmek istedi. Elmalardan birini burnuyla Alaca'nın önüne itti. "Bu elma senin, Alaca," dedi Doru. Alaca elmayı yavaşça ısırdı ve sevinçle zıpladı. "Çok güzelmiş, teşekkürler," dedi Alaca. İki at elmalarını yan yana yedi. Doru çok sevindi, çünkü elmasını Alaca ile paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki elmadan birini arkadaşıyla paylaştı"
   - Cümle 0 (plan satırı): «küçük arkadaşının hiç elması yoktu | iki elmadan birini arkadaşıyla paylaştı»
   - Açıklama: Tek bir elma verilir, paylaşılmaz; 'birini arkadaşına verdi' olmalı.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parktaki geniş çayırda kuşlar"
   - Cümle 1: «Parktaki geniş çayırda kuşlar ötüyordu.»
   - Açıklama: Kartın park kararı yeri sürünün çayırı olarak tarif ediyor; 'park' sözü dizide olmayan bir insan parkını çağrıştırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0082` birebir aynı, `@degisim: mercan -> elma` (tutuyorsan), ardından `@onarim: 5c80a9b614dcd7376efac479183f37003b77fbf6`, sonra gövde.

### Hikâye 4: tohum doru-0083 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0083
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'file', fiil 'gülümsemek', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: kozalak çalılara doğru yuvarlandı | hızla koşup kozalağı çalıların önünde durdurdu
@tohum: doru-0083
@degisim: file -> kozalak
Bir sabah Doru ormanda heyecanlı bir oyun oynuyordu. Yuvarlak bir kozalağı burnuyla itiyor ve peşinden koşuyordu. Ama kozalak birden sık çalılara doğru yuvarlandı. Doru onu çalılara girmeden yakalamak istedi. Doru düz yolda hızla koştu. Kozalağın önüne geçti ve onu burnuyla durdurdu. Kozalak çalıların hemen önünde kaldı. Doru gülümsedi ve kozalağı yeniden yolun ortasına götürdü. Bu kez onu daha yavaş itti. Kozalak ağaçların arasında yuvarlandı ve Doru arkasından koştu. Doru kozalakla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kozalak birden sık çalılara doğru yuvarlandı"
   - Cümle 3: «Ama kozalak birden sık çalılara doğru yuvarlandı.»
   - Açıklama: Kozalağın neden birden çalılara yuvarlandığı söylenmiyor ve sorun çok önemsiz kalıyor.
   - Açıklama: Kozalağın çalılara doğru yuvarlanıp hemen yakalanması önemsiz bir olay; yuvarlandı, durdurdu, bitti.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0083` birebir aynı, `@degisim: file -> kozalak` (tutuyorsan), ardından `@onarim: 6b5f6f2ca4a28464bef91f72edc25eb30cae4c81`, sonra gövde.

### Hikâye 5: tohum doru-0084 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0084
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'sepet', fiil 'belirmek', sıfat 'kabarık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: bulut dağa indi ve annesini hiç göremedi | cesaretle kayaların arasına yürüdü ve annesini buldu
@tohum: doru-0084
@degisim: sepet -> bulut
Doru annesiyle dağda saklambaç oynuyordu. Doru saydı ama o sırada kabarık bir bulut dağa indi. Her yer bembeyaz oldu ve Doru kayaları bile göremedi. Doru cesaretle kayaların arasına yürüdü. "Anneciğim, neredesin?" diye seslendi Doru. Büyük bir kayanın arkasından hafif bir ses geldi. Doru hemen kayanın arkasına baktı. Annesi orada gülerek duruyordu. "Seni buldum, anne!" dedi Doru. O sırada bulut dağdan gitti ve güneş yeniden belirdi. "Şimdi saklanma sırası sende," dedi annesi. Doru ile annesi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bulut dağa indi ve annesini hiç göremedi"
   - Cümle 0 (plan satırı): «bulut dağa indi ve annesini hiç göremedi | cesaretle kayaların arasına yürüdü ve annesini buldu»
   - Açıklama: Bağlanan iki yüklemin öznesi farklı olduğu halde belirtilmemiş, cümle bulutun annesini göremediği gibi okunuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bulut dağa indi ve annesini hiç göremedi"
   - Cümle 0 (plan satırı): «bulut dağa indi ve annesini hiç göremedi | cesaretle kayaların arasına yürüdü ve annesini buldu»
   - Açıklama: Plan satırında 'göremedi' fiilinin öznesi dilbilgisel olarak bulut görünüyor; kimin göremediği belli değil.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Doru kayaları bile göremedi"
   - Cümle 3: «Her yer bembeyaz oldu ve Doru kayaları bile göremedi.»
   - Açıklama: Sisli dağda annesini göremeyen yavru sahnesi küçük çocuk için korkutucu olabilir.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru kayaları bile göremedi"
   - Cümle 3: «Her yer bembeyaz oldu ve Doru kayaları bile göremedi.»
   - Açıklama: Doru kayaları bile göremiyor ama hemen sonra kayaların arasında yürüyüp büyük kayanın arkasına bakıyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle kayaların arasına yürüdü"
   - Cümle 4: «Doru cesaretle kayaların arasına yürüdü.»
   - Açıklama: Hiçbir şeyin görünmediği bulutta dağda kayaların arasına yürümek taklit edilince tehlikelidir.
   - Açıklama: Hiçbir şey görünmezken dağda kayaların arasına yürümek taklit edilince tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0084` birebir aynı, `@degisim: sepet -> bulut` (tutuyorsan), ardından `@onarim: 2b5472d8246c8b2c031d5ce9add32cf294298f35`, sonra gövde.

### Hikâye 6: tohum doru-0087 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0087
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'örtü', fiil 'görüşmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: kar topu yuvarlandı ve bir kar yığınına gömüldü | cesaretle karı kazıp topu dışarı itti
@tohum: doru-0087
@degisim: görüşmek -> yuvarlamak
Rüzgar hafif hafif esiyordu ve parkı beyaz bir kar örtüsü kaplamıştı. Doru burnuyla bir kar topu itiyor ve onu kocaman yapıyordu. Ama top küçük bir yokuştan kaydı ve yumuşak bir kar yığınına gömüldü. Doru topunu göremedi. Kar çok soğuktu ama Doru cesaretle burnunu yığının içine soktu. Karı kazdı ve topu buldu. Sonra topu yığından dışarı itti. Top biraz ezilmişti ama Doru onu yeniden yuvarladı. Top yine büyüdü ve bu kez düz yerde kaldı. Doru karda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parkı beyaz bir kar örtüsü kaplamıştı"
   - Cümle 1: «Rüzgar hafif hafif esiyordu ve parkı beyaz bir kar örtüsü kaplamıştı.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği çayırdır; hikaye yeri 'park' diye adlandırıp karla kaplı gösteriyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yumuşak bir kar yığınına gömüldü"
   - Cümle 3: «Ama top küçük bir yokuştan kaydı ve yumuşak bir kar yığınına gömüldü.»
   - Açıklama: Kar topunun yığına gömülüp kazılıp çıkarılması önemsiz bir olay; kolayca yenisi yapılabilecek bir top için gerçek bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0087` birebir aynı, `@degisim: görüşmek -> yuvarlamak` (tutuyorsan), ardından `@onarim: 9d37b40c080553c4f85df20d202eaf8906f7169c`, sonra gövde.

### Hikâye 7: tohum doru-0088 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0088
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'armut', fiil 'dolanmak', sıfat 'dar'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: armut ağacına giden yol çok dardı | cesaretle dar yola girdi ve ağaca vardı
@tohum: doru-0088
Ormanda Doru ile Karatay yavaşça yürüyordu. Doru uzakta, üstünde sarı armutlar olan bir ağaç fark etti. Ama ağaca giden yol çok dardı ve dallarla doluydu. Karatay bütün ormanı dolanmak istedi ama bu çok uzun sürerdi. Doru cesaretle dar yola girdi. Doru dalların altından yavaşça geçti. Karatay da onun arkasından geldi. Biraz sonra ikisi armut ağacının altına vardı. Yerde sarı armutlar duruyordu. Doru bir armudu Karatay'ın önüne itti ve kendisi de bir tane yedi. Armutlar çok tatlıydı. Doru çok sevindi, çünkü dar yoldan geçip armut ağacını bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ağaca giden yol çok dardı"
   - Cümle 3: «Ama ağaca giden yol çok dardı ve dallarla doluydu.»
   - Açıklama: Dar yol gerçek bir engel olarak kurulmuyor; Doru yalnızca içine girince sorun kendiliğinden bitiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru cesaretle dar yola girdi"
   - Cümle 5: «Doru cesaretle dar yola girdi.»
   - Açıklama: Cesaretle yola girmek yolun darlığı sebebine yönelmiyor; sorun kendiliğinden ortadan kalkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0088` birebir aynı, ardından `@onarim: 4d93e8337dc16321fde8e5ff9def43a1fdc07cca`, sonra gövde.

### Hikâye 8: tohum doru-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0089
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'erik', fiil 'yemek', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: son erik karanlık bir çalının altına yuvarlandı | cesurca başını çalıya uzattı ve eriği çıkardı
@tohum: doru-0089
Hava kapalıydı ve serin bir rüzgar esiyordu. Kırat çok acıkmıştı ve Doru onunla erik arıyordu. Ağaçtan düşen son erik, sık bir çalının altına yuvarlandı. Çalının altı çok karanlık ve dardı. "Ben onu çıkarırım, Kırat," dedi Doru. "Dikkatli ol, Doru, çalı çok sık," dedi Kırat. Doru cesurca başını çalının altına uzattı. Eriği buldu ve dişleriyle nazikçe tuttu. Sonra onu çıkarıp Kırat'ın önüne koydu. Kırat eriği keyifle yedi. "Teşekkürler, Doru, çok tatlıymış!" dedi Kırat. Doru çok sevindi, çünkü aç Kırat sonunda eriğine kavuşmuştu.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalının altı çok karanlık ve dardı"
   - Cümle 4: «Çalının altı çok karanlık ve dardı.»
   - Açıklama: Karanlık ve dar çalı altı küçük çocuk için ürkütücü bir öğe olarak vurgulanıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesurca başını çalının altına uzattı"
   - Cümle 7: «Doru cesurca başını çalının altına uzattı.»
   - Açıklama: Karanlık ve dar, sık bir çalının altına baş sokmak çocuğun taklit edebileceği riskli bir davranıştır.
   - Açıklama: Karanlık ve dar bir çalının altına baş sokmak çocuğun taklit edebileceği riskli bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sonunda eriğine kavuşmuştu"
   - Cümle 12: «Doru çok sevindi, çünkü aç Kırat sonunda eriğine kavuşmuştu.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuk için soyut ve edebi bir fiil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0089` birebir aynı, ardından `@onarim: b737662409592f01fa40504e9b5e88200ef1ae3a`, sonra gövde.

### Hikâye 9: tohum doru-0092 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0092
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'böğürtlen', fiil 'susmak', sıfat 'neşeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: rüzgar çok gürültülüydü ve annesini duymadı | annesi şarkıyı bitirince başını da salladı
@tohum: doru-0092
Bir sabah Doru ile annesi çayırda neşeli bir oyun oynuyordu. Annesi şarkı söylerken Doru hızla koşuyor, şarkı bitince duruyordu. Ama rüzgar çok gürültülüydü ve Doru annesini duymadı. Doru durmadı ve böğürtlen çalısına kadar koştu. Annesi güldü. "Doru, şarkı bitti ama sen koşuyordun!" dedi annesi. Doru gülümsedi ve biraz düşündü. "Anne, şarkı bitince başını da salla," dedi Doru. Annesi yeniden şarkıya başladı. Sonra birden sustu ve başını salladı. Doru bunu hemen gördü ve tam yerinde durdu. "Aferin, Doru!" dedi annesi ve çalıdan ona bir böğürtlen verdi. Doru bundan sonra rüzgar esince annesinin başını da izledi.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "annesi şarkıyı bitirince başını da salladı"
   - Cümle 0 (plan satırı): «rüzgar çok gürültülüydü ve annesini duymadı | annesi şarkıyı bitirince başını da salladı»
   - Açıklama: Plan çözümü anneye veriyor; gövdede çözüm Doru'nun annesinden başını sallamasını istemesi.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile annesi çayırda neşeli"
   - Cümle 1: «Bir sabah Doru ile annesi çayırda neşeli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer park olduğu halde hikaye çayırda başlıyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile annesi çayırda neşeli bir oyun"
   - Cümle 1: «Bir sabah Doru ile annesi çayırda neşeli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "annesinin başını da izledi"
   - Cümle 13: «Doru bundan sonra rüzgar esince annesinin başını da izledi.»
   - Açıklama: 'Başını izlemek' anlamca bozuk; kastedilen annesinin baş sallamasına bakmak.
   - Açıklama: 'Başını izlemek' yanlış anlamda; 'annesinin başını sallamasını izledi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0092` birebir aynı, ardından `@onarim: f1f7fc8329c4c4f68a5e00e4511574272ec98976`, sonra gövde.

### Hikâye 10: tohum doru-0093 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0093
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'koni', fiil 'çözmek', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: kuru bir ot çiçeği aşağı çekiyordu | otu dişleriyle tuttu ve yavaşça çözdü
@tohum: doru-0093
@degisim: güvenli -> kuru
Doru ormanda, ağaçların arasında çiçeklere bakma oyunu oynuyordu. Birden yere eğilmiş, koni gibi mor bir çiçek gördü. Ona kuru bir ot sarılmıştı ve onu aşağı çekiyordu. Doru bu küçük çiçeğe yardım etmek istedi. Önce onu kırmamak için yavaşça yaklaştı. Otu dişleriyle tuttu ve dikkatle çözdü. Ot yere düştü ve mor çiçek hafifçe sallandı. Sonra yeniden yukarı kalktı ve güneşe doğru döndü. Doru onu bir kez daha burnuyla kokladı. Çiçeğin kokusu çok güzeldi. Doru çok sevindi, çünkü oyununda ilk çiçeğini kurtarmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "koni gibi mor bir çiçek"
   - Cümle 2: «Birden yere eğilmiş, koni gibi mor bir çiçek gördü.»
   - Açıklama: 'Koni' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "koni gibi mor bir"
   - Cümle 2: «Birden yere eğilmiş, koni gibi mor bir çiçek gördü.»
   - Açıklama: 'Koni' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru onu bir kez daha burnuyla kokladı"
   - Cümle 9: «Doru onu bir kez daha burnuyla kokladı.»
   - Açıklama: Doru çiçeği daha önce hiç koklamamışken bir kez daha kokladığı söyleniyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "oyununda ilk çiçeğini kurtarmıştı"
   - Cümle 11: «Doru çok sevindi, çünkü oyununda ilk çiçeğini kurtarmıştı.»
   - Açıklama: Oyun çiçeklere bakma oyunu olarak kuruldu ama sonda çiçek kurtarma oyunuymuş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0093` birebir aynı, `@degisim: güvenli -> kuru` (tutuyorsan), ardından `@onarim: 53dc6b7ad9adecf25771bcc4d559a40e5bba54cc`, sonra gövde.

### Hikâye 11: tohum doru-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0094
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'gül', fiil 'yapmak', sıfat 'zor'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: kokunun nereden geldiğini bulmak zordu | rüzgarın geldiği yöne dönüp kokunun peşinden gitti
@tohum: doru-0094
Bir sabah Doru ile Karatay dağda dolaşıyordu. Karatay birden güzel bir koku aldı ve durdu. Kokunun nereden geldiğini bulmak zordu, çünkü vadide bir sürü çiçek vardı. "Doru, bu koku nereden geliyor?" diye sordu Karatay. Doru ona yardım etmek istedi ve biraz düşündü. Sonra rüzgarın geldiği yöne döndü. "Koku rüzgarla geliyor, hadi şuraya gidelim!" dedi Doru. İkisi birlikte yürüdü ve büyük bir kayanın arkasına geldi. Orada pembe bir gül çalısı vardı. Karatay gülleri kokladı ve sevinçle zıpladı. "Teşekkürler, Doru, bunu birlikte yaptık!" dedi Karatay.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dönüp kokunun peşinden gitti"
   - Cümle 0 (plan satırı): «kokunun nereden geldiğini bulmak zordu | rüzgarın geldiği yöne dönüp kokunun peşinden gitti»
   - Açıklama: 'Kokunun peşinden gitmek' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0094` birebir aynı, ardından `@onarim: 63aee603ad40cc0d40daf13ce0cd62349cefe7c4`, sonra gövde.

### Hikâye 12: tohum doru-0095 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0095
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'baloncuk', fiil 'guruldamak', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar yaprak gemisini derenin ortasına itti | gemiyi burnuyla yavaşça kıyıya itti
@tohum: doru-0095
Bir sabah Doru, vadideki sığ bir derenin kenarında gemi oyunu oynuyordu. Geniş bir yaprak onun gemisiydi ve üstünde küçük bir papatya vardı. Birden rüzgar esti ve gemi derenin ortasına kaydı. Dere taşların arasında guruldadı ve gemiyi uzağa götürdü. Ama uyanık Doru onun peşinden yürüdü. Gemi bir taşa takıldı ve etrafında baloncuklar oluştu. Doru papatyaya yardım etmek için boynunu uzattı. Yaprağı burnuyla yavaşça kıyıya itti. Papatya hiç ıslanmamıştı. Doru da gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (10):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "gemi oyunu oynuyordu"
   - Cümle 1: «Bir sabah Doru, vadideki sığ bir derenin kenarında gemi oyunu oynuyordu.»
   - Açıklama: Gemi bir araç kavramıdır ve kartın doğa dünyasında (tohum yasak kategorileri: araç) yer almaz.
   - Açıklama: Gemi, kartın doğa dünyasında (özgür at sürüsü) olmayan bir araç kavramı olarak hikayeye giriyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve gemi derenin ortasına kaydı"
   - Cümle 3: «Birden rüzgar esti ve gemi derenin ortasına kaydı.»
   - Açıklama: Rüzgarın yaprağı itip Doru'nun geri itmesi önemsiz bir olay; örnekteki 'rüzgar dağıttı, topladı, bitti' kalıbına denk.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dere taşların arasında guruldadı"
   - Cümle 4: «Dere taşların arasında guruldadı ve gemiyi uzağa götürdü.»
   - Açıklama: Guruldamak karın için kullanılır; dere şırıldar.
   - Açıklama: Dere guruldamaz, şırıldar; fiil öznesine uymuyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Doru onun peşinden yürüdü"
   - Cümle 5: «Ama uyanık Doru onun peşinden yürüdü.»
   - Açıklama: 'onun' zamiri dereyi mi gemiyi mi gösteriyor belli değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama uyanık Doru onun"
   - Cümle 5: «Ama uyanık Doru onun peşinden yürüdü.»
   - Açıklama: Tohumdaki özellik yardım; kartın özellikler alanında olmayan 'uyanık' ikinci bir özellik olarak ekleniyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama uyanık Doru"
   - Cümle 5: «Ama uyanık Doru onun peşinden yürüdü.»
   - Açıklama: Tohumdaki özellik yardım; uyanıklık kartın özellikler alanında olmayan ek bir özellik olarak ekleniyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Gemi bir taşa takıldı ve etrafında baloncuklar oluştu"
   - Cümle 6: «Gemi bir taşa takıldı ve etrafında baloncuklar oluştu.»
   - Açıklama: Geminin tesadüfen taşa takılması çözümü sebepsizce getiriyor, baloncuklar da işlevsiz ayrıntı.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Gemi bir taşa takıldı"
   - Cümle 6: «Gemi bir taşa takıldı ve etrafında baloncuklar oluştu.»
   - Açıklama: Uzağa sürüklenen gemi rastlantıyla bir taşa takılıyor, çözümü figür değil şans getiriyor.
9. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "etrafında baloncuklar oluştu"
   - Cümle 6: «Gemi bir taşa takıldı ve etrafında baloncuklar oluştu.»
   - Açıklama: Baloncuklar hiçbir işe yaramayan işlevsiz bir ayrıntı.
10. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru da gemi oyununa"
   - Cümle 10: «Doru da gemi oyununa mutlu mutlu devam etti.»
   - Açıklama: Başka oynayan kimse olmadığı için 'da' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0095` birebir aynı, ardından `@onarim: 84b9ee6282bde9e91b729d71e4526d2620bb39c3`, sonra gövde.
