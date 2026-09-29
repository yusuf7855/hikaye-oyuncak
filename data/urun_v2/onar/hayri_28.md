# Editör görevi (onarım): Hayri, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0031 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0031
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ayakkabı', fiil 'temizlenmek', sıfat 'puantiyeli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: ıslak ayakkabı bağı kaydı ve çözüldü | yardım istedi ve arkadaşı bağı bağladı
@tohum: hayri-0031
@degisim: puantiyeli -> ıslak
Evin bahçesinde sıcak bir güneş parlıyordu. Hayri, Akın'a baklava dükkanından bir tepsi tatlı getiriyordu. Ayakkabısı yeni temizlenmişti, bu yüzden ıslak bağı kaydı ve çözüldü. Hayri'nin iki eli de tepsiyle doluydu ve bağı bağlayamadı. Tam o sırada Akın evinden bahçeye çıktı. "Akın, bu bağı bağlar mısın?" diye sordu Hayri. "Tabii, hemen," dedi Akın. Akın eğildi ve bağı sıkıca bağladı. Hayri artık rahatça yürüyebildi. Teşekkür etti ve tepsiyi Akın'a uzattı. Sonra ikisi bahçede oturdu ve tatlıları mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ayakkabısı yeni temizlenmişti, bu yüzden ıslak bağı kaydı"
   - Cümle 3: «Ayakkabısı yeni temizlenmişti, bu yüzden ıslak bağı kaydı ve çözüldü.»
   - Açıklama: Ayakkabının temizlenmiş olması bağın kendiliğinden çözülmesi için akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0031` birebir aynı, `@degisim: puantiyeli -> ıslak` (tutuyorsan), ardından `@onarim: 6d88cd2420a5004e4a1d27e587f5d081d5f168a1`, sonra gövde.

### Hikâye 2: tohum hayri-0057 (deneme 5 -> 6)

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
Hayri ile Akın parkta saklambaç oynuyordu. Hayri sayarken Akın'ın nereye saklanacağını çok merak etti. Bu yüzden gizlice gözlerini açtı. Akın bunu gördü ve çok üzüldü. "Hayri, sen bana baktın, bu olmaz!" dedi Akın. Hayri yanlış yaptığını anladı. "Haklısın, Akın, özür dilerim," dedi Hayri. Sonra dükkandan getirdiği baklavayı Akın'la paylaştı. Akın gülümsedi. Bu kez Hayri gözlerini sıkıca kapadı ve ona kadar saydı. Akın çimlerin üstünden koştu ve yuvarlak bir çalının arkasına gizlendi. Hayri parkı dolaştı ve sonunda Akın'ı buldu. İkisi birlikte güldü. "Çok güzel oynadık, Hayri, bir daha oynayalım!" dedi Akın.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "dükkandan getirdiği baklavayı Akın'la paylaştı"
   - Cümle 8: «Sonra dükkandan getirdiği baklavayı Akın'la paylaştı.»
   - Açıklama: Baklava paylaşmak sebebe yönelmeyen fazladan bir çözüm adımı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra dükkandan getirdiği baklavayı Akın'la paylaştı"
   - Cümle 8: «Sonra dükkandan getirdiği baklavayı Akın'la paylaştı.»
   - Açıklama: Baklava sebepsiz beliriyor ve saklambaç sorununun çözümünde bir işe yaramıyor.
   - Açıklama: Baklava sebepsiz beliriyor ve saklambaç sorunuyla ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0057` birebir aynı, ardından `@onarim: e64c049ada9bf339a7271692b41f4d8127bd8bef`, sonra gövde.

