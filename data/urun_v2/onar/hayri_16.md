# Editör görevi (onarım): Hayri, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0032 (deneme 4 -> 5)

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
@plan: toprak yumuşaktı ve fidan yana yattı | toprak isteyip ekledi ve iki eliyle sıkıca bastırdı
@tohum: hayri-0032
Bir sabah Hayri, Basri Amca'yla parkta ilk kez fidan dikmeyi denedi. Basri Amca ona küçük, yemyeşil bir fidan verdi. Ama çukurdaki toprak yumuşaktı ve fidan hemen yana yattı. "Bu fidan en büyük ağaç olacak, çok toprak lazım!" diye abarttı Hayri. Basri Amca güldü ve ona bir kova toprak verdi. Hayri bu toprağı çukura ekledi. Sonra toprağı iki eliyle sıkıca bastırdı. Fidan bu kez dimdik durdu. Hayri fidanın yapraklarını okşadı. Basri Amca bir etikete Hayri'nin adını yazdı ve fidana astı. Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastırdı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Bu fidan en büyük ağaç olacak, çok toprak lazım!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez ve konuşma fiili olarak da uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Basri Amca bir etikete Hayri'nin adını yazdı"
   - Cümle 10: «Basri Amca bir etikete Hayri'nin adını yazdı ve fidana astı.»
   - Açıklama: Etiket sebepsiz beliriyor ve olayda bir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0032` birebir aynı, ardından `@onarim: c211486d62d77840d2235560a545efb8927c8ff0`, sonra gövde.

### Hikâye 2: tohum hayri-0033 (deneme 3 -> 4)

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
Rüzgar hafif hafif esiyordu. Hayri parkta Yumak ile oynuyordu. Hayri koşarken baklava dükkanının anahtarı cebinden uzun çimenlere düştü. Hayri yere eğildi ama anahtarı göremedi. Sonra elini yavaşça Yumak'ın burnuna indirdi. "Yumak, anahtarımı bulur musun?" diye sordu Hayri. Yumak onun elini kokladı ve burnunu yere eğdi. Çimenlerin arasında biraz ilerledi, sonra durup havladı. Heyecanlı Hayri hemen oraya koştu. Anahtar çimenlerin arasında parlıyordu. "Aferin sana, Yumak!" dedi Hayri ve anahtarı aldı. Anahtarı bu kez ceketinin iç cebine koydu. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "baklava dükkanının anahtarı cebinden"
   - Cümle 3: «Hayri koşarken baklava dükkanının anahtarı cebinden uzun çimenlere düştü.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız anahtarın etiketi olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0033` birebir aynı, `@degisim: şampuan -> anahtar` (tutuyorsan), ardından `@onarim: 2718cdeadd65e639232c6e44269e4b583134b439`, sonra gövde.

### Hikâye 3: tohum hayri-0034 (deneme 3 -> 4)

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
Evin bahçesinde, masada iki tabak börek duruyordu. Hayri çok acıkmıştı ve Kamil'i bekliyordu. Ama Kamil daha gelmemişti. Birden çitin arkasından ufak bir ses geldi. Hayri bu sesi çok merak etti ve çite doğru yürüdü. Sonra çitin üstünden baktı. Hayri, sabahlığıyla bankta uyuyan Kamil'i buldu. Ses, Kamil'in burnundan geliyordu. "Kamil, uyan, börekler soğuyor!" dedi Hayri. Kamil gözlerini açtı ve güldü. "Beni mi bekliyordun, Hayri?" diye sordu Kamil. "Evet, kahvaltıyı seninle yapmak istedim," dedi Hayri. Kamil hemen Hayri'nin bahçesine geldi. "Teşekkürler, Hayri, hadi birlikte yiyelim!" dedi Kamil.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri, sabahlığıyla bankta uyuyan"
   - Cümle 7: «Hayri, sabahlığıyla bankta uyuyan Kamil'i buldu.»
   - Açıklama: 'Sabahlık' küçük çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sabahlık' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0034` birebir aynı, ardından `@onarim: 7409ade9400392cf3c632e26bd7c86c5c2a886f7`, sonra gövde.

