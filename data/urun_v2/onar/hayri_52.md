# Editör görevi (onarım): Hayri, onarım partisi 52

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar52.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar52.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0128 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0128
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'avokado', fiil 'basmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: adımları küçük olduğu için resim kumda belli olmadı | adımlarını büyüttü ve kuma sertçe bastı
@tohum: hayri-0128
@degisim: avokado -> güneş
Deniz kıyısında Hayri kuma basarak bir resim yapıyordu. Şapkalı bir güneş yapmak istiyordu. Ama adımları küçüktü ve güneş kumda hiç belli olmadı. Hayri yine abarttı ve güneşi kocaman yapmaya karar verdi. Uzun adımlar attı ve kuma sertçe bastı. Güneşin ışıklarını iki ayağıyla zıplayarak yaptı. Sonra güneşin üstüne büyük adımlarla bir şapka yaptı. Geri çekildi ve resmine baktı. Resim artık çok büyük ve belliydi. Hayri çok güldü ve sevindi, çünkü şapkalı güneş uzaktan bile görünüyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abarttı"
   - Cümle 4: «Hayri yine abarttı ve güneşi kocaman yapmaya karar verdi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0128` birebir aynı, `@degisim: avokado -> güneş` (tutuyorsan), ardından `@onarim: 78a1909e330020b4b36fe0e7eb9ac647e026223c`, sonra gövde.

### Hikâye 2: tohum hayri-0130 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0130
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'dalga', fiil 'kalkmak', sıfat 'geniş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: dalga köpeğin topunu kumdaki çukura götürdü | geniş tepsiyi uzatıp topu kenara çekti
@tohum: hayri-0130
Bir sabah Hayri deniz kıyısında Yumak'la top oynuyordu. Dükkanın boş baklava tepsisi de yanında duruyordu. Birden bir dalga Yumak'ın topunu kumdaki büyük bir çukura götürdü. Çukur suyla doluydu ve top ortasında sallanıyordu. Hayri'nin eli topa yetişmedi. Yumak topa bakıp havladı ve kuma oturdu. Hayri suya girmedi ve çukurun kenarında durdu. Yanındaki geniş tepsiyi aldı ve ucunu topa uzattı. Tepsiyle topu yavaşça kendine doğru çekti. Top kuma yuvarlandı. Yumak hemen kalktı ve topa koştu. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. Hayri çok sevindi, çünkü Yumak'ın topunu çukurdan geri almıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dükkanın boş baklava tepsisi de yanında duruyordu"
   - Cümle 2: «Dükkanın boş baklava tepsisi de yanında duruyordu.»
   - Açıklama: Dükkan tepsisinin deniz kıyısında ne işi olduğu söylenmiyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Dükkanın baklava tepsisi deniz kıyısında sebepsizce beliriyor ve çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0130` birebir aynı, ardından `@onarim: 1a4be145922c5f96cd9bc28caec30826abc9acc4`, sonra gövde.

### Hikâye 3: tohum hayri-0135 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0135
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kask', fiil 'ışıldamak', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: bankın kenarındaki kask kayboldu | çalıların arasında ışıldayan şeye baktı ve kaskı buldu
@tohum: hayri-0135
Bir sabah Hayri parka bisikletiyle geldi. Kırmızı kaskını çıkarıp bankın kenarına koydu. Salıncağa koşarken kolu kaskı itti ve kask yere yuvarlandı. Ama Hayri bunu görmedi. Sonra bisikletiyle hızlı hızlı gezmek istedi ama kask bankta yoktu. Hayri kaskı olmadan binmedi ve etrafa baktı. Birden bankın arkasındaki çalıların arasında bir şey ışıldadı. Hayri bunun ne olduğunu çok merak etti. Hayri abartıp orada kocaman bir hazine var sandı. Hemen çalılara yürüdü ve eğilip baktı. Işık, kaskın parlak üstünden geliyordu! Hayri güldü ve kaskını başına taktı. Sonra bisikletine bindi ve parkta mutlu mutlu gezdi.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Salıncağa koşarken kolu kaskı itti ve kask yere yuvarlandı.»
   - Açıklama: Hayri'nin kaskı kaybetme sorunu ilk üç cümlede değil, 5. cümlede açıkça ortaya çıkıyor.
   - Açıklama: Hayri'nin sorunu olan kaskın bulunamaması ancak 5. cümlede söyleniyor, ilk 3 cümlede açıkça yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "abartıp orada kocaman bir hazine var sandı"
   - Cümle 9: «Hayri abartıp orada kocaman bir hazine var sandı.»
   - Açıklama: 'Abartıp sandı' anlamca yanlış; sanmak abartarak yapılan bir eylem değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıp orada kocaman"
   - Cümle 9: «Hayri abartıp orada kocaman bir hazine var sandı.»
   - Açıklama: 'Abartıp' soyut ve burada yanlış anlamda kullanılmış; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp orada kocaman bir hazine var sandı"
   - Cümle 9: «Hayri abartıp orada kocaman bir hazine var sandı.»
   - Açıklama: Tohumdaki abartma özelliği çözüme hiçbir katkı yapmadan süs olarak geçiyor; kartın özellik kullanımına göre işe yarar biçimde kullanılmamış.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hemen çalılara yürüdü"
   - Cümle 10: «Hemen çalılara yürüdü ve eğilip baktı.»
   - Açıklama: Yön eksik kalmış; 'çalılara doğru yürüdü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0135` birebir aynı, ardından `@onarim: 960c7ea590ea11473d07c0862130d6e3a014072b`, sonra gövde.

