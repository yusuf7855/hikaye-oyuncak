# Yazar görevi: Pamuk Prenses, parti 4

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v5/aday/pamuk_prenses_4.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Pamuk Prenses | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v5/aday/pamuk_prenses_4.txt --ad urun_v5`
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

## Kart: Pamuk Prenses (kaynaklı, kapalı dünya)

- Ad: Pamuk Prenses (okunuş: pamuk prenses; kesme eki okunuşa uyar)
- Kimlik: Pamuk Prenses, ormandaki küçük bir evde cücelerle yaşayan nazik bir prensestir.
- Tür: prenses
- Güvenli özellik kullanımı: Yardımseverliği tek başına uzak yerlere gitmek olarak gösterilmez; yardım ederken hep evin ve bahçenin yakınında kalır.
- Özellikler:
  - nazik: Herkese karşı nazik ve yardımseverdir. (örnek biçimler: nazik, nazikçe)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
  - düzen: Evi temiz ve düzenli tutmayı sever. (örnek biçimler: düzenli, düzenledi)
- Yerler:
  - orman: Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.
  - ev: Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.
  - bahçe: Küçük evin önündeki çiçekli bahçe.
  - şato: Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - en küçük cüce: Pamuk Prenses'le aynı evde yaşayan yedi cüceden en küçüğü; onun en yakın arkadaşı. Tür: cüce; konuşur. Yüzey biçimleri: en küçük cüce, küçük cüce, cüce
  - cüceler: Ormandaki küçük evde yaşayan yedi cüce; gündüz çalışır, akşam eve döner. Tür: cüce; KONUŞMAZ. Yüzey biçimleri: cüceler, yedi cüce
  - tavşan: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: tavşan; konuşur. Yüzey biçimleri: tavşan
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
- Dünya kuralları:
  - Kötü kraliçe, sihirli ayna, avcı ve zehirli elma hikayeye girmez.
  - Cüceler topluca konuşmaz; konuşan yalnız en küçük cücedir.
  - Prens, düğün, evlilik ve uzun uyku hikayeye girmez.
- Yasak adlar: Kraliçe, Prens
- Yasak: Büyü, cadı, zehir ve korkutucu kılık değiştirme hikayeye girmez.
- İzinli dünya kelimeleri: cüce, şarkı

## Tohumlar

### Pamuk Prenses | şato | -
@tohum: pamuk_prenses-0073
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'çarşaf', fiil 'sıçratmak', sıfat 'sıcak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | ev | -
@tohum: pamuk_prenses-0074
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kök', fiil 'çiğnemek', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | bahçe | -
@tohum: pamuk_prenses-0075
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'fincan', fiil 'gezmek', sıfat 'biberli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | orman | -
@tohum: pamuk_prenses-0076
- yer: orman (Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'küpe', fiil 'bitirmek', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Pamuk Prenses | şato | kuş
@tohum: pamuk_prenses-0077
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: kuş
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yem', fiil 'almak', sıfat 'uykulu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | orman | tavşan
@tohum: pamuk_prenses-0078
- yer: orman (Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: tavşan
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'yama', fiil 'dolaşmak', sıfat 'somurtkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pamuk Prenses | şato | en küçük cüce, kuş
@tohum: pamuk_prenses-0079
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: en küçük cüce, kuş
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'dalga', fiil 'taşmak', sıfat 'basit'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pamuk Prenses | orman | -
@tohum: pamuk_prenses-0080
- yer: orman (Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şişe', fiil 'değişmek', sıfat 'ılık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | bahçe | -
@tohum: pamuk_prenses-0081
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'boru', fiil 'yeşillenmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | ev | cüceler, kuş
@tohum: pamuk_prenses-0082
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: paylaşmak
- yan: cüceler, kuş
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'boya', fiil 'ilerlemek', sıfat 'sevinçli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pamuk Prenses | orman | cüceler
@tohum: pamuk_prenses-0083
- yer: orman (Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.)
- tema: sırayla oynamak
- yan: cüceler
- özellik: düzen (Evi temiz ve düzenli tutmayı sever.)
- kelimeler: isim 'blok', fiil 'aydınlanmak', sıfat 'üzgün'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | bahçe | en küçük cüce
@tohum: pamuk_prenses-0084
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: en küçük cüce
- özellik: düzen (Evi temiz ve düzenli tutmayı sever.)
- kelimeler: isim 'yiyecek', fiil 'üflemek', sıfat 'yemyeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | bahçe | tavşan
@tohum: pamuk_prenses-0085
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: tavşan
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'ayçiçeği', fiil 'kemirmek', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pamuk Prenses | bahçe | -
@tohum: pamuk_prenses-0086
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'kavun', fiil 'küçülmek', sıfat 'bembeyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | ev | -
@tohum: pamuk_prenses-0087
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'halat', fiil 'saymak', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | şato | -
@tohum: pamuk_prenses-0088
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: düzen (Evi temiz ve düzenli tutmayı sever.)
- kelimeler: isim 'yosun', fiil 'oturtmak', sıfat 'çekingen'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Pamuk Prenses | ev | cüceler, kuş
@tohum: pamuk_prenses-0089
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: sırayla oynamak
- yan: cüceler, kuş
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'çorap', fiil 'hatırlamak', sıfat 'pembe'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | ev | en küçük cüce, kuş
@tohum: pamuk_prenses-0090
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: en küçük cüce, kuş
- özellik: düzen (Evi temiz ve düzenli tutmayı sever.)
- kelimeler: isim 'pantolon', fiil 'beslemek', sıfat 'ekşi'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | ev | en küçük cüce
@tohum: pamuk_prenses-0091
- yer: ev (Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.)
- tema: paylaşmak
- yan: en küçük cüce
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'boncuk', fiil 'yardımlaşmak', sıfat 'kalın'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | şato | kuş
@tohum: pamuk_prenses-0092
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kuş
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'börek', fiil 'esnemek', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Pamuk Prenses | orman | tavşan
@tohum: pamuk_prenses-0093
- yer: orman (Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.)
- tema: sırayla oynamak
- yan: tavşan
- özellik: düzen (Evi temiz ve düzenli tutmayı sever.)
- kelimeler: isim 'ay', fiil 'okşamak', sıfat 'benekli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Pamuk Prenses | şato | -
@tohum: pamuk_prenses-0094
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'hamur', fiil 'uyanmak', sıfat 'hazırlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | bahçe | cüceler, tavşan
@tohum: pamuk_prenses-0095
- yer: bahçe (Küçük evin önündeki çiçekli bahçe.)
- tema: paylaşmak
- yan: cüceler, tavşan
- özellik: nazik (Herkese karşı nazik ve yardımseverdir.)
- kelimeler: isim 'çimen', fiil 'ışıldamak', sıfat 'işaretli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Pamuk Prenses | şato | -
@tohum: pamuk_prenses-0096
- yer: şato (Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'limonata', fiil 'uzaklaştırmak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
