# Deney planı: mantıklı olay örgüsü (C2)

> Beş bağımsız tasarımcının 20 önerisi, üç hakemin (etki, uygulanabilirlik, ölçülebilirlik) puanlarıyla
> birleştirildi. E0 araçları (`degerlendirme/`, `runtime/ornekle.h`) ve E1 (`prepare_ft2 --tema`) uygulandı.

## Durum (24 Eylül 2026, 07:36)
- **Ön-eğitim c2:** 6170/24000 adımda.
- **Ara ince ayar c2ara:** 270/1500 adımda. Ara checkpoint `runs/ple-c2-s0-ara.pt` üzerinde, temasız eski başlıkla koşuyor. Yaklaşık 42 dk kaldı. Bu koşu E1'in hazır taban kolu olacak.
- **Paralel koşmanın bedeli ölçüldü:** İki iş aynı anda 4'er thread ile koşarken ön-eğitim ~1.0 s/adımdan 3.9 s/adıma, c2ara 2.07 s/adıma çıkıyor. Toplam verim sıralı koşmaktan düşük. Bu yüzden ön-eğitimin yanında aynı anda en fazla bir ince ayar koşulmalı.

## 0. Tüm deneyler için ortak kurallar

**Sabit ayarlar**
- Test seti: `uret.test_seti()` ile 36 vaka. Seed 1000·i+j, K=8, temp 0.5, top-k 40, rep 1.1.
- Tema ataması: vakaya `TEMALAR[(7*i)%20]` verilir, KILAVUZ sırasıyla. 36 vaka 20 temanın hepsini kapsıyor ve 3'ten az örneği olan (yer, tema) hücresine düşen vaka yok; bunu kontrol ettim.

**Ölçüm paketi (her kol için)**
1. `otomatik.py` bekçileri: `uydurma_kelime_%`, `biten`, `kurallari_gecen`.
2. Hakemsiz mekanizma ölçüleri. Hepsi yeni `degerlendirme/olay.py` içinde:
   - `iki_yari_ayni_tema_%`, `istenen_tema_%`, `farkli_tema/20`: token-NB ile hesaplanır.
   - `top_%`, `paragraf_%`, `cunku_%`.
   - `kopya8_%`: eğitim setiyle 8-gram örtüşmesi.
3. Hakem:
   - RUBRIK.md'ye 3 evet/hayır sorusu eklenir. JSON'a `s1, s2, s3` alanları yazılır:
     - S1: Hikâyede tek cümleyle söylenebilen bir sorun var mı?
     - S2: Sonda çözülen şey o sorun mu?
     - S3: Aradaki olaylar o sorunla ilgili mi?
   - Her hikâyeyi 2 bağımsız hakem puanlar. 'mantiksiz' sayısı iki hakemin ortalamasıdır.
   - Taban kol da bu yeni rubrikle yeniden hakemlenir.
4. Kör ikili tercih. Yeni dosyalar `degerlendirme/IKILI.md` ve `degerlendirme/ikili.py hazirla|ozet A B`.
   - Aynı vakanın A ve B hikâyeleri rastgele sırayla verilir.
   - Soru: "Hangisinde sorun açık, çözüm o sorunu çözüyor ve olaylar birbirine bağlı?" Cevap A, B ya da eşit.
   - Hakemlere tema verilmez.
5. Kullanıcı puanı: web sayfasındaki yeni `mantik` düğmeleri (aşağıda). İkincil ölçüdür.

**Karar kuralı**
- **Kazandı:** İkili tercihte en az 24/36 (eşitler yarım sayılır; tek yönlü p=0.033), 'mantiksiz' artmamış ve bekçiler sağlam: `uydurma_kelime_%` artışı ≤ 0.1 puan, `biten` en fazla 2 düşüş.
- **Eşit:** 15–23/36. Yalnızca cihaz maliyeti yoksa ve mekanizma ölçüsü iyileştiyse benimsenir.
- **Kaybetti:** ≤14/36.
- 'mantiksiz' sayısının standart hatası n=36'da yaklaşık 2.6 vaka. Bu yüzden karar ikili tercihle verilir.

**Randomluk kuralı:** Yeni rastgelelik ayrı bir üreteçle yapılır, ör. `random.Random(seed+17)`. Böylece veri sırası ve genel dilim önceki kolla birebir aynı kalır.

