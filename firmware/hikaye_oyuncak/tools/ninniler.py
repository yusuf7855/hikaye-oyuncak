"""ninniler.txt -> yerlesik.h (Ay Dede'nin sabit ninnileri) ve biçim denetimi.

    python firmware/hikaye_oyuncak/tools/ninniler.py           # yerlesik.h'yi yeniden yazar
    python firmware/hikaye_oyuncak/tools/ninniler.py --denetle # yalnız denetler (yerlesik.h güncel mi)

Her dörtlüğün iki dizesi bir cümle olur (ses okurken cümle aralarında ninni modunun uzun sessizliği girer);
dize sonlarındaki virgül kısa duraktır.
"""
import os
import re
import sys

SKETCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(SKETCH, "ninniler.txt")
HEDEF = os.path.join(SKETCH, "yerlesik.h")
SESLI = set("aeıioöuüâîûAEIİOÖUÜÂÎÛ")
ADET = 15


def hece(dize):
    """Kaba hece sayısı (ünlü sayısı); uzatılmış "eee" tek hece sayılır."""
    return sum(c in SESLI for c in re.sub(r"([eE])e+", r"\1", dize))


def oku(yol=KAYNAK):
    """[(ad, [[dize, ...], ...]), ...]: ninni adı ve kıtaları."""
    ninniler = []
    for satir in open(yol, encoding="utf-8").read().split("\n"):
        s = satir.strip()
        if s.startswith("## "):
            ninniler.append((s[3:].strip(), [[]]))
        elif s.startswith("#") or not ninniler:
            continue
        elif not s:
            if ninniler[-1][1][-1]:
                ninniler[-1][1].append([])
        else:
            ninniler[-1][1][-1].append(s)
    return [(ad, [d for d in dortlukler if d]) for ad, dortlukler in ninniler]


def denetle(ninniler):
    """Halk ninnileri serbest kalıplıdır: kıta 1-6 dize, dize 3-13 hece; dize virgülle, kıta noktayla biter."""
    hatalar = []
    if len(ninniler) != ADET:
        hatalar.append(f"{len(ninniler)} ninni var, {ADET} olmalı")
    for ad, kitalar in ninniler:
        if not kitalar:
            hatalar.append(f"{ad}: boş")
        for d in kitalar:
            if not 1 <= len(d) <= 6:
                hatalar.append(f"{ad}: kıta {len(d)} dize: {d[0]}")
            for dize in d[:-1]:
                if not dize.endswith(","):
                    hatalar.append(f"{ad}: dize virgülle bitmeli: {dize}")
            for dize in d:
                if not 3 <= hece(dize) <= 13:
                    hatalar.append(f"{ad}: {hece(dize)} hece: {dize}")
            if not d[-1].endswith("."):
                hatalar.append(f"{ad}: kıta noktayla bitmeli: {d[-1]}")
    return hatalar


OZEL = ("Ay Dede",)  # cümle içinde de büyük harfle başlar


def kucuk(c):
    return {"I": "ı", "İ": "i"}.get(c, c.lower())


def metin(dortlukler):
    """Kıtaları kartın okuyacağı tek metne çevirir: her iki dize bir cümle."""
    cumleler = []
    for d in dortlukler:
        for i in range(0, len(d), 2):
            cift = list(d[i:i + 2])
            if len(cift) == 2 and not cift[1].startswith(OZEL):
                cift[1] = kucuk(cift[1][0]) + cift[1][1:]
            cumleler.append(" ".join(cift).rstrip(",.") + ".")
    return " ".join(cumleler)


def c_dizge(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def baslik(ninniler):
    out = [
        "// Üretildi: tools/ninniler.py (ninniler.txt). Elle değiştirme; ninniler.txt'yi düzenleyip aracı çalıştır.",
        "// Yerleşik metinler: kartta sabit duran, modelin yazmadığı içerik. Gece figürü (Ay Dede, mod \"uyku\") yalnız",
        "// bu ninnileri okur (ürün sahibinin kararı, 15 Ekim 2026: 15 sabit, bilinen anonim halk ninnisi); sırayla döner, aynı",
        "// ninni art arda gelmez. Ninni modunda yavaş, alçak, kısık okunur; her iki dize bir cümle (arada uzun durak).",
        "#pragma once",
        "",
        "static const char *const NINNILER[] = {",
    ]
    for ad, dortlukler in ninniler:
        out.append(f"    // {ad}")
        m = metin(dortlukler)
        parca, satir = [], ""
        for sozcuk in m.split(" "):
            if satir and len(satir) + len(sozcuk) > 100:
                parca.append(satir)
                satir = ""
            satir += sozcuk + " "
        parca.append(satir.rstrip())
        for i, p in enumerate(parca):
            out.append("    " + c_dizge(p) + ("," if i == len(parca) - 1 else ""))
    out += [
        "};",
        "",
        "typedef struct {",
        "  const char *kimlik;              // DONANIM_KIMLIK",
        "  const char *const *metin;",
        "  int n;",
        "} YerlesikListe;",
        "",
        "static const YerlesikListe YERLESIK[] = {",
        "    {\"gece\", NINNILER, (int)(sizeof NINNILER / sizeof NINNILER[0])},",
        "};",
        "",
    ]
    return "\n".join(out)


def main():
    ninniler = oku()
    hatalar = denetle(ninniler)
    for h in hatalar:
        print("HATA:", h)
    if hatalar:
        sys.exit(1)
    yeni = baslik(ninniler)
    if "--denetle" in sys.argv:
        eski = open(HEDEF, encoding="utf-8").read() if os.path.exists(HEDEF) else ""
        if eski != yeni:
            print("yerlesik.h güncel değil: python firmware/hikaye_oyuncak/tools/ninniler.py")
            sys.exit(1)
        print(f"{len(ninniler)} ninni, yerlesik.h güncel")
        return
    with open(HEDEF, "w", encoding="utf-8") as f:
        f.write(yeni)
    print(f"yerlesik.h: {len(ninniler)} ninni, {sum(len(metin(d)) for _, d in ninniler)} bayt metin")


if __name__ == "__main__":
    main()
