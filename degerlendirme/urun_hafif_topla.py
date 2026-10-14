"""Hafif hat (urun_v3, urun_v4): kod kontrolünden geçmiş yazar hikâyelerini toplar ve hakemli urun_v2 ile birleşik
eğitim klasörü kurar.

urun_v2 her hikâyeyi yazar + kod kapısı + 5 hakem + onarım döngüsünden geçirdi (1030 kabul, binlerce ajan çağrısı).
10 kat hacim için urun_v3 ve urun_v4 yalnız yazar + kod kontrolü (veri_hakem.py kontrol: K1–K11) kullanır; hakem
yoktur. Bu yüzden hafif hat hikâyeleri "kusursuz" değildir (docs/KUSURSUZ_VERI.md tanımı karşılanmaz) ve ayrı
klasörlerde tutulur.

  python degerlendirme/urun_hafif_topla.py topla [AD]     # data/AD/kontrol/*.json -> data/AD/<figür>.txt + gecen.txt
                                                          # (AD varsayılan urun_v3)
  python degerlendirme/urun_hafif_topla.py birlestir      # data/urun_karma/: v2 kabulleri + v3 geçenler, izin.txt
  python degerlendirme/urun_hafif_topla.py birlestir urun_karma2 urun_v3 urun_v4
                                                          # data/urun_karma2/: v2 + v3 + v4 (sıra önemli: aynı sha1
                                                          # ilk kümede kalır, sonrakilerde atlanır)
Doğrulama bölmesi yalnız v2'nin hakemli doğrulama bölmesidir; hafif hat hikâyeleri yalnız eğitime girer (val.bin ve
--en-iyi seçimi önceki modellerle karşılaştırılabilir kalır).

Gece (uyku modu, figür Ay Dede, kimlik 'gece'; urun_v4): gece metinleri eğitime girer (<hedef>/hafif_gece.txt),
ama GECE_DOGRULAMA (40: 20 ninni + 20 uyku masalı) metin belirlenimci olarak ayrılır ve eğitim klasörüne girmez:
<hedef>/gece_ayri/gece_dogrulama.txt (yazar biçimi) ve <hedef>/gece_ayri/liste.txt (<sha1> <tür>). prepare_ft2 --yalniz yalnız <hedef>/*.txt okur, alt
klasörü okumaz; bu 40 metin val.bin'e de girmez (val kaybı önceki modellerle aynı kümede kalır). Gece verisiyle
eğitilmiş modelin ninni kalitesi sonra bu 40 metnin planlarıyla (urun_uret.py, 'Sorun: ninni,' / 'Sorun: masal,')
ve kör kıyasla ölçülür. Tür plan sorununun ilk kelimesidir ('ninni,' | 'masal,'; degerlendirme/KILAVUZ_GECE.md).
Eğitim: prepare_ft2 --yalniz data/<hedef>/izin.txt (zincir_urun.sh IZIN=data/urun_karma2/izin.txt).
"""
import collections
import glob
import hashlib
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V2, V3, KARMA = (os.path.join(ROOT, "data", d) for d in ("urun_v2", "urun_v3", "urun_karma"))
sys.path.insert(0, HERE)
import urun_kayit  # noqa: E402

GECE = "gece"                    # gece figürünün kimliği (urun_kayit.figur_kimligi('Ay Dede'))
GECE_DOGRULAMA = {"ninni": 20, "masal": 20}
GECE_AYRI = "gece_ayri"


def _veri(ad, kok=None):
    return os.path.join(kok or os.path.join(ROOT, "data"), ad)


def topla(ad="urun_v3", kok=None):
    """Her tohumun son kontrol kaydı geçtiyse o bloğu alır (aynı sha1 bir kez)."""
    V = _veri(ad, kok)
    son = {}
    for yol in sorted(glob.glob(os.path.join(V, "kontrol", "*.json"))):
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
        with open(os.path.join(V, f"{f}.txt"), "w", encoding="utf-8") as out:
            out.write("\n\n".join(bloklar) + "\n")
    with open(os.path.join(V, "gecen.txt"), "w", encoding="utf-8") as out:
        out.write(f"# {ad} (hafif hat: yazar + kod kontrolü, hakemsiz) geçen hikâyeler: <sha1>\n")
        out.writelines(f"{s}\n" for s in sorted(gor))
    print(f"{ad}: tohum {len(son)}, geçen {len(gor)}: " + ", ".join(f"{f} {len(b)}" for f, b in sorted(figur.items())))
    return {f: len(b) for f, b in figur.items()}


def gece_turu(kayit):
    """'ninni' | 'masal' | None: plan sorununun ilk kelimesi."""
    s = urun_kayit.kucuk(kayit.get("sorun") or "")
    return next((t for t in GECE_DOGRULAMA if s.startswith(t + ",")), None)


def gece_ayir(kayitlar, n=GECE_DOGRULAMA):
    """Gece kayıtlarından türe göre doğrulama kümesi (belirlenimci: sha1'in tohumlu sha256 sırası). [(sha1, tür)]."""
    sec = []
    for tur, adet in n.items():
        aday = sorted((s for s, k in kayitlar.items() if gece_turu(k) == tur),
                      key=lambda s: hashlib.sha256(f"gece_dogrulama:{s}".encode()).hexdigest())
        sec += [(s, tur) for s in aday[:adet]]
    return sec


