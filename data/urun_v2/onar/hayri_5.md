# Editör görevi (onarım): Hayri, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0007 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0007
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'patlıcan', fiil 'doyurmak', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: plastik patlıcan düştü ve çimlerde kayboldu | eğilip çimlerin arasına baktı ve patlıcanı buldu
@tohum: hayri-0007
Bir sabah Hayri ile Mert bahçede lokanta oyunu oynuyordu. Hayri, Mert'i doyurmak için tabağa plastik bir patlıcan koydu. Ama Mert tabağı alırken patlıcan düştü ve uzun çimlerde kayboldu. Mert çok üzüldü. Hayri olayı abarttı ve büyük bir kaza olmuş gibi yere yattı. Mert bunu görünce çok güldü. Sonra Hayri eğildi ve çimlerin arasına dikkatle baktı. Kokulu nane yapraklarının altında mor bir şey gördü. Kaybolan plastik patlıcan orada duruyordu. Hayri onu çıkardı ve yeniden tabağa bıraktı. Mert bu kez tabağı iki eliyle sıkıca tuttu. İkisi de çok sevindi, çünkü lokanta oyunları yeniden başlamıştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bahçede lokanta oyunu oynuyordu"
   - Cümle 1: «Bir sabah Hayri ile Mert bahçede lokanta oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri olayı abarttı"
   - Cümle 5: «Hayri olayı abarttı ve büyük bir kaza olmuş gibi yere yattı.»
   - Açıklama: 'Olayı abarttı' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri olayı abarttı ve büyük bir kaza olmuş gibi yere yattı"
   - Cümle 5: «Hayri olayı abarttı ve büyük bir kaza olmuş gibi yere yattı.»
   - Açıklama: Abartma sahnesi sorunun çözümüne hiçbir katkı yapmayan işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0007` birebir aynı, ardından `@onarim: dd13464c6ce294023d99a08713d9364951edc88c`, sonra gövde.

### Hikâye 2: tohum hayri-0008 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0008
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'çömlek', fiil 'bırakmak', sıfat 'minicik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpeğin ayağı iki taşın arasında kaldı | çömleği bırakıp ayağın altındaki kumu kazdı
@tohum: hayri-0008
Deniz kıyısında Hayri çok acıkmıştı ve köfte dolu çömleği açacaktı. Tam o sırada yakından Yumak'ın havladığını duydu. Kumda koşan Yumak'ın ayağı iki taşın arasındaki minicik boşlukta kalmıştı. Yumak ayağını çekti ama çıkaramadı. Hayri yemeden önce çömleği kuma bıraktı ve Yumak'a koştu. "Bekle, Yumak, sana yardım edeceğim," dedi Hayri. Hayri, Yumak'ın ayağının altındaki kumu elleriyle kazdı. Yumak ayağını yukarı çekti ve kolayca çıkardı. Yumak sevinçle kuyruğunu salladı ve Hayri'nin yanına oturdu. Sonra Hayri çömleği açtı ve köftelerini yedi. "İyi ki ayağın kurtuldu, Yumak!" dedi Hayri gülerek.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "köfte dolu çömleği açacaktı"
   - Cümle 1: «Deniz kıyısında Hayri çok acıkmıştı ve köfte dolu çömleği açacaktı.»
   - Açıklama: 'Çömlek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Kumda koşan Yumak'ın ayağı iki taşın arasındaki minicik boşlukta kalmıştı"
   - Cümle 3: «Kumda koşan Yumak'ın ayağı iki taşın arasındaki minicik boşlukta kalmıştı.»
   - Açıklama: Köpeğin ayağının taşlar arasında sıkışması yaralanma ya da acı çağrıştırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0008` birebir aynı, ardından `@onarim: c98f3f50e9396f887bdb24e122eaf352cccf52be`, sonra gövde.

