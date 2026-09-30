# Editör görevi (onarım): Hayri, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0014 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0014
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'pul', fiil 'boyamak', sıfat 'sabırsız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: rüzgar amcanın pulunu uçurdu ve pul kayboldu | ekmeğini yemeden baktı ve pulu reçelin üstünde buldu
@tohum: hayri-0014
@degisim: sabırsız -> reçelli
Hayri parkta reçelli ekmeğini yemek istiyordu, çünkü çok acıkmıştı. Yanında Basri Amca bir zarf boyuyordu ve pulunu banka koymuştu. Birden rüzgar esti ve pulu Hayri'ye doğru uçurdu. "Eyvah, pulum kayboldu!" dedi Basri Amca. Hayri ekmeğini yemedi ve önce pulu aramak istedi. Yere ve bankın altına baktı ama pulu göremedi. Sonra elindeki ekmeğe baktı. Küçük pul ekmeğin üstündeki reçele yapışmıştı. Hayri pulu reçelden yavaşça ayırdı ve Basri Amca'ya uzattı. Basri Amca pulu sevinçle zarfa yapıştırdı. "Teşekkürler, Hayri, iyi ki ekmeğini hemen yemedin!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "pulu Hayri'ye doğru uçurdu"
   - Cümle 3: «Birden rüzgar esti ve pulu Hayri'ye doğru uçurdu.»
   - Açıklama: İlk üç cümlede pul yalnız Hayri'ye doğru uçuyor; pulun kaybolduğu sorunu ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0014` birebir aynı, `@degisim: sabırsız -> reçelli` (tutuyorsan), ardından `@onarim: 5a1dc500fd08aa6dadf2bcaecd95ba5a2a4ad733`, sonra gövde.

### Hikâye 2: tohum hayri-0016 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0016
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yapıştırıcı', fiil 'izlemek', sıfat 'bembeyaz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: rüzgar bembeyaz şapkayı uçurdu ve şapka kayboldu | uçan kumları izleyip şapkayı kayaların arasında buldu
@tohum: hayri-0016
@degisim: yapıştırıcı -> şapka
Deniz kıyısında rüzgar çok esiyordu. Hayri ile Kamil kumda oturmuş denize bakıyordu. Birden rüzgar Kamil'in bembeyaz şapkasını uçurdu ve şapka kayboldu. "Eyvah, şapkam gitti!" dedi Kamil. "Bu rüzgar bütün kumsalı götürecek!" dedi Hayri. Hayri biraz abartmıştı, ama rüzgar kumları gerçekten taşıyordu. Sonra Hayri havada uçan kum tanelerini dikkatle izledi. Kumlar hep büyük kayalara doğru uçuyordu. Hayri o yöne yürüdü ve kayaların arkasına baktı. Şapka iki kayanın arasına sıkışmıştı. Hayri şapkayı aldı ve Kamil'e götürdü. "Teşekkürler, Hayri!" dedi Kamil ve şapkasını taktı. Hayri bundan sonra uçan eşyaları rüzgarın estiği yönde aradı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 6: «Hayri biraz abartmıştı, ama rüzgar kumları gerçekten taşıyordu.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki bir çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0016` birebir aynı, `@degisim: yapıştırıcı -> şapka` (tutuyorsan), ardından `@onarim: 8b3ba5c314366445079e6415c6f8d3672376a448`, sonra gövde.

### Hikâye 3: tohum hayri-0017 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0017
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'forma', fiil 'göstermek', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: rüzgar formayı ipten uçurdu ve forma kayboldu | çadırın üstünde bulup dalla aşağı çekti
@tohum: hayri-0017
Bir sabah Hayri kamp yerinde çikolatalı kekini yemeye hazırlanıyordu, çünkü çok acıkmıştı. "Hayri, formam rüzgarda ipten uçtu!" dedi Mert koşarak. Hayri keki hemen çantasına geri koydu. "Formayı nereye astın, Mert, bana gösterir misin?" diye sordu Hayri. Mert ona çadırın yanındaki ipi gösterdi. Hayri ipin altına baktı ama yerde forma yoktu. Sonra başını kaldırdı ve çadırın üstüne baktı. Mavi forma çadırın tepesinde duruyordu. Hayri uzun bir dal aldı ve formayı yavaşça aşağı çekti. Mert formasını giydi ve çok sevindi. Sonra Hayri kekini ikiye böldü ve Mert'le paylaştı. İkisi keklerini yedi ve mutlu mutlu oyuna başladı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çadırın üstünde bulup dalla aşağı çekti"
   - Cümle 0 (plan satırı): «rüzgar formayı ipten uçurdu ve forma kayboldu | çadırın üstünde bulup dalla aşağı çekti»
   - Açıklama: Gövdede forma dalla aşağı çekilmiyor; plan çözümü gövdeyle uyuşmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0017` birebir aynı, ardından `@onarim: b31888e576588cec59390602fbedd54057e443e6`, sonra gövde.

