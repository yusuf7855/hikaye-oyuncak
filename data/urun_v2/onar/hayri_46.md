# Editör görevi (onarım): Hayri, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar46.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0130 (deneme 3 -> 4)

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
@plan: dalga köpeğin topunu suya çekti | geniş tepsiyi uzatıp topu kıyıya getirdi
@tohum: hayri-0130
Bir sabah Hayri boş baklava tepsisini dükkana götürüyordu. Deniz kıyısında tepsiyi kuma koydu ve Yumak'la top oynadı. Birden bir dalga geldi ve Yumak'ın topunu suya çekti. Top kıyıya çok yakın, sığ suda sallanıyordu ama Hayri'nin eli yetişmedi. Yumak topa bakıp havladı ve kuma oturdu. Hayri suya girmedi ve kuru kumda durdu. Kumdaki geniş tepsiyi aldı ve ucunu topa uzattı. Tepsiyle topu yavaşça kendine doğru çekti. Top kuma yuvarlandı. Yumak hemen kalktı ve topa koştu. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. Hayri çok sevindi, çünkü Yumak'ın topunu dalgadan geri almıştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri boş baklava tepsisini dükkana götürüyordu"
   - Cümle 1: «Bir sabah Hayri boş baklava tepsisini dükkana götürüyordu.»
   - Açıklama: Hikaye deniz kıyısında değil dükkana giden yolda başlıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok yakın, sığ suda sallanıyordu"
   - Cümle 4: «Top kıyıya çok yakın, sığ suda sallanıyordu ama Hayri'nin eli yetişmedi.»
   - Açıklama: 'Sığ' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kumdaki geniş tepsiyi aldı ve ucunu topa uzattı"
   - Cümle 7: «Kumdaki geniş tepsiyi aldı ve ucunu topa uzattı.»
   - Açıklama: Tek başına bir çocuğun dalgaların çektiği topu denizden almaya uğraşması taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0130` birebir aynı, ardından `@onarim: 67303baed45587018074485fdedbed5a3312dd26`, sonra gövde.

### Hikâye 2: tohum hayri-0135 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kaydırakta nereden geldiği bilinmeyen bir ışık vardı | başını sağa sola çevirdi ve ışığı kaskının yaptığını buldu
@tohum: hayri-0135
Bir sabah Hayri kırmızı kaskıyla parkta hızlı hızlı koşuyordu. Birden kaydırağın üstünde küçük bir şey ışıldadı. Hayri bu ışığın nereden geldiğini çok merak etti. Etrafa baktı ama bir şey bulamadı. Sonra durdu ve ışık da kaydırakta durdu. Her şeyi abartmayı seven Hayri, ışığı kaydırağa düşen bir yıldız sandı. Yıldıza bakmak için başını sağa sola çevirdi. Işık da kaydırakta bir o yana bir bu yana gitti. Hayri eliyle kaskını tuttu ve güldü. Işık, kaskın parlak üstünden geliyordu! Sonra Hayri ışığı kaydırakta gezdirdi ve koşmaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ışığı kaskının yaptığını buldu"
   - Cümle 0 (plan satırı): «kaydırakta nereden geldiği bilinmeyen bir ışık vardı | başını sağa sola çevirdi ve ışığı kaskının yaptığını buldu»
   - Açıklama: Işık yapılmaz; 'ışığın kaskından geldiğini' olmalı, fiil nesnesine uymuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ışığın nereden geldiğini çok merak etti"
   - Cümle 3: «Hayri bu ışığın nereden geldiğini çok merak etti.»
   - Açıklama: Kaydıraktaki bir ışık gerçek bir sorun değil, çözülmesi gereken önemli bir şey yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Her şeyi abartmayı seven"
   - Cümle 6: «Her şeyi abartmayı seven Hayri, ışığı kaydırağa düşen bir yıldız sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Her şeyi abartmayı seven Hayri"
   - Cümle 6: «Her şeyi abartmayı seven Hayri, ışığı kaydırağa düşen bir yıldız sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0135` birebir aynı, ardından `@onarim: b34d246133bf00938a5bc713e156efbc608f093b`, sonra gövde.

