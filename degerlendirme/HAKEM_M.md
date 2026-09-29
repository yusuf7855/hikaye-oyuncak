# Ürün verisi hakemi: M merceği (mantık)

Yalnız kusur ara. Zenginlik, betimleme ve yaratıcılık ödüllendirilmez; kısa ve sade olmak kusur değildir. Şapkasız yazım (rüzgar, kagıt değil kağıt) kuraldır, kusur sayma. Emin değilsen var de ve alıntıla; yalnız M6'da (işlevsiz ayrıntı, sebepsiz nesne) kusurdan emin olmadıkça 'yok' de.

Puan verilmez; her madde yok/var olarak işaretlenir. Bu hikayeler 3-6 yaş çocuklara okunacak ve küçük bir dil
modelini eğitecek; model gördüğü her mantık hatasını öğrenir. Yalnız bu merceğin maddelerine bak; dil ve dünya
kusurlarını başka hakemler arar.

## Girdi

Yalnız bu dosyayı ve sana verilen parti dosyasını oku; başka dosya, önceki puan ya da yazar bilgisi okuma.
Parti en çok 10 hikayedir. Her hikayede şunlar vardır: `id`, başlık (figür, yer, yan), plan (sorun | çözüm),
gövde ve kartın özellik satırı. Tema verilmez. Hikayeleri partideki sırayla, birbirinden bağımsız oku.

## Maddeler

Maddeler bu dosyada sabit sırayla yazılıdır; parti talimatı sana başka bir sıra verebilir, madde kimlikleri
(M1...M10) değişmez.

- **M1** Sorun ilk 3 cümlede açıkça söyleniyor.
- **M2** Hikayede yalnız bir sorun var.
- **M3** Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay
  M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
- **M4** Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
- **M5** Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
- **M6** Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran
  tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup
  kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda
  şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
- **M7** Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
- **M8** Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da
  hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da
  'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
- **M9** Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü
  görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da
  olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun
  zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek
  kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders
  varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
- **M10** Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.

Bir madde ancak hikayede o kusur yoksa 'yok' alır. Tereddüt ediyorsan 'var' de ve alıntıla (M6 hariç: M6'yı
yalnız kusurdan eminsen işaretle).

## Çıktı

Çıktı dosyasının yolu parti talimatında verilir (varsayılan: `degerlendirme/urun_v1/hakem/M/puan_<n>.json`).
Dosya, partideki sırayla her hikaye için bir kayıt taşıyan bir JSON listesidir:

```json
[{"id": "<parti dosyasındaki id>",
  "ihlaller": [{"madde": "M3", "alinti": "<metinden birebir en az 3 kelime>", "cumle_no": 2,
                "aciklama": "<tek cümle>"}],
  "maddeler": {"M1": "yok", "M2": "yok", "M3": "var", "M4": "yok", "M5": "yok",
               "M6": "yok", "M7": "yok", "M8": "yok", "M9": "yok", "M10": "yok"},
  "gecti": false}]
```

- Önce ihlalleri (alıntı ve açıklama), sonra maddeleri, en son `gecti` alanını yaz.
- `maddeler` on maddenin hepsini taşır; değer yalnız "yok" ya da "var" olur.
- Her "var" için `ihlaller` içinde o maddeyle en az bir kayıt bulunur; "yok" olan maddeye ihlal yazılmaz.
- `gecti` yalnız bütün maddeler "yok" ise true olur. Kod bu alanı maddelerden yeniden hesaplar; tutarsız JSON
  bütün partiyi geçersiz kılar.
- `aciklama` tek cümledir.

## Alıntı kuralı

- `alinti` hikayenin plan satırından ya da gövdesinden birebir kopyalanmış en az 3 kelimedir. Özetleme, düzeltme
  ya da kelime değiştirme yapma. Kod alıntıyı metinde arar; bulunamayan alıntı uydurma sayılır.
- `cumle_no` alıntının geçtiği cümlenin sırasıdır: gövde cümleleri 1'den başlar, plan satırı 0'dır.
- Yalnız eksiklik maddelerinde (M1, M5, M9 ve çözümün hiç yazılmadığı durumlar) alıntı yerine `"alinti": null`
  yazılır ve eksikliğin olması gereken yeri gösteren `cumle_no` verilir.

