"""v4 oyuncak hikâyelerini doğrula (v3 kontrolleri + plan satırı + seçicinin olay örgüsü kuralları + güvenlik).

v4 biçimi: başlık satırının altında "@plan: <sorun> | <çözüm>" satırı. oku() planı metinden ayırır; geçerli
hikâyelerde h["sorun"], h["cozum"] alanları olur. plan_yaz(): data/oyuncak_plan/plan_v4.jsonl (prepare_ft2 --plan
biçimi; kimlikler prepare_ft2.kimlik_ver ile aynı: "v4/<dosya>#<geçerliler arasındaki sıra>").

Kullanım: python kontrol.py [dosya_öneki]   -> rapor (önek verilirse sadece o dosyalar, örn. "tavsan_")
"""
import collections, glob, json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "degerlendirme"))
from sec import guvenlik_cezasi, olay_cezalari  # noqa: E402

HARF = "a-zçğıöşüâîû"
PLAN_BICIM = re.compile(rf"^[{HARF}]+(?:,? [{HARF}]+)*$")
PLAN_SATIR = re.compile(r"^@plan:\s*(.+?)\s*\|\s*(.+?)\s*$", re.M)

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
            neden = []
            m = PLAN_SATIR.search(govde)
            sorun = cozum = None
            if m and govde.startswith("@plan"):
                sorun, cozum = m.group(1), m.group(2)
                govde = govde[m.end():].strip()
                for p in (sorun, cozum):
                    if not PLAN_BICIM.match(p) or not 3 <= len(p.split()) <= 9:
                        neden.append(f"plan biçimi: {p[:40]}")
            else:
                neden.append("plan satırı yok")
            h = {"dosya": os.path.basename(yol), "turler": turler, "yer": y, "tema": t, "metin": govde,
                 "kelime": len(govde.split()), "sorun": sorun, "cozum": cozum}
            if not 1 <= len(turler) <= 2 or any(x not in ISIM for x in turler):
                neden.append(f"tür? {k}")
            if y not in YER:
                neden.append(f"yer? {y}")
            if not 70 <= h["kelime"] <= 150:
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
            for x in turler:
                n = ISIM.get(x)
                if n and re.search(rf"\b{n}\b,?\s+{n}['’]", govde):
                    neden.append(f"kendine gönderme ({n}, {n}'...)")
            if re.search(r'(kabuk|taş|top|ağaç|çiçek)\w*,?\s+"', govde) or re.search(r'"\s*(?:dedi|diye sordu)\s+(?:kabuk|taş|top|ağaç|çiçek)', govde):
                neden.append("konuşan nesne?")
            isimler = [ISIM[x] for x in turler if x in ISIM]
            for _, ad in olay_cezalari(govde, isimler):
                neden.append(ad)
            g = guvenlik_cezasi(govde)
            if g:
                neden.append(g[1])
            yab = yabanci_isimler(govde)
            if yab:
                neden.append(f"uydurma isim?: {', '.join(sorted(yab))}")
            (kotu if neden else iyi).append((h, neden) if neden else h)
    return iyi, kotu


def plan_yaz():
    """Geçerli v4 hikâyelerinin planları -> data/oyuncak_plan/plan_v4.jsonl."""
    iyi, _ = oku()
    sira, satirlar = {}, []
    for h in iyi:
        n = sira.get(h["dosya"], 0)
        sira[h["dosya"]] = n + 1
        satirlar.append(json.dumps({"id": f"v4/{h['dosya'][:-4]}#{n}", "sorun": h["sorun"], "cozum": h["cozum"],
                                    "yok": False, "bozuk": False}, ensure_ascii=False))
    yol = os.path.join(HERE, "..", "oyuncak_plan", "plan_v4.jsonl")
    open(yol, "w", encoding="utf-8").write("\n".join(satirlar) + "\n")
    print(f"{len(satirlar)} plan -> {os.path.normpath(yol)}")


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
    if sys.argv[1:] == ["--plan"]:
        plan_yaz()
    else:
        main()
