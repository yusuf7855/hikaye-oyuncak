"""KWS değerlendirmesi: kartın int8 hesabıyla (ortak.tamsayi_ileri = kws.h) uzun akışlarda ölçer, eşik seçer.

  .venv/bin/python ses/kws/degerlendir.py [--model ses_kws_veri/calisma/qat.pt] [--yaz]

Sınama verisi GÖRÜLMEMİŞ seslerle (Supertonic F4, M5 ve karışımları) ve sınamaya ayrılmış söyleyişlerle
(ifadeler.py "deneme") sentezlendi; hikâye cümleleri de eğitimde olmayan data/urun_v3'ten.
  * olumlu akış: her deneme ~8 sn: "Merhaba Eko" (+ %75 0,3–1,2 sn sonra komut); koşullar: sessiz oda, ev gürültüsü
    10/5 dB, hoparlörden hikâye sesi 10/0 dB (çocuk sesine göre), güçlü yankı, eğitimde olmayan süpürge sesi.
  * olumsuz akışlar: (a) yalnız hikâye okuması (kartın hoparlöründen, yüksek), (b) çocuk/yetişkin başka konuşma
    (karışan sözcükler: "Merhaba", "Eko", "Merhaba Ece", "Uykum geldi" ...), (c) yalnız ev gürültüsü,
    (d) konuşma + hikâye sesi birlikte. Ölçü: saatte yanlış uyanma.
Eşik seçimi: --yaz verilirse dev akışlarında (eğitim seslerinin ayrılmış %5'i + eğitim cümleleri) saatte en çok
--hedef-yu yanlış uyanma koşuluyla uyanma oranını en yükselten eşikler seçilir ve kayda (son_islem) yazılır.
Sınama sonuçları seçilen eşikte raporlanır (eşikler sınamaya bakılarak seçilmez); ayrıca eşik tablosu basılır.
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import torch
from scipy.signal import fftconvolve

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
sys.path.insert(0, BURASI)
import disa_aktar as D  # noqa: E402
import ifadeler as IF  # noqa: E402
import ortak as O  # noqa: E402
import veri as V  # noqa: E402

SR = O.SR
HAM = os.path.join(KOK, "ses_kws_veri", "ham")
CALISMA = os.path.join(KOK, "ses_kws_veri", "calisma")
KOMUTLAR = [s for s in IF.POZITIF if s != "UYANDIRMA"]


def supurge(rng, n):
    """Eğitimde olmayan gürültü: elektrik süpürgesi (motor uğultusu + hava sesi, yavaş genlik dalgası)."""
    t = np.arange(n) / SR
    f = rng.uniform(150, 400)
    motor = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 12))
    hava = V.suzgec(V.renkli_gurultu(rng, n, 0.5), "bandpass", [rng.uniform(500, 1500), rng.uniform(4000, 7000)])
    y = (0.3 * motor / V.rms(motor) + hava) * (1 + 0.2 * np.sin(2 * np.pi * rng.uniform(0.2, 1) * t))
    return (y / V.rms(y)).astype(np.float32)


def gurultu(rng, n, tur):
    if tur == "supurge":
        return supurge(rng, n)
    k = rng.integers(0, 6)
    if k < 3:
        return V.renkli_gurultu(rng, n, k)
    return [V.vantilator, V.tikirti, V.muzik][k - 3](rng, n)


def klip(k, rng, seviye_db):
    x = k.x.astype(np.float32) / 32768.0
    return x * V.db(seviye_db) / (V.rms(x[k.bas:k.son]) + 1e-9)


def sizinti_akisi(rng, cumle, n):
    """Kartın hoparlöründen hikâye: cümleler art arda (0,25 sn ara), küçük hoparlör benzetimi; rms 1'e."""
    y = np.zeros(n, np.float32)
    t = 0
    while t < n:
        k = cumle[rng.integers(len(cumle))]
        x = k.x.astype(np.float32) / 32768.0
        x /= V.rms(x[k.bas:k.son]) + 1e-9
        b = min(n, t + len(x))
        y[t:b] += x[: b - t]
        t += len(x) + int(rng.uniform(0.2, 0.4) * SR)
    parca = []
    for a in range(0, n, 10 * SR):  # hoparlör/oda 10 sn'de bir değişsin
        parca.append(V.hoparlor(rng, y[a:a + 10 * SR]))
    y = np.concatenate(parca)
    return y / (V.rms(y) + 1e-9)


