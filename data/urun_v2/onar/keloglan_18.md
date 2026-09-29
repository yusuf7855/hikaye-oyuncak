# Editör görevi (onarım): Keloğlan, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar18.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0048 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0048
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'gölge', fiil 'alışmak', sıfat 'plastik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşek acıktı ama tepedeki otlar kuruydu | kayanın gölgesinde taze ot bulup eşeği çağırdı
@tohum: keloglan-0048
@degisim: plastik -> taze
Tepede sıcak bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan yavaşça yürüyordu. Karakaçan çok acıkmıştı ama buradaki otlar kuruydu. Eşek durdu ve yüksek sesle anırdı. Karakaçan yeşil otlara alışmıştı ve sarı otları yemedi. "Üzülme, sana taze ot bulacağım," dedi Keloğlan. Taşların arasına baktı ama hiç yeşil ot göremedi. Keloğlan yorulmuştu ama dürüsttü, eşeğine dediği gibi aramaya devam etti. Sonra büyük bir kayanın gölgesine baktı. Gölgede taze ve yeşil otlar vardı. Keloğlan ıslık çaldı ve Karakaçan hemen yanına geldi. Eşek otları yedi ve başını salladı. Karakaçan ile Keloğlan serin gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yorulmuştu ama dürüsttü"
   - Cümle 8: «Keloğlan yorulmuştu ama dürüsttü, eşeğine dediği gibi aramaya devam etti.»
   - Açıklama: 'Dürüst' aramaya devam etmek için yanlış anlamda kullanılmış; 'sözünü tuttu' kastediliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan yorulmuştu ama dürüsttü"
   - Cümle 8: «Keloğlan yorulmuştu ama dürüsttü, eşeğine dediği gibi aramaya devam etti.»
   - Açıklama: 'Dürüst' burada söz tutmak anlamında yanlış kullanılmış ve 'yorulmuştu ama' karşıtlığına uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0048` birebir aynı, `@degisim: plastik -> taze` (tutuyorsan), ardından `@onarim: 6aa5cddc31edc80a573f7c1eeb87e74b7423bcff`, sonra gövde.

### Hikâye 2: tohum keloglan-0049 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0049
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'balon', fiil 'şişirmek', sıfat 'elmalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: kırmızı balon çok sert olduğu için büyümedi | balonu önce çekip yumuşattı sonra şişirdi
@tohum: keloglan-0049
@degisim: elmalı -> kırmızı
Ormanda kuşlar neşeyle ötüyordu. Keloğlan ile Balkız ağaçların altında balon dükkanı oyunu oynuyordu. Balkız kırmızı bir balon istedi ama balon çok sertti ve hiç büyümüyordu. Keloğlan balonu çekip yumuşatmak istedi. Ama biraz sakardı ve balon elinden yere düştü. Keloğlan balonu yerden aldı ve iki eliyle birkaç kez çekip gerdi. Balon biraz yumuşadı. Sonra Keloğlan derin bir nefes aldı ve balonu şişirdi. Kırmızı balon yavaş yavaş büyüdü. "İşte kırmızı balonun, Balkız!" dedi Keloğlan. Balkız balonu aldı ve sevinçle güldü. Sonra ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "biraz sakardı ve balon elinden yere düştü"
   - Cümle 5: «Ama biraz sakardı ve balon elinden yere düştü.»
   - Açıklama: Tohumdaki sakarlık özelliği balonun düşmesiyle gösteriliyor ama çözüme hiçbir katkısı yok, yani işe yarar biçimde kullanılmamış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama biraz sakardı ve balon elinden yere düştü"
   - Cümle 5: «Ama biraz sakardı ve balon elinden yere düştü.»
   - Açıklama: Balonun yere düşmesi hiçbir sonuç doğurmuyor; olaya bağlanmayan işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "balon elinden yere düştü"
   - Cümle 5: «Ama biraz sakardı ve balon elinden yere düştü.»
   - Açıklama: Balonun düşmesi hiçbir sonuç doğurmuyor; işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0049` birebir aynı, `@degisim: elmalı -> kırmızı` (tutuyorsan), ardından `@onarim: 686c965946e3feb08b5e5caf7d20ca4c095880c8`, sonra gövde.

