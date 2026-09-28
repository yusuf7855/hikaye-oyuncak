"""Eğitilmiş ses modellerini karta aktarır: tek dosya ses.bin (+ C'yi sınamak için altın örnekler).

  python ses/disa_aktar.py --akustik ses_calisma/akustik/son.pt --vocoder ses_calisma/vocoder_gta/son.pt \
      --cikti ses.bin [--altin ses_altin.bin]

Kartta saklama (kuant.py ile birebir; model bu yuvarlamayla QAT eğitildi):
- Akustik: kuantize edilen her ağırlık (kuant._kuantize_edilecek) 4 bit, satır içinde 32'lik gruplar, grup başına
  fp16 ölçek (sütun sayısı 32'ye bölünmüyorsa grup = satırın tamamı; ör. derinlemesine evrişim, k=5 -> grup 5).
- Vocoder: 8 bit, satır başına float32 ölçek.
- Geri kalan küçük parametreler (LayerNorm, bias, gamma) fp16. istat buffer'ı float32. Hizalayıcı (hiz.*) gitmez.
Her tensör için kodlardan geri açılan değerin kuant.q_agirlik ile bit bit aynı olduğu doğrulanır.

Dosya düzeni (küçük uçlu):
  0   "SES1", sürüm u32, başlık baytı u32, tensör sayısı u32
  16  32 x i32 ayar (AYARLAR sırası)
  144 tensör tablosu, kayıt başına 64 B: ad[40] (NUL dolgulu), tip u8 (0 f32, 1 f16, 2 q4, 3 q8), 3 B boş,
      satır u32, sütun u32, grup u32, kod ofseti u32, ölçek ofseti u32 (yoksa 0)
  veri: her parça 16 bayta hizalı.
  q4: satır başına ceil(sütun/2) bayt, çift sütun alt nibble, değer q+8 (0..15); ölçekler fp16 [satır x grup_sayısı].
  q8: int8 [satır x sütun]; ölçekler float32 [satır].
  Adlar: akustik "a.<state_dict adı>", vocoder "v.<state_dict adı>". Çok boyutlu ağırlıklar [satır, geri kalan]
  olarak düzleşir (Conv1d [out, in, k] -> satır out, sütun in*k, sıra in dışta k içte).

Altın dosya ("SESA"): her örnek için metin (UTF-8), sembol kimlikleri; ses=1 ise süreler, mel [T x 80] ve dalga
(kırpılmamış float). Hepsi PyTorch'ta kartın ağırlıklarıyla (kuantize + fp16 küçük parametreler) hesaplanır.
"""
import argparse
import os
import struct
import sys

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kuant import _kuantize_edilecek, q_agirlik  # noqa: E402
from metin import N_SEMBOL, kodla  # noqa: E402
from model import Akustik, Vocoder  # noqa: E402
from ortak import HOP, N_FFT, N_MEL, SR  # noqa: E402

SIHIR, SURUM = b"SES1", 1
F32, F16, Q4, Q8 = 0, 1, 2, 3
GRUP = 32
AYARLAR = ["n_sembol", "n_mel", "n_fft", "hop", "sr", "a_d", "a_n_kod", "a_k_kod", "a_n_coz", "a_k_coz",
           "a_genis", "a_d_tah", "a_n_tah", "a_k_tah", "v_d", "v_n_blok", "v_genis", "v_k", "v_k_giris", "grup"]
ALTIN_CUMLELER = [
    "Bir varmış bir yokmuş.",
    "\"Yardım eder misin?\" diye sordu karınca.",
    "Güneş batarken arkadaşlar ağacın altında toplandı, birlikte güldüler!",
]
# yalnız metin -> kimlik denemesi (C'deki metin_kodla için zor durumlar)
METIN_DENEMELERI = [
    "İSTANBUL'DA IŞIK, ılık İğne ÇĞÖŞÜ çğöşü ÂÎÛ âîû",
    "“Merhaba” dedi… — ‘tek tırnak’ Alev'e O’na; iki:nokta!",
    "  boşluklar\t\tsekme\nsatır   sonu  ",
    "rakamlar 123 ve #@% işaretler _alt_çizgi_ qwx QWX é É ß",
    "K (Kelvin)   bölünmez boşluk İ̇ İ",
    "",
    "...!!!???",
    "Ağaç",
]


