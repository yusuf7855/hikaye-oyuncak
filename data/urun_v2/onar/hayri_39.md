# Editör görevi (onarım): Hayri, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0109 (deneme 2 -> 3)

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
Bir sabah Hayri kamp yerinde ilk kez bloklarla kule yapmayı denedi. Tahta blokları bir kütüğün üstüne üst üste dizdi. Ama en altta yalnız bir blok vardı ve kule sallanıp yıkıldı. Hayri yere düşen bloklara baktı ve biraz düşündü. Sonra blokların hepsini yerden aldı. Hayri yıkılan kuleyi biraz abarttı. Bu yüzden en alta yan yana tam altı blok koydu. Üstüne blokları tek tek dikkatle yerleştirdi. En üste de kıpkırmızı bir blok koydu. Kule bu kez hiç sallanmadı ve dimdik durdu. Hayri bundan sonra kulenin en altına hep çok blok koydu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yıkılan kuleyi biraz abarttı"
   - Cümle 6: «Hayri yıkılan kuleyi biraz abarttı.»
   - Açıklama: 'Abartmak' burada anlamsız ve yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri yıkılan kuleyi biraz abarttı"
   - Cümle 6: «Hayri yıkılan kuleyi biraz abarttı.»
   - Açıklama: 'Abartmak' fiili burada yanlış anlamda kullanılmış; cümle anlamsız.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yıkılan kuleyi biraz abarttı"
   - Cümle 6: «Hayri yıkılan kuleyi biraz abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yıkılan kuleyi biraz abarttı"
   - Cümle 6: «Hayri yıkılan kuleyi biraz abarttı.»
   - Açıklama: Kartın özellikler alanındaki abartma olayları anlatırken abartmaktır; burada anlamı kaydırılıp çözüme zorla bağlanıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri yıkılan kuleyi biraz abarttı"
   - Cümle 6: «Hayri yıkılan kuleyi biraz abarttı.»
   - Açıklama: Kuleyi abartmak anlamsız bir olay ve çözüme 'bu yüzden' diye bağlanması sebep-sonuç zincirini bozuyor.
   - Açıklama: Yıkılan kuleyi abartmak anlamsız bir olay ve çözüm bu sebepsiz cümleden çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0109` birebir aynı, ardından `@onarim: a35be95a3b64dc069952d549333757de81223bb3`, sonra gövde.

### Hikâye 2: tohum hayri-0110 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0110
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'madalya', fiil 'şakalaşmak', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: arkadaşı yarışı kaybettiği için çok üzüldü | çadırını çok övdü ve madalyayı ona verdi
@tohum: hayri-0110
Bir sabah Hayri ile Mert kamp yerinde koşu yarışı yaptı. Ödül, dala asılı ışıltılı bir oyuncak madalyaydı. Hayri kazandı, Mert ise kaybettiği için çok üzüldü. Hayri arkadaşını sevindirmek istedi. Mert'in sabah kurduğu çadıra baktı. Dimdik ve düzgün duruyordu. Hayri biraz abarttı ve çadırın dünyanın en güzeli olduğunu söyledi. Mert buna çok güldü. Hayri madalyayı daldan alıp Mert'in boynuna taktı. İki arkadaş bir kütüğe oturup uzun uzun şakalaştı. Hayri çok mutluydu, çünkü Mert yine gülüyordu.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çadırını çok övdü"
   - Cümle 0 (plan satırı): «arkadaşı yarışı kaybettiği için çok üzüldü | çadırını çok övdü ve madalyayı ona verdi»
   - Açıklama: Plan satırında 'çadırını' zamirinin kimin çadırını gösterdiği belli değil; özne Hayri olduğu için onun çadırı gibi okunuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dimdik ve düzgün duruyordu"
   - Cümle 6: «Dimdik ve düzgün duruyordu.»
   - Açıklama: Öznesiz cümlede dimdik duranın çadır mı Hayri mi olduğu belli değil; son özne Hayri.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı ve çadırın dünyanın en güzeli"
   - Cümle 7: «Hayri biraz abarttı ve çadırın dünyanın en güzeli olduğunu söyledi.»
   - Açıklama: 'Abarttı' ve 'dünyanın en güzeli' soyut/abartılı anlatım, küçük çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 7: «Hayri biraz abarttı ve çadırın dünyanın en güzeli olduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "çadırın dünyanın en güzeli olduğunu söyledi"
   - Cümle 7: «Hayri biraz abarttı ve çadırın dünyanın en güzeli olduğunu söyledi.»
   - Açıklama: Mert yarışı kaybettiği için üzgün; çadırı övmek bu sebebe yönelmiyor ve çözüme gereksiz bir adım ekliyor.
   - Açıklama: Sorunun sebebi yarışı kaybetmek ama çadırı övmek bu sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0110` birebir aynı, ardından `@onarim: 35f8a55353bd9c627372158ebc92db7420c3b61c`, sonra gövde.

