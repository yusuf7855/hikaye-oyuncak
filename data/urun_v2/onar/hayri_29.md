# Editör görevi (onarım): Hayri, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hayri | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar29.txt --ad urun_v2`
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

## Kart: Hayri (kaynaklı, kapalı dünya)

- Ad: Hayri (okunuş: hayri; kesme eki okunuşa uyar)
- Kimlik: Hayri, mahallede arkadaşlarıyla maceralar yaşayan, yemek yemeyi çok seven bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Hayri'nin yemek sevgisi paylaşmak, beklemek ya da yemek hazırlamak olarak gösterilir; çok yiyip midesi ağrımaz, kimse onun yemesiyle ya da kilosuyla alay etmez, tanımadığı birinden yiyecek almaz.
- Özellikler:
  - acık: Yemek yemeyi çok sever; sık sık acıkır. (örnek biçimler: acıktı, acıkmıştı)
  - baklava: Mahalledeki baklava dükkanında çalışır. (örnek biçimler: baklava, baklavayı)
  - abart: Olayları abartmayı sever. (örnek biçimler: abarttı, abartarak)
- Yerler:
  - deniz: Mahallenin yakınındaki deniz kıyısı.
  - orman: Şehrin dışında, ağaçların arasındaki kamp yeri.
  - park: Mahallenin çocuk parkı.
  - ev: Mahalledeki evler, sokak ve bahçeler.
    - yan Basri Amca ise: Basri Amca'nın bahçesi; izinsiz girilmez.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Akın: Mert'in küçük kardeşi ve arkadaş grubunun en küçüğü; çok zekidir, hayvanları çok sever. Tür: oğlan; konuşur. Yüzey biçimleri: Akın
  - Mert: Akın'ın ağabeyi; sakin ve düzenlidir, tartışmaları o bitirir. Tür: oğlan; konuşur. Yüzey biçimleri: Mert
  - Kamil: Hayri'nin yakın arkadaşı; uyumayı ve kitap okumayı çok sever, mahalle bakkalına bakar. Sık sık tartışsalar da birbirlerini çok severler. Tür: oğlan; konuşur. Yüzey biçimleri: Kamil
  - Basri Amca: Mahallede yaşar; çabuk kızar ama iyi kalplidir. Bahçesine izin almadan kimsenin girmesini istemez. Tür: amca; konuşur. Yüzey biçimleri: Basri Amca, Basri, amca
  - Yumak: Basri Amca'nın köpeği; onu Akın bulmuş ve Basri Amca'ya vermiştir. Tür: köpek; KONUŞMAZ. Yüzey biçimleri: Yumak, köpek, köpeği
- Dünya kuralları:
  - Mert ile Akın kardeştir, ağabey Mert'tir; hiçbiri Hayri'nin kardeşi değildir.
  - Yumak Basri Amca'nın köpeğidir; Hayri'nin köpeği yoktur.
  - Yumak konuşmaz; havlar, koklar, kuyruğunu sallar.
- Yasak adlar: Hale, Sevim, Rüstem, Fatma Nine, Sadettin, Saadettin, Kuşçu Baba, Ozan, Nuri, Tamtam
- Yasak: Hayri'nin kız kardeşi kartta yoktur; ailesi hikayeye girmez.
- İzinli dünya kelimeleri: mahalle, baklava, bakkal, abart

## Onarılacak hikâyeler

