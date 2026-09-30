# Editör görevi (onarım): Maşa, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar40.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0072
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'delik', fiil 'getirmek', sıfat 'hazır'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: cebindeki delikten kozalaklar yere düşüyordu | reçeli yiyip boş kavanozu kuzenine verdi
@tohum: masa-0072
Ormanda yapraklar rüzgarda sallanıyordu. Maşa reçel kavanozunu tutuyordu, kuzeni Daşa da şehre götürmek için kozalak topluyordu. Ama Daşa'nın cebinde bir delik vardı ve kozalaklar yere düşüyordu. "Maşa, bunları nasıl taşıyacağım?" dedi Daşa. Maşa kavanozdaki son reçeli afiyetle yedi. Sonra boş kavanozu hemen Daşa'ya getirdi. "Onları buna koy, Daşa," dedi Maşa. Daşa yerdeki kozalakları tek tek kavanoza koydu. Maşa kapağı sıkıca kapattı. "Artık hepsi şehre gitmeye hazır!" dedi Daşa. Maşa çok sevindi, çünkü kuzenine yardım etmişti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra boş kavanozu hemen Daşa'ya getirdi"
   - Cümle 6: «Sonra boş kavanozu hemen Daşa'ya getirdi.»
   - Açıklama: Reçeli Daşa yiyor ve kavanozu yine Daşa'ya getiriyor; kimin ne yaptığı çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0072` birebir aynı, ardından `@onarim: bc8c7a8e615f88352197e4537a3d94ea95c9da79`, sonra gövde.

### Hikâye 2: tohum masa-0079 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0079
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pilav', fiil 'kucaklamak', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: pilavı koyduğu ince yaprak yırtıldı ve pilav döküldü | reçeli yiyip taşları boş kavanoza doldurdu
@tohum: masa-0079
Maşa ormanda bir kütüğe sofra kurmuş, yemek oyunu oynuyordu. Beyaz taşlardan pilav yaptı ve pilavı temiz bir yaprağa koydu. Ama yaprak çok inceydi, yırtıldı ve pilav yere döküldü. Maşa üzülmedi ve taşları tek tek topladı. Sofrada biraz reçel kalmış bir kavanoz vardı. Maşa reçeli çok sevdiği için kavanozu hemen boşalttı. Sonra taşların hepsini boş kavanoza doldurdu. Kavanoz sağlamdı ve içindeki hiçbir taş dökülmedi. Maşa kavanozu sevinçle kucakladı ve kütüğe taşıdı. Kavanozu sofranın tam ortasına koydu. Sofra artık hazırdı. Maşa bundan sonra pilavını hep kavanoza koydu.
```

**Hakem bulguları (4):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "bir kütüğe sofra kurmuş,"
   - Cümle 1: «Maşa ormanda bir kütüğe sofra kurmuş, yemek oyunu oynuyordu.»
   - Açıklama: Anlatım -mış ile başlıyor; -dı'lı geçmiş zaman olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa üzülmedi ve taşları tek tek topladı"
   - Cümle 4: «Maşa üzülmedi ve taşları tek tek topladı.»
   - Açıklama: Oyun taşlarının dökülmesi Maşa'yı bile üzmeyen, hemen toplanan önemsiz bir olay.
   - Açıklama: Taş pilavın yere dökülmesi figürün bile üzülmediği önemsiz bir olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sofrada biraz reçel kalmış bir kavanoz vardı"
   - Cümle 5: «Sofrada biraz reçel kalmış bir kavanoz vardı.»
   - Açıklama: Kavanoz önceden kurulmadan tam gerektiği anda beliriyor ve çözümü sebepsizce getiriyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kavanozu sevinçle kucakladı ve kütüğe taşıdı"
   - Cümle 9: «Maşa kavanozu sevinçle kucakladı ve kütüğe taşıdı.»
   - Açıklama: Sofra zaten kütüğün üstündeyken kavanoz kütüğe taşınıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0079` birebir aynı, ardından `@onarim: d9a55aca8785917b89efa3fe9e7459ee52bdb990`, sonra gövde.

