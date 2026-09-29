# Editör görevi (onarım): Hayri, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0023 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0023
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'piyano', fiil 'eklemek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: parkta bir müzik sesi geldi | sesin peşinden gitti ve sabırla bekledi
@tohum: hayri-0023
Parkta neşeli bir müzik sesi geliyordu. Hayri kaydıraktan indi ve sesi dinledi. Sesin nereden geldiğini çok merak etti. Hayri abarttı ve parkta kocaman bir piyano olduğunu düşündü. Ama hiçbir yerde kocaman bir piyano göremedi. Hayri sesin peşinden bankların yanına yürüdü. Orada Basri Amca oturuyordu. Kucağında küçük bir oyuncak piyano vardı. Basri Amca piyanoya yeni bir tuş ekledi ve çalmaya başladı. Hayri sabırlı davrandı ve şarkının bitmesini sessizce bekledi. Sonunda Basri Amca gülümsedi ve piyanoyu Hayri'ye uzattı. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "parkta bir müzik sesi geldi"
   - Cümle 0 (plan satırı): «parkta bir müzik sesi geldi | sesin peşinden gitti ve sabırla bekledi»
   - Açıklama: Bir müzik sesinin gelmesi sebebi söylenmiş bir sorun değil, yalnız bir merak.
   - Açıklama: Sorun gerçek bir engel değil, yalnız bir sesin duyulması; çözülmesi gereken akla yatkın bir sorun kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve parkta"
   - Cümle 4: «Hayri abarttı ve parkta kocaman bir piyano olduğunu düşündü.»
   - Açıklama: 'Abarttı' soyut ve küçük çocuğa uygun olmayan bir kelime, cümlede de yerinde kullanılmamış.
   - Açıklama: 'Abartmak' soyut bir kavram ve burada yerinde kullanılmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Basri Amca piyanoya yeni bir tuş ekledi"
   - Cümle 9: «Basri Amca piyanoya yeni bir tuş ekledi ve çalmaya başladı.»
   - Açıklama: Tuş ekleme ve piyanonun Hayri'ye uzatılması olaydan çıkmayan işlevsiz ayrıntılar.
   - Açıklama: Oyuncak piyanoya tuş eklenmesi sebepsiz ve olayda hiçbir işe yaramayan bir ayrıntı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri sabırlı davrandı ve şarkının bitmesini"
   - Cümle 10: «Hayri sabırlı davrandı ve şarkının bitmesini sessizce bekledi.»
   - Açıklama: Tohumdaki özellik abartmak; sorun abartmayla değil, kartın özellik listesinde olmayan sabırla çözülüyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri sabırlı davrandı"
   - Cümle 10: «Hayri sabırlı davrandı ve şarkının bitmesini sessizce bekledi.»
   - Açıklama: Tohumdaki özellik abartma; sabır ikinci bir özellik olarak çözüme ekleniyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri sabırlı davrandı ve şarkının bitmesini sessizce bekledi"
   - Cümle 10: «Hayri sabırlı davrandı ve şarkının bitmesini sessizce bekledi.»
   - Açıklama: Ses zaten bulunmuşken beklemek sorunun sebebine yönelmeyen gereksiz bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0023` birebir aynı, ardından `@onarim: 6778a0ef0148bb39683008b092033ff16d894ac5`, sonra gövde.

### Hikâye 2: tohum hayri-0024 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0024
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'paket', fiil 'paketlemek', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kurabiyelerin kağıdını her seferinde açtı | kağıdın kenarlarını katladı ve sıkı bir paket yaptı
@tohum: hayri-0024
@degisim: somurtkan -> sıkı
Deniz kıyısında hafif bir rüzgar esiyordu. Hayri kumda kurabiye dükkanı oyunu oynuyordu. Islak kumdan küçük kurabiyeler yaptı ve bir taşa dizdi. Sonra çantasından bir kağıt çıkardı. Kurabiyeleri kağıda koyup paketlemek istedi. Ama rüzgar kağıdı her seferinde açtı. Hayri baklava dükkanında çalışıyordu ve kutu kapatmayı iyi biliyordu. Kağıdın kenarlarını içe doğru kıvırdı ve sıkıca katladı. Böylece sıkı bir paket yaptı. Rüzgar yine esti ama paket hiç açılmadı. Hayri paketi taştan tezgahın üstüne koydu. Sonra mutlu mutlu yeni kum kurabiyeleri yapmaya devam etti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Islak kumdan küçük kurabiyeler yaptı ve bir taşa dizdi.»
   - Açıklama: Sorun ancak 6. cümlede söyleniyor, ilk 3 cümlede sorun yok.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar kağıdı her seferinde açtı"
   - Cümle 6: «Ama rüzgar kağıdı her seferinde açtı.»
   - Açıklama: Sorun ancak 6. cümlede söyleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri baklava dükkanında çalışıyordu"
   - Cümle 7: «Hayri baklava dükkanında çalışıyordu ve kutu kapatmayı iyi biliyordu.»
   - Açıklama: Hayri o sırada kumsalda oynarken 'çalışıyordu' onun aynı anda dükkanda olduğunu söylüyor; zaman/anlam uyumsuz.
   - Açıklama: 'Çalışıyordu' o anda dükkanda çalıştığını anlatıyor; kumsaldaki sahneyle çelişiyor, alışkanlık için 'çalışırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0024` birebir aynı, `@degisim: somurtkan -> sıkı` (tutuyorsan), ardından `@onarim: ca8dc65e06285eecd0f55da77e7bb30fbe046246`, sonra gövde.

