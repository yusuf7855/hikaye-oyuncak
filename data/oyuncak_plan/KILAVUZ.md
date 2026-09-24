# Plan etiketleme kılavuzu (E3)

Her eğitim hikâyesine (`web/veri.json`, 2364 hikâye) iki satırlık bir plan yazılır. E3'te model önce planı, sonra
hikâyeyi yazmayı öğrenecek:

```
Karakter: tavşan | Yer: orman | Tema: yardım etmek
Sorun: böcek yolda kalakaldı çünkü sırtüstü dönmüştü
Çözüm: burnuyla iterek böceği yavaşça çevirdi

Ormanın yamacında Pamuk adında bembeyaz bir tavşan yaşardı. ...
```

Plan figürden bağımsızdır: ileride aynı plan başka figürlerle de kullanılacak. Bu yüzden planda ad ve figür türü
geçmez. Etiketlerken her hikâye ayrıca denetlenir: modele yanlış bir şey öğretecek hikâye `bozuk` diye işaretlenir.

Hikâye metnini değiştirme, düzeltme ya da yeniden yazma. Yalnızca etiket yaz.

## 1. Çıktı biçimi

Sana verilen partideki her hikâye için tek satırlık bir JSON kaydı yaz (JSONL), partideki sırayla. Dosya UTF-8
olmalı; Türkçe harfleri `\u` kaçışıyla değil, olduğu gibi yaz. Her kayıtta tam olarak şu 9 alan bulunur, başka alan
eklenmez:

```json
{"id": "v3/tavsan_orman#4", "sorun": "böcek yolda kalakaldı çünkü sırtüstü dönmüştü", "cozum": "burnuyla iterek böceği yavaşça çevirdi", "anahtar_sorun": "sırtüstü", "anahtar_cozum": "çevirdi", "yardimci": "küçük böcek", "yok": false, "bozuk": false, "bozuk_neden": null}
```

| alan | değer | kısaca |
|---|---|---|
| `id` | metin | `web/veri.json`'daki kimlik, aynen. Bir dosyada her kimlik bir kez geçer. |
| `sorun` | metin / null | 3–9 kelime, -dı'lı geçmiş zaman. Hikâyede sebep varsa sebebiyle birlikte yazılır (Bölüm 4). |
| `cozum` | metin / null | 3–9 kelime, -dı'lı. O sorunu çözen eylemi anlatır, mutlu sonu değil (Bölüm 4). |
| `anahtar_sorun` | metin / null | Hikâyeden tek kelime. İlk %60'ta geçer ve `sorun` cümlesinde de bulunur (Bölüm 5). |
| `anahtar_cozum` | metin / null | Hikâyeden tek kelime. `anahtar_sorun`'dan sonra ve son %60'ta geçer, `cozum` cümlesinde de bulunur (Bölüm 5). |
| `yardimci` | metin / null | Figür olmayan yan karakter, hikâyedeki adıyla: `"küçük yengeç"` (Bölüm 6). |
| `yok` | true / false | Plan yazılamıyorsa `true`. O zaman dört plan alanı `null` olur (Bölüm 3). |
| `bozuk` | true / false | Hikâye modele yanlış bir şey öğretiyorsa `true` (Bölüm 7). |
| `bozuk_neden` | metin / null | `bozuk` true ise en fazla 25 kelimelik Türkçe gerekçe, false ise `null`. |

Değeri olmayan alana boş metin (`""`) değil, `null` yaz.

## 2. Çalışma sırası

1. Hikâyeyi baştan sona oku. Temayı (`t`) yalnızca ipucu olarak kullan; sorunu temadan değil metinden çıkar.
2. Hikâye bozuk mu, karar ver (Bölüm 7). Bu karar plan alanlarını değiştirmez; tek istisna Bölüm 3b'dir.
3. Plan yazılabilir mi, karar ver (Bölüm 3).
4. Plan yazılabiliyorsa `sorun` ile `cozum`'u yaz (Bölüm 4), sonra anahtar kelimeleri seç (Bölüm 5).
5. `yardimci` alanını doldur (Bölüm 6).
6. `python data/oyuncak_plan/kontrol.py <dosya>.jsonl` komutunu çalıştır. Tek HATA kalmayana kadar düzelt,
   UYARI'lara da bak (Bölüm 9).