### Hikâye 3: tohum hayri-0061 (deneme 5 -> 6)

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
@plan: uçurtmanın kuyruğu yoktu ve uçurtma dönüp düşüyordu | atkısını uçurtmaya uzun bir kuyruk olarak bağladı
@tohum: hayri-0061
Rüzgar esiyordu ve gökyüzü beyaz bulutlarla doluydu. Hayri parkta ilk kez uçurtma uçurmayı deniyordu. Ama uçurtmanın kuyruğu yoktu ve uçurtma havada dönüp düşüyordu. Hayri uçurtmayı çimlere yaydı ve dikkatle baktı. Sonra boynundaki uzun kırmızı atkıyı çıkardı. Hayri abarttı ve uçurtmanın bulutlara kadar çıkacağını düşündü. Bu yüzden bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı. Hayri ipi tuttu ve rüzgara karşı koştu. Bu kez uçurtma hiç dönmedi. Kırmızı kuyruğuyla yavaş yavaş yükseldi. Hayri çok sevindi, çünkü ilk uçurtmasını kendisi uçurmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abarttı ve uçurtmanın"
   - Cümle 6: «Hayri abarttı ve uçurtmanın bulutlara kadar çıkacağını düşündü.»
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; Hayri bir şeyi abartmıyor, bir şey umuyor.
   - Açıklama: 'Abarttı' burada yanlış anlamda; Hayri bir şeyi abartmıyor, yalnız düşünüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve uçurtmanın"
   - Cümle 6: «Hayri abarttı ve uçurtmanın bulutlara kadar çıkacağını düşündü.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abarttı ve uçurtmanın bulutlara kadar çıkacağını düşündü"
   - Cümle 6: «Hayri abarttı ve uçurtmanın bulutlara kadar çıkacağını düşündü.»
   - Açıklama: Abartma özelliği zorla sokulmuş; bütün atkıyı bağlamanın sebebi olarak işlevsiz ve mantıksız kalıyor.
   - Açıklama: Abartma düşüncesi atkıyı bağlamanın sebebi olarak sunuluyor ama olaydan çıkmıyor ve hiçbir işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0061` birebir aynı, ardından `@onarim: a50e1fe15128c4a72585677671ffe78aa8368d8a`, sonra gövde.

### Hikâye 4: tohum hayri-0066 (deneme 5 -> 6)

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
@plan: köpek baklava kutusunu ağaçların arasına götürdü | köpekten yardım istedi ve kutuyu geri aldı
@tohum: hayri-0066
@degisim: ödemek -> koklamak
Ormandaki kamp yerinde Hayri küçük bir zil çalıyor, Yumak da sese koşuyordu. Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi. Ama Yumak kutuyu ağzına aldı, ağaçların arasına koştu ve kutusuz döndü. Hayri her yere baktı ama kutuyu bulamadı. "Yumak, kutuyu bulmama yardım eder misin?" diye sordu Hayri. Yumak burnuyla yeri kokladı. Sonra ağaçların arasına koştu ve kutuyu ağzında geri getirdi. Hayri kutuyu açtı ve baklavaların hepsinin yerinde olduğunu gördü. Sonra Hayri ile Yumak zil oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Yumak burnuyla yeri kokladı"
   - Cümle 6: «Yumak burnuyla yeri kokladı.»
   - Açıklama: Kutuyu ağaçların arasına kendisi götüren Yumak onu koklayarak aramak zorunda kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0066` birebir aynı, `@degisim: ödemek -> koklamak` (tutuyorsan), ardından `@onarim: 4aef4c39f729646e7ae8affbc0bed382d379bc1b`, sonra gövde.

### Hikâye 5: tohum hayri-0071 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0071
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'scooter', fiil 'sormak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: kütük çok sertti ve arkadaşı rahat oturamadı | çadırdan tüylü battaniyesini getirip kütüğe serdi
@tohum: hayri-0071
@degisim: scooter -> kitap
Bir sabah Hayri kamp yerinde Kamil ile oturuyordu. Kamil bir kütüğün üstünde kitap okumak istedi. Ama kütük çok sertti ve Kamil hemen ayağa kalktı. Hayri ona ne olduğunu sordu. Kamil kütüğün çok sert olduğunu söyledi. Hayri hemen çadıra koştu ve tüylü battaniyesini getirdi. Battaniyeyi ikiye katladı ve kütüğün üstüne serdi. Hayri biraz abarttı ve bunun ormandaki en yumuşak yer olduğunu söyledi. Kamil güldü ve battaniyenin üstüne oturdu. Kütük artık hiç sert değildi. Hayri de Kamil'in yanına oturdu. İki arkadaş kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 8: «Hayri biraz abarttı ve bunun ormandaki en yumuşak yer olduğunu söyledi.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0071` birebir aynı, `@degisim: scooter -> kitap` (tutuyorsan), ardından `@onarim: d65e1138f570ed6b9dcbe57eb554e7d269a8d406`, sonra gövde.

