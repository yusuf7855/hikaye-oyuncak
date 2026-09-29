# Editör görevi (onarım): Hayri, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0058 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0058
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hamur', fiil 'kapamak', sıfat 'incecik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: domates kaygandı ve açık ekmekten kaydı | ekmeği ikiye katlayıp kenarlarını kapadı
@tohum: hayri-0058
@degisim: hamur -> sandviç
Hayri parkta ilk kez kendi sandviçini yapmayı denedi. Çok acıkmıştı ve incecik bir dilim ekmeğe peynirle domates koydu. Ama domates kaygandı ve ekmeğin üstünden dışarı kaydı. Hayri durdu ve sandviçe dikkatle baktı. Ekmeğin üstü açıktı ve domatesi hiçbir şey tutmuyordu. Sonra domatesi ekmeğin ortasına geri koydu. Ekmeği ikiye katlayıp kenarlarını sıkıca kapadı. Bu kez hiçbir şey kaymadı. Hayri büyük bir ısırık aldı ve gülümsedi. Peynir de domates de içeride kalmıştı. Hayri çok sevindi, çünkü ilk sandviçini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "domates kaygandı ve açık ekmekten kaydı"
   - Cümle 0 (plan satırı): «domates kaygandı ve açık ekmekten kaydı | ekmeği ikiye katlayıp kenarlarını kapadı»
   - Açıklama: 'Açık ekmek' doğal bir söyleyiş değil; 'ekmeğin üstünden kaydı' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0058` birebir aynı, `@degisim: hamur -> sandviç` (tutuyorsan), ardından `@onarim: ae0fd9e040c17f73739c3951945dc3605baf7f98`, sonra gövde.

### Hikâye 2: tohum hayri-0061 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0061
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'atkı', fiil 'yaymak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: uçurtmanın kuyruğu yoktu ve uçurtma dönüp düşüyordu | atkısını uçurtmaya uzun bir kuyruk olarak bağladı
@tohum: hayri-0061
Rüzgar esiyordu ve gökyüzü beyaz bulutlarla doluydu. Hayri parkta ilk kez uçurtma uçurmayı deniyordu. Ama uçurtmanın kuyruğu yoktu ve uçurtma havada dönüp düşüyordu. Hayri uçurtmayı çimlere yaydı ve dikkatle baktı. Sonra boynundaki uzun kırmızı atkıyı çıkardı. Hayri abartarak kuyruğu bir ağaç kadar uzun yapmak istedi. Bu yüzden bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı. Hayri ipi tuttu ve rüzgara karşı koştu. Bu kez uçurtma hiç dönmedi. Kırmızı kuyruğuyla yavaş yavaş yükseldi. Hayri çok sevindi, çünkü ilk uçurtmasını kendisi uçurmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kuyruğu"
   - Cümle 6: «Hayri abartarak kuyruğu bir ağaç kadar uzun yapmak istedi.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kuyruğu bir ağaç kadar uzun"
   - Cümle 6: «Hayri abartarak kuyruğu bir ağaç kadar uzun yapmak istedi.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 'bir ağaç kadar uzun' abartma mecazı 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kuyruğu bir ağaç kadar uzun yapmak istedi"
   - Cümle 6: «Hayri abartarak kuyruğu bir ağaç kadar uzun yapmak istedi.»
   - Açıklama: Kuyruğu ağaç kadar uzun yapma isteği hiçbir olaya bağlanmayan işlevsiz bir ayrıntı.
   - Açıklama: Atkıyı ağaç kadar uzun yapma isteği gerçekleşmiyor ve olayda hiçbir işe yaramayan işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0061` birebir aynı, ardından `@onarim: 9905a05b2ca1fa78443ce0930fb1f79bdf5a8d89`, sonra gövde.

