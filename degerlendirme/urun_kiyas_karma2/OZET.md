# 16,5 bin hikâyeli model (c3ft_karma2) – 10,6 bin hikâyeli model (c3ft_karma): kör ikili kıyas

- **c3ft_karma2:** urun_v2 hakemli 1030 + urun_v3 hafif hat 9567 + urun_v4 hafif hat 5922 (gece/ninni metinleri
  hariç, `birlestir urun_karma2 urun_v3 urun_v4 --gecesiz`) = 16 519 hikâye.
  `IZIN=data/urun_karma2/izin.txt TEKRAR=2 GENEL=6000000 STEPS=10000 zincir_urun.sh` (bulutta CPU, ~3,5 saat),
  en iyi adım 8500, val 1,929 (aynı 41 hikâyelik doğrulama bölmesi).
- **c3ft_karma:** 10 597 hikâye, 6000 adım, val 2,015 (`degerlendirme/urun_kiyas_karma/OZET.md`).
- Model boyutu aynı (c3, model.bin 10,3 MB). Golden testi geçti (C = PyTorch).

Aynı 164 vaka (41 figür×yer × 4 tohum), ikisi de 8 aday + isim süzgeci + seçici (`urun_uret.py --aday 8
--tekrar-vaka 4`). Bu konteynerde `degerlendirme/sozluk.pkl` yoktu (gitignore); `sozluk_olustur.py` ile yeniden
kuruldu. Adil olsun diye c3ft_karma'nın kayıtlı 8 adayı da aynı (güncel) seçiciyle yeniden seçildi
(`mkarma.json`; 164 vakanın 4'ünde seçim değişti).

Seçici puanı: karma2 −2,00 (138 cezasız) – karma −2,05 (133 cezasız).

4 parti × 2 hakem (IKILI_GENEL.md, IKILI.md; `hakem/`); A/B sırası rastgele (tohum 4141), anahtar hakemlik
süresince klasör dışındaydı (`anahtar.json` sonradan kondu).

| Hakem | karma2 | karma | eşit | p (tek yönlü işaret testi, karma2 > karma) |
|---|---|---|---|---|
| Genel kalite | 83 | 81 | 0 | 0,47 |
| Olay örgüsü | 83 | 77 | 4 | 0,35 |

**Sonuç:** fark yok. Veri 10,6 binden 16,5 bine çıkınca (urun_v4 eklendi) doğrulama kaybı belirgin düştü (2,015 →
1,929) ama kör hakemler iki modeli ayırt edemedi. 1030 → 10 597 artışının getirdiği büyük kazanç (127–37) bu
adımda tekrarlanmadı: bu model boyutunda alan içi veri artışının getirisi azalıyor ya da urun_v4 hikâyeleri v3'e
çok benziyor. Doğrulama kaybı tek başına karar vermez (CLAUDE.md §5).

Ürün için: c3ft_karma2 c3ft_karma'dan kötü değil; yeni 12 figürlü son model (urun_v5) bütün veriyle eğitilecek.
