# Editör görevi (onarım): Hayri, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0148 (deneme 2 -> 3)

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
@plan: top çok büyüktü ve köpek onu ağzıyla tutamadı | acıkınca kutusunu açtı ve hafif kapağı attı
@tohum: hayri-0148
@degisim: saçmak -> atmak
Parkta taşların üstünde yeşil yosunlar vardı. Hayri, Yumak'la yeni bir oyun denemek istiyordu. Hayri bir şey atacak, Yumak da onu havada yakalayacaktı. Ama top çok büyüktü ve Yumak onu ağzıyla tutamadı. Tam o sırada Hayri acıktı. Çantasından yuvarlak yemek kutusunu çıkardı ve kapağını açtı. Kapak düz ve çok hafifti. Hayri kapağı havaya attı. Kapak uçtu ve yosunlu bir taşın üstüne düştü. Yumak koştu, kapağı ağzına aldı ve geri getirdi. "Ne şanslıyım, Yumak, yeni bir oyunumuz oldu!" dedi Hayri. Hayri sandviçini yedi ve kapağı yine attı. Bu sefer Yumak kapağı havada yakaladı. İkisi kapak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 5: «Tam o sırada Hayri acıktı.»
   - Açıklama: Çözüm büyük top sorununa yönelmiyor, tesadüfi bir acıkmayla geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 5: «Tam o sırada Hayri acıktı.»
   - Açıklama: Çözümü getiren kapak sebepsizce, yalnız acıkma tesadüfüyle ortaya çıkıyor.
   - Açıklama: Çözümü getiren kapak, tesadüfi bir acıkmayla sebepsizce ortaya çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yosunlu bir taşın üstüne düştü"
   - Cümle 9: «Kapak uçtu ve yosunlu bir taşın üstüne düştü.»
   - Açıklama: Yosunlu taşlar kuruluyor ama olayda hiçbir işe yaramıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ne şanslıyım, Yumak, yeni bir oyunumuz oldu"
   - Cümle 11: «"Ne şanslıyım, Yumak, yeni bir oyunumuz oldu!" dedi Hayri.»
   - Açıklama: Çözüm topun büyüklüğüne yönelmiyor, kapak tesadüfen atılınca şans eseri ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0148` birebir aynı, `@degisim: saçmak -> atmak` (tutuyorsan), ardından `@onarim: a30963cfc5c0ac55654890450b1bc221f7c6e1fd`, sonra gövde.

### Hikâye 2: tohum hayri-0149 (deneme 2 -> 3)

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
Bir sabah Hayri deniz kıyısında bir çubukla kuma bıyıklı bir patates çizdi. Patates küçüktü ve çizgileri çok inceydi. Ama rüzgar kumu savurdu ve ince çizgiler kapandı. Komik patates hemen kayboldu. Hayri elindeki çubuğa baktı ve biraz düşündü. Sonra patatesin her yerini abartıp yeniden çizdi. Kumda ayaklarıyla büyük bir daire çizerek dolaştı. Daireye iki kocaman göz ve çok uzun bir bıyık ekledi. Çizgiler bu kez hem geniş hem de derindi. Rüzgar yine esti ama büyük patates kaybolmadı. Hayri patatesin ortasına oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri elindeki çubuğa baktı ve biraz düşündü"
   - Cümle 5: «Hayri elindeki çubuğa baktı ve biraz düşündü.»
   - Açıklama: Çubuk çözümün aracı gibi kuruluyor ama Hayri yeni patatesi ayaklarıyla çiziyor, çubuk işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "patatesin her yerini abartıp yeniden"
   - Cümle 6: «Sonra patatesin her yerini abartıp yeniden çizdi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "patatesin her yerini abartıp"
   - Cümle 6: «Sonra patatesin her yerini abartıp yeniden çizdi.»
   - Açıklama: 'Abartmak' soyut ve 3 yaşındaki çocuğun bilmediği bir kelime.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "patatesin her yerini abartıp yeniden çizdi"
   - Cümle 6: «Sonra patatesin her yerini abartıp yeniden çizdi.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartı büyük çizim yapmak olarak kullanılmış, karttaki gibi değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra patatesin her yerini abartıp yeniden çizdi"
   - Cümle 6: «Sonra patatesin her yerini abartıp yeniden çizdi.»
   - Açıklama: Kartta özellik olayları abartmaktır; burada abartma sözle değil çizimi büyütmek olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0149` birebir aynı, `@degisim: kibar -> kocaman` (tutuyorsan), ardından `@onarim: ea0808de521d06679a17397e47acbe275fe01fe7`, sonra gövde.

