# Editör görevi (onarım): Hayri, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0155
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'fiyonk', fiil 'yuvarlamak', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kazdığı çukura su gelmedi çünkü çukur denizden uzaktı | çok uzun bir yol kazdı ve su geldi
@tohum: hayri-0155
@degisim: fiyonk -> top
Deniz kıyısında Hayri kumda küçük bir çukur kazmıştı. Hafif topunu bu küçük havuzda yüzdürmek istiyordu. Ama çukura hiç su gelmedi, çünkü çukur denizden çok uzaktaydı. Hayri bu kez abartarak suyun kenarına kadar çok uzun bir yol kazdı. Sonra yolun başına oturup bekledi. Küçük bir dalga geldi ve su yoldan akmaya başladı. Su yavaş yavaş çukura doldu. Hayri hafif topunu çukura doğru yuvarladı. Top suyun üstünde yüzmeye başladı. Hayri topu parmağıyla itti ve küçük havuzunda mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri bu kez abartarak"
   - Cümle 4: «Hayri bu kez abartarak suyun kenarına kadar çok uzun bir yol kazdı.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bu kez abartarak suyun kenarına"
   - Cümle 4: «Hayri bu kez abartarak suyun kenarına kadar çok uzun bir yol kazdı.»
   - Açıklama: Karttaki özellik olayları abartmaktır (anlatım); burada abartma fazla kazmak eylemine dönüştürülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0155` birebir aynı, `@degisim: fiyonk -> top` (tutuyorsan), ardından `@onarim: cc97af12996838a33e7cb2247ad7999e8d3198ab`, sonra gövde.

### Hikâye 2: tohum hayri-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0156
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'fasulye', fiil 'katlamak', sıfat 'parlak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: rüzgar kağıt bardağı uçurdu ve bardak yırtıldı | yemeğini yiyip boş kabı yeni hedef yaptı
@tohum: hayri-0156
Ormandaki kamp yerinde Hayri bir kağıdı katlayıp küçük bir bardak yaptı. Sonra uzaktan bu bardağa kuru fasulye atmaya başladı. Ama rüzgar esti ve hafif bardak uçup çalılarda yırtıldı. Hayri oyunun bitmesini hiç istemiyordu. O sırada Hayri çok acıkmıştı. Çantasından parlak yemek kabını çıkardı. İçindeki peynirli ekmeği afiyetle yedi. Sonra boş kabı bardağın yerine koydu. Bu kap ağırdı ve rüzgarda uçmadı. Hayri fasulyeleri yine tek tek attı. Her fasulye kaba düşünce tın diye komik bir ses çıktı. Hayri bu sese kahkahalarla güldü. Hayri çok mutluydu, çünkü oyunu yeniden oynayabiliyordu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıkmıştı"
   - Cümle 5: «O sırada Hayri çok acıkmıştı.»
   - Açıklama: Çözüm sorundan değil, rastlantıyla gelen açlıktan çıkıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İçindeki peynirli ekmeği afiyetle yedi"
   - Cümle 7: «İçindeki peynirli ekmeği afiyetle yedi.»
   - Açıklama: Çözüme sebepsizce araya giren bir yemek adımı ekleniyor; hafif bardak sorununa doğrudan yönelmiyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri çok mutluydu, çünkü"
   - Cümle 13: «Hayri çok mutluydu, çünkü oyunu yeniden oynayabiliyordu.»
   - Açıklama: 'Hayri' adı art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0156` birebir aynı, ardından `@onarim: 33a272ac03c7fa966a749b3a46a117d6bac4ee09`, sonra gövde.