### Hikâye 3: tohum hayri-0136 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@degisim: korunmak -> koklamak
Hayri sırtında çantasıyla parkta salıncakta sallanıyordu. Çok acıkmıştı ve birden tatlı bir koku geldi. Hayri bu kokunun nereden geldiğini çok merak etti. Önce bunun pahalı bir parfüm kokusu olduğunu düşündü. Ama koku, kek kokusuna daha çok benziyordu. Hayri salıncaktan indi ve kaydırağın yanına yürüdü. Orada durdu ve havayı kokladı. Hayri nereye gitse koku da oradaydı. Hayri şaşırdı ve çantasını açtı. Çantanın içinde bir dilim kek vardı. Keki kendisi hazırlayıp çantaya koymuş ama unutmuştu. Hayri güldü ve keki mutlu mutlu yedi. Hayri bundan sonra çantasına koyduğu yiyecekleri hiç unutmadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pahalı bir parfüm kokusu"
   - Cümle 4: «Önce bunun pahalı bir parfüm kokusu olduğunu düşündü.»
   - Açıklama: 'Pahalı parfüm' 3 yaşındaki çocuğa uzak, soyut bir nitelendirme.
   - Açıklama: 'Pahalı parfüm' soyut ve küçük çocuğa yabancı bir kavram.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce bunun pahalı bir parfüm kokusu olduğunu düşündü"
   - Cümle 4: «Önce bunun pahalı bir parfüm kokusu olduğunu düşündü.»
   - Açıklama: Parfüm tahmini olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pahalı bir parfüm kokusu olduğunu"
   - Cümle 4: «Önce bunun pahalı bir parfüm kokusu olduğunu düşündü.»
   - Açıklama: Parfüm düşüncesi hiçbir işe yaramayan, olaydan çıkmayan bir ayrıntı.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "çantaya koymuş ama unutmuştu"
   - Cümle 11: «Keki kendisi hazırlayıp çantaya koymuş ama unutmuştu.»
   - Açıklama: Anlatımda '-mış' kipine kayılıyor; 'koymuştu' olmalı.
   - Açıklama: Anlatım -mış'lı zamana kayıyor; 'koymuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0136` birebir aynı, `@degisim: korunmak -> koklamak` (tutuyorsan), ardından `@onarim: d3321038a0ca0fcd80b6dae0ee741b1aae239239`, sonra gövde.

### Hikâye 4: tohum hayri-0137 (deneme 3 -> 4)

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
@degisim: tomurcuk -> sandviç
Hayri kamp yerinde yemek yapma oyunu oynuyordu. Çok acıkmıştı, bu yüzden kendine peynirli bir sandviç hazırladı. Ama tabak kütüğün üstünde durmadı, çünkü kütük eğriydi. Tabak kaydı ve sandviç neredeyse yere düşüyordu. Hayri tabağı hemen tuttu ve etrafa baktı. Ağaçların arasında büyük ve düz bir taş gördü. Tabağı bu taşın üstüne koydu. Tabak artık hiç kaymadı. Hayri bir adım geri çekildi ve tabağa baktı. Sandviç tabağın ortasında mükemmel duruyordu. Hayri taşın yanına oturdu ve sandviçini yedi. Hayri çok sevindi, çünkü sandviçini yere düşürmeden yiyebilmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tabağın ortasında mükemmel duruyordu"
   - Cümle 10: «Sandviç tabağın ortasında mükemmel duruyordu.»
   - Açıklama: 'Mükemmel' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0137` birebir aynı, `@degisim: tomurcuk -> sandviç` (tutuyorsan), ardından `@onarim: 9ad6b1a89be26a2514b8dde5d728ee86447f0e05`, sonra gövde.

