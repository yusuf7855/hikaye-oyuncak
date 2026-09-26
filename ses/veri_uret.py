"""Ses modeli için eğitim verisi: hikâye cümlelerini Emel (kadın) sesiyle seslendirir.

Kullanım:
  python ses/veri_uret.py --cikti ses_veri --adet 25000 [--es 8]
Yazar:
  ses_veri/metin.tsv   kimlik<TAB>metin (tüm seçilen cümleler; sabit sıra, tohum 1)
  ses_veri/mp3/<kimlik>.mp3   24 kHz mp3 (edge-tts)
Yarıda kalırsa aynı komutla devam eder (var olan mp3'ler atlanır). İnternet gerekir.
"""
import argparse, asyncio, glob, os, random, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SES = "tr-TR-EmelNeural"


def cumleler():
    """Bütün hikâye dosyalarından temiz cümleler (başlık ve plan satırları hariç), tekrarsız."""
    gor, out = set(), []
    for f in sorted(glob.glob(os.path.join(KOK, "data", "oyuncak_*", "*.txt"))):
        for satir in open(f, encoding="utf-8"):
            satir = satir.strip()
            if not satir or satir.startswith(("###", "@", "#")):
                continue
            # cümlelere böl: nokta/ünlem/soru ve ardından boşluk; tırnak kapanışını cümlede tut
            for c in re.split(r'(?:(?<=[.!?])|(?<=[.!?]["”]))\s+(?=["“A-ZÇĞİÖŞÜ])', satir):
                c = c.strip()
                if 12 <= len(c) <= 180 and c not in gor:
                    gor.add(c)
                    out.append(c)
    return out


async def seslendir(metin, yol, sem):
    import edge_tts
    async with sem:
        for deneme in range(4):
            try:
                veri = b""
                async for p in edge_tts.Communicate(metin, SES).stream():
                    if p["type"] == "audio":
                        veri += p["data"]
                if veri:
                    tmp = yol + ".tmp"
                    open(tmp, "wb").write(veri)
                    os.replace(tmp, yol)
                    return True
            except Exception as e:  # ağ hatası: bekleyip tekrar dene
                await asyncio.sleep(2 * (deneme + 1))
        print("başarısız:", yol, file=sys.stderr)
        return False


async def main(a):
    os.makedirs(os.path.join(a.cikti, "mp3"), exist_ok=True)
    tsv = os.path.join(a.cikti, "metin.tsv")
    hazir_liste = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metin.tsv")
    if not os.path.exists(tsv) and os.path.exists(hazir_liste):   # depodaki sabit 25 bin cümle
        import shutil
        shutil.copy(hazir_liste, tsv)
    if os.path.exists(tsv):
        secim = [l.rstrip("\n").split("\t", 1) for l in open(tsv, encoding="utf-8")]
    else:
        cs = cumleler()
        random.Random(1).shuffle(cs)
        secim = [(f"e{i:06d}", c) for i, c in enumerate(cs[: a.adet])]
        with open(tsv, "w", encoding="utf-8") as f:
            for k, c in secim:
                f.write(f"{k}\t{c}\n")
        print(f"{len(cs)} tekrarsız cümle; {len(secim)} seçildi -> {tsv}")
    sem = asyncio.Semaphore(a.es)
    kalan = [(k, c) for k, c in secim if not os.path.exists(os.path.join(a.cikti, "mp3", k + ".mp3"))]
    print(f"seslendirilecek: {len(kalan)} / {len(secim)}")
    for i in range(0, len(kalan), 200):
        parca = kalan[i:i + 200]
        await asyncio.gather(*(seslendir(c, os.path.join(a.cikti, "mp3", k + ".mp3"), sem) for k, c in parca))
        print(f"{i + len(parca)} / {len(kalan)}", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_veri"))
    ap.add_argument("--adet", type=int, default=25000)
    ap.add_argument("--es", type=int, default=8, help="aynı anda istek")
    asyncio.run(main(ap.parse_args()))
