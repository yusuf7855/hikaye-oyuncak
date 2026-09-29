# Editör görevi (onarım): Hayri, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0007 (deneme 4 -> 5)

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
Bir sabah Hayri ile Mert evin bahçesinde lokanta oyunu oynuyordu. Hayri, Mert'i doyurmak için tabağa plastik bir patlıcan koydu. Ama Mert tabağı alırken patlıcan düştü ve uzun çimlerde kayboldu. Mert çok üzüldü. Hayri, Mert'i güldürmek için aramayı abarttı ve çimlere uzandı. Mert bunu görünce güldü. Hayri yüzünü çimlere yaklaştırdı ve dikkatle baktı. Kokulu nane yapraklarının altında mor bir şey gördü. Kaybolan plastik patlıcan orada duruyordu. Hayri onu çıkardı ve yeniden tabağa bıraktı. Mert bu kez tabağı iki eliyle sıkıca tuttu. İkisi de çok sevindi, çünkü lokanta oyunları yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güldürmek için aramayı abarttı"
   - Cümle 5: «Hayri, Mert'i güldürmek için aramayı abarttı ve çimlere uzandı.»
   - Açıklama: 'Aramayı abartmak' soyut bir anlatım; 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "için aramayı abarttı"
   - Cümle 5: «Hayri, Mert'i güldürmek için aramayı abarttı ve çimlere uzandı.»
   - Açıklama: 'Aramayı abartmak' soyut ve küçük çocuk için anlaşılmaz bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0007` birebir aynı, ardından `@onarim: cb99be5fad8317ebb2f70d268baea20d7010538e`, sonra gövde.

### Hikâye 2: tohum hayri-0011 (deneme 4 -> 5)

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
Deniz kıyısında rüzgar hafif hafif esiyordu. Hayri gökyüzünde gemiye benzeyen bir bulut gördü. Ama bulut yavaş yavaş dağılıyordu ve Akın onu daha görmemişti. Akın uzakta, kumda eskimiş bir kovaya kabuk topluyordu. Hayri bulutu hemen Akın'a göstermek istedi. "Akın, koş, gökyüzünde dünyanın en büyük gemisi var!" diye bağırdı Hayri. "Hayri, yine abartıyorsun!" dedi Akın ve hemen koştu. İkisi yan yana durdu ve buluta baktı. "Çok güzel, Hayri, iyi ki beni çağırdın," diye fısıldadı Akın. Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri, yine abartıyorsun!"
   - Cümle 7: «"Hayri, yine abartıyorsun!" dedi Akın ve hemen koştu.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kavram.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0011` birebir aynı, `@degisim: kristal -> kabuk` (tutuyorsan), ardından `@onarim: 8b0fd3bbfe65ad6bc90c8afa56f572e63446e144`, sonra gövde.

### Hikâye 3: tohum hayri-0012 (deneme 3 -> 4)

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
Evin bahçesinde Hayri, kapının önünde üzgün duran Kamil'e yaklaştı. Kapı kilitliydi ve Kamil anahtarı bulamıyordu. "Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil. "Eyvah, anahtar yoksa bahçede uyuyacaksın!" dedi Hayri. "Hayri, yine abartıyorsun!" dedi Kamil ve güldü. Sonra Hayri çöp kutusunun yanına gitti ve yere eğildi. Kutunun arkasında parlayan küçük bir anahtar vardı. Hayri anahtarı aldı ve Kamil'e uzattı. Kamil kapıyı hemen açtı. "Teşekkürler, Hayri, sen çok iyi bir arkadaşsın!" dedi Kamil.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri, yine abartıyorsun!"
   - Cümle 5: «"Hayri, yine abartıyorsun!" dedi Kamil ve güldü.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0012` birebir aynı, ardından `@onarim: 57bb55cedc117bedc5c7d2f02dea25b09e5613d7`, sonra gövde.

### Hikâye 4: tohum hayri-0013 (deneme 3 -> 4)

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
Rüzgar esiyordu. Hayri deniz kıyısında renkli plaj topunu şişirmeye çalışıyordu. Ama top hep sönüyordu, çünkü üstünde küçük bir delik vardı. Yumak topa yavaş adımlarla yaklaştı ve onu kokladı. Hayri biraz düşündü. Hayri baklava dükkanında kutuları hep bantla kapatırdı. Bu yüzden cebinde her zaman bir parça bant taşırdı. Hayri bandı deliğin üstüne sıkıca yapıştırdı. Sonra topu yeniden şişirdi ve top kocaman oldu. Hayri topu hafifçe Yumak'a doğru attı. Yumak havladı ve topu burnuyla geri itti. İkisi kumda uzun uzun oynadı. "Bu top artık ikimizin, Yumak!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yumak topa yavaş adımlarla"
   - Cümle 4: «Yumak topa yavaş adımlarla yaklaştı ve onu kokladı.»
   - Açıklama: Yumak hiç tanıtılmadan hikayeye giriyor; kimin ya da neyin olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0013` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: de8fe9f943eb2e360492ef8935a1d5a9a5418094`, sonra gövde.

### Hikâye 5: tohum hayri-0014 (deneme 3 -> 4)

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
Hayri parkta reçelli ekmeğini yemek istiyordu, çünkü çok acıkmıştı. Yanında Basri Amca mektubunun kenarlarını boyamıştı ve şimdi pul yapıştırıyordu. Birden rüzgar esti ve pulu Hayri'ye doğru uçurdu. "Eyvah, pulum kayboldu!" dedi Basri Amca. Hayri ekmeğini yemedi ve önce pulu aramak istedi. Yere ve bankın altına baktı ama pulu göremedi. Sonra elindeki ekmeğe baktı. Küçük pul ekmeğin üstündeki reçele yapışmıştı. Hayri pulu reçelden yavaşça ayırdı ve Basri Amca'ya uzattı. Basri Amca pulu sevinçle mektubuna yapıştırdı. "Teşekkürler, Hayri, iyi ki ekmeğini hemen yemedin!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "mektubunun kenarlarını boyamıştı"
   - Cümle 2: «Yanında Basri Amca mektubunun kenarlarını boyamıştı ve şimdi pul yapıştırıyordu.»
   - Açıklama: Mektubun kenarlarının boyanması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0014` birebir aynı, `@degisim: sabırsız -> reçelli` (tutuyorsan), ardından `@onarim: 28705ea097879ad07627747941d796491d6f8635`, sonra gövde.

