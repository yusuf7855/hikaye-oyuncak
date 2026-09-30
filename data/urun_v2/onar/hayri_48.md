# Editör görevi (onarım): Hayri, onarım partisi 48

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar48.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar48.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0160 (deneme 2 -> 3)

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
@plan: uçurtmanın kuyruğu yoktu ve uçurtma kuma düştü | yemek kutusundaki peçeteden kuyruk yaptı
@tohum: hayri-0160
Hayri deniz kıyısında kağıttan bir uçurtma yapmıştı. Uçurtmayı rüzgara bıraktı ama uçurtma dönüp kuma düştü. Uçurtmanın kuyruğu yoktu, bu yüzden havada duramıyordu. Hayri çantasına baktı ama ip ya da kumaş bulamadı. Sonra yemek kutusunu açtı. Peynirli ekmeği büyük, benekli bir peçetenin içindeydi. Hayri çok acıkmıştı ama ekmeğini sonra yiyecekti. Önce peçeteyi uzun bir şerit gibi büktü. Sonra onu uçurtmanın alt ucuna bağladı. Bu kuyruk uçurtmayı düz tuttu. Uçurtma yükseldi ve dalgaların üstünde uçtu. Hayri ipi tuttu ve sevinçle zıpladı. Hayri bundan sonra her uçurtmasına uzun bir kuyruk yaptı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri çok acıkmıştı ama ekmeğini sonra yiyecekti"
   - Cümle 7: «Hayri çok acıkmıştı ama ekmeğini sonra yiyecekti.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümüne katkı vermeyen süs bir cümle olarak kalıyor, işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ama ekmeğini sonra yiyecekti"
   - Cümle 7: «Hayri çok acıkmıştı ama ekmeğini sonra yiyecekti.»
   - Açıklama: Açlık ayrıntısı kurulup bir daha kullanılmıyor ve olaya hiçbir katkı yapmıyor.
   - Açıklama: Açlık ve sonra yenecek ekmek kurulup bir daha hiç kullanılmıyor, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0160` birebir aynı, ardından `@onarim: 7bbf382407378e6d5f2c44dc2c0b2b03b241b0e8`, sonra gövde.

### Hikâye 2: tohum hayri-0161 (deneme 2 -> 3)

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
Parkta sıcak bir öğle vaktiydi. Hayri elinde boş bir baklava tepsisi taşıyordu. Tepsiyi yakındaki dükkana, çalıştığı yere götürüyordu. Bankın yanında köpek Yumak'ı gördü. Yumak dilini çıkarmıştı, çünkü çok susamıştı. Hayri çantasından su şişesini çıkardı. "Gel, Yumak, biraz su iç," dedi Hayri. Ama Yumak dar şişeden su içemedi. Hayri tepsiyi yere koydu ve içine su döktü. Yumak hemen yaklaştı ve suyu içti. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. "Afiyet olsun, Yumak, bol bol iç!" dedi Hayri gülerek.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yumak dilini çıkarmıştı, çünkü çok susamıştı"
   - Cümle 5: «Yumak dilini çıkarmıştı, çünkü çok susamıştı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak beşinci cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Yumak dar şişeden su içemedi"
   - Cümle 8: «Ama Yumak dar şişeden su içemedi.»
   - Açıklama: Köpeğin susuzluğu ancak 5. cümlede, asıl sorun ise 8. cümlede söyleniyor; ilk 3 cümlede sorun yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0161` birebir aynı, `@degisim: mikroskop -> tepsi` (tutuyorsan), ardından `@onarim: d277f5b7a1302c6b1204e4e6d0099e8d7336c0a9`, sonra gövde.

