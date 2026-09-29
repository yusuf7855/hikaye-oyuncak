# Editör görevi (onarım): Keloğlan, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0031
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'damla', fiil 'işaretlemek', sıfat 'kirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: kağıda boya damladı ve kağıt kirlendi | fırçayı kabın kenarına silip yeniden boyadı
@tohum: keloglan-0031
Keloğlan şatonun bahçesinde ilk kez boyayla resim yapmayı denedi. Karakaçan resim çantasını sırtında taşımıştı. Ama kağıda iri bir boya damlası düştü ve kağıt kirli oldu. "Ah, resmim bozuldu!" dedi Keloğlan. Keloğlan fırçaya dikkatle baktı. Fırça boyayla doluydu. Fırçayı kabın kenarına hafifçe sildi. Böylece boyayı az almayı öğrendi. Sonra çantadan temiz bir kağıt aldı. Önce fırçanın ucuyla kağıtta kapının yerini işaretledi. Sonra şatonun yüksek kapısını yavaşça boyadı ve kağıda hiç leke düşmedi. Karakaçan başını salladı. "Karakaçan, bak, ilk resmim ne güzel oldu!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra çantadan temiz bir kağıt aldı"
   - Cümle 9: «Sonra çantadan temiz bir kağıt aldı.»
   - Açıklama: Çözüm silme, yeni kağıt alma, işaretleme ve boyama ile ikiden fazla adım sürüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kağıtta kapının yerini işaretledi"
   - Cümle 10: «Önce fırçanın ucuyla kağıtta kapının yerini işaretledi.»
   - Açıklama: Kapının yerini işaretleme adımı sorunla ilgisiz ve işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "fırçanın ucuyla kağıtta kapının yerini işaretledi"
   - Cümle 10: «Önce fırçanın ucuyla kağıtta kapının yerini işaretledi.»
   - Açıklama: İşaretleme adımı sorunla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0031` birebir aynı, ardından `@onarim: 5aca689b3c76a3d1522c7820716fc7c8103d53fe`, sonra gövde.

### Hikâye 2: tohum keloglan-0033 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0033
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'eldiven', fiil 'açmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek acıktı ama ormanda hiç ot yoktu | çantasını açıp havuçları eşeğine yedirdi
@tohum: keloglan-0033
Keloğlan puantiyeli eldivenleriyle ormanda odun topluyordu. Eşeği Karakaçan odunları sırtında taşıyordu. Birden Karakaçan durdu ve yürümedi, çünkü çok acıkmıştı. Ama büyük ağaçların altında hiç ot yoktu. "Bekle, Karakaçan, çantamda havuç var," dedi Keloğlan. Hemen eldivenlerini çıkardı ve çantasını açtı. Sakar Keloğlan bütün havuçları yere düşürdü. Havuçlar yuvarlandı ve eşeğin ayaklarının önüne geldi. Eşek havuçları tek tek yedi. Sonra mutlu mutlu kuyruğunu oynattı. "Karnın doydu mu, Karakaçan?" diye sordu Keloğlan. Karakaçan başını iki kez salladı. Keloğlan çok sevindi, çünkü eşeği artık aç değildi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan puantiyeli eldivenleriyle ormanda"
   - Cümle 1: «Keloğlan puantiyeli eldivenleriyle ormanda odun topluyordu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hemen eldivenlerini çıkardı ve çantasını açtı"
   - Cümle 6: «Hemen eldivenlerini çıkardı ve çantasını açtı.»
   - Açıklama: Puantiyeli eldivenler işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlev görmüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan bütün havuçları yere düşürdü"
   - Cümle 7: «Sakar Keloğlan bütün havuçları yere düşürdü.»
   - Açıklama: Puantiyeli eldiven ve havuçların düşmesi çözüme katkısı olmayan işlevsiz ayrıntılar; havuçlar şans eseri eşeğe yuvarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0033` birebir aynı, ardından `@onarim: cb6fa3c4a9ad5706c122bc04f918358ff9e2823e`, sonra gövde.

