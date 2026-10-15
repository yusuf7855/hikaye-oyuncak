# Çakıl stand — basılacak parçalar (ölçüler TAHMİN, parçalar gelince `cad/cakil_ic.py` PARCA sözlüğünden düzeltilir)

Üretmek: `python cad/cakil_ic.py --stl --onizle` (önce çarpışma denetimi yazar; "0 sorun" olmalı).
`rc522/` ve `pn5180/` klasörleri yalnız **halka_nfc_tutucu.stl**'de farklı (okuyucu rayları); öteki parçalar aynı.

| Dosya | Malzeme / renk | Baskı notu |
|---|---|---|
| kabuk.stl | PLA/PETG; figür zemininin altındaki ışık oyuğunda zemin 0,6 mm: **beyaz** basılırsa LED ışığı geçer (renkli basılacaksa oyuk delik yapılabilir); "eco ai" için logo katmanında filament değiştir | Ters (üst yüz tabla üstünde) çevrilmiş kaydedildi; çanak deliği ve iç direkler için destek gerekebilir |
| halka_nfc_tutucu.stl | PLA, herhangi bir renk | Halka üstte, okuyucu altta raylara kayar; kabuğun 4 direğine M2,5 vida |
| taban_plakasi.stl | PLA/PETG | Hoparlör ızgarası altta; 4 x M3 vida + kabukta ısıl gömme somun (M3 x 5,7) |
| esp32_rafi.stl | PLA | Taban plakasındaki 4 bacağa M2,5 vida |

Ek: 3 silikon ayak (Ø10 x 1 mm yuva), M3 x 8 vida (4), M3 ısıl gömme somun (4), M2,5 x 6 vida (8).
Hoparlör aşağı bakar: ses tabandaki yıldız ızgarasından ve ayak boşluğundan çıkar.
