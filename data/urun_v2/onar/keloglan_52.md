# Editör görevi (onarım): Keloğlan, onarım partisi 52

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar52.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar52.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0183 (deneme 3 -> 4)

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
@plan: top dedenin kutusunu devirdi ve mücevherler döküldü | özür diledi ve mücevherleri tek tek topladı
@tohum: keloglan-0183
@degisim: huzurlu -> mutlu
Bir sabah Keloğlan ormanda top oynuyordu. Bilgecan Dede yakında oturuyordu ve kutusundaki parlak mücevherlere bakıyordu. Ama Keloğlan topa çok sert vurdu ve top dedenin kutusunu devirdi. Mücevherler yerdeki yaprakların arasına döküldü. Keloğlan bir an hiç kıpırdamadı. Sonra dürüst davrandı ve dedenin yanına gitti. "Özür dilerim, Bilgecan Dede, topa ben vurdum," dedi Keloğlan. "Doğruyu söyledin, teşekkürler, Keloğlan," dedi Bilgecan Dede. Keloğlan yaprakların arasından mücevherleri tek tek topladı. Hepsini yeniden kutuya koydu. Bilgecan Dede gülümsedi ve çok mutlu oldu, çünkü hiçbiri eksik değildi. Keloğlan bundan sonra topla dedenin kutusundan uzakta oynadı.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kutusundaki parlak mücevherlere bakıyordu"
   - Cümle 2: «Bilgecan Dede yakında oturuyordu ve kutusundaki parlak mücevherlere bakıyordu.»
   - Açıklama: Kartta Bilgecan Dede'nin ilişki alanı kitap ve icat anlatır; mücevher kutusu kartta olmayan bir eşya olarak ekleniyor.
   - Açıklama: Kartın yanlar bölümünde Bilgecan Dede kitap ve icatlarla anılır; mücevher kutusu kartta olmayan bir eşya.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0183` birebir aynı, `@degisim: huzurlu -> mutlu` (tutuyorsan), ardından `@onarim: 1da25860f6ce5aa97454ca9ff40e9a8d25413e39`, sonra gövde.

### Hikâye 2: tohum keloglan-0186 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0186
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'etek', fiil 'özlemek', sıfat 'devasa'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: çocuğun boyu yüksek kapının üstüne yetmedi | çiçekleri kapının iki yanına alçak yerlere dizdi
@tohum: keloglan-0186
@degisim: etek -> çiçek
Şatonun bahçesinde devasa bir taş kapı vardı. Keloğlan, Bilgecan Dede için kapıyı çiçeklerle süslemek istedi. Ama kapı çok yüksekti ve Keloğlan'ın boyu kapının üstüne yetmedi. Keloğlan, Dede'yi çok özlemişti ve Dede biraz sonra buraya gelecekti. Keloğlan çiçek sepetini kucakladı ve kapıya doğru yürüdü. Sakar Keloğlan acele etti ve sepeti elinden düşürdü. Çiçekler kapının önüne döküldü. Keloğlan çiçekleri tek tek topladı. Sonra onları kapının iki yanına, alçak yerlere dizdi. Biraz sonra Bilgecan Dede kapıdan içeri girdi. Süslü kapıyı görünce "Ne güzel bir sürpriz, Keloğlan!" dedi Dede. Keloğlan çok sevindi, çünkü Dede çiçekli kapıyı çok sevmişti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bahçesinde devasa bir taş"
   - Cümle 1: «Şatonun bahçesinde devasa bir taş kapı vardı.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "devasa bir taş kapı"
   - Cümle 1: «Şatonun bahçesinde devasa bir taş kapı vardı.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sakar Keloğlan acele etti ve sepeti elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan acele etti ve sepeti elinden düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği plandaki sorunla (kapının yüksekliği) ilgisiz bir ara olay olarak ekleniyor, çözüme işe yarar biçimde bağlanmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan acele etti ve sepeti elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan acele etti ve sepeti elinden düşürdü.»
   - Açıklama: Sepetin düşmesi çözüme bir şey katmıyor; çiçekler yalnız yeniden toplanıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepeti elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan acele etti ve sepeti elinden düşürdü.»
   - Açıklama: Sepetin düşmesi olaya bir şey katmıyor, işlevsiz bir ara olay.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra onları kapının iki yanına, alçak yerlere dizdi"
   - Cümle 9: «Sonra onları kapının iki yanına, alçak yerlere dizdi.»
   - Açıklama: Çözüm boy yetmeme sebebine yönelmiyor, kapının üstünü süsleme hedefinden vazgeçip sorunu atlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0186` birebir aynı, `@degisim: etek -> çiçek` (tutuyorsan), ardından `@onarim: 3e419a3b593b29c2cd01997c4c90505654df754c`, sonra gövde.