### Hikâye 5: tohum hayri-0138 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0138
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hortum', fiil 'soğumak', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: tek kova vardı ve ikisi de aynı anda istedi | sırayı arkadaşına verip önce sandviçini yedi
@tohum: hayri-0138
@degisim: hortum -> kova
Hayri ile Akın deniz kıyısında kumda bir havuz kazdı. Kum çok sıcaktı ve havuza su doldurmak istediler. Ama yalnız bir kova vardı. İkisi de kovayı aynı anda çekti. Kovanın kulpu lastik gibi esnekti ve iki yana büküldü. Hayri kulp kopmasın diye kovayı bıraktı. Hayri çok acıkmıştı ve çantasında sandviç vardı. "Akın, sen önce su taşı, ben de sandviçimi yerim," dedi Hayri. Akın sevindi ve kovayla denizden su getirdi. "Sıra sende, Hayri," dedi Akın ve kovayı ona verdi. Hayri de havuza su döktü. Havuz dolunca etrafındaki sıcak kum da soğudu. Sonra Hayri ile Akın sırayla su taşımaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sırayı arkadaşına verip önce sandviçini yedi"
   - Cümle 0 (plan satırı): «tek kova vardı ve ikisi de aynı anda istedi | sırayı arkadaşına verip önce sandviçini yedi»
   - Açıklama: Gövdede Hayri sandviç yiyeceğini söylüyor ama yediği hiç gösterilmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kulpu lastik gibi esnekti"
   - Cümle 5: «Kovanın kulpu lastik gibi esnekti ve iki yana büküldü.»
   - Açıklama: 'Lastik gibi' benzetme ve 'esnek' soyut kelime 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "lastik gibi esnekti"
   - Cümle 5: «Kovanın kulpu lastik gibi esnekti ve iki yana büküldü.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki çocuk bilmez ve benzetme soyut kalıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kovanın kulpu lastik gibi esnekti"
   - Cümle 5: «Kovanın kulpu lastik gibi esnekti ve iki yana büküldü.»
   - Açıklama: Kulbun lastik gibi esnemesi sebepsiz ve tuhaf bir ayrıntı; ayrıca havuzun kumu soğutması da işlevsiz kalıyor.
   - Açıklama: Kulbun lastik gibi esnemesi sebepsiz ve tuhaf bir ayrıntı olarak beliriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "etrafındaki sıcak kum da soğudu"
   - Cümle 12: «Havuz dolunca etrafındaki sıcak kum da soğudu.»
   - Açıklama: Kumun soğuması sorunla bağı olmayan işlevsiz bir olay olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0138` birebir aynı, `@degisim: hortum -> kova` (tutuyorsan), ardından `@onarim: 0acaf9f3de3b6a1b013aed08048ade3a9c1c0080`, sonra gövde.

### Hikâye 6: tohum hayri-0140 (deneme 3 -> 4)

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
Hayri deniz kıyısında Basri Amca'nın doğum günü için sürpriz hazırlıyordu. Kumun üstüne bir kalp çizmişti ama kalp çok küçüktü. Basri Amca yukarıdaki bankta oturuyordu ve küçük kalbi oradan göremezdi. Hayri bu kez kalbin boyunu çok abarttı. Kumun üstüne kocaman bir kalp çizdi. Ortasına da getirdiği erik sepetini koydu. "Basri Amca, aşağı bak!" diye seslendi Hayri. Basri Amca kocaman kalbi gördü ve kıyıya indi. Hayri'ye sıkıca sarıldı. "Bu çok güzel bir sürpriz, Hayri," dedi Basri Amca. Sonra ikisi yan yana oturup erikleri mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kalbin boyunu çok abarttı"
   - Cümle 4: «Hayri bu kez kalbin boyunu çok abarttı.»
   - Açıklama: 'Abartmak' fiziksel boyutu büyütmek anlamında yanlış kullanılmış.
   - Açıklama: 'Abartmak' fiili kalbi büyük çizmek anlamında yanlış kullanılmış; 'kalbi çok büyük çizdi' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kalbin boyunu çok abarttı"
   - Cümle 4: «Hayri bu kez kalbin boyunu çok abarttı.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bu kez kalbin boyunu çok abarttı"
   - Cümle 4: «Hayri bu kez kalbin boyunu çok abarttı.»
   - Açıklama: Karttaki özellik olayları abartmaktır, hikayede kalbi büyük çizmek olarak kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "getirdiği erik sepetini koydu"
   - Cümle 6: «Ortasına da getirdiği erik sepetini koydu.»
   - Açıklama: Erik sepeti önceden kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0140` birebir aynı, `@degisim: değerli -> güzel` (tutuyorsan), ardından `@onarim: e5db86bec3d1a071382b685a0fc6ecb8758e5669`, sonra gövde.

