# Yazar görevi: Nasreddin Hoca, parti 29

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/nasreddin_hoca_29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/nasreddin_hoca_29.txt --ad urun_v5`
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

### Nasreddin Hoca | dağ | -
@tohum: nasreddin_hoca-0673
- yer: dağ (Akşehir'in yakınındaki tepe.)
- tema: bir şey yapmak
- yan: -
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'masa', fiil 'yağmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0674
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'mermer', fiil 'düzeltmek', sıfat 'değerli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0675
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: bir şey yapmak
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'harita', fiil 'dinmek', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | bahçe | eşeği, kedi
@tohum: nasreddin_hoca-0676
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği, kedi
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'güneş', fiil 'değişmek', sıfat 'yapraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | kuş
@tohum: nasreddin_hoca-0677
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: kuş
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'halı', fiil 'tanıştırmak', sıfat 'tatlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | bahçe | komşusu, kedi
@tohum: nasreddin_hoca-0678
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: paylaşmak
- yan: komşusu, kedi
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'yün', fiil 'buruşturmak', sıfat 'yemyeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | komşusu
@tohum: nasreddin_hoca-0679
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: komşusu
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'kereviz', fiil 'giydirmek', sıfat 'ılık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | bahçe | kuş
@tohum: nasreddin_hoca-0680
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: kuş
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'lokma', fiil 'birleşmek', sıfat 'kolay'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | kedi
@tohum: nasreddin_hoca-0681
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kedi
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'çorap', fiil 'koşturmak', sıfat 'mükemmel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0682
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'raf', fiil 'yayılmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | eşeği
@tohum: nasreddin_hoca-0683
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'bluz', fiil 'uçurmak', sıfat 'umutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | bahçe | kuş
@tohum: nasreddin_hoca-0684
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: kuş
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'mobilya', fiil 'gelmek', sıfat 'tekerlekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | ev | eşeği
@tohum: nasreddin_hoca-0685
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'kabak', fiil 'çekinmek', sıfat 'beyaz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | bahçe | komşusu, kedi
@tohum: nasreddin_hoca-0686
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: paylaşmak
- yan: komşusu, kedi
- özellik: ters (Eşeğine bazen ters biner.)
- kelimeler: isim 'bağcık', fiil 'yaratmak', sıfat 'büyük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | komşusu, kuş
@tohum: nasreddin_hoca-0687
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: komşusu, kuş
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'nota', fiil 'eğilmek', sıfat 'yardımsever'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | ev | eşeği
@tohum: nasreddin_hoca-0688
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: paylaşmak
- yan: eşeği
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'direk', fiil 'asılmak', sıfat 'sakin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | ev | komşusu, kuş
@tohum: nasreddin_hoca-0689
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: paylaşmak
- yan: komşusu, kuş
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'pantolon', fiil 'uyumak', sıfat 'bulutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | dağ | kuş
@tohum: nasreddin_hoca-0690
- yer: dağ (Akşehir'in yakınındaki tepe.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kuş
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'buket', fiil 'yoğurmak', sıfat 'geniş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | park | eşeği
@tohum: nasreddin_hoca-0691
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: eşeği
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'atkı', fiil 'yumuşamak', sıfat 'reçelli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | bahçe | kedi
@tohum: nasreddin_hoca-0692
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kedi
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'pelerin', fiil 'paketlemek', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Nasreddin Hoca | bahçe | komşusu
@tohum: nasreddin_hoca-0693
- yer: bahçe (Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: komşusu
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'basamak', fiil 'gezinmek', sıfat 'sabırsız'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Nasreddin Hoca | park | -
@tohum: nasreddin_hoca-0694
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'fener', fiil 'akmak', sıfat 'keyifli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Nasreddin Hoca | ev | -
@tohum: nasreddin_hoca-0695
- yer: ev (Hoca'nın Akşehir'deki küçük evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: fikir (Akıllı fikirleriyle sorunları çözer.)
- kelimeler: isim 'çimen', fiil 'sabırsızlanmak', sıfat 'serin'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Nasreddin Hoca | park | eşeği, kedi
@tohum: nasreddin_hoca-0696
- yer: park (Akşehir'in meydanı ve pazarı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği, kedi
- özellik: komik (Herkesi güldüren komik cevaplar verir.)
- kelimeler: isim 'marul', fiil 'soğumak', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
