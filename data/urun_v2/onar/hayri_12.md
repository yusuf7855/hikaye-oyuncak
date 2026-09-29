# Editör görevi (onarım): Hayri, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0025
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kalıp', fiil 'guruldamak', sıfat 'yeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: arkadaşının kalıbı yoktu ve kuleleri yıkılıyordu | kalıbını paylaştı ve birlikte kule yaptılar
@tohum: hayri-0025
@degisim: guruldamak -> doldurmak
Hayri'nin yeşil bir kalıbı vardı ve kumdan kuleler yapıyordu. Mert de kıyıda elleriyle kum topluyordu. Ama Mert'in kuleleri hep yıkılıyordu. "Mert, kalıbı birlikte kullanalım mı?" diye sordu Hayri. Mert sevindi ve başını salladı. Hayri kalıbı ıslak kumla doldurdu ve Mert'e verdi. Mert kalıbı ters çevirdi ve yavaşça kaldırdı. Kumda düzgün bir kule duruyordu. "Mert, bu kule dünyanın en güzel kulesi!" dedi Hayri abartarak. Mert güldü ve bir kule daha yaptı. Hayri çok mutluydu, çünkü paylaşınca ikisi de kule yapmıştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Mert'in kuleleri hep yıkılıyordu"
   - Cümle 3: «Ama Mert'in kuleleri hep yıkılıyordu.»
   - Açıklama: Kulelerin neden yıkıldığı gövdede açıkça söylenmiyor, kalıbın olmaması yalnız ima ediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Mert, bu kule dünyanın en güzel kulesi!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Mert, bu kule dünyanın en güzel kulesi!" dedi Hayri abartarak.»
   - Açıklama: Tohumdaki abartma özelliği çözüme katkı vermiyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0025` birebir aynı, `@degisim: guruldamak -> doldurmak` (tutuyorsan), ardından `@onarim: 2dc2b3e5c3b7bae375fb8f6194fb1a9d04374501`, sonra gövde.

### Hikâye 2: tohum hayri-0028 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0028
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kova', fiil 'koklamak', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: yağmur damlaları tabaktaki tatlılara düştü | kovasını boşaltıp tabağın üstüne ters kapattı
@tohum: hayri-0028
Yağmur damlaları bahçede tıp tıp ses çıkarıyordu. Hayri yeni kovasıyla yağmur suyu topluyordu. Ama damlalar masadaki tabakta duran tatlılara da düşüyordu. Hayri baklava dükkanında tatlıların üstünü hep kapatırdı. Hemen kovadaki suyu çimene döktü. Kovayı ters çevirdi ve tabağın üstüne kapattı. Biraz sonra yağmur dindi. Hayri kovayı kaldırdı ve tatlıları kokladı. Tatlılar kuru kalmıştı ve çok güzel kokuyordu. Hayri bir dilim aldı ve afiyetle yedi. Sonra yeni kovasıyla bahçede mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tatlılar kuru kalmıştı"
   - Cümle 9: «Tatlılar kuru kalmıştı ve çok güzel kokuyordu.»
   - Açıklama: Damlalar tatlılara zaten düşmüşken tatlıların kuru kaldığı söyleniyor.
   - Açıklama: Damlalar kapatılmadan önce tatlılara düşmüştü, ama sonra tatlıların kuru kaldığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0028` birebir aynı, ardından `@onarim: 2b070bdd23b52cbed7e93ab96f915d385b510f12`, sonra gövde.

