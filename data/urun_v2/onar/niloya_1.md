# Editör görevi (onarım): Niloya, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Niloya | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar1.txt --ad urun_v2`
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

## Kart: Niloya (kaynaklı, kapalı dünya)

- Ad: Niloya (okunuş: niloya; kesme eki okunuşa uyar)
- Kimlik: Niloya, nehir kenarındaki bir köyde ailesiyle yaşayan küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Niloya'nın merakı bakarak, sorarak ve bir büyüğe haber vererek gösterilir; nehre ya da dereye girmez, suya yalnız kıyıdan bakar; ağaca ya da yüksek yere tırmanmaz.
- Özellikler:
  - keşfet: Öğrenmeyi ve yeni şeyler keşfetmeyi sever. (örnek biçimler: keşfetti, keşfetmeyi, keşfedince)
  - soru: Merak ettiği her şeyi sorar. (örnek biçimler: sordu, soruyu, sorular)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
- Yerler:
  - orman: Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.
  - dağ: Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.
  - ev: Niloya'nın nehir kenarındaki köy evi ve bahçesi.
  - park: Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Murat: Niloya'nın ağabeyi; küçük kardeşi Niloya'yı çok sever. Tür: oğlan; konuşur; huy: Top oynamayı, koşturmayı ve fındık toplamayı sever.. Yüzey biçimleri: Murat, ağabey, ağabeyi, abi, abisi, abiciğim
  - Mete: Murat'ın en yakın arkadaşı; Niloya ile aynı yaştadır ve onun da arkadaşıdır. Tür: oğlan; konuşur; huy: Oyuncaklarını dağıtır, sonra aradığını bulamaz.. Yüzey biçimleri: Mete
  - Tospik: Niloya'nın kaplumbağası ve en yakın arkadaşı. Tür: kaplumbağa; konuşur; huy: Oyun oynamayı ve uyumayı sever; Niloya'ya yetişmekte zorlanır.. Yüzey biçimleri: Tospik, kaplumbağa, kaplumbağası
  - dedesi: Niloya'nın dedesi; herkese iyi öğütler verir. Tür: dede; konuşur. Yüzey biçimleri: dede, dedesi, dedeciğim, Dede
  - babaannesi: Niloya'nın babaannesi; yemek yapmayı ve fındık toplamayı sever. Tür: babaanne; konuşur. Yüzey biçimleri: babaanne, babaannesi, babaanneciğim, Babaanne, nine, ninesi
  - annesi: Niloya'nın annesi; yemek yapmayı, ekinleri ve yaylayı sever. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
- Dünya kuralları:
  - Niloya'nın ağabeyi Murat'tır. Mete Niloya'nın ağabeyi değildir; Murat'ın arkadaşıdır.
  - Tospik yavaştır; Niloya'ya yetişmekte zorlanır, hızla koşmaz.
  - Köy nehir kenarındadır; hikayede kimse nehre ya da dereye girmez, suya kıyıdan bakılır.
- Yasak adlar: Elif, Mine, Fatoş, Cem, Ayşecik, Sarıkanat, Miniş
- Yasak: Babası kartta yok; hikayeye girmez (kapalı dünya).
- İzinli dünya kelimeleri: köy, nehir, yayla, fındık, kaplumbağa, kekik

## Onarılacak hikâyeler

