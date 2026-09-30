# Editör görevi (onarım): Hayri, onarım partisi 55

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar55.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hayri | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar55.txt --ad urun_v2`
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

## Kart: Hayri (kaynaklı, kapalı dünya)

- Ad: Hayri (okunuş: hayri; kesme eki okunuşa uyar)
- Kimlik: Hayri, mahallede arkadaşlarıyla maceralar yaşayan, yemek yemeyi çok seven bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Hayri'nin yemek sevgisi paylaşmak, beklemek ya da yemek hazırlamak olarak gösterilir; çok yiyip midesi ağrımaz, kimse onun yemesiyle ya da kilosuyla alay etmez, tanımadığı birinden yiyecek almaz.
- Özellikler:
  - acık: Yemek yemeyi çok sever; sık sık acıkır. (örnek biçimler: acıktı, acıkmıştı)
  - baklava: Mahalledeki baklava dükkanında çalışır. (örnek biçimler: baklava, baklavayı)
  - abart: Olayları abartmayı sever. (örnek biçimler: abarttı, abartarak)
- Yerler:
  - deniz: Mahallenin yakınındaki deniz kıyısı.
  - orman: Şehrin dışında, ağaçların arasındaki kamp yeri.
  - park: Mahallenin çocuk parkı.
  - ev: Mahalledeki evler, sokak ve bahçeler.
    - yan Basri Amca ise: Basri Amca'nın bahçesi; izinsiz girilmez.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Akın: Mert'in küçük kardeşi ve arkadaş grubunun en küçüğü; çok zekidir, hayvanları çok sever. Tür: oğlan; konuşur. Yüzey biçimleri: Akın
  - Mert: Akın'ın ağabeyi; sakin ve düzenlidir, tartışmaları o bitirir. Tür: oğlan; konuşur. Yüzey biçimleri: Mert
  - Kamil: Hayri'nin yakın arkadaşı; uyumayı ve kitap okumayı çok sever, mahalle bakkalına bakar. Sık sık tartışsalar da birbirlerini çok severler. Tür: oğlan; konuşur. Yüzey biçimleri: Kamil
  - Basri Amca: Mahallede yaşar; çabuk kızar ama iyi kalplidir. Bahçesine izin almadan kimsenin girmesini istemez. Tür: amca; konuşur. Yüzey biçimleri: Basri Amca, Basri, amca
  - Yumak: Basri Amca'nın köpeği; onu Akın bulmuş ve Basri Amca'ya vermiştir. Tür: köpek; KONUŞMAZ. Yüzey biçimleri: Yumak, köpek, köpeği
- Dünya kuralları:
  - Mert ile Akın kardeştir, ağabey Mert'tir; hiçbiri Hayri'nin kardeşi değildir.
  - Yumak Basri Amca'nın köpeğidir; Hayri'nin köpeği yoktur.
  - Yumak konuşmaz; havlar, koklar, kuyruğunu sallar.
- Yasak adlar: Hale, Sevim, Rüstem, Fatma Nine, Sadettin, Saadettin, Kuşçu Baba, Ozan, Nuri, Tamtam
- Yasak: Hayri'nin kız kardeşi kartta yoktur; ailesi hikayeye girmez.
- İzinli dünya kelimeleri: mahalle, baklava, bakkal, abart

## Onarılacak hikâyeler

### Hikâye 1: tohum hayri-0190 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0190
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kutu', fiil 'dikmek', sıfat 'kararlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: fidan dikerken toprakta kapağı sıkı bir kutu buldular | baklava kutusunu tanıdı ve kapağını açtı
@tohum: hayri-0190
@degisim: kararlı -> sıkı
Bir sabah Hayri ile Mert parkta küçük bir fidan dikiyordu. Birden Hayri'nin küreği sert bir şeye değdi. "Tak" diye bir ses çıktı. "Orada ne var, Hayri?" diye sordu Mert. İkisi toprağı elleriyle yavaşça kazdı. Toprağın altından küçük, eski bir kutu çıktı. Mert kutuyu açmak istedi ama kapağı çok sıkıydı. "Bu bir baklava kutusu, dükkanda bunları her gün açarım," dedi Hayri. Hayri kapağı yandan bastırdı ve kapak hemen açıldı. Kutunun içinde renkli misketler vardı. Mert misketleri tek tek saydı ve güldü. Sonra kutuyu bir kenara koydular ve fidanı dikmeyi bitirdiler. Hayri çok sevindi, çünkü kutunun içinde ne olduğunu bulmuştu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «"Tak" diye bir ses çıktı.»
   - Açıklama: Kapağın sıkı olduğu sorun ilk üç cümlede değil ancak yedinci cümlede söyleniyor.
   - Açıklama: Kapağı sıkı kutu sorunu ilk 3 cümlede değil ancak 7. cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Toprağın altından küçük, eski bir kutu çıktı"
   - Cümle 6: «Toprağın altından küçük, eski bir kutu çıktı.»
   - Açıklama: Misketli kutunun parkın toprağında ne aradığı ve kapağın neden sıkı olduğu söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0190` birebir aynı, `@degisim: kararlı -> sıkı` (tutuyorsan), ardından `@onarim: 54f2dd34d36360c769d9fc31de751fd17d84e0f4`, sonra gövde.

