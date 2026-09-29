# Editör görevi (onarım): Hayri, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0007 (deneme 3 -> 4)

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
Bir sabah Hayri ile Mert evin bahçesinde lokanta oyunu oynuyordu. Hayri, Mert'i doyurmak için tabağa plastik bir patlıcan koydu. Ama Mert tabağı alırken patlıcan düştü ve uzun çimlerde kayboldu. Mert çok üzüldü. Hayri biraz abarttı ve onu aramak için yere uzandı. Mert bunu görünce güldü. Hayri yüzünü çimlere yaklaştırdı ve dikkatle baktı. Kokulu nane yapraklarının altında mor bir şey gördü. Kaybolan plastik patlıcan orada duruyordu. Hayri onu çıkardı ve yeniden tabağa bıraktı. Mert bu kez tabağı iki eliyle sıkıca tuttu. İkisi de çok sevindi, çünkü lokanta oyunları yeniden başlamıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri biraz abarttı ve"
   - Cümle 5: «Hayri biraz abarttı ve onu aramak için yere uzandı.»
   - Açıklama: Neyi abarttığı belli değil; fiil burada anlamsız kalıyor.
   - Açıklama: 'Abarttı' burada anlamsız ve yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 5: «Hayri biraz abarttı ve onu aramak için yere uzandı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onu aramak için yere uzandı"
   - Cümle 5: «Hayri biraz abarttı ve onu aramak için yere uzandı.»
   - Açıklama: Son anılan kişi Mert olduğu için 'onu' zamirinin patlıcanı gösterdiği belli değil.
   - Açıklama: 'Onu' zamiri son geçen Mert'i mi patlıcanı mı gösteriyor belli değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abarttı ve onu aramak için yere uzandı"
   - Cümle 5: «Hayri biraz abarttı ve onu aramak için yere uzandı.»
   - Açıklama: Karttaki özellik olayları abartmaktır; yere uzanmak abartma değildir, özellik karttaki gibi kullanılmamış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abarttı ve onu aramak"
   - Cümle 5: «Hayri biraz abarttı ve onu aramak için yere uzandı.»
   - Açıklama: Tohumdaki abartma özelliği kartta tarif edildiği gibi bir abartı olarak değil, yere uzanmakla karıştırılarak işlevsiz kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0007` birebir aynı, ardından `@onarim: c01f10afa8fcc28d226688bc11905a0e19c7787f`, sonra gövde.

### Hikâye 2: tohum hayri-0011 (deneme 3 -> 4)

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
Deniz kıyısında rüzgar hafif hafif esiyordu. Hayri gökyüzünde gemiye benzeyen bir bulut gördü. Ama bulut yavaş yavaş dağılıyordu ve Akın onu daha görmemişti. Akın uzakta, kumda eskimiş bir kovaya kabuk topluyordu. Hayri bulutu hemen Akın'a göstermek istedi. "Akın, koş, gökyüzünde dünyanın en büyük gemisi var!" diye bağırdı Hayri. Hayri biraz abartmıştı, ama Akın bunu duyunca hemen koştu. İkisi yan yana durdu ve buluta baktı. "Çok güzel, Hayri, iyi ki beni çağırdın," diye fısıldadı Akın. Hayri bundan sonra güzel bir şey görünce arkadaşını hemen çağırdı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 7: «Hayri biraz abartmıştı, ama Akın bunu duyunca hemen koştu.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kavram.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0011` birebir aynı, `@degisim: kristal -> kabuk` (tutuyorsan), ardından `@onarim: e534f7da616fc5f78da011334927e953a1170a29`, sonra gövde.