### Hikâye 3: tohum keloglan-0052 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0052
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'poğaça', fiil 'bükmek', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annesinin hamuru çoktu ve kolları yorulmuştu | poğaça yapmayı öğrendi ve annesine yardım etti
@tohum: keloglan-0052
@degisim: narin -> yumuşak
Dışarıda yağmur yağıyordu. Keloğlan mutfakta anasının yanına geldi. Anası poğaça yapıyordu ama hamur çok fazlaydı ve kolları yorulmuştu. "Anneciğim, ben de poğaça yapmayı öğrenmek istiyorum," dedi Keloğlan. Anası küçük bir hamur parçasını açtı ve ay gibi büktü. "Hamur yumuşak, yavaşça bük," dedi anası. Keloğlan ilk poğaçayı biraz yamuk yaptı ve ikisi de güldü. İkinci poğaçayı ise çok güzel yaptı. Sonra Keloğlan ile anası bütün hamuru birlikte bükerek tepsiye dizdi. Kısa sürede tepsi doldu. "Teşekkür ederim, Keloğlan, işimiz ne çabuk bitti!" dedi anası.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bütün hamuru birlikte bükerek tepsiye dizdi"
   - Cümle 9: «Sonra Keloğlan ile anası bütün hamuru birlikte bükerek tepsiye dizdi.»
   - Açıklama: Tek parça hamur tepsiye dizilmez; dizilen poğaçalardır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0052` birebir aynı, `@degisim: narin -> yumuşak` (tutuyorsan), ardından `@onarim: 6578916dfe12e10dcfa744bc68542cf6341044ea`, sonra gövde.

### Hikâye 4: tohum keloglan-0053 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0053
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'dolma', fiil 'esmek', sıfat 'parlak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek sırasını bekleyemedi ve topu hep kendisi itti | bir sen bir ben diyerek sırayla oynamayı önerdi
@tohum: keloglan-0053
@degisim: dolma -> top
Bir sabah Keloğlan ile eşeği Karakaçan ormanda top oynuyordu. Parlak topu sırayla büyük bir ağaca doğru itiyorlardı. Ama Karakaçan sırasını bekleyemedi ve topu hep kendisi itti. Keloğlan Karakaçan'ın başını okşadı. "Karakaçan, bir sen, bir ben oynayalım," dedi Keloğlan. Karakaçan başını salladı. Keloğlan topa ayağıyla vurdu ve kenara çekildi. Sonra Karakaçan topu burnuyla ileri sürdü. Tam o anda rüzgar esti ve top ağaca kadar yuvarlandı. Keloğlan dürüst davrandı. "Bu sefer sen kazandın, Karakaçan!" dedi Keloğlan. Keloğlan çok mutluydu, çünkü sırayla oynamak yine eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o anda rüzgar esti"
   - Cümle 9: «Tam o anda rüzgar esti ve top ağaca kadar yuvarlandı.»
   - Açıklama: Rüzgar sebepsizce gelip topu ağaca götürüyor ve hiç kurulmamış bir yarışın kazananını belirliyor.
   - Açıklama: Rüzgar sebepsiz beliriyor ve sonucu figür yerine belirliyor; ardından gelen dürüstlük cümlesi olaydan çıkmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 10: «Keloğlan dürüst davrandı.»
   - Açıklama: Dürüstlük cümlesi olaydan çıkmıyor; ortada dürüstlük gerektiren bir durum yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0053` birebir aynı, `@degisim: dolma -> top` (tutuyorsan), ardından `@onarim: 1b10db0b7d28cb39e36a21593aa6340de882e638`, sonra gövde.

