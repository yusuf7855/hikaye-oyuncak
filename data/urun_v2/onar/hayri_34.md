# Editör görevi (onarım): Hayri, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0016 (deneme 3 -> 4)

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
Deniz kıyısında rüzgar çok esiyordu. Hayri ile Kamil kumda oturmuş denize bakıyordu. Birden rüzgar Kamil'in bembeyaz şapkasını uçurdu ve şapka kayboldu. "Eyvah, şapkam gitti!" dedi Kamil. "Bu rüzgar bütün kumları da uçuracak!" dedi Hayri abartarak. Sonra Hayri havada uçan kum tanelerini dikkatle izledi. Kumlar hep büyük kayalara doğru uçuyordu. Hayri o yöne yürüdü ve kayaların arkasına baktı. Şapka iki kayanın arasına sıkışmıştı. Hayri şapkayı aldı ve Kamil'e götürdü. "Teşekkürler, Hayri!" dedi Kamil ve şapkasını taktı. Hayri bundan sonra uçan eşyaları rüzgarın estiği yönde aradı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Bu rüzgar bütün kumları da uçuracak!" dedi Hayri abartarak.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0016` birebir aynı, `@degisim: yapıştırıcı -> şapka` (tutuyorsan), ardından `@onarim: 6706b1af89cfc522d96e2fa1f041babd291402c9`, sonra gövde.

### Hikâye 2: tohum hayri-0098 (deneme 1 -> 2)

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
Bir sabah Hayri bahçede Mert için bir sürpriz hazırlıyordu. O gün Mert'in doğum günüydü. Ama dükkandan getirdiği baklavalar kutuda dağılmıştı, çünkü yolda kutu çok sallanmıştı. Hayri kutuya baktı ve biraz düşündü. Hayri dükkanda her gün baklavaları tepsiye diziyordu. Önce ellerini sabunla yıkadı. Sonra masadaki büyük ve düz tabağı aldı. Hayri baklavaları dükkanda yaptığı gibi tabağa sıra sıra dizdi. Her sırada dört baklava vardı. Az sonra Mert bahçeye geldi. "Doğum günün kutlu olsun, Mert!" dedi Hayri. Mert tabağı görünce çok sevindi. "Tıpkı dükkandaki gibi olmuş, teşekkürler, Hayri!" dedi Mert.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri bahçede Mert için"
   - Cümle 1: «Bir sabah Hayri bahçede Mert için bir sürpriz hazırlıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0098` birebir aynı, ardından `@onarim: e0da70e065519099ca523e2e449ca4f9d8397624`, sonra gövde.

### Hikâye 3: tohum hayri-0099 (deneme 1 -> 2)

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
@plan: oyunun ilk siparişi için tencerede yemek yoktu | acıkınca sepetten gerçek bir sandviç hazırladı
@tohum: hayri-0099
Bir sabah Hayri kamp yerinde yemek oyunu oynuyordu. Düz bir taşın üstüne düzenli bir mutfak kurmuştu. Yanında yiyecek sepeti de vardı. Hayri oyuncak telefonu kulağına götürdü ve sipariş alır gibi yaptı. Sipariş peynirli bir sandviçti. Ama oyuncak tencere boştu, çünkü oyunda hiç gerçek yemek yoktu. Tam o sırada Hayri'nin karnı guruldadı, çünkü acıkmıştı. Hayri sepetten ekmek ve peynir aldı. Peyniri iki ekmeğin arasına koydu ve bir sandviç hazırladı. Sandviçi oyuncak tabağa koydu ve masaya getirdi. Sonra sandviçi yavaş yavaş yedi. Hayri çok sevindi, çünkü oyunun ilk siparişini gerçekten hazırlamıştı.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve sipariş alır gibi yaptı"
   - Cümle 4: «Hayri oyuncak telefonu kulağına götürdü ve sipariş alır gibi yaptı.»
   - Açıklama: 'Sipariş' ve 'alır gibi yapmak' 3 yaşındaki çocuk için soyut ve zor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama oyuncak tencere boştu"
   - Cümle 6: «Ama oyuncak tencere boştu, çünkü oyunda hiç gerçek yemek yoktu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak altıncı cümlede söyleniyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çünkü oyunda hiç gerçek yemek yoktu"
   - Cümle 6: «Ama oyuncak tencere boştu, çünkü oyunda hiç gerçek yemek yoktu.»
   - Açıklama: Oyun oynarken gerçek yemek olmaması akla yatkın bir sorun değil, oyunun doğası gereğidir.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "oyunda hiç gerçek yemek yoktu"
   - Cümle 6: «Ama oyuncak tencere boştu, çünkü oyunda hiç gerçek yemek yoktu.»
   - Açıklama: Yemek oyununda gerçek yemek olmaması akla yatkın bir sorun sebebi değil.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hayri'nin karnı guruldadı, çünkü acıkmıştı"
   - Cümle 7: «Tam o sırada Hayri'nin karnı guruldadı, çünkü acıkmıştı.»
   - Açıklama: Acıkma ikinci bir sorun olarak ortaya çıkıyor ve çözümü o getiriyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra sandviçi yavaş yavaş yedi"
   - Cümle 11: «Sonra sandviçi yavaş yavaş yedi.»
   - Açıklama: Siparişi hazırlayıp masaya getirdikten sonra kendisi yiyor, sipariş hikayesiyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0099` birebir aynı, ardından `@onarim: adbbd277af2cd48d721dd53cfd8e695c45b6a977`, sonra gövde.