### Hikâye 3: tohum hayri-0012 (deneme 2 -> 3)

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
Evin bahçesinde Hayri, kapının önünde üzgün duran Kamil'e yaklaştı. Kapı kilitliydi ve Kamil anahtarı bulamıyordu. "Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil. "Eyvah, anahtar yoksa bahçede uyuyacaksın!" dedi Hayri. Hayri biraz abartmıştı. Kamil buna güldü ve rahatladı. Sonra Hayri çöp kutusunun yanına gitti ve yere eğildi. Kutunun arkasında parlayan küçük bir anahtar vardı. Hayri anahtarı aldı ve Kamil'e uzattı. Kamil kapıyı hemen açtı. "Teşekkürler, Hayri, sen çok iyi bir arkadaşsın!" dedi Kamil.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 5: «Hayri biraz abartmıştı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0012` birebir aynı, ardından `@onarim: c5e27113f09f86a77dd18dddd14174c8c16e447e`, sonra gövde.

### Hikâye 4: tohum hayri-0013 (deneme 2 -> 3)

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
@plan: top hep söndü çünkü üstünde küçük bir delik vardı | deliğe bant yapıştırıp topu yeniden şişirdi
@tohum: hayri-0013
@degisim: temkinli -> yavaş
Rüzgar esiyordu. Hayri deniz kıyısında renkli plaj topunu şişirmeye çalışıyordu. Ama top hep sönüyordu, çünkü üstünde küçük bir delik vardı. Yumak topa yavaş adımlarla yaklaştı ve onu kokladı. Hayri biraz düşündü. Hayri baklava dükkanında kutuları hep bantla kapatırdı. Cebinde de dükkandan kalan bir parça bant vardı. Hayri bandı deliğin üstüne sıkıca yapıştırdı. Sonra topu yeniden şişirdi ve top kocaman oldu. Hayri topu hafifçe Yumak'a doğru attı. Yumak havladı ve topu burnuyla geri itti. İkisi kumda uzun uzun oynadı. "Bu top artık ikimizin, Yumak!" dedi Hayri sevinçle.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "top hep söndü çünkü"
   - Cümle 0 (plan satırı): «top hep söndü çünkü üstünde küçük bir delik vardı | deliğe bant yapıştırıp topu yeniden şişirdi»
   - Açıklama: 'hep' tekrarlanan eylem ister; plan satırında 'hep sönüyordu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Cebinde de dükkandan kalan bir parça bant vardı"
   - Cümle 7: «Cebinde de dükkandan kalan bir parça bant vardı.»
   - Açıklama: Bant tam gerektiği anda cepte hazır bulunuyor; çözümü getiren nesne önceden kurulmadan beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0013` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: a53a2648254aa4904e1333592c785b534dc91353`, sonra gövde.

### Hikâye 5: tohum hayri-0014 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: bank çok uzundu ve boyamak uzun sürüyordu | yemeğe gitmeyip ikinci fırçayla boyamaya yardım etti
@tohum: hayri-0014
@degisim: pul -> fırça
Hayri parkta Basri Amca'yı gördü. Basri Amca parktaki eski bankı yeşile boyuyordu. Ama bank çok uzundu. Basri Amca sabırsızdı, çünkü işi hemen bitirmek istiyordu. "Bu iş hiç bitmeyecek!" dedi Basri Amca. Hayri çok acıkmıştı ve eve yemeğe gidiyordu. "Önce size yardım edeyim, Basri Amca, yemeği sonra yerim!" dedi Hayri. Basri Amca kutudan ikinci bir fırça çıkarıp ona verdi. Hayri bankın bir ucunu, Basri Amca öbür ucunu boyadı. Az sonra ikisi ortada buluştu. Eski bank yepyeni ve yemyeşil oldu. "Teşekkürler, Hayri, birlikte ne çabuk bitirdik!" dedi Basri Amca.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Basri Amca sabırsızdı, çünkü"
   - Cümle 4: «Basri Amca sabırsızdı, çünkü işi hemen bitirmek istiyordu.»
   - Açıklama: 'Sabırsız' soyut bir özellik kelimesi ve figürün kart kelimesi değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Basri Amca sabırsızdı"
   - Cümle 4: «Basri Amca sabırsızdı, çünkü işi hemen bitirmek istiyordu.»
   - Açıklama: 'Sabırsız' figürün kart kelimesi olmayan soyut bir kavram ve 3 yaşındaki çocuk için zor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Basri Amca sabırsızdı, çünkü işi hemen bitirmek istiyordu"
   - Cümle 4: «Basri Amca sabırsızdı, çünkü işi hemen bitirmek istiyordu.»
   - Açıklama: Sorun bir yetişkinin uzun bankı boyamaktaki sabırsızlığı; çocuğun önemseyeceği bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0014` birebir aynı, `@degisim: pul -> fırça` (tutuyorsan), ardından `@onarim: 7456c4e25a9417b48a0ae93301ed228e09f4371c`, sonra gövde.

