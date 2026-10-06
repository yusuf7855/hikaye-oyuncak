# Lisans gerektirmeyen karakterler: öneri ve plan

> 7 Ekim 2026. `docs/PAZAR_ARASTIRMASI.md`'nin bulgusu: ürün demosundaki 11 figürün 10'u lisanslı; satış için
> lisanssız bir karakter seti gerekiyor. Bu belge karar için seçenekleri ve iş planını veriyor. Hukuki görüş
> değildir: seçilen adlar için TÜRKPATENT marka araması ve avukat görüşü gerekir.

## Elimizde zaten olan: kendi hayvan karakterlerimiz

Projenin ilk döneminde (Eylül 2026) kendi tasarladığımız 12 karakterle çalıştık (`data/karakterler.json`):

| Karakter | Tür | Not |
|---|---|---|
| Pamuk | tavşan | |
| Tekir | kedi | "tekir" bir kedi rengi; tek başına marka olması zor [T] |
| Karabaş | köpek | Türkçede yaygın köpek adı [T] |
| Bal | ayı | |
| Kızıl | tilki | |
| Cikcik | kuş | |
| Tosbi | kaplumbağa | |
| Paytak | penguen | |
| Dino | dinozor | "Dino" adlı başka ürünler var: marka araması şart [?] |
| Alev | ejderha | |
| Elif | kız | |
| Can | oğlan | |

Bu karakterlerle yazılmış **~5.000 hikâye** var (`data/oyuncak_hikayeleri` 960, `oyuncak_v2` 1248, `oyuncak_v3`
1116, `oyuncak_v4` 1680). Ama bunlar ürün hattından (kart, yazar + kod kontrolü + hakem) önce yazıldı; kalitesi
`urun_v2/v3` düzeyinde değil ve figür kartı biçiminde değiller.

## Seçenekler

| | A. Kendi hayvan karakterlerimiz | B. A + halk figürleri | C. Yeni özgün karakter seti |
|---|---|---|---|
| Karakterler | Yukarıdaki 12 (ya da 8–10'u) | + Keloğlan, Nasreddin Hoca | Sıfırdan 8–10 karakter |
| Lisans riski | Düşük (marka araması gerekir) | Düşük; Keloğlan'ın TRT çizgi film tasarımı ve yan karakterleri kullanılmaz | Düşük |
| Hazır veri | ~5 bin (eski hat) | Halk figürleri için yok | Yok |
| Tanınırlık | Yok: çocuk karakteri oyuncakla tanır | Halk figürleri tanınır | Yok |
| Figür jetonu/oyuncak | Kendi tasarımımız, telifi bizde | Halk figürleri için de kendi çizimimiz | Kendi tasarımımız |

**Öneri: B.** Kendi hayvan karakterlerimiz ürünün çekirdeği olur (figür jetonlarının telifi bizde, ek paket
satışı yapılabilir). Keloğlan ve Nasreddin Hoca tanınırlık ve "yerli masal" kimliği katar.

## İş planı (veri artışı ile birlikte, haftaya)

`docs/YAPILACAKLAR.md`'deki "veriyi 20–30 bine çıkar" işi doğrudan yeni karakterlerle yapılırsa lisans sorunu ve
veri artışı tek seferde çözülür:

1. **Kartlar:** Her karakter için `data/urun_kartlari.json` biçiminde kart: kimlik cümlesi, 3 özellik
   (anahtar ifadeleriyle), güvenli kullanım kuralı, 4–6 yer, adlı yan karakterler. Özgün karakterlerde özellikleri
   biz belirleriz (kaynak = "urun_karari").
2. **Tohum ve istem:** `data/urun_v3/tohum` ve `istem` üretimi yeni kartlarla (figür başına ~2.000 tohum).
3. **Yazım:** Hafif hat (yazar + kod kontrolü; hakemsiz kalite 9,72 / 10 ölçüldü). 10 bin hikâye ≈ 14 saat.
4. **Eğitim:** Lisanslı figürlerin verisi eğitimden çıkarılır (ya da yalnız genel dil için kalır, adları isim
   süzgecine yasak olarak eklenir). `zincir_urun.sh` ile eğitim, `--en-iyi`.
5. **Ölçüm:** Aynı 164 vakalık kör kıyas düzeni ve rubrik; hedef ≥ c3ft_karma'nın 4,51'i.
6. **Kart ve web:** `firmware/hikaye_oyuncak/tools/basliklar.py` kartlardan tabloları yeniden üretir; Atölye paketi.

Karar gereken tek şey: **karakter listesi** (A/B/C ve hangi adlar). Karar verilince 1–2. adımlar birkaç saatlik iş.