### Hikâye 4: tohum hayri-0062 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0062
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'ceket', fiil 'parıldamak', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: arkadaşının sandviçi kuma düştü ve kirlendi | kendi simidini ikiye böldü ve arkadaşına verdi
@tohum: hayri-0062
Deniz kıyısında su güneşte parıldıyordu. Hayri ile Mert kumun üstünde oturuyordu. Birden Mert'in sandviçi elinden kaydı ve kuma düştü. Sandviç kum yüzünden çok kirliydi ve artık yenmezdi. Mert üzgün üzgün ona baktı. Hayri de çok acıkmıştı. Ama Hayri ceketinin cebinden simidini çıkardı. Simidi ikiye böldü ve büyük parçayı Mert'e verdi. Mert gülümsedi ve Hayri'ye sarıldı. Sonra Mert kumdaki sandviçi alıp çöpe attı. Hayri ile Mert yan yana oturup simidi mutlu mutlu yediler.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kumdaki sandviçi alıp çöpe attı"
   - Cümle 10: «Sonra Mert kumdaki sandviçi alıp çöpe attı.»
   - Açıklama: Çöp kaybolmuşken Mert sandviçi çöpe atıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0062` birebir aynı, ardından `@onarim: 044728d4820f07664009513dfbe76ef63cef84e1`, sonra gövde.

### Hikâye 5: tohum hayri-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0098
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabak', fiil 'yıkamak', sıfat 'düz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: sürpriz için aldığı baklavalar kutuda dağılmıştı | baklavaları dükkandaki gibi düz tabağa dizdi
@tohum: hayri-0098
Bir sabah Hayri evde Mert için bir sürpriz hazırlıyordu. O gün Mert'in doğum günüydü. Ama dükkandan getirdiği baklavalar kutuda dağılmıştı, çünkü yolda kutu çok sallanmıştı. Hayri kutuya baktı ve biraz düşündü. Hayri dükkanda her gün baklavaları tepsiye diziyordu. Önce ellerini sabunla yıkadı. Sonra masadaki büyük ve düz tabağı aldı. Hayri baklavaları dükkanda yaptığı gibi tabağa sıra sıra dizdi. Her sırada dört baklava vardı. Az sonra Mert eve geldi. "Doğum günün kutlu olsun, Mert!" dedi Hayri. Mert tabağı görünce çok sevindi. "Tıpkı dükkandaki gibi olmuş, teşekkürler, Hayri!" dedi Mert.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce ellerini sabunla yıkadı"
   - Cümle 6: «Önce ellerini sabunla yıkadı.»
   - Açıklama: Çözüm el yıkama, tabak alma ve dizme olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0098` birebir aynı, ardından `@onarim: 657fde53d23572926e93140adca4a28a3f949eba`, sonra gövde.