### Hikâye 1: tohum hayri-0085 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0085
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kabuk', fiil 'kurutmak', sıfat 'kırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuru olduğu için yüksek kale yıkıldı | kovayla su getirip kumu ıslattı
@tohum: hayri-0085
@degisim: kurutmak -> ıslatmak
Parkın kum havuzunda Hayri bir kale yapıyordu. Hayri çok yüksek bir kale yapmak istiyordu. Ama kum çok kuruydu ve kale her seferinde yıkıldı. Hayri kırmızı kovasını aldı ve çeşmeye koştu. Hayri abartarak bir kova değil, tam dört kova su getirdi. Suyu döktü ve kumu iyice ıslattı. Islak kum şimdi sıkı sıkı duruyordu. Hayri kovayı kumla doldurdu ve ters çevirdi. Yerdeki kalın bir ağaç kabuğuyla duvarları bastırdı ve düzeltti. Kovayı bir kez daha doldurdu ve üstüne bir kule yaptı. Bu sefer hiçbir şey yıkılmadı. Hayri çok sevindi, çünkü yüksek kalesi artık dimdik duruyordu.
```

**Hakem bulguları (6):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri çok yüksek bir kale"
   - Cümle 2: «Hayri çok yüksek bir kale yapmak istiyordu.»
   - Açıklama: Hayri adı art arda cümlelerde gereksiz tekrarlanıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kale her seferinde yıkıldı"
   - Cümle 3: «Ama kum çok kuruydu ve kale her seferinde yıkıldı.»
   - Açıklama: Tekrarlanan olay için -dı yerine 'yıkılıyordu' olmalı; zaman/görünüş uyumu bozuk.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak bir kova değil"
   - Cümle 5: «Hayri abartarak bir kova değil, tam dört kova su getirdi.»
   - Açıklama: 'Abartarak' yanlış anlamda kullanılmış; abartmak bir şeyi olduğundan büyük anlatmaktır.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bir kova"
   - Cümle 5: «Hayri abartarak bir kova değil, tam dört kova su getirdi.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abartarak bir kova değil, tam dört kova su getirdi"
   - Cümle 5: «Hayri abartarak bir kova değil, tam dört kova su getirdi.»
   - Açıklama: Abartma ayrıntısı olaya bir şey katmıyor ve eylemle anlamca uyuşmuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yerdeki kalın bir ağaç kabuğuyla duvarları bastırdı"
   - Cümle 9: «Yerdeki kalın bir ağaç kabuğuyla duvarları bastırdı ve düzeltti.»
   - Açıklama: Ağaç kabuğu sebepsiz beliriyor ve çözüme kurulmadan dahil ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0085` birebir aynı, `@degisim: kurutmak -> ıslatmak` (tutuyorsan), ardından `@onarim: a0876948328801514e718a1d56962f88277fd1ef`, sonra gövde.

### Hikâye 2: tohum hayri-0089 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0089
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kırıntı', fiil 'yeşermek', sıfat 'hazırlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: köpek çok hızlıydı ve kırıntılar çabuk bitti | çantadan ikinci simidi çıkarıp oyuna devam etti
@tohum: hayri-0089
@degisim: hazırlıklı -> dolu
Hayri parkta Yumak ile koku oyunu oynuyordu. Simit kırıntılarını yeşermiş çimlere saklıyordu, Yumak da onları kokluyor ve buluyordu. Ama Yumak çok hızlıydı ve kırıntılar çabuk bitti. Yumak kuyruğunu salladı ve Hayri'ye baktı. Hayri sık sık acıkırdı, bu yüzden çantası hep doluydu. Çantasında bir simit daha vardı. Simidi ikiye ayırdı ve yarısını kendisi yedi. Öbür yarısını küçük küçük kırıntı yaptı ve çimlere serpti. "Hadi, Yumak, bul bakalım!" dedi Hayri. Yumak burnunu yere yaklaştırdı ve çimlerde koştu. Her kırıntıyı buldukça sevinçle zıpladı ve havladı. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü oyunları yarım kalmamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırıntılarını yeşermiş çimlere saklıyordu"
   - Cümle 2: «Simit kırıntılarını yeşermiş çimlere saklıyordu, Yumak da onları kokluyor ve buluyordu.»
   - Açıklama: 'Yeşermiş' kelimesini 3 yaşındaki bir çocuk bilmez ve çimler için gereksiz ağır bir sözcük.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0089` birebir aynı, `@degisim: hazırlıklı -> dolu` (tutuyorsan), ardından `@onarim: 294da0a1c87db7d5520ad6f9d2910cfdf334e64e`, sonra gövde.

### Hikâye 3: tohum hayri-0090 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0090
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'saman', fiil 'birleştirmek', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kabuğun öbür yarısı yoktu çünkü dalgalar onu kırmıştı | kıyıda dolaşıp öbür yarısını buldu ve birleştirdi
@tohum: hayri-0090
@degisim: saman -> kabuk
Deniz kıyısında ıslak kumun üstünde tuhaf bir kabuk vardı. Hayri kabuğu aldı ve çok beğendi. Ama kabuğun öbür yarısı yoktu, çünkü dalgalar onu kırmıştı. Kabuğun üstünde pembe ve mavi çizgiler vardı. Hayri öbür yarısını bulmak için kıyıda yavaş yavaş yürüdü. Hayri abartarak kumdaki bütün kabuklara tek tek baktı. Sonunda taşların arasında aynı çizgileri olan bir parça gördü. Hayri iki parçayı yan yana koydu ve birleştirdi. Parçalar tam oturdu ve çizgiler bir yıldız şekli yaptı. Hayri kabuğu iki eliyle tuttu ve ona güneşte uzun uzun baktı. Hayri çok sevindi, çünkü tuhaf kabuğun öbür yarısını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak kumdaki bütün"
   - Cümle 6: «Hayri abartarak kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: 'Abartarak' bakmak fiiline anlamca uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak kumdaki"
   - Cümle 6: «Hayri abartarak kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: 'Abartarak' kabuklara bakma eylemine uymuyor; kelime yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kumdaki"
   - Cümle 6: «Hayri abartarak kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak kumdaki bütün kabuklara"
   - Cümle 6: «Hayri abartarak kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: Tohumdaki abartma özelliği olayları abartmak olarak değil kabuklara bakmayı abartmak olarak kullanılıyor ve kartın özellik tanımına uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0090` birebir aynı, `@degisim: saman -> kabuk` (tutuyorsan), ardından `@onarim: 479af543a57ef672ce0df96f5ea6cd7281a4853f`, sonra gövde.

