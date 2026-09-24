"""Hakemsiz olay örgüsü ölçüleri: tema tutarlılığı (token-NB, tema_sinif.py), örgü işaretleri, eğitimden kopya.

Kullanım: python degerlendirme/olay.py <hikayeler.json | adaylar_<ad>.json> [--model <model_dizini>] [--aday K]
  --model: tema_nb.json ve tokenizer.json'un olduğu dizin; adaylar dosyasında varsayılanı dosyanın dizini.
  --aday K: adaylar dosyasında vaka başına yalnız ilk K aday.
Ölçüler (yüzdeler hikâye sayısına göre):
  iki_yari_ayni_tema_%  ilk ve ikinci yarının NB teması aynı (yarılar cümle sayısına göre)
  istenen_tema_%        tam metnin NB teması istenen tema (yalnız temalı üretimde, yoksa null)
  farkli_tema           tam metinlerin NB temalarından kaç farklısı çıktı (/20); en_sik_tema: en sık olanı
  top_%                 top geçen hikâye (modelin genel geri dönüş örgüsü)
  cunku_%               'çünkü' geçen hikâye
  paragraf_%            satır sonu içeren hikâye
  kopya8_%              kelime 8-gram'larının eğitim hikâyelerinde de geçen payı (sec.kucuk ile küçültülmüş)
Plan modunda (uret.py --baslik plan; kayıtlarda 'plan' alanı varsa) ek ölçüler:
  plan_bozuk_%          gövdesi olmayan (gen plan_bozuk / Ċ Ċ yok / boş gövde) hikâye, tüm hikâyelere göre
  plan_bicim_%          planı "Sorun: S\nÇözüm: Ç" biçiminde olan (aşağıdakilerin paydası: plan_bozuk olmayanlar)
  plan_uyum_%           planın sorun içerik kelimelerinden biri gövdenin ilk %60'ında VE çözüm içerik
                        kelimelerinden biri son %60'ında geçiyor (kök = ilk 5 harf, önek eşleşmesi; kelime bölme ve
                        %60 sınırları data/oyuncak_plan/kontrol.py ile aynı; durak kelimeler, figür adları ve türleri
                        sayılmaz). Üretilen planda anahtar kelime olmadığı için etiketlerdeki anahtar kuralının
                        gevşek karşılığıdır. plan_sorun_uyum_% / plan_cozum_uyum_%: yalnız bir yarısı.
  plan_kelime           ortalama plan uzunluğu (sorun + çözüm kelimeleri, etiketler hariç)
Adaylar dosyasında üç küme raporlanır: seçicisiz (j=0), en_iyi_K (sec.puanla ile, otomatik.py gibi), tüm adaylar.
Çıktı: ekrana ve girdinin yanına: hikayeler.json -> olay.json, adaylar_<ad>.json -> olay_<ad>.json
Ölçüm aracıdır: NB seçiciye girerse (E5) bu ölçüler o seçicinin başarısını ölçmek için kullanılmaz.
"""
import argparse
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), "data", "oyuncak_plan"))
from sec import kucuk, puanla  # noqa: E402
from tema_sinif import egitim_hikayeleri, yukle  # noqa: E402
from uret import plan_bol  # noqa: E402
import kontrol  # noqa: E402  (plan etiketlerinin konum kuralı: kelime bölme, kök, %60 sınırları)

KELIME = re.compile(r"[a-zçğıöşüâîû]+")
TOP = re.compile(r"\btop(?:u|a|un|ta|tan|la|lar|ları|ların|larla|um|umu|umun|una|unu|unda|undan|uyla|umuz"
                 r"|cuk|cuğu|cuğunu|çuk|çuğu|çuğunu)?\b")


def sekizliler(metin, n=8):
    w = KELIME.findall(kucuk(metin))
    return [tuple(w[i:i + n]) for i in range(len(w) - n + 1)]


ISIM_KOK = {kontrol.kok(i) for i in kontrol.ISIM_KIMLIK}


def icerik_kokleri(cumle):
    """Plan cümlesinin içerik kelimelerinin kökleri (ilk 5 harf): durak kelimeler, figür adları ve türleri,
    yabancı adlar çıkarılır."""
    kokler = []
    for w in kontrol.kelimeler(cumle):
        k = kontrol.kok(w)
        if (w in kontrol.DURAK or k in kontrol.DURAK_KOK or k in ISIM_KOK or w in kontrol.YABANCI_K
                or any(t.match(w) for t in kontrol.TURLER.values()) or k in kokler):
            continue
        kokler.append(k)
    return kokler


def plan_uyumu(plan, metin):
    """(sorun_ok, cozum_ok) ya da plan biçimi bozuksa None. sorun_ok: sorun içerik köklerinden biri gövdenin ilk
    %60'ında; cozum_ok: çözüm içerik köklerinden biri son %60'ında (kontrol.ilk60 / kontrol.son60)."""
    p = plan_bol(plan)
    if p is None:
        return None
    ws = kontrol.kelimeler(metin)
    n = len(ws)

    def var(kokler, dilim):
        return any(dilim(i, n) and w.startswith(k) for k in kokler for i, w in enumerate(ws))
    return var(icerik_kokleri(p[0]), kontrol.ilk60), var(icerik_kokleri(p[1]), kontrol.son60)


