# Editör görevi (onarım): Maşa, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0039 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0039
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'koni', fiil 'yıkamak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çamur oyunu yüzünden elleri çamur içindeydi | yağmur suyunu kovada toplayıp ellerini yıkadı
@tohum: masa-0039
@degisim: koni -> kova
Maşa bulutlu bir günde ormanda çamurdan pasta yapıyordu. Birden karnı acıktı ve sepetindeki en sevdiği reçelli ekmeği yemek istedi. Ama çamur oyunu yüzünden elleri çamur içindeydi. O sırada hafif bir yağmur yağmaya başladı. Maşa yanındaki boş kovayı yağmurun altına koydu. Kovada biraz yağmur suyu birikti. Maşa bu suyla ellerini iyice yıkadı. Sonra büyük bir ağacın altına oturdu. Ekmeğini sepetten aldı ve afiyetle yedi. Maşa çok mutluydu, çünkü elleri temizdi ve karnı doymuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği reçelli ekmeği yemek istedi"
   - Cümle 2: «Birden karnı acıktı ve sepetindeki en sevdiği reçelli ekmeği yemek istedi.»
   - Açıklama: Tohumdaki reçel özelliği yalnız istek olarak anılıyor, çözümde işe yaramıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çamur oyunu yüzünden elleri çamur içindeydi"
   - Cümle 3: «Ama çamur oyunu yüzünden elleri çamur içindeydi.»
   - Açıklama: Aynı cümlede 'çamur' gereksiz yere tekrar ediyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada hafif bir yağmur yağmaya başladı"
   - Cümle 4: «O sırada hafif bir yağmur yağmaya başladı.»
   - Açıklama: Çözümü getiren yağmur ve boş kova sebepsizce tam gerektiği anda beliriyor.
   - Açıklama: Çözümü getiren yağmur tam o anda sebepsizce başlıyor ve boş kova da önceden kurulmadan beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0039` birebir aynı, `@degisim: koni -> kova` (tutuyorsan), ardından `@onarim: 56aa001d84fc986257ff0a27057050a8659bb8ac`, sonra gövde.

### Hikâye 2: tohum masa-0040 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Daşa
@tohum: masa-0040
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boncuk', fiil 'kavuşmak', sıfat 'uyanık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Daşa
@plan: koşarken kutu elinden düştü ve boncuklar döküldü | özür diledi ve boncukları tek tek topladı
@tohum: masa-0040
@degisim: uyanık -> renkli
Rüzgar tepede hafif hafif esiyordu. Daşa çimenlere oturmuş, kolye yapmak için Maşa'yı bekliyordu. Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü. Renkli boncuklar çimenlerin arasına döküldü. Daşa çok üzüldü. "Özür dilerim, Daşa, hepsini hemen toplayacağım," dedi Maşa. Maşa çimenlere eğildi ve boncukları tek tek toplamayı denedi. Daşa da kutuyu açık tuttu. Sonunda bütün boncuklar kutudaydı. Daşa kutuya baktı ve gülümsedi. "Teşekkürler, Maşa, hadi kolyeyi birlikte yapalım," dedi Daşa. Maşa çok sevindi, çünkü kuzeni yine gülüyordu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kuzenine kavuşmak için"
   - Cümle 3: «Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' uzun ayrılıktan sonra buluşmak demektir; bekleyen kuzenin yanına gitmek için yanlış kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa kuzenine kavuşmak için"
   - Cümle 3: «Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' uzun ayrılık sonrası buluşma demektir; birkaç adım ötedeki kuzene koşmaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0040` birebir aynı, `@degisim: uyanık -> renkli` (tutuyorsan), ardından `@onarim: 89f6ca993e3bab4ad6cdc1ccfbac6cdf408a9ceb`, sonra gövde.

