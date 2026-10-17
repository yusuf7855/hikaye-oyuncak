# Çakıl stand — STEP dosyaları (tek renkli tasarım)

`python cad/step_yaz.py` ile üretilir: `cakil_ic.py`'deki aynı tasarım OpenCASCADE ile gerçek katı (B-rep) olarak
kurulur. Kavisli dış yüz düzgün B-spline, delikler gerçek silindir; Fusion 360, SolidWorks, Onshape, FreeCAD'de
düzenlenebilir katı olarak açılır. Birim mm; z yukarı; parçalar montajdaki yerinde (+y ön/logo, -y arka/USB-C).

| Dosya | Parça |
|---|---|
| `kabuk.step` | dış kabuk ("eco ai" logolu, figür çukuru, ışık oyuğu, hoparlör ızgarası, USB-C ve anahtar delikleri, TP4056 kızakları, vida kolonları) |
| `taban_plakasi.step` | alt kapak (pil yatağı cebi, hoparlör beşiği, TP4056 kaidesi, ESP32 yuvası, MAX98357A cebi, vida havşaları, ayak yuvaları) |
| `halka_nfc_tutucu_rc522.step` / `_pn5180.step` | NeoPixel halka + NFC okuyucu tutucusu (kullandığın okuyucunun dosyası) |
| `figur_taban.step` | figür tabanı Ø28 (çukurdaki yerinde) |
| `ayar_karti.step` | ayar kartı (z = 0'da) |
| `0_montaj_rc522.step` / `0_montaj_pn5180.step` | kabuk + taban + tutucu + figür tabanı, adlı ve renkli ayrı katılar |

Denetim: her dosya tek ve geçerli katı; STEP ile baskı STL'leri arasındaki hacim farkı kabukta %0,3 (kavisli yüzün
düzgünleşmesi), ötekilerde %0,1'in altında. Baskı için hazır STL/3MF'ler `cad/stl_cakil/`'de.