### Hikâye 4: tohum hayri-0035 (deneme 3 -> 4)

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
@plan: top düz tahtadan zıplayıp yere düştü | kenarı yüksek boş bir tepsi kullandı
@tohum: hayri-0035
@degisim: konuşmak -> zıplamak
Evin bahçesinde Hayri çok oynaktı ve yeni bir oyun buldu. Topu düz bir tahtayla çimenin öbür ucuna taşıyacaktı. Ama Hayri yürürken top tahtada zıpladı ve yere düştü. Hayri durdu ve düşündü. Dükkanda baklavaları hep kenarı yüksek bir tepsiyle taşıyordu. Hayri hemen eve koştu ve boş bir tepsi getirdi. Topu tepsiye koydu. Tepsiyi iki eliyle tuttu ve yavaş yavaş yürüdü. Top kenara çarptı ama yere düşmedi. Sonunda Hayri çimenin öbür ucuna vardı. Hayri çok sevindi, çünkü topu düşürmeden bahçeyi geçmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Evin bahçesinde Hayri çok oynaktı"
   - Cümle 1: «Evin bahçesinde Hayri çok oynaktı ve yeni bir oyun buldu.»
   - Açıklama: Kalıcı bir özellik olan 'oynak' bir yere bağlanarak yanlış kullanılmış.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dükkanda baklavaları hep kenarı"
   - Cümle 5: «Dükkanda baklavaları hep kenarı yüksek bir tepsiyle taşıyordu.»
   - Açıklama: Öznesi yok; baklavaları kimin taşıdığı ve hangi dükkan olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0035` birebir aynı, `@degisim: konuşmak -> zıplamak` (tutuyorsan), ardından `@onarim: a59860a3256b881cc921337d4b4e292191ea46ea`, sonra gövde.

### Hikâye 5: tohum hayri-0037 (deneme 3 -> 4)

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
Ağaçların arasında kuşlar ötüyordu. Hayri kamp yerinde tahta topacını çevirdi. Ama toprak yumuşaktı ve topaç hemen devrildi. Hayri topacı iki kez daha çevirdi ama topaç yine toprağa battı. Biraz düşündü. Hayri baklava dükkanında tepsileri hep düz ve sert masaya koyardı. Etrafına baktı ve yerde büyük, düz bir taş gördü. Topacı taşın üstünde çevirdi. Topaç bu kez uzun uzun döndü. Hayri bir, iki, üç, dört, beş diye saydı. Hayri gururlu bir yüzle güldü, çünkü topacını düşürmeden döndürmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri gururlu bir yüzle güldü"
   - Cümle 11: «Hayri gururlu bir yüzle güldü, çünkü topacını düşürmeden döndürmüştü.»
   - Açıklama: 'Gururlu bir yüz' soyut bir duygu ifadesi ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0037` birebir aynı, `@degisim: tasarlamak -> çevirmek` (tutuyorsan), ardından `@onarim: 8997f3ea2ba0971e5a4b8a004117ea5b844550e5`, sonra gövde.

