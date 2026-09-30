# Editör görevi (onarım): Hayri, onarım partisi 53

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar53.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar53.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0150
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'tablo', fiil 'dolanmak', sıfat 'buzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: arkadaşı tablo yüzünden önündeki buzu göremedi | bağırıp onu durdurdu ve buzun etrafından dolandılar
@tohum: hayri-0150
Soğuk bir rüzgar esiyordu. Hayri evinin önünde arkadaşı Kamil'i gördü. Kamil iki eliyle büyük bir tablo taşıyordu ve önündeki buzlu yeri göremiyordu. "Dur, Kamil, önünde kocaman bir buz var!" diye bağırdı Hayri. Kamil hemen durdu ve yana eğilip baktı. "Buz kocaman değil, Hayri, biraz abarttın ama yer çok kaygan," dedi Kamil. Hayri tabloyu bir ucundan tuttu, Kamil de öbür ucundan. İkisi buzun etrafından yavaşça dolandı. Birlikte Kamil'in kapısına kadar yürüdüler. Hayri çok sevindi, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "biraz abarttın ama yer"
   - Cümle 6: «"Buz kocaman değil, Hayri, biraz abarttın ama yer çok kaygan," dedi Kamil.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri, biraz abarttın"
   - Cümle 6: «"Buz kocaman değil, Hayri, biraz abarttın ama yer çok kaygan," dedi Kamil.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Birlikte Kamil'in kapısına kadar yürüdüler"
   - Cümle 9: «Birlikte Kamil'in kapısına kadar yürüdüler.»
   - Açıklama: Hikaye Hayri'nin evinin önünde başlıyor ama Kamil'in kapısında bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0150` birebir aynı, ardından `@onarim: d80426fee84e81b5dc400134f2733a2fd68efee3`, sonra gövde.

### Hikâye 2: tohum hayri-0152 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0152
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tahta', fiil 'güldürmek', sıfat 'biberli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: dalga kaleyi yıktı ve arkadaşı üzüldü | tahtanın üstüne sandviçlerden bir kale yaptı
@tohum: hayri-0152
Deniz kıyısında Hayri ile Mert düz bir tahtanın yanında kumdan kale yapmıştı. Ama küçük bir dalga geldi ve kaleyi yıktı. Mert buna çok üzüldü. Hayri, Mert'i güldürmek için bir sürpriz hazırlamak istedi. "Mert, gözlerini kapat ve bekle!" dedi Hayri. Hayri acıkmıştı ve çantasında biberli sandviçler vardı. Düz tahtayı suyun uzağına koydu. Sandviçleri tahtanın üstüne üst üste dizdi ve bir kale yaptı. "Sürpriz, Mert, gel bak!" dedi Hayri. Mert sandviçten kaleyi görünce çok güldü. İkisi yan yana oturup sandviçleri paylaştı. "Teşekkürler, Hayri, bu en güzel sürpriz!" dedi Mert.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri acıkmıştı ve çantasında"
   - Cümle 6: «Hayri acıkmıştı ve çantasında biberli sandviçler vardı.»
   - Açıklama: Hayri'nin acıkması kurulup kullanılmıyor, sandviçler de çözüme sebepsizce geliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sandviçleri tahtanın üstüne üst üste dizdi"
   - Cümle 8: «Sandviçleri tahtanın üstüne üst üste dizdi ve bir kale yaptı.»
   - Açıklama: Çözüm yıkılan kumdan kaleye yönelmiyor, sorunu sandviçten bir kaleyle dolaylı olarak geçiştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0152` birebir aynı, ardından `@onarim: a345dc787336959aedf542c5fbf31b82b4156a84`, sonra gövde.

