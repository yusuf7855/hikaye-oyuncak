# Editör görevi (onarım): Maşa, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 4 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar29.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0119 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0119
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'eldiven', fiil 'toplamak', sıfat 'beyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: utangaç sincap fındık almak için yanına gelmedi | fındıkları kütüğe koyup geri çekildi ve bekledi
@tohum: masa-0119
Rüzgar soğuk soğuk esiyordu. Maşa beyaz eldivenlerini takmış, ağacın altında fındık topluyordu. Fındıklarını sincapla paylaşmak istedi, ama utangaç sincap onu görünce dala kaçtı. "Gel, sincap, bu fındıklar senin!" dedi Maşa. Ama sincap aşağı inmedi. Maşa hemen başka bir yol denedi. Sepetinden bir avuç fındık aldı ve yakındaki bir kütüğün üstüne koydu. Sonra birkaç adım geri gitti ve sessizce bekledi. Sincap daldan yavaşça indi. Fındıkları tek tek ağzına aldı. Maşa sevinçle ellerini çırptı. Sonra ikisi ağacın altında birlikte fındık toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen başka bir yol denedi"
   - Cümle 6: «Maşa hemen başka bir yol denedi.»
   - Açıklama: 'Yol' burada yöntem anlamında mecazlı kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa hemen başka bir yol denedi"
   - Cümle 6: «Maşa hemen başka bir yol denedi.»
   - Açıklama: 'Başka bir yol denemek' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0119` birebir aynı, ardından `@onarim: c59f063927a6e177d6c6b5a319989259918db761`, sonra gövde.

### Hikâye 2: tohum masa-0120 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0120
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'küp', fiil 'doldurmak', sıfat 'açık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: patikadaki çilekler daha yeşildi | güneşli açık yeri fark edip kırmızı çilek topladı
@tohum: masa-0120
Hafif bir rüzgar esiyordu ve güneş ormanı ısıtıyordu. Maşa elinde küçük bir küple patikada yürüyordu. Reçel için küpü doldurmak istedi, ama patikadaki çilekler daha yeşildi. Maşa etrafa dikkatle baktı ve bir şey fark etti. Ağaçların altındaki çilekler yeşildi, ama güneşte olan çilekler kırmızıydı. Maşa ağaçların arasındaki açık bir yere koştu. Burası güneşliydi ve çimenlerde çok kırmızı çilek vardı. Maşa en kırmızı çilekleri tek tek topladı ve küpe koydu. Az sonra küp doldu. Maşa dolu küpü kucakladı ve mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "patikadaki çilekler daha yeşildi"
   - Cümle 3: «Reçel için küpü doldurmak istedi, ama patikadaki çilekler daha yeşildi.»
   - Açıklama: 'Daha' burada 'henüz' anlamında ama karşılaştırma gibi okunabiliyor; anlam belirsiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama patikadaki çilekler daha yeşildi"
   - Cümle 3: «Reçel için küpü doldurmak istedi, ama patikadaki çilekler daha yeşildi.»
   - Açıklama: 'Daha yeşildi' 'daha çok yeşil' diye okunabiliyor; 'henüz yeşildi' anlamı belirsiz.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimenlerde çok kırmızı çilek vardı"
   - Cümle 7: «Burası güneşliydi ve çimenlerde çok kırmızı çilek vardı.»
   - Açıklama: 'Çok kırmızı' hem 'çok sayıda' hem 'koyu kırmızı' diye okunabiliyor, anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0120` birebir aynı, ardından `@onarim: 6b25276fa0492f4480c10a623b30c22560654c5a`, sonra gövde.

