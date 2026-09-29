# Editör görevi (onarım): Örümcek Adam, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Örümcek Adam | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar2.txt --ad urun_v2`
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

## Kart: Örümcek Adam (kaynaklı, kapalı dünya)

- Ad: Örümcek Adam (okunuş: örümcek adam; kesme eki okunuşa uyar)
- Kimlik: Örümcek Adam, arkadaşlarıyla birlikte şehre yardım eden, ağ atabilen genç bir süper kahramandır.
- Tür: kahraman
- Güvenli özellik kullanımı: Ağ ve tırmanma yalnız süper güç olarak kullanılır; çocuğun taklit edebileceği ev içi tırmanma (dolap, masa, pencere, perde) yoktur; 'tehlike' yerine 'bir sorun olduğunu haber verir' yazılır. Kavga ve vurma yoktur.
- Özellikler:
  - ağ: Bileğinden ağ atar. (örnek biçimler: ağ, ağını, ağla)
  - tırman: Duvarlara tırmanabilir. (örnek biçimler: tırmandı, tırmanarak)
  - örümcek hissi: Örümcek hissi bir sorun olduğunu ona haber verir. (örnek biçimler: örümcek hissi)
- Yerler:
  - deniz: Şehrin kumsalı ve limanı.
  - park: Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.
  - ev: Takımın gizli evi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Ghost-Spider: Örümcek Adam'ın ve Spin'in arkadaşı; iyi davul çalar, kostümüyle havada süzülebilir. Tür: kahraman; konuşur. Yüzey biçimleri: Ghost-Spider
  - Spin: Örümcek Adam'ın en iyi arkadaşı; görünmez olabilir, çok güzel resim yapar. Tür: kahraman; konuşur. Yüzey biçimleri: Spin
  - Hulk: Takıma bazen yardım eden kocaman, yeşil ve çok güçlü bir süper kahraman. Tür: kahraman; konuşur. Yüzey biçimleri: Hulk
- Dünya kuralları:
  - 'Tehlike' kelimesi kullanılmaz; örümcek hissi bir sorun olduğunu haber verir.
  - Ev içinde eşyalara tırmanılmaz.
  - 'Üs' kelimesi kullanılmaz (çocuk 'üst' ile karıştırır); takımın yeri 'gizli ev' diye anlatılır.
  - Kavga, yumruk ve dövüş yoktur; sorun yardımla ve ağla çözülür.
- Yasak adlar: Spidey, Peter, Miles, Gwen, Ghosty, May, Rhino, Doc Ock, Goblin, Electro, Black Cat, Sandman, Black Panther, Iron Man, Lizard
- Yasak: Kötü karakterler, robotlar ve dev bilgisayar hikayeye girmez.
- İzinli dünya kelimeleri: ağ, kahraman, tırman, örümcek

## Onarılacak hikâyeler