### Hikâye 3: tohum hayri-0010 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0010
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kravat', fiil 'kopmak', sıfat 'uyanık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: ikisi de kravatı takmak isteyip çekti | kravatı sırayla takmayı önerdi
@tohum: hayri-0010
Ormanda, kamp yerinde Hayri ile Kamil dükkan oyunu oynuyordu. Kamil bu sabah çok uyanıktı ve çantasından bir kravat çıkardı. Ama ikisi de onu takmak istedi ve iki ucundan çekti. "Dur, Kamil, kravat kopacak!" dedi Hayri. İkisi de hemen bıraktı. "Sırayla takalım, ilk sıra senin," dedi Hayri. Kamil kravatı taktı ve oyuna başladı. Hayri baklava dükkanında çalıştığı için tepsi taşımayı iyi biliyordu. Kamil'e bir tepsiyi tek elle nasıl tutacağını gösterdi. Sonra sıra Hayri'ye geldi ve kravatı o taktı. "Sana çok yakıştı, Hayri!" dedi Kamil ve güldü. Hayri ile Kamil bundan sonra tek bir şey olunca sırayla kullandı.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu sabah çok uyanıktı"
   - Cümle 2: «Kamil bu sabah çok uyanıktı ve çantasından bir kravat çıkardı.»
   - Açıklama: 'Uyanık' burada kurnaz anlamında mecazlı kullanılmış ve çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kamil bu sabah çok uyanıktı"
   - Cümle 2: «Kamil bu sabah çok uyanıktı ve çantasından bir kravat çıkardı.»
   - Açıklama: Kamil'in uyanık olması hiçbir işe yaramayan bir ayrıntı.
   - Açıklama: Kamil'in uyanıklığı olayda hiçbir işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri baklava dükkanında çalıştığı için tepsi taşımayı"
   - Cümle 8: «Hayri baklava dükkanında çalıştığı için tepsi taşımayı iyi biliyordu.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği kravat sorununun çözümünde işe yaramıyor, yalnız anılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kamil'e bir tepsiyi tek elle nasıl tutacağını gösterdi"
   - Cümle 9: «Kamil'e bir tepsiyi tek elle nasıl tutacağını gösterdi.»
   - Açıklama: Tepsi sebepsiz beliriyor ve kravat sorunuyla ilgisiz bir yan olay ekliyor.
   - Açıklama: Tepsi sebepsiz beliriyor ve kravat sorunuyla ilgisi yok.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tek bir şey olunca sırayla kullandı"
   - Cümle 12: «Hayri ile Kamil bundan sonra tek bir şey olunca sırayla kullandı.»
   - Açıklama: Cümle bozuk; ne kullanıldığı belirtilmemiş ve 'tek bir şey olunca' yapısı dilbilgisel değil.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tek bir şey olunca sırayla kullandı"
   - Cümle 12: «Hayri ile Kamil bundan sonra tek bir şey olunca sırayla kullandı.»
   - Açıklama: 'Tek bir şey olunca' anlamı belirsiz ve kelimeler yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0010` birebir aynı, ardından `@onarim: 9d9cd0bd762c55b72fab344dcfa9f8f3d4ca6dc3`, sonra gövde.

### Hikâye 4: tohum hayri-0011 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0011
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kristal', fiil 'fısıldamak', sıfat 'eskimiş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: küçük bir dalga parlak şeyi kumla örttü | dalgayı izleyip geri gidince kabuğu aldı
@tohum: hayri-0011
Deniz kıyısında Hayri ile Akın eskimiş bir kovayla kabuk topluyordu. "Akın, bak, suyun kenarında kocaman bir kristal parlıyor!" dedi Hayri abartarak. Ama küçük bir dalga geldi ve onu kumla örttü. Hayri dalgaları dikkatle izledi. Dalga geri gidince o şey yeniden göründü. Hayri hemen eğildi ve onu kumdan aldı. Bu, pembe ve çok parlak bir deniz kabuğuydu. Akın kabuğu kulağına tuttu. "Dinle, Hayri, içinden deniz sesi geliyor," diye fısıldadı Akın. Hayri de dinledi ve gülümsedi. Sonra kabuğu kovaya koydular. Hayri bundan sonra dalga geri gidince kıyıda kabuk aradı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 2: «"Akın, bak, suyun kenarında kocaman bir kristal parlıyor!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük bir dalga geldi ve onu kumla örttü"
   - Cümle 3: «Ama küçük bir dalga geldi ve onu kumla örttü.»
   - Açıklama: Dalganın örttüğü şeyi bir sonraki dalga kendiliğinden açıyor; sorun önemsiz ve kendiliğinden çözülüyor.
   - Açıklama: Dalga kabuğu örtüp hemen geri açıyor; sorun kendiliğinden çözülen önemsiz bir olay.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri bundan sonra dalga geri gidince kıyıda kabuk aradı"
   - Cümle 12: «Hayri bundan sonra dalga geri gidince kıyıda kabuk aradı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde çekilen dalganın ardından su çizgisine gitmek örnek gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0011` birebir aynı, ardından `@onarim: 8573ab314eec9b180d021403b4f5fa49505c0425`, sonra gövde.

