# Editör görevi (onarım): Hayri, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0110 (deneme 1 -> 2)

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
Bir sabah Hayri ile Mert kamp yerinde koşu yarışı yaptı. Ödül, dala asılı ışıltılı bir oyuncak madalyaydı. Hayri kazandı, Mert ise kaybettiği için çok üzüldü. Hayri arkadaşını sevindirmek istedi. Mert'in sabah kurduğu çadıra baktı. Dimdik ve düzgün duruyordu. Hayri abartarak bunun dünyadaki en güzel çadır olduğunu söyledi. Mert buna çok güldü. Hayri madalyayı daldan alıp Mert'in boynuna taktı. İki arkadaş bir kütüğe oturup uzun uzun şakalaştı. Hayri çok mutluydu, çünkü Mert yine gülüyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bunun dünyadaki"
   - Cümle 7: «Hayri abartarak bunun dünyadaki en güzel çadır olduğunu söyledi.»
   - Açıklama: 'abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0110` birebir aynı, ardından `@onarim: b8b096ad7adeedcb0f30ebcf31cd41d350ecfce5`, sonra gövde.

### Hikâye 2: tohum hayri-0111 (deneme 1 -> 2)

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
@plan: kozalaklar bozuk çantadan hep yere düştü | dükkandan getirdiği boş tepsiyle kozalakları taşıdı
@tohum: hayri-0111
@degisim: palmiye -> kozalak
Bir sabah Hayri kamp yerinde çam ağaçlarının altında yürüyordu. Yerde bir sürü büyük kozalak fark etti. Onlarla çadırının kapısını süslemek istedi. Ama çantasının fermuarı bozuktu ve topladığı her şey yere düşüyordu. Hayri biraz düşündü. Kampa, çalıştığı baklava dükkanından bir tepsi getirmişti. Tepsi kahvaltıdan sonra boş kalmıştı. Hayri onu kullanmaya karar verdi. Kozalakları tek tek üstüne dizdi. Dükkanda her gün tepsi taşıdığı için onu hiç sallamadan götürdü. Yolda hiçbiri kaymadı. Sonra hepsini kapının iki yanına sıra sıra koydu. Böylece çadırı çok güzel oldu ve Hayri mutlu mutlu gülümsedi.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama çantasının fermuarı bozuktu"
   - Cümle 4: «Ama çantasının fermuarı bozuktu ve topladığı her şey yere düşüyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kampa, çalıştığı baklava dükkanından bir tepsi getirmişti"
   - Cümle 6: «Kampa, çalıştığı baklava dükkanından bir tepsi getirmişti.»
   - Açıklama: Çözümü getiren tepsi önceden kurulmadan tam gerektiği anda ortaya çıkarılıyor.
   - Açıklama: Baklava tepsisinin kampa getirilmiş olması önceden kurulmadan tam çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0111` birebir aynı, `@degisim: palmiye -> kozalak` (tutuyorsan), ardından `@onarim: 1bb914aa31a044a0e5d3e04fe05247c3bfd795df`, sonra gövde.

### Hikâye 3: tohum hayri-0112 (deneme 1 -> 2)

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
@plan: koşarken arkadaşının kumdan kalesini yıktı | özür dileyip baklava verdi ve kaleyi yeniden yaptılar
@tohum: hayri-0112
@degisim: salıncak -> kova
Hayri, elinde bir kutuyla Akın'a doğru koşuyordu. Kutuda çalıştığı dükkandan getirdiği kremalı baklavalar vardı. Hayri koşarken Akın'ın kumdan kalesini görmedi ve ayağıyla yıktı. Akın kalesine bakıp çok üzüldü. Hayri hemen durdu ve yanına oturdu. "Özür dilerim, Akın, seni görmedim," dedi Hayri. Sonra kutuyu açıp ona bir tane uzattı. "Bunu senin için getirdim," dedi Hayri. Akın gülümsedi ve bir ısırık aldı. "Kreması güneşte akıyor, çabuk yiyelim!" dedi Akın. İkisi gülerek yedi. Sonra kovayla kaleyi birlikte yeniden yaptılar. Bu kez eskisinden de büyük oldu. Hayri çok rahatladı, çünkü Akın onu affetmişti.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Özür dilerim, Akın, seni görmedim"
   - Cümle 6: «"Özür dilerim, Akın, seni görmedim," dedi Hayri.»
   - Açıklama: Hayri kaleyi görmemişti ama Akın'ı görmediğini söylüyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kutuyu açıp ona bir tane uzattı"
   - Cümle 7: «Sonra kutuyu açıp ona bir tane uzattı.»
   - Açıklama: Çözüm özür, baklava ve kaleyi yeniden yapma diye üç adıma yayılıyor ve baklava sebebe yönelmiyor.
   - Açıklama: Baklava vermek yıkılan kaleye yönelmiyor ve çözüm özür, baklava, yeniden yapma diye üç adıma çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kreması güneşte akıyor, çabuk yiyelim"
   - Cümle 10: «"Kreması güneşte akıyor, çabuk yiyelim!" dedi Akın.»
   - Açıklama: Kremanın akması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Kremanın akması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü Akın onu affetmişti"
   - Cümle 14: «Hayri çok rahatladı, çünkü Akın onu affetmişti.»
   - Açıklama: 'Affetmek' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0112` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: a086e3f7cbdaa9d910729e70ea9d4c29f3630c5a`, sonra gövde.

### Hikâye 4: tohum hayri-0113 (deneme 1 -> 2)

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
@plan: ikisi ipi aynı anda çekince uçurtma düştü | her baklavada sırayı değiştirmeyi önerdi
@tohum: hayri-0113
@degisim: çekmece -> uçurtma
Deniz kıyısında güzel bir rüzgar esiyordu. Hayri, Basri Amca'nın yepyeni uçurtmasına bakıyordu. Hayri de onunla oynamak istedi ve ipe uzandı. İkisi ipi aynı anda çekince uçurtma kuma düştü. Basri Amca biraz kızdı. Hayri'nin çantasında, çalıştığı dükkandan getirdiği bir kutu baklava vardı. Kutuyu açınca tatlı bir koku kumsala yayıldı. "Amca, sırayla oynayalım, ben baklavamı yerken sen tut!" dedi Hayri. Basri Amca güldü ve kabul etti. Önce o uçurtmayı gökyüzüne yükseltti. Hayri tatlısını bitirince Basri Amca ipi ona uzattı. "Sıra sende, Hayri," dedi Basri Amca. İkisi böyle sırayla oynayıp kumsalda çok eğlendi.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "her baklavada sırayı değiştirmeyi"
   - Cümle 0 (plan satırı): «ikisi ipi aynı anda çekince uçurtma düştü | her baklavada sırayı değiştirmeyi önerdi»
   - Açıklama: 'Her baklavada sırayı değiştirmek' anlamca uygun değil; baklava sıra değiştirme birimi olamaz.
   - Açıklama: 'Her baklavada' anlamca uygun değil; hikayede her baklava yenişinde sıra değişmiyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "her baklavada sırayı değiştirmeyi önerdi"
   - Cümle 0 (plan satırı): «ikisi ipi aynı anda çekince uçurtma düştü | her baklavada sırayı değiştirmeyi önerdi»
   - Açıklama: Gövdede sıra yalnız bir kez, baklava bitince değişiyor; her baklavada değişmiyor.
   - Açıklama: Gövdede sıra her baklavada değişmiyor; Hayri tatlısını bitirince bir kez değişiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı dükkandan getirdiği bir kutu baklava"
   - Cümle 6: «Hayri'nin çantasında, çalıştığı dükkandan getirdiği bir kutu baklava vardı.»
   - Açıklama: Baklava kutusu sebepsiz beliriyor ve çözümü dışarıdan getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutuyu açınca tatlı bir koku kumsala yayıldı"
   - Cümle 7: «Kutuyu açınca tatlı bir koku kumsala yayıldı.»
   - Açıklama: Kokunun yayılması kurulup hiçbir işe yaramayan işlevsiz bir ayrıntı.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben baklavamı yerken sen tut"
   - Cümle 8: «"Amca, sırayla oynayalım, ben baklavamı yerken sen tut!" dedi Hayri.»
   - Açıklama: Güvenli özellik kullanımı satırı yemek sevgisini paylaşmak, beklemek ya da hazırlamak olarak ister; burada Hayri baklavayı paylaşmadan tek başına yiyor.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Önce o uçurtmayı gökyüzüne"
   - Cümle 10: «Önce o uçurtmayı gökyüzüne yükseltti.»
   - Açıklama: 'o' zamirinin Basri Amca'yı mı yoksa uçurtmayı mı gösterdiği belli değil.
   - Açıklama: 'O' zamirinin Basri Amca'yı mı gösterdiği yoksa işaret sıfatı mı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0113` birebir aynı, `@degisim: çekmece -> uçurtma` (tutuyorsan), ardından `@onarim: fc5872d78b8fd3ce3c2883735946f66512dcb9bb`, sonra gövde.