### Hikâye 2: tohum hayri-0191 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0191
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'tutkal', fiil 'yüklemek', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: kamyonun kasası küçüktü ve bloklar düşüyordu | kamyona kocaman bir kutu yapıştırdı ve blokları yükledi
@tohum: hayri-0191
@degisim: cömert -> kocaman
Evin içi sıcak ve aydınlıktı. Hayri oyuncak kamyonuna tahta bloklar yüklüyordu. Ama kamyonun kasası küçüktü ve bloklar hep yere düşüyordu. Hayri bunu çok abarttı ve kamyonun bozuk olduğunu sandı. Bu yüzden odadaki en kocaman karton kutuyu getirdi. Kutuyu tutkalla kamyonun üstüne yapıştırdı. Biraz bekledi ve tutkal kurudu. Sonra bütün blokları yeni kasaya tek tek yükledi. Artık hiçbir blok yere düşmedi. Hayri kamyonun ipini tuttu ve onu odada yavaş yavaş çekti. Kamyon blokları rahatça taşıdı. Hayri çok sevindi, çünkü kocaman kasa bütün blokları tutmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri bunu çok abarttı"
   - Cümle 4: «Hayri bunu çok abarttı ve kamyonun bozuk olduğunu sandı.»
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; Hayri bir şeyi abartmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri bunu çok abarttı"
   - Cümle 4: «Hayri bunu çok abarttı ve kamyonun bozuk olduğunu sandı.»
   - Açıklama: 'Abarttı' soyut bir kavram ve burada anlamı da yerine oturmuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden odadaki en kocaman karton kutuyu getirdi"
   - Cümle 5: «Bu yüzden odadaki en kocaman karton kutuyu getirdi.»
   - Açıklama: Kamyonun bozuk olduğunu sanmak kutu yapıştırmayı gerektirmiyor; olay bir öncekinden çıkmıyor.
   - Açıklama: Kamyonun bozuk olduğunu sanmak kutu getirmeye sebep olamaz; olay bir öncekinden çıkmıyor ve 'bozuk sandı' ayrıntısı işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0191` birebir aynı, `@degisim: cömert -> kocaman` (tutuyorsan), ardından `@onarim: c0b58eb48d8103620c90f806c3d37da8ad587ef2`, sonra gövde.

### Hikâye 3: tohum hayri-0192 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0192
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'fincan', fiil 'gülümsemek', sıfat 'ekşi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: çanta açıktı ve elma düşüp kayboldu | yerdeki izin yanından yürüyüp elmayı buldu
@tohum: hayri-0192
Ormandaki kamp yerinde Hayri ile Akın top oynuyordu. Biraz sonra Hayri acıktı ve çantasındaki ekşi elmayı almak istedi. Ama çantanın ağzı açıktı ve elma içinde yoktu. Çantanın yanından ağaçlara doğru ince bir iz gidiyordu. "Bu iz nereye gidiyor, Akın?" diye sordu Hayri. "Bilmiyorum, hadi birlikte bakalım," dedi Akın. Hayri izin yanından yavaş yavaş yürüdü. İz bir ağacın altındaki küçük bir çukurda bitti. Elma orada duruyordu, çünkü çantadan düşüp yuvarlanmıştı. Elmanın üstünde biraz toprak vardı. Akın gülümsedi ve şişedeki suyu bir fincana koydu. Hayri elmayı fincandaki suyla yıkadı ve Akın'a uzattı. "İlk ısırık senin, Akın, elmayı birlikte bulduk!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çünkü çantadan düşüp yuvarlanmıştı"
   - Cümle 9: «Elma orada duruyordu, çünkü çantadan düşüp yuvarlanmıştı.»
   - Açıklama: Yerde duran çantadan elmanın kendiliğinden düşüp ağaçlara kadar iz bırakarak yuvarlanması akla yatkın değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şişedeki suyu bir fincana koydu"
   - Cümle 11: «Akın gülümsedi ve şişedeki suyu bir fincana koydu.»
   - Açıklama: Fincan ve su sebepsiz beliriyor; elma yıkama sorunla ilgisiz bir ek olay.
   - Açıklama: Şişe ve fincan daha önce kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0192` birebir aynı, ardından `@onarim: d19350127a46a2967c49acc41dbdacb91ddeb5e3`, sonra gövde.

