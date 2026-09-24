"""Kör ikili tercih: iki kolun aynı vakadaki hikâyelerini sırası gizli çiftler olarak hakeme hazırla, kararları topla.

Kullanım: python degerlendirme/ikili.py hazirla <adA> <adB> [--parti 3] [--hakem 1] [--tohum 17]
          python degerlendirme/ikili.py ozet <adA> <adB> [--ayrinti] [--json]
Girdi : degerlendirme/<ad>/hikayeler.json (id ile eşlenir; yalnız 'metin' hakeme gider: tema, başlık, plan gitmez)
Çıktı : degerlendirme/ikili_<adA>__<adB>/parti_N.json  [{id, A, B}]  (A/B sırası vaka başına rastgele, dengeli)
        gorev.json  hakem işleri: IKILI.md + parti_N.json -> karar_N.json (ikinci hakem karar_N_b.json)
        anahtar.json  gizli (hakeme verilmez): her vakada A ve B konumundaki kol
ozet  : adA'nın puanı /n (eşit = yarım; birden çok hakemde vaka başına ortalama), tek yönlü kesin binom p
        (H1: adA > adB) ve plandaki bant: Kazandı ≥ 24/36, Eşit 15–23, Kaybetti ≤ 14 (n ≠ 36 ise oranla).
Metni iki kolda aynı olan vakalar hakeme gitmez ve n'den düşülür (E5: yalnız seçimin değiştiği vakalar).
"""
import argparse, glob, json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sec import kucuk  # noqa: E402

EKLER = ["", "_b", "_c", "_d"]  # hakem sırası -> dosya eki (karar_N.json, karar_N_b.json, ...)


def oku(kok, ad):
    return {h["id"]: h for h in json.load(open(os.path.join(kok, ad, "hikayeler.json"), encoding="utf-8"))}


def klasor(kok, a, b):
    return os.path.join(os.path.abspath(kok), f"ikili_{a}__{b}")


def yaz(yol, veri):
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=1)


