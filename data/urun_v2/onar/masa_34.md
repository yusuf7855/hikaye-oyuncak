# Editör görevi (onarım): Maşa, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0151 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0151
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bez', fiil 'korumak', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ormanda tatlı bir reçel kokusu vardı | her yeri kokladı ve kokuyu kendi sepetinde buldu
@tohum: masa-0151
Maşa sepetiyle ormandaki patikada yürüyordu. Birden tatlı bir reçel kokusu aldı. Maşa bu kokunun nereden geldiğini çok merak etti. Önce çiçekleri, sonra bir ağacın kabuğunu kokladı. Ama koku onlardan gelmiyordu. Sonra Maşa burnunu sepetine yaklaştırdı. Koku tam oradan geliyordu! Sepette ekmekleri korumak için bir bez vardı. Maşa bezi kaldırdı ve reçel kavanozunu gördü. Kavanozun kapağı açılmıştı ve reçel beze dökülmüştü. Maşa önce somurtkan bir yüz yaptı. Sonra kapağı sıkıca kapattı ve parmağındaki reçeli yaladı. Maşa çok güldü, çünkü tatlı koku kendi sepetinden geliyordu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ormanda tatlı bir reçel kokusu vardı"
   - Cümle 0 (plan satırı): «ormanda tatlı bir reçel kokusu vardı | her yeri kokladı ve kokuyu kendi sepetinde buldu»
   - Açıklama: Sorun yalnız bir koku merakı; çocuğun önemseyeceği gerçek bir sorun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden tatlı bir reçel kokusu aldı"
   - Cümle 2: «Birden tatlı bir reçel kokusu aldı.»
   - Açıklama: Hoş bir koku almak sorun değil; asıl dert olan dökülen reçel ancak sonda ortaya çıkıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "reçel beze dökülmüştü"
   - Cümle 10: «Kavanozun kapağı açılmıştı ve reçel beze dökülmüştü.»
   - Açıklama: Koku merakının yanında dökülen reçel ikinci bir sorun olarak çıkıyor ve bez ile ekmekler çözülmeden kalıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa önce somurtkan bir yüz yaptı"
   - Cümle 11: «Maşa önce somurtkan bir yüz yaptı.»
   - Açıklama: 'Somurtkan bir yüz yapmak' Türkçede doğal bir kullanım değil; 'yüzünü astı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0151` birebir aynı, ardından `@onarim: 447e35b14c84fd6924bf024b6f47cc7db3174754`, sonra gövde.

### Hikâye 2: tohum masa-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0152
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'portakal', fiil 'çekinmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: yapraklar sağa sola sallanıp elinden kaçıyordu | koşmayı bırakıp açık elleriyle yaprağın altında bekledi
@tohum: masa-0152
Maşa ormanda portakal renginde yaprakların düştüğünü gördü. Bir yaprağı yere düşmeden yakalamak istedi. Ama yapraklar garip bir şekilde sağa sola sallanıyordu. Maşa koştu ve bir yaprağa hemen uzandı. Yaprak parmaklarının arasından kaydı ve yere düştü. Maşa hiç çekinmeden yeni bir yol denedi. Bu kez koşmadı, inen bir yaprağın altında durdu. İki elini açtı ve sessizce bekledi. Yaprak ağır ağır yaklaştı. Sonunda tam avucunun içine kondu. Maşa yaprağı güneşe doğru tuttu ve ona uzun uzun baktı. Maşa çok sevindi, çünkü ilk yaprağını havada yakalamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa hiç çekinmeden yeni"
   - Cümle 6: «Maşa hiç çekinmeden yeni bir yol denedi.»
   - Açıklama: 'Çekinmeden' burada yanlış anlamda kullanılmış; Maşa'nın çekinmesini gerektiren bir durum yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiç çekinmeden yeni bir yol denedi"
   - Cümle 6: «Maşa hiç çekinmeden yeni bir yol denedi.»
   - Açıklama: 'Yeni bir yol denemek' mecaz ve soyut bir anlatım.
   - Açıklama: 'Yeni bir yol denemek' mecazdır; yol burada yöntem anlamında.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0152` birebir aynı, ardından `@onarim: a15f534672f2fc94083d00ea3ae6a2806601a84e`, sonra gövde.

### Hikâye 3: tohum masa-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0153
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'davul', fiil 'serpmek', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: damlalar arasındaki renkli ışıklar kayboldu | güneşe sırtını dönüp havaya çok su serpti
@tohum: masa-0153
@degisim: davul -> şişe
Maşa tepede reçelli ekmeğini yedi ve ellerini şişedeki suyla yıkadı. Islak ellerini salladı ve damlalar arasında renkli ışıklar gördü. Ama ışıklar hemen kayboldu, çünkü damlalar çok azdı. Maşa bu renkleri yeniden görmek istedi. Tozlu patikada durdu ve güneşe sırtını döndü. Sonra kalan suyu avucuna döktü ve havaya serpti. Havada bir sürü damla parladı. Karşısında kırmızı, sarı ve mavi renkler belirdi. Maşa sevinçle ellerini çırptı ve zıpladı. Maşa tepede renk oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa tepede reçelli ekmeğini yedi"
   - Cümle 1: «Maşa tepede reçelli ekmeğini yedi ve ellerini şişedeki suyla yıkadı.»
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız geçerken anılıyor, sorunun çözümünde doğrudan işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0153` birebir aynı, `@degisim: davul -> şişe` (tutuyorsan), ardından `@onarim: fd788f953276105889fe29e1e8eb243fd80ebe6f`, sonra gövde.