### Hikâye 4: tohum hayri-0136 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0136
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'parfüm', fiil 'korunmak', sıfat 'pahalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: tatlı bir koku geldi ama nereden geldiği belli değildi | kokuyu izledi ve keki kendi çantasında buldu
@tohum: hayri-0136
@degisim: pahalı -> tatlı
Hayri sırtında çantasıyla, güneşten korunmak için ağacın altındaki salıncakta sallanıyordu. Çok acıkmıştı ve birden tatlı bir koku geldi. Hayri bu kokunun nereden geldiğini çok merak etti. Önce bunu bir parfüm kokusu sandı. Ama koku, kek kokusuna daha çok benziyordu. Hayri salıncaktan indi ve kaydırağın yanına yürüdü. Orada durdu ve havayı kokladı. Hayri nereye gitse koku da oradaydı. Hayri şaşırdı ve çantasını açtı. Çantanın içinde bir dilim kek vardı. Keki kendisi hazırlamıştı ve çantaya koymuştu ama sonra unutmuştu. Hayri güldü ve keki mutlu mutlu yedi. Hayri bundan sonra çantasına koyduğu yiyecekleri hiç unutmadı.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kokuyu izledi ve keki kendi çantasında buldu"
   - Cümle 0 (plan satırı): «tatlı bir koku geldi ama nereden geldiği belli değildi | kokuyu izledi ve keki kendi çantasında buldu»
   - Açıklama: Gövdede Hayri kokuyu izlemiyor; kokunun her yerde onunla olduğunu görüp çantasını açıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bu kokunun nereden geldiğini çok merak etti"
   - Cümle 3: «Hayri bu kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Sorun yalnız bir kokunun kaynağını merak etmek; çocuğun önemseyeceği gerçek bir sorun zayıf kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0136` birebir aynı, `@degisim: pahalı -> tatlı` (tutuyorsan), ardından `@onarim: 323c449c8a0614a988f5af4c304a2a476189ff8d`, sonra gövde.

### Hikâye 5: tohum hayri-0137 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0137
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tomurcuk', fiil 'çekilmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: tabak eğri kütüğün üstünde kayıyordu | tabağı büyük ve düz bir taşa koydu
@tohum: hayri-0137
@degisim: mükemmel -> düz
Hayri kamp yerinde yemek yapma oyunu oynuyordu. Çok acıkmıştı, bu yüzden kendine peynirli bir sandviç hazırladı. Ama tabak kütüğün üstünde durmadı, çünkü kütük eğriydi. Tabak kaydı ve sandviç neredeyse yere düşüyordu. Hayri tabağı hemen tuttu ve etrafa baktı. Ağaçların arasında büyük ve düz bir taş gördü. Tabağı bu taşın üstüne koydu. Tabak artık hiç kaymadı. Hayri bir adım geri çekildi ve tabağa baktı. Tabağı süslemek için yere düşmüş küçük bir tomurcuğu kenarına koydu. Hayri taşın yanına oturdu ve sandviçini yedi. Hayri çok sevindi, çünkü sandviçini yere düşürmeden yiyebilmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir tomurcuğu kenarına"
   - Cümle 10: «Tabağı süslemek için yere düşmüş küçük bir tomurcuğu kenarına koydu.»
   - Açıklama: 'Tomurcuk' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yere düşmüş küçük bir tomurcuğu kenarına koydu"
   - Cümle 10: «Tabağı süslemek için yere düşmüş küçük bir tomurcuğu kenarına koydu.»
   - Açıklama: Tomurcukla süsleme sebepsiz ve işlevsiz bir ayrıntı; olaya hiçbir katkısı yok.
   - Açıklama: Tomurcukla süsleme olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0137` birebir aynı, `@degisim: mükemmel -> düz` (tutuyorsan), ardından `@onarim: 0b2d63aaf4227c19bcffe28b173dd4f72b9bfd66`, sonra gövde.