### Hikâye 6: tohum hayri-0099 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0099
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'telefon', fiil 'kurmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: rüzgar esti ve boş kağıt tabak yere uçtu | acıkınca tabağa yemek koydu ve tabak ağırlaştı
@tohum: hayri-0099
@degisim: telefon -> tabak
Bir sabah Hayri kamp yerinde evcilik oyunu oynuyordu. Düz bir kütüğün üstüne düzenli bir sofra kurmuştu. Ama rüzgar esti ve boş kağıt tabak yere uçtu. Hayri tabağı yerden aldı ve kütüğe geri koydu. Rüzgar yine esti ve tabak kıpırdadı. Hayri çok acıkmıştı ve yanındaki yemek sepetine baktı. Sepetten ekmek, peynir ve iki elma aldı. Hepsini tabağın üstüne koydu. Dolu tabak ağırlaştı ve rüzgarda hiç kıpırdamadı. Sonra Hayri kütüğün yanına oturdu ve yemeğini afiyetle yedi. Hayri çok sevindi, çünkü tabağı rüzgarda bir daha uçmamıştı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "boş kağıt tabak yere uçtu"
   - Cümle 3: «Ama rüzgar esti ve boş kağıt tabak yere uçtu.»
   - Açıklama: Boş tabağın uçup hemen geri konması çocuğun önemseyeceği bir sorun olmaktan çok önemsiz bir olay.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri çok acıkmıştı ve yanındaki yemek sepetine baktı"
   - Cümle 6: «Hayri çok acıkmıştı ve yanındaki yemek sepetine baktı.»
   - Açıklama: Çözüm tabağı sabitleme amacından değil açlıktan rastlantıyla geliyor, sebebe bilerek yönelmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ve yanındaki yemek sepetine baktı"
   - Cümle 6: «Hayri çok acıkmıştı ve yanındaki yemek sepetine baktı.»
   - Açıklama: Çözüm soruna yönelen bir düşünceden değil, sebepsizce gelen açlıktan çıkıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "tabağı rüzgarda bir daha uçmamıştı"
   - Cümle 11: «Hayri çok sevindi, çünkü tabağı rüzgarda bir daha uçmamıştı.»
   - Açıklama: Hayri yemeği yiyip tabağı yeniden boşaltmışken tabağın bir daha uçmadığı söyleniyor.
   - Açıklama: Hayri yemeği yiyince tabak yeniden boşalıyor, yine de tabağın bir daha uçmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0099` birebir aynı, `@degisim: telefon -> tabak` (tutuyorsan), ardından `@onarim: 8b97fae07110863d2407768dfa79e390e3b8f06d`, sonra gövde.

### Hikâye 7: tohum hayri-0100 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0100
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yelkenli', fiil 'tatmak', sıfat 'düzgün'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: yerdeki yelkenliyi görmedi ve üstüne bastı | özür diledi ve arkadaşıyla yeni bir yelkenli katladı
@tohum: hayri-0100
@degisim: tatmak -> katlamak
Hayri ile Akın bahçede kağıttan yelkenli yapıyordu. Akın mavi yelkenliyi çok düzgün yapmış ve çimlere koymuştu. Hayri yerdeki yelkenliyi görmedi ve üstüne bastı. Kağıt ezildi ve Akın çok üzüldü. Hayri hemen Akın'ın yanına oturdu. "Özür dilerim, Akın, onu görmedim," dedi Hayri. Sonra Hayri abartarak kollarını iki yana açtı. "Şimdi sana dünyanın en güzel yelkenlisini yapacağım!" dedi Hayri. Akın buna güldü ve Hayri'ye yeni bir kağıt verdi. İkisi birlikte yeni bir tane katladı. Yeni yelkenli de çok güzel oldu. "Bu gerçekten çok güzel, Hayri," dedi Akın. Hayri bundan sonra bahçede yürürken önce yere baktı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Akın bahçede kağıttan yelkenli yapıyordu"
   - Cümle 1: «Hayri ile Akın bahçede kağıttan yelkenli yapıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kollarını"
   - Cümle 7: «Sonra Hayri abartarak kollarını iki yana açtı.»
   - Açıklama: 'Abartarak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra Hayri abartarak kollarını"
   - Cümle 7: «Sonra Hayri abartarak kollarını iki yana açtı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu gerçekten çok güzel"
   - Cümle 12: «"Bu gerçekten çok güzel, Hayri," dedi Akın.»
   - Açıklama: Anlatıcının hemen önceki cümlede söylediği 'çok güzel oldu' replikte gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0100` birebir aynı, `@degisim: tatmak -> katlamak` (tutuyorsan), ardından `@onarim: 3e3d29e37fc190ad8cf0af6f37466d731fbac565`, sonra gövde.

