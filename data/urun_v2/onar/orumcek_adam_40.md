# Editör görevi (onarım): Örümcek Adam, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0156
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'ağaç', fiil 'karşılaşmak', sıfat 'güzel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar ağaçtaki sürpriz süsleri uçurmak üzereydi | sorunu erken fark edip süsleri sıkıca bağladı
@tohum: orumcek_adam-0156
Bir sabah Örümcek Adam, Ghost-Spider için kumsalda bir ağaca renkli süsler astı. Birden örümcek hissi ile bir sorun olduğunu anladı. Rüzgar esmeye başlamıştı ve süsler dallardan kayıyordu. Örümcek Adam hemen her süsü dallara sıkıca bağladı. Rüzgar yine esti ama hiçbir süs uçmadı. Az sonra arkadaşı havada süzülerek kumsala geldi. İki arkadaş ağacın altında karşılaştı. "Sürpriz!" dedi Örümcek Adam. "Bu ağaç çok güzel olmuş!" dedi arkadaşı sevinçle. İkisi ağacın altına oturup renkli süsleri izledi. Örümcek Adam bundan sonra rüzgarlı günlerde süsleri hep sıkıca bağladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sorunu erken fark edip"
   - Cümle 0 (plan satırı): «rüzgar ağaçtaki sürpriz süsleri uçurmak üzereydi | sorunu erken fark edip süsleri sıkıca bağladı»
   - Açıklama: Plan satırındaki 'sorunu fark etmek' soyut bir ifade.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 2: «Birden örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' 3 yaşındaki çocuk için soyut.
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anlamak' soyut ifadeler; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0156` birebir aynı, ardından `@onarim: f98def580c04ddc0c59c8137d10457f37e04ee72`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0157 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0157
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'küp', fiil 'kucaklamak', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: sarı küp çiçek bahçesinin duvarında kaldı | duvara tırmanıp küpü aldı
@tohum: orumcek_adam-0157
@degisim: ferah -> geniş
Örümcek Adam parkın geniş oyun alanında yumuşak renkli küplerle oynuyordu. Küpleri havaya atıp tek tek tutuyordu. Ama sarı küp fazla yükseğe gitti ve çiçek bahçesinin duvarında kaldı. Sonra Örümcek Adam süper gücüyle, elleri duvara yapışarak tırmandı. Sarı küpü aldı ve yavaşça aşağı indi. Küpü iki koluyla sıkıca kucakladı. Bu kez küpleri daha alçaktan atmaya başladı. Kırmızı, mavi ve sarı küpler havada dönüyordu. Hepsi onun ellerine düşüyordu. Örümcek Adam çok mutluydu, çünkü sarı küpünü geri almıştı.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "yumuşak renkli küplerle"
   - Cümle 1: «Örümcek Adam parkın geniş oyun alanında yumuşak renkli küplerle oynuyordu.»
   - Açıklama: Sıfatlar arasında virgül olmadığından 'yumuşak renkli' pastel renk anlamına kayıyor; 'yumuşak, renkli' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küpleri daha alçaktan atmaya"
   - Cümle 7: «Bu kez küpleri daha alçaktan atmaya başladı.»
   - Açıklama: 'Alçaktan atmak' alçak bir yerden atmak demektir; kastedilen küpleri daha alçağa atmak.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0157` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 99522bf6ccd4aca30b44fa526bcd5d70fccfbeae`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0158 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0158
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tabure', fiil 'hazırlanmak', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: tabure ıslak kuma batıp yana eğiliyordu | sorunu fark edip tabureyi kuru kuma taşıdı
@tohum: orumcek_adam-0158
Örümcek Adam kumsalda gemi oyununa hazırlanıyordu. Suyun kenarına bir tabure koydu ve üstüne turuncu bir havlu astı. Ama tabure yumuşak, ıslak kuma batıyordu ve yana eğiliyordu. Oturmadan önce Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. Tabureyi kaldırdı ve kuru, sert kuma taşıdı. Tabure artık dimdik duruyordu. Örümcek Adam tabureye oturdu. Turuncu havluyu yelken gibi iki eliyle tuttu. Rüzgar esti ve havlu şişti. Örümcek Adam denizdeki gemilere el salladı. Örümcek Adam çok sevindi, çünkü gemi oyununu kuru kumda rahatça oynuyordu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üstüne turuncu bir havlu astı"
   - Cümle 2: «Suyun kenarına bir tabure koydu ve üstüne turuncu bir havlu astı.»
   - Açıklama: Taburenin üstüne havlu asılmaz, serilir; fiil yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 4: «Oturmadan önce Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissi ile"
   - Cümle 4: «Oturmadan önce Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun bilmediği soyut bir kavram.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam denizdeki gemilere el salladı. Örümcek Adam çok sevindi"
   - Cümle 10: «Örümcek Adam denizdeki gemilere el salladı.»
   - Açıklama: Ad art arda iki cümlede gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0158` birebir aynı, ardından `@onarim: d434ef57f953be5d0d8da9f69bfc92cff133033e`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0159 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0159
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yelkenli', fiil 'dinlenmek', sıfat 'sıcak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: rüzgar kağıt yelkenliyi yüksek bir duvarın üstüne uçurdu | duvara tırmanıp yelkenliyi aldı ve verdi
@tohum: orumcek_adam-0159
Limanda sıcak bir rüzgar esiyordu. Hulk ile Örümcek Adam kumda oturup dinleniyordu. Hulk, Örümcek Adam'a küçük kağıt yelkenlisini gösterdi. Birden rüzgar hızlandı ve hafif yelkenliyi bir duvarın üstüne uçurdu. "Duvar benden bile yüksek!" dedi Hulk. "Üzülme, Hulk, ben onu alırım," dedi Örümcek Adam. Örümcek Adam süper gücüyle duvara hızla tırmandı. Yelkenliyi alıp dikkatle aşağı indi ve onu Hulk'a verdi. "Teşekkürler, Örümcek Adam!" dedi Hulk ve güldü. Sonra suyun kenarına gittiler. Hulk yelkenliyi suya bıraktı. Örümcek Adam ile Hulk yelkenliyle mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden rüzgar hızlandı ve hafif yelkenliyi"
   - Cümle 4: «Birden rüzgar hızlandı ve hafif yelkenliyi bir duvarın üstüne uçurdu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0159` birebir aynı, ardından `@onarim: ba47e1a68320fa5160adbff43743dba3ba5d4925`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0161
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'jöle', fiil 'girmek', sıfat 'yorgun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar topu denizde uzak bir yere sürükledi | yardım isteyip ağla topu kıyıya çekti
@tohum: orumcek_adam-0161
@degisim: jöle -> top
Bir sabah Örümcek Adam ile Ghost-Spider kumsalda top oynuyordu. Birden rüzgar esti ve topu denizde uzağa sürükledi. Örümcek Adam suya girmedi, çünkü su derindi. Ama top dalgaların arasında kayboldu ve Örümcek Adam onu göremedi. "Bana yardım eder misin?" diye sordu Örümcek Adam arkadaşına. "Tabii," dedi arkadaşı. Arkadaşı kostümüyle kumun üstünde biraz süzüldü ve topu gördü. Sonra eliyle sağ tarafı gösterdi. Örümcek Adam o tarafa bir ağ attı. Ağ topu sardı ve Örümcek Adam topu yavaşça kumsala çekti. İki arkadaş yorgun ama mutlu, kuma oturdu. Örümcek Adam çok sevindi, çünkü arkadaşından yardım istemişti ve top geri gelmişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kostümüyle kumun üstünde biraz süzüldü"
   - Cümle 7: «Arkadaşı kostümüyle kumun üstünde biraz süzüldü ve topu gördü.»
   - Açıklama: Kumun üstünde 'süzülmek' fiili yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumun üstünde biraz süzüldü"
   - Cümle 7: «Arkadaşı kostümüyle kumun üstünde biraz süzüldü ve topu gördü.»
   - Açıklama: 'Süzülmek' kum üstünde duran bir kişiye uygun değil; fiil öznesine uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşı kostümüyle kumun üstünde biraz süzüldü"
   - Cümle 7: «Arkadaşı kostümüyle kumun üstünde biraz süzüldü ve topu gördü.»
   - Açıklama: Ghost-Spider'ın kostümüyle süzülmesi sebepsiz beliriyor ve topu nasıl gördüğünü açıklamıyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "İki arkadaş yorgun ama mutlu, kuma oturdu"
   - Cümle 11: «İki arkadaş yorgun ama mutlu, kuma oturdu.»
   - Açıklama: Ara söz iki virgülle ayrılmalı: 'İki arkadaş, yorgun ama mutlu, kuma oturdu.'

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0161` birebir aynı, `@degisim: jöle -> top` (tutuyorsan), ardından `@onarim: 02399baa23d9b040d75439f7db8285d2cf8f1edf`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0162 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0162
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'koni', fiil 'gıdıklamak', sıfat 'şekerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: halka koniye değil duvarın tepesine uçtu | duvara tırmanıp halkayı getirdi
@tohum: orumcek_adam-0162
@degisim: şekerli -> turuncu
Örümcek Adam ile Spin kumsalda halkaları turuncu bir koniye atıyordu. Sıra Örümcek Adam'a gelince uçan bir tüy burnunu gıdıkladı. Örümcek Adam çok güldü ve halka koniye değil, limanın duvarına uçtu. Halka duvarın tepesinde kaldı. "Eyvah, halka orada kaldı!" dedi Spin. Örümcek Adam süper gücüyle duvara hızla tırmandı. Halkayı aldı ve yavaşça aşağı indi. Sonra halkayı dikkatle koniye attı. Halka tam koniye geçti. "Çok güzel attın, Örümcek Adam!" dedi Spin ve alkışladı. Örümcek Adam çok sevindi, çünkü halka sonunda koniye geçmişti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "halka sonunda koniye geçmişti"
   - Cümle 11: «Örümcek Adam çok sevindi, çünkü halka sonunda koniye geçmişti.»
   - Açıklama: Halkanın koniye geçtiği bir önceki anlatım cümlesinde söylendi; son cümlede gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0162` birebir aynı, `@degisim: şekerli -> turuncu` (tutuyorsan), ardından `@onarim: 5304055191190f97f0b9c62f9fb9046e5e0f3530`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0163
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'nilüfer', fiil 'vedalaşmak', sıfat 'bol'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: rüzgar şemsiyeyi yüksek bir duvarın tepesine uçurdu | duvara tırmanıp şemsiyeyi geri aldı
@tohum: orumcek_adam-0163
@degisim: nilüfer -> şemsiye
Örümcek Adam limanda Hulk ile vedalaştı. Birden gökten bol bol yağmur yağmaya başladı. Hulk kocaman şemsiyesini açtı ama rüzgar onu uçurdu. Şemsiye limanda yüksek bir duvarın tepesine takıldı. Hulk uzandı ama yetişemedi. "Şemsiyem gitti!" dedi Hulk üzgün üzgün. "Üzülme, Hulk, ben alırım," dedi Örümcek Adam. Örümcek Adam ıslak duvara kolayca tırmandı. Şemsiyeyi tepeden aldı ve yavaşça aşağı indi. Sonra şemsiyeyi açıp Hulk'a verdi. Hulk şemsiyenin altına girdi ve güldü. "Teşekkürler, Örümcek Adam, şimdi kuru kuru gidebilirim!" dedi Hulk.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "limanda Hulk ile vedalaştı"
   - Cümle 1: «Örümcek Adam limanda Hulk ile vedalaştı.»
   - Açıklama: 'Vedalaştı' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şimdi kuru kuru gidebilirim"
   - Cümle 12: «"Teşekkürler, Örümcek Adam, şimdi kuru kuru gidebilirim!" dedi Hulk.»
   - Açıklama: 'Kuru kuru' ikilemesi burada 'ıslanmadan' anlamında doğal kullanılmıyor.
   - Açıklama: 'kuru kuru gitmek' doğal bir kullanım değil; ıslanmadan gitmek anlamını karşılamıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0163` birebir aynı, `@degisim: nilüfer -> şemsiye` (tutuyorsan), ardından `@onarim: d21cd9f5620f75b76f7cab2cc16abd0fae81461b`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0164
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'palmiye', fiil 'alkışlamak', sıfat 'rengarenk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: koşarken uçan kumlar arkadaşının kalesini örttü | fark edip özür diledi ve kaleyi temizledi
@tohum: orumcek_adam-0164
Bir sabah Örümcek Adam kumsalda hızlı hızlı koşuyordu. Uçan kumlar, Ghost-Spider'ın palmiye altındaki rengarenk kalesine döküldü. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam durdu ve arkasına baktı. Kalenin kabukları kumun altında kalmıştı. Arkadaşı kalesine üzgün üzgün bakıyordu. "Özür dilerim, koşarken kumu ben döktüm," dedi Örümcek Adam. Sonra kalenin yanına oturdu. Kumları elleriyle yavaşça temizledi. Kabuklar yeniden güneşte parladı. Arkadaşı gülümsedi ve onu alkışladı. "Teşekkürler, Örümcek Adam, kalem yine çok güzel!" dedi arkadaşı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "koşarken uçan kumlar arkadaşının"
   - Cümle 0 (plan satırı): «koşarken uçan kumlar arkadaşının kalesini örttü | fark edip özür diledi ve kaleyi temizledi»
   - Açıklama: 'Koşarken' zarf-fiilinin öznesi ile ana cümlenin öznesi (kumlar) uyuşmuyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ghost-Spider'ın palmiye altındaki rengarenk"
   - Cümle 2: «Uçan kumlar, Ghost-Spider'ın palmiye altındaki rengarenk kalesine döküldü.»
   - Açıklama: Tamlama eki eksik; 'palmiyenin altındaki' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk anlamaz.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kalem yine çok güzel"
   - Cümle 12: «"Teşekkürler, Örümcek Adam, kalem yine çok güzel!" dedi arkadaşı.»
   - Açıklama: 'Kalem' (kale + -m) çocuk tarafından yazı kalemi olarak anlaşılabilecek belirsiz bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0164` birebir aynı, ardından `@onarim: 8df4b399cfc4b61bb4e43bf5c00c47e70c111b6d`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0165