### Hikâye 6: tohum hayri-0140 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0140
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'erik', fiil 'sarılmak', sıfat 'değerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: küçük kalp yukarıdaki banktan görünmüyordu | kumun üstüne kocaman bir kalp çizdi
@tohum: hayri-0140
@degisim: değerli -> güzel
Hayri, Basri Amca'nın doğum günü için deniz kıyısına bir sepet erik getirmişti. Kumun üstüne de bir kalp çizmişti ama kalp çok küçüktü. Basri Amca yukarıdaki bankta oturuyordu ve küçük kalbi oradan göremiyordu. Hayri bu kez çok daha büyük bir kalp çizdi. Ortasına da erik sepetini koydu. "Amca, kumda dünyanın en büyük kalbi var!" dedi Hayri abartarak. Basri Amca kocaman kalbi gördü ve kıyıya indi. Hayri'ye sıkıca sarıldı. "Bu çok güzel bir sürpriz, Hayri," dedi Basri Amca. Sonra ikisi yan yana oturup erikleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 6: «"Amca, kumda dünyanın en büyük kalbi var!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0140` birebir aynı, `@degisim: değerli -> güzel` (tutuyorsan), ardından `@onarim: 43afe46b8398b952dc457e79a93a229c93eefb9c`, sonra gövde.

### Hikâye 7: tohum hayri-0142 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0142
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'jöle', fiil 'ovuşturmak', sıfat 'uzun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: soğuk parmaklarıyla arkadaşı kabın kapağını açamadı | ellerini hızlı hızlı ovuşturup kabı onun için açtı
@tohum: hayri-0142
Bir sabah Hayri ile Akın kamp yerindeydi ve hava çok serindi. Akın küçük bir jöle kabını açmak istedi. Ama parmakları soğuktu ve kapağı sıkıca tutamadı. Hayri bunu gördü ve arkadaşına yardım etmek istedi. "Akın, bana ver, ben dünyada en güçlüyüm!" dedi Hayri abartarak. Akın güldü ve kabı Hayri'ye verdi. Hayri'nin elleri de biraz soğuktu. Hayri ellerini hızlı hızlı ve uzun uzun ovuşturdu. Elleri hemen ısındı. Hayri kapağı iki eliyle tuttu ve kolayca açtı. Sonra kabı Akın'a geri verdi. "Teşekkürler, Hayri, sen de biraz jöle ister misin?" diye sordu Akın. Hayri çok sevindi, çünkü arkadaşına yardım edebilmişti.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Akın kamp yerindeydi"
   - Cümle 1: «Bir sabah Hayri ile Akın kamp yerindeydi ve hava çok serindi.»
   - Açıklama: Başlıktaki yer orman ama hikaye ormanı hiç kurmadan kamp yerinde geçiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ben dünyada en güçlüyüm"
   - Cümle 5: «"Akın, bana ver, ben dünyada en güçlüyüm!" dedi Hayri abartarak.»
   - Açıklama: Tamlama bozuk; 'dünyanın en güçlüsüyüm' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben dünyada en güçlüyüm"
   - Cümle 5: «"Akın, bana ver, ben dünyada en güçlüyüm!" dedi Hayri abartarak.»
   - Açıklama: Abartılı söz ve 'abartarak' soyut kavramdır.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Akın, bana ver, ben dünyada en güçlüyüm!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri ellerini hızlı hızlı ve uzun uzun ovuşturdu"
   - Cümle 8: «Hayri ellerini hızlı hızlı ve uzun uzun ovuşturdu.»
   - Açıklama: Eller uzun uzun ovuşturuluyor ama sonraki cümlede hemen ısındığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0142` birebir aynı, ardından `@onarim: b96f56462b5bb583f817b8ba279d087cb089b7c5`, sonra gövde.

### Hikâye 8: tohum hayri-0143 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0143
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çember', fiil 'yaklaştırmak', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çember belinde dönmüyordu ve hemen yere düşüyordu | belini güçlü ve hızlı hareketlerle salladı
@tohum: hayri-0143
Deniz kıyısında güneş parlıyordu. Hayri kumda ilk kez çember çevirmeyi deniyordu. Ama çember her seferinde düştü, çünkü Hayri belini çok yavaş sallıyordu. Hayri çemberi yerden aldı. Çemberi iki eliyle beline yaklaştırdı. Hayri, abartmayı sevdiği için bu kez belini çok güçlü ve hızlı salladı. Çember belinde bir kez, iki kez, üç kez döndü! Hayri durmadı ve saymaya devam etti. Çember tam on kez dönüp kuma indi. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü yeni oyunu sonunda öğrenmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartmayı sevdiği için"
   - Cümle 6: «Hayri, abartmayı sevdiği için bu kez belini çok güçlü ve hızlı salladı.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "abartmayı sevdiği için bu kez belini çok güçlü ve hızlı salladı"
   - Cümle 6: «Hayri, abartmayı sevdiği için bu kez belini çok güçlü ve hızlı salladı.»
   - Açıklama: Karttaki özellik olayları abartmaktır; burada fiziksel olarak aşırı güç kullanmaya çevrilmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0143` birebir aynı, ardından `@onarim: 2fcd7c77a0ec5ce4208d41d55c9773e515833732`, sonra gövde.

