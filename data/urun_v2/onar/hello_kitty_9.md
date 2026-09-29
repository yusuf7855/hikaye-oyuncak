# Editör görevi (onarım): Hello Kitty, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hello Kitty | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar9.txt --ad urun_v2`
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

## Kart: Hello Kitty (kaynaklı, kapalı dünya)

- Ad: Hello Kitty (okunuş: helo kiti; kesme eki okunuşa uyar)
- Kimlik: Hello Kitty, ailesiyle birlikte bir evde yaşayan, kırmızı kurdeleli, beyaz ve iyi kalpli bir kedidir.
- Tür: kedi
- Güvenli özellik kullanımı: Kurabiye ve turta bir büyükle birlikte yapılır; fırını ve sıcak tepsiyi annesi ya da babası tutar. Kimse yabancıyla bir yere gitmez; kimse tek başına uzağa gitmez.
- Özellikler:
  - arkadaş: Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır. (örnek biçimler: arkadaş, arkadaşlar, arkadaşıyla)
  - kurabiye: Kurabiye yapmayı çok sever. (örnek biçimler: kurabiye, kurabiyeler, kurabiyeleri)
  - turta: En çok elmalı turtayı sever. (örnek biçimler: turta, turtayı, turtası)
- Yerler:
  - park: Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.
  - orman: Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.
  - ev: Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Mimi: Hello Kitty'nin ikiz kız kardeşi ve en iyi arkadaşı; utangaçtır ve sarı kurdele takar. Tür: kedi; konuşur. Yüzey biçimleri: Mimi, kardeş, kardeşi, ikiz, ikizi
  - annesi: Hello Kitty'nin annesi; çok iyi yemek yapar, elmalı turtası çok güzeldir. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
  - babası: Hello Kitty'nin babası; güvenilir ve komiktir, bazen bir şeyi unutur. Tür: baba; konuşur. Yüzey biçimleri: baba, babası, babacığım, Baba
- Dünya kuralları:
  - Hello Kitty, Mimi, annesi ve babası konuşur. Hikayede Hello Kitty'nin ağzından söz edilmez.
  - Mimi, Hello Kitty'nin ikiz kız kardeşidir; ablası ya da kuzeni değildir. Mimi sarı kurdele takar.
  - Hikaye evde, parkta ya da ormanda tek sahnede geçer; Londra'ya ya da başka bir şehre yolculuk yoktur.
  - Hello Kitty bir marka ya da satılan bir eşya olarak anılmaz; mağaza ve alışveriş yoktur.
- Yasak adlar: Dear Daniel, Daniel, Charmmy Kitty, Charmmy, Sugar, Ichigoman, Mimmy, Kitty White, George, Mary, Anthony, Margaret, Joey, Judy, Tippy, Thomas, Tracy, Rorry, My Melody
- Yasak: Marka, mağaza, alışveriş, uçak ya da trenle şehir yolculuğu ve zamanda yolculuk hikayeye girmez.
- İzinli dünya kelimeleri: kurdele, kurabiye, turta, piknik, kamp

## Onarılacak hikâyeler