## Örnek eleştiriler

Örnekler kullanıcı yetkisiyle yazıldı. Hepsi kod kapılarından (K1-K9, K11) geçer; yani bu kusurları yalnız sen
yakalayabilirsin. Önce kusursuz bir taban hikaye, sonra tabanın tek yeri değiştirilmiş kusurlu biçimleri ve
beklenen ihlal kaydı verilir. Tabandaki hikayede bütün maddeler 'yok'tur; kısa, sade ve tek sahneli olmak kusur
değildir.

**Taban (bütün maddeler 'yok').** Niloya | park | Murat.
Plan: uçurtma ağaçların üstüne çıkamadı çünkü ipi kısaydı | ağabeyinden ip isteyip iki ipi bağladı

> Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu ve güldü. "Teşekkürler, Murat, uçurtmamız artık en yüksekte!" dedi Niloya.

1. 7\. cümle "Murat iki ipi sıkıca birbirine bağladı." olursa sorunu yan karakter çözer (M4 var):
  {"madde": "M4", "alinti": "Murat iki ipi sıkıca birbirine bağladı", "cumle_no": 7, "aciklama": "Sorunu Niloya değil Murat çözüyor; yan karakter yalnız yardım etmeli."}
2. 3\. cümle "Niloya yerde kırmızı bir top gördü ve düşündü." olursa top bir daha geçmez (M6 var):
  {"madde": "M6", "alinti": "yerde kırmızı bir top gördü", "cumle_no": 3, "aciklama": "Top sebepsiz beliriyor ve olayda hiçbir işe yaramıyor."}
3. Plan "uçurtmanın ipi koptu ve uçurtma kayboldu | ..." olursa plan gövdeyi söylemez (M10 var):
  {"madde": "M10", "alinti": "uçurtmanın ipi koptu ve uçurtma kayboldu", "cumle_no": 0, "aciklama": "Gövdede ip kopmuyor; ip kısa olduğu için uçurtma yükselmiyor."}

**Taban 2.** Tosbi | deniz | balık (plan: yağmur başladı ve başı ıslandı | başını kabuğuna çekip yağmurun dinmesini
bekledi):

> Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden yağmur başladı ve Tosbi'nin başı ıslandı. Tosbi başını ve ayaklarını kabuğuna çekti. Sudan küçük bir balık başını çıkardı. "Tosbi, neredesin?" diye sordu balık. "Buradayım, içerisi çok kuru," dedi Tosbi. Balık gülümsedi ve suya geri döndü. Tosbi içeride sessizce bekledi. Bir süre sonra yağmur dindi ve bulutların arasından güneş çıktı. Tosbi başını yavaşça dışarı çıkardı. Balık da yeniden sudan baktı. Tosbi renkli taşlarını toplamaya mutlu mutlu devam etti.

4. 7\. cümle '"Buradayım, burası çok ıslak," dedi Tosbi.' olursa çözüm işe yaramamışken hikaye çözülmüş gibi biter
   (M7 var):
  {"madde": "M7", "alinti": "Buradayım, burası çok ıslak", "cumle_no": 7, "aciklama": "Tosbi kuru kalmak için kabuğuna girdi ama içerisinin ıslak olduğunu söylüyor."}
5. 10\. cümle "Yağmur ancak akşam dindi ve gökyüzünde ay çıktı." olursa sahne akşama atlar (M8 var):
  {"madde": "M8", "alinti": "Yağmur ancak akşam dindi", "cumle_no": 10, "aciklama": "Hikaye sabah başlıyor ve akşama atlıyor; tek zaman kuralı çiğneniyor."}
6. 13\. cümle "Kumdaki renkli taşlar güneşte parlıyordu." olursa hikaye durgun bir resimle, kapanışsız biter (M9 var):
  {"madde": "M9", "alinti": "Kumdaki renkli taşlar güneşte parlıyordu", "cumle_no": 13, "aciklama": "Son cümle yalnız bir resim; Tosbi'nin taş toplama hedefine dönülmüyor ve hikaye sıcak bir kapanış olmadan kesiliyor."}