### Hikâye 3: tohum hayri-0111 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0111
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'palmiye', fiil 'kullanmak', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kozalaklar bozuk çantadan hep yere düştü | boş tepsiyi kullanıp kozalakları taşıdı
@tohum: hayri-0111
@degisim: palmiye -> kozalak
Bir sabah Hayri kahvaltıdan kalan boş tepsiyi çadırının önüne koydu. Sonra çam ağaçlarının altında büyük kozalaklar gördü. Onlarla çadırın kapısını süslemek istedi ama çantasının fermuarı bozuktu. Topladığı kozalaklar çantadan hep yere düşüyordu. Hayri biraz düşündü ve tepsiyi kullanmaya karar verdi. Onu çadırdan getirdi ve kozalakları tek tek üstüne dizdi. Çalıştığı baklava dükkanında her gün tepsi taşıyordu. Bu yüzden tepsiyi hiç sallamadan çadırına götürdü. Yolda hiçbiri kaymadı. Sonra hepsini kapının iki yanına sıra sıra koydu. Böylece çadırı çok güzel oldu ve Hayri mutlu mutlu gülümsedi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Onu çadırdan getirdi"
   - Cümle 6: «Onu çadırdan getirdi ve kozalakları tek tek üstüne dizdi.»
   - Açıklama: Tepsi ilk cümlede çadırın önüne konmuşken burada çadırın içinden getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0111` birebir aynı, `@degisim: palmiye -> kozalak` (tutuyorsan), ardından `@onarim: aaa292a471b32c6819ee8f0e2d457939ed21ea08`, sonra gövde.

### Hikâye 4: tohum hayri-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0112
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'salıncak', fiil 'akmak', sıfat 'kremalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: koşarken arkadaşının kumdan kalesini yıktı | özür dileyip kaleyi onunla yeniden yaptı
@tohum: hayri-0112
@degisim: salıncak -> kova
Hayri, elinde bir kutuyla Akın'a doğru koşuyordu. Kutuda çalıştığı dükkandan getirdiği kremalı baklavalar vardı. Hayri koşarken Akın'ın kumdan kalesini görmedi ve ayağıyla yıktı. Akın kalesine bakıp çok üzüldü. Hayri hemen durdu ve yanına oturdu. "Özür dilerim, Akın, kaleni görmedim," dedi Hayri. Sonra Akın'ın kovasıyla deniz suyu getirdi. Su kuma aktı ve kumu ıslattı. İkisi ıslak kumdan kaleyi birlikte yeniden yaptı. Bu kez eskisinden de büyük oldu. "Çok güzel oldu, Hayri!" dedi Akın. Sonra kutuyu açtılar ve baklavaları birlikte yediler. Hayri çok sevindi, çünkü Akın yine gülüyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "baklavaları birlikte yediler"
   - Cümle 12: «Sonra kutuyu açtılar ve baklavaları birlikte yediler.»
   - Açıklama: Tohumdaki özellik (baklava dükkanında çalışma) çözüme katkı vermiyor, yalnız süs olarak sonda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0112` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 02d45c1c35369fa00fe3fd5044fb3d346f675d5e`, sonra gövde.

### Hikâye 5: tohum hayri-0113 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0113
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çekmece', fiil 'yayılmak', sıfat 'yepyeni'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: ikisi ipi aynı anda çekince uçurtma düştü | uçurtmayı sırayla uçurmayı önerdi
@tohum: hayri-0113
@degisim: çekmece -> uçurtma
Deniz kıyısında Hayri'nin elinde, çalıştığı dükkandan getirdiği bir kutu baklava vardı. Basri Amca yepyeni uçurtmasını uçuruyordu. Hayri de ipe uzandı ama ikisi aynı anda çekince uçurtma kuma düştü. Basri Amca biraz kızdı ve yere yayılan ipi topladı. "Amca, sırayla oynayalım, önce sen uçur!" dedi Hayri. Basri Amca güldü ve uçurtmayı yeniden gökyüzüne yükseltti. Hayri bu sırada oturdu ve kutuyu açtı. Biraz sonra Basri Amca ipi Hayri'ye uzattı. "Sıra sende, Hayri," dedi Basri Amca. Hayri de baklavaların yarısını amcaya verdi. Hayri uçurtmayı uçurdu, Basri Amca da baklavasını afiyetle yedi. İkisi böyle sırayla oynayıp kumsalda çok eğlendi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı dükkandan getirdiği bir kutu baklava"
   - Cümle 1: «Deniz kıyısında Hayri'nin elinde, çalıştığı dükkandan getirdiği bir kutu baklava vardı.»
   - Açıklama: Baklava kutusu uçurtma sorunuyla ilgisiz bir yan olay olarak kuruluyor ve olay zincirinden çıkmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "baklavaların yarısını amcaya verdi"
   - Cümle 10: «Hayri de baklavaların yarısını amcaya verdi.»
   - Açıklama: Tohumdaki baklava özelliği uçurtma sorununun çözümünde işe yaramıyor, yalnız yan süs olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri de baklavaların yarısını amcaya verdi"
   - Cümle 10: «Hayri de baklavaların yarısını amcaya verdi.»
   - Açıklama: Baklava kutusu uçurtma sorunuyla ilgisiz, olaylardan çıkmayan bir yan iplik olarak kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0113` birebir aynı, `@degisim: çekmece -> uçurtma` (tutuyorsan), ardından `@onarim: 04c8ed5091a50455ce758fa8304ed0fe3af05530`, sonra gövde.