### Hikâye 3: tohum hayri-0025 (deneme 1 -> 2)

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
Hayri'nin yeşil bir kalıbı vardı ve kumdan kuleler yapıyordu. Mert de kıyıda elleriyle kum topluyordu. Ama Mert'in kuleleri hep yıkılıyordu. "Mert, kalıbı birlikte kullanalım mı?" diye sordu Hayri. Mert sevindi ve başını salladı. Hayri kalıbı ıslak kumla doldurdu ve Mert'e verdi. Mert kalıbı ters çevirdi ve yavaşça kaldırdı. Kumda düzgün bir kule duruyordu. "Bu, dünyanın en büyük kulesi!" dedi Hayri abartarak. Mert güldü ve bir kule daha yaptı. Hayri çok mutluydu, çünkü paylaşınca ikisi de kule yapmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Bu, dünyanın en büyük kulesi!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 'dünyanın en büyük' abartısı küçük çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Bu, dünyanın en büyük kulesi!" dedi Hayri abartarak.»
   - Açıklama: Tohumdaki abartma özelliği çözümde işe yaramıyor; çözüm paylaşmakla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0025` birebir aynı, `@degisim: guruldamak -> doldurmak` (tutuyorsan), ardından `@onarim: 32942fb81a8ad2e7f77e47f73c58994650dd24e0`, sonra gövde.

### Hikâye 4: tohum hayri-0027 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0027
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'dosya', fiil 'esnemek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: ince kağıttan yaptığı uçağın kanatları esnedi | dosyanın kalın kapağını düzgünce katladı
@tohum: hayri-0027
@degisim: nefis -> kalın
Bir sabah Hayri parkta ilk kez kağıttan uçak yapmayı denedi. Çantasındaki dosyadan ince bir kağıt aldı. Kağıdı katladı ve uçağı havaya attı. Ama ince kanatlar esnedi ve uçak hemen yere düştü. Hayri dosyanın kapağına baktı. Kapak kalın ve sertti. Hayri baklava dükkanında kutu katlamayı öğrenmişti. Kapağı düzgünce ve sıkıca katladı. Sonra yeni uçağı yavaşça havaya bıraktı. Uçak bu kez düşmedi ve parkın üstünde uzun uzun süzüldü. Hayri koştu ve uçağı çimenden aldı. Sonra uçağını mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında kutu katlamayı öğrenmişti"
   - Cümle 7: «Hayri baklava dükkanında kutu katlamayı öğrenmişti.»
   - Açıklama: Baklava dükkanı bilgisi sahneye sebepsizce sokuluyor ve çözümü dışarıdan getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0027` birebir aynı, `@degisim: nefis -> kalın` (tutuyorsan), ardından `@onarim: 31cb9e2aa4aab6e20403612c856a3e4e300674b7`, sonra gövde.

