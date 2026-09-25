# 50 hikâye analizi (E3 / v4 modeli) ve seçici kuralları

Kaynak: v4'ün (c2ft_plan, planlı) seçtiği 50 hikâye. Bunların 36'sı sabit test setinin tamamı (`degerlendirme/c2ft_plan`),
14'ü doğrulama vakalarından rastgele alındı (`degerlendirme/c2ft_plan_dog`, seed 5). Hepsi tek tek okundu. Aşağıdaki
sayılar el ile sayıldı; bir hikâyede birden çok sorun olabilir.

## Sorunlar

| # | Sorun | Hikâye | Örnek | Seçici yakalayabilir mi? |
|---|---|---|---|---|
| 1 | **Sondaki ders olaydan kopuk** | 11/50 | Top bulunuyor, sonra "paylaşmanın ne kadar güzel olduğunu anladı" (T30, D29) | evet: `ders olaydan kopuk` |
| 2 | **Aynı karakter iki kez / kendi kendine** | 9/50 | "Kızıl adında … tilki yaşardı. … Kızıl adında … tilki koşardı" (T9); "Paytak geldiğinde Paytak'ı görünce" (T34); "Bal, Bal'ın elini tuttu" (T35); tavşan: "Ben de Tekir" (T3) | evet: `iki kez tanıtılıyor`, `kendi kendine`, `başkası kendini X diye tanıtıyor` |
| 3 | **Plan ile hikâye uyuşmuyor** | ~10/50 | Plan "kıskandı", hikâye kaybolan top (T4) | kelime uyumu denendi, **işe yaramadı** (aşağıda) |
| 4 | **Bozuk neden-sonuç ("çünkü")** | 5/50 | "bulamadı çünkü çok severdi" (T12), "kırdı çünkü doğruyu söyledi" (D113) | hayır: eğitim tarafı |
| 5 | **Özellik karışması** | 5/50 | Köpek "gagasıyla" (T25), Cikcik baloncuk üflüyor (T26), Tosbi kabuğunu çıkarıyor (D102) | kısmen: `özellik karışması` (gaga, baloncuk, kuyruk, burnunu sokmak, kabuk) |
| 6 | **Kekeme tekrar** | 5/50 | "üzgün üzgün üzgün üzgün" (T29), "kucağına aldı ve kucağına aldı" (T35), "o kadar büyüktü ki o kadar büyüktü ki" (T6) | evet: `kekeme tekrar` (eğitimdeki ikilemeler serbest: paytak paytak, yavaş yavaş) |
| 7 | **Yanlış konuşmacı / itiraf karışması** | 4/50 | Paytak'ın yaptığını Cikcik itiraf ediyor (T29) | hayır: eğitim tarafı |
| 8 | **Uydurma kelime / isim** | 4/50 | "buldularler", "Minnoş" (D10) | kelime: vardı; isim: yeni `uydurma karakter adı` |
| 9 | **Çocuğa uygun olmayan ayrıntı** | 3/50 | "dizleri kanadı", "yara bandı" (D15) | evet: güvenlik listesine kan, yara, dizi kanamak, canı acımak eklendi |
| 10 | **Plan biçimi bozuk** | 2/50 | iki "Çözüm:" satırı (D100, D113) | evet: `plan bozuk` |
| 11 | Sorunu figür değil yan karakter çözüyor | 2/50 | T5, T6 | hayır |
| 12 | Yer kayması | 2/50 | dağda "şatonun" (D119) | vardı: `yer kayması` |

Özet: 50 hikâyenin yaklaşık yarısında seçicinin yakalayabileceği, **eğitim hikâyelerinde neredeyse hiç görülmeyen**
hatalar var. Kalan hatalar (neden-sonuç, konuşmacı, kim çözüyor) metin kuralıyla güvenle yakalanamıyor; bunlar
modelin kapasitesiyle ilgili.

## Yeni kurallar (`degerlendirme/sec.py: olay_cezalari`, sayfada `olayCezalari`)

Her kural önce eğitim verisinin 2364 hikâyesinde denendi. Eğitim hikâyelerinde de sık tetiklenen kural, iyi
hikâyeyi de cezalandıracağı için alınmadı.

| Kural | Ceza | Eğitimde tetiklenme | 50 model hikâyesinde |
|---|---|---|---|
| X iki kez tanıtılıyor | 3 | 0 | 5 |
| X kendi kendine (aynı cümlede X … X'e/X'ı, arada başka özne yok) | 2 | 1 | 3 |
| başkası kendini X diye tanıtıyor | 2 | 0 | 1 |
| uydurma karakter adı (tanınmayan özel ad + kesme işareti) | 2 | 0 | 1 |
| özellik karışması (gaga, baloncuk, kuyruk sallamak, burnunu sokmak, kabuğunu çıkarmak) | 2 | 0 | 2 |
| kekeme tekrar (üçlü tekrar ya da eğitimde görülmemiş ikileme / öbek tekrarı) | 1–2 | 0 | 6 |
| ders olaydan kopuk (sondaki değer, ör. paylaşmak, için gövdede hiçbir olay kanıtı yok) | 1.5 | 42 (%1.8) | 8 |
| plan bozuk | 2 | — | 2 |
| güvenlik: kan, yara, dizi kanamak, canı acımak (her zaman açık, −4) | 4 | +0 | 1 yeni |