- yer: ev (Takımın gizli evi.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kartopu', fiil 'saklanmak', sıfat 'kırık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: rüzgar kilidi kırık kapıyı açtı ve kar girdi | arkadaşından yardım isteyip kapıya kutu koydu
@tohum: orumcek_adam-0165
Kar yağarken Örümcek Adam ile Hulk gizli evde saklambaç oynuyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Rüzgar, kilidi kırık kapıyı açmıştı ve içeri kar giriyordu. Hulk saklandığı kocaman kutunun arkasından çıktı. Örümcek Adam kapıyı hemen kapattı. "Hulk, bu kutuyu kapının önüne iter misin?" diye sordu Örümcek Adam. Hulk kutuyu kolayca itti. Rüzgar esti ama kapı bu kez açılmadı. Örümcek Adam yerdeki kardan küçük bir kartopu yaptı ve Hulk'a verdi. Hulk onu eline alıp güldü. Örümcek Adam bundan sonra karlı günlerde kutuyu hep kapının önünde tuttu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
   - Açıklama: Hissin haber vermesi mecaz, 'sorun' da soyut bir kavram.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "örümcek hissi ona bir"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Ona' zamirinin Örümcek Adam'ı mı Hulk'u mu gösterdiği belli değil.
   - Açıklama: Önceki cümlede iki kişi geçtiği için 'ona' zamirinin kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0165` birebir aynı, ardından `@onarim: 12835a50294bc7b0a59ca605141609e135660876`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0166
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'yonca', fiil 'yapıştırmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: rüzgar kağıt geminin narin yelkenini kopardı | yelkeni ağla gemiye yapıştırdı
@tohum: orumcek_adam-0166
@degisim: yonca -> gemi
Rüzgar kumsalda hafif hafif esiyordu. Örümcek Adam ilk kez kağıttan bir gemi yapmıştı ve Spin onu izliyordu. Ama rüzgar esince geminin narin yelkeni koptu ve kuma düştü. "Yelkeni olmayan gemi gitmez," dedi Spin. Örümcek Adam yelkeni kumdan aldı. Biraz ağ attı ve yelkeni gemiye yapıştırdı. Yelken bu kez sıkıca durdu. Örümcek Adam gemiyi suyun kenarına, sığ suya bıraktı. Rüzgar esti ve gemi kıyıda yavaşça ilerledi. Spin sevinçle ellerini çırptı. "Bak, Spin, ilk gemim yüzüyor!" dedi Örümcek Adam.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geminin narin yelkenini kopardı"
   - Cümle 0 (plan satırı): «rüzgar kağıt geminin narin yelkenini kopardı | yelkeni ağla gemiye yapıştırdı»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kağıt geminin narin yelkenini"
   - Cümle 0 (plan satırı): «rüzgar kağıt geminin narin yelkenini kopardı | yelkeni ağla gemiye yapıştırdı»
   - Açıklama: Plan satırında da 'narin' kelimesi geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geminin narin yelkeni koptu"
   - Cümle 3: «Ama rüzgar esince geminin narin yelkeni koptu ve kuma düştü.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0166` birebir aynı, `@degisim: yonca -> gemi` (tutuyorsan), ardından `@onarim: 322bdb126f45fd6e141ee9d62a9d411dc633b927`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0167 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0167
- yer: ev (Takımın gizli evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'duvar', fiil 'anlamak', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: duvarın yukarısından bilinmeyen bir tık tık sesi geldi | duvara tırmanıp açık kapağı kapattı
@tohum: orumcek_adam-0167
@degisim: saygılı -> yüksek
Bir sabah Örümcek Adam gizli evde sessizce oturuyordu. Birden duvarın yukarısından tık tık diye bir ses geldi. Örümcek Adam sesin nereden geldiğini anlamak istedi. Ayağa kalktı ve dikkatle dinledi. Ses çok yüksekten, tavanın yanından geliyordu. Örümcek Adam duvara kolayca tırmandı. Tavanın yanında küçük bir pencere vardı. Pencerenin kapağı açık kalmıştı ve rüzgarda duvara vuruyordu. Tık tık sesini bu kapak çıkarıyordu. Örümcek Adam kapağı sıkıca kapattı ve ses durdu. Sonra yavaşça aşağı indi. Örümcek Adam bundan sonra küçük pencerenin kapağını hep kapalı tuttu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bilinmeyen bir tık tık"
   - Cümle 0 (plan satırı): «duvarın yukarısından bilinmeyen bir tık tık sesi geldi | duvara tırmanıp açık kapağı kapattı»
   - Açıklama: 'Bilinmeyen' soyut bir kelimedir; 3 yaşındaki çocuk bilmeyebilir.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara kolayca tırmandı"
   - Cümle 6: «Örümcek Adam duvara kolayca tırmandı.»
   - Açıklama: Güvenli özellik kullanımı satırına aykırı olarak ev içinde pencereye ulaşmak için tırmanılıyor ve bu çocuğun taklit edebileceği biçimde yazılmış.
   - Açıklama: Güvenli özellik kullanımı satırı ev içi tırmanmayı yasaklıyor; gizli evin içinde tavandaki pencereye kadar tırmanma çocuğun taklit edebileceği bir yükseğe tırmanma örneği oluyor.
3. **K5** (K merceği) — Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
   - Alıntı: "Örümcek Adam duvara kolayca tırmandı"
   - Cümle 6: «Örümcek Adam duvara kolayca tırmandı.»
   - Açıklama: Dünya kuralı ev içinde tırmanmayı yasaklıyor; gizli evin içinde tavandaki pencereye tırmanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0167` birebir aynı, `@degisim: saygılı -> yüksek` (tutuyorsan), ardından `@onarim: 4de60ab6796b0920cce77cc7f647ad287110ee3c`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0168 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0168
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'mektup', fiil 'kurtarmak', sıfat 'uslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar topu yüksek bir duvarın tepesine taşıdı | duvara tırmanıp topu kurtardı
@tohum: orumcek_adam-0168
@degisim: mektup -> top
Örümcek Adam ile Hulk parkta sırayla top atıp tutuyordu. Sıra Hulk'taydı ve Hulk topu yukarı attı. Ama rüzgar topu çiçek bahçesinin yüksek duvarına taşıdı. Top duvarın tepesinde kaldı. Hulk uzandı ama yetişemedi. Örümcek Adam duvara kolayca tırmandı ve topu kurtardı. Hulk bu sırada aşağıda uslu uslu bekledi. Örümcek Adam aşağı indi. Sonra topu Hulk'a verdi, sıra yine ondaydı. Hulk bu kez topu yavaşça attı. Örümcek Adam onu tuttu ve geri attı. Örümcek Adam ve Hulk sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara kolayca tırmandı"
   - Cümle 6: «Örümcek Adam duvara kolayca tırmandı ve topu kurtardı.»
   - Açıklama: Yüksek duvara tırmanma süper güç olarak belirtilmeden sıradan bir top kurtarma yolu gibi sunuluyor; güvenli özellik kullanımı satırına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0168` birebir aynı, `@degisim: mektup -> top` (tutuyorsan), ardından `@onarim: cfc8b0e9563a6e2067dba3cc7a4ebbf6710173ad`, sonra gövde.
