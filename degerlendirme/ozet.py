"""Hakem puanlarını topla. Kullanım: python degerlendirme/ozet.py <ad>"""
import collections, glob, json, os, sys
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
puan = {}
for f in glob.glob(os.path.join(d, "puan_*.json")):
    for p in json.load(open(f, encoding="utf-8")):
        puan.setdefault(p["id"], []).append(p)
hik = {h["id"]: h for h in json.load(open(os.path.join(d, "hikayeler.json"), encoding="utf-8"))}
if not puan:
    sys.exit("puan yok")
ort = {i: sum(p["puan"] for p in ps) / len(ps) for i, ps in puan.items()}
tek = [v for i, v in ort.items() if len(hik[i]["figurler"]) == 1]
cift = [v for i, v in ort.items() if len(hik[i]["figurler"]) == 2]
tum = list(ort.values())
print(f"{sys.argv[1]}: ORTALAMA {sum(tum)/len(tum):.2f}/10  (tek {sum(tek)/max(1,len(tek)):.2f}, ikili {sum(cift)/max(1,len(cift)):.2f})  "
      f"n={len(tum)}/{len(hik)}  10'luk: {sum(v >= 9.5 for v in tum)}  ≤5: {sum(v <= 5 for v in tum)}")
sorun = collections.Counter(s for ps in puan.values() for p in ps for s in p.get("kategoriler", []))
print("en sık kusurlar:", sorun.most_common(8))
