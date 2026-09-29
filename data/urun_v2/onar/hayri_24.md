# Editör görevi (onarım): Hayri, onarım partisi 24

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar24.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0081 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0081
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'top', fiil 'saklamak', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga kum tepesini yıktı ve top kayboldu | kumun yüksek kalan yerini kazdı ve topu buldu
@tohum: hayri-0081
@degisim: nazik -> sarı
Dalgaların sesi kıyıdan geliyordu. Hayri sarı topunu kuma sakladı ve abartarak kocaman bir tepe yaptı. Ama bir dalga tepeyi yıktı ve Hayri topun yerini bulamadı. Kumun her yeri aynı görünüyordu. Hayri eğildi ve kuma dikkatle baktı. Tepe çok büyük olduğu için bir yerde kum biraz yüksek kalmıştı. Hayri orayı elleriyle kazdı. Kumun altından sarı top çıktı. Hayri topu havaya kaldırdı ve güldü. Bu sefer topu dalgalardan uzağa, kuru kuma gömdü. Üstüne yine kocaman bir tepe yaptı. Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartarak kocaman bir tepe"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve abartarak kocaman bir tepe yaptı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve abartarak kocaman bir"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve abartarak kocaman bir tepe yaptı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "abartarak kocaman bir tepe yaptı"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve abartarak kocaman bir tepe yaptı.»
   - Açıklama: Kartın özellikler alanında abartmak olayları abartmaktır; burada yalnız büyük bir kum tepesi yapmak olarak kullanılıyor.
   - Açıklama: Karttaki özellik olayları abartmak iken burada yalnız büyük bir kum tepesi yapmak olarak kullanılıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hayri sarı topunu kuma sakladı"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve abartarak kocaman bir tepe yaptı.»
   - Açıklama: Topu kuma gömüp üstüne tepe yapmanın amacı söylenmiyor, bu yüzden sorunun ve hedefin anlamı belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0081` birebir aynı, `@degisim: nazik -> sarı` (tutuyorsan), ardından `@onarim: 6262f263791e8d14a02951ec9b904de13065a211`, sonra gövde.

### Hikâye 2: tohum hayri-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0083
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tekne', fiil 'silkmek', sıfat 'kalın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek kuru yapraklarla oynuyordu ve tekneye gelmedi | ekmekten bir parça uzatıp köpeği tekneye çağırdı
@tohum: hayri-0083
Ormanda büyük ağaçların altında kalın bir kütük vardı. Hayri kütüğe oturdu ve onu bir tekne yaptı. Ama Yumak tekneye gelmedi, çünkü kuru yapraklarla oynuyordu. "Yumak, gel, yola çıkıyoruz!" dedi Hayri. Yumak ona hiç bakmadı. O sırada Hayri acıktı ve çantasından ekmeğini çıkardı. Ekmekten küçük bir parça kopardı ve Yumak'a uzattı. "Bu parça senin, Yumak!" dedi Hayri. Yumak ekmeğin kokusunu aldı ve koşarak geldi. Tekneye atladı ve üstündeki yaprakları silkti. Sonra parçayı yedi ve kuyruğunu salladı. Hayri de ekmeğin kalanını yedi. Hayri ile Yumak tekne oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kütüğe oturdu ve onu bir tekne yaptı"
   - Cümle 2: «Hayri kütüğe oturdu ve onu bir tekne yaptı.»
   - Açıklama: Kütük tekneye dönüştürülmüyor; 'onu tekne yaptı' yerine oyunda tekne sayması anlatılmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu bir tekne yaptı"
   - Cümle 2: «Hayri kütüğe oturdu ve onu bir tekne yaptı.»
   - Açıklama: Hayri kütüğü tekne yapmadı, yalnız tekne gibi oynadı; fiil anlamca yanlış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri acıktı ve çantasından ekmeğini çıkardı"
   - Cümle 6: «O sırada Hayri acıktı ve çantasından ekmeğini çıkardı.»
   - Açıklama: Çözümü getiren ekmek, Hayri'nin düşünmesinden değil tesadüfen acıkmasından çıkıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri acıktı"
   - Cümle 6: «O sırada Hayri acıktı ve çantasından ekmeğini çıkardı.»
   - Açıklama: Çözümü getiren ekmek, Hayri'nin tesadüfen acıkmasıyla ortaya çıkıyor; çözüm sebepsizce geliyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Tekneye atladı ve üstündeki yaprakları silkti"
   - Cümle 10: «Tekneye atladı ve üstündeki yaprakları silkti.»
   - Açıklama: 'Üstündeki' kelimesinin teknenin mi köpeğin mi üstünü gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0083` birebir aynı, ardından `@onarim: 4f24ad05683cf73d0191b2126f06571ace09d1a1`, sonra gövde.