### Hikâye 3: tohum keloglan-0187 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0187
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'sünger', fiil 'gelmek', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: sünger çok hafifti ve kovaya girmedi | süngeri suyla ıslatıp ağır yaptı
@tohum: keloglan-0187
@degisim: esnek -> yumuşak
Keloğlan evin önünde süngerle bir atma oyunu oynuyordu. Kovayı duvarın dibine koymuştu ve süngeri içine atıyordu. Ama sünger çok hafifti ve hep kovanın yanına düşüyordu. Karakaçan her seferinde gelip süngeri ağzıyla getiriyordu. Keloğlan dürüst davrandı ve "Bu atış olmadı, yine deneyeceğim," dedi. Kapının önünde su dolu bir tas vardı. Keloğlan yumuşak süngeri suya batırdı ve iyice ıslattı. Islak sünger şimdi daha ağırdı. Keloğlan süngeri attı ve sünger bu kez kovanın içine düştü! Karakaçan başını salladı. "Oldu, Karakaçan, sen de bana çok iyi yardım ettin!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı ve"
   - Cümle 5: «Keloğlan dürüst davrandı ve "Bu atış olmadı, yine deneyeceğim," dedi.»
   - Açıklama: Kartın özellik alanındaki dürüstlük süs olarak söyleniyor; sorunu çözmede işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kapının önünde su dolu bir tas vardı"
   - Cümle 6: «Kapının önünde su dolu bir tas vardı.»
   - Açıklama: Çözümü sağlayan su tası tam gerektiği anda sebepsizce beliriyor.
   - Açıklama: Su dolu tas daha önce kurulmadan tam çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0187` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: 852a39176a449b9b847329f9783c94c6e66bad70`, sonra gövde.

