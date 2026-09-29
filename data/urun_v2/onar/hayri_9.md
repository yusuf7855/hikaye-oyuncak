# Editör görevi (onarım): Hayri, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0025 (deneme 2 -> 3)

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
Hayri'nin yeşil bir kalıbı vardı ve kumdan kuleler yapıyordu. Mert de kıyıda elleriyle kum topluyordu. Ama Mert'in kuleleri hep yıkılıyordu. "Mert, kalıbı birlikte kullanalım mı?" diye sordu Hayri. Mert sevindi ve başını salladı. Hayri kalıbı ıslak kumla doldurdu ve Mert'e verdi. Mert kalıbı ters çevirdi ve yavaşça kaldırdı. Kumda düzgün bir kule duruyordu. "Mert, bu kule bir dağ kadar büyük!" diye abarttı Hayri. Mert güldü ve bir kule daha yaptı. Hayri çok mutluydu, çünkü paylaşınca ikisi de kule yapmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu kule bir dağ kadar büyük"
   - Cümle 9: «"Mert, bu kule bir dağ kadar büyük!" diye abarttı Hayri.»
   - Açıklama: Abartılı benzetme ve 'abarttı' fiili küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0025` birebir aynı, `@degisim: guruldamak -> doldurmak` (tutuyorsan), ardından `@onarim: e81c14a296b7a1e1c2286a5d83812742bfe514b6`, sonra gövde.

### Hikâye 2: tohum hayri-0028 (deneme 2 -> 3)

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
Yağmur damlaları bahçede tıp tıp ses çıkarıyordu. Hayri yeni kovasıyla yağmur suyu topluyordu. Ama damlalar masadaki tabakta duran tatlılara düşmeye başladı. Hayri baklava dükkanında tatlıların üstünü hep kapatırdı. Hemen kovadaki suyu çimene döktü. Kovayı ters çevirdi ve tabağın üstüne kapattı. Sonra tabağı çatının altındaki kuru köşeye taşıdı. Orada kovayı kaldırdı ve tatlıları kokladı. Tatlılar yine çok güzel kokuyordu. Hayri bir dilim aldı ve afiyetle yedi. Sonra kuru köşede oturdu ve yağmuru mutlu mutlu izledi.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ama damlalar masadaki tabakta duran tatlılara düşmeye başladı"
   - Cümle 3: «Ama damlalar masadaki tabakta duran tatlılara düşmeye başladı.»
   - Açıklama: Yağmur baştan beri bahçede yağarken damlaların tatlılara ancak şimdi düşmeye başlaması çelişkili.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra tabağı çatının altındaki kuru köşeye taşıdı"
   - Cümle 7: «Sonra tabağı çatının altındaki kuru köşeye taşıdı.»
   - Açıklama: Tabak zaten kovayla kapatılmışken bir de kuru köşeye taşınıyor; çözüm gereksiz üçüncü bir adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0028` birebir aynı, ardından `@onarim: a2871f18303fb75151827b0299cf1bf83bc1e908`, sonra gövde.

