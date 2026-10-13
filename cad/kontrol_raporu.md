# Masal standı — üretim ve denetim raporu (cad/uret.py üretir, elle düzenlemeyin)

## Parçalar
| Dosya | Hacim cm³ | Boyut (x × y × z) mm | Su geçirmez | Malzeme | Katman | Dolgu % | ~Filament g | ~Süre sa | Yön |
|---|---|---|---|---|---|---|---|---|---|
| `stl/govde_alt.stl` | 86.0 | 128.0 × 128.0 × 47.0 | evet | PETG ya da PLA | 0.2 | 15 | 76 | 3.5 | taban tablada (olduğu gibi), destek YOK |
| `stl/ust_kapak.stl` | 65.3 | 128.0 × 128.0 × 8.0 | evet | PETG ya da PLA | 0.2 | 15 | 41 | 1.9 | alt yüz tablada (olduğu gibi), destek YOK |
| `stl/difuzor_halka.stl` | 8.3 | 107.6 × 107.6 × 6.0 | evet | PETG doğal/beyaz yarı saydam | 0.2 | 100 | 11 | 0.5 | etekler tablada (olduğu gibi), destek YOK |
| `stl/rc522_tutucu.stl` | 2.0 | 69.9 × 58.4 × 3.0 | evet | PLA/PETG | 0.2 | 30 | 3 | 0.1 | alt yüz tablada, destek YOK |
| `stl/figur_taban.stl` | 17.3 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/niloya.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/masa.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/pepee.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/keloglan.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/doru.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/hayri.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/sakir.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/elsa.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/chase.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/orumcek_adam.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/hello_kitty.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/figurler/gece.stl` | 17.2 | 62.0 × 61.8 × 6.0 | evet | PLA/PETG | 0.16 | 30 | 11 | 0.6 | alt yüz (etiket cebi) tablada, destek YOK |
| `stl/ayar_karti.stl` | 22.7 | 62.0 × 61.8 × 20.0 | evet | PLA/PETG | 0.16 | 30 | 14 | 0.8 | alt yüz tablada, destek YOK |

## Basılan parçalar arası çakışma (montajda, mm³; ≈0 olmalı)
- govde_alt × ust_kapak: 0.0000 mm³ TAMAM
- (listelenmeyen çiftlerde kesişim hacmi tam 0)

## İç parçaların (elektronik zarfları) basılan parçalarla çakışması ve en küçük boşluk
- Taşıyıcı pertinaks 5x7: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (govde_alt)
- Pertinaks altı lehim/kablo: kesişim 0.0000 mm³ → TAMAM; en yakın parça 2.44 mm (govde_alt)
- ESP32-S3-DevKitC-1 (+headerlar): kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.56 mm (govde_alt)
- ESP32 anten çıkıntısı: kesişim 0.0000 mm³ → TAMAM; en yakın parça > 5 mm
- Seviye çevirici + 1000 µF + klemensler: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.40 mm (govde_alt)
- MAX98357A PCB: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (govde_alt)
- MAX98357A bileşen/klemens: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.45 mm (govde_alt)
- Hoparlör Ø40x20: kesişim -0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (govde_alt)
- USB-C kartı: kesişim -0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (govde_alt)
- INMP441 kartı: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.05 mm (govde_alt)
- RC522 PCB: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (ust_kapak)
- RC522 bileşenleri (alt): kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.80 mm (rc522_tutucu)
- NeoPixel halka Ø104/Ø90: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (ust_kapak)
- NTAG213 Ø25: kesişim 0.0000 mm³ → TAMAM; en yakın parça 0.00 mm (figur_taban)

## İç parçaların birbiriyle çakışması
- yok (TAMAM)

## Ölçü kuralları
- TAMAM Halka kanalı halkayı alır (Ø90/Ø104 + boşluk): kanal Ø89.2–Ø104.8, halka Ø90–Ø104, radyal boşluk 0.4 mm
- TAMAM Kanal derinliği ≥ halka kalınlığı + 0,5: 4.3 mm (halka 3.5)
- TAMAM Işık boşluğu (LED → difüzör) ≥ 4 mm: 5.0 mm; LED aralığı (35 LED, Ø97 çevre) ≈ 8.7 mm
- TAMAM Difüzör kalınlığı 1,2–2 mm: 1.8 mm
- TAMAM Yuva tabanı (anten üstü plastik) ≤ 2 mm: 1.8 mm
- TAMAM RC522 anten merkezi yuva merkezinde: kart merkezi x=-10.0, anten kayması 10.0 → anten x=0.0
- TAMAM NFC mesafesi (etiket → anten bakırı) ≤ 6 mm: 3.55 mm (yuva tabanı 1.8 + RC522 FR4 1.6 + cep payı); anahtar oturmazsa (kama üstünde) 8.6 mm — yine okunur
- TAMAM Taban–yuva boşluğu 0,3–0,6 mm: radyal 0.4 mm
- TAMAM Taban yuvada gömülü, üstü kapak yüzeyini aşmaz: taban üstü kapak üstünden 0.2 mm aşağıda
- TAMAM Etiket cebi 0,4 mm ve etiket altında plastik ≤ 1 mm: etiket cebe yapışır; altında plastik yok (koruma için Ø30 keçe/şeffaf bant önerilir)
- TAMAM Duvar ≥ 2 mm: duvar 2.5, taban 2.5, kanal tabanı 2.0; yuva tabanı 1.8 (NFC için bilerek ince)
- TAMAM Toplam yükseklik 45–60 mm: 57.3 mm (+ silikon ayak ~2,5 mm)
- TAMAM Dış çap 120–130 mm: Ø128 mm
- TAMAM USB-C fiş gövdesi ↔ soket ağzı ≤ 1,5 mm: 1.3 mm (dış düz alın)
- TAMAM Mikrofon deliği hoparlör ızgarasından ≥ 80 mm: 127 mm
- TAMAM Birleştirme vidası M3x10 (6 mm kolon + 4 mm insert): M3x10

STL toplamı: 4.1 MB. Süre/filament kaba tahmindir (6 mm³/s, 0,4 meme); dilimleyicinin değerine bakın.

SONUÇ: HATA YOK
