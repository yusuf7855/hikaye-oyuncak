# Editör görevi (onarım): Hayri, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar26.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0074 (deneme 3 -> 4)

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
@plan: yüksek sesle bağırdı ve uyuyan köpeği korkuttu | uzaktan özür diledi ve köpek yanına geldi
@tohum: hayri-0074
@degisim: kumbara -> simit
Bir sabah Hayri kamp yerinde çok acıkmıştı. Hayri masadan bir simit aldı ve "Kahvaltı hazır!" diye yüksek sesle bağırdı. Sesi ağaçlara çarpıp yankılandı ve uyuyan Yumak birden uyandı. Yumak korktu ve çadırın arkasına koştu. Hayri simidi yemedi ve masaya geri koydu. Çadırın arkasındaki toprak kaygandı, bu yüzden Hayri oraya gitmedi. Çadırın önünde yere oturdu. "Özür dilerim, Yumak, seni korkuttum," dedi Hayri yavaşça. Yumak başını çadırın arkasından çıkardı. Sonra kuyruğunu sallayarak Hayri'nin yanına geldi. Hayri simidini aldı ve Yumak'ın yanında yedi. Hayri bundan sonra Yumak uyurken hep alçak sesle konuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sesi ağaçlara çarpıp yankılandı"
   - Cümle 3: «Sesi ağaçlara çarpıp yankılandı ve uyuyan Yumak birden uyandı.»
   - Açıklama: Sesin ağaçlara çarpıp yankılanması 3 yaşındaki çocuk için soyut ve zor bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaçlara çarpıp yankılandı"
   - Cümle 3: «Sesi ağaçlara çarpıp yankılandı ve uyuyan Yumak birden uyandı.»
   - Açıklama: 'Yankılanmak' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çadırın arkasındaki toprak kaygandı"
   - Cümle 6: «Çadırın arkasındaki toprak kaygandı, bu yüzden Hayri oraya gitmedi.»
   - Açıklama: Kaygan toprak sebepsiz ortaya çıkıyor ve olaya hiçbir şey katmıyor.
   - Açıklama: Kaygan toprak ayrıntısı olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0074` birebir aynı, `@degisim: kumbara -> simit` (tutuyorsan), ardından `@onarim: dfd3ec3f071a26f7dc03a49407acc7802bcd0432`, sonra gövde.

### Hikâye 2: tohum hayri-0079 (deneme 3 -> 4)

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
Bir sabah Hayri kıyıda Akın'ın doğum günü için bir sürpriz hazırlıyordu. Kumun üstüne bir örtü serdi ve kurabiyeleri dizdi. Ama rüzgar esti ve örtünün kenarları havaya kalktı. Kurabiyeler kuma kaymaya başladı. Hayri çevreye baktı ve dört büyük taş topladı. Taşları örtünün dört ucuna koydu. Örtünün kenarları artık kalkmadı ve kurabiyeler yerinde durdu. Hayri çok acıkmıştı ama Akın'ı bekledi. Akın kıyıya geldi. Hayri ellerini çırptı. "İyi ki doğdun, Akın!" dedi Hayri. Akın sevecen bir çocuktu ve hemen Hayri'ye sarıldı. "Bu en güzel sürpriz," dedi Akın. İkisi kurabiyeleri birlikte yedi. Hayri bundan sonra rüzgarlı günlerde örtünün ucuna hep taş koydu.
```

