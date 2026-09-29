# Editör görevi (onarım): Niloya, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Niloya | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar10.txt --ad urun_v2`
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

## Kart: Niloya (kaynaklı, kapalı dünya)

- Ad: Niloya (okunuş: niloya; kesme eki okunuşa uyar)
- Kimlik: Niloya, nehir kenarındaki bir köyde ailesiyle yaşayan küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Niloya'nın merakı bakarak, sorarak ve bir büyüğe haber vererek gösterilir; nehre ya da dereye girmez, suya yalnız kıyıdan bakar; ağaca ya da yüksek yere tırmanmaz.
- Özellikler:
  - keşfet: Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever. (örnek biçimler: merak etti, merakla, keşfetti)
  - soru: Merak ettiği her şeyi sorar. (örnek biçimler: sordu, soruyu, sorular)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
- Yerler:
  - orman: Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.
  - dağ: Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.
  - ev: Niloya'nın nehir kenarındaki köy evi ve bahçesi.
  - park: Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Murat: Niloya'nın ağabeyi; küçük kardeşi Niloya'yı çok sever. Tür: oğlan; konuşur; huy: Top oynamayı, koşturmayı ve fındık toplamayı sever.. Yüzey biçimleri: Murat, ağabey, ağabeyi, abi, abisi, abiciğim
  - Mete: Murat'ın en yakın arkadaşı; Niloya ile aynı yaştadır ve onun da arkadaşıdır. Tür: oğlan; konuşur; huy: Oyuncaklarını dağıtır, sonra aradığını bulamaz.. Yüzey biçimleri: Mete
  - Tospik: Niloya'nın kaplumbağası ve en yakın arkadaşı. Tür: kaplumbağa; konuşur; huy: Oyun oynamayı ve uyumayı sever; Niloya'ya yetişmekte zorlanır.. Yüzey biçimleri: Tospik, kaplumbağa, kaplumbağası
  - dedesi: Niloya'nın dedesi; herkese iyi öğütler verir. Tür: dede; konuşur. Yüzey biçimleri: dede, dedesi, dedeciğim, Dede
  - babaannesi: Niloya'nın babaannesi; yemek yapmayı ve fındık toplamayı sever. Tür: babaanne; konuşur. Yüzey biçimleri: babaanne, babaannesi, babaanneciğim, Babaanne, nine, ninesi
  - annesi: Niloya'nın annesi; yemek yapmayı, ekinleri ve yaylayı sever. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
- Dünya kuralları:
  - Niloya'nın ağabeyi Murat'tır. Mete Niloya'nın ağabeyi değildir; Murat'ın arkadaşıdır.
  - Tospik yavaştır; Niloya'ya yetişmekte zorlanır, hızla koşmaz.
  - Köy nehir kenarındadır; hikayede kimse nehre ya da dereye girmez, suya kıyıdan bakılır.
- Yasak adlar: Elif, Mine, Fatoş, Cem, Ayşecik, Sarıkanat, Miniş
- Yasak: Babası kartta yok; hikayeye girmez (kapalı dünya).
- İzinli dünya kelimeleri: köy, nehir, yayla, fındık, kaplumbağa, kekik

## Onarılacak hikâyeler

