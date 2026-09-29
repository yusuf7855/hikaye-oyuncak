# Editör görevi (onarım): Hayri, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0033 (deneme 5 -> 6)

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
Rüzgar hafif hafif esiyordu. Hayri parkta Yumak ile oynuyordu. Hayri koşarken baklava dükkanının anahtarı cebinden uzun çimenlere düştü. Yere eğilip baktı ama anahtarı göremedi. Sabah dükkanda tepsi taşımıştı ve eli de anahtarı da baklava kokuyordu. Elini yavaşça Yumak'ın burnuna indirdi. "Yumak, anahtarımı bulur musun?" diye sordu Hayri. Yumak onun elini kokladı ve burnunu yere eğdi. Çimenlerin arasında biraz ilerledi, sonra durup havladı. Heyecanlı Hayri hemen oraya koştu. Anahtar çimenlerin arasında parlıyordu. "Aferin sana, Yumak!" dedi Hayri ve anahtarı aldı. Anahtarı bu kez ceketinin iç cebine koydu. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "eli de anahtarı da baklava kokuyordu"
   - Cümle 5: «Sabah dükkanda tepsi taşımıştı ve eli de anahtarı da baklava kokuyordu.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği bir kez değil, anahtar ve koku olarak iki kez kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0033` birebir aynı, `@degisim: şampuan -> anahtar` (tutuyorsan), ardından `@onarim: 742645e51bc828da81b71fba6212d3b4d1dd0145`, sonra gövde.

### Hikâye 2: tohum hayri-0035 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: top oynak tahtadan zıplayıp yere düştü | kenarı yüksek boş bir tepsi kullandı
@tohum: hayri-0035
@degisim: konuşmak -> zıplamak
Evin bahçesinde Hayri yeni bir oyun buldu. Topunu düz bir tahtayla çimenin öbür ucuna taşıyacaktı. Ama tahta ince ve oynak olduğu için top zıplayıp yere düştü. Hayri durdu ve düşündü. Çalıştığı baklava dükkanında hep kenarı yüksek tepsiler taşıyordu. Hemen eve koştu ve boş bir tepsi getirdi. Topu tepsiye koydu. Tepsiyi iki eliyle tuttu ve yavaş yavaş yürüdü. Top kenara çarptı ama yere düşmedi. Sonunda Hayri çimenin öbür ucuna vardı. Hayri çok sevindi, çünkü topu düşürmeden bahçeyi geçmişti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Topunu düz bir tahtayla çimenin öbür ucuna taşıyacaktı"
   - Cümle 2: «Topunu düz bir tahtayla çimenin öbür ucuna taşıyacaktı.»
   - Açıklama: Sorun Hayri'nin kendi uydurduğu keyfi bir kuraldan doğuyor ve tahtayı tepsiyle değiştirmek oyunun amacını boşa çıkardığı için sorun saçma kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0035` birebir aynı, `@degisim: konuşmak -> zıplamak` (tutuyorsan), ardından `@onarim: b402beb376dabcc64c5975bf3f4587dfc4a0ee96`, sonra gövde.

