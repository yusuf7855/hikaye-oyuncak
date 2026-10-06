"""Kartın üretim yolu (hikaye_oyuncak.ino, bilgisayarda sahte ESP32 başlıklarıyla: tools/kart_pc) ile
degerlendirme/urun_uret.py'nin aynı vakalarda aynı hikâyeleri ürettiğini ve aynı adayı seçtiğini doğrular.

Her vaka (urun_uret.vakalar: figür × kart yeri, sabit seed) için kartta "f j K" komutu, aday j'de srand(seed + j)
(urun_uret: gen'e seed + j); bilgisayarda urun_uret.istem + suzgec_dosyasi + aday_uret + puanla. Karşılaştırılan:
plan ve gövde metni, bitti, plan_bozuk, gövde token sayısı, ortalama lp ve puan (birebir), seçilen aday.

Kart int8 aktivasyon kullanır (LLM_INT8_ACT; çekirdek ve head q4f/int8 yolları matvec_q8 ile bit bit aynı), depodaki
./gen ise float aktivasyonla derlenir (cc -O3 gen.c): bu yüzden karşılaştırma gen.c'nin -DLLM_INT8_ACT ile
derlenmiş kopyasıyla yapılır (GEN ortam değişkeni; urun_uret aynen çalışır). --float: ayrıca ./gen (float) ile
kaç adayın aynı çıktığını bilgi olarak yazar (fark beklenir: aktivasyon nicemlemesi).

Kullanım: python firmware/hikaye_oyuncak/tools/kart_pc_karsilastir.py [--model hf_c3ft_karma] [--vaka 11] [--aday 4]
          [--hepsi] [--float]
  --vaka N: figür başına ilk vakadan başlayarak N vaka (varsayılan 11: her figürden bir); --hepsi: 41 vakanın hepsi.
Çıkış kodu: uyuşmazlık varsa 1.
"""
import argparse
import os
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SKETCH = os.path.dirname(TOOLS)
ROOT = os.path.dirname(os.path.dirname(SKETCH))


def derle(d):
    gen_i8 = os.path.join(d, "gen_i8")
    subprocess.run([os.environ.get("CC", "cc"), "-O3", "-DLLM_INT8_ACT", "-o", gen_i8,
                    os.path.join(ROOT, "runtime", "host_verify", "gen.c"), "-lm"], check=True)
    kart = os.path.join(d, "kart_pc")
    subprocess.run([os.environ.get("CXX", "g++"), "-O2", "-Wall", "-Wno-unused-function",
                    "-I" + os.path.join(TOOLS, "kart_pc", "sahte"), "-o", kart,
                    os.path.join(TOOLS, "kart_pc", "kart_pc.cpp")], check=True)
    return gen_i8, kart