### Hikâye 5: tohum keloglan-0055 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0055
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kilit', fiil 'oynatmak', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: kolyenin kilidi açıldı ve boncuklar çimenlere döküldü | boncukları tek tek bulup hepsini arkadaşına verdi
@tohum: keloglan-0055
@degisim: çekingen -> parlak
Şatonun geniş bahçesinde Balkız ile Keloğlan oturuyordu. Balkız kolyesinin kilidini parmaklarıyla oynatıyordu. Birden kilit açıldı ve boncuklar çimenlere döküldü. "Ah, kolyem!" dedi Balkız. Keloğlan hemen çimenlere eğildi. Boncukları tek tek topladı ve saydı. Keloğlan dürüst davrandı. "Bir boncuk eksik, Balkız," dedi Keloğlan. Sonra aramaya devam etti. Sonunda bir çiçeğin dibinde parlak bir boncuk buldu. Keloğlan bütün boncukları Balkız'a verdi. Balkız boncukları ipe dizdi ve kilidi sıkıca kapattı. "Teşekkür ederim, Keloğlan, kolyem yine tamam!" dedi Balkız. Keloğlan çok mutlu oldu, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı."
   - Cümle 7: «Keloğlan dürüst davrandı.»
   - Açıklama: Boncukları toplayıp saymak dürüstlük göstermiyor; özellik kelimesi olaya uymayan yerde kullanılmış.
   - Açıklama: Boncuk toplayıp saymak dürüstlük değil; 'dürüst davrandı' olaya uymadan araya konmuş.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 7: «Keloğlan dürüst davrandı.»
   - Açıklama: Dürüstlük cümlesi olaydan çıkmıyor ve hikayede hiçbir işe yaramayan eklenmiş bir ayrıntı.
   - Açıklama: Eksik boncuğu söylemek dürüstlükle ilgisiz; cümle işlevsiz ve olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0055` birebir aynı, `@degisim: çekingen -> parlak` (tutuyorsan), ardından `@onarim: e1d911dbdc8c560129d2b7a5818cad1811c0a241`, sonra gövde.

### Hikâye 6: tohum keloglan-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0057
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kalem', fiil 'bindirmek', sıfat 'tozlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: tepede tuhaf bir ses duyuldu | sesin peşinden gidip kayada küçük bir delik buldu
@tohum: keloglan-0057
@degisim: bindirmek -> karıştırmak
Rüzgar esiyordu ve tepede tuhaf bir ses duyuluyordu. Keloğlan tozlu bir taşa oturmuş, kalemiyle resim çiziyordu. Bu sesi çok merak etti. Keloğlan önce bu sesi yanında otlayan eşeği Karakaçan'ın sesiyle karıştırdı. "Karakaçan, bunu sen mi yapıyorsun?" diye sordu Keloğlan. Karakaçan başını iki yana salladı. Keloğlan sesin peşinden kayaların arasına yürüdü. Keloğlan biraz sakardı ve kalemini yere düşürdü. Kalemi almak için eğilince bir kayanın dibinde küçük bir delik gördü. Rüzgar bu delikten geçerken ıslık gibi bir ses çıkıyordu. Keloğlan kalemiyle deliği de resmine çizdi. "Bak, Karakaçan, sesi yapan bu küçük delik!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve kalemini yere düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve kalemini yere düşürdü.»
   - Açıklama: Deliği Keloğlan'ın araması değil, kalemin tesadüfen düşmesi buluyor; çözüm sebepsizce geliyor.
   - Açıklama: Delik Keloğlan'ın aramasıyla değil kalemin tesadüfen düşmesiyle bulunuyor; çözümü sebepsiz bir kaza getiriyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "delikten geçerken ıslık gibi bir ses çıkıyordu"
   - Cümle 10: «Rüzgar bu delikten geçerken ıslık gibi bir ses çıkıyordu.»
   - Açıklama: Özne uyumsuz; 'Rüzgar ... geçerken ıslık gibi bir ses çıkarıyordu' olmalı.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: ""Bak, Karakaçan, sesi yapan bu küçük delik!" dedi Keloğlan"
   - Cümle 12: «"Bak, Karakaçan, sesi yapan bu küçük delik!" dedi Keloğlan.»
   - Açıklama: Hikaye yalnız deliği gösteren bir cümleyle bitiyor; sıcak bir kapanış ya da olaya bağlı bir his yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0057` birebir aynı, `@degisim: bindirmek -> karıştırmak` (tutuyorsan), ardından `@onarim: 49a5c9da7e197b4590a48b876dbb9018ab9e1463`, sonra gövde.

