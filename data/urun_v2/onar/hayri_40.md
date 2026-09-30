# Editör görevi (onarım): Hayri, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0122 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0122
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pelerin', fiil 'tutunmak', sıfat 'açık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: sürpriz bitmeden amca erken geldi | amcayı güldürdü ve sürprizi hızla bitirdi
@tohum: hayri-0122
@degisim: pelerin -> örtü
Bir sabah Hayri ormanda Basri Amca'ya doğum günü sürprizi hazırlıyordu. Açık bir yere örtü serdi ve üstüne çiçek koymaya başladı. Ama sürpriz bitmeden Basri Amca erken geldi. Hayri koşarak amcanın önüne geçti. "Amca, şimdi bakarsan dünyanın en büyük sürprizi bozulur!" dedi Hayri. Hayri'nin abarttığını anlayan Basri Amca güldü ve gözlerini kapattı. Hayri hızla dönüp son çiçekleri de koydu. Basri Amca gözleri kapalı Hayri'nin koluna tutundu ve yürüdü. "Şimdi bak, iyi ki doğdun!" dedi Hayri. Amca çiçekleri görünce gülümsedi. "Çok güzel bir sürpriz, teşekkürler, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü sürprizini tam zamanında bitirmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dünyanın en büyük sürprizi"
   - Cümle 5: «"Amca, şimdi bakarsan dünyanın en büyük sürprizi bozulur!" dedi Hayri.»
   - Açıklama: Abartılı söz mecaz ve soyut, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri'nin abarttığını anlayan"
   - Cümle 6: «Hayri'nin abarttığını anlayan Basri Amca güldü ve gözlerini kapattı.»
   - Açıklama: 'Abartmak' ve 'abarttığını anlamak' 3 yaşındaki çocuk için soyut bir kavram.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri'nin abarttığını anlayan Basri Amca"
   - Cümle 6: «Hayri'nin abarttığını anlayan Basri Amca güldü ve gözlerini kapattı.»
   - Açıklama: 'Abartmak' soyut bir kavramdır ve 3 yaşındaki bir çocuk bu kelimeyi bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0122` birebir aynı, `@degisim: pelerin -> örtü` (tutuyorsan), ardından `@onarim: 121263b28296ba7a1593bf523065f186bf3d6dd4`, sonra gövde.

### Hikâye 2: tohum hayri-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0123
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'keman', fiil 'dizmek', sıfat 'sarı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: kozalaklar uzaktı ve top onlara çarpmadı | kozalakları tepsideki baklava gibi yan yana dizdi
@tohum: hayri-0123
@degisim: keman -> kozalak
Ormandaki kamp yerinde Hayri ile Yumak sırayla oynuyordu. Hayri yere kozalakları dizdi ve sarı topu onlara yuvarladı. Ama kozalaklar birbirinden uzaktı ve top hiçbir kozalağa çarpmadı. Yumak da topu itti ama yine hiçbiri devrilmedi. Yumak kulaklarını indirdi ve yere yattı. Hayri dükkanda baklavaları tepsiye sıkı sıkı dizerdi. Şimdi kozalakları da öyle, yan yana dizdi. "Sıra yine sende, Yumak!" dedi Hayri. Yumak kalktı, koştu ve topa burnuyla vurdu. Top ilk kozalağa çarptı ve hepsi birden devrildi. Yumak havladı ve kuyruğunu salladı. "Aferin, Yumak, çok güzel vurdun!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Hayri dükkanda baklavaları tepsiye sıkı sıkı dizerdi"
   - Cümle 6: «Hayri dükkanda baklavaları tepsiye sıkı sıkı dizerdi.»
   - Açıklama: Anlatım -dı'lı geçmişten -erdi'li geçmişe kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0123` birebir aynı, `@degisim: keman -> kozalak` (tutuyorsan), ardından `@onarim: 186f100fd8b633ae1b4f95f47fe0fc8ac0a1f157`, sonra gövde.

