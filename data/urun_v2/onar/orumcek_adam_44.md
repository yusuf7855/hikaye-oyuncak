# Editör görevi (onarım): Örümcek Adam, onarım partisi 44

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar44.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar44.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0144 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0144
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yiyecek', fiil 'ıslanmak', sıfat 'umutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: dalgalar yükselince duvardaki resimler ıslanmaya başladı | süper gücüyle duvara tırmanıp resimleri en yükseğe astı
@tohum: orumcek_adam-0144
@degisim: umutlu -> güzel
Dalgalar gürültüyle limanın duvarına çarpıyordu. Örümcek Adam, sürpriz için Spin'in resimlerini duvara asmıştı. Ama dalgalar yükselince resimler ıslanmaya başladı. Örümcek Adam onları hemen topladı. Sonra süper gücüyle duvara tırmandı ve resimleri en yükseğe astı. Dalgalar artık onlara ulaşamıyordu. Örümcek Adam aşağı indi ve yanındaki sepetten yiyecekleri çıkardı. Sonra oturdu ve Spin'i bekledi. Az sonra Spin geldi ve duvardaki resimlerini gördü. "Bu sürpriz çok güzel, Örümcek Adam!" dedi Spin. "Hepsi senin için, Spin," dedi Örümcek Adam. İki arkadaş limanda yiyecekleri birlikte yedi. Örümcek Adam çok mutluydu, çünkü sürprizi Spin'i sevindirmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yanındaki sepetten yiyecekleri çıkardı"
   - Cümle 7: «Örümcek Adam aşağı indi ve yanındaki sepetten yiyecekleri çıkardı.»
   - Açıklama: Sepet ve yiyecekler önceden kurulmadan sebepsiz beliriyor ve sorunla ilgisi olmayan ikinci bir olay başlatıyor.
   - Açıklama: Sepet ve yiyecekler önceden kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0144` birebir aynı, `@degisim: umutlu -> güzel` (tutuyorsan), ardından `@onarim: 16b0292d26932ccc30ccf5933138292368ae620d`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0145 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0145
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gevrek', fiil 'oturmak', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: arkadaşı yiyeceğini unutmuştu ve acıkmıştı | gevreği ikiye böldü ve onunla paylaştı
@tohum: orumcek_adam-0145
@degisim: açık -> sıcak
Örümcek Adam parkta bir bankta oturup gevrek yiyordu. Birden Örümcek Adam'ın örümcek hissi çalıştı. Hemen etrafına baktı. Ağacın altında Ghost-Spider aç ve üzgündü, çünkü yiyeceğini gizli evde unutmuştu. Örümcek Adam elindeki gevreği ikiye böldü. Sonra arkadaşının yanına gitti. "Bunun yarısı senin," dedi Örümcek Adam. Arkadaşı gevreği aldı ve "Çok teşekkür ederim!" dedi. İkisi onu ağacın altında birlikte yedi. Gevrek sıcak ve çıtır çıtırdı. Arkadaşı artık aç değildi ve çok mutluydu. Örümcek Adam bundan sonra yiyeceğini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi çalıştı"
   - Cümle 2: «Birden Örümcek Adam'ın örümcek hissi çalıştı.»
   - Açıklama: Hissin çalışması soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi çalıştı"
   - Cümle 2: «Birden Örümcek Adam'ın örümcek hissi çalıştı.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut bir kavram, 3 yaşındaki çocuk anlamaz.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Hemen etrafına baktı.»
   - Açıklama: Ghost-Spider'ın aç olduğu sorun ancak dördüncü cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ağacın altında Ghost-Spider aç ve üzgündü, çünkü yiyeceğini gizli evde unutmuştu.»
   - Açıklama: Arkadaşının aç olduğu sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0145` birebir aynı, `@degisim: açık -> sıcak` (tutuyorsan), ardından `@onarim: b0638590b165e35bb728eb06f6a3f826679e892b`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0146 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0146
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çember', fiil 'yumuşamak', sıfat 'biberli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: çember çamura battı ve çıkmadı | duvara tırmanıp güçlü arkadaşından yardım istedi
@tohum: orumcek_adam-0146
@degisim: biberli -> kırmızı
Bir sabah Örümcek Adam parkta kırmızı çemberiyle oynuyordu. Çember çiçek bahçesine yuvarlandı ve çamura battı. Bahçenin toprağı suyla çok yumuşamıştı. Örümcek Adam çemberi iki eliyle çekti ama çamur çok yapışkandı. Hulk da parktaydı ama ağaçların arasında görünmüyordu. Örümcek Adam süper gücüyle bahçenin duvarına tırmandı. Oradan Hulk'ı oyun alanında gördü. "Hulk, bana yardım eder misin?" diye seslendi Örümcek Adam. Hulk hemen koşup geldi. Kocaman eliyle çemberi tuttu ve kolayca çıkardı. Sonra çemberi Örümcek Adam'a verdi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım isteyerek çemberini geri almıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Örümcek Adam çemberi iki eliyle çekti ama çamur çok yapışkandı"
   - Cümle 4: «Örümcek Adam çemberi iki eliyle çekti ama çamur çok yapışkandı.»
   - Açıklama: Bahçe çamuruna batmış bir çemberin iki elle çekilince çıkmaması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0146` birebir aynı, `@degisim: biberli -> kırmızı` (tutuyorsan), ardından `@onarim: 8c6d202fe8853a45559b5437effad363f3046454`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0147 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0147
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kravat', fiil 'ovmak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: yüksek duvarın tepesinden bilinmeyen bir ses geldi | duvara tırmanıp sesi yapan balonu buldu
@tohum: orumcek_adam-0147
@degisim: kravat -> balon
Parkta ince bir ses duyuluyordu. Örümcek Adam ile Ghost-Spider sesin nereden geldiğini merak etti. Ses yüksek bir duvarın tepesinden geliyordu ama yerden bir şey görünmüyordu. "Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı. "Ben bakarım," dedi Örümcek Adam. Süper gücüyle duvarın tepesine tırmandı. Tepede ipi takılmış mavi bir balon vardı. Rüzgar esince balon duvara değiyor ve ses çıkarıyordu. Örümcek Adam ipi dikkatle çözdü ve balonla aşağı indi. Balonu eliyle ovdu ve yine aynı ses geldi. "Demek ses balondan geliyormuş!" dedi arkadaşı ve güldü. Örümcek Adam ve arkadaşı çok sevindi, çünkü sesi yapan balonu bulmuşlardı.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "diye sordu konuşkan arkadaşı"
   - Cümle 4: «"Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı.»
   - Açıklama: Kartın yanlar bölümünde Ghost-Spider için konuşkanlık diye bir özellik ya da ilişki yok.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "diye sordu konuşkan arkadaşı"
   - Cümle 4: «"Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı.»
   - Açıklama: Kartın yanlar bölümünde Ghost-Spider için konuşkanlık diye bir özellik yok; yanlış bilgi ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0147` birebir aynı, `@degisim: kravat -> balon` (tutuyorsan), ardından `@onarim: 6325826c315715f7ef324190bcd9451cede702ef`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0148 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0148
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'flüt', fiil 'uçmak', sıfat 'kalın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar sürpriz uçurtmayı banktan uçurmaya başladı | kuyruğunu yakalayıp uçurtmaya kalın ip bağladı
@tohum: orumcek_adam-0148
@degisim: flüt -> uçurtma
Örümcek Adam, Spin'e sürpriz olsun diye uçurtma ve kalın ip getirdi. Birden örümcek hissiyle Örümcek Adam'ın başı karıncalandı. Sert bir rüzgar esti ve uçurtma banktan uçmaya başladı. Örümcek Adam hemen döndü ve uçurtmanın kuyruğunu yakaladı. Sonra uçurtmaya ipi sıkıca bağladı. Az sonra Spin parka geldi. "Bu uçurtma senin için, Spin," dedi Örümcek Adam. "Çok güzel, teşekkür ederim!" dedi Spin sevinçle. İki arkadaş ipi birlikte tuttu. Uçurtma rüzgarla gökyüzüne uçtu. Spin mutlu mutlu güldü. Örümcek Adam bundan sonra rüzgarlı havada uçurtmaya hep önce ip bağladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın başı karıncalandı"
   - Cümle 2: «Birden örümcek hissiyle Örümcek Adam'ın başı karıncalandı.»
   - Açıklama: 'Örümcek hissi' ve 'başı karıncalandı' 3 yaşındaki çocuğun bilmeyeceği mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle Örümcek Adam'ın başı karıncalandı"
   - Cümle 2: «Birden örümcek hissiyle Örümcek Adam'ın başı karıncalandı.»
   - Açıklama: 'Örümcek hissi' ve 'başı karıncalandı' soyut ve mecazlı anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0148` birebir aynı, `@degisim: flüt -> uçurtma` (tutuyorsan), ardından `@onarim: f7973184270c5f087b9c9f234ebf6e8e02c11ee6`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0149 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0149
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'salata', fiil 'uzanmak', sıfat 'süslü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: masa sallanıyordu ve salata kabı düşmek üzereydi | uzanıp kabı tuttu ve masanın ayağına taş koydu
@tohum: orumcek_adam-0149
Parkta, çiçek bahçesinin yanında, Örümcek Adam Hulk'a bir sürpriz hazırlıyordu. Eski bir masaya kocaman, süslü bir salata koydu ama masa sallanıyordu. Birden Örümcek Adam'ın örümcek hissi çalıştı. Salata kabı masanın kenarına kaymıştı ve düşmek üzereydi. Örümcek Adam hemen uzandı ve kabı tuttu. Sonra masanın kısa ayağının altına düz bir taş koydu. Masa artık hiç sallanmıyordu. Az sonra Hulk geldi. "Bu salata senin için, Hulk!" dedi Örümcek Adam. "Ne güzel bir sürpriz!" dedi Hulk ve güldü. İkisi masaya oturup salatayı birlikte yedi. Örümcek Adam çok mutluydu, çünkü salata yere düşmedi ve Hulk çok sevindi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Adam'ın örümcek hissi çalıştı"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi çalıştı.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut ve mecazlı; 3 yaşındaki çocuk anlamaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi çalıştı"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi çalıştı.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut ve mecazlı bir ifade, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0149` birebir aynı, ardından `@onarim: 3384b41d32002c9a45404b46c9e23166dec6d9cb`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0150
- yer: ev (Takımın gizli evi.)
- tema: sırayla oynamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'yaprak', fiil 'eklemek', sıfat 'rahat'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: ikisi aynı anda küp koyunca kule sallandı | kuleyi tuttu ve sırayla oynamayı önerdi
@tohum: orumcek_adam-0150
@degisim: yaprak -> küp
Örümcek Adam ile Spin gizli evde tahta küplerle kule yapıyordu. İkisi de aynı anda bir küp eklemek istedi. Elleri çarpıştı ve kule sallanmaya başladı. Birden Örümcek Adam'ın örümcek hissi çalıştı, çünkü kule düşmek üzereydi. Elini hemen çekti ve kuleyi iki yandan tuttu. Kule yıkılmadı. "Sırayla koyalım, Spin," dedi Örümcek Adam. "Olur, önce sen koy," dedi Spin. Örümcek Adam kırmızı bir küpü yavaşça kulenin üstüne koydu. Sonra Spin mavi bir küp ekledi. Kule yavaş yavaş yükseldi ve ikisi de artık çok rahattı. Örümcek Adam çok sevindi, çünkü sırayla oynayınca kuleleri yıkılmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi çalıştı"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi çalıştı, çünkü kule düşmek üzereydi.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut ve mecazlı bir anlatım, küçük çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi çalıştı"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi çalıştı, çünkü kule düşmek üzereydi.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0150` birebir aynı, `@degisim: yaprak -> küp` (tutuyorsan), ardından `@onarim: 4842109846d5605f6a84925ebebdb81df5c22a8c`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0151 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0151
- yer: ev (Takımın gizli evi.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'yosun', fiil 'görüşmek', sıfat 'farklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: rüzgar yüksek pencereyi açtı ve yağmur yastıkları ıslattı | pencereye ağ atıp çekti ve pencereyi kapattı
@tohum: orumcek_adam-0151
@degisim: yosun -> yastık
Gizli evde yağmurlu bir sabahtı. Hulk, Örümcek Adam'a "Görüşürüz!" deyip gidecekti ama dışarıda çok yağmur vardı. Sonra rüzgar yukarıdaki pencereyi açtı ve yağmur yerdeki farklı renkli yastıkları ıslattı. "Yastıklar ıslanıyor!" dedi Hulk. Pencere tavanın yanındaydı ve Hulk'tan bile yüksekti. Örümcek Adam pencereye hemen bir ağ attı ve sıkıca çekti. Pencere kapandı. Hulk ıslak yastıkları kenara koydu. İki arkadaş kuru yastıklarla yerde bir kale kurdu. Sonra kalenin içine oturup yağmurun sesini dinlediler. Örümcek Adam ile Hulk çok sevindi, çünkü yağmur artık içeri giremiyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "deyip gidecekti ama dışarıda çok yağmur vardı"
   - Cümle 2: «Hulk, Örümcek Adam'a "Görüşürüz!" deyip gidecekti ama dışarıda çok yağmur vardı.»
   - Açıklama: Hulk'un gitmek üzere olması kuruluyor ama hikayede hiç kullanılmıyor.
   - Açıklama: Hulk'un gitme niyeti kurulup bir daha hiç kullanılmıyor, işlevsiz bir ayrıntı kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0151` birebir aynı, `@degisim: yosun -> yastık` (tutuyorsan), ardından `@onarim: 961e67b2ed0d2e08b428df20cc1fa5a167e515ae`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0152 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0152
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'pantolon', fiil 'erimek', sıfat 'düz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar heykelin pantolonunu yüksek bir kayaya uçurdu | ağını atıp pantolonu geri çekti
@tohum: orumcek_adam-0152
@degisim: erimek -> giydirmek
Rüzgar kumsalda hızlı hızlı esiyordu. Örümcek Adam ile Ghost-Spider düz kumda komik bir heykel yapmıştı. İkisi heykele eski bir pantolon giydirdi ama rüzgar pantolonu uçurdu. Pantolon yüksek bir kayanın ucuna takıldı. "Pantolonu geri alalım!" dedi arkadaşı gülerek. Örümcek Adam ağını kayaya doğru attı. Ağ pantolonu yakaladı. Örümcek Adam ağı yavaşça çekti ve pantolon eline geldi. Sonra pantolonu yeniden heykele giydirdi. "Teşekkürler, Örümcek Adam, heykel yine çok komik oldu!" dedi arkadaşı.
```

**Hakem bulguları (1):**

1. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "dedi arkadaşı gülerek"
   - Cümle 5: «"Pantolonu geri alalım!" dedi arkadaşı gülerek.»
   - Açıklama: İki kahraman birlikte anılırken 'arkadaşı' denmesi konuşanın kim olduğunu belirsiz bırakıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0152` birebir aynı, `@degisim: erimek -> giydirmek` (tutuyorsan), ardından `@onarim: 3ece1668ff75ca5a6b35986b709849d100bc9075`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0153 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0153
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'şişe', fiil 'dayamak', sıfat 'eksik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: büyük bir dalga sürpriz sofraya doğru geliyordu | sofrayı hemen kuru kuma taşıdı
@tohum: orumcek_adam-0153
Dalgalar kumsala gürültüyle vuruyordu. Örümcek Adam, Spin gelmeden kumsalda sürpriz bir sofra kuruyordu. Birden örümcek hissiyle başı karıncalandı ve sofraya gelen büyük dalgayı gördü. Örümcek Adam hemen örtünün dört ucunu topladı. Keki, sepeti ve meyve suyu şişesini örtüyle birlikte kaldırdı. Hepsini sudan uzak, kuru kuma taşıdı. Dalga geldi ama yalnız boş kumu ıslattı. Örümcek Adam örtüyü yeniden serdi. Şişeyi düşmesin diye sepete dayadı. Sofraya baktı, hiçbir şey eksik değildi. Sonra Spin geldi. "Bu sürpriz benim için mi?" diye sordu Spin. "Evet, iyi ki doğdun, Spin!" dedi Örümcek Adam. Örümcek Adam ile Spin kuru kumda oturup keki mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle başı karıncalandı"
   - Cümle 3: «Birden örümcek hissiyle başı karıncalandı ve sofraya gelen büyük dalgayı gördü.»
   - Açıklama: 'Örümcek hissi' soyut, 'başı karıncalandı' deyimsel; 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi' ve 'başı karıncalanmak' soyut/mecazlı anlatım, küçük çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0153` birebir aynı, ardından `@onarim: e49098b50d9c2525560eccee14fe70f69c1413f7`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0154
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'terazi', fiil 'şakalaşmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: arkadaşının kırmızı kovası kayboldu | sesin geldiği yere gidip kovayı buldu
@tohum: orumcek_adam-0154
@degisim: terazi -> kova
Rüzgarlı bir sabah Örümcek Adam ile Hulk kumsalda şakalaşıyordu. Birden Hulk kırmızı kovasını bulamadı. Tam o sırada taşların arasından garip bir tık tık sesi geldi. Örümcek Adam'ın örümcek hissi çalıştı. Sesin geldiği yere hemen yürüdü. Hulk da peşinden gitti. Taşların arasında kırmızı kova vardı. Rüzgar kovayı taşlara çarpıyordu ve tık tık sesi buradan geliyordu. Örümcek Adam kovayı aldı ve Hulk'a verdi. Hulk kovasını tuttu ve kocaman gülümsedi. "Teşekkürler, Örümcek Adam, sen çok iyi bir arkadaşsın!" dedi Hulk.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi çalıştı"
   - Cümle 4: «Örümcek Adam'ın örümcek hissi çalıştı.»
   - Açıklama: 'Örümcek hissi çalıştı' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0154` birebir aynı, `@degisim: terazi -> kova` (tutuyorsan), ardından `@onarim: ab5fe727d63a1de2ee9a2e8f580f624cb90e9845`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0156 (deneme 3 -> 4)

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
@plan: rüzgar ağaçtaki sürpriz süsleri uçurmak üzereydi | süsleri dallara sıkıca bağladı
@tohum: orumcek_adam-0156
Bir sabah Örümcek Adam, Ghost-Spider için kumsalda bir ağaca renkli süsler astı. Birden örümcek hissi ile güçlü bir rüzgarın geleceğini anladı. Rüzgar esti ve süsler dallardan kaymaya başladı. Örümcek Adam hemen her süsü dallara sıkıca bağladı. Rüzgar yine esti ama hiçbir süs uçmadı. Az sonra arkadaşı havada süzülerek kumsala geldi. İki arkadaş ağacın altında karşılaştı. "Sürpriz!" dedi Örümcek Adam. "Bu ağaç çok güzel olmuş!" dedi arkadaşı sevinçle. İkisi ağacın altına oturup renkli süsleri izledi. Örümcek Adam bundan sonra rüzgarlı günlerde süsleri hep sıkıca bağladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile güçlü bir rüzgarın geleceğini anladı"
   - Cümle 2: «Birden örümcek hissi ile güçlü bir rüzgarın geleceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ile"
   - Cümle 2: «Birden örümcek hissi ile güçlü bir rüzgarın geleceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, küçük çocuğa açık değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissi ile güçlü bir rüzgarın geleceğini anladı"
   - Cümle 2: «Birden örümcek hissi ile güçlü bir rüzgarın geleceğini anladı.»
   - Açıklama: Örümcek hissinin uyarısı çözüme katkı vermiyor; Örümcek Adam ancak süsler kaymaya başlayınca harekete geçiyor, özellik işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0156` birebir aynı, ardından `@onarim: fe981440718d418637715a278f65497607d1df61`, sonra gövde.