### Hikâye 5: tohum hayri-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0012
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çöp', fiil 'yaklaşmak', sıfat 'kilitli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: bakkalın anahtarı düştü ve kayboldu | çöp kutusunun yanına eğilip anahtarı buldu
@tohum: hayri-0012
Sokakta Hayri, bakkalın önünde üzgün duran Kamil'e yaklaştı. Bakkalın kapısı kilitliydi ve Kamil anahtarı bulamıyordu. "Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil. Hayri olayı abartarak "Eyvah, bakkal kapalı kalırsa bütün mahalle aç kalır!" dedi. Kamil buna güldü ve biraz rahatladı. Sonra Hayri çöp kutusunun yanına gitti ve yere eğildi. Kutunun dibinde parlayan küçük bir anahtar vardı. Hayri anahtarı aldı ve Kamil'e uzattı. Kamil kapıyı hemen açtı. "Teşekkürler, Hayri, sen çok iyi bir arkadaşsın!" dedi Kamil.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sokakta Hayri, bakkalın önünde"
   - Cümle 1: «Sokakta Hayri, bakkalın önünde üzgün duran Kamil'e yaklaştı.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta, bakkalın önünde geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sokakta Hayri, bakkalın önünde üzgün duran Kamil'e yaklaştı"
   - Cümle 1: «Sokakta Hayri, bakkalın önünde üzgün duran Kamil'e yaklaştı.»
   - Açıklama: Başlıktaki yer ev iken hikaye sokakta, bakkalın önünde geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri olayı abartarak"
   - Cümle 4: «Hayri olayı abartarak "Eyvah, bakkal kapalı kalırsa bütün mahalle aç kalır!" dedi.»
   - Açıklama: 'Olayı abartarak' soyut bir anlatım ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0012` birebir aynı, ardından `@onarim: 9f227818db8bb2739d9fdcb5ea0ef5ab715475f1`, sonra gövde.

### Hikâye 6: tohum hayri-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0013
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'delik', fiil 'şişirmek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: top hep söndü çünkü üstünde küçük bir delik vardı | deliğe bant yapıştırıp topu yeniden şişirdi
@tohum: hayri-0013
Rüzgar esiyordu. Hayri deniz kıyısında renkli plaj topunu şişirmeye çalışıyordu. Ama top hep sönüyordu, çünkü üstünde küçük bir delik vardı. Yumak topa temkinli adımlarla yaklaştı ve onu kokladı. Hayri biraz düşündü. Hayri baklava dükkanında kutuları hep bantla kapatırdı. Cebinde de dükkandan kalan bir parça bant vardı. Hayri bandı deliğin üstüne sıkıca yapıştırdı. Sonra topu yeniden şişirdi ve top kocaman oldu. Hayri topu yavaşça Yumak'a doğru attı. Yumak havladı ve topu burnuyla geri itti. İkisi kumda uzun uzun oynadı. "Bu top artık ikimizin, Yumak!" dedi Hayri sevinçle.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yumak topa temkinli adımlarla"
   - Cümle 4: «Yumak topa temkinli adımlarla yaklaştı ve onu kokladı.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmediği soyut bir kelimedir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "topa temkinli adımlarla yaklaştı"
   - Cümle 4: «Yumak topa temkinli adımlarla yaklaştı ve onu kokladı.»
   - Açıklama: 'Temkinli' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0013` birebir aynı, ardından `@onarim: 24e0d11eabf2d1de405c15addebc5aa9bbc0ff27`, sonra gövde.