### Hikâye 3: tohum hayri-0029 (deneme 2 -> 3)

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
Bir sabah erkenden ormandaki kamp yeri karanlıktı. Hayri çadırında fenerini açtı ve gölge oyunu oynamak istedi. Ama fener yumuşak yastığın üstünde durmadı ve yana kaydı. Işık çadırın tavanına gitti ve duvar karanlık kaldı. Hayri feneri çantasının üstüne dik koydu. Işık bu kez duvara gitti. Hayri elleriyle duvara garip şekiller yaptı. Gölgeler duvarda bir o yana bir bu yana gezindi. Sonra çalıştığı dükkandaki baklava dilimini düşündü. Parmaklarını birleştirdi ve duvarda tam bir dilim gölgesi çıktı. Hayri çok sevindi, çünkü en sevdiği tatlının gölgesini yapmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Işık bu kez duvara gitti"
   - Cümle 6: «Işık bu kez duvara gitti.»
   - Açıklama: Işık bir yere gitmez; 'duvara vurdu' ya da 'duvara düştü' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra çalıştığı dükkandaki baklava dilimini düşündü"
   - Cümle 9: «Sonra çalıştığı dükkandaki baklava dilimini düşündü.»
   - Açıklama: Tohumdaki baklava özelliği sorunun (kayan fener) çözümüne katkı vermiyor, sorun çözüldükten sonra süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0029` birebir aynı, ardından `@onarim: 01b0b332a60718cbb832d34df2d25f74062b3567`, sonra gövde.

### Hikâye 4: tohum hayri-0030 (deneme 2 -> 3)

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
Ormanda, kamp yerinde Hayri ile zeki Akın teneke telefonla oynuyordu. "Akın, beni duyuyor musun?" diye fısıldadı Hayri. Ama Akın hiçbir şey duymadı, çünkü ip bir dala takılmıştı. Hayri ipe baktı ve takılan yeri gördü. İpi daldan dikkatle çıkardı. Sonra geri geri yürüdü ve ipi çekti. "Akın, ben çok acıktım!" dedi Hayri kutuya. Akın bu kez sesi duydu ve güldü. "Hadi, birlikte yemek yiyelim!" dedi Akın. "Teşekkürler, Akın, telefon artık çalışıyor!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Akın, ben çok acıktım!" dedi Hayri kutuya"
   - Cümle 7: «"Akın, ben çok acıktım!" dedi Hayri kutuya.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız deneme cümlesi olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0030` birebir aynı, `@degisim: şekillendirmek -> çekmek` (tutuyorsan), ardından `@onarim: ded42c35b7f9c20344eb9dbaa9a3408915027944`, sonra gövde.

### Hikâye 5: tohum hayri-0032 (deneme 2 -> 3)

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
Bir sabah Hayri, Basri Amca'yla parkta ilk kez fidan dikmeyi denedi. Basri Amca ona küçük, yemyeşil bir fidan verdi. Ama çukurdaki toprak yumuşaktı ve fidan hemen yana yattı. "Bu fidan kocaman ağaç olacak, çok toprak lazım!" diye abarttı Hayri. Basri Amca güldü ve ona bir kova toprak verdi. Hayri bu toprağı çukura ekledi. Sonra toprağı iki eliyle sıkıca bastı. Fidan bu kez dimdik durdu. Hayri fidanın yapraklarını okşadı. Basri Amca bir etikete Hayri'nin adını yazdı ve fidana astı. Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Bu fidan kocaman ağaç olacak, çok toprak lazım!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bu kelimeyi bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0032` birebir aynı, ardından `@onarim: 16113e56c20882b194e29e29474d59729096c65a`, sonra gövde.

### Hikâye 6: tohum hayri-0033 (deneme 1 -> 2)

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
Rüzgar hafif hafif esiyordu. Hayri parkta Yumak ile oynuyordu. Hayri koşarken cebindeki anahtar uzun çimenlere düştü. Bu anahtar, Hayri'nin çalıştığı baklava dükkanının anahtarıydı. Hayri yere eğildi ama anahtarı göremedi. Sonra elini yavaşça Yumak'ın burnuna indirdi. "Yumak, anahtarımı bulur musun?" diye sordu Hayri. Yumak onun elini kokladı ve burnunu yere eğdi. Çimenlerin arasında biraz ilerledi, sonra durup havladı. Heyecanlı Hayri hemen oraya koştu. Anahtar çimenlerin arasında parlıyordu. "Aferin sana, Yumak!" dedi Hayri ve anahtarı aldı. Anahtarı bu kez ceketinin iç cebine koydu. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri'nin çalıştığı baklava dükkanının"
   - Cümle 4: «Bu anahtar, Hayri'nin çalıştığı baklava dükkanının anahtarıydı.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız anahtarın etiketi olarak anılıyor, sorunu çözmekte işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu anahtar, Hayri'nin çalıştığı baklava dükkanının anahtarıydı"
   - Cümle 4: «Bu anahtar, Hayri'nin çalıştığı baklava dükkanının anahtarıydı.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0033` birebir aynı, `@degisim: şampuan -> anahtar` (tutuyorsan), ardından `@onarim: 7686fd151a080205c160c4854307ce93c648adfb`, sonra gövde.

