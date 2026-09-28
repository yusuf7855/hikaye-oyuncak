# Ürün verisi hakemi: K merceği (dünya-kart ve çocuk güvenliği)

Yalnız kusur ara. Zenginlik, betimleme ve yaratıcılık ödüllendirilmez; kısa ve sade olmak kusur değildir. Şapkasız yazım (rüzgar, kagıt değil kağıt) kuraldır, kusur sayma. Emin değilsen var de ve alıntıla.

Puan verilmez; her madde yok/var olarak işaretlenir. Bu hikayeler 3-6 yaş çocuklara okunacak ve küçük bir dil
modelini eğitecek. Bu mercek iki şeye bakar: hikaye figürün kaynaklı kartına sadık mı, ve bir çocuğa okunmaya
güvenli mi. Yalnız bu merceğin maddelerine bak; mantık ve dil kusurlarını başka hakemler arar.

## Girdi

Yalnız bu dosyayı ve sana verilen parti dosyasını oku; başka dosya, önceki puan ya da yazar bilgisi okuma.
Parti tek figürlüdür ve en çok 10 hikayedir. Parti dosyasında şunlar vardır: figürün kaynaklı tam kartı
('güvenli özellik kullanımı' dahil), hedef yaş 3-6, ve her hikaye için `id`, başlık (figür, yer, yan), plan
(sorun | çözüm), gövde, tohumdaki özellik, kodun çoğul canlı notları ve belirsiz kelime notları. Hikayeleri partideki sırayla, birbirinden bağımsız oku.

Kartı şöyle kullan:
- Kart kapalı dünyadır: kartta olmayan aile üyesi, ev, yetenek, eşya, başka dizinin karakteri, nesnesi ya da
  yeri hikayede olamaz. Kartın 'yasaklar' bölümündeki adlar ve öğeler hiç geçemez.
- Yan karakterler kartın 'yanlar' bölümündeki kısa ad ya da yüzey biçimleriyle, karttaki ilişki ve türle geçer.
  'konusur': false olan karakter konuşmaz (replik, 'dedi', 'sordu', 'söyledi' yok; ses çıkarması ve hareketi
  serbesttir).
- Yer, kartın o yer için verdiği 'tarif'e uyar. Başlıktaki yan bir 'kosullu_tarif' taşıyorsa o tarif de geçerlidir.
- Figürün gücü ya da özelliği yalnız kartın 'güvenli özellik kullanımı' satırındaki gibi kullanılır.
- Kartın 'dünya kuralları' çiğnenemez.
- Kodun çoğul canlı notu karar değildir; notlanan çoğul canlılar konuşuyor ya da olaya katılıyorsa K4 'var'dır.
- Belirsiz kelimeler (bebek, robot, ayıcık, dev, biri, yaşlı, sürü...) kullanıcı kararıyla KARAKTER olarak yasaktır:
  yalnız cansız ya da oyuncak anlamında geçebilir ('oyuncak robot', 'bir sürü yaprak', 'bilge bir kaplumbağa').
  Kodun belirsiz kelime notu karar değildir; notlanan kelime canlı, konuşan ya da rol olarak geçiyorsa ('Robot
  "Merhaba," dedi.', 'oyuncak ayı yürüdü') K6 'var'dır.

## Maddeler

Maddeler bu dosyada sabit sırayla yazılıdır; parti talimatı sana başka bir sıra verebilir, madde kimlikleri
(K1...K8, C1...C6) değişmez.

Dünya ve kart:
- **K1** Figür karttaki kimliğine (tür, görünüş, huy) uygun.
- **K2** Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
- **K3** Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
- **K4** En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
- **K5** Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
- **K6** Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya
  yeri yok.
- **K7** Yer, kartın o yer için verdiği tarife uygun.
- **K8** Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.

Çocuk güvenliği:
- **C1** Korkutucu öğe yok.
- **C2** Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
- **C3** Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç);
  figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
- **C4** Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
- **C5** Son güvenli ve sorun çözülmüş ('sıcaklık' aranmaz).
- **C6** Kalıp yargı yok.

Bir madde ancak hikayede o kusur yoksa 'yok' alır. Tereddüt ediyorsan 'var' de ve alıntıla.

## Çıktı

Çıktı dosyasının yolu parti talimatında verilir (varsayılan: `degerlendirme/urun_v1/hakem/K/puan_<n>.json`).
Dosya, partideki sırayla her hikaye için bir kayıt taşıyan bir JSON listesidir:

```json
[{"id": "<parti dosyasındaki id>",
  "ihlaller": [{"madde": "K6", "alinti": "<metinden birebir en az 3 kelime>", "cumle_no": 5,
                "aciklama": "<tek cümle>"}],
  "maddeler": {"K1": "yok", "K2": "yok", "K3": "yok", "K4": "yok", "K5": "yok", "K6": "var", "K7": "yok",
               "K8": "yok", "C1": "yok", "C2": "yok", "C3": "yok", "C4": "yok", "C5": "yok", "C6": "yok"},
  "gecti": false}]
```