### Hikâye 3: tohum hayri-0163 (deneme 2 -> 3)

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
@plan: küçük bir dalga peynirli ekmeği ıslattı | ilk kez waffle denedi ve sevdi
@tohum: hayri-0163
Bir sabah Hayri deniz kıyısında kumdan bir kale yapıyordu. Havlunun üstünde peynirli ekmeği, çantasında da bir waffle vardı. Birden küçük bir dalga geldi ve ekmeği ıslattı. Hayri çok acıkmıştı ve üzgün bir yüzle ekmeğe baktı. Sonra çantasındakileri havlunun kuru ucuna döktü. Hayri daha önce hiç waffle yememişti. Önce ucundan bir parça ısırdı. Waffle yumuşak ve tatlıydı. Hayri bir parça daha, sonra bir parça daha yedi. Karnı doyunca Hayri kumdan kalesini mutlu mutlu yapmaya devam etti.
```

**Hakem bulguları (5):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra çantasındakileri havlunun kuru ucuna döktü"
   - Cümle 5: «Sonra çantasındakileri havlunun kuru ucuna döktü.»
   - Açıklama: Çözüm ıslanan ekmeğe yönelmiyor, sorunu bırakıp başka bir yiyeceğe geçiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Önce ucundan bir parça"
   - Cümle 7: «Önce ucundan bir parça ısırdı.»
   - Açıklama: 'Ucundan' kelimesinin neyi gösterdiği belli değil; son geçen 'havlunun kuru ucu'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Önce ucundan bir parça ısırdı"
   - Cümle 7: «Önce ucundan bir parça ısırdı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına göre yemek sevgisi paylaşmak, beklemek ya da hazırlamak olarak gösterilmeli; burada yalnız yiyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri bir parça daha, sonra bir parça daha yedi"
   - Cümle 9: «Hayri bir parça daha, sonra bir parça daha yedi.»
   - Açıklama: Yemek sevgisi güvenli kullanım satırının dışında art arda yemek olarak gösteriliyor.
   - Açıklama: Figürün özelliği güvenli özellik kullanımı satırının dışında, art arda yeme örneği olarak gösteriliyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bir parça daha, sonra bir parça daha yedi"
   - Cümle 9: «Hayri bir parça daha, sonra bir parça daha yedi.»
   - Açıklama: Yemek sevgisi kartın güvenli özellik kullanımı satırındaki gibi paylaşmak, beklemek ya da hazırlamak olarak değil, tek başına art arda yemek olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0163` birebir aynı, ardından `@onarim: 015930e043ce53a26c593d45b5f92a4e0de8c99f`, sonra gövde.

### Hikâye 4: tohum hayri-0164 (deneme 2 -> 3)

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
@degisim: aceleci -> ıslak
Hayri, Kamil ile evin önündeki bahçede yan yana oturuyordu. Hayri'nin tabağında iki dilim baklava, Kamil'in elinde bir dilim karpuz vardı. Ama ıslak karpuz Kamil'in elinden kaydı ve toprağa düştü. Kırmızı karpuzu baştan sona toprak kapladı. Kamil boş eline üzgün üzgün baktı. Hayri bu baklavaları çalıştığı dükkandan getirmişti. Hayri, Kamil'in eli boş kalmasın diye baklavalarından birini ona verdi. Kamil baklavayı aldı ve sevinçle gülümsedi. İki arkadaş baklavalarını birlikte yedi. Sonra yere düşen karpuzu çöpe attılar. Kamil, Hayri'ye tatlı için teşekkür etti. Hayri bundan sonra baklavasını her zaman arkadaşlarıyla paylaştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bu baklavaları çalıştığı dükkandan getirmişti"
   - Cümle 6: «Hayri bu baklavaları çalıştığı dükkandan getirmişti.»
   - Açıklama: Baklavanın dükkandan gelmesi olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0164` birebir aynı, `@degisim: aceleci -> ıslak` (tutuyorsan), ardından `@onarim: af5256f40cc28edac3362fda2527e891eeef554b`, sonra gövde.

### Hikâye 5: tohum hayri-0166 (deneme 2 -> 3)

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
@plan: kutuyu çeken ince iplik koptu | cebindeki kalın kırmızı ipi kutuya bağladı
@tohum: hayri-0166
@degisim: çekingen -> kırmızı
Rüzgar hafif hafif esiyordu. Hayri parkta boş bir baklava kutusunu ipliğe bağlamış, araba gibi çekiyordu. Ama kutu bir taşa takıldı ve ince iplik koptu. Hayri kopan ipliğe üzgün üzgün baktı. Sonra elini cebine soktu ve kutunun kalın, kırmızı ipini buldu. Bu ipi dükkanda kutudan çözmüş, sonra unutmuştu. Hayri kırmızı ipi kutuya sıkıca bağladı. Sonra kutunun içine üç küçük taş koydu. Sağlam ip Hayri'yi çok rahatlattı. Hayri kutuyu kaydırağın etrafında hızlı hızlı çekti. İçindeki taşlar her adımda komik bir ses çıkardı. Hayri bu sese kahkahalarla güldü. Çok mutluydu, çünkü araba oyunu yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kutunun içine üç küçük taş koydu"
   - Cümle 8: «Sonra kutunun içine üç küçük taş koydu.»
   - Açıklama: Taşları kutuya koymak önceki olaydan çıkmıyor ve sorunla ilgisi olmayan işlevsiz bir ayrıntı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sağlam ip Hayri'yi çok rahatlattı"
   - Cümle 9: «Sağlam ip Hayri'yi çok rahatlattı.»
   - Açıklama: 'Rahatlattı' soyut bir duygu anlatımı ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Rahatlattı' soyut bir duygu anlatımı ve ipi özne yapıyor, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0166` birebir aynı, `@degisim: çekingen -> kırmızı` (tutuyorsan), ardından `@onarim: 0cdb73e55678ec7559e97588bab5d1feeba0db81`, sonra gövde.

