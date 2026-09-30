# Editör görevi (onarım): Hayri, onarım partisi 54

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar54.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar54.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0171 (deneme 3 -> 4)

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
@plan: yağmurda köpek dışarıda kaldı ve çalının altına girdi | yemek kutusunu açtı ve köpek kokuya geldi
@tohum: hayri-0171
@degisim: şeffaf -> küçük
Hayri, Yumak ile ormandaki kamp yerindeydi. Birden yağmur başladı ve Hayri çadıra koştu. Ama Yumak dışarıda kaldı ve bir çalının altına girdi. "Gel, Yumak, burası kuru!" diye seslendi Hayri. Hayri çadırın küçük penceresinden baktı ama Yumak gelmedi. Hayri'nin yanında bir dolma kutusu vardı. Yumak yemek kokusunu çok severdi. Hayri çok acıkmıştı ama kutuyu önce Yumak için açtı. Güzel koku çalıya kadar gitti. Yumak kokuyu aldı ve koşarak çadıra girdi. Hayri onu hemen bir havluya sardı. Sonra yemeğini Yumak ile paylaştı. Hayri çok sevindi, çünkü Yumak artık kuru ve yanındaydı.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Hayri, Yumak ile ormandaki kamp yerindeydi"
   - Cümle 1: «Hayri, Yumak ile ormandaki kamp yerindeydi.»
   - Açıklama: Kartın yanlar ilişkisine göre Yumak Basri Amca'nın köpeğidir; Basri Amca olmadan Hayri'nin kamp arkadaşı gibi gösteriliyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama Yumak gelmedi"
   - Cümle 5: «Hayri çadırın küçük penceresinden baktı ama Yumak gelmedi.»
   - Açıklama: Yumak'ın çağrıya rağmen neden çalının altında kaldığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0171` birebir aynı, `@degisim: şeffaf -> küçük` (tutuyorsan), ardından `@onarim: 3b67c3c2010b3e231bbc2f891da8c9edbc53368d`, sonra gövde.

### Hikâye 2: tohum hayri-0174 (deneme 3 -> 4)

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
Deniz kıyısında Hayri kumda top oynuyordu. Basri Amca yakında şemsiyesinin altında oturuyordu. Hayri topa çok sert vurdu ve top şemsiyeye çarptı. Şemsiye yana yattı ve gölgesi küçüldü. "Hayri, şemsiyem düştü!" diye bağırdı Basri Amca. Hayri hemen koştu ve şemsiyeyi yeniden dikti. "Özür dilerim, Basri Amca, dikkat etmedim," dedi Hayri. Sonra çalıştığı dükkandan getirdiği baklavayı ona uzattı. Basri Amca baklavayı yedi ve gülümsedi. "Sen çok sevimli bir çocuksun, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü Basri Amca ona artık kızmıyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra çalıştığı dükkandan getirdiği baklavayı ona uzattı"
   - Cümle 8: «Sonra çalıştığı dükkandan getirdiği baklavayı ona uzattı.»
   - Açıklama: Baklava önceden kurulmadan sebepsizce beliriyor ve sorunun çözümüne bir katkısı yok.
   - Açıklama: Baklava önceden hiç kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0174` birebir aynı, `@degisim: gitar -> şemsiye` (tutuyorsan), ardından `@onarim: d87633cd2dec08e4e2509b2674bf63183098d526`, sonra gövde.

### Hikâye 3: tohum hayri-0175 (deneme 3 -> 4)

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
@plan: sert bir rüzgar kitabın sayfalarını çevirdi | yemek kutusunun lastiğini kitaba geçirdi
@tohum: hayri-0175
Bir sabah Hayri ile Mert deniz kıyısında bilmece oyunu oynuyordu. Mert kitaptan bilmeceler okuyordu, Hayri de cevapları buluyordu. Ama sert bir rüzgar esti ve kitabın sayfaları hızla döndü. "Hayri, okuduğum sayfa kayboldu!" dedi Mert. Hayri acıkmıştı ve yemek kutusunu açacaktı. Ama önce oyuna devam etmek istedi. Mert sayfayı yeniden açtı ve Hayri kutunun lastiğini kitaba geçirdi. Artık sayfalar rüzgarda dönmedi. Mert bilmeceyi okudu, Hayri cevabı bildi ve ikisi kahkahalarla güldü. Oyun bitince Hayri kutuyu açtı ve yemeğini Mert ile paylaştı. Hayri bundan sonra rüzgarlı günlerde kitabı lastikle tuttu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Mert sayfayı yeniden açtı"
   - Cümle 7: «Mert sayfayı yeniden açtı ve Hayri kutunun lastiğini kitaba geçirdi.»
   - Açıklama: Sayfanın dönmesi önemsiz; sayfa hemen yeniden açılabiliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri kutunun lastiğini kitaba geçirdi"
   - Cümle 7: «Mert sayfayı yeniden açtı ve Hayri kutunun lastiğini kitaba geçirdi.»
   - Açıklama: Yemek kutusunun lastiği önceden hiç kurulmadan çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0175` birebir aynı, ardından `@onarim: 5308e64c13ade91be7fee3c76d302e269f9af528`, sonra gövde.

