"""Hakemsiz hızlı ölçüm: sabit 36 vakalık test setinde kural cezaları ve uydurma kelime oranı.

Kullanım: python degerlendirme/otomatik.py <model_dizini> [--aday 8] [--temp 0.5] [--rep 1.1] [--ad AD]
                                          [--baslik eski|tema|plan] [--pencere tum|govde] [--satir-yasak] [--eot-on]
                                          [--plan-kosul model|oracle] [--dogrulama <dogrulama.json>]
Her vaka için K aday üretilir (uret.py ile aynı seed'ler), seçici (sec.py) en iyisini alır; ölçümler hem
ilk adaydan (seçicisiz model) hem seçilenden raporlanır. Hakem puanının yerini tutmaz ama sürümleri
birkaç dakikada, aynı ölçüyle karşılaştırır. Üretim bayrakları uret.py'dekilerle aynı.
Adaylar <model_dizini>/adaylar_<ad>.json'a yazılır (uret.aday_havuzu); uret.py'ye verilen adla (--ad) ve aynı
ayarlarla çağrılırsa onun adayları yeniden üretilmez. --ad verilmezse ad bayraklardan türetilir.
Plan modunda (--baslik plan) ölçüler gövdeden alınır; ek alan plan_bozuk: gövdesi olmayan (atılan) aday sayısı.
--dogrulama: vakalar test seti yerine doğrulama hikâyeleri (uret.py'ye bakın).
Çıktı: <model_dizini>/otomatik.json (yeni bayraklar ve --ad yoksa), yoksa otomatik_<ad>.json
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tokenizers import Tokenizer  # noqa: E402
from sec import SOZLUK, cezalar, kucuk, puanla, yer_cezasi  # noqa: E402
from uret import aday_havuzu, bayraklar, test_seti, vakalar  # noqa: E402,F401


TURLER = ["yeterince yok", "sonda yok", "kendine gönderme", " ve ", "sonradan beliren", "aynı konuşmacı",
          "yanlış isim", "tekrarlanan cümle", "yarım son", "çok kısa", "uydurma kelime", "tekrar eden ifade",
          "yer kayması", "iki kez tanıtılıyor", "kendi kendine", "kendini", "uydurma karakter adı",
          "özellik karışması", "kekeme tekrar", "ders olaydan kopuk", "plan bozuk"]


def olc(hikayeler):
    n = len(hikayeler)
    kelime = bilinmeyen = 0
    temiz = bitti = 0
    ceza_top = 0.0
    turler = {}
    for h in hikayeler:
        c = cezalar(h["metin"], h["kim"], h["n"], bitti=h["bitti"], plan=h.get("plan"))
        yc = yer_cezasi(h["metin"], h["yer"])
        ceza_top += sum(p for p, _ in c) + yc
        temiz += not c and not yc
        bitti += h["bitti"]
        for _, ad in c + ([(yc, "yer kayması")] if yc else []):
            tur = next((t for t in TURLER if t in ad), ad)
            turler[tur] = turler.get(tur, 0) + 1
        if SOZLUK is not None:
            w = re.findall(r"[a-zçğıöşüâîû]+", kucuk(h["metin"]))
            kelime += len(w)
            bilinmeyen += sum(x not in SOZLUK for x in w)
    sonuc = {
        "kurallari_gecen": f"{temiz}/{n}",
        "ort_ceza": round(ceza_top / n, 2),
        "biten": f"{bitti}/{n}",
        "uydurma_kelime_%": round(100 * bilinmeyen / max(1, kelime), 2) if SOZLUK is not None else None,
        "ort_token": round(sum(h["n"] for h in hikayeler) / n, 1),
        "ceza_turleri": dict(sorted(turler.items(), key=lambda x: -x[1])),
    }
    if any("plan" in h for h in hikayeler):  # yalnız plan modunda: eski çıktılar aynı kalır
        sonuc["plan_bozuk"] = f"{sum(bool(h.get('plan_bozuk')) for h in hikayeler)}/{n}"
    return sonuc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("--aday", type=int, default=8)
    ap.add_argument("--temp", type=float, default=0.5)
    ap.add_argument("--rep", type=float, default=1.1)
    ap.add_argument("--ad", default=None, help="aday havuzu adı: <model_dizini>/adaylar_<ad>.json")
    bayraklar(ap)
    a = ap.parse_args()
    ekler = ([a.baslik] if a.baslik != "eski" else []) + (["govde"] if a.pencere == "govde" else []) + \
        (["N"] if a.satir_yasak else []) + (["eot"] if a.eot_on else []) + \
        ([a.plan_kosul] if a.plan_kosul != "model" else []) + (["dog"] if a.dogrulama else [])
    ad = a.ad or "_".join(ekler) or "otomatik"
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    havuz = aday_havuzu(a.model_dir, ad, a.aday, a.temp, a.rep, tok, a.baslik, a.pencere, a.satir_yasak, a.eot_on,
                        a.plan_kosul, a.dogrulama)
    ilk, secilen = [], []
    for i, (kim, yer, _) in enumerate(vakalar(a.dogrulama)):
        adaylar = havuz[i]
        ilk.append(adaylar[0])
        secilen.append(max(adaylar, key=lambda h: puanla(h["metin"], kim, h["lp"], h["n"], yer, h["bitti"],
                                                            plan=h.get("plan"))))
    # eski komut satırlarında çıktı aynı kalsın: varsayılan değerdeki yeni ayarlar yazılmaz
    ayar = {k: v for k, v in vars(a).items() if k in ("model_dir", "aday", "temp", "rep") or v != ap.get_default(k)}
    sonuc = {"ayar": ayar, "seçicisiz": olc(ilk), f"en_iyi_{a.aday}": olc(secilen)}
    cikti = "otomatik.json" if ad == "otomatik" and not a.ad else f"otomatik_{ad}.json"
    json.dump(sonuc, open(os.path.join(a.model_dir, cikti), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