### Hikâye 7: tohum hayri-0034 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: çitin arkasından çıtır çıtır bir ses geldi | çite gidip baktı ve kraker yiyen arkadaşını buldu
@tohum: hayri-0034
Evin bahçesi serin ve sessizdi. Hayri sabahlığını giymiş, bahçede oturuyordu ve çok acıkmıştı. Birden çitin arkasından çıtır çıtır bir ses geldi. Hayri bu sesi çok merak etti. Hayri çite doğru yürüdü. Yerde ufak kraker parçaları vardı. Sonra çitin üstünden baktı. Kamil öbür tarafta oturmuş, kitap okuyordu. Elinde bir kutu kraker vardı. "Kamil, bu ses kraker sesi mi?" diye sordu Hayri. "Evet, gel, birlikte yiyelim," dedi Kamil. Kamil kutuyu çitin üstünden uzattı ve Hayri iki kraker aldı. "Teşekkürler, Kamil, hem sesi hem de kraker kutusunu buldum!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çitin arkasından çıtır çıtır bir ses geldi"
   - Cümle 3: «Birden çitin arkasından çıtır çıtır bir ses geldi.»
   - Açıklama: Sorun yalnız merak edilen bir ses; çocuğun önemseyeceği gerçek bir sorun ve sebebi kurulmuyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "hem sesi hem de kraker kutusunu buldum"
   - Cümle 13: «"Teşekkürler, Kamil, hem sesi hem de kraker kutusunu buldum!" dedi Hayri.»
   - Açıklama: Hayri kutuyu bulmuyor, Kamil uzatıyor; son replik olayla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0034` birebir aynı, ardından `@onarim: 723b6446ae5765704a612d14dce4f5a331e4f846`, sonra gövde.

### Hikâye 8: tohum hayri-0035 (deneme 1 -> 2)

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
Evin bahçesinde güneşli bir gündü. Hayri çimenin üstünde düz bir tahtayla komik bir oyun oynuyordu. Ama oynak top her adımda tahtadan zıpladı ve yere düştü. Hayri durdu ve düşündü. Hayri baklava dükkanında çalışıyordu ve orada hep tepsi taşıyordu. Tepsinin kenarı yüksekti ve baklavalar yerinde kalıyordu. Bankın üstünde dükkandan getirdiği boş bir tepsi vardı. Hayri topu tepsiye koydu. Tepsiyi iki eliyle tuttu ve yavaş yavaş yürüdü. Top kenara çarptı ama yere düşmedi. Sonunda Hayri bahçenin öbür ucuna vardı. Hayri çok sevindi, çünkü topu düşürmeden bahçeyi geçmişti.
```

