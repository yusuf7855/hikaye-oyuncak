# Yazar görevi: Alaaddin, parti 11

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/alaaddin_11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Alaaddin | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/alaaddin_11.txt --ad urun_v5`
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

## Kart: Alaaddin (kaynaklı, kapalı dünya)

- Ad: Alaaddin (okunuş: alaaddin; kesme eki okunuşa uyar)
- Kimlik: Alaaddin, annesiyle küçük bir evde yaşayan cesur ve iyi kalpli bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Cin yalnız küçük, iyi ve eğlenceli şeyler yapar; kimseyi korkutmaz. Keşif tek başına uzağa gitmek ya da karanlık bir yere girmek olarak gösterilmez.
- Özellikler:
  - lamba: Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar. (örnek biçimler: lamba, lambayı)
  - yardım: Arkadaşlarına yardım etmeyi sever. (örnek biçimler: yardım, yardımcı)
  - keşf: Yeni yerler görmeyi ve keşfetmeyi sever. (örnek biçimler: keşfetti, keşif)
- Yerler:
  - ev: Alaaddin'in annesiyle yaşadığı küçük ev.
  - park: Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.
  - bahçe: Meyve ağaçları olan büyük bir bahçe.
  - şato: Kasabanın büyük ve güzel sarayı; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Alaaddin'in annesi; onunla küçük bir evde yaşar. Tür: anne; konuşur. Yüzey biçimleri: annesi, anne, anneciğim
  - lamba cini: Eski lambadan çıkan iyi kalpli ve şakacı cin; Alaaddin'in arkadaşıdır. Tür: cin; konuşur. Yüzey biçimleri: lamba cini, cin, Lamba Cini
  - kedi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kedi; konuşur. Yüzey biçimleri: kedi
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
- Dünya kuralları:
  - Kötü büyücü ve hırsızlar hikayeye girmez; kimse lambayı çalmaz.
  - Cin altın, zenginlik ya da güç vermez; küçük ve eğlenceli yardımlar yapar.
  - Mağara, yer altı ve karanlık yerler hikayeye girmez.
- Yasak adlar: Cafer, Yasemin, Abu
- Yasak: Uçan halı ve Disney'e özgü karakterler hikayeye girmez.
- İzinli dünya kelimeleri: lamba, cin, çarşı

## Tohumlar

### Alaaddin | ev | annesi
@tohum: alaaddin-0241
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'pirinç', fiil 'eşleştirmek', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | bahçe | lamba cini, kedi
@tohum: alaaddin-0242
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: lamba cini, kedi
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'tarak', fiil 'kaybetmek', sıfat 'gururlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | şato | -
@tohum: alaaddin-0243
- yer: şato (Kasabanın büyük ve güzel sarayı; bahçesi ve yüksek kapıları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'şeftali', fiil 'uyanmak', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | park | annesi, kuş
@tohum: alaaddin-0244
- yer: park (Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi, kuş
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'kabuk', fiil 'planlamak', sıfat 'renkli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | bahçe | -
@tohum: alaaddin-0245
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'mendil', fiil 'acıkmak', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | ev | annesi
@tohum: alaaddin-0246
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'köfte', fiil 'yapmak', sıfat 'koyu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | bahçe | lamba cini
@tohum: alaaddin-0247
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: lamba cini
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'fıskiye', fiil 'saklanmak', sıfat 'hevesli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | ev | annesi, kedi
@tohum: alaaddin-0248
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi, kedi
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'bilezik', fiil 'açılmak', sıfat 'çevik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | ev | kuş
@tohum: alaaddin-0249
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'bisküvi', fiil 'şakımak', sıfat 'farklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Alaaddin | ev | -
@tohum: alaaddin-0250
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: kaybolan eşya
- yan: -
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'papatya', fiil 'sormak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Alaaddin | park | lamba cini
@tohum: alaaddin-0251
- yer: park (Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.)
- tema: paylaşmak
- yan: lamba cini
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'şekerleme', fiil 'durdurmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | ev | lamba cini, kuş
@tohum: alaaddin-0252
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: lamba cini, kuş
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'beşik', fiil 'çekinmek', sıfat 'esnek'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | ev | -
@tohum: alaaddin-0253
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: bir şey yapmak
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'kese', fiil 'incelemek', sıfat 'utangaç'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | park | -
@tohum: alaaddin-0254
- yer: park (Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'balon', fiil 'taramak', sıfat 'yeterli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | ev | kedi
@tohum: alaaddin-0255
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: paylaşmak
- yan: kedi
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'mobilya', fiil 'mırıldanmak', sıfat 'çalışkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | bahçe | kedi
@tohum: alaaddin-0256
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kedi
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'fasulye', fiil 'bozulmak', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | bahçe | -
@tohum: alaaddin-0257
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: bir şey yapmak
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'simit', fiil 'şişirmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | ev | annesi, kuş
@tohum: alaaddin-0258
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi, kuş
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'kek', fiil 'saymak', sıfat 'harika'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Alaaddin | şato | -
@tohum: alaaddin-0259
- yer: şato (Kasabanın büyük ve güzel sarayı; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'zil', fiil 'düşürmek', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Alaaddin | park | kuş
@tohum: alaaddin-0260
- yer: park (Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: yardım (Arkadaşlarına yardım etmeyi sever.)
- kelimeler: isim 'leke', fiil 'kilitlemek', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | şato | -
@tohum: alaaddin-0261
- yer: şato (Kasabanın büyük ve güzel sarayı; bahçesi ve yüksek kapıları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'kıyafet', fiil 'sulamak', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | ev | annesi, kedi
@tohum: alaaddin-0262
- yer: ev (Alaaddin'in annesiyle yaşadığı küçük ev.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi, kedi
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'fındık', fiil 'içmek', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Alaaddin | bahçe | lamba cini
@tohum: alaaddin-0263
- yer: bahçe (Meyve ağaçları olan büyük bir bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: lamba cini
- özellik: keşf (Yeni yerler görmeyi ve keşfetmeyi sever.)
- kelimeler: isim 'kızartma', fiil 'koşuşturmak', sıfat 'meyveli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Alaaddin | park | -
@tohum: alaaddin-0264
- yer: park (Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: lamba (Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.)
- kelimeler: isim 'yonca', fiil 'dokunmak', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