### Hikâye 3: tohum hayri-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0150
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'tablo', fiil 'dolanmak', sıfat 'buzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: arkadaşı tablo yüzünden önündeki buzu göremedi | bağırıp onu durdurdu ve buzun etrafından dolandılar
@tohum: hayri-0150
Soğuk bir rüzgar esiyordu. Hayri sokakta arkadaşı Kamil'i gördü. Kamil iki eliyle evine bir tablo taşıyordu. Tablo çok büyüktü ve Kamil ayaklarını göremiyordu. Önündeki yolda buzlu bir yer vardı. "Dur, Kamil, önünde kocaman bir buz dağı var!" diye abartarak bağırdı Hayri. Kamil hemen durdu ve yana eğilip baktı. "Dağ değil ama yer gerçekten çok kaygan," dedi Kamil. Hayri tabloyu bir ucundan tuttu. İkisi buzun etrafından yavaşça dolandı. Birlikte Kamil'in kapısına kadar yürüdüler. Hayri çok sevindi, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri sokakta arkadaşı Kamil'i gördü"
   - Cümle 2: «Hayri sokakta arkadaşı Kamil'i gördü.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta geçiyor.
   - Açıklama: Hikaye başlıktaki evde değil sokakta geçiyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Tablo çok büyüktü ve Kamil ayaklarını göremiyordu.»
   - Açıklama: Kamil'in önünü görememesi ve buz ancak 4. ve 5. cümlelerde söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak bağırdı Hayri"
   - Cümle 6: «"Dur, Kamil, önünde kocaman bir buz dağı var!" diye abartarak bağırdı Hayri.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 'buz dağı' abartısı 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Abartarak' soyut bir kavram, 3 yaşındaki çocuk bu kelimeyi bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0150` birebir aynı, ardından `@onarim: a7d571a85463cfeafb7b17b9b965dba772b04754`, sonra gövde.

### Hikâye 4: tohum hayri-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0151
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tüy', fiil 'güzelleşmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: arkadaşı çok iyi saklandı ve bulunamadı | bisküvi paketini açıp arkadaşını yemeye çağırdı
@tohum: hayri-0151
@degisim: tüy -> bisküvi
Hayri ile Akın evin güvenli bahçesinde saklambaç oynuyordu. Akın çalıların arkasına saklandı. Hayri her yere baktı ama Akın'ı bulamadı, çünkü Akın çok iyi saklanmıştı. "Neredesin, Akın?" diye seslendi Hayri. Ama Akın hiç ses çıkarmadı. Hayri acıkmıştı ve cebindeki bisküvileri Akın'la yemek istiyordu. Paketi açtı ve paket hışır hışır ses çıkardı. "Akın, gel, bisküvi yiyelim!" diye seslendi Hayri. Birden çalıların arkasından Akın'ın başı göründü. "Seni buldum, Akın!" dedi Hayri ve güldü. Bisküvileri paylaşınca oyun daha da güzelleşti. Sonra Hayri ile Akın oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "evin güvenli bahçesinde saklambaç"
   - Cümle 1: «Hayri ile Akın evin güvenli bahçesinde saklambaç oynuyordu.»
   - Açıklama: 'Güvenli' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Güvenli' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: ""Seni buldum, Akın!" dedi Hayri"
   - Cümle 10: «"Seni buldum, Akın!" dedi Hayri ve güldü.»
   - Açıklama: Hayri Akın'ı bulmuyor, Akın bisküvi çağrısıyla kendisi çıkıyor; yine de Hayri onu bulmuş gibi konuşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0151` birebir aynı, `@degisim: tüy -> bisküvi` (tutuyorsan), ardından `@onarim: 482002d7d53c883f3168bb57c54da33cd39de8c1`, sonra gövde.

