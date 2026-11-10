# Yazar görevi: Bilge Baykuş, parti 24

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/bilge_baykus_24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Bilge Baykuş | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/bilge_baykus_24.txt --ad urun_v5`
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

## Kart: Bilge Baykuş (kaynaklı, kapalı dünya)

- Ad: Bilge Baykuş (okunuş: bilge baykuş; kesme eki okunuşa uyar)
- Kimlik: Bilge Baykuş, çok şey bilen ve soru sormayı seven yaşlı bir baykuştur.
- Tür: baykuş
- Güvenli özellik kullanımı: Bilgisini yardım etmek için kullanır; kimseyi küçümsemez. Geceleri yalnız yıldızlara bakar, karanlıkta kimse yolunu kaybetmez.
- Özellikler:
  - bil: Çok şey bilir ve bildiklerini anlatmayı sever. (örnek biçimler: bilir, bilgi)
  - göz: Kocaman, yuvarlak gözleri vardır. (örnek biçimler: gözleri, gözlerini)
  - uyku: Geceleri uyanıktır, gündüz biraz uykuludur. (örnek biçimler: uykulu, uykusu)
- Yerler:
  - orman: Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.
  - dağ: Ağaçları olan bir tepe.
  - gökyüzü: Yıldızlı ve sakin gece göğü.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - sincap: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: sincap; konuşur. Yüzey biçimleri: sincap
  - tavşan: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: tavşan; konuşur. Yüzey biçimleri: tavşan
  - kirpi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kirpi; konuşur. Yüzey biçimleri: kirpi
- Dünya kuralları:
  - Bilge Baykuş hiçbir hayvanı avlamaz, yakalamaz ya da yemez.
- Yasak adlar: -
- İzinli dünya kelimeleri: baykuş, yuva

## Tohumlar

### Bilge Baykuş | orman | tavşan
@tohum: bilge_baykus-0553
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: tavşan
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'iplik', fiil 'çalıştırmak', sıfat 'uzak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | dağ | sincap
@tohum: bilge_baykus-0554
- yer: dağ (Ağaçları olan bir tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: sincap
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'elma', fiil 'okumak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Bilge Baykuş | dağ | kirpi
@tohum: bilge_baykus-0555
- yer: dağ (Ağaçları olan bir tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kirpi
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'balkabağı', fiil 'durdurmak', sıfat 'rahat'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Bilge Baykuş | dağ | sincap
@tohum: bilge_baykus-0556
- yer: dağ (Ağaçları olan bir tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: sincap
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'kalıp', fiil 'süpürmek', sıfat 'yapışkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | orman | tavşan
@tohum: bilge_baykus-0557
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: kaybolan eşya
- yan: tavşan
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'papatya', fiil 'selamlamak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | orman | kirpi
@tohum: bilge_baykus-0558
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: sırayla oynamak
- yan: kirpi
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'bitki', fiil 'kurtulmak', sıfat 'uzun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0559
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'kapak', fiil 'serinlemek', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0560
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: bir şey yapmak
- yan: -
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'güneş', fiil 'korunmak', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | orman | tavşan
@tohum: bilge_baykus-0561
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: sırayla oynamak
- yan: tavşan
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'yaprak', fiil 'dinmek', sıfat 'gururlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Bilge Baykuş | orman | sincap
@tohum: bilge_baykus-0562
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: kaybolan eşya
- yan: sincap
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'torba', fiil 'birikmek', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Bilge Baykuş | dağ | tavşan
@tohum: bilge_baykus-0563
- yer: dağ (Ağaçları olan bir tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: tavşan
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'sis', fiil 'yeşermek', sıfat 'gürültülü'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Bilge Baykuş | orman | sincap
@tohum: bilge_baykus-0564
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: paylaşmak
- yan: sincap
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'mercan', fiil 'susmak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0565
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'gökkuşağı', fiil 'durmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | dağ | kirpi
@tohum: bilge_baykus-0566
- yer: dağ (Ağaçları olan bir tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: kirpi
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'gölge', fiil 'saçmak', sıfat 'mutsuz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | dağ | kirpi
@tohum: bilge_baykus-0567
- yer: dağ (Ağaçları olan bir tepe.)
- tema: kaybolan eşya
- yan: kirpi
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'nane', fiil 'uçurmak', sıfat 'kaygan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0568
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'damla', fiil 'okşamak', sıfat 'pahalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0569
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: bir şey yapmak
- yan: -
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'baston', fiil 'örtmek', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0570
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'fide', fiil 'şişirmek', sıfat 'meraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | orman | tavşan
@tohum: bilge_baykus-0571
- yer: orman (Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: tavşan
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'oyuncak', fiil 'üflemek', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Bilge Baykuş | dağ | -
@tohum: bilge_baykus-0572
- yer: dağ (Ağaçları olan bir tepe.)
- tema: bir şey yapmak
- yan: -
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'kabuk', fiil 'kırpmak', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | dağ | sincap
@tohum: bilge_baykus-0573
- yer: dağ (Ağaçları olan bir tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: sincap
- özellik: uyku (Geceleri uyanıktır, gündüz biraz uykuludur.)
- kelimeler: isim 'taş', fiil 'aşmak', sıfat 'süslü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0574
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'koni', fiil 'eklemek', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Bilge Baykuş | gökyüzü | -
@tohum: bilge_baykus-0575
- yer: gökyüzü (Yıldızlı ve sakin gece göğü.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: bil (Çok şey bilir ve bildiklerini anlatmayı sever.)
- kelimeler: isim 'paket', fiil 'yetiştirmek', sıfat 'tedbirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Bilge Baykuş | dağ | sincap
@tohum: bilge_baykus-0576
- yer: dağ (Ağaçları olan bir tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: sincap
- özellik: göz (Kocaman, yuvarlak gözleri vardır.)
- kelimeler: isim 'çim', fiil 'yatmak', sıfat 'mükemmel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