### Hikâye 1: tohum niloya-0026 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0026
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'tabure', fiil 'uyumak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: ağaçların arasından komik bir ses geliyordu | sesi izledi ve uyuyan babaannesini buldu
@tohum: niloya-0026
Ağaçların arasından komik bir ses geliyordu. Niloya fındık toplamayı bıraktı ve sesi dinledi. Sesin nereden geldiğini bulmak istedi. Sesi izleyerek yakındaki büyük bir fındık ağacına yürüdü. Ağacın arkasına baktı ve güldü. Babaannesi küçük bir taburede oturmuş, uyuyordu. Ses ondan geliyordu. Yanındaki sepette ikisi için kremalı bir kek vardı. Niloya babaannesini yavaşça uyandırmak için bir şarkı söyledi. Babaannesi gözlerini açtı ve Niloya'ya gülümsedi. İkisi keki birlikte yedi. Sonra fındık toplamaya mutlu mutlu devam ettiler.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ağaçların arasından komik bir ses geliyordu"
   - Cümle 1: «Ağaçların arasından komik bir ses geliyordu.»
   - Açıklama: Komik bir ses yalnız merak uyandırıyor; ortada çocuğun önemseyeceği gerçek bir sorun yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanındaki sepette ikisi için kremalı bir kek vardı"
   - Cümle 8: «Yanındaki sepette ikisi için kremalı bir kek vardı.»
   - Açıklama: Kek sorunla ilgisiz biçimde sebepsiz beliriyor ve hikayeye işlevsiz bir ek olay katıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0026` birebir aynı, ardından `@onarim: 8fc2ad1540f2a6a4ebc2e21de4bda27866c4423a`, sonra gövde.

### Hikâye 2: tohum niloya-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0027
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'perde', fiil 'ıslanmak', sıfat 'boş'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yağmur başladı ama şapkası yolda bir dala takılmıştı | şarkısını yeniden söyleyip geldiği yoldan geri yürüdü
@tohum: niloya-0027
@degisim: perde -> şapka
Niloya boş sepetiyle fındık ağaçlarına yürüyordu. Hafif bir yağmur başladı ve Niloya şapkasını aradı. Ama şapka başında yoktu, yolda bir dala takılmıştı. Niloya buraya gelirken en sevdiği şarkıyı söylemişti. Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü. Şarkının sonunda alçak bir dalın altına geldi. Sarı şapkası o dalın ucunda sallanıyordu. Niloya elini uzattı ve şapkasını aldı. Onu hemen başına taktı ve yağmurda ıslanmadı. Sonra sepetiyle fındık ağaçlarına döndü. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü"
   - Cümle 5: «Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü.»
   - Açıklama: Şarkı söylemek şapkanın dala takılması sebebine yönelmiyor; çözüm yalnız geri yürümek.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü"
   - Cümle 5: «Şarkıyı yeniden söyledi ve geldiği yoldan geri yürüdü.»
   - Açıklama: Şarkı söylemenin şapkayı bulmaya hiçbir işlevi yok ve çözüm şarkının sonunda sebepsizce dalın altına varmakla geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şarkının sonunda alçak bir dalın altına geldi"
   - Cümle 6: «Şarkının sonunda alçak bir dalın altına geldi.»
   - Açıklama: Şarkı sebepsizce Niloya'yı şapkanın yanına getiriyor gibi kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0027` birebir aynı, `@degisim: perde -> şapka` (tutuyorsan), ardından `@onarim: 4611aef5f81ac984d5750296f593787ae57809d9`, sonra gövde.

### Hikâye 3: tohum niloya-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0031
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kızak', fiil 'katılmak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: rüzgar ağabeyinin sepetindeki kekikleri uçurdu | kendi kekiklerinin yarısını ona verdi
@tohum: niloya-0031
@degisim: kızak -> sepet
Niloya ile Murat yeşil tepede kekik topluyordu. Birden güçlü bir rüzgar esti ve Murat'ın sepeti devrildi. Sepetteki kekikler rüzgarla uçup gitti. Murat boş sepetine baktı ve üzüldü. Niloya kendi dolu sepetine baktı. Sonra kekiklerinin yarısını Murat'ın sepetine koydu. "Al, abi, yarısı senin," dedi Niloya. "Sen çok yardımseversin, Niloya!" dedi Murat. Niloya ağabeyini daha çok sevindirmek için neşeli bir şarkı söyledi. Murat güldü ve hemen şarkıya katıldı. Niloya ile Murat tepede mutlu mutlu şarkı söylemeye devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "daha çok sevindirmek için neşeli bir şarkı söyledi"
   - Cümle 9: «Niloya ağabeyini daha çok sevindirmek için neşeli bir şarkı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunu çözmüyor, sorun paylaşmayla çözüldükten sonra süs olarak ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya ağabeyini daha çok sevindirmek için neşeli bir şarkı söyledi"
   - Cümle 9: «Niloya ağabeyini daha çok sevindirmek için neşeli bir şarkı söyledi.»
   - Açıklama: Sorun çözüldükten sonra şarkı sahnesi eklenmiş ve hikaye kekik sorunundan uzaklaşarak işlevsiz bir eklemeyle bitiyor.
   - Açıklama: Sorun çözüldükten sonra şarkı olaydan çıkmayan işlevsiz bir ek olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0031` birebir aynı, `@degisim: kızak -> sepet` (tutuyorsan), ardından `@onarim: 86c8fa330092bee1fcad358e36f63ad64fac0d68`, sonra gövde.

### Hikâye 4: tohum niloya-0032 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | annesi
@tohum: niloya-0032
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'zambak', fiil 'sıçratmak', sıfat 'tekerlekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | annesi
@plan: bir çiçeğin yanından bilinmeyen bir ses geldi | yavaşça bakıp sesi yapan damlaları buldu
@tohum: niloya-0032
@degisim: tekerlekli -> yeşil
Niloya annesiyle ormanda meyve topluyordu. Birden büyük bir zambağın yanından küçük bir ses geldi. Niloya bu sesi çok merak etti. "Anne, şu sese bakacağım," dedi Niloya. Annesi başını salladı ve onun arkasından yürüdü. Niloya yavaşça çiçeğe yaklaştı ve yaprakların altına baktı. Orada küçük bir su birikintisi vardı. Ağacın yeşil yapraklarından birikintiye damlalar düşüyordu. Her damla suyu biraz sıçratıyor ve o sesi yapıyordu. "Ses yağmurdan kalan damlalardan geliyor, anne!" dedi Niloya. Annesi gülümsedi ve "Doğru buldun," dedi. Sonra Niloya ile annesi meyve toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir zambağın yanından"
   - Cümle 2: «Birden büyük bir zambağın yanından küçük bir ses geldi.»
   - Açıklama: 'Zambak' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0032` birebir aynı, `@degisim: tekerlekli -> yeşil` (tutuyorsan), ardından `@onarim: a10c506eac122c0ee6f16d1dbda7b26ba8991a6a`, sonra gövde.