### Hikâye 3: tohum hayri-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0124
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'salatalık', fiil 'toplamak', sıfat 'çıtır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: bir dalga salatalık dolu örtüye doğru geldi | amcaya bağırdı ve salatalıkları hızla topladı
@tohum: hayri-0124
Deniz kıyısında Hayri ile Basri Amca kuma bir örtü sermişti. Örtü suya yakındı ve üstünde çıtır salatalıklar vardı. Birden örtüye doğru bir dalga geldi. Basri Amca oturuyordu ve dalgayı görmedi. "Amca, kocaman bir dalga geliyor, kalk!" diye bağırdı Hayri. Basri Amca hemen ayağa kalktı ve sepeti aldı. Hayri de salatalıkları hızla topladı ve sepete koydu. Dalga küçüktü ama örtünün ucunu ıslattı. Salatalıklar sepette hiç ıslanmadı. "Biraz abarttın ama iyi ki bağırdın, Hayri," dedi Basri Amca gülerek. Sonra Hayri ile Basri Amca kuru kumda salatalıkları mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hemen ayağa kalktı ve sepeti aldı"
   - Cümle 6: «Basri Amca hemen ayağa kalktı ve sepeti aldı.»
   - Açıklama: Daha önce hiç kurulmamış bir sepet çözümü getirmek için sebepsizce beliriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Basri Amca hemen ayağa kalktı ve sepeti aldı"
   - Cümle 6: «Basri Amca hemen ayağa kalktı ve sepeti aldı.»
   - Açıklama: Sepet daha önce hiç kurulmadan sebepsizce beliriyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri de salatalıkları hızla topladı"
   - Cümle 7: «Hayri de salatalıkları hızla topladı ve sepete koydu.»
   - Açıklama: Suya yakın örtüye dalga gelirken çocuğun eşya toplamak için orada kalması taklit edilince tehlikeli olabilir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Biraz abarttın ama iyi"
   - Cümle 10: «"Biraz abarttın ama iyi ki bağırdın, Hayri," dedi Basri Amca gülerek.»
   - Açıklama: 'abarttın' soyut bir kelime; 3 yaşındaki çocuk bilmez.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Biraz abarttın ama"
   - Cümle 10: «"Biraz abarttın ama iyi ki bağırdın, Hayri," dedi Basri Amca gülerek.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0124` birebir aynı, ardından `@onarim: 69c122c89296581dac1d9858d262b5239562dd54`, sonra gövde.

### Hikâye 4: tohum hayri-0125 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0125
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yorgan', fiil 'koşmak', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı pembe yorganına yattı ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı
@tohum: hayri-0125
Bir sabah Hayri ile Kamil deniz kıyısında yarış yapacaktı. Ama uyumayı çok seven Kamil pembe yorganına yattı ve uyudu. "Kamil, kalk, yarış zamanı!" dedi Hayri. Kamil uyanmadı, yalnız yorganın üstünde döndü. Hayri arkadaşının omzuna dokundu ama Kamil gözlerini açmadı. Hayri acıkmıştı ve çantasında sıcak bir simit vardı. Güzel koku belki Kamil'i uyandırırdı. Hayri simidi Kamil'in burnuna doğru tuttu. Kamil gözlerini açtı ve "Bu koku ne?" diye sordu. Hayri güldü, simidi ikiye böldü ve yarısını Kamil'e verdi. İkisi simidi yedi ve kumda koşarak yarıştı. Hayri çok sevindi, çünkü Kamil sonunda uyanmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kamil pembe yorganına yattı"
   - Cümle 2: «Ama uyumayı çok seven Kamil pembe yorganına yattı ve uyudu.»
   - Açıklama: Yorgana yatılmaz, yorganın altına girilir ya da yatağa yatılır; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0125` birebir aynı, ardından `@onarim: 74c30e8ec388a2eb04e9cba40d86da9e77c50e9b`, sonra gövde.

