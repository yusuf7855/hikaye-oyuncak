# Editör görevi (onarım): Hayri, onarım partisi 49

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar49.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar49.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0177 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0177
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kar', fiil 'süslenmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: pencereden garip bir tık tık sesi geldi | bahçeye çıktı ve cama vuran karlı dalı buldu
@tohum: hayri-0177
Bir sabah mahallede her yer bembeyazdı. Hayri evde, pencerenin yanında oturuyordu. Birden camdan "tık tık" diye bir ses geldi. Hayri bu sesi çok merak etti. Hayri olayı biraz abarttı ve montunu, atkısını, eldivenlerini, botlarını giydi. Sonra bahçeye çıktı ve pencerenin önüne geldi. Pencerenin yanında karla süslenmiş bir ağaç dalı vardı. Rüzgar esince dal cama vuruyor ve o sesi çıkarıyordu. Hayri dala hafifçe dokundu ve kar başına döküldü. Bu çok eğlenceliydi ve Hayri güldü. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "montunu, atkısını, eldivenlerini, botlarını giydi"
   - Cümle 5: «Hayri olayı biraz abarttı ve montunu, atkısını, eldivenlerini, botlarını giydi.»
   - Açıklama: Atkı giyilmez, takılır; fiil nesnelerin hepsine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri olayı biraz abarttı"
   - Cümle 5: «Hayri olayı biraz abarttı ve montunu, atkısını, eldivenlerini, botlarını giydi.»
   - Açıklama: 'Olayı abartmak' soyut bir anlatım; 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Olayı abartmak' deyimsel ve soyut bir ifade, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'olayı abartmak' soyut bir anlatım; 3 yaşındaki çocuk anlamaz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri olayı biraz abarttı"
   - Cümle 5: «Hayri olayı biraz abarttı ve montunu, atkısını, eldivenlerini, botlarını giydi.»
   - Açıklama: Kartın 'Olayları abartmayı sever' özelliği bol giyinmeye indirgenmiş ve sesin kaynağını bulmaya hiçbir katkısı yok, yani işe yarar biçimde kullanılmamış.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sonra bahçeye çıktı ve pencerenin önüne geldi"
   - Cümle 6: «Sonra bahçeye çıktı ve pencerenin önüne geldi.»
   - Açıklama: Hikaye başlıktaki evde başlıyor ama dışarıda, bahçede bitiyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sonra bahçeye çıktı ve pencerenin"
   - Cümle 6: «Sonra bahçeye çıktı ve pencerenin önüne geldi.»
   - Açıklama: Hikaye evde başlıyor ama bahçede bitiyor; tek sahne kuralı çiğneniyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karla süslenmiş bir ağaç dalı"
   - Cümle 7: «Pencerenin yanında karla süslenmiş bir ağaç dalı vardı.»
   - Açıklama: Karın dalı 'süslemesi' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0177` birebir aynı, ardından `@onarim: 4994122295eaa2af519e4057ff6c0759bae76bb3`, sonra gövde.

### Hikâye 2: tohum hayri-0178 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0178
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'buket', fiil 'rahatlamak', sıfat 'yüksek'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: sokakta güzel bir koku geldi ve köpek havladı | acıkınca kokuya doğru yürüdü ve bir çiçek buketi buldu
@tohum: hayri-0178
Bir sabah Hayri ile Yumak sokakta yürüyordu. Birden çok güzel bir koku geldi. Yumak durdu ve yüksek bir pencereye bakıp havladı. Hayri çok acıkmıştı ve kokunun bir yemekten geldiğini düşündü. Hayri kokuya doğru yürüdü ve pencerenin altına geldi. Pencerenin önünde büyük bir çiçek buketi duruyordu. Koku bu çiçeklerden geliyordu. "Bu yemek değil, çiçek kokusu, Yumak!" dedi Hayri. Yumak havlamayı bıraktı ve rahatladı. Kuyruğunu sallayarak Hayri'nin yanına geldi. Hayri güldü ve çantasından elmasını çıkardı. Hayri ile Yumak yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (9):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Hayri ile Yumak sokakta yürüyordu"
   - Cümle 1: «Bir sabah Hayri ile Yumak sokakta yürüyordu.»
   - Açıklama: Kartın yanlar ilişkisine göre Yumak Basri Amca'nın köpeğidir, hikaye onu Basri Amca olmadan Hayri'nin yürüyüş arkadaşı gibi sunuyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Yumak sokakta yürüyordu"
   - Cümle 1: «Bir sabah Hayri ile Yumak sokakta yürüyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta başlıyor ve bitiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta geçiyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Birden çok güzel bir koku"
   - Cümle 2: «Birden çok güzel bir koku geldi.»
   - Açıklama: 'Birden' sonrası virgül yok, 'birden çok' (birden fazla) diye okunabiliyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çok güzel bir koku geldi"
   - Cümle 2: «Birden çok güzel bir koku geldi.»
   - Açıklama: Güzel bir kokunun gelmesi ve köpeğin havlaması çocuğun önemseyeceği açık bir sorun değil.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yumak durdu ve yüksek bir pencereye bakıp havladı"
   - Cümle 3: «Yumak durdu ve yüksek bir pencereye bakıp havladı.»
   - Açıklama: Güzel bir kokunun gelmesi ve köpeğin havlaması çocuğun önemseyeceği açık bir sorun değil, havlamanın sebebi de söylenmiyor.
6. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hayri çok acıkmıştı"
   - Cümle 4: «Hayri çok acıkmıştı ve kokunun bir yemekten geldiğini düşündü.»
   - Açıklama: Yumak'ın havlaması ve Hayri'nin açlığı iki ayrı sorun olarak karışıyor.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir çiçek buketi"
   - Cümle 6: «Pencerenin önünde büyük bir çiçek buketi duruyordu.»
   - Açıklama: 'Buket' 3 yaşındaki çocuğun bilmediği bir kelime.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasından elmasını çıkardı"
   - Cümle 11: «Hayri güldü ve çantasından elmasını çıkardı.»
   - Açıklama: Elma sebepsizce beliriyor ve açlık sorunu çözülmüş gibi gösterilmeden bırakılıyor.
   - Açıklama: Elma sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
9. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 12: «Hayri ile Yumak yürüyüşlerine mutlu mutlu devam etti.»
   - Açıklama: Hikayenin hedefi belirsiz; ne havlama ne açlık sorunu doyurucu biçimde çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0178` birebir aynı, ardından `@onarim: 66baccbb675c100f043f108f67a176126a6252c6`, sonra gövde.

