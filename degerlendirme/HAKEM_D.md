# Ürün verisi hakemi: D merceği (dil)

Yalnız kusur ara. Zenginlik, betimleme ve yaratıcılık ödüllendirilmez; kısa ve sade olmak kusur değildir. Şapkasız yazım (rüzgar, kagıt değil kağıt) kuraldır, kusur sayma. Emin değilsen var de ve alıntıla; yalnız D6 (deyim, mecaz, soyut kavram) ve D7 (gereksiz tekrar) maddelerinde kusurdan emin olmadıkça 'yok' de.

Puan verilmez; her madde yok/var olarak işaretlenir. Bu hikayeler 3-6 yaş çocuklara okunacak ve küçük bir dil
modelini eğitecek; model gördüğü her dil hatasını öğrenir. Cihazda model plan satırını da kendisi yazdığı için
plan satırı da gövde gibi denetlenir. Yalnız bu merceğin maddelerine bak; mantık ve dünya kusurlarını başka
hakemler arar.

## Girdi

Yalnız bu dosyayı ve sana verilen parti dosyasını oku; başka dosya, önceki puan ya da yazar bilgisi okuma.
Parti en çok 10 hikayedir. Her hikayede şunlar vardır: `id`, plan satırları (sorun | çözüm), gövde, hikayede
geçmesine izin verilen adlar listesi ve kodun K6 işaretleri. K6 işaretleri karar değil, 'özellikle bak'
notudur: bitişik yazılmış olabilecek 'de/da' ve 'ki', birden çok biçimde çözümlenen belirsiz kelimeler ve
çoğul arka plan canlıları. İşaret olan yerde kusur yoksa 'yok' de; işaret olmayan yerde kusur varsa 'var' de.
Hikayeleri partideki sırayla, birbirinden bağımsız oku.

## Maddeler

Maddeler bu dosyada sabit sırayla yazılıdır; parti talimatı sana başka bir sıra verebilir, madde kimlikleri
(D1...D9) değişmez.

