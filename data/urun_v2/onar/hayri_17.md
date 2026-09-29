# Editör görevi (onarım): Hayri, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0048 (deneme 2 -> 3)

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
Hayri deniz kıyısında küreğiyle yumuşak kumda bir çukur kazıyordu. Hayri abartmadı, küçük bir havuz yapmak istedi. Ama çukur sudan uzaktı ve içine hiç su gelmedi. Hayri durdu ve denize dikkatle baktı. Dalgaların kıyıya gelip geri gittiğini fark etti. Sonra çukurdan denize doğru ince bir yol kazdı. Az sonra bir dalga geldi. Su yolun içinde yavaş yavaş ilerledi ve çukura aktı. Dalgalar geldi ve havuz biraz daha doldu. Hayri sevinçle zıpladı ve ellerini çırptı. Hayri bundan sonra havuzuna suyu hep böyle bir yoldan getirdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartmadı, küçük bir havuz"
   - Cümle 2: «Hayri abartmadı, küçük bir havuz yapmak istedi.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartmadı, küçük"
   - Cümle 2: «Hayri abartmadı, küçük bir havuz yapmak istedi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartmadı, küçük bir havuz"
   - Cümle 2: «Hayri abartmadı, küçük bir havuz yapmak istedi.»
   - Açıklama: Tohumdaki abartma özelliği yalnız olumsuzlanarak anılıyor, işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartmadı, küçük bir"
   - Cümle 2: «Hayri abartmadı, küçük bir havuz yapmak istedi.»
   - Açıklama: Tohumdaki abartma özelliği olumsuzlanarak geçiyor ve hikayede işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0048` birebir aynı, ardından `@onarim: 84e0a9f6ea2c2b056804988f9a779e53fb6e73d6`, sonra gövde.

### Hikâye 2: tohum hayri-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0049
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'güneş', fiil 'selamlamak', sıfat 'mutsuz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek onu selamladı ama o hiç bakmadı | köpekten özür diledi ve köpeğin başını okşadı
@tohum: hayri-0049
Ormandaki kamp yerinde güneş yeni doğuyordu. Hayri çok acıkmıştı ve ekmeğine peynir koyuyordu. Yumak koşup onu selamladı, ama Hayri ona hiç bakmadı. Yumak kuyruğunu indirdi ve bir ağacın altına oturdu. Köpek çok mutsuz görünüyordu. Hayri bunu görünce üzüldü. Ekmeğini bıraktı ve Yumak'ın yanına gitti. "Özür dilerim, Yumak, sana günaydın demedim," dedi Hayri. Sonra Hayri, Yumak'ın başını yavaşça okşadı. Yumak havladı ve kuyruğunu yine salladı. "Günaydın, Yumak, gel birlikte oturalım," dedi Hayri. Sonra Hayri ile Yumak ağacın altında mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "köpek onu selamladı ama o hiç bakmadı"
   - Cümle 0 (plan satırı): «köpek onu selamladı ama o hiç bakmadı | köpekten özür diledi ve köpeğin başını okşadı»
   - Açıklama: Plan satırında 'onu' ve 'o' zamirlerinin kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0049` birebir aynı, ardından `@onarim: 504284900ad6f9d04084c209cbed836c9ca2eb47`, sonra gövde.

