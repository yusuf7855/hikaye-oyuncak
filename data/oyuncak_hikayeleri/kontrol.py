"""Oyuncak hikâyelerini doğrula ve eğitim metnine çevir.

Kullanım: python kontrol.py            -> rapor
          python kontrol.py --yaz      -> geçerli hikâyeleri oyuncak.txt'ye yaz (<|endoftext|> ayraçlı)
"""
import collections, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KARAKTER = {"tavşan", "kedi", "ayı", "köpek", "ejderha", "kız", "oğlan", "kuş"}
YER = {"orman", "deniz", "ev", "park", "şato", "dağ"}
BASLIK = re.compile(r"^###\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$", re.M)


def oku():
    hikayeler, sorunlar = [], []
    for yol in sorted(glob.glob(os.path.join(HERE, "*_*.txt"))):
        metin = open(yol, encoding="utf-8").read()
        parcalar = BASLIK.split(metin)
        dosya = os.path.basename(yol)
        for i in range(1, len(parcalar), 4):
            k, y, t, govde = (s.strip() for s in parcalar[i:i + 4])
            govde = govde.strip()
            kelime = len(govde.split())
            y = {"sato": "şato", "dag": "dağ", "kopek": "köpek"}.get(y.lower(), y)
            k = {"tavsan": "tavşan", "ayi": "ayı", "kopek": "köpek", "kiz": "kız", "oglan": "oğlan", "kus": "kuş"}.get(k.lower(), k)
            h = {"dosya": dosya, "karakter": k.lower(), "yer": y.lower(), "tema": t, "metin": govde, "kelime": kelime}
            neden = []
            if h["karakter"] not in KARAKTER: neden.append(f"karakter? {k}")
            if h["yer"] not in YER: neden.append(f"yer? {y}")
            if not 90 <= kelime <= 280: neden.append(f"uzunluk {kelime}")
            if govde.count('"') % 2: neden.append("tırnak dengesiz")
            if re.search(r"[a-zA-Z]{3,}\s*\|", govde) or "###" in govde: neden.append("biçim artığı")
            (sorunlar.append((h, neden)) if neden else hikayeler.append(h))
    return hikayeler, sorunlar


def main():
    hikayeler, sorunlar = oku()
    print(f"geçerli: {len(hikayeler)}   sorunlu: {len(sorunlar)}")
    kombi = collections.Counter((h["karakter"], h["yer"]) for h in hikayeler)
    print(f"kombinasyon: {len(kombi)}/48   hikâye/kombinasyon min-max: "
          f"{min(kombi.values(), default=0)}-{max(kombi.values(), default=0)}")
    if hikayeler:
        k = sorted(h["kelime"] for h in hikayeler)
        print(f"kelime: medyan {k[len(k) // 2]}, min {k[0]}, max {k[-1]}")
    acilis = collections.Counter(" ".join(h["metin"].split()[:2]) for h in hikayeler)
    print("en sık açılışlar:", acilis.most_common(5))
    ilk = collections.Counter(h["metin"][:60] for h in hikayeler)
    tekrar = sum(c - 1 for c in ilk.values() if c > 1)
    print(f"ilk 60 karakteri aynı olan tekrar: {tekrar}")
    for h, neden in sorunlar[:15]:
        print(f"  SORUN {h['dosya']} [{h['tema']}]: {', '.join(neden)}")
    if "--yaz" in sys.argv:
        with open(os.path.join(HERE, "oyuncak.txt"), "w", encoding="utf-8") as f:
            for h in hikayeler:
                f.write(f"Karakter: {h['karakter']} | Yer: {h['yer']}\n\n{h['metin']}\n<|endoftext|>\n")
        print("yazıldı: oyuncak.txt")


if __name__ == "__main__":
    main()