### Hikâye 5: tohum hayri-0127 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0127
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fide', fiil 'koparmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga kovayı götürdü ve kale yarım kaldı | boş baklava kutusunu kova yaptı ve sırayla doldurdular
@tohum: hayri-0127
@degisim: fide -> kova
Deniz kıyısında Hayri ile Akın sırayla kumdan kale yapıyordu. Hayri kovayı dolduruyor, Akın ters çeviriyordu. Birden bir dalga geldi ve kovayı alıp uzağa götürdü. Akın üzüldü, çünkü kale daha yarımdı. Hayri çantasına baktı ve dükkandan getirdiği boş baklava kutusunu buldu. Az önce kutudaki baklavaları birlikte yemişlerdi. Hayri kutunun kapağını kopardı ve kutuyu kova gibi kullandı. "Şimdi sıra sende, Akın," dedi Hayri. Akın kutuyu kumla doldurdu ve ters çevirdi. Kumdan kare bir kule çıktı. Akın kuleyi çok beğendi ve memnun memnun ellerini çırptı. Hayri ile Akın sırayla kuleler yaptı ve kaleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "memnun memnun ellerini çırptı"
   - Cümle 11: «Akın kuleyi çok beğendi ve memnun memnun ellerini çırptı.»
   - Açıklama: 'Memnun memnun' doğal olmayan bir ikileme; 'memnunca' ya da 'sevinçle' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve memnun memnun ellerini"
   - Cümle 11: «Akın kuleyi çok beğendi ve memnun memnun ellerini çırptı.»
   - Açıklama: 'Memnun memnun' ikilemesi ve 'memnun' kelimesi 3 yaşındaki çocuk için ağır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0127` birebir aynı, `@degisim: fide -> kova` (tutuyorsan), ardından `@onarim: 2092b98e189ca1641969216997814b326b3e8244`, sonra gövde.

### Hikâye 6: tohum hayri-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0128
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'avokado', fiil 'basmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: adımları küçük olduğu için resim kumda belli olmadı | adımlarını büyüttü ve kuma sertçe bastı
@tohum: hayri-0128
@degisim: avokado -> güneş
Deniz kıyısında Hayri kuma basarak bir resim yapıyordu. Şapkalı bir güneş yapmak istiyordu. Ama adımları küçüktü ve güneş kumda hiç belli olmadı. Hayri anlattığı her şeyi hep abartırdı. Bu kez güneşi de öyle kocaman yapacaktı. Uzun adımlar attı ve kuma sertçe bastı. Güneşin ışıklarını iki ayağıyla zıplayarak yaptı. Sonra güneşin üstüne büyük adımlarla bir şapka yaptı. Geri çekildi ve resmine baktı. Resim artık çok büyük ve belliydi. Hayri çok güldü ve sevindi, çünkü şapkalı güneş uzaktan bile görünüyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "anlattığı her şeyi hep abartırdı"
   - Cümle 4: «Hayri anlattığı her şeyi hep abartırdı.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: 'Abartmak' soyut bir kavramdır ve olayla somut bağı yoktur.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez güneşi de öyle kocaman yapacaktı"
   - Cümle 5: «Bu kez güneşi de öyle kocaman yapacaktı.»
   - Açıklama: Karttaki özellik olayları abartmak (anlatmak) iken hikayede resmi büyük çizmeye çevrilmiş, ozellikler alanındaki biçimiyle kullanılmıyor.
   - Açıklama: Kartta özellik olayları abartmak iken burada resmi kocaman yapmaya kaydırılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0128` birebir aynı, `@degisim: avokado -> güneş` (tutuyorsan), ardından `@onarim: f12ae7fdf8c0ebe016250ec42e6df5d182aca8e5`, sonra gövde.

### Hikâye 7: tohum hayri-0129 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0129
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: kaybolan eşya
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabela', fiil 'işaretlemek', sıfat 'güzel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: rüzgar dükkanın tabelasını uçurdu ve tabela kayboldu | yaprakların toplandığı köşeye bakıp tabelayı buldu
@tohum: hayri-0129
@degisim: işaretlemek -> asmak
Evlerin arasındaki sokakta sert bir rüzgar esiyordu. Hayri'nin çalıştığı dükkan da bu sokaktaydı. Dükkanın güzel tabelası kaybolmuştu. Rüzgar tabelayı kapıdan düşürmüş ve alıp götürmüştü. Mert de Hayri'ye yardım etmek için geldi. İkisi evlerin önüne baktı ama tabelayı bulamadı. Hayri dükkanın önünü süpürürken yaprakları hep köşedeki duvarın yanında bulurdu. "Rüzgar yaprakları o köşeye götürür, Mert," dedi Hayri. İkisi köşeye koştu. Tabela yaprakların arasında, duvarın yanında duruyordu. Hayri tabelayı kaldırdı ve üstündeki yaprakları silkti. Sonra ikisi tabelayı dükkanın kapısına sıkıca astı. Hayri, Mert'e bir dilim baklava verdi ve ikisi mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Evlerin arasındaki sokakta sert bir rüzgar esiyordu"
   - Cümle 1: «Evlerin arasındaki sokakta sert bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye sokakta ve dükkanın önünde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta ve dükkanın önünde geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0129` birebir aynı, `@degisim: işaretlemek -> asmak` (tutuyorsan), ardından `@onarim: 9af1679bf85a8b25457ef193ecf49f2232fa862f`, sonra gövde.

### Hikâye 8: tohum hayri-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0130
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'dalga', fiil 'kalkmak', sıfat 'geniş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: dalga köpeğin topunu suya çekti | geniş tepsiyi uzatıp topu kıyıya getirdi
@tohum: hayri-0130
Bir sabah Hayri deniz kıyısında Yumak'la top oynuyordu. Birden bir dalga geldi ve Yumak'ın topunu suya çekti. Top kıyıya çok yakın, sığ suda sallanıyordu ama Hayri'nin eli yetişmedi. Yumak topa bakıp havladı ve kuma oturdu. Hayri suya girmedi ve kuru kumda durdu. Hayri dükkanda baklavaları geniş bir tepsiyle taşırdı. O tepsi şimdi de yanındaydı, onu dükkana geri götürecekti. Geniş tepsiyi aldı ve ucunu topa uzattı. Tepsiyle topu yavaşça kendine doğru çekti. Top kuma yuvarlandı. Yumak hemen kalktı ve topa koştu. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. Hayri çok sevindi, çünkü Yumak'ın topunu dalgadan geri almıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O tepsi şimdi de yanındaydı"
   - Cümle 7: «O tepsi şimdi de yanındaydı, onu dükkana geri götürecekti.»
   - Açıklama: Baklava tepsisi kumsalda tam gerektiği anda sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Baklava tepsisi kumsalda sebepsizce beliriyor ve çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0130` birebir aynı, ardından `@onarim: b9fe7f4abc2608be685fb0fbd4e0a3eb0cf63299`, sonra gövde.