### Hikâye 3: tohum masa-0080 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0080
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'süs', fiil 'kurulamak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: reçel kavanozu yokuştan yuvarlandı ve çimenlerde kayboldu | kavanozdaki kırmızı süsü arayıp kavanozu buldu
@tohum: masa-0080
Bir sabah Maşa ile kuzeni Daşa tepede sincapla piknik yapıyordu. Daşa tuzlu ekmekleri örtünün üstüne koydu. Ama Maşa'nın reçel kavanozu kaydı ve yokuştan aşağı yuvarlandı. Kavanoz ıslak çimenlerin arasında kayboldu. "Reçelim nerede?" diye sordu Maşa. Maşa reçelini çok sevdiği için kavanozun kapağına kırmızı bir süs bağlamıştı. Maşa çimenlerin arasında o kırmızı süsü aradı. Sonunda süsü bir çalının altında gördü. Maşa eğildi ve kavanozu oradan aldı. Kavanoz ıslanmıştı, Daşa onu örtünün ucuyla kuruladı. "Reçelim burada, Daşa!" dedi Maşa. Maşa ekmeğine reçel sürdü ve sincaba da bir parça verdi. Maşa ile Daşa çok sevindi, çünkü kaybolan reçel yine yanlarındaydı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kavanozun kapağına kırmızı bir süs bağlamıştı"
   - Cümle 6: «Maşa reçelini çok sevdiği için kavanozun kapağına kırmızı bir süs bağlamıştı.»
   - Açıklama: Kırmızı süs sorun çıktıktan sonra, yalnızca çözümü getirmek için geriye dönük olarak kuruluyor.
   - Açıklama: Kırmızı süs sorun çıktıktan sonra geriye dönük olarak kuruluyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0080` birebir aynı, ardından `@onarim: 834e34edcffc76ffc55db1c03ddb48b15adcc1af`, sonra gövde.

### Hikâye 4: tohum masa-0083 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0083
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kemer', fiil 'sallamak', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: kavanozdaki çiçek gölgede kaldı ve açılmadı | kavanozu güneşli bir yere taşıyıp reçel yiyerek bekledi
@tohum: masa-0083
@degisim: kemer -> sepet
Hava aydınlıktı ve evin önünde kuşlar ötüyordu. Maşa ile kirpi kavanozdaki kırmızı çiçeğin açılmasını bekliyordu. Ama kavanoz ağacın gölgesinde kalmıştı ve çiçek açılmıyordu. Maşa kavanozu aldı ve güneşli bir yere taşıdı. Beklemek Maşa için zordu. Maşa reçel dolu sepetini getirdi ve çiçeğin yanına oturdu. En sevdiği reçeli kaşık kaşık yedi ve beklerken hiç kalkmadı. Güneş çiçeği ısıttı. Kırmızı çiçek yavaş yavaş açıldı. "Bak, kirpi, çiçek açıldı!" dedi Maşa. Kirpi çiçeği kokladı ve sevinçle başını salladı. Maşa ile kirpi çiçeğin yanında mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "reçel dolu sepetini getirdi"
   - Cümle 6: «Maşa reçel dolu sepetini getirdi ve çiçeğin yanına oturdu.»
   - Açıklama: Sepet reçelle dolmaz; 'reçel kavanozlarıyla dolu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa reçel dolu sepetini getirdi"
   - Cümle 6: «Maşa reçel dolu sepetini getirdi ve çiçeğin yanına oturdu.»
   - Açıklama: Reçel sepeti ve reçel yemek çiçeğin açılmasına hiçbir katkı yapmıyor; işlevsiz ayrıntı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "En sevdiği reçeli kaşık kaşık yedi"
   - Cümle 7: «En sevdiği reçeli kaşık kaşık yedi ve beklerken hiç kalkmadı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümüne katkı vermiyor; çiçek güneşe taşındığı için açılıyor, reçel yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0083` birebir aynı, `@degisim: kemer -> sepet` (tutuyorsan), ardından `@onarim: cf0658014730ef1af395f08dba0f7480904aa273`, sonra gövde.