### Hikâye 3: tohum masa-0041 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0041
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'filiz', fiil 'somurtmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: ıslak top kaydı ve dikenli çalının altına girdi | kirpiden yardım istedi ve kirpi topu dışarı itti
@tohum: masa-0041
@degisim: filiz -> top
Tepede hava yağmurluydu. Maşa kırmızı topunu çimenlerde zıplatıyordu. Islak top elinden kaydı ve dikenli bir çalının altına girdi. Maşa eğildi ama dikenler yüzünden topu alamadı. Sonra yere oturdu ve somurttu. O sırada çalının yanından küçük bir kirpi geçti. Maşa bu kez yeni bir şey denedi ve kirpiden yardım istedi. "Kirpi, topumu bana getirir misin?" diye sordu Maşa. Kirpi başını salladı ve çalının altına koştu. Burnuyla topu itip dışarı yuvarladı. Maşa topunu aldı ve kirpiye teşekkür etti. Maşa bundan sonra yapamadığı işlerde arkadaşlarından yardım istedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada çalının yanından küçük bir kirpi geçti"
   - Cümle 6: «O sırada çalının yanından küçük bir kirpi geçti.»
   - Açıklama: Çözümü getiren kirpi tam o anda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0041` birebir aynı, `@degisim: filiz -> top` (tutuyorsan), ardından `@onarim: fcc91268876259c5641a6691b9cf116330085510`, sonra gövde.

### Hikâye 4: tohum masa-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0042
- yer: dağ (Ormanın yanındaki tepe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'nane', fiil 'tanıştırmak', sıfat 'neşeli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: sincap kuzeni tanımadığı için ağacın arkasına saklandı | fındıkları sincapla paylaştı ve sincap yanlarına geldi
@tohum: masa-0042
@degisim: nane -> fındık
Tepede hafif bir rüzgar esiyordu. Maşa, kuzeni Daşa'yı tepedeki sincapla tanıştırmak istiyordu. Ama sincap Daşa'yı tanımadığı için ağacın arkasına saklandı. Maşa önce sincaba el sallamayı denedi ama sincap çıkmadı. Sonra Maşa cebinden bir avuç fındık aldı. "Daşa, fındıkları sincapla paylaşalım mı?" diye sordu Maşa. "Evet, bence çok sevinir," dedi Daşa. İkisi onları ağacın dibine koydu. Sincap yavaşça çıktı ve bir tanesini aldı. Sonra Daşa'nın yanına gelip ona baktı. "Merhaba, sincap," dedi Daşa neşeli bir sesle. Maşa, Daşa ve sincap fındıkları birlikte mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa önce sincaba el sallamayı denedi ama sincap çıkmadı"
   - Cümle 4: «Maşa önce sincaba el sallamayı denedi ama sincap çıkmadı.»
   - Açıklama: Tohumdaki deneme özelliği işe yaramıyor; sorunu fındık paylaşmak çözüyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İkisi onları ağacın dibine koydu"
   - Cümle 8: «İkisi onları ağacın dibine koydu.»
   - Açıklama: 'onları' zamirinin gösterdiği fındıklar yalnız önceki replikte geçiyor, anlatımda kimi/neyi gösterdiği belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0042` birebir aynı, `@degisim: nane -> fındık` (tutuyorsan), ardından `@onarim: 86c9b159509c66d0c6e63ed7a6e898d691c4dad8`, sonra gövde.