**Hakem bulguları (4):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "düz bir tahtayla komik bir oyun oynuyordu"
   - Cümle 2: «Hayri çimenin üstünde düz bir tahtayla komik bir oyun oynuyordu.»
   - Açıklama: Oyunun ne olduğu ve hedefi baştan açık değil; hedef ancak son cümlede anlaşılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama oynak top her adımda"
   - Cümle 3: «Ama oynak top her adımda tahtadan zıpladı ve yere düştü.»
   - Açıklama: 'Oynak top' ve 'her adımda' bu bağlamda anlamca belirsiz; Hayri yürümüyorken adım geçiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama oynak top her"
   - Cümle 3: «Ama oynak top her adımda tahtadan zıpladı ve yere düştü.»
   - Açıklama: 'Oynak' topa uygun olmayan belirsiz bir sıfat; 'zıplayan top' kastediliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bankın üstünde dükkandan getirdiği boş bir tepsi vardı"
   - Cümle 7: «Bankın üstünde dükkandan getirdiği boş bir tepsi vardı.»
   - Açıklama: Kenarı yüksek tepsi çözüm gerektiği anda sebepsizce bahçede beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0035` birebir aynı, `@degisim: konuşmak -> zıplamak` (tutuyorsan), ardından `@onarim: 96c10471e2ce745f26e8860a61159531963aedff`, sonra gövde.

### Hikâye 9: tohum hayri-0036 (deneme 1 -> 2)

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
Deniz kıyısında güneş yeni doğmuştu. Hayri ile Mert kuma beş temiz plastik şişe dizdi. Ama tek top vardı ve ikisi de önce atmak istedi. İkisi de topu aynı anda tuttu ve çekti. Hayri biraz düşündü. O sırada çok acıkmıştı ve çantasında bir simit vardı. "Önce sen at, Mert, ben de simit yerim," dedi Hayri. Mert topu attı ve üç şişe devrildi. Sonra sıra Hayri'ye geldi. Hayri simidini bitirdi ve topu attı. Kalan iki şişe de devrildi. Hayri ile Mert çok sevindi, çünkü ikisi de sırayla topu atmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada çok acıkmıştı ve çantasında bir simit vardı"
   - Cümle 6: «O sırada çok acıkmıştı ve çantasında bir simit vardı.»
   - Açıklama: Açlık ve simit tam çözüm anında sebepsizce beliriyor ve sıra vermeyi kolaylaştırmak için getiriliyor.
   - Açıklama: Açlık ve simit tam çözüm anında sebepsizce beliriyor ve sıra vermeyi paylaşma yerine rastlantısal bir açlığa bağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0036` birebir aynı, ardından `@onarim: 8064028b8c7efabf794b447a907f17834f723968`, sonra gövde.

### Hikâye 10: tohum hayri-0037 (deneme 1 -> 2)

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
@plan: yumuşak toprakta topaç hemen devrildi | baklava kutusunun düz kapağında topacı çevirdi
@tohum: hayri-0037
Ağaçların arasında kuşlar ötüyordu. Hayri kamp yerinde yeni bir oyun tasarladı ve tahta topacını çevirdi. Ama toprak yumuşaktı ve topaç hemen devrildi. Hayri topacı iki kez daha çevirdi ama topaç yine toprağa battı. Hayri etrafına baktı. Yanında dükkandan getirdiği bir kutu baklava vardı. Kutunun kapağı düz ve sertti. Hayri kapağı yere koydu ve topacı üstünde çevirdi. Topaç kamp yerinde uzun uzun döndü. Hayri topaç dönerken bir, iki, üç, dört, beş diye saydı. Hayri çok gururluydu, çünkü yeni oyununu sonunda başarmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir oyun tasarladı"
   - Cümle 2: «Hayri kamp yerinde yeni bir oyun tasarladı ve tahta topacını çevirdi.»
   - Açıklama: 'Tasarladı' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Tasarlamak' 3 yaşındaki çocuğun bilmeyeceği soyut bir fiil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında dükkandan getirdiği bir kutu baklava vardı"
   - Cümle 6: «Yanında dükkandan getirdiği bir kutu baklava vardı.»
   - Açıklama: Baklava kutusu çözüm için sebepsizce ortaya çıkıyor.
   - Açıklama: Baklava kutusu ormandaki kampta sebepsizce beliriyor ve çözümü hazır getiriyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yeni oyununu sonunda başarmıştı"
   - Cümle 11: «Hayri çok gururluydu, çünkü yeni oyununu sonunda başarmıştı.»
   - Açıklama: Oyun başarılmaz; 'başarmak' fiili nesnesine uymuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri çok gururluydu"
   - Cümle 11: «Hayri çok gururluydu, çünkü yeni oyununu sonunda başarmıştı.»
   - Açıklama: 'Gururlu' küçük çocuk için soyut bir duygu kelimesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0037` birebir aynı, ardından `@onarim: c32f3aa6dbfe516dd5115068a89989a25ad68b3b`, sonra gövde.

### Hikâye 11: tohum hayri-0038 (deneme 1 -> 2)

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
Parkta tek bir salıncak vardı. Hayri ile Mert aynı anda salıncağa koştu. İkisi de salıncağın zincirini tuttu ve önce binmek istedi. Mert'in elinde elmalı bir lolipop vardı. Hayri biraz düşündü. Onun çalıştığı baklava dükkanında müşteriler hep sırayla beklerdi. "Mert, sırayla binelim, ikimiz de on kez sallanırız," dedi Hayri. "Tamam, önce sen bin," dedi Mert. Hayri salıncağa bindi ve on kez sallandı. Mert o sırada lolipopunu yaladı ve saydı. Sonra Hayri indi ve Mert salıncağa bindi. Bu kez Hayri yüksek sesle saydı. Hayri ile Mert çok sevindi, çünkü sırayla ikisi de salıncağa binmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mert'in elinde elmalı bir lolipop vardı"
   - Cümle 4: «Mert'in elinde elmalı bir lolipop vardı.»
   - Açıklama: Lolipop olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı.
   - Açıklama: Lolipop işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun çalıştığı baklava dükkanında"
   - Cümle 6: «Onun çalıştığı baklava dükkanında müşteriler hep sırayla beklerdi.»
   - Açıklama: Bir önceki cümlelerde hem Hayri hem Mert geçtiği için 'Onun' kimi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0038` birebir aynı, `@degisim: kilit -> salıncak` (tutuyorsan), ardından `@onarim: 1457c782d472fb59be6e6af3ec9ceecc88336730`, sonra gövde.