### Hikâye 4: tohum keloglan-0188 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0188
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'börek', fiil 'affetmek', sıfat 'garip'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: ikisi tek uçurtmanın ipini aynı anda çekti | sırayla uçurmayı söyledi ve sırası gelince ipi sıkı tuttu
@tohum: keloglan-0188
@degisim: affetmek -> seçmek
Tepede rüzgar esiyordu ve Keloğlan ile anası uçurtma uçurmak istiyordu. Ama tek bir uçurtma vardı ve ikisi de ipi aynı anda çekti. Uçurtma garip bir şekilde döndü ve yere düştü. "Anne, sırayla uçuralım, önce sen uçur," dedi Keloğlan. Anası ipi tuttu ve uçurtma yükseldi. Keloğlan beklerken sepetten bir börek seçti ve yedi. Sonra anası ipi Keloğlan'a verdi. Keloğlan biraz sakardı ve ipi düşürmemek için iki eliyle sıkıca tuttu. Uçurtma bu kez hiç dönmeden yükseldi. Anası sevinçle alkışladı. "Sırayla oynamak çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan beklerken sepetten bir börek seçti ve yedi"
   - Cümle 6: «Keloğlan beklerken sepetten bir börek seçti ve yedi.»
   - Açıklama: Börek yeme olayı hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepetten bir börek seçti ve yedi"
   - Cümle 6: «Keloğlan beklerken sepetten bir börek seçti ve yedi.»
   - Açıklama: Sepet ve börek sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve ipi düşürmemek için"
   - Cümle 8: «Keloğlan biraz sakardı ve ipi düşürmemek için iki eliyle sıkıca tuttu.»
   - Açıklama: Sakarlık kartın güvenli kullanım satırındaki gibi bir şeyi düşürmek olarak gösterilmiyor, yalnız adı anılıyor ve çözüme katkısı yok.
   - Açıklama: Tohumdaki sakarlık özelliği karttaki gibi bir şeyi düşürme ya da karıştırma olarak gösterilmiyor ve olayda işe yaramıyor, yalnız adı anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0188` birebir aynı, `@degisim: affetmek -> seçmek` (tutuyorsan), ardından `@onarim: d0584af1e8aec7fa53cb51299a2879d373f68713`, sonra gövde.

### Hikâye 5: tohum keloglan-0189 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0189
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'meşe', fiil 'kirletmek', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: çamur küçük meşe ağacının yapraklarını kirletti | testiyle yapraklara su döktü ve çamuru yıkadı
@tohum: keloglan-0189
Bir sabah Keloğlan ormanda yürüyordu. Hafif bir rüzgar büyük ağaçların yapraklarını sallıyordu. Ama küçük bir meşe ağacının yaprakları çamurdan ağırdı ve hareketsizdi. Keloğlan eğilip ona baktı. Yağmurdan kalan çamur yaprakları kirletmişti. Keloğlan ağacı temizlemek istedi. Elinde içmek için bir testi su vardı. Keloğlan biraz sakardı ve testiyi düşürmemek için iki eliyle tuttu. Suyu yapraklara yavaşça döktü. Su çamuru yıkadı. Temiz yapraklar rüzgarda yeniden sallandı. Keloğlan çok sevindi, çünkü küçük meşe yine tertemizdi.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yaprakları çamurdan ağırdı"
   - Cümle 3: «Ama küçük bir meşe ağacının yaprakları çamurdan ağırdı ve hareketsizdi.»
   - Açıklama: 'Çamurdan ağırdı' kuruluşu kusurlu; 'çamurla ağırlaşmıştı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yağmurdan kalan çamur yaprakları kirletmişti"
   - Cümle 5: «Yağmurdan kalan çamur yaprakları kirletmişti.»
   - Açıklama: Yağmurun çamuru ağacın yapraklarına nasıl taşıdığı akla yatkın değil ve sorun çocuk için zayıf.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elinde içmek için bir testi su vardı"
   - Cümle 7: «Elinde içmek için bir testi su vardı.»
   - Açıklama: Testi tam çözüm gerektiğinde önceden kurulmadan beliriyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve testiyi düşürmemek için iki eliyle tuttu"
   - Cümle 8: «Keloğlan biraz sakardı ve testiyi düşürmemek için iki eliyle tuttu.»
   - Açıklama: Tohumdaki sakarlık özelliği yalnız anılıyor, hiçbir şey düşürülmediği için çözüme işe yarar biçimde kullanılmıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve testiyi düşürmemek"
   - Cümle 8: «Keloğlan biraz sakardı ve testiyi düşürmemek için iki eliyle tuttu.»
   - Açıklama: Tohumdaki sakarlık yalnız anılıyor, güvenli özellik kullanımındaki gibi bir şeyi düşürme ya da karıştırma olarak işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0189` birebir aynı, ardından `@onarim: bafad7d207d3462cbb9c1bf43f9e3092a36a3888`, sonra gövde.

### Hikâye 6: tohum keloglan-0192 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0192
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'dilim', fiil 'uyandırmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kuru bir dal küçük çiçeklerin üstüne gölge yaptı | dalı kaldırdı ve güneş çiçeklere ulaştı
@tohum: keloglan-0192
@degisim: dilim -> dal
Bir sabah güneş Keloğlan'ı erkenden uyandırmıştı ve Keloğlan ormana gelmişti. Güneşin altındaki sarı çiçekler açıktı. Ama kuru bir dalın altında saklı küçük çiçekler kapalıydı. Keloğlan onların da açılmasını istedi. İki yere dikkatle baktı. Açık çiçeklerin üstünde güneş vardı, kapalı çiçekler gölgede kalmıştı. Böylece Keloğlan çiçeklerin güneşte açıldığını öğrendi. Kuru dalı kaldırdı ve kenara koydu. Güneş saklı çiçeklere de ulaştı. Biraz sonra küçük çiçekler yavaş yavaş açıldı. Keloğlan çok sevindi, çünkü bütün çiçekler artık açıktı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "güneş Keloğlan'ı erkenden uyandırmıştı"
   - Cümle 1: «Bir sabah güneş Keloğlan'ı erkenden uyandırmıştı ve Keloğlan ormana gelmişti.»
   - Açıklama: Hikaye ormanda değil uyanma anıyla başlıyor; tek sahne ve tek zaman kuralı zorlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0192` birebir aynı, `@degisim: dilim -> dal` (tutuyorsan), ardından `@onarim: 0b860a1515c2c03fca39fbe168179c8e909abbd9`, sonra gövde.

### Hikâye 7: tohum keloglan-0193 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0193
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'erik', fiil 'sıkmak', sıfat 'aydınlık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: bahçeden pat diye bir ses geldi | erikleri sıkıp sesin olgun eriklerden geldiğini buldu
@tohum: keloglan-0193
Şatonun aydınlık bahçesinde Keloğlan yürüyordu. Birden yakından pat diye bir ses geldi. Keloğlan sesin nereden geldiğini merak etti. Biraz sonra aynı ses yine duyuldu. Keloğlan sesin geldiği yere, büyük bir erik ağacının altına gitti. Yerde mor erikler vardı. Keloğlan yerdeki bir eriği hafifçe sıktı ve yumuşak buldu. Sonra dalda asılı bir erik tuttu, o sertti. Keloğlan böylece sesin olgun eriklerden geldiğini öğrendi. Tam o sırada olgun bir erik daha pat diye yere düştü. Keloğlan güldü ve düşen erikleri mutlu mutlu saydı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yakından pat diye bir ses geldi"
   - Cümle 2: «Birden yakından pat diye bir ses geldi.»
   - Açıklama: Gelen bir ses gerçek bir sorun değil; hikayede çözülecek önemli bir dert yok.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan yerdeki bir eriği hafifçe sıktı ve yumuşak buldu"
   - Cümle 7: «Keloğlan yerdeki bir eriği hafifçe sıktı ve yumuşak buldu.»
   - Açıklama: Erikleri sıkmak sesin kaynağını göstermiyor; çözüm sebebe doğrudan yönelmiyor ve sonuç ancak sonradan düşen erikle doğrulanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0193` birebir aynı, ardından `@onarim: 0023c2aca2cdc2cdf14640a20ec92d3edef39f18`, sonra gövde.

