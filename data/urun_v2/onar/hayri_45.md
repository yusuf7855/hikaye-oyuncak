# Editör görevi (onarım): Hayri, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar45.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0114 (deneme 3 -> 4)

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
@degisim: sergilemek -> asmak
Bir öğle vakti Hayri ile Kamil, mahalledeki bir bahçede resim yapıyordu. Resimlerini çitin üstüne asmak istiyorlardı. Ama Kamil'in tek kalemi yere düşüp kırıldı ve kağıdı boş kaldı. Hayri'nin kutusunda bir sürü renkli kalem vardı. Hayri bunların yarısını Kamil'e uzattı. Kamil, Hayri'ye kalem kalmayacak diye almak istemedi. Hayri abartarak kutuda bin tane kalem olduğunu söyledi. Kamil buna çok güldü ve onları aldı. İkisi birlikte oturdu. Kamil kocaman bir kitap, Hayri de mavi bir bornoz çizdi. Sonra iki kağıdı çite yan yana astılar. Hayri bundan sonra kalemlerini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "mahalledeki bir bahçede resim yapıyordu"
   - Cümle 1: «Bir öğle vakti Hayri ile Kamil, mahalledeki bir bahçede resim yapıyordu.»
   - Açıklama: Başlıktaki yer ev olduğu halde hikaye mahalledeki bir bahçede geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye mahalledeki bir bahçede geçiyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kalem kalmayacak diye almak istemedi"
   - Cümle 6: «Kamil, Hayri'ye kalem kalmayacak diye almak istemedi.»
   - Açıklama: Hayri kalemlerin yalnız yarısını verdiği halde Kamil ona kalem kalmayacağını düşünüyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kutuda bin"
   - Cümle 7: «Hayri abartarak kutuda bin tane kalem olduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0114` birebir aynı, `@degisim: sergilemek -> asmak` (tutuyorsan), ardından `@onarim: 25b1f9124dfc551f9485e54707e83fe884cd3866`, sonra gövde.

### Hikâye 2: tohum hayri-0115 (deneme 3 -> 4)

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
Deniz kıyısında Yumak, Hayri'yi havlayarak karşıladı. Ama oyun sırasında Yumak'ın topu iki büyük taşın arasına sıkışmıştı. Yumak burnuyla topu itti ama çıkaramadı. Hayri'nin eli de taşların arasına sığmadı. "Yumak, buna ağaç kadar uzun bir dal lazım!" dedi Hayri abartarak. Sonra Hayri kumda uzun bir dal buldu. Dalı taşların arasına soktu ve topu yavaşça itti. Top taşların arasından çıktı ve kuma düştü. Yumak kabarık kuyruğunu sallayarak topa koştu. Yumak havladı ve topu Hayri'ye getirdi. Hayri bundan sonra Yumak'la taşlardan uzakta top oynadı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama oyun sırasında Yumak'ın topu"
   - Cümle 2: «Ama oyun sırasında Yumak'ın topu iki büyük taşın arasına sıkışmıştı.»
   - Açıklama: Yumak Hayri'yi daha yeni karşılamışken top oyun sırasında çoktan sıkışmış; olay bir öncekinden çıkmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buna ağaç kadar uzun"
   - Cümle 5: «"Yumak, buna ağaç kadar uzun bir dal lazım!" dedi Hayri abartarak.»
   - Açıklama: 'Ağaç kadar uzun' abartı bir mecazdır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Yumak, buna ağaç kadar uzun bir dal lazım!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelimedir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaç kadar uzun bir dal lazım!" dedi Hayri abartarak"
   - Cümle 5: «"Yumak, buna ağaç kadar uzun bir dal lazım!" dedi Hayri abartarak.»
   - Açıklama: 'Ağaç kadar uzun' abartı/mecazdır ve 'abartarak' soyut bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0115` birebir aynı, `@degisim: buğday -> top` (tutuyorsan), ardından `@onarim: 78a2587e01d450145fc5b71409d1b6f9501ee70e`, sonra gövde.

