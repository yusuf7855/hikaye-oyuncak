# Yazar görevi: Zıpzıp, parti 16

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/zipzip_16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Zıpzıp | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/zipzip_16.txt --ad urun_v5`
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

## Kart: Zıpzıp (kaynaklı, kapalı dünya)

- Ad: Zıpzıp (okunuş: zıpzıp; kesme eki okunuşa uyar)
- Kimlik: Zıpzıp, zıplamayı çok seven neşeli bir tavşandır.
- Tür: tavşan
- Güvenli özellik kullanımı: Zıplarken yükseğe çıkmaz, kimseye çarpmaz; zıplaması hep yumuşak ve kısadır.
- Özellikler:
  - zıpla: Her yere zıplayarak gider. (örnek biçimler: zıpladı, zıplayarak)
  - kulak: Uzun kulakları vardır. (örnek biçimler: kulakları, kulağı)
  - havuç: Havucu çok sever. (örnek biçimler: havuç, havucu)
- Yerler:
  - bahçe: Sebzeli ve çiçekli bir bahçe.
  - orman: Büyük ağaçları olan yeşil bir orman.
  - park: Çimenleri olan bir park.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - kirpi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kirpi; konuşur. Yüzey biçimleri: kirpi
  - sincap: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: sincap; konuşur. Yüzey biçimleri: sincap
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
- Dünya kuralları:
  - Hayvanlar tek tek konuşabilir; arka plandaki hayvan toplulukları konuşmaz.
- Yasak adlar: -
- İzinli dünya kelimeleri: zıpla, havuç

## Tohumlar

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0361
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'yaprak', fiil 'zıplamak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | park | sincap
@tohum: zipzip-0362
- yer: park (Çimenleri olan bir park.)
- tema: paylaşmak
- yan: sincap
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'boncuk', fiil 'koşmak', sıfat 'mutsuz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | orman | -
@tohum: zipzip-0363
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'paket', fiil 'hazırlamak', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0364
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kuş
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'nilüfer', fiil 'söylemek', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | -
@tohum: zipzip-0365
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'misket', fiil 'kucaklamak', sıfat 'keyifli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | kirpi
@tohum: zipzip-0366
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: paylaşmak
- yan: kirpi
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'kaya', fiil 'incelemek', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | bahçe | -
@tohum: zipzip-0367
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'kürek', fiil 'kırpmak', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0368
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'bez', fiil 'cıvıldamak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | park | -
@tohum: zipzip-0369
- yer: park (Çimenleri olan bir park.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'köpük', fiil 'değişmek', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0370
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'çuval', fiil 'çevirmek', sıfat 'parlak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0371
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'su', fiil 'sevmek', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0372
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'iplik', fiil 'açılmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | orman | -
@tohum: zipzip-0373
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'buğday', fiil 'tekrarlamak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0374
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kirpi
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'ot', fiil 'sıçramak', sıfat 'mavi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | sincap
@tohum: zipzip-0375
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: sırayla oynamak
- yan: sincap
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'çimen', fiil 'bozulmak', sıfat 'çiçekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | orman | sincap
@tohum: zipzip-0376
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: sincap
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'oyuncak', fiil 'temizlenmek', sıfat 'nazik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | orman | sincap
@tohum: zipzip-0377
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: paylaşmak
- yan: sincap
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'kozalak', fiil 'anlaşmak', sıfat 'kibar'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | orman | -
@tohum: zipzip-0378
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'yelpaze', fiil 'çıkarmak', sıfat 'dağınık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0379
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'koni', fiil 'şekillendirmek', sıfat 'sert'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0380
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kuş
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'filiz', fiil 'götürmek', sıfat 'meşgul'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0381
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kirpi
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'saman', fiil 'anlamak', sıfat 'karışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0382
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'nane', fiil 'somurtmak', sıfat 'bol'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | park | sincap
@tohum: zipzip-0383
- yer: park (Çimenleri olan bir park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'ay', fiil 'çıkmak', sıfat 'sabırlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0384
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: kaybolan eşya
- yan: kirpi
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'gökkuşağı', fiil 'yeşillenmek', sıfat 'kararlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
