# Editör görevi (onarım): Maşa, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0132 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0132
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'leke', fiil 'uzatmak', sıfat 'düzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: top kocaman bir çalının altına kaçtı | kirpiye reçel uzatıp ondan yardım istedi
@tohum: masa-0132
@degisim: düzgün -> kocaman
Maşa bahçede kırmızı topuyla oynuyordu. Yanında bir kavanoz reçel ve bir kaşık vardı. Birden top yere çarpıp zıpladı ve kocaman bir çalının altına kaçtı. Maşa kolunu dalların arasına soktu ama topa yetişemedi. O sırada çalının yanından küçük bir kirpi geçti. Maşa kirpiden yardım istemeye karar verdi. Kaşığa biraz reçel koydu ve kirpiye uzattı. Sonra parmağıyla çalının altını gösterdi. Kirpi kaşığı yaladı ve dalların altına girdi. Burnuyla topu dışarı itti. Top yuvarlandı ve Maşa'nın ayağına geldi. Kirpi burnunda küçük bir reçel lekesiyle çıktı. Maşa güldü ve lekeyi bir yaprakla sildi. Maşa çok mutlu oldu, çünkü kirpi topunu geri getirmişti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bahçede kırmızı topuyla oynuyordu"
   - Cümle 1: «Maşa bahçede kırmızı topuyla oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bitiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kirpi topunu geri getirmişti"
   - Cümle 14: «Maşa çok mutlu oldu, çünkü kirpi topunu geri getirmişti.»
   - Açıklama: 'Topunu' kirpinin kendi topu gibi okunuyor; top Maşa'nın.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0132` birebir aynı, `@degisim: düzgün -> kocaman` (tutuyorsan), ardından `@onarim: 7f467f37390fbece753181f496cdfb77902d89dd`, sonra gövde.

### Hikâye 2: tohum masa-0133 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap, Daşa
@tohum: masa-0133
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'tebeşir', fiil 'olgunlaşmak', sıfat 'hızlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | sincap, Daşa
@plan: iki kız çizmek istedi ama tek tebeşir vardı | tebeşiri ikiye bölüp bir parçayı kuzenine verdi
@tohum: masa-0133
@degisim: olgunlaşmak -> çizmek
Maşa'nın evinin önünde serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa ağaçtaki hızlı bir sincabı izliyordu. İkisi de bu sincabın resmini yere çizmek istedi. Ama ellerinde tek bir beyaz tebeşir vardı. Maşa tebeşiri ikiye bölmeyi denedi. Tebeşir kolayca iki parça oldu. "Al, Daşa, bu parça senin!" dedi Maşa. "Teşekkürler, Maşa!" dedi Daşa. Maşa yere zıplayan bir sincap çizdi. Daşa da sincabın önüne üç fındık ekledi. Sincap ağaçtan indi, resimdeki fındıkları kokladı ve kuyruğunu salladı. İki kuzen buna çok güldü. Sonra Maşa ile Daşa yeni resimler yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ellerinde tek bir beyaz tebeşir vardı"
   - Cümle 4: «Ama ellerinde tek bir beyaz tebeşir vardı.»
   - Açıklama: Tek tebeşir sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0133` birebir aynı, `@degisim: olgunlaşmak -> çizmek` (tutuyorsan), ardından `@onarim: 04f4e9e5d6c717a0aff46b7986dfde117f4cd340`, sonra gövde.

### Hikâye 3: tohum masa-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı
@tohum: masa-0134
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'nota', fiil 'kurtulmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı
@plan: yağmur pikniği bozdu ve ayı çok üzüldü | boş kavanozla yağmur şarkısı yapıp ayıyı güldürdü
@tohum: masa-0134
@degisim: utangaç -> boş
Ormanda Maşa ile Koca Ayı piknik yapıyordu. Birden yağmur başladı ve piknik yarım kaldı. Koca Ayı buna çok üzüldü. İkisi büyük bir ağacın altına koştu ve yağmurdan kurtuldu. Maşa, Koca Ayı'yı güldürmek istedi. Sepette biraz reçel kalmıştı. Maşa reçeli çok severdi ve son kaşığını hemen yedi. Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu. Damlalar kavanoza ve bardaklara düşünce farklı sesler çıktı. Her ses ayrı bir nota gibiydi. "Dinle, Koca Ayı, bu bizim yağmur şarkımız!" dedi Maşa. Koca Ayı gülümsedi ve başını sağa sola salladı. Maşa çok sevindi, çünkü Koca Ayı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "boş kavanozu ve iki boş bardağı yağmurun altına koydu"
   - Cümle 8: «Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu.»
   - Açıklama: Sorunun sebebi yağmurun pikniği bozması ama çözüm pikniğe dönmüyor, yalnız ayıyı oyalıyor; çözüm sebebe doğrudan yönelmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Her ses ayrı bir nota gibiydi"
   - Cümle 10: «Her ses ayrı bir nota gibiydi.»
   - Açıklama: Benzetme ve 'nota' kelimesi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Nota' benzetmesi 3 yaşındaki çocuk için soyut ve bilinmeyen bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0134` birebir aynı, `@degisim: utangaç -> boş` (tutuyorsan), ardından `@onarim: c295a834ef9634d8b9356cf1c5f5933f6bdba7d2`, sonra gövde.

