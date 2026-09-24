"""Rubrik hakemleri: hikâyeleri partilere böl; puanları (iki hakem, s1–s3, 'mantiksiz') topla.

Kullanım: python degerlendirme/hakem.py hazirla <ad> [--parti 3] [--hakem 2]
          python degerlendirme/hakem.py ozet <ad> [<ad> ...] [--json]
hazirla: degerlendirme/<ad>/hikayeler.json -> parti_N.json [{id, figurler, yer, baslik, metin, token}]
         (tema, plan ve başlıktaki Tema/Sorun satırı çıkarılır: hakem temayı görmez; eski başlıkta çıktı aynıdır)
         gorev.json: RUBRIK.md + parti_N.json -> puan_N.json (1. hakem), puan_N_b.json (2. bağımsız hakem)
ozet   : vaka başına hakem ortalaması üstünden ortalama puan, s1/s2/s3 oranları, 'mantiksiz' (alan: olay/hikâye;
         kategori: vaka sayısı, eski puanlarla karşılaştırılabilir), iki hakem varsa uyum. ozet.py aynı dosyaları okur.
"""
import argparse, collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EKLER = ["", "_b", "_c", "_d"]  # hakem sırası -> dosya eki (puan_N.json, puan_N_b.json, ...)
ALANLAR = ("id", "figurler", "yer", "baslik", "metin", "token")  # hakeme giden alanlar (eski parti biçimi)


def hazirla(a):
    d = os.path.join(os.path.abspath(a.kok), a.ad)  # gorev.json'daki yollar mutlak olsun
    hik = sorted(json.load(open(os.path.join(d, "hikayeler.json"), encoding="utf-8")), key=lambda h: h["id"])
    if glob.glob(os.path.join(d, "puan_*.json")) and not a.zorla:
        sys.exit(f"{d} içinde puan dosyaları var; yeni rubrikle yeniden hakemlemek için hikayeler.json'u yeni bir "
                 "klasöre kopyalayın (ya da --zorla: yalnız partiler yeniden yazılır)")
    for h in hik:
        if "baslik" in h:  # "Karakter: X | Yer: Y | Tema: T\nSorun: ..." -> "Karakter: X | Yer: Y"
            h["baslik"] = h["baslik"].split("\n")[0].split(" | Tema:")[0]
    p = min(a.parti, len(hik))
    isler = []
    for k in range(p):
        with open(os.path.join(d, f"parti_{k}.json"), "w", encoding="utf-8") as f:
            json.dump([{x: h[x] for x in ALANLAR if x in h} for h in hik[k::p]], f, ensure_ascii=False, indent=1)
        isler += [{"parti": os.path.join(d, f"parti_{k}.json"), "cikti": os.path.join(d, f"puan_{k}{e}.json")}
                  for e in EKLER[:a.hakem]]
    with open(os.path.join(d, "gorev.json"), "w", encoding="utf-8") as f:
        json.dump({"kural": os.path.join(HERE, "RUBRIK.md"), "isler": isler}, f, ensure_ascii=False, indent=1)
    print(f"{len(hik)} hikâye -> {d}/parti_0..{p - 1}.json, gorev.json")
    for i in isler:
        print(f"  hakem: RUBRIK.md + {os.path.basename(i['parti'])} -> {os.path.basename(i['cikti'])}")


def puanlar(d):
    """{hakem eki: {id: kayıt}}; puan_N.json -> "a", puan_N_b.json -> "b"."""
    setler = {}
    for f in sorted(glob.glob(os.path.join(d, "puan_*.json"))):
        m = re.fullmatch(r"puan_\d+(?:_(\w+))?\.json", os.path.basename(f))
        if m:
            for p in json.load(open(f, encoding="utf-8")):
                setler.setdefault(m.group(1) or "a", {})[p["id"]] = p
    return setler