### Hikâye 9: tohum hayri-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0133
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'mektup', fiil 'eğmek', sıfat 'beyaz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: rüzgar arkadaşının mektubunu kumda sürükledi | kağıdın ucuna baklava kutusunu koydu
@tohum: hayri-0133
Hayri, dükkandan getirdiği bir kutu baklavayla Mert'in yanına oturdu. Mert beyaz bir kağıda mektup yazıyordu. Ama rüzgar esti ve mektubu kumda sürükledi. Mert kağıdı yakaladı ama rüzgar yine esti. "Böyle yazamıyorum," dedi Mert. Hayri baklava kutusunu kağıdın ucuna koydu. Kutu ağırdı ve kağıt artık hiç kıpırdamadı. Mert başını eğdi ve mektubunu rahatça bitirdi. Sonra Hayri kutuyu açtı ve Mert'e bir baklava verdi. "Teşekkürler, Hayri, hem mektubum bitti hem de baklava geldi!" dedi Mert.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kağıdın ucuna baklava kutusunu koydu"
   - Cümle 0 (plan satırı): «rüzgar arkadaşının mektubunu kumda sürükledi | kağıdın ucuna baklava kutusunu koydu»
   - Açıklama: Plan kutuyu figürün koyduğunu söylüyor ama gövdede kutuyu Mert koyuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0133` birebir aynı, ardından `@onarim: 0271cffc07cd7411ac7df269f2d56ad524446430`, sonra gövde.

### Hikâye 10: tohum hayri-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0135
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kask', fiil 'ışıldamak', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kaydırakta nereden geldiği bilinmeyen bir ışık vardı | başını sağa sola çevirdi ve ışığı kaskının yaptığını buldu
@tohum: hayri-0135
Bir sabah Hayri parkta yarış oyunu oynuyordu. Kırmızı kaskını takmış, hızlı hızlı koşuyordu. Birden kaydırağın üstünde küçük bir şey ışıldadı. Hayri bu ışığın nereden geldiğini çok merak etti. Etrafa baktı ama bir şey bulamadı. Sonra durdu ve ışık da kaydırakta durdu. Hayri abarttı ve bu ışığı kaçan bir yıldız sandı. Yıldıza bakmak için başını sağa sola çevirdi. Işık da kaydırakta bir o yana bir bu yana gitti. Hayri eliyle kaskını tuttu ve güldü. Işık, kaskın parlak üstünden geliyordu! Sonra Hayri ışığı kaydırakta gezdirdi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ışığın nereden geldiğini çok merak etti"
   - Cümle 4: «Hayri bu ışığın nereden geldiğini çok merak etti.»
   - Açıklama: Işığın nereden geldiği sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abarttı ve bu"
   - Cümle 7: «Hayri abarttı ve bu ışığı kaçan bir yıldız sandı.»
   - Açıklama: 'Abarttı' fiili burada yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu ışığı kaçan bir yıldız sandı"
   - Cümle 7: «Hayri abarttı ve bu ışığı kaçan bir yıldız sandı.»
   - Açıklama: 'Abarttı' soyut, 'kaçan yıldız' mecazlı; küçük çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve bu"
   - Cümle 7: «Hayri abarttı ve bu ışığı kaçan bir yıldız sandı.»
   - Açıklama: 'abarttı' soyut bir kelime ve burada yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0135` birebir aynı, ardından `@onarim: 3d05f841b3dd09610ecfac3c5520512e529be5fd`, sonra gövde.

