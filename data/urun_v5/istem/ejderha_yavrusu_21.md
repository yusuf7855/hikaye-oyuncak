# Yazar görevi: Ejderha Yavrusu, parti 21

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/ejderha_yavrusu_21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Ejderha Yavrusu | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/ejderha_yavrusu_21.txt --ad urun_v5`
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

## Kart: Ejderha Yavrusu (kaynaklı, kapalı dünya)

- Ad: Ejderha Yavrusu (okunuş: ejderha yavrusu; kesme eki okunuşa uyar)
- Kimlik: Ejderha Yavrusu, ağzından baloncuk üfleyen küçük ve şirin bir ejderhadır.
- Tür: ejderha
- Güvenli özellik kullanımı: Uçarken alçakta kalır ve hep dikkatlidir; baloncukları kimseye zarar vermez.
- Özellikler:
  - baloncuk: Ağzından renkli baloncuklar üfler. (örnek biçimler: baloncuk, baloncukları)
  - kanat: Küçük kanatlarıyla uçmayı öğreniyor. (örnek biçimler: kanatları, kanatlarını)
  - neşe: Çok meraklı ve neşelidir. (örnek biçimler: neşeli, neşeyle)
- Yerler:
  - dağ: Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.
  - gökyüzü: Bulutlu ve güneşli gökyüzü.
  - orman: Yeşil bir orman.
  - şato: Tepedeki eski ve boş taş saray; bahçesinde çiçekler vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
  - kelebek: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kelebek; konuşur. Yüzey biçimleri: kelebek
  - sincap: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: sincap; konuşur. Yüzey biçimleri: sincap
- Dünya kuralları:
  - Ejderha Yavrusu ateş üflemez, hiçbir şeyi yakmaz.
  - Şövalye, savaş ve canavar hikayeye girmez.
- Yasak adlar: -
- İzinli dünya kelimeleri: ejderha, baloncuk

## Tohumlar

### Ejderha Yavrusu | orman | -
@tohum: ejderha_yavrusu-0481
- yer: orman (Yeşil bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'fidan', fiil 'döndürmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | orman | kelebek
@tohum: ejderha_yavrusu-0482
- yer: orman (Yeşil bir orman.)
- tema: paylaşmak
- yan: kelebek
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'tüy', fiil 'yoğurmak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0483
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'yelpaze', fiil 'kaçmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0484
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: sırayla oynamak
- yan: kuş
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'salıncak', fiil 'götürmek', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0485
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: yeni bir şeyi denemek
- yan: kuş
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'mercan', fiil 'basmak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | orman | sincap
@tohum: ejderha_yavrusu-0486
- yer: orman (Yeşil bir orman.)
- tema: paylaşmak
- yan: sincap
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'köpük', fiil 'katlamak', sıfat 'faydalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | şato | kuş
@tohum: ejderha_yavrusu-0487
- yer: şato (Tepedeki eski ve boş taş saray; bahçesinde çiçekler vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'leke', fiil 'göndermek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | dağ | kelebek
@tohum: ejderha_yavrusu-0488
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kelebek
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'lokma', fiil 'sallanmak', sıfat 'yumuşak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0489
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'ay', fiil 'çizmek', sıfat 'paslı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0490
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: kaybolan eşya
- yan: kuş
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'yosun', fiil 'yatmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | dağ | sincap
@tohum: ejderha_yavrusu-0491
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'buket', fiil 'kemirmek', sıfat 'utangaç'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0492
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kuş
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'dilim', fiil 'almak', sıfat 'kirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | -
@tohum: ejderha_yavrusu-0493
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'çuval', fiil 'denemek', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | dağ | -
@tohum: ejderha_yavrusu-0494
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'ip', fiil 'tatmak', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | dağ | -
@tohum: ejderha_yavrusu-0495
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'odun', fiil 'ıslatmak', sıfat 'zeki'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0496
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: neşe (Çok meraklı ve neşelidir.)
- kelimeler: isim 'meyve', fiil 'kapatmak', sıfat 'elmalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | şato | kuş
@tohum: ejderha_yavrusu-0497
- yer: şato (Tepedeki eski ve boş taş saray; bahçesinde çiçekler vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'çubuk', fiil 'yakalamak', sıfat 'koyu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | dağ | kelebek
@tohum: ejderha_yavrusu-0498
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kelebek
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'yıldız', fiil 'taşınmak', sıfat 'bozuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0499
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'güneş', fiil 'cıvıldamak', sıfat 'üzgün'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | dağ | sincap
@tohum: ejderha_yavrusu-0500
- yer: dağ (Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'çalı', fiil 'düşürmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | -
@tohum: ejderha_yavrusu-0501
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'çan', fiil 'hazırlanmak', sıfat 'düzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | -
@tohum: ejderha_yavrusu-0502
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baloncuk (Ağzından renkli baloncuklar üfler.)
- kelimeler: isim 'yağmur', fiil 'havalanmak', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0503
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: paylaşmak
- yan: kuş
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'kartopu', fiil 'uzanmak', sıfat 'tertemiz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Ejderha Yavrusu | gökyüzü | kuş
@tohum: ejderha_yavrusu-0504
- yer: gökyüzü (Bulutlu ve güneşli gökyüzü.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: kanat (Küçük kanatlarıyla uçmayı öğreniyor.)
- kelimeler: isim 'yem', fiil 'kutlamak', sıfat 'benekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