### Hikâye 1: tohum orumcek_adam-0004 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0004
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'maske', fiil 'bakmak', sıfat 'dürüst'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar maskeyi iki taşın arasındaki boşluğa düşürdü | boşluğa ağ atıp maskeyi yukarı çekti
@tohum: orumcek_adam-0004
@degisim: dürüst -> temiz
Bir sabah Örümcek Adam limanda yürüyordu. Birden rüzgar esti ve yanındaki Ghost-Spider'ın maskesi elinden uçtu. Maske iki taşın arasındaki dar boşluğa, kumun içine düştü. O elini uzattı ama maskeye yetişemedi. Örümcek Adam boşluğa dikkatli bir şekilde baktı. Sonra maskeye ince bir ağ attı. Ağ maskeye yapıştı ve Örümcek Adam maskeyi yavaşça yukarı çekti. Maskeyi arkadaşına verdi. "Maskem temiz mi?" diye sordu arkadaşı. "Evet, üstünde tek bir kum tanesi bile yok," dedi Örümcek Adam. Arkadaşı maskesini taktı ve çok sevindi. Sonra iki arkadaş limanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O elini uzattı"
   - Cümle 4: «O elini uzattı ama maskeye yetişemedi.»
   - Açıklama: 'O' zamirinin Örümcek Adam'ı mı Ghost-Spider'ı mı gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O elini uzattı ama maskeye yetişemedi"
   - Cümle 4: «O elini uzattı ama maskeye yetişemedi.»
   - Açıklama: 'O' zamirinin Örümcek Adam'ı mı Ghost-Spider'ı mı gösterdiği belli değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "üstünde tek bir kum tanesi bile yok"
   - Cümle 10: «"Evet, üstünde tek bir kum tanesi bile yok," dedi Örümcek Adam.»
   - Açıklama: Maske kumun içine düşmüşken üstünde hiç kum olmadığı söyleniyor.
   - Açıklama: Maske kumun içine düştüğü halde üstünde hiç kum olmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0004` birebir aynı, `@degisim: dürüst -> temiz` (tutuyorsan), ardından `@onarim: ac24e60919cc3a7d3987845fdb6704946e61b780`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0005
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kova', fiil 'konuşmak', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: en güzel yaprak uzun bir ağacın dalına takıldı | dala ağ atıp yaprağı yavaşça çekti
@tohum: orumcek_adam-0005
@degisim: konuşmak -> toplamak
Rüzgar hafif hafif esiyordu. Örümcek Adam parkta hazine arama oyunu oynuyordu ve kovasına renkli yapraklar topluyordu. Ama en güzel kırmızı yaprak uzun bir ağacın dalına takılmıştı. Örümcek Adam o yaprağı da kovasına koymak istiyordu. Elini uzattı ama yaprağa yetişemedi. Sonra dala doğru ince bir ağ attı. Ağ kırmızı yaprağa yapıştı. Örümcek Adam ağı yavaşça çekti ve yaprak eline düştü. Yaprağı dikkatli bir şekilde kovasına koydu. Kova artık kırmızı, sarı ve turuncu yapraklarla doluydu. Kovayı iki eliyle havaya kaldırdı. Örümcek Adam çok sevindi, çünkü en güzel hazineyi de bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "en güzel hazineyi de bulmuştu"
   - Cümle 12: «Örümcek Adam çok sevindi, çünkü en güzel hazineyi de bulmuştu.»
   - Açıklama: Kaybolan hazine hiç aranmadığı halde sonda bulunmuş sayılıyor ve yaprakla karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0005` birebir aynı, `@degisim: konuşmak -> toplamak` (tutuyorsan), ardından `@onarim: e2860edde060f6928fd5998dd52fdc6b09422b02`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0006
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kabak', fiil 'bindirmek', sıfat 'enerjik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: kalem kaydı ve kabağa çizilen ağız üzgün göründü | arkadaşından yardım isteyip ağzın iki ucunu yukarı çizdi
@tohum: orumcek_adam-0006
@degisim: bindirmek -> taşımak
Örümcek Adam büyük bir kabağı taşıyarak limanda bir duvara tırmandı. Kabağı duvarın üstüne koydu ve ona gülen bir yüz çizdi. Ama kabak çok yuvarlaktı, kalem kaydı ve ağız üzgün çıktı. Örümcek Adam ağzı düzeltmeye çalıştı ama yapamadı. Sonra aşağıda duran Spin'e baktı. "Spin, bana resimde yardım eder misin?" diye sordu Örümcek Adam. Enerjik Spin hemen duvarın dibine koştu. "Ağzın iki ucunu yukarı doğru çiz," dedi Spin. Örümcek Adam kalemi sıkıca tuttu ve iki küçük çizgi çekti. Kabağın üzgün ağzı birden gülen bir ağız oldu. "Teşekkürler, Spin, artık kabağın gülen bir yüzü var!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "büyük bir kabağı taşıyarak limanda bir duvara tırmandı"
   - Cümle 1: «Örümcek Adam büyük bir kabağı taşıyarak limanda bir duvara tırmandı.»
   - Açıklama: Limanda ağır bir kabakla duvara tırmanma süper güç olarak çerçevelenmeden anlatılıyor ve çocuk taklit edebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "limanda bir duvara tırmandı"
   - Cümle 1: «Örümcek Adam büyük bir kabağı taşıyarak limanda bir duvara tırmandı.»
   - Açıklama: Tohumdaki tırmanma özelliği sorunu çözmüyor; sorun Spin'in resim yardımıyla çözülüyor, tırmanma işe yaramayan bir süs olarak kalıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "büyük bir kabağı taşıyarak limanda bir duvara tırmandı"
   - Cümle 1: «Örümcek Adam büyük bir kabağı taşıyarak limanda bir duvara tırmandı.»
   - Açıklama: Tohumdaki tırmanma özelliği sorunu çözmekte işe yaramıyor, yalnız başta süs olarak geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "büyük bir kabağı taşıyarak limanda bir duvara tırmandı"
   - Cümle 1: «Örümcek Adam büyük bir kabağı taşıyarak limanda bir duvara tırmandı.»
   - Açıklama: Kabağı duvarın üstüne taşıyıp orada çizmek için hiçbir sebep verilmiyor ve bu tırmanış olayda işe yaramıyor.
   - Açıklama: Kabağa resim çizmek için limandaki bir duvara tırmanmanın hiçbir sebebi yok ve bu kurulum olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0006` birebir aynı, `@degisim: bindirmek -> taşımak` (tutuyorsan), ardından `@onarim: 8879260857d5a10b124a277024c4cdca8a17d25f`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0008 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0008
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'paket', fiil 'alışmak', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar kurabiye paketini ince bir duvarın üstüne uçurdu | duvara tırmanıp paketi aldı ve arkadaşına verdi
@tohum: orumcek_adam-0008
@degisim: alışmak -> paylaşmak
Örümcek Adam parkta Hulk ile dağınık yaprakları topluyordu. Birden rüzgar esti ve Hulk'ın kurabiye paketini uçurdu. Paket ince ve uzun bir duvarın üstüne düştü. Hulk'ın eli çok büyüktü ve kurabiyeleri ezebilirdi. "Hulk, üzülme, ben alırım!" dedi Örümcek Adam. Örümcek Adam süper gücüyle duvara tırmandı ve paketi aldı. Sonra paketi elinde tutarak duvardan yavaşça indi. Paketi Hulk'a verdi. "Teşekkürler, Örümcek Adam!" dedi Hulk. Hulk paketi açtı ve kurabiyeleri Örümcek Adam ile paylaştı. İki arkadaş kurabiyelerini yiyip yaprakları toplamaya devam etti. Örümcek Adam çok sevindi, çünkü arkadaşının paketini geri getirmişti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hulk paketi açtı ve kurabiyeleri"
   - Cümle 10: «Hulk paketi açtı ve kurabiyeleri Örümcek Adam ile paylaştı.»
   - Açıklama: Hulk'ın büyük eli kurabiyeleri ezebileceği için paketi alamıyor ama aynı elle paketi açıp kurabiyeleri sorunsuz paylaşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0008` birebir aynı, `@degisim: alışmak -> paylaşmak` (tutuyorsan), ardından `@onarim: 58619991a76f83306c1bf72741da274679f6bef2`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0011 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0011
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar topu çiçeklerin arasına yuvarladı ve top kayboldu | sesin geldiği yere bakıp taşların arasındaki topu buldu
@tohum: orumcek_adam-0011
@degisim: yağ -> top
Rüzgar hafif hafif esiyordu. Örümcek Adam parkta yeşil topuyla oynuyordu. Birden rüzgar topu çiçek bahçesine yuvarladı ve top çiçeklerin arasında kayboldu. Örümcek Adam önce üzüldü, sonra sakinleşti ve dikkatlice dinledi. Çiçeklerin arasından garip bir tık tık sesi geliyordu. Örümcek hissiyle orada bir sorun olduğunu anladı. Sesin ne olduğunu çok merak etti. Çiçeklerin yanına yavaşça yürüdü ve aşağı baktı. Yeşil top iki taşın arasında kalmıştı. Rüzgar estikçe top sallanıyor ve taşlara çarpıyordu. Örümcek Adam topu taşların arasından dikkatlice çıkardı. Örümcek Adam çok sevindi, çünkü garip sesi yapan kayıp topunu bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissiyle orada bir sorun olduğunu anladı"
   - Cümle 6: «Örümcek hissiyle orada bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' soyut kavramlar, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' küçük çocuğa uygun olmayan soyut, deyimsel bir anlatım.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek hissiyle orada bir sorun olduğunu anladı"
   - Cümle 6: «Örümcek hissiyle orada bir sorun olduğunu anladı.»
   - Açıklama: Topun çiçeklere gittiği zaten biliniyorken örümcek hissi yeni bir şey getirmiyor ve olayda işlevsiz kalıyor.
   - Açıklama: Top zaten kayıpken örümcek hissi hiçbir işe yaramayan eklenmiş bir ayrıntı.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam çok sevindi"
   - Cümle 12: «Örümcek Adam çok sevindi, çünkü garip sesi yapan kayıp topunu bulmuştu.»
   - Açıklama: Art arda iki cümle 'Örümcek Adam' ile başlıyor; ad gereksiz tekrarlanıyor.
   - Açıklama: Art arda iki cümle 'Örümcek Adam' ile başlıyor; gereksiz ad tekrarı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0011` birebir aynı, `@degisim: yağ -> top` (tutuyorsan), ardından `@onarim: 6f295ffc9528fd26d8d04964cc2e4079a3e12278`, sonra gövde.