### Hikâye 3: tohum hayri-0158 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0158
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'resim', fiil 'dağılmak', sıfat 'bomboş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: rüzgar masadaki resimleri her yere dağıttı | çadırda uyuyan arkadaşından yardım istedi
@tohum: hayri-0158
Bir sabah Hayri ormandaki kamp yerinde resim yapıyordu. Masada Hayri'nin çizdiği beş orman resmi vardı. Birden güçlü bir rüzgar esti ve resimler her yere dağıldı. Masa bomboş kaldı. Hayri bir resmi tutunca öteki uçuyordu. Kamil ise çadırda uyuyordu. Hayri çadıra koştu ve abarttı. "Kamil, uyan, resimler bütün ormana uçtu, bana yardım et!" diye bağırdı Hayri. Kamil bu komik sözleri duyunca hemen uyandı ve gülerek dışarı çıktı. İki arkadaş resimlerin peşinden koştu. Hayri üç resmi, Kamil iki resmi yakaladı. Hayri resimlerin üstüne birer taş koydu. "Teşekkürler, Kamil, bütün resimler burada!" dedi Hayri.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden güçlü bir rüzgar esti ve resimler her yere dağıldı"
   - Cümle 3: «Birden güçlü bir rüzgar esti ve resimler her yere dağıldı.»
   - Açıklama: Rüzgar resimleri dağıttı, toplandı, bitti türünden önemsiz bir sorun.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri bir resmi tutunca öteki uçuyordu"
   - Cümle 5: «Hayri bir resmi tutunca öteki uçuyordu.»
   - Açıklama: Bir önceki cümlede masa bomboş kalmışken Hayri'nin masadaki resimleri tutmaya çalışması çelişiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri çadıra koştu ve abarttı"
   - Cümle 7: «Hayri çadıra koştu ve abarttı.»
   - Açıklama: 'Abarttı' soyut bir kavram; 3 yaşındaki çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çadıra koştu ve abarttı"
   - Cümle 7: «Hayri çadıra koştu ve abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0158` birebir aynı, ardından `@onarim: a25b20883f8382f242ed820fd31a5b5a5dbfee27`, sonra gövde.

### Hikâye 4: tohum hayri-0159 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0159
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yama', fiil 'gezmek', sıfat 'ilginç'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: yerde uzun ve ilginç bir iz vardı | köpekle izi takip edip topu buldu
@tohum: hayri-0159
Güçlü bir rüzgar esiyordu. Hayri, köpek Yumak ile parkta geziyordu. Birden toprak yolda ilginç, uzun bir iz gördü ve çok merak etti. Hayri abarttı ve "Yumak, bu iz bir trenden kalmış!" dedi. Yumak bu heyecanlı sesi duyunca kuyruğunu salladı. Sonra burnunu yere dayadı ve izi koklayarak yürüdü. Hayri de onun arkasından gitti. İz salıncakların yanından geçip bankın altına uzanıyordu. Hayri eğilip bankın altına baktı. Orada üstünde yama olan eski, hafif bir top vardı. Rüzgar topu yolda yuvarlamış ve bu izi bırakmıştı. Yumak topu görünce sevinçle havladı. "Aferin, Yumak, izi yapan tren bu topmuş!" dedi Hayri gülerek.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerde uzun ve ilginç bir iz vardı"
   - Cümle 0 (plan satırı): «yerde uzun ve ilginç bir iz vardı | köpekle izi takip edip topu buldu»
   - Açıklama: Yerdeki iz bir sorun değil, yalnız merak uyandıran bir durum; çözülmesi gereken bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve"
   - Cümle 4: «Hayri abarttı ve "Yumak, bu iz bir trenden kalmış!" dedi.»
   - Açıklama: 'Abartmak' soyut kavram, 3 yaşındaki çocuğa uygun değil.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "burnunu yere dayadı ve izi koklayarak yürüdü"
   - Cümle 6: «Sonra burnunu yere dayadı ve izi koklayarak yürüdü.»
   - Açıklama: İzi Hayri değil Yumak takip edip çözüyor; Hayri yalnız arkasından gidiyor.
   - Açıklama: İzi koklayarak topa ulaştıran Yumak; Hayri yalnız arkasından gidiyor, yani asıl işi yan karakter yapıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rüzgar topu yolda yuvarlamış ve bu izi bırakmıştı"
   - Cümle 11: «Rüzgar topu yolda yuvarlamış ve bu izi bırakmıştı.»
   - Açıklama: İzi bırakan top olduğu halde 'bırakmıştı' fiilinin öznesi rüzgar oluyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "izi yapan tren bu topmuş"
   - Cümle 13: «"Aferin, Yumak, izi yapan tren bu topmuş!" dedi Hayri gülerek.»
   - Açıklama: Topa 'tren' denmesi yanlış anlamlı ve kafa karıştırıcı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0159` birebir aynı, ardından `@onarim: f97ce70118df7a548bb2a5ae52d9212d324a5a3f`, sonra gövde.

