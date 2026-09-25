# Oyuncak hikâyeleri v4 — yazım kılavuzu

Dinleyici 3–6 yaş. Hikâyeler NFC figürlü bir oyuncakta sesli okunacak ve KÜÇÜK bir dil modelini eğitecek.
Model bu hikâyeleri taklit eder; bu yüzden TUTARLILIK, SADELİK ve KURALLARA KESİN UYUM her şeyden önemli.
v4'ün amacı: modelin her seferinde aşağıdaki HEDEF ÖRNEK kadar temiz bir hikâye yazmayı öğrenmesi.

## HEDEF ÖRNEK (kullanıcı 10/10 verdi; her hikâye bu sadelikte ve bu netlikte olmalı)

    ### ejderha | orman | yardım etmek
    @plan: karınca ağır yaprağı yuvasına taşıyamadı | birlikte yaprağı yuvaya taşıdılar

    Ormanın kenarında Alev adında küçük ve sevimli bir ejderha yaşardı. Ateş yerine ağzından rengarenk
    baloncuklar üflerdi. Bir gün küçük bir karınca ağır bir yaprağı taşımaya çalışıyordu ama başaramıyordu.
    Alev karıncayı görünce yanına gitti. "Yardım eder misin?" diye sordu karınca. "Elbette, yardım ederim."
    dedi Alev. İkisi birlikte yaprağı karıncanın yuvasına taşıdılar. Karınca çok mutlu oldu. "Yardımın için
    teşekkür ederim." dedi karınca. Alev mutlulukla gülümsedi çünkü birine yardım etmek onu iyi hissettirmişti.
    O günden sonra her gün birlikte oynadılar.

## Figür karakterleri (isimler SABİT, asla değiştirme)
| tür | isim | özellik |
|---|---|---|
| tavşan | Pamuk | bembeyaz, uzun kulaklı, zıplamayı ve havucu sever, biraz utangaç |
| kedi | Tekir | çizgili, çok meraklı, her yere burnunu sokar, mırlayarak sevinir |
| köpek | Karabaş | sadık, neşeli, koşmayı ve top oyununu sever, kuyruğunu sallar |
| ayı | Bal | kocaman ve yumuşacık, balı çok sever, biraz uykucu, çok sevecen |
| tilki | Kızıl | turuncu, akıllı, bilmeceleri ve plan yapmayı sever, iyi kalpli |
| kuş | Cikcik | minik, şarkı söylemeyi sever, gökyüzünden her şeyi görür |
| kaplumbağa | Tosbi | yavaş ama sabırlı ve bilge, kabuğuna saklanabilir |
| penguen | Paytak | paytak paytak yürür, kaymayı ve yüzmeyi sever, soğuğu sever |
| dinozor | Dino | uzun boyunlu, çok büyük ama çok nazik, yaprak yer |
| ejderha | Alev | küçük ve sevimli, ateş yerine renkli baloncuklar üfler |
| kız | Elif | meraklı ve cesur küçük bir kız, soru sormayı sever |
| oğlan | Can | enerjik ve yardımsever küçük bir oğlan, oyun kurmayı sever |

## Biçim (kesin)
Her hikâye bir başlık satırı, hemen altında bir PLAN satırı, bir boş satır ve hikâye metniyle yazılır;
hikâyeler arasında bir boş satır:

    ### <tür> | <yer> | <tema>                 (tek figür)
    ### <tür1>, <tür2> | <yer> | <tema>         (iki figür)
    @plan: <sorun> | <çözüm>

- **Plan satırı:** sorun ve çözüm, her biri 3–9 kelime, küçük harf, noktalama yok (yalnız kelime sonunda virgül
  olabilir), -dı'lı geçmiş zaman. Planda figür adı ve figür türü GEÇMEZ (yan karakter geçebilir: "karınca").
  Sorun hikâyedeki sorunun ta kendisi, çözüm o sorunu çözen eylem (mutlu son değil).

- tür: yukarıdaki tablodaki tür adı (tavşan, kedi, ..., kız, oğlan). yer: orman, deniz, ev, park, şato, dağ.
- Başlık dışında "###" kullanma, hikâyeye başlık koyma.

## İçerik kuralları
1. **Uzunluk 75–130 kelime.** (Oyuncak en fazla ~150 kelimelik hikâye tutabiliyor.)
2. **İlk cümle ana karakter(ler)i ismi VE türüyle tanıtır, yeri de söyler.** Örnek:
   "Ormanın kenarında Pamuk adında bembeyaz bir tavşan yaşardı."
   İki figürde ikisi de ilk iki cümle içinde isim+türle tanıtılır.
3. **Ana karakter(ler) hikâyenin başından sonuna kadar vardır ve olayı onlar çözer.** İki figürlü hikâyede
   ikisi de aktiftir, birlikte bir şey yaparlar.
4. **Sadece figür karakterlerinin ismi olur.** Başka herkes isimsizdir: "annesi", "babası", "bir sincap",
   "yaşlı bir baykuş", "küçük bir balık". Başka isim uydurma. Başlıkta olmayan bir figürün ismini kullanma.
5. Karakterlerin tablodaki özelliklerine sadık kal (Tosbi yavaştır, Alev ateş değil baloncuk üfler...).
6. Yapı: tanıtım → küçük bir sorun → çocuğun anlayacağı bir çözüm → sıcak, mutlu son.
7. Kısa, basit cümleler; 3–6 yaşın bildiği kelimeler. Deyim, mecaz, zor kelime yok.
8. **Tek zaman kullan: -dı'lı geçmiş zaman** (gitti, dedi, gördü). "Bir varmış bir yokmuş" açılışı serbest,
   sonrası yine -dı'lı.
9. Diyaloglar kısa, çift tırnakla: "Merhaba!" dedi Pamuk. Özel isim ekleri kesme işaretiyle: Pamuk'un, Bal'a.
10. Korku en fazla hafif ve hemen geçer. Şiddet, yaralanma, ölüm, marka, gerçek kişi yok.
11. Açılışları çeşitlendir; aynı olay örgüsünü kelime değiştirip tekrar etme.

## Temalar
paylaşmak, yeni arkadaş edinmek, korkuyu yenmek, kaybolan bir şeyi bulmak, yardım etmek, özür dilemek,
sabırlı olmak, doğayı korumak, sırasını beklemek, dürüstlük, merak ve keşif, hasta bir arkadaşa bakmak,
farklılıklara saygı, birlikte çalışmak, hatadan öğrenmek, doğum günü sürprizi, kıskançlığı yenmek,
uyku vakti, yağmur ya da kar günü, teşekkür etmek

## v3 EK KURALLAR (küçük model bunlar olmadan karakterleri karıştırıyor — HEPSİ ZORUNLU)
12. **Karakter sayısı sınırlı.** Tek figürlü hikâyede figür + EN FAZLA BİR yan karakter. İki figürlü hikâyede yan
    karakter YOK (sadece iki figür; gerekirse "annesi" gibi bir anne/baba bir kez geçebilir, konuşmaz).
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

## v4 EK KURALLAR (50 model hikâyesinde en sık görülen hatalar — hepsi YASAK)
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
27. **Özellikler karışmaz:** gaga ve kanat yalnız kuşlarda; kuyruk sallamak köpekte; baloncuk yalnız Alev'de;
    kabuk yalnız kaplumbağada ve kabuk hiç çıkarılmaz.
28. Çeşitlilik: aynı partide olayları, nesneleri ve yan karakterleri çeşitlendir; ama kalıbı (kural 20) koru.
