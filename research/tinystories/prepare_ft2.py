"""v2 oyuncak ince ayar verisi (12 figür, tek + ikili, sabit isimler) + genel Türkçe dilim.

Başlık biçimi (firmware/arayüz de aynısını üretir; ikili sırası karakterler.json sırasıdır):
    "Karakter: tavşan | Yer: orman\n\n"            tek figür
    "Karakter: tavşan, tilki | Yer: orman\n\n"     iki figür
    "Karakter: tavşan | Yer: orman\nSorun: S\nÇözüm: Ç\n\n"   --plan (E3): hikâyenin iki satırlık planı
Her tek-figür kombinasyonundan ve her ikiliden 1 hikâye doğrulamaya ayrılır.
Eski (v1) 960 hikâye bilerek dışarıda: çok isimli oldukları için isim çorbasını geri öğretirler.

Kullanım: PYTHONPATH=src python -m research.tinystories.prepare_ft2 [--vocab 16384]
Çıktı: data/tr_ft2/vocab-<V>/{train,val}.bin + aynı tokenizer.json
       + {train,val}_{bas,son}.npy (E2: her oyuncak hikâyesinin [bas, son) aralığı; train.py --hizala toy)
"""
import argparse
import importlib.util
import json
import random
import shutil
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "data" / "oyuncak_v2"
SIRA = [k["tur"] for k in json.load(open(ROOT / "data" / "karakterler.json", encoding="utf-8"))["karakterler"]]
# Popüler karakterler (data/oyuncak_populer/karakterler.json): başlıkta türleri yerine adları geçer ("Karakter: Elsa")
_POP = ROOT / "data" / "oyuncak_populer" / "karakterler.json"
if _POP.exists():
    SIRA += [k["isim"] for k in json.load(open(_POP, encoding="utf-8"))]


def kimlik_ver(kaynak, hikayeler):
    """Kalıcı hikâye kimliği: <küme>/<dosya>#<dosyadaki sıra>, ör. "v3/tavsan_orman#4".
    Hikâye Atölyesi'nde "bozuk" işaretlenenler bu kimlikle --haric'e verilir."""
    sira = {}
    for h in hikayeler:
        n = sira.get(h["dosya"], 0)
        sira[h["dosya"]] = n + 1
        h["id"] = f"{kaynak.split('_')[-1]}/{h['dosya'][:-4]}#{n}"
    return hikayeler


def baslik(h, tema=False, plan=None):
    """Eğitim satırı: başlık + hikâye. tema=True: başlığa hikâyenin konusu da girer
    ("Karakter: ayı | Yer: ev | Tema: kaybolan bir şeyi bulmak"); model sorunu kendisi uydurmak zorunda kalmaz.
    plan=(sorun, çözüm): başlığın ardına iki plan satırı girer ("…\nSorun: S\nÇözüm: Ç\n\n<hikâye>", E3).
    Cihaz ve arayüz aynı biçimi baslangic.baslangic(..., tema=..., plan_metni=...) ile kurar."""
    turler = sorted(h["turler"], key=SIRA.index)
    ek = f" | Tema: {h['tema']}" if tema else ""
    if plan is not None:
        ek += f"\nSorun: {plan[0]}\nÇözüm: {plan[1]}"
    return f"Karakter: {', '.join(turler)} | Yer: {h['yer']}{ek}\n\n{h['metin']}"


def plan_oku(yol):
    """data/oyuncak_plan/plan.jsonl -> {kimlik: kayıt}. Plan metni başlığın satır yapısını bozamaz."""
    planlar = {}
    for satir in open(yol, encoding="utf-8"):
        if satir.strip():
            k = json.loads(satir)
            planlar[k["id"]] = k
    for k in planlar.values():
        for alan in ("sorun", "cozum"):
            if not k.get("yok") and k.get(alan) and ("\n" in k[alan] or "|" in k[alan]):
                raise SystemExit(f"--plan: {k['id']} {alan} satır sonu ya da '|' içeriyor")
    return planlar