### Hikâye 5: tohum masa-0043 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0043
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'güneş', fiil 'çalıştırmak', sıfat 'resimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: müzik kutusu çalmadı ve içinden tık tık sesi geldi | kutunun kapağını açıp içindeki taşı çıkardı
@tohum: masa-0043
Maşa güneşli bir sabah Koca Ayı'nın bahçesine geldi. Resimli müzik kutusuyla Koca Ayı ile dans etmek istiyordu. Ama kolu çevirince müzik çalmadı, içinden tık tık diye bir ses geldi. Maşa bu sesi çok merak etti. Kutunun altındaki küçük kapağı açmayı denedi. Kapak açıldı ve içinden küçük bir taş düştü. "Koca Ayı, bak, kutunun içine taş girmiş!" dedi Maşa. Koca Ayı taşa baktı ve başını salladı. Maşa kolu yeniden çevirdi ve kutuyu çalıştırdı. Bu kez güzel bir şarkı başladı. Maşa ile Koca Ayı bahçede mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Koca Ayı'nın bahçesine geldi"
   - Cümle 1: «Maşa güneşli bir sabah Koca Ayı'nın bahçesine geldi.»
   - Açıklama: Başlıktaki yer ev iken hikaye Koca Ayı'nın bahçesine gelişle başlıyor ve bahçede bitiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama kolu çevirince"
   - Cümle 3: «Ama kolu çevirince müzik çalmadı, içinden tık tık diye bir ses geldi.»
   - Açıklama: 'Kolu' ilk kez geçiyor ve kimin ya da neyin kolu olduğu belli değil; 'kutunun kolunu' olmalı.
   - Açıklama: 'Kolu' kimin ya da neyin kolu olduğu belli değil; kutunun kolu daha önce tanıtılmadı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0043` birebir aynı, ardından `@onarim: 7dadb4cc432d49f2f97028b54c7e6ac2936181cb`, sonra gövde.

### Hikâye 6: tohum masa-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0046
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bisküvi', fiil 'koşuşturmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi yaprakların altında uyuyordu ve pikniğe gelemedi | reçelin kapağını açtı ve koku kirpiyi uyandırdı
@tohum: masa-0046
Maşa ormanda Koca Ayı ile piknik yapıyordu. Sepette vanilyalı bisküvi ve reçel vardı. Ama kirpi yaprakların altında uyuyordu. Maşa bisküvileri kirpiyle birlikte yemek istiyordu. Beklerken ağaçların arasında koşuşturdu. Koca Ayı parmağını ağzına götürdü ve kirpiyi gösterdi. Maşa hemen durdu ve sessizce oturdu. Sonra kirpiyi yavaşça uyandırmak için en sevdiği reçelin kapağını açtı. Tatlı koku yapraklara kadar gitti. Kirpi burnunu oynattı ve dışarı çıktı. "Günaydın, kirpi, seni bekledik!" dedi Maşa. Her bisküviye reçel sürdü ve herkese birer tane verdi. Maşa çok sevindi, çünkü beklediği arkadaşı sonunda gelmişti.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Beklerken ağaçların arasında koşuşturdu"
   - Cümle 5: «Beklerken ağaçların arasında koşuşturdu.»
   - Açıklama: Koşuşturma ve susturulma bölümü sonuca bağlanmıyor ve ikinci bir olay açıyor.
   - Açıklama: Koşuşturma ve susturulma bölümü sorunla ya da çözümle bağlantısız, işlevsiz bir ara olay.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en sevdiği reçelin kapağını"
   - Cümle 8: «Sonra kirpiyi yavaşça uyandırmak için en sevdiği reçelin kapağını açtı.»
   - Açıklama: Reçelin Maşa'nın mı kirpinin mi en sevdiği olduğu belli değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kirpiyi yavaşça uyandırmak için"
   - Cümle 8: «Sonra kirpiyi yavaşça uyandırmak için en sevdiği reçelin kapağını açtı.»
   - Açıklama: Koca Ayı kirpiyi uyutmak için Maşa'yı susturuyor ama hemen ardından Maşa kirpiyi uyandırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0046` birebir aynı, ardından `@onarim: 521229398c65babe2d603f3236829594fd0807fa`, sonra gövde.

### Hikâye 7: tohum masa-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0047
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kereviz', fiil 'soğumak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: içecek güneşte kaldığı için ılık olmuştu | şişeyi soğuk sulu kovaya koyup gölgede bekledi
@tohum: masa-0047
@degisim: kereviz -> şişe
Hava çok sıcaktı. Maşa, kuzeni Daşa için bahçede çilek reçelinden bir içecek hazırlamıştı. Ama şişe güneşte kaldığı için içecek ılık olmuştu. Maşa evden bir kova soğuk su getirdi. Şişeyi kovaya koydu ve kovayı ağacın gölgesine taşıdı. Maşa beklerken şişeye birkaç kez dokundu. Sonunda içecek iyice soğudu. Tam o sırada bahçe kapısından Daşa geldi. "Sürpriz, Daşa, bu içecek senin için!" dedi Maşa. Daşa bir yudum aldı ve gülümsedi. "Çok güzel olmuş, teşekkür ederim, Maşa," dedi Daşa. Daşa çok sevindi ve birden konuşkan oldu. Maşa ile Daşa ağacın altında oturup içeceklerini mutlu mutlu içti.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çilek reçelinden bir içecek"
   - Cümle 2: «Maşa, kuzeni Daşa için bahçede çilek reçelinden bir içecek hazırlamıştı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor; sorun soğuk suyla çözülüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "birden konuşkan oldu"
   - Cümle 12: «Daşa çok sevindi ve birden konuşkan oldu.»
   - Açıklama: 'Konuşkan' kalıcı bir özelliktir; bir anda olunan durum için yanlış kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "birden konuşkan oldu"
   - Cümle 12: «Daşa çok sevindi ve birden konuşkan oldu.»
   - Açıklama: 'Konuşkan olmak' soyut bir özellik ve olaya uymayan bir anlatım.
4. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Daşa çok sevindi ve birden konuşkan oldu"
   - Cümle 12: «Daşa çok sevindi ve birden konuşkan oldu.»
   - Açıklama: Kartın yanlar alanında Daşa düşünceli ve ciddi bir kızdır; birden konuşkan olması karta aykırı.
   - Açıklama: Kartın yanlar alanında Daşa düşünceli ve ciddi bir kız olarak tanımlı; sessizken birden konuşkan olması karta dayanmıyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "birden konuşkan oldu"
   - Cümle 12: «Daşa çok sevindi ve birden konuşkan oldu.»
   - Açıklama: Diziyi izlemiş çocuk Daşa'yı ciddi ve düşünceli bilir; yanlış bilgi var.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Daşa çok sevindi ve birden konuşkan oldu"
   - Cümle 12: «Daşa çok sevindi ve birden konuşkan oldu.»
   - Açıklama: Daşa'nın birden konuşkan olması sebepsiz ve olayla ilgisiz bir ayrıntı.
   - Açıklama: Daşa'nın birden konuşkan olması sebepsiz ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0047` birebir aynı, `@degisim: kereviz -> şişe` (tutuyorsan), ardından `@onarim: c7cbc540e9ac5da378ad135291979dfd237ddb4a`, sonra gövde.

