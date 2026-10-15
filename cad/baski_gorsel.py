"""Baskıya hazır STL'lerin önizlemesi: her parça baskı yönünde (tablada) + montajlı tüm stand.

    python cad/baski_gorsel.py     # cad/onizleme/baski_parcalar.png
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import trimesh  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
import dis_konsept as K  # noqa: E402


def main(nfc="rc522"):
    d = os.path.join(C.KOK, "stl_cakil", nfc)
    fig = plt.figure(figsize=(18, 11), dpi=100)
    kutular = [("0_tum_stand_%s_montajli" % nfc, "TÜM STAND (montajlı)", 30, 35)] + [
        (dosya, f"{dosya[0]}) {dosya[2:].replace('_', ' ')}\n{yon}", 28, 35) for dosya, _, yon in C.BASKI]
    for i, (dosya, baslik, elev, azim) in enumerate(kutular):
        m = trimesh.load(os.path.join(d, dosya + ".stl"))
        ax = fig.add_subplot(2, 3, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, [(m, "#E8DCCB" if i else "#F6E7D2", False)], [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        b = m.bounds
        s = max(b[1] - b[0]) / 2 + 2
        c = (b[0] + b[1]) / 2
        ax.set_xlim(c[0] - s, c[0] + s); ax.set_ylim(c[1] - s, c[1] + s); ax.set_zlim(0, 2 * s)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(baslik + f"\n{b[1][0] - b[0][0]:.0f} x {b[1][1] - b[0][1]:.0f} x {b[1][2] - b[0][2]:.0f} mm", fontsize=10)
    fig.suptitle(f"Baskıya hazır parçalar ({nfc.upper()}): her parça tablada, baskı yönünde", fontsize=15)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", f"baski_parcalar_{nfc}.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    print(main(sys.argv[1] if len(sys.argv) > 1 else "rc522"))