### Hikâye 8: tohum keloglan-0194 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0194
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'su', fiil 'selamlamak', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: eşek sürpriz havuçlara bakmadı bile | eşeğini izleyip önce su istediğini anladı
@tohum: keloglan-0194
Keloğlan, eşeği Karakaçan ile şatonun bahçesine geldi. Karakaçan için çıtır havuçlar ve bir kova su getirmişti. Ama Karakaçan sürpriz havuçlara bakmadı bile. Keloğlan bunun nedenini öğrenmek istedi. Karakaçan'ı iyi izledi. Karakaçan başını kovaya uzattı. "Önce su mu istiyorsun, Karakaçan?" diye sordu Keloğlan. Karakaçan başını salladı. Keloğlan kovayı onun önüne koydu. Karakaçan suyun hepsini içti. Sonra havuçları da yedi. Karakaçan, Keloğlan'ın yanına geldi ve onu selamladı. Keloğlan çok sevindi, çünkü eşeği sürprizini sevmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geldi ve onu selamladı"
   - Cümle 12: «Karakaçan, Keloğlan'ın yanına geldi ve onu selamladı.»
   - Açıklama: Eşek selamlamaz; fiil öznesine uymuyor.
   - Açıklama: Eşek selamlamaz; fiil öznesine uygun değil.
2. **K5** (K merceği) — Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
   - Alıntı: "yanına geldi ve onu selamladı"
   - Cümle 12: «Karakaçan, Keloğlan'ın yanına geldi ve onu selamladı.»
   - Açıklama: Kartta konusur false olan Karakaçan'ın 'selamladı' ile sözlü selam vermesi konuşma olarak okunabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0194` birebir aynı, ardından `@onarim: 94c63f5fbc4d81e981391d0192808a4a7105d15a`, sonra gövde.