### Hikâye 3: tohum hayri-0179 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0179
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'toprak', fiil 'gıdıklamak', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kamp yerinde garip bir ses duyuldu | sesin kendi karnından geldiğini bulup sandviç hazırladı
@tohum: hayri-0179
Bir sabah kamp yerinde Hayri garip bir ses duydu. Ses alçaktı ve uzun sürdü. Hayri sesin nereden geldiğini merak etti. Önce yere eğildi ve kulağını toprağa dayadı. Otlar yüzünü gıdıkladı ve Hayri gülmeye başladı. Gülerken elini karnına koydu. O anda ses yine geldi, hem de tam elinin altından. Ses onun karnından geliyordu, çünkü Hayri çok acıkmıştı. Hayri çantasından ekmek, peynir ve renkli biberler çıkardı. Hepsiyle kendine güzel bir sandviç hazırladı. Sandviçi yedikten sonra karnındaki ses kesildi ve Hayri mutlu oldu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Otlar yüzünü gıdıkladı ve Hayri gülmeye başladı"
   - Cümle 5: «Otlar yüzünü gıdıkladı ve Hayri gülmeye başladı.»
   - Açıklama: Sesin kaynağı Hayri'nin bilinçli bir arayışıyla değil, gıdıklanıp gülerken elini tesadüfen karnına koymasıyla bulunuyor; çözüm sebepsizce geliyor.
   - Açıklama: Sesin kaynağı Hayri'nin arayışıyla değil tesadüfi bir gülme ile bulunuyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0179` birebir aynı, ardından `@onarim: b230f143a773159aadd214a9abcaaeeaeb342d45`, sonra gövde.

