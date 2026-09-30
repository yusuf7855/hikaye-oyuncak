# Editör görevi (onarım): Keloğlan, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0122
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yonca', fiil 'götürmek', sıfat 'sert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: rüzgar otları sallıyordu ve yaprakları saymak zordu | otları eliyle tuttu ve birer birer saydı
@tohum: keloglan-0122
Rüzgar ormanda sert esiyordu. Keloğlan ilk kez dört yapraklı bir yonca aramayı denedi. Ama rüzgar yüzünden otlar hep sallanıyordu ve yaprakları saymak zordu. Birden dört yapraklı gibi görünen bir yonca gördü. Keloğlan dürüst davrandı ve onu hemen almadı. Önce eliyle tuttu ve yapraklarını saydı. Yaprakları aslında üç taneydi. O sırada bir şey gördü: elindeki ot hiç sallanmıyordu. Keloğlan otları birer birer eliyle tuttu ve yapraklara baktı. Sonunda gerçek bir dört yapraklı yonca buldu. Keloğlan onu eve götürmek için dikkatle cebine koydu ve sevinçle güldü.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı ve"
   - Cümle 5: «Keloğlan dürüst davrandı ve onu hemen almadı.»
   - Açıklama: Yoncayı hemen almamak dürüstlük değildir; kelime yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı ve onu hemen almadı"
   - Cümle 5: «Keloğlan dürüst davrandı ve onu hemen almadı.»
   - Açıklama: Yoncayı hemen almamak dürüstlük değildir; özellik kelimesi yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı ve onu hemen almadı"
   - Cümle 5: «Keloğlan dürüst davrandı ve onu hemen almadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği yoncayı hemen almamak gibi dürüstlükle ilgisiz bir davranışa bağlanarak işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı ve onu hemen almadı"
   - Cümle 5: «Keloğlan dürüst davrandı ve onu hemen almadı.»
   - Açıklama: Yoncayı hemen almamak dürüstlükle ilgili değil; özellik olaydan çıkmadan sebepsizce ekleniyor.
   - Açıklama: Dürüstlük olayla ilgisiz; yonca almamak dürüstlükle açıklanamaz ve ayrıntı olaydan çıkmıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yaprakları aslında üç taneydi"
   - Cümle 7: «Yaprakları aslında üç taneydi.»
   - Açıklama: 'Aslında' soyut bir kelime, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0122` birebir aynı, ardından `@onarim: c18013eee5517a13b7974c120f9b24d2de161615`, sonra gövde.

### Hikâye 2: tohum keloglan-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0124
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fıstık', fiil 'tanışmak', sıfat 'dağınık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: rüzgar taşları yapraklarla örttü ve saklanan paket kayboldu | düşen fıstıkları görüp doğru taşı buldu
@tohum: keloglan-0124
Rüzgar tepede sert esiyordu. Keloğlan, Balkız ile tanıştığı bu tepede bir taşın altına fıstık saklamıştı. Ama rüzgar taşları yapraklarla örttü ve Keloğlan fıstık paketini bulamadı. "Keloğlan, neden buraya geldik?" diye sordu Balkız. "Sana bir sürprizim var," dedi Keloğlan. Keloğlan yaprakların arasına dikkatle baktı. Birden yerde dağınık duran üç fıstık gördü. Paketi koyarken sakar bir hareketle onları düşürmüştü. Üçü de düz bir taşın yanındaydı. Keloğlan taşı kaldırdı ve paketi buldu. "İşte, en sevdiğin fıstıklar!" dedi Keloğlan. Balkız paketi aldı ve sevinçle güldü. Keloğlan da çok sevindi, çünkü sürprizi Balkız'ı mutlu etmişti.
```

**Hakem bulguları (5):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Balkız ile tanıştığı bu tepede"
   - Cümle 2: «Keloğlan, Balkız ile tanıştığı bu tepede bir taşın altına fıstık saklamıştı.»
   - Açıklama: Kartın yanlar bölümünde Balkız ile tepede tanışıldığına dair bilgi yok; uydurma geçmiş ekleniyor.
   - Açıklama: Kartın dağ yeri kararı dizi bilgisi eklenmeyeceğini söylüyor; Balkız ile tepede tanışma uydurma bir dizi bilgisi.