### Hikâye 11: tohum hayri-0136 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0136
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'parfüm', fiil 'korunmak', sıfat 'pahalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: parkta tatlı bir koku geldi | acıktığı için kokuyu izledi ve çiçekli bir çalı buldu
@tohum: hayri-0136
@degisim: korunmak -> koklamak
Hayri parkta salıncakta sallanıyordu. Birden rüzgarla tatlı bir koku geldi. Hayri bu kokunun nereden geldiğini çok merak etti. Koku kek kokusuna benziyordu. Hayri çok acıkmıştı, bu yüzden hemen salıncaktan indi. Burnunu havaya kaldırdı ve kokuyu izleyerek yürüdü. Parkın köşesinde beyaz çiçekli bir çalı vardı. Ama orada hiç kek yoktu. Hayri eğildi ve küçük çiçekleri kokladı. Tatlı koku bu çiçeklerden geliyordu. Çiçekler pahalı bir parfüm gibi güzel kokuyordu. Hayri kek ararken çiçek bulduğuna çok güldü. Hayri bundan sonra parka gelince bu çalının yanına da gitti.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "parkta tatlı bir koku geldi"
   - Cümle 0 (plan satırı): «parkta tatlı bir koku geldi | acıktığı için kokuyu izledi ve çiçekli bir çalı buldu»
   - Açıklama: Tatlı bir koku gelmesi sorun değil; hikayede çözülecek gerçek bir güçlük yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgarla tatlı bir koku geldi"
   - Cümle 2: «Birden rüzgarla tatlı bir koku geldi.»
   - Açıklama: Bir kokunun gelmesi sorun değil; hikayede gerçek bir sorun kurulmuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı"
   - Cümle 5: «Hayri çok acıkmıştı, bu yüzden hemen salıncaktan indi.»
   - Açıklama: Açlık olayı yönlendiriyormuş gibi kuruluyor ama hiç giderilmiyor ve sonuçsuz kalıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çiçekler pahalı bir parfüm gibi"
   - Cümle 11: «Çiçekler pahalı bir parfüm gibi güzel kokuyordu.»
   - Açıklama: 'Pahalı bir parfüm gibi' benzetmesi soyut ve 3 yaşındaki çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pahalı bir parfüm gibi"
   - Cümle 11: «Çiçekler pahalı bir parfüm gibi güzel kokuyordu.»
   - Açıklama: 'Pahalı bir parfüm gibi' benzetmesi soyut ve 3 yaşındaki çocuğa uygun değil.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hayri bundan sonra parka gelince bu çalının yanına da gitti"
   - Cümle 13: «Hayri bundan sonra parka gelince bu çalının yanına da gitti.»
   - Açıklama: 'Bundan sonra' ile süreklilik anlatılırken görünen geçmiş kullanılmış; 'giderdi' olmalı.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri bundan sonra parka gelince bu çalının yanına da gitti"
   - Cümle 13: «Hayri bundan sonra parka gelince bu çalının yanına da gitti.»
   - Açıklama: Son cümle olaydan çıkan bir ders ya da sıcak kapanış değil, açlık hedefi de karşılanmadan çıplak bir alışkanlıkla bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0136` birebir aynı, `@degisim: korunmak -> koklamak` (tutuyorsan), ardından `@onarim: 8914932697de03b61f82a13787630a6134b36246`, sonra gövde.

### Hikâye 12: tohum hayri-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0137
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tomurcuk', fiil 'çekilmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: tabak eğri kütüğün üstünde kayıyordu | tabağı büyük ve düz bir taşa koydu
@tohum: hayri-0137
@degisim: tomurcuk -> sandviç
Hayri kamp yerinde yemek yapma oyunu oynuyordu. Çok acıkmıştı, bu yüzden kendine peynirli bir sandviç hazırladı. Ama tabak kütüğün üstünde durmadı, çünkü kütük eğriydi. Tabak kaydı ve sandviç neredeyse yere düşüyordu. Hayri tabağı hemen tuttu ve etrafa baktı. Ağaçların arasında büyük ve düz bir taş gördü. Tabağı bu taşın üstüne koydu. Tabak artık hiç kaymadı. Hayri bir adım geri çekildi ve tabağa baktı. Sandviç mükemmel görünüyordu. Hayri taşın yanına oturdu ve sandviçini yedi. Hayri çok sevindi, çünkü sandviçini yere düşürmeden yiyebilmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sandviç mükemmel görünüyordu"
   - Cümle 10: «Sandviç mükemmel görünüyordu.»
   - Açıklama: 'Mükemmel' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0137` birebir aynı, `@degisim: tomurcuk -> sandviç` (tutuyorsan), ardından `@onarim: d54e935ce4055f139b010301bf7078a16c3b9939`, sonra gövde.