### Hikâye 5: tohum hayri-0028 (deneme 1 -> 2)

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
@plan: yağmur damlaları tabaktaki tatlılara düştü | tabağın üstüne yeni kovasını ters kapattı
@tohum: hayri-0028
Yağmur damlaları sokakta tıp tıp ses çıkarıyordu. Hayri baklava dükkanından elinde küçük bir tabakla geliyordu. Tabağın üstü açıktı ve damlalar tatlılara düşmeye başladı. Hayri bahçe kapısının yanında yeni kovasını gördü. Kovayı ters çevirdi ve tabağın üstüne kapattı. Sonra tabağı çatının altındaki kuru köşeye taşıdı. Orada kovayı kaldırdı ve tatlıları kokladı. Tatlılar kuru ve sıcacıktı. Hayri bir dilim aldı ve afiyetle yedi. Sonra kuru köşede oturdu ve yağmuru mutlu mutlu izledi.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Yağmur damlaları sokakta tıp tıp"
   - Cümle 1: «Yağmur damlaları sokakta tıp tıp ses çıkarıyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye sokakta, dükkandan dönüşte başlıyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Yağmur damlaları sokakta tıp tıp ses"
   - Cümle 1: «Yağmur damlaları sokakta tıp tıp ses çıkarıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta başlıyor ve bahçe kapısıyla çatı altına geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri baklava dükkanından elinde küçük bir tabakla"
   - Cümle 2: «Hayri baklava dükkanından elinde küçük bir tabakla geliyordu.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız anılıyor, çözüm kovayla geliyor ve özellik işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bahçe kapısının yanında yeni kovasını gördü"
   - Cümle 4: «Hayri bahçe kapısının yanında yeni kovasını gördü.»
   - Açıklama: Çözümü sağlayan kova sokakta dönen Hayri'nin önüne sebepsizce çıkıyor.
   - Açıklama: Kova çözüm için sebepsizce tam gereken yerde beliriyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tatlılar kuru ve sıcacıktı"
   - Cümle 8: «Tatlılar kuru ve sıcacıktı.»
   - Açıklama: Damlalar tatlılara düşmüştü ama sonra tatlıların kuru olduğu söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0028` birebir aynı, ardından `@onarim: fe5bb6fa9862fae67ec1300b129cb4bcb9c51136`, sonra gövde.

### Hikâye 6: tohum hayri-0029 (deneme 1 -> 2)

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
@plan: fener kaydı ve ışık tavana gitti | feneri çantanın üstüne dik koydu
@tohum: hayri-0029
Bir sabah erkenden ormandaki kamp yeri daha karanlıktı. Hayri çadırında fenerini açtı ve gölge oyunu oynadı. Elleriyle çadırın duvarına garip şekiller yaptı. Gölgeler duvarda bir o yana bir bu yana gezindi. Sonra çalıştığı dükkandaki baklava dilimini düşündü. Parmaklarıyla aynı şekli yapmak istedi. Ama fener uyku tulumunun üstünden kaydı. Işık çadırın tavanına gitti ve gölgeler kayboldu. Hayri feneri çantasının üstüne dik koydu. Işık yine duvara vurdu. Hayri parmaklarını birleştirdi ve duvarda tam bir dilim gölgesi çıktı. Hayri çok sevindi, çünkü en sevdiği tatlının gölgesini yapmıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kamp yeri daha karanlıktı"
   - Cümle 1: «Bir sabah erkenden ormandaki kamp yeri daha karanlıktı.»
   - Açıklama: 'daha' karşılaştırma mı 'henüz' mü belli değil; 'hâlâ karanlıktı' anlamı net verilmemiş.
   - Açıklama: 'Daha' burada 'hâlâ' anlamında kullanılmış; çocuk 'daha çok karanlık' diye anlar.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elleriyle çadırın duvarına garip şekiller yaptı.»
   - Açıklama: Sorun ancak 7. cümlede geliyor; ilk üç cümlede yalnız gölge oyunu anlatılıyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 7: «Ama fener uyku tulumunun üstünden kaydı.»
   - Açıklama: Sorun (fenerin kayması) ancak 7. cümlede söyleniyor, ilk 3 cümlede sorun yok.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama fener uyku tulumunun üstünden kaydı"
   - Cümle 7: «Ama fener uyku tulumunun üstünden kaydı.»
   - Açıklama: Fenerin neden kaydığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0029` birebir aynı, ardından `@onarim: f14f9b7a15b9da6cf1991d84f8ca5f86c72972b2`, sonra gövde.