### Hikâye 6: tohum hayri-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0114
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bornoz', fiil 'sergilemek', sıfat 'boş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: arkadaşının kalemi kırıldı ve kağıdı boş kaldı | kalemlerinin yarısını ona verdi
@tohum: hayri-0114
@degisim: bornoz -> kalem
Bir öğle vakti Hayri ile Kamil, evin önündeki bahçede resim yapıyordu. Resimlerini çitin üstüne koyup sergilemek istiyorlardı. Ama Kamil'in tek kalemi yere düşüp kırıldı ve kağıdı boş kaldı. Hayri'nin kutusunda bir sürü renkli kalem vardı. Hayri bunların yarısını Kamil'e uzattı. Kamil, Hayri'ye kalem kalmayacak diye almak istemedi. Hayri biraz abarttı ve kutuda bin tane kalem olduğunu söyledi. Kamil buna çok güldü ve onları aldı. İkisi birlikte oturdu. Kamil kocaman bir kitap, Hayri de bir tabak köfte çizdi. Sonra iki kağıdı çite yan yana astılar. Hayri bundan sonra kalemlerini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "evin önündeki bahçede resim yapıyordu"
   - Cümle 1: «Bir öğle vakti Hayri ile Kamil, evin önündeki bahçede resim yapıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye evin dışındaki bahçede geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "koyup sergilemek istiyorlardı"
   - Cümle 2: «Resimlerini çitin üstüne koyup sergilemek istiyorlardı.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuk için ağır bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 7: «Hayri biraz abarttı ve kutuda bin tane kalem olduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0114` birebir aynı, `@degisim: bornoz -> kalem` (tutuyorsan), ardından `@onarim: dbdf40c7af4a593ea760b68e03034731395d344e`, sonra gövde.

### Hikâye 7: tohum hayri-0115 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0115
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'buğday', fiil 'karşılamak', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpeğin topu iki taşın arasına sıkıştı | uzun bir dalla topu itip çıkardı
@tohum: hayri-0115
@degisim: buğday -> top
Deniz kıyısında Yumak, Hayri'yi havlayarak karşıladı. Ama Yumak'ın topu iki büyük taşın arasına sıkışmıştı. Yumak burnuyla topu itti ama çıkaramadı. Hayri'nin eli de taşların arasına sığmadı. Sonra Hayri kumda uzun bir dal buldu. Dalı taşların arasına soktu ve topu yavaşça itti. Top taşların arasından çıktı ve kuma düştü. Yumak kabarık kuyruğunu sallayarak topa koştu. Hayri sevinçle biraz abarttı. "Yumak, sen dünyanın en mutlu köpeğisin!" dedi Hayri. Yumak havladı ve topu Hayri'ye getirdi. Hayri bundan sonra Yumak'la taşlardan uzakta top oynadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "topu iki büyük taşın arasına sıkışmıştı"
   - Cümle 2: «Ama Yumak'ın topu iki büyük taşın arasına sıkışmıştı.»
   - Açıklama: Topun taşların arasına nasıl sıkıştığı, yani sorunun sebebi söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri sevinçle biraz abarttı"
   - Cümle 9: «Hayri sevinçle biraz abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri sevinçle biraz abarttı"
   - Cümle 9: «Hayri sevinçle biraz abarttı.»
   - Açıklama: Tohumdaki abartma özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak ekleniyor.
   - Açıklama: Tohumdaki abartma özelliği sorun çözüldükten sonra süs olarak ekleniyor ve çözüme bir işe yaramıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dünyanın en mutlu köpeğisin"
   - Cümle 10: «"Yumak, sen dünyanın en mutlu köpeğisin!" dedi Hayri.»
   - Açıklama: Abartılı mecazlı söz küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0115` birebir aynı, `@degisim: buğday -> top` (tutuyorsan), ardından `@onarim: d33820d596bab21ed5bbec3e3978d20eacc304fc`, sonra gövde.