### Hikâye 4: tohum masa-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0138
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kavun', fiil 'çekilmek', sıfat 'şeffaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: ağacın arkasından bilinmeyen bir ses geldi | parmak uçlarında yürüdü ve sesi yapan kirpiyi buldu
@tohum: masa-0138
Bir sabah Maşa ormanda bir kütüğün üstünde oturuyordu. Şeffaf bir kutudan dilim dilim kavun yiyordu. Birden ağacın arkasından hışır hışır bir ses geldi. Maşa bu sesi çok merak etti. "Orada kim var?" diye seslendi Maşa. Ama ses hemen kesildi. Bu kez Maşa parmak uçlarında sessizce yürümeyi denedi. Ağacın arkasında küçük bir kirpi kuru yaprakları eşeliyordu. Kirpi Maşa'yı görünce durdu. Maşa yere bir dilim kavun bıraktı ve biraz geri çekildi. Kirpi yavaşça yaklaştı ve kavunu kokladı. Sonra kavunu afiyetle yemeye başladı. "Demek o ses sendin," dedi Maşa gülerek. Maşa çok sevindi, çünkü sesi yapan küçük kirpiyi bulmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şeffaf bir kutudan dilim"
   - Cümle 2: «Şeffaf bir kutudan dilim dilim kavun yiyordu.»
   - Açıklama: 'Şeffaf' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden ağacın arkasından hışır hışır bir ses geldi"
   - Cümle 3: «Birden ağacın arkasından hışır hışır bir ses geldi.»
   - Açıklama: Ormanda bilinmeyen bir sesin gizemi küçük çocuk için ürkütücü bir öğe kuruyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bu kez Maşa parmak uçlarında sessizce yürümeyi denedi"
   - Cümle 7: «Bu kez Maşa parmak uçlarında sessizce yürümeyi denedi.»
   - Açıklama: Çocuk ormanda bilinmeyen bir sese tek başına gizlice yaklaşıyor; taklit edilirse güvensiz.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuru yaprakları eşeliyordu"
   - Cümle 8: «Ağacın arkasında küçük bir kirpi kuru yaprakları eşeliyordu.»
   - Açıklama: 'Eşelemek' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0138` birebir aynı, ardından `@onarim: 4664d61e2f542b92d11b408873bbc1756ec34e95`, sonra gövde.

### Hikâye 5: tohum masa-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0139
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çekirdek', fiil 'ilgilenmek', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ayçiçeği çok uzundu ve eli ona yetişemedi | sapını yavaşça salladı ve çekirdekler döküldü
@tohum: masa-0139
Maşa ormanda çiçekli bir açıklıkta koşuyordu. Birden kocaman bir ayçiçeği gördü ve onunla hemen ilgilendi. Ortası siyah çekirdek doluydu, ama ayçiçeği Maşa'dan çok uzundu. Maşa birkaç çekirdek alıp bahçesine ekmek istedi. Parmak uçlarında uzandı ama eli yetişemedi. Maşa çevresine baktı ve biraz düşündü. Sonra ince sapı yavaşça sallamayı denedi. Ayçiçeğinin başı eğildi ve çekirdekler çimenlere döküldü. Maşa onları tek tek topladı. Hepsini cebine koydu. Küçük cebi hemen doldu. Maşa çok sevindi, çünkü artık bahçesi için çekirdekleri vardı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onunla hemen ilgilendi"
   - Cümle 2: «Birden kocaman bir ayçiçeği gördü ve onunla hemen ilgilendi.»
   - Açıklama: 'İlgilenmek' burada yanlış anlamda; kastedilen 'merak etti' ya da 'baktı'.
   - Açıklama: 'İlgilenmek' burada yanlış anlamda; çiçeğe merakla baktığı anlatılmıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ortası siyah çekirdek doluydu, ama ayçiçeği Maşa'dan çok uzundu.»
   - Açıklama: İlk üç cümlede Maşa'nın hedefi ve elinin yetişmediği söylenmiyor; sorun ancak 4. ve 5. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0139` birebir aynı, ardından `@onarim: 74ee4ed0524a80db71ece94d0b7788cb7588d659`, sonra gövde.