def bitir(rng, y):
    y = V.mikrofon(rng, y) + rng.standard_normal(len(y)).astype(np.float32) * V.db(-85)
    return np.clip(np.round(y * 32767), -32768, 32767).astype(np.int16)


def olumlu_akis(h, kosul, n_deneme, tohum, sizinti_kaynagi):
    rng = np.random.default_rng(tohum)
    uz = int(8.5 * SR)
    N = uz * n_deneme
    on = np.zeros(N, np.float32)
    dogru = []
    for i in range(n_deneme):
        t0 = i * uz + int(rng.uniform(0.6, 1.2) * SR)
        ku = h["poz"]["UYANDIRMA"][rng.integers(len(h["poz"]["UYANDIRMA"]))]
        sev = rng.uniform(-35, -20)
        xw = klip(ku, rng, sev)
        on[t0: t0 + len(xw)] += xw
        rec = dict(uyan_bas=(t0 + ku.bas) / SR, uyan_son=(t0 + ku.son) / SR, uyan_tur=ku.tur + ("/" + ku.ozel if ku.ozel else ""), metin=ku.metin)
        s = KOMUTLAR[i % len(KOMUTLAR)]
        if rng.random() < 0.75 and h["poz"][s]:
            kc = h["poz"][s][rng.integers(len(h["poz"][s]))]
            xc = klip(kc, rng, sev + rng.uniform(-4, 4))
            tc = t0 + ku.son + int(rng.uniform(0.3, 1.2) * SR) - kc.bas
            on[tc: tc + len(xc)] += xc
            rec.update(komut=s, komut_son=(tc + kc.son) / SR, komut_metin=kc.metin)
        dogru.append(rec)
    oda = V.yanki(rng, rt=rng.uniform(0.9, 1.2)) if kosul == "yanki" else V.yanki(rng)  # yankı: eğitimdekinden uzun
    on = fftconvolve(on, oda)[:N].astype(np.float32)
    konusma_rms = V.db(-28)
    y = on + V.renkli_gurultu(rng, N, 1) * V.db(-70)
    if kosul.startswith("gurultu") or kosul in ("supurge", "yanki"):
        snr = {"gurultu_10": 10, "gurultu_5": 5, "supurge": 5, "yanki": 15}[kosul]
        tur = "supurge" if kosul == "supurge" else "karisik"
        parca = [gurultu(rng, min(10 * SR, N - a), tur) for a in range(0, N, 10 * SR)]
        y += np.concatenate(parca) * konusma_rms * V.db(-snr)
    if kosul.startswith("hikaye"):
        snr = {"hikaye_10": 10, "hikaye_0": 0}[kosul]
        y += sizinti_akisi(rng, sizinti_kaynagi, N) * konusma_rms * V.db(-snr)
    return bitir(rng, y), dogru


