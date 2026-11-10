"""Kabuk şeffaf: içindeki her parça görünür (iki açıdan).

    python cad/seffaf_gorsel.py [rc522|pn5180]     # cad/onizleme/seffaf_ic_<nfc>.png
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402

ISIK = np.array([0.3, 0.55, 0.78]) / np.linalg.norm([0.3, 0.55, 0.78])


def yuzler(m, renk, kamera, alfa=1.0, tum=False):
    """trimesh/manifold -> (üçgenler, renkler); arka yüzler (opaklar için) atılır."""
    t = m if hasattr(m, "faces") else C._tm(m)
    v = t.vertices[t.faces]
    n = np.cross(v[:, 1] - v[:, 0], v[:, 2] - v[:, 0])
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    if not tum:
        on = n @ kamera > -0.05
        v, n = v[on], n[on]
    k = 0.45 + 0.55 * np.clip(np.abs(n @ ISIK), 0, 1)
    c = np.array(matplotlib.colors.to_rgb(renk))
    rgba = np.c_[np.clip(c[None, :] * k[:, None], 0, 1), np.full(len(v), alfa)]
    return v, rgba


def main(nfc="rc522"):
    z, yapi, sorun, mesafe = C.denetle(nfc)
    ic = [(yapi["taban"], "#E3D5BF"), (yapi["pil_kapagi"], "#c9a57a"), (yapi["tutucu"], "#e2c27a"),
          (z["NeoPixel 16"], "#ff4fa3"), (z[f"{nfc.upper()} okuyucu"], "#1f6f3f" if nfc == "rc522" else "#1f4f8f"),
          (z["hoparlör (önden)"], "#6b7280"), (C.esp_stl(), "#1d1d1d"), (z["4xAA yatağı"], "#3b3b42"),
          (z["MAX98357A"], "#7b3fbf"), (z["5 V düzenleyici"], "#2d6cdf"), (z["KCD11 anahtar"], "#111111"),
          (yapi["figur"], "#1FB5B0")]
    fig = plt.figure(figsize=(20, 10), dpi=110)
    for i, (elev, azim, bas) in enumerate(((24, 60, "Önden-sağdan"), (24, -125, "Arkadan-soldan"))):
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        kam = np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        vs, cs = [], []
        for m, renk in ic:
            v, c = yuzler(m, renk, kam)
            vs.append(v); cs.append(c)
        v, c = yuzler(yapi["kabuk"], "#d9c9b0", kam, alfa=0.07, tum=True)
        vs.append(v); cs.append(c)
        pc = Poly3DCollection(np.concatenate(vs), facecolors=np.concatenate(cs), edgecolors="none", linewidths=0)
        ax.add_collection3d(pc)
        ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-18, 70); ax.set_box_aspect((1, 1, 0.73))
        ax.set_axis_off(); ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas, fontsize=14)
    lejant = ("figür (turkuaz)  |  LED halka (pembe)  |  tutucu (sarımsı)  |  NFC okuyucu (yeşil/mavi)  |  hoparlör (gri)  |  "
              "ESP32 (siyah)\n4xAA yatağı (koyu)  |  MAX98357A (mor)  |  5 V düzenleyici (mavi)  |  anahtar (siyah)  |  "
              "taban ve pil kapağı (bej)")
    fig.text(0.5, 0.03, lejant, ha="center", fontsize=11, bbox=dict(fc="white", ec="#999"))
    fig.suptitle(f"Kabuk şeffaf: içindeki parçalar ({nfc.upper()})", fontsize=16, fontweight="bold")
    plt.subplots_adjust(left=0, right=1, top=0.93, bottom=0.07, wspace=0)
    yol = os.path.join(C.KOK, "onizleme", f"seffaf_ic_{nfc}.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    print(main(sys.argv[1] if len(sys.argv) > 1 else "rc522"))
