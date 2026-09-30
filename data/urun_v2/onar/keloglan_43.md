# Editör görevi (onarım): Keloğlan, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0175 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0175
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'topaç', fiil 'kilitlemek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: topaç uzun çimenlerin üstünde dönmeden devrildi | nedenini öğrendi ve topacı düz bir taşın üstünde döndürdü
@tohum: keloglan-0175
@degisim: kilitlemek -> sarmak
Tepede güneşli ve güzel bir gündü. Keloğlan yeni tahta topacını döndürmek istiyordu. Ama çimenler uzundu ve topaç hemen devrildi. Keloğlan ipi yeniden sardı ve topacı bir daha attı. Topaç bu kez top gibi zıpladı ve yine yere düştü. Keloğlan kahkahalarla güldü. Sonra nedenini öğrenmek istedi. Yere eğildi ve çimenlere dikkatle baktı. Topaç uzun çimenlere takılıyordu. Keloğlan yakında büyük ve düz bir taş buldu. Sabırlı davrandı ve ipi sıkıca sardı. Topacı taşın üstüne attı ve topaç hızlı hızlı döndü. Keloğlan sevinçle ellerini çırptı. Keloğlan bundan sonra topacını hep düz bir yerde döndürdü.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Topaç bu kez top gibi zıpladı"
   - Cümle 5: «Topaç bu kez top gibi zıpladı ve yine yere düştü.»
   - Açıklama: Uzun çimende devrilen topacın top gibi zıplaması sebepten çıkmıyor ve olaya bir şey katmıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Topaç bu kez top gibi zıpladı"
   - Cümle 5: «Topaç bu kez top gibi zıpladı ve yine yere düştü.»
   - Açıklama: Topacın top gibi zıplaması, sonradan söylenen çimenlere takılma sebebiyle çelişiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sabırlı davrandı ve ipi sıkıca sardı"
   - Cümle 11: «Sabırlı davrandı ve ipi sıkıca sardı.»
   - Açıklama: Tohumdaki özellik öğrenmek; sabır ikinci bir özellik olarak ekleniyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sabırlı davrandı ve ipi"
   - Cümle 11: «Sabırlı davrandı ve ipi sıkıca sardı.»
   - Açıklama: Tohumdaki özellik öğrenme sevgisi; sabır karttaki özelliklere ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0175` birebir aynı, `@degisim: kilitlemek -> sarmak` (tutuyorsan), ardından `@onarim: 722dbe477cc344c6e72539065ed30979d1c7fa1c`, sonra gövde.

### Hikâye 2: tohum keloglan-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0176
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'bluz', fiil 'akmak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: derenin sesi yüzünden garip sesin yeri bulunamadı | dereden uzaklaşıp dinledi ve sesi yapan elmaları buldu
@tohum: keloglan-0176
@degisim: bluz -> elma
Rüzgar esiyordu ve dere şırıl şırıl akıyordu. Keloğlan ormanda büyük ağaçların arasında yürüyordu. Birden tak tak diye garip bir ses duydu. Ama derenin sesi yüzünden sesin yerini bulamadı. Keloğlan önce sağa, sonra sola yürüdü. Ses bir kesildi, bir yeniden geldi. Dürüst ve azimli Keloğlan yine de vazgeçmedi. Dereden biraz uzaklaştı ve dikkatle dinledi. Ses şimdi daha açık geliyordu. Sesin peşinden yürüdü ve büyük bir elma ağacı buldu. Rüzgar esince ağaçtan kıpkırmızı elmalar düşüyordu. Elmalar ağacın altındaki düz bir taşa çarpıp tak tak ses yapıyordu. Keloğlan güldü ve yerdeki elmaları topladı. Keloğlan bundan sonra merak ettiği bir sesi sonuna kadar aradı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama derenin sesi yüzünden sesin yerini bulamadı"
   - Cümle 4: «Ama derenin sesi yüzünden sesin yerini bulamadı.»
   - Açıklama: Plandaki sorun olan sesin yerinin bulunamaması ilk 3 cümlede değil, 4. cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dürüst ve azimli Keloğlan"
   - Cümle 7: «Dürüst ve azimli Keloğlan yine de vazgeçmedi.»
   - Açıklama: 'Azimli' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime ve olayla ilgisiz 'dürüst' ile birlikte etiket gibi kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0176` birebir aynı, `@degisim: bluz -> elma` (tutuyorsan), ardından `@onarim: 6a4cdfebb481c41606f613abf776bbf4c1182707`, sonra gövde.