### Hikâye 5: tohum hayri-0114 (deneme 1 -> 2)

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
Bir öğle vakti Hayri ile Kamil bahçede resim yapıyordu. Resimlerini çitin üstünde sergilemek istiyorlardı. Ama Kamil'in tek kalemi kırıldı ve kağıdı boş kaldı. Hayri'nin kutusunda bir sürü renkli kalem vardı. Hayri bunların yarısını Kamil'e uzattı. Kamil, Hayri'ye kalem kalmayacak diye almak istemedi. Hayri abartarak kutuda bin tane kalem olduğunu söyledi. Kamil buna çok güldü ve onları aldı. İkisi birlikte oturdu. Kamil kocaman bir kitap, Hayri de bir tabak köfte çizdi. Sonra iki kağıdı çite yan yana astılar. Hayri bundan sonra kalemlerini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Kamil bahçede resim yapıyordu"
   - Cümle 1: «Bir öğle vakti Hayri ile Kamil bahçede resim yapıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çitin üstünde sergilemek istiyorlardı"
   - Cümle 2: «Resimlerini çitin üstünde sergilemek istiyorlardı.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Kamil'in tek kalemi kırıldı"
   - Cümle 3: «Ama Kamil'in tek kalemi kırıldı ve kağıdı boş kaldı.»
   - Açıklama: Kalemin neden kırıldığı söylenmiyor; sorunun sebebi yok.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kutuda"
   - Cümle 7: «Hayri abartarak kutuda bin tane kalem olduğunu söyledi.»
   - Açıklama: 'Abartarak' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Abartarak' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0114` birebir aynı, `@degisim: bornoz -> kalem` (tutuyorsan), ardından `@onarim: 6ef6600a45dd1c99a196bcb622e1bb4d45137c9b`, sonra gövde.

