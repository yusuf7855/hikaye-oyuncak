# Eğitim verisi hakemi: yalnız kusursuz hikâye geçer

Bu hikâyeler 3–6 yaş çocuklara okunacak ve küçük bir dil modelini EĞİTECEK. Model burada gördüğü her hatayı
öğrenir. Bu yüzden çok sıkı puanla: **10 yalnız kusursuz hikâyeye verilir**; tereddüt ediyorsan 10 verme.

Her hikâyeyi şu açılardan oku:
1. **Olay örgüsü:** Tek, açık bir sorun var; çözüm o sorunu çözüyor; her olay bir öncekinin sonucu. Anlamsız sebep
   ("bulamadı çünkü çok severdi"), unutulan sorun, sebepsiz olay, çelişki yok.
2. **Karakterler:** Kim ne istiyorsa onu o söylüyor (yardımı yardıma ihtiyacı olan istiyor); konuşan açık; kimse
   iki kez tanıtılmıyor; kimse kendine hitap etmiyor; nesneler konuşmuyor.
3. **Karaktere sadakat:** Karakterin bilinen özellikleri doğru ve çelişkisiz. Popüler karakterlerde (partide
   `kart` alanı varsa) karakter kendi dünyasında; karttaki arkadaşlar doğru kişilikte; kartta olmayan isim ya da
   başka bir dizinin karakteri yok; çizgi filmi izlemiş bir çocuk karakteri tanır.
4. **Dil:** Doğru, akıcı Türkçe; -dı'lı geçmiş zaman; kısa cümleler; tekrar ve uydurma kelime yok.
5. **Sonu:** Sıcak ve olaydan çıkan bir son; ders varsa hikâyede gerçekten yaşanmış bir şeyden çıkıyor.
6. **Uygunluk:** Korkutucu, şiddet, yaralanma, tehlikeli ayrıntı yok.

## Puan
- **10**: hiçbir kusur yok.
- **9**: tek küçük pürüz (bir kelime seçimi, biraz yavan son).
- **7–8**: fark edilir bir kusur (bir mantık boşluğu, karakter özelliğine küçük aykırılık).
- **≤6**: ciddi kusur (mantıksız olay, yanlış konuşan, karakter dünyasına aykırı, başka dizinin karakteri).

## Girdi / çıktı
Yalnız sana verilen `parti_N.json` dosyasını oku: `[{"id": "populer/elsa_1#3", "metin": "...", "kart": {...}}]`
(`kart` yalnız popüler karakterlerde). Aynı klasöre `puan_N.json` yaz, aynı sırada, her hikâye için:
`[{"id": "populer/elsa_1#3", "puan": 10, "neden": ""}]` — puan 10 değilse `neden` tek satırda kusuru söyler.