### Hikâye 4: tohum masa-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0154
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'baharat', fiil 'ıslatmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi baharatlı elmayı kokladı ve yemedi | elma dilimini suyla ıslattı ve yıkadı
@tohum: masa-0154
Güneşli bir gündü ve ormanda kuşlar ötüyordu. Koca Ayı, Maşa ile kirpiye elma dilimleri verdi ve üstlerine baharat serpti. Ama kirpi baharatlı elmayı kokladı, yüzünü buruşturdu ve yemedi. Maşa elmasını kirpiyle paylaşmak istedi. Hemen yeni bir şey denedi. Bir elma dilimini şişedeki suyla ıslattı ve iyice yıkadı. Sonra dilimi kirpiye uzattı. "Kirpi, bu sana, afiyet olsun!" dedi Maşa. Kirpi dilimi kokladı ve bu kez yüzünü buruşturmadı. Elmayı çıtır çıtır yedi ve burnunu Maşa'nın eline sürdü. Koca Ayı da gülümsedi ve başını salladı. Maşa çok sevindi, çünkü elmasını kirpiyle paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "suyla ıslattı ve iyice yıkadı"
   - Cümle 6: «Bir elma dilimini şişedeki suyla ıslattı ve iyice yıkadı.»
   - Açıklama: Islatmak ve yıkamak aynı işi anlatıyor, gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0154` birebir aynı, ardından `@onarim: 9e521602132545b05987875402070ebedfb66005`, sonra gövde.

### Hikâye 5: tohum masa-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0155
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bambu', fiil 'yağmak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: dönerken uçurtmanın ipi ayaklarına dolandı ve karıştı | ipi boş reçel kavanozuna yavaşça sardı
@tohum: masa-0155
@degisim: bambu -> uçurtma
Tepede yağmur yağmıyordu ve güzel bir rüzgar esiyordu. Maşa uçurtmasını tutarak çimenlerin üstünde dönüyordu. Ama dönerken ip ayaklarına dolandı ve karmakarışık oldu. Uçurtma yere indi ve Maşa buna çok güldü. Sepetinde boş bir reçel kavanozu vardı. Az önce içindeki reçelin hepsini yemişti. Maşa ipin ucunu kavanoza bağladı. Sonra ipi yavaş yavaş kavanozun üstüne sardı. Böylece düğümler tek tek açıldı. Sonunda bütün ip kavanozun üstünde düzgünce duruyordu. Uçurtma yeniden havaya yükseldi. Maşa kavanozu sıkıca tuttu ve uçurtma oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipi yavaş yavaş kavanozun üstüne sardı"
   - Cümle 8: «Sonra ipi yavaş yavaş kavanozun üstüne sardı.»
   - Açıklama: İp kavanozun üstüne değil etrafına sarılır; kelime yanlış anlamda.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Böylece düğümler tek tek açıldı"
   - Cümle 9: «Böylece düğümler tek tek açıldı.»
   - Açıklama: Ayaklara dolanmış ipi kavanoza sarmanın düğümleri nasıl açtığı akla yatkın değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonunda bütün ip kavanozun üstünde düzgünce duruyordu"
   - Cümle 10: «Sonunda bütün ip kavanozun üstünde düzgünce duruyordu.»
   - Açıklama: Bütün ip kavanoza sarılmışken uçurtmanın hemen yeniden havaya yükselmesi çelişiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Uçurtma yeniden havaya yükseldi"
   - Cümle 11: «Uçurtma yeniden havaya yükseldi.»
   - Açıklama: Bütün ip kavanozun üstüne sarılmışken uçurtmanın havaya yükselmesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0155` birebir aynı, `@degisim: bambu -> uçurtma` (tutuyorsan), ardından `@onarim: f08933df3fdbed27e40f5d50bbd3a7c5075c1b56`, sonra gövde.

### Hikâye 6: tohum masa-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0156
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kumaş', fiil 'beğenmek', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: tepede nereden geldiği bilinmeyen bir ses vardı | kurabiyelere baktı ve sesi kayanın arkasında buldu
@tohum: masa-0156
Maşa ile Daşa tepede piknik yapıyordu. Çıtır reçelli kurabiyeler sepette, bir kumaşın altındaydı. Birden yakından çıtır çıtır bir ses geldi. Ama ikisi de bir şey yemiyordu. "Kurabiyeleri kim yiyor?" diye sordu Daşa. Maşa hemen sepete koştu ve kumaşı kaldırdı. Ama reçelli kurabiyelerin hepsi yerindeydi. Maşa sessizce durdu ve dinledi. "Ses şu kayanın arkasından geliyor, Daşa!" dedi Maşa. İkisi yavaşça kayanın arkasına baktı. Orada bir sincap fındık kırıyordu. Ses fındığın kabuğundan geliyordu. Sincap fındığını çok beğenmiş gibi kuyruğunu salladı. Maşa çok güldü, çünkü çıtır sesi yapan küçük bir sincaptı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çıtır reçelli kurabiyeler sepette"
   - Cümle 2: «Çıtır reçelli kurabiyeler sepette, bir kumaşın altındaydı.»
   - Açıklama: Tohumdaki reçel özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız süs sıfatı olarak geçiyor, olayda işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız kurabiyenin süsü olarak geçiyor, sesin bulunmasında işe yaramıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa hemen sepete koştu ve kumaşı kaldırdı"
   - Cümle 6: «Maşa hemen sepete koştu ve kumaşı kaldırdı.»
   - Açıklama: Çözüm önce sebebe yönelmeyen bir kurabiye kontrolüyle başlıyor, sonra dinleme ve kayanın arkasına bakma geliyor; iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0156` birebir aynı, ardından `@onarim: 39247a8b11ff5b873125e69e4a0343610244a3ee`, sonra gövde.
