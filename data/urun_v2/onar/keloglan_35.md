# Editör görevi (onarım): Keloğlan, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <aynı tohum kimliği>
@degisim: <eski> -> <yeni>      (yalnız özgün blokta varsa ve tutuyorsan)
@onarim: <özgün bloğun sha1'i; her hikâyede verilir>
<gövde>
```

- **Yalnız bulguların gösterdiği yeri düzelt** ve tutarlılık için değişmesi gerekeni (ör. çözüm değiştiyse plan
  satırı, silinen nesnenin sonraki anılışı). Öteki cümleler olduğu gibi kalır.
- **Tohumu ve hikâyeyi koru:** figür, yer, yan, tema, açılış, kapanış türü, diyalog, özellik ve tohum kelimeleri
  (isim, fiil, sıfat) aynı kalır; sorun ve çözüm aynı kalır. Tohum kelimelerinden en çok biri değişebilir ve
  `@degisim` satırına yazılır (özgün bloktaki değişim sayılır).
- Gövde 70-100 kelime, her cümle en çok 12 kelime, tek paragraf.
- Bir bulgu sana yanlış görünse bile o cümleyi daha basit ve açık biçimde yeniden söyle: hakem orada takıldı,
  okuyan çocuk da takılabilir. İşaretlenen kelimeyi ya da yapıyı tekrarlama.
- Görevi **YENİDEN YAZ** olan hikâyede (M3: çekirdek önemsiz ya da saçma) hikâyeyi aynı tohumdan baştan yaz:
  çocuğun önemseyeceği, sebebi ilk 3 cümlede söylenen bir sorun ve figürün 1-2 adımlık çözümü; başlık, tohum
  kimliği ve `@onarim` satırı yine verilir.
- Onarılmış metin özgünden farklı olmalıdır (aynı metin aynı kayıttır ve reddedilir).
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar35.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0095 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0095
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'süt', fiil 'kapamak', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: gözü kapalıyken kabarık şeyin ne olduğunu bilemedi | yavaşça dokundu ve ortasındaki sert sapı buldu
@tohum: keloglan-0095
@degisim: süt -> tüy
Ormanda Bilgecan Dede ile Keloğlan bir oyun oynuyordu. Keloğlan gözlerini kapadı ve dede onun avucuna bir şey koydu. Keloğlan bu kabarık şeyin ne olduğunu bilemedi, çünkü çok yumuşaktı. "Bu pamuk mu?" diye sordu Keloğlan. Bilgecan Dede güldü. "Hayır, bir daha dokun," dedi Bilgecan Dede. Keloğlan parmaklarını yavaşça gezdirdi. Ortasında ince ve sert bir sap vardı. "Bu bir tüy!" dedi Keloğlan. Keloğlan gözlerini açtı ve beyaz bir tüy gördü. Böylece tüylerin ortasında sert bir sap olduğunu öğrendi. Bilgecan Dede onu alkışladı. Keloğlan çok sevindi, çünkü tüyü kendi başına bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "beyaz bir tüy gördü"
   - Cümle 10: «Keloğlan gözlerini açtı ve beyaz bir tüy gördü.»
   - Açıklama: Tüy kayboldu denmişken Keloğlan onu avucunda görüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0095` birebir aynı, `@degisim: süt -> tüy` (tutuyorsan), ardından `@onarim: 4260f87f743dcc0ec0c6524653b0cbfeaecce410`, sonra gövde.