### Hikâye 9: tohum hayri-0146 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0146
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'küpe', fiil 'seçmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı kovadaki kabuklar bitmesin diye almadı | kabukları kuma döktü ve kocaman bir tepe yaptı
@tohum: hayri-0146
@degisim: küpe -> kabuk
Bir sabah Hayri ile Kamil deniz kıyısında oturuyordu. Hayri'nin kovası renkli kabuklarla doluydu ama Kamil'in kovası boştu. Hayri kovasını uzattı ama Kamil, Hayri'nin kabukları az kalmasın diye almadı. Hayri abartıp bütün kabukları kuma döktü ve kocaman bir tepe yaptı. Kamil tepeye bakıp güldü, çünkü kabuklar gerçekten çok fazlaydı. Kamil de elini uzattı. Kabuklar ince ve kırılgandı, bu yüzden Kamil onları yavaşça tuttu. Sonra en güzel üç tanesini seçti. Onları kendi kovasına dikkatle koydu. Hayri de Kamil de çok sevindi, çünkü ikisinin de kabukları vardı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıp bütün kabukları"
   - Cümle 4: «Hayri abartıp bütün kabukları kuma döktü ve kocaman bir tepe yaptı.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp bütün kabukları kuma döktü"
   - Cümle 4: «Hayri abartıp bütün kabukları kuma döktü ve kocaman bir tepe yaptı.»
   - Açıklama: Karttaki özellik olayları anlatırken abartmaktır; burada abartma bir eylemi aşırıya kaçırma olarak kartın özellikler alanından farklı kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kabuklar ince ve kırılgandı"
   - Cümle 7: «Kabuklar ince ve kırılgandı, bu yüzden Kamil onları yavaşça tuttu.»
   - Açıklama: Kabukların kırılganlığı olayda hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0146` birebir aynı, `@degisim: küpe -> kabuk` (tutuyorsan), ardından `@onarim: 6c78b642a96f9906c0e5cacd80158f9abd0edb5b`, sonra gövde.

### Hikâye 10: tohum hayri-0147 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0147
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fıskiye', fiil 'parlamak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: sormadan amcanın kutusunu açtı ve amca kızdı | özür diledi ve dükkandan getirdiği baklavayı paylaştı
@tohum: hayri-0147
@degisim: fıskiye -> kutu
Rüzgar ağaçların arasında serin serin esiyordu. Hayri kamp yerine, çalıştığı dükkandan bir paket baklava getirmişti. Hayri, Basri Amca'nın kapalı kutusunu sormadan açınca amca kızdı. Kutu gizemliydi ve Hayri içini çok merak etmişti ama izin istememişti. Kutunun içinde güneşte parlayan renkli taşlar vardı. Hayri kutuyu hemen kapattı ve Basri Amca'dan özür diledi. Basri Amca özrü duyunca gülümsedi. Hayri de getirdiği baklavayı Basri Amca ile paylaştı. Sonra Basri Amca kutuyu kendisi açtı ve taşları Hayri'ye tek tek gösterdi. Hayri çok rahatladı, çünkü Basri Amca artık ona kızgın değildi.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hayri kamp yerine, çalıştığı"
   - Cümle 2: «Hayri kamp yerine, çalıştığı dükkandan bir paket baklava getirmişti.»
   - Açıklama: Gereksiz virgül 'kamp yerine'yi 'kamp yapmak yerine' gibi okutuyor; virgül kaldırılmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kutu gizemliydi ve Hayri"
   - Cümle 4: «Kutu gizemliydi ve Hayri içini çok merak etmişti ama izin istememişti.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0147` birebir aynı, `@degisim: fıskiye -> kutu` (tutuyorsan), ardından `@onarim: 98d4aac9ec6df295e8a36a1c96770aef870e8ae5`, sonra gövde.