### Hikâye 5: tohum niloya-0033 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0033
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'çamaşır', fiil 'durdurmak', sıfat 'meşgul'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: ağaçların arasında beyaz bir şey sallanıyordu | yanına gidip baktı ve dala takılan çamaşırı buldu
@tohum: niloya-0033
Ormanda rüzgar esiyordu. Niloya ise fındıklarla meşguldü. Birden iki ağacın arasında beyaz bir şey gördü. Niloya toplamayı durdurdu ve o yana merakla baktı. O şey bir dala takılmıştı ve sallanıyordu. Niloya yavaş yavaş ağaçlara yaklaştı. Yakından bakınca onu tanıdı. Bu, ipten uçmuş bir çamaşırdı. Rüzgar onu evin bahçesinden buraya getirmişti. Niloya elini uzattı ve onu daldan kolayca aldı. Sonra onu güzelce katladı ve koluna aldı. Niloya çok sevindi, çünkü beyaz şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya ise fındıklarla meşguldü"
   - Cümle 2: «Niloya ise fındıklarla meşguldü.»
   - Açıklama: 'Meşguldü' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden iki ağacın arasında beyaz bir şey gördü"
   - Cümle 3: «Birden iki ağacın arasında beyaz bir şey gördü.»
   - Açıklama: Ağaçta sallanan beyaz bir şey görmek gerçek bir sorun değil, yalnız bir merak konusu.
   - Açıklama: Dalda sallanan beyaz bir şey gerçek bir sorun değil, yalnız merak konusu; çocuğun önemseyeceği bir sorun kurulmuyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra onu güzelce katladı ve koluna aldı"
   - Cümle 11: «Sonra onu güzelce katladı ve koluna aldı.»
   - Açıklama: Art arda cümlelerde 'onu' ve 'aldı' gereksiz yere tekrarlanıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "onu güzelce katladı ve koluna aldı"
   - Cümle 11: «Sonra onu güzelce katladı ve koluna aldı.»
   - Açıklama: 'onu' ve 'aldı' art arda cümlelerde gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0033` birebir aynı, ardından `@onarim: 1c401e1e53b33be2c0baeb8b1316fed3eb677801`, sonra gövde.

### Hikâye 6: tohum niloya-0035 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Murat
@tohum: niloya-0035
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'toka', fiil 'katlamak', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | Murat
@plan: sormadan attığı uçak duvara çarpıp ezildi | özür diledi ve abisiyle yeni uçak katladı
@tohum: niloya-0035
@degisim: toka -> kağıt
Bir sabah Murat bahçede yeşil bir kağıttan uçak yapıyordu. Niloya uçağı görünce çok sevindi ve hemen aldı. Ama Murat'a sormadan atınca uçak duvara çarptı ve ezildi. Murat uçağına üzgün üzgün baktı. Niloya abisinden hemen özür diledi. Sonra ona uçağı nasıl yaptığını sordu. Murat yeni bir kağıt aldı ve ona yavaşça gösterdi. Niloya kağıdı dikkatle ikiye katladı. Sonunda yeni uçak hazırdı. Bu kez Niloya uçağı abisine verdi ve ilk sırayı ona bıraktı. Uçak bahçede uzun uzun uçtu. Sonra Niloya ile Murat uçağı sırayla atıp mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Murat bahçede yeşil bir kağıttan"
   - Cümle 1: «Bir sabah Murat bahçede yeşil bir kağıttan uçak yapıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0035` birebir aynı, `@degisim: toka -> kağıt` (tutuyorsan), ardından `@onarim: 9f48be2aaf089efa9cfc835c2c8cbec4ced477ee`, sonra gövde.

