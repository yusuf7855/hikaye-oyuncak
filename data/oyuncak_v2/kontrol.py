"""v2 oyuncak hikâyelerini doğrula.

Kullanım: python kontrol.py [dosya_öneki]   -> rapor (önek verilirse sadece o dosyalar, örn. "tavsan_")
"""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KATALOG = json.load(open(os.path.join(HERE, "..", "karakterler.json"), encoding="utf-8"))
ISIM = {k["tur"]: k["isim"] for k in KATALOG["karakterler"]}
YER = {y["ad"] for y in KATALOG["yerler"]}
ASCII = {"sato": "şato", "dag": "dağ"}
BASLIK = re.compile(r"^###\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$", re.M)
TUM_ISIMLER = set(ISIM.values())


def yabanci_isimler(metin):
    """Cümle başı olmayan büyük harfli kelimelerden figür ismi olmayanlar (uydurma isim şüphesi)."""
    sus = set()
    for m in re.finditer(r"(\S*?)([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)(?:['’][a-zçğıöşü]+)?", metin):
        onceki = metin[:m.start(2)].rstrip()
        if not onceki or onceki[-1] in '.!?"“”:…' or m.group(1).endswith(('"', "“")):
            continue
        if m.group(2) not in TUM_ISIMLER:
            sus.add(m.group(2))
    return sus


def oku(onek=""):
    iyi, kotu = [], []
    for yol in sorted(glob.glob(os.path.join(HERE, f"{onek}*.txt"))):
        parcalar = BASLIK.split(open(yol, encoding="utf-8").read())
        for i in range(1, len(parcalar), 4):
            k, y, t, govde = (s.strip() for s in parcalar[i:i + 4])
            turler = [x.strip().lower() for x in k.split(",")]
            y = ASCII.get(y.lower(), y.lower())
            h = {"dosya": os.path.basename(yol), "turler": turler, "yer": y, "tema": t, "metin": govde,
                 "kelime": len(govde.split())}
            neden = []
            if not 1 <= len(turler) <= 2 or any(x not in ISIM for x in turler):
                neden.append(f"tür? {k}")
            if y not in YER:
                neden.append(f"yer? {y}")
            if not 85 <= h["kelime"] <= 170:
                neden.append(f"uzunluk {h['kelime']}")
            if govde.count('"') % 2:
                neden.append("tırnak dengesiz")
            if "###" in govde:
                neden.append("biçim artığı")
            ilk = " ".join(re.split(r"(?<=[.!?])\s+", govde)[:2])
            for x in turler:
                if x in ISIM and ISIM[x] not in ilk:
                    neden.append(f"{ISIM[x]} ilk 2 cümlede yok")
            baska = {n for n in TUM_ISIMLER if re.search(rf"\b{n}\b", govde)} - {ISIM.get(x) for x in turler}
            if baska:
                neden.append(f"başlıkta olmayan figür: {', '.join(sorted(baska))}")
            yab = yabanci_isimler(govde)
            if yab:
                neden.append(f"uydurma isim?: {', '.join(sorted(yab))}")
            (kotu if neden else iyi).append((h, neden) if neden else h)
    return iyi, kotu


def main():
    onek = sys.argv[1] if len(sys.argv) > 1 else ""
    iyi, kotu = oku(onek)
    print(f"geçerli: {len(iyi)}   sorunlu: {len(kotu)}")
    tek = collections.Counter((h["turler"][0], h["yer"]) for h in iyi if len(h["turler"]) == 1)
    cift = collections.Counter(tuple(sorted(h["turler"])) for h in iyi if len(h["turler"]) == 2)
    print(f"tek figür: {sum(tek.values())} hikâye, {len(tek)}/72 kombinasyon | "
          f"iki figür: {sum(cift.values())} hikâye, {len(cift)}/66 ikili")
    if iyi:
        k = sorted(h["kelime"] for h in iyi)
        print(f"kelime: medyan {k[len(k) // 2]}, min {k[0]}, max {k[-1]}")
    for h, neden in kotu[:25]:
        print(f"  SORUN {h['dosya']} [{', '.join(h['turler'])} | {h['tema']}]: {'; '.join(neden)}")


if __name__ == "__main__":
    main()