2. **K5** (K merceği) — Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
   - Alıntı: "Sana bir sürprizim var"
   - Cümle 5: «"Sana bir sürprizim var," dedi Keloğlan.»
   - Açıklama: Tanışılan yerde sürpriz sahnesi kartın dünya kurallarındaki aşk konusu yasağına yaklaşan romantik bir çağrışım taşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden yerde dağınık duran üç fıstık gördü"
   - Cümle 7: «Birden yerde dağınık duran üç fıstık gördü.»
   - Açıklama: Düşen fıstıklar ancak çözüm anında sonradan uyduruluyor ve sert rüzgara rağmen yerinde kalıyor; çözüm sebepsizce geliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sakar bir hareketle onları"
   - Cümle 8: «Paketi koyarken sakar bir hareketle onları düşürmüştü.»
   - Açıklama: 'Sakar' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Paketi koyarken sakar bir hareketle onları düşürmüştü"
   - Cümle 8: «Paketi koyarken sakar bir hareketle onları düşürmüştü.»
   - Açıklama: Çözümü getiren fıstık ipucu önceden kurulmadan sonradan uydurulan bir geçmiş olayla açıklanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0124` birebir aynı, ardından `@onarim: 0cfb7efe836330fc9d2c8edffed0d307d930307c`, sonra gövde.

### Hikâye 3: tohum keloglan-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0125
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ayakkabı', fiil 'atlamak', sıfat 'zeki'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğin sırtındaki sepetin ipi bir çalıya takıldı | ipi çalının dallarından yavaş yavaş çözdü
@tohum: keloglan-0125
@degisim: ayakkabı -> çalı
Ormanda büyük ağaçların arasında dar bir yol vardı. Keloğlan ile zeki eşeği Karakaçan bu yoldan yürüyordu. Birden Karakaçan'ın sırtındaki sepetin ipi dikenli bir çalıya takıldı. Karakaçan ileri gidemedi. Keloğlan ona dürüst davrandı. "Bu biraz uzun sürecek ama seni kurtaracağım, Karakaçan," dedi Keloğlan. İp çok karışmıştı. Ama Keloğlan işini bırakmadı ve ipi dallardan yavaş yavaş çözdü. Sonunda ip çalıdan kurtuldu. Karakaçan sevinçle küçük bir kütüğün üstünden atladı. Sonra başını salladı ve Keloğlan'a sokuldu. Keloğlan bundan sonra dar yollarda sepetin ipine dikkat etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan ona dürüst davrandı"
   - Cümle 5: «Keloğlan ona dürüst davrandı.»
   - Açıklama: İpi çözme durumunda 'dürüst davranmak' anlama uymuyor.
   - Açıklama: 'Dürüst davranmak' bu olaya uymuyor; kelime yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan ona dürüst davrandı"
   - Cümle 5: «Keloğlan ona dürüst davrandı.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunu çözmede hiçbir işe yaramıyor, yalnız adı anılıyor.
   - Açıklama: Tohum özelliğindeki dürüstlük eşeğe karşı işe yaramaz, süs olarak ekleniyor; kartın özellikler alanındaki kullanımla örtüşmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0125` birebir aynı, `@degisim: ayakkabı -> çalı` (tutuyorsan), ardından `@onarim: ed3a072eb7f20bc2699e3aa9030a3473fff05202`, sonra gövde.