### Hikâye 6: tohum hayri-0015 (deneme 2 -> 3)

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
Ormanda, kamp yerinde hava çok güneşliydi. Hayri ile Mert kaşıkla turp taşıyarak büyük ağaca kadar yarışıyordu. Ama Hayri'nin turpu çok yuvarlaktı ve hep yere düşüyordu. "Mert, turp yine düştü!" dedi Hayri ve güldü. Hayri eğildi ve turpu yerden aldı. Hayri çok acıkmıştı ama turpu yemedi ve ona dikkatle baktı. Turpun bir yanı biraz düzdü. Hayri turpu kaşığa düz yanından koydu. Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi. "Bak, Mert, artık düşmüyor!" dedi Hayri. İkisi de gülerek büyük ağaca vardı. Hayri bundan sonra yuvarlak şeyleri kaşığa düz yanından koydu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri çok acıkmıştı ama turpu yemedi"
   - Cümle 6: «Hayri çok acıkmıştı ama turpu yemedi ve ona dikkatle baktı.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ama turpu yemedi"
   - Cümle 6: «Hayri çok acıkmıştı ama turpu yemedi ve ona dikkatle baktı.»
   - Açıklama: Açlık ayrıntısı olaya hiçbir şey katmayan işlevsiz bir ekleme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0015` birebir aynı, ardından `@onarim: 7b5cf5c7438cdcdc49fc3d391494a171121f95a4`, sonra gövde.

### Hikâye 7: tohum hayri-0016 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0016
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yapıştırıcı', fiil 'izlemek', sıfat 'bembeyaz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: rüzgar bembeyaz şapkayı uçurdu ve şapka kayboldu | uçan kumları izleyip şapkayı kayaların arasında buldu
@tohum: hayri-0016
@degisim: yapıştırıcı -> şapka
Deniz kıyısında rüzgar çok esiyordu. Hayri ile Kamil kumda oturmuş denize bakıyordu. Birden rüzgar Kamil'in bembeyaz şapkasını uçurdu ve şapka kayboldu. "Eyvah, şapkam gitti!" dedi Kamil. "Şapkan uçup bulutlara kadar çıktı!" dedi Hayri. Hayri biraz abartmıştı. Kamil güldü ama yine de şapkasını istiyordu. Hayri havada uçan kum tanelerini izledi. Kumlar hep büyük kayalara doğru uçuyordu. Hayri o yöne yürüdü ve kayaların arkasına baktı. Şapka iki kayanın arasına sıkışmıştı. Hayri şapkayı aldı ve Kamil'e götürdü. "Teşekkürler, Hayri!" dedi Kamil ve şapkasını taktı. Hayri bundan sonra uçan eşyaları rüzgarın estiği yönde aradı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı."
   - Cümle 6: «Hayri biraz abartmıştı.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 6: «Hayri biraz abartmıştı.»
   - Açıklama: Tohumdaki abartma özelliği şapkayı bulmada işe yaramıyor, yalnız süs olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 6: «Hayri biraz abartmıştı.»
   - Açıklama: Abartma repliği olayda hiçbir işe yaramayan, çözüme katkısı olmayan bir ayrıntı.
   - Açıklama: Abartma ayrıntısı olay akışına hiçbir katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0016` birebir aynı, `@degisim: yapıştırıcı -> şapka` (tutuyorsan), ardından `@onarim: b011f04208f8b8af5d9b31c503996d57f0a5d646`, sonra gövde.