### Hikâye 4: tohum hayri-0177 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0177
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kar', fiil 'süslenmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: pencereden garip bir tık tık sesi geldi | camı silip sesi yapan karlı dalı buldu
@tohum: hayri-0177
@degisim: süslenmek -> silmek
Bir sabah mahallede her yer bembeyazdı. Hayri evde, pencerenin yanında oturuyordu. Birden camdan "tık tık" diye bir ses geldi. Hayri bu sesi çok merak etti. Ama cam buharla kaplıydı ve dışarısı görünmüyordu. Hayri yine abarttı ve bütün camı baştan sona sildi. Camın arkasında üstü karlı bir ağaç dalı vardı. Rüzgar esince dal cama vuruyor ve o sesi çıkarıyordu. Hayri pencereyi açtı ve dala hafifçe dokundu. Dalın üstündeki kar yere döküldü. Bu çok eğlenceliydi ve Hayri güldü. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abarttı"
   - Cümle 6: «Hayri yine abarttı ve bütün camı baştan sona sildi.»
   - Açıklama: 'abartmak' soyut bir kavram ve 3 yaşındaki çocuk için anlaşılır değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abarttı ve"
   - Cümle 6: «Hayri yine abarttı ve bütün camı baştan sona sildi.»
   - Açıklama: 'Abartmak' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yine abarttı ve bütün camı baştan sona sildi"
   - Cümle 6: «Hayri yine abarttı ve bütün camı baştan sona sildi.»
   - Açıklama: Karttaki özellik olayları (sözle) abartmaktır; burada bir işi aşırı yapmak anlamında kullanılmış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri yine abarttı ve bütün camı baştan sona sildi"
   - Cümle 6: «Hayri yine abarttı ve bütün camı baştan sona sildi.»
   - Açıklama: Buharlı camı silmek abartma değil; özellik zorla eklenmiş ve 'yine' önceden olmayan bir olaya dayanıyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri pencereyi açtı ve dala hafifçe dokundu"
   - Cümle 9: «Hayri pencereyi açtı ve dala hafifçe dokundu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde pencere açılıp dışarıdaki dala uzanılıyor.
   - Açıklama: Çocuğun taklit edebileceği biçimde açık pencereden dışarı uzanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0177` birebir aynı, `@degisim: süslenmek -> silmek` (tutuyorsan), ardından `@onarim: 9519c4ff6a9366aacdbd11797341593383227681`, sonra gövde.

### Hikâye 5: tohum hayri-0178 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0178
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'buket', fiil 'rahatlamak', sıfat 'yüksek'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: rüzgar ekmek paketini uçurdu ve paket kayboldu | köpekten yardım istedi ve paketi çiçeklerde buldu
@tohum: hayri-0178
@degisim: buket -> çiçek
Bir sabah Hayri bahçede oturuyordu ve çok acıkmıştı. Ama rüzgar ekmek paketini uçurmuştu ve paket kaybolmuştu. Hayri onun nereye gittiğini çok merak etti. O sırada Yumak koşarak yanına geldi. "Yumak, paketi bulur musun?" diye sordu Hayri. Yumak burnunu yere dayadı ve çiçeklere doğru koştu. Sonra orada durdu ve yüksek sesle havladı. Hayri eğildi ve çiçeklerin arasına baktı. Paket tam orada duruyordu. Hayri rahatladı ve onu aldı. Ekmeğini ikiye böldü ve bir parçayı Yumak'a verdi. İkisi yan yana oturdu ve ekmeklerini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bir parçayı Yumak'a verdi"
   - Cümle 11: «Ekmeğini ikiye böldü ve bir parçayı Yumak'a verdi.»
   - Açıklama: Hayri başkasının köpeğini sahibine sormadan besliyor; çocuk bunu taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0178` birebir aynı, `@degisim: buket -> çiçek` (tutuyorsan), ardından `@onarim: 1a5e7f216da0814d3690a4f8a13541fb02cd39aa`, sonra gövde.