## 3. `yok`: plan yazılabilir mi?

**Sorun**, hikâyenin başında ortaya çıkan ve figürlerin (ya da yan karakterin) bir şey YAPMASINI gerektiren
durumdur:

- engel: "top ağaca takıldı"
- kayıp: "havucu kayboldu"
- korku: "karanlıktan korktu"
- anlaşmazlık: "salıncak için tartıştılar"
- birinin ihtiyacı: "martı üşüyordu"
- çaba isteyen bir istek: "doğum günü sürprizi hazırlamak istedi", "zirveye çıkmak istedi"
- bir hata: "vazoyu kırdı", "taşları dağıttı"

`yok: true` yalnızca şu üç durumda yazılır.

**a) Hikâyede sorun yok.** Olaylar yalnızca art arda sıralanıyor (gezdi, oynadı, yedi). Merak edilen şeye hiçbir
engelle karşılaşmadan gidilip bakılıyor. İstek anında ve çabasız gerçekleşiyor. Merak TEK BAŞINA sorun sayılmaz.
Merakın önüne bir engel çıkarsa (karanlık, korku, ulaşamamak) sorun o engeldir.

**b) Sorun var ama çözülmüyor.** Sorun unutuluyor, hikâye onu çözmeden bitiyor ya da sorun kendiliğinden
kayboluyor ("sonra her şey düzeldi"). Bu durumda `yok: true` ile birlikte `bozuk: true` da yazılır.

**c) Konum kuralı dürüstçe sağlanamıyor.** Sorun ilk kez hikâyenin son %40'ında ortaya çıkıyor ya da çözüm ilk
%40'ta bitiyor ve hikâye başka bir konuya kayıyor (Bölüm 5). Kurala uysun diye sorunu ya da çözümü taşımayan bir
kelime SEÇME, `yok: true` yaz. Hikâye başka konuya kayıyorsa `bozuk: true` da yaz.

`yok: true` olduğunda `sorun`, `cozum`, `anahtar_sorun` ve `anahtar_cozum` alanları `null` olur. `yardimci`, `bozuk`
ve `bozuk_neden` yine doldurulur.

- **Birden çok sorun varsa** sonda çözülen, hikâyeyi taşıyan sorunu seç.
- **Sorunu yan karakter ya da tesadüf çözüyorsa** planı yine yaz; `cozum`, sorunu gideren eylem ya da olay olur.
  Bu tek başına bozukluk değildir. Sebep-sonuç kopuksa hikâye bozuktur (Bölüm 7).
- **Beklenen oran:** hikâyelerin yaklaşık onda biri `yok` (planın tahmini ~203/2364). Bundan çok daha fazlasına
  `yok` yazıyorsan sorun eşiğini fazla yüksek tutuyorsun demektir.

## 4. `sorun` ve `cozum` cümleleri

**Biçim** (bu kuralların hepsini `kontrol.py` denetler):

1. 3–9 kelime. Kelimeler boşlukla ayrılır; "çünkü" de bir kelime sayılır.
2. Bütün harfler küçük. Yalnızca harf, boşluk ve virgül kullanılır. Nokta, tırnak, kesme işareti, rakam, `|` ve
   satır sonu yoktur. Sayıları yazıyla yaz ("üç"). Sonda nokta olmaz.
3. **-dı'lı geçmiş zaman.** Son kelime -dı/-di/-du/-dü/-tı/-ti/-tu/-tü ile, isteğe bağlı olarak ardından -lar/-ler
   ile biter: kayboldu, buldular, yoktu, ağırdı, dönmüştü, bulamadı. -yor, -acak/-ecek, -mış, -malı, -dır ya da
   mastarla (-mak/-mek) biten cümle HATA alır. Başka türlü biten cümle UYARI alır. Ad cümlesi de -dı alır:
   "çok yorgundu" doğru, "çok yorgun" yanlış.
