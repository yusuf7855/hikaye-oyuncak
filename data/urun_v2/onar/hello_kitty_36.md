# Editör görevi (onarım): Hello Kitty, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0128
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kurdele', fiil 'şişirmek', sıfat 'mutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: küçük bir kedi açtı çünkü yerde yiyecek yoktu | sepetten tatlı çıkarıp küçük parçalarını kediye verdi
@tohum: hello_kitty-0128
Bir sabah Hello Kitty ile Mimi parkta piknik yapıyordu. Birden ağacın altında küçük bir kedi gördüler. Kedi tüylerini şişirmişti ve yerde yiyecek arıyordu, ama hiç bulamıyordu. "Bu kedi çok aç galiba," dedi Mimi yavaşça. Hello Kitty sepete baktı. Sepetin kapağı kırmızı bir kurdeleyle bağlıydı. Hello Kitty kurdeleyi çözdü ve en sevdiği elmalı turtayı çıkardı. Onun kenarından küçük parçalar kopardı. Parçaları kedinin yanına, çimenlerin üstüne koydu. Kedi yavaşça geldi ve parçaları yedi. "Bak, Mimi, artık karnı tok!" dedi Hello Kitty. Kedi neşeyle miyavladı. Sonra Hello Kitty ile Mimi pikniğe mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük bir kedi açtı"
   - Cümle 0 (plan satırı): «küçük bir kedi açtı çünkü yerde yiyecek yoktu | sepetten tatlı çıkarıp küçük parçalarını kediye verdi»
   - Açıklama: 'açtı' hem 'aç idi' hem 'bir şeyi açtı' anlamına gelir; plan satırında anlam belirsiz, 'kedi açtı' yerine 'kedi açtı/aç kaldı' ayrımı yapılmalı.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "ağacın altında küçük bir kedi gördüler"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Kartın yanlar bölümünde olmayan bir kedi karakter olaya katılıyor.
   - Açıklama: Başlığın Yan alanında yalnız Mimi var; kedi kartın yanlar bölümünde olmayan ek bir yan karakter.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ağacın altında küçük bir kedi gördüler"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları kartta yok, ama sahipsiz bir kedi olaya katılıyor.
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları ve evcil hayvanlar kapalı dünyada yok.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parçaları kedinin yanına, çimenlerin üstüne koydu"
   - Cümle 9: «Parçaları kedinin yanına, çimenlerin üstüne koydu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yabancı bir sokak hayvanına yaklaşılıp yemek veriliyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parçaları kedinin yanına, çimenlerin"
   - Cümle 9: «Parçaları kedinin yanına, çimenlerin üstüne koydu.»
   - Açıklama: Tanımadığı sokak kedisine yaklaşıp turta yedirmek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0128` birebir aynı, ardından `@onarim: d1c94b159c97d333741ba401e99cd9a07ff7cb12`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0130
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kepçe', fiil 'sokulmak', sıfat 'pahalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi son çorbayı kızına verdi ve kendine yemek kalmadı | tatlısını ikiye bölüp büyük parçayı annesine verdi
@tohum: hello_kitty-0130
@degisim: pahalı -> sıcak
Ormanda serin bir rüzgar esiyordu. Hello Kitty ile annesi kamp yerinde oturmuş, yemek yiyordu. Annesi son kepçe sıcak çorbayı Hello Kitty'ye verdi ve kendine hiç kalmadı. Hello Kitty annesinin boş tabağını gördü. "Anne, senin tabağın boş," dedi Hello Kitty. Çantasında en sevdiği elmalı turtadan bir dilim vardı. Hello Kitty dilimi ikiye böldü. Büyük parçayı annesine uzattı. "Al, anneciğim, birlikte yiyelim," dedi Hello Kitty. Sonra çorbasını da annesiyle paylaştı. Annesi kızını öptü ve gülümsedi. Hello Kitty annesine sokuldu ve ikisi yemeklerini mutlu mutlu bitirdi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "verdi ve kendine hiç kalmadı"
   - Cümle 3: «Annesi son kepçe sıcak çorbayı Hello Kitty'ye verdi ve kendine hiç kalmadı.»
   - Açıklama: Ikinci yan cümlenin öznesi eksik; 'kendine hiç çorba kalmadı' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra çorbasını da annesiyle paylaştı"
   - Cümle 10: «Sonra çorbasını da annesiyle paylaştı.»
   - Açıklama: Turtayı bölüp verdikten sonra çorbayı da paylaşmak çözüme gereksiz bir ek adım katıyor.
   - Açıklama: Turta paylaşıldıktan sonra çorba da paylaşılıyor; çözüm iki adımı aşıyor ve plana eklenmemiş fazladan bir adım içeriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0130` birebir aynı, `@degisim: pahalı -> sıcak` (tutuyorsan), ardından `@onarim: 5da4a512f916b17ba5c3b6180eb6fba00aec1864`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0131 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0131
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'gevrek', fiil 'kapanmak', sıfat 'yapışkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: kutunun kapağı kapanmadı ve hep geri açıldı | annesinden yardım istedi ve annesi kutuya bant yapıştırdı
@tohum: hello_kitty-0131
Mutfakta Hello Kitty parktaki yeni arkadaşları için bir kutu hazırlıyordu. Kutuya annesiyle yaptığı küçük gevrekleri koydu. Ama kutunun kapağı kapanmadı ve hep geri açıldı. Hello Kitty üstüne bastırdı, ama kapak yine açıldı. "Anne, bana yardım eder misin?" diye sordu Hello Kitty. Annesi çekmeceden yapışkan bir bant çıkardı. Bandı kesti ve bir ucunu Hello Kitty'ye verdi. Hello Kitty kapağı sıkıca tuttu. Annesi bandı kutunun üstüne yapıştırdı. Kapak artık kapalı kaldı. Hello Kitty kutuyu iki eliyle kaldırdı ve gülümsedi. "Teşekkürler, anneciğim, şimdi kutum hazır!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parktaki yeni arkadaşları için"
   - Cümle 1: «Mutfakta Hello Kitty parktaki yeni arkadaşları için bir kutu hazırlıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız amaç olarak anılıyor, hikayenin sorununda ya da çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kutunun kapağı kapanmadı ve hep geri açıldı"
   - Cümle 3: «Ama kutunun kapağı kapanmadı ve hep geri açıldı.»
   - Açıklama: Kapağın neden kapanmadığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0131` birebir aynı, ardından `@onarim: 57628ea1f32e0aa90d7fe9feaeda31894691c027`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0132 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0132
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'armut', fiil 'fırçalamak', sıfat 'yaratıcı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası oyunu unutup gülen çizgi olan muzu yedi | turtasından eğri bir parçayı yeni çizgi yaptı
@tohum: hello_kitty-0132
@degisim: fırçalamak -> koymak
Rüzgar hafif esiyordu. Hello Kitty ile babası tabağa meyvelerden gülen komik bir yüz yapıyordu. Ama babası oyunu unuttu ve gülen çizgi olan muzu yedi. Yüzün iki üzüm gözü ve bir armut burnu vardı, ama artık gülmüyordu. "Babacığım, gülen çizgiyi yedin!" dedi Hello Kitty gülerek. "Ah, unuttum!" dedi babası ve o da güldü. Sepette başka muz kalmamıştı. Hello Kitty en çok elmalı turtayı severdi ve sepette onun turtası vardı. Turtasından ince ve eğri bir parça kopardı. Parçayı gözlerin altına, gülen bir çizgi gibi koydu. "Ne yaratıcı bir fikir, kızım!" dedi babası. "Bak babacığım, komik yüz yine gülüyor!" dedi Hello Kitty.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rüzgar hafif esiyordu"
   - Cümle 1: «Rüzgar hafif esiyordu.»
   - Açıklama: Hikaye başlıktaki parkta başladığını hiç göstermiyor; yer kurulmuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sepette onun turtası vardı"
   - Cümle 8: «Hello Kitty en çok elmalı turtayı severdi ve sepette onun turtası vardı.»
   - Açıklama: 'Onun' zamirinin Hello Kitty'yi mi babasını mı gösterdiği belli değil.
   - Açıklama: 'Onun' zamirinin Hello Kitty'yi mi başka birini mi gösterdiği belirsiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepette onun turtası vardı"
   - Cümle 8: «Hello Kitty en çok elmalı turtayı severdi ve sepette onun turtası vardı.»
   - Açıklama: Meyve sepetinde turta sebepsizce beliriyor ve çözümü kolayca getiriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Ne yaratıcı bir fikir, kızım!""
   - Cümle 11: «"Ne yaratıcı bir fikir, kızım!" dedi babası.»
   - Açıklama: 'Yaratıcı' ve 'fikir' soyut kelimelerdir, 3 yaşındaki çocuk bilmez.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ne yaratıcı bir fikir"
   - Cümle 11: «"Ne yaratıcı bir fikir, kızım!" dedi babası.»
   - Açıklama: 'Yaratıcı fikir' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0132` birebir aynı, `@degisim: fırçalamak -> koymak` (tutuyorsan), ardından `@onarim: e550a056bf94567af42dca9851921683461693cb`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0133 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0133
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'nilüfer', fiil 'gerinmek', sıfat 'kapalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: sürpriz için toplanacak çiçekler daha kapalıydı | kurabiyeleri dizip kardeşine bir kalp yaptı
@tohum: hello_kitty-0133
@degisim: nilüfer -> çiçek
Hello Kitty kamp yerinde uyandı, ama Mimi daha çadırda uyuyordu. Kardeşine çiçeklerden bir kalp yapıp sürpriz hazırlamak istedi. Ama sabah serindi ve çiçeklerin hepsi daha kapalıydı. Hello Kitty biraz düşündü. Kurabiye yapmayı çok severdi ve çantasında kendi yaptığı kurabiyeler vardı. Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi. Böylece kocaman bir kalp yaptı. Az sonra Mimi çadırdan çıktı ve gerindi. "Bu kalp ne?" diye sordu Mimi. "Günaydın sürprizi, Mimi, hepsi senin için!" dedi Hello Kitty. Mimi utangaç utangaç gülümsedi ve bir kurabiye aldı. "Teşekkürler, Hello Kitty, bu en güzel sürpriz!" dedi Mimi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çantasında kendi yaptığı kurabiyeler vardı"
   - Cümle 5: «Kurabiye yapmayı çok severdi ve çantasında kendi yaptığı kurabiyeler vardı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle yapılır, burada Hello Kitty kendi başına yapmış gibi anlatılıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle birlikte yapılır.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi"
   - Cümle 6: «Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi.»
   - Açıklama: Çözüm çiçeklerin kapalı olması sebebine yönelmiyor, sorunu başka bir malzemeyle atlatıyor.
   - Açıklama: Çözüm kapalı çiçekler sorununa yönelmiyor, çiçeklerin yerine başka bir şey koyarak sorunu atlıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Mimi utangaç utangaç gülümsedi"
   - Cümle 11: «Mimi utangaç utangaç gülümsedi ve bir kurabiye aldı.»
   - Açıklama: 'Utangaç utangaç' doğal bir ikileme değil; 'utana utana' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0133` birebir aynı, `@degisim: nilüfer -> çiçek` (tutuyorsan), ardından `@onarim: 9ff22d3108956ee5bf4291e342463a6964d63136`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0134
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'posta', fiil 'kırpmak', sıfat 'şık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: yağmur başladı ve kurabiye sepetinin üstü açıktı | sepetin üstünü örtüyle kapatıp ağacın altına koştu
@tohum: hello_kitty-0134
@degisim: posta -> örtü
Yağmur damla damla yağmaya başladı. Hello Kitty parkta çimenlerin üstünde piknik yapıyordu. Sepetinde kendi yaptığı kurabiyeler vardı ve sepetin üstü açıktı. Bir damla burnuna düştü ve Hello Kitty gözlerini kırptı. Hemen şık kırmızı örtüsünü kaldırdı ve sepetin üstünü sıkıca kapattı. Sonra sepeti alıp büyük ağacın altına koştu. Ağacın yaprakları çok sıktı ve altı kuruydu. Hello Kitty örtüyü açtı ve sepete baktı. Kurabiyelerin hepsi kuru ve çıtır çıtırdı. Hello Kitty ağacın altında bir kurabiye yedi ve yağmuru izledi. Hello Kitty çok mutluydu, çünkü kurabiyelerini yağmurdan korumuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sepetinde kendi yaptığı kurabiyeler"
   - Cümle 3: «Sepetinde kendi yaptığı kurabiyeler vardı ve sepetin üstü açıktı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle yapılır; burada kendi başına yaptığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0134` birebir aynı, `@degisim: posta -> örtü` (tutuyorsan), ardından `@onarim: c8f719ef7c1acfe3876db3b4cfc79f2c8490ca34`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0135
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'bambu', fiil 'atlamak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: rüzgar çok gürültülü olduğu için geri gelen sesi duyamadı | rüzgarın durmasını bekledi ve yeniden seslendi
@tohum: hello_kitty-0135
@degisim: bambu -> rüzgar
Rüzgar ormanda hızlı hızlı esiyordu. Hello Kitty ile annesi kamp yerinde oturuyordu. Hello Kitty ağaçlara seslendi ama geri gelen sesi duyamadı. "Anne, sesim neden geri gelmedi?" diye sordu Hello Kitty. "Rüzgar çok gürültülü, o yüzden duyamadın," dedi annesi. Hello Kitty yerinde iki kez atladı. "Sabırsız olma, rüzgar birazdan durur," dedi annesi. Sonra annesinin yanına oturdu ve rüzgarın durmasını bekledi. Biraz sonra orman sessiz oldu. "Benimle arkadaş olur musun?" diye seslendi Hello Kitty. Uzaktan "Olur musun?" diye bir ses geri geldi. Annesi güldü ve kızına sarıldı. Hello Kitty çok sevindi, çünkü sesinin geri geldiğini sonunda duymuştu.
```

**Hakem bulguları (4):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "rüzgar birazdan durur"
   - Cümle 7: «"Sabırsız olma, rüzgar birazdan durur," dedi annesi.»
   - Açıklama: Sebebi de çözümü de annesi söylüyor; Hello Kitty yalnız söyleneni yapıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sabırsız olma, rüzgar birazdan durur"
   - Cümle 7: «"Sabırsız olma, rüzgar birazdan durur," dedi annesi.»
   - Açıklama: Sorunun sebebini de çözümünü de annesi söylüyor; Hello Kitty yalnız onun dediğini yapıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra annesinin yanına oturdu"
   - Cümle 8: «Sonra annesinin yanına oturdu ve rüzgarın durmasını bekledi.»
   - Açıklama: Son konuşan anne olduğu için oturan kişinin kim olduğu belli değil ve Hello Kitty zaten oturuyordu.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Benimle arkadaş olur musun?" diye seslendi"
   - Cümle 10: «"Benimle arkadaş olur musun?" diye seslendi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız yankı denemesi için söyleniyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0135` birebir aynı, `@degisim: bambu -> rüzgar` (tutuyorsan), ardından `@onarim: a3e83aeb29c98c104c53da3affe03256bc4d7773`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0137
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çamaşır', fiil 'şakalaşmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken kardeşinin çamaşırlarını yere düşürdü | özür diledi ve çamaşırları kardeşiyle yeniden katladı
@tohum: hello_kitty-0137
Dışarıda yağmur yağıyordu. Hello Kitty ile en iyi arkadaşı olan ikizi Mimi evde şakalaşıyordu. Hello Kitty koşarken Mimi'nin katladığı çamaşırlara çarptı ve hepsi yere düştü. Mimi yerdeki çamaşırlara baktı ve çok üzüldü. Hello Kitty hemen durdu. Kardeşinin yanına gitti ve ondan özür diledi. Sonra Mimi'ye sıkıca sarıldı. Hello Kitty yumuşak havluları yerden tek tek topladı. Mimi de ona yardım etti. İkisi birlikte bütün çamaşırları yeniden katladı ve sepete koydu. Mimi gülümsedi ve Hello Kitty'nin elini tuttu. Hello Kitty bundan sonra evde koşarken etrafına dikkat etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi evde şakalaşıyordu"
   - Cümle 2: «Hello Kitty ile en iyi arkadaşı olan ikizi Mimi evde şakalaşıyordu.»
   - Açıklama: 'Şakalaşıyordu' 3 yaşındaki çocuk için zor bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşı olan ikizi"
   - Cümle 2: «Hello Kitty ile en iyi arkadaşı olan ikizi Mimi evde şakalaşıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız Mimi'yi tanıtan bir etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0137` birebir aynı, ardından `@onarim: 6f0d3e25dfb071001a9959bd367199ea5fc37490`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0139
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'limon', fiil 'üflemek', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: resmin üstüne küçük sarı şeyler düşüyordu | çiçekleri üfledi ve güneşli bir yere oturdu
@tohum: hello_kitty-0139
Hello Kitty parkta bir ağacın gölgesinde oturuyordu. Yeni arkadaşlarına vermek için kağıda resim çiziyordu. Ama resmin üstüne küçük sarı şeyler düşüyordu. Hello Kitty bunların ne olduğunu çok merak etti. Bir tanesini eline aldı, çok hafif ve yumuşaktı. Sonra başını kaldırıp ağaca baktı. Dallarda limon sarısı küçük çiçekler vardı. Rüzgar esince çiçekler dallardan resmin üstüne düşüyordu. Hello Kitty çiçekleri resmin üstünden yavaşça üfledi. Sonra çimenlerde güneşli bir yere oturdu. Artık resmin üstüne hiç çiçek düşmedi. Hello Kitty resmini çizmeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına vermek için"
   - Cümle 2: «Yeni arkadaşlarına vermek için kağıda resim çiziyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "eline aldı, çok hafif ve yumuşaktı"
   - Cümle 5: «Bir tanesini eline aldı, çok hafif ve yumuşaktı.»
   - Açıklama: Özne Hello Kitty'den çiçeğe belirtilmeden geçiyor; iki cümle virgülle yanlış bağlanmış.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bir tanesini eline aldı, çok hafif"
   - Cümle 5: «Bir tanesini eline aldı, çok hafif ve yumuşaktı.»
   - Açıklama: Özneleri farklı iki cümle virgülle bağlanmış; nokta ile ayrılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0139` birebir aynı, ardından `@onarim: 61600f5e1b7631b816882e1e2f61cfa4400ae1d4`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0140 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0140
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'süpürge', fiil 'yarışmak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: oyunda elmalı turta yapacaktı ama elması yoktu | kozalakları toplayıp taşın üstüne dizdi
@tohum: hello_kitty-0140
@degisim: yarışmak -> toplamak
Rüzgar ağaçların arasında yavaş yavaş esiyordu. Hello Kitty ormandaki kamp yerinde, çadırların yanında yemek oyunu oynuyordu. Oyunda elmalı turta yapacaktı ama hiç elması yoktu. Elma sağlıklı bir meyveydi ve turtaya elma gerekiyordu. Hello Kitty etrafına baktı ve yerde yuvarlak kozalaklar gördü. Kozalaklar küçük elmalara benziyordu. Kuru bir dalı süpürge gibi kullandı ve kozalakları bir yere topladı. Sonra kozalakları düz bir taşın üstüne daire şeklinde dizdi. Taşın üstünde yuvarlak bir kozalak turtası oldu. Hello Kitty turtasına baktı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elma sağlıklı bir meyveydi"
   - Cümle 4: «Elma sağlıklı bir meyveydi ve turtaya elma gerekiyordu.»
   - Açıklama: 'sağlıklı' soyut bir kavram ve olaya bağlı olmayan bilgi cümlesi.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elma sağlıklı bir meyveydi ve turtaya elma gerekiyordu"
   - Cümle 4: «Elma sağlıklı bir meyveydi ve turtaya elma gerekiyordu.»
   - Açıklama: Elmanın gerektiği bir önceki cümlede zaten söylendi; cümle gereksiz tekrar ve konu dışı bilgi taşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma sağlıklı bir meyveydi"
   - Cümle 4: «Elma sağlıklı bir meyveydi ve turtaya elma gerekiyordu.»
   - Açıklama: Elmanın sağlıklı olduğu bilgisi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Elmanın sağlıklı olduğu bilgisi olayda hiçbir işe yaramayan ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0140` birebir aynı, `@degisim: yarışmak -> toplamak` (tutuyorsan), ardından `@onarim: 74cbf0b1124cb07ed832684422bf53761d675b46`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0141
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mont', fiil 'incelemek', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: oyun hamuru çok kuruydu ve kurabiyeler kırılıyordu | hamura biraz su koydu ve yoğurdu
@tohum: hello_kitty-0141
@degisim: mont -> su
Evin mutfağında Hello Kitty oyun hamuruyla oynuyordu. Kahverengi hamurdan çikolatalı kurabiyeler yapacaktı. Ama hamur çok kuruydu ve her kurabiye kırılıyordu. Hello Kitty hamuru dikkatle inceledi. Gerçek kurabiye yaparken de kuru hamura biraz su koyardı. Bir kaşık suyu hamura yavaşça damlattı. Sonra hamuru uzun uzun yoğurdu. Hamur yumuşadı. Hello Kitty hamurdan yuvarlak kurabiyeler yaptı ve hiçbiri kırılmadı. Her kurabiyeye komik bir yüz çizdi. Bir tanesinin burnu çok büyük oldu ve Hello Kitty güldü. Sonra kurabiyeleri tabağa dizdi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bir kaşık suyu hamura"
   - Cümle 6: «Bir kaşık suyu hamura yavaşça damlattı.»
   - Açıklama: Belirsiz miktarla belirtme eki uyumsuz; 'Bir kaşık su' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0141` birebir aynı, `@degisim: mont -> su` (tutuyorsan), ardından `@onarim: 83b366347fee1648cba26b467d48b00afbff96ab`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0142
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'bant', fiil 'paylaşmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: koşarken kardeşinin uçurtmasına bastı ve yırttı | özür diledi ve yırtık yeri bantla yapıştırdı
@tohum: hello_kitty-0142
Hello Kitty ile Mimi parkta uçurtma uçurmaya hazırlanıyordu. Hello Kitty koşarken Mimi'nin kağıt uçurtmasına bastı ve uçurtma yırtıldı. Mimi yırtık uçurtmaya baktı ve çok üzüldü. Hello Kitty hemen kardeşinin yanına oturdu ve ondan özür diledi. Kardeşini sevindirmek için çantasındaki kurabiyeleri Mimi ile paylaştı. Mimi bir kurabiye yedi ve gülümsedi. Mimi'nin çantası her zaman çok düzenliydi. Mimi çantasından bir bant çıkardı ve Hello Kitty'ye verdi. Hello Kitty yırtık yeri bantla dikkatlice yapıştırdı. Rüzgar esince uçurtma yükseldi. Hello Kitty ile Mimi uçurtmayı mutlu mutlu uçurdu.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çantasındaki kurabiyeleri Mimi ile paylaştı"
   - Cümle 5: «Kardeşini sevindirmek için çantasındaki kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Tohum özelliği kurabiye yapmak ama kurabiye yalnız paylaşılıyor ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; kurabiye yalnız paylaşılan atıştırmalık olarak geçiyor ve sorunun çözümünde işe yaramıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kardeşini sevindirmek için çantasındaki kurabiyeleri"
   - Cümle 5: «Kardeşini sevindirmek için çantasındaki kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; özür, kurabiye ve bant ile ikiden fazla adım sürüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasındaki kurabiyeleri Mimi ile paylaştı"
   - Cümle 5: «Kardeşini sevindirmek için çantasındaki kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Kurabiye paylaşımı yırtık uçurtma sorununa hiçbir katkı yapmayan işlevsiz bir ara olay.
   - Açıklama: Kurabiye paylaşımı yırtık uçurtma sorununa yönelmiyor ve çözümde işlevi yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mimi'nin çantası her zaman çok düzenliydi"
   - Cümle 7: «Mimi'nin çantası her zaman çok düzenliydi.»
   - Açıklama: Bandı getirmek için sonradan eklenen bu ayrıntı çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0142` birebir aynı, ardından `@onarim: 629b8aeaa47c2dc1f9fe6215c781a7324efb8066`, sonra gövde.