### Hikâye 6: tohum hayri-0180 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0180
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'iz', fiil 'tekrarlamak', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: acıkınca simit çantasını kumsalda bulamadı | arkadaşından yardım istedi ve ayak izleri sayesinde çantayı buldu
@tohum: hayri-0180
Bir sabah Hayri ile Mert deniz kıyısında top oynuyordu. Bir süre sonra Hayri çok acıktı. Ama top oynarken simit çantası çok uzakta kalmıştı. Hayri etrafa baktı ama çantayı göremedi. "Mert, çantamı bulamıyorum, bana yardım eder misin?" diye sordu Hayri. Mert bir an hareketsiz durdu ve düşündü. "Bak, kumda her adım bir iz bırakıyor," dedi Mert. Hayri önce anlamadı ve Mert'e baktı. Mert sözünü yavaşça tekrarladı. Hayri kendi izleri boyunca geri yürüdü. Böylece büyük bir taşın arkasına geldi. Çanta orada duruyordu. Hayri bir simidi hemen Mert'e verdi. Hayri çok sevindi, çünkü Mert'ten yardım istemiş ve çantasını bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri önce anlamadı ve Mert'e baktı"
   - Cümle 8: «Hayri önce anlamadı ve Mert'e baktı.»
   - Açıklama: Anlamama ve sözün tekrarlanması olayı ilerletmeyen işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mert sözünü yavaşça tekrarladı"
   - Cümle 9: «Mert sözünü yavaşça tekrarladı.»
   - Açıklama: Anlamama ve sözü tekrarlama olaya hiçbir şey katmayan işlevsiz bir oyalanma.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0180` birebir aynı, ardından `@onarim: 516d0ef226f60a3bff5988731915f1a2568dd056`, sonra gövde.

### Hikâye 7: tohum hayri-0181 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0181
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'misket', fiil 'inanmak', sıfat 'dar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: misketler köklerin arasındaki dar yerlere kaçıyordu | baklava tepsisini düz bir yere koyup içinde oynadılar
@tohum: hayri-0181
Bir sabah Hayri ile Kamil kamp yerinde misket oynuyordu. Hayri çalıştığı dükkandan bir tepsi baklava getirmişti. Ama yerde çok kök ve taş vardı. Misketler hep köklerin arasındaki dar yerlere kaçıyordu. "Böyle oynayamayız, Hayri," dedi Kamil. Tepside iki dilim baklava kalmıştı. İkisi birer dilim yedi ve tepsi boşaldı. Hayri boş tepsiyi düz bir yere koydu. "Misketleri tepside oynayalım, bana inan!" dedi Hayri. "Peki, deneyelim," dedi Kamil. Tepsinin kenarları vardı ve misketler artık kaçmadı. Kamil kendi misketiyle Hayri'nin misketini itti. "Harika oldu, Hayri, tepsi en güzel oyun yeri!" dedi Kamil.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Misketler hep köklerin arasındaki dar yerlere kaçıyordu"
   - Cümle 4: «Misketler hep köklerin arasındaki dar yerlere kaçıyordu.»
   - Açıklama: Sorun açıkça ancak dördüncü cümlede söyleniyor; ilk üç cümlede yalnız kök ve taş anılıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İkisi birer dilim yedi"
   - Cümle 7: «İkisi birer dilim yedi ve tepsi boşaldı.»
   - Açıklama: 'İkisi' hemen önceki 'iki dilim baklava' ile karışıyor; Hayri ile Kamil'i gösterdiği açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0181` birebir aynı, ardından `@onarim: 35e82a1a60009778e130110f3842b955a7a06821`, sonra gövde.