### Hikâye 6: tohum hayri-0015 (deneme 3 -> 4)

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
Ormanda, kamp yerinde hava çok güneşliydi. Hayri ile Mert kaşıkla turp taşıyarak büyük ağaca kadar yarışıyordu. Ama Hayri'nin turpu çok yuvarlaktı ve hep yere düşüyordu. "Mert, turp yine düştü!" dedi Hayri ve güldü. Hayri eğildi ve turpu yerden aldı. Hayri çok acıkmıştı ve yarış bitince turpu yiyecekti. Bu yüzden turpa dikkatle baktı. Turpun bir yanı biraz düzdü. Hayri turpu kaşığa düz yanından koydu. Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi. "Bak, Mert, artık düşmüyor!" dedi Hayri. İkisi büyük ağaca vardı ve turplarını mutlu mutlu yedi. Hayri bundan sonra yuvarlak şeyleri kaşığa düz yanından koydu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ve yarış bitince turpu yiyecekti"
   - Cümle 6: «Hayri çok acıkmıştı ve yarış bitince turpu yiyecekti.»
   - Açıklama: Açlık turpa dikkatle bakmanın akla yatkın sebebi değil; bağlantı zorlama.
   - Açıklama: Açlık ayrıntısı sorunla ilgisiz ve 'Bu yüzden turpa dikkatle baktı' sebebi bağlanmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "turplarını mutlu mutlu yedi"
   - Cümle 12: «İkisi büyük ağaca vardı ve turplarını mutlu mutlu yedi.»
   - Açıklama: Yarışta defalarca yere düşen ve yerden alınan turp yıkanmadan yeniyor; taklit edilince sağlığa aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0015` birebir aynı, ardından `@onarim: 5ec0948e9c5ec98d8662a7da48cd259312d6d9ec`, sonra gövde.

### Hikâye 7: tohum hayri-0018 (deneme 3 -> 4)

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
Hayri evin bahçesinde yürürken yerde çamurlu izler gördü. İzler çitin altındaki bir deliğe kadar gidiyordu. Hayri bu izleri çok merak etti. Hayri küçük izleri abartarak bir kamyonun izleri sandı. Sonra deliğe kadar yürüdü. Çitin arasından öbür bahçeye dikkatle baktı. Çalışkan Yumak orada ıslak toprağı eşeliyordu. Yumak'ın ayakları çamurluydu. "Yumak, izler senin, ben onları kamyon izi sandım!" dedi Hayri ve güldü. Yumak kuyruğunu salladı ve bir kez havladı. Hayri çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "izleri abartarak bir kamyonun"
   - Cümle 4: «Hayri küçük izleri abartarak bir kamyonun izleri sandı.»
   - Açıklama: 'Abartarak' fiili 'sandı' ile anlamca uyuşmuyor; yanlış anlamda kullanılmış.
   - Açıklama: 'Abartmak' konuşmayla olur, 'sanmak' fiiliyle birlikte yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri küçük izleri abartarak"
   - Cümle 4: «Hayri küçük izleri abartarak bir kamyonun izleri sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0018` birebir aynı, `@degisim: bindirmek -> eşelemek` (tutuyorsan), ardından `@onarim: 2e480d9e807a37181785bbe7932f7b04dac0c44a`, sonra gövde.