def olumsuz_akis(h, tur, tohum, sure_s=None):
    """tur: dogal (karışan olmayan sözler + çocuk sesli cümleler), karisan (yalnız karışan ifadeler, aralıklı),
    karisik (dogal + hoparlörden hikâye), hikaye (yalnız hoparlörden hikâye), gurultu."""
    rng = np.random.default_rng(tohum)
    olaylar = []
    if tur in ("dogal", "karisik", "karisan"):
        if tur == "karisan":
            kl = [k for k in h["neg"] if IF.karisan_mi(k.metin)]
        else:
            kl = [k for k in h["neg"] if not IF.karisan_mi(k.metin)] + [k for k in h["cumle"] if k.tur == "cocuk"]
        rng.shuffle(kl)
        parcalar, t = [], 0
        for k in kl:
            bos = int((rng.uniform(1.5, 3.0) if tur == "karisan" else rng.uniform(0.3, 2.0)) * SR)
            x = klip(k, rng, rng.uniform(-35, -15))
            parcalar += [np.zeros(bos, np.float32), x]
            olaylar.append(((t + bos + k.bas) / SR, (t + bos + k.son) / SR, k.metin))
            t += bos + len(x)
        on = np.concatenate(parcalar)
        N = len(on)
        on = np.concatenate([fftconvolve(on[a:a + 30 * SR], V.yanki(rng))[: min(30 * SR, N - a)]
                             for a in range(0, N, 30 * SR)]).astype(np.float32)
        y = on + V.renkli_gurultu(rng, N, 1) * V.db(-65)
        if tur == "karisik":
            y += sizinti_akisi(rng, [k for k in h["cumle"] if k.tur != "cocuk"], N) * V.db(rng.uniform(-28, -18))
    elif tur == "hikaye":
        cumle = [k for k in h["cumle"] if k.tur != "cocuk"]
        N = int(sum(len(k.x) for k in cumle) * 1.08) if sure_s is None else int(sure_s * SR)
        y = np.concatenate([sizinti_akisi(rng, cumle, min(60 * SR, N - a)) * V.db(rng.uniform(-30, -8))
                            for a in range(0, N, 60 * SR)])
        y += V.renkli_gurultu(rng, N, 1) * V.db(-70)
    else:  # gurultu
        N = int((sure_s or 1200) * SR)
        y = np.concatenate([gurultu(rng, min(10 * SR, N - a), "karisik") * V.db(rng.uniform(-60, -20))
                            for a in range(0, N, 10 * SR)])
    return bitir(rng, y), olaylar


def karisan_olc(olaylar_kare, ifadeler):
    """Her karışan söyleyiş için: [bas-0.2, son+0.8] içinde uyanma oldu mu -> (oran, {ifade: [uyandı, toplam]})."""
    ts = np.array([(t * O.ADIM + O.PENCERE) / SR for t, o in olaylar_kare if o == 1])
    tablo = {}
    for a, b, m in ifadeler:
        u = bool(len(ts) and np.any((ts >= a - 0.2) & (ts <= b + 0.8)))
        n = IF._norm(m)
        tablo.setdefault(n, [0, 0])
        tablo[n][0] += u
        tablo[n][1] += 1
    top = sum(v[0] for v in tablo.values()) / max(1, sum(v[1] for v in tablo.values()))
    return top, tablo