### Hikâye 3: tohum hayri-0116 (deneme 3 -> 4)

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
Bir sabah Hayri parkta yürürken çimenlerde farklı bir çiçek gördü. Hayri çiçeğin beyaz, tüylü tohumlarını havaya uçurmak istedi. Ama hiç rüzgar yoktu ve tohumlar yerinden kıpırdamadı. Hayri çiçeğe yavaşça üfledi. Yalnız bir tanesi uçtu ve hemen yere indi. Hayri abartıp bu kez tohumların hepsini birden uçurmak istedi. Yanaklarını şişirdi ve derin bir nefes aldı. Sonra bütün gücüyle üfledi. Tohumların hepsi birden havaya yükseldi. Hepsi yavaş yavaş gökyüzüne doğru uçtu. Hayri sevinçle ellerini çırptı. Hayri bundan sonra rüzgar yokken tohumları hep kendi nefesiyle uçurdu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıp bu kez"
   - Cümle 6: «Hayri abartıp bu kez tohumların hepsini birden uçurmak istedi.»
   - Açıklama: 'Abartmak' soyut bir kavramdır ve 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez ve burada anlamı da belirsiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp bu kez tohumların"
   - Cümle 6: «Hayri abartıp bu kez tohumların hepsini birden uçurmak istedi.»
   - Açıklama: Karttaki özellik olayları abartmaktır; burada abartma kelimesi aşırıya kaçma anlamında kullanılıyor ve özellik karttaki gibi değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartıp bu kez tohumların hepsini"
   - Cümle 6: «Hayri abartıp bu kez tohumların hepsini birden uçurmak istedi.»
   - Açıklama: Karttaki özellik olayları abartmaktır; burada abartmak fazla üflemek anlamında kullanılıyor ve karttaki gibi değil.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri sevinçle ellerini çırptı. Hayri bundan sonra"
   - Cümle 11: «Hayri sevinçle ellerini çırptı.»
   - Açıklama: Art arda iki cümle aynı adla başlıyor; ikincide ad gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0116` birebir aynı, `@degisim: buzdolabı -> tohum` (tutuyorsan), ardından `@onarim: 1979fcf19c4a5df5550c4f7ff0e756955b657355`, sonra gövde.

### Hikâye 4: tohum hayri-0118 (deneme 3 -> 4)

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
Bir sabah Hayri parkta oynarken çok acıktı. Büyük bir ağacın altına oturdu ve cebindeki cevizleri çıkardı. Ama kabuklar çok sertti ve Hayri onları elleriyle açamadı. Hayri biraz düşündü ve iki cevizi avucuna aldı. Onları birbirine sürttü ve sıkıca bastırdı. Çıt diye bir ses geldi ve bir tanesi kırıldı. İçinden minik, beyaz bir ceviz içi çıktı. Hayri onu hemen afiyetle yedi. Sonra kalan cevizleri de böyle kırıp yedi. Hayri çok sevindi, çünkü sert kabuğu kendisi açmıştı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "İçinden minik, beyaz bir ceviz içi"
   - Cümle 7: «İçinden minik, beyaz bir ceviz içi çıktı.»
   - Açıklama: 'İçinden' ve 'ceviz içi' aynı cümlede gereksiz tekrar ediyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri onu hemen afiyetle yedi"
   - Cümle 8: «Hayri onu hemen afiyetle yedi.»
   - Açıklama: 3-6 yaş için boğulma riski taşıyan cevizi çocuk tek başına kırıp yiyor ve bu taklit edilebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0118` birebir aynı, `@degisim: sos -> ceviz` (tutuyorsan), ardından `@onarim: 89c86566682540a37dede2fcaa024443bc0cbaa5`, sonra gövde.