4. **Özel ad yok, figür adı ya da türü yok.** Şu figür adları hiçbir çekimle geçmez: Pamuk, Tekir, Karabaş, Bal,
   Kızıl, Cikcik, Tosbi, Paytak, Dino, Alev, Elif, Can. Şu figür türleri de hiçbir çekimle geçmez (kediye, kuşun,
   kızı, köpeğe...): tavşan, kedi, köpek, ayı, tilki, kuş, kaplumbağa, penguen, dinozor, ejderha, kız, oğlan.
   "kızdı", "kızak", "canı sıkıldı", "bal kavanozu" gibi sıradan kelimeler serbesttir. Yalnız hikâyede Bal, Can,
   Alev, Pamuk ya da Kızıl figürü varsa bu kelimeyi hikâyede küçük harfle geçtiği biçimiyle yaz ("balı", "canı");
   hikâyede sıradan kelime olarak hiç geçmeyen çıplak "bal" ya da "can" ad sayılır.
   - Özne ya düşer ya da "ikisi" olur. "Pamuk havucunu kaybetti" yerine "havucunu kaybetti"; "Tekir ile Karabaş
     topu paylaşamadı" yerine "ikisi topu paylaşamadı".
   - Yan karakterin türü bir figür türüyse (kuş, kedi...) plan cümlesinde türü yazma, başka bir sözcük kullan.
     "yavru kuş yuvadan düştü" yerine "yavru yuvasından düştü"; "kedi yavrusunun oyuncağı yoktu" yerine
     "yavrunun hiç oyuncağı yoktu". Figür olmayan türler serbesttir: yengeç, sincap, baykuş, karınca, martı, böcek.
   - Çözüm figüre özgü bir özelliğe dayanıyorsa (kabuk, baloncuk, uçmak) o kelimeyi kullanabilirsin. Ad ve tür
     yine yazılmaz.

**İçerik:**

5. Hikâye sorunun sebebini söylüyorsa (v3 hikâyeleri çoğunlukla "çünkü" ile söyler) `sorun` sebebi de söyler:
   "top ağaca takıldı çünkü rüzgâr esti". Hikâyede sebep yoksa sebep uydurma. 9 kelimeye sığmıyorsa ayrıntıyı at,
   sebebi koru.
6. `cozum`, O sorunu gideren eylemdir. Mutlu son, duygu ya da ders çözüm sayılmaz.
   - Yanlış: "çok mutlu oldular", "sevindi", "paylaşmanın güzel olduğunu anladı", "teşekkür etti" (sorun teşekkür
     etmemek değilse).
   - Doğru: "dalı sallayıp topu düşürdü", "havucu çalıların arkasında buldu", "özür dileyip taşları yeniden dizdi".
7. Hikâyenin kelimelerini kullan, eş anlamlısını koyma. Hikâye "sıkışmıştı" diyorsa "takıldı" değil "sıkıştı" yaz.
   Anahtar kelime cümlede geçmek zorunda olduğu için bu kural önemlidir (Bölüm 5).
8. `sorun` ile `cozum` farklı cümlelerdir; çözüm sorunu tekrarlamaz.

## 5. `anahtar_sorun` ve `anahtar_cozum`

Plan uyumu bu iki kelimeyle ölçülür (E3'te `plan_uyum_%`, E5b'de seçici cezası). Ölçüm şöyle yapılır
(`kontrol.py` içindeki `plan_uyumu`):

- Metin Türkçe kurala göre küçük harfe çevrilir: önce I→ı ve İ→i, sonra `lower()`. Ardından `[a-zçğıöşüâîû]+`
  kelimelerine bölünür; "Pamuk'un" iki kelime olur: "pamuk", "un". N kelime sayısı, i bir kelimenin 0'dan
  başlayan sırasıdır.
- **Kök**, kelimenin ilk 5 harfidir; 5 harften kısa kelimenin kökü kelimenin kendisidir. Bir metin kelimesi kökle
  başlıyorsa anahtarla eşleşir. Örneğin "kaybolmuştu"nun kökü "kaybo"dur; "kayboldu" ve "kaybolan" onunla eşleşir.