### Hikâye 4: tohum hayri-0092 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0092
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'ipek', fiil 'hızlanmak', sıfat 'resimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: dar yolda beklemek arkadaşına çok sıkıcı geldi | arkadaşı koşarken çok komik sözlerle bağırdı
@tohum: hayri-0092
Hayri ile Kamil ormandaki kamp yerinde koşu oyunu oynuyordu. Kamil bitiş yeri için resimli ipek mendilini alçak bir dala bağladı. Yol çok dardı, sırayla koşacaklardı ama Kamil beklemek istemedi. "Beklemek çok sıkıcı, Hayri," dedi Kamil. "Önce sen başla, Kamil," dedi Hayri. Kamil hemen başladı ve yolun ortasında çok hızlandı. "Bu, ormanın en hızlı koşusu!" diye bağırdı Hayri abartarak. Kamil dala varınca çok güldü. "Sıra sende, Hayri, şimdi bağırma sırası bende!" dedi Kamil. Hayri koşarken Kamil de yüksek sesle bağırdı ve bekledi. İki arkadaş sırayla koşmaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "arkadaşı koşarken çok komik sözlerle bağırdı"
   - Cümle 0 (plan satırı): «dar yolda beklemek arkadaşına çok sıkıcı geldi | arkadaşı koşarken çok komik sözlerle bağırdı»
   - Açıklama: Gövdede Hayri komik sözler değil abartılı bir övgü bağırıyor ve çözüm sırayı Kamil'e vermekle başlıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "resimli ipek mendilini alçak"
   - Cümle 2: «Kamil bitiş yeri için resimli ipek mendilini alçak bir dala bağladı.»
   - Açıklama: Kartın yanlar alanında Kamil'e ait resimli ipek mendil gibi bir eşya yok.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce sen başla, Kamil"
   - Cümle 5: «"Önce sen başla, Kamil," dedi Hayri.»
   - Açıklama: Çözüm beklemenin sıkıcılığına doğrudan yönelmiyor; önce sırayı vermek, sonra bağırmak dolaylı ve dağınık bir çözüm.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye bağırdı Hayri abartarak"
   - Cümle 7: «"Bu, ormanın en hızlı koşusu!" diye bağırdı Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, küçük çocuk bilmez.
   - Açıklama: 'Abartarak' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "diye bağırdı Hayri abartarak"
   - Cümle 7: «"Bu, ormanın en hızlı koşusu!" diye bağırdı Hayri abartarak.»
   - Açıklama: Sorun Kamil'in beklemekten sıkılması ama Hayri Kamil koşarken bağırıyor, bu da beklemenin sıkıcılığına doğrudan yönelmiyor; bekleme sorununu Kamil'in kendi bağırma fikri gideriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0092` birebir aynı, ardından `@onarim: 8ef1e8b5f53fb90fa143f2cbff573cbb4f9139ce`, sonra gövde.

### Hikâye 5: tohum hayri-0093 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0093
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yastık', fiil 'ayrılmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: yastık çok kaygandı ve başından düştü | yastığı düşürmemek için minicik adımlar attı
@tohum: hayri-0093
Bir sabah Hayri parkta komik bir oyun oynuyordu. Evden getirdiği küçük yastığı başının üstünde taşıyarak banktan ağaca yürüyecekti. Ama yastık yumuşak ve kaygandı, ilk adımda başından kayıp düştü. Hayri yastığı yerden aldı, banka döndü ve yeniden başına koydu. Hayri banktan ayrıldı ve bu kez adımlarını abartarak minicik attı. Her adımda bir ayağını havada uzun uzun tuttu. Yastık başının üstünde hiç kıpırdamadı. Hayri yavaş yavaş yürüdü ve sonunda eliyle ağaca dokundu. Sevinçli Hayri, oyunu mutlu mutlu bir kez daha oynadı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "adımlarını abartarak minicik attı"
   - Cümle 5: «Hayri banktan ayrıldı ve bu kez adımlarını abartarak minicik attı.»
   - Açıklama: 'Abartarak' ile 'minicik' çelişiyor, kelime yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "adımlarını abartarak minicik attı"
   - Cümle 5: «Hayri banktan ayrıldı ve bu kez adımlarını abartarak minicik attı.»
   - Açıklama: 'Abartarak minicik' çelişkili ve soyut bir anlatım.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "adımlarını abartarak minicik attı"
   - Cümle 5: «Hayri banktan ayrıldı ve bu kez adımlarını abartarak minicik attı.»
   - Açıklama: Kartın özellik alanı olayları abartmayı söylüyor; burada abartma yalnız adım biçimine dönüşmüş, özellik karttaki gibi kullanılmamış.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bu kez adımlarını abartarak minicik attı"
   - Cümle 5: «Hayri banktan ayrıldı ve bu kez adımlarını abartarak minicik attı.»
   - Açıklama: Sorunun sebebi yastığın kayganlığı ama çözüm kayganlığa değil adımların boyuna yöneliyor ve tek ayak havada beklemek dengeyi bozar.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sevinçli Hayri, oyunu mutlu mutlu"
   - Cümle 9: «Sevinçli Hayri, oyunu mutlu mutlu bir kez daha oynadı.»
   - Açıklama: 'Sevinçli' ve 'mutlu mutlu' aynı duyguyu gereksizce tekrarlıyor.
   - Açıklama: 'Sevinçli' ve 'mutlu mutlu' aynı cümlede gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0093` birebir aynı, ardından `@onarim: 3e671d9842f6979ffed28455236b7eaa41fa5e8d`, sonra gövde.