### Hikâye 8: tohum hayri-0019 (deneme 3 -> 4)

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
Bir sabah Hayri ile Akın kamp yerinde çeşmede ellerini yıkıyordu. Hayri musluğu birden çok fazla açtı. Su her yana fışkırdı ve Akın'ın yüzü sırılsıklam oldu. Akın gözlerini hızlı hızlı kırptı ve yüzünü buruşturdu. Hayri musluğu hemen biraz kapattı. "Özür dilerim, Akın, seni ıslatmak istemedim," dedi Hayri. Sonra çadıra koştu ve kocaman bir havlu getirdi. Akın havluyla yüzünü ve saçlarını kuruladı. "Akın, üstüne bütün çeşmenin suyu geldi!" dedi Hayri. "Yine abartıyorsun, Hayri, ama özrünü kabul ettim!" dedi Akın ve güldü.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yine abartıyorsun, Hayri"
   - Cümle 10: «"Yine abartıyorsun, Hayri, ama özrünü kabul ettim!" dedi Akın ve güldü.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yine abartıyorsun, Hayri, ama özrünü kabul ettim!"
   - Cümle 10: «"Yine abartıyorsun, Hayri, ama özrünü kabul ettim!" dedi Akın ve güldü.»
   - Açıklama: 'Abartmak' ve 'özrünü kabul etmek' soyut, küçük çocuğun bilmeyeceği ifadeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0019` birebir aynı, ardından `@onarim: b011778f2f2975ba611a0300f545d720230d7d9e`, sonra gövde.

### Hikâye 9: tohum hayri-0020 (deneme 3 -> 4)

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
Bir sabah deniz çok sakindi. Hayri kıyıda Basri Amca'yla kumdan bir kale yapıyordu. Ama kale hep yıkılıyordu, çünkü kum çok kuruydu. "Of, yine olmadı, bırakalım!" dedi Basri Amca. "Bırakmayalım, bu kale saray kadar büyük olacak!" dedi Hayri abartarak. Basri Amca güldü ve yeniden denemek istedi. Hayri suyun kenarında küçük bir çukur açtı, oradaki kum ıslaktı. Hayri kovasını bu kumla doldurdu ve geri getirdi. İkisi ıslak kumu sıkıca bastırdı ve kaleyi yeniden kurdu. Bu kez kale hiç yıkılmadı. Hayri çok sevindi, çünkü birlikte güzel bir kale yapmışlardı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Bırakmayalım, bu kale saray kadar büyük olacak!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0020` birebir aynı, `@degisim: kamera -> kova` (tutuyorsan), ardından `@onarim: 4ba5fa9c8f7550f6d5ff19c3a10fd5bc11433a4a`, sonra gövde.

