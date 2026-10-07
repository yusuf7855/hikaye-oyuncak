# Yapılacaklar

## Haftaya (2026-10-12 haftası): veriyi 20–30 bine çıkar

Durum (2026-10-06): 10 597 hikâyeli c3ft_karma, 1030 hikâyeli c3ft_urun1030s2'yi kör kıyasta açık farkla geçti
(genel 127–37, olay örgüsü 112–41; `degerlendirme/urun_kiyas_karma/OZET.md`). Veri artışı olay örgüsünü iyileştiren tek
şey oldu; model boyutu aynı kalıyor (c3, 10,3 MB, ESP32-S3 N16R8'e sığar).

Adımlar:
1. Yeni tohumlar: `data/urun_v3/tohum/` gibi figür başına ~950 → ~2000–2800 (farklı seed; mevcut tohumlarla çakışma
   olmasın), istemleri üret (`data/urun_v3/istem/`, scratchpad `v3_istem.py` mantığı; 24 tohum/istem).
2. Hafif hat yazım (yazar + kod kontrolü, hakemsiz): `v3_yaz.js` workflow, 4 kol × 12'li grup. 10 bin ≈ 14 saat;
   konteyner yeniden başlarsa bitmemiş istemleri (kontrol/*.json olmayanlar) yeniden başlat.
3. `urun_hafif_topla.py topla` + `birlestir` (yeni klasör için V3 yolunu genişlet ya da urun_v4 ekle).
4. Eğitim: `IZIN=data/urun_karma/izin.txt TEKRAR=2 GENEL=4000000 STEPS=<6000 × veri/10 bin> TAG=c3ft_karma2 zincir_urun.sh`
   (aynı 10 bin veride 12 bin adım 6000'den kötü çıktı: val 2,054 / 2,015; adımı veriyle orantılı artır.
   Arka plan görevi 2 saatte kesilir, train kaldığı yerden sürer).
   Disk dolabilir: önce eski `data/tr_c*`, `runs/ple-c2*` vb. temizle.
5. Kör kıyas c3ft_karma2 – c3ft_karma: `urun_uret.py --aday 8 --tekrar-vaka 4` + 8 hakem (IKILI_GENEL/IKILI),
   anahtar hakemlik süresince klasör dışında; ardından rubrik puanı (RUBRIK.md).

## Sonra
- ESP32 yazılımını ürün figürlerine (11 figür, kart kataloğu) uyarla ve c3ft_karma'yı cihaza koy; cihaz hâlâ eski hayvan
  kataloğunu kullanıyor. Cihazda K=16 aday kuyruğu, web'de K=4.