### Hikâye 6: tohum hayri-0094 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0094
- yer: park (Mahallenin çocuk parkı.)
- tema: kaybolan eşya
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'saksı', fiil 'gerinmek', sıfat 'uslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: rüzgar esti ve şapka başından uçtu | bankın arkasına bakıp şapkayı saksının yanında buldu
@tohum: hayri-0094
@degisim: uslu -> kırmızı
Hayri parktaki bankta oturdu ve keyifle gerindi. O anda rüzgar esti ve kırmızı şapkası başından uçtu. Hayri çevresine baktı ama şapkayı hiçbir yerde göremedi. Hayri biraz abarttı ve şapkayı parkın her yerinde aradı. Ağaçların altına ve kaydırağın yanına koştu. En son eğildi ve bankın arkasına baktı. Orada büyük bir çiçek saksısı duruyordu. Şapka saksının yanına sıkışmıştı. Hayri şapkayı alıp başına sıkıca taktı. Hayri güldü ve çok sevindi, çünkü şapkasını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri biraz abarttı ve"
   - Cümle 4: «Hayri biraz abarttı ve şapkayı parkın her yerinde aradı.»
   - Açıklama: Şapkayı her yerde aramak abartmak değildir; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı ve"
   - Cümle 4: «Hayri biraz abarttı ve şapkayı parkın her yerinde aradı.»
   - Açıklama: 'Abarttı' soyut bir kelime, 3 yaşındaki çocuk bilmez ve burada anlamı belirsiz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abarttı ve şapkayı"
   - Cümle 4: «Hayri biraz abarttı ve şapkayı parkın her yerinde aradı.»
   - Açıklama: Abartma özelliği olayları abartmak olarak değil aramayı abartmak olarak kullanılıyor ve çözüme katkısı yok.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "şapkayı parkın her yerinde aradı"
   - Cümle 4: «Hayri biraz abarttı ve şapkayı parkın her yerinde aradı.»
   - Açıklama: Çözüm şapkanın uçtuğu banka doğrudan yönelmiyor, önce parkın her yerinde dolaşan fazladan adımlar sürüyor.
   - Açıklama: Çözüm rüzgarın şapkayı uçurduğu yere yönelmiyor; ağaçlar, kaydırak ve bank arasında ikiden fazla adımlı gelişigüzel bir arama var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0094` birebir aynı, `@degisim: uslu -> kırmızı` (tutuyorsan), ardından `@onarim: d72c8a27f16aceddce39384dd2992fa8aa0c242e`, sonra gövde.

### Hikâye 7: tohum hayri-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0095
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'sandalye', fiil 'bükmek', sıfat 'yardımsever'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpek devrilen bir sandalyenin ayakları arasına sıkıştı | dizlerini büküp sandalyeyi yavaşça kaldırdı
@tohum: hayri-0095
Deniz kıyısında bir köpek durmadan havlıyordu. Yardımsever Hayri sese doğru koştu ve Yumak'ı gördü. Yumak koşarken boş bir sandalyeye çarpmıştı. Sandalye devrilmişti ve Yumak sandalyenin ayakları arasına sıkışmıştı. Yumak çıkmak için çok uğraştı ama kurtulamadı. Hayri sandalyeye baktı ve biraz abarttı. "Yumak, bu sandalye bir kaya kadar ağır!" dedi Hayri. Bu yüzden dizlerini büktü ve sandalyeyi iki eliyle sıkıca tuttu. Sonra sandalyeyi yavaşça yukarı kaldırdı. Yumak hemen dışarı çıktı ve kumda zıpladı. Hayri sandalyeyi düz bir şekilde kuma koydu. Yumak koşup Hayri'nin elini yaladı. "Haydi, Yumak, şimdi birlikte oynayalım!" dedi Hayri.
```