### Hikâye 4: tohum hayri-0101 (deneme 1 -> 2)

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
Hayri parkta çam ağacının altında bir sürü kozalak fark etti. Kozalakları kağıt bir torbada topladı. Ama torba ağırlaştı ve yırtıldı, kozalaklar yere döküldü. Basri Amca yakındaki bankta oturuyordu. "Basri Amca, bin tane kozalak her yere kaçtı!" diye abartarak seslendi Hayri. Basri Amca bu söze güldü ve yanına geldi. "Bin tane değil ama çok kozalak var," dedi Basri Amca. Sonra Hayri'ye yumuşacık bir kumaş çanta verdi. Çantanın sağlam bir fermuarı vardı. Hayri kozalakları tek tek çantaya koydu. Sonra fermuarı dikkatle kapattı. "Teşekkürler, Basri Amca," dedi Hayri. Hayri çok sevindi, çünkü bütün kozalaklarını yeniden toplamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kozalak her yere kaçtı"
   - Cümle 5: «"Basri Amca, bin tane kozalak her yere kaçtı!" diye abartarak seslendi Hayri.»
   - Açıklama: Kozalaklar kaçmaz; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bin tane kozalak her yere kaçtı"
   - Cümle 5: «"Basri Amca, bin tane kozalak her yere kaçtı!" diye abartarak seslendi Hayri.»
   - Açıklama: Kozalaklar kaçmaz; mecazlı kullanım küçük çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0101` birebir aynı, ardından `@onarim: 43557d285d344758abdb28f9a2169c395650896d`, sonra gövde.

### Hikâye 5: tohum hayri-0102 (deneme 1 -> 2)

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
@plan: koşarken kum sıçradı ve anahtar kayboldu | özür diledi ve kumu yavaşça açıp anahtarı buldu
@tohum: hayri-0102
Deniz kıyısında Kamil bir havlunun üstünde güneşleniyordu. Hayri kumda koşarken ayağıyla havluya kum sıçrattı. Havlunun üstündeki bakkal anahtarı kumun altında kayboldu. "Anahtar olmadan bakkalı açamam!" dedi Kamil. Hayri durdu ve Kamil'in yanına geldi. "Özür dilerim, Kamil, bütün kumsalı sana taşıdım!" dedi Hayri. Kamil bu abartılı söze güldü. Sonra Hayri yavaş hareketlerle kumu parmaklarıyla açtı. Kısa bir süre sonra parlak anahtarı buldu. Anahtarı silkeledi ve Kamil'e verdi. "Teşekkürler, Hayri, seni affettim!" dedi Kamil.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Havlunun üstündeki bakkal anahtarı"
   - Cümle 3: «Havlunun üstündeki bakkal anahtarı kumun altında kayboldu.»
   - Açıklama: 'bakkal anahtarı' tamlaması eksik; 'bakkalın anahtarı' ya da 'dükkanın anahtarı' olmalı.
   - Açıklama: Tamlama eksik; 'bakkalın anahtarı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bütün kumsalı sana taşıdım"
   - Cümle 6: «"Özür dilerim, Kamil, bütün kumsalı sana taşıdım!" dedi Hayri.»
   - Açıklama: Abartılı mecaz 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Abartı/mecaz, 3 yaşındaki çocuk için uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kamil bu abartılı söze güldü"
   - Cümle 7: «Kamil bu abartılı söze güldü.»
   - Açıklama: 'abartılı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu abartılı söze güldü"
   - Cümle 7: «Kamil bu abartılı söze güldü.»
   - Açıklama: 'Abartılı söz' soyut bir kavram.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumu parmaklarıyla açtı"
   - Cümle 8: «Sonra Hayri yavaş hareketlerle kumu parmaklarıyla açtı.»
   - Açıklama: Kum açılmaz; 'kumu parmaklarıyla eşeledi' gibi bir fiil gerekir.
   - Açıklama: Kum açılmaz; 'eşeledi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0102` birebir aynı, ardından `@onarim: 7431c4a9ac22d5f86ae02211d6677d0d13ff802f`, sonra gövde.

