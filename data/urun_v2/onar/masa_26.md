# Editör görevi (onarım): Maşa, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar26.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0077 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi, Daşa
@tohum: masa-0077
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'reçel', fiil 'parıldamak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi, Daşa
@plan: reçel kavanozunun kapağı çok sıkıydı ve açılmadı | kuzeninden yardım isteyip kapağı birlikte açtı
@tohum: masa-0077
Maşa bahçede kirpiye bir elma getirmişti. Elmanın üstüne en sevdiği reçelden koymak istedi. Ama kavanozun kapağı çok sıkıydı ve açılmadı. Maşa kapağı iki eliyle çevirdi ama kapak dönmedi. Daşa ağacın altında kitap okuyordu ve çok meşguldü. "Daşa, bu kapağı açmama yardım eder misin?" diye sordu Maşa. Daşa kitabını bıraktı ve kavanozu sıkıca tuttu. Maşa kapağı bir kez daha çevirdi. Kapak birden açıldı. Kırmızı reçel güneşte parıldadı. Maşa elmanın üstüne biraz reçel koydu ve kirpiye verdi. Kirpi elmayı yedi ve sevinçle burnunu oynattı. "Teşekkürler, Daşa!" dedi Maşa. Maşa bundan sonra zorda kalınca Daşa'dan yardım istedi.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bahçede kirpiye bir elma getirmişti"
   - Cümle 1: «Maşa bahçede kirpiye bir elma getirmişti.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede, ağacın altında geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede ağacın altında geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kitap okuyordu ve çok meşguldü"
   - Cümle 5: «Daşa ağacın altında kitap okuyordu ve çok meşguldü.»
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelimedir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bundan sonra zorda kalınca"
   - Cümle 14: «Maşa bundan sonra zorda kalınca Daşa'dan yardım istedi.»
   - Açıklama: 'Zorda kalmak' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Zorda kalmak' deyimdir; 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0077` birebir aynı, ardından `@onarim: d36813b2706a56df70dbbd76d0936abdac1f0748`, sonra gövde.

### Hikâye 2: tohum masa-0079 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0079
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pilav', fiil 'kucaklamak', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: pilavı koyduğu ince yaprak yırtıldı ve pilav döküldü | pilavı boş reçel kavanozuna doldurup sofraya taşıdı
@tohum: masa-0079
Maşa ormanda yemek oyunu oynuyordu ve bir kütüğe sofra kurmuştu. Beyaz taşlardan pilav yaptı ve pilavı temiz bir yaprağa koydu. Ama yaprak çok inceydi, yırtıldı ve pilav yere döküldü. Maşa taşları tek tek topladı. Sonra yanındaki boş reçel kavanozunu gördü. Maşa en sevdiği reçeli az önce bitirmişti. Taşları bu kavanoza doldurdu. Kavanoz sağlamdı ve hiçbir taş dökülmedi. Maşa kavanozu sevinçle kucakladı ve kütüğe taşıdı. Kavanozu sofranın ortasına koydu. Sofra artık hazırdı. Maşa bundan sonra pilavını yaprağa değil, kavanoza koydu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra pilavını yaprağa değil, kavanoza koydu"
   - Cümle 12: «Maşa bundan sonra pilavını yaprağa değil, kavanoza koydu.»
   - Açıklama: 'Bundan sonra' süreklilik bildirir ama tek seferlik 'koydu' ile uyumsuz; 'hep kavanoza koydu' ya da 'koyardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0079` birebir aynı, ardından `@onarim: 54d10064bc5539c9317657e002deb9c303204ea3`, sonra gövde.