### Hikâye 6: tohum hayri-0115 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar köpeğin topunu suya doğru yuvarladı | hemen koşup topu kumda yakaladı
@tohum: hayri-0115
@degisim: buğday -> top
Deniz kıyısında Hayri, Yumak'la top oynuyordu. Top çok hafifti. Birden rüzgar esti ve Yumak'ın topunu suya doğru yuvarladı. Yumak topa yetişemedi ve telaşla havladı. Hayri abartarak "Top denizi geçip uzak ülkelere gidecek!" diye bağırdı. Bu yüzden hiç beklemeden çok hızlı koştu. Topu suya girmeden hemen önce ıslak kumda yakaladı. Yumak kabarık kuyruğunu sallayarak geldi ve Hayri'yi karşıladı. "Al bakalım, Yumak, topun kurtuldu," dedi Hayri. Yumak sevinçle havladı ve topu ağzına aldı. Hayri bundan sonra rüzgarlı havalarda Yumak'la hep sudan uzakta oynadı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve Yumak'ın topunu suya doğru yuvarladı"
   - Cümle 3: «Birden rüzgar esti ve Yumak'ın topunu suya doğru yuvarladı.»
   - Açıklama: Rüzgarın topu yuvarlaması ve koşup yakalamak, örnekteki 'dağıttı, topladı, bitti' gibi önemsiz bir olay.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak "Top denizi"
   - Cümle 5: «Hayri abartarak "Top denizi geçip uzak ülkelere gidecek!" diye bağırdı.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 'uzak ülkelere gidecek' abartısı küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak "Top"
   - Cümle 5: «Hayri abartarak "Top denizi geçip uzak ülkelere gidecek!" diye bağırdı.»
   - Açıklama: 'Abartarak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "hiç beklemeden çok hızlı koştu"
   - Cümle 6: «Bu yüzden hiç beklemeden çok hızlı koştu.»
   - Açıklama: Hayri suya doğru yuvarlanan topun peşinden denize doğru koşuyor; çocuk için taklit edilince tehlikeli.
   - Açıklama: Çocuk rüzgarda kaçan topun ardından suya doğru hızla koşmayı taklit edebilir.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu yüzden hiç beklemeden"
   - Cümle 6: «Bu yüzden hiç beklemeden çok hızlı koştu.»
   - Açıklama: 'Bu yüzden' Hayri'nin abartılı sözünü gösteriyor gibi; koşmanın nedeni belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0115` birebir aynı, `@degisim: buğday -> top` (tutuyorsan), ardından `@onarim: 8ae467fd3b1fe67d4ea082572cb8c71ab11b8231`, sonra gövde.