def hazirla(a):
    ha, hb = oku(a.kok, a.adA), oku(a.kok, a.adB)
    ortak = sorted(set(ha) & set(hb))
    if set(ha) ^ set(hb):
        print(f"uyarı: yalnız bir kolda olan vakalar atlandı: {sorted(set(ha) ^ set(hb))}", file=sys.stderr)
    ayni = [i for i in ortak if ha[i]["metin"].strip() == hb[i]["metin"].strip()]
    vakalar = [i for i in ortak if i not in ayni]
    if not vakalar:
        sys.exit("hakeme gidecek vaka yok (bütün metinler aynı)")
    d = klasor(a.kok, a.adA, a.adB)
    if glob.glob(os.path.join(d, "karar_*.json")) and not a.zorla:
        sys.exit(f"{d} içinde karar dosyaları var; yeniden hazırlamak için --zorla")
    rng = random.Random(a.tohum)
    ters = [k < len(vakalar) // 2 for k in range(len(vakalar))]  # yarısında adB A konumunda: konum yanlılığı dengelenir
    rng.shuffle(ters)
    sira = [{"id": i, "A": a.adB if t else a.adA, "B": a.adA if t else a.adB} for i, t in zip(vakalar, ters)]
    hik = {a.adA: ha, a.adB: hb}
    os.makedirs(d, exist_ok=True)
    p = min(a.parti, len(sira))
    isler = []
    for k in range(p):
        yaz(os.path.join(d, f"parti_{k}.json"),
            [{"id": s["id"], "A": hik[s["A"]][s["id"]]["metin"], "B": hik[s["B"]][s["id"]]["metin"]}
             for s in sira[k::p]])
        isler += [{"parti": os.path.join(d, f"parti_{k}.json"), "cikti": os.path.join(d, f"karar_{k}{e}.json")}
                  for e in EKLER[:a.hakem]]
    yaz(os.path.join(d, "anahtar.json"), {"adA": a.adA, "adB": a.adB, "tohum": a.tohum, "sira": sira, "ayni": ayni})
    yaz(os.path.join(d, "gorev.json"), {"kural": os.path.join(HERE, "IKILI.md"), "isler": isler})
    print(f"{len(sira)} vaka ({len(ayni)} aynı metin hariç) -> {d}/parti_0..{p - 1}.json, gorev.json, "
          "anahtar.json (gizli)")
    for i in isler:
        print(f"  hakem: IKILI.md + {os.path.basename(i['parti'])} -> {os.path.basename(i['cikti'])}")


def normal(karar):
    k = kucuk(str(karar).strip().strip("\"'")).replace("ş", "s").replace("ı", "i")
    return {"a": "A", "b": "B", "esit": "esit", "=": "esit"}.get(k)


def ust_kuyruk(k, n):
    """P(X ≥ k), X ~ Binom(n, 1/2)."""
    return sum(math.comb(n, j) for j in range(max(0, k), n + 1)) / 2 ** n


def bant(s, n):
    if s >= 24 * n / 36 - 1e-9:
        return "Kazandı"
    return "Kaybetti" if s <= 14 * n / 36 + 1e-9 else "Eşit"


def ozet(a):
    d = klasor(a.kok, a.adA, a.adB)
    if not os.path.exists(os.path.join(d, "anahtar.json")):
        sys.exit(f"{d}/anahtar.json yok: önce 'hazirla {a.adA} {a.adB}' (sıra önemli)")
    anahtar = json.load(open(os.path.join(d, "anahtar.json"), encoding="utf-8"))
    if (anahtar["adA"], anahtar["adB"]) != (a.adA, a.adB):
        sys.exit(f"anahtar {anahtar['adA']}/{anahtar['adB']} için hazırlanmış")
    sira = {s["id"]: s for s in anahtar["sira"]}
    kararlar, konum = {}, {"A": 0, "B": 0, "esit": 0}
    for f in sorted(glob.glob(os.path.join(d, "karar_*.json"))):
        dosya = {}  # aynı dosyada bir vaka iki kez yazılmışsa sonuncusu sayılır
        for k in json.load(open(f, encoding="utf-8")):
            i = k.get("id")
            dosya[int(i) if str(i).strip().isdigit() else i] = k
        for i, k in dosya.items():
            karar = normal(k.get("karar"))
            if i not in sira or karar is None:
                print(f"uyarı: {os.path.basename(f)} geçersiz kayıt atlandı: {k}", file=sys.stderr)
                continue
            konum[karar] += 1
            kazanan = "esit" if karar == "esit" else sira[i][karar]
            puan = 0.5 if karar == "esit" else float(kazanan == a.adA)
            kararlar.setdefault(i, []).append({"puan": puan, "kazanan": kazanan, "neden": k.get("neden", ""),
                                               "dosya": os.path.basename(f)})
    if not kararlar:
        sys.exit("karar yok")
    eksik = sorted(set(sira) - set(kararlar))
    if eksik:
        print(f"uyarı: kararı olmayan vakalar n'den düşüldü: {eksik}", file=sys.stderr)
    n = len(kararlar)
    ort = {i: sum(k["puan"] for k in ks) / len(ks) for i, ks in kararlar.items()}
    s = sum(ort.values())
    kaz, kay = sum(v > 0.5 for v in ort.values()), sum(v < 0.5 for v in ort.values())
    cok = [ks for ks in kararlar.values() if len(ks) > 1]
    sonuc = {"adA": a.adA, "adB": a.adB, "n": n, "puan": s, "puan_B": n - s, "kazandi": kaz, "kaybetti": kay,
             "esit": n - kaz - kay, "p": ust_kuyruk(math.floor(s + 1e-9), n),
             "p_isaret": ust_kuyruk(kaz, kaz + kay), "bant": bant(s, n), "ayni_metin": len(anahtar["ayni"]),
             "konum": konum, "hakem_uyumu": (sum(len({k["kazanan"] for k in ks}) == 1 for ks in cok) / len(cok)
                                             if cok else None)}
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False))
        return
    print(f"{a.adA} vs {a.adB}: {a.adA} {s:g}/{n} (%{100 * s / n:.0f}; {a.adB} {n - s:g})  "
          f"kazandı {kaz}, eşit {n - kaz - kay}, kaybetti {kay}  aynı metin (hariç): {len(anahtar['ayni'])}")
    esik = "" if n == 36 else f"  (n={n} eşikleri: ≥{24 * n / 36:.1f} / ≤{14 * n / 36:.1f})"
    print(f"  tek yönlü binom p({a.adA} > {a.adB}) = {sonuc['p']:.4f} (eşit yarım; puan aşağı yuvarlanır)  "
          f"işaret testi (eşitler hariç) p = {sonuc['p_isaret']:.4f}")
    print(f"  bant: {sonuc['bant']}{esik}  [tam karar için 'mantiksiz' ve bekçiler ayrıca bakılır]")
    print(f"  konum: A seçildi {konum['A']}, B {konum['B']}, eşit {konum['esit']}"
          + (f"  hakem uyumu %{100 * sonuc['hakem_uyumu']:.0f} ({len(cok)} vaka)" if cok else ""))
    if a.ayrinti:
        for i in sorted(kararlar):
            for k in kararlar[i]:
                print(f"  {i:>3} {k['kazanan']:<20} {k['neden']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    alt = ap.add_subparsers(dest="komut", required=True)
    for ad in ("hazirla", "ozet"):
        p = alt.add_parser(ad)
        p.add_argument("adA")
        p.add_argument("adB")
        p.add_argument("--kok", default=HERE, help="kolların klasörlerini içeren dizin (varsayılan: degerlendirme/)")
    alt.choices["hazirla"].add_argument("--parti", type=int, default=3)
    alt.choices["hazirla"].add_argument("--hakem", type=int, default=1, choices=range(1, len(EKLER) + 1))
    alt.choices["hazirla"].add_argument("--tohum", type=int, default=17)
    alt.choices["hazirla"].add_argument("--zorla", action="store_true", help="karar dosyaları varken yeniden hazırla")
    alt.choices["ozet"].add_argument("--ayrinti", action="store_true", help="vaka başına kazanan ve neden")
    alt.choices["ozet"].add_argument("--json", action="store_true")
    a = ap.parse_args()
    {"hazirla": hazirla, "ozet": ozet}[a.komut](a)


if __name__ == "__main__":
    main()