**Hakem bulguları (8):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Yardımsever Hayri sese doğru koştu"
   - Cümle 2: «Yardımsever Hayri sese doğru koştu ve Yumak'ı gördü.»
   - Açıklama: Çocuk durmadan havlayan, henüz tanımadığı bir köpeğin sesine doğru koşuyor; taklit edilince tehlikeli.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yardımsever Hayri sese doğru koştu"
   - Cümle 2: «Yardımsever Hayri sese doğru koştu ve Yumak'ı gördü.»
   - Açıklama: Tohumdaki özellik abartmak; yardımseverlik kartın özellikler alanında olmayan ikinci bir özellik olarak ekleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yumak sandalyenin ayakları arasına sıkışmıştı"
   - Cümle 4: «Sandalye devrilmişti ve Yumak sandalyenin ayakları arasına sıkışmıştı.»
   - Açıklama: Asıl sorun olan sıkışma ilk 3 cümlede değil 4. cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Sandalye devrilmişti ve Yumak sandalyenin ayakları arasına sıkışmıştı.»
   - Açıklama: Yumak'ın sandalyeye sıkıştığı sorun ilk üç cümlede değil ancak dördüncü cümlede açıkça söyleniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "baktı ve biraz abarttı"
   - Cümle 6: «Hayri sandalyeye baktı ve biraz abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu sandalye bir kaya kadar ağır!"
   - Cümle 7: «"Yumak, bu sandalye bir kaya kadar ağır!" dedi Hayri.»
   - Açıklama: Abartılı benzetme küçük çocuğa uygun olmayan bir mecaz.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kaya kadar ağır"
   - Cümle 7: «"Yumak, bu sandalye bir kaya kadar ağır!" dedi Hayri.»
   - Açıklama: Benzetme ve abartı mecazdır, küçük çocuk için uygun değil.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden dizlerini büktü"
   - Cümle 8: «Bu yüzden dizlerini büktü ve sandalyeyi iki eliyle sıkıca tuttu.»
   - Açıklama: Hayri'nin dikkatli kaldırışı gerçek bir sebepten değil kendi abartısından çıkarılıyor; boş sandalye aslında hafif.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0095` birebir aynı, ardından `@onarim: f968fd6230de974e36001c7b154bf8cde0b20c84`, sonra gövde.