### Hikâye 6: tohum hayri-0072 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0072
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyonet', fiil 'ayırmak', sıfat 'özel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı | kumu elleriyle iki yana ayırıp kamyoneti çekti
@tohum: hayri-0072
Dalgalar kıyıya yavaşça vuruyordu. Hayri ile Akın, oyuncak kamyoneti kumla doldurup bir tepe yapıyordu. Birden küçük bir dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı. Hayri olayı abarttı. "Kamyonet denizin dibine gidiyor!" dedi Hayri. Akın güldü. "Hayır, yalnız tekerlekleri battı," dedi Akın. Hayri tekerleklerin önündeki kumu elleriyle iki yana ayırdı. Sonra kamyoneti yavaşça çekti ve kumdan çıkardı. "Teşekkürler, Hayri, bu kamyonet benim için çok özel!" dedi Akın. İki arkadaş kamyoneti dalgalardan uzağa, kuru kuma götürdü. Orada tepeyi büyütmeye mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri olayı abarttı."
   - Cümle 4: «Hayri olayı abarttı.»
   - Açıklama: 'Olayı abarttı' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Olayı abartmak' soyut bir anlatım, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0072` birebir aynı, ardından `@onarim: 80a50d2a6d5a0918ef7d50c2e396530c219b08e3`, sonra gövde.

### Hikâye 7: tohum hayri-0074 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0074
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kumbara', fiil 'yankılanmak', sıfat 'kaygan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: yüksek sesle bağırdı ve uyuyan köpeği korkuttu | uzaktan özür diledi ve köpek yanına geldi
@tohum: hayri-0074
@degisim: kumbara -> simit
Bir sabah Hayri kamp yerinde çok acıkmıştı. Hayri masadan bir simit aldı ve "Kahvaltı hazır!" diye yüksek sesle bağırdı. Hayri'nin sesi ormanda yankılandı ve uyuyan Yumak birden uyandı. Yumak korktu ve çadırın arkasına koştu. Hayri simidi yemedi ve masaya geri koydu. Yumak'ın yanına gitmek istedi ama çadırın arkasındaki toprak kaygandı. Bu yüzden çadırın önünde yere oturdu. "Özür dilerim, Yumak, seni korkuttum," dedi Hayri yavaşça. Yumak başını çadırın arkasından çıkardı. Sonra kuyruğunu sallayarak Hayri'nin yanına geldi. Hayri simidini aldı ve Yumak'ın yanında yedi. Hayri bundan sonra Yumak uyurken hep alçak sesle konuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesi ormanda yankılandı"
   - Cümle 3: «Hayri'nin sesi ormanda yankılandı ve uyuyan Yumak birden uyandı.»
   - Açıklama: 'Yankılanmak' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çadırın arkasındaki toprak kaygandı"
   - Cümle 6: «Yumak'ın yanına gitmek istedi ama çadırın arkasındaki toprak kaygandı.»
   - Açıklama: Kaygan toprak yalnızca Hayri'yi uzakta tutmak için sebepsizce kurulmuş yapay bir engel.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0074` birebir aynı, `@degisim: kumbara -> simit` (tutuyorsan), ardından `@onarim: 927eeaa54a5ac3f296315427dc456deedde23df9`, sonra gövde.