### Hikâye 7: tohum hayri-0014 (deneme 1 -> 2)

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
@plan: bank çok uzundu ve boyamak uzun sürüyordu | yemeği bekletip ikinci fırçayla boyamaya yardım etti
@tohum: hayri-0014
@degisim: pul -> fırça
Hayri parkta Basri Amca'yı gördü. Basri Amca parktaki eski bankı yeşile boyuyordu. Ama bank çok uzundu ve Basri Amca çok sabırsızdı. "Bu iş hiç bitmeyecek!" dedi Basri Amca. Hayri çok acıkmıştı ve eve yemeğe gidiyordu. "Yemek bekleyebilir, Basri Amca, ben de size yardım edeyim!" dedi Hayri. Basri Amca kutudan ikinci bir fırça çıkarıp ona verdi. Hayri bankın bir ucunu, Basri Amca öbür ucunu boyadı. Az sonra ikisi ortada buluştu. Eski bank yepyeni ve yemyeşil oldu. "Teşekkürler, Hayri, birlikte ne çabuk bitirdik!" dedi Basri Amca.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Basri Amca çok sabırsızdı"
   - Cümle 3: «Ama bank çok uzundu ve Basri Amca çok sabırsızdı.»
   - Açıklama: 'Sabırsız' soyut bir karakter kelimesi, 3 yaşındaki çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yemek bekleyebilir, Basri Amca"
   - Cümle 6: «"Yemek bekleyebilir, Basri Amca, ben de size yardım edeyim!" dedi Hayri.»
   - Açıklama: 'Yemek bekleyebilir' deyimsel bir kullanım; yemek beklemez, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0014` birebir aynı, `@degisim: pul -> fırça` (tutuyorsan), ardından `@onarim: bbd862a7ee4db798a7b4be637859043497d34a5b`, sonra gövde.

### Hikâye 8: tohum hayri-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0015
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'turp', fiil 'eğilmek', sıfat 'güneşli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: yuvarlak turp yarışta hep yere düşüyordu | turpu düz yanından kaşığa koyup yavaş yürüdü
@tohum: hayri-0015
Ormanda, kamp yerinde hava çok güneşliydi. Hayri ile Mert kaşıkla turp taşıyarak büyük ağaca kadar yarışıyordu. Ama Hayri'nin turpu çok yuvarlaktı ve hep yere düşüyordu. "Mert, turp yine düştü!" dedi Hayri ve güldü. Hayri eğildi ve turpu yerden aldı. Çok acıkmıştı ama onu yemedi, çünkü yarış daha bitmemişti. Turpun bir yanı biraz düzdü. Hayri turpu kaşığa düz yanından koydu. Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi. "Bak, Mert, artık düşmüyor!" dedi Hayri. İkisi de gülerek büyük ağaca vardı. Hayri bundan sonra yuvarlak şeyleri kaşığa düz yanından koydu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı ama onu yemedi"
   - Cümle 6: «Çok acıkmıştı ama onu yemedi, çünkü yarış daha bitmemişti.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor; kartın özellik alanının işe yarar kullanımı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı ama onu yemedi"
   - Cümle 6: «Çok acıkmıştı ama onu yemedi, çünkü yarış daha bitmemişti.»
   - Açıklama: Acıkma ayrıntısı olayda hiçbir işe yaramıyor, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0015` birebir aynı, ardından `@onarim: ef739cfe85babf752712bf1f3d014fb96869030a`, sonra gövde.