### Hikâye 8: tohum hayri-0096 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0096
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'reçel', fiil 'ovmak', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: ikisi aynı anda kum döktü ve katlar karıştı | baklava yapar gibi sırayla tek tek serdiler
@tohum: hayri-0096
@degisim: reçel -> kum
Bir sabah Hayri ile Akın parkta kumdan baklava yapıyordu. Çiçekli oyuncak bir tepsiye kumdan katlar koyacaklardı. Ama ikisi aynı anda kum döktü ve katlar karıştı. Hayri baklava dükkanında baklavayı hep kat kat, tek tek yapardı. Burada da tepsiyi boşalttı ve ilk katı kendisi serdi. Sonra sırayı Akın'a verdi ve bekledi. Akın ikinci katı serdi ve üstünü eliyle ovdu. Böylece sırayla tam altı kat yaptılar. Bu kez katlar hiç bozulmadı. Akın en üste parmağıyla küçük çizgiler yaptı. Hayri ile Akın çok sevindi, çünkü kumdan baklavayı sırayla yapmışlardı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi aynı anda kum döktü ve katlar karıştı"
   - Cümle 3: «Ama ikisi aynı anda kum döktü ve katlar karıştı.»
   - Açıklama: Kumdan katların karışması önemsiz ve belirsiz bir sorun; kum katları zaten birbirinden ayırt edilemez.
   - Açıklama: Aynı kumdan yapılan katların karışması akla yatkın ve önemli bir sorun değil, çünkü kum katları zaten birbirinden ayırt edilemez.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üstünü eliyle ovdu"
   - Cümle 7: «Akın ikinci katı serdi ve üstünü eliyle ovdu.»
   - Açıklama: Kum katı ovulmaz; 'düzeltti' ya da 'bastırdı' olmalı, fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0096` birebir aynı, `@degisim: reçel -> kum` (tutuyorsan), ardından `@onarim: 98af916f2e6bece326d1d3f614819e8dfdcf69a3`, sonra gövde.

### Hikâye 9: tohum hayri-0097 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0097
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'takvim', fiil 'yerleşmek', sıfat 'ıslak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca sırasını beklerken sıkıldı ve kızdı | beklerken yemesi için sandviç hazırladı
@tohum: hayri-0097
@degisim: takvim -> sandviç
Hayri ile Basri Amca kamp yerinde kozalak atma oyunu oynuyordu. Kozalakları sırayla eski bir kovaya atıyorlardı. Ama Basri Amca sırasını beklerken sıkıldı ve kızdı. "Beklemek çok uzun sürüyor, Hayri," dedi Basri Amca. O sırada Hayri de acıkmıştı. Çantasından ekmek ve peynir çıkarıp iki sandviç hazırladı. "Beklerken bunu yiyin, Basri Amca," dedi Hayri. Çimenler ıslaktı, bu yüzden Basri Amca kuru bir kütüğe yerleşti. Amca sandviçini yerken Hayri kozalağı attı. Sonra Basri Amca attı, Hayri de kütükte sandviçini yedi. "Böyle beklemek çok güzel, Hayri," dedi Basri Amca. İkisi sırayla kozalak atmaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Basri Amca sırasını beklerken sıkıldı ve kızdı"
   - Cümle 3: «Ama Basri Amca sırasını beklerken sıkıldı ve kızdı.»
   - Açıklama: İki kişilik sıra oyununda tek atış beklemek kızacak kadar uzun değil; sorunun sebebi akla yatkın değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Beklemek çok uzun sürüyor, Hayri"
   - Cümle 4: «"Beklemek çok uzun sürüyor, Hayri," dedi Basri Amca.»
   - Açıklama: İki kişilik sırayla atma oyununda bekleme çok kısadır; amcanın sıkılıp kızması akla yatkın bir sebep değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "O sırada Hayri de acıkmıştı"
   - Cümle 5: «O sırada Hayri de acıkmıştı.»
   - Açıklama: 'de' başka birinin de acıktığını gösteriyor ama başka acıkan yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çimenler ıslaktı, bu yüzden Basri Amca kuru bir kütüğe yerleşti"
   - Cümle 8: «Çimenler ıslaktı, bu yüzden Basri Amca kuru bir kütüğe yerleşti.»
   - Açıklama: Islak çimen ve kütük ayrıntısı sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Islak çimen ve kütük ayrıntısı soruna ya da çözüme hiçbir katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0097` birebir aynı, `@degisim: takvim -> sandviç` (tutuyorsan), ardından `@onarim: eeac0e4900ae79beddf865bccd461018d56e0fc4`, sonra gövde.