### Hikâye 3: tohum hayri-0050 (deneme 2 -> 3)

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
@plan: rüzgar örtünün kenarlarını hep havaya kaldırdı | yardım istedi ve her köşeye bir taş koydu
@tohum: hayri-0050
@degisim: paspas -> örtü
Rüzgar ormanda hızlı hızlı esiyordu. Hayri kamp yerinde baklava yemek için yere büyük bir örtü yaymak istedi. Ama rüzgar örtünün kenarlarını hep havaya kaldırdı. Hayri onu tek başına tutamadı. "Basri Amca, bana yardım eder misin?" diye sordu Hayri. "Tabii, hemen geliyorum," dedi Basri Amca. Basri Amca iki köşeyi sıkıca tuttu. Hayri de dört köşeye birer büyük taş koydu. Artık rüzgar örtüyü hiç kaldıramadı. Hayri, çalıştığı dükkandan getirdiği baklava kutusunu çıkardı. Kutu örtünün tam ortasına kondu. Kutudaki tatlılar ikisine de yeterliydi. Basri Amca bir dilim yedi ve gülümsedi. Hayri çok sevindi, çünkü örtü artık yerinde duruyordu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dört köşeye birer büyük taş koydu"
   - Cümle 8: «Hayri de dört köşeye birer büyük taş koydu.»
   - Açıklama: Taşlar daha önce kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalıştığı dükkandan getirdiği baklava kutusunu çıkardı"
   - Cümle 10: «Hayri, çalıştığı dükkandan getirdiği baklava kutusunu çıkardı.»
   - Açıklama: Tohumdaki baklava özelliği iki kez geçiyor ve örtü sorununun çözümüne katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0050` birebir aynı, `@degisim: paspas -> örtü` (tutuyorsan), ardından `@onarim: b9f37793e829d339e56a3c844f93d052e0f077db`, sonra gövde.

### Hikâye 4: tohum hayri-0051 (deneme 2 -> 3)

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
@plan: patlak kovadan kozalaklar yere düştü | yağmurluğunu katlayıp kovanın dibine koydu
@tohum: hayri-0051
Bir sabah Hayri kamp yerinde çok acıkmıştı ve kahvaltıyı bekliyordu. Beklerken kozalakları bir kovaya atıp oynadı. Ama kova patlaktı ve kozalaklar delikten yere düştü. Bir kozalak otların arasına yuvarlandı. Hayri birkaç adımda ona yetişti. Sonra deliğe baktı ve biraz düşündü. Sarı yağmurluğunu çıkardı, katladı ve kovanın dibine koydu. Artık delik kapanmıştı. Hayri kozalağı yine kovaya attı. Bu kez kozalak yere düşmedi. Hayri sevinçle zıpladı ve bir tane daha attı. Hayri kahvaltıya kadar kozalak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri kamp yerinde çok acıkmıştı"
   - Cümle 1: «Bir sabah Hayri kamp yerinde çok acıkmıştı ve kahvaltıyı bekliyordu.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız açılışta geçiyor ve patlak kova sorununun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri kamp yerinde çok acıkmıştı ve kahvaltıyı bekliyordu"
   - Cümle 1: «Bir sabah Hayri kamp yerinde çok acıkmıştı ve kahvaltıyı bekliyordu.»
   - Açıklama: Açlık ve kahvaltı beklemek işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0051` birebir aynı, ardından `@onarim: edfe4b52bd1ccaba2044be99e87aef9aa745ba47`, sonra gövde.

### Hikâye 5: tohum hayri-0052 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0052
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'dondurma', fiil 'boşaltmak', sıfat 'tedbirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: yerde çantaya kadar pembe damlalar vardı | çantayı boşalttı ve eriyen dondurmayı buldu
@tohum: hayri-0052
Hayri ile Mert kamp yerinde ağaçların altında oturuyordu. Birden Hayri yerde küçük, pembe damlalar gördü. Damlalar sıra sıra dizilmişti ve çantanın yanında bitiyordu. İkisi de bunu çok merak etti. Tedbirli Mert, çantaya el sokmadan önce içini görmek istedi. Bu yüzden Hayri çantayı yavaşça yere boşalttı. İçinden ekmek, iki kaşık ve bir kutu çıktı. Kutunun kapağı açılmıştı ve çilekli dondurma eriyordu. Pembe damlalar ondan geliyordu! Hayri zaten çok acıkmıştı. Bir kaşığı Mert'e verdi ve kutuyu onunla paylaştı. Hayri ile Mert ağaçların altında dondurmayı mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerde küçük, pembe damlalar gördü"
   - Cümle 2: «Birden Hayri yerde küçük, pembe damlalar gördü.»
   - Açıklama: Sorun yalnız yerdeki pembe damlalar; çocuğun önemseyeceği gerçek bir sorun kurulmuyor, merak bitince hikaye yemekle kapanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden Hayri çantayı yavaşça yere boşalttı"
   - Cümle 6: «Bu yüzden Hayri çantayı yavaşça yere boşalttı.»
   - Açıklama: Çantayı Mert'in isteği yüzünden Hayri'nin boşaltması bir öncekinden mantıkla çıkmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri zaten çok acıkmıştı"
   - Cümle 10: «Hayri zaten çok acıkmıştı.»
   - Açıklama: Acıkma özelliği sorun çözüldükten sonra ekleniyor ve çözümde işe yaramıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir kaşığı Mert'e verdi ve kutuyu onunla paylaştı"
   - Cümle 11: «Bir kaşığı Mert'e verdi ve kutuyu onunla paylaştı.»
   - Açıklama: Kime ait olduğu belirtilmeyen çantadan çıkan açık, eriyen dondurma yeniyor; güvenli kullanım satırına göre tanımadığı kaynaktan yiyecek alınmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0052` birebir aynı, ardından `@onarim: 88e86dd3e015477bf8d38cf2969ccea6938216a9`, sonra gövde.

### Hikâye 6: tohum hayri-0053 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0053
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'plak', fiil 'birikmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: arkadaşı yiyeceğini evde unutmuştu | sandviçini ikiye böldü ve arkadaşıyla paylaştı
@tohum: hayri-0053
@degisim: plak -> kitap
Bir sabah Hayri kamp yerinde çok acıkmıştı. Çantasından büyük bir sandviç çıkardı ve bir ağacın altına oturdu. Yanındaki Kamil ise yiyeceğini evde unutmuştu. Kamil birikmiş yaprakların üstünde sessizce kitap okuyordu. Ama arada bir sandviçe bakıyordu. Hayri sandviçi ikiye böldü. "Al, Kamil, yarısı senin," dedi Hayri. "Teşekkür ederim, Hayri," dedi Kamil ve gülümsedi. Kamil sandviçini yerken kitaptan komik bir şey okudu. Hayri buna çok güldü. "Paylaşınca sandviç daha lezzetli oldu, Kamil!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kitaptan komik bir şey okudu"
   - Cümle 9: «Kamil sandviçini yerken kitaptan komik bir şey okudu.»
   - Açıklama: Kitaptan komik şey okuma olayı paylaşma sorunundan çıkmıyor ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0053` birebir aynı, `@degisim: plak -> kitap` (tutuyorsan), ardından `@onarim: 0a5a7d34887dfe6691173874d4a2301f18534526`, sonra gövde.

