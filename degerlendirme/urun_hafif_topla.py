"""Hafif hat (urun_v3): kod kontrolünden geçmiş yazar hikâyelerini toplar ve hakemli urun_v2 ile birleşik eğitim
klasörü kurar.

urun_v2 her hikâyeyi yazar + kod kapısı + 5 hakem + onarım döngüsünden geçirdi (1030 kabul, binlerce ajan çağrısı).
10 kat hacim için urun_v3 yalnız yazar + kod kontrolü (veri_hakem.py kontrol: K1–K11) kullanır; hakem yoktur. Bu yüzden
v3 hikâyeleri "kusursuz" değildir (docs/KUSURSUZ_VERI.md tanımı karşılanmaz) ve ayrı bir klasörde tutulur.

  python degerlendirme/urun_hafif_topla.py topla      # data/urun_v3/kontrol/*.json -> data/urun_v3/<figür>.txt + gecen.txt
  python degerlendirme/urun_hafif_topla.py birlestir  # data/urun_karma/: v2 kabulleri + v3 geçenler, izin.txt
                                                      # (doğrulama = v2'nin hakemli doğrulama bölmesi; v3 yalnız eğitim)
Eğitim: prepare_ft2 --yalniz data/urun_karma/izin.txt (zincir_urun.sh IZIN=data/urun_karma/izin.txt).
"""
import collections
import glob
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V2, V3, KARMA = (os.path.join(ROOT, "data", d) for d in ("urun_v2", "urun_v3", "urun_karma"))
sys.path.insert(0, HERE)
import urun_kayit  # noqa: E402


def topla():
    """Her tohumun son kontrol kaydı geçtiyse o bloğu alır (aynı sha1 bir kez)."""
    son = {}
    for yol in sorted(glob.glob(os.path.join(V3, "kontrol", "*.json"))):
        d = json.load(open(yol, encoding="utf-8"))
        for tohum, kayitlar in d.items():
            if kayitlar:
                son[tohum] = kayitlar[-1]
    figur = collections.defaultdict(list)
    gor = set()
    for tohum, k in sorted(son.items()):
        if not k.get("gecti") or k["sha1"] in gor:
            continue
        gor.add(k["sha1"])
        blok = urun_kayit.ayristir(k["ham"])[0]
        figur[urun_kayit.figur_kimligi(blok["figur"])].append(k["ham"].strip())
    for f, bloklar in figur.items():
        with open(os.path.join(V3, f"{f}.txt"), "w", encoding="utf-8") as out:
            out.write("\n\n".join(bloklar) + "\n")
    with open(os.path.join(V3, "gecen.txt"), "w", encoding="utf-8") as out:
        out.write("# urun_v3 (hafif hat: yazar + kod kontrolü, hakemsiz) geçen hikâyeler: <sha1>\n")
        out.writelines(f"{s}\n" for s in sorted(gor))
    print(f"tohum {len(son)}, geçen {len(gor)}: " + ", ".join(f"{f} {len(b)}" for f, b in sorted(figur.items())))


def birlestir():
    if os.path.exists(KARMA):
        shutil.rmtree(KARMA)
    os.makedirs(KARMA)
    for yol in glob.glob(os.path.join(V2, "*.txt")):
        if os.path.basename(yol) != "izin.txt":
            shutil.copy(yol, os.path.join(KARMA, "v2_" + os.path.basename(yol)))
    for yol in glob.glob(os.path.join(V3, "*.txt")):
        if os.path.basename(yol) != "gecen.txt":
            shutil.copy(yol, os.path.join(KARMA, "v3_" + os.path.basename(yol)))
    izin = {}
    for satir in open(os.path.join(V2, "izin.txt"), encoding="utf-8"):
        p = satir.split()
        if len(p) == 2 and not satir.startswith("#"):
            izin[p[0]] = p[1]
    v3 = [s.strip() for s in open(os.path.join(V3, "gecen.txt"), encoding="utf-8") if s.strip() and not s.startswith("#")]
    yeni = [s for s in v3 if s not in izin]
    with open(os.path.join(KARMA, "izin.txt"), "w", encoding="utf-8") as out:
        out.write(f"# urun_karma: urun_v2 hakemli {len(izin)} (doğrulama bölmesi v2'den) + urun_v3 hafif hat {len(yeni)} "
                  f"(yalnız eğitim)\n")
        out.writelines(f"{s} {b}\n" for s, b in izin.items())
        out.writelines(f"{s} egitim\n" for s in yeni)
    print(f"karma: v2 {len(izin)} + v3 {len(yeni)} -> {os.path.relpath(KARMA, ROOT)}/izin.txt")


if __name__ == "__main__":
    {"topla": topla, "birlestir": birlestir}[sys.argv[1]]()