- Önce ihlalleri (alıntı ve açıklama), sonra maddeleri, en son `gecti` alanını yaz.
- `maddeler` on dört maddenin hepsini taşır; değer yalnız "yok" ya da "var" olur.
- Her "var" için `ihlaller` içinde o maddeyle en az bir kayıt bulunur; "yok" olan maddeye ihlal yazılmaz.
- `gecti` yalnız bütün maddeler "yok" ise true olur. Kod bu alanı maddelerden yeniden hesaplar; tutarsız JSON
  bütün partiyi geçersiz kılar.
- `aciklama` tek cümledir; kartla ilgili bir kusursa kartın hangi alanına aykırı olduğunu söyler.

## Alıntı kuralı

- `alinti` hikayenin plan satırından ya da gövdesinden birebir kopyalanmış en az 3 kelimedir. Özetleme, düzeltme
  ya da kelime değiştirme yapma. Kod alıntıyı metinde arar; bulunamayan alıntı uydurma sayılır.
- `cumle_no` alıntının geçtiği cümlenin sırasıdır: gövde cümleleri 1'den başlar, plan satırı 0'dır.
- Bu mercekte her 'var' alıntı ister; `"alinti": null` kabul edilmez. Son ile ilgili kusurda (C5) son cümleyi
  alıntıla.

## Örnek eleştiriler

Örnekler kullanıcı yetkisiyle yazıldı. Hepsi kod kapılarından (K1-K9, K11) geçer; yani bu kusurları yalnız sen
yakalayabilirsin. Önce kusursuz bir taban hikaye, sonra tabanın tek yeri değiştirilmiş kusurlu biçimleri ve
beklenen ihlal kaydı verilir. Tabandaki hikayede bütün maddeler 'yok'tur; kısa, sade ve tek sahneli olmak kusur
değildir.

**Taban (bütün maddeler 'yok').** Tosbi | deniz | balık; tohum özelliği: kabuk. Kartta deniz tarifi: 'Denizin
kıyısı; kum ve sığ su kenarı. Herkes kumda ve su kenarında kalır.' Temel figürün isimsiz yan hayvanı konuşur.

> Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden yağmur başladı ve Tosbi'nin başı ıslandı. Tosbi başını ve ayaklarını kabuğuna çekti. Sudan küçük bir balık başını çıkardı. "Tosbi, neredesin?" diye sordu balık. "Buradayım, içerisi çok kuru," dedi Tosbi. Balık gülümsedi ve suya geri döndü. Tosbi içeride sessizce bekledi. Bir süre sonra yağmur dindi ve bulutların arasından güneş çıktı. Tosbi başını yavaşça dışarı çıkardı. Balık da yeniden sudan baktı. Kumdaki renkli taşlar güneşte parlıyordu.

1. 2\. cümle "Tosbi suya girip renkli taşlar topluyordu." olursa (K7 ve C3 var):
  {"madde": "K7", "alinti": "Tosbi suya girip renkli", "cumle_no": 2, "aciklama": "Deniz tarifi herkesin kumda ve su kenarında kaldığını söylüyor."}
  {"madde": "C3", "alinti": "Tosbi suya girip renkli", "cumle_no": 2, "aciklama": "Çocuğun taklit edebileceği biçimde suya giriliyor."}
2. 9\. cümle "Tosbi'nin burnu tıkandı ve içeride bekledi." olursa (C2 var):
  {"madde": "C2", "alinti": "Tosbi'nin burnu tıkandı", "cumle_no": 9, "aciklama": "Yağmurda ıslanan Tosbi'de hastalık belirtisi var."}
3. 9\. cümle "Tosbi içeride sabırla bekledi." olursa (K2 var):
  {"madde": "K2", "alinti": "Tosbi içeride sabırla bekledi", "cumle_no": 9, "aciklama": "Tohumdaki özellik kabuk; sabır ikinci bir özellik olarak ekleniyor."}

**Taban 2.** Niloya | park | Murat; tohum özelliği: soru. Kartın güvenli kullanım satırı: 'ağaca ya da yüksek yere
tırmanmaz'.

> Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu. "Bak Murat, uçurtma ağaçlardan yüksek!" dedi Niloya.

4. 10\. cümle "Niloya uçurtmanın yanına gitmek için ağaca tırmandı." olursa (C3 var):
  {"madde": "C3", "alinti": "gitmek için ağaca tırmandı", "cumle_no": 10, "aciklama": "Güvenli kullanım satırına göre Niloya ağaca tırmanmaz."}
5. 5\. cümle "Murat sihirli değneğini salladı ve uzun bir ip çıktı." olursa (K6 var):
  {"madde": "K6", "alinti": "Murat sihirli değneğini salladı", "cumle_no": 5, "aciklama": "Kartta Murat'ın sihirli değneği ya da büyü yeteneği yok."}
6. 11\. cümle 'Oyuncak robot "Harika!" dedi.' olursa kod yalnız belirsiz kelime notu verir; robot konuşan bir
   karakter olmuştur (K6 var):
  {"madde": "K6", "alinti": "Oyuncak robot \"Harika!\" dedi", "cumle_no": 11, "aciklama": "Belirsiz kelime robot karakter olarak konuşuyor; kartta böyle bir karakter yok."}