### Hikâye 3: tohum masa-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0122
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kabak', fiil 'yoğurmak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: fındıklar kaygan tatlının üstünden yere yuvarlandı | tatlıya reçel sürüp fındıkları üstüne dizdi
@tohum: masa-0122
@degisim: yoğurmak -> süslemek
Bir sabah Maşa'nın kuzeni Daşa şehirden ziyarete gelecekti. Maşa ormanda kütüğün üstüne bir tabak kabak tatlısı koydu. Tatlıyı fındıklarla süslemek istedi, ama tatlı kaygandı ve fındıklar hep yere yuvarlandı. Simsiyah gözlü sincap düşen fındıkları tek tek geri getirdi. Maşa'nın sepetinde en sevdiği çilek reçeli de vardı. Maşa kavanozu açtı ve tatlının üstüne ince ince reçel sürdü. Sonra fındıkları reçelin üstüne güzelce dizdi. Bu kez fındıklar reçele yapıştı ve hiç düşmedi. Tam o sırada Daşa patikadan geldi. Maşa sevinçle kütüğü gösterdi. Daşa süslü tatlıyı görünce güldü ve Maşa'ya sarıldı. Maşa çok sevindi, çünkü sürprizi Daşa gelmeden bitmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın sepetinde en sevdiği çilek reçeli de vardı"
   - Cümle 5: «Maşa'nın sepetinde en sevdiği çilek reçeli de vardı.»
   - Açıklama: Reçel önceden kurulmadan tam gerektiği anda sepette beliriyor ve çözümü sebepsizce getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sürprizi Daşa gelmeden bitmişti"
   - Cümle 12: «Maşa çok sevindi, çünkü sürprizi Daşa gelmeden bitmişti.»
   - Açıklama: Sürpriz bitmez; 'sürprizini bitirmişti' ya da 'sürprizi hazırdı' olmalı.
   - Açıklama: Sürpriz bitmez; 'hazırdı' ya da 'bitirmişti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0122` birebir aynı, `@degisim: yoğurmak -> süslemek` (tutuyorsan), ardından `@onarim: 008a9291f3124797d2f45a15d510183bed67a17e`, sonra gövde.

### Hikâye 4: tohum masa-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0124
- yer: dağ (Ormanın yanındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'maske', fiil 'atlamak', sıfat 'çabuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: maske zıplarken gözlerinin üstüne kaydı | maskeyi yüzünden alıp başının üstüne taktı
@tohum: masa-0124
Tepedeki yumuşak çimenlerde Maşa zıplama oyunu oynuyordu. Yüzünde kağıttan, uzun kulaklı bir maske vardı ve ağaca kadar atlayarak gidecekti. Ama maske büyüktü ve her zıpladığında gözlerinin üstüne kaydı. Maşa önünü göremedi ve durdu. Koca Ayı ile kirpi merakla ona baktı. Maşa hemen yeni bir şey denedi. Maskeyi yüzünden aldı ve başının üstüne taktı. Şimdi maskenin kulakları yukarıdaydı ve Maşa her yeri görüyordu. "Koca Ayı, kirpi, haydi benimle zıplayın!" dedi Maşa. Maşa çabuk çabuk zıplayarak ağaca ilk vardı. Koca Ayı ağır ağır, kirpi de küçük adımlarla arkasından geldi. Sonra üçü ağacın altında zıplama oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "maske zıplarken gözlerinin"
   - Cümle 0 (plan satırı): «maske zıplarken gözlerinin üstüne kaydı | maskeyi yüzünden alıp başının üstüne taktı»
   - Açıklama: Zıplayan maske değil Maşa; '-ken' yan cümlesi yanlış özneye bağlanıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir maske vardı ve ağaca kadar atlayarak gidecekti"
   - Cümle 2: «Yüzünde kağıttan, uzun kulaklı bir maske vardı ve ağaca kadar atlayarak gidecekti.»
   - Açıklama: Bağlı iki yüklemin öznesi farklı (maske ve Maşa), cümle bozuk.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "her zıpladığında gözlerinin üstüne kaydı"
   - Cümle 3: «Ama maske büyüktü ve her zıpladığında gözlerinin üstüne kaydı.»
   - Açıklama: Özne 'maske' iken 'zıpladığında' Maşa'ya bağlanıyor ve 'her' ile 'kayıyordu' gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0124` birebir aynı, ardından `@onarim: b836537c3c4dc63a0a2237fe8a5ddb1793b8adf5`, sonra gövde.