### Hikâye 7: tohum hayri-0116 (deneme 1 -> 2)

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
@plan: rüzgar yoktu ve tohumlar çiçekten uçmadı | kocaman bir nefes alıp güçlü üfledi
@tohum: hayri-0116
@degisim: buzdolabı -> tohum
Bir sabah Hayri parkta yürürken çimenlerde farklı bir çiçek fark etti. Çiçek beyaz ve top gibi yuvarlaktı. Hayri onun tüylü tohumlarını havaya uçurmak istedi. Ama hiç rüzgar yoktu ve tohumlar yerinden kıpırdamadı. Hayri çiçeğe yavaşça üfledi. Yalnız bir tanesi uçtu ve hemen yere indi. Bu kez Hayri üflemeyi abarttı. Yanaklarını kocaman şişirdi ve derin bir nefes aldı. Sonra bütün gücüyle üfledi. Bütün tohumlar birden havaya yükseldi. Minik şemsiyeler gibi göğe doğru süzüldüler. Hayri bundan sonra rüzgar yokken tohumlara hep güçlü üfledi.
```

**Hakem bulguları (6):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama hiç rüzgar yoktu ve tohumlar yerinden kıpırdamadı.»
   - Açıklama: Sorun (rüzgar olmadığı için tohumların uçmaması) ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama hiç rüzgar yoktu"
   - Cümle 4: «Ama hiç rüzgar yoktu ve tohumlar yerinden kıpırdamadı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri üflemeyi abarttı"
   - Cümle 7: «Bu kez Hayri üflemeyi abarttı.»
   - Açıklama: 'Abartmak' olumsuz bir anlam taşır ve burada güçlü üflemek anlamında yanlış kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri üflemeyi abarttı"
   - Cümle 7: «Bu kez Hayri üflemeyi abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez Hayri üflemeyi abarttı"
   - Cümle 7: «Bu kez Hayri üflemeyi abarttı.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartma güçlü üflemek olarak kullanılıyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Minik şemsiyeler gibi göğe doğru süzüldüler"
   - Cümle 11: «Minik şemsiyeler gibi göğe doğru süzüldüler.»
   - Açıklama: Tohumları şemsiyeye benzeten mecaz 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0116` birebir aynı, `@degisim: buzdolabı -> tohum` (tutuyorsan), ardından `@onarim: 5bed3a044d950077c0e05f80801f3531f4195f2c`, sonra gövde.