### Hikâye 5: tohum hayri-0119 (deneme 3 -> 4)

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
Güneş çok sıcaktı ve denizden hafif bir rüzgar esiyordu. Hayri kumda sosisli ekmeğini yerken başını serinletmek istedi. Siyah şapkasını çıkarıp kuma koydu ama rüzgar onu uzağa uçurdu. Hayri bu şapkayı baklava dükkanında çalışırken takıyordu. Ekmeğini bırakıp hemen aramaya başladı. Kıyıda bir sürü siyah taş ve yosun vardı. Hayri her birine tek tek baktı ama şapkayı göremedi. Sonra şapkanın üstündeki beyaz un lekelerini hatırladı. Bu kez yalnız beyaz lekeli bir şey aradı. Büyük bir taşın arkasında onu hemen gördü. Hayri şapkayı silkeledi ve yeniden taktı. Sonra ekmeğini afiyetle bitirdi. Hayri çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "beyaz una bakıp onu buldu"
   - Cümle 0 (plan satırı): «rüzgar siyah şapkayı kıyıda bir yere uçurdu | şapkanın üstündeki beyaz una bakıp onu buldu»
   - Açıklama: Plandaki 'onu' en yakın isim olan una da şapkaya da gidebiliyor; kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0119` birebir aynı, ardından `@onarim: a1fb943c78c6f222b45a302b8a6e82a511308a04`, sonra gövde.

### Hikâye 6: tohum hayri-0122 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0122
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pelerin', fiil 'tutunmak', sıfat 'açık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: sürpriz bitmeden amca erken geldi | amcayı güldürdü ve sürprizi hızla bitirdi
@tohum: hayri-0122
@degisim: pelerin -> örtü
Bir sabah Hayri ormanda Basri Amca'ya doğum günü sürprizi hazırlıyordu. Açık bir yere örtü serdi ve üstüne çiçek koymaya başladı. Ama sürpriz bitmeden Basri Amca erken geldi. Hayri koşarak amcanın önüne geçti. "Amca, şimdi bakarsan sürpriz bin kere bozulur!" dedi Hayri. Basri Amca bu abartılı söze güldü ve gözlerini kapattı. Hayri hızla dönüp son çiçekleri de koydu. Basri Amca gözleri kapalı Hayri'nin koluna tutundu ve yürüdü. "Şimdi bak, iyi ki doğdun!" dedi Hayri. Amca çiçekleri görünce gülümsedi. "Çok güzel bir sürpriz, teşekkürler, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü sürprizini tam zamanında bitirmişti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sürpriz bitmeden Basri Amca erken geldi"
   - Cümle 3: «Ama sürpriz bitmeden Basri Amca erken geldi.»
   - Açıklama: Amcanın neden erken geldiği, yani sorunun sebebi söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sürpriz bin kere bozulur"
   - Cümle 5: «"Amca, şimdi bakarsan sürpriz bin kere bozulur!" dedi Hayri.»
   - Açıklama: 'Bin kere bozulur' abartılı bir mecaz; bir sürpriz bin kez bozulmaz.
   - Açıklama: 'Bin kere bozulur' abartılı bir mecazdır ve 'abartılı söz' soyut bir kavramdır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu abartılı söze güldü"
   - Cümle 6: «Basri Amca bu abartılı söze güldü ve gözlerini kapattı.»
   - Açıklama: 'Abartılı söz' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0122` birebir aynı, `@degisim: pelerin -> örtü` (tutuyorsan), ardından `@onarim: 7cd4660c5abe2e24b4f05f43d3df8b9cc010a8ce`, sonra gövde.

### Hikâye 7: tohum hayri-0123 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0123
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'keman', fiil 'dizmek', sıfat 'sarı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: kozalaklar uzaktı ve top onlara çarpmadı | kozalakları tepsideki baklava gibi yan yana dizdi
@tohum: hayri-0123
@degisim: keman -> kozalak
Ormandaki kamp yerinde Hayri ile Yumak sırayla oynuyordu. Hayri yere kozalakları dizdi ve sarı topu onlara yuvarladı. Ama kozalaklar birbirinden uzaktı ve top hiçbir kozalağa çarpmadı. Yumak da topu itti ama yine hiçbiri devrilmedi. Yumak kulaklarını indirdi ve yere yattı. Hayri dükkanda baklavaları tepsiye sıkı sıkı dizmeyi biliyordu. Şimdi kozalakları da öyle, yan yana dizdi. "Sıra yine sende, Yumak!" dedi Hayri. Yumak kalktı, koştu ve topa burnuyla vurdu. Top ilk kozalağa çarptı ve hepsi birden devrildi. Yumak havladı ve kuyruğunu salladı. "Aferin, Yumak, çok güzel vurdun!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Şimdi kozalakları da öyle"
   - Cümle 7: «Şimdi kozalakları da öyle, yan yana dizdi.»
   - Açıklama: Geçmiş zaman anlatımında 'Şimdi' zaman kaymasına yol açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0123` birebir aynı, `@degisim: keman -> kozalak` (tutuyorsan), ardından `@onarim: cbc31b34ed045adfe10f3a07c1acf12507d4db73`, sonra gövde.

### Hikâye 8: tohum hayri-0124 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0124
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'salatalık', fiil 'toplamak', sıfat 'çıtır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: bir dalga salatalık dolu örtüye doğru geldi | amcaya bağırdı ve salatalıkları hızla topladı
@tohum: hayri-0124
Deniz kıyısında Hayri ile Basri Amca kuma bir örtü sermişti. Örtü suya yakındı ve üstünde çıtır salatalıklar vardı. Birden örtüye doğru bir dalga geldi. Basri Amca oturuyordu ve dalgayı görmedi. "Amca, kocaman bir dalga geliyor, kalk!" diye bağırdı Hayri. Basri Amca hemen ayağa kalktı ve geri çekildi. Hayri de salatalıkları hızla topladı ve amcanın yanına koştu. Dalga yalnız örtünün ucunu ıslattı. Salatalıklar Hayri'nin kucağında hiç ıslanmadı. "Dalga küçükmüş ama iyi ki abartarak bağırdın, Hayri," dedi Basri Amca gülerek. Sonra Hayri ile Basri Amca kuru kumda salatalıkları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kocaman bir dalga geliyor, kalk!"
   - Cümle 5: «"Amca, kocaman bir dalga geliyor, kalk!" diye bağırdı Hayri.»
   - Açıklama: Üstlerine gelen kocaman dalga küçük çocuk için korkutucu bir tehlike anı kuruyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri de salatalıkları hızla topladı"
   - Cümle 7: «Hayri de salatalıkları hızla topladı ve amcanın yanına koştu.»
   - Açıklama: Dalga gelirken su kenarında kalıp yiyecek toplamak taklit edilince tehlikeli bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iyi ki abartarak bağırdın"
   - Cümle 10: «"Dalga küçükmüş ama iyi ki abartarak bağırdın, Hayri," dedi Basri Amca gülerek.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "iyi ki abartarak bağırdın"
   - Cümle 10: «"Dalga küçükmüş ama iyi ki abartarak bağırdın, Hayri," dedi Basri Amca gülerek.»
   - Açıklama: Dalga küçük çıkmışken amcanın abartılı uyarıyı övmesi olayla çelişiyor ve yanlış bir ders veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0124` birebir aynı, ardından `@onarim: 2f98f99f7749058d8a1045beb39b5bfb684b8654`, sonra gövde.