### Hikâye 5: tohum hayri-0152 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0152
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tahta', fiil 'güldürmek', sıfat 'biberli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: dalga kaleyi yıktı ve arkadaşı üzüldü | tahtayla yeni kaleyi korudu ve sandviç hazırladı
@tohum: hayri-0152
Deniz kıyısında Hayri ile Mert kumdan bir kale yapmıştı. Ama küçük bir dalga geldi ve kaleyi yıktı. Mert buna çok üzüldü. Hayri, Mert'i güldürmek için bir sürpriz hazırlamak istedi. "Mert, gözlerini kapat ve bekle!" dedi Hayri. Hayri yeni bir kale yaptı. Kıyıda düz bir tahta buldu ve onu kalenin önüne dikti. Su tahtaya çarptı ve kaleye gelemedi. Hayri acıkmıştı ama çantasındaki iki biberli sandviçi yemedi. Onları Mert için kalenin yanına koydu. "Sürpriz, Mert, gel bak!" dedi Hayri. Mert yeni kaleyi ve sandviçleri görünce çok güldü. İkisi yan yana oturup sandviçleri paylaştı. "Teşekkürler, Hayri, bu en güzel sürpriz!" dedi Mert.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "tahtayla yeni kaleyi korudu ve sandviç hazırladı"
   - Cümle 0 (plan satırı): «dalga kaleyi yıktı ve arkadaşı üzüldü | tahtayla yeni kaleyi korudu ve sandviç hazırladı»
   - Açıklama: Çözüm yeni kale yapmak, tahta dikmek ve sandviç hazırlamak olarak iki adımı aşıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kıyıda düz bir tahta buldu"
   - Cümle 7: «Kıyıda düz bir tahta buldu ve onu kalenin önüne dikti.»
   - Açıklama: Tahta önceden kurulmadan çözüm için sebepsizce beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasındaki iki biberli sandviçi yemedi"
   - Cümle 9: «Hayri acıkmıştı ama çantasındaki iki biberli sandviçi yemedi.»
   - Açıklama: Sandviçler yıkılan kale sorununa bağlı değil, çözüme sonradan eklenmiş işlevsiz bir ayrıntı.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Onları Mert için kalenin yanına koydu"
   - Cümle 10: «Onları Mert için kalenin yanına koydu.»
   - Açıklama: Çözüm yeni kale, tahta ve sandviç olmak üzere ikiden fazla adıma yayılıyor ve sandviç yıkılan kaleye yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0152` birebir aynı, ardından `@onarim: c269c9d5a2c79986fb055c85aa5a13f4e53e162f`, sonra gövde.

### Hikâye 6: tohum hayri-0153 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0153
- yer: park (Mahallenin çocuk parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'heykel', fiil 'aydınlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: doğum gününde yağmur yağdı ve arkadaşı ıslandı | ona havlu verdi ve sakladığı kurabiyelerle sürpriz yaptı
@tohum: hayri-0153
@degisim: heykel -> kurabiye
Bir sabah Hayri ile Akın parktaydı ve o gün Akın'ın doğum günüydü. Birden kısa bir yağmur yağdı ve Akın sırılsıklam oldu. Akın, doğum gününde ıslak kaldığı için çok üzüldü. Hayri çantasından kuru bir havlu çıkardı ve Akın'a verdi. Akın saçını ve kollarını havluyla kuruladı. Yağmur bitince park aydınlandı. Hayri çok acıkmıştı ama çantasındaki kurabiyeleri yememişti. Onları Akın'a sürpriz yapmak için saklamıştı. Hayri kurabiye kutusunu açtı. "İyi ki doğdun, Akın!" dedi Hayri. Akın kurabiyelere baktı ve sevinçle güldü. "Hepsi benim için mi?" diye sordu Akın. "Hayır, ikimiz için," dedi Hayri. Sonra Hayri ile Akın kurabiyeleri paylaştı ve mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çantasından kuru bir havlu çıkardı"
   - Cümle 4: «Hayri çantasından kuru bir havlu çıkardı ve Akın'a verdi.»
   - Açıklama: Parkta çantada kuru bir havlu bulunması kurulmadan çözümü sebepsizce getiriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasındaki kurabiyeleri yememişti"
   - Cümle 7: «Hayri çok acıkmıştı ama çantasındaki kurabiyeleri yememişti.»
   - Açıklama: Kurabiyeler önceden kurulmadan çözümün ortasında birden beliriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri kurabiye kutusunu açtı"
   - Cümle 9: «Hayri kurabiye kutusunu açtı.»
   - Açıklama: Kurabiye sürprizi sorunun sebebine (ıslanmaya) yönelmiyor ve çözüm havluyu aşan ek bir adım oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0153` birebir aynı, `@degisim: heykel -> kurabiye` (tutuyorsan), ardından `@onarim: 88afcb99d8a4693eb6af80e7346278cdca1cd465`, sonra gövde.