### Hikâye 4: tohum hayri-0193 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0193
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: bir şey yapmak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'üniforma', fiil 'girmek', sıfat 'kırık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: bilye kutusunun altında delik vardı ve bilyeler düşüyordu | kartonu baklava kutusu gibi katlayıp yeni kutu yaptı
@tohum: hayri-0193
@degisim: üniforma -> karton
Hayri ile Mert evde bilye oynuyordu. Mert'in bilye kutusu kırıktı ve altında büyük bir delik vardı. Bilyeler bu delikten yere düşüp dağılıyordu. "Yeni bir kutu yapalım mı, Mert?" diye sordu Hayri. "Olur ama nasıl yapacağız?" dedi Mert. Hayri odadan düz bir karton getirdi. Hayri kartonu, dükkandaki baklava kutuları gibi dört yerden katladı. Köşeleri birbirine geçirdi ve sağlam bir kutu yaptı. Mert yerdeki bilyeleri tek tek topladı. Bütün bilyeler yeni kutuya rahatça girdi. "Harika bir kutu olmuş, Hayri!" dedi Mert. Bundan sonra Hayri kırık bir kutu görünce yenisini yapardı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hayri kartonu, dükkandaki baklava"
   - Cümle 7: «Hayri kartonu, dükkandaki baklava kutuları gibi dört yerden katladı.»
   - Açıklama: Nesneden sonra gelen virgül gereksiz; 'Hayri kartonu dükkandaki' olmalı.
   - Açıklama: Nesneden sonra gereksiz virgül kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0193` birebir aynı, `@degisim: üniforma -> karton` (tutuyorsan), ardından `@onarim: 57b7e6c67eee4733506707bd7ff19ff25acbbe6f`, sonra gövde.

### Hikâye 5: tohum hayri-0194 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0194
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'minibüs', fiil 'yaratmak', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: yol suya yakındı ve dalga yolu bozdu | yolun önüne yüksek bir kum duvarı yaptı
@tohum: hayri-0194
@degisim: yaratmak -> yapmak
Bir sabah Hayri kıyıda oyuncak minibüs ile oynuyordu. Kumda minibüs için basit bir yol yapmıştı. Ama yol suya çok yakındı ve bir dalga gelip yolun yarısını bozdu. Minibüs ıslak kumun içinde kaldı. Hayri minibüsü çıkardı ve yolu yeniden düzeltti. Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı. Bu yüzden yolun önüne yüksek bir kum duvarı yaptı. Biraz sonra yeni bir dalga geldi. Dalga duvara çarptı ve geri döndü. Bu kez yol olduğu gibi kaldı. Hayri minibüs ile kumdaki yolda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bunu çok abarttı"
   - Cümle 6: «Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra bunu çok abarttı"
   - Cümle 6: «Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı.»
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği belli değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "dalganın bütün yolu götüreceğini sandı"
   - Cümle 6: «Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı.»
   - Açıklama: Dalga gerçekten yolu bozmuşken bu kaygı abartı sayılıyor, ama duvar gerçek bir tehlikeyi önlüyor; anlatım kendisiyle çelişiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı"
   - Cümle 6: «Sonra bunu çok abarttı ve dalganın bütün yolu götüreceğini sandı.»
   - Açıklama: Korku abartı diye sunuluyor ama gelen dalga gerçekten yolu tehdit ediyor ve duvar gerekli çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0194` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: d8ff03a049999fc8b4862f90cdadd6e745bae092`, sonra gövde.

### Hikâye 6: tohum hayri-0197 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0197
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'yıldız', fiil 'uzaklaştırmak', sıfat 'reçelli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: rüzgar şapkayı çalıların arasına uzaklaştırdı | köpekten yardım istedi ve köpek şapkayı buldu
@tohum: hayri-0197
Bir sabah Hayri ile Yumak kamp yerindeydi. Hayri bir kütüğe oturmuş, reçelli ekmeğini yiyordu. Birden güçlü bir rüzgar Hayri'nin yıldızlı şapkasını çalılara doğru uzaklaştırdı. Hayri çalılara baktı ama şapkayı göremedi. Hayri bu şapkayı baklava dükkanında çalışırken hep takardı. "Yumak, şapkam baklava kokuyor, onu bulmama yardım eder misin?" diye sordu Hayri. Yumak kuyruğunu salladı ve yeri kokladı. Hemen çalıların arasına koştu. Biraz sonra şapkayı ağzında getirdi. Hayri şapkayı silkeledi ve başına taktı. Sonra kütüğe döndü ve ekmeğini mutlu mutlu bitirdi. "Teşekkürler, Yumak, şapkamı sen buldun!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkayı çalıların arasına uzaklaştırdı"
   - Cümle 0 (plan satırı): «rüzgar şapkayı çalıların arasına uzaklaştırdı | köpekten yardım istedi ve köpek şapkayı buldu»
   - Açıklama: Rüzgar şapkayı 'uzaklaştırmaz', uçurur; fiil bu kullanıma uymuyor.
   - Açıklama: 'Uzaklaştırmak' bir yere varışla kullanılmaz; 'çalıların arasına uçurdu' olmalı.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Hayri bu şapkayı baklava dükkanında çalışırken hep takardı"
   - Cümle 5: «Hayri bu şapkayı baklava dükkanında çalışırken hep takardı.»
   - Açıklama: Kartın özellikler ve kimlik alanlarında Hayri'nin dükkanda hep taktığı bir şapka yok; diziye ait olmayan bir bilgi uyduruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0197` birebir aynı, ardından `@onarim: 268b33267be51a1364de9e335f52736a1753a6ac`, sonra gövde.

