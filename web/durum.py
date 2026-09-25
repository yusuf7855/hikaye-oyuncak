"""Eğitim durumunu tek bir JSON belgesinde topla (Hikâye Atölyesi'ndeki "Eğitim" paneli için).

Kullanım: .venv/bin/python web/durum.py <çıktı.json>
Okur: runs/*.progress.json (train.py her checkpoint'te yazar) ve web/olaylar.json (elle eklenen kilometre
taşları: "v1 yayında" gibi). Aşama sırası AŞAMALAR'da; her aşama bir eğitim etiketine bağlıdır.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AŞAMALAR = [
    {"ad": "Ön-eğitim (C2)", "etiket": "ple-c2-s0", "aciklama": "Türkçe TinyStories, 52M token, figür isimleri tek token"},
    {"ad": "Ara ince ayar", "etiket": "ple-c2ara-s0", "aciklama": "6000. adımdaki ön-eğitimden oyuncak hikâyeleri (v1 önizleme)"},
    {"ad": "Tema deneyi (E1)", "etiket": "ple-c2ara_tema-s0", "aciklama": "Aynı ara ince ayar, başlıkta hikâyenin teması da var: olay örgüsü daha mantıklı mı?"},
    {"ad": "Yeni taban R (C2)", "etiket": "ple-c2ft-s0", "aciklama": "Tam ön-eğitimden oyuncak hikâyeleri: sabit bölme, sızıntı temizliği, temasız başlık, 4-bit QAT"},
    {"ad": "R-temiz", "etiket": "ple-c2ft_temiz-s0", "aciklama": "R'nin aynısı, denetimde bozuk bulunan 289 hikâye çıkarılmış"},
    {"ad": "E2 · hizalı pencereler", "etiket": "ple-c2ft_hiz-s0", "aciklama": "R'nin aynısı, eğitim pencereleri hikâye başına hizalı"},
    {"ad": "E3 · önce plan", "etiket": "ple-c2ft_plan-s0", "aciklama": "R'nin aynısı, model hikâyeden önce Sorun/Çözüm planı yazıyor"},
    {"ad": "Tur 1 · E4 oyuncak payı", "etiket": "ple-c2ft_e4-s0", "aciklama": "E3'ün aynısı, genel veri 8M -> 4M token: eğitimin %32'si oyuncak hikâyesi (önce %15)"},
]


def surec_durumu(etiket):
    """ple-<tag>-s0 eğitim sürecinin durumu: 'T' (duraklatılmış, SIGSTOP), 'R'/'S' (çalışıyor) ya da None."""
    tag = etiket[len("ple-"):-len("-s0")]
    for pid in filter(str.isdigit, os.listdir("/proc")):
        try:
            args = open(f"/proc/{pid}/cmdline", "rb").read().split(b"\0")
            if b"research.tinystories.train" in args and args[args.index(b"--tag") + 1].decode() == tag:
                return open(f"/proc/{pid}/stat").read().rsplit(")", 1)[1].split()[0]
        except (OSError, ValueError, IndexError):
            pass
    return None


def oku(etiket):
    yol = os.path.join(ROOT, "runs", f"{etiket}.progress.json")
    if not os.path.exists(yol):
        return None
    d = json.load(open(yol))
    durum = d.get("status")
    if durum == "training" and surec_durumu(etiket) == "T":
        durum = "duraklatildi"
    return {
        "durum": durum, "adim": d.get("step"), "toplam": d.get("steps"),
        "train": round(d["train_loss"], 4) if d.get("train_loss") is not None else None,
        "sn_adim": round(d.get("sec_per_step") or 0, 3), "kalan_sn": int(d.get("eta_seconds") or 0),
        "gecen_sn": int(d.get("elapsed") or 0), "guncel": int(d.get("updated") or os.path.getmtime(yol)),
        "egri": [{"adim": h["step"], "val": round(h["val"], 4), "train": round(h["train"], 4)}
                 for h in d.get("history", []) if h.get("val") is not None],
    }


def main():
    olaylar_yol = os.path.join(HERE, "olaylar.json")
    olaylar = json.load(open(olaylar_yol, encoding="utf-8")) if os.path.exists(olaylar_yol) else []
    asamalar = []
    for a in AŞAMALAR:
        d = oku(a["etiket"])
        asamalar.append({**a, **(d or {"durum": "bekliyor"})})
    belge = {"guncellendi": int(time.time()), "asamalar": asamalar, "olaylar": olaylar[-12:]}
    json.dump(belge, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False)
    for a in asamalar:
        print(a["ad"], a.get("durum"), a.get("adim"), "/", a.get("toplam"))


if __name__ == "__main__":
    main()
