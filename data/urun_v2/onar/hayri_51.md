# Editör görevi (onarım): Hayri, onarım partisi 51

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar51.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar51.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0098 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0098
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabak', fiil 'yıkamak', sıfat 'düz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: sürpriz için aldığı baklavalar kutuda dağılmıştı | baklavaları dükkandaki gibi düz tabağa dizdi
@tohum: hayri-0098
Bir sabah Hayri evde Mert için bir sürpriz hazırlıyordu. O gün Mert'in doğum günüydü. Ama dükkandan getirdiği baklavalar kutuda dağılmıştı, çünkü yolda kutu çok sallanmıştı. Hayri kutuya baktı ve biraz düşündü. Dükkanda baklavaları hep tepsiye diziyordu. Masadaki büyük ve düz tabağı alıp yıkadı. Sonra baklavaları tabağa sıra sıra dizdi. Her sırada dört baklava vardı. Az sonra Mert eve geldi. "Doğum günün kutlu olsun, Mert!" dedi Hayri. Mert tabağı görünce çok sevindi. "Tıpkı dükkandaki gibi olmuş, teşekkürler, Hayri!" dedi Mert.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dükkanda baklavaları hep tepsiye diziyordu"
   - Cümle 5: «Dükkanda baklavaları hep tepsiye diziyordu.»
   - Açıklama: Baklavaları dükkanda kimin dizdiği belli değil; özne Hayri gibi okunuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Her sırada dört baklava vardı"
   - Cümle 8: «Her sırada dört baklava vardı.»
   - Açıklama: Sıralardaki baklava sayısı hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0098` birebir aynı, ardından `@onarim: 90c1b2dbe6990292133f1d8dd13f9fefab25cbd0`, sonra gövde.

### Hikâye 2: tohum hayri-0099 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0099
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'telefon', fiil 'kurmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kütüğün üstü düz değildi ve elmalar çalıya düştü | elmaları bulup kağıt tabağın içine koydu
@tohum: hayri-0099
@degisim: telefon -> tabak
Bir sabah Hayri kamp yerinde evcilik oyunu oynuyordu. Çok acıkmıştı ve kütüğün üstüne düzenli bir sofra kurdu. Ama kütüğün üstü düz değildi ve iki elma kayarak çalıya düştü. Hayri çalının dibine eğildi ve iki elmayı da buldu. Elmalar yine düşmesin diye çantasından bir kağıt tabak aldı. Elmaları tabağın içine koydu ve tabağı kütüğe bıraktı. Bu kez elmalar hiç kıpırdamadı. Hayri kütüğe baktı ve gülümsedi. Sonra kütüğün yanına oturdu ve elmalarını afiyetle yedi. Hayri çok sevindi, çünkü elmaları bulmuş ve sofrayı yeniden kurmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "iki elma kayarak çalıya düştü"
   - Cümle 3: «Ama kütüğün üstü düz değildi ve iki elma kayarak çalıya düştü.»
   - Açıklama: Elmaların çalıya düşüp hemen bulunması önemsiz bir olay; sorun çocuğun önemseyeceği bir sorun olarak kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0099` birebir aynı, `@degisim: telefon -> tabak` (tutuyorsan), ardından `@onarim: 927e4c474997fc1391a242dd0441af90dc1df37e`, sonra gövde.

### Hikâye 3: tohum hayri-0101 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0101
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'fermuar', fiil 'yırtılmak', sıfat 'yumuşacık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: kağıt torba yırtıldı ve kozalaklar yere döküldü | amcadan yardım istedi ve kozalakları çantaya koydu
@tohum: hayri-0101
Hayri parkta çam ağacının altında bir sürü kozalak fark etti. Kozalakları kağıt bir torbada topladı. Ama torba ağırlaştı ve yırtıldı, kozalaklar yere döküldü. Basri Amca yakındaki bankta oturuyordu. "Basri Amca, bin tane kozalak dağıldı, yardım eder misin?" diye abarttı Hayri. Basri Amca güldü ve Hayri'nin yanına geldi. "Bin tane değil ama çok kozalak var," dedi Basri Amca. Sonra Hayri'ye yumuşacık bir kumaş çanta verdi. Çantanın sağlam bir fermuarı vardı. Hayri kozalakları tek tek çantaya koydu. Sonra fermuarı dikkatle kapattı. "Teşekkürler, Basri Amca," dedi Hayri. Hayri çok sevindi, çünkü bütün kozalaklarını yeniden toplamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yardım eder misin?" diye abarttı Hayri"
   - Cümle 5: «"Basri Amca, bin tane kozalak dağıldı, yardım eder misin?" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' soyut bir kavram ve konuşma fiili olarak 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 5: «"Basri Amca, bin tane kozalak dağıldı, yardım eder misin?" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime ve konuşma fiili olarak yerinde değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0101` birebir aynı, ardından `@onarim: 72cda9f1a959626fc35585389c213eb69ecba4d5`, sonra gövde.

