# Editör görevi (onarım): Hayri, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0135 (deneme 1 -> 2)

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
@plan: kaydırakta nereden geldiği bilinmeyen bir ışık vardı | başını salladı ve ışığı kaskının yaptığını buldu
@tohum: hayri-0135
Bir sabah Hayri parkta yarış oyunu oynuyordu. Kırmızı kaskını takmış, hızlı hızlı koşuyordu. Birden kaydırağın üstünde küçük bir ışık ışıldadı. Hayri bu ışığın nereden geldiğini çok merak etti. Etrafa baktı ama bir şey bulamadı. Sonra durdu ve ışık da kaydırakta durdu. Hayri abartarak başını sağa sola kocaman salladı. Işık da kaydırakta bir o yana bir bu yana gitti. Hayri eliyle kaskını tuttu ve güldü. Işık, kaskın parlak üstünden geliyordu! Sonra Hayri ışığı kaydırakta gezdirdi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "küçük bir ışık ışıldadı"
   - Cümle 3: «Birden kaydırağın üstünde küçük bir ışık ışıldadı.»
   - Açıklama: 'Işık ışıldadı' aynı kökü gereksiz tekrarlıyor.
   - Açıklama: 'Işık ışıldadı' gereksiz tekrar.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "başını sağa sola kocaman salladı"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: 'Kocaman' boyut bildirir, sallama fiiline uymuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sağa sola kocaman salladı"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: 'Kocaman' sıfatı fiili nitelemek için yanlış kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak başını sağa"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak başını"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: 'Abartarak' soyut bir kelime, küçük çocuk bilmez.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak başını sağa sola kocaman salladı"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartma yalnız kocaman bir baş hareketi olarak kullanılıyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak başını sağa sola"
   - Cümle 7: «Hayri abartarak başını sağa sola kocaman salladı.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek); burada abartı yalnız bedensel büyük bir harekete dönüşmüş, özellik karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0135` birebir aynı, ardından `@onarim: c12fa1216b7aac3a47317998447761804d8353a3`, sonra gövde.

### Hikâye 2: tohum hayri-0137 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: oyun yemeği taştı ve taşlar yenmezdi | acıkınca sandviçini ve elmasını tabaklara koydu
@tohum: hayri-0137
Hayri kamp yerinde yemek yapma oyunu oynuyordu. Büyük bir taşın üstüne yapraktan tabaklar dizdi. Ama tabakların üstünde yalnız küçük taşlar vardı ve taşlar yenmezdi. Tam o sırada Hayri acıktı. Taşları kaldırdı. Çantasından sandviçini ve kırmızı elmasını çıkardı. Sandviçi bir tabağa, elmayı öbür tabağa koydu. Yerde düşmüş bir tomurcuk buldu ve süs için tabağın kenarına yerleştirdi. Sonra Hayri bir adım geri çekildi ve tabaklara baktı. Her şey mükemmel görünüyordu. Hayri yemeğini afiyetle yedi. Hayri çok mutlu oldu, çünkü oyunu gerçek bir yemekle bitmişti.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oyun yemeği taştı ve"
   - Cümle 0 (plan satırı): «oyun yemeği taştı ve taşlar yenmezdi | acıkınca sandviçini ve elmasını tabaklara koydu»
   - Açıklama: 'Taştı' hem 'taş idi' hem 'taşmak' olarak okunabiliyor; anlam belirsiz.
   - Açıklama: 'Taştı' hem 'taş idi' hem 'taşmak' fiili olarak okunuyor, anlam belirsiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tabakların üstünde yalnız küçük taşlar vardı ve taşlar yenmezdi"
   - Cümle 3: «Ama tabakların üstünde yalnız küçük taşlar vardı ve taşlar yenmezdi.»
   - Açıklama: Oyun yemeğinin taş olması oyunun doğası; çocuğun önemseyeceği gerçek bir sorun değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "taşlar yenmezdi"
   - Cümle 3: «Ama tabakların üstünde yalnız küçük taşlar vardı ve taşlar yenmezdi.»
   - Açıklama: Oyun yemeğinin yenmemesi gerçek bir sorun değil; sorun saçma ve önemsiz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 4: «Tam o sırada Hayri acıktı.»
   - Açıklama: Çözümü sebepsiz bir rastlantı olan acıkma getiriyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Yerde düşmüş bir tomurcuk"
   - Cümle 8: «Yerde düşmüş bir tomurcuk buldu ve süs için tabağın kenarına yerleştirdi.»
   - Açıklama: Hal eki yanlış; 'yere düşmüş' olmalı.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düşmüş bir tomurcuk buldu"
   - Cümle 8: «Yerde düşmüş bir tomurcuk buldu ve süs için tabağın kenarına yerleştirdi.»
   - Açıklama: 'Tomurcuk' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yerde düşmüş bir tomurcuk buldu"
   - Cümle 8: «Yerde düşmüş bir tomurcuk buldu ve süs için tabağın kenarına yerleştirdi.»
   - Açıklama: Tomurcuk sebepsiz beliriyor ve olayda işlevi yok.
   - Açıklama: Tomurcuk sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0137` birebir aynı, ardından `@onarim: 94fc9d13102159ac87f4d14cba4969cbf3b36ed3`, sonra gövde.