### Hikâye 7: tohum hayri-0054 (deneme 2 -> 3)

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
@plan: teknenin yelkeni yoktu ve tekne suda gitmedi | bezi açıp çubuğa takarak büyük bir yelken yaptı
@tohum: hayri-0054
@degisim: cesur -> büyük
Rüzgar deniz kıyısında hafif hafif esiyordu. Hayri kumda bulduğu tahtadan küçük bir tekne yaptı. Ama yelkeni olmadığı için tekne suda hiç gitmedi. Hayri cebinden bir bez çıkardı. Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi. Bezi iyice açtı ve bir çubuğa geçirdi. Çubuğu teknedeki bir deliğe taktı. Sonra tekneyi sığ suya bıraktı. Bez rüzgarla şişti ve tekne hızla yüzmeye başladı. Hayri kıyıda koşarak tekneyle yarıştı. Hayri çok mutluydu, çünkü kendi yaptığı tekne sonunda suda ilerliyordu.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri cebinden bir bez çıkardı"
   - Cümle 4: «Hayri cebinden bir bez çıkardı.»
   - Açıklama: Yelken olacak bez önceden kurulmadan cepte hazır beliriyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Bez sebepsizce cepten çıkıyor ve çözümü hazır getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tekneye büyük bir yelken istedi"
   - Cümle 5: «Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi.»
   - Açıklama: Kimden istediği belli değil; 'istedi' fiili burada yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartmayı severdi"
   - Cümle 5: «Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kavram.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bu yüzden tekneye büyük bir yelken istedi"
   - Cümle 5: «Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi.»
   - Açıklama: Kartın özellikler alanında abartma olayları abartmaktır; burada büyük yelken istemenin gerekçesi olarak karttaki gibi kullanılmıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi"
   - Cümle 5: «Hayri abartmayı severdi, bu yüzden tekneye büyük bir yelken istedi.»
   - Açıklama: Karttaki özellik olayları abartmaktır; büyük yelken istemek bu özelliğin karttaki gibi kullanımı değildir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0054` birebir aynı, `@degisim: cesur -> büyük` (tutuyorsan), ardından `@onarim: 1751f6553d846b2379ba590de2d60a623de095f4`, sonra gövde.

### Hikâye 8: tohum hayri-0055 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0055
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'gümüş', fiil 'çözmek', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar uçurtmayı çok döndürdü ve ip düğüm oldu | ipin ucunu buldu ve düğümü yavaşça çözdü
@tohum: hayri-0055
Deniz kıyısında Hayri değişik, gümüş renkli bir uçurtma uçuruyordu. Acıkınca ipi çantasına bağladı ve sandviçini yemeye oturdu. Ama rüzgar uçurtmayı çok döndürdü ve ip büyük bir düğüm oldu. Uçurtma yavaşça kuma indi. Hayri sandviçini bıraktı ve düğüme dikkatle baktı. İpin bir ucunu buldu ve düğümü yavaş yavaş çözdü. Sonra ipi sıkıca tuttu ve koşmaya başladı. Uçurtma yine gökyüzüne yükseldi ve güneşte parladı. Hayri bir eliyle ipi tuttu, öbür eliyle sandviçini bitirdi. Hayri uçurtmasını uçurmaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Acıkınca ipi çantasına bağladı ve sandviçini yemeye oturdu"
   - Cümle 2: «Acıkınca ipi çantasına bağladı ve sandviçini yemeye oturdu.»
   - Açıklama: Acıkma özelliği güvenli kullanım satırındaki paylaşma, bekleme ya da hazırlama biçiminde değil ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0055` birebir aynı, ardından `@onarim: 54b0c1bdecf5d814581ed9218ecebcd6dba91a89`, sonra gövde.