### Hikâye 8: tohum hayri-0116 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0116
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'buzdolabı', fiil 'yükselmek', sıfat 'farklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: rüzgar yoktu ve tohumlar çiçekten uçmadı | derin bir nefes alıp güçlü üfledi
@tohum: hayri-0116
@degisim: buzdolabı -> tohum
Bir sabah Hayri parkta yürürken çimenlerde farklı bir çiçek fark etti. Hayri çiçeğin beyaz, tüylü tohumlarını havaya uçurmak istedi. Ama hiç rüzgar yoktu ve tohumlar yerinden kıpırdamadı. Hayri çiçeğe yavaşça üfledi. Yalnız bir tanesi uçtu ve hemen yere indi. Bu kez Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı. Yanaklarını şişirdi ve derin bir nefes aldı. Sonra bütün gücüyle üfledi. Tohumların hepsi birden havaya yükseldi. Hepsi yavaş yavaş gökyüzüne doğru uçtu. Hayri bundan sonra rüzgar yokken tohumlara hep güçlü üfledi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı"
   - Cümle 6: «Bu kez Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı.»
   - Açıklama: 'Abarttı' soyut bir kelime ve kendini rüzgar sanmak küçük çocuğa uygun olmayan bir mecaz.
   - Açıklama: 'Abarttı' soyut bir kelime ve 'kendini rüzgar sandı' mecaz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı"
   - Cümle 6: «Bu kez Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı.»
   - Açıklama: Karttaki özellik olayları abartmak iken burada abartma güçlü üflemeye dönüştürülmüş, özellik kartın 'ozellikler' alanındaki gibi kullanılmamış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı"
   - Cümle 6: «Bu kez Hayri biraz abarttı ve kendini kocaman bir rüzgar sandı.»
   - Açıklama: Kartın 'olayları abartmayı sever' özelliği burada güçlü üflemek anlamına kaydırılmış.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri bundan sonra rüzgar yokken tohumlara hep güçlü üfledi"
   - Cümle 11: «Hayri bundan sonra rüzgar yokken tohumlara hep güçlü üfledi.»
   - Açıklama: Son cümle olaya bağlı bir his ya da sıcak bir kapanış vermeyen çıplak bir alışkanlık cümlesi.
   - Açıklama: Son cümle sıcak bir his ya da olaydan çıkan bir ders değil, çıplak bir alışkanlık cümlesi; çözüm anında da hiçbir sevinç verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0116` birebir aynı, `@degisim: buzdolabı -> tohum` (tutuyorsan), ardından `@onarim: 787a476449ef44d0a7bdaa4565266ffbcbc68899`, sonra gövde.

### Hikâye 9: tohum hayri-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0118
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'sos', fiil 'sürtmek', sıfat 'minik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: cevizlerin kabukları çok sertti | iki cevizi birbirine sürttü ve sıktı
@tohum: hayri-0118
@degisim: sos -> ceviz
Bir sabah Hayri parkta oynarken çok acıktı. Büyük bir ağacın altında yere düşmüş cevizleri fark etti. Ama kabuklar çok sertti ve Hayri onları elleriyle açamadı. Hayri biraz düşündü ve iki cevizi avucuna aldı. Onları birbirine sürttü ve sıkıca bastırdı. Çıt diye bir ses geldi ve bir tanesi kırıldı. İçinden minik, beyaz bir ceviz içi çıktı. Hayri onu yıkamadan yemek istemedi ve cebine koydu. Sonra kalan cevizleri de böyle kırdı. Hayri çok sevindi, çünkü sert kabuğu kendisi açmıştı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yere düşmüş cevizleri fark etti"
   - Cümle 2: «Büyük bir ağacın altında yere düşmüş cevizleri fark etti.»
   - Açıklama: Parkta yerden bulunan yiyeceği yemek için toplamak çocuğun taklit edebileceği riskli bir davranış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri onu yıkamadan yemek istemedi ve cebine koydu"
   - Cümle 8: «Hayri onu yıkamadan yemek istemedi ve cebine koydu.»
   - Açıklama: Yıkama ayrıntısı hiçbir yere bağlanmıyor ve açlık hedefini sebepsizce kesiyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri onu yıkamadan yemek istemedi ve cebine koydu"
   - Cümle 8: «Hayri onu yıkamadan yemek istemedi ve cebine koydu.»
   - Açıklama: Hikaye çok acıkan Hayri ile başlıyor ama Hayri hiçbir cevizi yemiyor, açlık hedefine ulaşılmıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "yıkamadan yemek istemedi ve cebine koydu"
   - Cümle 8: «Hayri onu yıkamadan yemek istemedi ve cebine koydu.»
   - Açıklama: Hayri acıktığı için ceviz kırıyor ama hiç yemiyor; açlık hedefine ulaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0118` birebir aynı, `@degisim: sos -> ceviz` (tutuyorsan), ardından `@onarim: 74a619dfcc77a3dee57d3efa8e51fed77da37463`, sonra gövde.