- `anahtar_sorun` kökünün metindeki İLK geçişi ilk %60'ta olmalıdır (i < 0,6·N).
- `anahtar_cozum` kökü, `anahtar_sorun`'un ilk geçişinden SONRA ve son %60'ta (i ≥ 0,4·N) en az bir kez geçmelidir.

**Seçim kuralları:**

1. Anahtar tek kelimedir; hikâyede yazıldığı biçimde ama küçük harfle yazılır: "Sırtüstü" değil "sırtüstü".
   Metinde "sıkışmıştı" yazıyorsa "sıkıştı" değil "sıkışmıştı" yazılır. En az 3 harf olmalı; 4 harften kısa anahtar
   UYARI alır.
2. `anahtar_sorun`, `sorun` cümlesinde de geçer; `anahtar_cozum` da `cozum` cümlesinde geçer. Eşleşme aynı kökle
   yapılır: anahtar "sıkışmıştı" ise cümlede "sıkıştı" yeterlidir.
3. Anahtar, sorunu ya da çözümü TAŞIYAN kelime olmalıdır. Sorunda bu bir nesne ya da olaydır ("sırtüstü", "çöpler",
   "kayboldu", "korktu"). Çözümde bir eylemdir ("çevirdi", "topladılar", "buldu", "özür").
4. Anahtar olarak kullanılamayacak kelimeler:
   - figür adı ya da türü;
   - işlev kelimeleri ve genel kelimeler: bir, ve, çok, gün, dedi, sordu, sonra, çünkü, hemen, oldu, etti, yaptı,
     vardı, yoktu, adında, birlikte, ikisi, mutlu, sevindi, yaşardı...
   - Hikâyelerin %30'undan fazlasında geçen kökler (gülümsedi, yavaş, güzel, teşekkür...) UYARI alır. Bunların
     yerine daha özgül bir kelime seç.
5. İki anahtarın kökü farklı olmalı. Birinin kökü diğerinin öneki de olamaz.
6. `anahtar_cozum`'un kökü sorun kısmında da geçebilir. Sayılan yalnızca `anahtar_sorun`'dan sonraki ve son %60'taki
   geçiştir. Örneğin "çeviremiyordu" %33'te, "çevirdi" %64'te geçiyorsa "çevirdi" seçilebilir. Ama kurala uyan tek
   geçiş çözümle ilgisiz bir cümledeyse o kelimeyi seçme: başka bir kelime ara, bulamazsan `yok: true` yaz
   (Bölüm 3c).

## 6. `yardimci`

- Figürlerin dışında olayda rol alan karakterdir: sorunu yaşayan, yardım isteyen, yardım eden ya da konuşan biri.
  Birden fazla varsa en önemlisini yaz; hiç yoksa `null`. Başlıktaki figürler hiçbir zaman yardımcı değildir.
- Hikâyede ilk geçtiği addır. "bir" atılır ve küçük harfle, 1–4 kelime olarak yazılır: "küçük bir yengeç" →
  `"küçük yengeç"`, "yaşlı bir balıkçı" → `"yaşlı balıkçı"`, "Küçük bir kedi yavrusu" → `"küçük kedi yavrusu"`.
  Bütün kelimeler hikâyede geçmeli; son kelime hikâyede aynen bulunmalı.
- Olaya katılmayan kalabalık ("diğer hayvanlar", "gezginler") ve bir kez anılıp geçen anne ya da baba yardımcı
  sayılmaz.
- `yardimci` plan satırına girmez, yalnızca kayıt için tutulur. Bu yüzden tür kelimesi (kedi, kuş) burada
  serbesttir. Tek istisna: yardımcı, hikâyenin kendi figürüyle aynı türden olamaz.

## 7. `bozuk` ve `bozuk_neden`

Hikâye modele yanlış bir şey öğretecekse `bozuk: true` yazılır. Ölçüt `degerlendirme/RUBRIK.md`'deki kusurlardır:

1. **Mantıksız olay ya da kopuk sebep-sonuç.** Nesne anlamsızca canlanıyor ya da konuşuyor. Çözüm sebepsiz geliyor
   (sihir, birden beliren pasta). Hikâye kendisiyle çelişiyor (balık suda boğuluyor). Hikâye ortada başka bir soruna
   kayıyor (top kaybı → yuva kaybı). Sorun çözülmeden bitiyor (Bölüm 3b).
2. **Figürün özelliğiyle çelişki** (bkz. `data/oyuncak_v3/KILAVUZ.md` tablosu). Örnekler: Tosbi koşuyor ya da hızlı;
   Alev ateş püskürüyor (Alev ateş değil, renkli baloncuk üfler); Cikcik uçamıyor; Paytak kaymayı ya da yüzmeyi
   sevmiyor; Dino kaba ya da küçük; Bal balı sevmiyor. Başka bir karakterin koşması ya da "yardıma koştu" deyimi
   çelişki sayılmaz.
3. **Karakter karışıklığı.** Kimin konuştuğu anlaşılmıyor. Aynı ad iki karaktere verilmiş. Figür kendine hitap
   ediyor ya da kendi adını başkası için kullanıyor ("Tosbi, Tosbi'nin evine"). Başlıkta olmayan bir figürün adı ya
   da uydurma bir özel ad geçiyor (Lily, Zeynep).
4. **Açık dil hatası.** Uydurma ya da yanlış kelime, yanlış ek ("Tosbi da"; doğrusu "Tosbi de",
   `v2/cift_kedi_kaplumbaga#5`), özne ile yüklemin uyuşmaması, yarım kalan ya da anlamı bozuk cümle. Anlamı bozmayan
   tek bir üslup pürüzü bozukluk sayılmaz.
5. **3–6 yaşa uygun olmayan içerik.** Boğulma ya da boğulmak üzere olma (örnek: `v2/oglan_deniz#9`). Derin suya ya
   da büyük dalgaya girmek; özellikle Elif ve Can için, bir de bu davranış cesaret diye öğütleniyorsa. Yaralanma,
   kan, kırık kanat. Gerçek tehlike: yüksekten düşmek, ateşle oynamak, yabancıyla gitmek. Geçmeyen korku, şiddet.
   Balığın ya da penguenin olağan yüzmesi, sığ suda oynamak ve hafif, hemen geçen korku bozukluk değildir.

**Bozuk sayılmayanlar:**

- Sıradanlık, tahmin edilebilir olay örgüsü, kalıp açılış ya da kalıp son ("Sonra her biri kendi yoluna...").
- Sorunsuz hikâye: bu Bölüm 3a'dır, yalnızca `yok: true` yazılır.
- Ders cümlesiyle bitmek, tek bir kısa ilgisiz cümle, küçük bir tekrar.
- v3 biçim kurallarının ihlali ("aynı konuşmacı üst üste" gibi); kimin konuştuğu yine de açıksa.

**Karar verirken şunu sor:** Bir ebeveyn bu hikâyeyi dinleyince "bu saçma" ya da "bunu çocuğuma okutmam" der mi?
Diyorsa hikâye bozuktur.

**`bozuk_neden`:** kısa bir Türkçe gerekçe; en fazla 25 kelime, `|` ve satır sonu yok. Kusurun türünü ve yerini
söyle. Örnek: "Tosbi yarışta koşarak kazanıyor (özellik çelişkisi)". `bozuk: false` ise `null` yaz.

Bozuk hikâyenin diğer alanları da normal doldurulur; plan yazılabiliyorsa yazılır.

## 8. Örnekler (`web/veri.json`'dan)

### Örnek 1: tek figür, yan karakter, sebepli sorun (`v3/tavsan_orman#4`)