### Hikâye 7: tohum hayri-0141 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0141
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: kaybolan eşya
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'sofra', fiil 'durdurmak', sıfat 'konuşkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: baklava kutusu yolda sepetten düşüp kaybolmuştu | köpekten yardım isteyip kutuyu birlikte buldu
@tohum: hayri-0141
@degisim: konuşkan -> tatlı
Hayri kamp yerinde bir sofra kuruyordu. Çalıştığı baklava dükkanından bir kutu tatlı baklava getirmişti. Ama kutu yolda sepetten düşüp kaybolmuştu. Yumak da yanında zıplıyordu. Hayri onu nazikçe durdurdu. Kutuyu Hayri taşıdığı için elleri baklava kokuyordu. Ellerini Yumak'ın burnuna uzattı. "Yumak, bu kokuyu bulabilir misin?" diye sordu Hayri. Yumak elleri kokladı ve ağaçların arasına koştu. Bir çalının yanında durdu ve havladı. Kutu çalının altındaydı! Hayri kutuyu alıp sofranın ortasına koydu. "Teşekkürler, Yumak, baklavayı birlikte bulduk!" dedi Hayri.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bir kutu tatlı baklava getirmişti"
   - Cümle 2: «Çalıştığı baklava dükkanından bir kutu tatlı baklava getirmişti.»
   - Açıklama: Hayri kutuyu getirmiş deniyor ama hemen ardından kutunun yolda düşüp kaybolduğu söyleniyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kutuyu Hayri taşıdığı için elleri"
   - Cümle 6: «Kutuyu Hayri taşıdığı için elleri baklava kokuyordu.»
   - Açıklama: Söz dizimi bozuk; 'Hayri kutuyu taşıdığı için elleri' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu kokuyu bulabilir misin"
   - Cümle 8: «"Yumak, bu kokuyu bulabilir misin?" diye sordu Hayri.»
   - Açıklama: Koku bulunmaz; kokunun geldiği kutu aranır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0141` birebir aynı, `@degisim: konuşkan -> tatlı` (tutuyorsan), ardından `@onarim: 2a881c723471c0cdc5b1018cf57c067515d6f026`, sonra gövde.

### Hikâye 8: tohum hayri-0142 (deneme 3 -> 4)

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
@plan: soğuk parmaklarıyla arkadaşı kabın kapağını açamadı | ellerini hızlı hızlı ovuşturup kapağı ona açtı
@tohum: hayri-0142
Bir sabah Hayri ile Akın kamp yerindeydi ve hava çok serindi. Akın küçük bir jöle kabını açmak istedi. Ama parmakları soğuktu ve kapağı sıkıca tutamadı. Hayri bunu gördü ve arkadaşına yardım etmek istedi. "Akın, kabı bana ver, ben açarım," dedi Hayri. Hayri'nin elleri de biraz soğuktu. Hayri ellerini abartarak çok hızlı ve uzun uzun ovuşturdu. Elleri hemen ısındı. Hayri kapağı iki eliyle tuttu ve kolayca açtı. Sonra kabı Akın'a geri verdi. "Teşekkürler, Hayri, sen de biraz jöle ister misin?" diye sordu Akın. Hayri çok sevindi, çünkü arkadaşına yardım edebilmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ovuşturup kapağı ona açtı"
   - Cümle 0 (plan satırı): «soğuk parmaklarıyla arkadaşı kabın kapağını açamadı | ellerini hızlı hızlı ovuşturup kapağı ona açtı»
   - Açıklama: 'Kapağı ona açtı' yanlış kullanım; 'kabı onun için açtı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ellerini abartarak çok hızlı"
   - Cümle 7: «Hayri ellerini abartarak çok hızlı ve uzun uzun ovuşturdu.»
   - Açıklama: 'Abartarak' soyut bir kelime ve burada yanlış yerde kullanılmış.
   - Açıklama: 'Abartarak' soyut ve bu bağlamda çocuğa uygun olmayan bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri ellerini abartarak çok hızlı"
   - Cümle 7: «Hayri ellerini abartarak çok hızlı ve uzun uzun ovuşturdu.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartı el ovuşturma hareketine dönüşmüş, karttaki gibi kullanılmamış.
   - Açıklama: Kartta özellik olayları abartmaktır; burada abartma el ovuşturma hareketine uygulanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0142` birebir aynı, ardından `@onarim: 9c61579212959eb8a19a425bf58b0dcb67bf1dc8`, sonra gövde.

