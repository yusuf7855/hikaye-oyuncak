# İskeletli üretim (degerlendirme/iskelet.py)

Soru: hazır plan (oracle) bile hikâyeyi iyileştirmedi (Tur 3, %47). Olay örgüsünü **kod** kurar, model yalnız cümleleri
tamamlarsa mantıksız olay (%89) ve bozuk dil (%82) şikâyetleri azalır mı? Model v4 (`hf_c2ft_plan`), seçici E5b
(`sec.puanla`), aynı test seti ve seed kuralı; karşılaştırılacak taban `c2ft_plan_olay2`.

## Açılış bankası: eğitim hikâyelerindeki sayılar

Kaynak: `data/oyuncak_v2` + `oyuncak_v3` (v4'ün ince ayar verisi, `ince_ayar_c2.sh` varsayılanı), 2364 hikâye, medyan 12
cümle. Sütun: cümlenin hikâyedeki göreli yeri (0 = ilk, 1 = son; iç cümleler dörde bölündü). `<İsim>` = figür adıyla
başlayan cümle.

| açılış | giriş | ≤.25 | ≤.5 | ≤.75 | <1 | son |
|---|---:|---:|---:|---:|---:|---:|
| Bir gün | 0 | **1175** | 35 | 0 | 5 | 0 |
| Bir sabah | 0 | **176** | 2 | 2 | 7 | 0 |
| Birden | 0 | 2 | 2 | 0 | 0 | 0 |
| O sırada / Tam o sırada | 0 | 5 | 26 | 10 | 0 | 0 |
| Ama | 0 | 15 | 76 | 2 | 0 | 0 |
| Sonra | 0 | 2 | **147** | 73 | 20 | 12 |
| Önce | 0 | 5 | 23 | 7 | 0 | 0 |
| Sonunda | 0 | 0 | 7 | **61** | 24 | 1 |
| Kısa sürede | 0 | 0 | 5 | **40** | 51 | 0 |
| İkisi birlikte | 0 | 0 | 15 | **68** | 87 | 58 |
| Birlikte | 0 | 0 | 54 | 260 | 177 | 24 |
| O günden sonra | 0 | 0 | 2 | 3 | 84 | **230** |
| Akşam olunca | 2 | 29 | 1 | 7 | 58 | **95** |
| Güneş batarken | 0 | 1 | 0 | 6 | 28 | 62 |
| `<İsim>` | 7 | **1474** | 2369 | 1998 | 2214 | 530 |
| `<İsim>` hemen | 0 | 58 | **206** | 66 | 1 | 0 |
| `<İsim>` önce | 0 | 31 | **224** | 34 | 0 | 0 |
| `<İsim>` artık | 0 | 0 | 0 | 11 | 171 | 61 |
| `"` (konuşma) | 0 | 31 | 1399 | 1497 | 532 | 5 |

- İkinci cümle %35 figür adıyla (çoğu "… çok severdi."), üçüncü cümle %32 "Bir gün" ile başlar.
- "Birden", "Bunun üzerine", "Neyse ki" bu veride hemen hiç yok: kullanılmadı (modelin görmediği üslup).
- Zaman: geçmiş (-dı), giriş/özellikte geniş zamanın hikâyesi (-ardı/-erdi). Açılışlar zaman eki taşımaz, model seçer.
- v4 verisinde (1680 hikâye) sıra aynı; "Birden" (37) ve "Ama" (226) orada daha sık, ama v4 modeli o veriyi görmedi.

## İskelet

| aşama | açılış (ağırlık = sayı) | model | 
|---|---|---|
| giriş | şablon: `baslangic(ilk_cumle=True)` → "Ormanın derinliklerinde Pamuk adında bembeyaz bir tavşan yaşardı." | — |
| özellik | `<A>` | 1 cümle |
| sorun | Bir gün (1175) / Bir sabah (176) | ≤2 cümle |
| deneme | `<A>` önce (224) / `<A>` hemen (206) | 1 cümle |
| dönüm | tek: Sonra; ikili: `<B>` / Sonra (eşit) | ≤2 cümle |
| çözüm | tek: Sonunda (61) / Kısa sürede (40); ikili: İkisi birlikte (68) / Sonunda (61) | 1 cümle |
| kapanış | O günden sonra (230) / Akşam olunca (95) | 1 cümle |

Toplam ~10 cümle (veride medyan 12, mevcut sistemin gövdesi ortalama 102 token). Açılış adayın seed'iyle ağırlıklı
seçilir, 8 aday farklı iskelet varyantları da görür.

- **Ek/ünlü uyumu:** yalnız katalogdaki biçimler (açılış "…-da/-de", isim, sıfat) ve yalın isim kullanılır; kod hiçbir
  ek üretmez. `<A>`/`<B>` yalın ad ("Pamuk önce"); ekleri (Pamuk'un) gerekirse model yazar.
- **Plan başlığı:** model %70 planlı başlıkla eğitildi ve plan modu (E3) en iyi koldu; plan korunur ve modelce yazılır
  (uret.py `--baslik plan` ile aynı istem). Tek fark: "Çözüm:" kodla eklenir (sorun satırı Ċ ile biter, `gen -e Ċ`),
  plan böylece her zaman iki satır. Plan token'ları tekrar penceresine girmez (`gen -W`), `-S`'deki gibi.
- **Giriş şablonu:** C2'nin eğitim hikâyelerinin ilk cümlesi bu kalıpta (giriş sütunu). İkili vakada iki figür tek
  cümlede tanıtılır (kartın şablonu), veride ikinci figür çoğu kez ayrı cümlede gelir: küçük bir üslup farkı.

## Cümle sonu

Token'lar: `.`=14, `."`=513, `!"`=365, `?"`=479, `...`, `?`, `!` ayrı; `"Merhaba." dedi` içindeki `."` tek token.
`gen -e` tek id alır ve bakış (sonraki token) olmadan `"Merhaba." dedi`yi ayıramaz. Bu yüzden aşama başına kısa bir
dilim üretilir (1 cümle: ≤48, 2 cümle: ≤80 token, EOT'de durur) ve Python'da kesilir: metin `[.!?]["”]?` ile biter,
tırnaklar dengeli, ardından boşluk + büyük harf / açılan tırnak ya da EOT gelir. Kartta aynı kural bir token bakışla
uygulanır (bakış token'ı KV önbelleğinde bir konum geri alınarak atılır); `n_cihaz` bu bakışları sayar.
Cümle bitmezse (çok uzun ya da bağlam 256 dolu) o aşama atılır, hikâye önceki cümlede biter ve `bitti=false`.

## Adaylar

`--aday K` = vaka başına K tam iskelet hikâye + mevcut seçici (`sec.puanla`, plan ile). Aşama başına log-olasılıkla
en iyi-k seçimi seçilmedi: (1) ortalama log-olasılık kısa/sıradan cümleyi seçer ve açgözlü; Tur 2'de log-olasılık
hakemle zayıf ilişkili çıktı, E5b kuralları ise hakemde doğrulandı ve hikâyenin bütününe bakar (figür sonda var mı,
sonradan beliren karakter, tekrar); (2) kartın önceden-üret + seç akışı değişmez. Hesap: 6 örnek adayda `n_cihaz`
113–134 token (plan ~25 + gövde ~90–106 + 6 bakış); mevcut sistem plan ~25 + gövde ortalama 102 ≈ 127. 8 aday aynı
bütçe.

`bitti`: sonu iskelet belirler; kapanış cümlesi tamamlandıysa true. Modelin kapanıştan sonra EOT seçip seçmediği
`eot_son`'da (tanı). `lp`: yalnız modelin ürettiği token'lar (zorlanan açılış ve giriş hariç).

## Bilinen riskler

- Tekrar penceresi (64): aşama çağrılarında istemin son 64 token'ı pencerede (`gen` varsayılanı). Gövde 64 token'ı
  geçene kadar plan token'ları da pencerede kalır (plan modunda `-S` onları dışarıda tutar); ceza 1.1, küçük fark.
- Sabit aşama yeri modelin kendi temposuyla çakışabilir: özellik cümlesinde sorun erken başlarsa "Bir gün" ikinci
  kez sorun açar; çözüm önceki aşamada gelmişse "Sonunda" tekrar eder ("Sonunda topu Sonunda topu buldular").
- "`<A>` önce" bazen kendine gönderme doğurur ("Dino önce Dino'nun…"); seçici bunu cezalar.
- Host'ta her aşama bağlamı baştan işler (gen durum tutmaz): aday başına ~7 sn (yüklü 4 çekirdekte).