### Hikâye 7: tohum hayri-0198 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0198
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'düğme', fiil 'dağıtmak', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga kumdaki kabukları dağıttı | kumdan yüksek bir duvar yapıp kabukları içine dizdi
@tohum: hayri-0198
Rüzgar hafif hafif esiyordu. Hayri kıyıda düğme gibi küçük kabuklar fark etti. Onları kuma baklava gibi dizdi ama bir dalga hepsini dağıttı. Hayri kabukları boyalı kovasına yeniden topladı. Sonra dükkandaki baklava tepsisini düşündü. Tepsinin yüksek kenarı şerbeti hep içeride tutardı. Hayri kovayla ıslak kum taşıdı ve yüksek bir kum duvarı yaptı. Kabukları duvarın içine tek tek dizdi. Küçük bir dalga daha geldi. Dalga duvara çarptı ve geri çekildi. Kabuklar yerinden hiç oynamadı. Hayri kabuk tepsisini bitirdi ve yeni kabuklar toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Onları kuma baklava gibi dizdi"
   - Cümle 3: «Onları kuma baklava gibi dizdi ama bir dalga hepsini dağıttı.»
   - Açıklama: 'Baklava gibi dizmek' desen anlatan bir benzetme; küçük çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Tepsinin yüksek kenarı şerbeti"
   - Cümle 6: «Tepsinin yüksek kenarı şerbeti hep içeride tutardı.»
   - Açıklama: Baklava tepsisi ve şerbet benzetmesi soyut bir karşılaştırma ve 'şerbet' 3 yaşındaki çocuğun bilmeyebileceği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri kabuk tepsisini bitirdi"
   - Cümle 12: «Hayri kabuk tepsisini bitirdi ve yeni kabuklar toplamaya mutlu mutlu devam etti.»
   - Açıklama: Kum duvarına 'kabuk tepsisi' demek küçük çocuğa uygun olmayan bir mecaz.
   - Açıklama: Kum duvarına 'kabuk tepsisi' demek mecazlı bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0198` birebir aynı, ardından `@onarim: 3cf0adb7e7dab7e75e2936721a7e217c451cc095`, sonra gövde.

### Hikâye 8: tohum hayri-0199 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0199
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'papatya', fiil 'dinlemek', sıfat 'sulu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: iki eli dolu olduğu için kapıyı açamadı | arkadaşından kapıyı açmasını istedi
@tohum: hayri-0199
Bahçede papatyalar açmıştı. Hayri, Kamil'e dükkandan bir tepsi sulu baklava getirdi. Ama bahçenin kapısı kapalıydı ve Hayri'nin iki eli de doluydu. Kamil içeride bir bankta kitap okuyordu. Hayri tepsiyi tek elle tutmayı düşündü. Ama dükkanda tepsiyi hep iki elle taşırdı. "Kamil, kapıyı açar mısın?" diye seslendi Hayri. Kamil kitabını bıraktı ve Hayri'yi dinledi. Sonra koşup kapıyı açtı. Hayri tepsiyi dikkatle bankın üstüne koydu. Hiçbir baklava yere düşmemişti. İkisi papatyaların yanına oturdu. "Teşekkürler, Kamil, şimdi baklavaları birlikte yiyelim!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dükkandan bir tepsi sulu baklava getirdi"
   - Cümle 2: «Hayri, Kamil'e dükkandan bir tepsi sulu baklava getirdi.»
   - Açıklama: Hayri henüz kapıdan giremediği için 'getirdi' yanlış; 'getiriyordu' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "dükkandan bir tepsi sulu baklava getirdi"
   - Cümle 2: «Hayri, Kamil'e dükkandan bir tepsi sulu baklava getirdi.»
   - Açıklama: Hayri henüz varmadığı için bitmiş 'getirdi' yerine 'getiriyordu' olmalı; zaman kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0199` birebir aynı, ardından `@onarim: 570f76c5facabca0f4aa932a94e7bc3f9bc7c16e`, sonra gövde.

