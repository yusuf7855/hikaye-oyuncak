# Editör görevi (onarım): Hayri, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0007 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0007
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'patlıcan', fiil 'doyurmak', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: plastik patlıcan düştü ve çimlerde kayboldu | yere uzanıp nane yapraklarının altında buldu
@tohum: hayri-0007
Bir sabah Hayri ile Mert evin bahçesinde lokanta oyunu oynuyordu. Hayri, Mert'i doyurmak için tabağa plastik bir patlıcan koydu. Ama Mert tabağı alırken patlıcan düştü ve uzun çimlerde kayboldu. Mert çok üzüldü. Hayri, Mert'i güldürmek için abarttı ve patlıcanı karpuz kadar büyük anlattı. Mert bunu duyunca güldü. Hayri yere uzandı ve çimlerin arasına dikkatle baktı. Kokulu nane yapraklarının altında mor bir şey gördü. Kaybolan plastik patlıcan orada duruyordu. Hayri onu çıkardı ve yeniden tabağa bıraktı. Mert bu kez tabağı iki eliyle sıkıca tuttu. İkisi de çok sevindi, çünkü lokanta oyunları yeniden başlamıştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "patlıcanı karpuz kadar büyük anlattı"
   - Cümle 5: «Hayri, Mert'i güldürmek için abarttı ve patlıcanı karpuz kadar büyük anlattı.»
   - Açıklama: 'büyük anlattı' eksik bir yapı; 'büyük olduğunu anlattı' olmalı.
   - Açıklama: Yapı bozuk; 'patlıcanın karpuz kadar büyük olduğunu anlattı' olmalı.
   - Açıklama: Yapı bozuk; 'patlıcanı karpuz kadar büyükmüş gibi anlattı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mert'i güldürmek için abarttı"
   - Cümle 5: «Hayri, Mert'i güldürmek için abarttı ve patlıcanı karpuz kadar büyük anlattı.»
   - Açıklama: 'Abartmak' soyut bir kavram, küçük çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "patlıcanı karpuz kadar büyük anlattı"
   - Cümle 5: «Hayri, Mert'i güldürmek için abarttı ve patlıcanı karpuz kadar büyük anlattı.»
   - Açıklama: Abartma sahnesi patlıcanın bulunmasına hiçbir katkı yapmayan işlevsiz bir ara olay.
   - Açıklama: Abartma ve güldürme olayı aramaya hiçbir katkı yapmayan işlevsiz bir ara ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0007` birebir aynı, ardından `@onarim: c04c66cfef3ea6299b2cc691e816345ed1a6b8a9`, sonra gövde.

### Hikâye 2: tohum hayri-0011 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0011
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kristal', fiil 'fısıldamak', sıfat 'eskimiş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: bulut dağılıyordu ve arkadaşı onu görmemişti | arkadaşına bağırıp onu hemen yanına çağırdı
@tohum: hayri-0011
@degisim: kristal -> kabuk
Deniz kıyısında rüzgar hafif hafif esiyordu. Hayri gökyüzünde gemiye benzeyen bir bulut gördü. Ama bulut yavaş yavaş dağılıyordu ve Akın onu daha görmemişti. Akın uzakta, kumda eskimiş bir kovaya kabuk topluyordu. Hayri bulutu hemen Akın'a göstermek istedi. "Akın, koş, gökyüzünde dünyanın en büyük gemisi var!" diye bağırdı Hayri. Hayri biraz abartıyordu ama Akın hemen koştu. İkisi yan yana durdu ve buluta baktı. "Çok güzel, Hayri, iyi ki beni çağırdın," diye fısıldadı Akın. Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartıyordu ama"
   - Cümle 7: «Hayri biraz abartıyordu ama Akın hemen koştu.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı"
   - Cümle 10: «Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı.»
   - Açıklama: 'Bundan sonra' alışkanlık bildirdiği için fiil 'çağırırdı' olmalı; kip uyumsuz.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı"
   - Cümle 10: «Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor; tek seferlik -dı yerine 'çağırırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0011` birebir aynı, `@degisim: kristal -> kabuk` (tutuyorsan), ardından `@onarim: 15a63321f8adf92320f794382b725280b2769429`, sonra gövde.