### Hikâye 3: tohum hayri-0065 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0065
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca beklemekten sıkıldı ve gitmek istedi | baklava paylaştı ve amcayla birlikte bekledi
@tohum: hayri-0065
@degisim: patik -> çiçek
Ormandaki kamp yerinde turuncu bir çiçek açılmak üzereydi. Hayri, Basri Amca ile çiçeğin yanında oturmuş bekliyordu. Ama Basri Amca beklemekten sıkıldı ve ayağa kalktı. "Çok uzun sürdü, ben gidiyorum," dedi Basri Amca. Hayri, çiçeği amcayla birlikte görmek istiyordu. Yanında, çalıştığı baklava dükkanından getirdiği bir kutu vardı. Hayri kutuyu açtı ve amcaya uzattı. "Beklerken birer baklava yiyelim mi, Basri Amca?" diye sordu Hayri. Amca gülümsedi ve yeniden oturdu. İkisi baklavalarını yerken çiçeğe baktı. Az sonra turuncu çiçek bütün yapraklarıyla açıldı. "Çok güzel, Hayri, iyi ki gitmemişim!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı baklava dükkanından getirdiği bir kutu vardı"
   - Cümle 6: «Yanında, çalıştığı baklava dükkanından getirdiği bir kutu vardı.»
   - Açıklama: Baklava kutusu tam çözüm gerektiğinde sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0065` birebir aynı, `@degisim: patik -> çiçek` (tutuyorsan), ardından `@onarim: 3bfe260a69d45a73b6c30d77a74ef9d9b2b76338`, sonra gövde.

### Hikâye 4: tohum hayri-0066 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0066
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zil', fiil 'ödemek', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek baklava kutusunu ağaçların arasına götürdü | köpekten yardım istedi ve kutuyu geri aldı
@tohum: hayri-0066
@degisim: ödemek -> koklamak
Ormandaki kamp yerinde Hayri küçük bir zil çalıyor, Yumak da sese koşuyordu. Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi. Ama Yumak kutuyu ağzına aldı, ağaçların arasına koştu ve kutusuz döndü. Hayri her yere baktı ama kutuyu bulamadı. "Yumak, kutuyu bulmama yardım eder misin?" diye sordu Hayri. Yumak yeri kokladı. Sonra ağaçların arasına koştu ve kutuyu ağzında geri getirdi. Hayri kutuyu açtı ve baklavaların hepsinin yerinde olduğunu gördü. Sonra Hayri ile Yumak zil oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu"
   - Cümle 2: «Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi.»
   - Açıklama: Baklava dükkanı özelliği sorunun çözümünde işe yaramıyor, yalnız bir eşya olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0066` birebir aynı, `@degisim: ödemek -> koklamak` (tutuyorsan), ardından `@onarim: d7cef46d92a066fbd1bb8b7e9b4d2ade070e0c5c`, sonra gövde.

### Hikâye 5: tohum hayri-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0070
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'gardırop', fiil 'dökülmek', sıfat 'soğuk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: amca ağacın altında olduğu için bulutu göremedi | seslendi ve amcayı salıncakların yanına götürdü
@tohum: hayri-0070
@degisim: gardırop -> bulut
Soğuk bir rüzgar esiyordu. Hayri parkta gökyüzünde kocaman pembe bir bulut gördü. Ama Basri Amca onu göremedi, çünkü büyük bir ağacın altında oturuyordu. Ağacın yapraklarından yağmur damlaları dökülüyordu. Hayri bulutu amcaya da göstermek istedi. "Amca, gökyüzünde dünyanın en büyük bulutu var!" dedi Hayri abartarak. Basri Amca merak etti ve banktan kalktı. Hayri amcanın elinden tuttu ve onu salıncakların yanına götürdü. Orada ağaç yoktu ve her yer açıktı. Basri Amca başını kaldırdı ve pembe bulutu gördü. "Gerçekten çok büyükmüş, Hayri," dedi Basri Amca. Hayri ile Basri Amca oradaki banka oturdu ve bulutu mutlu mutlu izledi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın yapraklarından yağmur damlaları dökülüyordu"
   - Cümle 4: «Ağacın yapraklarından yağmur damlaları dökülüyordu.»
   - Açıklama: Yağmur damlaları ayrıntısı kuruluyor ama olayda hiç kullanılmıyor.
   - Açıklama: Yapraklardan dökülen yağmur damlaları olayda hiçbir işe yaramıyor ve pembe bulutlu açık gökle de uyuşmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 6: «"Amca, gökyüzünde dünyanın en büyük bulutu var!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0070` birebir aynı, `@degisim: gardırop -> bulut` (tutuyorsan), ardından `@onarim: 1d240090f5416e06113459d556b5a16da9c68cdc`, sonra gövde.