### Hikâye 6: tohum masa-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0141
- yer: dağ (Ormanın yanındaki tepe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yatak', fiil 'temizlenmek', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: kuzeninin yiyeceği yoktu ve tek ekmek vardı | reçelli ekmeğini ikiye bölüp kuzeniyle paylaştı
@tohum: masa-0141
@degisim: yatak -> kırıntı
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa çimenlerin üstünde oturuyordu. Maşa'nın elinde tek bir reçelli ekmek vardı, ama Daşa'nın yiyeceği yoktu. Daşa şehirden gelirken çantasını evde unutmuştu. Maşa reçeli çok severdi, ama ekmeğini hemen ikiye böldü. "Al, Daşa, yarısı senin!" dedi Maşa. "Teşekkürler, Maşa!" dedi Daşa. İkisi ekmeklerini yerken bir kayanın arkasında saklı bir sincap gördü. Maşa ekmeğinden birkaç kırıntıyı sincap için yere bıraktı. Sincap hemen dışarı çıktı ve kırıntıları topladı. Çimenlerin üstü bir anda temizlendi. Maşa bundan sonra ekmeğini hep dostlarıyla paylaştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir kayanın arkasında saklı bir sincap gördü"
   - Cümle 8: «İkisi ekmeklerini yerken bir kayanın arkasında saklı bir sincap gördü.»
   - Açıklama: Sorun çözüldükten sonra sincap sebepsiz beliriyor ve ana olaya hiçbir katkı yapmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çimenlerin üstü bir anda temizlendi"
   - Cümle 11: «Çimenlerin üstü bir anda temizlendi.»
   - Açıklama: Çimenlerin temizlenmesi hiçbir sorunla bağlı olmayan işlevsiz bir ayrıntı.
   - Açıklama: Birkaç kırıntı bırakılmışken çimenlerin temizlenmesi sebepsiz ve olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0141` birebir aynı, `@degisim: yatak -> kırıntı` (tutuyorsan), ardından `@onarim: 18b2ba14a682405499bb21a7d03b8d2d59d9bbe0`, sonra gövde.

### Hikâye 7: tohum masa-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0142
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çöp', fiil 'kıvırmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: böğürtlenler küçük ellerinden düşüyordu | büyük bir yaprağı külah gibi kıvırdı
@tohum: masa-0142
@degisim: çöp -> yaprak
Bir sabah Maşa ormanda bir patikada yürüyordu. Birden böğürtlenlerle dolu bir çalı gördü. Maşa reçel için böğürtlen topladı, ama hepsi küçük ellerinden düşüyordu. Maşa etrafına baktı ve büyük, yumuşacık bir yaprak buldu. Yaprağı bir külah gibi kıvırdı. Sonra böğürtlenleri tek tek külahın içine koydu. Yaprak hiç yırtılmadı ve hiçbir böğürtlen düşmedi. Biraz sonra külah doldu. Maşa dolu külahı iki eliyle tuttu. Artık reçel için bir sürü böğürtleni vardı ve Maşa mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa reçel için böğürtlen topladı"
   - Cümle 3: «Maşa reçel için böğürtlen topladı, ama hepsi küçük ellerinden düşüyordu.»
   - Açıklama: 'Topladı' işin başarıldığını söylüyor ama hepsi düşüyor; 'toplamaya çalıştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0142` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: 8321035e7942894de1a33f968324e564588167ba`, sonra gövde.

### Hikâye 8: tohum masa-0143 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0143
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pasta', fiil 'oynamak', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: utangaç kirpi taşın arkasına saklandı | ona reçelli pasta verip oyuna çağırdı
@tohum: masa-0143
Bir sabah tepede ılık bir rüzgar esiyordu. Maşa çimenlere oturmuş, reçelli pastasını yiyordu. Küçük bir kirpi ona bakıyordu ama çok utangaçtı ve taşın arkasına saklandı. Maşa onunla arkadaş olmak ve oynamak istedi. Sonra küçük bir parça kopardı. Parçayı yavaşça taşın yanına koydu. "Bu senin için, gel birlikte yiyelim," dedi Maşa. Kirpi burnunu çıkardı ve kokladı. Sonra küçük adımlarla yaklaştı ve parçayı yedi. Maşa yerden bir çam kozalağı aldı ve kirpiye doğru yuvarladı. Kirpi kozalağı burnuyla geri itti. "Sen çok iyi oynuyorsun!" dedi Maşa gülerek. Maşa çok mutluydu, çünkü tepede yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "ama çok utangaçtı ve taşın arkasına saklandı"
   - Cümle 3: «Küçük bir kirpi ona bakıyordu ama çok utangaçtı ve taşın arkasına saklandı.»
   - Açıklama: Kartın yanlar bölümünde kirpi dost canlısı olarak geçiyor; utangaç ve kaçan bir kirpi ilişkiye aykırı.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "tepede yeni bir arkadaş bulmuştu"
   - Cümle 13: «Maşa çok mutluydu, çünkü tepede yeni bir arkadaş bulmuştu.»
   - Açıklama: Kartta kirpi Maşa'nın bilinen orman dostu; yeni tanışılan bir yabancı gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0143` birebir aynı, ardından `@onarim: 1acbeb2b6335e332cad42538d016c2b83db80b45`, sonra gövde.

### Hikâye 9: tohum masa-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0148
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kaya', fiil 'ayrılmak', sıfat 'benekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: rüzgar kavanoz kapağını dikenli çalının altına yuvarladı | kirpiden kapağı getirmesi için yardım istedi
@tohum: masa-0148
Maşa ile kirpi tepede benekli bir kayanın yanında oturuyordu. Maşa reçel yiyordu, kirpi de elmasını kemiriyordu. Birden rüzgar esti ve kayadaki kavanoz kapağı dikenli bir çalının altına yuvarlandı. Maşa dikenlere dokunmak istemedi. Ama kapak olmazsa en sevdiği reçele toz girecekti. Maşa kirpiye döndü. "Kirpi, senin de dikenlerin var, kapağı getirir misin?" diye sordu Maşa. Kirpi elmasından ayrıldı ve çalının altına girdi. Burnuyla kapağı itti ve dışarı çıkardı. Maşa kapağı aldı ve kavanozu sıkıca kapattı. "Çok teşekkürler, kirpi," dedi Maşa. Kirpi de mutlu mutlu burnunu oynattı. Maşa bundan sonra zor bir işte hep yardım istedi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "senin de dikenlerin var"
   - Cümle 7: «"Kirpi, senin de dikenlerin var, kapağı getirir misin?" diye sordu Maşa.»
   - Açıklama: 'de' (dahi) Maşa'nın da dikeni varmış gibi yanlış anlam veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0148` birebir aynı, ardından `@onarim: 2f282feb24487a8e6e57cd372e949ba438983bec`, sonra gövde.

### Hikâye 10: tohum masa-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0150
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'zincir', fiil 'saklanmak', sıfat 'çalışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: papatyaları bağladı ama ince bir sap koptu | her sapı parmağıyla deldi ve çiçekleri geçirdi
@tohum: masa-0150
@degisim: saklanmak -> bağlamak
Çalışkan arılar çiçeklerin arasında vızıldıyordu. Maşa ormanda ilk kez papatyalardan bir zincir yapıyordu. Maşa papatyaları birbirine bağladı ama bir papatyanın ince sapı hemen koptu. Zincir dağıldı ve çiçekler yere düştü. Maşa durmadı ve yeniden denedi. Parmağıyla her sapı ortasından deldi. Sonra bir çiçeği öbür çiçeğin deliğinden geçirdi. Bu kez zincir hiç kopmadı. Maşa bir sürü papatyayı arka arkaya dizdi. Sonra uzun zinciri bir halka yaptı ve başına taç gibi taktı. Maşa bundan sonra papatya zincirini hep böyle yaptı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve çiçekleri geçirdi"
   - Cümle 0 (plan satırı): «papatyaları bağladı ama ince bir sap koptu | her sapı parmağıyla deldi ve çiçekleri geçirdi»
   - Açıklama: Plandaki 'geçirdi' fiilinin nereden geçirildiğini gösteren tümleci eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0150` birebir aynı, `@degisim: saklanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 4f167598747bf98a40a57e62dbc47dec7fd88e3e`, sonra gövde.

### Hikâye 11: tohum masa-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: reçel için çilek arıyordu ama hiç göremedi | her yeri kokladı ve çilekleri yaprakların altında buldu
@tohum: masa-0151
Maşa sepetiyle ormandaki patikada yürüyordu. Reçel yapmak için çilek arıyordu ama bir tane bile göremedi. Patikanın kenarı büyük yapraklarla kaplıydı. Maşa somurtkan bir yüzle bir ağacın altına oturdu. Birden tatlı bir koku aldı. Maşa reçeli çok severdi ve bu kokuyu hemen tanıdı. Bu, çilek reçelinin kokusuna benziyordu. Maşa kokunun nereden geldiğini çok merak etti. Yere eğildi ve her yeri kokladı. Koku büyük yaprakların altından geliyordu. Maşa yaprakları kaldırdı ve kırmızı çilekleri gördü. Çilekleri toplayıp sepetine doldurdu. Sonra onları korumak için üstlerine sepetteki bezi örttü. Maşa çok sevindi, çünkü reçel için çilekleri bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "onları korumak için üstlerine sepetteki bezi örttü"
   - Cümle 13: «Sonra onları korumak için üstlerine sepetteki bezi örttü.»
   - Açıklama: Bez ve koruma adımı sorunla ilgisiz, hiçbir işe yaramayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0151` birebir aynı, ardından `@onarim: d733197438be0ee2d4d8d0c55b6e8494ab97e8f7`, sonra gövde.

### Hikâye 12: tohum masa-0154 (deneme 2 -> 3)

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
@plan: kirpi baharatlı elmayı kokladı ve yemedi | elma dilimini suyla ıslattı ve üstünü sildi
@tohum: masa-0154
Güneşli bir gündü ve ormanda kuşlar ötüyordu. Koca Ayı, Maşa ile kirpiye elma dilimleri verdi ve üstlerine baharat serpti. Ama kirpi baharatlı elmayı kokladı, yüzünü buruşturdu ve yemedi. Maşa elmasını kirpiyle paylaşmak istedi. Hemen yeni bir şey denedi. Bir elma dilimini şişedeki suyla ıslattı ve üstünü parmağıyla sildi. Sonra dilimi kirpiye uzattı. "Kirpi, bu sana, afiyet olsun!" dedi Maşa. Kirpi dilimi kokladı ve bu kez yüzünü buruşturmadı. Elmayı çıtır çıtır yedi ve burnunu Maşa'nın eline sürdü. Koca Ayı da gülümsedi ve başını salladı. Maşa çok sevindi, çünkü elmasını kirpiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa elmasını kirpiyle paylaşmak istedi"
   - Cümle 4: «Maşa elmasını kirpiyle paylaşmak istedi.»
   - Açıklama: Kirpiye zaten kendi elma dilimi verilmişken hedef paylaşmak olarak kuruluyor ve sorun (baharat) ile hedef birbirini tutmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şişedeki suyla ıslattı"
   - Cümle 6: «Bir elma dilimini şişedeki suyla ıslattı ve üstünü parmağıyla sildi.»
   - Açıklama: Su şişesi daha önce hiç kurulmadan çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0154` birebir aynı, ardından `@onarim: 28df99aeefa7f6cd7906b9d55571df1f10c1dc00`, sonra gövde.