### Hikâye 4: tohum hayri-0102 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0102
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'anahtar', fiil 'güneşlenmek', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: koşarken kum sıçradı ve anahtar kayboldu | özür diledi ve anahtarı kumun altında buldu
@tohum: hayri-0102
Deniz kıyısında Kamil bir havlunun üstünde güneşleniyordu. Hayri kumda koşarken ayağıyla havluya kum sıçrattı. Havlunun üstündeki bakkalın anahtarı kumun altında kayboldu. "Anahtar olmadan bakkalı açamam!" dedi Kamil. Hayri durdu ve Kamil'in yanına geldi. "Özür dilerim, Kamil, anahtarı artık hiç bulamayız!" diye abarttı Hayri. Kamil güldü ve havlunun yanını gösterdi. Sonra Hayri kumu parmaklarıyla yavaş yavaş eşeledi. Kısa bir süre sonra parlak anahtarı buldu. Anahtarı silkeledi ve Kamil'e verdi. "Teşekkürler, Hayri, seni affettim!" dedi Kamil.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Havlunun üstündeki bakkalın anahtarı"
   - Cümle 3: «Havlunun üstündeki bakkalın anahtarı kumun altında kayboldu.»
   - Açıklama: Bakkalın kim olduğu tanıtılmadan belirli gibi anılıyor, anahtarın kime ait olduğu belirsiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "diye abarttı Hayri"
   - Cümle 6: «"Özür dilerim, Kamil, anahtarı artık hiç bulamayız!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' konuşma fiili olarak kullanılamaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 6: «"Özür dilerim, Kamil, anahtarı artık hiç bulamayız!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' soyut bir kavram ve konuşma fiili olarak 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0102` birebir aynı, ardından `@onarim: c9a7867bd1b304d390fabfe22c7148e48936bb32`, sonra gövde.

### Hikâye 5: tohum hayri-0103 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0103
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'havuç', fiil 'taşınmak', sıfat 'keyifli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: hızlı yürüdü ve havuç yere düştü | çok yavaş ve komik adımlarla yürüdü
@tohum: hayri-0103
@degisim: taşınmak -> taşımak
Hayri kamp yerinde yeni bir oyun deniyordu. Kaşıkta küçük bir havucu ağaçtan masaya kadar taşıyacaktı. Ama Hayri hızlı yürüdü ve havuç kaşıktan yere düştü. Hayri havucu yerden aldı ve tekrar denedi. Havuç yine düştü. Bu kez Hayri abarttı ve çok yavaş, komik adımlarla yürüdü. Her adımda bir ayağını havaya kaldırdı ve biraz bekledi. Kaşığı da iki eliyle sıkıca tuttu. Havuç kaşıkta hiç kıpırdamadı. Sonunda Hayri masaya vardı ve havucu tabağa bıraktı. Sonra sevinçle zıpladı ve bu keyifli oyunu bir kez daha oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu kez Hayri abarttı"
   - Cümle 6: «Bu kez Hayri abarttı ve çok yavaş, komik adımlarla yürüdü.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez Hayri abarttı"
   - Cümle 6: «Bu kez Hayri abarttı ve çok yavaş, komik adımlarla yürüdü.»
   - Açıklama: Kart özelliği olayları abartmak; burada abartma yalnız yürüyüş biçimi, karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0103` birebir aynı, `@degisim: taşınmak -> taşımak` (tutuyorsan), ardından `@onarim: 8895062fedb9581b27d46effedb1992723bc0d62`, sonra gövde.

### Hikâye 6: tohum hayri-0108 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0108
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'boncuk', fiil 'çiğnemek', sıfat 'dağınık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: ipin ucu dağınıktı ve boncuklar ipe geçmiyordu | arkadaşından yardım istedi ve ipin ucunu ıslattı
@tohum: hayri-0108
@degisim: çiğnemek -> ıslatmak
Deniz kıyısında Hayri renkli boncuklarla bir bileklik yapıyordu. Ama ipin ucu dağınıktı, bu yüzden boncuklar ipe geçmiyordu. Hayri üç kez denedi ama olmadı. Akın biraz uzakta kumda oynuyordu. "Akın, yüz kez denedim, bana yardım et!" diye abarttı Hayri. Akın güldü ve hemen gelip ipe baktı. "İpin ucunu suyla ıslatmalısın," dedi Akın. Hayri su kenarında ipin ucunu ıslattı ve parmaklarıyla yuvarladı. İpin ucu incecik oldu ve boncuklar ipe kolayca geçti. Hayri bütün boncukları ipe dizdi ve bilekliği taktı. "Teşekkürler, Akın, bileklik çok güzel oldu!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 5: «"Akın, yüz kez denedim, bana yardım et!" diye abarttı Hayri.»
   - Açıklama: 'Yüz kez denedim' abartması ve 'abarttı' fiili soyut, 3 yaşındaki çocuğun bilmeyeceği bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0108` birebir aynı, `@degisim: çiğnemek -> ıslatmak` (tutuyorsan), ardından `@onarim: acce425b6a7356ed5e84696507107c14b61cdfce`, sonra gövde.