### Hikâye 3: tohum hayri-0037 (deneme 5 -> 6)

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
@plan: yumuşak toprakta topaç hemen devrildi | boş bir tepsiyi ters koyup üstünde topacı çevirdi
@tohum: hayri-0037
@degisim: tasarlamak -> çevirmek
Ağaçların arasında kuşlar ötüyordu. Hayri kamp yerinde tahta topacını çevirdi. Ama toprak yumuşaktı ve topaç hemen devrildi. Hayri topacı iki kez daha çevirdi ama topaç yine toprağa battı. Biraz düşündü. Sonra baklava dükkanından getirdiği boş tepsiyi hatırladı. Tepsiyi toprağa ters koydu. Topacı sert ve düz tepsinin üstünde çevirdi. Topaç bu kez uzun uzun döndü. Bir, iki, üç, dört, beş diye saydı. Hayri çok gururluydu, çünkü topacı bu kez hiç devrilmemişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "baklava dükkanından getirdiği boş tepsiyi hatırladı"
   - Cümle 6: «Sonra baklava dükkanından getirdiği boş tepsiyi hatırladı.»
   - Açıklama: Ormandaki kamp yerinde baklava tepsisi önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Ormandaki kamp yerinde boş baklava tepsisi önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri çok gururluydu"
   - Cümle 11: «Hayri çok gururluydu, çünkü topacı bu kez hiç devrilmemişti.»
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0037` birebir aynı, `@degisim: tasarlamak -> çevirmek` (tutuyorsan), ardından `@onarim: b0394b47c9a5cb2f1db0dd0daa409ced973ebd53`, sonra gövde.

### Hikâye 4: tohum hayri-0042 (deneme 5 -> 6)

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
Rüzgar denizden sert sert esiyordu. Hayri kumda portakal dilimleriyle dükkan oyunu oynuyordu. Ama rüzgar kumu portakal tabağına doğru savurmaya başladı. Hayri, çalıştığı baklava dükkanında tatlıları hep temiz tutardı. Etrafına baktı ve büyük bir kaya gördü. Kayanın arkası iyi bir yerdi, çünkü orada rüzgar yoktu. Hayri tabağı iki eliyle dikkatle kaldırdı ve kayaya götürdü. Sonra kayanın dibine sokuldu ve tabağı kucağına koydu. Artık portakalın üstüne hiç kum gelmedi. Sonra dükkan oyununa mutlu mutlu devam etti. Hayri bundan sonra rüzgarlı günlerde kayanın arkasında oynadı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalıştığı baklava dükkanında tatlıları hep temiz"
   - Cümle 4: «Hayri, çalıştığı baklava dükkanında tatlıları hep temiz tutardı.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak anılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri, çalıştığı baklava dükkanında tatlıları hep temiz tutardı"
   - Cümle 4: «Hayri, çalıştığı baklava dükkanında tatlıları hep temiz tutardı.»
   - Açıklama: Baklava dükkanı bilgisi olayla bağsız ve hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0042` birebir aynı, ardından `@onarim: a0426c7157a7dd4f70d2743b89863f47313728bc`, sonra gövde.

### Hikâye 5: tohum hayri-0043 (deneme 5 -> 6)

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
Kumsal geniş ve serindi. Hayri, Yumak için kumdan kocaman bir kemik yapıyordu. Bu bir sürprizdi ama Yumak topunu bırakıp geldi ve kemiği bozdu. Hayri biraz düşündü. Sonra Yumak'ın kırmızı topunu kayaların yanına götürdü. Yelpaze gibi bir kabukla kumu kazdı ve topu gömdü. Topun üstüne küçük bir kum tepesi de yaptı. Yumak topun kokusunu aldı ve orada uzun uzun kumu eşeledi. Hayri hemen işine döndü ve kum kemiğini bitirdi. "Yumak, gel, ev kadar büyük bir kemik yaptım!" diye abarttı Hayri. Yumak koşup geldi ve kuyruğunu salladı. Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu sakladı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yelpaze gibi bir kabukla"
   - Cümle 6: «Yelpaze gibi bir kabukla kumu kazdı ve topu gömdü.»
   - Açıklama: Benzetme ve 'yelpaze' kelimesi 3 yaşındaki çocuğa uygun değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Topun üstüne küçük bir kum tepesi de yaptı"
   - Cümle 7: «Topun üstüne küçük bir kum tepesi de yaptı.»
   - Açıklama: Çözüm topu götürme, kazıp gömme ve üstüne tepe yapma diye ikiden fazla adıma yayılıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ev kadar büyük bir kemik yaptım!" diye abarttı Hayri"
   - Cümle 10: «"Yumak, gel, ev kadar büyük bir kemik yaptım!" diye abarttı Hayri.»
   - Açıklama: Abartma mecazı ve soyut 'abarttı' fiili 3 yaşındaki çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 10: «"Yumak, gel, ev kadar büyük bir kemik yaptım!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ev kadar büyük bir kemik yaptım"
   - Cümle 10: «"Yumak, gel, ev kadar büyük bir kemik yaptım!" diye abarttı Hayri.»
   - Açıklama: Tohumdaki abartma özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak eklenmiş bir replikte geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0043` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 328b04bfec67ee96882f5851613d09a07ab8079b`, sonra gövde.