### Hikâye 4: tohum keloglan-0126 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0126
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'bambu', fiil 'silmek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kütük tozluydu ve halkalar iyi görünmüyordu | şişeyi düşürdü, su kütüğü ıslattı ve toz gitti
@tohum: keloglan-0126
@degisim: bambu -> kütük
Keloğlan ile anası ormanda kesilmiş büyük bir kütüğün yanına geldi. Keloğlan kütüğün üstünde ince halkalar fark etti. Halkaları saymak istedi ama kütük tozluydu ve halkalar iyi görünmüyordu. Keloğlan su içmek için şişesini açtı. Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü. Su bütün tozu ıslattı. Anası yepyeni bir mendil çıkardı ve ıslak kütüğü sildi. Toz gitti ve halkalar çok açık göründü. Keloğlan halkaları tek tek saydı ve tam yirmi halka buldu. Sonra ikisi ormanda başka kütükler aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (8):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şişeyi düşürdü, su kütüğü ıslattı ve toz gitti"
   - Cümle 0 (plan satırı): «kütük tozluydu ve halkalar iyi görünmüyordu | şişeyi düşürdü, su kütüğü ıslattı ve toz gitti»
   - Açıklama: Gövdede tozu suyun kendisi değil, ananın mendille silmesi gideriyor.
   - Açıklama: Planda toz sudan gidiyor ama gövdede anası kütüğü mendille siliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sakar bir hareketle şişeyi"
   - Cümle 5: «Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü.»
   - Açıklama: 'Sakar' kişiyi niteler, harekete uygun değil ve çocuk için zor bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sakar bir hareketle şişeyi"
   - Cümle 5: «Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü.»
   - Açıklama: 'Sakar bir hareketle' soyut bir anlatım; 3 yaşındaki çocuk 'sakar' kelimesini bilmeyebilir.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakar bir hareketle şişeyi kütüğün üstüne düşürdü"
   - Cümle 5: «Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü.»
   - Açıklama: Çözüm bilinçli bir eylem değil, bir kaza.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü"
   - Cümle 5: «Ama sakar bir hareketle şişeyi kütüğün üstüne düşürdü.»
   - Açıklama: Çözüm figürün bir kararı değil, sebepsiz bir kazayla geliyor.
6. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Anası yepyeni bir mendil çıkardı ve ıslak kütüğü sildi"
   - Cümle 7: «Anası yepyeni bir mendil çıkardı ve ıslak kütüğü sildi.»
   - Açıklama: Sorunu Keloğlan değil anası çözüyor.
   - Açıklama: Tozu Keloğlan değil anası silerek gideriyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Anası yepyeni bir mendil çıkardı"
   - Cümle 7: «Anası yepyeni bir mendil çıkardı ve ıslak kütüğü sildi.»
   - Açıklama: Mendil sebepsiz beliriyor ve çözümü getiriyor.
8. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "halkalar çok açık göründü"
   - Cümle 8: «Toz gitti ve halkalar çok açık göründü.»
   - Açıklama: 'Açık' burada 'net' anlamında yanlış kullanılmış, renk olarak da okunabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0126` birebir aynı, `@degisim: bambu -> kütük` (tutuyorsan), ardından `@onarim: 4dc5782f35a7ed97fcf658f6a26b358af036d649`, sonra gövde.

### Hikâye 5: tohum keloglan-0127 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0127
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'cetvel', fiil 'katmak', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ağaçların arasından garip bir tık tık sesi geldi | ağaçları dolaşıp ağaca çarpan kuru dalı buldu
@tohum: keloglan-0127
@degisim: yaratıcı -> kuru
Rüzgar ormanda hafif esiyordu. Keloğlan dalları cetvelle ölçüyor ve küçük bir ev yapıyordu. Birden ağaçların arasından garip bir "tık tık" sesi geldi. Keloğlan bu sesi çok merak etti ve aramaya başladı. Önce büyük ağaçların arkasına baktı ama bir şey bulamadı. Keloğlan dürüst bir çocuktu ve işini bırakmadı. Ağaçları birer birer dolaştı. Sonunda yarı kopmuş kuru bir dal buldu. Dal rüzgarda sallanıyor ve ağaca çarpıyordu. Keloğlan dalı yavaşça kopardı. Dal tam istediği boydaydı. Keloğlan onu da küçük evin duvarına kattı. Keloğlan çok sevindi, çünkü hem sesi bulmuştu hem de küçük ev bitmişti.
```