def plani(planlar, h):
    """(sorun, çözüm) ya da None: yok=true, etiketsiz ya da eksik plan -> plansız (eski) başlık."""
    k = planlar.get(h["id"]) if planlar else None
    if not k or k.get("yok") or not k.get("sorun") or not k.get("cozum"):
        return None
    return k["sorun"], k["cozum"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocab", type=int, default=16384)
    ap.add_argument("--tekrar", type=int, default=6)
    ap.add_argument("--genel-token", type=int, default=8_000_000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="tr_ft2", help="data/<out>/vocab-<V> altına yaz")
    ap.add_argument("--kaynak", default="oyuncak_v2", help="virgülle ayrılmış hikâye klasörleri (data/ altında)")
    ap.add_argument("--tema", action="store_true", help="başlığa hikâyenin temasını da yaz (rastgeleliği etkilemez)")
    ap.add_argument("--haric", default=None,
                    help="dışarıda bırakılacak hikâye kimlikleri: her satırda bir kimlik olan dosya")
    ap.add_argument("--bolme", default=None, help="sabit doğrulama bölmesi + sızıntı listesi (data/bolme.json)")
    ap.add_argument("--blok-eot", action="store_true",
                    help="her oyuncak bloğunun önüne <|endoftext|>: genel dilim hikâye ortasında bitse de blok temiz başlar")
    ap.add_argument("--genel", default="tr_tinystories",
                    help="genel Türkçe veri + tokenizer klasörü (data/ altında); C2 için tr2_tinystories")
    ap.add_argument("--plan", default=None,
                    help="E3 plan etiketleri (data/oyuncak_plan/plan.jsonl): planlı hikâyeler plan başlığıyla da görülür")
    ap.add_argument("--plan-orani", type=float, default=0.7,
                    help="--plan: her kopyada planlı hikâyenin plan başlığıyla yazılma olasılığı (kalanı eski başlık)")
    args = ap.parse_args()
    if not 0.0 <= args.plan_orani <= 1.0:
        raise SystemExit("--plan-orani 0 ile 1 arasında olmalı")
    rng = random.Random(args.seed)

    hikayeler = []
    for kaynak in args.kaynak.split(","):
        d = ROOT / "data" / kaynak
        spec = importlib.util.spec_from_file_location(f"kontrol_{kaynak}", d / "kontrol.py")
        kontrol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(kontrol)
        iyi, sorunlu = kontrol.oku()
        if sorunlu:
            print(f"UYARI: {kaynak}: {len(sorunlu)} sorunlu hikâye dışarıda bırakıldı")
        hikayeler += kimlik_ver(kaynak, iyi)
    tum = hikayeler[:]
    if args.haric:
        haric = {s.strip() for s in open(args.haric, encoding="utf-8") if s.strip()}
        once = len(hikayeler)
        hikayeler = [h for h in hikayeler if h["id"] not in haric]
        print(f"--haric: {once - len(hikayeler)} hikâye dışarıda bırakıldı ({len(haric)} kimlik)")

    if args.bolme:
        # Sabit bölme (research/tinystories/benzerlik.py): doğrulama her kolda aynı 138 hikâye (--haric onları
        # etkilemez); doğrulama hikâyelerinin isim değiştirilmiş kopyaları ("haric") eğitimden çıkar.
        b = json.load(open(args.bolme, encoding="utf-8"))
        dset, sizinti = set(b["dogrulama"]), set(b["haric"])
        dogrulama = [h for h in tum if h["id"] in dset]
        egitim = [h for h in hikayeler if h["id"] not in dset and h["id"] not in sizinti]
        print(f"--bolme: {len(dogrulama)} doğrulama, {sum(h['id'] in sizinti for h in hikayeler)} sızıntı eğitimden çıktı")
    else:
        gruplar = {}
        for h in hikayeler:
            anahtar = (h["turler"][0], h["yer"]) if len(h["turler"]) == 1 else tuple(sorted(h["turler"]))
            gruplar.setdefault(anahtar, []).append(h)
        egitim, dogrulama = [], []
        for k in sorted(gruplar, key=str):
            g = gruplar[k][:]
            rng.shuffle(g)
            dogrulama.append(g[0])
            egitim.extend(g[1:])

    src = ROOT / "data" / args.genel / f"vocab-{args.vocab}"
    out = ROOT / "data" / args.out / f"vocab-{args.vocab}"
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src / "tokenizer.json", out / "tokenizer.json")
    tok = Tokenizer.from_file(str(out / "tokenizer.json"))
    eot = tok.token_to_id("<|endoftext|>")

    def kodla(metinler, ids, bas, son):
        """Hikâyeleri ids'in sonuna ekler (her birinin ardına EOT). E2 için her hikâyenin aralığı: bas = başlıktan
        önceki EOT'nin konumu (yoksa başlığın başı), son = kendi EOT'sinin bir ötesi."""
        for enc in tok.encode_batch(metinler):
            bas.append(len(ids) - 1 if ids and ids[-1] == eot else len(ids))
            ids.extend(enc.ids)
            ids.append(eot)
            son.append(len(ids))

    genel_kaynak = np.memmap(src / "train.bin", dtype=np.uint16, mode="r")
    if args.genel_token > 0:
        bas = rng.randrange(0, len(genel_kaynak) - args.genel_token - 1)
        while genel_kaynak[bas] != eot:
            bas += 1
        genel = genel_kaynak[bas + 1: bas + 1 + args.genel_token]
    else:
        genel = np.zeros(0, dtype=np.uint16)

    planlar = plan_oku(args.plan) if args.plan else None
    # --plan'ın kura çekimi ayrı rng'de: veri sırası ve genel dilim --plan'sız kolla birebir aynı kalır.
    plan_rng = random.Random(args.seed + 17)
    planli_kopya = 0

    # Her tekrarda hikâye sırası karışık; oyuncak blokları genel verinin arasına dağıtılır.
    train, t_bas, t_son = [], [], []
    for g in np.array_split(genel, args.tekrar):
        train.extend(g.tolist())
        blok = egitim[:]
        rng.shuffle(blok)
        if args.blok_eot and train and train[-1] != eot:
            train.append(eot)
        if planlar is None:
            metinler = [baslik(h, args.tema) for h in blok]
        else:
            metinler = []
            for h in blok:
                p = plani(planlar, h)
                kura = plan_rng.random() < args.plan_orani  # her kopya ve her hikâye için bir çekim
                metinler.append(baslik(h, args.tema, p if kura else None))
                planli_kopya += bool(p and kura)
        kodla(metinler, train, t_bas, t_son)
    # doğrulamada planı olan her hikâye plan başlığıyla (kurasız)
    val, v_bas, v_son = [], [], []
    kodla([baslik(h, args.tema, plani(planlar, h)) for h in dogrulama], val, v_bas, v_son)
    uzun = sum(1 for h in egitim if len(tok.encode(baslik(h, args.tema, plani(planlar, h))).ids) + 1 > 256)
    # koşul duyarlılığı ve hakem ölçümleri doğrulama hikâyelerini tek tek ister
    kayitlar = [{k: h[k] for k in ("id", "turler", "yer", "tema", "metin")} for h in dogrulama]
    if planlar is not None:
        for d, h in zip(kayitlar, dogrulama):
            p, k = plani(planlar, h), planlar.get(h["id"], {})
            d["sorun"], d["cozum"] = p or (None, None)
            d["anahtar_sorun"] = k.get("anahtar_sorun") if p else None
            d["anahtar_cozum"] = k.get("anahtar_cozum") if p else None
    json.dump(kayitlar, open(out / "dogrulama.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)

    np.array(train, dtype=np.uint16).tofile(out / "train.bin")
    np.array(val, dtype=np.uint16).tofile(out / "val.bin")
    # E2 (train.py --hizala toy): oyuncak hikâyelerinin [bas, son) aralıkları, artan sırada
    for ad, dizi in (("train_bas", t_bas), ("train_son", t_son), ("val_bas", v_bas), ("val_son", v_son)):
        np.save(out / f"{ad}.npy", np.array(dizi, dtype=np.uint32))
    tek = sum(len(h["turler"]) == 1 for h in egitim)
    print(f"oyuncak: {len(egitim)} eğitim ({tek} tek, {len(egitim) - tek} ikili) / {len(dogrulama)} doğrulama; "
          f"x{args.tekrar} | 256 tokeni aşan hikâye: {uzun}")
    print(f"genel: {len(genel):,} token | toplam train {len(train):,} | val {len(val):,}")
    if planlar is not None:
        e_planli = sum(plani(planlar, h) is not None for h in egitim)
        etiketsiz = sum(h["id"] not in planlar for h in egitim + dogrulama)
        print(f"plan: {e_planli}/{len(egitim)} eğitim hikâyesinin planı var; kopyaların "
              f"{planli_kopya}/{len(egitim) * args.tekrar} tanesi plan başlığıyla (oran {args.plan_orani}) | "
              f"doğrulama {sum(plani(planlar, h) is not None for h in dogrulama)}/{len(dogrulama)} planlı | "
              f"etiketsiz {etiketsiz} (plansız sayıldı)")


if __name__ == "__main__":
    main()