### Hikâye 9: tohum hayri-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0056
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kakao', fiil 'kapatmak', sıfat 'zarif'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: iki çocuk da tek dürbünü kullanmak istedi | sırayla bakmayı önerdi ve dürbünü arkadaşına verdi
@tohum: hayri-0056
@degisim: zarif -> güzel
Bir sabah Hayri ile Kamil kamp yerinde oturuyordu. Kamil'in elinde küçük bir dürbün vardı. İkisi de onunla kuşları görmek istedi, ama tek dürbün vardı. "Kamil, sırayla bakalım mı?" diye sordu Hayri. "Olur, ilk sıra senin," dedi Kamil. Hayri dürbünü aldı ve dallara uzun uzun baktı. Dalda güzel, beyaz kuşlar oturuyordu. Sonra dürbünü Kamil'e verdi. Hayri sırasını beklerken acıktı ve çantasından kakao şişesini çıkardı. İki bardağa soğuk kakao doldurdu ve şişeyi kapattı. Kamil dürbünü geri verince kakaosunu aldı ve teşekkür etti. Hayri çok mutluydu, çünkü sırayla kullanınca ikisi de kuşları görmüştü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasından kakao şişesini çıkardı"
   - Cümle 9: «Hayri sırasını beklerken acıktı ve çantasından kakao şişesini çıkardı.»
   - Açıklama: Kakao olayı dürbün sorunundan çıkmıyor ve çözüme hiçbir katkı yapmayan eklenmiş bir ayrıntı.
   - Açıklama: Kakao bölümü dürbün sorunuyla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0056` birebir aynı, `@degisim: zarif -> güzel` (tutuyorsan), ardından `@onarim: 309b7d01e1c1a024291bc5d886a3cf406246d031`, sonra gövde.

### Hikâye 10: tohum hayri-0057 (deneme 1 -> 2)

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
Hayri ile Akın parkta saklambaç oynuyordu. Ama Hayri sayarken gizlice gözlerini açtı. Akın bunu gördü ve çok üzüldü. "Hayri, sen bana baktın, bu olmaz!" dedi Akın. Hayri yanlış yaptığını anladı. "Haklısın, Akın. Özür dilerim," dedi Hayri. Hayri, çalıştığı baklava dükkanından yuvarlak bir kutu baklava getirmişti. Kutuyu açtı ve Akın'a en büyük dilimi verdi. Sonra gözlerini sıkıca kapadı ve ona kadar saydı. Akın çimlerin üstünden koştu ve büyük ağacın arkasına gizlendi. Hayri parkı dolaştı ve sonunda Akın'ı buldu. İkisi birlikte güldü. "Çok güzel oynadık, Hayri, şimdi sıra sende!" dedi Akın.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalıştığı baklava dükkanından yuvarlak bir kutu baklava getirmişti"
   - Cümle 8: «Hayri, çalıştığı baklava dükkanından yuvarlak bir kutu baklava getirmişti.»
   - Açıklama: Tohumdaki baklava özelliği sorunun çözümüne (özür ve yeniden sayma) katkı vermeyen süs olarak geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı baklava dükkanından yuvarlak bir kutu baklava getirmişti"
   - Cümle 8: «Hayri, çalıştığı baklava dükkanından yuvarlak bir kutu baklava getirmişti.»
   - Açıklama: Baklava kutusu sebepsiz beliriyor ve saklambaç sorununun çözümüne hiçbir katkısı yok.
   - Açıklama: Baklava kutusu sebepsiz beliriyor ve sorunun çözümüne hiçbir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0057` birebir aynı, ardından `@onarim: d8433824b00e9cc87461963bb98130139800b9a6`, sonra gövde.