**Hakem bulguları (1):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Akın sevecen bir çocuktu"
   - Cümle 12: «Akın sevecen bir çocuktu ve hemen Hayri'ye sarıldı.»
   - Açıklama: Kartın yanlar bölümünde Akın zeki ve hayvansever olarak tanımlanır; sevecenlik karttan olmayan bir huy olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0079` birebir aynı, `@degisim: kanepe -> kurabiye` (tutuyorsan), ardından `@onarim: 53a14a03778536e806436252c9d8e763ad034e33`, sonra gövde.

### Hikâye 3: tohum hayri-0080 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: garip bir ses geldi ve arkadaşı kitap okuyamadı | sesin karnından geldiğini buldu ve simidini paylaştı
@tohum: hayri-0080
Parkta hafif bir rüzgar esiyordu ve gökyüzü masmaviydi. Hayri ile Kamil bir bankta oturuyordu. Kamil kitap okumak istedi ama yakından garip bir ses geliyordu. "Hayri, bu ses nereden geliyor?" diye sordu Kamil. Hayri bankın altına baktı ama bir şey göremedi. Ses yine geldi ve bu kez Hayri'nin karnından geldi. Hayri çok acıkmıştı, bu yüzden karnı guruldamıştı. Hayri güldü ve çantasından yüzük gibi yuvarlak bir simit çıkardı. Simidi ikiye böldü ve yarısını Kamil'e verdi. İkisi simitlerini yedi ve ses bitti. "Şimdi kitabımı okuyabilirim," dedi Kamil. Hayri çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yedi ve ses bitti"
   - Cümle 10: «İkisi simitlerini yedi ve ses bitti.»
   - Açıklama: Ses bitmez, kesilir; fiil öznesine uygun değil.
   - Açıklama: Ses için 'bitti' uygun değil; 'ses kesildi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0080` birebir aynı, ardından `@onarim: ed1c903b8b6d7e5be7ad41283ed77c4246efe6f4`, sonra gövde.

### Hikâye 4: tohum hayri-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0081
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'top', fiil 'saklamak', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga kum tepesini yıktı ve top kayboldu | kumun yüksek kalan yerini kazdı ve topu buldu
@tohum: hayri-0081
@degisim: nazik -> sarı
Dalgaların sesi kıyıdan geliyordu. Hayri bir oyun için sarı topunu kuma sakladı. Üstüne kocaman bir tepe yaptı ama bir dalga tepeyi yıktı. Hayri topun yerini bulamadı. Kumun her yeri aynı görünüyordu. Hayri eğildi ve kuma dikkatle baktı. Tepe çok büyük olduğu için bir yerde kum biraz yüksek kalmıştı. Hayri orayı elleriyle kazdı. Kumun altından sarı top çıktı. Hayri topu havaya kaldırdı ve güldü. Hayri bu küçük dalgayı çok abarttı. Bu yüzden topu bu sefer dalgalardan çok uzağa, kuru kuma gömdü. Üstüne yine kocaman bir tepe yaptı. Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (8):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Hayri topun yerini bulamadı.»
   - Açıklama: Topun kaybolması sorunu ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Hayri topun yerini bulamadı"
   - Cümle 4: «Hayri topun yerini bulamadı.»
   - Açıklama: Asıl sorun olan topun kaybolması ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kumun her yeri aynı görünüyordu"
   - Cümle 5: «Kumun her yeri aynı görünüyordu.»
   - Açıklama: Kumun her yeri aynı görünürken birkaç cümle sonra bir yerin yüksek kaldığı söyleniyor; ayrıca tepeyi yıkan dalga küçük diye anılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu küçük dalgayı çok abarttı"
   - Cümle 11: «Hayri bu küçük dalgayı çok abarttı.»
   - Açıklama: Dalgayı abartmak anlamsız; fiil yanlış kullanılmış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri bu küçük dalgayı çok abarttı"
   - Cümle 11: «Hayri bu küçük dalgayı çok abarttı.»
   - Açıklama: 'Abartmak' fiili burada yanlış anlamda kullanılmış, cümle anlamsız.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu küçük dalgayı çok abarttı"
   - Cümle 11: «Hayri bu küçük dalgayı çok abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram, çocuk anlamaz.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri bu küçük dalgayı çok abarttı"
   - Cümle 11: «Hayri bu küçük dalgayı çok abarttı.»
   - Açıklama: Kartın özellikler alanındaki abartma sorunu çözmeye yaramıyor; top zaten bulunduktan sonra gerekçesiz biçimde ekleniyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bu küçük dalgayı çok abarttı"
   - Cümle 11: «Hayri bu küçük dalgayı çok abarttı.»
   - Açıklama: Çözümden sonra gelen bu abartma cümlesi olaydan çıkmıyor ve hikayede işlevi yok.
   - Açıklama: Sorun çözüldükten sonra olaydan çıkmayan yeni bir abartma ve yeniden gömme bölümü ekleniyor; ayrıca tepeyi yıkan dalga birden küçük diye anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0081` birebir aynı, `@degisim: nazik -> sarı` (tutuyorsan), ardından `@onarim: 4765ca29476d2f5c153e73457138bb42eb4b35e9`, sonra gövde.

### Hikâye 5: tohum hayri-0083 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0083
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tekne', fiil 'silkmek', sıfat 'kalın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek kuru yapraklarla oynuyordu ve tekneye gelmedi | ekmekten bir parça uzatıp köpeği tekneye çağırdı
@tohum: hayri-0083
Ormanda büyük ağaçların altında kalın bir kütük vardı. Hayri tekne oyunu oynuyordu ve kütük onun teknesiydi. Ama Yumak tekneye gelmedi, çünkü kuru yapraklarla oynuyordu. "Yumak, gel, yola çıkıyoruz!" dedi Hayri. Yumak ona hiç bakmadı. Hayri acıkınca yemek kokusuna hemen koşardı. Bu yüzden çantasından ekmeğini çıkardı. Ekmekten küçük bir parça kopardı ve Yumak'a uzattı. "Bu parça senin, Yumak!" dedi Hayri. Yumak ekmeğin kokusunu aldı ve koşarak geldi. Tekneye atladı ve tüylerindeki yaprakları silkti. Sonra parçayı yedi ve kuyruğunu salladı. Hayri de ekmeğin kalanını yedi. Hayri ile Yumak tekne oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri acıkınca yemek kokusuna hemen koşardı."
   - Cümle 6: «Hayri acıkınca yemek kokusuna hemen koşardı.»
   - Açıklama: Yemek kokusuna koşan köpek Yumak olmalı; özne yanlış kişi olarak Hayri yazılmış.
   - Açıklama: Yemek kokusuna koşma özelliği köpek Yumak'a ait olmalı; özne yanlış kişi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri acıkınca yemek kokusuna hemen koşardı"
   - Cümle 6: «Hayri acıkınca yemek kokusuna hemen koşardı.»
   - Açıklama: Çözüme Hayri'nin kendi açlığından 'bu yüzden' diye geçiliyor; bu sebep Yumak'ı çağırmakla mantıksal olarak bağlanmıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri acıkınca yemek kokusuna hemen koşardı"
   - Cümle 6: «Hayri acıkınca yemek kokusuna hemen koşardı.»
   - Açıklama: Gerekçe köpeğe değil Hayri'ye yazılmış, bu yüzden 'Bu yüzden' ile gelen ekmek çözümü mantıksız kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0083` birebir aynı, ardından `@onarim: 17faba72e7f27e5cb03828985f63d0b541bc934e`, sonra gövde.