### Hikâye 8: tohum hayri-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0101
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'fermuar', fiil 'yırtılmak', sıfat 'yumuşacık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: kağıt torba yırtıldı ve kozalaklar yere döküldü | komik bir sesle yardım istedi ve kozalakları çantaya koydu
@tohum: hayri-0101
Hayri parkta çam ağacının altında bir sürü kozalak fark etti. Kozalakları kağıt bir torbada topladı. Ama torba ağırlaştı ve yırtıldı, kozalaklar yere döküldü. Basri Amca yakındaki bankta oturuyordu. "Basri Amca, bin tane kozalak her yere dağıldı!" diye abartarak seslendi Hayri. Basri Amca bu söze güldü ve yanına geldi. "Bin tane değil ama çok kozalak var," dedi Basri Amca. Sonra Hayri'ye yumuşacık bir kumaş çanta verdi. Çantanın sağlam bir fermuarı vardı. Hayri kozalakları tek tek çantaya koydu. Sonra fermuarı dikkatle kapattı. "Teşekkürler, Basri Amca," dedi Hayri. Hayri çok sevindi, çünkü bütün kozalaklarını yeniden toplamıştı.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "komik bir sesle yardım istedi"
   - Cümle 0 (plan satırı): «kağıt torba yırtıldı ve kozalaklar yere döküldü | komik bir sesle yardım istedi ve kozalakları çantaya koydu»
   - Açıklama: Gövdede Hayri komik bir sesle değil abartarak sesleniyor; plan çözümü doğru söylemiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak seslendi"
   - Cümle 5: «"Basri Amca, bin tane kozalak her yere dağıldı!" diye abartarak seslendi Hayri.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0101` birebir aynı, ardından `@onarim: 9404329d851d08e5cb020d5028f1c17fe42faf63`, sonra gövde.

### Hikâye 9: tohum hayri-0102 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0102
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'anahtar', fiil 'güneşlenmek', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: koşarken kum sıçradı ve anahtar kayboldu | özür diledi ve anahtarı kumun altında buldu
@tohum: hayri-0102
Deniz kıyısında Kamil bir havlunun üstünde güneşleniyordu. Hayri kumda koşarken ayağıyla havluya kum sıçrattı. Havlunun üstündeki bakkalın anahtarı kumun altında kayboldu. "Anahtar olmadan bakkalı açamam!" dedi Kamil. Hayri durdu ve Kamil'in yanına geldi. "Özür dilerim, Kamil, anahtarı artık hiç bulamayız!" dedi Hayri. Hayri biraz abartmıştı ve Kamil buna güldü. Sonra Hayri kumu parmaklarıyla yavaş yavaş eşeledi. Kısa bir süre sonra parlak anahtarı buldu. Anahtarı silkeledi ve Kamil'e verdi. "Teşekkürler, Hayri, seni affettim!" dedi Kamil.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 7: «Hayri biraz abartmıştı ve Kamil buna güldü.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0102` birebir aynı, ardından `@onarim: 14765655417442f8c0d77e8e16369ea7e2c315d2`, sonra gövde.