### Hikâye 3: tohum keloglan-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0034
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'krema', fiil 'güvenmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: sepet taşa çarptı ve arkadaşının keki ezildi | kekini paylaştı ve arkadaşına güvendi
@tohum: keloglan-0034
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız tekerlekli sepeti tepeye çekiyordu. Sepet bir taşa çarptı ve Balkız'ın keki yere düşüp ezildi. Balkız yerdeki keke üzgün üzgün baktı. Keloğlan'ın kremalı keki ise sepette duruyordu. Keloğlan kekini Balkız ile paylaşmak istedi. Keki bir tabağa koydu ve ikiye ayırmak istedi. Ama biraz sakardı ve kek elinden tabağın kenarına kaydı. Keloğlan bu kez Balkız'a güvendi ve tabağı ona verdi. Balkız keki dikkatle iki eşit parçaya böldü. İkisi tepede çimenlere oturdu ve keklerini yedi. Keloğlan'ın burnuna biraz krema bulaştı ve Balkız güldü. Keloğlan çok mutluydu, çünkü kekini arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (6):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keki bir tabağa koydu ve ikiye ayırmak istedi"
   - Cümle 7: «Keki bir tabağa koydu ve ikiye ayırmak istedi.»
   - Açıklama: Çözüm paylaşma, tabağa koyma, bölmeye çalışma, tabağı verme gibi ikiden çok adıma yayılıyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama biraz sakardı ve kek elinden tabağın kenarına kaydı"
   - Cümle 8: «Ama biraz sakardı ve kek elinden tabağın kenarına kaydı.»
   - Açıklama: Ezilen kek sorunundan sonra kekin kayması ikinci bir sorun olarak ekleniyor.
   - Açıklama: Ezilen kek sorununun üstüne kekin kayması ikinci bir sorun olarak ekleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan bu kez Balkız'a"
   - Cümle 9: «Keloğlan bu kez Balkız'a güvendi ve tabağı ona verdi.»
   - Açıklama: 'Bu kez' önceden Balkız'a güvenmediği bir durum ima ediyor ama öyle bir durum yok; kelime yanlış anlamda.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan bu kez Balkız'a güvendi"
   - Cümle 9: «Keloğlan bu kez Balkız'a güvendi ve tabağı ona verdi.»
   - Açıklama: 'Güvenmek' soyut bir kavram ve olaydan çıkan somut bir ders cümlesi değil.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tepede çimenlere oturdu ve keklerini yedi"
   - Cümle 11: «İkisi tepede çimenlere oturdu ve keklerini yedi.»
   - Açıklama: Tek kek paylaşıldığı için 'keklerini' çoğulu yanlış; 'keki' olmalı.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İkisi tepede çimenlere oturdu ve keklerini yedi"
   - Cümle 11: «İkisi tepede çimenlere oturdu ve keklerini yedi.»
   - Açıklama: Balkız'ın keki ezilmişken ikisinin de kendi kekini yemesi paylaşılan tek kekle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0034` birebir aynı, ardından `@onarim: 8a49a9c4fba2a7c594a7cf1d3a92dab6c2507813`, sonra gövde.