### Hikâye 3: tohum hayri-0084 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0084
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ay', fiil 'vermek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: koşarken arkadaşına çarptı ve onun sütü döküldü | özür diledi ve ona baklava verdi
@tohum: hayri-0084
Bir akşam ormandaki kamp yerinde gökyüzüne büyük bir ay çıktı. Hayri, Mert'e gökyüzünü göstermek için koşarken ona çarptı. Mert'in elindeki ılık süt yere döküldü. Mert boş bardağına üzgün üzgün baktı. Hayri hemen durdu ve Mert'in yanına gitti. "Özür dilerim, Mert, koşmamalıydım," dedi Hayri. Sonra çantasından küçük bir kutu çıkardı. Kutuda, çalıştığı baklava dükkanından getirdiği tatlılar vardı. Hayri en büyük baklavayı Mert'e verdi. Mert baklavayı yedi ve gülümsedi. "Çok güzelmiş, teşekkür ederim," dedi Mert. "Hadi, Mert, şimdi aya birlikte bakalım!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra çantasından küçük bir kutu çıkardı"
   - Cümle 7: «Sonra çantasından küçük bir kutu çıkardı.»
   - Açıklama: Baklava kutusu önceden kurulmadan çantadan çıkıyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0084` birebir aynı, ardından `@onarim: 794d89574694a4dde7d7440c3f96c0021d774a0f`, sonra gövde.

### Hikâye 4: tohum hayri-0085 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0085
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kabuk', fiil 'kurutmak', sıfat 'kırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuru olduğu için yüksek kale yıkıldı | kovayla su getirip kumu ıslattı
@tohum: hayri-0085
@degisim: kurutmak -> ıslatmak
Parkın kum havuzunda Hayri bir kale yapıyordu. Hayri abartarak çok yüksek bir kale yapmaya çalışıyordu. Ama kum çok kuruydu ve kale her seferinde yıkıldı. Hayri kırmızı kovasını aldı ve çeşmeden su doldurdu. Suyu döktü ve kumu iyice ıslattı. Islak kum artık sıkı sıkı duruyordu. Hayri kovayı kumla doldurdu ve ters çevirdi. Kalın bir ağaç kabuğuyla duvarları düzeltti. Kovayı bir kez daha doldurdu ve üstüne bir kule yaptı. Bu sefer hiçbir şey yıkılmadı. Hayri çok sevindi, çünkü yüksek kalesi artık dimdik duruyordu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak çok yüksek"
   - Cümle 2: «Hayri abartarak çok yüksek bir kale yapmaya çalışıyordu.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez ve burada yanlış kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak çok yüksek bir kale yapmaya çalışıyordu"
   - Cümle 2: «Hayri abartarak çok yüksek bir kale yapmaya çalışıyordu.»
   - Açıklama: Karttaki özellik olayları abartmak; burada aşırıya kaçmak olarak kullanılıyor ve çözümde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak çok yüksek bir kale"
   - Cümle 2: «Hayri abartarak çok yüksek bir kale yapmaya çalışıyordu.»
   - Açıklama: Karttaki özellik olayları abartmak iken burada yüksek kale yapmaya çalışmak olarak kullanılıyor ve çözüme katkı vermiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kalın bir ağaç kabuğuyla duvarları düzeltti"
   - Cümle 8: «Kalın bir ağaç kabuğuyla duvarları düzeltti.»
   - Açıklama: Ağaç kabuğu kum havuzunda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0085` birebir aynı, `@degisim: kurutmak -> ıslatmak` (tutuyorsan), ardından `@onarim: 7a4deaaced90e874c66999eed28f6c9caf9d5489`, sonra gövde.