### Hikâye 4: tohum hayri-0180 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0180
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'iz', fiil 'tekrarlamak', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: acıkınca simit çantasını geniş kumsalda bulamadı | arkadaşından yardım istedi ve ayak izleri sayesinde çantayı buldu
@tohum: hayri-0180
Bir sabah Hayri ile Mert deniz kıyısında top oynuyordu. Bir süre sonra Hayri çok acıktı. Ama kumsal çok genişti ve simit çantasını bulamadı. Hayri bir sağa, bir sola koştu ama çantayı göremedi. Sonra Mert'in yanına gitti. "Mert, çantamı bulamıyorum, bana yardım eder misin?" diye sordu Hayri. Mert bir an hareketsiz durdu ve düşündü. "Bak, kumda her adımın bir iz bırakıyor," dedi Mert. Hayri kendi izleri boyunca geri yürüdü ve yolunu tekrarladı. Böylece büyük bir taşın arkasına geldi. Çanta orada duruyordu. Hayri bir simidi hemen Mert'e verdi. Hayri çok sevindi, çünkü Mert'ten yardım istemiş ve çantasını bulmuştu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kumsal çok genişti ve simit çantasını bulamadı"
   - Cümle 3: «Ama kumsal çok genişti ve simit çantasını bulamadı.»
   - Açıklama: Bağlı iki cümlede özne kayıyor; dilbilgisel olarak çantayı bulamayan 'kumsal' oluyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kumsal çok genişti ve simit çantasını bulamadı"
   - Cümle 3: «Ama kumsal çok genişti ve simit çantasını bulamadı.»
   - Açıklama: Çantanın neden kaybolduğu söylenmiyor; kumsalın geniş olması kaybın akla yatkın bir sebebi değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geri yürüdü ve yolunu tekrarladı"
   - Cümle 9: «Hayri kendi izleri boyunca geri yürüdü ve yolunu tekrarladı.»
   - Açıklama: Geri yürürken yol 'tekrarlanmaz'; kelime yanlış anlamda kullanılmış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve yolunu tekrarladı"
   - Cümle 9: «Hayri kendi izleri boyunca geri yürüdü ve yolunu tekrarladı.»
   - Açıklama: 'Yolunu tekrarlamak' yanlış anlamda; izleri takip ederek geri yürümeyi anlatmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0180` birebir aynı, ardından `@onarim: 6ea8b96a9de18c062768c93a369133892c7fc95a`, sonra gövde.

### Hikâye 5: tohum hayri-0181 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0181
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'misket', fiil 'inanmak', sıfat 'dar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: misketler köklerin arasındaki dar yerlere kaçıyordu | baklava tepsisini düz bir yere koyup içinde oynadılar
@tohum: hayri-0181
Bir sabah Hayri ile Kamil ormandaki kamp yerinde misket oynuyordu. Ama yerde çok kök ve taş vardı. Misketler hep köklerin arasındaki dar yerlere kaçıyordu. "Böyle oynayamayız, Hayri," dedi Kamil. Hayri çalıştığı baklava dükkanından bir tepsi getirmişti. Tepside iki dilim baklava kalmıştı. İkisi birer dilim yedi ve tepsi boşaldı. Hayri boş tepsiyi düz bir yere koydu. "Misketleri tepside oynayalım!" dedi Hayri. "Buna inanmıyorum ama deneyelim," dedi Kamil. Tepsinin kenarları vardı ve misketler artık kaçmadı. Kamil kendi misketiyle Hayri'nin misketini itti. "Harika oldu, Hayri, tepsi en güzel oyun yeri!" dedi Kamil.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çalıştığı baklava dükkanından bir tepsi getirmişti"
   - Cümle 5: «Hayri çalıştığı baklava dükkanından bir tepsi getirmişti.»
   - Açıklama: Çözümü getiren tepsi sorun çıktıktan sonra sebepsizce ortaya çıkıyor.
   - Açıklama: Çözümü sağlayan tepsi daha önce kurulmadan tam gerektiği anda sebepsizce beliriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Buna inanmıyorum ama deneyelim"
   - Cümle 10: «"Buna inanmıyorum ama deneyelim," dedi Kamil.»
   - Açıklama: 'Buna inanmıyorum' şaşkınlık bildirir; burada 'işe yarayacağını sanmıyorum' anlamında yanlış kullanılmış.
   - Açıklama: 'İnanmıyorum' yanlış anlamda; tepside oynamanın işe yarayacağından şüphe kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0181` birebir aynı, ardından `@onarim: 16deb681137f29d60d042844704efaa596ed8429`, sonra gövde.