### Hikâye 6: tohum hayri-0167 (deneme 2 -> 3)

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
@plan: kağıt uçak çok hafifti ve hemen düşüyordu | yemek kutusunun lastiğini uçağın burnuna taktı
@tohum: hayri-0167
Hayri deniz kıyısında Basri Amca'yı gördü. Basri Amca mavi bir kağıttan uçak yapmıştı. Ama uçak çok hafifti ve havada sallanıp hemen kuma düşüyordu. Basri Amca kağıdı iki kez değiştirdi ama uçak yine uçmadı. Hayri, uçağın burnu biraz ağır olursa düz uçar diye düşündü. Hayri'nin yemek kutusunun etrafında küçük bir lastik vardı. Hayri lastiği çıkardı ve uçağın burnuna taktı. Basri Amca uçağı yeniden fırlattı. Mavi uçak bu kez uzağa kadar düz uçtu. Basri Amca gülerek ellerini çırptı. Acıkan Hayri ekmeğini çıkarıp Basri Amca ile paylaştı. İkisi de çok sevindi, çünkü uçak sonunda düz uçmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Acıkan Hayri ekmeğini çıkarıp"
   - Cümle 11: «Acıkan Hayri ekmeğini çıkarıp Basri Amca ile paylaştı.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümüyle ilgisiz, sorun çözüldükten sonra süs olarak eklenmiş; özellik işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Acıkan Hayri ekmeğini çıkarıp Basri Amca ile paylaştı"
   - Cümle 11: «Acıkan Hayri ekmeğini çıkarıp Basri Amca ile paylaştı.»
   - Açıklama: Ekmek sebepsiz beliriyor ve uçak sorununa hiçbir katkısı olmayan işlevsiz bir ayrıntı.
   - Açıklama: Acıkma ve ekmek paylaşma sebepsiz beliriyor ve uçak sorunuyla hiçbir bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0167` birebir aynı, ardından `@onarim: 425c6c77ac67d96aa52bc443418eb1be394a88cc`, sonra gövde.

### Hikâye 7: tohum hayri-0169 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0169
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tartı', fiil 'uzanmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: son elma tartıdan kayıp bankın altına yuvarlandı | küçük arkadaşından yardım istedi
@tohum: hayri-0169
@degisim: narin -> küçük
Rüzgar hafifçe esiyordu. Hayri ile Akın kamp yerinde topladıkları elmaları tartıya koyuyordu. Hayri yine acıkmıştı, ama son elma tartıdan kayıp bankın altına yuvarlandı. Hayri yere uzandı, ama eli elmaya yetişmedi. Bank çok alçaktı ve Hayri altına sığmadı. "Akın, sen benden küçüksün, elmayı alır mısın?" diye sordu Hayri. Akın hemen yere eğildi ve yavaşça bankın altına girdi. Elmayı tuttu ve dışarı çıkardı. Hayri elmayı Akın'la paylaştı. İkisi sırayla birer ısırık aldı. "Teşekkürler, Akın, elmamı sen kurtardın!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri yine acıkmıştı, ama son elma"
   - Cümle 3: «Hayri yine acıkmıştı, ama son elma tartıdan kayıp bankın altına yuvarlandı.»
   - Açıklama: 'ama' bağlacı acıkma ile elmanın yuvarlanması arasında karşıtlık kurmuyor; yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0169` birebir aynı, `@degisim: narin -> küçük` (tutuyorsan), ardından `@onarim: df3bb651dbc0a676c4b6f68d1e8fd384eaddd1f6`, sonra gövde.

