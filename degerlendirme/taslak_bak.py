"""Yazarın taslak ön denetimi: yalnız biçim ve kelime kapıları (K2 uzunluk/cümle/token, K3 seyrek kelime, az görülmüş
token, şapka, Ateşman). Kayıt YAZMAZ, yama saymaz: yazar taslağını resmî kontrolden (veri_hakem.py kontrol) önce istediği
kadar bununla düzeltebilir.

İçerik kapıları (K1 başlık/tohum, K4 kapalı dünya, K5 dil, K6–K8, K9 yakın kopya, K11) burada yoktur: onlar resmî
kontrolde bir kez denetlenir ve en çok 1 yerel düzeltme hakkı vardır (hikâyeyi denetime göre bükmek yerine yazarın
kendi yargısı). K2/K3 ise sözlük ve sayı kurallarıdır: kelimenin eğitim verisinde seyrek olması yazarın bilemeyeceği
bir şeydir; ön denetim yalnız onu gösterir.

Kullanım: .venv/bin/python degerlendirme/taslak_bak.py <taslak dosyası>
Çıktı: her hikâye için "TAMAM" ya da kapı kodları ve sorunlu kelimeler; sonda özet.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kapi  # noqa: E402
import urun_kayit as uk  # noqa: E402


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    bg = kapi.Baglam()
    with open(sys.argv[1], encoding="utf-8") as f:
        bloklar = uk.ayristir(f.read())
    tamam = 0
    for b in bloklar:
        ih, rapor = [], {}
        if b.get("bicim_hatalari"):
            ih += [{"kod": "biçim", "aciklama": h} for h in b["bicim_hatalari"]]
        try:
            kayit = uk.kayit(b)
            kapi.k2(kayit, bg, ih, rapor)
            kapi.k3(kayit, bg, ih, rapor)
        except Exception as e:  # noqa: BLE001 (bozuk blok: yazara göster)
            ih.append({"kod": "biçim", "aciklama": f"ayrıştırılamadı: {e}"})
        kim = b.get("tohum") or f"satır {b.get('satir')}"
        if ih:
            print(f"{kim}  DÜZELT")
            for x in ih:
                print(f"   {x['kod']}: {x['aciklama']}")
        else:
            tamam += 1
            print(f"{kim}  TAMAM  ({rapor.get('kelime')} kelime, Ateşman {rapor.get('atesman')})")
    print(f"{tamam}/{len(bloklar)} biçim ve kelime kapılarından geçiyor (içerik kapıları resmî kontrolde)")


if __name__ == "__main__":
    main()