### Hikâye 3: tohum hayri-0153 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0153
- yer: park (Mahallenin çocuk parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'heykel', fiil 'aydınlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: doğum gününde yağmur yağdı ve arkadaşı ıslandı ve üzüldü | sakladığı kurabiyelerle ona sürpriz yaptı
@tohum: hayri-0153
@degisim: heykel -> kurabiye
Bir sabah Hayri ile Akın parktaydı ve o gün Akın'ın doğum günüydü. Hayri'nin çantasında doğum günü için bir kutu kurabiye vardı. Ama birden kısa bir yağmur yağdı ve Akın sırılsıklam oldu. Akın, doğum gününde ıslandığı için çok üzüldü. Yağmur bitince güneş çıktı ve park aydınlandı. Hayri çok acıkmıştı ama kurabiyelere hiç dokunmamıştı. Şimdi kutuyu çıkardı ve Akın'ın önünde açtı. "İyi ki doğdun, Akın!" dedi Hayri. Akın kurabiyelere baktı ve sevinçle güldü. "Hepsi benim için mi?" diye sordu Akın. "Hayır, ikimiz için," dedi Hayri. Sonra Hayri ile Akın kurabiyeleri paylaştı ve mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şimdi kutuyu çıkardı ve Akın'ın önünde açtı"
   - Cümle 7: «Şimdi kutuyu çıkardı ve Akın'ın önünde açtı.»
   - Açıklama: Sorunun sebebi Akın'ın yağmurda ıslanması ama çözüm ıslaklığa değil yalnız üzüntüye kurabiyeyle yöneliyor.
   - Açıklama: Sorunun sebebi yağmur ve ıslanmak ama çözüm kurabiye vermek; sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0153` birebir aynı, `@degisim: heykel -> kurabiye` (tutuyorsan), ardından `@onarim: 8b536ef7e3ba1bafd99d385c9bb63182af5fc700`, sonra gövde.

### Hikâye 4: tohum hayri-0155 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0155
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'fiyonk', fiil 'yuvarlamak', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kazdığı çukura su gelmedi çünkü çukur denizden uzaktı | denize kadar uzun bir kanal kazdı
@tohum: hayri-0155
@degisim: fiyonk -> top
Deniz kıyısında Hayri kumda küçük bir çukur kazmıştı. Hafif topunu bu küçük havuzda yüzdürmek istiyordu. Ama çukura hiç su gelmedi, çünkü çukur denizden çok uzaktaydı. Hayri bu kez abarttı ve denize kadar kocaman bir kanal kazdı. Sonra çukurun yanına oturup bekledi. Bir dalga geldi ve su çukura doğru akmaya başladı. Su yavaş yavaş çukura doldu. Hayri topunu çukura doğru yuvarladı. Top suyun üstünde yüzmeye başladı. Hayri topu parmağıyla itti ve havuzunda mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri bu kez abarttı"
   - Cümle 4: «Hayri bu kez abarttı ve denize kadar kocaman bir kanal kazdı.»
   - Açıklama: 'Abarttı' burada yanlış anlamda kullanılmış; Hayri abartmıyor, uzun bir kanal kazıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri bu kez abarttı"
   - Cümle 4: «Hayri bu kez abarttı ve denize kadar kocaman bir kanal kazdı.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bu kelimeyi bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bu kez abarttı ve denize kadar kocaman bir kanal kazdı"
   - Cümle 4: «Hayri bu kez abarttı ve denize kadar kocaman bir kanal kazdı.»
   - Açıklama: Kartın özellik alanında abartma olayları abartarak anlatmaktır; burada iş yapmayı aşırıya kaçırmak anlamında kullanılmış.
   - Açıklama: Kartın özellik alanı olayları abartmayı (sözle büyütmeyi) söylüyor; burada abartma aşırı iş yapmak olarak kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0155` birebir aynı, `@degisim: fiyonk -> top` (tutuyorsan), ardından `@onarim: 827d81e92831fda585f2a22a942d2463135645ed`, sonra gövde.

### Hikâye 5: tohum hayri-0157 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0157
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'koza', fiil 'unutmak', sıfat 'faydalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca çadırın ipini kozanın olduğu dala bağlamak istedi | bağırıp amcayı durdurdu ve ip başka ağaca bağlandı
@tohum: hayri-0157
@degisim: faydalı -> küçük
Hayri, Basri Amca ile ormandaki kamp yerinde çadır kuruyordu. Basri Amca çadırın ipini bir ağaç dalına bağlamak istedi. Ama o dalda küçük bir koza vardı ve Basri Amca onu görmemişti. "Dur, amca, o dalda kocaman bir koza var!" diye bağırdı Hayri. Basri Amca hemen durdu ve dala dikkatle baktı. "Koza kocaman değil, Hayri, biraz abarttın ama ona dokunmayalım," dedi Basri Amca. Sonra ipi başka bir ağaca bağladı. Hayri de çadırın öbür ucunu tuttu. Çadır kuruldu ve koza dalında kaldı. "İyi ki bağırdın, Hayri, bunu hiç unutmayacağım!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "biraz abarttın ama ona"
   - Cümle 6: «"Koza kocaman değil, Hayri, biraz abarttın ama ona dokunmayalım," dedi Basri Amca.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0157` birebir aynı, `@degisim: faydalı -> küçük` (tutuyorsan), ardından `@onarim: 530801937f0877544af17964e28e899f06a6f6f7`, sonra gövde.

### Hikâye 6: tohum hayri-0159 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0159
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yama', fiil 'gezmek', sıfat 'ilginç'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: rüzgar topu yuvarladı ve top kayboldu | kumdaki izin peşinden gidip topu buldu
@tohum: hayri-0159
Rüzgar hızlı hızlı esiyordu. Hayri, köpek Yumak ile parkta geziyordu. Birden Hayri'nin yamalı topu elinden düştü ve rüzgarla uzağa yuvarlandı. Hayri etrafa baktı ama topu göremedi. "Yumak, topum çok uzağa, denize kadar gitti!" dedi Hayri. Yumak kuyruğunu salladı ve havladı. Sonra Hayri kumun üstünde ilginç, ince bir iz gördü. İz salıncakların arkasına doğru gidiyordu. Hayri, bu izi topun bıraktığını düşündü ve izin peşinden yürüdü. İz bankın altında bitiyordu. Hayri eğildi ve bankın altında yamalı topunu buldu. Yumak topu görünce sevinçle havladı. "Bak, Yumak, biraz abartmışım, topum denizde değil, burada!" dedi Hayri gülerek.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yumak, biraz abartmışım"
   - Cümle 13: «"Bak, Yumak, biraz abartmışım, topum denizde değil, burada!" dedi Hayri gülerek.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "biraz abartmışım, topum denizde"
   - Cümle 13: «"Bak, Yumak, biraz abartmışım, topum denizde değil, burada!" dedi Hayri gülerek.»
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0159` birebir aynı, ardından `@onarim: 8203c4bf1ca943f240c4a2f5146a7d1b203e36b1`, sonra gövde.

### Hikâye 7: tohum hayri-0161 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0161
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'mikroskop', fiil 'susamak', sıfat 'yakın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: köpek çok susamıştı ama şişeden su içemedi | boş baklava tepsisine köpek için su döktü
@tohum: hayri-0161
@degisim: mikroskop -> tepsi
Parkta sıcak bir öğle vaktiydi. Hayri boş bir baklava tepsisini çalıştığı yakın dükkana götürüyordu. Bankın yanında Yumak çok susamıştı ama su içecek kabı yoktu. Hayri çantasından su şişesini çıkardı. "Gel, Yumak, biraz su iç," dedi Hayri. Ama Yumak dar şişeden su içemedi. Hayri tepsiyi yere koydu ve içine su döktü. Yumak hemen yaklaştı ve suyu içti. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. "Afiyet olsun, Yumak, bol bol iç!" dedi Hayri gülerek.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çalıştığı yakın dükkana götürüyordu"
   - Cümle 2: «Hayri boş bir baklava tepsisini çalıştığı yakın dükkana götürüyordu.»
   - Açıklama: 'Yakın dükkana' dilbilgisel olarak aksak; 'yakındaki dükkana' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0161` birebir aynı, `@degisim: mikroskop -> tepsi` (tutuyorsan), ardından `@onarim: e880818220f0ac439e61425b84f476aab5efc5f6`, sonra gövde.

### Hikâye 8: tohum hayri-0163 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0163
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'waffle', fiil 'dökmek', sıfat 'üzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: küçük bir dalga peynirli ekmeği ıslattı | ilk kez waffle denedi ve sevdi
@tohum: hayri-0163
Bir sabah Hayri deniz kıyısında kumdan bir kale yapıyordu. Havlunun üstünde peynirli ekmeği, çantasında da bir waffle vardı. Birden küçük bir dalga geldi ve ekmeği ıslattı. Hayri çok acıkmıştı ve üzgün bir yüzle ıslak ekmeğe baktı. Başka bir yiyecek bulmak için çantasını havlunun kuru köşesine döktü. Hayri daha önce hiç waffle yememişti. Hayri onu küçük parçalara böldü ve ilk parçayı yavaşça tattı. Bu waffle yumuşak ve tatlıydı. Karnı doyunca Hayri kumdan kalesini mutlu mutlu yapmaya devam etti.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri daha önce hiç waffle yememişti"
   - Cümle 6: «Hayri daha önce hiç waffle yememişti.»
   - Açıklama: Waffle baştan Hayri'nin kendi çantasında duruyor ama hiç waffle yemediği söyleniyor; bu tutarsız kalıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hayri onu küçük parçalara"
   - Cümle 7: «Hayri onu küçük parçalara böldü ve ilk parçayı yavaşça tattı.»
   - Açıklama: 'Onu' zamiri önceki cümledeki genel 'waffle'a dayanıyor; bulunan belirli waffle hiç anılmadı.
   - Açıklama: 'Onu' zamiri önceki cümledeki genel 'waffle' sözüne dayanıyor; çantadaki waffle'ı bulduğu söylenmediği için gösterdiği şey belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0163` birebir aynı, ardından `@onarim: 777856a2a12c503d3c1ea19df6f24baa54b97540`, sonra gövde.

### Hikâye 9: tohum hayri-0164 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0164
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'karpuz', fiil 'kaplamak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: karpuz dilimi elden kayıp toprağa düştü | baklavalarından birini arkadaşına verdi
@tohum: hayri-0164
@degisim: aceleci -> ıslak
Hayri, Kamil ile evin önündeki bahçede yan yana oturuyordu. Hayri'nin tabağında iki dilim baklava, Kamil'in elinde bir dilim karpuz vardı. Ama ıslak karpuz Kamil'in elinden kaydı ve toprağa düştü. Kırmızı karpuzu baştan sona toprak kapladı. Kamil boş eline üzgün üzgün baktı. Hayri, Kamil'in eli boş kalmasın diye baklavalarından birini ona verdi. Kamil baklavayı aldı ve sevinçle gülümsedi. İki arkadaş baklavalarını birlikte yedi. Sonra yere düşen karpuzu çöpe attılar. Kamil, Hayri'ye tatlı için teşekkür etti. Hayri bundan sonra baklavasını her zaman arkadaşlarıyla paylaştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri'nin tabağında iki dilim baklava"
   - Cümle 2: «Hayri'nin tabağında iki dilim baklava, Kamil'in elinde bir dilim karpuz vardı.»
   - Açıklama: Tohum özelliği baklava dükkanında çalışmak, fakat hikayede özellik yalnız yiyecek olarak geçiyor ve karttaki gibi kullanılmıyor.
   - Açıklama: Kart özelliği baklava dükkanında çalışmak; hikayede dükkan ya da çalışma yok, baklava yalnız yiyecek olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0164` birebir aynı, `@degisim: aceleci -> ıslak` (tutuyorsan), ardından `@onarim: f2ea97d435be4c475e83a1dafe1d2335d63a6427`, sonra gövde.

### Hikâye 10: tohum hayri-0166 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0166
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'iplik', fiil 'rahatlatmak', sıfat 'çekingen'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kutuyu çeken ince iplik koptu | cebindeki kalın kırmızı ipi kutuya bağladı
@tohum: hayri-0166
@degisim: çekingen -> kırmızı
Rüzgar hafif hafif esiyordu. Hayri parkta boş bir baklava kutusunu ipliğe bağlamış, araba gibi çekiyordu. Ama kutu bir taşa takıldı ve ince iplik koptu. Hayri kopan ipliğe üzgün üzgün baktı. Sonra elini cebine soktu ve kutunun kalın, kırmızı ipini buldu. Bu ipi dükkanda kutudan çözmüş, sonra unutmuştu. Hayri kırmızı ipi kutuya sıkıca bağladı. İpi bir kez çekip denedi. İp kopmadı ve bu Hayri'yi çok rahatlattı. Hayri kutuyu kaydırağın etrafında hızlı hızlı çekti. Kutu her adımda zıpladı ve Hayri kahkahalarla güldü. Çok mutluydu, çünkü araba oyunu yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu Hayri'yi çok rahatlattı"
   - Cümle 9: «İp kopmadı ve bu Hayri'yi çok rahatlattı.»
   - Açıklama: 'Rahatlattı' soyut bir duygu kelimesi; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Soyut 'bu' öznesi ve 'rahatlattı' küçük çocuk için soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0166` birebir aynı, `@degisim: çekingen -> kırmızı` (tutuyorsan), ardından `@onarim: d028a0fe69aba84d4efc080ea24b4bf9354b7bc7`, sonra gövde.

### Hikâye 11: tohum hayri-0167 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0167
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'uçak', fiil 'değiştirmek', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kağıt uçak çok hafifti ve hemen düşüyordu | yemek kutusunun lastiğini uçağın burnuna taktı
@tohum: hayri-0167
Hayri deniz kıyısında Basri Amca'yı gördü. Basri Amca mavi bir kağıttan uçak yapmıştı. Ama uçak çok hafifti ve havada sallanıp hemen kuma düşüyordu. Basri Amca kağıdı iki kez değiştirdi ama uçak yine uçmadı. Hayri acıkmıştı ve yemek kutusunu açacaktı. Kutunun etrafında küçük bir lastik vardı. Hayri, uçağın burnu biraz ağır olursa düz uçar diye düşündü. Lastiği kutudan çıkardı ve uçağın burnuna taktı. Basri Amca uçağı yeniden fırlattı. Mavi uçak bu kez uzağa kadar düz uçtu. Basri Amca gülerek ellerini çırptı. Sonra Hayri kutuyu açtı ve ekmeğini Basri Amca ile paylaştı. İkisi de çok sevindi, çünkü uçak sonunda düz uçmuştu.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yemek kutusunun lastiğini uçağın burnuna taktı"
   - Cümle 0 (plan satırı): «kağıt uçak çok hafifti ve hemen düşüyordu | yemek kutusunun lastiğini uçağın burnuna taktı»
   - Açıklama: Plan lastiğin takıldığını söylüyor ama gövdede bu olay yok.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hayri acıkmıştı ve yemek kutusunu açacaktı"
   - Cümle 5: «Hayri acıkmıştı ve yemek kutusunu açacaktı.»
   - Açıklama: Uçak sorununun yanına Hayri'nin açlığı ikinci bir ihtiyaç olarak ekleniyor ve sonda ayrıca çözülüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutunun etrafında küçük bir lastik vardı"
   - Cümle 6: «Kutunun etrafında küçük bir lastik vardı.»
   - Açıklama: Lastik işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor ve uçak sebepsizce düz uçuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0167` birebir aynı, ardından `@onarim: a25ad389508203cd36abca37a3c310eef30ae6db`, sonra gövde.

### Hikâye 12: tohum hayri-0170 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0170
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'damla', fiil 'büyümek', sıfat 'çizgili'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: yolun ortasındaki minik çiçek güvende değildi | çevresine taşlardan kocaman bir çember yaptı
@tohum: hayri-0170
@degisim: damla -> taş
Bir sabah Hayri parkta salıncakların yanında yürüyordu. Birden yolun ortasında minik bir çiçek gördü. Ama burası bir yoldu ve çocuklar çiçeğe basabilirdi. Çiçeğin çizgili iki küçük yaprağı vardı. Hayri onun büyümesini çok istedi. Hayri abartarak parktaki bütün çocukların buraya koşacağını düşündü. Bu yüzden çiçeğin çevresine taşlardan kocaman bir çember yaptı. Bu büyük çember uzaktan bile görünüyordu. Artık yoldan geçen herkes çiçeği kolayca görecekti. Hayri çok sevindi, çünkü çiçek artık güvendeydi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çiçeğin çizgili iki küçük yaprağı vardı"
   - Cümle 4: «Çiçeğin çizgili iki küçük yaprağı vardı.»
   - Açıklama: Yaprakların çizgili olması kuruluyor ama olayda hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak parktaki bütün"
   - Cümle 6: «Hayri abartarak parktaki bütün çocukların buraya koşacağını düşündü.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime; düşünmeyle birlikte kullanımı da tuhaf.
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0170` birebir aynı, `@degisim: damla -> taş` (tutuyorsan), ardından `@onarim: 649cd09586b0e18be13cf3976032072fb5624e17`, sonra gövde.