def _bloklar(yol):
    """[(sha1, kanonik kayıt, ham blok)] (biçim hatalı blok betiği durdurur: prepare_ft2 de durdurur)."""
    with open(yol, encoding="utf-8") as f:
        metin = f.read()
    out = []
    for b in urun_kayit.ayristir(metin):
        if b["bicim_hatalari"]:
            raise SystemExit(f"{yol}:{b['satir']}: biçim hatası: {b['bicim_hatalari']}")
        k = urun_kayit.kayit(b)
        out.append((urun_kayit.sha1(k), k, b["ham"].strip()))
    return out


def birlestir(hedef="urun_karma", ekler=("urun_v3",), kok=None):
    """data/<hedef>/: v2 kabulleri (izin bölmesiyle) + eklerin geçen hikâyeleri (yalnız eğitim). Gece metinlerinden
    GECE_DOGRULAMA kadarı <hedef>/gece_ayri/ altına ayrılır (eğitime ve val.bin'e girmez)."""
    H = _veri(hedef, kok)
    v2 = _veri("urun_v2", kok)
    if os.path.exists(H):
        shutil.rmtree(H)
    os.makedirs(H)
    for yol in glob.glob(os.path.join(v2, "*.txt")):
        if os.path.basename(yol) != "izin.txt":
            shutil.copy(yol, os.path.join(H, "v2_" + os.path.basename(yol)))
    izin = {}
    for satir in open(os.path.join(v2, "izin.txt"), encoding="utf-8"):
        p = satir.split()
        if len(p) == 2 and not satir.startswith("#"):
            izin[p[0]] = p[1]
    v2_n = len(izin)
    say, gece_kayit, gece_ham = {}, {}, {}
    for ad in ekler:
        V = _veri(ad, kok)
        gecen = {s.strip() for s in open(os.path.join(V, "gecen.txt"), encoding="utf-8")
                 if s.strip() and not s.startswith("#")}
        onek = ad.split("_")[-1]                       # urun_v3 -> v3
        yeni = []
        for yol in sorted(glob.glob(os.path.join(V, "*.txt"))):
            if os.path.basename(yol) == "gecen.txt":
                continue
            fk = os.path.basename(yol)[:-4]
            kalan = []
            for s, k, ham in _bloklar(yol):
                if s not in gecen or s in izin or s in gece_kayit:
                    continue                           # geçmemiş ya da önceki kümede var (sha1 bir kez)
                if fk == GECE:
                    gece_kayit[s], gece_ham[s] = k, ham
                    continue                           # gece: ayırma sonrası yazılır
                kalan.append(ham)
                yeni.append(s)
            if kalan:
                with open(os.path.join(H, f"{onek}_{fk}.txt"), "w", encoding="utf-8") as out:
                    out.write("\n\n".join(kalan) + "\n")
        for s in sorted(yeni):                         # izin sırası = gecen.txt sırası (eski urun_karma ile aynı)
            izin[s] = "egitim"
        say[ad] = len(yeni)
    ayri = gece_ayir(gece_kayit) if gece_kayit else []
    ayri_s = {s for s, _ in ayri}
    if gece_kayit:
        egitim = sorted(s for s in gece_kayit if s not in ayri_s)
        if egitim:
            with open(os.path.join(H, "hafif_gece.txt"), "w", encoding="utf-8") as out:
                out.write("\n\n".join(gece_ham[s] for s in egitim) + "\n")
        izin.update({s: "egitim" for s in egitim})
        os.makedirs(os.path.join(H, GECE_AYRI))
        with open(os.path.join(H, GECE_AYRI, "gece_dogrulama.txt"), "w", encoding="utf-8") as out:
            out.write("\n\n".join(gece_ham[s] for s, _ in ayri) + "\n")
        with open(os.path.join(H, GECE_AYRI, "liste.txt"), "w", encoding="utf-8") as out:
            out.write("# gece doğrulama kümesi (eğitime ve val.bin'e girmez): <sha1> <tür>\n")
            out.writelines(f"{s} {t}\n" for s, t in ayri)
    hafif = sum(say.values()) + len(gece_kayit) - len(ayri)
    with open(os.path.join(H, "izin.txt"), "w", encoding="utf-8") as out:
        out.write(f"# {hedef}: urun_v2 hakemli {v2_n} (doğrulama bölmesi v2'den) + "
                  + " + ".join(f"{a} hafif hat {n}" for a, n in say.items())
                  + (f" + gece {len(gece_kayit) - len(ayri)} (ayrı tutulan gece doğrulaması {len(ayri)}: "
                     f"{GECE_AYRI}/)" if gece_kayit else "") + " (yalnız eğitim)\n")
        out.writelines(f"{s} {b}\n" for s, b in izin.items())
    print(f"{hedef}: v2 {v2_n} + " + " + ".join(f"{a} {n}" for a, n in say.items())
          + (f" + gece {len(gece_kayit) - len(ayri)} (ayrı {len(ayri)})" if gece_kayit else "")
          + f" = {v2_n + hafif} -> {os.path.relpath(os.path.join(H, 'izin.txt'), ROOT)}")
    return {"v2": v2_n, **say, "gece": len(gece_kayit) - len(ayri), "gece_ayri": len(ayri)}


if __name__ == "__main__":
    komut, arg = sys.argv[1], sys.argv[2:]
    if komut == "topla":
        topla(*(arg[:1] or ["urun_v3"]))
    elif komut == "birlestir":
        birlestir(arg[0], tuple(arg[1:]) or ("urun_v3",)) if arg else birlestir()
    else:
        raise SystemExit(__doc__)