### Hikâye 6: tohum hayri-0103 (deneme 1 -> 2)

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
Hayri kamp yerinde yeni bir oyun deniyordu. Kaşıkta küçük bir havucu ağaçtan masaya kadar taşıyacaktı. Ama Hayri hızlı yürüdü ve havuç kaşıktan yere düştü. Hayri havucu yerden aldı ve tekrar denedi. Havuç yine düştü. Bu kez Hayri adımlarını çok abarttı. Çok yavaş ve komik adımlarla yürüdü. Her adımda bir ayağını havaya kaldırdı ve biraz bekledi. Kaşığı da iki eliyle sıkıca tuttu. Havuç kaşıkta hiç kıpırdamadı. Sonunda Hayri masaya vardı ve havucu tabağa bıraktı. Sonra sevinçle zıpladı ve bu keyifli oyunu bir kez daha oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri adımlarını çok abarttı"
   - Cümle 6: «Bu kez Hayri adımlarını çok abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez Hayri adımlarını çok abarttı"
   - Cümle 6: «Bu kez Hayri adımlarını çok abarttı.»
   - Açıklama: Karttaki özellik olayları abartmak; burada yavaş adım atmak olarak yanlış kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0103` birebir aynı, `@degisim: taşınmak -> taşımak` (tutuyorsan), ardından `@onarim: 02258e24822754e92c23a7da08586df5ad32e661`, sonra gövde.

### Hikâye 7: tohum hayri-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0104
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'havlu', fiil 'korumak', sıfat 'peynirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: rüzgar esti ve tabağa toz ile yapraklar düştü | dükkandaki gibi tabağı temiz bir havluyla örttü
@tohum: hayri-0104
Ormandaki kamp yerinde Hayri ile Kamil peynirli sandviç yapıyordu. Ama rüzgar esti ve tabağın kenarına toz ile yapraklar düştü. "Sandviçler kirlenir, Hayri," dedi Kamil. Hayri dükkanda baklava tepsisinin üstüne hep bir bez koyuyordu. Hemen çantasından temiz bir havlu çıkardı. Havluyu dükkandaki gibi tabağın üstüne örttü. Kenarlarını da tabağın altına sıkıştırdı. Rüzgar yine esti ama havlu hiç kıpırdamadı. Hayri ile Kamil son sandviçleri de yapıp tabağa koydu. "Havlu sandviçleri çok iyi korudu," dedi Kamil. Sonra ikisi temiz sandviçlerini ağaçların altında mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "son sandviçleri de yapıp tabağa koydu"
   - Cümle 9: «Hayri ile Kamil son sandviçleri de yapıp tabağa koydu.»
   - Açıklama: Tabak havluyla örtülüp kenarları altına sıkıştırılmışken sandviçler yine tabağa konuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0104` birebir aynı, ardından `@onarim: 72f987bc4641808ff06a1e4ce729ef73ea988163`, sonra gövde.

### Hikâye 8: tohum hayri-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0105
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'dergi', fiil 'karıştırmak', sıfat 'küçücük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: amca yemeğini evde unuttu ve karnı guruldadı | acıkınca sandviçlerini çıkarıp amcayla paylaştı
@tohum: hayri-0105
Hayri parktaki bankta Basri Amca'nın yanına oturdu. Basri Amca bir yemek dergisini karıştırıyordu. Birden Basri Amca'nın karnı guruldadı, çünkü yemeğini evde unutmuştu. "Bu dergideki yemekler ne güzel görünüyor," dedi Basri Amca. Tam o sırada Hayri de acıktı. Çantasından dört küçücük sandviç çıkardı. İki sandviçi Basri Amca'ya uzattı. "Afiyet olsun, Basri Amca, birlikte yiyelim," dedi Hayri. Basri Amca önce şaşırdı, sonra gülümsedi. İkisi sandviçleri dergideki resimlere bakarak yedi. "Bunlar dergideki yemeklerden de güzel, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü sandviçlerini paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri de acıktı"
   - Cümle 5: «Tam o sırada Hayri de acıktı.»
   - Açıklama: Çözüm Hayri'nin amcanın açlığını fark etmesinden değil, tesadüfen kendisinin acıkmasından çıkıyor.
   - Açıklama: Çözüm, Hayri'nin amcanın açlığını fark etmesinden değil tesadüfen acıkmasından çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0105` birebir aynı, ardından `@onarim: 661247fc2076f4a6327c073354ed0b31dd0a53b2`, sonra gövde.