### Hikâye 8: tohum hayri-0079 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0079
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kanepe', fiil 'çırpmak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: rüzgar esti ve örtünün kenarları havaya kalktı | örtünün dört ucuna büyük taşlar koydu
@tohum: hayri-0079
@degisim: kanepe -> kurabiye
Bir sabah Hayri kıyıda Akın'ın doğum günü için bir sürpriz hazırlıyordu. Kumun üstüne bir örtü serdi ve kurabiyeleri dizdi. Ama rüzgar esti ve örtünün kenarları havaya kalktı. Kurabiyeler kuma kaymaya başladı. Hayri çevreye baktı ve dört büyük taş topladı. Taşları örtünün dört ucuna koydu. Örtünün kenarları artık kalkmadı ve kurabiyeler yerinde durdu. Hayri çok acıkmıştı ama Akın'ı bekledi. Akın kıyıya geldi. Hayri ellerini çırptı. "İyi ki doğdun, Akın!" dedi Hayri sevecen bir sesle. Akın hemen Hayri'ye sarıldı. "Bu en güzel sürpriz," dedi Akın. İkisi kurabiyeleri birlikte yedi. Hayri bundan sonra rüzgarlı günlerde örtünün ucuna hep taş koydu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri sevecen bir sesle"
   - Cümle 11: «"İyi ki doğdun, Akın!" dedi Hayri sevecen bir sesle.»
   - Açıklama: 'Sevecen' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Sevecen' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0079` birebir aynı, `@degisim: kanepe -> kurabiye` (tutuyorsan), ardından `@onarim: 0d2ce0e6691c8a377bc68df2a1f14f805c3ff0dd`, sonra gövde.

### Hikâye 9: tohum hayri-0080 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Kamil
@tohum: hayri-0080
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yüzük', fiil 'bitmek', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Kamil
@plan: garip bir ses geldi ve arkadaşı kitap okuyamadı | sesin karnından geldiğini buldu ve simidini paylaştı
@tohum: hayri-0080
Parkta hafif bir rüzgar esiyordu ve gökyüzü masmaviydi. Hayri ile Kamil bir bankta oturuyordu. Kamil kitap okumak istedi ama yakından garip bir ses geliyordu. "Hayri, bu ses nereden geliyor?" diye sordu Kamil. Hayri bankın altına baktı ama bir şey göremedi. Ses yine geldi ve bu kez Hayri'nin karnından geldi. Hayri çok acıkmıştı, bu yüzden karnı guruldamıştı. Hayri güldü ve çantasından yüzük gibi yuvarlak bir simit çıkardı. Simidi ikiye böldü ve yarısını Kamil'e verdi. Simit çabucak bitti ve Hayri'nin karnı bir daha ses çıkarmadı. "Şimdi kitabımı okuyabilirim," dedi Kamil. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bu kez Hayri'nin karnından geldi"
   - Cümle 6: «Ses yine geldi ve bu kez Hayri'nin karnından geldi.»
   - Açıklama: 'Bu kez' sesin önce başka yerden geldiğini ima ediyor, oysa sebep baştan beri Hayri'nin karnı; Hayri kendi karnının guruldamasını fark etmeyip bankın altına bakıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ses yine geldi ve bu kez Hayri'nin karnından geldi"
   - Cümle 6: «Ses yine geldi ve bu kez Hayri'nin karnından geldi.»
   - Açıklama: Ses baştan beri Hayri'nin karnından gelirken 'bu kez' deniyor ve Hayri kendi karnının guruldadığını fark etmeyip bankın altına bakıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yüzük gibi yuvarlak bir simit"
   - Cümle 8: «Hayri güldü ve çantasından yüzük gibi yuvarlak bir simit çıkardı.»
   - Açıklama: Benzetme kullanılmış; mecazsız somut anlatım isteniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0080` birebir aynı, ardından `@onarim: 18007697adda4792d56a629c326dde747f0d2414`, sonra gövde.

### Hikâye 10: tohum hayri-0081 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0081
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'top', fiil 'saklamak', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga kum tepesini yıktı ve top kayboldu | kumun yüksek kalan yerini kazdı ve topu buldu
@tohum: hayri-0081
@degisim: nazik -> sarı
Dalgaların sesi kıyıdan geliyordu. Hayri sarı topunu kuma sakladı ve üstüne abartarak kocaman bir tepe yaptı. Ama bir dalga tepeyi yıktı ve Hayri topun yerini bulamadı. Hayri eğildi ve kuma dikkatle baktı. Tepe çok büyük olduğu için bir yerde kum biraz yüksek kalmıştı. Hayri orayı elleriyle kazdı. Kumun altından sarı top çıktı. Hayri topu iki eliyle havaya kaldırdı ve güldü. Sonra topu dalgalardan uzağa, kuru kuma gömdü. Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "üstüne abartarak kocaman bir tepe"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve üstüne abartarak kocaman bir tepe yaptı.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 3 yaşındaki çocuk için anlaşılır değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "üstüne abartarak kocaman bir tepe"
   - Cümle 2: «Hayri sarı topunu kuma sakladı ve üstüne abartarak kocaman bir tepe yaptı.»
   - Açıklama: Karttaki özellik olayları abartmayı sevmek iken burada abartma kum tepesi yapmak için kelime olarak kullanılıyor, karttaki gibi değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0081` birebir aynı, `@degisim: nazik -> sarı` (tutuyorsan), ardından `@onarim: 17725ade63eb217b4ce42745b27c18b6105f0f36`, sonra gövde.