Toplam: 50 hikâyenin 20'si (%40) en az bir yeni kurala takılıyor. Eğitim hikâyelerinde bu oran yaklaşık %2.

Denenip **alınmayanlar**:
- Hayvan listesini genişletmek (keçi, serçe, güvercin…; "sonradan beliren karakter" için): eğitimde de aynı oranda
  (%2.2) tetikleniyor, yani ayırt edici değil.
- Ders cümlesindeki değer kelimesinin gövdede aynen geçmesini istemek: eğitimde %8 tetikleniyor, çünkü iyi hikâyeler
  de dersi yalnız sonda adıyla söylüyor. Bunun yerine olay kanıtı arandı (paylaşmak ← verdi, böldü, ikram…).
- Plan-hikâye kelime uyumu (sorunun kelimeleri ilk %60'ta, çözümünkiler son %60'ta): genel hakemde bu kuralın
  değiştirdiği seçimler kötüleşti (sorun: %23, çözüm: %47 kazanma). Çıkarıldı; yalnız biçim kontrolü kaldı.

## Ölçüm (E5b: yalnız seçimi değişen vakalar, kör ikili)

Aday havuzları yeniden üretilmedi. v4'ün mevcut 8'li havuzlarından (test 36 vaka, doğrulama 129 vaka) eski ve yeni
seçici ayrı ayrı seçti. Yalnız seçimi değişen vakalar hakeme gitti.

| Tur | Seçici | Değişen vaka | Olay örgüsü hakemi (IKILI.md) | Genel kalite hakemi (IKILI_GENEL.md) |
|---|---|---|---|---|
| 1 | bütün kurallar (plan uyumu dahil) | 12 test + 51 doğrulama = 63 | 34.25/63 (%54, 2 hakem, Eşit) | 39/63 (%62, p=0.038) |
| 2 | **son hâli** (plan uyumu çıkarıldı) | 11 test + 38 doğrulama = 49 | tur 1 kararlarından 43 vakada: 25.75/43 (%60) | **yeni hakemlerle 32/49 (%65, p=0.022)**, test setinde 9/11 |

- Olay örgüsü hakemine figür isimlerinin doğruluğuna ve dil pürüzlerine bakmaması söyleniyor. Yeni kuralların çoğu
  tam da bunları (iki kez tanıtma, kendi kendine, kekemelik) yakaladığı için ikinci bir hakem yazıldı:
  `degerlendirme/IKILI_GENEL.md` ("çocuğuna hangisini okurdun": karakter tutarlılığı, mantık, dil, uygunluk).
- Genel hakemde kural başına yeni seçimin kazanma oranı (tur 1): iki kez tanıtma %89, ders olaydan kopuk %82,
  kendi kendine %80, kekeme tekrar %67, plan bozuk %62. Olay örgüsü hakeminde de hiçbir kural belirgin kaybettirmedi.
- Uyarı: plan uyumu kurallarını çıkarma kararı tur 1'in verisiyle verildi. Tur 2'de hakemler yeni, ama vakalar aynı
  havuzlardan. Karar: **benimsendi** (Hikâye Atölyesi'nde açık). Model aynı kaldı (v4).
- Aday başına ek maliyet: birkaç düzenli ifade. Kartta da ucuz; C'ye taşınması firmware işiyle birlikte yapılacak.

## Eğitim tarafı için çıkarım

Seçici yalnız modelin ürettiği 8 aday arasından seçebilir. Neden-sonuç, konuşmacı ve "kim çözüyor" hataları
adayların çoğunda birlikte bulunuyor. Bunlar için sıradaki adımlar:
- **E4:** ince ayar karışımında oyuncak hikâyelerinin payını artırmak.
- Daha uzun ince ayar.
- Modelin kapasitesi kartın bütçesiyle sınırlı (docs/ESP32_BUTCE.md). Bu yüzden asıl kazanç veri ve seçiciden bekleniyor.

## Kullanıcının hedef örneği (10/10)

Kullanıcı, v4'ün test setindeki şu hikâyesine 10/10 verdi (hakem ortalaması 9). Döngünün hedefi, hikâyelerin
çoğunun bu seviyede olması: tek sorun, yardım, çözüm, teşekkür, olaydan çıkan duygu; 10-11 kısa cümle.

> Ormanın kenarında Alev adında küçük ve sevimli bir ejderha yaşardı. Ateş yerine ağzından rengarenk baloncuklar
> üflerdi ve çok güzel şeyler yapardı. Bir gün küçük bir karınca ağır bir yaprağı taşımaya çalışıyordu ama
> başaramıyordu. Alev yanına gitti ve yardım istedi. "Yardım eder misin?" diye sordu karınca. "Elbette, yardım
> ederim." dedi Alev. İkisi birlikte yaprağı karıncanın yuvasına taşıdılar. Karınca çok mutlu oldu. "Yardımın için
> teşekkür ederim." dedi karınca. Alev mutlulukla gülümsedi çünkü birine yardım etmek onu iyi hissettirmişti. O
> günden sonra her gün birlikte oynadılar.

(Tek kusur: "Alev yanına gitti ve yardım istedi"; yardımı isteyen karınca olmalı.)