### Hikâye 9: tohum hayri-0106 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0106
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'bulut', fiil 'taşmak', sıfat 'gizli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: ikisi aynı anda su döktü ve çukur taştı | dükkandaki gibi sırayla su döktüler
@tohum: hayri-0106
@degisim: bulut -> kova
Parktaki kum havuzunda Hayri ile Mert gizli bir göl yapıyordu. İkisi aynı anda kovayla çukura su döktü. Su çukurdan taştı ve kumdan duvarlar yıkıldı. "Göl bozuldu," dedi Mert. Hayri baklava dükkanında baklavayı herkese sırayla veriyordu. "Dükkanda herkes sırasını bekler, biz de sırayla dökelim," dedi Hayri. İkisi önce kumdan duvarları yeniden yaptı. Sonra önce Mert biraz su döktü. Ardından Hayri de biraz döktü. Bu kez su çukurda kaldı ve göl yavaş yavaş doldu. "Sırayla oynamak çok güzel, teşekkürler, Hayri!" dedi Mert.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İkisi aynı anda kovayla çukura su döktü"
   - Cümle 2: «İkisi aynı anda kovayla çukura su döktü.»
   - Açıklama: Taşmanın sebebi suyun aynı anda dökülmesi değil miktarıdır; sırayla dökmek sebebi akla yatkın biçimde çözmüyor.
   - Açıklama: Suyun taşmasının sebebi aynı anda dökmek değil suyun çokluğu olduğundan sebep akla yatkın değil.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "baklava dükkanında baklavayı herkese sırayla veriyordu"
   - Cümle 5: «Hayri baklava dükkanında baklavayı herkese sırayla veriyordu.»
   - Açıklama: Parktaki olay anlatılırken 'veriyordu' Hayri'nin o anda dükkanda olduğunu düşündürüyor; alışkanlık için 'verirdi' olmalı.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Hayri baklava dükkanında baklavayı herkese sırayla veriyordu"
   - Cümle 5: «Hayri baklava dükkanında baklavayı herkese sırayla veriyordu.»
   - Açıklama: Parktaki sahnenin ortasında şimdiki sahne gibi anlatılıyor; alışkanlık için 'verirdi' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında baklavayı herkese sırayla veriyordu"
   - Cümle 5: «Hayri baklava dükkanında baklavayı herkese sırayla veriyordu.»
   - Açıklama: Parktaki sahnenin ortasına dükkandan bir cümle sebepsizce giriyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra önce Mert biraz"
   - Cümle 8: «Sonra önce Mert biraz su döktü.»
   - Açıklama: Bir önceki cümledeki 'önce' ardından 'Sonra önce' gereksiz ve karışık bir tekrar yaratıyor.
   - Açıklama: 'Sonra' ve 'önce' yan yana gereksiz ve çelişkili tekrar oluşturuyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra önce Mert biraz su döktü"
   - Cümle 8: «Sonra önce Mert biraz su döktü.»
   - Açıklama: Çözüm sırayla dökmeye yöneliyor ama asıl işe yarayan az su dökmek, yani sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0106` birebir aynı, `@degisim: bulut -> kova` (tutuyorsan), ardından `@onarim: 2217b530cdcf39bd963e540fc3a89ec69d576261`, sonra gövde.

### Hikâye 10: tohum hayri-0107 (deneme 1 -> 2)

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
@plan: köpek çok susamıştı ama musluğa yetişemiyordu | dükkanın tepsisini suyla doldurup köpeğe verdi
@tohum: hayri-0107
Rüzgar yapraklı ağaçların arasında hafifçe esiyordu. Hayri kamp yerinde musluğun altında marul yıkarken Yumak'la karşılaştı. Yumak çok koşmuştu ve susamıştı ama musluğa yetişemiyordu. Yumak kuyruğunu salladı ve musluğa baktı. "Sana bir su kabı gerek, Yumak," dedi Hayri. Hayri'nin çantasında baklava dükkanından küçük ve derin bir tepsi vardı. Hayri tepsiyi çıkardı ve musluktan suyla doldurdu. Sonra tepsiyi Yumak'ın önüne koydu. Yumak suyu hızlı hızlı içti. Sonra havladı ve Hayri'nin elini kokladı. "Afiyet olsun, Yumak, bu su senin için!" dedi Hayri.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dükkanın tepsisini suyla doldurup"
   - Cümle 0 (plan satırı): «köpek çok susamıştı ama musluğa yetişemiyordu | dükkanın tepsisini suyla doldurup köpeğe verdi»
   - Açıklama: Plan satırında 'dükkanın' hangi dükkanı gösterdiği belli değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük ve derin bir tepsi"
   - Cümle 6: «Hayri'nin çantasında baklava dükkanından küçük ve derin bir tepsi vardı.»
   - Açıklama: Tepsi derin olmaz; sıfat nesneye uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri'nin çantasında baklava dükkanından küçük ve derin bir tepsi vardı"
   - Cümle 6: «Hayri'nin çantasında baklava dükkanından küçük ve derin bir tepsi vardı.»
   - Açıklama: Tepsi tam gerektiği anda sebepsizce çantada beliriyor ve çözümü hazır getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasında baklava dükkanından küçük ve derin bir tepsi vardı"
   - Cümle 6: «Hayri'nin çantasında baklava dükkanından küçük ve derin bir tepsi vardı.»
   - Açıklama: Tepsi önceden kurulmadan tam gerektiği anda çantada beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0107` birebir aynı, ardından `@onarim: fa617beac1af9194aef2d4fc1cbf32f00903ee4f`, sonra gövde.