### Hikâye 7: tohum hayri-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0030
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'teneke', fiil 'şekillendirmek', sıfat 'zeki'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: telefonun ipi bir dala takıldı ve ses gitmedi | ipi daldan çıkarıp çekti
@tohum: hayri-0030
@degisim: şekillendirmek -> çekmek
Ormanda, kamp yerinde Hayri ile Akın oyun oynuyordu. İki teneke kutu uzun bir iple bağlıydı. Bu telefonu zeki Akın yapmıştı. "Akın, beni duyuyor musun?" diye fısıldadı Hayri. Ama Akın hiçbir şey duymadı. Hayri ipe baktı ve bir dala takıldığını gördü. İpi daldan dikkatle çıkardı. Sonra geri geri yürüdü ve ipi çekti. "Akın, ben çok acıktım!" dedi Hayri kutuya. Akın bu kez hemen güldü. "Hadi, elmaları birlikte yiyelim!" dedi Akın. "Teşekkürler, Akın, telefon artık çalışıyor!" dedi Hayri sevinçle.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Akın hiçbir şey duymadı"
   - Cümle 5: «Ama Akın hiçbir şey duymadı.»
   - Açıklama: Sorun ilk 3 cümlede değil 5. cümlede ortaya çıkıyor.
   - Açıklama: Sorun ancak 5. cümlede ortaya çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hadi, elmaları birlikte yiyelim"
   - Cümle 11: «"Hadi, elmaları birlikte yiyelim!" dedi Akın.»
   - Açıklama: Elmalar hiç kurulmadan sebepsiz beliriyor.
   - Açıklama: Elmalar sebepsiz beliriyor ve olayla hiçbir bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0030` birebir aynı, `@degisim: şekillendirmek -> çekmek` (tutuyorsan), ardından `@onarim: 507b30231048dc12aeebe788daa90da324ee6098`, sonra gövde.

### Hikâye 8: tohum hayri-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0031
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ayakkabı', fiil 'temizlenmek', sıfat 'puantiyeli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: tepsi taşırken ayakkabısının bağı çözüldü | yardım istedi ve arkadaşı bağı bağladı
@tohum: hayri-0031
@degisim: temizlenmek -> bağlamak
Sokakta sıcak bir güneş parlıyordu. Hayri baklava dükkanından elinde bir tepsiyle çıktı. Birden puantiyeli ayakkabısının bağı çözüldü. Hayri'nin iki eli de tepsiyle doluydu ve Hayri yolda durdu. Tam o sırada Akın bahçe kapısından çıktı. "Akın, bu bağı bağlar mısın?" diye sordu Hayri. "Tabii, hemen," dedi Akın. Akın eğildi ve bağı sıkıca bağladı. Hayri artık rahatça yürüyebildi. Teşekkür etti ve tepsideki tatlılardan birini Akın'a verdi. Sonra ikisi kaldırıma oturdu ve tatlılarını mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sokakta sıcak bir güneş parlıyordu"
   - Cümle 1: «Sokakta sıcak bir güneş parlıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta ve dükkan önünde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta ve kaldırımda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden puantiyeli ayakkabısının"
   - Cümle 3: «Birden puantiyeli ayakkabısının bağı çözüldü.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden puantiyeli ayakkabısının bağı çözüldü"
   - Cümle 3: «Birden puantiyeli ayakkabısının bağı çözüldü.»
   - Açıklama: Bağın neden çözüldüğü söylenmiyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "doluydu ve Hayri yolda durdu"
   - Cümle 4: «Hayri'nin iki eli de tepsiyle doluydu ve Hayri yolda durdu.»
   - Açıklama: Aynı cümlede 'Hayri' adı gereksiz yere tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0031` birebir aynı, `@degisim: temizlenmek -> bağlamak` (tutuyorsan), ardından `@onarim: 6344907f8b9c6f437f48058702d82b641812831a`, sonra gövde.

### Hikâye 9: tohum hayri-0032 (deneme 1 -> 2)

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
@plan: toprak yumuşaktı ve fidan yana yattı | toprak ekledi ve iki eliyle sıkıca bastı
@tohum: hayri-0032
Bir sabah Basri Amca parka yeni fidanlar dikiyordu. Hayri koşarak yanına geldi. "Basri Amca, ben de fidan dikmeyi deneyebilir miyim?" diye sordu Hayri. Basri Amca ona küçük, yemyeşil bir fidan verdi. Hayri fidanı çukura koydu ve üstüne biraz toprak attı. Ama toprak yumuşaktı ve fidan hemen yana yattı. Hayri çukura biraz daha toprak ekledi. Sonra toprağı iki eliyle sıkıca bastı. Fidan bu kez dimdik durdu. Hayri fidanın yapraklarını okşadı. "Bu fidan parktaki en büyük ağaç olacak!" dedi Hayri abartarak. Basri Amca güldü ve fidana Hayri'nin adını yazan bir etiket astı. Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastı.
```

**Hakem bulguları (6):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama toprak yumuşaktı ve fidan hemen yana yattı"
   - Cümle 6: «Ama toprak yumuşaktı ve fidan hemen yana yattı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak altıncı cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 11: «"Bu fidan parktaki en büyük ağaç olacak!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 11: «"Bu fidan parktaki en büyük ağaç olacak!" dedi Hayri abartarak.»
   - Açıklama: Tohumdaki abartma özelliği fidanı dikmede işe yaramıyor, yalnız süs olarak ekleniyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri'nin adını yazan bir etiket"
   - Cümle 12: «Basri Amca güldü ve fidana Hayri'nin adını yazan bir etiket astı.»
   - Açıklama: Etiket ad yazmaz; 'adının yazılı olduğu bir etiket' olmalı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "adını yazan bir etiket"
   - Cümle 12: «Basri Amca güldü ve fidana Hayri'nin adını yazan bir etiket astı.»
   - Açıklama: Etiket ad yazmaz; 'adı yazılı bir etiket' olmalı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "fidana Hayri'nin adını yazan bir etiket astı"
   - Cümle 12: «Basri Amca güldü ve fidana Hayri'nin adını yazan bir etiket astı.»
   - Açıklama: Etiket sebepsiz beliriyor ve olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0032` birebir aynı, ardından `@onarim: 4c16b598cfefc41cf9ddd9731a5f068b9e13828d`, sonra gövde.