### Hikâye 6: tohum hayri-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0071
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'scooter', fiil 'sormak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: kütük çok sertti ve arkadaşı rahat oturamadı | çadırdan tüylü battaniyesini getirip kütüğe serdi
@tohum: hayri-0071
@degisim: scooter -> kitap
Bir sabah Hayri kamp yerinde Kamil ile oturuyordu. Kamil bir kütüğün üstünde kitap okumak istedi. Ama kütük çok sertti ve Kamil hemen ayağa kalktı. Hayri ona ne olduğunu sordu. Kamil kütüğün çok sert olduğunu söyledi. Hayri hemen çadıra koştu ve tüylü battaniyesini getirdi. Battaniyeyi ikiye katladı ve kütüğün üstüne serdi. Hayri biraz abarttı ve bunun ormandaki en yumuşak yer olduğunu söyledi. Kamil güldü ve battaniyenin üstüne oturdu. Kütük artık hiç sert değildi. Hayri de Kamil'in yanına oturdu. İki arkadaş kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı"
   - Cümle 8: «Hayri biraz abarttı ve bunun ormandaki en yumuşak yer olduğunu söyledi.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0071` birebir aynı, `@degisim: scooter -> kitap` (tutuyorsan), ardından `@onarim: d65e1138f570ed6b9dcbe57eb554e7d269a8d406`, sonra gövde.

### Hikâye 7: tohum hayri-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0072
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyonet', fiil 'ayırmak', sıfat 'özel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı | kumu elleriyle iki yana ayırıp kamyoneti çekti
@tohum: hayri-0072
Dalgalar kıyıya yavaşça vuruyordu. Hayri ile Akın, oyuncak kamyoneti kumla doldurup bir tepe yapıyordu. Birden büyük bir dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı. "Kamyonet denizin dibine gidiyor!" dedi Hayri. Hayri biraz abartmıştı. Akın güldü. "Hayır, yalnız tekerlekleri battı," dedi Akın. Hayri tekerleklerin önündeki kumu elleriyle iki yana ayırdı. Sonra kamyoneti yavaşça çekti ve kumdan çıkardı. "Teşekkürler, Hayri, bu kamyonet benim için çok özel!" dedi Akın. İki arkadaş kamyoneti dalgalardan uzağa, kuru kuma götürdü. Orada tepeyi büyütmeye mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı."
   - Cümle 5: «Hayri biraz abartmıştı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0072` birebir aynı, ardından `@onarim: 37765d05bba9b723f15a07b61c2fd8a0dd493e35`, sonra gövde.

### Hikâye 8: tohum hayri-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0073
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'saat', fiil 'hoplamak', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: küçük saat masadan düştü ve sisin içinde kayboldu | acıkınca saatin çalacağını anladı ve sesi dinledi
@tohum: hayri-0073
Kamp yerinde her yer çok sisliydi. Hayri küçük saatini masanın kenarına koymuştu. Ama saat şimdi masada yoktu. Sis yüzünden Hayri yerdeki çimenleri de iyi göremedi. Saat, öğle yemeğinde yüksek sesle çalacaktı. Biraz sonra Hayri çok acıktı. Hayri acıkınca öğle olduğunu anladı. Hemen durdu ve sessizce dinledi. Birden masanın yanındaki çalıdan saatin sesi geldi. Hayri sevinçle hopladı ve çalıya yürüdü. Saat masanın kenarından çalının dibine düşmüştü. Hayri saati aldı ve sesini kapattı. Sonra masaya oturdu ve yemeğini afiyetle yedi. Hayri bundan sonra saatini hep masanın ortasına koydu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama saat şimdi masada yoktu"
   - Cümle 3: «Ama saat şimdi masada yoktu.»
   - Açıklama: Saatin neden kaybolduğu sorun kurulurken söylenmiyor, ancak sonda açıklanıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Biraz sonra Hayri çok acıktı"
   - Cümle 6: «Biraz sonra Hayri çok acıktı.»
   - Açıklama: Hayri saati aramıyor, acıkıp saatin kendiliğinden çalmasını bekliyor; çözüm sebebe yönelmiyor ve rastlantıya dayanıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri acıkınca öğle olduğunu anladı"
   - Cümle 7: «Hayri acıkınca öğle olduğunu anladı.»
   - Açıklama: Saat zaten kendiliğinden çalacağı için acıkma ve öğleyi anlama sorunu çözmüyor; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0073` birebir aynı, ardından `@onarim: ffdd380af25b5a2f2c9d74c363a83ab42c5b6c89`, sonra gövde.

### Hikâye 9: tohum hayri-0074 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0074
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kumbara', fiil 'yankılanmak', sıfat 'kaygan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: yüksek sesle bağırdı ve uyuyan köpeği korkuttu | özür diledi ve ona simit verdi
@tohum: hayri-0074
@degisim: kumbara -> simit
Bir sabah Hayri kamp yerinde çok acıkmıştı. "Kahvaltı hazır!" diye yüksek sesle bağırdı Hayri. Sesi ağaçların arasında yankılandı ve uyuyan Yumak birden uyandı. Yumak korktu ve çadırın arkasına koştu. Hayri masadan bir simit aldı. Toprak kaygandı, bu yüzden Hayri çadırın arkasına yavaş yavaş yürüdü. Yumak orada yerde yatıyor ve ona bakıyordu. "Özür dilerim, Yumak, seni korkuttum," dedi Hayri yavaşça. Sonra simidi ikiye böldü ve küçük parçayı Yumak'ın önüne, yere bıraktı. Yumak simidi kokladı ve yedi. Sonra kuyruğunu sallayarak Hayri'nin yanına geldi. Hayri bundan sonra Yumak uyurken hep alçak sesle konuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sesi ağaçların arasında yankılandı"
   - Cümle 3: «Sesi ağaçların arasında yankılandı ve uyuyan Yumak birden uyandı.»
   - Açıklama: 'Yankılanmak' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Toprak kaygandı, bu yüzden Hayri"
   - Cümle 6: «Toprak kaygandı, bu yüzden Hayri çadırın arkasına yavaş yavaş yürüdü.»
   - Açıklama: Kaygan toprak sebepsiz ekleniyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Kaygan toprak işe yarayacakmış gibi kuruluyor ama olayda hiçbir sonucu olmuyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "küçük parçayı Yumak'ın önüne, yere bıraktı"
   - Cümle 9: «Sonra simidi ikiye böldü ve küçük parçayı Yumak'ın önüne, yere bıraktı.»
   - Açıklama: Korkmuş bir köpeğe yaklaşıp ona insan yiyeceği vermek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0074` birebir aynı, `@degisim: kumbara -> simit` (tutuyorsan), ardından `@onarim: 3869b400a4f99a105c83685ef7312e72ce042eae`, sonra gövde.