### Hikâye 3: tohum keloglan-0177 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0177
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'meyve', fiil 'kırılmak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: dedenin hareketli icadı meyveleri yere düşürüyordu | kırık çubuğu dedeye söyledi ve yerine kaşık bağladı
@tohum: keloglan-0177
Keloğlan evde, Bilgecan Dede'nin yeni icadına bakıyordu. Dedenin hareketli bir tahta kolu vardı ve kol meyveleri sepete atıyordu. Ama kol meyveleri sepete değil, yere düşürüyordu. "İcadım güzel mi, Keloğlan?" diye sordu Bilgecan Dede. Keloğlan kolu izledi ve dürüst bir cevap verdi. "Güzel, ama kolun çubuğu kırılmış," dedi Keloğlan. Bilgecan Dede eğilip baktı ve başını salladı. Keloğlan mutfaktan tahta bir kaşık getirdi. Kaşığı bir iple kırık çubuğun yerine bağladı. Kol yeniden döndü ve bir elmayı tam sepete attı. Bilgecan Dede sevinçle ellerini çırptı. Keloğlan da çok mutlu oldu, çünkü dedenin icadı artık çalışıyordu.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kırık çubuğu dedeye söyledi"
   - Cümle 0 (plan satırı): «dedenin hareketli icadı meyveleri yere düşürüyordu | kırık çubuğu dedeye söyledi ve yerine kaşık bağladı»
   - Açıklama: 'Söylemek' fiili nesne olarak eşya almaz; 'çubuğun kırık olduğunu dedeye söyledi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kırık çubuğu dedeye söyledi"
   - Cümle 0 (plan satırı): «dedenin hareketli icadı meyveleri yere düşürüyordu | kırık çubuğu dedeye söyledi ve yerine kaşık bağladı»
   - Açıklama: Bir nesne söylenmez; 'kırık çubuğu dedeye gösterdi' ya da 'çubuğun kırık olduğunu söyledi' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bilgecan Dede'nin yeni icadına bakıyordu"
   - Cümle 1: «Keloğlan evde, Bilgecan Dede'nin yeni icadına bakıyordu.»
   - Açıklama: 'İcat' kelimesini 3 yaşındaki bir çocuk bilmez.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dedenin hareketli bir tahta kolu vardı"
   - Cümle 2: «Dedenin hareketli bir tahta kolu vardı ve kol meyveleri sepete atıyordu.»
   - Açıklama: Cümle dedenin kendisinin tahta kolu varmış gibi okunuyor; icadın kolu kastediliyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dedenin hareketli bir tahta kolu vardı"
   - Cümle 2: «Dedenin hareketli bir tahta kolu vardı ve kol meyveleri sepete atıyordu.»
   - Açıklama: 'Dedenin kolu' dedenin kendi kolu gibi okunuyor; kolun icada ait olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0177` birebir aynı, ardından `@onarim: 105a229e339292f73af11ff582d51ced185009cf`, sonra gövde.

### Hikâye 4: tohum keloglan-0179 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0179
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'limon', fiil 'kopmak', sıfat 'benekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: dolu piknik sepetinin sapı koptu ve sepet çok ağırdı | anasından yardım istedi ve mendille yeni bir sap yaptı
@tohum: keloglan-0179
Ormanda büyük ağaçların altı serin ve güzeldi. Keloğlan piknik sepetini taşıyarak anasıyla yürüyordu. Sepet doluydu ve sapı birden koptu. Sepetteki sarı limonlar yere yuvarlandı. Keloğlan limonları topladı ve sepeti kucağına aldı. Ama sepet ağırdı ve kucağından kaydı. Keloğlan güçlüymüş gibi yapmadı, dürüst davrandı. "Anne, sepet ağır, bana yardım eder misin?" diye sordu Keloğlan. Anası gülümsedi ve cebinden benekli bir mendil çıkardı. Keloğlan mendili sepete bağladı ve yeni bir sap yaptı. Sonra ikisi sepeti birlikte taşıdı. "Teşekkürler, anneciğim, şimdi sepet çok hafif!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama sepet ağırdı ve kucağından kaydı"
   - Cümle 6: «Ama sepet ağırdı ve kucağından kaydı.»
   - Açıklama: Sapın kopması ve sepetin ağırlığı iki ayrı sorun olarak kuruluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan güçlüymüş gibi yapmadı, dürüst davrandı"
   - Cümle 7: «Keloğlan güçlüymüş gibi yapmadı, dürüst davrandı.»
   - Açıklama: Olmayan bir davranışı anlatan soyut cümle küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan güçlüymüş gibi yapmadı"
   - Cümle 7: «Keloğlan güçlüymüş gibi yapmadı, dürüst davrandı.»
   - Açıklama: 'Güçlüymüş gibi yapmak' soyut bir anlatım ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0179` birebir aynı, ardından `@onarim: 71cf17256e912b81cdc58220d7f197d8190150e8`, sonra gövde.

