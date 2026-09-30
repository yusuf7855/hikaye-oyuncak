# Editör görevi (onarım): Örümcek Adam, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar29.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0093 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0093
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bilye', fiil 'sunmak', sıfat 'yavaş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: mavi bilye yokuştan yuvarlandı ve kayboldu | bankın altına bakıp bilyeyi buldu
@tohum: orumcek_adam-0093
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin parkın oyun alanında bilye oynuyordu. Birden Spin'in mavi bilyesi yokuştan aşağı yuvarlandı ve kayboldu. "Bilyemi bulamıyorum, Örümcek Adam," dedi Spin üzgün bir sesle. Örümcek Adam yavaş yavaş aşağı yürüdü. Bir bankın yanına gelince örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen eğildi ve bankın altına baktı. Mavi bilye kuru yaprakların arasında duruyordu. Örümcek Adam onu aldı ve iki eliyle Spin'e sundu. "İşte bilyen, Spin," dedi Örümcek Adam. Spin sevinçle bilyesini tuttu. İki arkadaş oyun alanına döndü ve bilye oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 6: «Bir bankın yanına gelince örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve hissin haber vermesi soyut ve mecazlı bir anlatım.
   - Açıklama: Soyut 'örümcek hissi' ve 'sorun olduğunu haber verdi' anlatımı 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 6: «Bir bankın yanına gelince örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Bilyenin yeri örümcek hissiyle sebepsizce bulunuyor; çözüm aramadan değil kendiliğinden geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0093` birebir aynı, ardından `@onarim: 9d29c85d583be2b77f24b393f76f4eb89ef1629e`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0094
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'yapboz', fiil 'birleştirmek', sıfat 'büyük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: rüzgar yapbozun son parçasını denize doğru uçurdu | ağ atıp parçayı havada yakaladı
@tohum: orumcek_adam-0094
Kumsalda güneş parlıyordu. Örümcek Adam ile Hulk kumun üstünde büyük bir yapboz yapıyordu. Yapbozda mavi bir deniz resmi vardı. Birden rüzgar esti ve son parça havaya uçtu. "Parça denize gidiyor, Örümcek Adam!" diye bağırdı Hulk. Örümcek Adam hemen bir ağ attı. Ağ, parçayı havada yakaladı. Örümcek Adam onu Hulk'a verdi. Hulk kocaman parmaklarıyla onu tutmaya çalıştı. Minik parça iki kez kuma düştü. İkisi de buna çok güldü. Sonunda Hulk onu yavaşça yerine koydu. "Bütün parçaları birleştirdik!" dedi Hulk. Örümcek Adam çok sevindi, çünkü deniz resmi artık tamamdı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Yapbozda mavi bir deniz resmi vardı.»
   - Açıklama: Sorun ilk üç cümlede söylenmiyor, ancak dördüncü cümlede rüzgar parçayı uçuruyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Minik parça iki kez kuma düştü"
   - Cümle 10: «Minik parça iki kez kuma düştü.»
   - Açıklama: Parça yakalandıktan sonra Hulk'un parçayı tutamaması ikinci bir küçük sorun açıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Minik parça iki kez kuma düştü"
   - Cümle 10: «Minik parça iki kez kuma düştü.»
   - Açıklama: Hulk'un parçayı düşürmesi sorunla ilgisi olmayan, işlevsiz bir ek olaydır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0094` birebir aynı, ardından `@onarim: 13c20b6af6a50f4d7fee620fb3a808828f699c5c`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0096 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0096
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yeni bir şeyi denemek
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'cüzdan', fiil 'dinlemek', sıfat 'çiçekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: uzun çalılar bahçedeki çiçekleri kapatıyordu | duvara tırmanıp çiçeklere baktı ve resim çizdi
@tohum: orumcek_adam-0096
@degisim: cüzdan -> kalem
Parkın bahçesinde renkli çiçekler açmıştı. Örümcek Adam ilk kez onların resmini yapmayı denemek istiyordu. Ama önündeki uzun çalılar çiçeklerin çoğunu kapatıyordu. Spin ona kendi kağıdını ve kalemini verdi. "Önce iyice bak, sonra çiz," dedi Spin. Örümcek Adam onu dikkatle dinledi. Hemen bahçenin yanındaki taş duvara kolayca tırmandı. Duvarın üstünden bütün bahçe görünüyordu. Kırmızı, sarı ve mor çiçeklere uzun uzun baktı. Sonra aşağı indi ve çiçekli bir resim çizdi. "Çok güzel olmuş, Örümcek Adam!" dedi Spin. Örümcek Adam çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen bahçenin yanındaki taş duvara kolayca tırmandı"
   - Cümle 7: «Hemen bahçenin yanındaki taş duvara kolayca tırmandı.»
   - Açıklama: Güvenli özellik kullanımı satırına aykırı olarak parktaki alçak taş duvara tırmanma süper güç diye çerçevelenmeden, çocuğun taklit edebileceği biçimde anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0096` birebir aynı, `@degisim: cüzdan -> kalem` (tutuyorsan), ardından `@onarim: f69f0b3b9fe5f9d19583fdca347794f703fc38a4`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0097 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0097
- yer: ev (Takımın gizli evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'pizza', fiil 'kirletmek', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: uçurtma gizli evin çamurlu çatısına düştü | duvara tırmanıp uçurtmayı getirdi
@tohum: orumcek_adam-0097
@degisim: pizza -> uçurtma
Gizli evin önünde Hulk ile Örümcek Adam uçurtma uçuruyordu. Birden rüzgar durdu ve Hulk'ın uçurtması evin çatısına düştü. Çatıda yağmurdan kalan çamur vardı. "Çamur uçurtmamı kirletecek," dedi Hulk çekingen bir sesle. Hulk çatıya çıkamazdı, çünkü çok ağırdı. "Ben getiririm, Hulk," dedi Örümcek Adam. Örümcek Adam evin duvarına hızla tırmandı. Uçurtma çamura düşmeden onu hemen kaldırdı. Sonra duvardan yavaşça aşağı indi. Onu Hulk'a verdi. Hulk kocaman elleriyle sıkıca tuttu ve gülümsedi. "Teşekkürler, Örümcek Adam," dedi Hulk. Rüzgar yeniden esince ikisi uçurtmayı mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hulk çekingen bir sesle"
   - Cümle 4: «"Çamur uçurtmamı kirletecek," dedi Hulk çekingen bir sesle.»
   - Açıklama: 'Çekingen' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Çekingen' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam evin duvarına hızla tırmandı"
   - Cümle 7: «Örümcek Adam evin duvarına hızla tırmandı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre tırmanma yalnız süper güç olarak geçmeli; burada evin duvarından çatıya hızla tırmanma taklit edilebilir biçimde anlatılıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Uçurtma çamura düşmeden onu hemen kaldırdı"
   - Cümle 8: «Uçurtma çamura düşmeden onu hemen kaldırdı.»
   - Açıklama: Uçurtma zaten çamurlu çatıya düşmüşken çamura düşmeden kaldırıldığı söyleniyor.
   - Açıklama: Uçurtma zaten çatıya düşmüştü; 'çamura düşmeden' ifadesi önceki olayla çelişiyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu Hulk'a verdi"
   - Cümle 10: «Onu Hulk'a verdi.»
   - Açıklama: 'Onu' zamirinden önceki cümlede uçurtma geçmiyor; neyi gösterdiği belirsiz.
   - Açıklama: 'Onu' zamiri önceki cümlede adı geçmeyen uçurtmayı gösteriyor; gösterdiği şey belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0097` birebir aynı, `@degisim: pizza -> uçurtma` (tutuyorsan), ardından `@onarim: 99675eba40a70e6f7f66bb0937fe11068dfd149f`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0098 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0098
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kamyon', fiil 'giyinmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: kum dökülüyordu ve kale büyümüyordu | oyuncak kamyonunu arkadaşıyla paylaştı
@tohum: orumcek_adam-0098
@degisim: giyinmek -> taşımak
Bir sabah Örümcek Adam parkta çizgili oyuncak kamyonuyla oynuyordu. Yanında Spin kumdan bir kale yapıyordu. Ama Spin kumu elleriyle taşıyamıyordu, çünkü parmaklarından dökülüyordu. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam başını kaldırdı ve Spin'in üzgün yüzünü gördü. "Bu kale hiç büyümüyor," dedi Spin. Örümcek Adam kamyonunu Spin'e uzattı. "Al, Spin, kamyonumu birlikte kullanalım," dedi Örümcek Adam. Spin kamyonu kumla doldurdu ve kaleye götürdü. Sonra sırayla taşıdılar ve duvarlar hızla yükseldi. İkisi de çok sevindi, çünkü paylaşınca kale çabucak büyümüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0098` birebir aynı, `@degisim: giyinmek -> taşımak` (tutuyorsan), ardından `@onarim: 49e8e883e7d934dfeac104250771b74591135ac6`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0101 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0101
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'harita', fiil 'beslemek', sıfat 'sağlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: harita suyun kenarında kaldı ve dalga geliyordu | haritayı hemen aldı ve özür diledi
@tohum: orumcek_adam-0101
@degisim: beslemek -> yemek
Kumsalda Örümcek Adam ile Hulk hazine oyunu oynuyordu. Hulk bir harita çizmiş ve Örümcek Adam'a vermişti. Örümcek Adam haritayı suyun kenarına bıraktı ve bir deniz kabuğuna baktı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Büyük bir dalga ona doğru geliyordu. Örümcek Adam koştu ve kağıdı hemen aldı. Ama bir köşesi ıslanmıştı. "Özür dilerim, Hulk, haritanı suya çok yakın bıraktım," dedi Örümcek Adam. "Sorun değil, yol yine görünüyor," dedi Hulk. İkisi haritadaki yolu izleyip büyük bir kayanın yanına yürüdü. Kayanın arkasında Hulk'ın sakladığı sağlıklı meyveler vardı. İki arkadaş kumda oturdu ve meyveleri mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun"
   - Cümle 4: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk için uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 4: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' 3 yaşındaki çocuk için soyut kavram.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Büyük bir dalga ona doğru"
   - Cümle 5: «Büyük bir dalga ona doğru geliyordu.»
   - Açıklama: 'ona' zamirinin haritayı mı Örümcek Adam'ı mı gösterdiği belli değil.
   - Açıklama: 'ona' zamirinin Örümcek Adam'ı mı haritayı mı gösterdiği belli değil.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Büyük bir dalga ona doğru geliyordu"
   - Cümle 5: «Büyük bir dalga ona doğru geliyordu.»
   - Açıklama: Sorun olan dalga tehlikesi ilk üç cümlede değil beşinci cümlede söyleniyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam koştu ve kağıdı hemen aldı"
   - Cümle 6: «Örümcek Adam koştu ve kağıdı hemen aldı.»
   - Açıklama: Büyük dalga gelirken su kenarına koşmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0101` birebir aynı, `@degisim: beslemek -> yemek` (tutuyorsan), ardından `@onarim: c364d7520ab9597c91e5e7593b2424269239ca50`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0102 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0102
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'dolma', fiil 'şaşırmak', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: limandaki duvarın üstünden garip bir ses geldi | duvara tırmanıp takılı uçurtmayı buldu
@tohum: orumcek_adam-0102
@degisim: dolma -> uçurtma
Bir sabah Örümcek Adam limanda yürüyordu. Birden geniş taş duvarın üstünden garip bir ses geldi. Ses durmadan tekrar tekrar duyuluyordu. Örümcek Adam bu sese çok şaşırdı. Duvar yüksekti ve aşağıdan üstü görünmüyordu. Örümcek Adam merakla duvara tırmandı. Duvarın üstünde kırmızı bir uçurtma vardı. Uçurtmanın ipi eski bir demire takılmıştı. Rüzgar estikçe kağıdı pır pır sallanıyordu. Garip sesi bu kağıt çıkarıyordu. Sonra ipi dikkatle çözdü ve uçurtmayı aşağı indirdi. Örümcek Adam çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "geniş taş duvarın üstünden garip bir ses geldi"
   - Cümle 2: «Birden geniş taş duvarın üstünden garip bir ses geldi.»
   - Açıklama: Garip bir ses duymak kimseye zarar vermeyen, çözülmesi gereken bir sorun değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ses durmadan tekrar tekrar duyuluyordu"
   - Cümle 3: «Ses durmadan tekrar tekrar duyuluyordu.»
   - Açıklama: 'Durmadan' ile 'tekrar tekrar' aynı şeyi söylüyor.
   - Açıklama: 'Durmadan' ile 'tekrar tekrar' aynı şeyi söylüyor; gereksiz tekrar.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam merakla duvara tırmandı"
   - Cümle 6: «Örümcek Adam merakla duvara tırmandı.»
   - Açıklama: Yüksek duvara tırmanma süper güç olarak değil merakla yapılıyor; güvenli kullanım satırına göre taklit edilebilir.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra ipi dikkatle çözdü"
   - Cümle 11: «Sonra ipi dikkatle çözdü ve uçurtmayı aşağı indirdi.»
   - Açıklama: Önceki cümlenin öznesi 'kağıt' olduğu için ipi kimin çözdüğü belli değil.
   - Açıklama: Öznesiz cümlede son özne 'bu kağıt' olduğu için ipi kimin çözdüğü belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0102` birebir aynı, `@degisim: dolma -> uçurtma` (tutuyorsan), ardından `@onarim: 33f9e0eb143ff33b10b02d7b785c880268fa87c4`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0104
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kaymak', fiil 'kurmak', sıfat 'paslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar ıslak resmi uçurmak üzereydi | ağ atıp çite bir askı kurdu
@tohum: orumcek_adam-0104
@degisim: kaymak -> boya
Parkın ağaçları arasında Spin güzel bir çiçek resmi yapmıştı. Örümcek Adam ile Spin boyanın kurumasını bekliyordu. Ama rüzgar esiyordu ve ıslak resim çimenin üstünde kıpırdıyordu. "Kağıt uçarsa boya bozulur," dedi Spin. Örümcek Adam yakındaki paslı demir çite baktı. Hemen ağ attı ve çitin üstüne küçük bir askı kurdu. Spin kağıdı askıya dikkatle astı. Kağıdın köşeleri yapışkan ağda sıkıca durdu. Rüzgar esti ama kağıt artık uçmadı. İkisi yan yana oturup bekledi. Çiçeğin mavi yaprakları yavaş yavaş kurudu. "Resmin hazır, Spin!" dedi Örümcek Adam. Spin resmini aldı ve iki arkadaş oyun alanına mutlu mutlu koştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "köşeleri yapışkan ağda sıkıca durdu"
   - Cümle 8: «Kağıdın köşeleri yapışkan ağda sıkıca durdu.»
   - Açıklama: 'Sıkıca durmak' uygun değil; 'yapıştı' ya da 'tutundu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çiçeğin mavi yaprakları yavaş yavaş kurudu"
   - Cümle 11: «Çiçeğin mavi yaprakları yavaş yavaş kurudu.»
   - Açıklama: Kuruyan boya olmasına rağmen cümle çiçeğin yapraklarının solduğu anlamına da geliyor.
   - Açıklama: Kuruyan resimdeki boya olduğu halde cümle çiçeğin yapraklarının solduğu anlamını veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0104` birebir aynı, `@degisim: kaymak -> boya` (tutuyorsan), ardından `@onarim: 145b8bfbcf70fbc2b04335941d04a3cd198c6829`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0108
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'zarf', fiil 'ovuşturmak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: yüksek duvardan garip bir ses geldi | duvara tırmanıp sesi yapan uçurtmayı buldu
@tohum: orumcek_adam-0108
@degisim: zarf -> uçurtma
Tuzlu bir rüzgar esiyordu. Örümcek Adam kumsalda kumla oynarken garip bir ses duydu. Ses yüksek bir taş duvarın tepesinden geliyordu. Örümcek Adam aşağıdan baktı ama hiçbir şey göremedi. Sesi çok merak etti. Duvarı iyi tutmak için ellerindeki kumu ovuşturup temizledi. Sonra duvara tırmandı ve tepeye çıktı. Orada kırmızı bir uçurtma takılı kalmıştı. Uçurtmanın kağıdı rüzgarda sallanıp ses çıkarıyordu. Örümcek Adam uçurtmayı dikkatle kurtardı ve aşağı indi. Kumsalda ipini tuttu ve uçurtma havaya yükseldi. Örümcek Adam çok sevindi, çünkü o garip sesi yapan uçurtmayı bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Tuzlu bir rüzgar esiyordu"
   - Cümle 1: «Tuzlu bir rüzgar esiyordu.»
   - Açıklama: 'Tuzlu rüzgar' mecazlı bir betimleme, 3 yaşındaki çocuk için somut değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvarı iyi tutmak için ellerindeki kumu ovuşturup temizledi"
   - Cümle 6: «Duvarı iyi tutmak için ellerindeki kumu ovuşturup temizledi.»
   - Açıklama: Yüksek duvara tırmanma süper güç değil taklit edilebilir bir tırmanma tekniği gibi anlatılıyor; güvenli özellik kullanımı satırına aykırı.
   - Açıklama: Yüksek duvara tırmanma süper güç olarak değil, çocuğun taklit edebileceği sıradan bir tırmanış hazırlığıyla anlatılıyor; güvenli özellik kullanımına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0108` birebir aynı, `@degisim: zarf -> uçurtma` (tutuyorsan), ardından `@onarim: fcdc705a91ad44407b6a724466ad2ded863907fe`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0109
- yer: ev (Takımın gizli evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çim', fiil 'bırakmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: koşarken yerdeki resme bastı ve resim buruştu | özür dileyip resmi duvarın en üstüne astı
@tohum: orumcek_adam-0109
Örümcek Adam gizli evde koşarak oynuyordu. Spin yeşil çimleri kıvrımlı çizgilerle boyamış, resmi kurusun diye yere bırakmıştı. Örümcek Adam resmi görmedi ve üstüne bastı. Resim buruştu ve Spin çok üzüldü. Örümcek Adam hemen durdu ve Spin'den özür diledi. Sonra resmi elleriyle yavaşça düzeltti. Kimse basmasın diye onu yükseğe asmak istedi. Duvara tırmandı ve resmi en üstteki çiviye astı. Spin yukarıdaki resmine baktı ve gülümsedi. Örümcek Adam rahatladı, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Spin yeşil çimleri kıvrımlı çizgilerle boyamış"
   - Cümle 2: «Spin yeşil çimleri kıvrımlı çizgilerle boyamış, resmi kurusun diye yere bırakmıştı.»
   - Açıklama: Cümle gerçek çimlerin boyandığını söylüyor; resme çim çizildiği anlamı yanlış kelimeyle verilmiş.
   - Açıklama: 'Çimleri boyamak' gerçek çimleri boyamak gibi okunuyor; resim çizildiği anlatılmak isteniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çimleri kıvrımlı çizgilerle"
   - Cümle 2: «Spin yeşil çimleri kıvrımlı çizgilerle boyamış, resmi kurusun diye yere bırakmıştı.»
   - Açıklama: 'Kıvrımlı' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kimse basmasın diye onu yükseğe asmak istedi"
   - Cümle 7: «Kimse basmasın diye onu yükseğe asmak istedi.»
   - Açıklama: Çözüm özür, düzeltme ve asma olarak üç adım sürüyor ve asmak buruşukluğa yönelmiyor.
   - Açıklama: Çözüm özür, düzeltme ve asma olmak üzere üç adım sürüyor ve asma buruşmayı değil ileride basılmayı hedefliyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvara tırmandı ve resmi en üstteki çiviye astı"
   - Cümle 8: «Duvara tırmandı ve resmi en üstteki çiviye astı.»
   - Açıklama: Güvenli kullanım satırı ev içi tırmanmayı yasaklıyor; ev içinde yükseğe tırmanma taklit edilebilir.
   - Açıklama: Güvenli özellik kullanımı satırı çocuğun taklit edebileceği ev içi tırmanmayı yasaklıyor; burada evde bir şey asmak için duvara tırmanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0109` birebir aynı, ardından `@onarim: da97e2014384bb435f78e7a0ddd9ae862ae04057`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0111 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0111
