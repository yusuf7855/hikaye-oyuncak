# Yazar görevi: Zıpzıp, parti 39

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/zipzip_39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/zipzip_39.txt --ad urun_v5`
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
@tohum: zipzip-0913
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'kırıntı', fiil 'çoğalmak', sıfat 'kırık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | orman | kuş
@tohum: zipzip-0914
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'bayrak', fiil 'kokmak', sıfat 'yüksek'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0915
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'çam', fiil 'dökmek', sıfat 'bembeyaz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | sincap
@tohum: zipzip-0916
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'top', fiil 'almak', sıfat 'paslı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0917
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'halat', fiil 'somurtmak', sıfat 'değerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0918
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'ağaç', fiil 'kurtarmak', sıfat 'yapraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | orman | -
@tohum: zipzip-0919
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: bir şey yapmak
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'yuva', fiil 'toplamak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0920
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: sırayla oynamak
- yan: kirpi
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'yıldız', fiil 'inmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0921
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: paylaşmak
- yan: kuş
- özellik: kulak (Uzun kulakları vardır.)
- kelimeler: isim 'çilek', fiil 'güneşlenmek', sıfat 'uzun'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | park | sincap
@tohum: zipzip-0922
- yer: park (Çimenleri olan bir park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: sincap
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'elma', fiil 'oynamak', sıfat 'sağlam'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | orman | -
@tohum: zipzip-0923
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'menekşe', fiil 'doğmak', sıfat 'sadık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | -
@tohum: zipzip-0924
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'balon', fiil 'uzamak', sıfat 'uzak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0925
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: kuş
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'ceviz', fiil 'cıvıldamak', sıfat 'ekşi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | -
@tohum: zipzip-0926
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: kaybolan eşya
- yan: -
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'gölge', fiil 'koparmak', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | park | -
@tohum: zipzip-0927
- yer: park (Çimenleri olan bir park.)
- tema: kaybolan eşya
- yan: -
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'üzüm', fiil 'yayılmak', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | orman | sincap
@tohum: zipzip-0928
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'halka', fiil 'yapmak', sıfat 'zarif'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | park | -
@tohum: zipzip-0929
- yer: park (Çimenleri olan bir park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'leke', fiil 'dinmek', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0930
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'bağcık', fiil 'indirmek', sıfat 'kokulu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | orman | sincap
@tohum: zipzip-0931
- yer: orman (Büyük ağaçları olan yeşil bir orman.)
- tema: sırayla oynamak
- yan: sincap
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'su', fiil 'şakımak', sıfat 'çıtır'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0932
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'çubuk', fiil 'boyamak', sıfat 'yardımsever'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Zıpzıp | bahçe | kirpi
@tohum: zipzip-0933
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: kaybolan eşya
- yan: kirpi
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'külah', fiil 'beklemek', sıfat 'sıkı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | park | sincap
@tohum: zipzip-0934
- yer: park (Çimenleri olan bir park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: sincap
- özellik: zıpla (Her yere zıplayarak gider.)
- kelimeler: isim 'yün', fiil 'yıkamak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | kuş
@tohum: zipzip-0935
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: kaybolan eşya
- yan: kuş
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'dalga', fiil 'yeşermek', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Zıpzıp | bahçe | -
@tohum: zipzip-0936
- yer: bahçe (Sebzeli ve çiçekli bir bahçe.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: havuç (Havucu çok sever.)
- kelimeler: isim 'odun', fiil 'örmek', sıfat 'yeterli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