### Hikâye 3: tohum hayri-0012 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0012
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çöp', fiil 'yaklaşmak', sıfat 'kilitli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: evin anahtarı düştü ve kayboldu | çöp kutusunun yanına eğilip anahtarı buldu
@tohum: hayri-0012
Evin bahçesinde Hayri, kapının önünde üzgün duran Kamil'e yaklaştı. Kapı kilitliydi ve Kamil anahtarı bulamıyordu. "Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil. "Eyvah, anahtar yoksa bahçede uyuyacaksın!" dedi Hayri. Hayri yine abartıyordu ve Kamil buna güldü. Sonra Hayri çöp kutusunun yanına gitti ve yere eğildi. Kutunun arkasında parlayan küçük bir anahtar vardı. Hayri anahtarı aldı ve Kamil'e uzattı. Kamil kapıyı hemen açtı. "Teşekkürler, Hayri, sen çok iyi bir arkadaşsın!" dedi Kamil.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abartıyordu"
   - Cümle 5: «Hayri yine abartıyordu ve Kamil buna güldü.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yine abartıyordu ve"
   - Cümle 5: «Hayri yine abartıyordu ve Kamil buna güldü.»
   - Açıklama: Tohumdaki abartma özelliği yalnız şaka olarak geçiyor, anahtarın bulunmasında işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yine abartıyordu ve Kamil buna güldü"
   - Cümle 5: «Hayri yine abartıyordu ve Kamil buna güldü.»
   - Açıklama: Tohumdaki abartma özelliği yalnız şaka olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0012` birebir aynı, ardından `@onarim: c5bec5c19a7377de5c50f3f4aeaeb658623cccdf`, sonra gövde.

### Hikâye 4: tohum hayri-0013 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0013
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'delik', fiil 'şişirmek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: top hep sönüyordu çünkü üstünde küçük bir delik vardı | deliğe bant yapıştırıp topu yeniden şişirdi
@tohum: hayri-0013
@degisim: temkinli -> yavaş
Rüzgar esiyordu. Hayri deniz kıyısında renkli plaj topunu şişirmeye çalışıyordu. Ama top hep sönüyordu, çünkü üstünde küçük bir delik vardı. Mahalleden tanıdığı köpek Yumak topa yavaş adımlarla yaklaştı ve onu kokladı. Hayri biraz düşündü. Hayri baklava dükkanında kutuları hep bantla kapatırdı. Bu yüzden cebinde her zaman bir parça bant taşırdı. Hayri bandı deliğin üstüne sıkıca yapıştırdı. Sonra topu yeniden şişirdi ve top kocaman oldu. Hayri topu hafifçe Yumak'a doğru attı. Yumak havladı ve topu burnuyla geri itti. İkisi kumda uzun uzun oynadı. "Bu top artık ikimizin, Yumak!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri baklava dükkanında kutuları"
   - Cümle 6: «Hayri baklava dükkanında kutuları hep bantla kapatırdı.»
   - Açıklama: Art arda cümleler gereksiz yere hep 'Hayri' adıyla başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0013` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: b92d7b1e96b0c0a7485c7b866ffee3c5a8f2b2ba`, sonra gövde.

### Hikâye 5: tohum hayri-0014 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0014
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'pul', fiil 'boyamak', sıfat 'sabırsız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: rüzgar amcanın pulunu uçurdu ve pul kayboldu | ekmeğini yemeden baktı ve pulu reçelin üstünde buldu
@tohum: hayri-0014
@degisim: sabırsız -> reçelli
Hayri parkta reçelli ekmeğini yemek istiyordu, çünkü çok acıkmıştı. Yanında Basri Amca mektubunu boyarken pulunu banka bırakmıştı. Birden rüzgar esti ve pulu Hayri'ye doğru uçurdu. "Eyvah, pulum kayboldu!" dedi Basri Amca. Hayri ekmeğini yemedi ve önce pulu aramak istedi. Yere ve bankın altına baktı ama pulu göremedi. Sonra elindeki ekmeğe baktı. Küçük pul ekmeğin üstündeki reçele yapışmıştı. Hayri pulu reçelden yavaşça ayırdı ve Basri Amca'ya uzattı. Basri Amca pulu sevinçle mektubuna yapıştırdı. "Teşekkürler, Hayri, iyi ki ekmeğini hemen yemedin!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mektubunu boyarken pulunu"
   - Cümle 2: «Yanında Basri Amca mektubunu boyarken pulunu banka bırakmıştı.»
   - Açıklama: Mektup boyanmaz; fiil nesnesine uymuyor.
   - Açıklama: Mektup boyanmaz; 'yazarken' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0014` birebir aynı, `@degisim: sabırsız -> reçelli` (tutuyorsan), ardından `@onarim: c552caf3a778f378773e532472723df77aad27f5`, sonra gövde.