### Hikâye 8: tohum hayri-0170 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0170
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'damla', fiil 'büyümek', sıfat 'çizgili'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: minik filiz yolun ortasında güvende değildi | çevresine taşlardan kocaman bir çember yapıp suladı
@tohum: hayri-0170
Bir sabah Hayri parkta salıncakların yanında yürüyordu. Birden yolun ortasında minik bir filiz gördü. Filizin çizgili iki küçük yaprağı vardı. Ama burası bir yoldu ve filiz hiç güvende değildi. Hayri onun büyüyüp çiçek açmasını çok istedi. Hayri bu işi biraz abarttı. Minik yaprakların çevresine taşlardan kocaman bir çember yaptı. Bu büyük çember uzaktan bile görünüyordu. Sonra Hayri çeşmeden elleriyle biraz su getirdi. Suyu damla damla toprağa döktü. Hayri çok sevindi, çünkü filiz artık güvendeydi.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "filiz hiç güvende değildi"
   - Cümle 4: «Ama burası bir yoldu ve filiz hiç güvende değildi.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede açık değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri bu işi biraz abarttı"
   - Cümle 6: «Hayri bu işi biraz abarttı.»
   - Açıklama: 'Abartmak' ve 'bu iş' soyut; üstelik henüz bir iş yapılmadan söyleniyor, 3 yaşındaki çocuk anlamaz.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hayri bu işi biraz abarttı"
   - Cümle 6: «Hayri bu işi biraz abarttı.»
   - Açıklama: 'Bu işi' henüz yapılmamış bir işi gösteriyor; neyi kastettiği belli değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bu işi biraz abarttı"
   - Cümle 6: «Hayri bu işi biraz abarttı.»
   - Açıklama: Kartın özellikler alanı olayları abartmayı anlatır; burada özellik taş çemberi büyük yapmak gibi fiziksel bir aşırılığa kaydırılmış.
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek); burada abartma bir işi fazla yapmak olarak kullanılmış.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra Hayri çeşmeden elleriyle biraz su getirdi"
   - Cümle 9: «Sonra Hayri çeşmeden elleriyle biraz su getirdi.»
   - Açıklama: Sulamak filizin yolda güvende olmaması sebebine yönelmiyor, fazladan bir adım.
   - Açıklama: Sulama filizin güvenlik sorununa yönelmeyen fazladan bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0170` birebir aynı, ardından `@onarim: 8b2e004e4f81c368cb7bd3ef4e1d00be577f1716`, sonra gövde.

### Hikâye 9: tohum hayri-0171 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0171
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yağmur ya da kar günü
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'dolma', fiil 'sarmak', sıfat 'şeffaf'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: yağmurda köpek dışarıda kaldı ve çalının altına girdi | acıkınca yemek kutusunu açtı ve köpek kokuya geldi
@tohum: hayri-0171
Hayri, Yumak ile ormandaki kamp yerindeydi. Birden yağmur başladı ve Hayri çadıra koştu. Ama Yumak dışarıda kaldı ve bir çalının altına girdi. "Gel, Yumak, burası kuru!" diye seslendi Hayri. Hayri çadırın şeffaf penceresinden baktı ama Yumak gelmedi. O sırada Hayri acıktı ve dolma kutusunu açtı. Güzel yemek kokusu dışarıya kadar gitti. Yumak kokuyu aldı ve koşarak çadıra girdi. Hayri onu hemen bir havluya sardı. Sonra Yumak'a ekmekten küçük bir parça verdi. Hayri çok sevindi, çünkü Yumak artık kuru ve yanındaydı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çadırın şeffaf penceresinden baktı"
   - Cümle 5: «Hayri çadırın şeffaf penceresinden baktı ama Yumak gelmedi.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'şeffaf' kelimesi 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "O sırada Hayri acıktı ve dolma kutusunu açtı"
   - Cümle 6: «O sırada Hayri acıktı ve dolma kutusunu açtı.»
   - Açıklama: Çözüm Yumak'ı getirmeye yönelmiyor; Hayri yalnız acıktığı için kutuyu açıyor ve sorun tesadüfen çözülüyor.
   - Açıklama: Hayri kutuyu Yumak için değil acıktığı için açıyor; çözüm sebebe bilerek yönelmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güzel yemek kokusu dışarıya kadar gitti"
   - Cümle 7: «Güzel yemek kokusu dışarıya kadar gitti.»
   - Açıklama: Çözüm tesadüfi bir açlıktan sebepsizce doğuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Yumak'a ekmekten küçük bir parça verdi"
   - Cümle 10: «Sonra Yumak'a ekmekten küçük bir parça verdi.»
   - Açıklama: Dolma kutusundan sebepsizce ekmek çıkıyor ve çözüm olaylardan değil rastlantıdan geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0171` birebir aynı, ardından `@onarim: f8caf9fd643ca5213e09fbf6a9d1343754001e62`, sonra gövde.