### Hikâye 6: tohum hayri-0084 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0084
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ay', fiil 'vermek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: koşarken arkadaşına çarptı ve onun sütü döküldü | özür diledi ve ona baklava verdi
@tohum: hayri-0084
Bir akşam ormandaki kamp yerinde gökyüzüne büyük bir ay çıktı. Hayri, Mert'e gökyüzünü göstermek için koşarken ona çarptı. Mert'in elindeki ılık süt yere döküldü. Mert boş bardağına üzgün üzgün baktı. Hayri hemen durdu ve Mert'in yanına gitti. "Özür dilerim, Mert, koşmamalıydım," dedi Hayri. Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti. Kutuyu çantasından çıkardı ve açtı. Hayri en büyük baklavayı Mert'e verdi. Mert onu yedi ve gülümsedi. "Çok güzelmiş, teşekkür ederim," dedi Mert. "Hadi, Mert, şimdi aya birlikte bakalım!" dedi Hayri.
```

**Hakem bulguları (5):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hayri kamp için, çalıştığı"
   - Cümle 7: «Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti.»
   - Açıklama: 'Kamp için' ile 'çalıştığı' arasındaki virgül gereksiz.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hayri kamp için, çalıştığı dükkandan"
   - Cümle 7: «Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti.»
   - Açıklama: 'kamp için' ile 'çalıştığı' arasındaki virgül yersiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti"
   - Cümle 7: «Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti.»
   - Açıklama: Baklava tam gerektiği anda önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı dükkandan bir kutu baklava getirmişti"
   - Cümle 7: «Hayri kamp için, çalıştığı dükkandan bir kutu baklava getirmişti.»
   - Açıklama: Baklava kutusu önceden kurulmadan çözüm anında beliriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "en büyük baklavayı Mert'e verdi"
   - Cümle 9: «Hayri en büyük baklavayı Mert'e verdi.»
   - Açıklama: Dökülen süt yerine konmuyor; baklava vermek sorunun sebebine doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0084` birebir aynı, ardından `@onarim: a20b022059b4b4a4143227e8eca40a08777515b3`, sonra gövde.

