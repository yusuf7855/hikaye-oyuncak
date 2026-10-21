# Çakıl stand — STEP dosyaları (tek renkli tasarım)

`python cad/step_yaz.py` ile üretilir: `cakil_ic.py`'deki aynı tasarım OpenCASCADE ile gerçek katı (B-rep) olarak
kurulur. Kavisli dış yüz düzgün B-spline, delikler gerçek silindir; Fusion 360, SolidWorks, Onshape, FreeCAD'de
düzenlenebilir katı olarak açılır. Birim mm; z yukarı; parçalar montajdaki yerinde (+y ön/logo, -y arka).

| Dosya | Parça |
|---|---|
| `kabuk.step` | dış kabuk ("eco ai" logolu, figür çukuru, ışık oyuğu, hoparlör ızgarası, anahtar deliği, vida kolonları) |
| `taban_plakasi.step` | alt kapak (pil kutusu ve kapak deliği, hoparlör beşiği, ESP32 yuvası, MAX98357A ve düzenleyici çerçeveleri, vida havşaları, ayak yuvaları) |
| `pil_kapagi.step` | pil kapağı (iki dil, M3 havşa vida tablası) |
| `halka_nfc_tutucu_rc522.step` / `_pn5180.step` | NeoPixel halka + NFC okuyucu tutucusu (kullandığın okuyucunun dosyası) |
| `0_montaj_rc522.step` / `0_montaj_pn5180.step` | kabuk + taban + tutucu, adlı ve renkli ayrı katılar |

Figür tabanları (vidalı NFC kapaklı) yalnız STL: `cad/stl_cakil/figurler/`.

Denetim: her dosya tek ve geçerli katı; STEP ile baskı STL'leri arasındaki hacim farkı kabukta %0,3 (kavisli yüzün
düzgünleşmesi), ötekilerde %0,1'in altında. Baskı için hazır STL/3MF'ler `cad/stl_cakil/`'de.