> Ormanın yamacında Pamuk adında bembeyaz bir tavşan yaşardı. Pamuk zıplamayı ve havuç yemeyi çok severdi, her gün
> ormanda dolaşırdı. Bir gün küçük bir böcek yolun ortasında kalakalmıştı çünkü sırtüstü dönmüştü. Böcek kendini
> çeviremiyordu ve endişeliydi. Pamuk biraz utangaç olsa da hemen yanına koştu. "Sana yardım edebilir miyim?" diye
> sordu Pamuk. "Evet, lütfen." dedi böcek. Pamuk burnuyla ve ayaklarıyla iterek böceği yavaşça çevirdi. Böcek
> rahatlayıp ayağa kalktı. "Çok teşekkür ederim." dedi böcek. Pamuk mutlulukla zıpladı çünkü birine yardım etmek
> onu iyi hissettirmişti. İkisi birlikte gölgede biraz dinlendiler. Sonra her biri kendi yoluna güle güle giderek
> devam etti.

```json
{"id": "v3/tavsan_orman#4", "sorun": "böcek yolda kalakaldı çünkü sırtüstü dönmüştü", "cozum": "burnuyla iterek böceği yavaşça çevirdi", "anahtar_sorun": "sırtüstü", "anahtar_cozum": "çevirdi", "yardimci": "küçük böcek", "yok": false, "bozuk": false, "bozuk_neden": null}
```

- Sorun, hikâyedeki sebebiyle birlikte yazıldı ("çünkü sırtüstü dönmüştü"). "böcek" figür türü olmadığı için
  serbest.
- Çözüm Pamuk'un eylemidir ve özne düşmüştür. "mutlulukla zıpladı" çözüm değil, mutlu sondur.
- `anahtar_sorun` "sırtüstü" %29'da geçiyor. `anahtar_cozum` "çevirdi" %64'te. "çeviremiyordu" (%33) aynı kökten
  ama son %60'ın dışında kaldığı için sayılmaz; sayılan "çevirdi"dir.

### Örnek 2: yan karakterin türü bir figür türü (`v3/oglan_ev#0`)

> Evde Can adında enerjik ve yardımsever bir oğlan yaşardı. Bir gün odasında en sevdiği arabalarla yeni bir oyun
> kurdu ve keyifle oynamaya başladı. Küçük bir kedi yavrusu kapıdan içeri girdi ve arabalara meraklı gözlerle baktı
> çünkü hiç oyuncağı yoktu. Can kedi yavrusunun halini görünce durdu. "Sen de oynamak ister misin?" diye sordu Can.
> Kedi yavrusu miyavlayarak yaklaştı. Can arabalardan birkaçını kedi yavrusunun önüne koydu. Kedi yavrusu arabayı
> patisiyle ittirip sevinçle oynadı. Can da kalan arabalarla birlikte oyun kurmaya devam etti. İkisi odada uzun süre
> birlikte oynadı. Can o gün paylaşmanın oyunu daha eğlenceli yaptığını anladı.

```json
{"id": "v3/oglan_ev#0", "sorun": "yavru arabalara baktı çünkü hiç oyuncağı yoktu", "cozum": "arabalardan birkaçını yavrunun önüne koydu", "anahtar_sorun": "oyuncağı", "anahtar_cozum": "koydu", "yardimci": "küçük kedi yavrusu", "yok": false, "bozuk": false, "bozuk_neden": null}
```

- "kedi" bir figür türü olduğu için plan cümlesinde "kedi yavrusu" yerine "yavru" yazıldı. `yardimci` plana
  girmediği için orada "kedi" serbest; hikâyenin figürü de oğlan olduğundan kural çiğnenmiyor.
- "paylaşmanın oyunu daha eğlenceli yaptığını anladı" derstir, çözüm değil. "Can arabalarını paylaştı" ise ad
  içerdiği için yanlış.
- `anahtar_sorun` "oyuncağı" %39'da, `anahtar_cozum` "koydu" %66'da geçiyor.

### Örnek 3: iki figür, özne "ikisi" (`v3/cift_tilki_dinozor#0`)