### Hikâye 8: tohum hayri-0183 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0183
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'sebze', fiil 'binmek', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: karın altındaki taşlar yüzünden kızak takılıyordu | taşların üstüne bol kar taşıdı ve yol yaptı
@tohum: hayri-0183
@degisim: sebze -> kızak
Hayri parktaki küçük tepenin yeni karla bembeyaz olduğunu fark etti. Hemen kızağa bindi ama kızak biraz gidip durdu. Karın altında saklı küçük taşlar vardı ve kızak onlara takılıyordu. Hayri taşların üstüne kar taşımaya başladı. Biraz kar yeterdi ama Hayri abarttı ve durmadan kar getirdi. Böylece kalın, yumuşak bir yol yaptı. Artık taşlar hiç görünmüyordu. Hayri yeniden kızağa oturdu. Kızak bu yolda takılmadan en aşağıya kadar kaydı. Kızak durunca Hayri sevinçle güldü. Hayri tepeden kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama Hayri abarttı ve"
   - Cümle 5: «Biraz kar yeterdi ama Hayri abarttı ve durmadan kar getirdi.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama Hayri abarttı"
   - Cümle 5: «Biraz kar yeterdi ama Hayri abarttı ve durmadan kar getirdi.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelimedir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve durmadan kar getirdi"
   - Cümle 5: «Biraz kar yeterdi ama Hayri abarttı ve durmadan kar getirdi.»
   - Açıklama: Kartın özelliği olayları abartmaktır; burada abartma iş miktarını aşırıya kaçırmak olarak karttan farklı kullanılıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Artık taşlar hiç görünmüyordu"
   - Cümle 7: «Artık taşlar hiç görünmüyordu.»
   - Açıklama: Taşlar baştan beri karın altında saklıydı, yani önceden de görünmüyordu; 'artık görünmüyordu' demek çelişkili.
   - Açıklama: Taşlar baştan karın altında saklı olduğu halde artık görünmedikleri söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0183` birebir aynı, `@degisim: sebze -> kızak` (tutuyorsan), ardından `@onarim: c7a4811d69fb9aa1250767f8ff1fe0aa357c8902`, sonra gövde.

### Hikâye 9: tohum hayri-0186 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0186
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'koltuk', fiil 'yumuşamak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: sıkışmış koltuğu tek başına açamadı | arkadaşından yardım istedi ve birlikte açtılar
@tohum: hayri-0186
@degisim: yumuşamak -> açmak
Hayri ormandaki kamp yerinde küçük koltuğunu açmak istedi. Ama koltuk uzun süre kapalı kalmıştı ve sıkışmıştı. Hayri onu tek başına açamadı. Akın meşguldü, biraz uzakta çadırın ipini çekiyordu. "Akın, bu koltuğu yüz kez çektim, yardım et!" diye seslendi Hayri. Hayri biraz abartmıştı, koltuğu yalnız üç kez çekmişti. Akın bunu duyunca güldü, ipi bıraktı ve koşup geldi. "Yüz kez mi? Hadi, birlikte çekelim," dedi Akın. Akın koltuğun bir ucundan tuttu. Hayri de diğer ucundan çekti. Koltuk birden açıldı. Hayri hemen koltuğa oturdu. "Teşekkürler, Akın," dedi Hayri. Hayri çok sevindi, çünkü Akın'ın yardımıyla koltuğunu açmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Akın meşguldü, biraz uzakta"
   - Cümle 4: «Akın meşguldü, biraz uzakta çadırın ipini çekiyordu.»
   - Açıklama: 'Meşgul' kelimesini 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 6: «Hayri biraz abartmıştı, koltuğu yalnız üç kez çekmişti.»
   - Açıklama: 'Abartmak' soyut bir kavram ve küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı, koltuğu"
   - Cümle 6: «Hayri biraz abartmıştı, koltuğu yalnız üç kez çekmişti.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime; 'yüz kez' mübalağası da mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0186` birebir aynı, `@degisim: yumuşamak -> açmak` (tutuyorsan), ardından `@onarim: 06ede8a9ea43926924c581662621849975591ee9`, sonra gövde.

