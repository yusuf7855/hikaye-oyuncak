# Editör görevi (onarım): Örümcek Adam, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0041 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0041
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'domates', fiil 'basmak', sıfat 'ufak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: rüzgar arkadaşının resmini duvarın tepesine uçurdu | duvara tırmanıp resmi aldı ve arkadaşına verdi
@tohum: orumcek_adam-0041
Rüzgar hızlı hızlı esiyordu. Spin limanda ufak domatesler çiziyordu ve Örümcek Adam onu izliyordu. Birden rüzgar Spin'in kağıdını uçurdu ve yüksek bir duvarın tepesine bıraktı. "Resmim gitti!" dedi Spin üzgün üzgün. "Üzülme, Spin, ben getiririm," dedi Örümcek Adam. Örümcek Adam duvara hızla tırmandı. Duvarın kenarına dikkatle bastı ve kağıdı aldı. Sonra aşağı indi ve resmi Spin'e verdi. "Teşekkürler, Örümcek Adam!" dedi Spin sevinçle. Spin bundan sonra rüzgarlı havada kağıdın üstüne bir taş koydu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Spin bundan sonra rüzgarlı"
   - Cümle 10: «Spin bundan sonra rüzgarlı havada kağıdın üstüne bir taş koydu.»
   - Açıklama: 'Bundan sonra' süreklilik ister, tek seferlik 'koydu' ile uyumsuz; 'koymaya başladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0041` birebir aynı, ardından `@onarim: a079a0f6f6dd467a7f1ad1e52a745ea7ab27f063`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0042
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tuz', fiil 'eğmek', sıfat 'hazır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: arkadaşı salıncağa binmek için arkada sessizce bekliyordu | arkasına baktı ve sırayı arkadaşına verdi
@tohum: orumcek_adam-0042
@degisim: tuz -> salıncak
Parkın oyun alanında tek bir salıncak vardı. Örümcek Adam salıncakta uzun uzun sallanıyordu. Hulk da binmek istiyordu ama arkada sessizce bekliyordu. Birden Örümcek Adam örümcek hissiyle arkasında Hulk'ın beklediğini anladı. Örümcek Adam arkasına baktı ve arkadaşını gördü. Hulk başını eğmişti ve biraz üzgündü. Örümcek Adam hemen salıncaktan indi. "Sıra sende, Hulk! On kere sallan, sonra sıra bende," dedi Örümcek Adam. Hulk sevindi ve salıncağa oturdu. Örümcek Adam yüksek sesle saydı. Sonra yer değiştirdiler. "Hazır mısın, Örümcek Adam?" diye sordu Hulk ve o da saydı. İkisi sırayla sallandı ve çok güldü. "Sırayla oynamak çok eğlenceli, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissiyle"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle arkasında Hulk'ın beklediğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavramdır, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "diye sordu Hulk ve o da saydı"
   - Cümle 13: «"Hazır mısın, Örümcek Adam?" diye sordu Hulk ve o da saydı.»
   - Açıklama: 'o' zamirinin Hulk'u mu Örümcek Adam'ı mı gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0042` birebir aynı, `@degisim: tuz -> salıncak` (tutuyorsan), ardından `@onarim: bbf8609872c05598278007ec922e2086fea36bce`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0044
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gül', fiil 'aydınlanmak', sıfat 'sıkı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar kum gemisinin bayrağını düşürmek üzereydi | çubuğu tuttu ve kuma daha derine soktu
@tohum: orumcek_adam-0044
@degisim: gül -> bayrak
Kumsalda güçlü bir rüzgar esiyordu ve gökyüzünde bulutlar vardı. Örümcek Adam kumdan bir gemi yapmıştı ve gemi oyunu oynuyordu. Birden örümcek hissi ile bayrağın düşeceğini anladı. Bayrağın çubuğu kumda sağa sola eğiliyordu. Örümcek Adam çubuğu hemen tuttu. Onu kuma daha derine soktu. Çubuk artık kumda sıkı kaldı. Rüzgar yine esti ama bayrak düşmedi. Az sonra rüzgar bulutları götürdü ve kumsal aydınlandı. Örümcek Adam gemisinin önüne oturdu ve gülümsedi. Kırmızı bayrak rüzgarda sallanıyordu. Örümcek Adam çok mutluydu, çünkü gemisinin bayrağı yine yerinde duruyordu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bayrağın düşeceğini anladı"
   - Cümle 3: «Birden örümcek hissi ile bayrağın düşeceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; küçük çocuk için somut değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ile"
   - Cümle 3: «Birden örümcek hissi ile bayrağın düşeceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir ifade.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çubuk artık kumda sıkı kaldı"
   - Cümle 7: «Çubuk artık kumda sıkı kaldı.»
   - Açıklama: 'Sıkı kalmak' çubuk için doğru anlamda değil; 'sıkıca durdu' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Az sonra rüzgar bulutları götürdü"
   - Cümle 9: «Az sonra rüzgar bulutları götürdü ve kumsal aydınlandı.»
   - Açıklama: Bulutların gidip kumsalın aydınlanması sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0044` birebir aynı, `@degisim: gül -> bayrak` (tutuyorsan), ardından `@onarim: b634f0e1a2be4b15e01ea4a1361caaa963f14c8e`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0046
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tekne', fiil 'kaybetmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar hafif tekneleri çalıya doğru itiyordu | tekneleri rüzgarın geldiği yerden suya bıraktı
@tohum: orumcek_adam-0046
@degisim: zarif -> hafif
Bir sabah parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider bir su birikintisinde kağıt tekne yarışı yapıyordu. Birden Örümcek Adam örümcek hissi ile teknelerin çalıya gideceğini anladı. Rüzgar hafif tekneleri suyun kenarındaki çalıya doğru itiyordu. Örümcek Adam tekneleri çalıda kaybetmek istemedi. Hemen iki tekneyi de sudan aldı. Onları suyun öbür kenarına götürdü ve suya bıraktı. Şimdi rüzgar tekneleri çalıdan uzağa itti. Yarışta arkadaşının teknesi daha hızlı gitti. Arkadaşı sevinçle güldü. Örümcek Adam yarışı kaybetti ama o da güldü. Örümcek Adam bundan sonra tekneleri hep rüzgarın geldiği yerden suya bıraktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissi ile"
   - Cümle 3: «Birden Örümcek Adam örümcek hissi ile teknelerin çalıya gideceğini anladı.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki bir çocuğun bilmediği soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile teknelerin"
   - Cümle 3: «Birden Örümcek Adam örümcek hissi ile teknelerin çalıya gideceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şimdi rüzgar tekneleri çalıdan uzağa itti"
   - Cümle 8: «Şimdi rüzgar tekneleri çalıdan uzağa itti.»
   - Açıklama: Rüzgarın yönü değişmediği için rüzgarın geldiği yerden bırakılan tekneler yine çalıya doğru itilmeli, çalıdan uzağa değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0046` birebir aynı, `@degisim: zarif -> hafif` (tutuyorsan), ardından `@onarim: 04584e77e1a5c0169aeaf29ea2769a5b20fca5cc`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0047
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: kaybolan eşya
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'salıncak', fiil 'taşmak', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar siyah kovayı yuvarladı ve kova kayboldu | kumdaki izi takip etti ve kovayı buldu
@tohum: orumcek_adam-0047
@degisim: salıncak -> kova
Örümcek Adam kumsalda kumdan bir kale yapıyordu. O sırada rüzgar siyah kovasını yuvarladı ve uzağa götürdü. Örümcek Adam bunu görmedi ama örümcek hissiyle hemen yanına baktı. Kovası yoktu. Sonra kumda uzun bir iz gördü. Örümcek Adam izi yavaş yavaş takip etti. İz onu suyun kenarına götürdü. Siyah kova orada, kumun üstünde yatıyordu. Kova deniz suyuyla dolmuştu ve su kovadan taşmıştı. Örümcek Adam kovayı aldı ve kalesinin yanına geri döndü. Kovadaki suyu kuma döktü. Islak kumla kalesine yeni bir kule yaptı. Örümcek Adam çok sevindi, çünkü kaybolan kovasını kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama örümcek hissiyle hemen"
   - Cümle 3: «Örümcek Adam bunu görmedi ama örümcek hissiyle hemen yanına baktı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir ifade değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kova deniz suyuyla dolmuştu ve su kovadan taşmıştı"
   - Cümle 9: «Kova deniz suyuyla dolmuştu ve su kovadan taşmıştı.»
   - Açıklama: Kumun üstünde yan yatan bir kova suyla dolup taşamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0047` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 6a4350cb3176fdcff04084a73b88c9d71e6c4344`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0048
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'bardak', fiil 'bölmek', sıfat 'kısa'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: duvardaki saksıda çiçeğin toprağı kurumuştu | bardakla su alıp duvara tırmandı ve çiçeği suladı
@tohum: orumcek_adam-0048
@degisim: bölmek -> sulamak
Güneş sıcak sıcak parlıyordu. Örümcek Adam, Hulk ile parkta yürürken duvarın tepesinde bir saksı fark etti. Saksıdaki sarı çiçek solmuştu, çünkü toprağı çok kuruydu. "Hulk, bu çiçeği sulayalım mı?" diye sordu Örümcek Adam. "Evet, ben su getiririm!" dedi Hulk. Hulk çeşmeden bir bardağı suyla doldurdu. Örümcek Adam bardağı aldı ve duvara tırmandı. Saksıdaki toprağı yavaşça suladı. Kısa bir süre sonra çiçek yeniden dik durdu. Hulk aşağıdan sevinçle el salladı. Örümcek Adam çok mutlu oldu, çünkü sarı çiçeği kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk çeşmeden bir bardağı suyla doldurdu"
   - Cümle 6: «Hulk çeşmeden bir bardağı suyla doldurdu.»
   - Açıklama: Bardak hiç kurulmadan sebepsizce ortaya çıkıyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0048` birebir aynı, `@degisim: bölmek -> sulamak` (tutuyorsan), ardından `@onarim: 3e891de94474c4b9b405e902c1efbed7086f520c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0049
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'havlu', fiil 'küçültmek', sıfat 'tuhaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: sürpriz balonlardan birinin ipi duvara takıldı | duvara tırmanıp balonu aldı ve banka bağladı
@tohum: orumcek_adam-0049
@degisim: küçültmek -> bağlamak
Bir sabah Örümcek Adam parkta Spin için bir sürpriz hazırlıyordu. Çimlere büyük bir havlu serdi ve üstüne kurabiyeler koydu. Ama sonra tuhaf bir şey gördü. Bankın yanındaki üç balondan biri yoktu. Balonun ipi çözülmüştü ve balon duvarın üstüne takılmıştı. Örümcek Adam hemen duvarın yanına koştu. Bir örümcek gibi duvara hızla tırmandı. Balonun ipini dikkatle çözdü ve aşağı indi. Sonra ipi banka sıkıca bağladı. Az sonra Spin parka geldi. "Sürpriz, Spin!" dedi Örümcek Adam. Spin havluyu, kurabiyeleri ve üç balonu gördü. "Teşekkürler, Örümcek Adam, bu çok güzel bir sürpriz!" dedi Spin.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama sonra tuhaf bir şey gördü"
   - Cümle 3: «Ama sonra tuhaf bir şey gördü.»
   - Açıklama: İlk üç cümlede sorun yalnız belirsizce ima ediliyor; balonun duvara takıldığı ancak 5. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ama sonra tuhaf bir şey gördü.»
   - Açıklama: İlk üç cümlede yalnız 'tuhaf bir şey gördü' deniyor; balonun duvara takıldığı ancak 5. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bir örümcek gibi duvara"
   - Cümle 7: «Bir örümcek gibi duvara hızla tırmandı.»
   - Açıklama: Benzetme kullanılmış; mecaz sayılabilir.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Balonun ipini dikkatle çözdü"
   - Cümle 8: «Balonun ipini dikkatle çözdü ve aşağı indi.»
   - Açıklama: İp bağlı değil takılıydı; 'çözdü' yerine 'kurtardı' uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0049` birebir aynı, `@degisim: küçültmek -> bağlamak` (tutuyorsan), ardından `@onarim: 64d6c545ff88165252de78ab177145e967c511af`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0053
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'alet', fiil 'somurtmak', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar yüzünden küçük fidan yere eğildi | fidanı iple sağlam bir sopaya bağladı
@tohum: orumcek_adam-0053
@degisim: uyanık -> sağlam
Örümcek Adam parkta bahçe oyunu oynuyordu ve ufak bir fidan dikti. Birden örümcek hissi bir sorun olduğunu haber verdi. Rüzgar sert esti ve ince fidan yere doğru eğildi. Örümcek Adam fidana bakıp somurttu. Sonra bahçe aletleri arasında bir ip ile sağlam bir sopa buldu. Sopayı fidanın yanında toprağa soktu. Fidanı iple sopaya yavaşça bağladı. Rüzgar yine esti ama fidan bu kez hiç eğilmedi. Örümcek Adam aletlerini topladı ve küçük fidana gülümsedi. Örümcek Adam çok sevindi, çünkü fidanı rüzgardan korumuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
   - Açıklama: 'Örümcek hissi' ve onun haber vermesi soyut ve mecazlı bir anlatım.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Birden örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Tohumdaki örümcek hissi sorunun çözümünde işe yaramıyor, Örümcek Adam ona göre hiçbir şey yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0053` birebir aynı, `@degisim: uyanık -> sağlam` (tutuyorsan), ardından `@onarim: 898a22b884d2c8130802903a3eed5b06c416a6bb`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0054 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0054
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'lokma', fiil 'yollamak', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgarda kumdaki şemsiye sallanıp garip bir ses çıkarıyordu | şemsiyenin sapını tuttu ve kuma iyice bastırdı
@tohum: orumcek_adam-0054
@degisim: yollamak -> tutmak
Rüzgar sert sert esiyordu. Örümcek Adam kumsalda sulu bir şeftali yiyordu. Birden arkasından garip bir "pat pat" sesi duyuldu. Örümcek Adam son lokmayı yuttu ve bu sesi çok merak etti. O sırada örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam sese doğru koştu. Ses, kumdaki büyük bir şemsiyeden geliyordu. Rüzgar şemsiyeyi sallıyordu ve şemsiye kumdan çıkmak üzereydi. Örümcek Adam şemsiyenin sapını iki eliyle tuttu. Sonra sapı kuma iyice bastırdı. Şemsiye artık hiç sallanmadı ve ses durdu. Örümcek Adam çok sevindi, çünkü garip sesin ne olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kumsalda sulu bir şeftali yiyordu"
   - Cümle 2: «Örümcek Adam kumsalda sulu bir şeftali yiyordu.»
   - Açıklama: Şeftali olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sulu bir şeftali yiyordu"
   - Cümle 2: «Örümcek Adam kumsalda sulu bir şeftali yiyordu.»
   - Açıklama: Şeftali olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 5: «O sırada örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı, 3 yaşındaki çocuk anlamaz.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0054` birebir aynı, `@degisim: yollamak -> tutmak` (tutuyorsan), ardından `@onarim: af6b8db8f4c11a8662111af995fa34a768cde79e`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0055
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kese', fiil 'yüklemek', sıfat 'şeffaf'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: çöp dolu kese çok ağırdı | arkadaşından yardım istedi ve keseyi birlikte taşıdılar
@tohum: orumcek_adam-0055
@degisim: yüklemek -> taşımak
Kumsalda güneş parlıyordu. Örümcek Adam kumdaki çöpleri toplayıp büyük, şeffaf bir kese içine koyuyordu. Sonunda kese doldu ama çok ağırdı. Örümcek Adam keseyi tek başına taşıyamadı. Biraz ileride Ghost-Spider davul çalıyordu. Örümcek Adam ona gitti ve yardım istedi. Arkadaşı davulunu bıraktı ve hemen geldi. Örümcek Adam önce ağ attı ve keseyi sıkıca bağladı. Böylece çöpler dökülmedi. Sonra ikisi keseyi iki ucundan tuttu. Arkadaşı havada süzüldü, Örümcek Adam da yürüdü. Keseyi birlikte çöp kutusuna taşıdılar. Örümcek Adam çok sevindi, çünkü kumsal tertemiz olmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük, şeffaf bir kese"
   - Cümle 2: «Örümcek Adam kumdaki çöpleri toplayıp büyük, şeffaf bir kese içine koyuyordu.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki çocuk bilmez.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam önce ağ attı ve keseyi sıkıca bağladı"
   - Cümle 8: «Örümcek Adam önce ağ attı ve keseyi sıkıca bağladı.»
   - Açıklama: Ağla bağlama adımı ağırlık sorununa yönelmiyor ve çözümü gereksiz yere uzatıyor.
   - Açıklama: Sorun kesenin ağırlığı iken çözüme ağırlıkla ilgisi olmayan fazladan bir ağ adımı ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0055` birebir aynı, `@degisim: yüklemek -> taşımak` (tutuyorsan), ardından `@onarim: eb43c33364ab7736700b6d0a51d304cd4c8240b1`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0056 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0056
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yastık', fiil 'silkmek', sıfat 'elmalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: yastık parktaki duvarın tepesinde kaldı | duvara tırmanıp yastığı aldı ve tozunu silkti
@tohum: orumcek_adam-0056
Örümcek Adam ile Spin parkta yastık oyunu oynuyordu. Sırayla küçük, elmalı bir yastığı birbirine atıyorlardı. Ama Spin yastığı çok yükseğe attı ve yastık duvarın tepesinde kaldı. "Eyvah, yastığımız yukarıda!" dedi Spin. "Hemen alırım, Spin," dedi Örümcek Adam. Örümcek Adam duvara hızla tırmandı ve yastığı aldı. Sonra tozlu yastığı iki kez silkti. Aşağı indi ve yastığı Spin'e verdi. "Şimdi sıra sende, Örümcek Adam," dedi Spin gülerek. Oyun yine sırayla devam etti. Örümcek Adam ile Spin bundan sonra yastığı hep yavaşça attı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük, elmalı bir yastığı"
   - Cümle 2: «Sırayla küçük, elmalı bir yastığı birbirine atıyorlardı.»
   - Açıklama: 'Elmalı' içinde elma olan yiyecek için kullanılır; yastık için yanlış anlamda.
   - Açıklama: 'Elmalı' içinde elma olan anlamına gelir; yastık için yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0056` birebir aynı, ardından `@onarim: 629d26f1fc054313b7c5c594b6018bf11ad203ee`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0057 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0057
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kaktüs', fiil 'hoplamak', sıfat 'sakar'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: top kaktüslerin arasına yuvarlandı | ağ atıp topu dikenlere dokunmadan çekti
@tohum: orumcek_adam-0057
Örümcek Adam ile Hulk parkta top oynuyordu. Hulk topu yakaladı ve öyle güçlü hopladı ki top elinden kaydı. Top, çiçek bahçesindeki kaktüslerin arasına yuvarlandı. "Ah, ben ne sakarım!" dedi Hulk gülerek. Kaktüslerin dikenleri çok sivriydi. "Dokunma, Hulk, topu ben alırım," dedi Örümcek Adam. Örümcek Adam ağ attı. Ağ topa yapıştı. Örümcek Adam ağı çekti ve top dikenlere hiç dokunmadan geldi. Sonra topu Hulk'a verdi. Hulk kocaman ellerini çırptı ve yine hopladı. "Teşekkürler, Örümcek Adam, sen harika bir arkadaşsın!" dedi Hulk.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "öyle güçlü hopladı ki"
   - Cümle 2: «Hulk topu yakaladı ve öyle güçlü hopladı ki top elinden kaydı.»
   - Açıklama: 'Güçlü' hoplamayı niteleyen bir zarf olarak uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben ne sakarım"
   - Cümle 4: «"Ah, ben ne sakarım!" dedi Hulk gülerek.»
   - Açıklama: 'Sakar' kelimesi 3 yaşındaki çocuğun bilmeyeceği soyut bir sıfat.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0057` birebir aynı, ardından `@onarim: ed92a7942192268aca1701b91769a81d77a62664`, sonra gövde.