### Hikâye 6: tohum hayri-0015 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0015
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'turp', fiil 'eğilmek', sıfat 'güneşli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: yuvarlak turp yarışta hep yere düşüyordu | turpu düz yanından kaşığa koyup yavaş yürüdü
@tohum: hayri-0015
Ormanda, kamp yerinde hava çok güneşliydi. Hayri ile Mert kaşıkla turp taşıyarak büyük ağaca kadar yarışıyordu. Ama Hayri'nin turpu çok yuvarlaktı ve hep yere düşüyordu. "Mert, turp yine düştü!" dedi Hayri ve güldü. Hayri eğildi ve turpu yerden aldı. Hayri çok acıkmıştı ve yarışı çabuk bitirmek istiyordu. Bu yüzden turpa dikkatle baktı. Turpun bir yanı biraz düzdü. Hayri turpu kaşığa düz yanından koydu. Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi. "Bak, Mert, artık düşmüyor!" dedi Hayri. İkisi büyük ağaca vardı ve sonra birlikte mutlu mutlu yemek yedi. Hayri bundan sonra yuvarlak şeyleri kaşığa düz yanından koydu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ve yarışı çabuk bitirmek istiyordu"
   - Cümle 6: «Hayri çok acıkmıştı ve yarışı çabuk bitirmek istiyordu.»
   - Açıklama: Açlık işlevsiz bir ayrıntı ve turpa dikkatle bakmanın sebebi olarak akla yatmıyor; ardından yavaş yürümesiyle de uyuşmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu yüzden turpa dikkatle baktı"
   - Cümle 7: «Bu yüzden turpa dikkatle baktı.»
   - Açıklama: 'Bu yüzden' bağlacı acıkmayı dikkatle bakmaya bağlıyor; bağlaç yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0015` birebir aynı, ardından `@onarim: 2e17b31c452b46b6b08902c5a2b9c6e22d596720`, sonra gövde.

### Hikâye 7: tohum hayri-0018 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0018
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çit', fiil 'bindirmek', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: bahçede çamurlu izler vardı ve kimin olduğu belli değildi | deliğe gidip çitin arasından baktı
@tohum: hayri-0018
@degisim: bindirmek -> eşelemek
Hayri evin bahçesinde yürürken yerde çamurlu izler gördü. İzler çitin altındaki bir deliğe kadar gidiyordu. Hayri bu izleri çok merak etti. Önce bunları bir kamyonun izleri sandı. Sonra deliğe kadar yürüdü. Çitin arasından öbür bahçeye dikkatle baktı. Çalışkan köpek Yumak orada ıslak toprağı eşeliyordu. Yumak'ın ayakları çamurluydu. "Yumak, izler senin, ben biraz abarttım!" dedi Hayri ve güldü. Yumak kuyruğunu salladı ve bir kez havladı. Hayri çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ben biraz abarttım"
   - Cümle 9: «"Yumak, izler senin, ben biraz abarttım!" dedi Hayri ve güldü.»
   - Açıklama: Hayri bir şeyi abartmadı, izleri yanlış tahmin etti; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben biraz abarttım"
   - Cümle 9: «"Yumak, izler senin, ben biraz abarttım!" dedi Hayri ve güldü.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0018` birebir aynı, `@degisim: bindirmek -> eşelemek` (tutuyorsan), ardından `@onarim: 2e203dbdebb0910c47034dfc3830f63106a442d5`, sonra gövde.