### Hikâye 6: tohum hayri-0183 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0183
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'sebze', fiil 'binmek', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: karın altındaki taşlar yüzünden kızak takılıyordu | taşların üstüne bol kar taşıdı ve yol yaptı
@tohum: hayri-0183
@degisim: sebze -> kızak
Hayri parktaki küçük tepenin yeni karla bembeyaz olduğunu fark etti. Hemen kızağa bindi ama kızak biraz gidip durdu. Karın altında saklı küçük taşlar vardı ve kızak onlara takılıyordu. Hayri taşların üstüne kar taşımaya başladı ve bunu biraz abarttı. Durmadan kar getirdi ve kocaman, yumuşak bir yol yaptı. Artık taşlar hiç görünmüyordu. Hayri yeniden kızağa oturdu. Kızak bu yolda kayarak tepenin altına kadar indi. Kızak durunca Hayri sevinçle güldü. Hayri tepeden kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bunu biraz abarttı"
   - Cümle 4: «Hayri taşların üstüne kar taşımaya başladı ve bunu biraz abarttı.»
   - Açıklama: 'Abarttı' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve bunu biraz abarttı"
   - Cümle 4: «Hayri taşların üstüne kar taşımaya başladı ve bunu biraz abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayarak tepenin altına kadar indi"
   - Cümle 8: «Kızak bu yolda kayarak tepenin altına kadar indi.»
   - Açıklama: Tepenin 'altı' değil eteği ya da aşağısı kastediliyor; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0183` birebir aynı, `@degisim: sebze -> kızak` (tutuyorsan), ardından `@onarim: 9bd99e429526c17b4a6998767c5ac6af99ad3cf7`, sonra gövde.

### Hikâye 7: tohum hayri-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0184
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'dolap', fiil 'fırlatmak', sıfat 'uzak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: taşı dik attı ve taş hemen suya battı | taşı tepsi gibi düz tutarak alçaktan fırlattı
@tohum: hayri-0184
@degisim: dolap -> taş
Rüzgar hafif hafif esiyordu. Hayri deniz kıyısında ilk kez bir taşı suyun üstünde zıplatmak istedi. Ama taşı dik fırlattı ve taş hemen suya battı. Hayri biraz düşündü. Dükkanda baklava tepsisini hep düz tutardı. Bu kez taşı da tepsi gibi düz tuttu. Eğildi ve taşı suya doğru alçaktan fırlattı. Taş suyun üstünde üç kez zıpladı. Sonra çok uzak dalgaların arasına düştü. Sevinçle güldü ve ellerini çırptı. Hayri yeni taşlar topladı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sevinçle güldü ve ellerini"
   - Cümle 10: «Sevinçle güldü ve ellerini çırptı.»
   - Açıklama: Önceki cümlenin öznesi taş olduğu için gülen kişinin Hayri olduğu belirtilmemiş.
   - Açıklama: Önceki cümlenin öznesi taş olduğu için gülenin kim olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0184` birebir aynı, `@degisim: dolap -> taş` (tutuyorsan), ardından `@onarim: e072fc3e9fbbf19c4f41f86a4cb5a032f2094794`, sonra gövde.