### Hikâye 5: tohum hayri-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0160
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'uçurtma', fiil 'bakmak', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: uçurtmanın kuyruğu yoktu ve uçurtma kuma düştü | acıkınca ekmeğini yedi ve peçeteden kuyruk yaptı
@tohum: hayri-0160
Hayri deniz kıyısında kağıttan bir uçurtma yapmıştı. Uçurtmayı rüzgara bıraktı ama uçurtma dönüp kuma düştü. Uçurtmanın kuyruğu yoktu, bu yüzden havada duramıyordu. Hayri çantasına baktı ama ip ya da kumaş bulamadı. O sırada Hayri çok acıkmıştı. Yemek kutusunu açtı ve peynirli ekmeğini yedi. Ekmek büyük, benekli bir peçetenin içindeydi. Hayri peçeteyi uzun bir şerit gibi büktü. Sonra onu uçurtmanın alt ucuna bağladı. Bu kuyruk uçurtmayı düz tuttu. Uçurtma yükseldi ve dalgaların üstünde uçtu. Hayri ipi tuttu ve sevinçle zıpladı. Hayri bundan sonra her uçurtmasına uzun bir kuyruk yaptı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıkmıştı"
   - Cümle 5: «O sırada Hayri çok acıkmıştı.»
   - Açıklama: Çözümü getiren peçete, sorunla ilgisiz ve tesadüfi bir acıkma ile sebepsizce ortaya çıkıyor.
   - Açıklama: Acıkma önceki olaydan çıkmıyor ve peçeteyi, dolayısıyla çözümü tesadüfle getiriyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yemek kutusunu açtı ve peynirli ekmeğini yedi"
   - Cümle 6: «Yemek kutusunu açtı ve peynirli ekmeğini yedi.»
   - Açıklama: Güvenli özellik kullanımı satırı yemek sevgisini paylaşmak, beklemek ya da hazırlamak olarak ister; burada Hayri acıkınca yalnız yiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0160` birebir aynı, ardından `@onarim: b9932190c480a0fbfe5befef7d0a617003092c7d`, sonra gövde.

### Hikâye 6: tohum hayri-0161 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0161
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'mikroskop', fiil 'susamak', sıfat 'yakın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: köpek çok susamıştı ama şişeden su içemedi | boş baklava tepsisine köpek için su döktü
@tohum: hayri-0161
@degisim: mikroskop -> tepsi
Parkta sıcak bir öğle vaktiydi. Hayri, bankın yanında köpek Yumak'ı gördü. Yumak dilini çıkarmıştı, çünkü çok susamıştı. Hayri çantasından su şişesini çıkardı. "Gel, Yumak, biraz su iç," dedi Hayri. Ama Yumak dar şişeden su içemedi. Hayri elindeki boş tepsiye baktı. Bu tepsiyi yakındaki baklava dükkanına, çalıştığı yere götürüyordu. Tepsiyi yere koydu ve içine su döktü. Yumak hemen yaklaştı ve suyu içti. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. "Afiyet olsun, Yumak, bol bol iç!" dedi Hayri gülerek.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri elindeki boş tepsiye baktı"
   - Cümle 7: «Hayri elindeki boş tepsiye baktı.»
   - Açıklama: Tepsi daha önce kurulmadan çözüm anında beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0161` birebir aynı, `@degisim: mikroskop -> tepsi` (tutuyorsan), ardından `@onarim: 339d2e2b60510ffe0ef832d7a15c5e8f392df2c4`, sonra gövde.