### Hikâye 3: tohum hayri-0029 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0029
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fener', fiil 'gezinmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: fener yumuşak yastıktan kaydı ve ışık tavana gitti | feneri çantanın üstüne dik koydu
@tohum: hayri-0029
Bir sabah erkenden ormandaki kamp yeri karanlıktı. Hayri çadırında fenerini açtı ve gölge oyunu oynamak istedi. Ama fener yumuşak yastığın üstünde durmadı ve yana kaydı. Işık yalnız tavana vurdu ve duvar karanlık kaldı. Hayri baklava dükkanında tepsileri hep düz ve sert yere koyardı. Bu yüzden feneri çantasının düz üstüne dik koydu. Işık bu kez duvara düştü. Hayri elleriyle duvara garip şekiller yaptı. Gölgeler duvarda bir o yana bir bu yana gezindi. Hayri çok sevindi, çünkü gölge oyununu sonunda oynamıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve ışık tavana gitti"
   - Cümle 0 (plan satırı): «fener yumuşak yastıktan kaydı ve ışık tavana gitti | feneri çantanın üstüne dik koydu»
   - Açıklama: Işık bir yere gitmez; 'tavana vurdu' olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "feneri çantasının düz üstüne dik koydu"
   - Cümle 6: «Bu yüzden feneri çantasının düz üstüne dik koydu.»
   - Açıklama: Fener yana kayınca ışığın tavana gitmesi, dik konunca duvara düşmesi fiziksel olarak ters ve çelişkili.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elleriyle duvara garip şekiller yaptı"
   - Cümle 8: «Hayri elleriyle duvara garip şekiller yaptı.»
   - Açıklama: Duvara şekil yapılmıyor, ellerle gölge şekilleri yapılıyor; fiil yanlış yeri gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0029` birebir aynı, ardından `@onarim: a72a589ab160164aacf63aa3c7504abe705ac5cd`, sonra gövde.

### Hikâye 4: tohum hayri-0032 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0032
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'etiket', fiil 'okşamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: toprak yumuşaktı ve fidan yana yattı | toprak isteyip ekledi ve iki eliyle sıkıca bastı
@tohum: hayri-0032
Bir sabah Hayri, Basri Amca'yla parkta ilk kez fidan dikmeyi denedi. Basri Amca ona küçük, yemyeşil bir fidan verdi. Ama çukurdaki toprak yumuşaktı ve fidan hemen yana yattı. "Bu fidan en büyük ağaç olacak, çok toprak lazım!" dedi Hayri abartarak. Basri Amca güldü ve ona bir kova toprak verdi. Hayri bu toprağı çukura ekledi. Sonra toprağı iki eliyle sıkıca bastı. Fidan bu kez dimdik durdu. Hayri fidanın yapraklarını okşadı. Basri Amca bir etikete Hayri'nin adını yazdı ve fidana astı. Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 4: «"Bu fidan en büyük ağaç olacak, çok toprak lazım!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram, küçük çocuk bilmez.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "toprağı iki eliyle sıkıca bastı"
   - Cümle 7: «Sonra toprağı iki eliyle sıkıca bastı.»
   - Açıklama: 'Basmak' belirtme ekli nesne almaz; 'toprağı bastırdı' ya da 'toprağa bastı' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iki eliyle sıkıca bastı"
   - Cümle 7: «Sonra toprağı iki eliyle sıkıca bastı.»
   - Açıklama: Plan satırında da 'toprağı ... bastı' yapısı hatalı; 'bastırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0032` birebir aynı, ardından `@onarim: ec4b3924cca379ed8c8b8bba6c10c5dc92160b38`, sonra gövde.

