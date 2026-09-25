"""Eğitim verisini hakemle: yalnız 10/10 alan hikâyeler eğitime girer (HAKEM_VERI.md).

Kullanım: python degerlendirme/veri_hakem.py hazirla <klasör> [--onek tek_kus_2] [--parti-boyu 40] [--ad AD]
          python degerlendirme/veri_hakem.py ozet [<ad> ...]       # -> data/veri_haric.txt (10 almayanlar)
<klasör>: data/ altındaki hikâye klasörü (oyuncak_v4, oyuncak_populer); kimlikler prepare_ft2.kimlik_ver ile aynı
("v4/tek_kus_2#5", "populer/elsa_1#3"). Çıktı: degerlendirme/veri_<ad>/parti_N.json, gorev.json.
ozet bütün veri_* klasörlerindeki puanları toplar; 10'dan düşük (ya da puanı eksik) hikâyelerin kimliklerini
data/veri_haric.txt'ye yazar: ince ayarda prepare_ft2 --haric data/veri_haric.txt.
"""
import argparse, glob, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def hikayeler(klasor, onek=""):
    d = os.path.join(ROOT, "data", klasor)
    spec = importlib.util.spec_from_file_location(f"kontrol_{klasor}", os.path.join(d, "kontrol.py"))
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    iyi, _ = k.oku()   # kimlik sırası dosyanın bütün geçerlilerine göre: önek filtresi sonradan
    kartlar = {}
    yol = os.path.join(d, "karakterler.json")
    if os.path.exists(yol):
        kartlar = {c["isim"]: c for c in json.load(open(yol, encoding="utf-8"))}
    sira, out = {}, []
    for h in iyi:
        n = sira.get(h["dosya"], 0)
        sira[h["dosya"]] = n + 1
        if not h["dosya"].startswith(onek):
            continue
        kayit = {"id": f"{klasor.split('_')[-1]}/{h['dosya'][:-4]}#{n}", "metin": h["metin"]}
        if h["turler"][0] in kartlar:
            kayit["kart"] = kartlar[h["turler"][0]]
        out.append(kayit)
    return out


def hazirla(a):
    H = hikayeler(a.klasor, a.onek)
    ad = a.ad or (a.onek or a.klasor)
    d = os.path.join(HERE, f"veri_{ad}")
    os.makedirs(d, exist_ok=True)
    isler = []
    for i in range(0, len(H), a.parti_boyu):
        n = i // a.parti_boyu
        json.dump(H[i:i + a.parti_boyu], open(os.path.join(d, f"parti_{n}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        isler.append({"parti": os.path.join(d, f"parti_{n}.json"), "cikti": os.path.join(d, f"puan_{n}.json")})
    json.dump({"kural": os.path.join(HERE, "HAKEM_VERI.md"), "isler": isler}, open(os.path.join(d, "gorev.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"{len(H)} hikâye -> {d} ({len(isler)} parti)")


def ozet(a):
    klasorler = [os.path.join(HERE, f"veri_{x}") for x in a.adlar] if a.adlar else \
        sorted(p for p in glob.glob(os.path.join(HERE, "veri_*")) if os.path.isdir(p))
    haric, n, on = [], 0, 0
    for d in klasorler:
        for f in sorted(glob.glob(os.path.join(d, "parti_*.json"))):
            H = json.load(open(f, encoding="utf-8"))
            p = f.replace("parti_", "puan_")
            P = {r["id"]: r for r in json.load(open(p, encoding="utf-8"))} if os.path.exists(p) else {}
            for h in H:
                n += 1
                r = P.get(h["id"])
                if r and r.get("puan") == 10:
                    on += 1
                else:
                    haric.append(h["id"])
    open(os.path.join(ROOT, "data", "veri_haric.txt"), "w").write("\n".join(haric) + "\n")
    print(f"{n} hikâye hakemlendi: {on} tam puan (%{100 * on / max(1, n):.0f}), {len(haric)} dışarıda -> data/veri_haric.txt")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    alt = ap.add_subparsers(dest="komut", required=True)
    h = alt.add_parser("hazirla")
    h.add_argument("klasor")
    h.add_argument("--onek", default="")
    h.add_argument("--parti-boyu", type=int, default=40)
    h.add_argument("--ad", default=None)
    o = alt.add_parser("ozet")
    o.add_argument("adlar", nargs="*")
    a = ap.parse_args()
    hazirla(a) if a.komut == "hazirla" else ozet(a)