### Hikâye 9: tohum keloglan-0195 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0195
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'halat', fiil 'büyümek', sıfat 'sevecen'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: ağaç büyüdü ve halat ona yetmedi | doğruyu söyledi ve iki halatı bağladı
@tohum: keloglan-0195
Tepede serin bir rüzgar esiyordu. Keloğlan ile Bilgecan Dede, ağacı süslemek için kırmızı bir halat getirdi. Ama ağaç çok büyümüştü ve halat ona yetmedi. Bilgecan Dede ağacın öbür yanındaydı ve halatı göremiyordu. "Halat yetti mi, Keloğlan?" diye sordu Bilgecan Dede. Keloğlan dürüst davrandı. "Hayır, dede, halat kısa kaldı," dedi Keloğlan. Bilgecan Dede sevecen bir sesle güldü ve çantasından kısa bir halat verdi. Keloğlan iki halatı sıkıca birbirine bağladı. Şimdi kırmızı halat ağaca tam yetti. Bilgecan Dede ile Keloğlan ağacın yanında el ele döndü. Keloğlan çok mutluydu, çünkü ağaçları için güzel bir kutlama yapmışlardı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ağaç çok büyümüştü"
   - Cümle 3: «Ama ağaç çok büyümüştü ve halat ona yetmedi.»
   - Açıklama: Halatın yetmemesinin sebebi olarak ağacın birden büyümesi akla yatkın değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bilgecan Dede sevecen bir sesle"
   - Cümle 8: «Bilgecan Dede sevecen bir sesle güldü ve çantasından kısa bir halat verdi.»
   - Açıklama: 'Sevecen' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağaçları için güzel bir kutlama"
   - Cümle 12: «Keloğlan çok mutluydu, çünkü ağaçları için güzel bir kutlama yapmışlardı.»
   - Açıklama: Hikayede tek ağaç var ve kutlamadan söz edilmedi; 'ağaçları' ve 'kutlama' yanlış kelimeler.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ağaçları için güzel bir kutlama yapmışlardı"
   - Cümle 12: «Keloğlan çok mutluydu, çünkü ağaçları için güzel bir kutlama yapmışlardı.»
   - Açıklama: Kutlama hikayede hiç kurulmadan son cümlede sebepsiz beliriyor; amaç yalnız ağacı süslemekti.
   - Açıklama: Kutlama hikayede hiç kurulmadan sonda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0195` birebir aynı, ardından `@onarim: 3806615959e15a97e559d236212192f01dd492c8`, sonra gövde.

### Hikâye 10: tohum keloglan-0196 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0196
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'zeytin', fiil 'düzeltmek', sıfat 'sağlam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: odun yığını tek başına taşımak için çok ağırdı | ıslık çalıp eşeğinden yardım istedi
@tohum: keloglan-0196
@degisim: zeytin -> odun
Rüzgar ormanın büyük ağaçları arasında esiyordu. Keloğlan eve götürmek için kuru ve sağlam odunlar toplamıştı. Ama odun yığını çok ağırdı. Keloğlan odunları kucağına aldı ve yürüdü. Ama birkaç adım sonra kolları yoruldu ve odunlar yere düştü. Parmaklarını ağzına koyup uzun bir ıslık çaldı. Karakaçan ağaçların arasından koşarak geldi. "Bana yardım eder misin, Karakaçan?" diye sordu Keloğlan. Karakaçan başını salladı. Keloğlan odunları eşeğin sırtına yükledi. Keloğlan biraz sakardı, bu yüzden odunlar düşmesin diye yükü dikkatle düzeltti. Karakaçan odunları kolayca taşıdı. Keloğlan bundan sonra ağır yükler için hep Karakaçan'dan yardım istedi.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Keloğlan odunları eşeğin sırtına"
   - Cümle 10: «Keloğlan odunları eşeğin sırtına yükledi.»
   - Açıklama: Karakaçan'ın eşek olduğu hiç söylenmediği için 'eşeğin' kimi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "odunları eşeğin sırtına yükledi"
   - Cümle 10: «Keloğlan odunları eşeğin sırtına yükledi.»
   - Açıklama: Karakaçan'ın eşek olduğu önceden söylenmediği için 'eşeğin' kimi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden odunlar düşmesin diye yükü dikkatle düzeltti"
   - Cümle 11: «Keloğlan biraz sakardı, bu yüzden odunlar düşmesin diye yükü dikkatle düzeltti.»
   - Açıklama: Kartın özellikler ve güvenli kullanım alanına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada yalnız söylenip tersine dikkatli davranışla işlevsiz kalıyor.
   - Açıklama: Tohumdaki sakarlık kartın güvenli kullanımındaki gibi bir şeyi düşürmek olarak gösterilmiyor, yalnız söyleniyor ve çözüme katkısı yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden odunlar düşmesin diye yükü dikkatle düzeltti"
   - Cümle 11: «Keloğlan biraz sakardı, bu yüzden odunlar düşmesin diye yükü dikkatle düzeltti.»
   - Açıklama: Sakarlık özelliği olaya bağlanmadan ekleniyor ve sakar olduğu için dikkatle düzeltmesi sebep-sonuç olarak tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0196` birebir aynı, `@degisim: zeytin -> odun` (tutuyorsan), ardından `@onarim: b8ba72798f06f66a57aa8784ec1d21825c029ea6`, sonra gövde.