### Hikâye 11: tohum hayri-0108 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar kutuyu devirdi ve boncuklar kuma dağıldı | komik bir sesle yardım istedi ve boncukları topladılar
@tohum: hayri-0108
Deniz kıyısında Hayri renkli boncuklarla bir kolye yapıyordu. Birden rüzgar esti ve boncuk kutusu kuma devrildi. Boncuklar kumun üstünde dağınık bir halde kaldı. Akın biraz uzakta kumda oynuyordu. "Akın, yardım et, burada yüz tane boncuk var!" diye abartarak seslendi Hayri. Akın güldü ve hemen koşup geldi. "Yüz tane değil, yirmi tane var," dedi Akın. "Dikkat et, boncukları çiğneme," dedi Hayri. İkisi kuma oturdu ve boncukları tek tek topladı. Kısa sürede kutu yine doldu. "Teşekkürler, Akın, bütün boncuklar yine kutuda!" dedi Hayri.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve boncuk kutusu kuma devrildi"
   - Cümle 2: «Birden rüzgar esti ve boncuk kutusu kuma devrildi.»
   - Açıklama: Rüzgarın dağıttığı boncukları toplayıp bitirmek örnekteki önemsiz 'dağıttı, topladı, bitti' sorununa benziyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "boncuk kutusu kuma devrildi"
   - Cümle 2: «Birden rüzgar esti ve boncuk kutusu kuma devrildi.»
   - Açıklama: Rüzgar boncukları dağıtıyor, toplanıyor ve bitiyor; sorun önemsiz bir dağıl-topla olayı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak seslendi Hayri"
   - Cümle 5: «"Akın, yardım et, burada yüz tane boncuk var!" diye abartarak seslendi Hayri.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0108` birebir aynı, ardından `@onarim: 375bc3ffcf7591952b2709ef4cc3a561e53d2c25`, sonra gövde.

### Hikâye 12: tohum hayri-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0109
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'blok', fiil 'almak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: en altta tek blok vardı ve kule yıkıldı | en alta yan yana altı blok koydu
@tohum: hayri-0109
Bir sabah Hayri kamp yerinde ilk kez bloklarla kule yapmayı denedi. Tahta blokları bir kütüğün üstüne üst üste dizdi. Ama en altta yalnız bir blok vardı ve kule sallanıp yıkıldı. Hayri yere düşen bloklara baktı ve biraz düşündü. Sonra blokların hepsini yerden aldı. Bu kez en alt sırayı çok abarttı. En alta yan yana tam altı blok koydu. Üstüne blokları tek tek dikkatle yerleştirdi. En üste de kıpkırmızı bir blok koydu. Kule bu kez hiç sallanmadı ve dimdik durdu. Hayri bundan sonra kulenin en altına hep çok blok koydu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en alt sırayı çok abarttı"
   - Cümle 6: «Bu kez en alt sırayı çok abarttı.»
   - Açıklama: Altı blok koymak çözümdür, 'abartmak' yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "en alt sırayı çok abarttı"
   - Cümle 6: «Bu kez en alt sırayı çok abarttı.»
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez en alt sırayı çok abarttı"
   - Cümle 6: «Bu kez en alt sırayı çok abarttı.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartma blok sayısını artırmak olarak kullanılıyor.
   - Açıklama: Karttaki özellik olayları abartmak; burada blok sayısını artırmak olarak yanlış kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0109` birebir aynı, ardından `@onarim: 3399228fc6227cf9aa9bc7179378c138bfbeb4a6`, sonra gövde.
