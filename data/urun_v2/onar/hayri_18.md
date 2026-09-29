# Editör görevi (onarım): Hayri, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0061 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0061
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'atkı', fiil 'yaymak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: uçurtmanın kuyruğu yoktu ve uçurtma dönüp düşüyordu | atkısını uçurtmaya kuyruk olarak bağladı
@tohum: hayri-0061
Rüzgar esiyordu ve gökyüzü beyaz bulutlarla doluydu. Hayri parkta ilk kez uçurtma uçurmayı deniyordu. Ama uçurtmanın kuyruğu yoktu ve uçurtma havada dönüp düşüyordu. Hayri uçurtmayı çimlere yaydı ve dikkatle baktı. Sonra boynundaki uzun kırmızı atkıyı çıkardı. Atkıyı uçurtmanın alt ucuna sıkıca bağladı. Hayri ipi tuttu ve rüzgara karşı koştu. Bu kez uçurtma hiç dönmedi. Kırmızı kuyruğuyla yavaş yavaş yükseldi. Hayri abartarak uçurtmasının bulutlara değdiğini düşündü. Hayri çok sevindi, çünkü ilk uçurtmasını kendisi uçurmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak uçurtmasının bulutlara değdiğini düşündü"
   - Cümle 10: «Hayri abartarak uçurtmasının bulutlara değdiğini düşündü.»
   - Açıklama: 'Abartarak düşünmek' yanlış kullanım; fiil ve zarf uyuşmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak uçurtmasının bulutlara değdiğini düşündü"
   - Cümle 10: «Hayri abartarak uçurtmasının bulutlara değdiğini düşündü.»
   - Açıklama: 'Abartarak' soyut bir kelimedir ve 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak uçurtmasının bulutlara"
   - Cümle 10: «Hayri abartarak uçurtmasının bulutlara değdiğini düşündü.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak uçurtmasının bulutlara değdiğini düşündü"
   - Cümle 10: «Hayri abartarak uçurtmasının bulutlara değdiğini düşündü.»
   - Açıklama: Tohumdaki abartma özelliği sorun çözüldükten sonra süs olarak ekleniyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki abartma özelliği sona iliştirilmiş, sorunun çözümünde ya da olayda işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak uçurtmasının bulutlara değdiğini düşündü"
   - Cümle 10: «Hayri abartarak uçurtmasının bulutlara değdiğini düşündü.»
   - Açıklama: Abartma cümlesi olaydan çıkmıyor ve hikayede işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0061` birebir aynı, ardından `@onarim: eac981b28dfbb818d8f1a0907815a3ab893ed848`, sonra gövde.

### Hikâye 2: tohum hayri-0063 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0063
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'elbise', fiil 'kurtarmak', sıfat 'şekerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: şekerli elleriyle arkadaşının beyaz gömleğine dokundu | özür diledi ve lekeyi ıslak peçeteyle sildi
@tohum: hayri-0063
@degisim: elbise -> gömlek
Bir sabah Hayri ile Akın ormandaki kamp yerindeydi. Hayri, çalıştığı baklava dükkanından bir kutu baklava getirmişti. Bir baklava yedi ve ellerini yıkamadan Akın'ın beyaz gömleğine dokundu. Gömlekte yapışkan bir leke kaldı. "Hayri, gömleğim kirlendi!" dedi Akın. Hayri lekeye baktı ve yanlış yaptığını anladı. "Özür dilerim, Akın, ellerim şekerliydi," dedi Hayri. Sonra gömleği kurtarmak için bir peçeteyi şişedeki suyla ıslattı. Lekeyi yavaşça sildi ve gömlek yine bembeyaz oldu. Akın gülümsedi ve Hayri'ye teşekkür etti. Bu kez ikisi de önce ellerini suyla yıkadı. Sonra Hayri ile Akın baklavaları mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gömleği kurtarmak için"
   - Cümle 8: «Sonra gömleği kurtarmak için bir peçeteyi şişedeki suyla ıslattı.»
   - Açıklama: Gömleği 'kurtarmak' mecazlı bir kullanım; çocuğa uygun değil.
   - Açıklama: Gömleği 'kurtarmak' mecazlı bir kullanım, 3 yaşına uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0063` birebir aynı, `@degisim: elbise -> gömlek` (tutuyorsan), ardından `@onarim: 1037ef1be17041d2ad8f5f290d0c6b3959564f70`, sonra gövde.