### Hikâye 5: tohum masa-0090 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0090
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çarşaf', fiil 'sarılmak', sıfat 'ilginç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: rüzgar yere serilen çarşafı havaya kaldırdı | çarşafın her ucuna birer reçel kavanozu koydu
@tohum: masa-0090
@degisim: ilginç -> beyaz
Ormanda Maşa ile Daşa sincap için bir sürpriz hazırlıyordu. Maşa'nın sepetinde fındık ve en sevdiği reçelden dört kavanoz vardı. Bir ağacın altına beyaz bir çarşaf serdiler ama rüzgar onu havaya kaldırdı. "Maşa, rüzgar çarşafı uçuruyor!" dedi Daşa. Maşa çarşafı yeniden serdi. Sonra çarşafın her ucuna bir reçel kavanozu koydu. Rüzgar yine esti ama çarşaf artık kalkmadı. İki kız fındıkları çarşafın ortasına koydu. "Bak, Maşa, kavanozlar çarşafı tuttu!" dedi Daşa. Tam o sırada sincap ağaçtan hızla indi. Fındıkları görünce sevinçle bir tanesine sarıldı. Maşa çok sevindi, çünkü sürprizleri sincabı mutlu etmişti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tam o sırada sincap ağaçtan hızla indi"
   - Cümle 10: «Tam o sırada sincap ağaçtan hızla indi.»
   - Açıklama: Kavanozları koyan sincap sonradan ağaçtan yeni iniyormuş gibi anlatılıyor ve sürprizi zaten görmüş oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0090` birebir aynı, `@degisim: ilginç -> beyaz` (tutuyorsan), ardından `@onarim: d0b8371afec5048ec7c907061e7a0740c32c425b`, sonra gövde.

### Hikâye 6: tohum masa-0095 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi, Daşa
@tohum: masa-0095
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'paket', fiil 'süpürmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi, Daşa
@plan: zıplarken paketi düşürdü ve kurabiyeler kırıldı | özür diledi ve kırık parçaları reçelle yapıştırdı
@tohum: masa-0095
@degisim: berrak -> mavi
Bir sabah ormanda gökyüzü maviydi. Daşa şehirden bir paket kurabiye, Maşa da reçel getirmişti. Maşa sevinçle zıplarken paketi düşürdü ve içindeki kurabiyeler ikiye kırıldı. "Hepsi kırıldı," dedi Daşa üzgün bir sesle. "Özür dilerim, Daşa, çok hızlı zıpladım," dedi Maşa. Sonra reçel kavanozunu açtı. Kırık parçaların arasına reçel sürüp onları birbirine yapıştırdı. Kurabiyeler yine bütün ve reçelli oldu. Sonra Maşa yere dökülen kırıntıları bir dalla bir yaprağa süpürdü. Kirpi kırıntıları mutlu mutlu yedi. Daşa reçelli bir kurabiye tattı ve gülümsedi. "Teşekkürler, Maşa, bunlar çok güzel olmuş!" dedi Daşa.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kirpi kırıntıları mutlu mutlu yedi"
   - Cümle 10: «Kirpi kırıntıları mutlu mutlu yedi.»
   - Açıklama: Kirpi daha önce hiç anılmadan sebepsizce beliriyor.
   - Açıklama: Kirpi daha önce hiç tanıtılmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0095` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: 6987c2fc5a4519d6babbb69147b9c1cd832f3c84`, sonra gövde.

### Hikâye 7: tohum masa-0096 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı, sincap
@tohum: masa-0096
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boya', fiil 'sararmak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı, sincap
@plan: sincap boş bir kovaya girdi ve dışarı çıkamadı | kovaya uzun bir dal koydu ve sincap tırmandı
@tohum: masa-0096
Bir sabah Maşa, Koca Ayı'nın bahçesinde sararmış yapraklarla oynuyordu. Koca Ayı evinin kapısını boyamış, boş boya kovasını yere koymuştu. Oynayan bir sincap zıplayıp bu kovaya girdi ve dışarı çıkamadı. Kovanın içi çok kaygandı. Maşa heyecanlı heyecanlı sincabın yanına koştu. Önce elini uzattı ama kova çok derindi. Sonra yerdeki uzun bir dalı kovaya koymayı denedi. Sincap dala tutundu ve hızla yukarı tırmandı. Kovadan atladı ve kuyruğunu sallayarak ağaca koştu. Koca Ayı Maşa'ya bakıp gülümsedi. Maşa bundan sonra boş kovaları hep ters çevirip koydu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa heyecanlı heyecanlı sincabın"
   - Cümle 5: «Maşa heyecanlı heyecanlı sincabın yanına koştu.»
   - Açıklama: 'Heyecanlı heyecanlı' doğal bir ikileme değil; 'heyecanla' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0096` birebir aynı, ardından `@onarim: a400598aa9b8126dde5323444fab4c4af4042d86`, sonra gövde.