### Hikâye 1: tohum hello_kitty-0004 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0004
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'zil', fiil 'ölçmek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesinin küçük zili çantadan düştü | ince sesi dinledi ve zili çalının dalında buldu
@tohum: hello_kitty-0004
@degisim: ölçmek -> dinlemek
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Annesinin çantasındaki küçük zil yoktu. Zil yürürken bir yere düşmüştü ve annesi üzüldü. Hello Kitty herkese iyi davranan bir arkadaştı ve annesine hemen yardım etti. Ilık bir rüzgar esti. Birden ağaçların arasından ince bir ses geldi. Hello Kitty sesi merak etti ve durup dinledi. "Anne, bu ses nereden geliyor?" diye sordu Hello Kitty. "Bilmiyorum, gel bakalım," dedi annesi. İkisi sese doğru yürüdü. Ses bir çalının içinden geliyordu. Zil çalının dalına takılmıştı ve rüzgarda sallanıyordu. Annesi zili aldı ve Hello Kitty'ye sarıldı. Hello Kitty çok sevindi, çünkü annesinin zilini bulmuştu.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Annesinin çantasındaki küçük zil yoktu"
   - Cümle 2: «Annesinin çantasındaki küçük zil yoktu.»
   - Açıklama: 'Çantasındaki' ile 'yoktu' çelişiyor; 'Annesinin küçük zili çantasında yoktu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Zil yürürken bir yere"
   - Cümle 3: «Zil yürürken bir yere düşmüştü ve annesi üzüldü.»
   - Açıklama: 'Yürürken' zarf-fiilinin öznesi zil gibi duruyor; zil yürümez.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Zil yürürken bir yere düşmüştü"
   - Cümle 3: «Zil yürürken bir yere düşmüştü ve annesi üzüldü.»
   - Açıklama: 'Yürürken' zarf-fiilinin öznesi zil gibi okunuyor; zil yürümez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "herkese iyi davranan bir arkadaştı"
   - Cümle 4: «Hello Kitty herkese iyi davranan bir arkadaştı ve annesine hemen yardım etti.»
   - Açıklama: Tohumdaki arkadaş özelliği bir etiket olarak söyleniyor, zilin bulunmasında işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty herkese iyi davranan bir arkadaştı"
   - Cümle 4: «Hello Kitty herkese iyi davranan bir arkadaştı ve annesine hemen yardım etti.»
   - Açıklama: Hello Kitty'nin hemen yardım ettiği söyleniyor ama hiçbir yardım eylemi gelmiyor; çözüm tesadüfen gelen sesle bulunuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ilık bir rüzgar esti"
   - Cümle 5: «Ilık bir rüzgar esti.»
   - Açıklama: Zilin bulunmasını rüzgarın tesadüfen zili çalması getiriyor; çözüm sebepsizce geliyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Annesi zili aldı ve Hello Kitty'ye sarıldı"
   - Cümle 13: «Annesi zili aldı ve Hello Kitty'ye sarıldı.»
   - Açıklama: Zil ikisinin birlikte yürümesiyle bulunuyor ve zili annesi alıyor; figürün kendi çözümü belirgin değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0004` birebir aynı, `@degisim: ölçmek -> dinlemek` (tutuyorsan), ardından `@onarim: 1a3dcae8cc315e3491d617395b428a58785fea60`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0013 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0013
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fırça', fiil 'yollamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesinin fırçası çok kalındı | kendi incecik fırçasını annesine verdi
@tohum: hello_kitty-0013
@degisim: yollamak -> vermek
Hello Kitty ile annesi parkta düz taşları boyuyordu. Annesi taşına küçük bir kedi yaptı. Ama kalın fırçasıyla kedinin ince bıyıklarını yapamadı. "Bu fırça çok kalın," dedi annesi. Hello Kitty herkese yardım eden iyi bir arkadaştı. Annesi için hemen kendi fırçalarına baktı. Onun bir de incecik bir fırçası vardı. "Anne, bu fırçayı sana veriyorum!" dedi Hello Kitty. Annesi fırçayı aldı ve bıyıkları tek tek çizdi. Taşın üstündeki kedi artık çok tatlı görünüyordu. "Teşekkürler, kızım," dedi annesi. Hello Kitty çok mutlu oldu, çünkü fırçasını annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty herkese yardım eden iyi bir arkadaştı"
   - Cümle 5: «Hello Kitty herkese yardım eden iyi bir arkadaştı.»
   - Açıklama: Kartın özelliği yeni arkadaşlar edinmek; burada özellik bir etiket gibi söyleniyor ve anneye 'arkadaş' denerek karttaki gibi kullanılmıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun bir de incecik"
   - Cümle 7: «Onun bir de incecik bir fırçası vardı.»
   - Açıklama: Önceki cümle 'Annesi' ile başladığı için 'Onun' zamirinin Hello Kitty'yi mi annesini mi gösterdiği belli değil.
   - Açıklama: Önceki cümlede hem Hello Kitty hem annesi geçtiği için 'Onun' zamirinin kimi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0013` birebir aynı, `@degisim: yollamak -> vermek` (tutuyorsan), ardından `@onarim: 76c783a38ebed348d3ddcd5538b32a5ed69b9bde`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0014 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0014
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'karnabahar', fiil 'uzaklaşmak', sıfat 'sabunlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar esince köpük balonları küçükken uzaklaştı | kalın bir ağacın arkasına geçip çubuğu yavaşça salladı
@tohum: hello_kitty-0014
Bir sabah Hello Kitty parkta köpük balonu yapıyordu. Çubuğu sabunlu suya batırdı ve havada salladı. Ama rüzgar esince balonlar küçükken çubuktan koptu ve uzaklaştı. Hello Kitty arkadaşlarına göstermek için büyük bir balon yapmak istiyordu. Küçük balonlar çiçeklerin üstünde bir bir patladı. Hello Kitty etrafına baktı ve kalın bir ağaç gördü. Ağacın arkasına geçti, orada rüzgar yoktu. Bu kez çubuğu çok yavaş salladı. Çubuğun ucunda bir balon büyümeye başladı. Balon sonunda bir karnabahar kadar oldu! Hello Kitty çok sevindi, çünkü en büyük balonu yapmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarına göstermek için büyük"
   - Cümle 4: «Hello Kitty arkadaşlarına göstermek için büyük bir balon yapmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği işe yarar biçimde kullanılmıyor, yalnız gerekçe olarak anılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "arkadaşlarına göstermek için büyük bir balon"
   - Cümle 4: «Hello Kitty arkadaşlarına göstermek için büyük bir balon yapmak istiyordu.»
   - Açıklama: Balonu arkadaşlarına gösterme amacı kuruluyor ama arkadaşlar hikayede hiç görünmüyor ve bu amaç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0014` birebir aynı, ardından `@onarim: 67969e1e5bb96df9036e75c916b17d40359ba494`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0015 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0015
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'para', fiil 'gezdirmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşinin kurdelesi başının arkasında bir dala takıldı | kurdeleyi daldan yavaşça çıkardı ve yine bağladı
@tohum: hello_kitty-0015
@degisim: devasa -> büyük
Bir sabah Hello Kitty ile Mimi ormandaki kamp yerinde, çadırın yanındaydı. Mimi büyük bir ağacın altında parlak bir para gördü. Parayı aldı ama kalkarken sarı kurdelesi alçak bir dala takıldı. Mimi kurdeleyi göremedi, çünkü kurdele başının arkasındaydı. Mimi kurdelesini çok seviyordu ve üzüldü. Hello Kitty iyi bir arkadaştı ve hemen kardeşine yardım etti. Mimi'nin arkasına geçti ve dala baktı. Kurdele dala dolanmıştı. Hello Kitty parmaklarını dalın üstünde gezdirdi ve kurdelenin ucunu buldu. Kurdeleyi daldan yavaşça çözdü. Sonra onu Mimi'nin başına güzelce bağladı. Mimi sevinçle gülümsedi ve kardeşine sarıldı. İki kardeş çadırın yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mimi büyük bir ağacın altında parlak bir para gördü"
   - Cümle 2: «Mimi büyük bir ağacın altında parlak bir para gördü.»
   - Açıklama: Parlak para sebepsiz beliriyor ve hikayede bir daha hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "büyük bir ağacın altında parlak bir para gördü"
   - Cümle 2: «Mimi büyük bir ağacın altında parlak bir para gördü.»
   - Açıklama: Para sebepsiz beliriyor ve olayda bir daha hiçbir işe yaramıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty iyi bir arkadaştı"
   - Cümle 6: «Hello Kitty iyi bir arkadaştı ve hemen kardeşine yardım etti.»
   - Açıklama: Mimi kardeşi olduğu halde 'arkadaş' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Mimi kardeşi olduğu halde 'arkadaş' denmesi kelimeyi yanlış ilişkide kullanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0015` birebir aynı, `@degisim: devasa -> büyük` (tutuyorsan), ardından `@onarim: 91c9ede2f25409180384a9f092e4071cb55eca5f`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0016 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0016
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mercan', fiil 'giydirmek', sıfat 'kirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babasının elleri kirliydi ve babası temiz kazağını giyemedi | babasının ellerine su döktü ve babası ellerini yıkadı
@tohum: hello_kitty-0016
@degisim: mercan -> kazak
Bir sabah ormandaki kamp yerinde serin bir rüzgar esti. Hello Kitty'nin babası kazağını giymek istedi. Ama çadırı kurarken elleri çok kirli olmuştu. "Temiz kazağı kirletmek istemiyorum," dedi babası. Hello Kitty kurabiye yaparken hep önce ellerini yıkardı. Hemen şişeyle su getirdi ve babasının ellerine döktü. Babası ellerini güzelce yıkadı. "Baba, kazağı sana ben giydireyim mi?" diye sordu Hello Kitty. "Teşekkürler, kızım, ellerim artık temiz, kendim giyerim," dedi babası. Babası kazağını giydi ve kazak tertemiz kaldı. Sonra gülerek Hello Kitty'ye sarıldı. Hello Kitty bundan sonra kirli elleri görünce hemen su getirmeye başladı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kurabiye yaparken hep önce ellerini yıkardı"
   - Cümle 5: «Hello Kitty kurabiye yaparken hep önce ellerini yıkardı.»
   - Açıklama: Kamp yerinde kurabiye ayrıntısı sebepsiz ekleniyor ve olayda işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0016` birebir aynı, `@degisim: mercan -> kazak` (tutuyorsan), ardından `@onarim: 71997050c92d7d03a6fcfe02a54c2f2dd3430841`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0019 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0019
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'fener', fiil 'oturtmak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çantanın kapağı açık kaldı ve kurabiye kutusu düştü | fenerle çadırın içine baktı ve kutuyu buldu
@tohum: hello_kitty-0019
@degisim: gizemli -> küçük
Ağaçlarda kuşlar ötüyordu. Hello Kitty ormandaki kamp yerinde, çadırın hemen önündeydi. Çantasına baktı ama kurabiye kutusu yoktu. Çantanın kapağı açık kalmıştı ve kutu bir yere düşmüştü. Kutuda evde yaptığı yıldız kurabiyeleri vardı. Hello Kitty çantayı az önce çadırın içinde açmıştı. Çadırın içi biraz karanlıktı. Hello Kitty girişteki feneri açtı ve içeri tuttu. Işıkta köşedeki küçük kutuyu gördü. Bu, onun kurabiye kutusuydu! Hello Kitty kutuyu çıkardı ve kapağını açtı. Kurabiyelerin hepsi yerindeydi. Bir kurabiye aldı ve kapağı kutuya geri oturttu. Sonra çadırın önüne oturdu ve kurabiyesini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde, çadırın hemen önündeydi.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormandaki kamp yerinde yanında bir büyük olmadan yalnız.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kapağı kutuya geri oturttu"
   - Cümle 13: «Bir kurabiye aldı ve kapağı kutuya geri oturttu.»
   - Açıklama: 'Oturtmak' kapak için uygun fiil değil; 'kapağı kapattı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0019` birebir aynı, `@degisim: gizemli -> küçük` (tutuyorsan), ardından `@onarim: 6268856e8bb635c832a4613b5388220a3167c27d`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0021 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0021
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'boya', fiil 'değiştirmek', sıfat 'tuzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: rüzgar resim kağıdını alıp yüksek bir dala taktı | annesinden yardım istedi ve annesi kağıdı daldan aldı
@tohum: hello_kitty-0021
@degisim: değiştirmek -> tutmak
Rüzgar hızlı hızlı esiyordu. Hello Kitty parkta boyalarla resim yapıyordu, annesi de tuzlu kraker yiyordu. Birden rüzgar kağıdı havaya kaldırdı ve yüksek bir dala taktı. Hello Kitty zıpladı ama dala uzanamadı. "Anne, kağıdı daldan alır mısın?" diye sordu Hello Kitty. "Hemen alırım," dedi annesi. Annesi uzandı ve kağıdı daldan dikkatlice aldı. Sonra kağıdın bir köşesini sıkıca tuttu. Hello Kitty resmine annesini ve kendisini el ele çizdi. "Anneciğim, bu resim senin, sen benim en iyi arkadaşımsın!" dedi Hello Kitty.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesi de tuzlu kraker yiyordu"
   - Cümle 2: «Hello Kitty parkta boyalarla resim yapıyordu, annesi de tuzlu kraker yiyordu.»
   - Açıklama: Kraker ayrıntısı hiçbir işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgar kağıdı havaya kaldırdı ve yüksek bir dala taktı"
   - Cümle 3: «Birden rüzgar kağıdı havaya kaldırdı ve yüksek bir dala taktı.»
   - Açıklama: Takmak bilinçli bir eylemdir; rüzgar kağıdı dala takmaz, kağıt dala takılır.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra kağıdın bir köşesini sıkıca tuttu"
   - Cümle 8: «Sonra kağıdın bir köşesini sıkıca tuttu.»
   - Açıklama: Kağıdı kimin tuttuğu belirsiz; son özne anne ama resmi Hello Kitty çiziyor.
   - Açıklama: Cümlede özne yok; kağıdı kimin tuttuğu belli değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kağıdın bir köşesini sıkıca tuttu"
   - Cümle 8: «Sonra kağıdın bir köşesini sıkıca tuttu.»
   - Açıklama: Annenin kağıdı tutması işlevsiz ve kimin tuttuğu belirsiz.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen benim en iyi arkadaşımsın"
   - Cümle 10: «"Anneciğim, bu resim senin, sen benim en iyi arkadaşımsın!" dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son repliğe ekleniyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Kartın özellikler alanındaki arkadaş edinme özelliği sorunun çözümünde işe yaramıyor, yalnız son repliğe eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0021` birebir aynı, `@degisim: değiştirmek -> tutmak` (tutuyorsan), ardından `@onarim: ea392d7d8c1b03794067d107966612d17a0dd883`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0022 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0022
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'cetvel', fiil 'denemek', sıfat 'özel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: tabakta iki kardeşe tek bir kurabiye kaldı | kurabiyeyi cetvelle tam ortadan ikiye böldü
@tohum: hello_kitty-0022
@degisim: denemek -> yemek
Evin mutfağında Hello Kitty ile Mimi masadaki tabağa baktı. Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı. İkisi de onu yemek istiyordu, ama tabakta başka kurabiye yoktu. Mimi utangaçtı ve hiçbir şey söylemedi. "Mimi, bu kurabiyeyi seninle paylaşmak istiyorum," dedi Hello Kitty. "İki parça aynı büyüklükte olur mu?" diye sordu Mimi. Hello Kitty kurabiye yapmayı çok severdi ve hamuru hep cetvelle keserdi. Çekmeceden bir cetvel aldı. Cetveli kurabiyenin tam ortasına koydu. Sonra kurabiyeyi cetvelin kenarından yavaşça ikiye kırdı. İki parça tam aynı boydaydı. Hello Kitty bir parçayı Mimi'ye verdi. İki kardeş yan yana oturdu ve parçalarını mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kurabiye yapmayı çok severdi"
   - Cümle 7: «Hello Kitty kurabiye yapmayı çok severdi ve hamuru hep cetvelle keserdi.»
   - Açıklama: Kurabiye yapma özelliği işe yarar biçimde kullanılmıyor, yalnız cetveli gerekçelendirmek için anılıyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "hamuru hep cetvelle keserdi"
   - Cümle 7: «Hello Kitty kurabiye yapmayı çok severdi ve hamuru hep cetvelle keserdi.»
   - Açıklama: Kartın özellikler alanında hamuru cetvelle kesme alışkanlığı yok; uydurma bir bilgi ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0022` birebir aynı, `@degisim: denemek -> yemek` (tutuyorsan), ardından `@onarim: e76e6a6ba9ea92e636f9d6960951f429a9081428`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0024 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0024
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'böğürtlen', fiil 'koparmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: kırmızı böğürtlenler sertti ve daldan çıkmıyordu | annesine sordu ve siyah yumuşak olanları kopardı
@tohum: hello_kitty-0024
@degisim: pürüzsüz -> düz
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Hello Kitty, annesinin evden getirdiği daldan ilk kez böğürtlen koparmayı denedi. Ama kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu. Onları elmalı turtanın üstüne koymak istiyordu. Yaprakların arasında siyah ve yumuşak böğürtlenler de vardı. "Anne, siyah olanları koparabilir miyim?" diye sordu Hello Kitty. "Evet, siyah olanlar daha tatlı," dedi annesi. Hello Kitty siyah bir tanesine hafifçe dokundu ve o hemen koptu. Sonra birkaç tane daha kopardı. Onları turtanın düz üstüne dizdi. "Turtamız çok güzel oldu!" dedi annesi. İkisi gölgeye oturdu ve Hello Kitty'nin en sevdiği turtayı mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesinin evden getirdiği daldan"
   - Cümle 2: «Hello Kitty, annesinin evden getirdiği daldan ilk kez böğürtlen koparmayı denedi.»
   - Açıklama: Evden getirilen dal sebepsiz beliriyor ve ormandaki böğürtlen koparma olayıyla çelişen işlevsiz bir ayrıntı.
   - Açıklama: Böğürtlen dalının evden getirilmesi ormandaki sahneyle anlamsız ve sebepsiz bir ayrıntı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onları elmalı turtanın üstüne"
   - Cümle 4: «Onları elmalı turtanın üstüne koymak istiyordu.»
   - Açıklama: 'Onları' zamiri bir önceki cümledeki koparılamayan kırmızı böğürtlenleri gösteriyor gibi duruyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "turtanın düz üstüne dizdi"
   - Cümle 10: «Onları turtanın düz üstüne dizdi.»
   - Açıklama: 'Düz üstüne' ifadesi doğru anlamda kullanılmamış.
   - Açıklama: 'Düz üstüne' anlamca yanlış ve bozuk bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 26cc81349ddf25331c2ff9aa43e9fa7b832975af`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0025 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0025
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'şampuan', fiil 'erimek', sıfat 'kibar'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: şeker soğuk suda erimedi | kardeşinden kaşık isteyip limonatayı uzun uzun karıştırdı
@tohum: hello_kitty-0025
@degisim: şampuan -> kaşık
Hello Kitty ile Mimi mutfakta ilk kez limonata yapmayı denedi. Büyük bir kaseye soğuk su, limon suyu ve şeker koydular. Ama şeker erimedi ve kasenin dibinde kaldı, çünkü su çok soğuktu. Hello Kitty biraz düşündü. "Mimi, bana uzun bir kaşık verir misin?" diye sordu Hello Kitty. Mimi çekmeceden bir kaşık çıkardı ve ona verdi. Hello Kitty limonatayı kaşıkla uzun uzun karıştırdı. Şeker yavaş yavaş eridi ve limonata tatlı oldu. Hello Kitty iki bardağa limonata koydu. Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı. "Çok güzel olmuş, teşekkürler!" dedi Mimi. Sonra iki kardeş limonatalarını mutlu mutlu içti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty kibar bir arkadaştı"
   - Cümle 10: «Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı.»
   - Açıklama: Mimi onun kardeşi; 'arkadaş' kelimesi yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kibar bir arkadaştı"
   - Cümle 10: «Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı.»
   - Açıklama: Tohumdaki arkadaş özelliği çözüme katkı vermeden etiket olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0025` birebir aynı, `@degisim: şampuan -> kaşık` (tutuyorsan), ardından `@onarim: a300fb590468febd21d3e23fdd5b39447800fd34`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0028 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0028
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kavun', fiil 'sıkılmak', sıfat 'değerli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: ağacın altından garip bir ses geldi | turtasına baktı ve kavuna düşen kozalağı gördü
@tohum: hello_kitty-0028
@degisim: değerli -> küçük
Bir sabah Hello Kitty ormandaki kamp yerinde piknik yapıyordu ve biraz sıkılmıştı. Birden yakındaki bir ağacın altından garip bir ses geldi: tok, tok. Hello Kitty bu sesi çok merak etti. Sepeti de o ağacın altında duruyordu. Sepette kocaman bir kavun ve en sevdiği elmalı turta vardı. Hello Kitty önce turtasına baktı. Turtanın üstünde küçük bir kozalak vardı. Hello Kitty başını kaldırdı ve ağaca baktı. Tam o sırada ağaçtan bir kozalak düştü ve kavuna çarptı: tok! Sesi yapan, düşen kozalaklardı. Hello Kitty kozalağı turtadan aldı ve sepeti açık bir yere çekti. Hello Kitty çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde piknik yapıyordu"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerinde piknik yapıyordu ve biraz sıkılmıştı.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormanda yanında bir büyük olmadan yalnız piknik yapıyor.
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor, ama Hello Kitty ormanda yalnız piknik yapıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "piknik yapıyordu ve biraz sıkılmıştı"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerinde piknik yapıyordu ve biraz sıkılmıştı.»
   - Açıklama: Sıkılma ayrıntısı kuruluyor ama hikayede hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ve biraz sıkılmıştı"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerinde piknik yapıyordu ve biraz sıkılmıştı.»
   - Açıklama: Hello Kitty'nin sıkılmış olması hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0028` birebir aynı, `@degisim: değerli -> küçük` (tutuyorsan), ardından `@onarim: fa28f1b00186f4e96854fa4e1ae88ec7b2cb4355`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0029
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çorba', fiil 'açılmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: rüzgar kapıyı açtı ve kapı kapanmadı | kardeşinden yardım isteyip kapıyı birlikte itti
@tohum: hello_kitty-0029
Hello Kitty ile Mimi mutfakta sıcak çorbalarını içiyordu. Dışarısı çok rüzgarlıydı. Birden kapı rüzgarla açıldı ve içeri soğuk hava doldu. Hello Kitty kaşığını bıraktı ve kapıya gitti. Kapıyı itti, ama rüzgar çok güçlüydü ve kapı kapanmadı. Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı. "Mimi, lütfen bana yardım eder misin?" diye sordu Hello Kitty. Mimi gülümsedi ve hemen kardeşinin yanına koştu. İkisi "Bir, iki, üç!" diye saydı ve kapıyı birlikte itti. Kapı yavaşça kapandı. Mutfak yine sıcacık oldu. İkisi masaya döndü ve çorbalarını bitirdi. "Teşekkürler, Mimi, çok yardımcı oldun!" dedi Hello Kitty.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "en iyi arkadaşı gibi davranırdı"
   - Cümle 6: «Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı.»
   - Açıklama: Soyut bir anlatım; 3 yaşındaki çocuk için somut değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hep en iyi arkadaşı gibi davranırdı"
   - Cümle 6: «Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı.»
   - Açıklama: Benzetmeli ve soyut bir davranış cümlesi, 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kardeşine hep en iyi arkadaşı gibi davranırdı"
   - Cümle 6: «Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı.»
   - Açıklama: Kartın özellikler alanındaki arkadaş özelliği yalnız söylenip geçiliyor, kapıyı kapatma çözümünü doğurmuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kardeşine hep en iyi arkadaşı gibi davranırdı"
   - Cümle 6: «Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı.»
   - Açıklama: Bu özellik cümlesi olay zincirine bir şey katmayan işlevsiz bir ayrıntı.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı"
   - Cümle 6: «Hello Kitty kardeşine hep en iyi arkadaşı gibi davranırdı.»
   - Açıklama: Bu cümle olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0029` birebir aynı, ardından `@onarim: a5428b64a78b1fe8b0f230c4e4b2a37deaa5d449`, sonra gövde.