### Hikâye 7: tohum keloglan-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0058
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'atkı', fiil 'kutlamak', sıfat 'yetenekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: ikisi ipi aynı anda çekti ve topaç devrildi | sırayla oynamayı önerdi ve ipi düzgünce sardı
@tohum: keloglan-0058
@degisim: atkı -> topaç
Keloğlan ile Bilgecan Dede evde tahta bir topaçla oynuyordu. Topacın yalnız bir ipi vardı. İkisi de ipi aynı anda çekti ve topaç devrildi. "Sırayla oynayalım, önce sen çevir, dede," dedi Keloğlan. Dede ipi çekince topaç masada uzun uzun döndü. "Dede, sen topaç çevirmede çok yeteneklisin!" dedi Keloğlan. Sonra sıra Keloğlan'a geldi. Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve düzgünce sardı. Keloğlan ipi çekince topaç da dedeninki kadar uzun döndü. İkisi bu güzel dönüşü el çırparak kutladı. Keloğlan çok sevindi, çünkü sırayla oynamak ikisini de mutlu etmişti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sen topaç çevirmede çok yeteneklisin"
   - Cümle 6: «"Dede, sen topaç çevirmede çok yeteneklisin!" dedi Keloğlan.»
   - Açıklama: 'Yetenekli' 3 yaşındaki çocuk için soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "topaç çevirmede çok yeteneklisin"
   - Cümle 6: «"Dede, sen topaç çevirmede çok yeteneklisin!" dedi Keloğlan.»
   - Açıklama: 'Yetenekli' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve düzgünce sardı"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve düzgünce sardı.»
   - Açıklama: Tohumdaki sakarlık güvenli özellik kullanımı satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak gösterilmiyor, yalnız adı anılıp işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden ipi yavaşça"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden ipi yavaşça ve düzgünce sardı.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı yalnız düşürme ya da karıştırma olarak tanımlıyor; burada sakarlık gösterilmeden yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0058` birebir aynı, `@degisim: atkı -> topaç` (tutuyorsan), ardından `@onarim: e31dabeaf75c09efcf8ee2b9962956c0ae3dbd91`, sonra gövde.

### Hikâye 8: tohum keloglan-0061 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0061
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'davul', fiil 'parıldamak', sıfat 'saygılı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annesine sormadan tencereyi alıp davul gibi çaldı | özür dileyip tencereyi geri verdi
@tohum: keloglan-0061
Keloğlan evde davul çalmayı öğrenmek istedi. Anasına sormadan mutfaktan parıldayan büyük tencereyi aldı. Tencereyi ters çevirdi ve kaşıkla davul gibi çaldı. Tam o sırada anası mutfağa girdi. "Keloğlan, tencerem nerede, çorba pişirecektim," dedi anası. Keloğlan tencereyi hemen anasına geri verdi. "Sormadan aldım, özür dilerim, anneciğim," dedi Keloğlan saygılı bir sesle. Anası gülümsedi ve onu kucakladı. Sonra dolaptan eski bir tahta kova çıkardı. "Bu kova senin davulun olsun," dedi anası. Anası çorbayı pişirirken Keloğlan kovaya kaşıkla vurdu. İkisi mutfakta mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "davul çalmayı öğrenmek istedi"
   - Cümle 1: «Keloğlan evde davul çalmayı öğrenmek istedi.»
   - Açıklama: Tohumdaki öğrenme özelliği yalnız anılıyor, sorunun çözümünde (özür) işe yaramıyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "tencerem nerede, çorba pişirecektim,"
   - Cümle 5: «"Keloğlan, tencerem nerede, çorba pişirecektim," dedi anası.»
   - Açıklama: Soru cümlesi soru işaretiyle bitmiyor; 'tencerem nerede?' olmalı.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonra dolaptan eski bir tahta kova çıkardı"
   - Cümle 9: «Sonra dolaptan eski bir tahta kova çıkardı.»
   - Açıklama: Keloğlan'ın davul çalma hedefini figür değil anası kovayı vererek çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0061` birebir aynı, ardından `@onarim: 0e526f199669596ffcefa5265e835cee4b949d58`, sonra gövde.