### Hikâye 10: tohum hayri-0187 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0187
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ip', fiil 'gitmek', sıfat 'vanilyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: kutunun ipi dala takıldı ve kutu çalılara düştü | köpekten yardım istedi ve kutuyu çalılarda buldu
@tohum: hayri-0187
@degisim: vanilyalı -> küçük
Hayri ormandaki kampa küçük bir kutu baklava getirmişti. Ağaçların arasında yürürken kutunun ipi bir dala takıldı. Kutu düştü ve sık çalıların arasına yuvarlandı. Hayri eğildi ama kutuyu göremedi. Biraz uzakta Yumak kuyruğunu sallıyordu. Hayri Yumak'ın yanına gitti ve başını okşadı. Hayri'nin eli dükkandaki baklavalar gibi kokuyordu. Elini Yumak'ın burnuna uzattı ve sonra çalıları gösterdi. Yumak eli kokladı ve çalılara doğru koştu. Burnuyla yaprakları itti ve yüksek sesle havladı. Hayri oraya baktı ve kutunun ipini gördü. İpi tuttu ve kutuyu dışarı çekti. Hayri kutuyu mutlu mutlu kampa götürdü, Yumak da yanında yürüdü.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri Yumak'ın yanına gitti ve başını okşadı"
   - Cümle 6: «Hayri Yumak'ın yanına gitti ve başını okşadı.»
   - Açıklama: Çözüm kutuyu çalılarda aramak yerine köpeğe gitmek, okşamak, el koklatmak ve çalıları göstermek gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0187` birebir aynı, `@degisim: vanilyalı -> küçük` (tutuyorsan), ardından `@onarim: 2a6700db03632dffbb172ce9f2f442ea16abcbc2`, sonra gövde.

### Hikâye 11: tohum hayri-0188 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0188
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bileklik', fiil 'sevmek', sıfat 'dikkatli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca yemeğini unutmuştu ve acıkmıştı | sandviçini ikiye ayırıp amcayla paylaştı
@tohum: hayri-0188
@degisim: bileklik -> sandviç
Hayri ormandaki kamp yerinde çantasını açtı. Basri Amca da yanına oturdu, ama yemeğini evde unutmuştu. Karnı acıkmıştı ve biraz üzüldü. Hayri çantasından büyük bir peynirli sandviç çıkardı. "Basri Amca, bunu sizinle paylaşalım mı?" diye sordu Hayri. "Olmaz, sonra sen aç kalırsın," dedi Basri Amca. "Bu sandviç benden bile büyük, Basri Amca!" dedi Hayri. Hayri biraz abartmıştı ama sandviç gerçekten büyüktü. Amca bunu duyunca güldü ve başını salladı. Hayri sandviçi dikkatli bir şekilde ikiye böldü. Bir parçayı amcaya uzattı. Basri Amca büyük bir ısırık aldı. "Peynirli sandviçi çok severim, teşekkür ederim, Hayri!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı ama"
   - Cümle 8: «Hayri biraz abartmıştı ama sandviç gerçekten büyüktü.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0188` birebir aynı, `@degisim: bileklik -> sandviç` (tutuyorsan), ardından `@onarim: 462292c46490458a8789d6f802ad76a9fd703d49`, sonra gövde.

### Hikâye 12: tohum hayri-0189 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0189
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'raf', fiil 'damlamak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı uyuduğu için sürprizi göremiyordu | ballı ekmek hazırladı ve kokusuyla arkadaşını uyandırdı
@tohum: hayri-0189
@degisim: kıvrımlı -> renkli
Rüzgar serin serin esiyordu. Hayri, Kamil'in doğum günü için kuma renkli kabuklarla bir kalp yapmıştı. Ama Kamil kitap okurken uyumuştu ve kalbi göremiyordu. Hayri de çok acıkmıştı ve ballı ekmek hazırlamaya başladı. Çantasından iki ekmek ve bakkalın rafından aldığı bal kavanozunu çıkardı. Kavanozu eğdi ve bal ekmeklerin üstüne yavaş yavaş damladı. Hayri, Kamil'i uyandırmak için bir ekmeği onun burnuna yaklaştırdı. Kamil burnunu oynattı ve gözlerini açtı. "Bu tatlı koku nereden geliyor?" diye sordu Kamil. Hayri ona ekmeği uzattı ve kumdaki kalbi gösterdi. "İyi ki doğdun, Kamil!" dedi Hayri. "Çok teşekkür ederim, Hayri, bu harika bir sürpriz!" dedi Kamil.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri de çok acıkmıştı"
   - Cümle 4: «Hayri de çok acıkmıştı ve ballı ekmek hazırlamaya başladı.»
   - Açıklama: Başka acıkan biri anlatılmadığı için 'de' bağlacı yersiz kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri de çok acıkmıştı ve ballı ekmek hazırlamaya başladı"
   - Cümle 4: «Hayri de çok acıkmıştı ve ballı ekmek hazırlamaya başladı.»
   - Açıklama: Çözümü getiren ballı ekmek sorundan değil tesadüfi bir açlıktan çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bakkalın rafından aldığı bal kavanozunu"
   - Cümle 5: «Çantasından iki ekmek ve bakkalın rafından aldığı bal kavanozunu çıkardı.»
   - Açıklama: Kumsalda olmayan bakkal rafı işlevsiz bir ayrıntı ve çözüm için gereken bal sebepsizce ortaya çıkıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri, Kamil'i uyandırmak için bir ekmeği onun burnuna yaklaştırdı"
   - Cümle 7: «Hayri, Kamil'i uyandırmak için bir ekmeği onun burnuna yaklaştırdı.»
   - Açıklama: Uyuyan arkadaşı uyandırmak için ekmek hazırlamak dolaylı bir çözüm; sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0189` birebir aynı, `@degisim: kıvrımlı -> renkli` (tutuyorsan), ardından `@onarim: e61d2a30dcb81859b224c4e207c181e317cff299`, sonra gövde.