### Hikâye 10: tohum hayri-0174 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0174
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'gitar', fiil 'küçülmek', sıfat 'sevimli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: top şemsiyeye çarptı ve şemsiye yana yattı | şemsiyeyi yeniden dikti ve özür diledi
@tohum: hayri-0174
@degisim: gitar -> şemsiye
Deniz kıyısında Hayri kumda top oynuyordu. Basri Amca şemsiyesinin altında Hayri'nin çalıştığı dükkandan gelen baklavayı yiyordu. Hayri topa çok sert vurdu ve top şemsiyeye çarptı. Şemsiye yana yattı ve gölgesi küçüldü. "Hayri, şemsiyem düştü!" diye bağırdı Basri Amca. Hayri hemen koştu ve şemsiyeyi yeniden dikti. "Özür dilerim, Basri Amca, dikkat etmedim," dedi Hayri. Basri Amca bir baklava daha yedi ve gülümsedi. "Sen çok sevimli bir çocuksun, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü Basri Amca ona artık kızmıyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri'nin çalıştığı dükkandan gelen baklavayı"
   - Cümle 2: «Basri Amca şemsiyesinin altında Hayri'nin çalıştığı dükkandan gelen baklavayı yiyordu.»
   - Açıklama: Tohumdaki baklava özelliği yalnız süs olarak geçiyor ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki baklava dükkanı özelliği sorunun çözümünde işe yaramıyor, yalnız anılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri'nin çalıştığı dükkandan gelen baklavayı"
   - Cümle 2: «Basri Amca şemsiyesinin altında Hayri'nin çalıştığı dükkandan gelen baklavayı yiyordu.»
   - Açıklama: Hayri'nin dükkanda çalıştığı ve baklava ayrıntısı sorunla ya da çözümle hiç ilgili olmayan işlevsiz bir ayrıntı.
   - Açıklama: Baklava ve Hayri'nin dükkanda çalışması olayda hiçbir işe yaramayan, sebepsiz eklenmiş bir ayrıntı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Basri Amca bir baklava daha yedi"
   - Cümle 8: «Basri Amca bir baklava daha yedi ve gülümsedi.»
   - Açıklama: Baklava özelliği birden çok kez ve işlevsiz biçimde tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0174` birebir aynı, `@degisim: gitar -> şemsiye` (tutuyorsan), ardından `@onarim: 3012ec937b12f24e73a98b934c05ff8d94843767`, sonra gövde.

### Hikâye 11: tohum hayri-0175 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0175
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'lastik', fiil 'okumak', sıfat 'sert'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: sert bir dalga kumdaki yazıyı sildi | dalgaların gelmediği ıslak kuma yeniden yazdı
@tohum: hayri-0175
@degisim: lastik -> dal
Bir sabah Hayri ile Mert deniz kıyısında yazı oyunu oynuyordu. Hayri ıslak kuma bir dalla en sevdiği yemeklerin adlarını yazıyordu. Ama sert bir dalga geldi ve yazıyı hemen sildi. "Hayri, yazı silindi!" dedi Mert. Hayri denize baktı ve biraz düşündü. Sonra birkaç adım geri gitti. Dalgaların gelmediği ıslak kuma yeniden "köfte" yazdı. Mert eğildi ve kelimeyi yüksek sesle okudu. Sonra Hayri "pilav" ve "baklava" yazdı. Mert okudukça Hayri biraz daha acıktı ve ikisi kıkır kıkır güldü. Hayri bundan sonra kelimeleri hep dalgalardan uzak yazdı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sert bir dalga geldi ve yazıyı hemen sildi"
   - Cümle 3: «Ama sert bir dalga geldi ve yazıyı hemen sildi.»
   - Açıklama: Silinen yazı yeniden yazılıp bitiyor; sorun önemsiz, 'dağıttı, topladı, bitti' türünden.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Mert okudukça Hayri biraz daha acıktı"
   - Cümle 10: «Mert okudukça Hayri biraz daha acıktı ve ikisi kıkır kıkır güldü.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz daha acıktı"
   - Cümle 10: «Mert okudukça Hayri biraz daha acıktı ve ikisi kıkır kıkır güldü.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0175` birebir aynı, `@degisim: lastik -> dal` (tutuyorsan), ardından `@onarim: f994f7fd6b9d22a9931b5c941af389794a89a1ba`, sonra gövde.