### Hikâye 2: tohum keloglan-0110 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0110
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kızartma', fiil 'doldurmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: sepetler iki ağaca takıldı ve eşek sıkıştı | sepet elinden kaydı ve eşeğin sırtı hafifledi
@tohum: keloglan-0110
Bir sabah Keloğlan eşeğiyle ormanda yürüyordu. Karakaçan sırtında iki büyük sepet taşıyordu. İki ağacın arasından geçerken sepetler ağaçlara takıldı. Karakaçan sıkıştı ve ileri gidemedi. "Dur, Karakaçan, sana yardım edeceğim," dedi Keloğlan. Keloğlan bir sepeti indirmek için tuttu. Ama sakar Keloğlan'ın elinden sepet kaydı ve yere düştü. Eşeğin sırtı hafifledi. Eşek hemen ağaçların arasından çıktı. Sepetin kapağı sıkıca kapalıydı. Keloğlan onu sabah kızartma ile doldurmuştu. Kızartma yere hiç dökülmedi. Keloğlan sepeti yeniden eşeğin sırtına koydu. Sonra ikisi ağaçların yanından geçip yola mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Karakaçan sırtında iki büyük sepet"
   - Cümle 2: «Karakaçan sırtında iki büyük sepet taşıyordu.»
   - Açıklama: Karakaçan'ın eşek olduğu söylenmeden ad olarak giriyor, sonra 'eşek' diye anılıyor; kimi gösterdiği belli değil.
   - Açıklama: Karakaçan'ın eşeğin adı olduğu söylenmeden ad birden kullanılıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "elinden sepet kaydı ve yere düştü"
   - Cümle 7: «Ama sakar Keloğlan'ın elinden sepet kaydı ve yere düştü.»
   - Açıklama: Sorun Keloğlan'ın bilinçli çözümüyle değil, sepetin kazayla elinden kaymasıyla çözülüyor.
   - Açıklama: Sorunu Keloğlan bilerek çözmüyor, sepet kazayla düşünce sorun kendiliğinden çözülüyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "elinden sepet kaydı ve yere düştü"
   - Cümle 7: «Ama sakar Keloğlan'ın elinden sepet kaydı ve yere düştü.»
   - Açıklama: Çözüm sebebe bilinçli olarak yönelmiyor, bir kazayla geliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan onu sabah kızartma ile doldurmuştu"
   - Cümle 11: «Keloğlan onu sabah kızartma ile doldurmuştu.»
   - Açıklama: Kapak ve kızartma ayrıntısı olaydan çıkmıyor, sorun çözüldükten sonra sebepsizce ekleniyor.
   - Açıklama: Kızartma ve kapak ayrıntısı olaya bir şey katmıyor ve çözümü sebepsiz kaza getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0110` birebir aynı, ardından `@onarim: b1a1fb93b5a093fe8f1cb2e3a5e9da9a029ffe07`, sonra gövde.

### Hikâye 3: tohum keloglan-0111 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0111
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kaşık', fiil 'hazırlanmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda nereden geldiği bilinmeyen bir ses vardı | aramayı bırakmadı ve sesin kendi çantasından geldiğini buldu
@tohum: keloglan-0111
Hafif bir rüzgar esiyordu. Keloğlan ormanda yemek yemeye hazırlanıyordu. Çantasını alçak bir dala asmıştı. Birden yakından ince bir ses geldi. Keloğlan bu sesin nereden geldiğini çok merak etti. Büyük bir kayanın arkasına baktı ama hiçbir şey göremedi. Biraz mutsuz oldu. Ama Keloğlan dürüst ve azimliydi, aramayı bırakmadı. Durdu ve sesi dikkatle dinledi. Sonunda sesin kendi çantasından geldiğini buldu. Rüzgar çantayı sallıyordu. İçindeki kaşık da bardağa çarpıp ses çıkarıyordu. Keloğlan güldü ve kaşığı çıkardı. Ses hemen kesildi. Keloğlan bundan sonra bir sesi merak edince onu bulana kadar aradı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Birden yakından ince bir ses geldi.»
   - Açıklama: Sorun (gelen ses) ilk üç cümlede değil, dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst ve azimliydi"
   - Cümle 8: «Ama Keloğlan dürüst ve azimliydi, aramayı bırakmadı.»
   - Açıklama: 'Dürüst' kelimesi aramayı bırakmamakla ilgisiz, yanlış bağlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0111` birebir aynı, ardından `@onarim: d9f9a4f6f56c91fab534fc1370fd3c2d86d4ce7c`, sonra gövde.