### Hikâye 3: tohum hayri-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0138
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hortum', fiil 'soğumak', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: tek kova vardı ve ikisi de aynı anda istedi | acıkınca sırayı arkadaşına verip önce yemeğini yedi
@tohum: hayri-0138
@degisim: hortum -> kova
Hayri ile Akın deniz kıyısında kumda küçük bir havuz kazdı. Kum güneşte çok sıcaktı. Havuz için yalnız bir kova vardı. İkisi de kovayı aynı anda çekti. Esnek kova iki yana uzadı. Tam o sırada Hayri acıktı. Çantasında bir sandviç vardı. "Akın, sen önce su taşı, ben de sandviçimi yerim," dedi Hayri. Akın sevindi ve kovayla deniz kenarından su getirdi. Hayri sandviçini yedi ve Akın'ı izledi. "Sıra sende, Hayri," dedi Akın ve kovayı ona verdi. Hayri de havuza su döktü. Havuz dolunca sıcak kum da soğudu. Sonra Hayri ile Akın sırayla su taşımaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Esnek kova iki yana uzadı"
   - Cümle 5: «Esnek kova iki yana uzadı.»
   - Açıklama: Kova esnemez ve uzamaz; sıfat ve fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Esnek kova iki yana uzadı"
   - Cümle 5: «Esnek kova iki yana uzadı.»
   - Açıklama: 'Esnek' küçük çocuğun bilmeyeceği bir kelime ve kovanın uzaması tuhaf.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Esnek kova iki yana uzadı"
   - Cümle 5: «Esnek kova iki yana uzadı.»
   - Açıklama: Uzayan esnek kova, kartın çağdaş mahalle dünyasında (tohum_yasak_kategoriler: buyu) olmayan gerçek dışı bir eşya özelliğidir.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Esnek kova iki yana uzadı"
   - Cümle 5: «Esnek kova iki yana uzadı.»
   - Açıklama: Kovanın esneyip uzaması işlevsiz ve tuhaf bir ayrıntı, sıcak kumun soğuması da olaya bağlanmıyor.
   - Açıklama: Kovanın esneyip uzaması tuhaf ve işlevsiz bir ayrıntı; olayda hiçbir işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 6: «Tam o sırada Hayri acıktı.»
   - Açıklama: Çözüm Hayri'nin paylaşma kararından değil, rastlantısal bir acıkmadan çıkıyor.
   - Açıklama: Kova kavgasının çözümünü sebepsiz bir acıkma rastlantısı getiriyor.
   - Açıklama: Çözüm, Hayri'nin tesadüfen acıkmasıyla sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0138` birebir aynı, `@degisim: hortum -> kova` (tutuyorsan), ardından `@onarim: 26622d6aaa77c343bee62bbf69793186abe42a4d`, sonra gövde.