- yer: ev (Takımın gizli evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'bez', fiil 'savrulmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: rüzgar bezi uçurdu ve bez bir resmin arkasına girdi | duvara tırmanıp arkadaşından yardım istedi
@tohum: orumcek_adam-0111
Bir sabah Örümcek Adam ile Spin gizli evde resim yapıyordu. Açık pencereden sert bir rüzgar esti ve Spin'in boya bezi havaya savruldu. Bez duvarın en üstündeki resimlerin arkasında saklı kaldı. Spin'in fırçaları boyalı kaldı ve Spin üzüldü. Örümcek Adam hemen duvara tırmandı. Ama yukarıda üç resim vardı ve bez görünmüyordu. Örümcek Adam aşağıdaki Spin'den yardım istedi. Spin bezin yerini görmüştü ve sarı resmi gösterdi. Örümcek Adam sarı resmin arkasına baktı ve bezi buldu. Aşağı indi ve bezi Spin'e verdi. Spin fırçalarını sildi ve yeniden resim yapmaya başladı. Örümcek Adam çok sevindi, çünkü Spin'e sorunca bezi hemen bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Spin bezin yerini görmüştü"
   - Cümle 8: «Spin bezin yerini görmüştü ve sarı resmi gösterdi.»
   - Açıklama: Spin bezin yerini bildiği halde sorulana kadar söylemiyor; bilgi çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0111` birebir aynı, ardından `@onarim: 33b0d2ef32dcfecad401423371db8e85961ec40c`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0113
- yer: ev (Takımın gizli evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'menekşe', fiil 'yoğurmak', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: oyun hamuru yüksek tavana yapıştı | duvara tırmanıp hamuru tavandan aldı
@tohum: orumcek_adam-0113
Dışarıda yağmur yağıyordu. Örümcek Adam gizli evde masmavi oyun hamuru yoğuran Hulk'ı izliyordu. Hulk hamuru havaya çok güçlü attı ve hamur tavana yapıştı. "Hamurdan menekşe yapacaktım ama tavan çok yüksek!" dedi Hulk. "Ben sana yardım ederim, Hulk," dedi Örümcek Adam. Örümcek Adam duvara tırmandı ve tavana kadar çıktı. Yapışkan hamuru tavandan yavaşça çekip aldı. Sonra aşağı indi ve hamuru Hulk'a verdi. Hulk bu kez hamura yavaşça şekil verdi ve güzel bir menekşe yaptı. "Teşekkürler, bu menekşe senin!" dedi Hulk. Örümcek Adam çok sevindi, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Örümcek Adam gizli evde"
   - Cümle 2: «Örümcek Adam gizli evde masmavi oyun hamuru yoğuran Hulk'ı izliyordu.»
   - Açıklama: Tamlama eksik; 'gizli evinde' ya da 'gizli evlerinde' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hamuru havaya çok güçlü attı"
   - Cümle 3: «Hulk hamuru havaya çok güçlü attı ve hamur tavana yapıştı.»
   - Açıklama: 'Güçlü' sıfatı zarf gibi kullanılmış; 'güçlüce' ya da 'çok hızlı' olmalı.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara tırmandı ve tavana kadar çıktı"
   - Cümle 6: «Örümcek Adam duvara tırmandı ve tavana kadar çıktı.»
   - Açıklama: Güvenli özellik kullanımı satırı ev içi taklit edilebilir tırmanmayı yasaklıyor; burada ev içinde tavana kadar tırmanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0113` birebir aynı, ardından `@onarim: f30bdb682d9936398fa27d1588ca080ef38806f3`, sonra gövde.