### Hikâye 7: tohum hayri-0154 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0154
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'dal', fiil 'uyumak', sıfat 'taze'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: tahterevalli için arkadaşı gerekiyordu ama o uyuyordu | acıkınca poğaça çıkardı ve kokusuyla arkadaşını uyandırdı
@tohum: hayri-0154
Hafif bir rüzgar esiyordu. Hayri parktaki yeni tahterevalliyi denemek istiyordu. Ama bunun için bir arkadaş gerekiyordu ve Mert uyuyordu. Mert geniş bir dalın gölgesinde çimlere uzanmıştı. Tam o sırada Hayri acıktı ve çantasından poğaçaları çıkardı. Poğaçalar çok güzel kokuyordu. Hayri bir poğaçayı Mert'in burnuna yaklaştırdı. Mert kokuyu aldı ve gözlerini açtı. "Poğaça mı var, Hayri?" diye sordu Mert. "Evet, taze poğaça var, gel birlikte yiyelim," dedi Hayri. İkisi poğaçaları paylaştı. Sonra yan yana yürüyüp tahterevalliye bindiler. Hayri çok mutluydu, çünkü yeni tahterevalliyi sonunda denemişti.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Mert geniş bir dalın gölgesinde çimlere uzanmıştı"
   - Cümle 4: «Mert geniş bir dalın gölgesinde çimlere uzanmıştı.»
   - Açıklama: Kartın yanlar alanında uyumayı seven Kamil'dir; Mert sakin ve düzenli biri olarak tanımlanır, dizi izleyicisi için karışık bilgi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 5: «Tam o sırada Hayri acıktı ve çantasından poğaçaları çıkardı.»
   - Açıklama: Çözümü getiren acıkma tesadüfen ortaya çıkıyor; çözüm sebepsizce geliyor.
   - Açıklama: Çözümü getiren poğaça, Hayri'nin tesadüfen acıkmasıyla sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0154` birebir aynı, ardından `@onarim: f006117b87fef2e5e3f83c01f152cfc2fa85c48a`, sonra gövde.