### Hikâye 9: tohum hayri-0143 (deneme 3 -> 4)

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
Deniz kıyısında güneş parlıyordu. Hayri kumda ilk kez çember çevirmeyi deniyordu. Ama çember her seferinde düştü, çünkü Hayri belini çok yavaş sallıyordu. Hayri çemberi yerden aldı. Çemberi iki eliyle beline yaklaştırdı. Bu kez hareketini abarttı ve belini çok güçlü ve hızlı salladı. Çember belinde bir kez, iki kez, üç kez döndü! Hayri durmadı ve saymaya devam etti. Çember tam on kez dönüp kuma indi. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü yeni oyunu sonunda öğrenmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu kez hareketini abarttı"
   - Cümle 6: «Bu kez hareketini abarttı ve belini çok güçlü ve hızlı salladı.»
   - Açıklama: 'Abarttı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez hareketini abarttı"
   - Cümle 6: «Bu kez hareketini abarttı ve belini çok güçlü ve hızlı salladı.»
   - Açıklama: Kartta özellik olayları abartmak; burada abartma beden hareketini büyütmek olarak kullanılıyor.
   - Açıklama: Kartta özellik olayları abartmak iken burada beden hareketini abartmak olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0143` birebir aynı, ardından `@onarim: b6db237bfce98af260544e452e70053212b5cdef`, sonra gövde.

### Hikâye 10: tohum hayri-0144 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0144
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'araba', fiil 'çözülmek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: çantaya bağlı araba kayboldu ve yolda izler vardı | çalıya yürüdü ve altında arabasını buldu
@tohum: hayri-0144
@degisim: havalı -> mavi
Bir sabah Hayri çok acıkmıştı ve çantasını bıraktığı banka döndü. Ama çantasına bağlı mavi oyuncak arabası yerinde yoktu. Hayri arabasını çok seviyordu ve onu hemen bulmak istedi. Bankın yanındaki tozlu yolda ince izler gördü. İzler yokuş aşağı bir çalıya gidiyordu. Hayri izlere bakarak çalıya doğru yürüdü. Çalının altında arabasını buldu. Arabanın ipi boştu, çünkü düğüm çözülmüştü. Araba tekerlekleriyle yokuş aşağı inmiş ve izleri yapmıştı. Hayri arabayı çantasına sıkıca yeniden bağladı. Sonra banka oturdu ve sandviçini yedi. Hayri çok sevindi, çünkü arabasını bulmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri çok acıkmıştı ve"
   - Cümle 1: «Bir sabah Hayri çok acıkmıştı ve çantasını bıraktığı banka döndü.»
   - Açıklama: Tohumdaki acıkma özelliği arabayı bulma sorununun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Hayri çok acıkmıştı"
   - Cümle 1: «Bir sabah Hayri çok acıkmıştı ve çantasını bıraktığı banka döndü.»
   - Açıklama: Tohum özelliği acıkmak yalnız girişte anılıyor, arabanın bulunmasında hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0144` birebir aynı, `@degisim: havalı -> mavi` (tutuyorsan), ardından `@onarim: 31ab1b5abc059b2c1946a03eb49a9302ed145e4a`, sonra gövde.