### Hikâye 7: tohum hayri-0162 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0162
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'balkabağı', fiil 'silmek', sıfat 'komik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: kabak elinden kayıp çamura düştü | cebindeki temiz bezle kabağı sildi
@tohum: hayri-0162
@degisim: balkabağı -> kabak
Bir sabah Hayri parkta Mert ile karşılaştı. Mert kocaman bir kabağı eve taşıyordu. Ama ıslak kabak Mert'in elinden kaydı ve çamura düştü. Turuncu kabak baştan sona kahverengi oldu. "Bunu eve böyle nasıl götüreyim?" dedi Mert. Hayri cebine baktı. Cebinde baklava dükkanında kullandığı temiz bir bez vardı. Hayri bezle kabağı yavaş yavaş sildi. Kabak yeniden turuncu ve parlak oldu. Mert'in burnunda da küçük bir çamur lekesi vardı. "Burnun çok komik olmuş, Mert," dedi Hayri ve onu da sildi. İkisi birlikte güldü. Hayri çok sevindi, çünkü Mert'in kabağı tertemiz olmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mert'in burnunda da küçük bir çamur lekesi"
   - Cümle 10: «Mert'in burnunda da küçük bir çamur lekesi vardı.»
   - Açıklama: Burundaki çamur lekesi sorunla ilgisi olmayan ek bir ayrıntı olarak beliriyor.
2. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: ""Burnun çok komik olmuş, Mert," dedi Hayri"
   - Cümle 11: «"Burnun çok komik olmuş, Mert," dedi Hayri ve onu da sildi.»
   - Açıklama: Hayri arkadaşının çamurlu burnunun görünüşü üzerine takılıyor; hafif alay örnek alınabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0162` birebir aynı, `@degisim: balkabağı -> kabak` (tutuyorsan), ardından `@onarim: d91184ea2360d9398743302685ce591abe14f078`, sonra gövde.

### Hikâye 8: tohum hayri-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0163
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'waffle', fiil 'dökmek', sıfat 'üzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga ekmeği ıslattı ve yiyecek kalmadı | acıkınca ilk kez waffle denedi ve sevdi
@tohum: hayri-0163
Bir sabah Hayri deniz kıyısında kumdan bir kale yapıyordu. Peynirli ekmeğini de havlunun üstüne koymuştu. Birden büyük bir dalga geldi ve ekmeği ıslattı. Hayri çok acıkmıştı ve üzgün bir yüzle ekmeğe baktı. Sonra çantasındakileri havlunun kuru ucuna döktü. İçinden bir waffle çıktı. Hayri daha önce hiç waffle yememişti. Üstündeki küçük kareler ona tuhaf geldi. Ama karnı açtı, bu yüzden küçük bir parça ısırdı. Waffle yumuşak ve tatlıydı. Hayri bir parça daha, sonra bir parça daha yedi. Karnı doyunca Hayri kumdan kalesini mutlu mutlu yapmaya devam etti.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "dalga ekmeği ıslattı ve yiyecek kalmadı"
   - Cümle 0 (plan satırı): «dalga ekmeği ıslattı ve yiyecek kalmadı | acıkınca ilk kez waffle denedi ve sevdi»
   - Açıklama: Planda yiyecek kalmadığı söyleniyor ama gövdede çantada waffle var.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden büyük bir dalga geldi"
   - Cümle 3: «Birden büyük bir dalga geldi ve ekmeği ıslattı.»
   - Açıklama: Çocuğun oturduğu yere ansızın büyük bir dalganın gelmesi küçük çocuk için korkutucu ve tehlikeli bir öğedir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İçinden bir waffle çıktı"
   - Cümle 6: «İçinden bir waffle çıktı.»
   - Açıklama: Waffle önceden kurulmadan çantadan sebepsizce çıkıp çözümü hazır getiriyor.
   - Açıklama: Waffle çantada sebepsizce beliriyor ve çözümü hazır getiriyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Üstündeki küçük kareler ona tuhaf geldi"
   - Cümle 8: «Üstündeki küçük kareler ona tuhaf geldi.»
   - Açıklama: Islanan ekmek sorununun yanına yeni yiyeceği denemekten çekinme diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0163` birebir aynı, ardından `@onarim: e42deadfbdb02f42e2907a7c0ddcf26d20494067`, sonra gövde.