### Hikâye 4: tohum keloglan-0112 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0112
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çam', fiil 'fışkırmak', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: acele edip düğmeye sert bastı ve dedeyi ıslattı | özür diledi ve düğmeye yavaşça bastı
@tohum: keloglan-0112
Bir sabah Keloğlan ile Bilgecan Dede tepedeydi. Dede bir çam ağacına su veren kırılgan bir icat getirmişti. Keloğlan acele etti ve icadın düğmesine çok sert bastı. Su birden fışkırdı ve Dede'nin yüzünü ıslattı. "Özür dilerim, Bilgecan Dede, bu benim hatamdı," dedi Keloğlan. Dede gülümsedi ve yüzünü sildi. Keloğlan icadı kullanmayı öğrenmek istedi. "Bilgecan Dede, bana doğrusunu gösterir misin?" diye sordu Keloğlan. Bilgecan Dede düğmeye parmağıyla hafifçe dokundu. Keloğlan da tıpkı onun gibi yaptı. Bu kez su yavaşça ağacın dibine aktı. Keloğlan çok sevindi, çünkü Dede ona hiç kızmamıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırılgan bir icat getirmişti"
   - Cümle 2: «Dede bir çam ağacına su veren kırılgan bir icat getirmişti.»
   - Açıklama: 'Kırılgan' ve 'icat' kelimelerini 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "su veren kırılgan bir icat"
   - Cümle 2: «Dede bir çam ağacına su veren kırılgan bir icat getirmişti.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime ve hikayede işlevi yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kırılgan bir icat getirmişti"
   - Cümle 2: «Dede bir çam ağacına su veren kırılgan bir icat getirmişti.»
   - Açıklama: İcadın kırılgan olduğu vurgulanıyor ama bu ayrıntı olayda hiç kullanılmıyor.
   - Açıklama: İcadın kırılgan olduğu vurgulanıyor ama bu özellik hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0112` birebir aynı, ardından `@onarim: b50fe7dd28d09e566a4490d541440c29d79742a3`, sonra gövde.

### Hikâye 5: tohum keloglan-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0113
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'basamak', fiil 'hızlanmak', sıfat 'serin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: ağaçlardan garip bir tık tık sesi geliyordu | yere düşen kozalağı buldu ve annesine sordu
@tohum: keloglan-0113
@degisim: basamak -> kozalak
Ormanda serin bir rüzgar esiyordu. Keloğlan anasıyla büyük ağaçların altında yürüyordu. Birden yukarıdan tık tık diye bir ses geldi. Sonra ses gittikçe hızlandı. Keloğlan sesin ne olduğunu öğrenmek istedi. Yukarı baktı ama yaprakların arasında bir şey göremedi. Sonra ayağının yanına kahverengi bir şey düştü. Keloğlan onu yerden aldı ve anasına gösterdi. "Anneciğim, bu nedir?" diye sordu Keloğlan. "Bu bir kozalak, rüzgar esince dallardan düşüyor," dedi anası. O sırada bir kozalak daha tık diye yere düştü. Keloğlan çok sevindi, çünkü sesi yapan kozalakları bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra ses gittikçe hızlandı"
   - Cümle 4: «Sonra ses gittikçe hızlandı.»
   - Açıklama: Ses hızlanmaz; fiil öznesine uymuyor, 'tık tıklar sıklaştı' gibi olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sonra ses gittikçe hızlandı"
   - Cümle 4: «Sonra ses gittikçe hızlandı.»
   - Açıklama: Yukarıdan gelen ve hızlanan tık tık sesinin sebebi olarak ara sıra düşen kozalak akla yatkın değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra ayağının yanına kahverengi bir şey düştü"
   - Cümle 7: «Sonra ayağının yanına kahverengi bir şey düştü.»
   - Açıklama: Çözüm Keloğlan'ın bir çabasıyla değil, kozalağın rastlantıyla ayağının dibine düşmesiyle geliyor.
   - Açıklama: Çözümü getiren kozalak figürün bir eylemi olmadan tesadüfen düşüyor; ayrıca sesin hızlanması hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0113` birebir aynı, `@degisim: basamak -> kozalak` (tutuyorsan), ardından `@onarim: b60b9fbde1578c3b2f847c17f635d45a353f358f`, sonra gövde.