### Hikâye 9: tohum hayri-0200 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0200
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'bulmaca', fiil 'şaşırtmak', sıfat 'bol'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: rüzgar kutunun yerini gösteren kağıdı denize uçurdu | acıkınca kokuyu takip edip kutuyu kumda buldu
@tohum: hayri-0200
Güneş parlıyordu. Basri Amca, Hayri için kuma bir kutu saklamıştı. Ama birden bir rüzgar, kutunun yerini gösteren bulmacayı Hayri'nin elinden kaptı. Kağıt denize düştü ve dalgaların arasında kayboldu. Hayri kutunun yerini artık bilmiyordu. Tam o sırada Hayri acıktı ve burnuna güzel bir koku geldi. Koku, büyük bir kayanın yanındaki kumdan geliyordu. Hayri oraya koştu ve kumu elleriyle kazdı. Kumun altından kutu çıktı ve içinde bol çikolatalı kurabiyeler vardı. Hayri kutuyu çok çabuk buldu ve Basri Amca'yı çok şaşırttı. Basri Amca çok güldü. İkisi kayanın yanına oturup kurabiyeleri paylaştı. Hayri çok sevindi, çünkü acıkınca kutuyu burnuyla bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gösteren bulmacayı Hayri'nin elinden"
   - Cümle 3: «Ama birden bir rüzgar, kutunun yerini gösteren bulmacayı Hayri'nin elinden kaptı.»
   - Açıklama: Yeri gösteren kağıt bulmaca değil; plan ve sonraki cümle 'kağıt' diyor, kelime yanlış anlamda.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı ve burnuna güzel bir koku geldi"
   - Cümle 6: «Tam o sırada Hayri acıktı ve burnuna güzel bir koku geldi.»
   - Açıklama: Çözüm tesadüfen gelen bir kokuyla sebepsizce getiriliyor; kumun altındaki kutudan koku gelmesi de akla yatkın değil.
   - Açıklama: Çözüm tesadüfen beliren bir kokuyla sebepsizce geliyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çok çabuk buldu ve Basri Amca'yı çok şaşırttı"
   - Cümle 10: «Hayri kutuyu çok çabuk buldu ve Basri Amca'yı çok şaşırttı.»
   - Açıklama: 'çok' kelimesi art arda cümlelerde gereksiz tekrarlanıyor.
   - Açıklama: 'Çok' art arda cümlelerde gereksiz yere tekrarlanıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "acıkınca kutuyu burnuyla bulmuştu"
   - Cümle 13: «Hayri çok sevindi, çünkü acıkınca kutuyu burnuyla bulmuştu.»
   - Açıklama: Özellikler alanındaki acıkma, kumun altındaki kutuyu koklayarak bulma yeteneğine çevrilip iki kez anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0200` birebir aynı, ardından `@onarim: d27b1bf952b708357857cb662d47b50f93336f48`, sonra gövde.

### Hikâye 10: tohum hayri-0201 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0201
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'biber', fiil 'görüşmek', sıfat 'hareketli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: açtığı ilk ceviz boş çıktı | cevizleri eliyle tarttı ve ağır olanları topladı
@tohum: hayri-0201
@degisim: görüşmek -> tartmak
Rüzgar ağaçların arasında yavaşça esiyordu. Hayri kamp yerinde yere düşmüş cevizleri fark etti ve toplamaya başladı. Ama açtığı ilk ceviz boş çıktı. Hareketli Yumak kuyruğunu sallayarak yaprakları eşeledi. Biber gibi kırmızı yaprakların altından yeni cevizler çıktı. Hayri bu kez her birini açmak istemedi. Hayri'nin çalıştığı baklava dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi. Hayri cevizleri tek tek eline aldı ve tarttı. Ağır olanları çantasına koydu, hafif olanları yere bıraktı. Yumak da bulduğu her cevizi burnuyla Hayri'ye itti. Sonunda çanta doldu. Hayri çantayı sırtına aldı ve Yumak ile sevinçle koşup oynadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama açtığı ilk ceviz boş çıktı"
   - Cümle 3: «Ama açtığı ilk ceviz boş çıktı.»
   - Açıklama: Cevizin neden boş çıktığı söylenmiyor ve bu sorun zayıf, çocuğun önemseyeceği açık bir sorun kurulmuyor.
   - Açıklama: Sorunun sebebi söylenmiyor; tek bir boş ceviz çocuğun önemseyeceği açık bir sorun olarak kurulmuyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi"
   - Cümle 7: «Hayri'nin çalıştığı baklava dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi.»
   - Açıklama: Cümle bozuk kurulmuş; dükkanda cevizin ağır gelmesi anlamsız bir yapı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "baklava dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi"
   - Cümle 7: «Hayri'nin çalıştığı baklava dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi.»
   - Açıklama: Cevizin ağır ya da hafif gelmesi dükkana bağlanmış; 'gelirdi' fiili bu cümlede anlamca yerine oturmuyor.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "boş ceviz hafif gelirdi"
   - Cümle 7: «Hayri'nin çalıştığı baklava dükkanında dolu ceviz ağır, boş ceviz hafif gelirdi.»
   - Açıklama: Anlatım -dı'lı geçmişten -irdi'li geniş zamanın hikayesine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0201` birebir aynı, `@degisim: görüşmek -> tartmak` (tutuyorsan), ardından `@onarim: 8192c3692af275f689fee0202dd4780f14315c08`, sonra gövde.

