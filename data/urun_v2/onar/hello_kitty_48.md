# Editör görevi (onarım): Hello Kitty, onarım partisi 48

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar48.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar48.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0180 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0180
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'valiz', fiil 'alışmak', sıfat 'komik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: valizi yere koyunca komik bir ses geldi | valizi açıp sesi yapan oyuncak topu buldu
@tohum: hello_kitty-0180
Hello Kitty babasıyla ormandaki kamp yerine yeni gelmişti. Babası valizi yere koydu ve içinden komik bir ses geldi. Hello Kitty çok merak etti, çünkü içinde yalnız giysiler vardı. "Baba, bu ses ne?" diye sordu Hello Kitty. "Bilmiyorum, hadi birlikte bakalım," dedi babası. Hello Kitty valizi açtı ve giysileri kaldırdı. En altta küçük bir oyuncak top vardı. Hello Kitty topa bastı ve aynı ses yine geldi. "Onu sana getirdim ama söylemeyi unuttum," dedi babası. Hello Kitty güldü ve bu sese hemen alıştı. "Teşekkürler, baba, top kampta yeni arkadaşım olacak!" dedi Hello Kitty.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "içinden komik bir ses geldi"
   - Cümle 2: «Babası valizi yere koydu ve içinden komik bir ses geldi.»
   - Açıklama: Valizden gelen komik ses yalnız bir merak konusu; hiçbir şey tehlikede değil ve çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bilmiyorum, hadi birlikte bakalım"
   - Cümle 5: «"Bilmiyorum, hadi birlikte bakalım," dedi babası.»
   - Açıklama: Babası sesi bilmediğini söylüyor ama topu kendisinin koyduğunu açıklıyor; bu çelişkili ve sebepsiz kalıyor.
   - Açıklama: Babası sesi bilmediğini söylüyor ama topu kendisi koyduğunu açıklıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu sese hemen alıştı"
   - Cümle 10: «Hello Kitty güldü ve bu sese hemen alıştı.»
   - Açıklama: Sesi ilk kez duyan Hello Kitty için 'alıştı' uygun düşmüyor; kelime yerinde kullanılmamış.
   - Açıklama: 'Alışmak' fiili buraya uymuyor; yeni bulunan komik sese hemen alışmak anlamca tuhaf.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "top kampta yeni arkadaşım olacak"
   - Cümle 11: «"Teşekkürler, baba, top kampta yeni arkadaşım olacak!" dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş özelliği sorunun çözümünde işe yaramıyor, yalnız son cümlede etiket olarak geçiyor.
   - Açıklama: Tohumdaki arkadaş özelliği olayda işe yaramıyor, yalnız son replikte bir oyuncak için anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0180` birebir aynı, ardından `@onarim: 9678d9e6016c549f171dc8bc7fc5dd8f03f5b7e0`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0181 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0181
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'mürekkep', fiil 'oynamak', sıfat 'yırtık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: resim yapacağı tek kağıt ortadan yırtıktı | yırtık kağıdı ikiye bölüp annesine iki resim yaptı
@tohum: hello_kitty-0181
@degisim: mürekkep -> kalem
Parkta kuşlar neşeyle ötüyordu. Hello Kitty ağacın gölgesinde annesine güzel bir resim yapmak istedi. Ama sepetteki tek kağıt bir dala takılıp ortadan yırtılmıştı. Annesi ona sepetten bir kalem verdi. "Bu kağıda da resim yapabilirsin," dedi annesi. Hello Kitty kalemle biraz oynadı ve yırtık kağıda baktı. Sonra kağıdı yırtık yerinden iki parçaya ayırdı. Bir parçaya küçük bir çiçek çizdi. Öbür parçaya gülen bir güneş çizdi. Hello Kitty arkadaşça gülümsedi ve iki resmi de annesine verdi. "Anneciğim, ikisi de senin," dedi Hello Kitty. Annesi resimlere baktı ve Hello Kitty'ye sarıldı. "Teşekkürler, tatlım, bunlar çok güzel!" dedi annesi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sepetteki tek kağıt bir dala takılıp ortadan yırtılmıştı"
   - Cümle 3: «Ama sepetteki tek kağıt bir dala takılıp ortadan yırtılmıştı.»
   - Açıklama: Sepetin içindeki kağıdın dala takılıp yırtılması akla yatkın değil ve annesinin dediği gibi yırtık kağıda yine resim yapılabildiği için sorun zayıf kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty arkadaşça gülümsedi"
   - Cümle 10: «Hello Kitty arkadaşça gülümsedi ve iki resmi de annesine verdi.»
   - Açıklama: Annesine 'arkadaşça' gülümsemek kelimeyi yanlış bağlamda kullanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşça gülümsedi"
   - Cümle 10: «Hello Kitty arkadaşça gülümsedi ve iki resmi de annesine verdi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız süs sıfatı olarak geçiyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0181` birebir aynı, `@degisim: mürekkep -> kalem` (tutuyorsan), ardından `@onarim: e9805bf71b9226fae4570922c2883afc40a51ee4`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0182 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0182
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'ipek', fiil 'içmek', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yiyecek sepetini evde unuttu ve tabaklar boştu | çantasındaki kurabiyeleri çıkarıp tabaklara koydu
@tohum: hello_kitty-0182
@degisim: içmek -> düşünmek
Hello Kitty kamp yerinde babasıyla parti oyunu oynuyordu. Yere ipek bir örtü serdi ve renkli bardakları koydu. Ama babası yiyecek sepetini evde unutmuştu ve tabaklar boştu. "Şimdi ne yiyeceğiz?" diye sordu babası. Hello Kitty biraz düşündü. Birden kendi çantasını hatırladı. Çantada evde birlikte yaptıkları kurabiyeler vardı. Hello Kitty kurabiyeleri çıkardı ve tabaklara tek tek dizdi. Babası bir kurabiye yedi ve gözlerini kapattı. "Bunlar ormandaki en güzel kurabiyeler!" dedi babası. Hello Kitty de bir kurabiye aldı ve babasına gülümsedi. "Baba, partimiz şimdi çok güzel oldu!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden kendi çantasını hatırladı"
   - Cümle 6: «Birden kendi çantasını hatırladı.»
   - Açıklama: Kurabiyeli çanta önceden kurulmadan çözümü getirmek için birden beliriyor.
   - Açıklama: Daha önce hiç kurulmamış çanta ve içindeki kurabiyeler çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0182` birebir aynı, `@degisim: içmek -> düşünmek` (tutuyorsan), ardından `@onarim: 06c75629fafb66a226904d5a07afb760b7125b9d`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0183 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0183
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kek', fiil 'bozulmak', sıfat 'dürüst'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: tabak eğildi ve annesinin keki toprağa düştü | kendi kekini ikiye bölüp yarısını annesine verdi
@tohum: hello_kitty-0183
@degisim: dürüst -> düzgün
Ormandaki kamp yerinde Hello Kitty annesiyle kek partisi oyunu oynuyordu. Hello Kitty iki dilim keki iki tabağa koydu. Ama annesinin tabağı bir taşın üstünde eğildi ve keki toprağa düştü. Kekin şekli bozuldu ve üstü kirlendi. "Kızım, benim kekim nereye gitti?" diye sordu annesi gülerek. Hello Kitty kendi tabağına baktı. Tabakta tek bir düzgün dilim kalmıştı. Hello Kitty dilimi dikkatle ikiye böldü. Büyük yarısını arkadaşça annesinin tabağına koydu. "Al, anneciğim, bu dilim senin," dedi Hello Kitty. Annesi gülümsedi ve Hello Kitty'nin başını okşadı. Kirli keki de birlikte çöpe attılar. Sonra ikisi keklerini yedi ve oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yarısını arkadaşça annesinin tabağına"
   - Cümle 9: «Büyük yarısını arkadaşça annesinin tabağına koydu.»
   - Açıklama: 'Arkadaşça' anneye yapılan davranış için uygun kelime değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Büyük yarısını arkadaşça annesinin"
   - Cümle 9: «Büyük yarısını arkadaşça annesinin tabağına koydu.»
   - Açıklama: 'Arkadaşça' anneye karşı yapılan bir davranış için uygun kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0183` birebir aynı, `@degisim: dürüst -> düzgün` (tutuyorsan), ardından `@onarim: 4dd4f81a2a340edc5ae588a9e5b72478944de9d1`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0184 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0184
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kravat', fiil 'cevaplamak', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: oyuncağın kozalak başı kalın dalın üstünde durmadı | ince bir dala kozalağı sıkıca taktı
@tohum: hello_kitty-0184
@degisim: cevaplamak -> dikmek
Bir sabah Hello Kitty ormandaki kamp yerinde çadırın önündeydi. Oyuncak çantası bomboştu, bu yüzden dallardan oyuncak arkadaşlar yapıyordu. Bir tanesi hazırdı ama öbürünün kozalak başı dalın üstünde durmadı. Dalın ucu çok kalındı ve kozalak hep yere kayıyordu. Hello Kitty o dalı bıraktı ve ince bir dal buldu. Yeni dalı toprağa dikti. Kozalağı dalın ince ucuna sıkıca taktı. Bu kez baş hiç düşmedi. Hello Kitty uzun yeşil bir yapraktan yeni oyuncağa bir kravat yaptı. İki küçük taştan da gözler koydu. Sonra ikisinin arasına oturdu ve gülümsedi. Hello Kitty çok sevindi, çünkü oyuncak arkadaşlarının ikisi de hazırdı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ormandaki kamp yerinde çadırın önündeydi"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerinde çadırın önündeydi.»
   - Açıklama: Hello Kitty ormanda büyüksüz tek başına; güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söyler.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dallardan oyuncak arkadaşlar yapıyordu"
   - Cümle 2: «Oyuncak çantası bomboştu, bu yüzden dallardan oyuncak arkadaşlar yapıyordu.»
   - Açıklama: Kartın 'yeni arkadaşlar edinmeyi sever' özelliği dallardan oyuncak yapmaya çevrilmiş ve iki kez anılmış, işe yarar biçimde kullanılmamış.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "İki küçük taştan da gözler koydu"
   - Cümle 10: «İki küçük taştan da gözler koydu.»
   - Açıklama: 'Taştan' ile 'koymak' uyuşmuyor; 'iki küçük taşı göz yaptı' ya da 'taştan gözler yaptı' olmalı.
   - Açıklama: 'Taştan göz koymak' dilbilgisel olarak aksak; 'iki küçük taştan göz yaptı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0184` birebir aynı, `@degisim: cevaplamak -> dikmek` (tutuyorsan), ardından `@onarim: 3b53b9cc8baf0035c965d45a381e757a7169b0e4`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0186 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0186
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'lastik', fiil 'güzelleşmek', sıfat 'ıslak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: mutfaktan garip bir tık tık sesi geldi | sesin açık pencereden geldiğini bulup pencereyi kapattı
@tohum: hello_kitty-0186
@degisim: güzelleşmek -> kurulamak
Dışarıda yağmur yağıyordu. Hello Kitty ile Mimi odada resim yapıyordu. Birden mutfaktan garip bir tık tık sesi geldi. Mimi yerinden kalkmadı ve kardeşinin elini tuttu. "Gel, Mimi, bu sese birlikte bakalım," dedi Hello Kitty. İkisi yavaşça mutfağa yürüdü. Pencere biraz açıktı ve yağmur damlaları içeri düşüyordu. Damlalar pencerenin önündeki kurabiye kutusuna vuruyordu. Hello Kitty'nin yaptığı kurabiyeler o kutudaydı. Hello Kitty hemen pencereyi kapattı ve ses durdu. Mimi de ıslak kutuyu bir bezle kuruladı. Hello Kitty kutuyu açtı ve içine baktı. Lastik kapak sıkıydı ve kurabiyeler hiç ıslanmamıştı. Hello Kitty çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "mutfaktan garip bir tık tık sesi geldi"
   - Cümle 3: «Birden mutfaktan garip bir tık tık sesi geldi.»
   - Açıklama: Evde gizemli bir ses ve korkan Mimi küçük çocuk için ürkütücü bir öğe.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty'nin yaptığı kurabiyeler o kutudaydı"
   - Cümle 9: «Hello Kitty'nin yaptığı kurabiyeler o kutudaydı.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunun çözümünde işe yaramıyor, yalnız anılıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hello Kitty kutuyu açtı ve içine baktı"
   - Cümle 12: «Hello Kitty kutuyu açtı ve içine baktı.»
   - Açıklama: Ses sorunu pencere kapanınca çözülmüşken kurabiyelerin ıslanıp ıslanmadığı ikinci bir kaygı olarak açılıyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Lastik kapak sıkıydı ve kurabiyeler hiç ıslanmamıştı"
   - Cümle 13: «Lastik kapak sıkıydı ve kurabiyeler hiç ıslanmamıştı.»
   - Açıklama: Ses sorununun yanına kurabiyelerin ıslanıp ıslanmadığı ikinci bir kaygı ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0186` birebir aynı, `@degisim: güzelleşmek -> kurulamak` (tutuyorsan), ardından `@onarim: c3c5133deda4426c47da53d78e2abba0a919d4a7`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0192 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0192
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'değnek', fiil 'parıldamak', sıfat 'şeffaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası çok susadı ama şişesini evde unutmuştu | şeffaf şişedeki suyu babasıyla paylaştı
@tohum: hello_kitty-0192
@degisim: değnek -> şişe
Bir sabah Hello Kitty ile babası ormandaki kamp yerine yürüdü. Babası çok susadı ama su şişesini evde unutmuştu. Hello Kitty çantasından şeffaf şişesini çıkardı. Şişedeki su güneşte parıldadı. "Bu suyu paylaşalım, Baba," dedi Hello Kitty. "Ama bu senin suyun," dedi babası. "Sen benim kamp arkadaşımsın, önce sen iç," dedi Hello Kitty. Babası şişeden üç yudum içti. Sonra komik bir yüz yaptı ve "Oh, ne güzel su!" dedi. Şişeyi gülerek Hello Kitty'ye geri verdi. Hello Kitty de kalan suyu içti. "Teşekkür ederim, kızım, artık hiç susamıyorum!" dedi babası.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sen benim kamp arkadaşımsın"
   - Cümle 7: «"Sen benim kamp arkadaşımsın, önce sen iç," dedi Hello Kitty.»
   - Açıklama: Tohumdaki özellik yeni arkadaşlar edinmek; burada özellik yalnız babaya 'arkadaş' denerek etiket gibi geçiyor, yeni arkadaş edinilmiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "artık hiç susamıyorum"
   - Cümle 12: «"Teşekkür ederim, kızım, artık hiç susamıyorum!" dedi babası.»
   - Açıklama: 'Susamak' durum değişikliği fiili olduğundan burada 'susuzluğum geçti' gibi bir anlatım gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0192` birebir aynı, `@degisim: değnek -> şişe` (tutuyorsan), ardından `@onarim: 44ee8e39e7afdd545cb2b50b11953d13ff0cf014`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0193 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0193
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'pasta', fiil 'küçültmek', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: yapraktan pasta çok yüksek olduğu için devrildi | pastayı küçülttü ve elmalı turta gibi alçak yaptı
@tohum: hello_kitty-0193
Parkta, ağaçların gölgesinde Hello Kitty ile babası evcilik oyunu oynuyordu. Hello Kitty yerdeki yapraklardan babası için uzun bir pasta hazırladı. Ama pasta çok yüksekti, bu yüzden yana devrildi. Yapraklar çimenlerin üstüne dağıldı. Hello Kitty onları yeniden topladı. Bu kez pastayı küçülttü ve ona en sevdiği elmalı turtanın şeklini verdi. Yeni pasta alçak, yuvarlak ve sağlamdı. Hello Kitty üstüne kırmızı yapraklardan elma dilimleri dizdi. Artık pasta hiç devrilmedi. Babası pastaya bakıp sevinçle ellerini çırptı. Sonra baba ile kızı evcilik oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "için uzun bir pasta"
   - Cümle 2: «Hello Kitty yerdeki yapraklardan babası için uzun bir pasta hazırladı.»
   - Açıklama: Yüksek bir pasta için 'uzun' kelimesi yanlış anlamda kullanılmış; plan da 'yüksek' diyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0193` birebir aynı, ardından `@onarim: 0839adebbe7407c0bfc162aa0f750cb3b874e967`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0194 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0194
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'şeker', fiil 'ilerlemek', sıfat 'düzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: mutfaktan gelen garip sesin ne olduğu belli değildi | mutfağa ilerledi ve sesi yapan kağıdı buldu
@tohum: hello_kitty-0194
Rüzgar açık pencereden içeri esiyordu. Hello Kitty mutfaktan gelen garip bir ses duydu. Bu sesin ne olduğunu çok merak etti. Mutfağa doğru yavaş yavaş ilerledi. Masada şeker kutusunun altında bir kağıt vardı. Kağıdın ucu havaya kalkıp iniyor ve masaya vuruyordu. Hello Kitty kağıda yakından baktı. Kağıtta düzgün çizilmiş elmalar ve bir turta resmi vardı. Hello Kitty en sevdiği elmalı turtanın tarifini tanıdı. Hello Kitty tarifi korumak için pencereyi hemen kapattı. Kağıt artık hiç kıpırdamadı. Hello Kitty çok sevindi, çünkü sesi yapan kağıdı bulmuştu.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "mutfaktan gelen garip bir ses"
   - Cümle 2: «Hello Kitty mutfaktan gelen garip bir ses duydu.»
   - Açıklama: Evde yalnız olan figürün garip bir sesin peşine düşmesi küçük çocuk için ürkütücü olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0194` birebir aynı, ardından `@onarim: 5433b5847115e7b6af03b7b9030ffe51b5114bf6`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0196 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0196
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'davul', fiil 'olgunlaşmak', sıfat 'iyi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: kurabiye kutusunun kapağı çok sıkı kapanmıştı | kardeşinden kutuyu tutmasını isteyip kapağı açtı
@tohum: hello_kitty-0196
@degisim: olgunlaşmak -> açmak
Parkta, ağaçların gölgesinde Hello Kitty ile Mimi piknik yapıyordu. Hello Kitty kendi yaptığı kurabiyeleri davul gibi yuvarlak bir kutuya koymuştu. Ama kutunun kapağı çok sıkı kapanmıştı ve açılmadı. Hello Kitty kapağı çekti ama kutu elinden kaydı. "Mimi, kutuyu tutar mısın?" diye sordu Hello Kitty. "Tamam, tutarım," dedi Mimi utangaç bir sesle. Mimi kutuyu sıkıca tuttu. Bu kez Hello Kitty kapağı iki eliyle çekti. Kapak "pat" diye açıldı. Kurabiyeler çok iyi kokuyordu. Hello Kitty en büyük kurabiyeyi Mimi'ye verdi. İki kardeş çok sevindi, çünkü kutuyu birlikte açmışlardı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kendi yaptığı kurabiyeleri"
   - Cümle 2: «Hello Kitty kendi yaptığı kurabiyeleri davul gibi yuvarlak bir kutuya koymuştu.»
   - Açıklama: Güvenli özellik kullanımı satırı kurabiyenin bir büyükle birlikte yapılmasını ister; burada Hello Kitty kurabiyeyi kendi başına yapmış gibi anlatılıyor.
   - Açıklama: Güvenli kullanım satırına göre kurabiye bir büyükle yapılır; burada büyük anılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "davul gibi yuvarlak bir kutuya"
   - Cümle 2: «Hello Kitty kendi yaptığı kurabiyeleri davul gibi yuvarlak bir kutuya koymuştu.»
   - Açıklama: Benzetme kullanılmış; mecaz sayılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0196` birebir aynı, `@degisim: olgunlaşmak -> açmak` (tutuyorsan), ardından `@onarim: 32d6a53572daf975b1b70b1b6a1fb069dcad4ded`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0197 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0197
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'parfüm', fiil 'katlamak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: yağmur yağdığı için parktaki piknik olmadı | evde örtü serip kağıttan kurabiyelerle piknik yaptı
@tohum: hello_kitty-0197
@degisim: parfüm -> örtü
Bir sabah dışarıda çok sert bir yağmur yağıyordu. Hello Kitty parkta piknik yapmak istiyordu ama yağmur yüzünden gidemedi. Pencereden dışarı bakıp biraz üzüldü. Hello Kitty evde piknik yapmaya karar verdi. Piknik örtüsünü getirdi, ikiye katladı ve odanın ortasına serdi. Renkli kalemleri aldı ve kağıtlara kremalı kurabiyeler çizdi. Kurabiyeler kağıtta çok tatlı görünüyordu. Oyuncaklarını da örtünün çevresine oturttu. Her oyuncağın önüne kağıttan bir kurabiye koydu. Sonra Hello Kitty onlarla mutlu mutlu piknik oyunu oynadı.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Piknik örtüsünü getirdi, ikiye katladı ve odanın ortasına serdi"
   - Cümle 5: «Piknik örtüsünü getirdi, ikiye katladı ve odanın ortasına serdi.»
   - Açıklama: Çözüm örtü sermek, kurabiye çizmek, oyuncakları oturtmak ve kurabiye dağıtmak gibi ikiden fazla adıma yayılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kağıtlara kremalı kurabiyeler çizdi"
   - Cümle 6: «Renkli kalemleri aldı ve kağıtlara kremalı kurabiyeler çizdi.»
   - Açıklama: Tohum özelliği kurabiye yapmayı sevmek; kurabiyeler yalnız kağıda çiziliyor, özellik karttaki gibi kullanılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Oyuncaklarını da örtünün çevresine oturttu"
   - Cümle 8: «Oyuncaklarını da örtünün çevresine oturttu.»
   - Açıklama: Çözüm örtü sermek, kurabiye çizmek, oyuncak oturtmak ve kurabiye dağıtmak gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0197` birebir aynı, `@degisim: parfüm -> örtü` (tutuyorsan), ardından `@onarim: 41e7489e69e0a6b3e69d84ffb5b877a9feff10de`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0199 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0199
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kitaplık', fiil 'taramak', sıfat 'kırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesinin yeni turtasını hiç tatmamıştı ve yemek istemedi | turtanın içinde elma görünce bir ısırık aldı
@tohum: hello_kitty-0199
@degisim: kitaplık -> çilek
Rüzgar ağaçların arasında hafif hafif esiyordu. Hello Kitty ile annesi ormandaki kamp yerinde piknik yapıyordu. Hello Kitty annesinin yeni kırmızı turtasını hiç tatmamıştı ve yemek istemedi. "Bu çilekli bir turta, bir dilim dener misin?" diye sordu annesi. Hello Kitty turtayı gözleriyle dikkatle taradı. Kırmızı çileklerin arasında en sevdiği turtadaki elma parçalarını gördü. "Anneciğim, bunun içinde elma da var!" dedi Hello Kitty. "Evet, çileği ve elmayı birlikte koydum," dedi annesi. Elmayı görünce Hello Kitty hemen bir ısırık aldı. Turta hem tatlı hem biraz ekşiydi. Hello Kitty çok mutlu oldu, çünkü yeni turtayı da çok sevmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "turtayı gözleriyle dikkatle taradı"
   - Cümle 5: «Hello Kitty turtayı gözleriyle dikkatle taradı.»
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım ve küçük çocuk için zor.
   - Açıklama: 'Gözleriyle taramak' mecazdır ve 3 yaşındaki çocuk için uygun değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "en sevdiği turtadaki elma parçalarını"
   - Cümle 6: «Kırmızı çileklerin arasında en sevdiği turtadaki elma parçalarını gördü.»
   - Açıklama: 'En sevdiği turtadaki' tamlaması bozuk; elmanın başka bir turtaya ait olduğunu söylüyor, 'en sevdiği elmayı' gibi olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği turtadaki elma parçalarını gördü"
   - Cümle 6: «Kırmızı çileklerin arasında en sevdiği turtadaki elma parçalarını gördü.»
   - Açıklama: Elma parçaları önündeki yeni turtadadır, 'en sevdiği turtadaki' ifadesi anlamca yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0199` birebir aynı, `@degisim: kitaplık -> çilek` (tutuyorsan), ardından `@onarim: fff83f511450a2cae440bb98d0f7e3835da9fdda`, sonra gövde.