### Hikâye 8: tohum masa-0102 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0102
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kanepe', fiil 'fışkırmak', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: zıplarken ayakkabısı yumuşak çamura battı | ayağını sağa sola küçük küçük salladı
@tohum: masa-0102
@degisim: kanepe -> çamur
Bir sabah ormanda yağmur yeni dinmişti. Maşa patikadaki su birikintilerine zıplıyor, sular havaya fışkırıyordu. Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura battı. Maşa ayağını hızla çekti ama ayağı yerinden çıkmadı. Maşa durmadı ve başka bir şey denedi. Ayağını sağa ve sola küçük küçük salladı. Ayakkabı biraz oynayınca Maşa umutlu oldu ve daha çok salladı. Sonunda ayağı ayakkabısıyla birlikte çamurdan çıktı. Maşa çamurlu ayakkabısına baktı ve güldü. Sonra yine su birikintilerine zıpladı ama bu kez çamurdan uzak durdu. Maşa bundan sonra çamurda ayağını çekmedi, yavaşça salladı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama ayağı yerinden çıkmadı"
   - Cümle 4: «Maşa ayağını hızla çekti ama ayağı yerinden çıkmadı.»
   - Açıklama: 'Ayağı yerinden çıkmak' çıkık anlamına gelir; 'ayağı çamurdan çıkmadı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa umutlu oldu"
   - Cümle 7: «Ayakkabı biraz oynayınca Maşa umutlu oldu ve daha çok salladı.»
   - Açıklama: 'Umutlu' soyut bir duygu kavramı.
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk için ağır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0102` birebir aynı, `@degisim: kanepe -> çamur` (tutuyorsan), ardından `@onarim: ec4c3fc17fbe38bef5bcc7383fd5adcc2749a944`, sonra gövde.

### Hikâye 9: tohum masa-0103 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0103
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'şerit', fiil 'kaçmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: reçel kavanozu yokuştan aşağı yuvarlandı ve kayboldu | kavanozdaki kırmızı şeridi otların arasında aradı
@tohum: masa-0103
@degisim: kaçmak -> yuvarlanmak
Rüzgar hafif hafif esiyordu. Maşa tepede elmalı bir kurabiyeyi reçelle yiyordu. Ama reçel kavanozu elinden kaydı ve yokuştan aşağı yuvarlandı. Kavanoz uzun otların arasında kayboldu. Maşa aşağıya yavaşça indi ve otlara baktı. Ama otlar çok sıktı ve kavanoz görünmüyordu. Kavanozun kapağına kırmızı bir şerit bağlıydı. Maşa otların arasında o kırmızı şeridi aradı. Sonunda bir çalının dibinde kırmızı şerit göründü. Maşa kavanozu aldı ve ona sevinçle sarıldı. Sonra tepeye geri çıktı ve kurabiyeyi reçelle mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kavanozun kapağına kırmızı bir şerit bağlıydı"
   - Cümle 7: «Kavanozun kapağına kırmızı bir şerit bağlıydı.»
   - Açıklama: Çözümü sağlayan kırmızı şerit önceden kurulmadan tam gerektiği anda beliriyor.
   - Açıklama: Kırmızı şerit sorun çıktıktan sonra sebepsizce beliriyor ve çözümü hazır getiriyor.
   - Açıklama: Kırmızı şerit tam gerektiği anda sebepsizce beliriyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0103` birebir aynı, `@degisim: kaçmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: cb394ce533295a391de89a1a62e9390af0f412ee`, sonra gövde.

