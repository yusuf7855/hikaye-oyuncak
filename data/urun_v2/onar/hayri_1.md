# Editör görevi (onarım): Hayri, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0001 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0001
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'lamba', fiil 'zıplamak', sıfat 'neşeli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: ikisi aynı anda zıplayınca kazanan belli olmadı | sırayla zıplayıp yerleri çizgiyle gösterdiler
@tohum: hayri-0001
Hafif bir rüzgar esiyordu. Hayri ile Mert deniz kenarında lambanın yanından zıplıyordu. Ama ikisi hep aynı anda zıplıyordu ve kazanan belli olmuyordu. "Dükkanda baklavayı sırayla veririz, burada da öyle yapalım," dedi Hayri. "Tamam, önce sen zıpla," dedi Mert neşeli bir sesle. Hayri zıpladı ve Mert onun ayağının yanına bir çizgi çizdi. Sonra Mert zıpladı ve Hayri de bir çizgi çizdi. Mert'in çizgisi biraz daha uzaktaydı. İkisi de güldü ve bir kez daha oynadı. Hayri ile Mert çok sevindi, çünkü artık kazananı görebiliyorlardı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "lambanın yanından zıplıyordu"
   - Cümle 2: «Hayri ile Mert deniz kenarında lambanın yanından zıplıyordu.»
   - Açıklama: Yerde zıplama için ayrılma eki yanlış; 'lambanın yanında zıplıyordu' olmalı.
   - Açıklama: Hal eki yanlış; yerinde zıplama için 'lambanın yanında' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "deniz kenarında lambanın yanından zıplıyordu"
   - Cümle 2: «Hayri ile Mert deniz kenarında lambanın yanından zıplıyordu.»
   - Açıklama: Lamba sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi hep aynı anda zıplıyordu ve kazanan belli olmuyordu"
   - Cümle 3: «Ama ikisi hep aynı anda zıplıyordu ve kazanan belli olmuyordu.»
   - Açıklama: Aynı anda zıplamak kimin daha uzağa düştüğünü görmeyi engellemez; sorunun sebebi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0001` birebir aynı, ardından `@onarim: 3658691004fd9fa944c4059403eb6e8388c92b13`, sonra gövde.

### Hikâye 2: tohum hayri-0002 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0002
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'lokma', fiil 'tamamlanmak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: çok acıktı ama yalnız bir sandviç vardı | sandviçi ikiye bölüp yarısını amcaya verdi
@tohum: hayri-0002
@degisim: işaretli -> peynirli
Bir sabah Hayri deniz kıyısında Basri Amca ile kumdan kale yapıyordu. Kale sonunda tamamlandı ve Hayri çok acıktı. Ama tek bir peynirli sandviç vardı ve Basri Amca'nın yiyeceği yoktu. Hayri sandviçi eline aldı ve biraz düşündü. Sonra sandviçi tam ortasından ikiye böldü. Parçalardan birini Basri Amca'ya uzattı. Basri Amca önce şaşırdı, sonra gülümsedi. İkisi kalenin yanına yan yana oturdu. Hayri her lokmayı yavaş yavaş yedi. Basri Amca da kendi parçasını bitirdi. Karınları doyunca ikisi kumda yeni bir kale yapmaya mutlu mutlu başladı.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama tek bir peynirli sandviç vardı"
   - Cümle 3: «Ama tek bir peynirli sandviç vardı ve Basri Amca'nın yiyeceği yoktu.»
   - Açıklama: Neden tek sandviç olduğu söylenmiyor ve Hayri'nin açlığı sorun olarak zayıf; yiyeceği varken sorun belirsiz kalıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Basri Amca'nın yiyeceği yoktu"
   - Cümle 3: «Ama tek bir peynirli sandviç vardı ve Basri Amca'nın yiyeceği yoktu.»
   - Açıklama: Basri Amca'nın neden yiyeceği olmadığı söylenmiyor; sorunun sebebi verilmiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri sandviçi eline aldı"
   - Cümle 4: «Hayri sandviçi eline aldı ve biraz düşündü.»
   - Açıklama: Yiyeceğin kaybolduğu söylendikten hemen sonra Hayri tek sandviçi elinde tutuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sandviçi tam ortasından ikiye böldü"
   - Cümle 5: «Sonra sandviçi tam ortasından ikiye böldü.»
   - Açıklama: Sandviçi bölmek Hayri'nin açlığına yönelmiyor, tersine yiyeceğini azaltıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kalenin yanına yan yana oturdu"
   - Cümle 8: «İkisi kalenin yanına yan yana oturdu.»
   - Açıklama: 'Yanına' ve 'yan yana' gereksiz tekrar oluşturuyor.
   - Açıklama: 'Yanına' ile 'yan yana' aynı cümlede gereksiz tekrar oluşturuyor.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kalenin yanına yan yana"
   - Cümle 8: «İkisi kalenin yanına yan yana oturdu.»
   - Açıklama: 'yanına' ile 'yan yana' art arda gelerek gereksiz tekrar yaratıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0002` birebir aynı, `@degisim: işaretli -> peynirli` (tutuyorsan), ardından `@onarim: c139ed238eae23cc080b2ce0b6d1c88d5dc41f08`, sonra gövde.