### Hikâye 8: tohum hayri-0185 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0185
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çıkartma', fiil 'kaldırmak', sıfat 'sağlam'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: aynı anda taş koyunca kule yıkıldı | sırayla koymayı önerdi ve kuleyi yeniden yaptılar
@tohum: hayri-0185
@degisim: çıkartma -> taş
Hayri ile Basri Amca kıyıda taşlardan bir kule yapıyordu. İkisi aynı anda birer taş koyunca kule yıkıldı. Basri Amca biraz kızdı. "Basri Amca, sırayla koyalım mı?" diye sordu Hayri. "Olur, önce sen koy," dedi Basri Amca. Hayri en büyük taşı, dükkanda baklava tepsisi tutar gibi iki eliyle kaldırdı. Taşı en alta dikkatle yerleştirdi. Sonra amca kendi taşını onun üstüne koydu. Birer birer altı taş daha koydular. Kule bu kez hiç sallanmadı. "Aferin, Hayri, kulemiz çok sağlam oldu!" dedi Basri Amca. Hayri çok sevindi, çünkü sırayla oynayınca kule yıkılmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dükkanda baklava tepsisi tutar gibi"
   - Cümle 6: «Hayri en büyük taşı, dükkanda baklava tepsisi tutar gibi iki eliyle kaldırdı.»
   - Açıklama: Hikayeyle ilgisiz bir benzetme; 3 yaşındaki çocuk için mecazlı ve karışık bir anlatımdır.
   - Açıklama: Benzetme mecaz niteliğinde ve hikayede dükkan olmadığı için çocuğa yabancı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dükkanda baklava tepsisi tutar gibi"
   - Cümle 6: «Hayri en büyük taşı, dükkanda baklava tepsisi tutar gibi iki eliyle kaldırdı.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız bir benzetmede süs olarak geçiyor, sorunun çözümüne katkısı yok (kartın özellikler alanı işe yarar kullanım ister).
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız benzetme olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0185` birebir aynı, `@degisim: çıkartma -> taş` (tutuyorsan), ardından `@onarim: 51086d81e3ef26ea83855d210610be1d5e6486ca`, sonra gövde.

### Hikâye 9: tohum hayri-0186 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0186
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'koltuk', fiil 'yumuşamak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: koltuk sıkışmıştı ve tek başına açılmadı | arkadaşından yardım istedi ve birlikte açtılar
@tohum: hayri-0186
@degisim: yumuşamak -> açmak
Hayri ormandaki kamp yerinde küçük koltuğunu açmak istedi. Ama koltuk sıkışmıştı ve Hayri tek başına onu açamadı. Akın biraz uzakta kuşları izliyordu ve çok meşguldü. "Akın, bu koltuğu yüz kez çektim, yardım et!" diye abartarak seslendi Hayri. Akın güldü ve hemen koşup geldi. "Yüz kez mi? Hadi, birlikte çekelim," dedi Akın. Akın koltuğun bir ucundan tuttu. Hayri de diğer ucundan çekti. Koltuk birden açıldı. Hayri hemen koltuğa oturdu. "Teşekkürler, Akın," dedi Hayri. Hayri çok sevindi, çünkü Akın'ın yardımıyla koltuğu açılmıştı.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tek başına açılmadı"
   - Cümle 0 (plan satırı): «koltuk sıkışmıştı ve tek başına açılmadı | arkadaşından yardım istedi ve birlikte açtılar»
   - Açıklama: Plan satırında özne koltuk olduğu için 'tek başına açılmadı' koltuğun kendiliğinden açılmadığı anlamına geliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "koltuk sıkışmıştı ve tek başına açılmadı"
   - Cümle 0 (plan satırı): «koltuk sıkışmıştı ve tek başına açılmadı | arkadaşından yardım istedi ve birlikte açtılar»
   - Açıklama: Plan satırında 'tek başına' koltuğa bağlanıyor; açamayan Hayri, özne uyumsuz.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama koltuk sıkışmıştı ve"
   - Cümle 2: «Ama koltuk sıkışmıştı ve Hayri tek başına onu açamadı.»
   - Açıklama: Koltuğun neden sıkıştığı hiç söylenmiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve çok meşguldü"
   - Cümle 3: «Akın biraz uzakta kuşları izliyordu ve çok meşguldü.»
   - Açıklama: 'Meşgul' soyut ve 3 yaşındaki çocuğa uygun olmayan bir kelime.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuşları izliyordu ve çok meşguldü"
   - Cümle 3: «Akın biraz uzakta kuşları izliyordu ve çok meşguldü.»
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak seslendi"
   - Cümle 4: «"Akın, bu koltuğu yüz kez çektim, yardım et!" diye abartarak seslendi Hayri.»
   - Açıklama: 'Abartarak' soyut bir kavram, küçük çocuk bilmez.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak seslendi Hayri"
   - Cümle 4: «"Akın, bu koltuğu yüz kez çektim, yardım et!" diye abartarak seslendi Hayri.»
   - Açıklama: 'Abartarak' ve 'yüz kez' abartısı 3 yaşındaki çocuğa uygun olmayan soyut anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0186` birebir aynı, `@degisim: yumuşamak -> açmak` (tutuyorsan), ardından `@onarim: 1a9087b114762227c6276676767a3357635d3ed9`, sonra gövde.