### Hikâye 8: tohum hayri-0018 (deneme 2 -> 3)

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
Hayri evin bahçesinde yürürken yerde çamurlu izler gördü. İzler çitin altındaki bir deliğe kadar gidiyordu. Hayri bu izleri çok merak etti. Hayri biraz abarttı ve bunları bir kamyonun izleri sandı. Sonra deliğe kadar yürüdü. Çitin arasından öbür bahçeye dikkatle baktı. Çalışkan Yumak orada ıslak toprağı eşeliyordu. Yumak'ın ayakları çamurluydu. "Yumak, bu izler senin, ben seni kamyon sandım!" dedi Hayri ve güldü. Yumak kuyruğunu salladı ve bir kez havladı. Hayri çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 4: «Hayri biraz abarttı ve bunları bir kamyonun izleri sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı ve"
   - Cümle 4: «Hayri biraz abarttı ve bunları bir kamyonun izleri sandı.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ben seni kamyon sandım"
   - Cümle 9: «"Yumak, bu izler senin, ben seni kamyon sandım!" dedi Hayri ve güldü.»
   - Açıklama: Hayri Yumak'ı değil izleri kamyon izi sanmıştı; ifade yanlış anlam veriyor.
   - Açıklama: Hayri Yumak'ı değil izleri kamyonun sandı; 'seni kamyon sandım' anlamca yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0018` birebir aynı, `@degisim: bindirmek -> eşelemek` (tutuyorsan), ardından `@onarim: 35ee164abb1bea511c770f4b7a97cca62582c1d9`, sonra gövde.

### Hikâye 9: tohum hayri-0019 (deneme 2 -> 3)

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
Bir sabah Hayri ile Akın kamp yerinde çeşmede ellerini yıkıyordu. Hayri musluğu birden çok fazla açtı. Su her yana fışkırdı ve Akın'ın yüzü sırılsıklam oldu. Akın gözlerini hızlı hızlı kırptı ve yüzünü buruşturdu. Hayri musluğu hemen biraz kapattı. "Özür dilerim, Akın, seni ıslatmak istemedim," dedi Hayri. Sonra çadıra koştu ve kocaman bir havlu getirdi. Akın havluyla yüzünü ve saçlarını kuruladı. "Akın, üstüne bütün çeşmenin suyu geldi!" dedi Hayri. Hayri biraz abartmıştı ve Akın buna çok güldü. "Özrünü kabul ettim, Hayri, bu havlu çok yumuşak!" dedi Akın.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 10: «Hayri biraz abartmıştı ve Akın buna çok güldü.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuk için soyut bir kavram.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki bir çocuk bu kelimeyi bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0019` birebir aynı, ardından `@onarim: fdb54656026146c1fab6da42bd8a487b60944ac2`, sonra gövde.