### Hikâye 8: tohum hayri-0155 (deneme 2 -> 3)

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
@plan: kazdığı çukura su gelmedi çünkü çukur denizden uzaktı | suyun kenarına kadar uzun bir yol kazdı
@tohum: hayri-0155
@degisim: fiyonk -> top
Deniz kıyısında Hayri kumda küçük bir çukur kazmıştı. Hafif topunu bu küçük havuzda yüzdürmek istiyordu. Ama çukura hiç su gelmedi, çünkü çukur denizden çok uzaktaydı. Hayri bu kez suyun kenarına kadar çok uzun bir yol kazdı. Sonra yolun başına oturup bekledi. Küçük bir dalga geldi ve su yoldan akmaya başladı. Su yavaş yavaş çukura doldu. Hayri abartıp bu çukura kocaman göl adını verdi. Sonra hafif topunu çukura doğru yuvarladı. Top suyun üstünde yüzmeye başladı. Hayri topu parmağıyla itti ve gölünde mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çok uzun bir yol kazdı"
   - Cümle 4: «Hayri bu kez suyun kenarına kadar çok uzun bir yol kazdı.»
   - Açıklama: Su için kazılan şey yol değil ark ya da kanaldır; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıp bu çukura"
   - Cümle 8: «Hayri abartıp bu çukura kocaman göl adını verdi.»
   - Açıklama: 'abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Abartıp' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp bu çukura"
   - Cümle 8: «Hayri abartıp bu çukura kocaman göl adını verdi.»
   - Açıklama: Abartma özelliği sorun çözüldükten sonra süs olarak geçiyor, işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp bu çukura kocaman göl"
   - Cümle 8: «Hayri abartıp bu çukura kocaman göl adını verdi.»
   - Açıklama: Tohumdaki abartma özelliği sorun çözüldükten sonra yalnız süs olarak geçiyor, olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0155` birebir aynı, `@degisim: fiyonk -> top` (tutuyorsan), ardından `@onarim: 7a2e1b72a7ce4decfd3744fbf46fc1873bc38f7a`, sonra gövde.

### Hikâye 9: tohum hayri-0156 (deneme 2 -> 3)

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
@plan: rüzgar kağıt bardağı uçurdu ve bardak yırtıldı | ağır yemek kabını yeni hedef yaptı
@tohum: hayri-0156
Ormandaki kamp yerinde Hayri bir kağıdı katlayıp küçük bir bardak yaptı. Sonra uzaktan bu bardağa kuru fasulye atmaya başladı. Ama rüzgar esti ve hafif bardak uçup çalılarda yırtıldı. Hayri oyunun bitmesini hiç istemiyordu. Ağır bir şey aradı ve çantasından parlak yemek kabını çıkardı. Çok acıkmıştı ama yemeğini oyundan sonra yiyecekti. Dolu kabı bardağın yerine koydu. Bu kap ağırdı ve rüzgarda uçmadı. Hayri fasulyeleri yine tek tek attı. Her fasulye kabın kapağına düşünce tın diye komik bir ses çıktı. Bu sese kahkahalarla güldü. Hayri çok sevindi, çünkü fasulye oyunu yeniden başlamıştı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağır yemek kabını yeni hedef yaptı"
   - Cümle 0 (plan satırı): «rüzgar kağıt bardağı uçurdu ve bardak yırtıldı | ağır yemek kabını yeni hedef yaptı»
   - Açıklama: 'Hedef' kelimesi 3 yaşındaki bir çocuk için soyut ve bilinmedik.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bardağa kuru fasulye atmaya"
   - Cümle 2: «Sonra uzaktan bu bardağa kuru fasulye atmaya başladı.»
   - Açıklama: Küçük çocukların taklit edeceği kuru fasulyeyle oyun boğulma ya da burna kaçma tehlikesi taşır.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı ama yemeğini oyundan sonra"
   - Cümle 6: «Çok acıkmıştı ama yemeğini oyundan sonra yiyecekti.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümünde işe yaramıyor, süs olarak kalıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı ama yemeğini"
   - Cümle 6: «Çok acıkmıştı ama yemeğini oyundan sonra yiyecekti.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız süs olarak anılıyor; çözümü ağır kap sağlıyor, açlık sorunun çözümüne katkı vermiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı ama yemeğini oyundan sonra yiyecekti"
   - Cümle 6: «Çok acıkmıştı ama yemeğini oyundan sonra yiyecekti.»
   - Açıklama: Hayri'nin acıkması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Açlık ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0156` birebir aynı, ardından `@onarim: 13059829a3bc4a7ffd517bd6ca09c23d01c3d193`, sonra gövde.

