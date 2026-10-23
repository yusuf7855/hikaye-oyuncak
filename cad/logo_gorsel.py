"""Renkli kabuğun önden görünüşü (logo): python cad/logo_gorsel.py -> cad/onizleme/logo_3b.png"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import cakil_ic as C  # noqa: E402
import dis_konsept as K  # noqa: E402
import kulaklar as Ku  # noqa: E402
import renkli as R  # noqa: E402

if __name__ == "__main__":
    renk = {k: c for k, _, c in R.RENKLER}
    fig = plt.figure(figsize=(21, 8.5), dpi=105)
    gorunus = ((False, 8, 90, "Önden (kulaksız)"), (True, 14, 90, "Önden (kedi kulaklı)"), (False, 26, 55, "Sağ önden"))
    for i, (kulakli, elev, azim, bas) in enumerate(gorunus):
        b = R.kabuk_renk(kulak=kulakli)
        ls = [(m, renk[k], False) for k, m in b.items()]
        if kulakli:
            for aci in C.KULAK_ACILAR:
                g, kk = Ku.kedi_kulak(aci)
                ls += [(g - kk, "#F4F1EA", False), (kk, "#ff8fb8", False)]
        ax = fig.add_subplot(1, 3, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-5, 85); ax.set_box_aspect((1, 1, 0.75)); ax.set_axis_off()
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas, fontsize=14)
    fig.suptitle("Yeni logo: \"eco ai\" yıldızlar arasında (turkuaz harfler, sarı ve mor yıldızlar, 1,2 mm kabarık)",
                 fontsize=15, fontweight="bold")
    plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
    yol = os.path.join(C.KOK, "onizleme", "logo_3b.png")
    fig.savefig(yol)
    print(yol)