### Hikâye 6: tohum keloglan-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0115
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kıyafet', fiil 'güneşlenmek', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: resim için yeşil boya yoktu | sarı boya maviye döküldü ve yeşil oldu
@tohum: keloglan-0115
Tepede hafif bir rüzgar esiyordu. Keloğlan'ın eşeği Karakaçan otların üstünde güneşleniyordu. Keloğlan ilk kez resim yapıyordu, ama yeşil boyası yoktu. Elinde yalnız mavi ve sarı boya vardı. Üstünde eski bir kıyafet vardı. Keloğlan otları nasıl yeşil yapacağını düşündü. Sakar Keloğlan birden sarı boyayı elinden düşürdü. Sarı boya mavi boyanın içine döküldü ve biraz da kıyafete sıçradı. Keloğlan boyaları fırçayla karıştırınca yeşil bir boya oldu. Keloğlan çok şaşırdı ve güldü. Hemen resimdeki otları yeşile boyadı. Karakaçan resme bakıp başını salladı. Keloğlan bundan sonra yeşil boya için sarı ve maviyi karıştırdı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Üstünde eski bir kıyafet vardı"
   - Cümle 5: «Üstünde eski bir kıyafet vardı.»
   - Açıklama: Eski kıyafet işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
   - Açıklama: Kıyafet işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "otları nasıl yeşil yapacağını"
   - Cümle 6: «Keloğlan otları nasıl yeşil yapacağını düşündü.»
   - Açıklama: Gerçek otlar zaten yeşil; resimdeki otlar kastedildiği belirtilmediği için anlam yanlış.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sakar Keloğlan birden sarı boyayı elinden düşürdü"
   - Cümle 7: «Sakar Keloğlan birden sarı boyayı elinden düşürdü.»
   - Açıklama: Sorunu figürün çabası değil rastlantı bir kaza çözüyor.
   - Açıklama: Yeşil boya figürün çözümüyle değil kazayla elde ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0115` birebir aynı, ardından `@onarim: 42cfeedf8d25bbedffb96788b19e089a5ce5ba50`, sonra gövde.

### Hikâye 7: tohum keloglan-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0116
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kereviz', fiil 'küçültmek', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: annesinin yemeği yoktu ve kereviz ikiye kırılmadı | kereviz elinden kayıp taşa çarptı ve ikiye ayrıldı
@tohum: keloglan-0116
Keloğlan anasıyla ormanda ferah bir açıklığa geldi. Anası yemeğini evde unutmuştu ve çok acıkmıştı. Keloğlan'ın çantasında yalnız bir kereviz vardı. Keloğlan kerevizi anasıyla paylaşmak istedi. Onu küçültmek için iki eliyle bükmeye çalıştı. Ama kereviz çok sertti ve hiç kırılmadı. Birden kereviz sakar Keloğlan'ın elinden kaydı ve düz bir taşa çarptı. Kereviz çat diye ikiye ayrıldı. Keloğlan parçaları aldı ve güldü. "Anneciğim, bu parça senin, bu da benim," dedi Keloğlan. Anası parçasını aldı ve Keloğlan'ı öptü. İkisi ağaçların gölgesinde oturup kerevizi yedi. "Teşekkürler, Keloğlan, birlikte yemek çok güzel!" dedi anası.
```