### Hikâye 3: tohum masa-0081 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | sincap
@tohum: masa-0081
- yer: dağ (Ormanın yanındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'ekmek', fiil 'guruldamak', sıfat 'renkli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | sincap
@plan: rüzgar esti ve sofradaki yapraklar uçup gitti | her yaprağın üstüne küçük bir taş koydu
@tohum: masa-0081
@degisim: ekmek -> fındık
Tepede serin bir rüzgar vardı. Maşa sincaba sürpriz bir sofra kurdu ve renkli yapraklarla süsledi. Ama rüzgar esti ve yapraklar uçup gitti. Maşa yaprakları topladı ve yeni bir şey denedi. Her yaprağın üstüne küçük bir taş koydu. Rüzgar yine esti ama bu kez yapraklar yerinde kaldı. Sonra Maşa sofraya fındık ve ekmek koydu. Tam o sırada Maşa'nın karnı guruldadı. Ama Maşa ekmeğe dokunmadı ve sincabı bekledi. Az sonra sincap bir çalının arkasından çıktı. "Sürpriz, sincap!" dedi Maşa. Sincap fındıkları görünce sevinçle zıpladı. Maşa ile sincap süslü sofrada mutlu mutlu yemek yedi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve yapraklar uçup gitti"
   - Cümle 3: «Ama rüzgar esti ve yapraklar uçup gitti.»
   - Açıklama: Süs yapraklarının uçması önemsiz bir olay; yönergedeki 'rüzgar oyun yapraklarını dağıttı' örneğine çok benziyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama rüzgar esti ve yapraklar uçup gitti"
   - Cümle 3: «Ama rüzgar esti ve yapraklar uçup gitti.»
   - Açıklama: Süs yapraklarının uçması önemsiz bir olay; örnekteki 'rüzgar yaprakları dağıttı, topladı, bitti' kalıbının aynısı.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Tam o sırada Maşa'nın karnı guruldadı"
   - Cümle 8: «Tam o sırada Maşa'nın karnı guruldadı.»
   - Açıklama: Sofra sorunu çözüldükten sonra açlık ve sabretme üzerine ikinci bir sorun açılıyor.
   - Açıklama: Yaprak sorunu çözüldükten sonra açlık ve sabretme gibi ikinci bir küçük sorun açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0081` birebir aynı, `@degisim: ekmek -> fındık` (tutuyorsan), ardından `@onarim: 46d5698ee83b8446401cb5b300ff6fe8dedf7087`, sonra gövde.

### Hikâye 4: tohum masa-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0083
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kemer', fiil 'sallamak', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: çiçek ağacın gölgesinde kalmıştı ve daha açılmıyordu | kirpiyle reçel ve elma yiyerek güneşi bekledi
@tohum: masa-0083
@degisim: kemer -> sepet
Hava aydınlıktı ve bahçede kuşlar ötüyordu. Maşa ile kirpi bahçedeki kırmızı çiçeğin açılmasını bekliyordu. Ama çiçek ağacın gölgesinde kalmıştı ve daha açılmıyordu. Maşa yerinde duramadı ve ayaklarını salladı. Sonra sepetinden en sevdiği reçeli, ekmeği ve bir elma çıkardı. Elmayı kirpiye verdi. Kendisi de ekmeğine reçel sürdü. İkisi yan yana oturup yavaşça yedi. Bu sırada güneş yükseldi ve gölge çiçeğin üstünden çekildi. Kırmızı çiçek yavaş yavaş açıldı. "Bak, kirpi, çiçek açıldı!" dedi Maşa. Kirpi burnunu kaldırdı ve çiçeği kokladı. Maşa ile kirpi çiçeğin yanında kahvaltıya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa yerinde duramadı"
   - Cümle 4: «Maşa yerinde duramadı ve ayaklarını salladı.»
   - Açıklama: 'Yerinde duramamak' sabırsızlık anlatan bir deyim.
   - Açıklama: 'Yerinde duramamak' sabırsızlık anlatan bir deyim; küçük çocuk için mecaz.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra sepetinden en sevdiği reçeli"
   - Cümle 5: «Sonra sepetinden en sevdiği reçeli, ekmeği ve bir elma çıkardı.»
   - Açıklama: Reçel ve elma yemek gölge sebebine hiç yönelmiyor; çözüm bir eylem değil beklemek.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kendisi de ekmeğine reçel sürdü"
   - Cümle 7: «Kendisi de ekmeğine reçel sürdü.»
   - Açıklama: Tohumdaki reçel özelliği sorunu çözmüyor; çiçeği güneş açıyor, reçel yalnız beklerken yeniyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi yan yana oturup yavaşça yedi"
   - Cümle 8: «İkisi yan yana oturup yavaşça yedi.»
   - Açıklama: Yemek yemek gölge sorununa yönelmiyor; yalnız bekleniyor.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bu sırada güneş yükseldi ve gölge çiçeğin üstünden çekildi"
   - Cümle 9: «Bu sırada güneş yükseldi ve gölge çiçeğin üstünden çekildi.»
   - Açıklama: Sorunu Maşa değil kendiliğinden yükselen güneş çözüyor.
   - Açıklama: Sorunu Maşa değil güneşin yükselmesi çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0083` birebir aynı, `@degisim: kemer -> sepet` (tutuyorsan), ardından `@onarim: 152faff9aa8563f7fbb8f7bc947fadfee9e68fc2`, sonra gövde.

### Hikâye 5: tohum masa-0084 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap
@tohum: masa-0084
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'avokado', fiil 'güzelleştirmek', sıfat 'yumuşak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | sincap
@plan: fındık gözler kaygan avokadoya yapışmadı | fındıkları reçelle avokadoya yapıştırdı
@tohum: masa-0084
Bahçede Maşa ile sincap komik bir oyun oynuyordu. Maşa yumuşak bir avokadoya fındıkla gözler yapıyordu. Ama avokado kaygandı ve fındık gözler hep yere düştü. Sincap düşen fındıkları topladı ama bir fındığı da yedi. Maşa güldü ve biraz düşündü. Sonra en sevdiği reçelden biraz aldı. Reçeli fındıklara sürdü ve onları avokadoya yapıştırdı. Bu kez gözler hiç düşmedi. Sonra bir yaprakla avokadoyu güzelleştirdi. Sincap avokadoya baktı ve sevinçle zıpladı. "Teşekkürler, sincap, avokado çok komik oldu!" dedi Maşa.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fındık gözler kaygan avokadoya"
   - Cümle 0 (plan satırı): «fındık gözler kaygan avokadoya yapışmadı | fındıkları reçelle avokadoya yapıştırdı»
   - Açıklama: Tamlama eki eksik; 'fındık gözleri' ya da 'fındıktan gözler' olmalı.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede Maşa ile sincap"
   - Cümle 1: «Bahçede Maşa ile sincap komik bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve fındık gözler hep"
   - Cümle 3: «Ama avokado kaygandı ve fındık gözler hep yere düştü.»
   - Açıklama: Tamlama eki eksik; 'fındık gözleri' olmalı.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fındık gözler hep yere düştü"
   - Cümle 3: «Ama avokado kaygandı ve fındık gözler hep yere düştü.»
   - Açıklama: 'hep' süreklilik bildirdiği için bitmiş geçmişle uyumsuz; 'hep yere düşüyordu' olmalı.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir fındığı da yedi"
   - Cümle 4: «Sincap düşen fındıkları topladı ama bir fındığı da yedi.»
   - Açıklama: Sincabın bir fındığı yemesi olayda hiçbir işe yaramayan ayrıntı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ama bir fındığı da yedi"
   - Cümle 4: «Sincap düşen fındıkları topladı ama bir fındığı da yedi.»
   - Açıklama: Sincabın fındık yemesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bir yaprakla avokadoyu güzelleştirdi"
   - Cümle 9: «Sonra bir yaprakla avokadoyu güzelleştirdi.»
   - Açıklama: Yaprak sebepsiz beliriyor ve sorunla ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0084` birebir aynı, ardından `@onarim: 526d4c4415d238d038ec12a5054858092aa32e52`, sonra gövde.

### Hikâye 6: tohum masa-0085 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0085
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kütük', fiil 'örtmek', sıfat 'yeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: eski bir kütükten garip bir ses geldi | yaprakları kaldırıp uyuyan kirpiyi buldu
@tohum: masa-0085
Maşa ile Koca Ayı ormanda patikada yürüyordu. Birden eski bir kütükten garip bir ses geldi. Kütüğün deliğini yeşil yapraklar örtüyordu ve içi görünmüyordu. Maşa bu sesi çok merak etti. "Koca Ayı, bu ses ne?" diye sordu Maşa. Koca Ayı başını salladı ve kütüğe yaklaştı. Maşa yaprakları tek tek kaldırmayı denedi. Yaprakların altında küçük bir kirpi uyuyordu. Ses, uyuyan kirpiden geliyordu. Kirpi gözlerini açtı ve burnunu oynattı. "Merhaba, kirpi, ses senden geliyordu!" dedi Maşa. Koca Ayı yaprakları yavaşça geri koydu. Maşa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "eski bir kütükten garip bir ses geldi"
   - Cümle 2: «Birden eski bir kütükten garip bir ses geldi.»
   - Açıklama: Garip bir sesin gelmesi çocuğun çözmesi gereken gerçek bir sorun değil, yalnız merak.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı başını salladı ve kütüğe yaklaştı"
   - Cümle 6: «Koca Ayı başını salladı ve kütüğe yaklaştı.»
   - Açıklama: Koca Ayı'nın yaklaşması olayda işe yaramıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ses senden geliyordu!"
   - Cümle 11: «"Merhaba, kirpi, ses senden geliyordu!" dedi Maşa.»
   - Açıklama: Sesin kirpiden geldiği bir önceki cümlelerde söylenmişken replikte gereksizce tekrar ediliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı yaprakları yavaşça geri koydu"
   - Cümle 12: «Koca Ayı yaprakları yavaşça geri koydu.»
   - Açıklama: Kirpi uyanmışken yaprakların geri konması sebepsiz ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0085` birebir aynı, ardından `@onarim: eef5522736d2498c7ec6d7be8f48fcd20e3993e7`, sonra gövde.

### Hikâye 7: tohum masa-0086 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0086
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'düğüm', fiil 'uzaklaşmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: atlama ipi ayağına dolandı ve düğüm oldu | kuzeninin arkasından koşup ondan yardım istedi
@tohum: masa-0086
Bir sabah Maşa bahçede ip atlıyordu. Birden ip ayağına dolandı ve ortasında sıkı bir düğüm oldu. Maşa iki ucu da çekti ama düğüm daha çok sıkıştı. O sırada Daşa kitabını alıp eve doğru uzaklaşıyordu. Maşa yeni bir şey denedi ve Daşa'nın arkasından koştu. Ondan yardım istedi ve düğümü gösterdi. Daşa ipi elinde dikkatle çevirdi. Sonra düğümün içinde gizli kalmış küçük bir ucu gösterdi. Maşa o ucu yavaşça çekti ve düğüm çözüldü. Maşa sevinçle zıpladı ve Daşa'ya sarıldı. Daşa da kitabını bir kenara bıraktı. İkisi bahçede sırayla ip atlayıp mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah Maşa bahçede ip atlıyordu"
   - Cümle 1: «Bir sabah Maşa bahçede ip atlıyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0086` birebir aynı, ardından `@onarim: 85f51112c6826207f6cfb44f924aaaa3b255bc41`, sonra gövde.

### Hikâye 8: tohum masa-0087 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0087
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'meyve', fiil 'sergilemek', sıfat 'serin'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: tepe eğikti ve yuvarlak elmalar aşağı kaydı | başka bir yer denedi ve düz bir taş buldu
@tohum: masa-0087
Maşa serin bir sabah tepede meyvelerle oynuyordu. İlk kez meyvelerden kocaman bir güneş resmi yapacaktı. Ama tepe eğikti ve yuvarlak elmalar hep aşağı kaydı. Maşa elmaları tek tek topladı ve biraz düşündü. Sonra hemen başka bir yer denedi. Yakında düz ve geniş bir taş buldu. Meyveleri bu taşın üstüne dizdi. Ortaya bir portakal, çevresine sarı muzlar koydu. Bu kez hiçbir meyve kaymadı. Güneş resmi çok güzel oldu. Maşa resmini taşın üstünde sergiledi ve ellerini çırptı. Maşa bundan sonra meyvelerini hep düz bir yere dizdi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ortaya bir portakal, çevresine"
   - Cümle 8: «Ortaya bir portakal, çevresine sarı muzlar koydu.»
   - Açıklama: 'Çevresine' ile uyum için 'ortasına' olmalı; 'ortaya' tamlamayı bozuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ortaya bir portakal, çevresine sarı muzlar koydu"
   - Cümle 8: «Ortaya bir portakal, çevresine sarı muzlar koydu.»
   - Açıklama: Sorunu yaratan elmalar toplanıp düz taşa taşınıyor ama resimde hiç kullanılmıyor; portakal ve muzlar sebepsiz beliriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "resmini taşın üstünde sergiledi"
   - Cümle 11: «Maşa resmini taşın üstünde sergiledi ve ellerini çırptı.»
   - Açıklama: 'Sergiledi' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sergiledi' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0087` birebir aynı, ardından `@onarim: ac66428db15f6586feec003e415943cc5d540c3b`, sonra gövde.

### Hikâye 9: tohum masa-0088 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0088
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'sis', fiil 'doymak', sıfat 'sabırlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: sis yüzünden aç kirpi elmaları göremedi | yere eğilip çimenlere elleriyle dokundu ve elma buldu
@tohum: masa-0088
@degisim: sabırlı -> kalın
Ormanda kalın bir sis vardı. Maşa patikada aç bir kirpi gördü. Kirpi elma arıyordu ama sis yüzünden hiçbir şey göremiyordu. "Gel, kirpi, birlikte elma arayalım," dedi Maşa. İkisi büyük bir elma ağacının altına gitti. Maşa yere eğildi ve çimenlere elleriyle dokunmayı denedi. Parmakları yuvarlak bir şeye değdi. Bu, kırmızı bir elmaydı! Maşa iki elma daha buldu ve kirpiye verdi. Kirpi elmaları hemen yedi ve sonunda doydu. Sonra burnunu Maşa'nın eline sürttü. Maşa ile kirpi sisin içinde yan yana mutlu mutlu yürüdü.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İkisi büyük bir elma ağacının altına gitti"
   - Cümle 5: «İkisi büyük bir elma ağacının altına gitti.»
   - Açıklama: Sis yüzünden hiçbir şey görünmezken elma ağacı sebepsizce bulunuyor ve çözümü kolaylaştırıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İkisi büyük bir elma ağacının altına gitti"
   - Cümle 5: «İkisi büyük bir elma ağacının altına gitti.»
   - Açıklama: Sis yüzünden hiçbir şey görülemiyorken elma ağacını kolayca bulmaları çelişiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimenlere elleriyle dokunmayı denedi"
   - Cümle 6: «Maşa yere eğildi ve çimenlere elleriyle dokunmayı denedi.»
   - Açıklama: Dokunmak denenecek bir iş değil; 'denedi' fiili burada yanlış anlamda kullanılmış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elleriyle dokunmayı denedi"
   - Cümle 6: «Maşa yere eğildi ve çimenlere elleriyle dokunmayı denedi.»
   - Açıklama: Dokunmak zor bir iş değil; 'denedi' fiili yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0088` birebir aynı, `@degisim: sabırlı -> kalın` (tutuyorsan), ardından `@onarim: 41700eaf1d009c9d4822a7026572263d340afc7e`, sonra gövde.

### Hikâye 10: tohum masa-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0089
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çalı', fiil 'düzelmek', sıfat 'çizgili'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çalıdan garip bir tık tık sesi geldi | çalının altından baktı ve sesi yapan dalı buldu
@tohum: masa-0089
Rüzgar esiyordu. Maşa ormandaki patikada koşuyordu. Birden bir çalıdan tık tık diye garip bir ses geldi. Maşa bu sesi çok merak etti ve çalının yanına gitti. Ama yapraklar sıktı ve içi görünmüyordu. Maşa önce parmak uçlarına kalktı ama bir şey göremedi. Sonra yere yatıp çalının altından bakmayı denedi. İçeride ince bir dal vardı. Rüzgar esince bu dal eğiliyor ve çizgili büyük bir taşa vuruyordu. Rüzgar durunca dal yavaşça düzeldi ve ses de kesildi. Maşa yerden kalktı ve ellerini çırptı. Maşa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama yapraklar sıktı"
   - Cümle 5: «Ama yapraklar sıktı ve içi görünmüyordu.»
   - Açıklama: 'sıktı' hem 'sık idi' hem 'sıkmak' fiili olarak okunabiliyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0089` birebir aynı, ardından `@onarim: 4bc956f2031031da666ce7f50422f284b70a2aa0`, sonra gövde.

### Hikâye 11: tohum masa-0090 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0090
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çarşaf', fiil 'sarılmak', sıfat 'ilginç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: rüzgar sürprizin çarşafını havaya kaldırdı | çarşafın her köşesine bir reçel kavanozu koydu
@tohum: masa-0090
Ormanda Maşa ile Daşa, sincap için bir sürpriz hazırlıyordu. Büyük bir ağacın altına beyaz bir çarşaf serdiler ve fındık koydular. Ama rüzgar esti, çarşaf havaya kalktı ve fındıklar yere yuvarlandı. "Maşa, rüzgar fındıkları uçuruyor!" dedi Daşa. Maşa hemen sepetine baktı. Sepette en sevdiği reçellerden dört küçük kavanoz vardı. Maşa kavanozları çarşafın dört ucuna tek tek koydu. Rüzgar yine esti ama çarşaf artık kalkmadı. İki kız fındıkları toplayıp ortaya geri koydu. "Reçel kavanozları çarşafı tuttu, ne ilginç, Maşa!" dedi Daşa. Tam o sırada sincap ağaçtan hızla indi. Fındıkları görünce sevinçle bir tanesine sarıldı. Maşa çok sevindi, çünkü sürprizleri sincabı mutlu etmişti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "rüzgar sürprizin çarşafını havaya"
   - Cümle 0 (plan satırı): «rüzgar sürprizin çarşafını havaya kaldırdı | çarşafın her köşesine bir reçel kavanozu koydu»
   - Açıklama: 'Sürprizin çarşafı' tamlaması anlamsız; plan satırı bozuk.
   - Açıklama: 'Sürprizin çarşafı' tamlaması anlamsız ve bozuk.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Maşa ile Daşa, sincap"
   - Cümle 1: «Ormanda Maşa ile Daşa, sincap için bir sürpriz hazırlıyordu.»
   - Açıklama: Özne ile tümleç arasına gereksiz virgül konmuş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa hemen sepetine baktı"
   - Cümle 5: «Maşa hemen sepetine baktı.»
   - Açıklama: Daha önce hiç anılmayan sepet ve içindeki dört reçel kavanozu çözümü getirmek için sebepsizce beliriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepette en sevdiği reçellerden dört küçük kavanoz vardı"
   - Cümle 6: «Sepette en sevdiği reçellerden dört küçük kavanoz vardı.»
   - Açıklama: Çözümü sağlayan reçel kavanozları daha önce kurulmadan sepette sebepsizce beliriyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ne ilginç, Maşa"
   - Cümle 10: «"Reçel kavanozları çarşafı tuttu, ne ilginç, Maşa!" dedi Daşa.»
   - Açıklama: 'İlginç' soyut bir kelime, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'İlginç' soyut bir kelime, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0090` birebir aynı, ardından `@onarim: 8147c2c89c98509595175272f4f4f0d9a4af83de`, sonra gövde.

### Hikâye 12: tohum masa-0091 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0091
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: kaybolan eşya
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'baston', fiil 'sığınmak', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: koşarken çikolatalı baston şeker elinden düştü | yerdeki reçel izlerine bakarak şekeri buldu
@tohum: masa-0091
Bahçede Maşa, Koca Ayı'nın yanında çikolatalı baston şekerini reçele batırıp yiyordu. Birden sert bir rüzgar çıktı ve ikisi koşarak eve sığındı. Ama koşarken baston şeker Maşa'nın elinden düşmüştü. Biraz sonra rüzgar durdu ve Maşa bahçeye çıktı. Çimenlerin arasında şekeri hiçbir yerde göremedi. Sonra reçel yediği yere döndü. Otların üstünde küçük, parlak reçel damlaları vardı. Şekerden damlayan reçel, koştuğu yola iz bırakmıştı. Maşa damlaların peşinden yürüdü. Son damla bir çalının dibindeydi. Çikolatalı şeker de orada, yaprakların arasında duruyordu. Maşa şekeri aldı ve sevinçle Koca Ayı'ya gösterdi. Koca Ayı gülümseyip başını salladı. Maşa bundan sonra rüzgarlı havada şekerini sıkıca tuttu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ikisi koşarak eve sığındı"
   - Cümle 2: «Birden sert bir rüzgar çıktı ve ikisi koşarak eve sığındı.»
   - Açıklama: 'Sığınmak' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "ikisi koşarak eve sığındı"
   - Cümle 2: «Birden sert bir rüzgar çıktı ve ikisi koşarak eve sığındı.»
   - Açıklama: Hikaye bahçede başlıyor, eve geçiyor ve yeniden bahçeye dönüyor; tek sahne kuralı çiğneniyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Biraz sonra rüzgar durdu ve Maşa bahçeye çıktı"
   - Cümle 4: «Biraz sonra rüzgar durdu ve Maşa bahçeye çıktı.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor, eve geçiyor ve yeniden bahçede bitiyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "koştuğu yola iz bırakmıştı"
   - Cümle 8: «Şekerden damlayan reçel, koştuğu yola iz bırakmıştı.»
   - Açıklama: Cümlenin öznesi reçel olduğu için 'koştuğu' kelimesinin kimi gösterdiği belli değil.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "reçel, koştuğu yola iz"
   - Cümle 8: «Şekerden damlayan reçel, koştuğu yola iz bırakmıştı.»
   - Açıklama: Cümlenin öznesi reçel iken 'koştuğu' kimin koştuğunu belirtmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0091` birebir aynı, ardından `@onarim: 0b9d4904894d8af2e6be551e410e45f4c49a538f`, sonra gövde.