### Hikâye 7: tohum hayri-0109 (deneme 4 -> 5)

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
Bir sabah Hayri kamp yerinde ilk kez bloklarla kule yapmayı denedi. Tahta blokları bir kütüğün üstüne üst üste dizdi. Ama en altta yalnız bir blok vardı ve kule sallanıp yıkıldı. Hayri yere düşen bloklara baktı ve biraz düşündü. Sonra blokların hepsini yerden aldı. Hayri abarttı ve en alta yan yana tam altı blok koydu. Üstüne blokları tek tek dikkatle yerleştirdi. En üste de kıpkırmızı bir blok koydu. Kule bu kez hiç sallanmadı ve dimdik durdu. Hayri bundan sonra kulenin en altına hep çok blok koydu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve en"
   - Cümle 6: «Hayri abarttı ve en alta yan yana tam altı blok koydu.»
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez ve burada anlamı da uymuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve en alta"
   - Cümle 6: «Hayri abarttı ve en alta yan yana tam altı blok koydu.»
   - Açıklama: Karttaki özellik olayları abartmak (anlatımda büyütmek); burada abartma fazla blok koymak anlamında kartın özellik tanımından farklı kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "En üste de kıpkırmızı bir blok koydu"
   - Cümle 8: «En üste de kıpkırmızı bir blok koydu.»
   - Açıklama: Kırmızı blok olayda işlevi olmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0109` birebir aynı, ardından `@onarim: 4be6cd328cc2ca36ef1fad26c06e9024ade2add4`, sonra gövde.

### Hikâye 8: tohum hayri-0112 (deneme 4 -> 5)

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
Hayri, elinde bir kutuyla Akın'a doğru koşuyordu. Kutuda çalıştığı dükkandan getirdiği kremalı baklavalar vardı. Hayri koşarken Akın'ın kumdan kalesini görmedi ve ayağıyla yıktı. Akın kalesine bakıp çok üzüldü. Hayri hemen durdu ve yanına oturdu. "Özür dilerim, Akın, kaleni görmedim," dedi Hayri. Sonra Akın'ın kovasıyla deniz suyu getirdi. Su kuma aktı ve kumu ıslattı. İkisi ıslak kumdan kaleyi birlikte yeniden yaptı. Bu kez eskisinden de büyük oldu. "Çok güzel oldu, Hayri!" dedi Akın. Sonra ikisi baklavaları birlikte yedi. Hayri çok sevindi, çünkü Akın yine gülüyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ikisi baklavaları birlikte yedi"
   - Cümle 12: «Sonra ikisi baklavaları birlikte yedi.»
   - Açıklama: Tohumdaki baklava özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak başta ve sonda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0112` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 7b28889b33df881c00ab7ebbe3cc0c21cc49fad7`, sonra gövde.

### Hikâye 9: tohum hayri-0115 (deneme 4 -> 5)

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
Deniz kıyısında Yumak, Hayri'yi havlayarak karşıladı. Sonra ikisi top oynadı ve Yumak'ın topu iki büyük taşın arasına sıkıştı. Yumak burnuyla topu itti ama çıkaramadı. Hayri'nin eli de taşların arasına sığmadı. "Üzülme, Yumak, sana dünyanın en uzun dalını bulurum!" diye abarttı Hayri. Sonra Hayri kumda uzun bir dal buldu. Dalı taşların arasına soktu ve topu yavaşça itti. Top taşların arasından çıktı ve kuma düştü. Yumak kabarık kuyruğunu sallayarak topa koştu. Yumak havladı ve topu Hayri'ye getirdi. Hayri bundan sonra Yumak'la taşlardan uzakta top oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dünyanın en uzun dalını bulurum!" diye abarttı Hayri"
   - Cümle 5: «"Üzülme, Yumak, sana dünyanın en uzun dalını bulurum!" diye abarttı Hayri.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 'dünyanın en uzun dalı' abartma kalıbı 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bulurum!" diye abarttı Hayri"
   - Cümle 5: «"Üzülme, Yumak, sana dünyanın en uzun dalını bulurum!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime ve konuşma fiili olarak uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0115` birebir aynı, `@degisim: buğday -> top` (tutuyorsan), ardından `@onarim: f32977badc72323368e80aa43e0aab2f5e6044ec`, sonra gövde.