### Hikâye 9: tohum keloglan-0063 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0063
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kağıt', fiil 'sıçramak', sıfat 'kilitli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: rüzgar kağıt topu sepetten uzağa itti | rüzgarın durmasını bekledi ve topu yavaşça attı
@tohum: keloglan-0063
@degisim: kilitli -> beyaz
Rüzgar tepede hafif hafif esiyordu. Keloğlan beyaz kağıttan topunu eşeği Karakaçan'ın sırtındaki sepete atmak istiyordu. Ama rüzgar kağıt topu her seferinde sepetten uzağa itti. Bir kez top Karakaçan'ın kulağına değdi. Karakaçan şaşırdı ve yerinde sıçradı. Keloğlan eşeğinin başını yavaşça okşadı. Sonra top sepetin hemen yanına düştü. Keloğlan dürüst davrandı. "Bu atış sayılmaz, Karakaçan, top dışarıda kaldı," dedi Keloğlan. Sonra rüzgarın durmasını bekledi. Rüzgar durunca topu yavaşça attı. Kağıt top sepetin içine düştü. Karakaçan başını salladı ve neşeyle anırdı. Keloğlan çok sevindi, çünkü kağıt topu sonunda sepete sokmuştu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir kez top Karakaçan'ın kulağına değdi"
   - Cümle 4: «Bir kez top Karakaçan'ın kulağına değdi.»
   - Açıklama: Bir hayvanın başına doğru bir şey atmak çocuğun taklit edebileceği bir davranış olarak gösteriliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "top Karakaçan'ın kulağına değdi"
   - Cümle 4: «Bir kez top Karakaçan'ın kulağına değdi.»
   - Açıklama: Hayvana doğru bir şey atıp ona değdirmek çocuğun taklit edebileceği bir davranış olarak gösteriliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kez top Karakaçan'ın kulağına değdi"
   - Cümle 4: «Bir kez top Karakaçan'ın kulağına değdi.»
   - Açıklama: Topun eşeğin kulağına değmesi ve eşeğin okşanması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Topun eşeğin kulağına değmesi, sıçrama ve okşama sorunu ya da çözümü ilerletmeyen işlevsiz bir ara olay.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 8: «Keloğlan dürüst davrandı.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunun çözümüne katkı vermiyor; sorun rüzgarın durmasını beklemekle çözülüyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu atış sayılmaz, Karakaçan"
   - Cümle 9: «"Bu atış sayılmaz, Karakaçan, top dışarıda kaldı," dedi Keloğlan.»
   - Açıklama: Dürüstlük sahnesi özellik için eklenmiş, sorunun çözümüyle bağı olmayan işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0063` birebir aynı, `@degisim: kilitli -> beyaz` (tutuyorsan), ardından `@onarim: 5a8ddccdd0671267bd7238a767d8a6f25ae7181d`, sonra gövde.

### Hikâye 10: tohum keloglan-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0064
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'önlük', fiil 'çözülmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepede nereden geldiği belli olmayan bir ses vardı | aramayı bırakmadı ve sesi yapan buzu buldu
@tohum: keloglan-0064
@degisim: önlük -> buz
Hava soğuktu ama güneş parlıyordu. Keloğlan tepede yürürken küçük bir ses duydu. Ses hep aynıydı, nereden geldiği belli değildi. Keloğlan bu sesi çok merak etti. Önce büyük bir çalının arkasına baktı, orası boştu. Sonra ağaçların altını aradı, yine bulamadı. Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı. Sesi dinleyerek bir kayanın yanına gitti. Kayanın üstünde ışıltılı bir buz parçası vardı. Güneşte buzun ucu çözüldü ve küçük damlalar taşa düştü. Sesi bu damlalar yapıyordu. Keloğlan çok sevindi, çünkü sesin nereden geldiğini sonunda bulmuştu.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "nereden geldiği belli değildi"
   - Cümle 3: «Ses hep aynıydı, nereden geldiği belli değildi.»
   - Açıklama: Sorun yalnız merak edilen küçük bir ses; çocuğun önemseyeceği bir sorun ya da tehlike kurulmuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce büyük bir çalının arkasına baktı"
   - Cümle 5: «Önce büyük bir çalının arkasına baktı, orası boştu.»
   - Açıklama: Çözüm çalı, ağaçlar ve kaya olmak üzere ikiden fazla adım sürüyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Dürüstlük aramayı bırakmamakla ilgili değil; kelime yanlış anlamda kullanılmış.
   - Açıklama: Dürüstlük aramayı sürdürmekle ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Kartın özellik alanındaki dürüstlük aramayı sürdürmenin nedeni gibi yanlış kullanılıyor; dürüstlük işe yarar biçimde gösterilmiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Tohum kökü dürüst, azim gerektiren aramayı bırakmama davranışının gerekçesi olarak yanlış bağlamda kullanılıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Aramayı bırakmamanın sebebi olarak dürüstlük gösteriliyor; olayla ilgisi yok.
   - Açıklama: Dürüstlük aramayı sürdürmenin sebebi değil; olay bir öncekinden mantıklı olarak çıkmıyor.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "üstünde ışıltılı bir buz"
   - Cümle 9: «Kayanın üstünde ışıltılı bir buz parçası vardı.»
   - Açıklama: 'Işıltılı' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
8. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "buzun ucu çözüldü"
   - Cümle 10: «Güneşte buzun ucu çözüldü ve küçük damlalar taşa düştü.»
   - Açıklama: Buz çözülmez, erir; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0064` birebir aynı, `@degisim: önlük -> buz` (tutuyorsan), ardından `@onarim: 73660d019a139cc3386c5ed09892ffd5f8ef3d05`, sonra gövde.