### Hikâye 4: tohum hayri-0139 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0139
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'cips', fiil 'eşleştirmek', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: küçük elleriyle yaptığı gölge uçağa benzemiyordu | kollarını kocaman açıp büyük bir uçak gölgesi yaptı
@tohum: hayri-0139
@degisim: cips -> gölge
Güneş parlıyordu ve kamp yeri çok aydınlıktı. Hayri, Basri Amca'yla ilk kez gölge oyunu oynuyordu. Basri Amca yere büyük bir uçak gölgesi yaptı ama Hayri bunu yapamadı. Çünkü Hayri'nin elleri çok küçüktü. "Hayri, iki gölgeyi eşleştirmek ister misin?" diye sordu Basri Amca. Hayri biraz düşündü. Sonra abartarak iki kolunu kocaman açtı. Yerde kanatları uzun, büyük bir uçak gölgesi belirdi. "Aferin, Hayri, senin uçağın benimkinden de büyük!" dedi Basri Amca ve güldü. "Teşekkürler, Basri Amca, bu oyun çok güzel!" dedi Hayri.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çünkü Hayri'nin elleri çok küçüktü"
   - Cümle 4: «Çünkü Hayri'nin elleri çok küçüktü.»
   - Açıklama: 'Çünkü' ile başlayan cümle ana cümlesinden kopuk, yarım bir yan cümle olarak kalmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki gölgeyi eşleştirmek ister misin?"
   - Cümle 5: «"Hayri, iki gölgeyi eşleştirmek ister misin?" diye sordu Basri Amca.»
   - Açıklama: 'Eşleştirmek' burada yanlış anlamda kullanılmış; Basri Amca gölgeleri eşleştirmeyi değil, uçak gölgesi yapmayı kastediyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gölgeyi eşleştirmek ister misin?"
   - Cümle 5: «"Hayri, iki gölgeyi eşleştirmek ister misin?" diye sordu Basri Amca.»
   - Açıklama: 'Eşleştirmek' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime ve burada anlamı belirsiz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "iki gölgeyi eşleştirmek ister misin"
   - Cümle 5: «"Hayri, iki gölgeyi eşleştirmek ister misin?" diye sordu Basri Amca.»
   - Açıklama: Basri Amca'nın gölge eşleştirme sorusu olaydan çıkmıyor ve çözüme hiçbir katkı sağlamıyor.
   - Açıklama: Gölge eşleştirme önerisi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra abartarak iki kolunu"
   - Cümle 7: «Sonra abartarak iki kolunu kocaman açtı.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuk için soyut bir kelime.
   - Açıklama: 'Abartarak' soyut bir kelime ve 3 yaşındaki bir çocuk bunu bilmez.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra abartarak iki kolunu kocaman açtı"
   - Cümle 7: «Sonra abartarak iki kolunu kocaman açtı.»
   - Açıklama: Kartta özellik olayları abartmaktır; burada yalnız kolları açmak olarak kullanılıyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra abartarak iki kolunu kocaman"
   - Cümle 7: «Sonra abartarak iki kolunu kocaman açtı.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek); burada abartı yalnız bedensel büyük bir harekete dönüşmüş, özellik karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0139` birebir aynı, `@degisim: cips -> gölge` (tutuyorsan), ardından `@onarim: cdf9076a5cce2618ae75a0cbaf685604c2b0200d`, sonra gövde.

### Hikâye 5: tohum hayri-0140 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0140
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'erik', fiil 'sarılmak', sıfat 'değerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: küçük kalp yukarıdaki banktan görünmüyordu | kumun üstüne kocaman bir kalp çizdi
@tohum: hayri-0140
Hayri deniz kıyısında Basri Amca'nın doğum günü için sürpriz hazırlıyordu. Kumun üstüne bir kalp çizmişti ama kalp çok küçüktü. Basri Amca yukarıdaki bankta oturuyordu ve küçük kalbi oradan göremezdi. Hayri abartarak bu kez kocaman bir kalp çizdi. Ortasına da getirdiği bir sepet eriği koydu. "Basri Amca, aşağı bak!" diye seslendi Hayri. Basri Amca kocaman kalbi gördü ve Hayri'nin yanına geldi. Ona sıkıca sarıldı. "Bu sürpriz benim için çok değerli," dedi Basri Amca. Sonra Hayri ile Basri Amca kıyıya oturup erikleri mutlu mutlu yediler.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bu kez"
   - Cümle 4: «Hayri abartarak bu kez kocaman bir kalp çizdi.»
   - Açıklama: 'Abartarak' soyut bir kelime ve burada yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bu kez kocaman"
   - Cümle 4: «Hayri abartarak bu kez kocaman bir kalp çizdi.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez ve burada yerinde kullanılmamış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak bu kez kocaman bir kalp çizdi"
   - Cümle 4: «Hayri abartarak bu kez kocaman bir kalp çizdi.»
   - Açıklama: Kartta özellik olayları abartmaktır; burada yalnız büyük çizmek olarak kullanılıyor.
   - Açıklama: Karttaki özellik olayları abartmak iken burada abartma bir şeyi büyük çizmek olarak kartın tarifinden farklı kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0140` birebir aynı, ardından `@onarim: 8b9c1685fa732a7acba544f6b730df01c4c721df`, sonra gövde.

