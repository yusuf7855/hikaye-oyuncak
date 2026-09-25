# Düzeltici: hakemin bulduğu kusuru gider

Eğitim hikâyeleri kusursuz (10/10) olmalı. Sana verilen `duzelt.json` listesindeki her hikâyede hakem bir kusur
buldu (`neden`). Görevin: hikâyeyi kaynağında (`dosya`) bulup kusuru gidermek.

1. `dosya`daki hikâyeyi `ilk_cumle` ile bul (metin `metin` alanıyla aynıdır).
2. Hikâyeyi yeniden yaz ya da düzelt: `neden`deki kusur tamamen gitsin, başka kusur eklenmesin. Başlık satırını
   (`### ...`) değiştirme. Plan satırını (`@plan: ...`) yalnız hikâye değiştiği için gerekiyorsa güncelle.
3. Dosyanın o hikâye dışındaki hiçbir yerine dokunma; hikâyelerin sırası ve sayısı aynı kalmalı.
4. Kurallar: dosyanın klasöründeki `KILAVUZ.md` (yazım kılavuzu) ve `degerlendirme/HAKEM_VERI.md` (hakemin
   ölçüsü). Popüler karakterde `kart`a sadık kal.
5. Bitince klasörün `kontrol.py`'sini dosya önekiyle çalıştır (ör. `.venv/bin/python data/oyuncak_v4/kontrol.py
   tek_kus_2`) ve "sorunlu: 0" olana kadar düzelt.