### Hikâye 11: tohum keloglan-0065 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0065
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tuğla', fiil 'çekinmek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kırmızı elmalar yüksek bir dalda duruyordu | önce çekindi sonra anasından yardım istedi
@tohum: keloglan-0065
@degisim: tuğla -> elma
Ormanda kuşlar ötüyordu. Keloğlan ile anası büyük bir ağacın altında elma topluyordu. Ama en kırmızı elmalar yüksek bir dalda duruyordu ve Keloğlan onlara yetişemedi. Keloğlan önce yardım istemeye çekindi. Sonra dürüst davrandı ve anasına döndü. "Anneciğim, dal çok yüksek, bana yardım eder misin?" diye sordu Keloğlan. "Tabii ki," dedi anası. Anası dalı temkinli ve yavaş bir şekilde aşağı eğdi. Keloğlan kırmızı elmaları tek tek sepete koydu. Sepet kısa sürede doldu. Sonra ikisi ağacın gölgesinde oturdu ve elmaları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra dürüst davrandı"
   - Cümle 5: «Sonra dürüst davrandı ve anasına döndü.»
   - Açıklama: Yardım istemek dürüstlük değildir; kelime yanlış anlamda kullanılmış.
   - Açıklama: Yardım istemek dürüstlük değildir; 'dürüst' kelimesi yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra dürüst davrandı ve anasına döndü"
   - Cümle 5: «Sonra dürüst davrandı ve anasına döndü.»
   - Açıklama: Tohum özelliği dürüstlük/azim; yardım istemek dürüstlük diye adlandırılıyor ama özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki dürüstlük/azim özelliği kartta tanımlandığı gibi işe yaramıyor; yardım istemek dürüstlük olarak etiketlenmiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra dürüst davrandı ve anasına döndü"
   - Cümle 5: «Sonra dürüst davrandı ve anasına döndü.»
   - Açıklama: Yardım istemek dürüstlükle ilgili değil; dürüstlük olaydan çıkmadan sebepsizce ekleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dalı temkinli ve yavaş"
   - Cümle 8: «Anası dalı temkinli ve yavaş bir şekilde aşağı eğdi.»
   - Açıklama: 'Temkinli' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0065` birebir aynı, `@degisim: tuğla -> elma` (tutuyorsan), ardından `@onarim: 7a0bd587c877fb6b765e15f4dbb6e2ac0490730a`, sonra gövde.

### Hikâye 12: tohum keloglan-0066 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0066
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'koni', fiil 'yankılanmak', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: sesi küçük çıktı ve tepede yankı yapmadı | yapraktan bir koni yaptı ve yeniden bağırdı
@tohum: keloglan-0066
Keloğlan ile Balkız tepede, yeni açan sarı çiçeklere bakıyordu. Keloğlan bu güzel günü kutlamak için "Yaşasın!" diye bağırdı. Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı. "Keloğlan, bir yaprağı sar ve koni yap," dedi Balkız. Keloğlan bu yeni şeyi hemen öğrenmek istedi. Büyük bir yaprak buldu ve onu koni gibi sardı. Sonra koniyi ağzına tuttu. "Yaşasın, çiçekler açtı!" diye bağırdı Keloğlan. Bu kez sesi tepede uzun uzun yankılandı. Çalışkan Balkız sevinçle ellerini çırptı. "Teşekkürler, Balkız, bu çok güzel bir kutlama oldu!" dedi Keloğlan.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi küçük çıktı"
   - Cümle 0 (plan satırı): «sesi küçük çıktı ve tepede yankı yapmadı | yapraktan bir koni yaptı ve yeniden bağırdı»
   - Açıklama: Plan satırında ses için 'küçük' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi çok küçük çıktı"
   - Cümle 3: «Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı.»
   - Açıklama: Ses için 'küçük' uygun değil; 'cılız' ya da 'kısık' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tepede hiç yankı yapmadı"
   - Cümle 3: «Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı.»
   - Açıklama: 'Yankı' kelimesi 3 yaşındaki bir çocuk için bilinmeyen, soyut bir kavram.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sesi çok küçük çıktı"
   - Cümle 3: «Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı.»
   - Açıklama: Sesin neden küçük çıktığı söylenmiyor; sorunun sebebi verilmiyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı"
   - Cümle 3: «Ama sesi çok küçük çıktı ve tepede hiç yankı yapmadı.»
   - Açıklama: Sesin neden küçük çıktığı söylenmiyor ve sorun çocuk için zayıf bir sorun.
6. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "bir yaprağı sar ve koni yap"
   - Cümle 4: «"Keloğlan, bir yaprağı sar ve koni yap," dedi Balkız.»
   - Açıklama: Çözüm fikrini Balkız veriyor, Keloğlan yalnız uyguluyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Keloğlan, bir yaprağı sar ve koni yap"
   - Cümle 4: «"Keloğlan, bir yaprağı sar ve koni yap," dedi Balkız.»
   - Açıklama: Çözüm fikrini Keloğlan istemeden Balkız veriyor; figür yalnız uyguluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0066` birebir aynı, ardından `@onarim: 63f4ef7dc01072d3c6662f7c10ccc5ffc23c9dcf`, sonra gövde.
