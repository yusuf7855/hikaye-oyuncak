# Yazar görevi: Pinokyo, parti 28

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/pinokyo_28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Pinokyo | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/pinokyo_28.txt --ad urun_v5`
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

## Kart: Pinokyo (kaynaklı, kapalı dünya)

- Ad: Pinokyo (okunuş: pinokyo; kesme eki okunuşa uyar)
- Kimlik: Pinokyo, yaşlı bir marangozun tahtadan yaptığı meraklı bir kukladır.
- Tür: kukla
- Güvenli özellik kullanımı: Burnunun uzaması yalnız komik ve küçük bir şey olarak gösterilir; ceza ya da korku değildir. Doğruyu söyleyince burnu hemen eski haline döner. Merakı tek başına uzağa gitmek olarak gösterilmez.
- Özellikler:
  - tahta: Tahtadan yapılmıştır. (örnek biçimler: tahtadan, tahta)
  - burn: Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner. (örnek biçimler: burnu, burun)
  - merak: Her şeyi merak eder ve yeni şeyler öğrenmek ister. (örnek biçimler: meraklı, merakla)
- Yerler:
  - ev: Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.
  - park: Kasabanın meydanı; çeşmesi ve ağaçları vardır.
  - orman: Kasabanın yanındaki orman.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Gepetto Usta: Pinokyo'yu tahtadan yapan yaşlı ve iyi kalpli marangoz; onun babasıdır. Tür: dede; konuşur. Yüzey biçimleri: Gepetto Usta, Gepetto, usta, babası
  - cırcır böceği: Pinokyo'ya doğruyu söyleyen ve ona yol gösteren konuşan cırcır böceği. Tür: böcek; konuşur. Yüzey biçimleri: cırcır böceği, böcek
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
  - köpek: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: köpek; konuşur. Yüzey biçimleri: köpek
- Dünya kuralları:
  - Tilki, kedi ve dev balık hikayeye girmez; kimse Pinokyo'yu kandırmaz ya da yutmaz.
  - Pinokyo eşeğe dönüşmez ve kimse onu cezalandırmaz.
  - Gepetto Usta Pinokyo'nun babasıdır; annesi hikayede yoktur.
- Yasak adlar: Mavi Peri, Jiminy, Lambalı
- Yasak: Kötü kukla tiyatrosu sahibi, hırsızlar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: kukla, tahta, marangoz, cırcır, atölye

## Tohumlar

### Pinokyo | ev | -
@tohum: pinokyo-0649
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'paspas', fiil 'ulaşmak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | -
@tohum: pinokyo-0650
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'küp', fiil 'dinlenmek', sıfat 'bilgili'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Pinokyo | ev | cırcır böceği, kuş
@tohum: pinokyo-0651
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: yeni bir şeyi denemek
- yan: cırcır böceği, kuş
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'çekirdek', fiil 'aşmak', sıfat 'kilitli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | orman | -
@tohum: pinokyo-0652
- yer: orman (Kasabanın yanındaki orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'altın', fiil 'süslemek', sıfat 'hazır'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | orman | -
@tohum: pinokyo-0653
- yer: orman (Kasabanın yanındaki orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'balon', fiil 'aydınlanmak', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | orman | Gepetto Usta
@tohum: pinokyo-0654
- yer: orman (Kasabanın yanındaki orman.)
- tema: paylaşmak
- yan: Gepetto Usta
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'sepet', fiil 'dağılmak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | cırcır böceği, köpek
@tohum: pinokyo-0655
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: paylaşmak
- yan: cırcır böceği, köpek
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'çamaşır', fiil 'indirmek', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | ev | Gepetto Usta
@tohum: pinokyo-0656
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Gepetto Usta
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'kristal', fiil 'gülümsemek', sıfat 'aceleci'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Pinokyo | orman | Gepetto Usta, kuş
@tohum: pinokyo-0657
- yer: orman (Kasabanın yanındaki orman.)
- tema: paylaşmak
- yan: Gepetto Usta, kuş
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'paket', fiil 'hazırlamak', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | cırcır böceği
@tohum: pinokyo-0658
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: cırcır böceği
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'önlük', fiil 'tamamlanmak', sıfat 'şaşkın'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | köpek
@tohum: pinokyo-0659
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: köpek
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'elbise', fiil 'dönmek', sıfat 'ucuz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | ev | -
@tohum: pinokyo-0660
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'direk', fiil 'parlamak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | ev | cırcır böceği, köpek
@tohum: pinokyo-0661
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: paylaşmak
- yan: cırcır böceği, köpek
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'şeftali', fiil 'görmek', sıfat 'incecik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | ev | kuş
@tohum: pinokyo-0662
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: kuş
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'zincir', fiil 'uyanmak', sıfat 'minicik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | Gepetto Usta, kuş
@tohum: pinokyo-0663
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Gepetto Usta, kuş
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'karabiber', fiil 'küçültmek', sıfat 'sıcak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | -
@tohum: pinokyo-0664
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'mektup', fiil 'temizlenmek', sıfat 'şanslı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | park | -
@tohum: pinokyo-0665
- yer: park (Kasabanın meydanı; çeşmesi ve ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'köfte', fiil 'şakımak', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | park | -
@tohum: pinokyo-0666
- yer: park (Kasabanın meydanı; çeşmesi ve ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: merak (Her şeyi merak eder ve yeni şeyler öğrenmek ister.)
- kelimeler: isim 'dondurma', fiil 'boyamak', sıfat 'kapalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | ev | köpek
@tohum: pinokyo-0667
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: bir şey yapmak
- yan: köpek
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'uçurtma', fiil 'keşfetmek', sıfat 'gururlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | park | köpek
@tohum: pinokyo-0668
- yer: park (Kasabanın meydanı; çeşmesi ve ağaçları vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: köpek
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'çimen', fiil 'çıkarmak', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pinokyo | orman | cırcır böceği
@tohum: pinokyo-0669
- yer: orman (Kasabanın yanındaki orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: cırcır böceği
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'yonca', fiil 'alkışlamak', sıfat 'faydalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | park | kuş
@tohum: pinokyo-0670
- yer: park (Kasabanın meydanı; çeşmesi ve ağaçları vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'kepçe', fiil 'uçuşmak', sıfat 'büyük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pinokyo | park | Gepetto Usta
@tohum: pinokyo-0671
- yer: park (Kasabanın meydanı; çeşmesi ve ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Gepetto Usta
- özellik: tahta (Tahtadan yapılmıştır.)
- kelimeler: isim 'saat', fiil 'çözülmek', sıfat 'çabuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pinokyo | ev | Gepetto Usta
@tohum: pinokyo-0672
- yer: ev (Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.)
- tema: paylaşmak
- yan: Gepetto Usta
- özellik: burn (Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.)
- kelimeler: isim 'ayna', fiil 'alışmak', sıfat 'sarı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