### Hikâye 10: tohum hayri-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0119
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'sosis', fiil 'serinletmek', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar siyah şapkayı kıyıda bir yere uçurdu | şapkanın üstündeki beyaz una bakıp onu buldu
@tohum: hayri-0119
Denizden serin bir rüzgar esiyordu. Hayri kumda sosisli ekmeğini yerken başını serinletmek istedi. Siyah şapkasını çıkarıp kuma koydu ama rüzgar onu uzağa uçurdu. Hayri bu şapkayı baklava dükkanında çalışırken takıyordu. Ekmeğini bırakıp hemen aramaya başladı. Kıyıda bir sürü siyah taş ve yosun vardı. Hayri her birine tek tek baktı ama şapkayı göremedi. Sonra şapkanın üstündeki beyaz un lekelerini hatırladı. Bu kez yalnız beyaz lekeli bir şey aradı. Büyük bir taşın arkasında onu hemen gördü. Hayri şapkayı silkeledi ve yeniden taktı. Sonra ekmeğini afiyetle bitirdi. Hayri çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "serin bir rüzgar esiyordu"
   - Cümle 1: «Denizden serin bir rüzgar esiyordu.»
   - Açıklama: Rüzgar serinken Hayri'nin başını serinletmek istemesi çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0119` birebir aynı, ardından `@onarim: f965c2a6cfda5a968cf3acbf1d32cd6a199c0263`, sonra gövde.