### Hikâye 9: tohum hayri-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0164
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'karpuz', fiil 'kaplamak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: karpuz dilimi elden kayıp toprağa düştü | dükkandan getirdiği baklavayı arkadaşıyla paylaştı
@tohum: hayri-0164
Hayri bahçede Kamil ile yan yana oturuyordu. Hayri'nin tabağında iki dilim baklava, Kamil'in elinde bir dilim karpuz vardı. Ama aceleci Kamil karpuzu hızlı ısırınca karpuz elinden kaydı ve toprağa düştü. Toprak kırmızı karpuzun her yerini kapladı. Kamil boş eline üzgün üzgün baktı. Hayri bu baklavaları çalıştığı dükkandan getirmişti. Hayri bir dilim baklavayı Kamil'e uzattı. Kamil baklavayı aldı ve sevinçle gülümsedi. İki arkadaş baklavalarını birlikte yedi. Sonra yere düşen karpuzu birlikte çöpe attılar. Kamil, Hayri'ye tatlı için teşekkür etti. Hayri bundan sonra baklavasını her zaman arkadaşlarıyla paylaştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri bahçede Kamil ile"
   - Cümle 1: «Hayri bahçede Kamil ile yan yana oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye evden hiç söz etmeden bir bahçede geçiyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Ama aceleci Kamil karpuzu"
   - Cümle 3: «Ama aceleci Kamil karpuzu hızlı ısırınca karpuz elinden kaydı ve toprağa düştü.»
   - Açıklama: Kartın yanlar alanında Kamil uykuyu ve kitabı seven biri; aceleci olarak göstermek yanlış bilgi veriyor.
   - Açıklama: Kartın yanlar bölümünde Kamil uyumayı ve kitap okumayı seven biri; aceleci huyu yanlış bilgi.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Toprak kırmızı karpuzun her yerini kapladı"
   - Cümle 4: «Toprak kırmızı karpuzun her yerini kapladı.»
   - Açıklama: Toprak karpuzu kaplamaz; fiil öznesine uygun değil, 'karpuz toprağa bulandı' olmalı.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri bir dilim baklavayı Kamil'e uzattı"
   - Cümle 7: «Hayri bir dilim baklavayı Kamil'e uzattı.»
   - Açıklama: Çözüm karpuzun düşme sebebine yönelmiyor, yalnız başka bir yiyecekle telafi ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0164` birebir aynı, ardından `@onarim: 5f505c91449140939b8c76ce8d5625f4dab1a3ec`, sonra gövde.

### Hikâye 10: tohum hayri-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0165
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'karabiber', fiil 'düzeltmek', sıfat 'ağır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: rüzgar sandviçlere kum savurdu | sandviçleri baklava kutusuna koyup kapağı kapattı
@tohum: hayri-0165
Deniz kıyısında Hayri ile Akın havlunun üstünde sandviç yapıyordu. Akın yumurtaların üstüne biraz karabiber serpti. Ama rüzgar esti ve sandviçlere kum savurdu. "Hayri, sandviçler kumlu olacak!" dedi Akın. Hayri çantasından çalıştığı baklava dükkanının boş kutusunu çıkardı. Sandviçleri tek tek kutunun içine dizdi. Kapak biraz yamuk kalmıştı, Hayri onu düzeltti. Sonra kutunun üstüne ağır bir taş koydu. Rüzgar yine esti ama kutunun içine kum giremedi. "Harika fikir, Hayri!" dedi Akın. İkisi sandviçleri kutudan tek tek alıp yedi. Karınları doyunca Hayri ile Akın kumda mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yumurtaların üstüne biraz karabiber serpti"
   - Cümle 2: «Akın yumurtaların üstüne biraz karabiber serpti.»
   - Açıklama: Karabiber ayrıntısı olayda hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Akın yumurtaların üstüne biraz karabiber serpti"
   - Cümle 2: «Akın yumurtaların üstüne biraz karabiber serpti.»
   - Açıklama: Karabiber ayrıntısı olayda hiçbir işe yaramıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "rüzgar esti ve sandviçlere kum savurdu"
   - Cümle 3: «Ama rüzgar esti ve sandviçlere kum savurdu.»
   - Açıklama: Sandviçlere kum zaten savrulmuşken kutuya konup sonra sorunsuz yenmeleri çelişiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kutunun üstüne ağır bir taş koydu"
   - Cümle 8: «Sonra kutunun üstüne ağır bir taş koydu.»
   - Açıklama: Çözüm kutuya koyma, kapağı düzeltme ve taş koyma ile iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0165` birebir aynı, ardından `@onarim: cc5e81dfeb2beb8f9fc6a88a012577bc818a2cd9`, sonra gövde.

