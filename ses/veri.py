"""Eğitim verisi: ses_veri/hazir/*.npz okuma, uzunluğa göre gruplanmış toplu işler."""
import os
import random

import numpy as np
import torch


def uzunluklar(veri):
    uz = {}
    for satir in open(os.path.join(veri, "uzunluk.tsv"), encoding="utf-8"):
        p = satir.split()
        if len(p) == 3:
            uz[p[0]] = (int(p[1]), int(p[2]))
    return uz


def liste(veri, ad):
    return [s.strip() for s in open(os.path.join(veri, ad + ".txt")) if s.strip()]


def yukle(veri, kimlik):
    with np.load(os.path.join(veri, "hazir", kimlik + ".npz")) as z:
        return {k: z[k] for k in z.files}


class Kumeler(torch.utils.data.Sampler):
    """Benzer uzunluktakileri aynı toplu işe koyar (dolgu israfı az), toplu işlerin sırası karışık.
    Bir toplu işin toplam karesi `kare_siniri`nı geçmez (bellek 8 GB)."""

    def __init__(self, kimlikler, uz, toplu, kare_siniri, tohum=0):
        self.kimlikler = sorted(kimlikler, key=lambda k: uz[k][0])
        self.uz, self.toplu, self.sinir, self.tohum = uz, toplu, kare_siniri, tohum
        self.donem = 0

    def _kumeler(self):
        r = random.Random(self.tohum + self.donem)
        # sıralamayı biraz boz ki her dönem aynı gruplar çıkmasın
        k = sorted(self.kimlikler, key=lambda x: self.uz[x][0] * (1 + 0.1 * r.random()))
        out, cur = [], []
        for x in k:
            t = self.uz[x][0]
            if cur and (len(cur) >= self.toplu or (len(cur) + 1) * t > self.sinir):
                out.append(cur)
                cur = []
            cur.append(x)
        if cur:
            out.append(cur)
        r.shuffle(out)
        return out

    def __iter__(self):
        k = self._kumeler()
        self.donem += 1
        return iter(k)

    def __len__(self):
        return len(self._kumeler())


class AkustikVeri(torch.utils.data.Dataset):
    def __init__(self, veri):
        self.veri = veri

    def __getitem__(self, kimlik):
        return yukle(self.veri, kimlik)

    def __len__(self):
        return 0


def akustik_birlestir(orn):
    b = len(orn)
    n = max(len(o["metin"]) for o in orn)
    t = max(o["mel"].shape[1] for o in orn)
    metin = torch.zeros(b, n, dtype=torch.long)
    mel = torch.full((b, 80, t), -11.5129)            # log(1e-5): sessizlik
    f0 = torch.zeros(b, t)
    m_uz = torch.zeros(b, dtype=torch.long)
    k_uz = torch.zeros(b, dtype=torch.long)
    for i, o in enumerate(orn):
        m_uz[i], k_uz[i] = len(o["metin"]), o["mel"].shape[1]
        metin[i, : m_uz[i]] = torch.from_numpy(o["metin"].astype(np.int64))
        mel[i, :, : k_uz[i]] = torch.from_numpy(o["mel"].astype(np.float32))
        f0[i, : k_uz[i]] = torch.from_numpy(o["f0"].astype(np.float32))
    return metin, m_uz, mel, k_uz, f0


class Kare(torch.utils.data.Dataset):
    """Vocoder için rastgele dalga parçası. gta=True ise tam cümle + parça başlangıcı döner."""

    def __init__(self, veri, kimlikler, parca, hop, gta=False):
        self.veri, self.k, self.parca, self.hop, self.gta = veri, kimlikler, parca, hop, gta

    def __len__(self):
        return len(self.k) * 1000

    def __getitem__(self, i):
        o = yukle(self.veri, self.k[i % len(self.k)])
        x = o["dalga"].astype(np.float32) / 32767
        kare = self.parca // self.hop
        bas = random.randint(0, max(0, len(x) // self.hop - kare))
        if self.gta:
            return o, bas
        p = x[bas * self.hop: bas * self.hop + self.parca]
        if len(p) < self.parca:
            p = np.pad(p, (0, self.parca - len(p)))
        return torch.from_numpy(p)