def plan_olc(hikayeler):
    """Plan modu ölçüleri (modül belgesine bakın); hikâyelerde 'plan' alanı yoksa {}."""
    if not any("plan" in h for h in hikayeler):
        return {}
    yuz = lambda x, n: round(100 * x / n, 1) if n else None  # noqa: E731
    bozuk = sum(bool(h.get("plan_bozuk")) for h in hikayeler)
    planli = [h for h in hikayeler if "plan" in h and not h.get("plan_bozuk")]
    uyum = [plan_uyumu(h["plan"], h["metin"]) for h in planli]
    kelime = [len([w for w in h["plan"].split() if w not in ("Sorun:", "Çözüm:")]) for h in planli]
    return {
        "plan_bozuk_%": yuz(bozuk, len(hikayeler)),
        "plan_bicim_%": yuz(sum(u is not None for u in uyum), len(planli)),
        "plan_uyum_%": yuz(sum(u == (True, True) for u in uyum), len(planli)),
        "plan_sorun_uyum_%": yuz(sum(bool(u and u[0]) for u in uyum), len(planli)),
        "plan_cozum_uyum_%": yuz(sum(bool(u and u[1]) for u in uyum), len(planli)),
        "plan_kelime": round(sum(kelime) / len(kelime), 1) if kelime else None,
    }


def olc(hikayeler, nb, egitim8):
    """hikayeler: [{metin, tema?}] -> ölçüler."""
    n = max(1, len(hikayeler))
    yuz = lambda x: round(100 * x / n, 1)  # noqa: E731
    ayni = istenen = temali = kopya = sekiz = 0
    tahmin = collections.Counter()
    for h in hikayeler:
        temali += bool(h.get("tema"))
        s = sekizliler(h["metin"])
        sekiz += len(s)
        kopya += sum(x in egitim8 for x in s)
        if not h["metin"].strip():  # boş hikâye tema ölçülerinde başarısız sayılır
            continue
        tam, a, b = nb.uc_tema(h["metin"])
        tahmin[tam] += 1
        ayni += a == b
        istenen += nb.temalar[tam] == h.get("tema")
    en_sik = [f"{nb.temalar[t]} {k}/{len(hikayeler)}" for t, k in tahmin.most_common(1)]
    return {
        "n": len(hikayeler),
        "iki_yari_ayni_tema_%": yuz(ayni),
        "istenen_tema_%": round(100 * istenen / temali, 1) if temali else None,
        "farkli_tema": f"{len(tahmin)}/{len(nb.temalar)}",
        "en_sik_tema": en_sik[0] if en_sik else None,
        "top_%": yuz(sum(bool(TOP.search(kucuk(h["metin"]))) for h in hikayeler)),
        "cunku_%": yuz(sum("çünkü" in kucuk(h["metin"]) for h in hikayeler)),
        "paragraf_%": yuz(sum("\n" in h["metin"].strip() for h in hikayeler)),
        "kopya8_%": round(100 * kopya / max(1, sekiz), 2),
        **plan_olc(hikayeler),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dosya", help="uret.py'nin hikayeler.json'u ya da <model_dizini>/adaylar_<ad>.json")
    ap.add_argument("--model", default=None, help="tema_nb.json + tokenizer.json dizini")
    ap.add_argument("--aday", type=int, default=None, help="adaylar dosyasında vaka başına ilk K aday")
    a = ap.parse_args()
    veri = json.load(open(a.dosya, encoding="utf-8"))
    aday_mi = bool(veri) and "vaka" in veri[0]
    model = a.model or (os.path.dirname(os.path.abspath(a.dosya)) if aday_mi else None)
    if model is None:
        ap.error("hikayeler.json için --model <model_dizini> gerekli (tema_nb.json orada olmalı)")
    nb = yukle(model)
    egitim8 = {x for h in egitim_hikayeleri(nb.nb) for x in sekizliler(h["metin"])}
    sonuc = {"dosya": a.dosya, "model": model}
    if aday_mi:
        vakalar = {}
        for h in sorted(veri, key=lambda h: (h["vaka"], h["j"])):
            if a.aday is None or h["j"] < a.aday:
                vakalar.setdefault(h["vaka"], []).append(h)
        K = min(map(len, vakalar.values()))
        secilen = [max(v, key=lambda h: puanla(h["metin"], h["kim"], h["lp"], h["n"], h["yer"], h["bitti"]))
                   for v in vakalar.values()]
        sonuc["seçicisiz"] = olc([v[0] for v in vakalar.values()], nb, egitim8)
        sonuc[f"en_iyi_{K}"] = olc(secilen, nb, egitim8)
        sonuc["tum_adaylar"] = olc([h for v in vakalar.values() for h in v], nb, egitim8)
    else:
        sonuc["hikayeler"] = olc(veri, nb, egitim8)
    ad = os.path.basename(a.dosya)
    cikti = os.path.join(os.path.dirname(os.path.abspath(a.dosya)),
                         "olay.json" if ad == "hikayeler.json" else "olay_" + ad.removeprefix("adaylar_"))
    json.dump(sonuc, open(cikti, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