### Hikâye 8: tohum hayri-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0117
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'köfte', fiil 'sakinleşmek', sıfat 'mor'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: taşı dik tuttuğu için taş suda zıplamadı | tepsiyi tuttuğu gibi taşı düz tuttu ve attı
@tohum: hayri-0117
Deniz kıyısında hafif bir rüzgar esiyordu. Kamil suya ince taşlar atıyordu ve Hayri onu izliyordu. Taşlar suyun üstünde zıplıyordu. Hayri bunu ilk kez denemek istedi. Ama taşı dik tuttuğu için o hemen suya battı. Hayri biraz kızdı, sonra derin bir nefes alıp sakinleşti. Dükkanda baklava tepsisini hep düz tuttuğunu hatırladı. Mor ve ince bir taş seçti. Onu tıpkı o tepsi gibi düz tuttu ve fırlattı. Taş suyun üstünde üç kez zıpladı. "Bak, Kamil, tam üç kez!" dedi Hayri. "Harika atış, Hayri!" dedi Kamil. Sonra ikisi kumda oturup Kamil'in getirdiği köfte ekmekleri mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tepsiyi tuttuğu gibi taşı"
   - Cümle 0 (plan satırı): «taşı dik tuttuğu için taş suda zıplamadı | tepsiyi tuttuğu gibi taşı düz tuttu ve attı»
   - Açıklama: 'Tuttuğu gibi' 'tutar tutmaz' anlamına da gelir; 'tepsiyi tutar gibi' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "o hemen suya battı"
   - Cümle 5: «Ama taşı dik tuttuğu için o hemen suya battı.»
   - Açıklama: 'o' zamirinin taşı mı Hayri'yi mi gösterdiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "tuttuğu için o hemen suya battı"
   - Cümle 5: «Ama taşı dik tuttuğu için o hemen suya battı.»
   - Açıklama: 'O' zamirinin taşı mı Hayri'yi mi gösterdiği belli değil.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 5: «Ama taşı dik tuttuğu için o hemen suya battı.»
   - Açıklama: Sorun (taşın batması) ilk üç cümlede değil, beşinci cümlede söyleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kamil'in getirdiği köfte ekmekleri"
   - Cümle 13: «Sonra ikisi kumda oturup Kamil'in getirdiği köfte ekmekleri mutlu mutlu yedi.»
   - Açıklama: Köfte ekmekleri daha önce kurulmadan sebepsizce beliriyor.
   - Açıklama: Köfte ekmekler önceden kurulmadan son cümlede sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0117` birebir aynı, ardından `@onarim: db9380ef0323ba3161ccfc0174339240fba9e33d`, sonra gövde.

### Hikâye 9: tohum hayri-0118 (deneme 1 -> 2)

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
@plan: kabuklar çok sertti ve açılmadı | iki cevizi birbirine sürttü ve sıktı
@tohum: hayri-0118
@degisim: sos -> ceviz
Bir sabah Hayri parkta oynarken çok acıktı. Büyük bir ağacın altında yere düşmüş cevizler fark etti. Ama kabuklar çok sertti ve elleriyle açılmadı. Hayri acıkmıştı, bu yüzden hemen vazgeçmedi. Biraz düşündü ve iki cevizi avucuna aldı. Onları birbirine sürttü ve sıkıca bastırdı. Çıt diye bir ses geldi ve bir tanesi kırıldı. İçinden minik, beyaz bir ceviz içi çıktı. Hayri onu afiyetle yedi. Sonra kalan cevizleri de böyle kırdı. Hayri çok sevindi, çünkü sert kabuğu kendisi açmıştı.
```