### Hikâye 3: tohum hayri-0003 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0003
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yün', fiil 'güzelleştirmek', sıfat 'saygılı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: rüzgar arkadaşının sandviçini kuma düşürdü | kendi sandviçini ikiye bölüp yarısını verdi
@tohum: hayri-0003
@degisim: güzelleştirmek -> bölmek
Deniz kıyısında Hayri ile Kamil yün bir örtünün üstünde oturuyordu. Birden sert bir rüzgar esti ve Kamil'in sandviçi kuma düştü. Sandviçin her yeri kum oldu. Kamil üzgün üzgün sandviçine baktı. Hayri de çok acıkmıştı ve elinde tek bir sandviç vardı. Ama Hayri sandviçini hemen ikiye böldü. "Kamil, bu yarısı senin," dedi Hayri. "Çok teşekkür ederim, Hayri," dedi Kamil saygılı bir sesle. Kamil kumlu sandviçi alıp çantasına koydu. Sonra ikisi örtünün üstünde yan yana oturup sandviçlerini yedi. Hayri çok sevindi, çünkü arkadaşı artık aç değildi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sandviçin her yeri kum oldu"
   - Cümle 3: «Sandviçin her yeri kum oldu.»
   - Açıklama: Sandviç kum olmaz; 'kumla kaplandı' ya da 'kumlandı' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kamil, bu yarısı senin"
   - Cümle 7: «"Kamil, bu yarısı senin," dedi Hayri.»
   - Açıklama: İşaret sıfatıyla iyelik eki birlikte kullanılmış; 'bu yarı senin' ya da 'yarısı senin' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0003` birebir aynı, `@degisim: güzelleştirmek -> bölmek` (tutuyorsan), ardından `@onarim: 5dd2b63c3fb0c8808634f222593c995f7dc61144`, sonra gövde.

### Hikâye 4: tohum hayri-0004 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0004
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fotoğraf', fiil 'sevinmek', sıfat 'ahşap'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: kutu kaybolunca köpeğe kızdı | kutuyu bankın arkasında bulup köpekten özür diledi
@tohum: hayri-0004
@degisim: fotoğraf -> kutu
Hayri parkta Yumak ile top oynuyordu. Çalıştığı baklava dükkanından getirdiği kutu ahşap bankın üstündeydi. Hayri bankın yanına döndü ama kutu yerinde yoktu. "Yumak, kutuyu sen mi aldın?" dedi Hayri kızgın bir sesle. Yumak kulaklarını indirdi ve bankın arkasına koştu. Orada durup havladı. Hayri bankın arkasına baktı ve kutuyu çimenlerin üstünde buldu. Kutu rüzgarla düşmüştü ve kapağı sıkıca kapalıydı. Hayri, Yumak'ın kutuyu almadığını anladı. "Özür dilerim, Yumak, kutuyu sen almadın," dedi Hayri. Sonra Yumak'ın başını okşadı. Yumak sevindi ve kuyruğunu salladı. Hayri kutuyu bankın üstüne geri koydu. Sonra Hayri ile Yumak top oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çalıştığı baklava dükkanından getirdiği kutu"
   - Cümle 2: «Çalıştığı baklava dükkanından getirdiği kutu ahşap bankın üstündeydi.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız kutunun kaynağı olarak anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Yumak kulaklarını indirdi ve bankın arkasına koştu"
   - Cümle 5: «Yumak kulaklarını indirdi ve bankın arkasına koştu.»
   - Açıklama: Kutunun yerini Hayri değil Yumak buluyor ve gösteriyor; sorunu yan karakter çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0004` birebir aynı, `@degisim: fotoğraf -> kutu` (tutuyorsan), ardından `@onarim: 9a1b1e81a8e8e4469db3ea3df3165cf9453525f4`, sonra gövde.