### Hikâye 6: tohum hayri-0038 (deneme 3 -> 4)

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
Parkta tek bir salıncak vardı. Hayri ile Mert aynı anda salıncağa koştu. İkisi de salıncağın zincirini tuttu ve önce binmek istedi. Hayri biraz düşündü. Hayri'nin çalıştığı baklava dükkanında müşteriler hep sırayla beklerdi. "Mert, gel, sırayla binelim," dedi Hayri. "Tamam, önce sen bin, ben de beklerken elmalı lolipopumu yalarım," dedi Mert. Hayri salıncağa bindi ve on kez sallandı. Mert o sırada bir, iki, üç diye saydı. Sonra Hayri indi ve Mert salıncağa bindi. Bu kez Hayri yüksek sesle saydı. Hayri ile Mert çok sevindi, çünkü sırayla ikisi de salıncağa binmişti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "elmalı lolipopumu yalarım"
   - Cümle 7: «"Tamam, önce sen bin, ben de beklerken elmalı lolipopumu yalarım," dedi Mert.»
   - Açıklama: Kartta Mert'e ait böyle bir eşya yok; kapalı dünyaya kart dışı öğe ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ben de beklerken elmalı lolipopumu yalarım"
   - Cümle 7: «"Tamam, önce sen bin, ben de beklerken elmalı lolipopumu yalarım," dedi Mert.»
   - Açıklama: Lolipop sebepsiz beliriyor ve bir daha hiç kullanılmıyor; Mert beklerken lolipop yalamak yerine sayıyor.
   - Açıklama: Lolipop sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0038` birebir aynı, `@degisim: kilit -> salıncak` (tutuyorsan), ardından `@onarim: 7cd5c1561e2d5d964f365c4639459412a56b77ed`, sonra gövde.

### Hikâye 7: tohum hayri-0042 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0042
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'portakal', fiil 'sokulmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu portakal tabağına doğru savurdu | tabağı kayanın arkasına götürdü ve oraya sokuldu
@tohum: hayri-0042
Rüzgar denizden sert sert esiyordu. Hayri kumda portakal dilimleriyle baklava dükkanı oyunu oynuyordu. Ama rüzgar kumu portakal tabağına doğru savurmaya başladı. Hayri kumlu portakal yemek istemiyordu. Etrafına baktı ve büyük bir kaya gördü. Kayanın arkasında rüzgar yoktu. Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti. Tabağı iki eliyle dikkatle kaldırdı ve kayaya götürdü. Sonra kayanın dibine sokuldu ve tabağı kucağına koydu. Burada portakalın üstüne hiç kum gelmedi. Hayri tatlı bir portakal parçası yedi ve güldü. Hayri bundan sonra rüzgarlı günlerde kayanın arkasında oynadı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti"
   - Cümle 7: «Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti.»
   - Açıklama: Baklava dükkanı özelliği bir kez değil iki ayrı yerde kullanılıyor.
   - Açıklama: Tohumdaki baklava özelliği 2. cümlede de geçtiği için bir kez değil iki kez kullanılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti"
   - Cümle 7: «Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti.»
   - Açıklama: Tepsi taşıma bilgisi tabağı birkaç adım götürmek için gereksiz, zorla eklenmiş işlevsiz bir ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Burada portakalın üstüne hiç"
   - Cümle 10: «Burada portakalın üstüne hiç kum gelmedi.»
   - Açıklama: Geçmiş zaman anlatımında 'Burada' yerine 'Orada' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0042` birebir aynı, ardından `@onarim: 98ae472c43b4b5d32c456135f98b2ab9e300c4ac`, sonra gövde.

### Hikâye 8: tohum hayri-0043 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0043
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yelpaze', fiil 'götürmek', sıfat 'ferah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpek gelip kumdan kemiği bozdu | topu uzağa götürdü ve kuma gömdü
@tohum: hayri-0043
@degisim: ferah -> geniş
Kumsal geniş ve serindi. Hayri, Yumak için kumdan kocaman bir kemik yapıyordu. Bu bir sürprizdi ama Yumak topunu bırakıp geldi ve kemiği bozdu. Hayri biraz düşündü. Sonra Yumak'ın kırmızı topunu kayaların yanına götürdü ve kuma gömdü. Topun üstüne küçük bir kum tepesi de yaptı. Yumak topun kokusunu aldı ve orada uzun uzun kumu eşeledi. Hayri hemen işine döndü ve kum kemiğini bitirdi. Üstüne yelpaze gibi beyaz kabuklar dizdi. "Yumak, gel, sana dünyanın en büyük kemiğini yaptım!" dedi Hayri abartarak. Yumak topuyla koşup geldi ve kuyruğunu salladı. Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu sakladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Üstüne yelpaze gibi beyaz kabuklar dizdi"
   - Cümle 9: «Üstüne yelpaze gibi beyaz kabuklar dizdi.»
   - Açıklama: 'Yelpaze gibi' benzetmesi küçük çocuk için belirsiz bir mecaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 10: «"Yumak, gel, sana dünyanın en büyük kemiğini yaptım!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' ve 'dünyanın en büyük' soyut, 3 yaşındaki çocuğun bilmeyeceği bir anlatım.
   - Açıklama: 'Abartarak' soyut bir kavram ve 'dünyanın en büyük' abartısı 3 yaşındaki çocuğa uygun değil.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu sakladı"
   - Cümle 12: «Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu sakladı.»
   - Açıklama: 'Bundan sonra' ile gelecekteki alışkanlık anlatılıyor ama fiil tek seferlik geçmişte; 'saklayacaktı' ya da 'saklardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0043` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: f15c04386afd109d139dbeb88349c835c6d39836`, sonra gövde.