### Hikâye 9: tohum hayri-0125 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0125
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yorgan', fiil 'koşmak', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı pembe yorganına yattı ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı
@tohum: hayri-0125
Bir sabah Hayri ile Kamil deniz kıyısında yarış yapacaktı. Ama uyumayı çok seven Kamil pembe yorganını kuma serdi ve üstünde uyudu. "Kamil, kalk, yarış zamanı!" dedi Hayri. Kamil uyanmadı, yalnız yorganın üstünde döndü. Hayri arkadaşının omzuna dokundu ama Kamil gözlerini açmadı. Hayri acıkmıştı ve çantasında sıcak bir simit vardı. Hayri simidi Kamil'in burnuna doğru tuttu. Kamil gözlerini açtı ve "Bu koku ne?" diye sordu. Hayri güldü, simidi ikiye böldü ve yarısını Kamil'e verdi. İkisi simidi yedi ve kumda koşarak yarıştı. Hayri çok sevindi, çünkü Kamil sonunda uyanmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "pembe yorganına yattı"
   - Cümle 0 (plan satırı): «arkadaşı pembe yorganına yattı ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı»
   - Açıklama: Plan satırında yer eki yanlış; 'yorganının üstüne yattı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşı pembe yorganına yattı"
   - Cümle 0 (plan satırı): «arkadaşı pembe yorganına yattı ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı»
   - Açıklama: Yorgan üstüne örtülür; 'yorganına yattı' yanlış, 'yorganının üstüne yattı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0125` birebir aynı, ardından `@onarim: 892c451752dba94d2f0ff8e7d9581c419e62b60a`, sonra gövde.

