"""Eğitim verisini (oyuncak_v2 + oyuncak_v3) Hikâye Atölyesi'nin "Eğitim verisi" sekmesi için paketle.

Kullanım: .venv/bin/python web/veri.py   ->  web/veri.json
Her hikâyeye kalıcı bir kimlik verilir: <küme>/<dosya>#<dosyadaki sıra>. Arayüzde "bozuk" işaretlenen
kimlikler bir sonraki ince ayarda prepare_ft2 --haric ile dışarıda bırakılır.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from baslangic import KAR  # noqa: E402
from research.tinystories.prepare_ft2 import kimlik_ver  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
from sec import SOZLUK, cezalar, kucuk, yer_cezasi  # noqa: E402

TUR_KIMLIK = {k["tur"]: k["kimlik"] for k in KAR.values()}
YER_KIMLIK = {"orman": "orman", "deniz": "deniz", "ev": "ev", "park": "park", "şato": "sato", "dağ": "dag"}


def kimlikli(kaynak):
    spec = importlib.util.spec_from_file_location(f"kontrol_{kaynak}", os.path.join(ROOT, "data", kaynak, "kontrol.py"))
    kontrol = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(kontrol)
    iyi, _ = kontrol.oku()
    return kimlik_ver(kaynak, iyi)


def main():
    hikayeler = []
    for kaynak in ("oyuncak_v2", "oyuncak_v3"):
        for h in kimlikli(kaynak):
            k, y = [TUR_KIMLIK[t] for t in h["turler"]], YER_KIMLIK[h["yer"]]
            # Seçicinin kuralları eğitim hikâyesine de uygulanır: arayüz şüphelileri önce gösterir
            # (sözlük dışı kelimeler ayrı: çoğu nadir ama doğru çekimler, arayüz onları metin içinde işaretler)
            c = [re.sub(r"[\[\]']", "", ad) for _, ad in cezalar(h["metin"], k, bitti=True) if not ad.startswith("uydurma")]
            c += ["yer kayması"] if yer_cezasi(h["metin"], y) else []
            u = sorted({w for w in re.findall(r"[a-zçğıöşüâîû]+", kucuk(h["metin"])) if SOZLUK and w not in SOZLUK})
            hikayeler.append({"id": h["id"], "k": k, "y": y, "t": h["tema"], "m": h["metin"], "c": c, "u": u})
    json.dump(hikayeler, open(os.path.join(HERE, "veri.json"), "w", encoding="utf-8"), ensure_ascii=False,
              separators=(",", ":"))
    import collections
    say = collections.Counter(c.split(" [")[0].split(":")[0] for h in hikayeler for c in h["c"])
    print(f"kural uyarısı olan: {sum(bool(h['c']) for h in hikayeler)}", dict(say.most_common(12)))
    print(f"{len(hikayeler)} hikâye -> web/veri.json ({os.path.getsize(os.path.join(HERE, 'veri.json')) / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