### Hikâye 12: tohum hayri-0039 (deneme 1 -> 2)

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
@plan: rüzgar esti ve teyp havlunun altında kayboldu | çantasına gidince havluyu kaldırıp teybi buldu
@tohum: hayri-0039
Hayri deniz kıyısında Basri Amca ile oturuyordu. Birden sert bir rüzgar esti ve havlular kumda uçuştu. Rüzgar durunca Basri Amca teybini göremedi. "Teyp nerede, az önce buradaydı!" dedi Basri Amca. Hayri kumun her yerine baktı ama teybi bulamadı. O sırada Hayri çok acıkmıştı. Simidini almak için çantasına gitti. Çantanın üstüne kuru bir havlu düşmüştü. Hayri havluyu kaldırdı ve altında teybi gördü. "Basri Amca, teyp burada!" dedi Hayri. Hayri havluyu uçmasın diye çantanın sapına sıkıca bağladı. Basri Amca teybi aldı ve gülümsedi. "Teşekkür ederim, Hayri, onu sen buldun!" dedi Basri Amca.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Basri Amca teybini göremedi"
   - Cümle 3: «Rüzgar durunca Basri Amca teybini göremedi.»
   - Açıklama: 'Teyp' 3 yaşındaki bir çocuğun bilmeyeceği eski bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıkmıştı"
   - Cümle 6: «O sırada Hayri çok acıkmıştı.»
   - Açıklama: Açlık çözümü sebepsizce getiriyor ve havluyu çantaya bağlama ayrıntısı da işlevsiz.
   - Açıklama: Açlık sebepsizce araya giriyor ve çözümü tesadüfen getiriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Simidini almak için çantasına gitti"
   - Cümle 7: «Simidini almak için çantasına gitti.»
   - Açıklama: Teyp sebebe yönelen bir arama ile değil, Hayri acıktığı için tesadüfen bulunuyor.
   - Açıklama: Teyp aramaya yönelik bir eylemle değil, yemek almaya giderken tesadüfen bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0039` birebir aynı, ardından `@onarim: af2d88fcafb4ea14f975a7d9d139e1c1048a949c`, sonra gövde.