### Hikâye 9: tohum hayri-0044 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0044
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'basamak', fiil 'buruşturmak', sıfat 'çabuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: kalp gibi bir bulut çıktı ama arkadaşı uyuyordu | sandviçi burnuna yaklaştırdı ve arkadaşını uyandırdı
@tohum: hayri-0044
Hayri kamp yerinde çok acıkmıştı ve iki sandviç yapıyordu. Birden gökyüzünde kalp şeklinde büyük bir bulut gördü. Hayri bulutu Kamil'e göstermek istedi ama Kamil basamakta uyuyordu. Hayri çabuk olmalıydı, çünkü bulut yavaş yavaş dağılıyordu. "Kamil, uyan, bak!" diye seslendi Hayri. Ama Kamil uyanmadı. Hayri elindeki sandviçi Kamil'in burnuna yaklaştırdı. Kamil sandviçi kokladı, burnunu buruşturdu ve gözlerini açtı. "Kamil, yukarı bak, bulut kalp gibi!" dedi Hayri. Kamil başını kaldırdı ve bulutu gördü. İkisi basamağa oturdu, sandviç yedi ve buluta baktı. Hayri çok sevindi, çünkü bulutu Kamil ile birlikte görmüştü.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sandviçi burnuna yaklaştırdı"
   - Cümle 0 (plan satırı): «kalp gibi bir bulut çıktı ama arkadaşı uyuyordu | sandviçi burnuna yaklaştırdı ve arkadaşını uyandırdı»
   - Açıklama: Plan satırında 'burnuna' zamirinin kimin burnunu gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0044` birebir aynı, ardından `@onarim: 4a1a7b826c2fc8d9894a91ba6870fab27cc9fb7f`, sonra gövde.

### Hikâye 10: tohum hayri-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0045
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'flüt', fiil 'belirmek', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: iki çocuk da tek flütü ilk çalmak istedi | sırayla çalmayı ve beklerken baklava yemeyi buldu
@tohum: hayri-0045
Rüzgar ağaçların arasında esiyordu. Akın kamp yerinde küçük bir flüt çıkardı ve Hayri'ye gösterdi. İkisi de onu ilk çalmak istedi, ama tek flüt vardı. Hayri biraz düşündü ve çantasını açtı. İçinde, çalıştığı baklava dükkanından getirdiği tatlılar vardı. Hayri sırayla çalmayı söyledi. Bir çocuk çalarken öteki baklava yiyecekti. Böylece bekleyen çocuk da sıkılmayacaktı. Önce Akın yavaş bir şarkı çaldı. Hayri onu dinlerken bir baklava yedi. Sonra sıra Hayri'ye geldi. Hayri neşeli bir şarkı çaldı, Akın da yapışkan bir baklava yedi. Akın'ın yüzünde kocaman bir gülümseme belirdi. Hayri bundan sonra flütü hep Akın ile sırayla çaldı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı baklava dükkanından getirdiği tatlılar vardı"
   - Cümle 5: «İçinde, çalıştığı baklava dükkanından getirdiği tatlılar vardı.»
   - Açıklama: Baklava sıra sorununun sebebine yönelmiyor, çözüme sonradan eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0045` birebir aynı, ardından `@onarim: 3994394eb9977744fa6075ccd8443bf870bd910c`, sonra gövde.