### Hikâye 8: tohum hayri-0019 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0019
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çeşme', fiil 'kırpmak', sıfat 'kocaman'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: musluğu çok açtı ve su arkadaşını ıslattı | özür dileyip ona kocaman bir havlu getirdi
@tohum: hayri-0019
Bir sabah Hayri ile Akın kamp yerinde çeşmede ellerini yıkıyordu. Hayri musluğu birden çok fazla açtı. Su her yana fışkırdı ve Akın'ın yüzü sırılsıklam oldu. Akın gözlerini hızlı hızlı kırptı ve yüzünü buruşturdu. Hayri musluğu hemen biraz kapattı. "Özür dilerim, Akın, seni ıslatmak istemedim," dedi Hayri. Sonra çadıra koştu ve kocaman bir havlu getirdi. Akın havluyla yüzünü ve saçlarını kuruladı. "Akın, üstüne bütün çeşmenin suyu geldi!" dedi Hayri. Hayri yine abartıyordu ve Akın buna güldü. "Sorun değil, Hayri, havlu için teşekkürler!" dedi Akın.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri musluğu hemen biraz kapattı"
   - Cümle 5: «Hayri musluğu hemen biraz kapattı.»
   - Açıklama: Çözüm musluğu kapatma, özür ve havlu getirme olarak üç adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0019` birebir aynı, ardından `@onarim: 40bf871e3e1c54d3a9b22d57d35c153bdda45d80`, sonra gövde.

### Hikâye 9: tohum hayri-0020 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0020
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamera', fiil 'açmak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kum kuru olduğu için kale hep yıkılıyordu | kovayla ıslak kum getirip kaleyi yeniden yaptı
@tohum: hayri-0020
@degisim: kamera -> kova
Bir sabah deniz çok sakindi. Hayri kıyıda Basri Amca'yla kumdan bir kale yapıyordu. Ama kale hep yıkılıyordu, çünkü kum çok kuruydu. "Of, yine olmadı, bırakalım!" dedi Basri Amca. "Bırakmayalım, bu kale saray kadar büyük olacak!" dedi Hayri. Hayri abartıyordu ama Basri Amca güldü ve yeniden denemek istedi. Hayri suyun kenarında küçük bir çukur açtı, oradaki kum ıslaktı. Hayri kovasını bu kumla doldurdu ve geri getirdi. İkisi ıslak kumu sıkıca bastırdı ve kaleyi yeniden kurdu. Bu kez kale hiç yıkılmadı. Hayri çok sevindi, çünkü birlikte güzel bir kale yapmışlardı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıyordu ama"
   - Cümle 6: «Hayri abartıyordu ama Basri Amca güldü ve yeniden denemek istedi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartıyordu ama Basri"
   - Cümle 6: «Hayri abartıyordu ama Basri Amca güldü ve yeniden denemek istedi.»
   - Açıklama: 'abartmak' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0020` birebir aynı, `@degisim: kamera -> kova` (tutuyorsan), ardından `@onarim: 2b9961136d5a34d966286653a0a76eb5f7090fc1`, sonra gövde.

