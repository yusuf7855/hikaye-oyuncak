# Kör ikili tercih: olay örgüsü

Hikâyeler 3–6 yaş çocuklara bir oyuncak tarafından sesli okunacak. Her vakada aynı istekten (aynı figür(ler), aynı
yer) yazılmış iki hikâye var: **A** ve **B**. Hangi sistemden geldikleri gizli, sıraları her vakada rastgele. Temaları
sana verilmez.

**Soru:** Hangisinde sorun açık, çözüm o sorunu çözüyor ve olaylar birbirine bağlı?

Her iki hikâyeye de şu üç şeyi sor:

1. **Sorun** — Tek cümleyle söylenebilen bir sorun var mı? (istek, engel, kayıp, korku, anlaşmazlık) Olayların art
   arda sıralanması (gezdi, oynadı, yedi) sorun değildir.
2. **Çözüm** — Sonda çözülen şey o sorun mu? Sorun unutulup başka bir şey çözülüyorsa, hikâye yarım kalıyorsa ya da
   son yalnızca "çok mutlu oldular" diyorsa çözüm yoktur.
3. **Bağ** — Aradaki olaylar o sorunla ilgili ve birbirinin sonucu mu? Ortada başka bir olaya kaymak (top kaybı →
   yuva kaybı), sebepsiz olaylar ve mantıksız anlar (nesne anlamsızca canlanıyor, çelişki) bağı bozar.

## Karar

- Bu üç ölçütte daha iyi olanı seç: `"A"` ya da `"B"`. Fark küçük olsa da bir taraf seç.
- `"esit"` yalnızca ikisi gerçekten ayırt edilemiyorsa: ikisi de sağlam ya da ikisi de dağınık ve biri öne çıkmıyor.
- **Dikkate alma:** uzunluk, kelime seçimi, dil pürüzleri (anlamayı engellemedikçe), figür isimlerinin doğruluğu,
  hikâyenin önce ya da sonra gelmesi. Hangi sistemin yazdığını tahmin etmeye çalışma. Yalnızca olay örgüsünü yargıla.
- Her vakayı ayrı değerlendir; önceki vakalardaki kararların bir tarafa kaymasın.

## Girdi ve çıktı

Yalnızca sana verilen `parti_N.json` dosyasını oku (aynı klasördeki başka dosyaları açma). Biçimi:

```json
[{"id": 7, "A": "hikâye metni ...", "B": "hikâye metni ..."}]
```

Aynı klasöre, aynı sırada, her vaka için bir kayıt içeren `karar_N.json` yaz (ikinci bağımsız hakem `karar_N_b.json`):

```json
[{"id": 7, "karar": "A", "neden": "A'da top ağaca takılıyor ve sonunda indiriliyor; B'de sorun ortada değişiyor."}]
```

- `karar` yalnızca `"A"`, `"B"` ya da `"esit"`.
- `neden` tek satır (en fazla ~25 kelime): kararı hangi ölçütteki farkın belirlediğini söyle.

## Yürütücü için

```
python degerlendirme/ikili.py hazirla <yeni_kol> <taban_kol> [--parti 3] [--hakem 1]
#   -> degerlendirme/ikili_<yeni>__<taban>/parti_N.json, gorev.json (hakem işleri), anahtar.json (gizli)
#   Hakeme yalnızca bu dosya (IKILI.md) ve kendi parti_N.json'u verilir; anahtar.json asla verilmez.
python degerlendirme/ikili.py ozet <yeni_kol> <taban_kol> [--ayrinti] [--json]
#   -> yeni kolun puanı /n (eşit = yarım), tek yönlü kesin binom p, karar bandı
```

Karar bandı (n = 36; başka n için oranla ölçeklenir): **Kazandı** ≥ 24, **Eşit** 15–23, **Kaybetti** ≤ 14. Metni iki
kolda aynı olan vakalar hakeme gitmez ve n'den düşülür. Tam karar için ayrıca 'mantiksiz' ve bekçiler kontrol edilir.