### Hikâye 6: tohum hayri-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0141
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: kaybolan eşya
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'sofra', fiil 'durdurmak', sıfat 'konuşkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: baklava kutusu yolda sepetten düşüp kaybolmuştu | köpekten yardım isteyip kutuyu birlikte buldu
@tohum: hayri-0141
@degisim: konuşkan -> tatlı
Hayri kamp yerinde bir sofra kuruyordu. Çalıştığı baklava dükkanından bir kutu tatlı baklava getirmişti. Ama kutu yürürken sepetten düşüp kaybolmuştu. Yumak da yanında kuyruğunu sallıyordu. Hayri boş sepeti Yumak'ın burnuna uzattı. "Yumak, bu kokuyu bulabilir misin?" diye sordu Hayri. Yumak sepeti kokladı ve ağaçların arasına koştu. Yumak bir çalının yanında durdu ve havladı. Kutu çalının altındaydı! Yumak kutuya yaklaştı ama Hayri onu nazikçe durdurdu. "Dur, Yumak, baklava köpekler için değil," dedi Hayri. Hayri kutuyu alıp sofranın ortasına koydu. "Teşekkürler, Yumak, baklavayı birlikte bulduk!" dedi Hayri.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çalıştığı baklava dükkanından bir kutu"
   - Cümle 2: «Çalıştığı baklava dükkanından bir kutu tatlı baklava getirmişti.»
   - Açıklama: Tohum özelliği (baklava dükkanında çalışmak) yalnız kaybolan eşyanın kaynağı olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama kutu yürürken sepetten"
   - Cümle 3: «Ama kutu yürürken sepetten düşüp kaybolmuştu.»
   - Açıklama: Kutu yürümez; zarf-fiil öznesine uymuyor.
   - Açıklama: 'Yürürken' kutuya bağlanıyor; kutu yürümez, yürüyen Hayri'dir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yumak kutuya yaklaştı ama Hayri onu nazikçe durdurdu"
   - Cümle 10: «Yumak kutuya yaklaştı ama Hayri onu nazikçe durdurdu.»
   - Açıklama: Köpeğin baklavaya yönelmesi sorunla ilgisiz, çözümden sonra eklenen işlevsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0141` birebir aynı, `@degisim: konuşkan -> tatlı` (tutuyorsan), ardından `@onarim: 39538e923b47dd4ea41d99f1eef836794b6c28c6`, sonra gövde.

### Hikâye 7: tohum hayri-0142 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0142
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'jöle', fiil 'ovuşturmak', sıfat 'uzun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: soğuk parmaklarıyla arkadaşı kabın kapağını açamadı | ellerini hızlı hızlı ovuşturdu ve ona da gösterdi
@tohum: hayri-0142
Bir sabah Hayri ile Akın kamp yerindeydi ve hava çok serindi. Akın küçük bir jöle kabını açmak istedi. Ama parmakları soğuktu ve kapağı sıkıca tutamadı. Hayri bunu gördü ve arkadaşına yardım etmek istedi. "Akın, sana bir yol göstereyim," dedi Hayri. Hayri abartarak ellerini çok hızlı ve uzun uzun ovuşturdu. Bir yandan da tren gibi ses çıkardı. Akın güldü ve o da aynısını yaptı. Parmakları hemen ısındı. Akın kapağı kolayca açtı. "Teşekkürler, Hayri, sen de biraz jöle ister misin?" diye sordu Akın. Hayri çok sevindi, çünkü arkadaşına yardım edebilmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sana bir yol göstereyim"
   - Cümle 5: «"Akın, sana bir yol göstereyim," dedi Hayri.»
   - Açıklama: 'Yol göstermek' burada mecaz anlamda kullanılmış.
   - Açıklama: 'Yol göstermek' burada mecazdır, küçük çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak ellerini"
   - Cümle 6: «Hayri abartarak ellerini çok hızlı ve uzun uzun ovuşturdu.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0142` birebir aynı, ardından `@onarim: b37387acb5d157e1e0e2e5bf44635beaf656da8e`, sonra gövde.