**Hakem bulguları (7):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yere düşmüş cevizler fark etti"
   - Cümle 2: «Büyük bir ağacın altında yere düşmüş cevizler fark etti.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yerden bulunan cevizler kırılıp yeniyor.
   - Açıklama: Çocuk parkta yerde bulduğu yiyeceği tek başına yemeyi taklit edebilir; güvenli kullanım satırı paylaşmak, beklemek ya da hazırlamak diyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yere düşmüş cevizler fark etti"
   - Cümle 2: «Büyük bir ağacın altında yere düşmüş cevizler fark etti.»
   - Açıklama: Belirtme eki eksik; 'cevizleri fark etti' olmalı.
   - Açıklama: 'Fark etmek' belirtme eki ister; 'cevizleri fark etti' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sertti ve elleriyle açılmadı"
   - Cümle 3: «Ama kabuklar çok sertti ve elleriyle açılmadı.»
   - Açıklama: Edilgen fiille araç kullanımı bozuk; 'elleriyle açamadı' olmalı.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri acıkmıştı, bu yüzden"
   - Cümle 4: «Hayri acıkmıştı, bu yüzden hemen vazgeçmedi.»
   - Açıklama: Hayri'nin acıktığı ilk cümlede söylenmişti, gereksiz tekrar.
   - Açıklama: Acıkma ilk cümlede söylendi, gereksiz yere tekrarlanıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri acıkmıştı, bu yüzden hemen vazgeçmedi"
   - Cümle 4: «Hayri acıkmıştı, bu yüzden hemen vazgeçmedi.»
   - Açıklama: Tohumdaki acıkma özelliği bir kez değil iki kez anlatılıyor ve güvenli kullanım satırındaki paylaşma, bekleme ya da hazırlama olarak gösterilmiyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri acıkmıştı, bu yüzden"
   - Cümle 4: «Hayri acıkmıştı, bu yüzden hemen vazgeçmedi.»
   - Açıklama: Tohum özelliği acıkma bir kez değil iki kez kullanılıyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri onu afiyetle yedi"
   - Cümle 9: «Hayri onu afiyetle yedi.»
   - Açıklama: Yerde bulunan ve küçük çocuklar için boğulma riski taşıyan ceviz yeniyor.
   - Açıklama: Yerden toplanan ceviz yeniyor; güvenli özellik kullanımına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0118` birebir aynı, `@degisim: sos -> ceviz` (tutuyorsan), ardından `@onarim: 415bf7e936033d680b536302e604bc7bf003307d`, sonra gövde.

### Hikâye 10: tohum hayri-0119 (deneme 1 -> 2)

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
@plan: rüzgar siyah şapkayı kıyıda bir yere uçurdu | dükkanın sarı işaretine bakıp şapkayı buldu
@tohum: hayri-0119
Denizden serin bir rüzgar esiyordu. Hayri başını serinletmek için siyah şapkasını çıkarıp kuma koydu. Ama rüzgar onu kaptı ve kıyıda uzağa uçurdu. Hayri bu şapkayı baklava dükkanında çalışırken takıyordu. Sosisli ekmeğini bırakıp hemen aramaya başladı. Kıyıda bir sürü siyah taş ve yosun vardı. Hayri her birine tek tek baktı ama şapkayı göremedi. Sonra şapkanın önündeki sarı dükkan işaretini hatırladı. Bu kez yalnız sarı bir işaret aradı. Büyük bir taşın arkasında onu hemen gördü. Şapkası oradaydı. Hayri kumunu silkeledi ve şapkayı yeniden taktı. Hayri çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sosisli ekmeğini bırakıp hemen"
   - Cümle 5: «Sosisli ekmeğini bırakıp hemen aramaya başladı.»
   - Açıklama: Sosisli ekmek sebepsiz beliriyor ve hiçbir işe yaramıyor.
   - Açıklama: Sosisli ekmek sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "şapkanın önündeki sarı dükkan işaretini"
   - Cümle 8: «Sonra şapkanın önündeki sarı dükkan işaretini hatırladı.»
   - Açıklama: Kartta Hayri'nin dükkan işaretli siyah şapkası gibi bir eşya yok.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hayri kumunu silkeledi"
   - Cümle 12: «Hayri kumunu silkeledi ve şapkayı yeniden taktı.»
   - Açıklama: İyelik eki yanlış kişiyi gösteriyor; 'şapkanın kumunu silkeledi' olmalı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hayri kumunu silkeledi"
   - Cümle 12: «Hayri kumunu silkeledi ve şapkayı yeniden taktı.»
   - Açıklama: 'kumunu' iyelik eki Hayri'yi gösteriyor; neyin kumu olduğu belli değil, 'şapkanın kumunu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0119` birebir aynı, ardından `@onarim: 5229aa77718475195dc8dc2fc0a15e434a78080c`, sonra gövde.

### Hikâye 11: tohum hayri-0120 (deneme 1 -> 2)

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
Hayri, Akın'la kumda deniz kabuğu topluyordu. "Bugün benim doğum günüm!" dedi Akın. Hayri bu günü kutlamak istedi. Ama kumsalda ona bir hediye bulmak çok zordu. Hayri çok acıkmıştı ve çantasında en sevdiği çilekli kek vardı. Onu yemedi. "Gözlerini kapa, Akın," dedi Hayri. Keki düz bir taşın üstüne koydu. Çevresini topladıkları kabuklarla süsledi. "Gözlerini aç, Akın, bu senin hediyen!" dedi Hayri. Akın süslü keki görünce sevinçle zıpladı. Sonra onu ikiye böldü ve yarısını Hayri'ye verdi. "İyi ki doğdun, Akın!" dedi Hayri. Hayri bundan sonra en sevdiği yiyecekleri de arkadaşlarıyla paylaştı.
```

**Hakem bulguları (1):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "en sevdiği yiyecekleri de arkadaşlarıyla paylaştı"
   - Cümle 14: «Hayri bundan sonra en sevdiği yiyecekleri de arkadaşlarıyla paylaştı.»
   - Açıklama: Notlanan çoğul canlı arkadaşlar paylaşım olayına katılan kişiler olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0120` birebir aynı, `@degisim: giydirmek -> süslemek` (tutuyorsan), ardından `@onarim: b435accb6b84df115da4bed285624a09d0c61624`, sonra gövde.