**Hakem bulguları (7):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Keloğlan dalları cetvelle ölçüyor"
   - Cümle 2: «Keloğlan dalları cetvelle ölçüyor ve küçük bir ev yapıyordu.»
   - Açıklama: Cetvel kartın masal köyü dünyasında olmayan çağdaş bir eşya; tohum_yasak_kategoriler alanına aykırı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip bir "tık tık" sesi geldi"
   - Cümle 3: «Birden ağaçların arasından garip bir "tık tık" sesi geldi.»
   - Açıklama: Merak edilen bir ses çocuğun önemseyeceği gerçek bir sorun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Aramayı bırakmamak dürüstlükle ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Aramayı bırakmamak dürüstlükle ilgili değil; kelime yanlış anlamda.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız söylenmiş, olayda dürüstlükle ilgili işe yarar bir kullanım yok.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Dürüstlük olayla hiç ilgisi olmayan işlevsiz bir ayrıntı olarak araya giriyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Keloğlan ev yapmayı bırakıp sesi aramaya gitmişken işini bırakmadığı söyleniyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dal tam istediği boydaydı"
   - Cümle 11: «Dal tam istediği boydaydı.»
   - Açıklama: Dalın tam ev için istenen boyda çıkması çözüme sebepsiz bir rastlantı ekliyor, cetvel de hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0127` birebir aynı, `@degisim: yaratıcı -> kuru` (tutuyorsan), ardından `@onarim: bb61950bd230dbb830f3416cf02eba9f4a543729`, sonra gövde.

### Hikâye 6: tohum keloglan-0128 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0128
- yer: dağ (Köyün yakınındaki tepe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fındık', fiil 'sıkışmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ahşap kutunun kapağı ıslanmış ve sıkışmıştı | kutuyu düşürdü ve kapak açıldı
@tohum: keloglan-0128
Tepede hava serin ve sessizdi. Keloğlan orada oturmuş güneşin doğmasını bekliyordu. Yanındaki ahşap kutu ıslanmıştı ve kapağı sıkışmıştı. Kutunun içinde Keloğlan'ın fındıkları vardı. Keloğlan kapağı çekti ama açamadı. Sonra kutuyu dizlerinin üstüne koymak istedi. Ama sakar bir hareketle kutuyu elinden düşürdü. Kutu bir taşa çarptı ve kapağı açıldı. Birkaç fındık otların üstüne döküldü. Keloğlan güldü ve fındıkları tek tek topladı. Tam o sırada güneş tepenin arkasından doğdu. Keloğlan fındıklarını yiyerek güneşi mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sakar bir hareketle kutuyu elinden düşürdü"
   - Cümle 7: «Ama sakar bir hareketle kutuyu elinden düşürdü.»
   - Açıklama: Kapak figürün çabasıyla değil tesadüfen düşürülünce açılıyor.
   - Açıklama: Kapak figürün bir çözümüyle değil kazayla açılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kutu bir taşa çarptı ve kapağı açıldı"
   - Cümle 8: «Kutu bir taşa çarptı ve kapağı açıldı.»
   - Açıklama: Çözüm ıslanıp sıkışan kapağa bilinçli yönelmiyor, kazayla geliyor.
   - Açıklama: Çözüm sıkışmanın sebebine yönelmiyor, tesadüfle geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0128` birebir aynı, ardından `@onarim: 4ba676fbc502b7c1aa68e7030d9d73f8052b2a0b`, sonra gövde.