### Hikâye 1: tohum niloya-0001 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0001
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi ve yeni şeyler keşfetmeyi sever.)
- kelimeler: isim 'düdük', fiil 'gülüşmek', sıfat 'pahalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: yakında kekik yoktu ve sepet boş kaldı | tepeyi keşfetti ve kekik bulunca düdük çaldı
@tohum: niloya-0001
@degisim: pahalı -> yeşil
Rüzgar tepelerde hafif hafif esiyordu. Niloya babaannesiyle dağda kekik topluyordu. Ama sepet boştu, çünkü yakında hiç kekik yoktu. "Buralarda hiç kekik kalmamış," dedi babaannesi. Sonra Niloya'ya küçük bir düdük verdi. "Kekik bulursan bu düdüğü çal," dedi babaannesi. Niloya tepeyi keşfetmeye başladı. Büyük bir kayanın arkasında yeşil kekikler buldu. Niloya hemen düdüğü çaldı. Babaannesi sesi duydu ve Niloya'nın yanına geldi. "Burada ne çok kekik var!" dedi babaannesi. İkisi sepeti birlikte doldurdu. Sonra dolu sepete bakıp gülüştüler. Niloya çok mutluydu, çünkü babaannesine yardım etmişti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya tepeyi keşfetmeye başladı"
   - Cümle 7: «Niloya tepeyi keşfetmeye başladı.»
   - Açıklama: Küçük çocuk büyüğünden ayrılıp tepede tek başına kayanın arkasına kadar gidiyor; güvenli kullanım satırı merakın bakarak, sorarak ve büyüğe haber vererek gösterilmesini istiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Niloya tepeyi keşfetmeye başladı."
   - Cümle 7: «Niloya tepeyi keşfetmeye başladı.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki bir çocuk için soyut ve zor bir kelime.
   - Açıklama: 'Keşfetmek' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0001` birebir aynı, `@degisim: pahalı -> yeşil` (tutuyorsan), ardından `@onarim: 1d7a2d7c149248f49919d8f230eb57bda6a4f5c1`, sonra gövde.

### Hikâye 2: tohum niloya-0003 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0003
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yağmur ya da kar günü
- yan: dedesi
- özellik: keşfet (Öğrenmeyi ve yeni şeyler keşfetmeyi sever.)
- kelimeler: isim 'kalem', fiil 'barışmak', sıfat 'ıslak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: yağmur başladı ve kağıt ıslandı | kayanın altında kuru bir yer keşfetti ve orada çizdi
@tohum: niloya-0003
@degisim: barışmak -> çizmek
Yağmur birden tıp tıp yağmaya başladı. Niloya o sırada dedesiyle dağda kalemle resim çiziyordu. Yağmur damlaları Niloya'nın kağıdını ıslattı. "Bu ıslak kağıda çizmek çok zor," dedi dedesi. Niloya çevreye dikkatle baktı. Büyük bir kayanın altında kuru bir yer keşfetti. "Dede, gel, burası hiç ıslak değil," dedi Niloya. İkisi kayanın altına oturdu. Niloya kağıdın kuru arkasını çevirdi ve yeşil tepeleri çizdi. Dedesi resme baktı ve gülümsedi. "Çok güzel olmuş, Niloya," dedi dedesi. Dedesi de Niloya da çok mutluydu, çünkü resim yağmurda bile bitmişti.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kayanın altında kuru bir yer keşfetti ve orada çizdi"
   - Cümle 0 (plan satırı): «yağmur başladı ve kağıt ıslandı | kayanın altında kuru bir yer keşfetti ve orada çizdi»
   - Açıklama: Islak kağıt sorununu çözen kağıdın kuru arkasını çevirmek, plan bu asıl adımı söylemiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "kuru bir yer keşfetti"
   - Cümle 6: «Büyük bir kayanın altında kuru bir yer keşfetti.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki çocuğun bilmeyebileceği bir kelime; 'buldu' olmalı.
   - Açıklama: 'Keşfetmek' 3 yaşındaki çocuğun bileceği bir kelime değil; 'buldu' yeterli.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kağıdın kuru arkasını çevirdi"
   - Cümle 9: «Niloya kağıdın kuru arkasını çevirdi ve yeşil tepeleri çizdi.»
   - Açıklama: Kağıdın arkası çevrilmez, kağıt çevrilir; fiil nesnesine uymuyor.
   - Açıklama: Kağıdın arkası çevrilmez, kağıt çevrilir; 'kağıdı çevirdi ve kuru arkasına' olmalı.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Niloya kağıdın kuru arkasını çevirdi"
   - Cümle 9: «Niloya kağıdın kuru arkasını çevirdi ve yeşil tepeleri çizdi.»
   - Açıklama: Kağıdın yağmurda ıslandığı söylendikten sonra arkasının kuru kalması çelişkili duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0003` birebir aynı, `@degisim: barışmak -> çizmek` (tutuyorsan), ardından `@onarim: 493c18b9965c264214df3aa39ed72ff6f6f33956`, sonra gövde.