### Hikâye 6: tohum hayri-0046 (deneme 4 -> 5)

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
Parkın kum havuzunda Hayri pasta yapma oyunu oynuyordu. Kule kadar yüksek bir pasta yapmak istiyordu. Ama kum çok kuruydu ve pasta hep dağıldı. Hayri abartarak kumun çöl kadar kuru olduğunu düşündü. Bu yüzden su şişesini açtı. Suyu oyuncak bardağıyla ölçtü ve iki bardak kuma döktü. Islak kumu eski kovasına sıkıca bastırdı. Sonra kovayı ters çevirdi ve yavaşça kaldırdı. Kumdan pasta bu kez hiç yıkılmadı. Hayri onun üstüne iki kat daha yaptı. Pasta bir kule gibi yükseldi. Hayri onu yapraklarla süsledi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak kumun çöl kadar kuru olduğunu düşündü"
   - Cümle 4: «Hayri abartarak kumun çöl kadar kuru olduğunu düşündü.»
   - Açıklama: Abartmak söze ait bir eylemdir; 'abartarak düşündü' fiile uymuyor ve 'çöl kadar' benzetmesi küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kumun çöl kadar kuru olduğunu düşündü"
   - Cümle 4: «Hayri abartarak kumun çöl kadar kuru olduğunu düşündü.»
   - Açıklama: 'Abartarak' soyut, 'çöl kadar kuru' benzetmesi 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak kumun çöl kadar kuru olduğunu düşündü"
   - Cümle 4: «Hayri abartarak kumun çöl kadar kuru olduğunu düşündü.»
   - Açıklama: Abartma cümlesi işlevsiz bir özellik eklemesi ve suyu dökmeyi bu düşünceye bağlamak sebep zincirini zayıflatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0046` birebir aynı, `@degisim: mıknatıs -> kova` (tutuyorsan), ardından `@onarim: 531933573b19b50bde24cc37d1b627fd373c4c82`, sonra gövde.

### Hikâye 7: tohum hayri-0047 (deneme 4 -> 5)

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
Rüzgar kıyıda hızlı esiyordu. Hayri denizin kenarında yürüyor ve dalgaları izliyordu. Birden rüzgar mavi şapkasını başından kaptı ve uçurdu. Hayri önce dalgaların ıslattığı çamurlu kumda aradı, ama şapka orada yoktu. Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü. Bu yüzden rüzgarın estiği yöne baktı. O yönde, kıyıda büyük taşlar vardı. Hayri taşların yanına gitti ve arkasına dikkatle baktı. Şapka orada, kuru bir taşın üstündeydi. Hayri şapkayı aldı ve başına sıkıca taktı. Hayri çok sevindi, çünkü kaybolan şapkasını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak şapkanın çok"
   - Cümle 5: «Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abartarak' düşünmek fiiline uymuyor, kelime yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "abartarak şapkanın çok uzağa uçtuğunu düşündü"
   - Cümle 5: «Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abartarak düşünmek' anlamca yerinde değil; kelime bağlama uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak şapkanın çok"
   - Cümle 5: «Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü"
   - Cümle 5: «Hayri abartarak şapkanın çok uzağa uçtuğunu düşündü.»
   - Açıklama: Abartma ayrıntısı çözümü sebepsizce getiriyor; şapkanın uzağa uçtuğunu düşünmek taşlara bakmayı açıklamıyor.
   - Açıklama: Abartma düşüncesi 'bu yüzden' ile doğru yöne bakmaya sebep gösteriliyor, oysa şapka yakında çıkıyor; sebep-sonuç bağı kopuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0047` birebir aynı, `@degisim: pizza -> şapka` (tutuyorsan), ardından `@onarim: e976731e7cfde81db6c0cac61e99de62da0b0a8d`, sonra gövde.

