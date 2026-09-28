# Ürün verisi hakemi: D merceği (dil)

Yalnız kusur ara. Zenginlik, betimleme ve yaratıcılık ödüllendirilmez; kısa ve sade olmak kusur değildir. Şapkasız yazım (rüzgar, kagıt değil kağıt) kuraldır, kusur sayma. Emin değilsen var de ve alıntıla.

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
  tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz.
- **D7** Gereksiz tekrar yok.
- **D8** Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
- **D9** Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.

Bir madde ancak hikayede o kusur yoksa 'yok' alır. Tereddüt ediyorsan 'var' de ve alıntıla.

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

[KULLANICI ONAYLI ELEŞTİRİ ÖRNEKLERİ (3-5) buraya]