def kart_kos(kart, model, komutlar):
    env = dict(os.environ, KART_MODEL=os.path.join(model, "model.bin"),
               KART_BOLUMLER=os.path.join(SKETCH, "partitions.csv"))
    r = subprocess.run([kart], input="".join(komutlar), capture_output=True, text=True, env=env, check=True)
    adaylar = []
    for s in r.stderr.splitlines():
        if s.startswith("PSRAM "):
            print("kart_pc:", s)
        if not s.startswith("ADAY "):
            continue
        p = s.split()
        adaylar.append({"j": int(p[1]), "n": int(p[2]), "n_plan": int(p[3]), "bitti": p[4] == "1",
                        "plan_bozuk": p[5] == "1", "lp": float(p[6]), "puan": float(p[7]),
                        "tok": [int(x) for x in p[8:]]})
    return adaylar, r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=os.path.join(ROOT, "hf_c3ft_karma"))
    ap.add_argument("--vaka", type=int, default=11)
    ap.add_argument("--aday", type=int, default=4)
    ap.add_argument("--hepsi", action="store_true")
    ap.add_argument("--float", action="store_true", help="./gen (float aktivasyon) ile de karşılaştır (bilgi)")
    a = ap.parse_args()
    d = tempfile.mkdtemp(prefix="kart_pc_")
    gen_i8, kart = derle(d)
    os.environ["GEN"] = gen_i8  # urun_uret GEN'i içe aktarılırken okur
    sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
    import urun_uret as U
    from tokenizers import Tokenizer
    tok = Tokenizer.from_file(os.path.join(a.model, "tokenizer.json"))
    tum = U.vakalar(U.FIGURLER)
    if a.hepsi:
        vakalar = tum
    else:  # her figürün sırayla kart yerleri: önce her figürün 1. yeri, sonra 2. yeri ...
        sira = sorted(range(len(tum)), key=lambda i: (sum(1 for v in tum[:i] if v["figur"] == tum[i]["figur"]), i))
        vakalar = [tum[i] for i in sira[:a.vaka]]
    komut = []
    for v in vakalar:
        f = U.FIGURLER.index(v["figur"])
        j = [y["etiket"] for y in U.KARTLAR[v["figur"]]["yerler"]].index(v["yer"])
        komut += [f"#tohum {v['seed']}\n", f"{f + 1} {j + 1} {a.aday}\n"]
    kart_adaylar, _ = kart_kos(kart, a.model, komut)
    assert len(kart_adaylar) == len(vakalar) * a.aday, (len(kart_adaylar), len(vakalar) * a.aday)
    suz_dir = os.path.join(d, "suzgec")
    os.makedirs(suz_dir)
    hata, secim_fark, uzun, ayni_float, n_float = 0, 0, 0, 0, 0
    for vi, v in enumerate(vakalar):
        k = U.KARTLAR[v["figur"]]
        suz = U.suzgec_dosyasi(tok, U.kadro_disi(v["figur"]), os.path.join(suz_dir, f"{v['figur']}.txt"))
        ids = U.istem(tok, k["ad"]["deger"], v["yer"], None)
        py, kr = [], kart_adaylar[vi * a.aday:(vi + 1) * a.aday]
        for j in range(a.aday):
            c = U.aday_uret(a.model, tok, ids, v["seed"] + j, 0.5, suz)
            c["puan"], _ = U.puanla(c, v["figur"], v["yer"])
            py.append(c)
            q = kr[j]
            t = q["tok"]
            kq = {"plan_bozuk": q["plan_bozuk"], "bitti": q["bitti"], "puan": q["puan"]}
            pq = {"plan_bozuk": c["plan_bozuk"], "bitti": c["bitti"], "puan": c["puan"]}
            if not q["plan_bozuk"]:
                kq.update(plan=("Sorun:" + tok.decode(t[:q["n_plan"] - 2])).strip(),
                          metin=tok.decode(t[q["n_plan"]:]).strip(), lp=q["lp"], n=q["n"] - q["n_plan"])
                pq.update(plan=c["plan"], metin=c["metin"], lp=c["lp"], n=c["n"])
            if len(ids) + q["n"] + 1 >= 224:
                uzun += 1  # kartın bağlamı (224) dolmuş olabilir: urun_uret 256'ya kadar sürer
            fark = {x: (pq[x], kq[x]) for x in pq if pq[x] != kq[x]}
            if fark:
                hata += 1
                print(f"  FARK {v['figur']} {v['yer']} seed {v['seed']} aday {j}:",
                      {x: (str(p)[:80], str(c_)[:80]) for x, (p, c_) in fark.items()})
            if a.float:
                U.GEN = os.path.join(ROOT, "gen")
                cf = U.aday_uret(a.model, tok, ids, v["seed"] + j, 0.5, suz)
                U.GEN = gen_i8
                n_float += 1
                ayni_float += cf["metin"] == c["metin"] and cf["plan"] == c["plan"]
        py_en = max(range(a.aday), key=lambda i: py[i]["puan"])
        kr_en = max(range(a.aday), key=lambda i: kr[i]["puan"])
        secim_fark += py_en != kr_en
        print(f"{v['figur']:12s} {v['yer']:6s} seed {v['seed']:6d}: seçilen urun_uret {py_en} kart {kr_en}, puan "
              f"{py[py_en]['puan']:.4f} / {kr[kr_en]['puan']:.4f}")
    n = len(vakalar) * a.aday
    print(f"{len(vakalar)} vaka x {a.aday} aday = {n} aday: uyuşmazlık {hata}, seçim farkı {secim_fark}, "
          f"bağlam sınırına yaklaşan aday {uzun}")
    if a.float:
        print(f"bilgi: ./gen (float aktivasyon) ile aynı plan+metin: {ayni_float}/{n_float}")
    sys.exit(1 if hata or secim_fark else 0)


if __name__ == "__main__":
    main()