## Başlık biçimi (tek karar; 1, 11 ve 17 birleştirildi)
```
eski : "Karakter: X | Yer: Y\n\n"
tema : "Karakter: X | Yer: Y | Tema: T\n\n"                          (+6–10 token)
plan : "Karakter: X | Yer: Y | Tema: T\nSorun: S\nÇözüm: Ç\n\n"      (istem "\nSorun:" ile biter)
```
- "Tema" ile "Konu" ikisi de 2 token'dır. "Tema" seçildi.
- "\n\n" iki ayrı Ċ (id 199) token'ıdır.
- Temalı başlık + hikâye en fazla ~184 token. Plan eklenince en fazla ~224 token; ikisi de 256 sınırının altında.

---

## E0 — Ölçüm altyapısı ve dekoder düzeltmeleri
Eğitim gerektirmez. c2ara biter bitmez yapılır; CPU ~20 dk.

**Kod**
- `degerlendirme/uret.py` ve `otomatik.py`'ye şu bayraklar eklenir:
  - `--baslik {eski,tema,plan}`
  - `--pencere {tum,govde}`
  - `--satir-yasak`
  - `--eot-on`
  - `--plan-kosul {model,oracle}`
- Her kol tüm adayları `<model_dir>/adaylar_<ad>.json` dosyasına yazar: `{vaka, j, metin, plan, n, lp, bitti}`. Seçici deneyleri bu havuz üzerinde çevrimdışı yapılır.
- `runtime/host_verify/gen.c`'ye iki bayrak eklenir:
  - `-P`: İstem token'ları `recent` penceresine girmez. Şu an gen.c'de istem döngüsü ve atolye.html:515 bunları pencereye koyuyor.
  - `-N`: Gövdede Ċ (199) ve ĠĊ (9491) yasaklanır.
- Örnekleme mantığı `runtime/ornekle.h` dosyasına taşınır. gen.c ve firmware aynı kodu kullanır.
- gen.c değişince `rm gen` yapılmalı. Betik yalnızca `gen` yoksa derliyor.
- Yeni `degerlendirme/tema_sinif.py`:
  - Öneri 9'daki token düzeyinde NB. Model tokenizer'ıyla yalnızca eğitim bölmesinden öğrenilir.
  - Çıktı `hf_x/tema_nb.bin` ve `.json`.
  - E5'e kadar yalnızca ölçüm aracıdır; seçicide kullanılmaz.
- Yeni `degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-<tag>-s0.pt --veri data/tr_<tag>/vocab-16384/dogrulama.json [--eot] [--plan]`:
  - 138 doğrulama hikâyesi üzerinde öğretmen zorlamalı NLL hesaplar.
  - Tema duyarlılığı: ΔNLL = NLL(hikâye | 3 rastgele yanlış tema) − NLL(hikâye | doğru tema). İlk ve ikinci yarı ile son üçte bir ayrı raporlanır.
  - EOT öneki: istem başında EOT'lu ve EOT'suz NLL karşılaştırılır.
  - `--plan` ile gerçek plan ve aynı temadaki başka hikâyenin planı karşılaştırılır.
- `research/tinystories/prepare_ft2.py`:
  - `baslik(h, tema=False, plan=None)` ve `--tema` bayrağı eklenir. Bayrak rng tüketmez.
  - Doğrulama hikâyeleri `out/dogrulama.json` dosyasına yazılır: `id, turler, yer, tema, metin`.

**Kollar:** c2ara modelinde, aynı seed'lerle, her biri tek başına tabana karşı:

| Kol | Değişiklik | Ölçü |
|---|---|---|
| P | `-P` | hakem |
| N | `-N` | hakem |
| E | EOT öneki | yalnızca NLL |

Komut örneği: `python degerlendirme/uret.py hf_c2ara c2ara_P --aday 8 --pencere govde`

**Başarı ve sonuç**
- P ve N: Kazandı ya da Eşit çıkarsa ve bekçiler sağlamsa varsayılan yapılır.
- E: Doğrulama NLL'i EOT ile anlamlı düşerse (eşli %95 güven aralığı 0'ı içermiyorsa) `prompt_idler(eot=True)` varsayılan olur.
- Kaybeden kapalı kalır.
- İstisna: E1'de iki kol da `-P` ile ölçülür. Tema kelimelerinin cezalanmaması E1'in ön koşulu.

