# Yazar görevi: Hayri, parti 32

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki 24 tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v3/aday/hayri_32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### Hayri | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v3/aday/hayri_32.txt --ad urun_v3`
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

## Tohumlar

### Hayri | ev | Akın
@tohum: hayri-0745
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ceviz', fiil 'oturmak', sıfat 'kirli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | park | Kamil
@tohum: hayri-0746
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çekmece', fiil 'öğrenmek', sıfat 'lezzetli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | deniz | Akın
@tohum: hayri-0747
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yün', fiil 'bağlamak', sıfat 'benekli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | park | Mert
@tohum: hayri-0748
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'turşu', fiil 'mırıldanmak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | deniz | Basri Amca
@tohum: hayri-0749
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'saksı', fiil 'kıpırdamak', sıfat 'sert'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | park | Yumak
@tohum: hayri-0750
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'baharat', fiil 'koşuşturmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | ev | Kamil
@tohum: hayri-0751
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'su', fiil 'değmek', sıfat 'boyalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | deniz | -
@tohum: hayri-0752
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'satranç', fiil 'çekinmek', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | orman | Akın
@tohum: hayri-0753
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'gitar', fiil 'uçurmak', sıfat 'şanslı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | orman | Kamil
@tohum: hayri-0754
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'brokoli', fiil 'getirmek', sıfat 'mor'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | orman | -
@tohum: hayri-0755
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabak', fiil 'aramak', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | orman | -
@tohum: hayri-0756
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kitaplık', fiil 'esnemek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | park | Mert
@tohum: hayri-0757
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fiyonk', fiil 'sığınmak', sıfat 'şeffaf'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | orman | -
@tohum: hayri-0758
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'lale', fiil 'boşalmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | deniz | Yumak
@tohum: hayri-0759
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'ipek', fiil 'girmek', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)

### Hayri | deniz | Basri Amca
@tohum: hayri-0760
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'etiket', fiil 'uyanmak', sıfat 'meyveli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | orman | -
@tohum: hayri-0761
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'lamba', fiil 'silmek', sıfat 'parlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | deniz | -
@tohum: hayri-0762
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'gümüş', fiil 'gülmek', sıfat 'taze'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | park | -
@tohum: hayri-0763
- yer: park (Mahallenin çocuk parkı.)
- tema: bir şey yapmak
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'battaniye', fiil 'rahatlatmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))

### Hayri | park | Basri Amca
@tohum: hayri-0764
- yer: park (Mahallenin çocuk parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kurdele', fiil 'almak', sıfat 'masmavi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | deniz | Kamil
@tohum: hayri-0765
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kamil
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kask', fiil 'seyretmek', sıfat 'değerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | deniz | Akın
@tohum: hayri-0766
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'beşik', fiil 'öpmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)

### Hayri | orman | Mert
@tohum: hayri-0767
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kek', fiil 'hatırlamak', sıfat 'sabırlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)

### Hayri | deniz | -
@tohum: hayri-0768
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'bambu', fiil 'giyinmek', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