### Hikâye 10: tohum hayri-0103 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0103
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'havuç', fiil 'taşınmak', sıfat 'keyifli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: hızlı yürüdü ve havuç yere düştü | çok yavaş ve komik adımlarla yürüdü
@tohum: hayri-0103
@degisim: taşınmak -> taşımak
Hayri kamp yerinde yeni bir oyun deniyordu. Kaşıkta küçük bir havucu ağaçtan masaya kadar taşıyacaktı. Ama Hayri hızlı yürüdü ve havuç kaşıktan yere düştü. Hayri havucu yerden aldı ve tekrar denedi. Havuç yine düştü. Hayri havucun düşmesini biraz abarttı. Bu kez çok yavaş ve komik adımlarla yürüdü. Her adımda bir ayağını havaya kaldırdı ve biraz bekledi. Kaşığı da iki eliyle sıkıca tuttu. Havuç kaşıkta hiç kıpırdamadı. Sonunda Hayri masaya vardı ve havucu tabağa bıraktı. Sonra sevinçle zıpladı ve bu keyifli oyunu bir kez daha oynadı.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri havucun düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: 'Havucun düşmesini abarttı' anlamsız; fiil bağlama uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "havucun düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: 'Abarttı' fiili burada anlamsız ve yanlış kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "havucun düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri havucun düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: Tohumdaki abartma özelliği yalnız adı geçerek kullanılmış, sorunun çözümüne işe yarar biçimde bağlanmıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri havucun düşmesini biraz abarttı"
   - Cümle 6: «Hayri havucun düşmesini biraz abarttı.»
   - Açıklama: Havucun düşmesini abartmak anlamsız ve olaydan çıkmayan, çözüme bağlanmayan bir ayrıntı.
   - Açıklama: Havucun düşmesini abartmak anlamsız ve çözüme hiçbir katkısı olmayan bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0103` birebir aynı, `@degisim: taşınmak -> taşımak` (tutuyorsan), ardından `@onarim: 39a0f18b53a4866bead8490032b6d6543b9f421f`, sonra gövde.

### Hikâye 11: tohum hayri-0107 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0107
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'marul', fiil 'karşılaşmak', sıfat 'yapraklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek çok susamıştı ama musluğa yetişemiyordu | baklava tepsisini suyla doldurup köpeğe verdi
@tohum: hayri-0107
Rüzgar yapraklı ağaçların arasında hafifçe esiyordu. Hayri kamp yerinde musluğun altında marul yıkıyordu. Yıkadığı marulları baklava dükkanından getirdiği küçük bir tepsiye koydu. Birden musluğun yanında Yumak'la karşılaştı. Yumak çok koşmuştu ve susamıştı ama musluğa yetişemiyordu. Yumak kuyruğunu salladı ve musluğa baktı. "Sana bir su kabı gerek, Yumak," dedi Hayri. Hayri marulları tepsiden alıp çantasına koydu. Tepsiyi musluktan suyla doldurdu ve Yumak'ın önüne koydu. Yumak suyu hızlı hızlı içti. Sonra havladı ve Hayri'nin elini kokladı. "Afiyet olsun, Yumak, bu su senin için!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yumak çok koşmuştu ve susamıştı"
   - Cümle 5: «Yumak çok koşmuştu ve susamıştı ama musluğa yetişemiyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak beşinci cümlede söyleniyor.
   - Açıklama: Sorun ilk 3 cümlede değil ancak 5. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0107` birebir aynı, ardından `@onarim: df011bd8355875b8e3921508ffcf2e628a32f21e`, sonra gövde.

### Hikâye 12: tohum hayri-0108 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0108
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'boncuk', fiil 'çiğnemek', sıfat 'dağınık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: ipin ucu dağınıktı ve boncuklar ipe geçmiyordu | arkadaşından yardım istedi ve ipin ucunu ıslattı
@tohum: hayri-0108
@degisim: çiğnemek -> ıslatmak
Deniz kıyısında Hayri renkli boncuklarla bir bileklik yapıyordu. Ama ipin ucu dağınıktı, bu yüzden boncuklar ipe geçmiyordu. Hayri üç kez denedi ama olmadı. Akın biraz uzakta kumda oynuyordu. "Akın, yardım et, bu ipi yüz kez denedim!" dedi Hayri. Hayri biraz abarttı ve Akın buna güldü. Akın hemen gelip ipe baktı. "İpin ucunu suyla ıslatmalısın," dedi Akın. Hayri su kenarında ipin ucunu ıslattı ve parmaklarıyla yuvarladı. İpin ucu incecik oldu ve boncuklar ipe kolayca geçti. Hayri bütün boncukları ipe dizdi ve bilekliği taktı. "Teşekkürler, Akın, bileklik çok güzel oldu!" dedi Hayri.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu ipi yüz kez denedim"
   - Cümle 5: «"Akın, yardım et, bu ipi yüz kez denedim!" dedi Hayri.»
   - Açıklama: Abartma (mübalağa) söz sanatıdır ve ardından gelen 'abarttı' kelimesi 3 yaşındaki çocuk için soyuttur.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 6: «Hayri biraz abarttı ve Akın buna güldü.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri biraz abarttı ve Akın buna güldü"
   - Cümle 6: «Hayri biraz abarttı ve Akın buna güldü.»
   - Açıklama: Abartma ayrıntısı olay akışında hiçbir işe yaramıyor, yalnız özellik göstermek için ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0108` birebir aynı, `@degisim: çiğnemek -> ıslatmak` (tutuyorsan), ardından `@onarim: d853128a902bfe804a540f745d407505febfd0e8`, sonra gövde.