### Hikâye 4: tohum keloglan-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0035
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'süpürge', fiil 'ısınmak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: koşarken un kabını düşürdü ve un döküldü | unu süpürgeyle temizleyip anasından özür diledi
@tohum: keloglan-0035
@degisim: aceleci -> hızlı
Soğuk rüzgar evin penceresini sallıyordu. Keloğlan ısınmak için odada hızlı hızlı koştu. Ama sakar Keloğlan koşarken kolunu un kabına çarptı ve kap düştü. Beyaz un yere döküldü. Anası yeri daha yeni temizlemişti ve biraz üzüldü. Keloğlan anasının yüzüne baktı ve çok utandı. Keloğlan hemen köşedeki süpürgeyi aldı. Dökülen bütün unu dikkatle süpürdü. Sonra anasına sarıldı ve özür diledi. Anası gülümsedi ve onu sıcacık öptü. Keloğlan çok rahatladı, çünkü anası artık üzgün değildi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan ısınmak için odada hızlı hızlı koştu"
   - Cümle 2: «Keloğlan ısınmak için odada hızlı hızlı koştu.»
   - Açıklama: Evin içinde hızla koşup eşyaya çarpmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0035` birebir aynı, `@degisim: aceleci -> hızlı` (tutuyorsan), ardından `@onarim: 13ee2e86047b1d8b14e8554304e98217911b8d95`, sonra gövde.

### Hikâye 5: tohum keloglan-0036 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0036
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'duvar', fiil 'öğrenmek', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kar çok yumuşaktı ve duvar hep yıkılıyordu | karı sıkıca sıkıp sert toplar yaptı
@tohum: keloglan-0036
@degisim: öğrenmek -> sıkmak
Bir sabah ormana bembeyaz kar yağmıştı. Keloğlan büyük ağaçların arasında kardan bir duvar yapmak istedi. Ama kar çok yumuşaktı ve duvar hep yıkılıyordu. Keloğlan dürüst ve azimli bir çocuktu, yeniden denedi. Karı iki elinin arasında sıkıca sıktı. Kar sert bir top oldu. Keloğlan böyle toplardan bir sürü yaptı. Sonra kar toplarını yan yana ve üst üste koydu. Duvar yavaş yavaş yükseldi. Sonunda Keloğlan'ın boyu kadar yüksek oldu. Keloğlan duvarın arkasına oturdu ve gülümsedi. Keloğlan çok sevindi, çünkü kardan duvarı bitirmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "azimli bir çocuktu, yeniden denedi"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, yeniden denedi.»
   - Açıklama: İki yüklem bağlaçsız virgülle bağlanmış; cümle bozuk kuruluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, yeniden denedi.»
   - Açıklama: 'Azimli' ve 'dürüst' 3 yaşındaki çocuğun bilmeyeceği soyut kelimeler ve olayla ilgisiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0036` birebir aynı, `@degisim: öğrenmek -> sıkmak` (tutuyorsan), ardından `@onarim: 9a3e559bc1f05d921c842fca1ec3f9e4f5d1a8fd`, sonra gövde.