### Hikâye 10: tohum hayri-0077 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0077
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zeytin', fiil 'somurtmak', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpek kapağı sıkı tuttu ve hiç bırakmadı | kuma oturup sessizce bekledi
@tohum: hayri-0077
@degisim: zeytin -> kapak
Hayri kıyıda Yumak ile kapak yakalama oyunu oynuyordu. Kapak, Hayri'nin çalıştığı baklava dükkanından geliyordu ve güzel kokuyordu. Yumak bu kokuyu çok sevdi ve kapağı dişleriyle sıkı sıkı tuttu. Hayri'nin atma sırası hiç gelmiyordu ve Hayri somurttu. "Yumak, bırak!" dedi Hayri. Yumak kuyruğunu salladı ama kapağı bırakmadı. Hayri kuma oturdu ve sessizce bekledi. Biraz sonra Yumak geldi ve kapağı Hayri'nin önüne koydu. "Aferin, Yumak, şimdi sıra bende!" dedi Hayri. Kapağı uzağa attı ve Yumak koşup getirdi. Bu kez Yumak kapağı hemen verdi. Hayri çok sevindi, çünkü artık Yumak ile sırayla oynayabiliyordu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri kuma oturdu ve sessizce bekledi"
   - Cümle 7: «Hayri kuma oturdu ve sessizce bekledi.»
   - Açıklama: Sebep kapağın güzel kokusu iken beklemek bu sebebe yönelmiyor ve Yumak'ın kapağı neden bıraktığı açıklanmıyor.
   - Açıklama: Beklemek sorunun sebebine yönelmiyor; köpek kapağı kendiliğinden getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0077` birebir aynı, `@degisim: zeytin -> kapak` (tutuyorsan), ardından `@onarim: 6d53cb145522e1a8b8cd9b971ec7a9901a0534bb`, sonra gövde.

### Hikâye 11: tohum hayri-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0079
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kanepe', fiil 'çırpmak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: rüzgar esti ve örtünün kenarları havaya kalktı | örtünün dört ucuna büyük taşlar koydu
@tohum: hayri-0079
@degisim: kanepe -> kurabiye
Bir sabah Hayri kıyıda Akın'ın doğum günü için bir sürpriz hazırlıyordu. Kumun üstüne bir örtü serdi ve kurabiyeleri dizdi. Ama rüzgar esti ve örtünün kenarları havaya kalktı. Kurabiyeler kuma kaymaya başladı. Hayri çevreye baktı ve dört büyük taş topladı. Taşları örtünün dört ucuna koydu. Örtü artık uçmadı ve kurabiyeler yerinde kaldı. Hayri çok acıkmıştı ama kurabiyelere dokunmadı ve Akın'ı bekledi. Biraz sonra Akın kıyıya geldi. Hayri ellerini çırptı. "İyi ki doğdun, Akın!" dedi Hayri. Akın sevecen bir çocuktu ve hemen Hayri'ye sarıldı. "Bu en güzel sürpriz," dedi Akın. Hayri bundan sonra rüzgarlı günlerde örtünün ucuna hep taş koydu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Örtü artık uçmadı"
   - Cümle 7: «Örtü artık uçmadı ve kurabiyeler yerinde kaldı.»
   - Açıklama: Örtü uçmuyordu, kenarları kalkıyordu; fiil olaya uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ama kurabiyelere dokunmadı"
   - Cümle 8: «Hayri çok acıkmıştı ama kurabiyelere dokunmadı ve Akın'ı bekledi.»
   - Açıklama: Açlık ayrıntısı sorunla ya da çözümle bağlantısız, işlevsiz bir ek olarak giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0079` birebir aynı, `@degisim: kanepe -> kurabiye` (tutuyorsan), ardından `@onarim: 7eb01eefda53c588a01db287fd3b4864450520e1`, sonra gövde.