def olasiliklar(tm, pcm, parca=20000, baglam=200):
    """Uzun akış: parça parça (bellek). Nedensel ve alıcı alanı 135 kare: 200 karelik ön bağlamla sonuç tam aynı."""
    q = np.concatenate([O.oznitelik_np(pcm[a * O.ADIM: (a + parca) * O.ADIM + O.PENCERE - O.ADIM])
                        for a in range(0, max(1, 1 + (len(pcm) - O.PENCERE) // O.ADIM), parca)])
    out = []
    for a in range(0, len(q), parca):
        b0 = max(0, a - baglam)
        lg = O.tamsayi_ileri(tm, q[b0: a + parca]).numpy()[a - b0:]
        out.append(lg.astype(np.float64) * np.float32(tm["cikis"]["olcek"]))
    lg = np.concatenate(out)
    p = np.exp(lg - lg.max(1, keepdims=True))
    return p / p.sum(1, keepdims=True)


def kare(t):
    return int(round(t * SR - O.PENCERE) / O.ADIM)


def olumlu_olc(olaylar, dogru):
    """Her deneme: uyanma [uyan_bas, uyan_son+1.0] içinde mi (erken, "Merhaba E.." sırasında uyanmak da sayılır);
    komut doğru mu (pencerede ilk komut)."""
    sonuc = []
    ol = sorted(olaylar)
    for d in dogru:
        a, b = kare(d["uyan_bas"]), kare(d["uyan_son"] + 1.0)
        uy = [t for t, o in ol if o == 1 and a <= t <= b]
        r = dict(uyandi=bool(uy), tur=d["uyan_tur"], komut=d.get("komut"))
        if uy:
            son = uy[0] + int(4.2 * O.KARE_HZ)
            k = [o for t, o in ol if uy[0] < t <= son and o >= 2]
            r["cikan"] = IF.SINIFLAR[k[0] + 1] if k else None
        sonuc.append(r)
    return sonuc


def ozet_olumlu(s):
    n = len(s)
    uy = np.mean([r["uyandi"] for r in s])
    km = [r for r in s if r["komut"]]
    kd = [r for r in km if r["uyandi"]]
    dog = np.mean([r.get("cikan") == r["komut"] for r in kd]) if kd else float("nan")
    uc = np.mean([r["uyandi"] and r.get("cikan") == r["komut"] for r in km]) if km else float("nan")
    bos = [r for r in s if not r["komut"] and r["uyandi"]]
    yk = np.mean([r.get("cikan") is not None for r in bos]) if bos else float("nan")
    return dict(n=n, uyanma=uy, komut_dogru_uyaninca=dog, uctan_uca=uc, bos_pencerede_komut=yk)


def yanlis_uyanma(olaylar, sure_s):
    return sum(1 for _, o in olaylar if o == 1) / (sure_s / 3600)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=os.path.join(CALISMA, "qat.pt"))
    ap.add_argument("--yaz", action="store_true", help="dev'de seçilen eşikleri kayda yaz")
    ap.add_argument("--hedef-yu", type=float, default=0.5, help="dev'de (doğal konuşma + hikâye sesi) saatte en çok yanlış uyanma")
    ap.add_argument("--hedef-karisan", type=float, default=0.05, help="dev'de karışan ifadelerde en çok uyanma oranı")
    ap.add_argument("--deneme", type=int, default=160, help="koşul başına olumlu deneme")
    ap.add_argument("--parcacik", type=int, default=2)
    ap.add_argument("--cikti", default=os.path.join(CALISMA, "sonuc.json"))
    a = ap.parse_args()
    torch.set_num_threads(a.parcacik)
    t0 = time.time()
    net, kayit = D.yukle(a.model)
    net.qat_ac(True)
    tm = O.tamsayi_model(net.eval())

    sinama = V.havuz_yukle(HAM, ["poz_sinama", "neg_sinama", "cumle_sinama"])
    dev = V.havuz_yukle(HAM, ["poz_egitim", "neg_egitim", "cumle_egitim"], "dev")
    egit_cumle = V.havuz_yukle(HAM, ["cumle_egitim"], "egitim")["cumle"]
    print(f"sınama: {V.havuz_ozet(sinama)}\ndev: {V.havuz_ozet(dev)} ({time.time() - t0:.0f} sn)", flush=True)

    # ---------------- dev: eşik seçimi
    izgara_u = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97]
    izgara_k = [0.4, 0.5, 0.6, 0.7, 0.8]
    yumusat = [3, 5]
    dev_poz = []
    for i, kosul in enumerate(["sessiz", "gurultu_5", "hikaye_0"]):
        pcm, dg = olumlu_akis(dev, kosul, 60, 500 + i, egit_cumle)
        dev_poz.append((olasiliklar(tm, pcm), dg))
    dev_neg = []
    dn = dict(neg=dev["neg"], cumle=dev["cumle"] + egit_cumle[:300], poz=dev["poz"])
    for i, tur in enumerate(["dogal", "hikaye", "karisik"]):
        pcm, _ = olumsuz_akis(dn, tur, 600 + i, sure_s=1200 if tur == "hikaye" else None)
        dev_neg.append((olasiliklar(tm, pcm), len(pcm) / SR))
    pcm, dev_kar_ol = olumsuz_akis(dn, "karisan", 610)
    dev_kar = olasiliklar(tm, pcm)
    dev_sure = sum(s for _, s in dev_neg)
    print(f"dev: olumsuz {dev_sure / 3600:.2f} saat + {len(dev_kar_ol)} karışan söyleyiş ({time.time() - t0:.0f} sn)",
          flush=True)
    secim, en = None, None
    for y in yumusat:
        for eu in izgara_u:
            yu = sum(len([1 for _, o in O.SonIslem(eu, 0.5, y).olaylar(p) if o == 1]) for p, _ in dev_neg)
            yu_h = yu / (dev_sure / 3600)
            kr, _ = karisan_olc(O.SonIslem(eu, 0.5, y).olaylar(dev_kar), dev_kar_ol)
            for ek in izgara_k:
                ss = []
                for p, dg in dev_poz:
                    ss += olumlu_olc(O.SonIslem(eu, ek, y).olaylar(p), dg)
                oz = ozet_olumlu(ss)
                puan = np.nan_to_num(oz["uctan_uca"]) - 0.5 * np.nan_to_num(oz["bos_pencerede_komut"])
                if yu_h <= a.hedef_yu and kr <= a.hedef_karisan and (en is None or puan > en):
                    en, secim = puan, dict(esik_uyan=eu, esik_komut=ek, yumusat=y, dev_yu_saat=yu_h, dev_karisan=kr,
                                           dev=oz)
    if secim is None:
        secim = dict(esik_uyan=0.95, esik_komut=0.6, yumusat=5, dev_yu_saat=None, dev=None)
        print("UYARI: dev hedefleri hiçbir eşikte tutmadı; en yüksek eşik kullanılıyor")
    print("dev'de seçilen:", json.dumps(secim, ensure_ascii=False, default=float), flush=True)

    # ---------------- sınama
    sonuc = dict(esik=secim, olumlu={}, olumsuz={}, kosul_tablo={})
    sizinti_kaynagi = [k for k in sinama["cumle"] if k.tur != "cocuk"]
    poz_p = {}
    for i, kosul in enumerate(["sessiz", "gurultu_10", "gurultu_5", "hikaye_10", "hikaye_0", "yanki", "supurge"]):
        pcm, dg = olumlu_akis(sinama, kosul, a.deneme, 100 + i, sizinti_kaynagi)
        poz_p[kosul] = (olasiliklar(tm, pcm), dg)
    neg_p = {}
    for i, tur in enumerate(["hikaye", "dogal", "gurultu", "karisik"]):
        pcm, ol = olumsuz_akis(sinama, tur, 200 + i, sure_s=1800 if tur == "gurultu" else None)
        neg_p[tur] = (olasiliklar(tm, pcm), len(pcm) / SR, ol)
    print(f"sınama akışları hazır ({time.time() - t0:.0f} sn)", flush=True)

    si = O.SonIslem(secim["esik_uyan"], secim["esik_komut"], secim["yumusat"])
    hepsi = []
    print("\n## Sınama (görülmemiş sesler), seçilen eşik: uyanma %.2f, komut %.2f, yumuşatma %d kare" %
          (secim["esik_uyan"], secim["esik_komut"], secim["yumusat"]))
    print("| koşul | deneme | uyanma oranı | komut doğru (uyanınca) | uçtan uca (uyanma+doğru komut) | boş pencerede yanlış komut |")
    print("|---|---|---|---|---|---|")
    for kosul, (p, dg) in poz_p.items():
        s = olumlu_olc(si.olaylar(p), dg)
        hepsi += s
        oz = ozet_olumlu(s)
        sonuc["olumlu"][kosul] = oz
        print(f"| {kosul} | {oz['n']} | {oz['uyanma']:.3f} | {oz['komut_dogru_uyaninca']:.3f} | {oz['uctan_uca']:.3f} | "
              f"{oz['bos_pencerede_komut']:.3f} |")
    # komut başına ve karışıklık
    kar = {s: {} for s in KOMUTLAR}
    for r in hepsi:
        if r["komut"] and r["uyandi"]:
            c = r.get("cikan") or "(yok)"
            kar[r["komut"]][c] = kar[r["komut"]].get(c, 0) + 1
    print("\n| komut | doğru oranı (uyanınca) | karışıklık |\n|---|---|---|")
    for s in KOMUTLAR:
        n = sum(kar[s].values())
        print(f"| {s} | {kar[s].get(s, 0) / max(n, 1):.3f} ({n}) | " +
              ", ".join(f"{k}:{v}" for k, v in sorted(kar[s].items(), key=lambda x: -x[1]) if k != s) + " |")
    sonuc["karisiklik"] = kar
    turler = {}
    for r in hepsi:
        turler.setdefault(r["tur"], []).append(r["uyandi"])
    print("\nuyanma oranı ses türüne göre: " + ", ".join(f"{k}: {np.mean(v):.3f} ({len(v)})" for k, v in turler.items()))
    sonuc["tur"] = {k: float(np.mean(v)) for k, v in turler.items()}

    print("\n| olumsuz akış | süre (saat) | yanlış uyanma / saat | uyandırmasız komut tetiklenmesi / saat (yalnız tanı) |")
    print("|---|---|---|---|")
    tetik = {}
    for tur, (p, sure, ol) in neg_p.items():
        ev = si.olaylar(p)
        yu = yanlis_uyanma(ev, sure)
        serbest = O.SonIslem(secim["esik_uyan"], secim["esik_komut"], secim["yumusat"], kapali_komut=True).olaylar(p)
        kom = sum(1 for _, o in serbest if o >= 2) / (sure / 3600)
        sonuc["olumsuz"][tur] = dict(saat=sure / 3600, yanlis_uyanma_saat=yu, adet=sum(1 for _, o in ev if o == 1),
                                     serbest_komut_saat=kom)
        print(f"| {tur} | {sure / 3600:.2f} | {yu:.2f} ({sum(1 for _, o in ev if o == 1)} adet) | {kom:.1f} |")
        for t, o in ev:
            if o == 1 and ol:
                ts = (t * O.ADIM + O.PENCERE) / SR
                m = [x for a_, b_, x in ol if a_ - 0.2 <= ts <= b_ + 0.8]
                if m:
                    tetik[m[0]] = tetik.get(m[0], 0) + 1
    pcm, kar_ol = olumsuz_akis(sinama, "karisan", 210)
    kr, tablo = karisan_olc(si.olaylar(olasiliklar(tm, pcm)), kar_ol)
    print(f"\nkarışan ifadeler (\"Merhaba\", \"Eko\", \"Merhaba Ece\" ...): {sum(v[1] for v in tablo.values())} söyleyişin "
          f"%{100 * kr:.1f}'i uyandırdı")
    kotu = sorted(((v[0] / v[1], k, v) for k, v in tablo.items() if v[0]), reverse=True)[:15]
    if kotu:
        print("en çok uyandıranlar: " + ", ".join(f"{k} {v[0]}/{v[1]}" for _, k, v in kotu))
    sonuc["karisan"] = dict(oran=kr, tablo=tablo)
    if tetik:
        print("yanlış uyandıran ifadeler:", ", ".join(f"{k} x{v}" for k, v in sorted(tetik.items(), key=lambda x: -x[1])[:20]))
    sonuc["yanlis_uyandiran"] = tetik

    # eşik tablosu (sınamada; bilgi için)
    print("\n| eşik (uyanma) | uyanma oranı (tüm koşullar) | yanlış uyanma / saat (tüm olumsuzlar) |\n|---|---|---|")
    top_sure = sum(s for _, s, _ in neg_p.values())
    for eu in izgara_u:
        si2 = O.SonIslem(eu, secim["esik_komut"], secim["yumusat"])
        uy = np.mean([r["uyandi"] for p, dg in poz_p.values() for r in olumlu_olc(si2.olaylar(p), dg)])
        yu = sum(sum(1 for _, o in si2.olaylar(p) if o == 1) for p, _, _ in neg_p.values()) / (top_sure / 3600)
        sonuc["kosul_tablo"][str(eu)] = dict(uyanma=float(uy), yu_saat=float(yu))
        print(f"| {eu:.2f} | {uy:.3f} | {yu:.2f} |")
    with open(a.cikti, "w", encoding="utf-8") as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=1, default=float)
    if a.yaz:
        kayit["son_islem"] = dict(esik_uyan=secim["esik_uyan"], esik_komut=secim["esik_komut"], yumusat=secim["yumusat"])
        torch.save(kayit, a.model)
        print("eşikler kayda yazıldı:", a.model)
    print(f"bitti ({time.time() - t0:.0f} sn)")


if __name__ == "__main__":
    main()
