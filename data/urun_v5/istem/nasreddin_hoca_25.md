# Yazar görevi: Nasreddin Hoca, parti 25

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/nasreddin_hoca_25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Nasreddin Hoca | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/nasreddin_hoca_25.txt --ad urun_v5`
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

## Kart: Nasreddin Hoca (kaynaklı, kapalı dünya)

- Ad: Nasreddin Hoca (okunuş: nasreddin hoca; kesme eki okunuşa uyar)
- Kimlik: Nasreddin Hoca, Akşehir'de yaşayan akıllı ve güler yüzlü bir dededir.
- Tür: dede
- Güvenli özellik kullanımı: Ters binmek yalnız yavaş yürüyen eşekte komik bir şey olarak gösterilir; kimse düşmez. Kimseyle alay etmez.
- Özellikler:
  - komik: Herkesi güldüren komik cevaplar verir. (örnek biçimler: komik, komikti)
  - ters: Eşeğine bazen ters biner. (örnek biçimler: ters, tersine)
  - fikir: Akıllı fikirleriyle sorunları çözer. (örnek biçimler: fikir, fikri)
- Yerler:
  - ev: Hoca'nın Akşehir'deki küçük evi.
  - park: Akşehir'in meydanı ve pazarı.
  - bahçe: Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.
  - dağ: Akşehir'in yakınındaki tepe.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - eşeği: Nasreddin Hoca'nın eşeği; Hoca bazen ona ters biner. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: eşek, eşeği, eşeğine
  - komşusu: Hoca'nın iyi kalpli komşusu; birlikte gülerler. Tür: komşu; konuşur. Yüzey biçimleri: komşu, komşusu, komşular
  - kedi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kedi; konuşur. Yüzey biçimleri: kedi
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
- Dünya kuralları:
  - Hoca'nın eşeği konuşmaz; yük taşır, başını sallar, anırır.
  - Kimse kızmaz, kavga etmez; şakalar herkesi güldürür.
- Yasak adlar: Timur, Kadı
- Yasak: Kadı, hükümdar, savaş ve borç fıkraları hikayeye girmez.
- İzinli dünya kelimeleri: hoca, ters, Akşehir

## Tohumlar

### Nasreddin Hoca | ev | kuş
@tohum: nasreddin_hoca-0577
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kuş
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'pencere', fiil 'dokunmak', sıfat 'yorgun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | park | komşusu, kedi
@tohum: nasreddin_hoca-0578
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: kaybolan eşya
- yan: komşusu, kedi
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'baloncuk', fiil 'kurtarmak', sıfat 'lezzetli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | kuş
@tohum: nasreddin_hoca-0579
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kuş
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'kebap', fiil 'parlamak', sıfat 'yakın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | kedi
@tohum: nasreddin_hoca-0580
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: sırayla oynamak
- yan: kedi
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'çamaşır', fiil 'çözülmek', sıfat 'şeffaf'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0581
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: bir şey yapmak
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'toka', fiil 'taşınmak', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | bahçe | eşeği
@tohum: nasreddin_hoca-0582
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: bir şey yapmak
- yan: eşeği
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'kozalak', fiil 'kazanmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | dağ | eşeği
@tohum: nasreddin_hoca-0583
- yer: dağ (Akşehir'in yakınındaki tepe.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'balon', fiil 'kıvırmak', sıfat 'kibar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | kedi
@tohum: nasreddin_hoca-0584
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kedi
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'perde', fiil 'utanmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0585
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'yama', fiil 'göndermek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | dağ | -
@tohum: nasreddin_hoca-0586
- yer: dağ (Akşehir'in yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'flüt', fiil 'şakalaşmak', sıfat 'resimli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0587
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: bir şey yapmak
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'karabiber', fiil 'uyandırmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | ev | komşusu, kuş
@tohum: nasreddin_hoca-0588
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: komşusu, kuş
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'bileklik', fiil 'ıslatmak', sıfat 'sevimli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | kuş
@tohum: nasreddin_hoca-0589
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'salata', fiil 'söylemek', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0590
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'avokado', fiil 'tanışmak', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | kedi
@tohum: nasreddin_hoca-0591
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kedi
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'çim', fiil 'gülümsemek', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0592
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'tomurcuk', fiil 'barışmak', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | park | komşusu
@tohum: nasreddin_hoca-0593
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: komşusu
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'sepet', fiil 'çırpmak', sıfat 'sisli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0594
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: kaybolan eşya
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'sos', fiil 'sürtmek', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | eşeği, kedi
@tohum: nasreddin_hoca-0595
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: paylaşmak
- yan: eşeği, kedi
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'damga', fiil 'erimek', sıfat 'kremalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | bahçe | kuş
@tohum: nasreddin_hoca-0596
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: paylaşmak
- yan: kuş
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'önlük', fiil 'fırçalamak', sıfat 'çamurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0597
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'zil', fiil 'görünmek', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0598
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'sis', fiil 'takılmak', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0599
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'mektup', fiil 'parıldamak', sıfat 'aydınlık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | dağ | eşeği, kuş
@tohum: nasreddin_hoca-0600
- yer: dağ (Akşehir'in yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği, kuş
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'yulaf', fiil 'yuvarlanmak', sıfat 'yapışkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