**Hakem bulguları (7):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormanda ferah bir açıklığa"
   - Cümle 1: «Keloğlan anasıyla ormanda ferah bir açıklığa geldi.»
   - Açıklama: 'Ferah' ve 'açıklık' 3 yaşındaki çocuğun bilmeyeceği kelimeler.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir açıklığa geldi"
   - Cümle 1: «Keloğlan anasıyla ormanda ferah bir açıklığa geldi.»
   - Açıklama: 'Ferah' ve 'açıklık' 3 yaşındaki çocuğun bilmeyeceği kelimeler.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kereviz çok sertti ve hiç kırılmadı"
   - Cümle 6: «Ama kereviz çok sertti ve hiç kırılmadı.»
   - Açıklama: Asıl sorun olan kerevizin kırılmaması ancak 6. cümlede söyleniyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "kereviz sakar Keloğlan'ın elinden kaydı"
   - Cümle 7: «Birden kereviz sakar Keloğlan'ın elinden kaydı ve düz bir taşa çarptı.»
   - Açıklama: Sorunu Keloğlan değil bir kaza çözüyor; kereviz elinden kayıp taşa çarparak kırılıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "elinden kaydı ve düz bir taşa çarptı"
   - Cümle 7: «Birden kereviz sakar Keloğlan'ın elinden kaydı ve düz bir taşa çarptı.»
   - Açıklama: Çözüm figürün sebebe yönelen bir eylemi değil, rastlantı.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kereviz sakar Keloğlan'ın elinden kaydı"
   - Cümle 7: «Birden kereviz sakar Keloğlan'ın elinden kaydı ve düz bir taşa çarptı.»
   - Açıklama: Kereviz bilinçli bir çözümle değil, kazayla kırılıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "düz bir taşa çarptı"
   - Cümle 7: «Birden kereviz sakar Keloğlan'ın elinden kaydı ve düz bir taşa çarptı.»
   - Açıklama: Çözüm önceki olaydan çıkmıyor, tesadüfen beliren bir taşla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0116` birebir aynı, ardından `@onarim: 120b631079c2ba2fe4cc712369f3cbac50f6348f`, sonra gövde.

### Hikâye 8: tohum keloglan-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0117
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fide', fiil 'gerinmek', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: fidan rüzgarda yana yatıyordu ve dallar kısaydı | gerindi, uzun bir dal düşürdü ve fidanı bağladı
@tohum: keloglan-0117
@degisim: fide -> fidan
Bir sabah Balkız ormanda küçük bir fidan dikiyordu. Keloğlan da ona yardım ediyordu. Ama rüzgar esince ince fidan hep yana yatıyordu. Onu bir dala bağlamak gerekiyordu, ama yerdeki dallar çok kısaydı. "Keloğlan, uzun bir dal lazım," dedi Balkız. Keloğlan düşünürken kollarını açıp gerindi. Sakar Keloğlan'ın eli alçak bir ağaçtaki kuru dala çarptı. Kuru dal kırıldı ve yere düştü. Keloğlan dalı fidanın yanına dikti. Balkız cebinden bir ip çıkardı ve Keloğlan fidanı dala bağladı. Rüzgar yine esti, ama fidan dik kaldı. "Teşekkürler, Keloğlan, sen çok iyi bir arkadaşsın!" dedi Balkız.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan düşünürken kollarını açıp gerindi"
   - Cümle 6: «Keloğlan düşünürken kollarını açıp gerindi.»
   - Açıklama: Çözüm sebebe bilinçli olarak yönelmiyor; dal şans eseri bulunuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sakar Keloğlan'ın eli alçak bir ağaçtaki kuru dala çarptı"
   - Cümle 7: «Sakar Keloğlan'ın eli alçak bir ağaçtaki kuru dala çarptı.»
   - Açıklama: Güvenli kullanım satırı sakarlığı yalnız düşürme ya da karıştırma olarak izin veriyor; burada ağaca çarpıp dal kırılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan'ın eli alçak bir ağaçtaki kuru dala çarptı"
   - Cümle 7: «Sakar Keloğlan'ın eli alçak bir ağaçtaki kuru dala çarptı.»
   - Açıklama: Çözümü getiren dal düşünülmüş bir eylemle değil tesadüfen, sebepsizce geliyor.
   - Açıklama: Çözümü getiren uzun dal tesadüfen, kaza sonucu ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0117` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: 50dae9f976c79be1bd902a84131a3cb1df16e47a`, sonra gövde.

### Hikâye 9: tohum keloglan-0118 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0118
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'havlu', fiil 'uyutmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşek acıkmıştı ama tepede hiç ot yoktu | havlu elinden düştü ve havuçlar eşeğin önüne döküldü
@tohum: keloglan-0118
Tepede serin bir rüzgar esiyordu. Keloğlan eşeği Karakaçan ile taşların arasında oturuyordu. Karakaçan çok acıkmıştı, ama tepede hiç ot yoktu. Havuçlar eşeğin sırtında, bir havlunun içindeydi. "Bekle, Karakaçan, havuçlarını hemen veriyorum," dedi Keloğlan. Sakar Keloğlan havluyu çekerken onu elinden düşürdü. Havlu açıldı ve havuçlar tam eşeğin önüne döküldü. Karakaçan hepsini mutlu mutlu yedi. Sonra eşek yere yattı ve esnedi. Keloğlan havluyu onun başının altına koydu. Şirin eşeğin başını sevip onu uyuttu. Keloğlan çok sevindi, çünkü aç eşeğine yardım etmişti.
```