### Hikâye 7: tohum hayri-0085 (deneme 2 -> 3)

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
Parkın kum havuzunda Hayri bir kale yapıyordu. Hayri çok yüksek bir kale yapmak istiyordu. Ama kum çok kuruydu ve kale her seferinde yıkıldı. Hayri yıkılan kaleyi çok abarttı. Bu yüzden kırmızı kovasını aldı ve çeşmeden su doldurdu. Suyu döktü ve kumu iyice ıslattı. Islak kum artık sıkı sıkı duruyordu. Hayri kovayı kumla doldurdu ve ters çevirdi. Ağaçtan düşmüş kalın bir kabukla duvarları düzeltti. Kovayı bir kez daha doldurdu ve üstüne bir kule yaptı. Bu sefer hiçbir şey yıkılmadı. Hayri çok sevindi, çünkü yüksek kalesi artık dimdik duruyordu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri yıkılan kaleyi çok abarttı"
   - Cümle 4: «Hayri yıkılan kaleyi çok abarttı.»
   - Açıklama: 'Abartmak' fiili burada yanlış anlamda kullanılmış ve cümle anlamsız.
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; cümle anlamsız.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yıkılan kaleyi çok abarttı"
   - Cümle 4: «Hayri yıkılan kaleyi çok abarttı.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yıkılan kaleyi çok abarttı"
   - Cümle 4: «Hayri yıkılan kaleyi çok abarttı.»
   - Açıklama: Tohumdaki abartma özelliği sorunun çözümüne hiç katkı vermeden, işe yaramayan bir ek olarak geçiyor.
   - Açıklama: Kartın özellikler alanındaki abartma çözüme işe yarar biçimde bağlanmıyor; su getirmenin nedeni abartma olamaz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri yıkılan kaleyi çok abarttı"
   - Cümle 4: «Hayri yıkılan kaleyi çok abarttı.»
   - Açıklama: Abartma olaydan çıkmıyor ve 'Bu yüzden' ile gelen su getirme eylemine sebep olamıyor; işlevsiz, bağlantısız bir ayrıntı.
   - Açıklama: Kaleyi abartmak anlamsız bir olay ve su getirmenin sebebi olamaz; 'Bu yüzden' bağı kopuk.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağaçtan düşmüş kalın bir kabukla duvarları düzeltti"
   - Cümle 9: «Ağaçtan düşmüş kalın bir kabukla duvarları düzeltti.»
   - Açıklama: Kabuk sebepsiz beliriyor ve sorunun çözümüne katkısı olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0085` birebir aynı, `@degisim: kurutmak -> ıslatmak` (tutuyorsan), ardından `@onarim: 513bc3539dd78e52bad04b37809b7234f677ffae`, sonra gövde.

### Hikâye 8: tohum hayri-0087 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0087
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'pantolon', fiil 'yazmak', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kağıt küçüktü ve büyük harfler sığmadı | çubukla toprağa büyük harflerle yazdı
@tohum: hayri-0087
Bir sabah Hayri kamp yerinde dükkan oyunu oynuyordu. Oyun dükkanına bir ad yazmak istedi ama pantolonunun cebindeki kağıt çok küçüktü. Büyük harfler bu kağıda sığmadı. Hayri mahalledeki baklava dükkanında çalışıyordu. Oradaki tabelanın harfleri uzaktan bile görünüyordu. Hayri ağaçların arasında düz bir toprak parçası buldu. Yerdeki uzun bir çubuğu aldı. Çubukla toprağa dükkanın adını kocaman harflerle yazdı. Sonra birkaç adım geri gidip yazıya baktı. Yazı şimdi uzaktan da kolayca okunuyordu. Sonra bir taşın üstüne tatlı yerine yeşil yapraklar dizdi. Hayri çok sevindi, çünkü artık onun da büyük bir tabelası vardı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri mahalledeki baklava dükkanında çalışıyordu"
   - Cümle 4: «Hayri mahalledeki baklava dükkanında çalışıyordu.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği sorunu çözmekte işe yaramıyor, yalnız arka plan bilgisi olarak ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri mahalledeki baklava dükkanında çalışıyordu"
   - Cümle 4: «Hayri mahalledeki baklava dükkanında çalışıyordu.»
   - Açıklama: Baklava dükkanı ve tabelası olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Kamp yerindeki oyunun ortasında mahalledeki baklava dükkanı sebepsizce anılıyor ve olayı ilerletmeyen işlevsiz bir ayrıntı olarak kalıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dükkanın adını kocaman harflerle"
   - Cümle 8: «Çubukla toprağa dükkanın adını kocaman harflerle yazdı.»
   - Açıklama: Oyun dükkanı mı baklava dükkanı mı olduğu belli değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bir taşın üstüne tatlı yerine yeşil yapraklar dizdi"
   - Cümle 11: «Sonra bir taşın üstüne tatlı yerine yeşil yapraklar dizdi.»
   - Açıklama: Çözümden sonra sorunla ilgisiz yeni bir olay sebepsiz ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0087` birebir aynı, ardından `@onarim: d11d6221b5dd471c1b4735db7ed2893fd07f35c0`, sonra gövde.