### Hikâye 11: tohum hayri-0148 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0148
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yosun', fiil 'saçmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: top çok büyüktü ve köpek onu ağzıyla tutamadı | yemek kutusunun düz ve hafif kapağını attı
@tohum: hayri-0148
@degisim: saçmak -> atmak
Parkta taşların üstünde yeşil yosunlar vardı. Hayri, Yumak'la yeni bir oyun denemek istiyordu. Hayri bir şey atacak, Yumak da onu havada yakalayacaktı. Ama top çok büyüktü ve Yumak onu ağzıyla tutamadı. Hayri küçük ve hafif bir şey aradı. Hayri sık sık acıktığı için çantasında hep yemek kutusu vardı. Kutunun yuvarlak kapağı düz ve çok hafifti. Hayri kapağı havaya attı. Kapak uçtu ve çimlere düştü. Yumak koştu, kapağı ağzına aldı ve geri getirdi. Hayri kapağı yine attı. Bu sefer Yumak kapağı havada yakaladı. "Aferin, Yumak, bu şanslı bir kapak!" dedi Hayri. İkisi kapak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama top çok büyüktü"
   - Cümle 4: «Ama top çok büyüktü ve Yumak onu ağzıyla tutamadı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu şanslı bir kapak"
   - Cümle 13: «"Aferin, Yumak, bu şanslı bir kapak!" dedi Hayri.»
   - Açıklama: Kapak şanslı olamaz; kelime öznesine uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu şanslı bir kapak"
   - Cümle 13: «"Aferin, Yumak, bu şanslı bir kapak!" dedi Hayri.»
   - Açıklama: 'Şanslı' soyut bir kavram ve bir kapağa yakıştırılması 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0148` birebir aynı, `@degisim: saçmak -> atmak` (tutuyorsan), ardından `@onarim: 02868a826af42ff25fef233d50acdc3941f4b52c`, sonra gövde.

### Hikâye 12: tohum hayri-0149 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0149
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'patates', fiil 'dolaşmak', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu savurdu ve küçük patates resmi kayboldu | patatesi kocaman ve derin çizgilerle yeniden çizdi
@tohum: hayri-0149
@degisim: kibar -> kocaman
Bir sabah Hayri deniz kıyısında bir çubukla kuma bıyıklı bir patates çizdi. Patates küçüktü ve çizgileri çok inceydi. Ama rüzgar kumu savurdu ve ince çizgiler kapandı. Komik patates hemen kayboldu. Hayri bu küçük rüzgarı abarttı ve onu fırtına sandı. Fırtınada kaybolmayacak büyük bir patates çizmek istedi. Çubuğu kuma bastırdı ve büyük bir daire çizerek dolaştı. Daireye iki kocaman göz ve çok uzun bir bıyık ekledi. Çizgiler bu kez hem geniş hem de derindi. Rüzgar yine esti ama büyük patates kaybolmadı. Hayri patatesin ortasına oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu küçük rüzgarı abarttı"
   - Cümle 5: «Hayri bu küçük rüzgarı abarttı ve onu fırtına sandı.»
   - Açıklama: 'Abartmak' fiili rüzgarla bu anlamda kullanılmaz ve 3 yaşındaki çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu küçük rüzgarı abarttı"
   - Cümle 5: «Hayri bu küçük rüzgarı abarttı ve onu fırtına sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bu küçük rüzgarı abarttı ve onu fırtına sandı"
   - Cümle 5: «Hayri bu küçük rüzgarı abarttı ve onu fırtına sandı.»
   - Açıklama: Rüzgarı fırtına sanması çözümü etkilemiyor; derin çizgiler zaten sebebe yetiyor, abartı işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0149` birebir aynı, `@degisim: kibar -> kocaman` (tutuyorsan), ardından `@onarim: e6464b22a00f1787dce8ad7058f68fe56aaeee8b`, sonra gövde.