### Hikâye 11: tohum hayri-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0166
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'iplik', fiil 'rahatlatmak', sıfat 'çekingen'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kutuyu çeken ince iplik koptu | kutunun kalın kırmızı ipini bağladı
@tohum: hayri-0166
@degisim: çekingen -> kırmızı
Rüzgar hafif hafif esiyordu. Hayri parkta boş bir baklava kutusunu ipliğe bağlamış, araba gibi çekiyordu. Ama kutu bir taşa takıldı ve ince iplik koptu. Hayri kopan ipliğe üzgün üzgün baktı. Dükkanda her baklava kutusunda kalın, kırmızı bir ip olurdu. Bu kutunun kırmızı ipi de cebindeydi. Hayri kırmızı ipi kutuya sıkıca bağladı. Sonra kutunun içine üç küçük taş koydu. Kalın ip çok sağlamdı ve bu Hayri'yi rahatlattı. Hayri kutuyu kaydırağın etrafında hızlı hızlı çekti. İçindeki taşlar her adımda komik bir ses çıkardı. Hayri bu sese kahkahalarla güldü. Hayri çok mutluydu, çünkü araba oyunu yeniden başlamıştı.
```

**Hakem bulguları (4):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "her baklava kutusunda kalın, kırmızı bir ip olurdu"
   - Cümle 5: «Dükkanda her baklava kutusunda kalın, kırmızı bir ip olurdu.»
   - Açıklama: Anlatım -dı'lı geçmişten geniş zamanlı genel anlatıma kayıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kutunun kırmızı ipi de cebindeydi"
   - Cümle 6: «Bu kutunun kırmızı ipi de cebindeydi.»
   - Açıklama: Çözümü getiren kalın ip sebepsizce cepte beliriyor; varken neden ince iplik kullanıldığı açıklanmıyor.
   - Açıklama: Kalın ip çözüm anında sebepsizce cepte beliriyor ve kalın ip varken neden ince iplik kullanıldığı açıklanmıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu Hayri'yi rahatlattı"
   - Cümle 9: «Kalın ip çok sağlamdı ve bu Hayri'yi rahatlattı.»
   - Açıklama: 'Bu' ile duyguya bağlanan soyut anlatım küçük çocuğa uygun değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bu Hayri'yi rahatlattı"
   - Cümle 9: «Kalın ip çok sağlamdı ve bu Hayri'yi rahatlattı.»
   - Açıklama: 'bu' zamirinin neyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0166` birebir aynı, `@degisim: çekingen -> kırmızı` (tutuyorsan), ardından `@onarim: e9b68ff295e9233028f126713df83c4073ed91ca`, sonra gövde.

### Hikâye 12: tohum hayri-0167 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0167
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'uçak', fiil 'değiştirmek', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kağıt uçak çok hafifti ve hemen düşüyordu | acıkınca kutunun lastiğini uçağın burnuna taktı
@tohum: hayri-0167
Hayri deniz kıyısında Basri Amca'yı gördü. Basri Amca mavi bir kağıttan uçak yapmıştı. Ama uçak çok hafifti ve havada sallanıp hemen kuma düşüyordu. Basri Amca kağıdı iki kez değiştirdi ama uçak yine uçmadı. O sırada Hayri acıktı ve yemek kutusunu açtı. Kutunun etrafında küçük bir lastik vardı. Hayri lastiği çıkardı ve uçağın burnuna taktı. Basri Amca uçağı yeniden fırlattı. Mavi uçak bu kez uzağa kadar düz uçtu. Basri Amca gülerek ellerini çırptı. Hayri de ekmeğini amcanın yanında oturup yedi. Hayri çok sevindi, çünkü Basri Amca'nın uçağı sonunda uçmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri acıktı ve yemek kutusunu açtı"
   - Cümle 5: «O sırada Hayri acıktı ve yemek kutusunu açtı.»
   - Açıklama: Çözümü getiren lastik, soruna yönelmeden sebepsiz bir acıkmayla ortaya çıkıyor.
   - Açıklama: Çözümü getiren lastik, Hayri'nin tesadüfen acıkmasıyla sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0167` birebir aynı, ardından `@onarim: 4a20ef0d61a7f60d006e2f8ae6a193a792a50072`, sonra gövde.