### Hikâye 7: tohum niloya-0036 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0036
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'kürek', fiil 'anlatmak', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: dedesi küreğini evde unutmuştu | küçük küreğini dedesiyle paylaştı ve fidanı birlikte diktiler
@tohum: niloya-0036
Bir sabah Niloya ile dedesi ormana bir fındık fidanı getirdi. Fidan için yerde bir çukur açmak gerekiyordu. Ama dedesi küreğini evde unutmuştu ve yalnız Niloya'nın küçük küreği vardı. Niloya küreğini hemen dedesine uzattı. Sonra ona fidanı nereye koyacaklarını sordu. Dedesi küreği aldı ve çukur açarken ona her adımı anlattı. Önce dedesi kazdı, sonra sıra Niloya'ya geldi. Siyah toprak yumuşaktı ve çukur çabucak açıldı. Niloya fidanı çukura koydu ve dedesi toprağı bastırdı. Sonra Niloya ile dedesi yeni fidanın yanına oturdu ve mutlu mutlu dinlendi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yalnız Niloya'nın küçük küreği vardı"
   - Cümle 3: «Ama dedesi küreğini evde unutmuştu ve yalnız Niloya'nın küçük küreği vardı.»
   - Açıklama: Ellerinde zaten kullanılabilir bir kürek olduğu için ortada gerçek bir sorun yok, küçük kürek hiç zorluk çıkarmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra ona fidanı nereye koyacaklarını sordu"
   - Cümle 5: «Sonra ona fidanı nereye koyacaklarını sordu.»
   - Açıklama: Soru hiç cevaplanmıyor ve olayda işe yaramayan bir ayrıntı olarak kalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "fidanı nereye koyacaklarını sordu"
   - Cümle 5: «Sonra ona fidanı nereye koyacaklarını sordu.»
   - Açıklama: Niloya'nın sorusu cevapsız kalıyor ve olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0036` birebir aynı, ardından `@onarim: c5ed099d9938aad829e9fadaab9fc509e04f1313`, sonra gövde.