### Hikâye 8: tohum masa-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0050
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tablo', fiil 'dikmek', sıfat 'kilitli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: resmin köşesinde yapışkan kırmızı izler vardı | kokudan reçeli tanıdı ve izleri takip edip sincabı buldu
@tohum: masa-0050
@degisim: kilitli -> yapışkan
Maşa tepede Koca Ayı'nın yanında reçel yiyordu. Koca Ayı bir tahtayı yere dikmiş, üstünde bir tablo yapıyordu. Birden Maşa resmin köşesinde küçük kırmızı izler gördü. Bunlar yapışkandı ve çok güzel kokuyordu. Maşa kokuyu hemen tanıdı, bu onun en sevdiği reçeldi! Maşa reçel kavanozuna baktı, kapak açıktı. Kavanozun yanında minik ayak izleri vardı. Maşa onların peşinden gitti ve ağacın arkasında bir sincap buldu. Sincabın patileri kırmızı reçelle kaplıydı. Koca Ayı sincabı görünce gülümsedi ve resmi temizledi. Maşa da çok sevindi, çünkü izleri yapanı bulmuştu.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa tepede Koca Ayı'nın yanında reçel yiyordu"
   - Cümle 1: «Maşa tepede Koca Ayı'nın yanında reçel yiyordu.»
   - Açıklama: Maşa kendisi resmin yanında reçel yerken izlerin ondan olabileceği hiç düşünülmüyor ve kavanozun açık olması onun yüzünden olabilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üstünde bir tablo yapıyordu"
   - Cümle 2: «Koca Ayı bir tahtayı yere dikmiş, üstünde bir tablo yapıyordu.»
   - Açıklama: 'Tablo yapmak' yerinde değil ve sonra 'resim' deniyor; 'resim yapıyordu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "üstünde bir tablo yapıyordu"
   - Cümle 2: «Koca Ayı bir tahtayı yere dikmiş, üstünde bir tablo yapıyordu.»
   - Açıklama: 'Tablo' küçük çocuğun bilmeyeceği bir kelime ve sonra 'resim' deniyor; 'resim yapıyordu' olmalı.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Koca Ayı sincabı görünce gülümsedi ve resmi temizledi"
   - Cümle 10: «Koca Ayı sincabı görünce gülümsedi ve resmi temizledi.»
   - Açıklama: Resimdeki izleri Maşa değil yan karakter Koca Ayı temizliyor; asıl sorunu yan karakter çözüyor.
   - Açıklama: Resimdeki izleri Maşa değil Koca Ayı temizliyor; sorunun bir kısmını yan karakter çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0050` birebir aynı, `@degisim: kilitli -> yapışkan` (tutuyorsan), ardından `@onarim: 2d419cff96e064e7f85ecbf603622f3d5b5930b4`, sonra gövde.

### Hikâye 9: tohum masa-0051 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi, Daşa
@tohum: masa-0051
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çamur', fiil 'sevinmek', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi, Daşa
@plan: tek kova vardı ve ikisi de onu istedi | sırayla oynamayı önerdi ve kovayı paylaştılar
@tohum: masa-0051
@degisim: faydalı -> ıslak
Ormanda patikanın kenarı ıslak çamurla doluydu. Maşa ile kuzeni Daşa çamurdan pasta yapmak istiyordu. Ama tek bir küçük kovaları vardı ve ikisi de onu hemen istedi. Yakında bir kirpi de onları merakla izliyordu. Maşa yeni bir oyun denedi. "Sırayla yapalım, önce ben, sonra sen, sonra kirpi," dedi Maşa. Maşa kovayı çamurla doldurdu ve ters çevirdi. Yere güzel bir pasta çıktı. "Şimdi sıra sende, Daşa," dedi Maşa. Daşa kovayı aldı ve dikkatle ikinci pastayı yaptı. "Sıra kirpide," dedi Daşa. Kirpi burnuyla bir yaprağı pastaların üstüne itti. Daşa çok sevindi ve güldü. "Sırayla oynamak çok eğlenceli, Daşa!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yakında bir kirpi de"
   - Cümle 4: «Yakında bir kirpi de onları merakla izliyordu.»
   - Açıklama: 'Yakında' burada 'yakınlarda' anlamında kullanılmış ama 'kısa süre sonra' diye de okunabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0051` birebir aynı, `@degisim: faydalı -> ıslak` (tutuyorsan), ardından `@onarim: 34e901a773460f533c6201b716bc3aeed87b4c4e`, sonra gövde.