**Hakem bulguları (7):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Keloğlan eşeği Karakaçan ile"
   - Cümle 2: «Keloğlan eşeği Karakaçan ile taşların arasında oturuyordu.»
   - Açıklama: Virgül eksik; 'Keloğlan eşeği' tamlama gibi okunuyor, 'Keloğlan, eşeği Karakaçan ile' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Havuçlar eşeğin sırtında, bir havlunun içindeydi"
   - Cümle 4: «Havuçlar eşeğin sırtında, bir havlunun içindeydi.»
   - Açıklama: Havuçlar zaten elde olduğu için gerçek bir sorun yok.
   - Açıklama: Havuçlar zaten elinin altındayken otun olmaması gerçek bir sorun oluşturmuyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "havluyu çekerken onu elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan havluyu çekerken onu elinden düşürdü.»
   - Açıklama: Sorunu figürün bilinçli eylemi değil bir kaza çözüyor.
   - Açıklama: Sorun Keloğlan'ın bilinçli bir eylemiyle değil, bir kazayla kendiliğinden çözülüyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "havuçlar tam eşeğin önüne döküldü"
   - Cümle 7: «Havlu açıldı ve havuçlar tam eşeğin önüne döküldü.»
   - Açıklama: Çözüm sebebe yönelen bir eylem değil, tesadüfle geliyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Havlu açıldı ve havuçlar tam eşeğin önüne döküldü"
   - Cümle 7: «Havlu açıldı ve havuçlar tam eşeğin önüne döküldü.»
   - Açıklama: Çözüm sebebe yönelen bir eylem değil, rastlantı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "havuçlar tam eşeğin önüne döküldü"
   - Cümle 7: «Havlu açıldı ve havuçlar tam eşeğin önüne döküldü.»
   - Açıklama: Çözümü sebepsiz bir kaza getiriyor.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şirin eşeğin başını sevip onu uyuttu"
   - Cümle 11: «Şirin eşeğin başını sevip onu uyuttu.»
   - Açıklama: Cümlenin öznesi belli değil; 'Şirin' bir ad gibi okunabiliyor ve eşeği kimin uyuttuğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0118` birebir aynı, ardından `@onarim: b9df563fd693207b80771774e9da05b3eb209a36`, sonra gövde.

### Hikâye 10: tohum keloglan-0119 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0119
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'bulaşık', fiil 'zıplatmak', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: top kapının altından şatonun bahçesine kaçtı | izinsiz içeri girmedi ve topu uzun bir dalla çekti
@tohum: keloglan-0119
@degisim: bulaşık -> dal
Hafif bir rüzgar esiyordu. Keloğlan şatonun yüksek kapısının önünde küçük bir top zıplatıyordu. Top her yere değdiğinde Keloğlan bir kez dönüyordu. Ama top bir taşa çarptı ve kapının altından bahçeye kaçtı. Bahçe Keloğlan'ın değildi. Dürüst Keloğlan izinsiz içeri girmedi. Yerde uzun bir dal buldu. Dalı kapının altından uzattı ve topu yavaşça kendine çekti. Top yeniden elindeydi. Bu kez kapıdan uzakta, düz taşların üstünde oynadı. Top tam on kez zıpladı ve Keloğlan on kez döndü. Keloğlan çok sevindi, çünkü topunu geri almış ve oyununa devam etmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Top her yere değdiğinde"
   - Cümle 3: «Top her yere değdiğinde Keloğlan bir kez dönüyordu.»
   - Açıklama: 'Her yere' yanlış sırada; 'yere her değdiğinde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0119` birebir aynı, `@degisim: bulaşık -> dal` (tutuyorsan), ardından `@onarim: 9831762818aa0ba9f2b7f1294fc580c373d6d0fb`, sonra gövde.