### Hikâye 11: tohum hayri-0202 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0202
- yer: park (Mahallenin çocuk parkı.)
- tema: yağmur ya da kar günü
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kraker', fiil 'döndürmek', sıfat 'rengarenk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: yağmurda uzun tepsi dar kapıdan geçmedi | tepsiyi yan döndürdü ve içeri soktu
@tohum: hayri-0202
Bir sabah Hayri ile Mert parktaki bankta oturuyordu. Hayri dükkandan uzun bir tepsi baklava, Mert de kraker getirmişti. Birden yağmur yağdı ve baklavalar ıslanmaya başladı. Mert rengarenk şemsiyesini hemen baklavaların üstüne tuttu. "Hayri, oyun evine koşalım!" dedi Mert. Ama uzun tepsi oyun evinin dar kapısından geçmedi. Hayri dükkanda tepsiyi kapıdan nasıl geçirdiğini hatırladı. Tepsiyi yan döndürdü ve kısa kenarını önce kapıya soktu. Tepsi rahatça içeri girdi. Mert de şemsiyesini kapatıp arkasından girdi. "Hepsi kurtuldu, Hayri!" dedi Mert. İkisi yağmuru izleyerek baklava ile kraker yedi. Mert bundan sonra uzun şeyleri dar kapıdan Hayri gibi yan çevirip geçirdi.
```

**Hakem bulguları (4):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "baklavalar ıslanmaya başladı"
   - Cümle 3: «Birden yağmur yağdı ve baklavalar ıslanmaya başladı.»
   - Açıklama: Önce baklavaların ıslanması sorunu Mert'in şemsiyesiyle çözülüyor, sonra tepsinin kapıdan geçmemesi ikinci bir sorun olarak geliyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Birden yağmur yağdı ve baklavalar ıslanmaya başladı"
   - Cümle 3: «Birden yağmur yağdı ve baklavalar ıslanmaya başladı.»
   - Açıklama: Önce baklavaların ıslanması, sonra tepsinin kapıdan geçmemesi olmak üzere iki ayrı sorun var.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "uzun tepsi oyun evinin dar kapısından geçmedi"
   - Cümle 6: «Ama uzun tepsi oyun evinin dar kapısından geçmedi.»
   - Açıklama: Plandaki asıl sorun ilk 3 cümlede değil ancak 6. cümlede ortaya çıkıyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama uzun tepsi oyun evinin dar kapısından geçmedi"
   - Cümle 6: «Ama uzun tepsi oyun evinin dar kapısından geçmedi.»
   - Açıklama: Plandaki sorun (tepsinin kapıdan geçmemesi) ilk 3 cümlede değil, 6. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0202` birebir aynı, ardından `@onarim: fa9cd6a9fbfaf43a93048ba76a2ffe3f151b618a`, sonra gövde.

