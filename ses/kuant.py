"""Kart için kuantizasyon: ağırlıkları kartta nasıl saklanacaklarsa öyle yuvarla.

- Akustik: 4 bit, satır içinde 32'lik gruplar (grup başına fp16 ölçek). LLM'deki q4 çekirdeğiyle aynı düzen.
- Vocoder: 8 bit, satır başına ölçek.
LayerNorm, bias, gamma ve küçük vektörler float kalır (kartta da float).

Kuantizasyonu hesaba katan eğitim (QAT): `with kuantize(model, bit):` içinde ileri + geri yapılır, sonra
float ağırlıklar geri yüklenip optimizer adımı atılır. Gradyan yuvarlanmış noktada hesaplanır, güncelleme
float ağırlığa gider (STE / BinaryConnect).
"""
import contextlib

import torch


def _kuantize_edilecek(ad, p):
    return p.dim() >= 2 and p.numel() >= 256 and not ad.startswith("hiz.")


def q_agirlik(w, bit, grup=32):
    """w -> kartta saklanacak değerin float karşılığı."""
    w2 = w.reshape(w.shape[0], -1)
    cols = w2.shape[1]
    if bit == 8:
        s = w2.abs().amax(1, keepdim=True).clamp_min(1e-8) / 127
        return (torch.round(w2 / s).clamp(-127, 127) * s).reshape(w.shape)
    g = grup if cols % grup == 0 else cols
    w3 = w2.reshape(w2.shape[0], cols // g, g)
    s = w3.abs().amax(2, keepdim=True).clamp_min(1e-4) / 7   # (sıfır grup: fp16 ölçek 0 olmasın)
    s = s.half().float()                              # kartta fp16 ölçek
    q = torch.round(w3 / s).clamp(-8, 7)
    return (q * s).reshape(w.shape)


@contextlib.contextmanager
def kuantize(model, bit):
    """Ağırlıkları geçici olarak kuantize değerlerle değiştirir; çıkışta float değerleri geri koyar."""
    yedek = {}
    with torch.no_grad():
        for ad, p in model.named_parameters():
            if _kuantize_edilecek(ad, p):
                yedek[ad] = p.data.clone()
                p.data.copy_(q_agirlik(p.data, bit))
    try:
        yield
    finally:
        with torch.no_grad():
            for ad, p in model.named_parameters():
                if ad in yedek:
                    p.data.copy_(yedek[ad])


def kart_boyutu(model, bit, grup=32, haric=("hiz.",)):
    """Kartta kaç bayt tutar (yaklaşık; başlıklar hariç)."""
    top = 0
    for ad, p in model.named_parameters():
        if any(ad.startswith(h) for h in haric):
            continue
        if _kuantize_edilecek(ad, p):
            satir, cols = p.shape[0], p.numel() // p.shape[0]
            if bit == 8:
                top += p.numel() + satir * 4
            else:
                g = grup if cols % grup == 0 else cols
                top += (p.numel() + 1) // 2 + satir * (cols // g) * 2
        else:
            top += p.numel() * 2          # kartta fp16 saklanır
    return top