### Hikâye 8: tohum niloya-0037 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0037
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'gül', fiil 'paylaşmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: rüzgarın getirdiği poşet güllerin üstüne takıldı | çalıya dikkatle bakıp poşeti yavaşça çıkardı
@tohum: niloya-0037
@degisim: paylaşmak -> katlamak
Ormanda kuşlar ötüyordu. Niloya fındık ağaçlarının yanında kırmızı güllerle dolu bir çalı gördü. Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı. Poşet çiçeklerin çoğunu kapatıyordu. Niloya merakla çalının etrafında dolaştı ve baktı. Poşet yalnız tek bir dala takılmıştı. Niloya dalı yavaşça tuttu ve poşeti oradan çıkardı. Hiçbir dal kırılmadı. Niloya poşeti küçük küçük katladı ve cebine koydu. Şimdi bütün çiçekler yeniden görünüyordu. Niloya çok sevindi, çünkü plastik poşeti güllerin üstünden almıştı.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "kırmızı güllerle dolu bir çalı"
   - Cümle 2: «Niloya fındık ağaçlarının yanında kırmızı güllerle dolu bir çalı gördü.»
   - Açıklama: Kartın orman tarifi meyve ve fındık ağaçlarıyla sınırlı; gül çalısı tarifte yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya dalı yavaşça tuttu"
   - Cümle 7: «Niloya dalı yavaşça tuttu ve poşeti oradan çıkardı.»
   - Açıklama: Dikenli gül çalısının dalını elle tutmak çocuğun taklit edince zarar görebileceği bir davranış.
   - Açıklama: Dikenli gül çalısının dalını elle tutmak çocuğun taklit edince yaralanabileceği bir davranış.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "plastik poşeti güllerin üstünden almıştı"
   - Cümle 11: «Niloya çok sevindi, çünkü plastik poşeti güllerin üstünden almıştı.»
   - Açıklama: Son cümle poşetin güllerin üstünden alındığını gereksiz yere yeniden anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0037` birebir aynı, `@degisim: paylaşmak -> katlamak` (tutuyorsan), ardından `@onarim: 030c1c21358776c83b4505567990f6c13acc6a5a`, sonra gövde.

### Hikâye 9: tohum niloya-0038 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Mete
@tohum: niloya-0038
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'nilüfer', fiil 'gıdıklamak', sıfat 'güçlü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | park | Mete
@plan: tek salıncak vardı ve ikisi de binmek istedi | bir şarkı bitince sırayı değiştirmeyi önerdi
@tohum: niloya-0038
@degisim: nilüfer -> salıncak
Bir sabah Niloya ile Mete parka geldi. Parkta yalnız bir salıncak vardı ve ikisi de binmek istedi. İkisi de aynı anda oraya koştu. "Sırayla binelim, Mete, önce sen bin, şarkı bitince de ben," dedi Niloya. Mete sevindi ve ilk o oturdu. Niloya onu hafifçe itti ve neşeli bir şarkı söyledi. Şarkı bitince Mete hemen indi. "Sıra sende, Niloya," dedi Mete. Bu kez Mete güçlü kollarıyla salıncağı yavaş yavaş itti. Salıncak durunca Mete Niloya'yı gıdıkladı ve ikisi de güldü. "Bu şarkı oyunu çok güzel, Mete, yine oynayalım!" dedi Niloya.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "İkisi de aynı anda oraya koştu"
   - Cümle 3: «İkisi de aynı anda oraya koştu.»
   - Açıklama: Bir önceki cümledeki 'ikisi de' hemen tekrarlanıyor.
   - Açıklama: 'ikisi de' art arda cümlelerde gereksizce tekrarlanıyor.
2. **C6** (K merceği) — Kalıp yargı yok.
   - Alıntı: "Mete güçlü kollarıyla salıncağı"
   - Cümle 9: «Bu kez Mete güçlü kollarıyla salıncağı yavaş yavaş itti.»
   - Açıklama: Oğlanın güçlü kollarla öne çıkarılması kız-oğlan kalıp yargısı taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0038` birebir aynı, `@degisim: nilüfer -> salıncak` (tutuyorsan), ardından `@onarim: dd0175510ea6b0bb527ad1170973b5a0d65bc1c7`, sonra gövde.

### Hikâye 10: tohum niloya-0039 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0039
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'turp', fiil 'kalkmak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: hızla geri gelen top bankın altına kaçtı | bankın arkasına geçip topu kolayca aldı
@tohum: niloya-0039
@degisim: turp -> top
Parkta güneşli bir sabah Niloya yerde oturmuş, topunu kaydırağa yuvarlıyordu. Top her seferinde geri geliyordu ve Niloya gülüyordu. Ama bir kez top hızla geri geldi ve bankın altına kaçtı. Niloya hemen kalktı ve bankın yanına koştu. Top bankın altında, arka köşede duruyordu. Niloya kolunu uzattı ama topa yetişemedi. Sonra aklına bir soru geldi: Topu bankın arkasından alabilir miydi? Niloya bankın arkasına geçti ve topu kolayca aldı. Bu kez topu kaydırağa daha yavaş yuvarladı. Top kaydıraktan indi ve tam Niloya'nın önünde durdu. Niloya çok memnun oldu ve oyununa neşeyle devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aklına bir soru geldi"
   - Cümle 7: «Sonra aklına bir soru geldi: Topu bankın arkasından alabilir miydi?»
   - Açıklama: 'Aklına gelmek' deyimi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Aklına gelmek' bir deyim; 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0039` birebir aynı, `@degisim: turp -> top` (tutuyorsan), ardından `@onarim: 4ab8f438f4d42c3263c88a9761825731b6540665`, sonra gövde.