### Hikâye 8: tohum hayri-0048 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0048
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kürek', fiil 'ilerlemek', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çukur sudan uzaktı ve içine su gelmedi | çukurdan denize doğru ince bir yol kazdı
@tohum: hayri-0048
Hayri deniz kıyısında küreğiyle yumuşak kumda bir çukur kazıyordu. Orada küçük bir havuz yapmak istiyordu. Ama çukur sudan uzaktı ve içine hiç su gelmedi. Hayri durdu ve denize dikkatle baktı. Dalgaların kıyıya gelip geri gittiğini fark etti. Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü. Bu yüzden çukurdan denize ince bir yol kazdı. Az sonra bir dalga geldi. Su yolun içinde yavaş yavaş ilerledi ve çukura aktı. Birkaç dalgadan sonra havuz suyla doldu. Hayri sevinçle zıpladı ve ellerini çırptı. Hayri bundan sonra havuzuna suyu hep böyle bir yoldan getirdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak çukurun denizden bir dağ kadar uzak"
   - Cümle 6: «Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü.»
   - Açıklama: 'Abartarak' ve 'bir dağ kadar uzak' abartı/mecaz olup 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Abartarak' soyut bir kelime ve 'bir dağ kadar uzak' abartma mecazı 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü"
   - Cümle 6: «Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü.»
   - Açıklama: Tohumdaki abartma özelliği çözüme katkı vermeyen süs olarak kullanılıyor; çözüm dalgaları gözlemlemekten geliyor.
   - Açıklama: Tohumdaki abartma özelliği çözüme gerçekten katkı vermiyor, 'bu yüzden' bağıyla işe yarıyormuş gibi gösteriliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü"
   - Cümle 6: «Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü.»
   - Açıklama: Kanal kazma abartılı düşünceye 'bu yüzden' ile bağlanıyor; olay dalgaları fark etmekten çıkmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çukurun denizden bir dağ kadar uzak olduğunu düşündü"
   - Cümle 6: «Hayri abartarak çukurun denizden bir dağ kadar uzak olduğunu düşündü.»
   - Açıklama: Çukuru dağ kadar uzak sanmak yol kazmayı gerektirmez; 'Bu yüzden' bağı sebepsiz ve olay bir öncekinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0048` birebir aynı, ardından `@onarim: 4bee2e4d8d404ee8bed41aeefaf67a7f8ad0c179`, sonra gövde.

### Hikâye 9: tohum hayri-0050 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0050
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'paspas', fiil 'konmak', sıfat 'yeterli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: rüzgar örtünün kenarlarını hep havaya kaldırdı | yardım istedi ve köşelere taş ve kutu koydu
@tohum: hayri-0050
@degisim: paspas -> örtü
Rüzgar ormanda hızlı hızlı esiyordu. Hayri dükkandan ağır bir kutu baklava getirmişti. Onu koymak için yere büyük bir örtü yaymak istedi. Ama rüzgar örtünün kenarlarını hep havaya kaldırdı. Hayri örtüyü tek başına tutamadı. "Basri Amca, bana yardım eder misin?" diye sordu Hayri. "Tabii, hemen geliyorum," dedi Basri Amca. Basri Amca iki köşeyi sıkıca tuttu. Hayri de ağaçların dibinden üç büyük taş getirdi. Taşları üç köşeye koydu. Sonra baklava kutusu da dördüncü köşeye kondu. Üç taş ve ağır kutu, örtüyü yerde tutmaya yeterliydi. Basri Amca bir dilim baklava yedi ve gülümsedi. Hayri çok sevindi, çünkü örtü artık yerinde duruyordu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar örtünün kenarlarını hep havaya kaldırdı"
   - Cümle 4: «Ama rüzgar örtünün kenarlarını hep havaya kaldırdı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örtüyü yerde tutmaya yeterliydi"
   - Cümle 12: «Üç taş ve ağır kutu, örtüyü yerde tutmaya yeterliydi.»
   - Açıklama: 'Yeterliydi' soyut bir kelime; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0050` birebir aynı, `@degisim: paspas -> örtü` (tutuyorsan), ardından `@onarim: 94004614fc472c2c748f934ae2220496197060bd`, sonra gövde.