### Hikâye 9: tohum hayri-0088 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0088
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kasa', fiil 'aydınlatmak', sıfat 'harika'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: parmakla kesince kumdan baklava dağıldı | düz bir deniz kabuğuyla kumu kesti
@tohum: hayri-0088
Deniz kıyısında kumun üstünde boş bir tahta kasa duruyordu. Hayri dükkan oyunu oynuyordu ve kasa onun baklava tepsisiydi. Kasaya ıslak kum doldurdu ama parmağıyla kesince kum dağıldı. Hayri kıyıda yürüdü ve yere dikkatle baktı. Kumda düz ve ince bir deniz kabuğu buldu. Hayri baklava dükkanında çalıştığı için baklavanın nasıl kesildiğini iyi biliyordu. Kabukla kumu küçük kareler halinde kesti. Sonra her karenin üstüne fıstık yerine küçük bir taş koydu. Güneş kasayı aydınlattı ve ıslak kum parladı. Harika bir tepsi olmuştu. Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "parmağıyla kesince kum dağıldı"
   - Cümle 3: «Kasaya ıslak kum doldurdu ama parmağıyla kesince kum dağıldı.»
   - Açıklama: Kumun parmakla kesince neden dağıldığı söylenmiyor; sorunun sebebi açık değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kumu küçük kareler halinde"
   - Cümle 7: «Kabukla kumu küçük kareler halinde kesti.»
   - Açıklama: 'Halinde' kalıbı 3 yaşındaki bir çocuğun bilmediği soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0088` birebir aynı, ardından `@onarim: 9c7a048e9454d1b06783890ea99f598889e0d438`, sonra gövde.

### Hikâye 10: tohum hayri-0089 (deneme 2 -> 3)

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
@degisim: yeşermek -> zıplamak
Hayri parkta Yumak ile koku oyunu oynuyordu. Simit kırıntılarını çimlere saklıyordu, Yumak da onları kokluyor ve buluyordu. Ama Yumak çok hızlıydı ve kırıntılar çabuk bitti. Yumak kuyruğunu salladı ve Hayri'ye baktı. Hayri sık sık acıktığı için parka hazırlıklı gelmişti. Çantasında bir simit daha vardı. Simidi ikiye ayırdı ve yarısını kendisi yedi. Öbür yarısını küçük küçük kırıntı yaptı ve çimlere serpti. "Hadi, Yumak, bul bakalım!" dedi Hayri. Yumak burnunu yere yaklaştırdı ve çimlerde koştu. Her kırıntıyı buldukça sevinçle zıpladı ve havladı. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü oyunları yarım kalmamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "parka hazırlıklı gelmişti"
   - Cümle 5: «Hayri sık sık acıktığı için parka hazırlıklı gelmişti.»
   - Açıklama: 'Hazırlıklı gelmek' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0089` birebir aynı, `@degisim: yeşermek -> zıplamak` (tutuyorsan), ardından `@onarim: 0a105a56b444e84891ff20380f295c9ff6c9af92`, sonra gövde.

