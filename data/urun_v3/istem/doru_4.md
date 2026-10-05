# Yazar görevi: Doru, parti 4

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v3/aday/doru_4.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Doru | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v3/aday/doru_4.txt --ad urun_v3`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Tohumlar

### Doru | dağ | Karatay
@tohum: doru-0073
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'patlıcan', fiil 'kirletmek', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | -
@tohum: doru-0074
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'zambak', fiil 'eğilmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | orman | Kırat
@tohum: doru-0075
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'patates', fiil 'sulamak', sıfat 'ıslak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | orman | Alaca
@tohum: doru-0076
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'küp', fiil 'kurulanmak', sıfat 'yumuşak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Doru | dağ | annesi
@tohum: doru-0077
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'salıncak', fiil 'hoplamak', sıfat 'narin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | dağ | Karatay
@tohum: doru-0078
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fıstık', fiil 'tanımak', sıfat 'düz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | annesi
@tohum: doru-0079
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kartopu', fiil 'dinmek', sıfat 'basit'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | orman | -
@tohum: doru-0080
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'basamak', fiil 'akmak', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | Kırat
@tohum: doru-0081
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kırıntı', fiil 'kırılmak', sıfat 'işaretli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | park | -
@tohum: doru-0082
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'misket', fiil 'paketlemek', sıfat 'yemyeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | Alaca
@tohum: doru-0083
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yağmur', fiil 'koşuşturmak', sıfat 'çabuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | dağ | annesi
@tohum: doru-0084
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çadır', fiil 'acıkmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Doru | park | Alaca
@tohum: doru-0085
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çilek', fiil 'seslenmek', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Doru | dağ | Karatay
@tohum: doru-0086
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'limon', fiil 'gülüşmek', sıfat 'sert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | park | Kırat
@tohum: doru-0087
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'armut', fiil 'yeşillenmek', sıfat 'çekingen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | orman | Alaca
@tohum: doru-0088
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'sis', fiil 'öğretmek', sıfat 'kaygan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Doru | dağ | Karatay
@tohum: doru-0089
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çöp', fiil 'seyretmek', sıfat 'yapraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Doru | orman | Kırat
@tohum: doru-0090
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yıldız', fiil 'sevmek', sıfat 'dalgalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Doru | orman | annesi
@tohum: doru-0091
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çiçek', fiil 'bindirmek', sıfat 'şık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Doru | dağ | Kırat
@tohum: doru-0092
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fındık', fiil 'kabarmak', sıfat 'çıtır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Doru | orman | Alaca
@tohum: doru-0093
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: bir şey yapmak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'nane', fiil 'düşürmek', sıfat 'boyalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Doru | dağ | -
@tohum: doru-0094
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'blok', fiil 'parlatmak', sıfat 'rengarenk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | Karatay
@tohum: doru-0095
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yosun', fiil 'sıkmak', sıfat 'geniş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Doru | dağ | -
@tohum: doru-0096
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'filiz', fiil 'giymek', sıfat 'kuru'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