## E1 — Tema başlıkta (öneri 1, çekirdek; ilk gerçek deney)
**Değişiklik:** Yalnızca `--tema`. Taban olarak c2ara kullanılır: aynı ara checkpoint, aynı 1500 adım, aynı bölme ve aynı genel dilim.

**Komut:** c2ara bittikten sonra, ön-eğitimin yanında tek iş olarak:
```
BAZ=runs/ple-c2-s0-ara.pt STEPS=1500 ./ince_ayar_c2.sh c2ara_tema --tema
python degerlendirme/uret.py hf_c2ara_tema c2ara_tema --aday 8 --baslik tema --pencere govde
python degerlendirme/otomatik.py hf_c2ara_tema --baslik tema --pencere govde
python degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-c2ara_tema-s0.pt --veri data/tr_c2ara_tema/vocab-16384/dogrulama.json
```

**CPU:** 1500 adım. Paralel koşarken ~2.1 s/adım, yani ~50 dk; tek başına ~21 dk. Üretim ve ölçüm ~10 dk daha. Ön-eğitimi yaklaşık 45 dk geciktirir.

**Başarı (hepsi gerekli)**
- İkili tercih ≥ 24/36.
- ΔNLL (ikinci yarı) ≥ 0.02 nat/token ve eşli güven aralığı 0'ı içermiyor.
- `iki_yari_ayni_tema_%` ≥ 50 (bugün 25–31).
- `farkli_tema` ≥ 17/20 (bugün 10/20).

**Başarısızsa**
- **ΔNLL ≈ 0 (model alanı yok sayıyor):** Doğrudan E3'e (plan) geçilir. Tema alanı plan başlığının parçası olarak kalır.
- **ΔNLL > 0 ama hakem farkı yok:** Tema korunur, çünkü destenin çeşitliliğini ve E5'teki seçiciyi mümkün kılıyor. E2 ve E3 uzun menzili hedefler.

## R — Nihai checkpoint'te yeniden taban (deney değil)
Ön-eğitim bitince yapılır.