### Hikâye 9: tohum hayri-0016 (deneme 1 -> 2)

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
Deniz kıyısında rüzgar çok esiyordu. Hayri ile Kamil kumda oturmuş denize bakıyordu. Birden rüzgar Kamil'in bembeyaz şapkasını uçurdu ve şapka kayboldu. "Eyvah, şapkam gitti!" dedi Kamil. Hayri olayı abartarak "Şapkan uçup bulutlara kadar çıktı!" dedi. Kamil güldü ama yine de şapkasını istiyordu. Hayri havada uçan kum tanelerini izledi. Kumlar hep büyük kayalara doğru uçuyordu. Hayri o yöne yürüdü ve kayaların arkasına baktı. Şapka iki kayanın arasına sıkışmıştı. Hayri şapkayı aldı ve Kamil'e götürdü. "Teşekkürler, Hayri!" dedi Kamil ve şapkasını taktı. Hayri bundan sonra uçan eşyaları rüzgarın estiği yönde aradı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri olayı abartarak"
   - Cümle 5: «Hayri olayı abartarak "Şapkan uçup bulutlara kadar çıktı!" dedi.»
   - Açıklama: 'Olay' ve 'abartmak' soyut kelimeler, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0016` birebir aynı, `@degisim: yapıştırıcı -> şapka` (tutuyorsan), ardından `@onarim: f4eaaebbd9ddb0b2ca8231169631cd5f65a31538`, sonra gövde.

### Hikâye 10: tohum hayri-0018 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0018
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çit', fiil 'bindirmek', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: sokakta çamurlu izler vardı ve kimin olduğu belli değildi | deliğe gidip çitin arasından baktı
@tohum: hayri-0018
@degisim: bindirmek -> eşelemek
Hayri sokakta yürürken yerde çamurlu izler gördü. İzler çitin altındaki bir deliğe kadar gidiyordu. Hayri bu izleri çok merak etti. Hayri abartarak bunları kocaman ayak izleri sandı. Sonra deliğe kadar yürüdü. Çitin arasından bahçeye dikkatle baktı. Çalışkan Yumak bahçede ıslak toprağı eşeledi. Yumak'ın ayakları çamurluydu. "Yumak, bu izler senin!" dedi Hayri ve güldü. Yumak kuyruğunu salladı ve bir kez havladı. Sonra toprağın içinden küçük bir kemik çıkardı. Hayri çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (6):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri sokakta yürürken yerde"
   - Cümle 1: «Hayri sokakta yürürken yerde çamurlu izler gördü.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri sokakta yürürken yerde çamurlu izler gördü"
   - Cümle 1: «Hayri sokakta yürürken yerde çamurlu izler gördü.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta başlıyor ve bitiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak bunları kocaman ayak izleri sandı"
   - Cümle 4: «Hayri abartarak bunları kocaman ayak izleri sandı.»
   - Açıklama: İzler zaten ayak izi; 'abartarak ... sandı' anlamca yerinde değil ve çocuk için soyut.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bunları"
   - Cümle 4: «Hayri abartarak bunları kocaman ayak izleri sandı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez ve cümlede yerinde kullanılmamış.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak bunları kocaman ayak izleri sandı"
   - Cümle 4: «Hayri abartarak bunları kocaman ayak izleri sandı.»
   - Açıklama: Abartma kurulup hiç kullanılmıyor, olayda bir işe yaramıyor.
   - Açıklama: Kocaman ayak izi sanısı kurulup olayda hiçbir işe yaramıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "toprağın içinden küçük bir kemik çıkardı"
   - Cümle 11: «Sonra toprağın içinden küçük bir kemik çıkardı.»
   - Açıklama: Kemik sebepsiz beliriyor ve işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0018` birebir aynı, `@degisim: bindirmek -> eşelemek` (tutuyorsan), ardından `@onarim: 6492ebfe01b1bddfe4c4931792bd8196e7a40ce4`, sonra gövde.