### Hikâye 6: tohum keloglan-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0039
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'zil', fiil 'katlamak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: zil ağırdı ve kağıt oyuncak hemen düştü | kanatları açıp daha geniş katladı
@tohum: keloglan-0039
Keloğlan ormanda kağıttan kanatlı bir oyuncak katladı ve ucuna bir zil bağladı. Oyuncak havada uçarken zil çalacak ve çok eğlenceli olacaktı. Ama zil ağırdı ve oyuncak her seferinde hemen yere düştü. Keloğlan düşünceli bir yüzle oyuncağa baktı. Sonra kanatları açtı ve onları daha geniş katladı. Oyuncağı yeniden büyük ağaçların arasına fırlattı. Bu kez oyuncak uzun uzun süzüldü ve zil çın çın çaldı. Böylece Keloğlan geniş kanatlı oyuncağın daha iyi uçtuğunu öğrendi. Keloğlan oyuncağını tekrar tekrar fırlattı ve güldü. Keloğlan çok mutluydu, çünkü kağıt oyuncak sonunda zilini çalarak uçmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kağıt oyuncak sonunda zilini çalarak uçmuştu"
   - Cümle 10: «Keloğlan çok mutluydu, çünkü kağıt oyuncak sonunda zilini çalarak uçmuştu.»
   - Açıklama: Son cümle oyuncağın zil çalarak uçtuğunu gereksizce yeniden söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0039` birebir aynı, ardından `@onarim: 07fc1b5d41083120a08785c1515ce61ca97eaa5d`, sonra gövde.

### Hikâye 7: tohum keloglan-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0040
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mermer', fiil 'savurmak', sıfat 'süslü'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: ikisi de ipi aynı anda çekti | sırayla oynamayı söyledi ve önce arkadaşına verdi
@tohum: keloglan-0040
Keloğlan ile Balkız şatonun bahçesinde mermer bir yolda oynuyordu. Ellerinde tek bir süslü topaç vardı. İkisi de ipi aynı anda çekti ve ip karmakarışık oldu. "Balkız, sırayla oynayalım, önce sen çevir," dedi Keloğlan. Keloğlan ipi çözdü ve topacı Balkız'a verdi. Balkız ipi sardı ve topacı yere savurdu. Topaç taşın üstünde uzun uzun döndü. Sıra Keloğlan'a geldi. Keloğlan ipi sardı, ama biraz sakardı ve topaç elinden düştü. Topaç yine de güzelce döndü. İkisi de güldü. "Sırayla oynamak çok eğlenceli, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şatonun bahçesinde mermer bir yolda"
   - Cümle 1: «Keloğlan ile Balkız şatonun bahçesinde mermer bir yolda oynuyordu.»
   - Açıklama: 'Şato' ve 'mermer' kelimelerini 3 yaşındaki bir çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ama biraz sakardı ve topaç elinden düştü"
   - Cümle 9: «Keloğlan ipi sardı, ama biraz sakardı ve topaç elinden düştü.»
   - Açıklama: Topacın elden düşmesi hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı ve düşen topacın yine de dönmesi sebepsiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "biraz sakardı ve topaç elinden düştü"
   - Cümle 9: «Keloğlan ipi sardı, ama biraz sakardı ve topaç elinden düştü.»
   - Açıklama: Topacın düşmesi hiçbir sonucu olmayan, kendiliğinden kapanan işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0040` birebir aynı, ardından `@onarim: ced066e8399157e3bbfea4180db343d1174f8d4c`, sonra gövde.

### Hikâye 8: tohum keloglan-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0042
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yağmurluk', fiil 'boyamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: tepeyi boyamak için yeşil boya bitmişti | yanlışlıkla sarıyı maviye karıştırıp yeşil yaptı
@tohum: keloglan-0042
@degisim: yağmurluk -> fırça
Keloğlan tepede resim yapma oyunu oynuyordu. Bilgecan Dede de yanına oturmuş, onu izliyordu. Keloğlan tepeyi boyamak istedi ama yeşil boyası bitmişti. Elinde yalnız sarı ile mavi boya vardı. Sakar Keloğlan sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı. Mavi renk yavaş yavaş yeşile döndü. "Dede, bak, yeşil oldu!" dedi Keloğlan. "Sarı ile mavi karışınca yeşil olur," dedi Bilgecan Dede. Keloğlan iki rengi biraz daha karıştırdı. Sonra resimdeki tepeyi yemyeşil boyadı. Bilgecan Dede resmi görünce ellerini çırptı. Keloğlan da mutlu mutlu yeni bir resme başladı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan tepeyi boyamak istedi"
   - Cümle 3: «Keloğlan tepeyi boyamak istedi ama yeşil boyası bitmişti.»
   - Açıklama: Keloğlan tepede olduğundan 'tepeyi boyamak' gerçek tepe mi resimdeki tepe mi belirsiz.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı"
   - Cümle 5: «Sakar Keloğlan sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı.»
   - Açıklama: Sorun figürün bilinçli çözümüyle değil bir kazayla çözülüyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı"
   - Cümle 5: «Sakar Keloğlan sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı.»
   - Açıklama: Yeşil boya sorunu Keloğlan'ın bilinçli bir çözümüyle değil tesadüfle çözülüyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı"
   - Cümle 5: «Sakar Keloğlan sarı boyalı fırçayı yanlışlıkla mavi boyaya batırdı.»
   - Açıklama: Çözümü sebepsiz bir rastlantı getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0042` birebir aynı, `@degisim: yağmurluk -> fırça` (tutuyorsan), ardından `@onarim: cd689c9b815de3f595dc89d19683d06ac35f5e3b`, sonra gövde.

### Hikâye 9: tohum keloglan-0043 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0043
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yelpaze', fiil 'karşılaşmak', sıfat 'küçücük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: annenin küçücük yelpazesi ormanda düşmüştü | bulduğu yelpazeyi hemen annesine geri verdi
@tohum: keloglan-0043
Keloğlan ormanda anasıyla karşılaştı. Anası üzgündü, çünkü küçücük yelpazesini ormanda düşürmüştü. "Hava çok sıcak," dedi anası. Keloğlan az önce bir ağacın altında güzel bir yelpaze bulmuş, cebine koymuştu. Onu çok beğenmişti. Ama dürüst Keloğlan yelpazeyi hemen cebinden çıkardı. "Anneciğim, bunu ağacın altında buldum, senin mi?" diye sordu Keloğlan. "Evet, bu benim!" dedi anası sevinçle. Keloğlan onu anasına verdi. Anası yelpazeyi salladı ve önce Keloğlan'ı, sonra kendini serinletti. "Teşekkür ederim, Keloğlan, sen bana çok yardım ettin!" dedi anası.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan az önce bir ağacın altında güzel bir yelpaze bulmuş"
   - Cümle 4: «Keloğlan az önce bir ağacın altında güzel bir yelpaze bulmuş, cebine koymuştu.»
   - Açıklama: Çözüm tesadüfle geliyor; kayıp yelpaze sebepsizce zaten Keloğlan'ın cebinde çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "az önce bir ağacın altında güzel bir yelpaze bulmuş"
   - Cümle 4: «Keloğlan az önce bir ağacın altında güzel bir yelpaze bulmuş, cebine koymuştu.»
   - Açıklama: Yelpaze tesadüfen Keloğlan'ın cebinde çıkıyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0043` birebir aynı, ardından `@onarim: e6769e423f9bf2f1f3e6f01f8d541544751fcf6a`, sonra gövde.