### Hikâye 12: tohum hayri-0203 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0203
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kupa', fiil 'güvenmek', sıfat 'hevesli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kum kuru olduğu için duvarlar yıkılıyordu | kupayla kuma su döktü ve kule yaptı
@tohum: hayri-0203
Hayri ile Basri Amca deniz kıyısında oturuyordu. Basri Amca kumdan bir kale yapmaya çok hevesliydi. Ama kum çok kuruydu ve duvarlar hemen yıkılıyordu. "Bu kum hiç durmuyor!" dedi Basri Amca. Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı. "Amca, kuma biraz su dökelim, o zaman sıkı durur," dedi Hayri. Basri Amca ona güvendi ve çantasından bir kupa çıkarıp verdi. Hayri kupayı sığ sudan doldurdu ve kuma döktü. Sonra ıslak kumu kupaya bastırdı ve kupayı ters çevirdi. Kumdan düzgün bir kule çıktı. Basri Amca güldü ve bir kule daha yaptı. Hayri ile Basri Amca kaleyi bitirince sevinçle el çırptı.
```

**Hakem bulguları (7):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kale yapmaya çok hevesliydi"
   - Cümle 2: «Basri Amca kumdan bir kale yapmaya çok hevesliydi.»
   - Açıklama: 'Hevesli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kum hiç durmuyor!"
   - Cümle 4: «"Bu kum hiç durmuyor!" dedi Basri Amca.»
   - Açıklama: Kum için 'durmuyor' fiili kastedilen anlamı (şeklini korumuyor) doğru vermiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı"
   - Cümle 5: «Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı.»
   - Açıklama: İki bağımsız cümle virgülle bağlanmış ve düşünce ile anlatım arasındaki ilişki kurulamamış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı"
   - Cümle 5: «Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı.»
   - Açıklama: Baklava benzetmesiyle kurulan soyut akıl yürütme 3 yaşındaki bir çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şekerli su onu hep sıkı tutardı"
   - Cümle 5: «Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı.»
   - Açıklama: Baklavadaki şerbetle kum arasında kurulan benzetme küçük çocuk için soyut.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "şekerli su onu hep sıkı tutardı"
   - Cümle 5: «Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı.»
   - Açıklama: 'onu' zamirinin baklavayı mı başka bir şeyi mi gösterdiği belli değil.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şekerli su onu hep sıkı tutardı"
   - Cümle 5: «Hayri dükkandaki baklavayı düşündü, şekerli su onu hep sıkı tutardı.»
   - Açıklama: Çözüm fikri baklava şerbetinden sebepsiz ve akla yatkın olmayan bir benzetmeyle geliyor.
   - Açıklama: Baklavadaki şerbetten ıslak kum fikrine sıçrama akla yatkın değil; çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0203` birebir aynı, ardından `@onarim: 3dc30d8a6ead8fee2c56397d2d20f56fc683ee77`, sonra gövde.