### Hikâye 10: tohum hayri-0021 (deneme 2 -> 3)

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
Ormanda, kamp yerinde Hayri büyük tarağıyla saçını tarıyordu. Birden bir köpek havladı ve Hayri sese koştu. Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı. "Gel, Yumak!" diye seslendi Hayri. Ama Yumak kıpırdadı ve tüyler çalıya daha çok takıldı. Hayri çok acıkmıştı ve çantasında bir ekmek vardı. Yine de ekmeğin yarısını Yumak'a verdi. Yumak durdu ve ekmeği sakince yedi. Bu sırada Hayri elindeki tarakla tüyleri çalıdan yavaş yavaş ayırdı. Yumak zıpladı ve kuyruğunu salladı. "Oh, Yumak, sonunda kurtuldun!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Birden bir köpek havladı ve Hayri sese koştu"
   - Cümle 2: «Birden bir köpek havladı ve Hayri sese koştu.»
   - Açıklama: Çocuk kimin olduğunu bilmediği havlayan bir köpeğin sesine doğru koşuyor; taklit edilince tehlikeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0021` birebir aynı, ardından `@onarim: f1e2496c799d976e6b99c8e2a4d584b26ca0a7a5`, sonra gövde.

### Hikâye 11: tohum hayri-0022 (deneme 2 -> 3)

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
Hayri ile Kamil kamp yerinde ağaçların resmini yapıyordu. Birden Kamil'in yeşil pasteli ikiye kırıldı. Parçalar çok küçüktü ve Kamil onları tutamadı. Kamil resmini bitiremedi ve üzüldü. Hayri hemen çadıra koştu. Çantasından kendi pastel kutusunu getirdi. Kutuda rengarenk boyalar vardı. Kamil yeşil bir pastel aldı ve ağaçları boyadı. Sonra resmini Hayri'ye gösterdi. Hayri resmi görünce abarttı ve tam on kez zıpladı. Kamil de ona bakıp güldü. Sonra ikisi resimlerini mutlu mutlu boyamaya devam etti.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Parçalar çok küçüktü ve Kamil onları tutamadı"
   - Cümle 3: «Parçalar çok küçüktü ve Kamil onları tutamadı.»
   - Açıklama: İkiye kırılan bir pastelin parçalarının tutulamayacak kadar küçük olması akla yatkın bir sebep değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çantasından kendi pastel kutusunu getirdi"
   - Cümle 6: «Çantasından kendi pastel kutusunu getirdi.»
   - Açıklama: Hayri de resim yaparken pastelleri yanında olmalıyken kutusunu çadırdan getirmesi çelişkili.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "resmi görünce abarttı"
   - Cümle 10: «Hayri resmi görünce abarttı ve tam on kez zıpladı.»
   - Açıklama: 'Abartmak' nesnesiz ve yanlış anlamda kullanılmış; sevinmeyi anlatmıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "resmi görünce abarttı"
   - Cümle 10: «Hayri resmi görünce abarttı ve tam on kez zıpladı.»
   - Açıklama: 'Abarttı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "resmi görünce abarttı ve tam"
   - Cümle 10: «Hayri resmi görünce abarttı ve tam on kez zıpladı.»
   - Açıklama: 'Abarttı' 3 yaşındaki çocuğun bilmediği soyut bir kelime ve burada nesnesiz, yanlış kullanılmış.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri resmi görünce abarttı ve tam on kez zıpladı"
   - Cümle 10: «Hayri resmi görünce abarttı ve tam on kez zıpladı.»
   - Açıklama: Karttaki 'olayları abartmayı sever' özelliği bir olayı abartarak anlatmak yerine anlamsız bir zıplama eylemine dönüşmüş ve işe yarar biçimde kullanılmamış.
   - Açıklama: Tohumdaki abartma özelliği sorun çözüldükten sonra süs olarak ekleniyor, çözüme hiçbir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0022` birebir aynı, `@degisim: ucuz -> rengarenk` (tutuyorsan), ardından `@onarim: d0e43b48cab2472d563a3944cf32b87ad31fa347`, sonra gövde.

### Hikâye 12: tohum hayri-0023 (deneme 2 -> 3)

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
Parkta ince bir müzik sesi geliyordu. Hayri salıncaktan indi ve Basri Amca'yı üzgün gördü. Basri Amca, Hayri için aldığı oyuncak piyanoyu parkta kaybetmişti. Hayri piyanoyu bulmak istedi ve sesi dikkatle dinledi. Ses büyük ağacın arkasından geliyordu. Hayri oraya koştu ve çimenlerin arasında sarı bir piyano buldu. Piyanonun şarkı düğmesi açık kalmıştı. Hayri, Basri Amca duysun diye abartarak bütün tuşlara bastı. Piyano çok yüksek çaldı ve Basri Amca koşarak geldi. Basri Amca güldü ve piyanoyu Hayri'ye verdi. Sonra Hayri piyanoyu çaldı ve şarkıya kendi sesini ekledi. Hayri çok sevindi, çünkü piyanoyu sesinden bulmuştu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "oyuncak piyanoyu parkta kaybetmişti"
   - Cümle 3: «Basri Amca, Hayri için aldığı oyuncak piyanoyu parkta kaybetmişti.»
   - Açıklama: Piyanonun nasıl kaybolduğu, yani sorunun sebebi hiç söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "duysun diye abartarak bütün"
   - Cümle 8: «Hayri, Basri Amca duysun diye abartarak bütün tuşlara bastı.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartarak bütün tuşlara bastı"
   - Cümle 8: «Hayri, Basri Amca duysun diye abartarak bütün tuşlara bastı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuk için soyut ve burada anlamı belirsiz bir kelime.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "abartarak bütün tuşlara bastı"
   - Cümle 8: «Hayri, Basri Amca duysun diye abartarak bütün tuşlara bastı.»
   - Açıklama: Karttaki özellik olayları abartmak iken burada tuşlara abartılı basmak olarak kartın özellik tanımından farklı kullanılıyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "piyanoyu Hayri'ye verdi"
   - Cümle 10: «Basri Amca güldü ve piyanoyu Hayri'ye verdi.»
   - Açıklama: Piyanoyu Hayri bulup elinde tutuyorken Basri Amca'nın onu Hayri'ye vermesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0023` birebir aynı, `@degisim: sabırlı -> sarı` (tutuyorsan), ardından `@onarim: 2b12afe02f78caa0cdb782fc72df98b71c7ba068`, sonra gövde.
