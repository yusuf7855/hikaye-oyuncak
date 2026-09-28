# Yazar görevi: Karabaş, parti 1

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 9 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v1/aday/karabas_1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Karabaş | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v1/aday/karabas_1.txt`
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
3. **Tek sorun.** Sorun ilk 3 cümlede sebebiyle birlikte söylenir ('Top çalıya takıldı.'). Sorunu figür kendisi
   1-2 adımda çözer; yardım istemek de figürün çözümüdür. Yan karakter en fazla yardım eder.
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
   kavram ve şapkalı harf yok; 'hâlâ' yerine 'yine' ya da 'daha' yazılır. Tohumdaki isim, fiil ve sıfat geçer;
   biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik kayda yazılır.
8. **Dil.** Anlatım -dı'lı geçmiş zamanda ('yürüdü', 'bakıyordu', 'takılmıştı'). Her replikte konuşan bellidir
   ('dedi Niloya'); hitaptan önce virgül konur ('Sıra sende, Niloya'). Kimse kendi kendine konuşmaz ya da kendine adıyla seslenmez. Plan satırları da aynı dil ve
   yazım kurallarına uyar; cihazda model planı kendisi yazıyor.
9. **Son.** Hikaye tohumdaki kapanış türüyle biter: eylem, replik, görüntü, ders ya da duygu. Son güvenlidir ve
   sorun çözülmüştür. Son cümlede 'çünkü' ile açıklama ve 'gülümsedi/sevindi' kalıbı yalnız kapanış türü 'duygu'
   ise kullanılır. Ders, olaydan çıkan tek ve somut bir cümledir. Korku, yaralanma, hastalık ve taklit edilince
   tehlikeli davranış (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç) yok.
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
'<Ad> adında ... yaşardı' bir açılış türü değildir. Kapanış türü: *eylem* (figür son bir şey yapar),
*replik* (son cümle bir konuşmadır), *görüntü* (sahneden son bir resim), *ders* (olaydan çıkan tek somut cümle),
*duygu* (figürün hissi). Diyalog 'yok' ise hikayede replik yoktur. Temalar tek sahneye uyarlanmıştır:
kaybolan eşya; yeni arkadaş (ilk adımı figür atar); paylaşmak; yardım istemek (çözüm figürün yardım
istemesidir); yeni bir şeyi denemek; sahne içinde beklemek (sıra, fırındaki kek, yağmurun dinmesi); özür
dilemek; sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil); bir şey yapmak;
yağmur ya da kar günü; aynı sahnede hazırlanıp verilen sürpriz; sırayla oynamak.

**İyi örnekler** (kullanıcı yetkisiyle seçildi; farklı figür ve farklı kapanış türü; ikisi de `veri_hakem.py kontrol`dan
geçer):

Tohum: deniz, yan balık, özellik kabuk, kelimeler taş/toplamak/renkli, tema yağmur, açılış yer, kapanış görüntü.

```
### Tosbi | deniz | balık
@plan: yağmur başladı ve başı ıslandı | başını kabuğuna çekip yağmurun dinmesini bekledi
@tohum: tosbi-9001
Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden yağmur başladı ve Tosbi'nin başı ıslandı. Tosbi başını ve ayaklarını kabuğuna çekti. Sudan küçük bir balık başını çıkardı. "Tosbi, neredesin?" diye sordu balık. "Buradayım, içerisi çok kuru," dedi Tosbi. Balık gülümsedi ve suya geri döndü. Tosbi içeride sessizce bekledi. Bir süre sonra yağmur dindi ve bulutların arasından güneş çıktı. Tosbi başını yavaşça dışarı çıkardı. Balık da yeniden sudan baktı. Kumdaki renkli taşlar güneşte parlıyordu.
```

Tohum: park, yan Murat, özellik soru, kelimeler uçurtma/bağlamak/uzun, tema yardım istemek, açılış figür adı,
kapanış replik.

```
### Niloya | park | Murat
@plan: uçurtma ağaçların üstüne çıkamadı çünkü ipi kısaydı | ağabeyinden ip isteyip iki ipi bağladı
@tohum: niloya-9001
Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu. "Bak Murat, uçurtma ağaçlardan yüksek!" dedi Niloya.
```

## Kart: Karabaş (kaynaklı, kapalı dünya)

- Ad: Karabaş (okunuş: karabaş; kesme eki okunuşa uyar)
- Kimlik: Karabaş, sadık ve neşeli bir köpektir.
- Tür: köpek
- Güvenli özellik kullanımı: Topun ya da bir hayvanın peşinden yola, suya ya da yüksek yere koşmaz; havlaması kimseyi korkutmaz.
- Özellikler:
  - sadık: Sadıktır; arkadaşını hiç bırakmaz. (örnek biçimler: sadık)
  - top: Koşmayı ve top oynamayı sever. (örnek biçimler: top, topu, topla)
  - kuyruk: Sevinince kuyruğunu sallar. (örnek biçimler: kuyruğunu)
- Yerler:
  - dağ: Dağda çiçekli, taşlı bir yer.
  - deniz: Denizin kıyısı; kum ve sığ su kenarı. Herkes kumda ve su kenarında kalır.
  - orman: Ağaçlarla dolu, sessiz bir orman.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - sincap: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: sincap; konuşur. Yüzey biçimleri: sincap
  - kirpi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kirpi; konuşur. Yüzey biçimleri: kirpi
  - keçi: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: keçi; konuşur. Yüzey biçimleri: keçi
  - kuş: Figürün dünyasında yaşayan bir doğa hayvanı. Tür: kuş; konuşur. Yüzey biçimleri: kuş
- Dünya kuralları:
  - Karabaş hiçbir hayvanı kovalamaz ya da yakalamaz.
  - Hayvanlar tek tek konuşabilir; arka plandaki hayvan toplulukları konuşmaz ve olaya katılmaz.
- Yasak adlar: -
- İzinli dünya kelimeleri: kuyruk, top

## Tohumlar

### Karabaş | dağ | -
@tohum: karabas-0001
- yer: dağ (Dağda çiçekli, taşlı bir yer.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: top (Koşmayı ve top oynamayı sever.)
- kelimeler: isim 'çit', fiil 'serpmek', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: eylem (figür son bir şey yapar)

### Karabaş | dağ | -
@tohum: karabas-0002
- yer: dağ (Dağda çiçekli, taşlı bir yer.)
- tema: bir şey yapmak
- yan: -
- özellik: kuyruk (Sevinince kuyruğunu sallar.)
- kelimeler: isim 'delik', fiil 'yedirmek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaydan çıkan tek ve somut bir cümle)

### Karabaş | orman | -
@tohum: karabas-0003
- yer: orman (Ağaçlarla dolu, sessiz bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sadık (Sadıktır; arkadaşını hiç bırakmaz.)
- kelimeler: isim 'tohum', fiil 'ulaşmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün hissi)

### Karabaş | deniz | -
@tohum: karabas-0004
- yer: deniz (Denizin kıyısı; kum ve sığ su kenarı. Herkes kumda ve su kenarında kalır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sadık (Sadıktır; arkadaşını hiç bırakmaz.)
- kelimeler: isim 'resim', fiil 'kaldırmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: eylem (figür son bir şey yapar)

### Karabaş | dağ | -
@tohum: karabas-0005
- yer: dağ (Dağda çiçekli, taşlı bir yer.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: top (Koşmayı ve top oynamayı sever.)
- kelimeler: isim 'torba', fiil 'mırıldanmak', sıfat 'komik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: goruntu (sahneden son bir resim)

### Karabaş | deniz | kuş
@tohum: karabas-0006
- yer: deniz (Denizin kıyısı; kum ve sığ su kenarı. Herkes kumda ve su kenarında kalır.)
- tema: sırayla oynamak
- yan: kuş
- özellik: kuyruk (Sevinince kuyruğunu sallar.)
- kelimeler: isim 'fındık', fiil 'yıkamak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: goruntu (sahneden son bir resim)

### Karabaş | orman | sincap
@tohum: karabas-0007
- yer: orman (Ağaçlarla dolu, sessiz bir orman.)
- tema: paylaşmak
- yan: sincap
- özellik: sadık (Sadıktır; arkadaşını hiç bırakmaz.)
- kelimeler: isim 'düğüm', fiil 'şakımak', sıfat 'kırık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle bir konuşmadır)

### Karabaş | dağ | kirpi
@tohum: karabas-0008
- yer: dağ (Dağda çiçekli, taşlı bir yer.)
- tema: paylaşmak
- yan: kirpi
- özellik: top (Koşmayı ve top oynamayı sever.)
- kelimeler: isim 'top', fiil 'bölmek', sıfat 'huzurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle bir konuşmadır)

### Karabaş | dağ | keçi
@tohum: karabas-0009
- yer: dağ (Dağda çiçekli, taşlı bir yer.)
- tema: sahne içinde beklemek (sıra, fırındaki kek, yağmurun dinmesi)
- yan: keçi
- özellik: sadık (Sadıktır; arkadaşını hiç bırakmaz.)
- kelimeler: isim 'nane', fiil 'homurdanmak', sıfat 'karmakarışık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaydan çıkan tek ve somut bir cümle)