# ---------------------------------------------------------------- kuantizasyon (kuant.q_agirlik ile aynı)
def q4_kodla(w, grup=GRUP):
    """-> (kod baytları [satır x satır_bayt], fp16 ölçekler, grup, açılmış float)."""
    w2 = w.reshape(w.shape[0], -1).float()
    satir, cols = w2.shape
    g = grup if cols % grup == 0 else cols
    w3 = w2.reshape(satir, cols // g, g)
    s = w3.abs().amax(2, keepdim=True).clamp_min(1e-4) / 7
    s = s.half().float()
    q = torch.round(w3 / s).clamp(-8, 7)
    acik = (q * s).reshape(w.shape)
    assert torch.equal(acik, q_agirlik(w.float(), 4, grup)), "q4 kuant.q_agirlik ile uyuşmuyor"
    u = (q.reshape(satir, cols) + 8).to(torch.uint8).numpy()
    if cols % 2:
        u = np.concatenate([u, np.zeros((satir, 1), np.uint8)], 1)
    kod = (u[:, 0::2] | (u[:, 1::2] << 4)).astype(np.uint8)
    return kod.tobytes(), s.reshape(satir, -1).half().numpy().tobytes(), g, acik


def q8_kodla(w):
    w2 = w.reshape(w.shape[0], -1).float()
    s = w2.abs().amax(1, keepdim=True).clamp_min(1e-8) / 127
    q = torch.round(w2 / s).clamp(-127, 127)
    acik = (q * s).reshape(w.shape)
    assert torch.equal(acik, q_agirlik(w.float(), 8)), "q8 kuant.q_agirlik ile uyuşmuyor"
    return q.to(torch.int8).numpy().tobytes(), s.reshape(-1).numpy().astype(np.float32).tobytes(), acik


def kart_tensorleri(model, bit, onek):
    """Kartta saklanacak tensörler ve modelin kart karşılığı state_dict'i (açılmış değerlerle)."""
    params = dict(model.named_parameters())
    kayit, kart_sd = [], {}
    for ad, t in model.state_dict().items():
        if ad.startswith("hiz."):
            continue
        t = t.detach().cpu()
        satir = t.shape[0] if t.dim() else 1
        sutun = t.numel() // max(satir, 1)
        if ad in params and _kuantize_edilecek(ad, params[ad]):
            if bit == 4:
                kod, olcek, g, acik = q4_kodla(t)
                kayit.append((onek + ad, Q4, satir, sutun, g, kod, olcek))
            else:
                kod, olcek, acik = q8_kodla(t)
                kayit.append((onek + ad, Q8, satir, sutun, sutun, kod, olcek))
            kart_sd[ad] = acik
        elif ad in params:                                  # küçük parametre: fp16
            h = t.float().half()
            kayit.append((onek + ad, F16, 1, t.numel(), 0, h.numpy().tobytes(), b""))
            kart_sd[ad] = h.float().reshape(t.shape)
        else:                                               # buffer (istat): float32
            kayit.append((onek + ad, F32, 1, t.numel(), 0, t.float().numpy().tobytes(), b""))
            kart_sd[ad] = t
    return kayit, kart_sd


# ---------------------------------------------------------------- yükleme
def _sd(yol):
    k = torch.load(yol, map_location="cpu", weights_only=False)
    return k["model"] if isinstance(k, dict) and "model" in k else k


def _say(sd, onek):
    return len({k.split(".")[1] for k in sd if k.startswith(onek + ".")})


def akustik_kur(sd):
    d = sd["gomme.weight"].shape[1]
    m = Akustik(d=d, n_kod=_say(sd, "kod"), n_coz=_say(sd, "coz"), d_tah=sd["tah_giris.weight"].shape[0],
                n_tah=_say(sd, "tah"))
    m.load_state_dict(sd)
    return m.eval()


def vocoder_kur(sd):
    d = sd["giris.weight"].shape[0]
    n = _say(sd, "bloklar")
    m = Vocoder(d=d, n_blok=n, genis=sd["bloklar.0.pw1.weight"].shape[0] // d)
    m.load_state_dict(sd)
    return m.eval()


def ayarlar(ak, vo):
    b0, v0 = ak.kod[0], vo.bloklar[0]
    a = dict(n_sembol=N_SEMBOL, n_mel=N_MEL, n_fft=N_FFT, hop=HOP, sr=SR,
             a_d=ak.gomme.weight.shape[1], a_n_kod=len(ak.kod), a_k_kod=b0.dw.kernel_size[0],
             a_n_coz=len(ak.coz), a_k_coz=ak.coz[0].dw.kernel_size[0],
             a_genis=b0.pw1.weight.shape[0] // b0.pw1.weight.shape[1], a_d_tah=ak.tah_giris.weight.shape[0],
             a_n_tah=len(ak.tah), a_k_tah=ak.tah[0].dw.kernel_size[0],
             v_d=vo.giris.weight.shape[0], v_n_blok=len(vo.bloklar),
             v_genis=v0.pw1.weight.shape[0] // v0.pw1.weight.shape[1], v_k=v0.dw.kernel_size[0],
             v_k_giris=vo.giris.kernel_size[0], grup=GRUP)
    assert ak.gomme.weight.shape[0] == N_SEMBOL
    for bl in list(ak.kod) + list(ak.coz):  # C tek genişlik varsayar
        assert bl.pw1.weight.shape[0] == a["a_genis"] * a["a_d"]
    return a


# ---------------------------------------------------------------- yazma
def _hizala(b, n=16):
    return b + b"\0" * (-len(b) % n)


def ses_bin_yaz(yol, ayar, kayitlar):
    n = len(kayitlar)
    baslik = 16 + 32 * 4 + 64 * n
    ofs = (baslik + 15) // 16 * 16
    tablo, veri = b"", b""
    for ad, tip, satir, sutun, g, kod, olcek in kayitlar:
        ab = ad.encode()
        assert len(ab) < 40, ad
        k_ofs = ofs + len(veri)
        veri += _hizala(kod)
        o_ofs = 0
        if olcek:
            o_ofs = ofs + len(veri)
            veri += _hizala(olcek)
        tablo += struct.pack("<40sB3xIIIII", ab, tip, satir, sutun, g, k_ofs, o_ofs)
    a = [ayar[k] for k in AYARLAR] + [0] * (32 - len(AYARLAR))
    bas = SIHIR + struct.pack("<III", SURUM, baslik, n) + struct.pack("<32i", *a) + tablo
    icerik = _hizala(bas) + veri
    assert len(_hizala(bas)) == ofs
    with open(yol, "wb") as f:
        f.write(icerik)
    return len(icerik)


@torch.no_grad()
def altin_yaz(yol, ak_k, vo_k, cumleler, metinler):
    """ak_k/vo_k: kartın ağırlıklarını taşıyan modeller."""
    out = [b"SESA", struct.pack("<I", len(cumleler) + len(metinler))]
    ozet = []
    for metin in cumleler + metinler:
        mb = metin.encode("utf-8")
        ids = kodla(metin)
        out += [struct.pack("<I", len(mb)), mb, struct.pack("<I", len(ids)), np.array(ids, np.int32).tobytes()]
        if metin not in cumleler or not ids:
            out.append(struct.pack("<I", 0))
            continue
        x = torch.tensor([ids])
        # süreler: Akustik.uret ile aynı satırlar (hiz=1)
        m_maske = torch.ones(x.shape)
        h, _ = ak_k.kodla(x, m_maske)
        tah = ak_k.tahmin(h, m_maske)
        sure = torch.clamp(torch.round(torch.exp(tah[..., 0]) - 1), min=1).long()[0]
        mel = ak_k.uret(x)[0]                                     # [80, T] (asıl yol)
        assert mel.shape[1] == int(sure.sum())
        dalga = vo_k(mel[None])[0]
        out += [struct.pack("<II", 1, mel.shape[1]), sure.numpy().astype(np.int32).tobytes(),
                mel.T.contiguous().numpy().astype(np.float32).tobytes(),
                struct.pack("<I", dalga.numel()), dalga.numpy().astype(np.float32).tobytes()]
        ozet.append((metin, len(ids), mel.shape[1], dalga.numel()))
    with open(yol, "wb") as f:
        f.write(b"".join(out))
    return ozet


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--akustik", required=True)
    ap.add_argument("--vocoder", required=True)
    ap.add_argument("--cikti", default="ses.bin")
    ap.add_argument("--altin", default=None, help="altın örnek dosyası (C denemesi için)")
    ap.add_argument("--cumle", action="append", default=None, help="altın cümle (birden çok verilebilir)")
    ap.add_argument("--butce", type=float, default=0x440000, help="ses bölümü (bayt)")
    a = ap.parse_args()
    torch.set_num_threads(1)
    ak = akustik_kur(_sd(a.akustik))
    vo = vocoder_kur(_sd(a.vocoder))
    ayar = ayarlar(ak, vo)
    ka, sd_a = kart_tensorleri(ak, 4, "a.")
    kv, sd_v = kart_tensorleri(vo, 8, "v.")
    boyut = ses_bin_yaz(a.cikti, ayar, ka + kv)
    ba = sum(len(_hizala(k[5])) + len(_hizala(k[6])) for k in ka)
    bv = sum(len(_hizala(k[5])) + len(_hizala(k[6])) for k in kv)
    print(f"ayarlar: " + " ".join(f"{k}={ayar[k]}" for k in AYARLAR))
    print(f"akustik {sum(p.numel() for n, p in ak.named_parameters() if not n.startswith('hiz.')) / 1e6:.3f} M"
          f" -> {ba / 1e6:.3f} MB | vocoder {sum(p.numel() for p in vo.parameters()) / 1e6:.3f} M -> {bv / 1e6:.3f} MB")
    print(f"{a.cikti}: {boyut} B = {boyut / 1048576:.3f} MiB ({len(ka) + len(kv)} tensör); bölüm {int(a.butce)} B, "
          f"{'SIĞAR' if boyut <= a.butce else 'SIĞMAZ!'} (boş {int(a.butce) - boyut} B)")
    if boyut > a.butce:
        sys.exit(1)
    if a.altin:
        sd_a.update({k: v for k, v in ak.state_dict().items() if k.startswith("hiz.")})
        ak_k = akustik_kur(sd_a)
        vo_k = vocoder_kur(sd_v)
        ozet = altin_yaz(a.altin, ak_k, vo_k, a.cumle or ALTIN_CUMLELER, METIN_DENEMELERI)
        for m, n, t, s in ozet:
            print(f"altın: {n} sembol, {t} kare, {s} örnek ({s / SR:.2f} s): {m}")
        print(f"yazıldı: {a.altin}")


if __name__ == "__main__":
    main()