### Hikâye 10: tohum hayri-0119 (deneme 4 -> 5)

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
@plan: rüzgar siyah şapkayı kıyıda bir yere uçurdu | üstündeki beyaz una bakarak şapkayı buldu
@tohum: hayri-0119
Güneş çok sıcaktı ve denizden hafif bir rüzgar esiyordu. Hayri kumda sosisli ekmeğini yerken başını serinletmek istedi. Siyah şapkasını çıkarıp kuma koydu ama rüzgar onu uzağa uçurdu. Hayri bu şapkayı baklava dükkanında çalışırken takıyordu. Ekmeğini bırakıp hemen aramaya başladı. Kıyıda bir sürü siyah taş ve yosun vardı. Hayri her birine tek tek baktı ama şapkayı göremedi. Sonra şapkanın üstündeki beyaz un lekelerini hatırladı. Bu kez yalnız beyaz lekeli bir şey aradı. Büyük bir taşın arkasında onu hemen gördü. Hayri şapkayı silkeledi ve yeniden taktı. Sonra ekmeğini afiyetle bitirdi. Hayri çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Siyah şapkasını çıkarıp kuma koydu"
   - Cümle 3: «Siyah şapkasını çıkarıp kuma koydu ama rüzgar onu uzağa uçurdu.»
   - Açıklama: Güneş çok sıcakken başı serinletmek için şapkayı çıkarmak çocuğun taklit edebileceği güvensiz bir davranış olarak gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0119` birebir aynı, ardından `@onarim: 2d12063df9102f67ede782b200d7c4818a3bd455`, sonra gövde.

### Hikâye 11: tohum hayri-0122 (deneme 4 -> 5)

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
Bir sabah Hayri ormanda Basri Amca'ya doğum günü sürprizi hazırlıyordu. Açık bir yere örtü serdi ve üstüne çiçek koymaya başladı. Ama Basri Amca odunları çabuk topladı ve sürpriz bitmeden geri geldi. Hayri koşarak amcanın önüne geçti. "Amca, şimdi bakarsan dünyanın en güzel sürprizi bozulur!" diye abarttı Hayri. Basri Amca bu söze güldü ve gözlerini kapattı. Hayri hızla dönüp son çiçekleri de koydu. Basri Amca gözleri kapalı Hayri'nin koluna tutundu ve yürüdü. "Şimdi bak, iyi ki doğdun!" dedi Hayri. Amca çiçekleri görünce gülümsedi. "Çok güzel bir sürpriz, teşekkürler, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü sürprizini tam zamanında bitirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 5: «"Amca, şimdi bakarsan dünyanın en güzel sürprizi bozulur!" diye abarttı Hayri.»
   - Açıklama: 'abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0122` birebir aynı, `@degisim: pelerin -> örtü` (tutuyorsan), ardından `@onarim: 9ea4410d90f958ffcb322032fb6fff42e751ea3e`, sonra gövde.

### Hikâye 12: tohum hayri-0125 (deneme 4 -> 5)

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
@plan: arkadaşı pembe yorganın üstünde uyudu ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı
@tohum: hayri-0125
Bir sabah Hayri ile Kamil deniz kıyısında yarış yapacaktı. Ama uyumayı çok seven Kamil pembe yorganını kuma serdi ve üstünde uyudu. "Kamil, kalk, yarış zamanı!" dedi Hayri. Kamil uyanmadı, yalnız yorganın üstünde döndü. Hayri arkadaşının omzuna dokundu ama Kamil gözlerini açmadı. Hayri acıkmıştı ve çantasında sıcak bir simit vardı. Hayri simidi Kamil'in burnuna doğru tuttu. Kamil gözlerini açtı ve "Bu koku ne?" diye sordu. Hayri güldü, simidi ikiye böldü ve yarısını Kamil'e verdi. İkisi simidi yedi ve kumda koşarak yarıştı. Hayri çok sevindi, çünkü Kamil sonunda uyanmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri acıkmıştı ve çantasında sıcak bir simit vardı"
   - Cümle 6: «Hayri acıkmıştı ve çantasında sıcak bir simit vardı.»
   - Açıklama: Çözümü getiren sıcak simit tam gerektiği anda sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0125` birebir aynı, ardından `@onarim: b304c1ce47316b4245a44a31d2b9fb38568ac4ca`, sonra gövde.
