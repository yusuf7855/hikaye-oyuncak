"""Popüler karakter hikâyelerini doğrula (karakter kartlarına göre).

Kullanım: python kontrol.py [dosya_öneki]     -> rapor
          python kontrol.py --plan            -> data/oyuncak_plan/plan_populer.jsonl
Kurallar: başlık "### <isim> | <yer> | <tema>" + "@plan: sorun | çözüm"; yer kartın yerlerinden; isim ilk 2 cümlede;
uzunluk 70–150 kelime; özel adlar yalnız kartta geçenler (başka dizinin karakteri yok); planda özel ad yok;
seçicinin olay örgüsü kuralları (degerlendirme/sec.py olay_cezalari) ve güvenlik.
oku() prepare_ft2 ile uyumlu sözlükler döndürür: turler = [isim], yer, tema, metin, sorun, cozum.
"""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "degerlendirme"))
from sec import guvenlik_cezasi, olay_cezalari  # noqa: E402

KARTLAR = {k["isim"]: k for k in json.load(open(os.path.join(HERE, "karakterler.json"), encoding="utf-8"))}
ESKI = {k["isim"] for k in json.load(open(os.path.join(HERE, "..", "karakterler.json"), encoding="utf-8"))["karakterler"]}
BASLIK = re.compile(r"^###\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$", re.M)
PLAN_SATIR = re.compile(r"^@plan:\s*(.+?)\s*\|\s*(.+?)\s*$", re.M)
HARF = "a-zçğıöşüâîû"
PLAN_BICIM = re.compile(rf"^[{HARF}]+(?:,? [{HARF}]+)*$")
BUYUK = re.compile(r"[A-ZÇĞİÖŞÜ][a-zçğıöşüA-Z]+")
UNVAN = {"Kraliçe", "Kral", "Prenses", "Prens", "Anne", "Baba", "Büyükanne", "Büyükbaba", "Dede", "Nine", "Teyze",
         "Amca", "Bay", "Bayan", "Belediye", "Başkanı", "Kaptan"}


def izinli(kart):
    """Kartın herhangi bir alanında büyük harfle geçen kelimeler (Arendelle, Anna, Olaf, Harita, ...)."""
    metin = json.dumps(kart, ensure_ascii=False)
    return set(BUYUK.findall(metin)) | UNVAN


def oku(onek=""):
    iyi, kotu = [], []
    baska_diziler = {i for i in KARTLAR}
    for yol in sorted(glob.glob(os.path.join(HERE, f"{onek}*.txt"))):
        parcalar = BASLIK.split(open(yol, encoding="utf-8").read())
        for i in range(1, len(parcalar), 4):
            isim, yer, tema, govde = (s.strip() for s in parcalar[i:i + 4])
            neden = []
            kart = KARTLAR.get(isim)
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
            h = {"dosya": os.path.basename(yol), "turler": [isim], "yer": yer.lower(), "tema": tema, "metin": govde,
                 "kelime": len(govde.split()), "sorun": sorun, "cozum": cozum}
            if not kart:
                neden.append(f"kartı olmayan karakter: {isim}")
            else:
                if h["yer"] not in kart["yerler"]:
                    neden.append(f"yer kartta yok: {yer}")
                if not 70 <= h["kelime"] <= 150:
                    neden.append(f"uzunluk {h['kelime']}")
                if govde.count('"') % 2:
                    neden.append("tırnak dengesiz")
                ilk = " ".join(re.split(r"(?<=[.!?])\s+", govde)[:2])
                if isim not in ilk:
                    neden.append(f"{isim} ilk 2 cümlede yok")
                izin = izinli(kart)
                baska = sorted(n for n in (baska_diziler | ESKI) - {isim} - izin if re.search(rf"\b{n}\b", govde))
                if baska:
                    neden.append(f"başka karakter: {', '.join(baska)}")
                bilinmeyen = set()
                for mm in BUYUK.finditer(govde):
                    once = govde[:mm.start()].rstrip()
                    if not once or once[-1] in '.!?"“”:…':
                        continue
                    if mm.group(0) not in izin and mm.group(0) != isim:
                        bilinmeyen.add(mm.group(0))
                if bilinmeyen:
                    neden.append(f"kartta olmayan isim?: {', '.join(sorted(bilinmeyen))}")
                for p in (sorun or "", cozum or ""):
                    if any(w[:1].isupper() for w in p.split()):
                        neden.append("planda özel ad")
                for _, ad in olay_cezalari(govde, [isim]):
                    if ad.startswith("uydurma karakter adı"):  # sec.py yalnız 12 eski figürü bilir: kart adları serbest
                        adlar = set(re.findall(r"'([^']+)'", ad))
                        if adlar <= izin | {isim}:
                            continue
                    neden.append(ad)
                g = guvenlik_cezasi(govde)
                if g:
                    neden.append(g[1])
            (kotu if neden else iyi).append((h, neden) if neden else h)
    return iyi, kotu


def plan_yaz():
    iyi, _ = oku()
    sira, satirlar = {}, []
    for h in iyi:
        n = sira.get(h["dosya"], 0)
        sira[h["dosya"]] = n + 1
        satirlar.append(json.dumps({"id": f"populer/{h['dosya'][:-4]}#{n}", "sorun": h["sorun"], "cozum": h["cozum"],
                                    "yok": False, "bozuk": False}, ensure_ascii=False))
    yol = os.path.join(HERE, "..", "oyuncak_plan", "plan_populer.jsonl")
    open(yol, "w", encoding="utf-8").write("\n".join(satirlar) + "\n")
    print(f"{len(satirlar)} plan -> {os.path.normpath(yol)}")


def main():
    onek = sys.argv[1] if len(sys.argv) > 1 else ""
    iyi, kotu = oku(onek)
    print(f"geçerli: {len(iyi)}   sorunlu: {len(kotu)}")
    c = collections.Counter((h["turler"][0], h["yer"]) for h in iyi)
    print(f"karakter-yer: {len(c)} kombinasyon, " + ", ".join(f"{k}: {v}" for k, v in
          sorted(collections.Counter(h['turler'][0] for h in iyi).items())))
    for h, neden in kotu[:25]:
        print(f"  SORUN {h['dosya']} [{h['turler'][0]} | {h['yer']} | {h['tema']}]: {'; '.join(neden)}")


if __name__ == "__main__":
    plan_yaz() if sys.argv[1:] == ["--plan"] else main()