### Hikâye 11: tohum hayri-0146 (deneme 2 -> 3)

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
@plan: arkadaşı kabukları az kalmasın diye almak istemedi | kabukları kuma döktü ve kocaman bir tepe yaptı
@tohum: hayri-0146
@degisim: küpe -> kabuk
Bir sabah Hayri ile Kamil deniz kıyısında oturuyordu. Hayri'nin kovası renkli kabuklarla doluydu ama Kamil'in kovası boştu. Hayri kovasını uzattı ama Kamil, Hayri'nin kabukları az kalmasın diye almadı. Hayri bütün kabukları kuma döktü. Sonra onları abartarak kocaman bir tepe yaptı. Kamil tepeye bakıp güldü, çünkü kabuklar gerçekten çok fazlaydı. Kamil de elini uzattı. Kabuklar ince ve kırılgandı. Kamil onları yavaşça tuttu ve en güzel üç tanesini seçti. Sonra onları kendi kovasına dikkatle koydu. Hayri de Kamil de çok sevindi, çünkü ikisinin de kabukları vardı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "arkadaşı kabukları az kalmasın diye"
   - Cümle 0 (plan satırı): «arkadaşı kabukları az kalmasın diye almak istemedi | kabukları kuma döktü ve kocaman bir tepe yaptı»
   - Açıklama: Plan satırında kimin kabuklarının az kalacağı belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onları abartarak kocaman bir"
   - Cümle 5: «Sonra onları abartarak kocaman bir tepe yaptı.»
   - Açıklama: 'Abartarak' soyut kavram; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime ve burada yanlış kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kabuklar ince ve kırılgandı"
   - Cümle 8: «Kabuklar ince ve kırılgandı.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmediği bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ince ve kırılgandı"
   - Cümle 8: «Kabuklar ince ve kırılgandı.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmediği bir kelime.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kabuklar ince ve kırılgandı"
   - Cümle 8: «Kabuklar ince ve kırılgandı.»
   - Açıklama: Kabukların kırılgan olduğu bilgisi sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0146` birebir aynı, `@degisim: küpe -> kabuk` (tutuyorsan), ardından `@onarim: 080fddb214c654b30c8d58f7d4dfbf0edeb794e9`, sonra gövde.

### Hikâye 12: tohum hayri-0147 (deneme 2 -> 3)

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
Rüzgar ağaçların arasında serin serin esiyordu. Hayri kamp yerinde Basri Amca'nın gizemli kutusunu merak etti ve sormadan açtı. Basri Amca bunu görünce kızdı, çünkü Hayri izin istememişti. Kutunun içinde güneşte parlayan renkli taşlar vardı. Hayri kutuyu hemen kapattı ve Basri Amca'dan özür diledi. Sonra çantasından bir paket baklava çıkardı. Hayri bu baklavayı sabah çalıştığı dükkandan getirmişti. Hayri baklavayı Basri Amca ile paylaştı. Basri Amca bir dilim yedi ve gülümsedi. Sonra kutuyu kendisi açtı ve taşları Hayri'ye tek tek gösterdi. Hayri çok rahatladı, çünkü Basri Amca artık ona kızgın değildi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Basri Amca'nın gizemli kutusunu"
   - Cümle 2: «Hayri kamp yerinde Basri Amca'nın gizemli kutusunu merak etti ve sormadan açtı.»
   - Açıklama: 'Gizemli' soyut bir kelimedir, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra çantasından bir paket baklava çıkardı"
   - Cümle 6: «Sonra çantasından bir paket baklava çıkardı.»
   - Açıklama: Baklava daha önce hiç kurulmadan çözüm anında sebepsizce beliriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Basri Amca bir dilim yedi ve gülümsedi"
   - Cümle 9: «Basri Amca bir dilim yedi ve gülümsedi.»
   - Açıklama: Amcayı özürden çok baklava yumuşatıyor; çözüm izinsiz açma sebebine değil ikrama dayanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0147` birebir aynı, `@degisim: fıskiye -> kutu` (tutuyorsan), ardından `@onarim: 531d80959166cbc0f18bafaa10937b1dafbb5824`, sonra gövde.
