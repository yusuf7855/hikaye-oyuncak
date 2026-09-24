# Oyuncak hikâyeleri v3 — yazım kılavuzu

Dinleyici 3–6 yaş. Hikâyeler NFC figürlü bir oyuncakta sesli okunacak ve KÜÇÜK bir dil modelini eğitecek.
Model bu hikâyeleri taklit eder; bu yüzden TUTARLILIK, SADELİK ve KURALLARA KESİN UYUM her şeyden önemli.

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
Her hikâye bir başlık satırıyla başlar, hikâyeler arasında bir boş satır:

    ### <tür> | <yer> | <tema>                 (tek figür)
    ### <tür1>, <tür2> | <yer> | <tema>         (iki figür)

- tür: yukarıdaki tablodaki tür adı (tavşan, kedi, ..., kız, oğlan). yer: orman, deniz, ev, park, şato, dağ.
- Başlık dışında "###" kullanma, hikâyeye başlık koyma.

## İçerik kuralları
1. **Uzunluk 90–140 kelime.** (Oyuncak en fazla ~150 kelimelik hikâye tutabiliyor.)
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