### Hikâye 10: tohum hayri-0188 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0188
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bileklik', fiil 'sevmek', sıfat 'dikkatli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca yemeğini unutmuştu ve acıkmıştı | sandviçini ikiye ayırıp amcayla paylaştı
@tohum: hayri-0188
@degisim: bileklik -> sandviç
Hayri ormandaki kamp yerinde çantasını açtı. Basri Amca da yanına oturdu, ama yemeğini evde unutmuştu. Karnı acıkmıştı ve biraz üzüldü. Hayri çantasından büyük bir peynirli sandviç çıkardı. "Basri Amca, bunu sizinle paylaşalım mı?" diye sordu Hayri. "Olmaz, sonra sen aç kalırsın," dedi Basri Amca. "Bu sandviç benden bile büyük, Basri Amca!" diye abarttı Hayri. Amca bunu duyunca güldü ve başını salladı. Hayri sandviçi dikkatli bir şekilde ikiye böldü. Bir parçayı amcaya uzattı. Basri Amca büyük bir ısırık aldı. "Peynirli sandviçi çok severim, teşekkür ederim, Hayri!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 7: «"Bu sandviç benden bile büyük, Basri Amca!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0188` birebir aynı, `@degisim: bileklik -> sandviç` (tutuyorsan), ardından `@onarim: 6c9024953907c194e7b034033ec5a65d1cf647be`, sonra gövde.

### Hikâye 11: tohum hayri-0189 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0189
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'raf', fiil 'damlamak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı uyuduğu için sürprizi göremiyordu | acıkınca ballı ekmek hazırladı ve kokusu arkadaşını uyandırdı
@tohum: hayri-0189
@degisim: raf -> kabuk
Rüzgar serin serin esiyordu. Hayri, Kamil'in doğum günü için kuma kıvrımlı kabuklarla bir kalp yapmıştı. Ama Kamil kitap okurken uyumuştu ve kalbi göremiyordu. Hayri o sırada çok acıkmıştı. Çantasından iki ekmek ve küçük bir bal kavanozu çıkardı. Kavanozu eğdi ve bal ekmeklerin üstüne yavaş yavaş damladı. Ballı ekmeklerin güzel kokusu Kamil'e kadar geldi. Kamil burnunu oynattı ve gözlerini açtı. "Bu tatlı koku nereden geliyor?" diye sordu Kamil. Hayri ona bir ekmek uzattı ve kumdaki kalbi gösterdi. "İyi ki doğdun, Kamil!" dedi Hayri. "Çok teşekkür ederim, Hayri, bu harika bir sürpriz!" dedi Kamil.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuma kıvrımlı kabuklarla"
   - Cümle 2: «Hayri, Kamil'in doğum günü için kuma kıvrımlı kabuklarla bir kalp yapmıştı.»
   - Açıklama: 'Kıvrımlı' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri o sırada çok acıkmıştı"
   - Cümle 4: «Hayri o sırada çok acıkmıştı.»
   - Açıklama: Açlık sebepsizce araya giriyor ve çözümü tesadüfle getiriyor.
   - Açıklama: Açlık tam o anda sebepsizce beliriyor ve çözümü rastlantıyla getiriyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Çantasından iki ekmek ve küçük bir bal kavanozu çıkardı"
   - Cümle 5: «Çantasından iki ekmek ve küçük bir bal kavanozu çıkardı.»
   - Açıklama: Hayri arkadaşını uyandırmaya çalışmıyor; sorun kendi açlığının yan etkisiyle tesadüfen çözülüyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ballı ekmeklerin güzel kokusu Kamil'e kadar geldi"
   - Cümle 7: «Ballı ekmeklerin güzel kokusu Kamil'e kadar geldi.»
   - Açıklama: Çözüm sebebe bilinçli olarak yönelmiyor, koku tesadüfen arkadaşı uyandırıyor.
   - Açıklama: Çözüm sebebe yönelmiyor; Kamil tesadüfen, Hayri'nin acıkıp yediği ekmeğin kokusuyla uyanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0189` birebir aynı, `@degisim: raf -> kabuk` (tutuyorsan), ardından `@onarim: 10683c1b7a9eb7b8c163c074f3a74b3e0567abc9`, sonra gövde.