### Hikâye 11: tohum hayri-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0046
- yer: park (Mahallenin çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'mıknatıs', fiil 'ölçmek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuruydu ve pasta hep dağıldı | kumu ıslattı ve eski kovayla pasta yaptı
@tohum: hayri-0046
@degisim: mıknatıs -> kova
Parkın kum havuzunda Hayri pasta yapma oyunu oynuyordu. Hayri pastayı abartmak istedi, pasta kule kadar yüksek olacaktı. Ama kum çok kuruydu ve pasta hep dağıldı. Hayri biraz düşündü ve su şişesini açtı. Suyu oyuncak bardağıyla ölçtü ve iki bardak kuma döktü. Islak kumu eski kovasına sıkıca bastırdı. Sonra kovayı ters çevirdi ve yavaşça kaldırdı. Kumdan pasta bu kez hiç yıkılmadı. Hayri onun üstüne iki kat daha yaptı. Pasta bir kule gibi yükseldi. Hayri onu yapraklarla süsledi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri pastayı abartmak istedi"
   - Cümle 2: «Hayri pastayı abartmak istedi, pasta kule kadar yüksek olacaktı.»
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; 'büyük yapmak' kastediliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "pastayı abartmak istedi"
   - Cümle 2: «Hayri pastayı abartmak istedi, pasta kule kadar yüksek olacaktı.»
   - Açıklama: 'Pastayı abartmak' fiil ile nesnenin uyuşmadığı yanlış bir kullanım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri pastayı abartmak istedi"
   - Cümle 2: «Hayri pastayı abartmak istedi, pasta kule kadar yüksek olacaktı.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri pastayı abartmak istedi"
   - Cümle 2: «Hayri pastayı abartmak istedi, pasta kule kadar yüksek olacaktı.»
   - Açıklama: Karttaki özellik olayları abartmak iken burada abartmak pastayı büyütmek anlamında kullanılıyor ve çözüme katkısı yok.
   - Açıklama: Karttaki özellik olayları abartmak; burada kum pastasını büyük yapmak olarak karttan farklı kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0046` birebir aynı, `@degisim: mıknatıs -> kova` (tutuyorsan), ardından `@onarim: 1ece2ced25102663f5c283937fea24355e6a7592`, sonra gövde.

### Hikâye 12: tohum hayri-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0047
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pizza', fiil 'ıslatmak', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar şapkayı uçurdu ve şapka kayboldu | kıyıda dikkatle aradı ve taşların arkasında buldu
@tohum: hayri-0047
@degisim: pizza -> şapka
Rüzgar kıyıda hızlı esiyordu. Hayri denizin kenarında yürüyor ve dalgaları izliyordu. Birden rüzgar mavi şapkasını başından kaptı ve uçurdu. Hayri hiç abartmadı, durdu ve etrafa dikkatle baktı. Önce dalgaların ıslattığı çamurlu kumda aradı, ama şapka orada yoktu. Rüzgar büyük taşlara doğru esiyordu. Hayri de o yöne yürüdü ve taşların arkasına baktı. Şapka orada, kuru bir taşın üstündeydi. Hayri şapkayı aldı ve başına sıkıca taktı. Hayri çok sevindi, çünkü kaybolan şapkasını bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri hiç abartmadı, durdu"
   - Cümle 4: «Hayri hiç abartmadı, durdu ve etrafa dikkatle baktı.»
   - Açıklama: 'Abartmak' soyut bir kavram ve burada anlamsız kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri hiç abartmadı"
   - Cümle 4: «Hayri hiç abartmadı, durdu ve etrafa dikkatle baktı.»
   - Açıklama: Kartın özellikler alanındaki abartma özelliği olumsuzlanarak kullanılıyor, işe yarar biçimde değil.
   - Açıklama: Tohumdaki özellik abartmayı sevmek, ama hikayede Hayri abartmıyor; özellik karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0047` birebir aynı, `@degisim: pizza -> şapka` (tutuyorsan), ardından `@onarim: 77c0afbef4d3ce5a3af9c1b4509c4c810d6b74b7`, sonra gövde.