> Ormanın kenarında Kızıl adında turuncu bir tilki yaşardı. Ağaçların arasında Dino adında uzun boyunlu ama çok
> nazik bir dinozor yaşardı. Bir gün ormanda dağılmış çöpler gördüler çünkü gezginler onları unutmuştu. Yapraklar
> çöplerin altında ezilmişti. Kızıl üzüldü ve hemen bir şeyler yapmak istedi. Dino nazikçe yardım etmeye karar
> verdi. "Hadi birlikte toplayalım." dedi Dino. "Olur, hemen başlayalım." dedi Kızıl. İkisi çöpleri küçük bir
> çukura topladılar. Kısa sürede orman yeniden tertemiz oldu. Yapraklar güneşe doğru yeniden uzandı. Kızıl sevinçle
> güldü ve Dino nazikçe gülümsedi. İkisi temiz ormanın tadını çıkardılar. Ormanı korumanın onları çok mutlu ettiğini
> anladılar.

```json
{"id": "v3/cift_tilki_dinozor#0", "sorun": "ormanda çöpler dağılmıştı çünkü gezginler unutmuştu", "cozum": "ikisi çöpleri küçük bir çukura topladı", "anahtar_sorun": "çöpler", "anahtar_cozum": "topladılar", "yardimci": null, "yok": false, "bozuk": false, "bozuk_neden": null}
```

- İki figür birlikte çözdüğü için özne "ikisi" oldu. "Kızıl ile Dino" yazılmaz.
- `anahtar_cozum` metindeki biçimiyle "topladılar" yazıldı (%67). Cümledeki "topladı" aynı kökten ("topla")
  olduğu için yeterli.
- "gezginler" olayda rol almadığı için `yardimci` alanı `null`.

### Örnek 4: sorun yok (`v2/ayi_orman#7`)

> Bir ormanın kenarında Bal adında kocaman ve sevecen bir ayı vardı. Bal, ormanın hiç gitmediği bir bölümünde parlak
> bir ışık gördü ve çok meraklandı. Yavaş yavaş o yöne doğru yürüdü, kalın çalıların arasından geçti. Işığın
> kaynağı, güneşin altında parıldayan küçük bir şelaleydi. Bal hiç böyle bir yer görmemişti ve hayretle etrafına
> bakındı. Şelalenin yanında minik renkli çiçekler açmıştı. Bal dikkatle yaklaşıp suyun serinliğini hissetti ve
> keyifle güldü. O gün fark etti ki ormanda keşfedilecek çok yeni yer vardı. Yuvasına dönerken kendi kendine, "Yarın
> başka bir yer keşfedeceğim" dedi. Bal, merakının onu güzel yerlere götürdüğünü öğrenmişti. Artık her sabah
> şelalenin yanına gidip suyun sesini dinlemekten büyük keyif alıyordu.

```json
{"id": "v2/ayi_orman#7", "sorun": null, "cozum": null, "anahtar_sorun": null, "anahtar_cozum": null, "yardimci": null, "yok": true, "bozuk": false, "bozuk_neden": null}
```

- Merak var ama önünde bir engel yok: Bal ışığa yürüdü, şelaleyi buldu ve keyif aldı (Bölüm 3a).
- Sıradan ama doğru bir hikâye olduğu için bozuk değil.

### Örnek 5: çözüm erken bitiyor, hikâye kayıyor (`v2/kiz_deniz#9`)

> Denizin kıyısında Elif adında meraklı bir kız yaşardı. Elif bir gün dalgaların arasında boğulmak üzere olan küçük
> bir balığı gördü, balık sığ bir kum çukuruna sıkışmıştı. Elif hemen ellerini suya soktu ve balığı nazikçe
> kaldırıp derin suya bıraktı. Balık bir süre etrafında dönüp Elif'e teşekkür eder gibi göründü. Ertesi gün Elif
> kumsalda yürürken ayağına bir şey takıldığını fark etti, eğilip baktığında güzel, parlak bir taş buldu. O akşam
> annesine bu taşı gösterirken denizin ona bir hediye bıraktığını düşündü. Elif küçük bir iyiliğin bile büyük bir
> mutluluk getirebileceğini anladı. O günden sonra denize her gittiğinde etrafına dikkatlice baktı ve karşılaştığı
> canlılara nazikçe davrandı.

