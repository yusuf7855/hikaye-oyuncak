# Yazar görevi: Fıstık, parti 30

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/fistik_30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Fıstık | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/fistik_30.txt --ad urun_v5`
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

## Kart: Fıstık (kaynaklı, kapalı dünya)

- Ad: Fıstık (okunuş: fıstık; kesme eki okunuşa uyar)
- Kimlik: Fıstık, hortumuyla su püskürtmeyi seven neşeli bir yavru fildir.
- Tür: fil
- Güvenli özellik kullanımı: Su püskürtmeyi yalnız oyun olarak yapar; kimseyi ıslatıp üzmez, kimse suya girmez.
- Özellikler:
  - hortum: Hortumuyla su püskürtür. (örnek biçimler: hortumu, hortumuyla)
  - kulak: Kocaman kulaklarını yelpaze gibi sallar. (örnek biçimler: kulakları, kulağını)
  - oyun: Arkadaşlarıyla oyun oynamayı çok sever. (örnek biçimler: oyun, oynadı)
- Yerler:
  - orman: Büyük ağaçları olan yeşil bir orman.
  - park: Çimenleri ve ağaçları olan bir park.
  - bahçe: Çiçekli bir bahçe; küçük bir su birikintisi vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
  - kaplumbağa: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kaplumbağa; konuşur. Yüzey biçimleri: kaplumbağa
  - maymun: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: maymun; konuşur. Yüzey biçimleri: maymun
- Dünya kuralları:
  - Avcı ve tehlikeli hayvanlar hikayeye girmez.
- Yasak adlar: -
- İzinli dünya kelimeleri: hortum, püskürt

## Tohumlar

### Fıstık | park | maymun
@tohum: fistik-0697
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: maymun
- özellik: kulak (Kocaman kulaklarını yelpaze gibi sallar.)
- kelimeler: isim 'hazine', fiil 'sıkılmak', sıfat 'bol'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | orman | kaplumbağa
@tohum: fistik-0698
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: kaplumbağa
- özellik: kulak (Kocaman kulaklarını yelpaze gibi sallar.)
- kelimeler: isim 'misket', fiil 'affetmek', sıfat 'tatlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | park | -
@tohum: fistik-0699
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'ip', fiil 'sıralamak', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | park | kuş
@tohum: fistik-0700
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'fide', fiil 'yıkamak', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Fıstık | orman | -
@tohum: fistik-0701
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'çalı', fiil 'süpürmek', sıfat 'harika'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | bahçe | kuş
@tohum: fistik-0702
- yer: bahçe (Çiçekli bir bahçe; küçük bir su birikintisi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kuş
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'paket', fiil 'kapatmak', sıfat 'lezzetli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | park | maymun
@tohum: fistik-0703
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: maymun
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'iz', fiil 'sakinleşmek', sıfat 'tüylü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Fıstık | orman | kaplumbağa
@tohum: fistik-0704
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: yeni bir şeyi denemek
- yan: kaplumbağa
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'yumurta', fiil 'tatmak', sıfat 'sert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | orman | -
@tohum: fistik-0705
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: kaybolan eşya
- yan: -
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'ceviz', fiil 'aydınlatmak', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | bahçe | kaplumbağa
@tohum: fistik-0706
- yer: bahçe (Çiçekli bir bahçe; küçük bir su birikintisi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kaplumbağa
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'erik', fiil 'öğrenmek', sıfat 'ışıltılı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | orman | maymun
@tohum: fistik-0707
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: maymun
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'kütük', fiil 'dinmek', sıfat 'neşeli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | orman | kuş
@tohum: fistik-0708
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: kulak (Kocaman kulaklarını yelpaze gibi sallar.)
- kelimeler: isim 'gül', fiil 'sevmek', sıfat 'koyu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | orman | kaplumbağa
@tohum: fistik-0709
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kaplumbağa
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'çekirdek', fiil 'oturmak', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | orman | -
@tohum: fistik-0710
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'baloncuk', fiil 'parlatmak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Fıstık | park | maymun
@tohum: fistik-0711
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: maymun
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'boncuk', fiil 'kaydetmek', sıfat 'keyifli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Fıstık | bahçe | kuş
@tohum: fistik-0712
- yer: bahçe (Çiçekli bir bahçe; küçük bir su birikintisi vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kuş
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'değnek', fiil 'boyamak', sıfat 'düz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | park | -
@tohum: fistik-0713
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'çamur', fiil 'barışmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | park | kuş
@tohum: fistik-0714
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: kuş
- özellik: oyun (Arkadaşlarıyla oyun oynamayı çok sever.)
- kelimeler: isim 'yuva', fiil 'değmek', sıfat 'kirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | orman | kaplumbağa
@tohum: fistik-0715
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: kaplumbağa
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'şeftali', fiil 'karıştırmak', sıfat 'saklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | orman | -
@tohum: fistik-0716
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'rüzgar', fiil 'sığmak', sıfat 'berrak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Fıstık | bahçe | kuş
@tohum: fistik-0717
- yer: bahçe (Çiçekli bir bahçe; küçük bir su birikintisi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kuş
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'şemsiye', fiil 'kıvrılmak', sıfat 'ahşap'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | orman | maymun
@tohum: fistik-0718
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: maymun
- özellik: kulak (Kocaman kulaklarını yelpaze gibi sallar.)
- kelimeler: isim 'dal', fiil 'ilerlemek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Fıstık | orman | kaplumbağa
@tohum: fistik-0719
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kaplumbağa
- özellik: hortum (Hortumuyla su püskürtür.)
- kelimeler: isim 'dalga', fiil 'soğumak', sıfat 'yamuk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Fıstık | park | maymun
@tohum: fistik-0720
- yer: park (Çimenleri ve ağaçları olan bir park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: maymun
- özellik: kulak (Kocaman kulaklarını yelpaze gibi sallar.)
- kelimeler: isim 'topaç', fiil 'sıçratmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