### Hikâye 5: tohum keloglan-0180 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0180
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mürekkep', fiil 'kurtarmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: sağ eldiven karda aşağı kaydı ve kayboldu | düşen öbür eldivenin peşinden gidip ikisini de buldu
@tohum: keloglan-0180
@degisim: mürekkep -> eldiven
Keloğlan karlı tepede kardan bir kule yapıyordu. Kuleye küçük pencereler açmak için sağ eldivenini çıkarıp yere koydu. Ama eldiven kaygan karda aşağı kaydı ve kayboldu. Oyun oynarken karda bir sürü karışık iz yapmıştı. Keloğlan izlerin arasında eğilip baktı, ama eldiveni bulamadı. Sonra sakar Keloğlan sol eldivenini de elinden düşürdü. Sol eldiven de karda aşağı kaydı. Keloğlan onun nereye gittiğine dikkatle baktı ve peşinden yavaşça yürüdü. Sol eldiven bir kar yığınının dibinde durdu. Sağ eldiven de tam orada, karın içindeydi. Keloğlan iki eldiveni de kardan kurtardı. Eldivenleri salladı ve ellerine taktı. Sonra tepeye döndü ve kuleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Oyun oynarken karda bir sürü karışık iz yapmıştı"
   - Cümle 4: «Oyun oynarken karda bir sürü karışık iz yapmıştı.»
   - Açıklama: Önceki cümlenin öznesi eldiven olduğu için izleri kimin yaptığı belli değil.
   - Açıklama: Öznesiz cümlede son özne eldiven olduğu için izi kimin yaptığı belli değil.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sonra sakar Keloğlan sol eldivenini de elinden düşürdü"
   - Cümle 6: «Sonra sakar Keloğlan sol eldivenini de elinden düşürdü.»
   - Açıklama: İkinci eldivenin kayması hikayeye yeni bir sorun ekliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sol eldivenini de elinden düşürdü"
   - Cümle 6: «Sonra sakar Keloğlan sol eldivenini de elinden düşürdü.»
   - Açıklama: Çözüm figürün bilinçli bir eylemiyle değil, tesadüfi bir düşürmeyle sebepsizce geliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra sakar Keloğlan sol eldivenini de elinden düşürdü"
   - Cümle 6: «Sonra sakar Keloğlan sol eldivenini de elinden düşürdü.»
   - Açıklama: Kayıp eldiven figürün çabasıyla değil tesadüfi bir düşürmeyle bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0180` birebir aynı, `@degisim: mürekkep -> eldiven` (tutuyorsan), ardından `@onarim: b0f6155c17122d44c7de3ed0b68422c51c973430`, sonra gövde.

### Hikâye 6: tohum keloglan-0182 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0182
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tohum', fiil 'mırıldanmak', sıfat 'meşgul'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: rüzgar toprağın üstüne serpilen tohumları uçurdu | tohumları küçük çukurlara koyup üstünü toprakla örttü
@tohum: keloglan-0182
Tepede rüzgar hafif hafif esiyordu. Keloğlan çok meşguldü; ilk kez çiçek tohumu ekmeyi deniyordu. Ama tohumları toprağın üstüne atınca rüzgar onları uçurdu. Keloğlan yere eğildi ve dikkatle baktı. Bir tohum küçük bir çukura düşmüş ve orada kalmıştı. Keloğlan böylece yeni bir şey öğrendi: tohumlar çukurda kalıyordu. Yerden bir çubuk aldı ve toprakta küçük çukurlar açtı. Her çukura bir tohum koydu ve üstünü toprakla örttü. Bir yandan da bir şarkı mırıldanıyordu. Rüzgar yine esti, ama tohumlar yerinden kıpırdamadı. Keloğlan bütün tohumları ekti ve mutlu mutlu şarkısına devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan çok meşguldü"
   - Cümle 2: «Keloğlan çok meşguldü; ilk kez çiçek tohumu ekmeyi deniyordu.»
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir yandan da bir şarkı mırıldanıyordu"
   - Cümle 9: «Bir yandan da bir şarkı mırıldanıyordu.»
   - Açıklama: Şarkı sebepsiz beliriyor ve sorunun çözümünde hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0182` birebir aynı, ardından `@onarim: c66543d5b2851ed4d6f5e3a73cda246321cc5adc`, sonra gövde.