### Hikâye 10: tohum masa-0106 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0106
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'saat', fiil 'tamamlamak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: sincap yapbozun son parçasını fındık sandı ve kaçtı | yardım isteyip sincaba bir fındık verdi
@tohum: masa-0106
@degisim: saat -> yapboz
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa meyveli bir ağacın yapbozunu yapıyordu. Ama bir sincap yuvarlak, kahverengi son parçayı fındık sandı ve kapıp kaçtı. Sincap bir taşın üstüne oturdu. Parça olmadan yapboz bitmiyordu ve Maşa üzüldü. Maşa'nın cebinde hiç fındık yoktu, bu yüzden Daşa'dan yardım istedi. Daşa cebinden bir fındık çıkarıp Maşa'ya verdi. Maşa parçayı fındıkla değiştirmeyi denedi. Fındığı taşın yanına koydu. Sincap taştan indi, parçayı bıraktı ve fındığı aldı. Maşa son parçayı hemen yerine koydu ve yapbozu tamamladı. Daşa ile Maşa meyveli ağaca bakıp güldüler. Maşa bundan sonra zor bir işte hemen yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra zor bir işte hemen yardım istedi."
   - Cümle 13: «Maşa bundan sonra zor bir işte hemen yardım istedi.»
   - Açıklama: 'Bundan sonra' ile tek seferlik geçmiş zaman uyumsuz; 'yardım istemeye karar verdi' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0106` birebir aynı, `@degisim: saat -> yapboz` (tutuyorsan), ardından `@onarim: 921c758a06588192519f6cff8e0e9e36f548bfee`, sonra gövde.

### Hikâye 11: tohum masa-0112 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0112
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buz', fiil 'tamamlanmak', sıfat 'uykulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: reçel kavanozu kapının önünden kaybolmuştu | reçel damlalarını izledi ve kavanozu buldu
@tohum: masa-0112
@degisim: tamamlanmak -> damlamak
Soğuk bir rüzgar esiyordu. Maşa, Koca Ayı'nın bahçesinde oynarken reçel kavanozunu kapının önüne koymuştu. Ama geri döndüğünde kavanoz yerinde yoktu. Maşa kavanozu kimin aldığını çok merak etti. Kapının önündeki taşa kırmızı bir şey damlamıştı. Maşa eğilip kokladı ve kendi reçelini hemen tanıdı. Bahçedeki beyaz buzun üstünde de kırmızı damlalar vardı. Maşa damlaları izledi ve ağaç evin arkasına yürüdü. Orada uykulu Koca Ayı bir kütüğün üstünde oturuyordu. Koca Ayı iki dilim ekmeğe Maşa'nın reçelini sürüyordu. "Koca Ayı, reçelimi sen mi aldın?" diye sordu Maşa. Koca Ayı başını salladı ve bir dilimi Maşa'ya uzattı. "Teşekkürler, Koca Ayı, haydi birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Koca Ayı iki dilim ekmeğe Maşa'nın reçelini sürüyordu"
   - Cümle 10: «Koca Ayı iki dilim ekmeğe Maşa'nın reçelini sürüyordu.»
   - Açıklama: Kartta iyi kalpli eski dost olan Koca Ayı, Maşa'nın reçelini habersizce alan biri olarak gösteriliyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Koca Ayı iki dilim ekmeğe Maşa'nın reçelini sürüyordu"
   - Cümle 10: «Koca Ayı iki dilim ekmeğe Maşa'nın reçelini sürüyordu.»
   - Açıklama: Kartın iliski alanında iyi kalpli dost olan Koca Ayı Maşa'nın reçelini habersiz alıyor; dizideki rolleri ters çevriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0112` birebir aynı, `@degisim: tamamlanmak -> damlamak` (tutuyorsan), ardından `@onarim: 987debe790845fe297fe51141a0af9f338f8414f`, sonra gövde.