### Hikâye 5: tohum hayri-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0005
- yer: park (Mahallenin çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'bisiklet', fiil 'alışmak', sıfat 'şirin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: yemek kutusu bisiklet sepetine sıkıştı | arkadaşından yardım isteyip kutuyu düz çevirdi
@tohum: hayri-0005
Parkta Hayri yeni bisikletine alışmak için tur atıyordu. Bir süre sonra çok acıktı ve bisikletten indi. Ama yemek kutusu yan dönüp sepete sıkışmıştı. Hayri kutuyu çekti ama kutu yerinden oynamadı. O sırada Akın salıncaktan inip yanına geldi. "Akın, kutum çıkmıyor, bana yardım eder misin?" diye sordu Hayri. Akın sepete dikkatle baktı. "Kutuyu önce düz çevirmen lazım," dedi Akın. Akın sepeti tuttu, Hayri de kutuyu düz çevirdi. Kutu hemen sepetten çıktı. Hayri kutuyu açtı ve içinde iki şirin kurabiye buldu. "Teşekkürler, Akın, bu kurabiye senin!" dedi Hayri sevinçle.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kutuyu önce düz çevirmen lazım"
   - Cümle 8: «"Kutuyu önce düz çevirmen lazım," dedi Akın.»
   - Açıklama: Çözüm fikrini Hayri değil Akın buluyor; yan karakter yalnız yardım etmeli.
   - Açıklama: Çözüm fikrini Hayri değil Akın buluyor; yan karakter yardımın ötesine geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki şirin kurabiye"
   - Cümle 11: «Hayri kutuyu açtı ve içinde iki şirin kurabiye buldu.»
   - Açıklama: 'Şirin' kurabiye için uygun bir sıfat değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki şirin kurabiye buldu"
   - Cümle 11: «Hayri kutuyu açtı ve içinde iki şirin kurabiye buldu.»
   - Açıklama: 'Şirin' kurabiye için yerinde bir sıfat değil; kelime anlamına uygun kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0005` birebir aynı, ardından `@onarim: 609234fd3220ccd65c35df73ce710d2d3df478ef`, sonra gövde.

### Hikâye 6: tohum hayri-0006 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0006
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyon', fiil 'değişmek', sıfat 'pürüzsüz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: bulutun kamyon şekli rüzgarla değişiyordu | amcaya hemen gösterdi ve birlikte baktılar
@tohum: hayri-0006
Hayri parkta çimenlere uzanmış, bulutlara bakıyordu. Birden bir bulut tıpkı bir kamyona benziyordu. Ama rüzgar esiyordu ve bulutun şekli yavaş yavaş değişiyordu. Hayri bu bulutu hemen Basri Amca'ya göstermek istedi. Basri Amca yakındaki bankta oturuyordu. "Amca, gökyüzünde kocaman bir kamyon var, bütün mahalleyi taşır!" diye abarttı Hayri. Basri Amca merakla başını kaldırdı. "Gerçekten de bir kamyon, tekerlekleri bile var!" dedi Basri Amca. Az sonra kamyonun tekerlekleri kayboldu. Bulut şimdi pürüzsüz ve yuvarlak bir topa benziyordu. Basri Amca bu kez yüksek sesle güldü. "İyi ki kamyonu birlikte gördük, amca!" dedi Hayri.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Birden bir bulut tıpkı bir kamyona benziyordu"
   - Cümle 2: «Birden bir bulut tıpkı bir kamyona benziyordu.»
   - Açıklama: 'Birden' ani bir olay ister, sürerlik bildiren 'benziyordu' ile uyumsuz.
   - Açıklama: 'Birden' ile sürerlik bildiren 'benziyordu' uyuşmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Birden bir bulut tıpkı bir kamyona benziyordu"
   - Cümle 2: «Birden bir bulut tıpkı bir kamyona benziyordu.»
   - Açıklama: Ani olay bildiren 'Birden' süreklilik bildiren 'benziyordu' ile uyumsuz.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bulutun şekli yavaş yavaş değişiyordu"
   - Cümle 3: «Ama rüzgar esiyordu ve bulutun şekli yavaş yavaş değişiyordu.»
   - Açıklama: Bulutun şeklinin değişmesi doğal ve önemsiz bir olay; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
   - Açıklama: Bulutun şeklinin değişmesi önemsiz bir olay; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
   - Açıklama: Bulutun şeklinin değişmesi doğal ve önemsiz bir olay; gerçek bir sorun kurmuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 6: «"Amca, gökyüzünde kocaman bir kamyon var, bütün mahalleyi taşır!" diye abarttı Hayri.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 'bütün mahalleyi taşır' abartısı 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Abarttı' 3 yaşındaki çocuk için soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "pürüzsüz ve yuvarlak bir topa"
   - Cümle 10: «Bulut şimdi pürüzsüz ve yuvarlak bir topa benziyordu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0006` birebir aynı, ardından `@onarim: 8a94c7b8e6e486e47ff1cc650fb6ce8c6df9b6f5`, sonra gövde.

### Hikâye 7: tohum hayri-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0008
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'çömlek', fiil 'bırakmak', sıfat 'minicik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpeğin burnu dar çömleğin ağzına sıkıştı | çömleği yavaşça yana çevirip burnu çıkardı
@tohum: hayri-0008
Deniz kıyısında Hayri acıkmıştı ve köfte dolu çömleği açtı. Tam o sırada Yumak koşup geldi ve burnunu çömleğin içine soktu. Çömleğin ağzı dar olduğu için Yumak'ın burnu orada sıkıştı. "Bekle, Yumak, sana yardım edeceğim," dedi Hayri. Hayri çömleği iki eliyle tuttu ve yavaşça yana çevirdi. Yumak'ın burnu kolayca dışarı çıktı. Yumak sevinçle havladı. Hayri çömleği kuma bıraktı ve minicik bir köfteyi Yumak'a verdi. Yumak köfteyi hemen yedi ve kuyruğunu salladı. "Yumak, köfte istersen benden iste!" dedi Hayri gülerek.
```

**Hakem bulguları (3):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Yumak'ın burnu orada sıkıştı"
   - Cümle 3: «Çömleğin ağzı dar olduğu için Yumak'ın burnu orada sıkıştı.»
   - Açıklama: Köpeğin burnunun dar çömleğe sıkışması hayvanın canının yanabileceği bir sıkıntı olarak gösteriliyor.
   - Açıklama: Köpeğin burnunun çömleğe sıkışması hayvanın canının yanabileceği bir sıkıntı durumu olarak gösteriliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri çömleği iki eliyle tuttu ve yavaşça yana çevirdi"
   - Cümle 5: «Hayri çömleği iki eliyle tuttu ve yavaşça yana çevirdi.»
   - Açıklama: Sebep çömleğin ağzının dar olması ama çömleği yana çevirmek dar ağza yönelmiyor ve burnun neden kolayca çıktığı anlaşılmıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "minicik bir köfteyi Yumak'a verdi"
   - Cümle 8: «Hayri çömleği kuma bıraktı ve minicik bir köfteyi Yumak'a verdi.»
   - Açıklama: Başkasının köpeğine insan yemeği (köfte) vermek çocuğun taklit edebileceği, köpek için zararlı olabilecek bir davranıştır.
   - Açıklama: Başkasının köpeğine sahibinden izinsiz insan yemeği vermek çocuğun taklit edebileceği ve bir köfte daha vaat edilerek özendirilen bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0008` birebir aynı, ardından `@onarim: 7137431b7d1fdc410ac8ec5bf7488ab770283c42`, sonra gövde.

### Hikâye 8: tohum hayri-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0009
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tabure', fiil 'sallamak', sıfat 'hazır'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: arkadaşının karnı boştu ve yiyeceği yoktu | arkadaşına da bir dilim karpuz verdi
@tohum: hayri-0009
Bir sabah Hayri bahçedeki tabureye bir tabak karpuz koydu. Çok acıkmıştı ve iki dilim karpuz yemeye hazırdı. O sırada karnı boş olan Akın kapıdan el salladı. Hayri tabaktaki karpuza baktı ve biraz düşündü. "Akın, gel, bir dilim senin!" dedi Hayri. Akın koşup geldi ve çimlere oturdu. Hayri büyük dilimi Akın'a uzattı. İkisi yan yana oturup karpuz yedi. Sonra siyah çekirdekleri tabağa dizip gülen bir yüz yaptılar. "Teşekkürler, Hayri, paylaşınca karpuz daha tatlı oldu!" dedi Akın.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "boştu ve yiyeceği yoktu"
   - Cümle 0 (plan satırı): «arkadaşının karnı boştu ve yiyeceği yoktu | arkadaşına da bir dilim karpuz verdi»
   - Açıklama: Gövdede Akın'ın yiyeceği olmadığı söylenmiyor; plan gövdede olmayan bir bilgi ekliyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bahçedeki tabureye bir tabak"
   - Cümle 1: «Bir sabah Hayri bahçedeki tabureye bir tabak karpuz koydu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede ve çimlerde geçiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karnı boş olan Akın kapıdan el salladı"
   - Cümle 3: «O sırada karnı boş olan Akın kapıdan el salladı.»
   - Açıklama: Akın'ın neden aç olduğu ve yiyeceği olmadığı hiç söylenmiyor; sorunun sebebi verilmiyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karnı boş olan Akın"
   - Cümle 3: «O sırada karnı boş olan Akın kapıdan el salladı.»
   - Açıklama: Akın'ın neden aç olduğu ve yiyeceğinin neden olmadığı hiç söylenmiyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "O sırada karnı boş olan Akın kapıdan el salladı"
   - Cümle 3: «O sırada karnı boş olan Akın kapıdan el salladı.»
   - Açıklama: Akın'ın neden aç olduğu ve yiyeceği olmadığı söylenmiyor; sorunun sebebi verilmiyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "paylaşınca karpuz daha tatlı oldu"
   - Cümle 10: «"Teşekkürler, Hayri, paylaşınca karpuz daha tatlı oldu!" dedi Akın.»
   - Açıklama: Karpuz gerçekten tatlanmıyor; mecazlı anlatım küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0009` birebir aynı, ardından `@onarim: 1985269bd0d00be77eb5eac93132755b5ead13a1`, sonra gövde.