### Hikâye 10: tohum hayri-0157 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0157
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'koza', fiil 'unutmak', sıfat 'faydalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca çadırın ipini kozanın olduğu dala bağlamak istedi | bağırıp amcayı durdurdu ve ip başka ağaca bağlandı
@tohum: hayri-0157
Hayri, Basri Amca ile ormandaki kamp yerinde çadır kuruyordu. Basri Amca çadırın ipini bir ağaç dalına bağlamak istedi. Ama o dalda küçük bir koza vardı ve Basri Amca onu görmemişti. "Dur, amca, o dalda kocaman bir koza var!" diye abartarak bağırdı Hayri. Basri Amca hemen durdu ve dala dikkatle baktı. "Kocaman değil ama güzel bir koza, ona dokunmayalım," dedi Basri Amca. Sonra ipi başka bir ağaca bağladı. Hayri de çadırın öbür ucunu tuttu. Çadır kuruldu ve koza dalında kaldı. "İyi ki bağırdın, Hayri, çok faydalı oldu, hiç unutmayacağım!" dedi Basri Amca.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak bağırdı"
   - Cümle 4: «"Dur, amca, o dalda kocaman bir koza var!" diye abartarak bağırdı Hayri.»
   - Açıklama: 'Abartarak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak bağırdı Hayri"
   - Cümle 4: «"Dur, amca, o dalda kocaman bir koza var!" diye abartarak bağırdı Hayri.»
   - Açıklama: 'Abartarak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok faydalı oldu, hiç unutmayacağım"
   - Cümle 10: «"İyi ki bağırdın, Hayri, çok faydalı oldu, hiç unutmayacağım!" dedi Basri Amca.»
   - Açıklama: 'Faydalı' soyut bir kelime; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0157` birebir aynı, ardından `@onarim: 55a923fea86b25bfe7b16dd643c34b99043366ca`, sonra gövde.

### Hikâye 11: tohum hayri-0158 (deneme 2 -> 3)

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
@plan: rüzgar kalem kutusunu düşürdü ve kalemler dağıldı | arkadaşından yardım isteyip kalemleri birlikte buldu
@tohum: hayri-0158
Bir sabah Hayri ormandaki kamp yerinde resim yapmak istedi. Kağıdı bomboştu, kalem kutusu da masanın kenarındaydı. Ama rüzgar kutuyu yere düşürdü ve kalemler yaprakların arasına dağıldı. Hayri yaprakların arasına baktı ama yalnız bir kalem buldu. Kamil ağacın altında kitap okuyordu. Hayri ona koştu. "Kamil, kalemlerim bütün ormanda kayboldu, yardım et!" dedi Hayri abartarak. Kamil güldü ve kitabını kapattı. "Bütün orman değil, yalnız masanın altı," dedi Kamil. İki arkadaş yaprakları tek tek kaldırdı. Kırmızı, mavi ve sarı kalemleri buldular. Hayri kalemleri kutuya koydu ve kutuyu masanın ortasına bıraktı. "Teşekkürler, Kamil, kalemlerin hepsi burada!" dedi Hayri.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar kutuyu yere düşürdü ve kalemler yaprakların arasına dağıldı"
   - Cümle 3: «Ama rüzgar kutuyu yere düşürdü ve kalemler yaprakların arasına dağıldı.»
   - Açıklama: Rüzgarın dağıttığı kalemleri toplayıp bitirmek, örnekteki gibi önemsiz bir sorun.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 7: «"Kamil, kalemlerim bütün ormanda kayboldu, yardım et!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelimedir.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Teşekkürler, Kamil, kalemlerin hepsi burada"
   - Cümle 13: «"Teşekkürler, Kamil, kalemlerin hepsi burada!" dedi Hayri.»
   - Açıklama: Hikayenin hedefi resim yapmaktı ama sona kadar resme hiç dönülmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0158` birebir aynı, ardından `@onarim: 8409a96a2c5454854414369cdceb223282725639`, sonra gövde.

### Hikâye 12: tohum hayri-0159 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar topu yuvarladı ve top kayboldu | kumdaki izin peşinden gidip topu buldu
@tohum: hayri-0159
Rüzgar hızlı hızlı esiyordu. Hayri, köpek Yumak ile parkta geziyordu. Birden Hayri'nin yamalı topu elinden düştü ve rüzgarla uzağa yuvarlandı. Hayri etrafa baktı ama topu göremedi. "Yumak, topum çok uzağa, denize kadar gitti!" dedi Hayri abartarak. Yumak kuyruğunu salladı ve havladı. Sonra Hayri kumun üstünde ilginç, ince bir iz gördü. İz salıncakların arkasına doğru gidiyordu. Hayri bu izi merak etti ve izin peşinden yürüdü. İz bankın altında bitiyordu. Hayri eğildi ve bankın altında yamalı topunu buldu. Top rüzgarla yuvarlanmış ve kumda bu izi bırakmıştı. Yumak topu görünce sevinçle havladı. "Bak, Yumak, topum denizde değil, burada!" dedi Hayri gülerek.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Yumak, topum çok uzağa, denize kadar gitti!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri bu izi merak etti ve izin peşinden yürüdü"
   - Cümle 9: «Hayri bu izi merak etti ve izin peşinden yürüdü.»
   - Açıklama: Hayri izi topu aramak için değil merakla izliyor; top tesadüfen bulunuyor, çözüm sebebe bilinçli yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0159` birebir aynı, ardından `@onarim: 3e053ee5413221bd8ad192e634a11852182e4d1b`, sonra gövde.