### Hikâye 11: tohum hayri-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0120
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hediye', fiil 'giydirmek', sıfat 'zor'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: arkadaşının doğum günüydü ama hediye yoktu | kekini yemedi ve ona hediye etti
@tohum: hayri-0120
@degisim: giydirmek -> süslemek
Hayri, Akın'la kumda deniz kabuğu topluyordu. "Bugün benim doğum günüm!" dedi Akın. Hayri bu günü kutlamak istedi. Ama kumsalda ona bir hediye bulmak çok zordu. Hayri çok acıkmıştı ve çantasında en sevdiği çilekli kek vardı. Onu yemedi. "Gözlerini kapa, Akın," dedi Hayri. Keki düz bir taşın üstüne koydu. Çevresini topladıkları kabuklarla süsledi. "Gözlerini aç, Akın, bu senin hediyen!" dedi Hayri. Akın süslü keki görünce sevinçle zıpladı. Sonra onu ikiye böldü ve yarısını Hayri'ye verdi. "İyi ki doğdun, Akın!" dedi Hayri. Hayri bundan sonra en sevdiği yiyecekleri Akın'la hep paylaştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kumsalda ona bir hediye bulmak çok zordu"
   - Cümle 4: «Ama kumsalda ona bir hediye bulmak çok zordu.»
   - Açıklama: Hediye yokluğu sorunu ancak 4. cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0120` birebir aynı, `@degisim: giydirmek -> süslemek` (tutuyorsan), ardından `@onarim: ae715bcb51cdd0ceb440727fb204fd833d180b40`, sonra gövde.

### Hikâye 12: tohum hayri-0121 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0121
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'torba', fiil 'sulamak', sıfat 'yaratıcı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: arkadaşına kutlama pastası vermek istedi ama pasta yoktu | ıslak kumdan bir pasta yaptı
@tohum: hayri-0121
@degisim: yaratıcı -> güzel
Güneş parlıyordu ve kıyıya küçük dalgalar geliyordu. Hayri, Mert'in kumda bitirdiği kocaman kaleye bakıyordu. Mert'e bir kutlama pastası vermek istedi ama kıyıda pasta yoktu. Hayri çok acıkmıştı ama torbasındaki iki kurabiyeyi yemedi. Hayri, Mert'ten arkasını dönmesini istedi. Kumu elleriyle suladı ve ıslak kumdan yuvarlak bir pasta yaptı. "Dönebilirsin, Mert, bu senin için!" dedi Hayri. Mert sürprizi görünce çok güldü. Hayri kurabiyelerden birini ona verdi. "Bu gördüğüm en güzel pasta, Hayri, teşekkür ederim!" dedi Mert.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ama torbasındaki"
   - Cümle 4: «Hayri çok acıkmıştı ama torbasındaki iki kurabiyeyi yemedi.»
   - Açıklama: Hayri'nin açlığı kuruluyor ama olayda bir işe yaramıyor ve sonuçlanmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ama torbasındaki iki kurabiyeyi yemedi"
   - Cümle 4: «Hayri çok acıkmıştı ama torbasındaki iki kurabiyeyi yemedi.»
   - Açıklama: Hayri'nin açlığı kuruluyor ama hiç giderilmiyor, sarkan bir ayrıntı olarak kalıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kumu elleriyle suladı"
   - Cümle 6: «Kumu elleriyle suladı ve ıslak kumdan yuvarlak bir pasta yaptı.»
   - Açıklama: Kum sulanmaz ve elle sulama olmaz; 'kumu ıslattı' olmalı.
   - Açıklama: 'Sulamak' elle yapılmaz ve kum için uygun değil; 'ıslattı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0121` birebir aynı, `@degisim: yaratıcı -> güzel` (tutuyorsan), ardından `@onarim: 2f647e5f80439d085d38ccc6a94dded37dc0fddd`, sonra gövde.