### Hikâye 3: tohum niloya-0004 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Murat
@tohum: niloya-0004
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'halı', fiil 'tutunmak', sıfat 'yaratıcı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | Murat
@plan: halı küçük bir taşa takıldı ve durdu | neye takıldığını sordu ve ucunu taştan geçirdi
@tohum: niloya-0004
@degisim: yaratıcı -> eski
Parkta Niloya ile Murat uçan halı oyunu oynuyordu. Niloya eski bir halıya oturmuştu, Murat da halıyı çimenlerde çekiyordu. Birden halı bir yere takıldı ve durdu. "Murat, halı neye takıldı?" diye sordu Niloya. "Bilmiyorum, hiç gitmiyor," dedi Murat. Niloya kalktı ve halının ucunu kaldırıp baktı. Halının ucu küçük bir taşa takılmıştı. Niloya ucu taşın üstünden geçirdi. Sonra yine oturdu ve halıya sıkıca tutundu. "Uçan halı yeniden kalkıyor!" dedi Murat. Murat çekince halı çimenlerde kaydı. İkisi kahkahalarla güldü. Niloya ile Murat çok eğlendi, çünkü oyunları yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ucunu taştan geçirdi"
   - Cümle 0 (plan satırı): «halı küçük bir taşa takıldı ve durdu | neye takıldığını sordu ve ucunu taştan geçirdi»
   - Açıklama: Halının ucu taşın içinden geçirilmez; 'taşın üstünden geçirdi' olmalı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Niloya ile Murat uçan halı oyunu oynuyordu"
   - Cümle 1: «Parkta Niloya ile Murat uçan halı oyunu oynuyordu.»
   - Açıklama: Uçan halı masal dünyasından gelen büyülü bir öğedir; kartın kapalı dünyasında ve tohum yasak kategorilerinde (büyü) böyle bir öğe yoktur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0004` birebir aynı, `@degisim: yaratıcı -> eski` (tutuyorsan), ardından `@onarim: 5a276421fb688b639679b7cb15521d8b7fb6015a`, sonra gövde.

### Hikâye 4: tohum niloya-0006 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0006
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'ip', fiil 'taşınmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: ağaçtan tık tık diye bir ses geliyordu | sesin geldiği yere bakıp kovayı iple indirdi
@tohum: niloya-0006
@degisim: taşınmak -> taşımak
Bahçede rüzgar esiyordu. Niloya çimenlerde oynarken tık tık diye bir ses duydu. Ses ağacın dalından geliyordu. Niloya'nın aklına hemen bir soru geldi: Bu ses neydi? Niloya ağacın altına gitti ve yukarı baktı. Alçak bir dalda iple asılı bir kova vardı. Rüzgar esince ağaçtan fındıklar kovaya düşüyordu. İpin öbür ucu ağacın gövdesine bağlıydı. Niloya ipi çözdü ve kovayı yavaşça aşağı indirdi. Kovanın içi fındıkla doluydu. Tık tık sesini fındıklar çıkarıyordu. Niloya kovayı mutlu mutlu eve taşıdı.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede rüzgar esiyordu"
   - Cümle 1: «Bahçede rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor ve eve taşınmayla bitiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor ve eve taşınarak bitiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tık tık diye bir ses duydu"
   - Cümle 2: «Niloya çimenlerde oynarken tık tık diye bir ses duydu.»
   - Açıklama: Zararsız bir sesi merak etmek gerçek bir sorun değil; çözülecek bir dert kurulmuyor.
   - Açıklama: Ağaçtan gelen bir ses yalnız merak konusu; ortada çocuğun önemseyeceği gerçek bir sorun yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Niloya'nın aklına hemen bir soru geldi"
   - Cümle 4: «Niloya'nın aklına hemen bir soru geldi: Bu ses neydi?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Alçak bir dalda iple asılı bir kova vardı"
   - Cümle 6: «Alçak bir dalda iple asılı bir kova vardı.»
   - Açıklama: Kova ve ip kimin astığı söylenmeden sebepsizce beliriyor ve çözümü hazır getiriyor.
   - Açıklama: Kovayı kimin neden astığı söylenmeden kova sebepsizce beliriyor.
   - Açıklama: Dala asılı kova sebepsiz beliriyor ve kimin neden astığı söylenmiyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya kovayı mutlu mutlu eve taşıdı"
   - Cümle 12: «Niloya kovayı mutlu mutlu eve taşıdı.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor ve Niloya sonda eve gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0006` birebir aynı, `@degisim: taşınmak -> taşımak` (tutuyorsan), ardından `@onarim: 1211eaacbf74f71463d3385f88182c544315b905`, sonra gövde.