### Hikâye 8: tohum hayri-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0143
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çember', fiil 'yaklaştırmak', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çember belinde dönmüyordu ve hemen yere düşüyordu | belini güçlü ve hızlı salladı
@tohum: hayri-0143
Deniz kıyısında güneş parlıyordu. Hayri kumda ilk kez çember çevirmeyi deniyordu. Ama çember her seferinde düştü, çünkü Hayri belini çok yavaş sallıyordu. Hayri çemberi yerden aldı ve biraz düşündü. Çemberi iki eliyle beline yaklaştırdı. Sonra abartarak belini kocaman, güçlü ve hızlı salladı. Çember belinde bir kez, iki kez, üç kez döndü! Hayri durmadı ve saymaya devam etti. Çember tam on kez dönüp kuma indi. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü yeni oyunu sonunda öğrenmişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "belini güçlü ve hızlı salladı"
   - Cümle 0 (plan satırı): «çember belinde dönmüyordu ve hemen yere düşüyordu | belini güçlü ve hızlı salladı»
   - Açıklama: Planda 'güçlü' zarf olarak yanlış kullanılmış; 'güçlüce' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "belini kocaman, güçlü ve hızlı salladı"
   - Cümle 6: «Sonra abartarak belini kocaman, güçlü ve hızlı salladı.»
   - Açıklama: 'Kocaman' boyut sıfatıdır, sallama eylemini nitelemez.
   - Açıklama: 'Kocaman' ve 'güçlü' zarf olarak bel sallamaya uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra abartarak belini"
   - Cümle 6: «Sonra abartarak belini kocaman, güçlü ve hızlı salladı.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime.
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra abartarak belini kocaman"
   - Cümle 6: «Sonra abartarak belini kocaman, güçlü ve hızlı salladı.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek); burada abartı yalnız bedensel büyük bir harekete dönüşmüş, özellik karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0143` birebir aynı, ardından `@onarim: 0c543e3a3b8eac4bee5c25ff493509fe714d1284`, sonra gövde.

### Hikâye 9: tohum hayri-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0144
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'araba', fiil 'çözülmek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: tozlu yolda nereden geldiği bilinmeyen ince izler vardı | acıkınca çantasını açtı ve izleri arabasının yaptığını anladı
@tohum: hayri-0144
Bir sabah Hayri parkın tozlu yolunda ince izler gördü. İzler bankın yanından yokuş aşağı bir çalıya gidiyordu. Hayri bu izleri neyin yaptığını çok merak etti. Önce eğilip yere baktı ama bir şey anlamadı. Tam o sırada Hayri acıktı ve çantasını bıraktığı banka döndü. Sandviçini almak için çantasını açtı. Çantaya bağlı oyuncak arabasının ipi boştu. Düğüm çözülmüştü ve havalı mavi arabası yoktu! Hayri güldü, çünkü izleri kendi arabası yapmıştı. Çalıya gitti ve arabasını altında buldu. İpi sıkıca yeniden bağladı ve sandviçini yedi. Hayri çok sevindi, çünkü izleri neyin yaptığını bulmuştu.
```