### Hikâye 12: tohum hayri-0190 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: parkta nereden geldiği bilinmeyen tatlı bir koku vardı | baklava kokusunu tanıdı ve bankın altında kutuyu buldu
@tohum: hayri-0190
@degisim: dikmek -> koklamak
Bir sabah Hayri ile Mert parkta salıncakta sallanıyordu. Birden rüzgar tatlı bir koku getirdi. İkisi de bu kokunun nereden geldiğini çok merak etti. Hayri burnunu havaya kaldırdı ve derin derin kokladı. "Mert, bu dükkandaki baklavaların kokusu!" dedi Hayri. "Parkta baklava mı var?" diye sordu Mert. Hayri kararlı adımlarla yakındaki banka yürüdü. Bankın altında bir baklava kutusu vardı. Kutunun içinde küçük bir baklava parçası kalmıştı. "Koku bu parçadan geliyormuş," dedi Hayri. Mert kutuyu aldı ve çöpe attı. Hayri çok sevindi, çünkü kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "parkta nereden geldiği bilinmeyen tatlı bir koku vardı"
   - Cümle 0 (plan satırı): «parkta nereden geldiği bilinmeyen tatlı bir koku vardı | baklava kokusunu tanıdı ve bankın altında kutuyu buldu»
   - Açıklama: Bilinmeyen bir koku gerçek bir sorun değil, çocuğun önemseyeceği bir kayıp ya da güçlük yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bu kokunun nereden geldiğini çok merak etti"
   - Cümle 3: «İkisi de bu kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Kokunun kaynağını merak etmek gerçek bir sorun değil, önemsiz bir olay.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bu dükkandaki baklavaların kokusu"
   - Cümle 5: «"Mert, bu dükkandaki baklavaların kokusu!" dedi Hayri.»
   - Açıklama: 'Bu dükkan' hikayede hiç geçmeyen bir yeri gösteriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kararlı adımlarla yakındaki banka"
   - Cümle 7: «Hayri kararlı adımlarla yakındaki banka yürüdü.»
   - Açıklama: 'Kararlı adımlarla' soyut, çocuğa uygun olmayan bir anlatım.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri kararlı adımlarla yakındaki"
   - Cümle 7: «Hayri kararlı adımlarla yakındaki banka yürüdü.»
   - Açıklama: 'Kararlı adımlarla' soyut bir kalıp; 3 yaşındaki çocuk anlamaz.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri kararlı adımlarla yakındaki banka yürüdü"
   - Cümle 7: «Hayri kararlı adımlarla yakındaki banka yürüdü.»
   - Açıklama: Hayri'nin kutunun bankın altında olduğunu nereden bildiği söylenmiyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0190` birebir aynı, `@degisim: dikmek -> koklamak` (tutuyorsan), ardından `@onarim: 7b94e32a6eade6ec51778aa2d247e5f99cc10f27`, sonra gövde.