### Hikâye 7: tohum keloglan-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0129
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kolye', fiil 'içmek', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin kolyesini otların arasına düşürdü | özür diledi, otlara baktı ve kolyeyi buldu
@tohum: keloglan-0129
@degisim: içmek -> aramak
Rüzgar ormanda hafif hafif esiyordu. Bilgecan Dede, Keloğlan'a yeni icadını gösterdi: küçük bir düdüğü olan kolye. Keloğlan kolyeyi aldı ama sakar bir hareketle onu kokulu otların arasına düşürdü. Otlar çok sıktı ve kolye hiç görünmüyordu. "Özür dilerim, Dede, icadını düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan, onu bulabiliriz," dedi Dede. Keloğlan eğildi ve otları yavaşça aradı. Sonunda otların arasında küçük düdüğü gördü. Onu dikkatle aldı ve iki eliyle Dede'ye verdi. Dede düdüğü çaldı ve ormanda ince bir ses çıktı. "Seni affettim, Keloğlan, hem de icadımı buldun!" dedi Bilgecan Dede.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan'a yeni icadını gösterdi"
   - Cümle 2: «Bilgecan Dede, Keloğlan'a yeni icadını gösterdi: küçük bir düdüğü olan kolye.»
   - Açıklama: 'İcat' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama sakar bir hareketle"
   - Cümle 3: «Keloğlan kolyeyi aldı ama sakar bir hareketle onu kokulu otların arasına düşürdü.»
   - Açıklama: 'Sakar bir hareketle' 3 yaşındaki çocuğun bilmeyeceği bir ifade.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sakar bir hareketle onu"
   - Cümle 3: «Keloğlan kolyeyi aldı ama sakar bir hareketle onu kokulu otların arasına düşürdü.»
   - Açıklama: 'Sakar' ve 'hareketle' 3 yaşındaki çocuğun bilmeyeceği soyut bir anlatım.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hem de icadımı buldun"
   - Cümle 11: «"Seni affettim, Keloğlan, hem de icadımı buldun!" dedi Bilgecan Dede.»
   - Açıklama: 'hem de' bağlacı affetmekle bulmayı anlamca uygunsuz bağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0129` birebir aynı, `@degisim: içmek -> aramak` (tutuyorsan), ardından `@onarim: 161c1e2c522c9803d24ed6a532821ce4ad5b081d`, sonra gövde.

### Hikâye 8: tohum keloglan-0131 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0131
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'avokado', fiil 'göndermek', sıfat 'minicik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: topu çok hızlı attı ve arkadaşı tutamadı | özür diledi ve topu yavaş atmayı öğrendi
@tohum: keloglan-0131
@degisim: avokado -> top
Bir sabah Keloğlan ile Balkız tepede top oynuyordu. Balkız minicik kırmızı bir top getirmişti. Keloğlan topu Balkız'a çok hızlı gönderiyordu ve Balkız hiç tutamıyordu. Top hep çimenlere yuvarlanıyordu. Balkız topu getirmekten yoruldu ve oturdu. "Özür dilerim, Balkız, topu çok hızlı attım," dedi Keloğlan. "Yavaş ve aşağıdan at, o zaman tutarım," dedi Balkız. Keloğlan bunu öğrenmek için birkaç kez denedi. Sonra topu yavaşça ve aşağıdan attı. Balkız bu kez topu hemen yakaladı. "Yakaladım, Keloğlan, şimdi oyun çok eğlenceli!" dedi Balkız.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Yavaş ve aşağıdan at, o zaman tutarım"
   - Cümle 7: «"Yavaş ve aşağıdan at, o zaman tutarım," dedi Balkız.»
   - Açıklama: Çözümün fikrini yan karakter Balkız veriyor; Keloğlan yalnız uyguluyor.
   - Açıklama: Çözüm yolunu Keloğlan değil Balkız buluyor ve söylüyor; Keloğlan yalnız uyguluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0131` birebir aynı, `@degisim: avokado -> top` (tutuyorsan), ardından `@onarim: fe84c174ad13f496cc1abfdce7d9cdf33b21d968`, sonra gövde.