### Hikâye 12: tohum hayri-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0176
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'zambak', fiil 'sürmek', sıfat 'lezzetli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: soğuk tereyağı sert olduğu için ekmek yırtıldı | tereyağını güneşe koyup bekledi ve yeni ekmeğe sürdü
@tohum: hayri-0176
Parkta beyaz zambakların yanında güneşli bir bank vardı. Hayri banka oturdu ve çantasını açtı. Hayri acıkmıştı ve ilk kez ekmeğe kendisi tereyağı sürmeyi denedi. Ama tereyağı soğuk ve sertti, bu yüzden ekmek yırtıldı. Hayri tereyağı kutusunu güneşe koydu ve bekledi. Bu arada çiçekleri kokladı. Biraz sonra tereyağı yumuşadı. Hayri onu kaşıkla yeni bir ekmeğe yavaşça sürdü. Bu kez ekmek sağlam kaldı. Hayri ilk ısırığı aldı. Kendi hazırladığı ekmek çok lezzetliydi. Hayri ekmeğini çiçeklerin yanında mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "tereyağını güneşe koyup bekledi"
   - Cümle 0 (plan satırı): «soğuk tereyağı sert olduğu için ekmek yırtıldı | tereyağını güneşe koyup bekledi ve yeni ekmeğe sürdü»
   - Açıklama: Gövdede tereyağı güneşe konmuyor; plan çözümü yanlış söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0176` birebir aynı, ardından `@onarim: cf6d3f0d895129d4311ddcb0566d4f087b1959e8`, sonra gövde.