- **D1** Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
- **D2** Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
- **D3** Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
- **D4** Her replikte konuşan belli ve doğru kişi.
- **D5** Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
- **D6** Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan
  tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi
  (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış
  kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit
  benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek
  mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır:
  kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
- **D7** Gereksiz tekrar yok.
- **D8** Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
- **D9** Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.

Bir madde ancak hikayede o kusur yoksa 'yok' alır. Tereddüt ediyorsan 'var' de ve alıntıla (D6 ve D7 hariç:
bunları yalnız kusurdan eminsen işaretle).

## Çıktı

Çıktı dosyasının yolu parti talimatında verilir (varsayılan: `degerlendirme/urun_v1/hakem/D/puan_<n>.json`).
Dosya, partideki sırayla her hikaye için bir kayıt taşıyan bir JSON listesidir:

```json
[{"id": "<parti dosyasındaki id>",
  "ihlaller": [{"madde": "D1", "alinti": "<metinden birebir en az 3 kelime>", "cumle_no": 4,
                "aciklama": "<tek cümle>"}],
  "maddeler": {"D1": "var", "D2": "yok", "D3": "yok", "D4": "yok", "D5": "yok",
               "D6": "yok", "D7": "yok", "D8": "yok", "D9": "yok"},
  "gecti": false}]
```

- Önce ihlalleri (alıntı ve açıklama), sonra maddeleri, en son `gecti` alanını yaz.
- `maddeler` dokuz maddenin hepsini taşır; değer yalnız "yok" ya da "var" olur.
- Her "var" için `ihlaller` içinde o maddeyle en az bir kayıt bulunur; "yok" olan maddeye ihlal yazılmaz.
- `gecti` yalnız bütün maddeler "yok" ise true olur. Kod bu alanı maddelerden yeniden hesaplar; tutarsız JSON
  bütün partiyi geçersiz kılar.
- `aciklama` tek cümledir.

## Alıntı kuralı

- `alinti` hikayenin plan satırından ya da gövdesinden birebir kopyalanmış en az 3 kelimedir. Özetleme, düzeltme
  ya da kelime değiştirme yapma; yanlış yazımı düzeltmeden, olduğu gibi alıntıla. Kod alıntıyı metinde arar;
  bulunamayan alıntı uydurma sayılır.
- `cumle_no` alıntının geçtiği cümlenin sırasıdır: gövde cümleleri 1'den başlar, plan satırı 0'dır.
- Bu mercekte her 'var' alıntı ister; `"alinti": null` kabul edilmez.

## Örnek eleştiriler

Örnekler kullanıcı yetkisiyle yazıldı. Hepsi kod kapılarından (K1-K9, K11) geçer; yani bu kusurları yalnız sen
yakalayabilirsin. Önce kusursuz bir taban hikaye, sonra tabanın tek yeri değiştirilmiş kusurlu biçimleri ve
beklenen ihlal kaydı verilir. Tabandaki hikayede bütün maddeler 'yok'tur; kısa, sade ve tek sahneli olmak kusur
değildir.

**Taban (bütün maddeler 'yok').** Niloya | park | Murat.

> Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu. "Bak Murat, uçurtma ağaçlardan yüksek!" dedi Niloya.

1. 10\. cümle "Sarı uçurtma ağaçların üst çıktı." olursa (D1 var):
  {"madde": "D1", "alinti": "uçurtma ağaçların üst çıktı", "cumle_no": 10, "aciklama": "Tamlama eki ve yönelme eki eksik; 'ağaçların üstüne' olmalı."}
2. 9\. cümle "Rüzgar esti ve uçurtma yüzdü." olursa (D2 var):
  {"madde": "D2", "alinti": "esti ve uçurtma yüzdü", "cumle_no": 9, "aciklama": "Uçurtma yüzmez; fiil öznesine uymuyor."}
3. 4\. cümlenin yerine 'Murat da ipe baktı. "Çantada başka ip var mı?" diye sordu.' gelirse (D4 var):
  {"madde": "D4", "alinti": "Çantada başka ip var mı?", "cumle_no": 5, "aciklama": "Soruyu kimin sorduğu belli değil; son özne Murat ama çanta Murat'ın."}
4. 12\. cümle "Niloya'da ipi iki eliyle tuttu." olursa (D8 var):
  {"madde": "D8", "alinti": "Niloya'da ipi iki", "cumle_no": 12, "aciklama": "Bağlaç olan 'da' ayrı yazılır: 'Niloya da'."}

**Taban 2.** Tosbi | deniz | balık.

> Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden yağmur başladı ve Tosbi'nin başı ıslandı. Tosbi başını ve ayaklarını kabuğuna çekti. Sudan küçük bir balık başını çıkardı. "Tosbi, neredesin?" diye sordu balık. "Buradayım, içerisi çok kuru," dedi Tosbi. Balık gülümsedi ve suya geri döndü. Tosbi içeride sessizce bekledi. Bir süre sonra yağmur dindi ve bulutların arasından güneş çıktı. Tosbi başını yavaşça dışarı çıkardı. Balık da yeniden sudan baktı. Kumdaki renkli taşlar güneşte parlıyordu.

5. 9\. cümle '"Burada beklerim," dedi Tosbi kendi kendine.' olursa (D5 var):
  {"madde": "D5", "alinti": "dedi Tosbi kendi kendine", "cumle_no": 9, "aciklama": "Tosbi kendi kendine konuşuyor."}
6. 13\. cümle "Kumdaki renkli taşlar güneşe gülümsüyordu." olursa (D6 var):
  {"madde": "D6", "alinti": "taşlar güneşe gülümsüyordu", "cumle_no": 13, "aciklama": "Taşlar gülümsemez; mecaz 3 yaşındaki çocuğa uygun değil."}