### Hikâye 10: tohum hayri-0051 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0051
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yağmurluk', fiil 'yetişmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kırık kovadan kozalaklar yere düştü | yağmurluğunu katlayıp kovanın dibine koydu
@tohum: hayri-0051
@degisim: patlak -> kırık
Bir sabah Hayri kamp yerinde kozalakları bir kovaya atıp oynuyordu. Kovayı doldurmak istiyordu. Ama kova kırıktı ve kozalaklar alttaki delikten yere düştü. Bir kozalak otların arasına yuvarlandı. Hayri birkaç adımda ona yetişti. Sonra deliğe baktı ve biraz düşündü. Sarı yağmurluğunu çıkardı, katladı ve kovanın dibine koydu. Artık delik kapanmıştı. Hayri kozalağı yine kovaya attı. Bu kez kozalak yere düşmedi. Hayri hızlı hızlı attı ve kova çabucak doldu. Oyun bitince Hayri çok acıkmıştı. Ağacın altına oturdu ve kahvaltısını mutlu mutlu yaptı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Oyun bitince Hayri çok acıkmıştı"
   - Cümle 12: «Oyun bitince Hayri çok acıkmıştı.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümünde işe yaramıyor, sona eklenmiş süs olarak kalıyor; kartın özellik ve güvenli özellik kullanımı alanına göre işlevsiz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyun bitince Hayri çok acıkmıştı"
   - Cümle 12: «Oyun bitince Hayri çok acıkmıştı.»
   - Açıklama: Acıkma ve kahvaltı olaydan çıkmıyor ve sorunla ilgisi olmayan işlevsiz bir ayrıntı olarak ekleniyor.
   - Açıklama: Acıkma ve kahvaltı olayla ilgisiz, işlevsiz bir ayrıntı olarak sona ekleniyor.
   - Açıklama: Acıkma sorunla ilgisiz biçimde sonradan ekleniyor ve işlevsiz bir ayrıntı.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Ağacın altına oturdu ve kahvaltısını mutlu mutlu yaptı"
   - Cümle 13: «Ağacın altına oturdu ve kahvaltısını mutlu mutlu yaptı.»
   - Açıklama: Son cümle kovayı doldurma hedefine değil ilgisiz bir kahvaltıya bağlanıyor, bu yüzden kapanış olaydan çıkmıyor.
   - Açıklama: Son cümle kova doldurma hedefine değil ilgisiz bir kahvaltıya bağlanıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "kahvaltısını mutlu mutlu yaptı"
   - Cümle 13: «Ağacın altına oturdu ve kahvaltısını mutlu mutlu yaptı.»
   - Açıklama: Son cümle kova doldurma hedefine değil ilgisiz bir kahvaltıya bağlanıyor; kapanış olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0051` birebir aynı, `@degisim: patlak -> kırık` (tutuyorsan), ardından `@onarim: 684122c5f40b37f9d6ac6af4ff6eb73be2297253`, sonra gövde.

### Hikâye 11: tohum hayri-0054 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0054
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bez', fiil 'yarışmak', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: teknenin yelkeni yoktu ve tekne suda gitmedi | bezi çubuğa takarak büyük bir yelken yaptı
@tohum: hayri-0054
@degisim: cesur -> büyük
Rüzgar deniz kıyısında hafif hafif esiyordu. Hayri tahta teknesini kumdaki küçük bir su çukuruna koydu. Ama teknenin yelkeni yoktu ve tekne suda hiç gitmedi. Hayri abartarak teknesini kocaman bir gemi gibi düşündü. Gemilerin büyük yelkenleri vardı. Hayri kumda bir çubuk buldu ve cebindeki bezi çıkardı. Bezi iyice açtı ve çubuğa geçirdi. Çubuğu teknedeki bir deliğe taktı. Büyük yelken rüzgarla şişti ve tekne hızla ilerledi. Hayri çukurun kenarında koşarak tekneyle yarıştı. Hayri çok mutluydu, çünkü teknesi sonunda suda gidiyordu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "teknesini kocaman bir gemi gibi düşündü"
   - Cümle 4: «Hayri abartarak teknesini kocaman bir gemi gibi düşündü.»
   - Açıklama: 'Gemi gibi düşündü' yanlış anlamda; teknesini gemi olarak hayal etti denmeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "teknesini kocaman bir gemi gibi düşündü"
   - Cümle 4: «Hayri abartarak teknesini kocaman bir gemi gibi düşündü.»
   - Açıklama: Bir şeyi başka bir şey gibi düşünmek soyut bir hayal anlatımıdır ve küçük çocuğa somut gelmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "cebindeki bezi çıkardı"
   - Cümle 6: «Hayri kumda bir çubuk buldu ve cebindeki bezi çıkardı.»
   - Açıklama: Yelken yapacak bez sebepsizce cepte beliriyor ve çözümü hazır getiriyor.
   - Açıklama: Yelken yapacak bez önceden kurulmadan tam gereken anda cepten beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0054` birebir aynı, `@degisim: cesur -> büyük` (tutuyorsan), ardından `@onarim: 1f3a72ce1f2c00c42e56c0f3726e7f002097cad7`, sonra gövde.