### Hikâye 12: tohum hayri-0080 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Kamil
@tohum: hayri-0080
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yüzük', fiil 'bitmek', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Kamil
@plan: boş kurabiye kutusundan bir ses geldi | kutuyu ters çevirdi ve içindeki yüzüğü buldu
@tohum: hayri-0080
Parkta hafif bir rüzgar esiyordu. Hayri acıkmıştı ve Kamil ile bankta kurabiye yiyordu. Kurabiyeler bitti ama Hayri kutuyu sallayınca içinden bir ses geldi. "Kamil, kutuda başka bir şey var!" dedi Hayri. Kamil kutunun içine baktı ama bir şey göremedi. "İçi çok karanlık," dedi Kamil. Hayri kutuyu ters çevirdi. Bankın üstüne kırıntılar ve masmavi bir yüzük düştü. "Bu, kutunun hediyesi olan oyuncak bir yüzük!" dedi Kamil. Hayri yüzüğü aldı ve güneşe tuttu. Sonra onu Kamil'e uzattı. Kamil yüzüğü parmağına taktı ve güldü. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri acıkmıştı ve Kamil ile bankta kurabiye yiyordu"
   - Cümle 2: «Hayri acıkmıştı ve Kamil ile bankta kurabiye yiyordu.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız geçiyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri acıkmıştı ve Kamil ile"
   - Cümle 2: «Hayri acıkmıştı ve Kamil ile bankta kurabiye yiyordu.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız anılıyor, sesin kaynağını bulma çözümünde işe yaramıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hayri kutuyu sallayınca içinden bir ses geldi"
   - Cümle 3: «Kurabiyeler bitti ama Hayri kutuyu sallayınca içinden bir ses geldi.»
   - Açıklama: Kutudan gelen ses çocuğun önemseyeceği gerçek bir sorun değil, tek hamlede biten önemsiz bir merak.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kutuyu sallayınca içinden bir ses geldi"
   - Cümle 3: «Kurabiyeler bitti ama Hayri kutuyu sallayınca içinden bir ses geldi.»
   - Açıklama: Kutudan gelen ses gerçek bir sorun değil, çocuğun önemseyeceği bir sıkıntı yaratmayan önemsiz bir merak olayı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kutunun hediyesi olan oyuncak"
   - Cümle 9: «"Bu, kutunun hediyesi olan oyuncak bir yüzük!" dedi Kamil.»
   - Açıklama: 'Kutunun hediyesi' anlamca tuhaf; kutu hediye vermez.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kutunun hediyesi olan oyuncak bir yüzük"
   - Cümle 9: «"Bu, kutunun hediyesi olan oyuncak bir yüzük!" dedi Kamil.»
   - Açıklama: Kutu hediye vermez; 'kutunun hediyesi' yanlış ve belirsiz bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0080` birebir aynı, ardından `@onarim: bae1ed56906a0483176c96f610a122440c9535b5`, sonra gövde.