### Hikâye 3: tohum hayri-0065 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0065
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: turuncu çiçek kapalıydı çünkü güneş gelmemişti | baklava yiyerek güneşin gelmesini bekledi
@tohum: hayri-0065
@degisim: patik -> çiçek
Ormandaki kamp yerinde hava serindi. Hayri, Basri Amca ile turuncu bir çiçeğin yanında oturuyordu. Çiçek daha kapalıydı, çünkü güneş ağaçların arkasındaydı. "Güneş gelince çiçek açılacak," dedi Basri Amca. Hayri çiçeğin açılmasını görmek istiyordu. Çalıştığı baklava dükkanından getirdiği kutunun kapağını kaldırdı. "Beklerken birer baklava yiyelim mi, Basri Amca?" diye sordu Hayri. Basri Amca gülümsedi ve bir dilim aldı. İkisi yavaş yavaş yedi ve çiçeğe baktı. Az sonra güneş dalların arasından ona ulaştı. Turuncu çiçek yavaşça açıldı. "Basri Amca, iyi ki birlikte bekledik!" dedi Hayri.
```

**Hakem bulguları (5):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "baklava yiyerek güneşin gelmesini bekledi"
   - Cümle 0 (plan satırı): «turuncu çiçek kapalıydı çünkü güneş gelmemişti | baklava yiyerek güneşin gelmesini bekledi»
   - Açıklama: Baklava yemek sebebe, yani güneşin gelmemesine hiç yönelmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çiçek daha kapalıydı, çünkü güneş ağaçların arkasındaydı"
   - Cümle 3: «Çiçek daha kapalıydı, çünkü güneş ağaçların arkasındaydı.»
   - Açıklama: Çiçeğin henüz açılmamış olması doğal bir durum, çocuğun önemseyeceği gerçek bir sorun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalıştığı baklava dükkanından getirdiği kutunun"
   - Cümle 6: «Çalıştığı baklava dükkanından getirdiği kutunun kapağını kaldırdı.»
   - Açıklama: Baklava kutusu çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dalların arasından ona ulaştı"
   - Cümle 10: «Az sonra güneş dalların arasından ona ulaştı.»
   - Açıklama: 'Ona' zamirinin çiçeği mi Hayri'yi mi gösterdiği belli değil.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Az sonra güneş dalların arasından ona ulaştı"
   - Cümle 10: «Az sonra güneş dalların arasından ona ulaştı.»
   - Açıklama: Çiçeği Hayri değil kendiliğinden gelen güneş açıyor; figür sorunu çözmüyor.
   - Açıklama: Sorunu Hayri çözmüyor; güneş kendiliğinden gelince çiçek açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0065` birebir aynı, `@degisim: patik -> çiçek` (tutuyorsan), ardından `@onarim: dd1dc27150650db916d673a903e2cef2b7a5e6c9`, sonra gövde.

### Hikâye 4: tohum hayri-0066 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0066
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zil', fiil 'ödemek', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek baklava kutusunu ağaçların arasına götürdü | köpekten yardım istedi ve zilin sesini izledi
@tohum: hayri-0066
@degisim: ödemek -> koklamak
Ormandaki kamp yerinde Hayri, Yumak ile oynuyordu. Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi. Ama Yumak kutuyu ağzına aldı, ağaçların arasına koştu ve kutusuz döndü. Hayri her yere baktı ama kutuyu bulamadı. "Yumak, kutuyu bulmama yardım eder misin?" diye sordu Hayri. Yumak yeri kokladı ve havladı. Sonra ağaçların arasına doğru koştu. Yumak'ın boynundaki zil çın çın öttü. Hayri zilin sesini izledi ve Yumak'ın peşinden yürüdü. Kutu büyük bir ağacın dibindeydi. Hayri kutuyu açtı ve baklavaların hepsinin orada olduğunu gördü. Sonra Hayri ile Yumak kamp yerine mutlu mutlu geri döndü.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "boynundaki zil çın çın öttü"
   - Cümle 8: «Yumak'ın boynundaki zil çın çın öttü.»
   - Açıklama: Zil ötmez, çalar; fiil öznesine uymuyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Yumak'ın boynundaki zil çın çın öttü"
   - Cümle 8: «Yumak'ın boynundaki zil çın çın öttü.»
   - Açıklama: Kartın yanlar bölümünde Yumak'ın boynunda zil gibi bir eşya yok; çözüm kartta olmayan bu eşyaya dayanıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yumak'ın boynundaki zil çın çın öttü"
   - Cümle 8: «Yumak'ın boynundaki zil çın çın öttü.»
   - Açıklama: Zil önceden kurulmadan çözüm anında sebepsizce beliriyor.
   - Açıklama: Zil daha önce hiç kurulmadan çözüm anında sebepsizce beliriyor, üstelik Hayri zaten Yumak'ın peşinden yürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0066` birebir aynı, `@degisim: ödemek -> koklamak` (tutuyorsan), ardından `@onarim: 977b10f8bb72bbac7b4421e42593bb6815893595`, sonra gövde.