### Hikâye 10: tohum hayri-0020 (deneme 2 -> 3)

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
Bir sabah deniz çok sakindi. Hayri kıyıda Basri Amca'yla kumdan bir kale yapıyordu. Ama kale hep yıkılıyordu, çünkü kum çok kuruydu. "Of, yine olmadı!" dedi Basri Amca. Hayri suyun kenarına baktı, oradaki kum koyu ve ıslaktı. Hayri kovasını bu kumla doldurdu ve geri getirdi. İkisi ıslak kumu sıkıca bastırdı ve kaleyi yeniden kurdu. Bu kez kale hiç yıkılmadı. "Basri Amca, bu kale bir saray kadar büyük oldu!" dedi Hayri. Hayri biraz abartmıştı. Basri Amca güldü ve kaleyi mahalleye göstermek için kamerasını açtı. Sonra kalenin önünde Hayri'nin fotoğrafını çekti. Hayri çok sevindi, çünkü birlikte güzel bir kale yapmışlardı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 10: «Hayri biraz abartmıştı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kavram.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 10: «Hayri biraz abartmıştı.»
   - Açıklama: Tohumdaki abartma özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak ekleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kaleyi mahalleye göstermek"
   - Cümle 11: «Basri Amca güldü ve kaleyi mahalleye göstermek için kamerasını açtı.»
   - Açıklama: 'Mahalleye göstermek' mecazlı bir anlatım.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kaleyi mahalleye göstermek için kamerasını açtı"
   - Cümle 11: «Basri Amca güldü ve kaleyi mahalleye göstermek için kamerasını açtı.»
   - Açıklama: Kamera sebepsizce beliriyor ve sorun çözüldükten sonra işlevsiz bir ek sahne getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0020` birebir aynı, ardından `@onarim: 67a00e5868b707653f8a620b170dc60aeb5c108d`, sonra gövde.

### Hikâye 11: tohum hayri-0021 (deneme 1 -> 2)

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
Ormanda, kamp yerinin yanında bir köpek havlıyordu. Hayri sese koştu ve Yumak'ı gördü. Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı. "Gel, Yumak!" diye seslendi Hayri. Ama Yumak kıpırdadı ve tüyler daha çok dolandı. Hayri çok acıkmıştı ve çantasında bir ekmek vardı. Yine de ekmeğin yarısını Yumak'a verdi. Yumak durdu ve ekmeği sakince yedi. Bu sırada Hayri çantadan büyük tarağını aldı. Tüyleri tarakla çalıdan yavaş yavaş ayırdı. Yumak zıpladı ve kuyruğunu salladı. "Oh, Yumak, sonunda kurtuldun!" dedi Hayri sevinçle.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tüyler daha çok dolandı"
   - Cümle 5: «Ama Yumak kıpırdadı ve tüyler daha çok dolandı.»
   - Açıklama: Takılan tüyler için doğru fiil 'dolaştı' olmalı; 'dolandı' anlamca uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çantadan büyük tarağını aldı"
   - Cümle 9: «Bu sırada Hayri çantadan büyük tarağını aldı.»
   - Açıklama: Ormandaki çantada büyük bir tarak önceden kurulmadan belirip çözümü sebepsizce getiriyor.
   - Açıklama: Tarak daha önce kurulmadan sebepsizce beliriyor ve çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0021` birebir aynı, ardından `@onarim: ca1de36763133a148954cb3de0e29a090601fb0c`, sonra gövde.

### Hikâye 12: tohum hayri-0022 (deneme 1 -> 2)

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
@plan: arkadaşının yeşil pasteli kırıldı ve resmini bitiremedi | çadırdan kendi pastel kutusunu getirdi
@tohum: hayri-0022
Hayri ile Kamil kamp yerinde ağaçların resmini yapıyordu. Birden Kamil'in yeşil pasteli ikiye kırıldı. Parçalar çok küçüktü ve Kamil onları tutamadı. Kamil resmini bitiremedi ve üzüldü. Hayri hemen çadıra koştu. Çantasından kendi pastel kutusunu getirdi. Kutuda ucuz ama rengarenk boyalar vardı. Kamil yeşil bir pastel aldı ve ağaçları boyadı. Sonra resmini Hayri'ye gösterdi. Hayri resmi görünce abartarak alkışladı ve zıpladı. Kamil de ona bakıp güldü. Sonra ikisi resimlerini mutlu mutlu boyamaya devam etti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "pasteli kırıldı ve resmini bitiremedi"
   - Cümle 0 (plan satırı): «arkadaşının yeşil pasteli kırıldı ve resmini bitiremedi | çadırdan kendi pastel kutusunu getirdi»
   - Açıklama: Plan cümlesinde 'kırıldı' öznesi pastel, 'bitiremedi' öznesi arkadaş; özne uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kutuda ucuz ama rengarenk"
   - Cümle 7: «Kutuda ucuz ama rengarenk boyalar vardı.»
   - Açıklama: 'Ucuz' fiyat kavramı soyut ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Ucuz' fiyatla ilgili soyut bir kavram; çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutuda ucuz ama rengarenk boyalar vardı"
   - Cümle 7: «Kutuda ucuz ama rengarenk boyalar vardı.»
   - Açıklama: Boyaların ucuz olması hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Boyaların ucuz olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartarak alkışladı ve zıpladı"
   - Cümle 10: «Hayri resmi görünce abartarak alkışladı ve zıpladı.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0022` birebir aynı, ardından `@onarim: d9dbc754a39b783bd42231bd6b6b538b0955d1b0`, sonra gövde.