### Hikâye 12: tohum hayri-0057 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0057
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çim', fiil 'gizlenmek', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: saklambaçta sayarken gizlice gözlerini açtı | özür diledi ve gözlerini kapayıp yeniden saydı
@tohum: hayri-0057
Hayri ile Akın parkta saklambaç oynuyordu. Hayri'nin yuvarlak baklava kutusu bankın üstünde duruyordu. Ama Hayri sayarken gizlice gözlerini açtı. Akın bunu gördü ve çok üzüldü. "Hayri, sen bana baktın, bu olmaz!" dedi Akın. Hayri yanlış yaptığını anladı. "Haklısın, Akın, özür dilerim. Bu baklava senin," dedi Hayri. Akın baklavayı aldı ve yine gülümsedi. Sonra Hayri gözlerini sıkıca kapadı ve ona kadar saydı. Akın çimlerin üstünden koştu ve büyük ağacın arkasına gizlendi. Hayri parkı dolaştı ve sonunda Akın'ı buldu. İkisi birlikte güldü. "Çok güzel oynadık, Hayri, bir daha oynayalım!" dedi Akın.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri'nin yuvarlak baklava kutusu"
   - Cümle 2: «Hayri'nin yuvarlak baklava kutusu bankın üstünde duruyordu.»
   - Açıklama: Karttaki özellik baklava dükkanında çalışmak iken hikayede yalnız bir baklava kutusu var ve özellik karttaki gibi kullanılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Hayri sayarken gizlice gözlerini açtı"
   - Cümle 3: «Ama Hayri sayarken gizlice gözlerini açtı.»
   - Açıklama: Hayri'nin neden gözlerini açtığı, yani sorunun sebebi hiç söylenmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu baklava senin"
   - Cümle 8: «Bu baklava senin," dedi Hayri.»
   - Açıklama: Bankın üstüne kurulan baklava kutusu özrün içine sebepsizce bir hediye olarak giriyor ve sorunun çözümüyle ilgisi yok.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aldı ve yine gülümsedi"
   - Cümle 9: «Akın baklavayı aldı ve yine gülümsedi.»
   - Açıklama: Akın daha önce gülümsemedi; 'yine' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0057` birebir aynı, ardından `@onarim: b32965a1da166ebf5e3be2e7a1891256930ef191`, sonra gövde.