### Hikâye 10: tohum hayri-0127 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0127
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fide', fiil 'koparmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga kovayı götürdü ve kale yarım kaldı | boş baklava kutusunu kova yaptı ve sırayla doldurdular
@tohum: hayri-0127
@degisim: fide -> kova
Deniz kıyısında Hayri ile Akın sırayla kumdan kale yapıyordu. Hayri kovayı dolduruyor, Akın ters çeviriyordu. Birden bir dalga geldi ve kovayı alıp uzağa götürdü. Akın üzüldü, çünkü kale daha yarımdı. Hayri çantasına baktı ve dükkandan getirdiği boş baklava kutusunu buldu. Az önce kutudaki baklavaları birlikte yemişlerdi. Hayri kutunun kapağını kopardı ve kutuyu kova gibi kullandı. "Şimdi sıra sende, Akın," dedi Hayri. Akın kutuyu kumla doldurdu ve ters çevirdi. Kumdan kare bir kule çıktı. Akın kuleyi çok beğendi ve memnun oldu. Hayri ile Akın sırayla kuleler yaptı ve kaleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kuleyi çok beğendi ve memnun oldu"
   - Cümle 11: «Akın kuleyi çok beğendi ve memnun oldu.»
   - Açıklama: 'Çok beğendi' ile 'memnun oldu' aynı şeyi gereksiz yere tekrarlıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çok beğendi ve memnun oldu"
   - Cümle 11: «Akın kuleyi çok beğendi ve memnun oldu.»
   - Açıklama: 'Memnun oldu' aynı duyguyu gereksizce tekrar ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0127` birebir aynı, `@degisim: fide -> kova` (tutuyorsan), ardından `@onarim: cd162041423287380965e93f213f7135868ffce7`, sonra gövde.

### Hikâye 11: tohum hayri-0128 (deneme 3 -> 4)

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
Deniz kıyısında Hayri kuma basarak bir resim yapıyordu. Şapkalı bir güneş yapmak istiyordu. Ama adımları küçüktü ve güneş kumda hiç belli olmadı. Hayri her şeyi hep abartarak anlatmayı seviyordu. Bu kez güneşi de öyle kocaman yapmaya karar verdi. Uzun adımlar attı ve kuma sertçe bastı. Güneşin ışıklarını iki ayağıyla zıplayarak yaptı. Sonra güneşin üstüne büyük adımlarla bir şapka yaptı. Geri çekildi ve resmine baktı. Resim artık çok büyük ve belliydi. Hayri çok güldü ve sevindi, çünkü şapkalı güneş uzaktan bile görünüyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "her şeyi hep abartarak anlatmayı seviyordu"
   - Cümle 4: «Hayri her şeyi hep abartarak anlatmayı seviyordu.»
   - Açıklama: 'Abartarak anlatmak' 3 yaşındaki çocuk için soyut bir kavram.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri her şeyi hep abartarak anlatmayı seviyordu"
   - Cümle 4: «Hayri her şeyi hep abartarak anlatmayı seviyordu.»
   - Açıklama: Anlatırken abartma huyu kumdaki resmin küçük kalması sorunuyla bağlantısız ve çözümü sebepsizce getiriyor.
   - Açıklama: Abartarak anlatma özelliği resmi büyük yapma kararına mantıklı biçimde bağlanmıyor; çözüm bu ilgisiz ayrıntıyla getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0128` birebir aynı, `@degisim: avokado -> güneş` (tutuyorsan), ardından `@onarim: 0bcffd21aa78ee28e32f9542e4201c37a2baf909`, sonra gövde.

### Hikâye 12: tohum hayri-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0129
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: kaybolan eşya
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabela', fiil 'işaretlemek', sıfat 'güzel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: rüzgar dükkanın tabelasını uçurdu ve tabela kayboldu | yaprakların toplandığı köşeye bakıp tabelayı buldu
@tohum: hayri-0129
@degisim: işaretlemek -> asmak
Mahalledeki evlerin önünde sert bir rüzgar esiyordu. Hayri'nin çalıştığı dükkan da bu evlerin arasındaydı. Dükkanın güzel tabelası kaybolmuştu. Rüzgar tabelayı kapıdan düşürmüş ve alıp götürmüştü. Mert de Hayri'ye yardım etmek için geldi. İkisi evlerin önüne baktı ama tabelayı bulamadı. Hayri dükkanın önünü süpürürken yaprakları hep köşede görmüştü. "Rüzgar yaprakları o köşeye götürür, Mert," dedi Hayri. İkisi köşeye koştu. Tabela yaprakların arasında, duvarın yanında duruyordu. Hayri tabelayı kaldırdı ve üstündeki yaprakları silkti. Sonra ikisi tabelayı dükkanın kapısına sıkıca astı. Hayri, Mert'e bir dilim baklava verdi ve ikisi mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri'nin çalıştığı dükkan da bu evlerin arasındaydı"
   - Cümle 2: «Hayri'nin çalıştığı dükkan da bu evlerin arasındaydı.»
   - Açıklama: Başlıktaki yer ev ama hikaye evde değil, dükkanın ve evlerin önünde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye dükkanın önünde ve sokakta geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0129` birebir aynı, `@degisim: işaretlemek -> asmak` (tutuyorsan), ardından `@onarim: 0b076b90a27e1ed4b92b032708498922888a2bd6`, sonra gövde.