### Hikâye 12: tohum masa-0117 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi, Daşa
@tohum: masa-0117
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buket', fiil 'toplanmak', sıfat 'memnun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi, Daşa
@plan: reçel kavanozunun kapağı çok sıkıydı | kuzeninden yardım isteyip kapağı birlikte açtı
@tohum: masa-0117
@degisim: memnun -> mutlu
Bir sabah kuzeni Daşa, Maşa'ya bir buket çiçek getirdi. Maşa buketi bahçedeki masaya koydu ve kirpiyle Daşa'yı kahvaltıya çağırdı. Maşa ekmeğine reçel sürmek istedi, ama reçel kavanozunun kapağı çok sıkıydı. "Daşa, kapak açılmıyor, bana yardım eder misin?" diye sordu Maşa. Daşa kavanozu sıkıca tuttu. Maşa kapağı çevirdi. Bu kez kapak "pıt" diye açıldı. Maşa iki dilim ekmeğe bol bol reçel sürdü ve birini Daşa'ya verdi. Kirpiye de masadan küçük bir elma verdi ve kirpi çok sevindi. Sonra üçü çiçeklerin yanında toplandı ve mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bir sabah kuzeni Daşa,"
   - Cümle 1: «Bir sabah kuzeni Daşa, Maşa'ya bir buket çiçek getirdi.»
   - Açıklama: 'Kuzeni' iyeliği Maşa henüz anılmadan kullanılıyor; kimin kuzeni olduğu cümle başında belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bir sabah kuzeni Daşa, Maşa'ya"
   - Cümle 1: «Bir sabah kuzeni Daşa, Maşa'ya bir buket çiçek getirdi.»
   - Açıklama: 'kuzeni' iyelik eki, kimin kuzeni olduğu henüz tanıtılmamış bir kişiyi gösteriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kuzeni Daşa, Maşa'ya bir buket çiçek getirdi"
   - Cümle 1: «Bir sabah kuzeni Daşa, Maşa'ya bir buket çiçek getirdi.»
   - Açıklama: Çiçek buketi hikayeyi açıyor ama sorunla ve çözümle hiçbir ilgisi yok; işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir buket çiçek getirdi"
   - Cümle 1: «Bir sabah kuzeni Daşa, Maşa'ya bir buket çiçek getirdi.»
   - Açıklama: Hikaye kavanoz sorunuyla ilgisiz bir buketle açılıyor ve buket olayda hiçbir işe yaramıyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kirpiyle Daşa'yı kahvaltıya çağırdı"
   - Cümle 2: «Maşa buketi bahçedeki masaya koydu ve kirpiyle Daşa'yı kahvaltıya çağırdı.»
   - Açıklama: 'kirpiyle' yapısı belirsiz; Maşa'nın kirpiyle birlikte mi çağırdığı yoksa kirpiyi ve Daşa'yı mı çağırdığı anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0117` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: cccdc14724760483c7dc88a7916ec24668b10c41`, sonra gövde.