### Hikâye 11: tohum keloglan-0120 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0120
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ip', fiil 'kırpmak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: kayaların arkasından gürültülü bir ses geldi | bilmediğini söyledi ve ipin ucunda kutuları buldu
@tohum: keloglan-0120
Bir sabah Keloğlan ile Bilgecan Dede tepede yürüyordu. Birden kayaların arkasından gürültülü bir ses geldi. "Dede, bu ses nereden geliyor?" diye merakla sordu Keloğlan. Dede gülümsedi ve bir gözünü kırptı. "Sen ne düşünüyorsun?" diye sordu Dede. Keloğlan dürüst davrandı ve "Bilmiyorum, Dede," dedi. Dede bu cevabı sevdi ve kayalara giden uzun bir ipi gösterdi. Keloğlan ipin yanından yürüdü. İpin ucunda üç teneke kutu sallanıyordu. Rüzgar esince kutular birbirine çarpıyordu. "Bu senin icadın mı?" diye sordu Keloğlan. "Evet, bu benim rüzgar icadım," dedi Dede. Keloğlan çok sevindi, çünkü sesin nereden geldiğini kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kayaların arkasından gürültülü bir ses geldi"
   - Cümle 2: «Birden kayaların arkasından gürültülü bir ses geldi.»
   - Açıklama: Ses yalnız bir merak konusu, çocuğun önemseyeceği gerçek bir sorun değil.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Dede bu cevabı sevdi ve kayalara giden uzun bir ipi gösterdi"
   - Cümle 7: «Dede bu cevabı sevdi ve kayalara giden uzun bir ipi gösterdi.»
   - Açıklama: Sesin kaynağını yan karakter Dede gösteriyor, Keloğlan yalnız takip ediyor.
   - Açıklama: Sesin kaynağını Keloğlan değil, ipi gösteren Dede buluyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sesin nereden geldiğini kendisi bulmuştu"
   - Cümle 13: «Keloğlan çok sevindi, çünkü sesin nereden geldiğini kendisi bulmuştu.»
   - Açıklama: Son cümle Keloğlan'ın kendisi bulduğunu söylüyor ama ipi Dede göstermişti.
   - Açıklama: Keloğlan'ın sesi kendisi bulduğu söyleniyor ama ipi Dede gösterdi ve icat zaten Dede'nindi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0120` birebir aynı, ardından `@onarim: 2391680649b860bf31c8201dafef7cca1fa0bc80`, sonra gövde.

### Hikâye 12: tohum keloglan-0121 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0121
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'etiket', fiil 'dinlenmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar sert sepetten hep dışarı zıplıyordu | yosunu görüp sepetin içine yumuşak yosun koydu
@tohum: keloglan-0121
@degisim: etiket -> kozalak
Keloğlan ormanda eğlenceli bir oyun oynuyordu. Kozalakları uzaktan sepetine atıyordu. Ama sepet çok sertti ve kozalaklar hep dışarı zıplıyordu. Keloğlan birkaç kez daha denedi ama olmadı. Sonra yoruldu ve bir kütüğün üstüne oturup dinlendi. Cebindeki sulu armudu yedi ve etrafa baktı. O sırada ağaçtan bir kozalak yumuşak yosunların üstüne düştü ve hiç kıpırdamadı. Keloğlan bunu görünce yumuşak yerde kozalakların zıplamadığını öğrendi. Hemen sepetin içine yumuşak yosun koydu. Sonra kozalakları yine attı. Bu kez hepsi sepette kaldı ve Keloğlan sevinçle el çırptı. Keloğlan bundan sonra oyunda bir sorun olunca etrafına dikkatle baktı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Cebindeki sulu armudu yedi"
   - Cümle 6: «Cebindeki sulu armudu yedi ve etrafa baktı.»
   - Açıklama: Armut hiçbir işe yaramayan işlevsiz bir ayrıntı; çözüm de ağaçtan tesadüfen düşen kozalakla geliyor.
   - Açıklama: Armut işlevsiz bir ayrıntı; olayda hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir sorun olunca etrafına"
   - Cümle 12: «Keloğlan bundan sonra oyunda bir sorun olunca etrafına dikkatle baktı.»
   - Açıklama: 'Sorun' soyut bir kavram ve ders cümlesi somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0121` birebir aynı, `@degisim: etiket -> kozalak` (tutuyorsan), ardından `@onarim: 2298d7e458eb4b180e6c7e810b23ce7600705c7b`, sonra gövde.