**Bölme bir kez sabitlenir** (öneri 8'in ilk adımı):
- `research/tinystories/benzerlik.py` yazılır: TF-IDF, 5 harflik kökler, figür isimleri çıkarılmış.
- Çıktı `data/bolme.json`: seed 0'daki 138 doğrulama kimliği + herhangi bir doğrulama hikâyesine kosinüsü > 0.6 olan ~86 eğitim hikâyesinin çıkarılma listesi.
- `prepare_ft2 --bolme data/bolme.json` bu listeyi okur.
- Aynı adımda her oyuncak bloğunun önüne EOT eklenir. `np.array_split` dilimleri hikâye ortasında bitiyor; E2 bu EOT'lere ihtiyaç duyuyor.
- Bundan sonraki bütün kollar bu bölmeyi kullanır.

**Komut:** `./ince_ayar_c2.sh c2ft_tema --tema --bolme data/bolme.json`, E0 kazananları ile. CPU ~45 dk.

**E1 net çıkmadıysa (Eşit bandı):** `c2ft` de aynı bölmeyle koşulur (+45 dk) ve E1 nihai checkpoint'te yinelenir.

## E2 — Başlıkla hizalı eğitim pencereleri (öneri 3; 13 ve 17'nin hizalama kısmı buna katıldı)
**Kod**
- `prepare_ft2`: `train_bas.npy` ve `train_son.npy` yazılır (uint32: başlıktan önceki EOT konumu, hikâye sonu+1). Val için aynıları.
- `train.py`: `--hizala toy` bayrağı eklenir. `Batcher.__call__`'da her `i` için:
  - `j = searchsorted(bas, i, 'right') - 1`
  - `j >= 0 and i < son[j]` ise `i = bas[j]` yapılır, `i + sl + 1 ≤ len` sınırı korunur.
  - Böylece karışım değişmez.
- `evaluate()` aynı kalır. Ek olarak `val_hizali` raporlanır: yalnızca hikâye token'ları, üçte birlik dilimler hâlinde.
- `ince_ayar_c2.sh`: train satırının sonuna `${EK_TRAIN:-}` eklenir.

**Komut:** `EK_TRAIN='--hizala toy' ./ince_ayar_c2.sh c2ft_hiz --tema --bolme data/bolme.json`

**CPU:** ~45 dk.

**Başarı**
- `val_hizali` son üçte birde düşüyor.
- ΔNLL (son üçte bir) en az %20 artıyor.
- İkili tercih ≥ 16/36.
- Cihaza maliyeti olmadığı için eşitlikte de benimsenir.

**Başarısızsa:** Bırakılır, taban R kalır.

## E3 — Model önce iki satırlık plan yazar (2 ve 15 birleşti; 6, 17 ve 20'den alanlar aşılandı)
**Etiketleme (tek iş, hemen başlar, CPU gerektirmez)**
- Klasör `data/oyuncak_plan/`: `KILAVUZ.md`, `parti.py` (24 × ~100, `web/veri.json`'dan), `birim.py` (v3 kuyruğu), `kontrol.py`, `plan.jsonl`.
- Her satır: `{"id","sorun","cozum","anahtar_sorun","anahtar_cozum","yardimci","yok"}`.
- Kurallar:
  - sorun ve cozum 3–9 kelime, -dı'lı geçmiş zaman.
  - Özel isim, figür adı ya da türü yok. Özne ya düşer ya 'ikisi' olur. Böylece plan figürden bağımsızdır ve ileride cihaz plan havuzu yapılabilir.
  - sorun, hikâyede geçiyorsa sebebini de söyler.
  - cozum, sorunu çözen eylemdir; mutlu son değildir.
  - `|` ve satır sonu yok.
  - `anahtar_sorun` hikâyenin ilk %60'ında, `anahtar_cozum` ondan sonra ve son %60'ta geçer (ilk 5 harf kök eşleşmesi).
  - Sorunu olmayan hikâyeye (~203) `yok: true` yazılır. Bu hikâyeler plansız başlıkla eğitilir; yeniden yazılmaz.
- `kontrol.py` bu kuralları denetler; reddedilen satır ajana geri gider.

**Veri:** `prepare_ft2 --plan data/oyuncak_plan/plan.jsonl --plan-orani 0.7`.
- Her kopya ve her hikâye için ayrı bir rng ile %70 plan başlığı, kalanı yalnızca tema başlığı.
- Plan token'ları kayba dahildir.
- `dogrulama.json`'a plan da yazılır.

**Çıkarım**
- İstem: `prompt_idler(..., plan=True)`. `header + "\nSorun: top"` kodlanır, ofseti `"\nSorun:"` sonuna kadar olan token'lar alınır.
- gen.c'ye `-S` bayrağı eklenir:
  - Gövde, üretilen ilk Ċ Ċ'den sonra başlar.
  - O noktada `recent` sıfırlanır; `-N` yalnızca gövdede uygulanır.
  - Plan 48 token'ı geçerse aday bırakılır (stderr: `plan_bozuk`).
  - `ort_logp` yalnızca gövde token'larından hesaplanır.
- `uret.py` metni plan ve gövde olarak böler. Hakem yalnızca gövdeyi görür.
- Seçiciye bu deneyde yalnızca "plan bozuksa reddet" kuralı girer. Plan uyum cezası E5'te ayrı ölçülür.

**Komut**
```
EK_TRAIN="<E2 kazandıysa --hizala toy>" ./ince_ayar_c2.sh c2ft_plan --tema --bolme data/bolme.json --plan data/oyuncak_plan/plan.jsonl --plan-orani 0.7
```
Aynı ağırlıklarla 3 koşul ölçülür:
- (a) `--baslik tema`: plansız mod gerilemiş mi?
- (b) `--baslik plan --plan-kosul model`: asıl kol.
- (c) `--plan-kosul oracle`: doğrulama hikâyelerinin gerçek planları; üst sınır.

**CPU:** 45 dk eğitim + 15 dk ölçüm.

**Başarı**
- (b), önceki en iyiye karşı ikili tercihte ≥ 24/36.
- 'mantiksiz' en az %25 azalıyor ve S2 oranı artıyor.
- `plan_uyum_%` ≥ 70: anahtar_sorun kökü ilk %60'ta, anahtar_cozum kökü son %60'ta.
- Öğretmen zorlamalı ölçüde gerçek plan, karıştırılmış plana göre son üçte birde ≥ 0.03 nat/token daha düşük NLL veriyor.
- `kopya8_%` ≤ 15.
- (a), önceki en iyiden kötü değil (ikili tercih ≥ 15/36).

**Başarısızsa**
- **(c) iyi, (b) kötü (model kötü plan yazıyor):** Sonraki deney E3', eğitim dışı plan havuzu (öneri 20). Ajanlar ~1600 figürden bağımsız plan yazar (~130 KB). Aynı model (c) koşuluyla ölçülür. Genelleme açığı = (c) − (havuz) en fazla 0.5 puan olmalı.
- **Plan uyumu düşük (model planı yok sayıyor):** `--plan-orani 0.9` ile tek bir tekrar yapılır; o da tutmazsa plan bırakılır.
- **İkisi de kötü:** Plan bırakılır, tema modeli kalır.

## E4 — Oyuncak payı (5 ve 13-A2 birleşti; tek değişken: pay)
**Değişiklik:** `--genel-token 3000000 --tekrar 8`. Oyuncak payı %18.5'ten ~%45'e çıkar, 3000 adım korunur.
- `train.py`'ye `--sakla-her 750` eklenir: `runs/{name}.step{N}.pt` kopyası saklanır, silinmez.
- 750, 1500, 2250 ve 3000. adım checkpoint'lerinde yalnızca hakemsiz ölçüler alınır: oyuncak val NLL, `genel_val` (tr2 val.bin), `kopya8_%`, `top_%`.
- Hakeme yalnızca 3000. adım modeli gider. Checkpoint'lerden birini "en iyi" diye seçmek kazananın lanetini doğurur; bu yapılmaz.

**Komut:** `EK_TRAIN="--sakla-her 750 ..." ./ince_ayar_c2.sh c2ft_pay <önceki en iyinin argümanları> --genel-token 3000000 --tekrar 8`

**CPU:** ~45 dk.

**Başarı**
- İkili tercih ≥ 24/36.
- `top_%` ≤ 10 (bugün 22).
- `genel_val` artışı ≤ 0.15 nat.
- `kopya8_%` ≤ 15.
- Uydurma kelime artışı yok.

**Başarısızsa**
- **Dil bozulduysa:** Ara pay denenir (genel 5M, tekrar 7).
- **Mantıkta fark yoksa:** E4b denenir, yani öneri 5'in filtresi: çatışma sözlüğü, yabancı isim yok, figür adı yok, 60–200 kelime, tek paragraf. Pay eski düzeyde tutulur; ayrı bir kol olarak koşulur.

## E5 — Seçici terimleri (eğitim yok; kayıtlı 36×16 aday havuzunda)
**E5a — Tema sadakati** (4 ve 11 birleşti; tablo 9'daki token-NB)
- `sec.py`'ye `tema_cezasi(ids, tema)` eklenir:
  - Tam metnin argmax teması istenen tema değilse −2.
  - İlk yarınınki değilse −1.
  - İkinci yarınınki değilse −1.5.
- `puanla(..., tema=)` bu cezayı ekler.
- Yanlış red oranı 138 doğrulama hikâyesinde ≤ %12 olmalı.

**E5b — Plan uyumu** (yalnızca E3 benimsendiyse)
- `plan_cezasi`: anahtar kök ilk %60'ta yoksa −2, son %60'ta yoksa −2.

**Ölçüm**
- Eski ve yeni seçici aynı havuzda çalıştırılır.
- Yalnızca seçimin değiştiği vakalar kör ikili olarak hakeme gider.
- NB ölçüleri başarı ölçütü olarak kullanılmaz; seçiciyi yapan araç ölçüm aracı olamaz.

**CPU:** ~15 dk. Havuz: 36×16 aday.

**Başarı:** Değişen vakaların en az %65'inde yeni seçici tercih ediliyor ve 'mantiksiz' artmıyor.

**Başarısızsa:** Terim eklenmez.

## E6 — Kilitler (öneri 18; eğitim yok)
- `kilit.py` bir `uint8[V]` tablosu üretir, `hf_x/kilit.bin` olarak yazılır. gen.c'ye `-G -A -K -N` bayrakları eklenir, `ban[512]` → `ban[4096]`.
- İki kol ayrı ölçülür:
  - **İsim + yer kilidi:** Veride 0/2364 ihlal var, yani eğitim verisiyle çelişmiyor.
  - **Hayvan kilidi:** Tek figürde K=1, ikilide K=0.

**CPU:** ~15 dk.

**Başarı**
- Hakem notlarında yeni karakter, uydurma isim ve yer kayması kusurları en az %50 azalıyor.
- İkili tercih ≥ 16/36.
- `uydurma_kelime_%` ≤ 0.3.

**Başarısızsa:** Yalnızca geçen kilit tutulur.

## E7 — Koşullu: kurgu tercih eğitimi (öneri 14)
Yalnızca E3 ve E4'ten sonra, 'mantiksiz' hâlâ 12/36'nın üstündeyse yapılır.
- `prepare_tercih.py`: SON ve ARA negatifleri, aynı figür kümesinden, farklı temalı hikâyelerden. SIRA testi ayrılmış tutulur.
- `tercih.py`: 800 adım, β=0.1, NLL=1.0, `--qat-emb`, erken durdurma.
- **Zorunlu kontrol kolu:** Aynı 800 adım yalnızca NLL ile. Bu kol olmadan kazanç tercih kaybına atfedilemez.
- **CPU:** ~0.5 saat.
- **Başarı:** Kontrol koluna karşı ikili tercih ≥ 24/36 ve `bozuk_dil` artmıyor.

---

## Web test sayfası
**`web/paketle.py`** — `meta.json`'a eklenenler:
- `baslik_bicimi` (`eski` / `tema` / `plan`). Alan yoksa sayfa `eski` kabul eder; eski sürümler çalışmaya devam eder.
- `prompts_bas["figürler|yer"]`: sondaki Ċ Ċ olmadan.
- `temalar`: `[{ad, ids}]`, ids = `" | Tema: T"` token'ları.
- `nl2`: `[199,199]`. `plan_ek`: `"\nSorun:"` token'ları.
- `seyrek`: 6×20 hücre sayısı; 3'ten az örneği olan hücreler.
- `eot_on`, `pencere: "govde"`, `satir_yasak: [199,9491]`.
- Parçalı birleştirmenin tam metin kodlamasıyla aynı olduğu 9360 başlığın hepsinde assert ile doğrulanır.
- E5 ve E6 benimsenirse `tema_nb.bin` ve `kilit.bin` base64 olarak eklenir.

**`web/atolye.html`**
- Tema seçici `<select id="tema">`: varsayılan "rastgele (deste)", yanında 20 tema. Deste, cihazdakiyle aynı algoritmadır; durumu localStorage'da tutulur ve try/catch ile sarılır.
- İstem `baslik_bicimi`'ne göre kurulur: `prompts_bas + temalar[t] + (nl2 | plan_ek)`.
- `uret()`: `pencere==="govde"` ise istem `recent`'e eklenmez (satır 515). Plan modunda Ċ Ċ'de `recent` sıfırlanır; satır yasağı yalnızca gövdede uygulanır; 48 token'ı geçen plan reddedilir.
- Plan gri bir satır olarak ayrı gösterilir. Seslendirme yalnızca gövdeyi okur.
- `puanla()`, sec.py ile birebir tutulur: plan biçim kuralı, sonra E5 terimleri.
- `degerlendirmeler` kaydına `tema`, `plan` ve `mantik` alanları eklenir. `mantik` yeni 3 düğmeden gelir: "Olay örgüsü: saçma / idare eder / mantıklı" → 0/1/2.
- Yan yana karşılaştırılan sürümlere aynı tema ve seed verilir.
- Her deney için `SURUMLER`'e bir kayıt eklenir; `olcum` alanına otomatik ve hakem özeti yazılır.

## Cihaz yolu
**`baslangic.py`**
- `TEMALAR` (KILAVUZ sırası) ve `SEYREK` listesi eklenir. SEYREK hücreleri: ev×birlikte çalışmak (0); orman×uyku vakti, orman×doğum günü sürprizi, orman×hasta bir arkadaşa bakmak (1'er); ev×merak ve keşif, dağ×paylaşmak (2'şer).
- Fonksiyon imzaları: `baslangic(kim, yer, ilk_cumle=True, tema=None, plan=False)` ve `prompt_idler(tok, kim, yer, tema=None, plan=False, eot=False)`. Mevcut "+Bir" hilesi korunur; plan modunda yerine "\nSorun: top" eklenir.
- `tema_destesi(rng, yer, son3)`: C tarafı için referans uygulama.

**`runtime/ornekle.h`** — gen.c ve firmware aynı kodu kullanır:
- Tekrar penceresi yalnızca gövde token'larını tutar.
- Gövdede satır sonu yasağı, plan/gövde bölme, plan uzunluk sınırı.
- Sonra kilit maskeleri eklenir.

**Firmware** (`esp32_tinystories.ino` şu an yalnızca greedy hız testi; bunlar ürün döngüsü yazılırken aynı başlık dosyasıyla gelir):
- Flash tabloları: `prompts_bas` (468 × ≤14 uint16), tema dizileri (<1 KB), seyrek hücre bit haritası.
- NVS'de tema destesi: figür grubu bit maskesi → 20 baytlık permütasyon + indeks (grup başına ~22 B). Bitince yeniden karıştırılır; son 3 tema yeni destenin başına gelmez; seyrek hücreler atlanır.
- K aday aynı istem KV'sini paylaşır: istem bir kez ileri geçirilir, her aday pos=P'den başlar ve P−1'deki son istem token'ı yeniden ileri geçirilir.
- Seslendirme yalnızca gövdeyi okur. Plan modunda gövde yoksa aday reddedilir.

## CPU takvimi
| Ne | Ne zaman | Süre |
|---|---|---|
| Etiketleme (E3) | Hemen, ajanlarla | CPU yok |
| E0 | c2ara bitince (~40 dk sonra) | 20 dk |
| E1 | E0'ın hemen ardından, ön-eğitimin yanında | ~50 dk |
| R | Ön-eğitim bitince | 45 dk |
| E2 | R'den sonra | 45 dk |
| E3 | E2'den sonra | 60 dk |
| E4 | E3'ten sonra | 45 dk |
| E5 + E6 | E4'ten sonra | 30 dk |

- Ön-eğitim sonrası toplam ~4.5 CPU saati.
- Etiketler hazır değilse E3 ile E4'ün yeri değiştirilir; birbirlerinden bağımsızlar.

## YAPILMAYACAKLAR
- **Ön-eğitimle aynı anda 4 thread'li ikinci bir ince ayar ya da üçüncü bir iş koşmak.** Ön-eğitim 3.9 s/adıma düştü ve toplam verim sıralı koşmaktan düşük. Paralel koşmak şartsa `OMP_NUM_THREADS=2` verilmeli.
- **Bir kolda birden fazla değişken değiştirmek.** Örnek: 5'in Kol B'si (filtre + birleştirme + pay + tekrar). Ayrıca seçici cezasını, ölçülen eğitim değişikliğiyle aynı kola koymak. Aksi hâlde kazanç hangi değişikliğe ait bilinemez.
- **2364 hikâyeyi iskelete yeniden yazdırmak (7) ve 2400 yeni v4 hikâyesi (8).** Yeniden yazım plan etiketlerini geçersiz kılar ve hikâyeleri tekdüzeleştirir; etkisi de ölçülmemiş. Yeni hikâye yazdırmadan önce öğrenme eğrisinin verinin sınır olduğunu göstermesi gerekir.
- **PMI yeniden sıralama (12) ve konu kilidi/geri alma (10).** Hakemli gerçek çıktılarda sinyal tutarsız (setler arasında işaret değişiyor). Cihaz süresini +%22 artırıyor ve karmaşık bir firmware durum makinesi gerektiriyor.
- **DAgger (16).** Düzeltmeyi yapan ile hakem aynı öğretmen olduğu için yanlılık var; zincir de uzun. En erken E7 olumlu çıkarsa düşünülür.
- **Eğitim hikâyelerinden türetilmiş sorun/kart kütüphanesini ya da yeniden anlatım kademesini cihazda kullanmak (6, 19).** Model eğitim hikâyesini ezberden okur. Cihaz planları eğitim dışından gelmeli (E3').
- **Satır sonu yasağını gövde başlamadan uygulamak.** Plan satırları ve "\n\n" ayırıcısı bozulur.
- **Başarıyı seçicide kullanılan NB ile ölçmek, hakeme temayı vermek ya da rubriği değiştirip tabanı yeniden hakemlememek.** Bunların her biri ölçüm aracını değiştirir.
- **Başlık maskesi (13) ve yalnız oyuncak verisiyle soğutma aşaması (5-C).** Mantığa beklenen etkisi yok; soğutma ezber riski taşıyor, ve maske plan token'larını yanlışlıkla kayıptan çıkarabilir.
- **Ara checkpoint modellerini (c2ara*) nihai modellerle karşılaştırmak ya da seyrek (yer, tema) hücrelerini destede vermek.**
- **Temp ve rep değerlerini deneyler sırasında değiştirmek.** 0.5 / 1.1 sabit kalmalı; yoksa her karşılaştırmaya ikinci bir değişken girer.