### Hikâye 11: tohum hayri-0090 (deneme 2 -> 3)

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
Deniz kıyısında ıslak kumun üstünde tuhaf bir kabuk vardı. Hayri onu aldı ve abarttı, bu kabuk onun için bir hazineydi. Ama kabuğun öbür yarısı yoktu, çünkü dalgalar onu kırmıştı. Kabuğun üstünde pembe ve mavi çizgiler vardı. Hayri öbür yarısını bulmak için kıyıda yavaş yavaş yürüdü. Kumdaki her kabuğa dikkatle baktı. Sonunda taşların arasında aynı çizgileri olan bir parça gördü. Hayri iki parçayı yan yana koydu ve birleştirdi. Parçalar tam oturdu ve çizgiler bir yıldız şekli yaptı. Hayri kabuğu iki eliyle tuttu ve ona güneşte uzun uzun baktı. Hayri çok sevindi, çünkü tuhaf kabuğun öbür yarısını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri onu aldı ve abarttı"
   - Cümle 2: «Hayri onu aldı ve abarttı, bu kabuk onun için bir hazineydi.»
   - Açıklama: 'Abarttı' fiili burada anlamsız ve nesnesiz kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aldı ve abarttı"
   - Cümle 2: «Hayri onu aldı ve abarttı, bu kabuk onun için bir hazineydi.»
   - Açıklama: 'Abarttı' yanlış anlamda kullanılmış; cümleye uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri onu aldı ve abarttı"
   - Cümle 2: «Hayri onu aldı ve abarttı, bu kabuk onun için bir hazineydi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri onu aldı ve abarttı"
   - Cümle 2: «Hayri onu aldı ve abarttı, bu kabuk onun için bir hazineydi.»
   - Açıklama: Tohumdaki abartma özelliği yalnız anılıyor, sorunun çözümünde hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0090` birebir aynı, `@degisim: saman -> kabuk` (tutuyorsan), ardından `@onarim: b59bf96061035c845829135e820a0463b09389bf`, sonra gövde.

### Hikâye 12: tohum hayri-0091 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0091
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bitki', fiil 'havalanmak', sıfat 'uykulu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: rüzgar esince pastanın üstündeki bitkiler havalandı | bitkileri ıslak kuma sıkıca bastırdı
@tohum: hayri-0091
Bir sabah deniz kıyısında Mert çok uykuluydu. Hayri onu sevindirmek için kumdan bir pasta yaptı. Ama rüzgar esince pastanın üstüne dizdiği bitkiler havalandı. Hayri bitkileri tek tek toplayıp geri getirdi. Bu kez hepsini ıslak kuma sıkıca bastırdı. Rüzgar yine esti ama bitkiler yerinde kaldı. Sonra Hayri, Mert'in omzuna yavaşça dokundu. "Mert, bak, sana bir sürprizim var!" dedi Hayri. Mert başını kaldırdı ve pastayı gördü. "Bu dünyanın en büyük, en güzel pastası!" dedi Hayri abartarak. Mert yüksek sesle güldü ve ayağa kalktı. "Teşekkürler, Hayri, bu pasta harika olmuş!" dedi Mert.
```

**Hakem bulguları (4):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Mert çok uykuluydu"
   - Cümle 1: «Bir sabah deniz kıyısında Mert çok uykuluydu.»
   - Açıklama: Kartta uykuyu seven Kamil'dir, Mert sakin ve düzenli olarak tanımlanır; uykululuk Mert'e aktarılmış görünüyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pastanın üstüne dizdiği bitkiler havalandı"
   - Cümle 3: «Ama rüzgar esince pastanın üstüne dizdiği bitkiler havalandı.»
   - Açıklama: Rüzgarın kum pastadaki bitkileri uçurması önemsiz bir olay; 'dağıttı, topladı, bitti' kalıbına çok yakın.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 10: «"Bu dünyanın en büyük, en güzel pastası!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bu dünyanın en büyük"
   - Cümle 10: «"Bu dünyanın en büyük, en güzel pastası!" dedi Hayri abartarak.»
   - Açıklama: Gösterme zamirinden sonra virgül eksik; 'Bu, dünyanın' olmalı, yoksa 'bu dünyanın' diye okunuyor.
   - Açıklama: Özneden sonra virgül eksik; 'Bu, dünyanın' olmalı, yoksa 'bu dünyanın' diye okunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0091` birebir aynı, ardından `@onarim: 766a92bdf817a0e217819f94cc43036350a9b5a1`, sonra gövde.