### Hikâye 7: tohum keloglan-0183 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0183
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'mücevher', fiil 'kıpırdamak', sıfat 'huzurlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: top dedenin taş kutusunu devirdi ve taşlar döküldü | özür diledi ve taşları tek tek topladı
@tohum: keloglan-0183
Bir sabah Keloğlan ormanda top oynuyordu. Bilgecan Dede yakında huzurlu bir yüzle taşlarını inceliyordu. Taşlar mücevher gibi parlıyordu. Keloğlan topa çok sert vurdu ve top dedenin taş kutusunu devirdi. Parlak taşlar yerdeki yaprakların arasına döküldü. Keloğlan bir an hiç kıpırdamadı. Sonra dürüst davrandı ve dedenin yanına gitti. "Özür dilerim, Bilgecan Dede, topa ben vurdum," dedi Keloğlan. "Doğruyu söyledin, teşekkürler, Keloğlan," dedi Bilgecan Dede. Keloğlan yaprakların arasından taşları tek tek topladı. Bütün taşları yeniden kutuya koydu. Bilgecan Dede gülümsedi, çünkü hiçbir taş eksik değildi. Keloğlan bundan sonra topla dedenin kutusundan uzakta oynadı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yakında huzurlu bir yüzle"
   - Cümle 2: «Bilgecan Dede yakında huzurlu bir yüzle taşlarını inceliyordu.»
   - Açıklama: 'Huzurlu bir yüzle' soyut bir anlatım, küçük çocuk için anlaşılır değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "huzurlu bir yüzle taşlarını"
   - Cümle 2: «Bilgecan Dede yakında huzurlu bir yüzle taşlarını inceliyordu.»
   - Açıklama: 'Huzurlu bir yüz' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Taşlar mücevher gibi parlıyordu"
   - Cümle 3: «Taşlar mücevher gibi parlıyordu.»
   - Açıklama: Benzetme ve 'mücevher' kelimesi 3 yaşındaki çocuğa uygun değil.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Taşlar mücevher gibi parlıyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Keloğlan topa çok sert vurdu ve top dedenin taş kutusunu devirdi.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0183` birebir aynı, ardından `@onarim: ccf5610c7a8c1b574380dcc3e45cd211cf54b9c1`, sonra gövde.

### Hikâye 8: tohum keloglan-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0184
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'portakal', fiil 'bozulmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: rüzgar hafif sepeti devirdi ve oyun bozuldu | düşen portakallar sepeti ağır yaptı ve sepet yerinde kaldı
@tohum: keloglan-0184
Bir sabah ormanda hava çok rüzgarlıydı. Keloğlan ile anası sırayla boş bir sepete kozalak atıyordu. Ama rüzgar hafif sepeti her seferinde devirdi ve oyun bozuldu. Yanlarında bir torba portakal vardı. "Şimdi kimin sırası, anne?" diye sordu Keloğlan. "Sıra sende, ama önce sepeti kaldır," dedi anası. Sakar Keloğlan sepeti kaldırırken portakal torbasını düşürdü. Torba açıldı ve portakallar sepetin içine döküldü. Rüzgar yine esti, ama ağır sepet bu kez devrilmedi. Keloğlan ile anası birbirine bakıp güldü. Keloğlan portakalları sepette bıraktı ve bir kozalak attı. Kozalak sepete girdi ve anası alkışladı. "Şimdi sıra sende, anneciğim, bu oyun çok eğlenceli!" dedi Keloğlan.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sepeti her seferinde devirdi"
   - Cümle 3: «Ama rüzgar hafif sepeti her seferinde devirdi ve oyun bozuldu.»
   - Açıklama: Tekrarlanan eylem için görünüş uyumsuz; 'her seferinde deviriyordu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanlarında bir torba portakal vardı"
   - Cümle 4: «Yanlarında bir torba portakal vardı.»
   - Açıklama: Portakal torbası çözümü sebepsizce getirmek için kuruluyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sakar Keloğlan sepeti kaldırırken portakal torbasını düşürdü"
   - Cümle 7: «Sakar Keloğlan sepeti kaldırırken portakal torbasını düşürdü.»
   - Açıklama: Sorun Keloğlan'ın bilinçli bir çözümüyle değil, torbayı kazayla düşürmesiyle çözülüyor.
   - Açıklama: Sorun figürün bilinçli bir çabasıyla değil kazayla çözülüyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Torba açıldı ve portakallar sepetin içine döküldü"
   - Cümle 8: «Torba açıldı ve portakallar sepetin içine döküldü.»
   - Açıklama: Çözüm sebebe bilinçli olarak yönelmiyor, tesadüfen gerçekleşiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Torba açıldı ve portakallar sepetin içine döküldü"
   - Cümle 8: «Torba açıldı ve portakallar sepetin içine döküldü.»
   - Açıklama: Çözümü getiren portakallar sepete tesadüfen dökülüyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0184` birebir aynı, ardından `@onarim: 68991e3ebe75ff1c514f41be807f5318f99cd323`, sonra gövde.