### Hikâye 11: tohum hayri-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0019
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çeşme', fiil 'kırpmak', sıfat 'kocaman'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: parmakla musluğu kapattı ve su arkadaşını ıslattı | özür dileyip ona kocaman bir havlu getirdi
@tohum: hayri-0019
Bir sabah Hayri ile Akın kamp yerinde çeşmede ellerini yıkıyordu. Hayri şaka olsun diye parmağıyla musluğun ucunu kapattı. Su her yana fışkırdı ve Akın'ın yüzü sırılsıklam oldu. Akın gözlerini hızlı hızlı kırptı ve yüzünü buruşturdu. Hayri hemen parmağını çekti. "Özür dilerim, Akın, seni ıslatmak istemedim," dedi Hayri. Sonra çadıra koştu ve kocaman bir havlu getirdi. Akın havluyla yüzünü ve saçlarını kuruladı. "Bu su bir şelale gibiydi!" dedi Hayri abartarak. Akın buna çok güldü. "Özrünü kabul ettim, Hayri, bu havlu çok yumuşak!" dedi Akın.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parmakla musluğu kapattı"
   - Cümle 0 (plan satırı): «parmakla musluğu kapattı ve su arkadaşını ıslattı | özür dileyip ona kocaman bir havlu getirdi»
   - Açıklama: 'Musluğu kapatmak' suyu kesmek anlamına gelir; kastedilen musluğun ucunu parmakla tıkamaktır.
   - Açıklama: 'Musluğu kapatmak' suyu kesmek anlamına gelir; kastedilen musluğun ucunu parmakla tıkamak.
2. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Hayri şaka olsun diye parmağıyla musluğun ucunu kapattı"
   - Cümle 2: «Hayri şaka olsun diye parmağıyla musluğun ucunu kapattı.»
   - Açıklama: Arkadaşını ıslatan şaka çocuğun taklit edebileceği bir davranış olarak gösteriliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Bu su bir şelale gibiydi!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelimedir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu su bir şelale gibiydi!"
   - Cümle 9: «"Bu su bir şelale gibiydi!" dedi Hayri abartarak.»
   - Açıklama: Benzetme ve 'abartarak' kelimesi 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0019` birebir aynı, ardından `@onarim: 5ebf28faf620e6122e2a6df01e2c2eb742d568de`, sonra gövde.

### Hikâye 12: tohum hayri-0020 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0020
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamera', fiil 'açmak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kum kuru olduğu için kale hep yıkılıyordu | kovayla ıslak kum getirip kaleyi yeniden yaptı
@tohum: hayri-0020
Bir sabah deniz çok sakindi. Hayri kıyıda Basri Amca'yla kumdan bir kale yapıyordu. Ama kale hep yıkılıyordu, çünkü kum çok kuruydu. "Of, yine olmadı!" dedi Basri Amca. Hayri suyun kenarına baktı, oradaki kum koyu ve ıslaktı. Hayri kovasını bu kumla doldurdu ve geri getirdi. İkisi kumu sıkıca bastırdı ve onu yeniden kurdu. Bu kez kale hiç yıkılmadı. "Basri Amca, bu kale bir saray kadar büyük oldu!" dedi Hayri abartarak. Basri Amca güldü ve kamerayı açtı. Sonra kalenin önünde Hayri'nin fotoğrafını çekti. Hayri çok sevindi, çünkü birlikte güzel bir kale yapmışlardı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bastırdı ve onu yeniden"
   - Cümle 7: «İkisi kumu sıkıca bastırdı ve onu yeniden kurdu.»
   - Açıklama: 'Onu' zamirinin kumu mu kaleyi mi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onu yeniden kurdu"
   - Cümle 7: «İkisi kumu sıkıca bastırdı ve onu yeniden kurdu.»
   - Açıklama: 'Onu' zamiri en son geçen kumu gösteriyor gibi; kalenin kastedildiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İkisi kumu sıkıca bastırdı ve onu yeniden kurdu"
   - Cümle 7: «İkisi kumu sıkıca bastırdı ve onu yeniden kurdu.»
   - Açıklama: 'onu' zamiri kumu mu kaleyi mi gösteriyor belli değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 9: «"Basri Amca, bu kale bir saray kadar büyük oldu!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'abartarak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Basri Amca güldü ve kamerayı açtı"
   - Cümle 10: «Basri Amca güldü ve kamerayı açtı.»
   - Açıklama: Kamera sebepsiz beliriyor ve sorunla bağı olmayan bir olay başlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0020` birebir aynı, ardından `@onarim: 80dcec11af88a0369c91de4211941c7596d90c26`, sonra gövde.
