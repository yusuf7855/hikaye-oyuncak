# Popüler karakter hikâyeleri — yazım kılavuzu

Dinleyici 3–6 yaş. Hikâyeler NFC figürlü bir oyuncakta sesli okunacak ve KÜÇÜK bir dil modelini eğitecek.
Model bu hikâyeleri taklit eder; bu yüzden TUTARLILIK, SADELİK ve KURALLARA KESİN UYUM her şeyden önemli.
Bu sette figürler çocukların sevdiği bilinen karakterlerdir. Her karakterin **karakter kartı**
`data/oyuncak_populer/karakterler.json` dosyasındadır: kim olduğu, arkadaşları, hangi yerlerde geçebileceği ve
dikkat edilecekler. Hikâye o karakterin KENDİ DÜNYASINDA geçmeli; çizgi filmini izlemiş bir çocuk "evet, bu Elsa"
demeli (Elsa'nın buz güçleri, kardeşi Anna, kardan adam Olaf; Peppa'nın çamur birikintileri ve George...).

## HEDEF ÖRNEK (kullanıcı 10/10 verdi; her hikâye bu sadelikte ve bu netlikte olmalı)

    ### ejderha | orman | yardım etmek
    @plan: karınca ağır yaprağı yuvasına taşıyamadı | birlikte yaprağı yuvaya taşıdılar

    Ormanın kenarında Alev adında küçük ve sevimli bir ejderha yaşardı. Ateş yerine ağzından rengarenk
    baloncuklar üflerdi. Bir gün küçük bir karınca ağır bir yaprağı taşımaya çalışıyordu ama başaramıyordu.
    Alev karıncayı görünce yanına gitti. "Yardım eder misin?" diye sordu karınca. "Elbette, yardım ederim."
    dedi Alev. İkisi birlikte yaprağı karıncanın yuvasına taşıdılar. Karınca çok mutlu oldu. "Yardımın için
    teşekkür ederim." dedi karınca. Alev mutlulukla gülümsedi çünkü birine yardım etmek onu iyi hissettirmişti.
    O günden sonra her gün birlikte oynadılar.

## Biçim (kesin)

    ### <karakter adı> | <yer> | <tema>
    @plan: <sorun> | <çözüm>

    <hikâye metni>