### Hikâye 11: tohum keloglan-0197 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0197
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'buğday', fiil 'sıkılmak', sıfat 'biberli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: yağmur yüzünden dışarı çıkamadılar ve sıkıldılar | gökkuşağını görüp renklerini sayma oyunu buldu
@tohum: keloglan-0197
@degisim: biberli -> renkli
Yağmur cama pıt pıt vuruyordu. Keloğlan ile Balkız evde oturuyordu. Yağmur yüzünden dışarıda oynayamıyorlardı ve çok sıkılmışlardı. Birden damlalar durdu ve güneş çıktı. Keloğlan pencereden baktı ve buğday tarlasının üstünde renkli bir gökkuşağı gördü. "Bak, Balkız, gökkuşağı çıktı! Hadi renklerini öğrenelim," dedi Keloğlan. Keloğlan her rengi parmağıyla gösterdi. "Kırmızı, turuncu, sarı, yeşil ve mavi," dedi Keloğlan. "En alttaki de mor," dedi Balkız. İkisi renkleri birlikte saydı. Keloğlan ile Balkız çok sevindi, çünkü yağmurlu günde güzel bir oyun bulmuşlardı.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Birden damlalar durdu ve güneş çıktı"
   - Cümle 4: «Birden damlalar durdu ve güneş çıktı.»
   - Açıklama: Sıkılma sorununu Keloğlan değil kendiliğinden duran yağmur ve çıkan gökkuşağı çözüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden damlalar durdu ve güneş çıktı"
   - Cümle 4: «Birden damlalar durdu ve güneş çıktı.»
   - Açıklama: Çözüme giden gökkuşağı figürün eylemiyle değil sebepsiz bir şans olayıyla geliyor.
   - Açıklama: Çözümü getiren gökkuşağı hiçbir sebep olmadan tam gerektiği anda beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0197` birebir aynı, `@degisim: biberli -> renkli` (tutuyorsan), ardından `@onarim: 077ff974fe00bbed6fb9ba1b501d7f5c94e88849`, sonra gövde.

### Hikâye 12: tohum keloglan-0199 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0199
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sandalye', fiil 'sunmak', sıfat 'uzak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: uzaktan garip bir ses geldi | kayalara seslenip sesin geri döndüğünü öğrendi
@tohum: keloglan-0199
@degisim: sunmak -> vermek
Rüzgar hafif hafif esiyordu. Keloğlan tepede Balkız'a bir elma verdi ve "Afiyet olsun, Balkız!" diye seslendi. Birden uzaktan "Balkız!" diye garip bir ses geldi. "Bu ses nereden geldi?" diye sordu Balkız. Keloğlan bunu bulmak istedi. Sandalye gibi düz bir kayadan kalktı ve karşıya baktı. Ellerini ağzına koydu ve karşıdaki büyük kayalara "Elma!" diye seslendi. Biraz sonra kayalardan da "Elma!" diye bir ses geldi. Böylece Keloğlan sesin kayalara çarpıp geri döndüğünü öğrendi. Balkız da kayalara seslendi ve güldü. Keloğlan bundan sonra merak ettiği şeyleri kendisi deneyip buldu.
```

**Hakem bulguları (5):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "uzaktan "Balkız!" diye garip bir ses geldi"
   - Cümle 3: «Birden uzaktan "Balkız!" diye garip bir ses geldi.»
   - Açıklama: Uzaktan gelen kaynağı bilinmeyen garip bir ses küçük çocukta ürküntü yaratabilir.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "diye garip bir ses geldi"
   - Cümle 3: «Birden uzaktan "Balkız!" diye garip bir ses geldi.»
   - Açıklama: Uzaktan ad çağıran garip ses küçük çocuk için ürkütücü olabilir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sandalye gibi düz bir kayadan"
   - Cümle 6: «Sandalye gibi düz bir kayadan kalktı ve karşıya baktı.»
   - Açıklama: Sandalye düz bir şey değildir; benzetme kelimenin anlamına uymuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sandalye gibi düz bir kayadan"
   - Cümle 6: «Sandalye gibi düz bir kayadan kalktı ve karşıya baktı.»
   - Açıklama: Benzetme 3 yaşındaki çocuk için soyut ve gereksiz.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sandalye gibi düz bir kayadan kalktı"
   - Cümle 6: «Sandalye gibi düz bir kayadan kalktı ve karşıya baktı.»
   - Açıklama: Keloğlan'ın oturduğu hiç söylenmemişken sandalye gibi kaya ayrıntısı sebepsiz ve işlevsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0199` birebir aynı, `@degisim: sunmak -> vermek` (tutuyorsan), ardından `@onarim: ce5c907529afc5c87b09b6a3b17d7eea097a1e4c`, sonra gövde.