### Hikâye 5: tohum niloya-0007 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0007
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi ve yeni şeyler keşfetmeyi sever.)
- kelimeler: isim 'peynir', fiil 'sallanmak', sıfat 'düzgün'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: ikisi de aynı dalı çekmek istedi | sırayla dalı çektiler ve fındık topladılar
@tohum: niloya-0007
@degisim: peynir -> fındık
Ormanda Niloya ile Mete fındık ağaçlarını keşfediyordu. Alçak bir dalda çok fındık vardı. İkisi de dalı çekmek istiyordu ama dal ikisine yetmiyordu. "Sırayla yapalım, Mete, önce sen çek," dedi Niloya. Önce Mete dalı çekti. Dal sallandı ve fındıklar yere düştü. Niloya fındıkları toplayıp taşın üstüne düzgün bir şekilde dizdi. Sonra sıra Niloya'ya geldi. Niloya dalı çekince yine fındıklar düştü. Bu kez Mete fındıkları toplayıp onların yanına dizdi. "Bak, ne çok fındık oldu!" dedi Mete. Niloya ile Mete gülüştü ve sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "fındık ağaçlarını keşfediyordu"
   - Cümle 1: «Ormanda Niloya ile Mete fındık ağaçlarını keşfediyordu.»
   - Açıklama: 'keşfetmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Keşfetmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "fındık ağaçlarını keşfediyordu"
   - Cümle 1: «Ormanda Niloya ile Mete fındık ağaçlarını keşfediyordu.»
   - Açıklama: Tohumdaki keşfetme özelliği yalnız açılışta anılıyor, sorunu sırayla çekmek çözüyor; özellik işe yarar biçimde kullanılmamış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Mete fındık ağaçlarını keşfediyordu"
   - Cümle 1: «Ormanda Niloya ile Mete fındık ağaçlarını keşfediyordu.»
   - Açıklama: Tohumdaki keşfetme özelliği yalnız açılışta ad olarak geçiyor, sorunun çözümünde işe yaramıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dal ikisine yetmiyordu"
   - Cümle 3: «İkisi de dalı çekmek istiyordu ama dal ikisine yetmiyordu.»
   - Açıklama: Bir dalın iki kişiye 'yetmemesi' anlamca yerinde değil; sorun ikisinin aynı anda çekememesi.
   - Açıklama: Dalın ikisine 'yetmemesi' anlamca uygun değil; dal paylaşılan bir yiyecek ya da alan değil.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "toplayıp onların yanına dizdi"
   - Cümle 10: «Bu kez Mete fındıkları toplayıp onların yanına dizdi.»
   - Açıklama: 'onların' zamirinin önceki fındıkları mı yoksa Niloya ile Mete'yi mi gösterdiği belirsiz.
   - Açıklama: 'Onların' zamirinin önceki fındıkları mı yeni düşenleri mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0007` birebir aynı, `@degisim: peynir -> fındık` (tutuyorsan), ardından `@onarim: bb8cc6a15d42a98643418a7bae77a7dd7a174d3d`, sonra gövde.

### Hikâye 6: tohum niloya-0011 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Murat
@tohum: niloya-0011
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Murat
- özellik: keşfet (Öğrenmeyi ve yeni şeyler keşfetmeyi sever.)
- kelimeler: isim 'ekmek', fiil 'akmak', sıfat 'çikolatalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | Murat
@plan: sıcakta çikolata eridi ve kurabiyeden aktı | kaydırağın altında gölge keşfetti ve kurabiyeyi orada soğuttu
@tohum: niloya-0011
@degisim: ekmek -> kurabiye
Parkta güneş çok sıcaktı. Niloya, Murat'a sürpriz için çikolatalı bir kurabiye getirmişti. Ama sıcakta çikolata eridi ve kurabiyeden akmaya başladı. Niloya parkı dolaştı ve kaydırağın altında serin bir gölge keşfetti. Kurabiyeyi gölgeye koydu ve biraz bekledi. Çikolata soğudu ve artık akmıyordu. Niloya kurabiyeyi arkasına sakladı ve top oynayan Murat'a gitti. "Gözlerini kapat, abi," dedi Niloya. Murat gözlerini kapattı ve Niloya kurabiyeyi onun eline verdi. Murat gözlerini açınca çok sevindi. "Teşekkürler, Niloya, tam acıkmıştım!" dedi Murat. Murat kurabiyeyi ikiye böldü ve yarısını Niloya'ya verdi. Niloya bundan sonra çikolatayı hep serin bir yerde sakladı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Murat'a sürpriz için çikolatalı"
   - Cümle 2: «Niloya, Murat'a sürpriz için çikolatalı bir kurabiye getirmişti.»
   - Açıklama: 'Sürpriz için' eksik bir yapı; 'sürpriz yapmak için' ya da 'sürpriz olarak' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "serin bir gölge keşfetti"
   - Cümle 4: «Niloya parkı dolaştı ve kaydırağın altında serin bir gölge keşfetti.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki çocuğun bilmeyebileceği bir kelime; 'buldu' yeterli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0011` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: ebe96cf99d2a3146188bb83b6263aef23557580f`, sonra gövde.