**Hakem bulguları (7):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 5: «Tam o sırada Hayri acıktı ve çantasını bıraktığı banka döndü.»
   - Açıklama: Çözüm izlerin sebebine yönelmiyor; Hayri acıktığı için tesadüfen çantayı açıp cevabı buluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada Hayri acıktı"
   - Cümle 5: «Tam o sırada Hayri acıktı ve çantasını bıraktığı banka döndü.»
   - Açıklama: Çözüm Hayri'nin acıkması gibi rastlantısal bir olayla sebepsizce geliyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sandviçini almak için çantasını açtı"
   - Cümle 6: «Sandviçini almak için çantasını açtı.»
   - Açıklama: Çözüm izlerin sebebine yönelmiyor; Hayri başka bir iş için çantayı açınca cevabı tesadüfen buluyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sandviçini almak için çantasını açtı"
   - Cümle 6: «Sandviçini almak için çantasını açtı.»
   - Açıklama: Çözümü figürün çabası değil, sebepsiz gelen acıkma ve sandviç tesadüfü getiriyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "havalı mavi arabası yoktu"
   - Cümle 8: «Düğüm çözülmüştü ve havalı mavi arabası yoktu!»
   - Açıklama: 'Havalı' argo bir kelime, 3 yaşındaki çocuğa uygun değil.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çalıya gitti ve arabasını altında buldu"
   - Cümle 10: «Çalıya gitti ve arabasını altında buldu.»
   - Açıklama: 'altında' tamlayansız kalmış, arabanın altı gibi okunuyor; 'arabasını çalının altında buldu' olmalı.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "gitti ve arabasını altında buldu"
   - Cümle 10: «Çalıya gitti ve arabasını altında buldu.»
   - Açıklama: 'Altında' kimin altını gösterdiği belli değil; 'çalının altında' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0144` birebir aynı, ardından `@onarim: bbf845fa4c255aa1a555ff8c4e8f7c87bc0bbf19`, sonra gövde.

### Hikâye 10: tohum hayri-0145 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0145
- yer: park (Mahallenin çocuk parkı.)
- tema: paylaşmak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'perde', fiil 'bölmek', sıfat 'kahverengi'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: arkadaşının sandviçi kuma düştü ve yiyecek bir şeyi kalmadı | acıkınca kekini çıkarıp ikiye böldü ve paylaştı
@tohum: hayri-0145
@degisim: perde -> kek
Parkta Hayri ile Mert salıncaktan yeni inmişti. Mert sandviçini çıkardı ama sandviç elinden kayıp kuma düştü. Artık yiyecek bir şeyi kalmamıştı ve Mert üzüldü. Tam o sırada Hayri de acıktı. Çantasından kahverengi bir kek çıkardı. Hayri keke ve üzgün arkadaşına baktı. Sonra keki tam ortadan ikiye böldü. Parçalardan birini Mert'e uzattı. Mert gülümsedi ve teşekkür etti. İkisi banka oturdu ve kekleri birlikte yediler. Hayri çok mutlu oldu, çünkü aç olduğu halde kekini paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "banka oturdu ve kekleri birlikte yediler"
   - Cümle 10: «İkisi banka oturdu ve kekleri birlikte yediler.»
   - Açıklama: Aynı özneye 'oturdu' tekil, 'yediler' çoğul çekimle bağlanmış; uyum bozuk.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kekleri birlikte yediler"
   - Cümle 10: «İkisi banka oturdu ve kekleri birlikte yediler.»
   - Açıklama: 'İkisi' öznesiyle çoğul 'yediler' uyumsuz ve aynı cümledeki 'oturdu' ile tutarsız; 'yedi' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aç olduğu halde kekini"
   - Cümle 11: «Hayri çok mutlu oldu, çünkü aç olduğu halde kekini paylaşmıştı.»
   - Açıklama: 'olduğu halde' yapısı 3 yaşındaki çocuk için soyut ve zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0145` birebir aynı, `@degisim: perde -> kek` (tutuyorsan), ardından `@onarim: 8ec405f2dcf6fe89de36bfc81b5142ca25022db4`, sonra gövde.