### Hikâye 5: tohum hayri-0033 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0033
- yer: park (Mahallenin çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'şampuan', fiil 'indirmek', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: koşarken anahtar uzun çimenlere düştü | köpekten yardım istedi ve anahtarı buldu
@tohum: hayri-0033
@degisim: şampuan -> anahtar
Rüzgar hafif hafif esiyordu. Hayri parkta Yumak ile oynuyordu. Hayri koşarken cebindeki anahtar uzun çimenlere düştü. Hayri'nin eli de anahtarı da çalıştığı dükkandaki baklava gibi kokuyordu. Hayri yere eğildi ama anahtarı göremedi. Sonra elini yavaşça Yumak'ın burnuna indirdi. "Yumak, anahtarımı bulur musun?" diye sordu Hayri. Yumak onun elini kokladı ve burnunu yere eğdi. Çimenlerin arasında biraz ilerledi, sonra durup havladı. Heyecanlı Hayri hemen oraya koştu. Anahtar çimenlerin arasında parlıyordu. "Aferin sana, Yumak!" dedi Hayri ve anahtarı aldı. Anahtarı bu kez ceketinin iç cebine koydu. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "eli de anahtarı da çalıştığı dükkandaki baklava gibi kokuyordu"
   - Cümle 4: «Hayri'nin eli de anahtarı da çalıştığı dükkandaki baklava gibi kokuyordu.»
   - Açıklama: Baklava kokusu yalnız köpeğin anahtarı bulmasını sağlamak için sebepsizce araya sokulmuş bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0033` birebir aynı, `@degisim: şampuan -> anahtar` (tutuyorsan), ardından `@onarim: 95157f27cda267e95abe18825949710f98dbcd4d`, sonra gövde.

### Hikâye 6: tohum hayri-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0034
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'sabahlık', fiil 'bulmak', sıfat 'ufak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: arkadaşı yemeğe gelmedi ve çitten bir ses geldi | sesin geldiği yere gidip uyuyan arkadaşını buldu
@tohum: hayri-0034
Evin bahçesinde, masada iki tabak börek duruyordu. Hayri çok acıkmıştı ve Kamil'i bekliyordu. Ama Kamil daha gelmemişti. Birden çitin arkasından ufak bir ses geldi. Hayri bu sesi çok merak etti ve çite doğru yürüdü. Sonra çitin üstünden baktı. Hayri, Kamil'i kendi bahçesinde sabahlığıyla uyurken buldu. "Kamil, uyan, börekler soğuyor!" dedi Hayri. Kamil gözlerini açtı ve güldü. "Beni mi bekliyordun, Hayri?" diye sordu Kamil. "Evet, kahvaltıyı seninle yapmak istedim," dedi Hayri. Kamil hemen Hayri'nin bahçesine geldi. "Teşekkürler, Hayri, hadi birlikte yiyelim!" dedi Kamil.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden çitin arkasından ufak bir ses geldi"
   - Cümle 4: «Birden çitin arkasından ufak bir ses geldi.»
   - Açıklama: Sesin neden geldiği hiç açıklanmıyor; uyuyan Kamil'le bağlantısı kurulmuyor.
   - Açıklama: Sesin kaynağı hiç açıklanmıyor; uyuyan Kamil'in sesi neden çıkardığı belirsiz.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kamil'i kendi bahçesinde sabahlığıyla"
   - Cümle 7: «Hayri, Kamil'i kendi bahçesinde sabahlığıyla uyurken buldu.»
   - Açıklama: 'Kendi' dilbilgisel olarak özne Hayri'yi gösteriyor, kimin bahçesi olduğu belirsiz.
   - Açıklama: 'Kendi' zamirinin Hayri'yi mi Kamil'i mi gösterdiği belli değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kamil'i kendi bahçesinde sabahlığıyla uyurken buldu"
   - Cümle 7: «Hayri, Kamil'i kendi bahçesinde sabahlığıyla uyurken buldu.»
   - Açıklama: Kamil'in bahçede sabahlıkla uyuması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0034` birebir aynı, ardından `@onarim: 6e09b7b26927a476afec3f964f3a5182dc7a67e1`, sonra gövde.

### Hikâye 7: tohum hayri-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0035
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çimen', fiil 'konuşmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: oynak top düz tahtadan zıplayıp düştü | kenarı yüksek boş bir tepsi kullandı
@tohum: hayri-0035
@degisim: konuşmak -> zıplamak
Evin bahçesinde güneşli bir gündü. Hayri topu düz bir tahtanın üstünde çimenin öbür ucuna taşımak istiyordu. Ama top çok oynaktı ve Hayri yürürken tahtadan zıplayıp düştü. Hayri durdu ve düşündü. Hayri baklava dükkanında çalışıyordu ve orada hep tepsi taşıyordu. Tepsinin yüksek kenarı baklavaları tutuyordu. Hayri hemen eve koştu ve boş bir tepsi getirdi. Hayri topu tepsiye koydu. Tepsiyi iki eliyle tuttu ve yavaş yavaş yürüdü. Top kenara çarptı ama yere düşmedi. Sonunda Hayri çimenin sonuna vardı. Hayri çok sevindi, çünkü topu düşürmeden bahçeyi geçmişti.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hayri topu düz bir tahtanın üstünde çimenin öbür ucuna taşımak istiyordu"
   - Cümle 2: «Hayri topu düz bir tahtanın üstünde çimenin öbür ucuna taşımak istiyordu.»
   - Açıklama: Topu elde değil de düz bir tahtayla taşıma hedefi sebepsiz ve yapay, sorun bu yüzden akla yatkın değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama top çok oynaktı"
   - Cümle 3: «Ama top çok oynaktı ve Hayri yürürken tahtadan zıplayıp düştü.»
   - Açıklama: 'Oynak' kelimesi topun zıplamasını anlatmak için uygun anlamda kullanılmamış.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hayri yürürken tahtadan zıplayıp düştü"
   - Cümle 3: «Ama top çok oynaktı ve Hayri yürürken tahtadan zıplayıp düştü.»
   - Açıklama: Cümlede düşenin top mu Hayri mi olduğu belli değil.
   - Açıklama: Tahtadan zıplayıp düşenin top mu Hayri mi olduğu belli değil.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri durdu ve düşündü. Hayri baklava"
   - Cümle 4: «Hayri durdu ve düşündü.»
   - Açıklama: Hayri adı ardışık cümlelerde gereksiz yere tekrar ediliyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonunda Hayri çimenin sonuna vardı"
   - Cümle 11: «Sonunda Hayri çimenin sonuna vardı.»
   - Açıklama: 'Sonunda' ve 'sonuna' aynı cümlede gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0035` birebir aynı, `@degisim: konuşmak -> zıplamak` (tutuyorsan), ardından `@onarim: c35b83ddeaa1c0e15f2e901b3da9673fde12a41e`, sonra gövde.

### Hikâye 8: tohum hayri-0036 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0036
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'şişe', fiil 'doğmak', sıfat 'temiz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: tek top vardı ve ikisi de önce atmak istedi | sırayı arkadaşına verdi ve beklerken simidini yedi
@tohum: hayri-0036
Deniz kıyısında güneş yeni doğmuştu ve Hayri çok acıkmıştı. Hayri ile Mert kuma beş temiz plastik şişe dizdi. Ama tek top vardı ve ikisi de önce atmak istedi. İkisi de topu aynı anda tuttu ve çekti. Hayri biraz düşündü. "Önce sen at, Mert, ben de beklerken simidimi yerim," dedi Hayri. Mert topu attı ve üç şişe devrildi. Sonra sıra Hayri'ye geldi. Hayri simidini bitirdi ve topu attı. Kalan iki şişe de devrildi. Hayri ile Mert çok sevindi, çünkü ikisi de sırayla topu atmıştı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hayri çok acıkmıştı"
   - Cümle 1: «Deniz kıyısında güneş yeni doğmuştu ve Hayri çok acıkmıştı.»
   - Açıklama: Top sırası sorununun yanında ayrıca Hayri'nin açlığı ikinci bir sorun olarak kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0036` birebir aynı, ardından `@onarim: e446f2e40f8284a0b6fb548dbe631ad8a9fabba1`, sonra gövde.

### Hikâye 9: tohum hayri-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0037
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'topaç', fiil 'tasarlamak', sıfat 'gururlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: yumuşak toprakta topaç hemen devrildi | düz ve sert bir taşın üstünde topacı çevirdi
@tohum: hayri-0037
@degisim: tasarlamak -> çevirmek
Ağaçların arasında kuşlar ötüyordu. Hayri kamp yerinde tahta topacını çevirdi. Ama toprak yumuşaktı ve topaç hemen devrildi. Hayri topacı iki kez daha çevirdi ama topaç yine toprağa battı. Hayri biraz düşündü. Hayri baklava dükkanında tepsileri hep düz ve sert masaya koyardı. Hayri etrafına baktı ve yerde büyük, düz bir taş gördü. Hayri topacı taşın üstünde çevirdi. Topaç bu kez uzun uzun döndü. Hayri topaç dönerken bir, iki, üç, dört, beş diye saydı. Hayri çok gururluydu, çünkü topacını düşürmeden döndürmüştü.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri etrafına baktı"
   - Cümle 7: «Hayri etrafına baktı ve yerde büyük, düz bir taş gördü.»
   - Açıklama: Yedi cümle üst üste 'Hayri' ile başlıyor; ad gereksiz tekrarlanıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri topacı taşın üstünde çevirdi"
   - Cümle 8: «Hayri topacı taşın üstünde çevirdi.»
   - Açıklama: Art arda sekiz cümle 'Hayri' adıyla başlıyor; gereksiz tekrar.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri çok gururluydu, çünkü"
   - Cümle 11: «Hayri çok gururluydu, çünkü topacını düşürmeden döndürmüştü.»
   - Açıklama: 'Gururlu' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri çok gururluydu"
   - Cümle 11: «Hayri çok gururluydu, çünkü topacını düşürmeden döndürmüştü.»
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0037` birebir aynı, `@degisim: tasarlamak -> çevirmek` (tutuyorsan), ardından `@onarim: 9eaa21fc713e621d497e1eafcc8cb0b9194164e3`, sonra gövde.

### Hikâye 10: tohum hayri-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0038
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kilit', fiil 'yalamak', sıfat 'elmalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: tek salıncak vardı ve ikisi de önce binmek istedi | dükkandaki sırayı hatırladı ve sırayla binmeyi söyledi
@tohum: hayri-0038
@degisim: kilit -> salıncak
Parkta tek bir salıncak vardı. Hayri ile Mert aynı anda salıncağa koştu. İkisi de salıncağın zincirini tuttu ve önce binmek istedi. Mert'in elinde elmalı bir lolipop vardı. Hayri biraz düşündü. Hayri'nin çalıştığı baklava dükkanında müşteriler hep sırayla beklerdi. "Mert, gel, sırayla binelim," dedi Hayri. "Tamam, önce sen bin, ben de lolipopumu yalarım," dedi Mert. Hayri salıncağa bindi ve on kez sallandı. Mert o sırada bir, iki, üç diye saydı. Sonra Hayri indi ve Mert salıncağa bindi. Bu kez Hayri yüksek sesle saydı. Hayri ile Mert çok sevindi, çünkü sırayla ikisi de salıncağa binmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elinde elmalı bir lolipop"
   - Cümle 4: «Mert'in elinde elmalı bir lolipop vardı.»
   - Açıklama: Lolipop sebepsiz beliriyor ve salıncak sorununun gidişinde işlevsiz bir ayrıntı olarak kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mert'in elinde elmalı bir lolipop vardı"
   - Cümle 4: «Mert'in elinde elmalı bir lolipop vardı.»
   - Açıklama: Lolipop sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0038` birebir aynı, `@degisim: kilit -> salıncak` (tutuyorsan), ardından `@onarim: 0e27786a43b10f20be55908c76493fce3ae9167d`, sonra gövde.

### Hikâye 11: tohum hayri-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0039
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'teyp', fiil 'bağlamak', sıfat 'kuru'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: rüzgar esti ve radyo havlunun altında kayboldu | havluları tek tek kaldırıp radyoyu buldu
@tohum: hayri-0039
@degisim: teyp -> radyo
Hayri deniz kıyısında Basri Amca ile oturuyordu. Birden sert bir rüzgar esti ve havlular kumda uçuştu. Rüzgar durunca Basri Amca radyosunu göremedi. "Radyo nerede, az önce buradaydı!" dedi Basri Amca. Hayri çok acıkmıştı ama önce radyoyu aramak istedi. Kumdaki havluları tek tek kaldırdı. Kuru bir havlunun altında radyoyu gördü. "Basri Amca, radyo burada!" dedi Hayri. Hayri havluyu yine uçmasın diye çantanın sapına sıkıca bağladı. Basri Amca radyoyu aldı ve gülümsedi. "Teşekkür ederim, Hayri, gel, birlikte simit yiyelim!" dedi Basri Amca.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantanın sapına sıkıca bağladı"
   - Cümle 9: «Hayri havluyu yine uçmasın diye çantanın sapına sıkıca bağladı.»
   - Açıklama: Havluyu çantaya bağlama adımı sorunun çözümüne katkısı olmayan fazladan bir olay.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Teşekkür ederim, Hayri, gel, birlikte simit yiyelim!"
   - Cümle 11: «"Teşekkür ederim, Hayri, gel, birlikte simit yiyelim!" dedi Basri Amca.»
   - Açıklama: İki ayrı cümle virgülle birleştirilmiş; noktalama yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0039` birebir aynı, `@degisim: teyp -> radyo` (tutuyorsan), ardından `@onarim: acea6d25a813910d961e7da95372e9ba51c1b6e5`, sonra gövde.

### Hikâye 12: tohum hayri-0041 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0041
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'oyuncak', fiil 'büyütmek', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kumdan pasta kuru kum yüzünden hep dağıldı | kovayla ıslak kum getirip pastayı büyüttü
@tohum: hayri-0041
Hayri deniz kıyısında kumdan pasta yapma oyunu oynuyordu. Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi. Kum kuruydu ve pasta hemen dağıldı. Hayri oyuncak kovasını aldı ve su kenarına yürüdü. Kovayı ıslak kumla doldurdu ve geri döndü. Islak kumu kuru kuma karıştırdı ve pastayı büyüttü. Bu kez pasta sağlam durdu ve hiç dağılmadı. Hayri pastanın üstüne beyaz kabuklar dizdi. Sonra kocaman pastanın yanına oturdu. Hayri pastasına mutlu mutlu baktı ve oyununa devam etti.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "en sevdiği limonlu pastayı kumdan yapmak istedi"
   - Cümle 2: «Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi.»
   - Açıklama: Hayri zaten kumdan pasta yapıyordu; ikinci cümle aynı bilgiyi gereksizce tekrar ediyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "pastayı kumdan yapmak istedi"
   - Cümle 2: «Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi.»
   - Açıklama: Pastanın kumdan olduğu ilk cümlede söylenmişken ikinci cümlede gereksiz yere tekrarlanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı ve en sevdiği"
   - Cümle 2: «Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor; güvenli kullanım satırındaki paylaşma, bekleme ya da hazırlama olarak kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı ve en sevdiği limonlu pastayı"
   - Cümle 2: «Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi.»
   - Açıklama: Hayri'nin acıkması kurulup hiç kullanılmıyor; kumdan pasta açlığa bir şey yapmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı ve en sevdiği"
   - Cümle 2: «Çok acıkmıştı ve en sevdiği limonlu pastayı kumdan yapmak istedi.»
   - Açıklama: Hayri'nin acıkması kuruluyor ama hikayede hiçbir işe yaramıyor ve karşılanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0041` birebir aynı, ardından `@onarim: 7bf98cf8e3ead2bf6d1893a2ac84a8ecf04c0988`, sonra gövde.