### Hikâye 10: tohum masa-0052 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0052
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'gölge', fiil 'süslenmek', sıfat 'limonlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: ikisi aynı anda keke uzandı ve çiçekler düştü | sırayla koymayı önerdi ve keki birlikte süslediler
@tohum: masa-0052
Rüzgar hafif hafif esiyordu. Maşa ile sincap bir ağacın gölgesinde limonlu bir keki çiçeklerle süslüyordu. Ama ikisi de aynı anda keke uzandı ve çiçekler yere düştü. Sincap üzgün üzgün düşen çiçeklere baktı. Maşa çiçekleri yerden topladı ve biraz düşündü. "Sırayla koyalım, sincap, önce sen," dedi Maşa. Sincap küçük bir çiçeği kekin üstüne koydu. Sonra sıra Maşa'ya geldi. Maşa yanındaki kavanozdan keke biraz reçel sürdü. Böylece ikisi sırayla çiçek ve reçel koydu. Kek sonunda rengarenk süslendi. Maşa ile sincap çok sevindi, çünkü sırayla koyunca hiç çiçek düşmedi.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi de aynı anda keke uzandı"
   - Cümle 3: «Ama ikisi de aynı anda keke uzandı ve çiçekler yere düştü.»
   - Açıklama: Düşen çiçeklerin yerden hemen toplanması sorunu önemsiz kılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa yanındaki kavanozdan keke biraz reçel sürdü"
   - Cümle 9: «Maşa yanındaki kavanozdan keke biraz reçel sürdü.»
   - Açıklama: Tohumdaki reçel özelliği sorunu çözmüyor, yalnız süs olarak geçiyor ve sonra ikinci kez tekrarlanıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa yanındaki kavanozdan keke biraz reçel sürdü"
   - Cümle 9: «Maşa yanındaki kavanozdan keke biraz reçel sürdü.»
   - Açıklama: Reçel kavanozu sebepsiz beliriyor ve çiçek düşme sorunuyla ilgisi yok.
   - Açıklama: Reçel kavanozu sebepsiz beliriyor ve sorunla ilgisi yok.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sırayla çiçek ve reçel koydu"
   - Cümle 10: «Böylece ikisi sırayla çiçek ve reçel koydu.»
   - Açıklama: Reçel konmaz, sürülür; fiil iki nesneye birden uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0052` birebir aynı, ardından `@onarim: 25484113c64d3acb0fe41b16733b7b5b1bd77f00`, sonra gövde.

### Hikâye 11: tohum masa-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0053
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: bir şey yapmak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kaktüs', fiil 'ovmak', sıfat 'sağlam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: fındık kabı olan kavanoz yuvarlandı ve fındıklar döküldü | kavanozu iki taşın arasına dik koydu
@tohum: masa-0053
@degisim: kaktüs -> kavanoz
Bir sabah Maşa ile kuzeni Daşa ormanda sincaba bir fındık kabı yapıyordu. Maşa kavanozdaki son reçeli yedi ve Daşa içini yaprakla ovdu. Ama içine fındık koyunca kavanoz yuvarlandı ve fındıklar döküldü. Yakındaki sincap dökülen fındıklara şaşkın şaşkın baktı. "Maşa, bu kavanoz hiç yerinde durmuyor," dedi Daşa. Maşa etrafına baktı ve iki büyük taş buldu. Kavanozu iki taşın arasına dik koydu. Kavanoz artık hiç kıpırdamadı. Daşa fındıkları topladı ve kavanoza geri koydu. Sincap hemen geldi ve kavanozdan bir fındık aldı. "Bak, Daşa, sincap bu kabı çok sevdi!" dedi Maşa. Maşa ile Daşa çok sevindi, çünkü sincabın artık sağlam bir kabı vardı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "içine fındık koyunca kavanoz yuvarlandı"
   - Cümle 3: «Ama içine fındık koyunca kavanoz yuvarlandı ve fındıklar döküldü.»
   - Açıklama: Kavanozun neden yuvarlandığı söylenmiyor; sorunun sebebi açık değil.
   - Açıklama: Kavanozun neden yuvarlandığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0053` birebir aynı, `@degisim: kaktüs -> kavanoz` (tutuyorsan), ardından `@onarim: bdca13161e892773737c156ad2e5cfabf64cef4e`, sonra gövde.

### Hikâye 12: tohum masa-0054 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0054
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'paspas', fiil 'boşaltmak', sıfat 'cömert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: sebzeleri sulamak istedi ama su dolu kova çok ağırdı | suyun yarısını boşalttı ve kovayı rahatça taşıdı
@tohum: masa-0054
@degisim: paspas -> kova
Ormandaki ağaç evin bahçesinde Koca Ayı bir ağacın altında uyuyordu. Maşa cömert Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi. Ama su dolu büyük kova çok ağırdı. Maşa kovayı iki eliyle çekti ama kova yerinden oynamadı. Maşa biraz düşündü ve suyun yarısını domateslere boşaltmayı denedi. Kova hafifledi ve Maşa onu rahatça taşıdı. Kalan suyu da havuçlara döktü. Sonra Koca Ayı uyandı ve ıslak bahçeyi gördü. Şaşırdı ve kocaman gülümsedi. Maşa'ya koştu ve ona sıkıca sarıldı. "Sürpriz, Koca Ayı! Bugün bahçeni ben suladım!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa cömert Koca Ayı'ya sürpriz"
   - Cümle 2: «Maşa cömert Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi.»
   - Açıklama: 'Cömert' özelliği yanlış kişiye, işi yapan Maşa yerine Koca Ayı'ya bağlanmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0054` birebir aynı, `@degisim: paspas -> kova` (tutuyorsan), ardından `@onarim: c2b2758e631bdcfc88b5e17f61114974d5bd9564`, sonra gövde.