### Hikâye 10: tohum keloglan-0044 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0044
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'şişe', fiil 'keşfetmek', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: şişeye üfledi ama hiç ses çıkmadı | şişenin ağzına yandan hafifçe üfledi
@tohum: keloglan-0044
@degisim: keşfetmek -> bulmak
Evde pencereden rüzgar esti ve masadaki boş şişeden ince bir ses çıktı. Keloğlan da bu sesi çıkarmak istedi ve şişeye üfledi. Ama şişenin tam içine üfledi, bu yüzden hiç ses çıkmadı. Bu kez daha güçlü üfledi, ama şişe yine sessizdi. Keloğlan şişeye yakından baktı ve rüzgarı düşündü. Sonunda cevabı buldu: rüzgar şişenin üstünden geçmişti. Keloğlan dudağını şişenin ağzına dayadı ve üstünden hafifçe üfledi. Bu kez şişeden aynı ince ses çıktı. Keloğlan birkaç kez daha üfledi ve güldü. Böylece şişeden ses çıkarmayı öğrendi. Keloğlan bundan sonra ilk seferde olmayan işleri başka türlü denedi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonunda cevabı buldu"
   - Cümle 6: «Sonunda cevabı buldu: rüzgar şişenin üstünden geçmişti.»
   - Açıklama: Soru sorulmadan geçen 'cevabı buldu' soyut bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilk seferde olmayan işleri başka türlü denedi"
   - Cümle 11: «Keloğlan bundan sonra ilk seferde olmayan işleri başka türlü denedi.»
   - Açıklama: 'İlk seferde olmayan işler' soyut ve deyimsel bir anlatım, somut bir ders cümlesi değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0044` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: cf3dacba45663b9d9e9b6cb85f28c81a80bdcdbc`, sonra gövde.