### Hikâye 5: tohum hayri-0067 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0067
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kavun', fiil 'esmek', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: tepsi sallandı ve yuvarlak kavun yere düştü | tepsiyi iki eliyle düz tuttu ve yavaşça yürüdü
@tohum: hayri-0067
@degisim: simsiyah -> yuvarlak
Ormanda serin bir rüzgar esiyordu. Hayri kamp yerinde yuvarlak bir kavunla tepsi oyunu oynuyordu. Ama tepsi sallandı ve kavun yere düştü. Hayri kavunu büyük ağaca kadar götürmek istiyordu. Hayri kavunu yerden aldı ve düşündü. Hayri, çalıştığı baklava dükkanında çok tepsi taşımıştı. Tepsiyi iki eliyle düz tuttu. Kavunu tam ortaya koydu. Sonra küçük adımlarla yavaş yavaş yürüdü. Kavun hiç kıpırdamadı. Hayri ağaçların arasından geçti ve büyük ağaca ulaştı. Hayri çok sevindi, çünkü kavunu hiç düşürmeden taşımıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kavunla tepsi oyunu oynuyordu"
   - Cümle 2: «Hayri kamp yerinde yuvarlak bir kavunla tepsi oyunu oynuyordu.»
   - Açıklama: 'Tepsi oyunu' belirsiz ve anlamı açık olmayan bir ifade.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama tepsi sallandı ve kavun yere düştü"
   - Cümle 3: «Ama tepsi sallandı ve kavun yere düştü.»
   - Açıklama: Tepsinin neden sallandığı söylenmiyor ve ormanda kavunla tepsi oyunu akla yatkın bir sorun kurmuyor.
   - Açıklama: Tepsinin neden sallandığı söylenmiyor, sorunun sebebi eksik.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri kavunu yerden aldı"
   - Cümle 5: «Hayri kavunu yerden aldı ve düşündü.»
   - Açıklama: 'Hayri' adı art arda üç cümlede gereksiz yere tekrarlanıyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kavunu tam ortaya koydu"
   - Cümle 8: «Kavunu tam ortaya koydu.»
   - Açıklama: Neyin ortası olduğu eksik; 'tepsinin ortasına' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0067` birebir aynı, `@degisim: simsiyah -> yuvarlak` (tutuyorsan), ardından `@onarim: c2b4280cd82b2d695d3dc5db569d4c1e9ae9382d`, sonra gövde.

### Hikâye 6: tohum hayri-0068 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0068
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'zincir', fiil 'olgunlaşmak', sıfat 'tertemiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: erikler olgunlaşmıştı ama çok yüksek bir daldaydı | arkadaşından yardım istedi ve erikleri topladı
@tohum: hayri-0068
@degisim: zincir -> dal
Güneş sokağı ısıtıyordu. Hayri ile Mert sokaktaki erik ağacının altında oturuyordu. Hayri acıkmıştı ama olgunlaşmış erikler çok yüksek bir daldaydı. Hayri zıpladı ama erikleri tutamadı. "Mert, sen benden uzunsun, bana yardım eder misin?" diye sordu Hayri. Mert ayağa kalktı ve dalın ucunu tuttu. Dalı yavaşça aşağı çekti. Hayri erikleri tek tek topladı. Sonra erikleri çeşmede yıkadı ve erikler tertemiz oldu. "Teşekkürler, Mert!" dedi Hayri. Hayri ile Mert erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Güneş sokağı ısıtıyordu"
   - Cümle 1: «Güneş sokağı ısıtıyordu.»
   - Açıklama: Başlıktaki yer ev olduğu halde hikaye sokaktaki erik ağacının altında geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Mert sokaktaki erik ağacının altında oturuyordu"
   - Cümle 2: «Hayri ile Mert sokaktaki erik ağacının altında oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0068` birebir aynı, `@degisim: zincir -> dal` (tutuyorsan), ardından `@onarim: 777c0816b2db75b91afd3da54c42f5069f887bef`, sonra gövde.