```json
{"id": "v2/kiz_deniz#9", "sorun": null, "cozum": null, "anahtar_sorun": null, "anahtar_cozum": null, "yardimci": "küçük balık", "yok": true, "bozuk": true, "bozuk_neden": "balık suda boğulmak üzere (mantıksız); sorun ilk üç cümlede çözülüyor, sonra ilgisiz taş bulmaya kayıyor"}
```

- Sorunun kelimesi "sıkışmıştı" %24'te geçiyor ama çözüm ("kaldırıp", "bıraktı") %33–36'da, yani son %60'ın
  dışında. Kurala uyan tek geçiş %75'teki "hediye bıraktığını", ki bu çözümle ilgisiz. Seçilmez: `yok: true`
  (Bölüm 3c).
- Balığın suda boğulması mantıksız ve hikâye ortada başka bir olaya kayıyor: `bozuk: true`.

### Örnek 6: plan yazılabiliyor ama hikâye güvensiz (`v2/cift_ejderha_kiz#1`)

> Denizin kıyısında Alev adında küçük ve sevimli bir ejderha yaşardı. Bir sabah kumsalda oynayan Elif adında cesur
> bir kızla tanıştı. Elif dalgalara girmek istiyordu ama derin sular onu korkutuyordu. Alev yanına gitti ve
> kanatlarını açtı. "Ben de yanındayım" dedi. Birlikte sığ suya adım attılar. Alev renkli baloncuklar üfledi,
> baloncuklar suyun üstünde parladı. Elif gülerek baloncukları kovaladı ve korkusunu unuttu. Yavaş yavaş daha
> derine girdiler, küçük balıkları izlediler. Elif artık dalgalardan korkmuyordu. Akşam olduğunda ikisi kumdan bir
> kale yaptılar. Elif, Alev'e sarıldı ve teşekkür etti. Güneş denize batarken beraber kıyıda oturup gökyüzünü
> seyrettiler.

```json
{"id": "v2/cift_ejderha_kiz#1", "sorun": "dalgalara girmek istedi ama derin sulardan korktu", "cozum": "renkli baloncukları kovalayıp korkusunu unuttu", "anahtar_sorun": "derin", "anahtar_cozum": "unuttu", "yardimci": null, "yok": false, "bozuk": true, "bozuk_neden": "çocuk figür korkuyu yenmek için giderek daha derin suya giriyor; 3-6 yaş için güvensiz örnek"}
```

- Plan normal yazıldı. `anahtar_sorun` "derin" %27'de; "derine" %67'de de geçiyor ama yalnızca ilk geçiş sayılır.
  `anahtar_cozum` "unuttu" %62'de.
- Bozukluk plandan bağımsız bir karardır: küçük bir kız, korkuyu yenmek için giderek daha derin suya giriyor
  (Bölüm 7.5).

## 9. Denetim: `kontrol.py`

```
python data/oyuncak_plan/kontrol.py parti_07.jsonl           # satır satır HATA/UYARI + özet
python data/oyuncak_plan/kontrol.py plan.jsonl --ozet         # yalnızca özet, dağılımlar, bozuk listesi
```

- **HATA** varsa satır reddedilir; düzeltip yeniden çalıştır. HATA kalırsa çıkış kodu 1 olur.
- **UYARI** kesin olmayan bir şüphedir: son kelime -dı ile bitmiyor ama bir ad cümlesi olabilir, anahtar fazla
  genel, figür adı olabilecek bir kelime var... Satıra yeniden bak; gerçekten doğruysa olduğu gibi bırak.
- Denetlenenler: alanların varlığı ve türleri; kimliğin `web/veri.json`'da olması ve dosyada tek olması; `yok` ve
  `bozuk` tutarlılığı; kelime sayısı; karakterler; figür adları ve türleri; zaman eki; anahtarın metinde aynen
  geçmesi, cümlede kökle geçmesi ve konumu; `yardimci`'nin metinde geçmesi. Sorunun gerçekten sorun, çözümün
  gerçekten o sorunun çözümü olup olmadığını ve bozukluk kararını yalnızca sen denetleyebilirsin.