### Hikâye 11: tohum keloglan-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0045
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'boya', fiil 'duymak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: boya kabını düşürdü ve boya yere döküldü | dededen özür diledi ve evi birlikte boyadılar
@tohum: keloglan-0045
Ormanda Bilgecan Dede kuşlar için tahta bir ev boyuyordu. Keloğlan da kırmızı boya kabını tutarak ona yardım ediyordu. Ama sakar Keloğlan kabı düşürdü ve boya yere döküldü. Bilgecan Dede sesi duydu ve arkasına döndü. Keloğlan yerdeki kırmızı lekeye baktı ve başını eğdi. "Özür dilerim, dede, boyayı ben düşürdüm," dedi Keloğlan. "Üzülme, ben hazırlıklıyım, çantamda bir kap daha var," dedi Bilgecan Dede. Dede yeni kabı çantasından çıkardı ve Keloğlan'a verdi. Keloğlan bu kez kabı iki eliyle sıkıca tuttu. İkisi evi birlikte boyadı ve bitirdi. Keloğlan çok sevindi, çünkü dede ona kızmamıştı ve kuşların evi hazırdı.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "çantamda bir kap daha var"
   - Cümle 7: «"Üzülme, ben hazırlıklıyım, çantamda bir kap daha var," dedi Bilgecan Dede.»
   - Açıklama: Sorunu Keloğlan değil, yedek kabı çıkaran Bilgecan Dede çözüyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Dede yeni kabı çantasından çıkardı"
   - Cümle 8: «Dede yeni kabı çantasından çıkardı ve Keloğlan'a verdi.»
   - Açıklama: Dökülen boya sorununu Keloğlan değil, çantasındaki yedek kabı veren dede çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0045` birebir aynı, ardından `@onarim: 5f2e143c752c0fd2a14643188324b9aba59f144e`, sonra gövde.

### Hikâye 12: tohum keloglan-0047 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0047
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kiraz', fiil 'koklamak', sıfat 'meraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: bahçedeki tatlı kokunun nereden geldiğini bilmiyordu | gözlerini kapatıp kokladı ve kiraz ağacını buldu
@tohum: keloglan-0047
Şatonun büyük bahçesinde tatlı bir koku vardı. Meraklı Keloğlan kokunun nereden geldiğini bulmak istedi. Ama bahçede bir sürü ağaç ve çiçek vardı. "Gözlerini kapat ve yalnız burnunu kullan," dedi Balkız. Dürüst Keloğlan gözlerini kapattı ve hiç açmadı. Sonra yavaşça döndü ve havayı kokladı. Sonunda eliyle kapının yanını gösterdi. "Koku buradan geliyor, Balkız!" dedi Keloğlan. Keloğlan gözlerini açtı ve ikisi o tarafa yürüdü. Kapının yanında beyaz çiçekli bir kiraz ağacı vardı. "İşte, kiraz çiçekleri!" dedi Balkız sevinçle. Keloğlan çok sevindi, çünkü kokuyu yalnız burnuyla bulmuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Meraklı Keloğlan kokunun nereden"
   - Cümle 2: «Meraklı Keloğlan kokunun nereden geldiğini bulmak istedi.»
   - Açıklama: Tohumdaki özellik dürüstlük; karttaki özellikler dışında merak ikinci bir özellik olarak ekleniyor ve dürüstlük yalnız gözünü açmamakla zayıf kullanılıyor.
   - Açıklama: Tohumdaki özellik dürüstlük; kartın özellikler alanında olmayan merak ikinci bir özellik olarak ekleniyor ve dürüstlük sorunu çözmüyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Gözlerini kapat ve yalnız burnunu kullan"
   - Cümle 4: «"Gözlerini kapat ve yalnız burnunu kullan," dedi Balkız.»
   - Açıklama: Çözüm yolunu Keloğlan istemeden Balkız buluyor; figür yalnız verilen yöntemi uyguluyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Koku buradan geliyor"
   - Cümle 8: «"Koku buradan geliyor, Balkız!" dedi Keloğlan.»
   - Açıklama: Keloğlan uzaktaki kapının yanını gösterirken 'buradan' değil 'oradan' demeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0047` birebir aynı, ardından `@onarim: 10d005e4a80a293bff14916961f7a6bc7ba5f725`, sonra gövde.