- karakter adı: kartındaki `isim` aynen (Elsa, Peppa, Bluey, Chase, Pepee, Niloya, Maşa, Örümcek Adam, Gabby,
  Stitch, Moana, Dora). yer: YALNIZ kartındaki `yerler` listesindekiler (orman, deniz, ev, park, şato, dağ'dan).
  Hikâye o yerin kartta yazan hâlinde geçer (Elsa + şato = Arendelle kalesi).
- **Plan satırı:** sorun ve çözüm, her biri 3–9 kelime, küçük harf, noktalama yok (yalnız kelime sonunda virgül),
  -dı'lı geçmiş zaman. Planda HİÇBİR özel ad geçmez (ne ana karakter ne arkadaşlar): "kardeşi", "kardan adam",
  "küçük kardeşi" gibi yazılır.
- Başlık dışında "###" kullanma.

## İçerik kuralları
1. **Uzunluk 75–130 kelime**, 10–13 kısa cümle.
2. **İlk cümle karakteri adıyla ve kim olduğuyla tanıtır, yeri söyler.** Örnekler: "Arendelle kalesinde, buz
   güçleri olan Kraliçe Elsa yaşardı." / "Tepenin üstündeki evde Peppa adında pembe, küçük bir domuz yaşardı."
3. **Ana karakter hikâyenin başından sonuna vardır ve olayı o çözer**, kendi özelliğiyle (Elsa buzla, Chase
   burnu ve ağıyla, Dora Harita'ya sorarak, Örümcek Adam ağıyla).
4. **Özel ad yalnız ana karakter ve KARTINDAKİ arkadaşlar.** Bir hikâyede en fazla 2 arkadaş (kartta adı geçen)
   ve en fazla 1 isimsiz yan karakter ("küçük bir sincap"). Kartta olmayan bir isim uydurma; başka bir çizgi
   filmin karakterini asla karıştırma (Elsa ile Peppa aynı hikâyede olmaz).
5. Karakterlerin kartlardaki özelliklerine ve "dikkat" notlarına kesin sadık kal. Konuşmayan karakterler
   (Sven, Koca Ayı) konuşmaz.
6. Yapı: tanıtım → küçük bir sorun → karakterin kendi davranışıyla çözüm → sıcak, mutlu son.
7. Kısa, basit cümleler; 3–6 yaşın bildiği kelimeler. Deyim, mecaz, zor kelime yok.
8. **Tek zaman: -dı'lı geçmiş zaman.**
9. Diyaloglar kısa, çift tırnakla, konuşan cümlenin sonunda: "Merhaba!" dedi Elsa. Özel isim ekleri kesme
   işaretiyle: Elsa'nın, Anna'ya.
10. Korku en fazla hafif ve hemen geçer. Şiddet, dövüş, yaralanma, kan, ölüm, tehlikeli derin su yok.
11. Açılışları ve olayları çeşitlendir; aynı olay örgüsünü kelime değiştirip tekrar etme.

## Temalar
paylaşmak, yeni arkadaş edinmek, korkuyu yenmek, kaybolan bir şeyi bulmak, yardım etmek, özür dilemek,
sabırlı olmak, doğayı korumak, sırasını beklemek, dürüstlük, merak ve keşif, hasta bir arkadaşa bakmak,
farklılıklara saygı, birlikte çalışmak, hatadan öğrenmek, doğum günü sürprizi, kıskançlığı yenmek,
uyku vakti, yağmur ya da kar günü, teşekkür etmek

## Ek kurallar (küçük model bunlar olmadan karakterleri karıştırıyor — HEPSİ ZORUNLU)
12. **Karakter sayısı sınırlı** (kural 4): ana karakter + en fazla 2 karttaki arkadaş + en fazla 1 isimsiz yan karakter.
13. **Yan karakter hep aynı adla anılır.** İlk geçişte "küçük bir yengeç", sonra HER SEFERİNDE "yengeç" (ya da
    "küçük yengeç"). Başka bir sözcükle (o, arkadaşı, deniz canlısı...) değiştirme. İsim verme.
14. **Her konuşmada konuşan açıkça yazılır, cümlenin sonunda:** "Yardım eder misin?" diye sordu yengeç.
    "Elbette!" dedi Tosbi. Bir karakter iki konuşmayı üst üste yapmaz; konuşmalar karşılıklıdır.
15. **Figür kendine hitap etmez, kendi adını başka biri için kullanmaz.** ("Tosbi, Tosbi'nin evine" gibi YASAK.)
16. **Nesneler konuşmaz ve canlanmaz** (kabuk, taş, top konuşmaz). Sadece hayvanlar ve insanlar konuşur.
17. **Figürün tablodaki özelliği en az bir cümlede görünür ve hiç çelişilmez** (Tosbi hiç koşmaz, yavaş yürür;
    Alev hep baloncuk üfler; Cikcik uçar ve şarkı söyler).
18. **Basit sebep-sonuç:** sorun tek cümleyle ve sebebiyle söylenir ("Top ağaca takıldı çünkü rüzgâr esti."),
    çözümü figür(ler)in kendi davranışı getirir. Rastgele sihir, açıklamasız olay yok.
19. Her cümle bir öncekinin devamıdır; konu değişmez, yeni karakter sonradan eklenmez.

## Kalite kuralları (50 model hikâyesinde en sık görülen hatalar — hepsi YASAK)
20. **Yapı hep aynı sade kalıp:** tanıtım (1–2 cümle, figürün özelliği) → sorun (sebebiyle) → figür fark eder /
    birisi yardım ister → figür(ler)in kendi davranışıyla çözüm → teşekkür ya da sevinç → kısa, olaydan çıkan duygu.
    10–13 kısa cümle, 75–130 kelime.
21. **Kim ne istiyorsa onu o söyler.** Yardıma ihtiyacı olan yardım ister, yardım eden yardım etmez-istemez.
    ("Alev yanına gitti ve yardım istedi" YANLIŞ: yardım isteyen karıncadır.) Hatayı yapan özür diler, özrü
    kabul eden başkasıdır. Kırılan/kaybolan/bulunan şey hikâye boyunca aynı şeydir.
22. **"çünkü" yalnız gerçek sebep için:** "Top ağaca takıldı çünkü rüzgâr esti." Anlamsız sebep yazma
    ("bulamadı çünkü çok severdi" YASAK). Emin değilsen "çünkü" kullanma.
23. **Sondaki ders ya da duygu olaydan çıkar.** Hikâyede paylaşma olmadıysa sonda "paylaşmanın güzel olduğunu
    anladı" YAZMA. En iyisi somut bir duygu: "Alev mutlulukla gülümsedi çünkü birine yardım etmek onu iyi
    hissettirmişti."
24. **Her figür hikâyede bir kez tanıtılır** ("X adında ... yaşardı" yalnız bir kez). İki figürlüde ikincisi
    "Aynı ormanda ... adında ... yaşardı" ya da "X'in en iyi arkadaşı ... adında ..." diye bir kez tanıtılır.
25. **Tekrar yok:** aynı kelimeyi art arda yazma ("üzgün üzgün" gibi ikilemeler hariç), aynı cümleyi tekrarlama.
26. **Olayı figür çözer.** Yan karakter yardım isteyebilir, teşekkür edebilir; çözümü getiren figürdür.
27. **Özellikler karışmaz:** bir karakterin gücü başkasına geçmez (buz yalnız Elsa'da, ağ yalnız Örümcek
    Takımı'nda, küçülme tacı yalnız Gabby'de).
28. Çeşitlilik: aynı partide olayları, nesneleri ve yan karakterleri çeşitlendir; ama kalıbı (kural 20) koru.

## Hakemden sık dönen hatalar (mutlaka kaçının)

- **Zaman kayması:** Hikâye başlamadan önce olmuş şeyler -mıştı/-mişti ile yazılır: "Gece sert bir rüzgâr esmişti",
  "Çocuk mahalleye yeni taşınmıştı", "Sincap çok acıkmıştı", "Anahtar suya düşmüştü".
- **Güçlü arkadaşlar:** Kartta güçleri olan arkadaşlar (ağ atan, tırmanan, çok güçlü, uçan…) sorunu kendi güçleriyle
  kolayca çözebilecekken "yapamıyorum" diyemez. Ya bu arkadaşı hikâyeye hiç koymayın ya da sorunu onların gücünün
  işe yaramadığı bir şey yapın (ör. duygusal bir sorun, aynı anda iki yerde olmak).
- **Sonradan beliren karakter:** Sonda rol alan her karakter hikâyenin başında ya da olay anında tanıtılır.
- **Nesnenin nereden geldiği:** Yüksek rafa, dolabın üstüne çıkan şeyin oraya nasıl gittiği bir cümleyle söylenir.
- **Sebepli değişim:** Birinin fikrini değiştirmesi, özür dilemesi ya da sevinmesi olaydan doğar; gösterilir.
- **Dünyanın kuralları:** Karakterin dizisinde hayvanlar konuşmuyorsa (ör. Elsa'nın dünyası: Sven konuşmaz, orman
  hayvanları konuşmaz; yalnız Olaf konuşur) hikâyede de konuşmaz. Karakterlerin bilinen kişiliği korunur (Olaf
  neşeli ve korkusuzdur, kıskanmaz). Kraliçenin ailesi sıradan işler için sıraya girmez.
- **Güçlü kahraman, kolay çözüm:** Elsa gibi büyü gücü olan kahraman sorunu doğrudan çözebiliyorsa uzun dolambaçlı
  yola gerek yok; sorun onun gücünün tek başına yetmediği bir şey olmalı.