### Hikâye 10: tohum hayri-0021 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0021
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tarak', fiil 'seslenmek', sıfat 'büyük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpeğin tüyleri dikenli bir çalıya takıldı | ekmeğini paylaştı ve tüyleri tarakla ayırdı
@tohum: hayri-0021
Ormanda, kamp yerinde Hayri büyük tarağıyla saçını tarıyordu. Birden mahalleden tanıdığı köpek Yumak havladı ve Hayri sese doğru yürüdü. Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı. "Gel, Yumak!" diye seslendi Hayri. Ama Yumak kıpırdadı ve tüyler çalıya daha çok takıldı. Hayri çok acıkmıştı ve çantasında bir ekmek vardı. Yine de ekmeğin yarısını Yumak'a verdi. Yumak durdu ve ekmeği sakince yedi. Bu sırada Hayri elindeki tarakla tüyleri çalıdan yavaş yavaş ayırdı. Yumak zıpladı ve kuyruğunu salladı. "Oh, Yumak, sonunda kurtuldun!" dedi Hayri sevinçle.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "mahalleden tanıdığı köpek Yumak havladı"
   - Cümle 2: «Birden mahalleden tanıdığı köpek Yumak havladı ve Hayri sese doğru yürüdü.»
   - Açıklama: Kartın ilişki alanına göre Yumak Basri Amca'nın köpeğidir; şehir dışındaki kamp yerinde sahipsiz bulunması dizideki bilgiyle uyuşmuyor olabilir.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "mahalleden tanıdığı köpek Yumak"
   - Cümle 2: «Birden mahalleden tanıdığı köpek Yumak havladı ve Hayri sese doğru yürüdü.»
   - Açıklama: Kart ilişkisine göre Basri Amca'nın köpeği olan Yumak şehir dışındaki kamp yerinde sahipsiz tek başına bulunuyor, bu dizi bilgisine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0021` birebir aynı, ardından `@onarim: 533354b331c53d5fc7263f13b1e72c07b66fc580`, sonra gövde.

### Hikâye 11: tohum hayri-0022 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0022
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pastel', fiil 'getirmek', sıfat 'ucuz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: yeşil pastel kırıldı ve arkadaşı resmini bitiremedi | çadırdan kendi pastel kutusunu getirdi
@tohum: hayri-0022
@degisim: ucuz -> rengarenk
Hayri kamp yerinde Kamil'in ağaç resmini izliyordu. Birden Kamil'in yeşil pasteli yere düştü ve kırıldı. Küçük parçalar toprağa karıştı ve Kamil resmini bitiremedi. Kamil çok üzüldü. Hayri, çadırda yüz tane pasteli olduğunu söyleyerek abarttı. Kamil buna güldü. Hayri hemen çadıra koştu ve kendi pastel kutusunu getirdi. Kutuda yüz tane yoktu ama rengarenk boyalar vardı. Kamil yeşil bir pastel aldı ve ağaçları boyadı. Sonra Hayri ile Kamil birlikte mutlu mutlu yeni bir resim yaptı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pasteli olduğunu söyleyerek abarttı"
   - Cümle 5: «Hayri, çadırda yüz tane pasteli olduğunu söyleyerek abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "söyleyerek abarttı"
   - Cümle 5: «Hayri, çadırda yüz tane pasteli olduğunu söyleyerek abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bu kelimeyi bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0022` birebir aynı, `@degisim: ucuz -> rengarenk` (tutuyorsan), ardından `@onarim: 308a5f682d9f0160c02cf1820def9ab5a9ca4226`, sonra gövde.

### Hikâye 12: tohum hayri-0023 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0023
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'piyano', fiil 'eklemek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: oyuncak piyano parkta kayboldu | sesin peşinden gitti ve piyanoyu buldu
@tohum: hayri-0023
@degisim: sabırlı -> sarı
Parkta ince bir müzik sesi geliyordu. Hayri salıncaktan indi ve Basri Amca'yı üzgün gördü. Basri Amca, Hayri için aldığı oyuncak piyanoyu yürürken düşürmüştü. Hayri piyanoyu bulmak istedi ve sesi dikkatle dinledi. Ses büyük ağacın arkasından geliyordu. Hayri oraya koştu ve çimenlerin arasında sarı bir piyano buldu. Piyanonun şarkı düğmesi açık kalmıştı. Hayri piyanoyu Basri Amca'ya götürdü. Hayri abarttı ve piyanonun sesini bütün mahallenin duyduğunu söyledi. Basri Amca buna güldü ve artık üzgün değildi. Sonra Hayri piyanoyu çaldı ve şarkıya kendi sesini ekledi. Hayri çok sevindi, çünkü piyanoyu sesinden bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve piyanonun"
   - Cümle 9: «Hayri abarttı ve piyanonun sesini bütün mahallenin duyduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Abarttı' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0023` birebir aynı, `@degisim: sabırlı -> sarı` (tutuyorsan), ardından `@onarim: 173cc68fe12dbae20c25eb93d87a4f4b2bdd7005`, sonra gövde.