### Hikâye 11: tohum hayri-0059 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0059
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'limonata', fiil 'temizlemek', sıfat 'yırtık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: rüzgarla güzel bir limon kokusu geldi | kokunun peşinden gidip limonatayı buldu
@tohum: hayri-0059
Hayri deniz kıyısında kumda yürüyordu ve çok acıkmıştı. Birden rüzgarla güzel bir limon kokusu geldi. Hayri bu kokunun nereden geldiğini çok merak etti. Hayri kayalara doğru yürüdü. Kayaların yanında Basri Amca'yı gördü. Basri Amca yırtık bir bezle bardakları temizliyordu. Yanında büyük bir sürahi limonata vardı. "Bu güzel koku limonatadan mı geliyor?" diye sordu Hayri. "Evet, Hayri, limonları az önce sıktım," dedi Basri Amca. Sonra bir bardak limonata doldurdu ve Hayri'ye verdi. Hayri limonatayı içti ve Basri Amca'nın yanına oturdu. Hayri çok sevindi, çünkü güzel kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarla güzel bir limon kokusu geldi"
   - Cümle 2: «Birden rüzgarla güzel bir limon kokusu geldi.»
   - Açıklama: Güzel bir koku gelmesi çözülmesi gereken bir sorun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgarla güzel bir limon kokusu geldi"
   - Cümle 2: «Birden rüzgarla güzel bir limon kokusu geldi.»
   - Açıklama: Güzel bir koku gelmesi bir sorun değil; hikayede çözülecek gerçek bir sorun yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yırtık bir bezle bardakları temizliyordu"
   - Cümle 6: «Basri Amca yırtık bir bezle bardakları temizliyordu.»
   - Açıklama: Yırtık bez ayrıntısı kuruluyor ama hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yırtık bir bezle bardakları"
   - Cümle 6: «Basri Amca yırtık bir bezle bardakları temizliyordu.»
   - Açıklama: Yırtık bez ve bardak temizleme ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0059` birebir aynı, ardından `@onarim: 50540ede582b99a2637433311dbe8418c69199b6`, sonra gövde.

### Hikâye 12: tohum hayri-0060 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0060
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'toz', fiil 'aşmak', sıfat 'mutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: kum toz gibi kuruydu ve kumdan baklava dağılıyordu | kovayla su getirip kumu ıslattı
@tohum: hayri-0060
@degisim: aşmak -> ıslatmak
Hafif bir rüzgar esiyordu. Hayri kıyıda Yumak ile dükkan oyunu oynuyordu. Kumdan baklava yapmak istiyordu ama kum toz gibi kuruydu. Kum hemen dağılıyordu. Yumak kumu kokladı ve havladı. "Yumak, bu kum çok kuru," dedi Hayri. Hayri kovasını aldı ve su kenarından biraz su doldurdu. Sonra kumu suyla ıslattı ve iyice bastırdı. Bu kez kum çok güzel oldu. Hayri kumu bir tepsi gibi düz yaptı. Çalıştığı baklava dükkanında gördüğü gibi kumu küçük dilimlere kesti. Yumak kuyruğunu salladı ve baklavaların etrafında koştu. "Yumak, baklavalarımız hazır, çok mutluyum!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "su kenarından biraz su doldurdu"
   - Cümle 7: «Hayri kovasını aldı ve su kenarından biraz su doldurdu.»
   - Açıklama: Aynı cümlede 'su' gereksiz tekrarlanıyor ve 'doldurdu' nesnesiz kalıyor; 'kovaya su doldurdu' daha doğru.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0060` birebir aynı, `@degisim: aşmak -> ıslatmak` (tutuyorsan), ardından `@onarim: 317ba55be251ecac6a124bb36b253d4501802db6`, sonra gövde.