### Hikâye 9: tohum keloglan-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0133
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tartı', fiil 'gülmek', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yeni tartı taşların üstünde sallanıyordu | tartıyı düz bir yere koydu
@tohum: keloglan-0133
Rüzgar büyük ağaçların arasında hafifçe esiyordu. Keloğlan ormanda Bilgecan Dede'nin yeni icadı olan tartıyı gördü. Ama tartı taşların üstünde oynak duruyor ve hep sallanıyordu. Dede cevizleri köyün çocukları için iki torbaya eşit koymak istiyordu. "Dede, bu tartı neden sallanıyor?" diye sordu Keloğlan. "Tartı yalnız düz bir yerde iyi çalışır," dedi Bilgecan Dede. Keloğlan bunu hemen öğrendi ve etrafına baktı. Tartıyı taşlardan aldı ve düz bir yere koydu. Tartı artık hiç sallanmadı. Dede cevizleri tarttı ve iki torba tam eşit oldu. Keloğlan ile Dede birlikte güldü ve torbaları mutlu mutlu bağladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni icadı olan tartıyı"
   - Cümle 2: «Keloğlan ormanda Bilgecan Dede'nin yeni icadı olan tartıyı gördü.»
   - Açıklama: 'İcat' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'İcat' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0133` birebir aynı, ardından `@onarim: b8d1178fa2576c8773170281d8f6fac89f6b1cf1`, sonra gövde.

### Hikâye 10: tohum keloglan-0134 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0134
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fidan', fiil 'görüşmek', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar deliğin önündeki fidana çarpıyordu | yüksekten atmayı öğrendi ve kozalağı deliğe attı
@tohum: keloglan-0134
@degisim: görüşmek -> fırlatmak
Keloğlan ormanda komik bir kozalak oyunu oynuyordu. Kozalakları büyük bir ağacın dibindeki deliğe atmaya çalışıyordu. Ama deliğin önünde küçük bir fidan vardı ve kozalaklar hep ona çarpıyordu. Keloğlan fidanın dallarını kırmak istemedi. Yeni bir yol öğrenmek için durup düşündü. Bu kez kozalağı yukarı doğru, yüksekten fırlattı. Kozalak fidanın üstünden geçti ama delikten uzağa düştü. Keloğlan birkaç kez daha denedi. Sonunda kozalak tam deliğin içine girdi! Keloğlan yüksekten atmayı böylece öğrenmişti. Sevinçle güldü ve oyunun sonunda kibarca eğildi. Sonra Keloğlan oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yeni bir yol öğrenmek"
   - Cümle 5: «Yeni bir yol öğrenmek için durup düşündü.»
   - Açıklama: 'Yol' yöntem anlamında mecazlı ve soyut kullanılmış.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan birkaç kez daha denedi"
   - Cümle 8: «Keloğlan birkaç kez daha denedi.»
   - Açıklama: Çözüm iki adımda bitmiyor, belirsiz sayıda denemeye yayılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yüksekten atmayı böylece öğrenmişti"
   - Cümle 10: «Keloğlan yüksekten atmayı böylece öğrenmişti.»
   - Açıklama: Tohumdaki öğrenme özelliği bir kez yerine iki kez (5. ve 10. cümle) vurgulanıyor, karttaki 'ozellikler' kullanımına aykırı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "oyunun sonunda kibarca eğildi"
   - Cümle 11: «Sevinçle güldü ve oyunun sonunda kibarca eğildi.»
   - Açıklama: Seyirci yokken kibarca eğilmek işlevsiz bir ayrıntı.
   - Açıklama: Keloğlan yalnızken kime eğildiği belli değil; eğilme olayla bağsız, işlevsiz bir ayrıntı.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra Keloğlan oyununa mutlu mutlu devam etti"
   - Cümle 12: «Sonra Keloğlan oyununa mutlu mutlu devam etti.»
   - Açıklama: Oyunun sonu denmişken Keloğlan oyuna devam ediyor.
   - Açıklama: Önceki cümlede oyun sona ermişken hemen ardından oyuna devam ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0134` birebir aynı, `@degisim: görüşmek -> fırlatmak` (tutuyorsan), ardından `@onarim: b456784a3d123e5c013085ff7461174a8cd7643f`, sonra gövde.