### Hikâye 5: tohum hayri-0088 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0088
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kasa', fiil 'aydınlatmak', sıfat 'harika'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kumdan baklavayı kesecek bir şeyi yoktu | düz bir deniz kabuğuyla kumu kesti
@tohum: hayri-0088
Deniz kıyısında kumun üstünde boş bir tahta kasa duruyordu. Hayri kasayı bir baklava tepsisi yaptı. Kasaya ıslak kum doldurdu ama kumu kesecek bir şeyi yoktu. Hayri kıyıda yürüdü ve yere dikkatle baktı. Kumda düz ve ince bir deniz kabuğu buldu. Hayri baklava dükkanında çalıştığı için baklavanın nasıl kesildiğini iyi biliyordu. Kabukla kumu küçük kareler halinde kesti. Sonra her karenin üstüne fıstık yerine küçük bir taş koydu. Güneş kasayı aydınlattı ve ıslak kum parladı. Harika bir tepsi olmuştu. Hayri dükkan oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hayri kasayı bir baklava tepsisi yaptı"
   - Cümle 2: «Hayri kasayı bir baklava tepsisi yaptı.»
   - Açıklama: Yapı bozuk; 'kasadan bir baklava tepsisi yaptı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kumu kesecek bir şeyi yoktu"
   - Cümle 3: «Kasaya ıslak kum doldurdu ama kumu kesecek bir şeyi yoktu.»
   - Açıklama: Sorun yalnız bir eksiklik olarak konuyor, sebebi söylenmiyor ve çocuğun önemseyeceği bir derde dönüşmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0088` birebir aynı, ardından `@onarim: 412c5a8234fd6e499fc5de701baf54798495d11a`, sonra gövde.

### Hikâye 6: tohum hayri-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0089
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kırıntı', fiil 'yeşermek', sıfat 'hazırlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: köpek çok hızlıydı ve kırıntılar çabuk bitti | çantadan ikinci simidi çıkarıp oyuna devam etti
@tohum: hayri-0089
@degisim: yeşermek -> zıplamak
Hayri parkta Yumak ile koku oyunu oynuyordu. Simit kırıntılarını çimlere saklıyordu, Yumak da onları kokluyor ve buluyordu. Ama Yumak çok hızlıydı ve simit çabuk bitti. Yumak kuyruğunu salladı ve Hayri'ye baktı. Hayri de o sırada acıkmıştı. Neyse ki hazırlıklı gelmişti ve çantasında bir simit daha vardı. Simidi ikiye ayırdı ve yarısını kendisi yedi. Öbür yarısını küçük küçük kırıntı yaptı ve çimlerin arasına serpti. "Hadi, Yumak, bul bakalım!" dedi Hayri. Yumak burnunu yere yaklaştırdı ve çimlerde koştu. Her kırıntıyı buldukça sevinçle zıpladı ve havladı. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü oyunları yarım kalmamıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri de o sırada acıkmıştı"
   - Cümle 5: «Hayri de o sırada acıkmıştı.»
   - Açıklama: Hayri'nin acıkması olaydan çıkmıyor ve sorunun çözümüne hiçbir katkı yapmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Neyse ki hazırlıklı gelmişti"
   - Cümle 6: «Neyse ki hazırlıklı gelmişti ve çantasında bir simit daha vardı.»
   - Açıklama: 'Neyse ki' ve 'hazırlıklı' soyut ifadeler, küçük çocuk için uygun değil.
   - Açıklama: 'Hazırlıklı' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çimlerin arasına serpti"
   - Cümle 8: «Öbür yarısını küçük küçük kırıntı yaptı ve çimlerin arasına serpti.»
   - Açıklama: Çim kayboldu denmişken sonra kırıntılar çimlerin arasına serpiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0089` birebir aynı, `@degisim: yeşermek -> zıplamak` (tutuyorsan), ardından `@onarim: 9316bac0d243ce05baf97f6165172d9372f5a4cb`, sonra gövde.

### Hikâye 7: tohum hayri-0090 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0090
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'saman', fiil 'birleştirmek', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kabuğun öbür yarısı yoktu çünkü dalgalar onu kırmıştı | kıyıda dolaşıp öbür yarısını buldu ve birleştirdi
@tohum: hayri-0090
@degisim: saman -> kabuk
Deniz kıyısında ıslak kumun üstünde tuhaf bir kabuk vardı. Hayri onu aldı ve abartarak bir hazine sandı. Ama kabuğun öbür yarısı yoktu, çünkü dalgalar onu kırmıştı. Kabuğun üstünde pembe ve mavi çizgiler vardı. Hayri öbür yarısını bulmak için kıyıda yavaş yavaş yürüdü. Kumdaki her kabuğa dikkatle baktı. Sonunda taşların arasında aynı çizgileri olan bir parça gördü. Hayri iki parçayı yan yana koydu ve birleştirdi. Parçalar tam oturdu ve çizgiler bir yıldız şekli yaptı. Hayri kabuğu iki eliyle tuttu ve güneşte uzun uzun baktı. Hayri çok sevindi, çünkü tuhaf kabuğun öbür yarısını bulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "abartarak bir hazine sandı"
   - Cümle 2: «Hayri onu aldı ve abartarak bir hazine sandı.»
   - Açıklama: 'Abartarak sanmak' anlamca yanlış bir kullanım.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aldı ve abartarak bir hazine sandı"
   - Cümle 2: «Hayri onu aldı ve abartarak bir hazine sandı.»
   - Açıklama: 'Abartarak sanmak' anlamca uyumsuz; zarf fiile uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartarak bir hazine sandı"
   - Cümle 2: «Hayri onu aldı ve abartarak bir hazine sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "abartarak bir hazine sandı"
   - Cümle 2: «Hayri onu aldı ve abartarak bir hazine sandı.»
   - Açıklama: Abartma özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kabuğu iki eliyle tuttu ve güneşte uzun uzun baktı"
   - Cümle 10: «Hayri kabuğu iki eliyle tuttu ve güneşte uzun uzun baktı.»
   - Açıklama: Ortak nesne 'kabuğu' belirtme ekinde, 'baktı' ise yönelme ister; ek uyumsuzluğu var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0090` birebir aynı, `@degisim: saman -> kabuk` (tutuyorsan), ardından `@onarim: 788336946bf0a36be48f632803ab319a629dd297`, sonra gövde.
