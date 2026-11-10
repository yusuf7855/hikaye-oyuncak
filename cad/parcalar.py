"""Masal standının basılan parçaları ve içteki elektronik parçaların zarfları.

Her parça kendi baskı koordinatında üretilir; montaj konumu `montaj_konumu()` ile verilir.
"""
import math

import manifold3d as m3

import parametreler as P
from geometri import (M, CS, kutu, silindir, silindir_y, halka, dondur, yay, yuvarlak_dikdortgen,
                      xz_den_y_ye, acida, kutup, cokgen, govde_kutusu_radyal, yazi_duz, yazi_yay, yildiz, hilal)


# ====================================================================== alt gövde
def _hoparlor_bolumu():
    """Ön: düz bölme (ped), hava odası, ızgara yarıkları, beşik, yan raylar, arka dayanak."""
    ek = M()
    cik = M()
    w = 25.5
    ust = P.HOP_Z + P.HOPARLOR_D / 2 + 1.0
    ek += kutu(-w, w, P.HOP_YUZ_Y, P.R_IC + 1.0, P.TABAN - 0.01, ust)
    # hava odası: Ø35 silindir, iç duvar yüzeyiyle sınırlı (duvar 2,5 mm kalır)
    oda = silindir_y(P.ON_ODA_D / 2, P.HOP_YUZ_Y - 0.5, P.R_DIS + 2, z=P.HOP_Z, seg=96)
    oda = oda ^ silindir(P.R_IC, 0, 60)
    cik += oda
    # ızgara: dikey yarıklar (genişlik 1,6) Ø33 alan içinde
    r = P.IZGARA_D / 2
    n = int(r // P.IZGARA_ADIM)
    for i in range(-n, n + 1):
        x = i * P.IZGARA_ADIM
        hy = math.sqrt(max(r * r - x * x, 0)) - P.IZGARA_YARIK / 2
        if hy < 2.0:
            continue
        cik += kutu(x - P.IZGARA_YARIK / 2, x + P.IZGARA_YARIK / 2, P.HOP_YUZ_Y, P.R_DIS + 2,
                    P.HOP_Z - hy, P.HOP_Z + hy)
    # beşik (alt) — hoparlörün alt yanlarını tutar
    rb = P.HOPARLOR_D / 2 + 0.3
    y_arka = P.HOP_YUZ_Y - P.HOPARLOR_DERIN + 1.0
    besik = kutu(-14, 14, y_arka, P.HOP_YUZ_Y, P.TABAN - 0.01, P.HOP_Z - 6)
    besik -= silindir_y(rb, y_arka - 1, P.HOP_YUZ_Y + 1, z=P.HOP_Z, seg=128)
    ek += besik
    # yan raylar (yandan kılavuz)
    for s in (-1, 1):
        x0, x1 = sorted((s * rb, s * (rb + 2.6)))
        ek += kutu(x0, x1, P.HOP_YUZ_Y - 14, P.HOP_YUZ_Y, P.TABAN - 0.01, P.HOP_Z + 8)
    # arka dayanak: mıknatısı 3 mm köpükle öne bastırır
    y1 = P.HOP_YUZ_Y - P.HOPARLOR_DERIN - 0.5
    ek += kutu(-10, 10, y1 - 3.0, y1, P.TABAN - 0.01, P.HOP_Z + 4)
    return ek, cik


def _radyal_silindir(r, r0, r1, z, aci, seg=32, rr=None):
    """Radyal eksenli silindir (r0..r1 yarıçap aralığında), z yüksekliğinde, aci yönünde."""
    c = silindir(r, 0, r1 - r0, seg=seg, r2=rr)           # z: 0..L
    c = c.rotate([0, 90, 0])                               # z -> +x ? (bkz. not)
    # rotate y +90: (x,y,z)->(x cos+ z sin, y, -x sin + z cos) = (z, y, -x): z -> +x
    c = c.translate([r0, 0, z])
    return acida(c, aci)


def _mikrofon():
    Rf = P.R_IC - P.MIK_YUZ_GERI
    g = P.MIK_YUVA_BOSLUK
    zm = P.MIK_Z
    hp = P.MIK_PCB_D / 2
    z0 = zm - hp - 2.3
    z1 = P.H_ALT - 0.5

    def L(t0, t1, r0, r1, za, zb):
        # yerel: t teğet, r radyal. Dünya x = r (0° yönü), y = t; sonra açıya döndür.
        return acida(kutu(r0, r1, t0, t1, za, zb), P.MIK_ACI)
    ek = L(-10.5, 10.5, Rf, P.R_IC + 1.0, z0, z1)
    for s in (-1, 1):
        a, b = sorted((s * (hp + 0.35), s * 10.5))
        ek += L(a, b, Rf - g - 1.5, Rf, z0, z1)
        a, b = sorted((s * (hp - 1.3), s * (hp + 0.35)))
        ek += L(a, b, Rf - g - 1.5, Rf - g, z0, z1)
    ek += L(-10.5, 10.5, Rf - g - 1.5, Rf, z0, zm - hp - 0.05)
    cik = _radyal_silindir(P.MIK_CONTA_D / 2, Rf - 1.0, Rf + P.MIK_CONTA_DERIN, zm, P.MIK_ACI)
    cik += _radyal_silindir(P.MIK_DELIK / 2, Rf - 1.0, P.R_DIS + 1.0, zm, P.MIK_ACI, seg=24)
    cik += _radyal_silindir(P.MIK_DELIK / 2, P.R_DIS - 1.5, P.R_DIS + 0.01, zm, P.MIK_ACI, seg=32,
                            rr=2.0)  # dış havşa (koni Ø1 -> Ø4)
    return ek, cik


def _usbc():
    ek = M()
    cik = M()
    zpl = P.USBC_Z - P.USBC_PCB - (P.USBC_KART_H - P.USBC_PCB) / 2   # kart alt yüzü
    hg = P.USBC_KART_G / 2 + 0.2
    y_on = P.USBC_ON_Y
    y_arka = y_on + P.USBC_KART_D + 0.3
    # platform + yan kılavuzlar + arka dayanak (fiş takma kuvvetini gövde taşır)
    ek += kutu(-hg - 2.0, hg + 2.0, y_on - 0.5, y_arka + 2.0, P.TABAN - 0.01, zpl)
    for s in (-1, 1):
        a, b = sorted((s * hg, s * (hg + 2.0)))
        ek += kutu(a, b, y_on + 2.0, y_arka, zpl - 0.01, zpl + 3.0)
        a, b = sorted((s * 5.0, s * hg))
        ek += kutu(a, b, y_arka, y_arka + 2.0, zpl - 0.01, zpl + 3.5)
    # duvarın içine düz cep (kart öne, duvara dayanır)
    cik += kutu(-hg, hg, y_on, y_on + 12.0, zpl, zpl + P.USBC_KART_H + 0.2)
    # soket ağzı
    ag = yuvarlak_dikdortgen(P.USBC_AGIZ[0], P.USBC_AGIZ[1], 1.5)
    cik += xz_den_y_ye(ag, -P.R_DIS - 3, y_on + 1.0, x=0, z=P.USBC_Z)
    # dış düz alın (fiş gövdesi dayanır), 14 x 8.6
    al = yuvarlak_dikdortgen(14.0, 8.6, 3.0)
    cik += xz_den_y_ye(al, -P.R_DIS - 3, P.USBC_DIS_DUZ, x=0, z=P.USBC_Z)
    return ek, cik, zpl


def _kablo_bagi(x, y):
    """Kablo bağı köprüsü (gerilme önleyici): 2,0 mm yüksek, 3,6 mm geniş tünel, y yönünde."""
    b = kutu(x - 4.5, x + 4.5, y - 1.5, y + 1.5, P.TABAN - 0.01, P.TABAN + 4.0)
    b -= kutu(x - 1.8, x + 1.8, y - 3, y + 3, P.TABAN - 0.5, P.TABAN + 2.0)
    return b


def _tasiyici_kizak():
    """5x7 cm pertinaks için 4 köşe: alt sehpa + uç dayanağı + esnek kenet dili (delik konumu gerekmez)."""
    cx, cy = P.TASIYICI_MERKEZ
    hx = P.TASIYICI[0] / 2 + P.TASIYICI_PAY
    hy = P.TASIYICI[1] / 2 + P.TASIYICI_PAY
    zc = P.TASIYICI_Z
    ust = zc + P.TASIYICI_PCB
    ek = M()
    for sx in (-1, 1):
        for sy in (-1, 1):
            kx, ky = cx + sx * hx, cy + sy * hy
            # sehpa (kartın köşesinin altında, 4x4)
            a, b = sorted((kx, kx - sx * 4.0))
            c, d = sorted((ky, ky - sy * 2.5))
            ek += kutu(a, b, c, d, P.TABAN - 0.01, zc)
            # uç dayanağı (y yönünde kartın ucunda, rijit)
            a, b = sorted((kx + sx * 1.6, kx - sx * 7.0))
            c, d = sorted((ky, ky + sy * 1.6))
            ek += kutu(a, b, c, d, P.TABAN - 0.01, ust + 1.2)
            # esnek kenet dili (x yanında, köşeden 3..10 mm), içe 0,4 mm tırnak
            a, b = sorted((kx, kx + sx * 1.2))
            c, d = sorted((ky - sy * 3.0, ky - sy * 10.0))
            ek += kutu(a, b, c, d, P.TABAN - 0.01, ust + 1.6)
            # tırnak: yatay tutma yüzü kart üstünde, üstte 45°'den yatık rampa
            pts = []
            for yy in (c, d):
                pts += [(kx, yy, ust + 0.05), (kx - sx * 0.4, yy, ust + 0.05), (kx, yy, ust + 1.05)]
            ek += M.hull_points(pts)
    return ek


def _amp_kizak():
    """MAX98357A: dikey U-raylı kızak, kart üstten kayar (delik konumu gerekmez)."""
    w = P.AMP_KART[0] + 2 * P.AMP_PAY
    y0 = P.AMP_Y0
    y1 = y0 + w
    z0 = P.AMP_TABAN_Z
    z1 = z0 + P.AMP_KART[1] - 2.0
    x = P.AMP_X
    ek = M()
    for ya, yb, ic in ((y0 - 2.0, y0 + 1.5, y0), (y1 - 1.5, y1 + 2.0, y1)):
        ray = kutu(x - 2.5, x + 2.5, ya, yb, P.TABAN - 0.01, z1)
        if ic == y0:
            ray -= kutu(x - 0.95, x + 0.95, y0, yb + 1, z0, z1 + 1)
        else:
            ray -= kutu(x - 0.95, x + 0.95, ya - 1, y1, z0, z1 + 1)
        ek += ray
    return ek


def _havalandirma():
    cik = M()
    # taban yarıkları (taşıyıcı kartın altında)
    for i in range(-4, 4):
        x = i * 5.0 + 2.5          # x=0'da yarık yok (A–A kesiti tabanı gösterir)
        cik += kutu(x - 1.0, x + 1.0, -30.0, -6.0, -1, P.TABAN + 1)
    # üst yan yarıklar (kapak altında, sıcak hava çıkışı)
    for aci in list(range(166, 196, 5)) + list(range(14, 34, 5)):
        cik += govde_kutusu_radyal(P.R_IC - 3.0, P.R_DIS + 1, 1.8, 34.0, 41.0, aci)
    return cik


def alt_govde():
    """Alt gövde: baskı konumu = montaj konumu (taban tablada)."""
    R, H = P.R_DIS, P.H_ALT
    g = dondur([(0, 0), (R - P.ALT_PAH, 0), (R, P.ALT_PAH), (R, H), (0, H)])
    g -= silindir(P.R_IC, P.TABAN, H + 1)
    # merkezleme dili
    g += halka(P.R_IC, P.R_IC + P.DIL_KAL, H - 0.01, H + P.DIL_Y)
    # vida kolonları (duvara bağlı)
    for a in P.VIDA_ACILAR:
        x, y = kutup(P.VIDA_R, a)
        g += silindir(P.KOLON_D / 2, P.TABAN - 0.01, H, x, y)
        g += govde_kutusu_radyal(P.VIDA_R, P.R_IC + 0.5, P.KOLON_D * 0.75, P.TABAN - 0.01, H, a)
    ic = silindir(P.R_IC + 1.0, -1, H + 0.01)   # iç eklemeler dış yüzeyi aşmasın
    ek, cik = _hoparlor_bolumu()
    g += ek ^ ic
    g -= cik
    ek, cik = _mikrofon()
    g += ek ^ ic
    g -= cik
    ek, cik, _ = _usbc()
    g += ek ^ ic
    g -= cik
    for x in (-16.0, 16.0):
        g += _kablo_bagi(x, -51.0)
    g += _tasiyici_kizak()
    g += _amp_kizak()
    g -= _havalandirma()
    # vida delikleri + derin havşa (alttan; vida başı gizli)
    for a in P.VIDA_ACILAR:
        x, y = kutup(P.VIDA_R, a)
        g -= silindir(P.VIDA_DELIK / 2, -1, H + 1, x, y)
        g -= silindir(P.VIDA_HAVSA_D / 2, -1, H - P.VIDA_SIKMA, x, y)
    # ayak yuvaları
    for a in P.AYAK_ACILAR:
        x, y = kutup(P.AYAK_R, a)
        g -= silindir(P.AYAK_D / 2, -1, P.AYAK_DERIN, x, y, seg=48)
    return g


# ====================================================================== kapak
def ust_kapak():
    """Üst kapak, kendi koordinatı: z=0 alt yüz (tablaya), z=KAPAK_KAL üst yüz. Montajda +H_ALT."""
    R, T, f = P.R_DIS, P.KAPAK_KAL, P.KAPAK_UST_YUVARLAK
    prof = [(0, 0), (R - P.KAPAK_ALT_PAH, 0), (R, P.KAPAK_ALT_PAH), (R, T - f)]
    prof += yay(R - f, T - f, f, 0, 90, 10)[1:]
    prof += [(0, T)]
    k = dondur(prof)
    # figür yuvası (pahlı ağız)
    rs = P.YUVA_R
    k -= dondur([(0, P.YUVA_TABAN_KAL), (rs, P.YUVA_TABAN_KAL), (rs, T - P.YUVA_PAH),
                 (rs + P.YUVA_PAH, T), (rs + P.YUVA_PAH, T + 1), (0, T + 1)])
    if P.ANAHTAR_VAR:
        # kama: arka (270°), üstü pahlı
        y_ic = -(rs - P.ANAHTAR_DERIN)
        prof_k = CS([cokgen([(-(rs + 0.5), P.YUVA_TABAN_KAL - 0.01), (y_ic, P.YUVA_TABAN_KAL - 0.01),
                      (y_ic, T - 2.2), (y_ic - 1.0, T - 1.2), (-(rs + 0.5), T - 1.2)])])
        kama = prof_k.extrude(P.ANAHTAR_G).rotate([90, 0, 90]).translate([-P.ANAHTAR_G / 2, 0, 0])
        k += kama
    # halka kanalı (alt bölge halka, üst bölge difüzör omzu + tırnak oluğu)
    z0, z1 = P.KILIT_OLUK_Z
    rd = P.KANAL_UST_R_DIS
    kanal = [(P.KANAL_R_IC, P.KANAL_TABAN), (P.KANAL_R_DIS, P.KANAL_TABAN), (P.KANAL_R_DIS, P.OMUZ_Z),
             (rd, P.OMUZ_Z), (rd, z0 - 0.2), (rd + P.KILIT_OLUK_DERIN, z0), (rd + P.KILIT_OLUK_DERIN, z1),
             (rd, z1 + 0.2), (rd, T + 1), (P.KANAL_UST_R_IC, T + 1), (P.KANAL_UST_R_IC, P.OMUZ_Z),
             (P.KANAL_R_IC, P.OMUZ_Z)]
    k -= dondur(kanal)
    # halka kablosu geçişi (kanal tabanında, arkada)
    k -= acida(kutu(46.0, 51.0, -8.0, 8.0, -1, P.KANAL_TABAN + 0.5), P.HALKA_KABLO_ACI)
    # alt yüzde dil oluğu
    k -= halka(P.R_IC - P.OLUK_PAY, P.R_IC + P.DIL_KAL + P.OLUK_PAY, -1, P.DIL_Y + 0.3)
    # ısıl gömme somun delikleri
    for a in P.VIDA_ACILAR:
        x, y = kutup(P.VIDA_R, a)
        k -= silindir(P.INSERT_D / 2, -1, P.INSERT_DERIN, x, y, seg=32)
    # RC522 tutucu vida pilotları
    for x, y in P.RC_VIDALAR:
        k -= silindir(P.RC_VIDA_PILOT / 2, -1, P.RC_VIDA_DERIN, x, y, seg=24)
    return k


# ====================================================================== difüzör
def difuzor_halka():
    """Kendi koordinatı: z=0 eteklerin alt ucu (= kapakta OMUZ_Z). Etekler aşağıda basılır."""
    ri = P.KANAL_UST_R_IC + P.DIF_PAY
    ro = P.KANAL_UST_R_DIS - P.DIF_PAY
    e = P.DIF_ETEK
    zp = P.LED_UST + P.ISIK_BOSLUGU - P.OMUZ_Z      # plaka alt yüzü
    zt = zp + P.DIF_KAL
    rr = 1.2
    oz0, oz1 = (z - P.OMUZ_Z for z in P.KILIT_OLUK_Z)
    t = P.DIF_TIRNAK
    prof = [(ri, 0), (ri + e, 0), (ri + e, zp), (ro - e, zp), (ro - e, 0), (ro, 0),
            (ro, oz0 - 0.2), (ro + t, oz0 + 0.15), (ro + t, oz1 - 0.1), (ro, oz1 + 0.15)]
    prof += yay(ro - rr, zt - rr, rr, 0, 90, 8)
    prof += yay(ri + rr, zt - rr, rr, 90, 180, 8)
    return dondur(prof)


# ====================================================================== figür tabanı
def _taban_govde():
    r, h = P.TABAN_D / 2, P.TABAN_H
    b = dondur([(0, 0), (r - P.TABAN_ALT_PAH, 0), (r, P.TABAN_ALT_PAH), (r, h - P.TABAN_UST_PAH),
                (r - P.TABAN_UST_PAH, h), (0, h)])
    if P.ANAHTAR_VAR:
        gx = P.ANAHTAR_G / 2 + P.ANAHTAR_PAY
        y_ic = -(P.YUVA_R - P.ANAHTAR_DERIN - P.ANAHTAR_PAY - 0.4)
        b -= kutu(-gx, gx, -r - 1, y_ic, -1, h + 1)
    # NTAG213 etiket cebi (alt yüz, 0,4 mm)
    b -= silindir(P.ETIKET_CEP_D / 2, -1, P.ETIKET_CEP_DERIN, seg=96)
    return b


def figur_taban(ad=None, nfc_no=None, motif=None, topuz=False):
    """Figür tabanı (jeton). ad: üst kenara kazınan yazı (öne okunur). nfc_no: alt yüze kazınır."""
    h = P.TABAN_H
    b = _taban_govde()
    if topuz:
        rt = P.AYAR_TOPUZ_D / 2
        ht = P.AYAR_TOPUZ_H
        prof = [(0, h - 0.5), (rt, h - 0.5), (rt, h + ht - 3.0)] + yay(rt - 3.0, h + ht - 3.0, 3.0, 0, 90, 10)[1:] \
            + [(0, h + ht)]
        b += dondur(prof, seg=96)
    elif P.YAPISTIRMA_D > 0:
        b -= silindir(P.YAPISTIRMA_D / 2, h - P.YAPISTIRMA_DERIN, h + 1, seg=96)
    if ad:
        yz = yazi_yay(ad, P.YAZI_BOY, P.YAZI_FONT, P.YAZI_R, 90.0)
        b -= yz.extrude(P.YAZI_DERIN + 1).translate([0, 0, h - P.YAZI_DERIN])
    if motif == "gece":
        # arka yarıda hilal + üç yıldız (kazıma)
        sek = hilal(-12.0, -21.5, 4.2, 1.9, 3.6, aci=30.0)
        sek += yildiz(0.0, -21.0, 2.6, 1.1)
        sek += yildiz(10.5, -22.0, 2.0, 0.85)
        sek += yildiz(18.0, -15.5, 1.6, 0.7)
        sek = sek.simplify(0.005)
        b -= sek.extrude(P.YAZI_DERIN + 1).translate([0, 0, h - P.YAZI_DERIN])
    if nfc_no is not None:
        # alt yüz: aşağıdan okunur (ayna), etiket cebinin dışında, önde
        t = yazi_duz(f"No {nfc_no}", P.ALT_YAZI_BOY, P.YAZI_FONT, ayna=True)
        t = t.translate([0, 20.0])
        b -= t.extrude(0.4 + 1).translate([0, 0, -1])
    return b


# ====================================================================== RC522 tutucu
def rc522_tutucu():
    """Kendi koordinatı = montaj x,y; z=0 alt yüz. Üst yüzü kapak alt yüzüne dayanır.
    RC522 bileşen yüzü AŞAĞI (anten bakırı PCB'nin alt yüzünde, NFC için 1,6 mm FR4 sorun değil),
    düz arka yüzü kapağa yaslanır."""
    L, W = RC522_cep()
    cx = -P.RC522_ANTEN_KAYMA
    hx, hy = L / 2, W / 2
    d = P.RC_TUT_DUVAR
    h = P.RC_TUT_ALT + P.RC522_PCB
    t = kutu(cx - hx - d, cx + hx + d, -hy - d, hy + d, 0, h)
    for x, y in P.RC_VIDALAR:
        t += silindir(3.2, 0, h, x, y, seg=32)
        yy = math.copysign(hy + d - 0.5, y)
        t += kutu(x - 3.2, x + 3.2, min(y, yy), max(y, yy), 0, h)
    # cep (kart)
    t -= kutu(cx - hx, cx + hx, -hy, hy, P.RC_TUT_ALT, h + 1)
    # pencere: uzun kenarlarda dudak 1,5; uzak uçta 3; header ucu tamamen açık
    dd = P.RC_TUT_DUDAK
    t -= kutu(cx - hx - d - 1, cx + hx - 3.0, -hy + dd, hy - dd, -1, h + 1)
    for x, y in P.RC_VIDALAR:
        t -= silindir(1.4, -1, h + 1, x, y, seg=24)   # M2,5 geçiş (Ø2,8)
    return t


def RC522_cep():
    return P.RC522[0] + 2 * P.RC522_PAY, P.RC522[1] + 2 * P.RC522_PAY


# ====================================================================== montaj
def montaj_konumu(ad):
    """Parçanın kendi koordinatından montaj koordinatına öteleme (x, y, z)."""
    return {
        "govde_alt": (0, 0, 0),
        "ust_kapak": (0, 0, P.H_ALT),
        "difuzor_halka": (0, 0, P.H_ALT + P.OMUZ_Z),
        "figur_taban": (0, 0, P.H_ALT + P.YUVA_TABAN_KAL),
        "rc522_tutucu": (0, 0, P.H_ALT - P.RC_TUT_ALT - P.RC522_PCB),
    }[ad]


def zarflar():
    """İçteki elektronik parçaların (basılmayan) zarfları: çakışma denetimi ve çizimler için."""
    z = {}
    cx, cy = P.TASIYICI_MERKEZ
    hx, hy = P.TASIYICI[0] / 2, P.TASIYICI[1] / 2
    zc = P.TASIYICI_Z
    ust = zc + P.TASIYICI_PCB
    z["Taşıyıcı pertinaks 5x7"] = kutu(cx - hx, cx + hx, cy - hy, cy + hy, zc, ust)
    z["Pertinaks altı lehim/kablo"] = kutu(cx - hx + 4.5, cx + hx - 4.5, cy - hy + 4.5, cy + hy - 4.5,
                                          zc - 2.0, zc)
    # DevKit: dişi header (8,5) + erkek header plastiği (2,5) + PCB + modül
    dx0, dx1 = P.DEVKIT_X - P.DEVKIT[0] / 2, P.DEVKIT_X + P.DEVKIT[0] / 2
    y_on = P.DEVKIT_Y_ON
    y_arka = y_on - P.DEVKIT[1]
    z_pcb = ust + P.DISI_HEADER_H + 2.5
    z["ESP32-S3-DevKitC-1 (+headerlar)"] = kutu(dx0, dx1, y_arka, y_on, ust, z_pcb) + \
        kutu(dx0, dx1, y_arka, y_on + 0.6, z_pcb, z_pcb + 1.6 + 3.4)   # USB soketleri 0,6 mm taşar
    z["ESP32 anten çıkıntısı"] = kutu(P.DEVKIT_X - 9, P.DEVKIT_X + 9, y_arka - P.DEVKIT_ANTEN_TASMA, y_arka,
                                     z_pcb + 0.8, z_pcb + 1.6 + 3.2)
    z["Seviye çevirici + 1000 µF + klemensler"] = kutu(4.0, cx + hx - 0.5, cy - hy + 2, cy + hy - 2,
                                                      ust, ust + 21.0)
    # amp
    x = P.AMP_X
    y0 = P.AMP_Y0 + P.AMP_PAY
    z0 = P.AMP_TABAN_Z
    z["MAX98357A PCB"] = kutu(x - 0.8, x + 0.8, y0, y0 + P.AMP_KART[0], z0, z0 + P.AMP_KART[1])
    z["MAX98357A bileşen/klemens"] = kutu(x + 0.8, x + 11.0, y0 + 1.7, y0 + P.AMP_KART[0] - 1.7, z0,
                                          z0 + P.AMP_KART[1])
    # hoparlör
    z["Hoparlör Ø40x20"] = silindir_y(P.HOPARLOR_D / 2, P.HOP_YUZ_Y - P.HOPARLOR_DERIN, P.HOP_YUZ_Y,
                                      z=P.HOP_Z, seg=96)
    # USB-C
    zpl = P.USBC_Z - P.USBC_PCB - (P.USBC_KART_H - P.USBC_PCB) / 2
    g = P.USBC_KART_G / 2
    z["USB-C kartı"] = kutu(-g, g, P.USBC_ON_Y, P.USBC_ON_Y + P.USBC_KART_D, zpl, zpl + P.USBC_KART_H)
    # mikrofon kartı (yuva içinde, conta 1 mm + PCB 1,2)
    Rf = P.R_IC - P.MIK_YUZ_GERI
    pcb = _radyal_silindir(P.MIK_PCB_D / 2, Rf - 1.0 - 1.2, Rf - 1.0, P.MIK_Z, P.MIK_ACI, seg=48)
    z["INMP441 kartı"] = pcb
    # RC522
    L, W = P.RC522
    cxr = -P.RC522_ANTEN_KAYMA
    z["RC522 PCB"] = kutu(cxr - L / 2, cxr + L / 2, -W / 2, W / 2, P.H_ALT - P.RC522_PCB, P.H_ALT)
    z["RC522 bileşenleri (alt)"] = kutu(cxr - L / 2 + 2, cxr + L / 2 - 3.5, -W / 2 + 2, W / 2 - 2,
                                        P.H_ALT - P.RC522_PCB - 4.5, P.H_ALT - P.RC522_PCB)
    # halka
    z["NeoPixel halka Ø104/Ø90"] = halka(P.HALKA_IC_D / 2, P.HALKA_DIS_D / 2, P.H_ALT + P.KANAL_TABAN,
                                         P.H_ALT + P.KANAL_TABAN + P.HALKA_KAL)
    # NTAG213 etiketi (taban cebinde)
    zt = P.H_ALT + P.YUVA_TABAN_KAL
    z["NTAG213 Ø25"] = silindir(P.ETIKET_D / 2, zt + P.ETIKET_CEP_DERIN - 0.25, zt + P.ETIKET_CEP_DERIN, seg=64)
    return z