### Hikâye 11: tohum keloglan-0135 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0135
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kabak', fiil 'ışıldamak', sıfat 'yalnız'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: sürpriz için yıkanacak kabak çok ağırdı | kabağı yerde iterek kovaya götürdü
@tohum: keloglan-0135
Bir sabah Keloğlan anasına bir sürpriz hazırlamak istedi. Anası dışarıdaydı ve biraz sonra kabak tatlısı yapacaktı. Keloğlan büyük kabağı yıkamak istedi, yalnız kabak çok ağırdı. Onu kucağına alıp su dolu kovanın yanına taşıyamadı. Keloğlan yeni bir yol denemek istedi. Kabağı yan yatırdı ve eliyle hafifçe itti. Kabak top gibi kolayca yuvarlandı. Keloğlan böylece ağır bir şeyi kaldırmadan götürmeyi öğrendi. Kabağı böyle kovanın yanına kadar getirdi ve bezle yıkadı. Temiz kabak pencerenin önünde ışıldadı. Az sonra anası içeri girdi ve kabağı gördü. Anası çok sevindi, çünkü Keloğlan kabağı onun için hazırlamıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yalnız kabak çok ağırdı"
   - Cümle 3: «Keloğlan büyük kabağı yıkamak istedi, yalnız kabak çok ağırdı.»
   - Açıklama: 'Yalnız' burada 'ama' anlamında bağlaç; küçük çocuk bunu 'tek başına' diye anlar.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir yol denemek istedi"
   - Cümle 5: «Keloğlan yeni bir yol denemek istedi.»
   - Açıklama: 'Yeni bir yol denemek' mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan yeni bir yol denemek istedi"
   - Cümle 5: «Keloğlan yeni bir yol denemek istedi.»
   - Açıklama: 'Yol denemek' yöntem anlamında mecazdır; 3 yaşındaki çocuk anlamaz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Temiz kabak pencerenin önünde ışıldadı"
   - Cümle 10: «Temiz kabak pencerenin önünde ışıldadı.»
   - Açıklama: Kaldırılamayan ağır kabağın kovanın yanından pencerenin önüne nasıl geldiği söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0135` birebir aynı, ardından `@onarim: 186acb482111c80fdeed2bcf7f8bb21894f9b053`, sonra gövde.

### Hikâye 12: tohum keloglan-0136 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0136
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'beşik', fiil 'sormak', sıfat 'lezzetli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: sürpriz elmaların sepetinin kapağı sıkışmıştı | sepeti elinden düşürdü ve kapak açıldı
@tohum: keloglan-0136
@degisim: beşik -> sepet
Tepede serin bir rüzgar esiyordu. Keloğlan, eşeği Karakaçan'a bir sürpriz hazırlamıştı. Sepette lezzetli elmalar vardı, ama sepetin kapağı sıkışmıştı ve açılmıyordu. Keloğlan kapağı çekti ama kapak kıpırdamadı. "Karakaçan, sürprizini görmek ister misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan sepeti yerden kaldırdı. Ama sakarlık yaptı ve sepeti elinden düşürdü. Sepet yere çarpınca kapak birden açıldı! Kırmızı elmalar çimenlere yuvarlandı. Karakaçan hemen bir elma yedi ve kulaklarını salladı. Keloğlan güldü ve eşeğinin başını okşadı. "Afiyet olsun, Karakaçan, bu elmalar senin için!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sepetin kapağı sıkışmıştı ve açılmıyordu"
   - Cümle 3: «Sepette lezzetli elmalar vardı, ama sepetin kapağı sıkışmıştı ve açılmıyordu.»
   - Açıklama: Kapağın neden sıkıştığı hiç söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama sakarlık yaptı"
   - Cümle 8: «Ama sakarlık yaptı ve sepeti elinden düşürdü.»
   - Açıklama: 'Sakarlık' 3 yaşındaki çocuk için soyut bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yaptı ve sepeti elinden düşürdü"
   - Cümle 8: «Ama sakarlık yaptı ve sepeti elinden düşürdü.»
   - Açıklama: Kapak figürün sebebe yönelik bir çabasıyla değil, sakarlıkla kazara açılıyor.
   - Açıklama: Çözüm bilinçli bir eylem değil, sıkışan kapağa yönelmeyen bir kaza.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepet yere çarpınca kapak birden açıldı"
   - Cümle 9: «Sepet yere çarpınca kapak birden açıldı!»
   - Açıklama: Çözüm önceki olaydan değil, sebepsiz bir tesadüften geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0136` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: 8bdf15fdc813d986636cdc36d6a69bd0c03b1435`, sonra gövde.