### Hikâye 12: tohum hayri-0121 (deneme 1 -> 2)

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
@plan: kaleyi kutlamak istedi ama ne yapacağını bilmedi | acıkınca kumdan bir pasta yaptı
@tohum: hayri-0121
Güneş parlıyordu ve kıyıya küçük dalgalar geliyordu. Hayri, Mert'in kumda bitirdiği kocaman kaleye bakıyordu. Onu bir sürprizle kutlamak istedi ama ne yapacağını bilmiyordu. O sırada çok acıktı ve aklına hemen bir pasta geldi. Hayri, Mert'ten arkasını dönmesini istedi. Kıyıdan elleriyle su getirip kumu suladı. Islak kumdan yuvarlak bir pasta yaptı. Sabah topladıkları kabukları torbadan çıkarıp üstüne dizdi. "Dönebilirsin, Mert, bu senin için!" dedi Hayri. Mert sürprizi görünce çok güldü. "Bu gördüğüm en yaratıcı pasta, Hayri, teşekkür ederim!" dedi Mert.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kaleyi kutlamak istedi"
   - Cümle 0 (plan satırı): «kaleyi kutlamak istedi ama ne yapacağını bilmedi | acıkınca kumdan bir pasta yaptı»
   - Açıklama: Bir kale kutlanmaz; fiil nesnesine uymuyor.
   - Açıklama: Bir kale kutlanmaz; 'kutlamak' fiili nesnesine uymuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu bir sürprizle kutlamak"
   - Cümle 3: «Onu bir sürprizle kutlamak istedi ama ne yapacağını bilmiyordu.»
   - Açıklama: 'Onu' zamirinin Mert'i mi kaleyi mi gösterdiği belli değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama ne yapacağını bilmiyordu"
   - Cümle 3: «Onu bir sürprizle kutlamak istedi ama ne yapacağını bilmiyordu.»
   - Açıklama: Sorunun sebebi yok; kutlama fikrinin neden bulunamadığı söylenmiyor ve sorun çocuğun önemseyeceği somut bir dert değil.
   - Açıklama: Sorun yalnız bir kararsızlık; somut bir sebebi söylenmiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aklına hemen bir pasta geldi"
   - Cümle 4: «O sırada çok acıktı ve aklına hemen bir pasta geldi.»
   - Açıklama: 'Aklına gelmek' deyimdir.
   - Açıklama: 'Aklına gelmek' deyimsel bir anlatım.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada çok acıktı ve aklına hemen bir pasta geldi"
   - Cümle 4: «O sırada çok acıktı ve aklına hemen bir pasta geldi.»
   - Açıklama: Çözüm sebepsiz bir acıkmayla geliyor ve acıkan Hayri yenmeyen bir kum pastası yapıyor.
   - Açıklama: Çözüm fikri kutlama isteğinden değil sebepsizce acıkmaktan geliyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kıyıdan elleriyle su getirip kumu suladı"
   - Cümle 6: «Kıyıdan elleriyle su getirip kumu suladı.»
   - Açıklama: Çözüm su getirme, pasta yapma ve kabuk dizme gibi ikiden fazla adım sürüyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sabah topladıkları kabukları torbadan çıkarıp"
   - Cümle 8: «Sabah topladıkları kabukları torbadan çıkarıp üstüne dizdi.»
   - Açıklama: Kabuklar ve torba önceden kurulmadan sebepsizce beliriyor.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "en yaratıcı pasta"
   - Cümle 11: «"Bu gördüğüm en yaratıcı pasta, Hayri, teşekkür ederim!" dedi Mert.»
   - Açıklama: 'Yaratıcı' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
9. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gördüğüm en yaratıcı pasta"
   - Cümle 11: «"Bu gördüğüm en yaratıcı pasta, Hayri, teşekkür ederim!" dedi Mert.»
   - Açıklama: 'Yaratıcı' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0121` birebir aynı, ardından `@onarim: b03d6e2e26a8037c273ead9cfef0d51496cd8ab8`, sonra gövde.