def ort(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else None


def vaka_ort(kayitlar, al):
    """Vaka başına hakem ortalaması, sonra vakalar üstünden ortalama (alanı olanlarla) -> (ortalama, vaka sayısı)."""
    v = [ort(al(p) for p in ps if al(p) is not None) for ps in kayitlar.values()]
    v = [x for x in v if x is not None]
    return ort(v), len(v)


def ozet(ad, kok):
    d = os.path.join(kok, ad)
    hik = {h["id"]: h for h in json.load(open(os.path.join(d, "hikayeler.json"), encoding="utf-8"))}
    setler = puanlar(d)
    kayitlar = collections.defaultdict(list)
    for s in setler.values():
        for i, p in s.items():
            kayitlar[i].append(p)
    if set(kayitlar) - set(hik):
        fazla = sorted(set(kayitlar) - set(hik))
        print(f"uyarı: {ad}: hikayeler.json'da olmayan id'ler atlandı: {fazla}", file=sys.stderr)
        kayitlar = {i: ps for i, ps in kayitlar.items() if i in hik}
    if not kayitlar:
        return None
    for e, s in setler.items():
        if set(s) != set(kayitlar):
            print(f"uyarı: {ad}: hakem {e} {len(set(kayitlar) - set(s))} vakayı puanlamamış", file=sys.stderr)
    v = {i: ort(p["puan"] for p in ps) for i, ps in kayitlar.items()}
    tek = [x for i, x in v.items() if len(hik[i]["figurler"]) == 1]
    cift = [x for i, x in v.items() if len(hik[i]["figurler"]) == 2]
    alan = lambda k: lambda p: float(p[k]) if isinstance(p.get(k), (bool, int, float)) else None  # noqa: E731
    kusur = collections.Counter()
    for ps in kayitlar.values():
        for p in ps:
            kusur.update({k: 1 / len(ps) for k in set(p.get("kategoriler", []))})
    o = {"ad": ad, "n": len(v), "toplam": len(hik), "puan": ort(v.values()), "tek": ort(tek), "ikili": ort(cift),
         "on": sum(x >= 9.5 for x in v.values()), "bes_alti": sum(x <= 5 for x in v.values()),
         "hakemler": {e: ort(p["puan"] for p in s.values()) for e, s in sorted(setler.items())},
         "mantiksiz_vaka": kusur["mantiksiz"], "kusurlar": dict(kusur.most_common())}
    for k in ("s1", "s2", "s3", "mantiksiz"):
        o[k], o[k + "_n"] = vaka_ort(kayitlar, alan(k))
    if len(setler) > 1:  # hakem uyumu: iki hakemin de puanladığı vakalarda
        ikili = [ps[:2] for ps in kayitlar.values() if len(ps) > 1]
        o["uyum"] = {"puan_fark": ort(abs(a["puan"] - b["puan"]) for a, b in ikili), "n": len(ikili)}
        for k in ("s1", "s2", "s3", "mantiksiz"):
            c = [(a[k], b[k]) for a, b in ikili if k in a and k in b]
            o["uyum"][k] = ort((x == y) if k != "mantiksiz" else abs(x - y) for x, y in c)
    return o


def yazdir(o):
    hk = "  hakem " + ", ".join(f"{e} {x:.2f}" for e, x in o["hakemler"].items()) if len(o["hakemler"]) > 1 else ""
    print(f"{o['ad']}: ORTALAMA {o['puan']:.2f}/10  (tek {o['tek'] or 0:.2f}, ikili {o['ikili'] or 0:.2f})  "
          f"n={o['n']}/{o['toplam']}  10'luk: {o['on']}  ≤5: {o['bes_alti']}{hk}")
    s = "  ".join(f"{k.upper()} %{100 * o[k]:.0f}" for k in ("s1", "s2", "s3") if o[k] is not None)
    print(f"  olay örgüsü: {s + '  (n=' + str(o['s1_n']) + ')' if s else 'yok (eski rubrik)'}  mantiksiz: "
          + (f"{o['mantiksiz']:.2f} olay/hikâye, " if o["mantiksiz"] is not None else "")
          + f"{o['mantiksiz_vaka']:g}/{o['n']} vaka (kategori)")
    print("  en sık kusurlar (vaka, hakem ort.):", ", ".join(f"{k} {x:g}" for k, x in list(o["kusurlar"].items())[:8]))
    if "uyum" in o:
        u = o["uyum"]
        print(f"  hakem uyumu ({u['n']} vaka): puan |Δ| {u['puan_fark']:.2f}  "
              + "  ".join(f"{k.upper()} %{100 * u[k]:.0f}" for k in ("s1", "s2", "s3") if u[k] is not None)
              + (f"  mantiksiz |Δ| {u['mantiksiz']:.2f}" if u["mantiksiz"] is not None else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    alt = ap.add_subparsers(dest="komut", required=True)
    h = alt.add_parser("hazirla")
    h.add_argument("ad")
    h.add_argument("--parti", type=int, default=3)
    h.add_argument("--hakem", type=int, default=2, choices=range(1, len(EKLER) + 1))
    h.add_argument("--zorla", action="store_true", help="puan dosyaları varken partileri yeniden yaz")
    z = alt.add_parser("ozet")
    z.add_argument("ad", nargs="+")
    z.add_argument("--json", action="store_true")
    for p in (h, z):
        p.add_argument("--kok", default=HERE, help="kolların klasörlerini içeren dizin (varsayılan: degerlendirme/)")
    a = ap.parse_args()
    if a.komut == "hazirla":
        return hazirla(a)
    for ad in a.ad:
        o = ozet(ad, a.kok)
        if o is None:
            print(f"{ad}: puan yok", file=sys.stderr)
        elif a.json:
            print(json.dumps(o, ensure_ascii=False))
        else:
            yazdir(o)


if __name__ == "__main__":
    main()