### Hikâye 11: tohum hayri-0083 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0083
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tekne', fiil 'silkmek', sıfat 'kalın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek kuru yapraklarla oynuyordu ve tekneye gelmedi | ekmekten bir parça uzatıp köpeği tekneye çağırdı
@tohum: hayri-0083
Ormanda büyük ağaçların altında kalın bir kütük vardı. Hayri tekne oyunu oynuyordu ve kütük onun teknesiydi. Ama Yumak tekneye gelmedi, çünkü kuru yapraklarla oynuyordu. "Yumak, gel, yola çıkıyoruz!" dedi Hayri. Yumak ona hiç bakmadı. Hayri acıkmıştı, bu yüzden çantasından ekmeğini çıkardı. Ekmekten küçük bir parça kopardı ve Yumak'a uzattı. "Bu parça senin, Yumak!" dedi Hayri. Yumak ekmeğin kokusunu aldı ve koşarak geldi. Tekneye atladı ve tüylerindeki yaprakları silkti. Sonra parçayı yedi ve kuyruğunu salladı. Hayri de ekmeğin kalanını yedi. Hayri ile Yumak tekne oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri acıkmıştı, bu yüzden çantasından ekmeğini çıkardı"
   - Cümle 6: «Hayri acıkmıştı, bu yüzden çantasından ekmeğini çıkardı.»
   - Açıklama: Çözümü getiren ekmek Hayri'nin açlığıyla tesadüfen çıkıyor, köpeği çağırma düşüncesinden doğmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0083` birebir aynı, ardından `@onarim: 1c12d62a90ad87f9e4d2a4f2421f5586bb6479c3`, sonra gövde.

### Hikâye 12: tohum hayri-0084 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0084
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ay', fiil 'vermek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: koşarken arkadaşına çarptı ve onun sütü döküldü | özür diledi, bardağını doldurdu ve baklava verdi
@tohum: hayri-0084
Bir akşam kamp masasında ılık süt ve baklava vardı. Hayri gökyüzünde büyük bir ay gördü. Hayri, Mert'e gökyüzünü göstermek için koşarken ona çarptı ve Mert'in sütü döküldü. Mert boş bardağına üzgün üzgün baktı. Hayri hemen durdu ve Mert'in yanına gitti. "Özür dilerim, Mert, koşmamalıydım," dedi Hayri. Sonra masadaki sütten Mert'in bardağını yeniden doldurdu. Hayri bu baklavaları çalıştığı dükkandan getirmişti. Hayri en büyük baklavayı Mert'e verdi. Mert onu yedi ve gülümsedi. "Çok güzelmiş, teşekkür ederim," dedi Mert. "Hadi, Mert, şimdi aya birlikte bakalım!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri en büyük baklavayı Mert'e verdi"
   - Cümle 9: «Hayri en büyük baklavayı Mert'e verdi.»
   - Açıklama: Sorun bardak doldurulunca çözülmüşken baklava vermek çözümü üçüncü bir adıma uzatıyor.
   - Açıklama: Süt yeniden doldurulunca sorun çözülmüş olmasına rağmen çözüm özür, doldurma ve baklava ile ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0084` birebir aynı, ardından `@onarim: c54575aee9dcb54d29390ae3980a3c4dde0ec791`, sonra gövde.
