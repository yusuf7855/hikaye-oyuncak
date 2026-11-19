// Eko – TÜBİTAK 1812 BiGG Yatırım sunumu (10 slayt). Metin: ../06_SUNUM_METNI.md, rakamlar: ../cikti/finans_ozet.json
// Çalıştır: NODE_PATH=<pptxgenjs, react-icons, react, react-dom, sharp kurulu node_modules> node sunum.js
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const md = require("react-icons/md");

const SKILL = process.env.PPTX_SKILL || "";
const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));
const KOK = path.resolve(__dirname, "..");
const CIKTI = path.join(KOK, "cikti", "Eko_Sunum.pptx");
const oz = JSON.parse(fs.readFileSync(path.join(KOK, "cikti", "finans_ozet.json"), "utf8"));

const THEME = {
  name: "Eko Gece Masalı",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2147", lt1: "FFFFFF", dk2: "2E3A7A", lt2: "EEF1FB",
    accent1: "F4B942", accent2: "E8645A", accent3: "2F9C8F", accent4: "7C6CD9",
    accent5: "5B8DEF", accent6: "8A93B8", hlink: "5B8DEF", folHlink: "7C6CD9",
  },
};
const HEX = THEME.colors;

async function ikon(Bilesen, renk, boy = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Bilesen, { color: "#" + renk, size: boy }));
  const png = await sharp(Buffer.from(svg)).resize(boy, boy).png().toBuffer();
  return "image/png;base64," + png.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
  pres.title = "Eko – TÜBİTAK 1812 BiGG Yatırım sunumu";
  pres.author = "[AD SOYAD]";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  // ---- Düzenler ----
  pres.defineSlideMaster({
    title: "KOYU",
    background: { color: C.text1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.2, w: 5.6, h: 1.3, fontSize: 60, bold: true, color: C.background1, fontFace: THEME.headFontFace, valign: "bottom", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 2.6, w: 5.6, h: 1.0, fontSize: 20, color: C.background2, fontFace: THEME.bodyFontFace, valign: "top", align: "left", margin: 0 }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "ICERIK",
    background: { color: C.background1 },
    margin: [0.5, 0.5, 0.6, 0.5],
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 9.0, h: 0.75, fontSize: 30, bold: true, color: C.text1, fontFace: THEME.headFontFace, valign: "middle", margin: 0 }, text: "" } },
      { text: { text: "Eko · TÜBİTAK 1812 BiGG Yatırım", options: { x: 0.5, y: 5.2, w: 5, h: 0.3, fontSize: 10, color: C.accent6, fontFace: THEME.bodyFontFace, margin: 0 } } },
    ],
    slideNumber: { x: 9.0, y: 5.2, w: 0.5, h: 0.3, fontSize: 10, color: C.accent6, align: "right" },
  });

  const ICON = {
    figur: await ikon(fa.FaChessPawn, HEX.dk1), isik: await ikon(fa.FaRegLightbulb, HEX.dk1),
    kitap: await ikon(fa.FaBookOpen, HEX.dk1), mik: await ikon(fa.FaMicrophone, HEX.dk1),
    tekrar: await ikon(fa.FaRedoAlt, HEX.lt1), bulut: await ikon(fa.FaCloudUploadAlt, HEX.lt1),
    cip: await ikon(fa.FaMicrochip, HEX.lt1), ay: await ikon(fa.FaMoon, HEX.dk1),
    oynat: await ikon(fa.FaPlayCircle, HEX.accent6), kalkan: await ikon(fa.FaShieldAlt, HEX.dk1),
    wifi: await ikon(md.MdWifiOff, HEX.dk1), ses: await ikon(fa.FaVolumeUp, HEX.dk1),
    beyin: await ikon(fa.FaFeatherAlt, HEX.dk1), kisi: await ikon(fa.FaUserAlt, HEX.dk1),
    ekip: await ikon(fa.FaUsers, HEX.dk1),
  };

  // halka motifi: 16 LED'li ışık halkası
  function halka(slide, cx, cy, r, renk, dolu, boy = 0.16) {
    for (let i = 0; i < 16; i++) {
      const a = (Math.PI * 2 * i) / 16 - Math.PI / 2;
      slide.addShape(pres.shapes.OVAL, {
        x: cx + r * Math.cos(a) - boy / 2, y: cy + r * Math.sin(a) - boy / 2, w: boy, h: boy,
        fill: { color: i < dolu ? renk : C.text2 }, line: { color: i < dolu ? renk : C.text2, width: 0 },
        objectName: `halka-led-${i + 1}`,
      });
    }
  }
  function ikonDaire(slide, x, y, d, ikonData, dolgu, ad) {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: dolgu }, line: { color: dolgu, width: 0 }, objectName: ad + "-daire" });
    slide.addImage({ data: ikonData, x: x + d * 0.22, y: y + d * 0.22, w: d * 0.56, h: d * 0.56, objectName: ad + "-ikon" });
  }
  function kart(slide, x, y, w, h, ad, dolgu = C.background2) {
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: dolgu }, line: { color: dolgu, width: 0 }, objectName: ad });
  }
  const tl = (x) => x.toLocaleString("tr-TR");

  // ---- 1 Kapak ----
  pres.addSection({ title: "Açılış" });
  let s = pres.addSlide({ masterName: "KOYU", sectionTitle: "Açılış" });
  s.addText("Eko", { placeholder: "title" });
  s.addText("İnternetsiz, cihaz içi yapay zekâlı Türkçe hikâye oyuncağı", { placeholder: "body" });
  s.addText("Her gece yeni bir masal. Çocuğunuzun sesi hiçbir yere gitmez.", { x: 0.6, y: 3.65, w: 5.6, h: 0.6, fontSize: 16, italic: true, color: C.accent1, margin: 0, isTextBox: true, objectName: "slogan" });
  s.addText("[AD SOYAD], kurucu  ·  TÜBİTAK 1812 BiGG Yatırım  ·  2027", { x: 0.6, y: 4.75, w: 6, h: 0.35, fontSize: 12, color: C.accent6, margin: 0, isTextBox: true, objectName: "sunan" });
  halka(s, 7.85, 2.75, 1.35, C.accent1, 16, 0.2);
  s.addShape(pres.shapes.OVAL, { x: 7.0, y: 1.9, w: 1.7, h: 1.7, fill: { color: C.text2 }, line: { color: C.text2, width: 0 }, objectName: "stand" });
  s.addImage({ data: await ikon(fa.FaChessPawn, HEX.accent1), x: 7.45, y: 2.3, w: 0.8, h: 0.9, objectName: "figur" });
  s.addNotes("Merhaba, ben [ad]. Eko'yu anlatacağım: çocuklara her seferinde yeni bir Türkçe hikâye anlatan, ama internete hiç bağlanmayan bir oyuncak.");

  // ---- 2 Demo ----
  pres.addSection({ title: "Ürün" });
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Ürün" });
  s.addText("Figürü koy, Eko yeni bir masal anlatsın", { placeholder: "title" });
  kart(s, 0.5, 1.3, 4.6, 3.6, "video-alani");
  s.addImage({ data: ICON.oynat, x: 2.35, y: 2.45, w: 0.9, h: 0.9, objectName: "oynat" });
  s.addText("Demo videosu (30–45 sn) buraya eklenecek", { x: 0.7, y: 3.5, w: 4.2, h: 0.5, fontSize: 14, color: C.text2, align: "center", isTextBox: true, objectName: "video-not" });
  const adimlar = [
    [ICON.figur, "Figürü standa koy", "Keloğlan, Pinokyo, Bulut, Bip … 13 figür"],
    [ICON.isik, "Eko selamlar", "Işık halkası figürün renginde dolar"],
    [ICON.kitap, "Her seferinde yeni hikâye", "Cihazın içinde o anda yazılır ve okunur"],
    [ICON.mik, "“Merhaba Eko, başka”", "Dur, devam, bir daha, sesini aç/kıs"],
  ];
  adimlar.forEach(([ik, bas, alt], i) => {
    const y = 1.3 + i * 0.92;
    ikonDaire(s, 5.45, y, 0.62, ik, C.accent1, `adim${i + 1}`);
    s.addText(bas, { x: 6.25, y: y - 0.02, w: 3.3, h: 0.36, fontSize: 16, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: `adim${i + 1}-baslik` });
    s.addText(alt, { x: 6.25, y: y + 0.33, w: 3.3, h: 0.36, fontSize: 13, color: C.text2, margin: 0, isTextBox: true, objectName: `adim${i + 1}-alt` });
  });
  s.addNotes("Figür standa konur, halka figürün renginde dolar, Eko selamlar ve hikâyeyi anlatır. 'Merhaba Eko, başka' denince yeni bir hikâye gelir. Gördüğünüz her şey bu küçük kartın içinde oluyor: hikâyeyi yazan model de, okuyan ses de, sesli komutu duyan model de. İnternet yok, uygulama yok, abonelik yok.");

  // ---- 3 Problem ----
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Ürün" });
  s.addText("Ebeveynler iki kötü seçenek arasında kalıyor", { placeholder: "title" });
  const sutun = (x, ik, renk, baslik, maddeler, ad) => {
    kart(s, x, 1.3, 4.35, 3.6, ad);
    ikonDaire(s, x + 0.3, 1.5, 0.7, ik, renk, ad);
    s.addText(baslik, { x: x + 1.15, y: 1.5, w: 3.0, h: 0.7, fontSize: 18, bold: true, color: C.text1, valign: "middle", margin: 0, isTextBox: true, objectName: ad + "-baslik" });
    s.addText(maddeler.map((m, i) => ({ text: m, options: { bullet: true, breakLine: i < maddeler.length - 1, paraSpaceAfter: 6 } })),
      { x: x + 0.3, y: 2.4, w: 3.85, h: 2.35, fontSize: 14, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: ad + "-maddeler" });
  };
  sutun(0.5, ICON.tekrar, C.accent6, "Ses kutuları\n(Toniebox, Yoto)", [
    "Her figür hep aynı kaydı çalar; çocuk sıkılır",
    "Yeni içerik için yeni figür almak gerekir",
    "Türkçe içerik yok denecek kadar az",
  ], "ses-kutulari");
  sutun(5.15, ICON.bulut, C.accent2, "Bulut yapay zekâlı oyuncaklar", [
    "Çocuğun sesi ve sohbeti sunucuya gider",
    "FoloToy: uygunsuz yanıtlar, erişimi kesildi (2025)",
    "Bondu: ≈50 bin çocuk sohbeti açıkta kaldı (2026)",
    "Moxie: sunucu kapandı, oyuncak çalışmaz oldu",
  ], "bulut-oyuncaklar");
  s.addNotes("Ebeveynler ekransız içerik istiyor ama ses kutuları hep aynı kaydı çalıyor. Bulut yapay zekâlı oyuncaklar ise çocuğun sesini sunucuya gönderiyor; FoloToy, Bondu ve Moxie örnekleri. Anne-babalar iki kötü seçenek arasında kalıyor: ya sıkıcı, ya riskli.");

  // ---- 4 Çözüm ----
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Ürün" });
  s.addText("Üç yapay zekâ modeli, tek mikrodenetleyicide", { placeholder: "title" });
  kart(s, 0.5, 1.25, 9.0, 0.75, "cip-bandi", C.text1);
  s.addImage({ data: ICON.cip, x: 0.75, y: 1.37, w: 0.5, h: 0.5, objectName: "cip-ikon" });
  s.addText("ESP32-S3  ·  16 MB flash  ·  8 MB PSRAM  ·  4 × AA pil", { x: 1.45, y: 1.25, w: 7.8, h: 0.75, fontSize: 18, bold: true, color: C.background1, valign: "middle", margin: 0, isTextBox: true, objectName: "cip-metin" });
  const modeller = [
    [ICON.beyin, "10,3 MB", "Hikâye modeli", "≈19,9 M parametre (4 bit); önce plan, sonra hikâye"],
    [ICON.ses, "4,3 MB", "Ses modeli", "Kadın sesi; gece modunda yavaş ve kısık"],
    [ICON.mik, "110 KB", "“Merhaba Eko”", "Uyandırma sözcüğü ve 6 sesli komut"],
  ];
  modeller.forEach(([ik, boyut, ad, alt], i) => {
    const x = 0.5 + i * 3.08;
    kart(s, x, 2.2, 2.84, 1.75, `model${i + 1}`);
    ikonDaire(s, x + 0.2, 2.38, 0.55, ik, C.accent1, `model${i + 1}`);
    s.addText(boyut, { x: x + 0.9, y: 2.33, w: 1.8, h: 0.6, fontSize: 26, bold: true, color: C.text1, fontFace: THEME.headFontFace, valign: "middle", margin: 0, isTextBox: true, objectName: `model${i + 1}-boyut` });
    s.addText(ad, { x: x + 0.2, y: 3.0, w: 2.5, h: 0.32, fontSize: 15, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: `model${i + 1}-ad` });
    s.addText(alt, { x: x + 0.2, y: 3.32, w: 2.5, h: 0.55, fontSize: 12, color: C.text2, margin: 0, valign: "top", isTextBox: true, objectName: `model${i + 1}-alt` });
  });
  const katman = ["Kapalı dünya (figür kartı)", "İsim süzgeci", "5 aday + seçici", "Hazır hikâye kuyruğu", "Ağ yok, kayıt yok"];
  katman.forEach((k, i) => {
    const x = 0.5 + i * 1.82;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.2, w: 1.7, h: 0.6, rectRadius: 0.3, fill: { color: C.accent3 }, line: { color: C.accent3, width: 0 }, objectName: `katman${i + 1}` });
    s.addText(k, { x, y: 4.2, w: 1.7, h: 0.6, fontSize: 12, bold: true, color: C.background1, align: "center", valign: "middle", margin: 2, isTextBox: true, objectName: `katman${i + 1}-metin` });
  });
  s.addNotes("Tek bir ESP32-S3 üzerinde üç model: 10,3 MB'lık Türkçe hikâye modeli, 4,3 MB'lık ses modeli ve 110 KB'lık uyandırma modeli. Güvenlik katmanları: her figürün kapalı dünyası, başka figür adlarını engelleyen isim süzgeci, 5 aday arasından seçici ve boştayken önceden yazılan hikâye kuyruğu.");

  // ---- 5 Kanıt ----
  pres.addSection({ title: "Kanıt ve pazar" });
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Kanıt ve pazar" });
  s.addText("Kalite ölçüldü, yazılım doğrulandı", { placeholder: "title" });
  const kanit = [
    ["28.493", "özgün hikâyeyle eğitildi"],
    ["102–78", "kör kıyas (yapay zekâ hakemli): son model ara modeli yendi"],
    ["52 / 52", "kart yazılımı PC referansıyla birebir aynı aday"],
    ["≥ 79 dB", "ses: kartın C kodu = PyTorch (SNR)"],
  ];
  kanit.forEach(([sayi, et], i) => {
    const x = 0.5 + i * 2.27;
    kart(s, x, 1.3, 2.1, 2.0, `kanit${i + 1}`);
    s.addText(sayi, { x: x + 0.12, y: 1.42, w: 1.86, h: 0.85, fontSize: 32, bold: true, color: C.text2, fontFace: THEME.headFontFace, align: "left", valign: "middle", margin: 0, isTextBox: true, objectName: `kanit${i + 1}-sayi` });
    s.addText(et, { x: x + 0.12, y: 2.3, w: 1.86, h: 0.9, fontSize: 13, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: `kanit${i + 1}-etiket` });
  });
  s.addText("Teknoloji hazırlık seviyesi", { x: 0.5, y: 3.6, w: 4, h: 0.35, fontSize: 14, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "trl-baslik" });
  for (let i = 1; i <= 9; i++) {
    const x = 0.5 + (i - 1) * 1.0;
    const renk = i <= 4 ? C.accent3 : i <= 8 ? C.accent1 : C.background2;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.05, w: 0.92, h: 0.42, rectRadius: 0.08, fill: { color: renk }, line: { color: renk, width: 0 }, objectName: `trl${i}` });
    s.addText(`TRL ${i}`, { x, y: 4.05, w: 0.92, h: 0.42, fontSize: 12, bold: true, color: i <= 8 ? C.text1 : C.accent6, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `trl${i}-metin` });
  }
  s.addText("Bugün yazılım ve modeller TRL 4, donanım TRL 3 (yeşil)  →  18. ayda TRL 8: CE belgeli, pilotta doğrulanmış ürün (sarı)", { x: 0.5, y: 4.55, w: 9, h: 0.35, fontSize: 12, color: C.text2, margin: 0, isTextBox: true, objectName: "trl-not" });
  s.addNotes("Modeli 28.493 özgün hikâyeyle eğittik. Kaliteyi kör kıyasla ölçtük: yapay zekâ hakemleri hangi modelin yazdığını bilmeden seçiyor; insan hakemli kör testi pilotta yapacağız. Son model ara modeli 180 vakada 102'ye 78, olay örgüsünde 99'a 73 yendi; Keloğlan'da önceki ürün modelini 34'e 14 yendi. Kart yazılımı PC'de referans üretimle birebir aynı; ses modelinin C kodu PyTorch ile aynı sonucu veriyor. Bugün TRL 4'teyiz; proje sonunda CE belgeli ürünle TRL 8.");

  // ---- 6 Pazar ----
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Kanıt ve pazar" });
  s.addText("3,3 milyon hane, büyüyen bir kategori", { placeholder: "title" });
  const katmanlar = [
    [0.5, 1.25, 5.2, 3.65, C.background2, "TAM  ≈8,2 milyar TL", "≈3,3 milyon hane (3–6 yaş), her yıl ≈0,93 milyon yeni çocuk", C.text1],
    [0.85, 2.3, 4.5, 2.4, C.accent4, "SAM  ≈2,5 milyar TL", "kentli, orta-üst gelirli ≈1 milyon hane", C.background1],
    [1.2, 3.3, 3.8, 1.2, C.text1, "SOM  86.000 set", "6,5 yılda, KDV hariç ≈240 M TL ciro", C.background1],
  ];
  katmanlar.forEach(([x, y, w, h, dolgu, bas, alt, renk], i) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: dolgu }, line: { color: dolgu, width: 0 }, objectName: `pazar${i + 1}` });
    s.addText([{ text: bas, options: { bold: true, fontSize: 16, breakLine: true } }, { text: alt, options: { fontSize: 12 } }],
      { x: x + 0.2, y: y + 0.1, w: w - 0.4, h: 0.85, color: renk, valign: "top", margin: 0, isTextBox: true, objectName: `pazar${i + 1}-metin` });
  });
  const istat = [["630 M€", "tonies 2025 cirosu, +%31"], ["%85", "Türkiye oyuncak pazarında ithalat payı"], ["2.500–3.500 TL", "Türkiye'de boş fiyat bandı"]];
  istat.forEach(([sayi, et], i) => {
    const y = 1.25 + i * 1.25;
    s.addText(sayi, { x: 6.0, y, w: 3.5, h: 0.6, fontSize: 28, bold: true, color: C.text2, fontFace: THEME.headFontFace, margin: 0, isTextBox: true, objectName: `istat${i + 1}-sayi` });
    s.addText(et, { x: 6.0, y: y + 0.6, w: 3.5, h: 0.45, fontSize: 13, color: C.text1, margin: 0, isTextBox: true, objectName: `istat${i + 1}-etiket` });
  });
  s.addText("Kaynak: TÜİK doğum istatistikleri, TOYDER, tonies; segment payları ve SOM varsayımdır.", { x: 6.0, y: 4.85, w: 3.5, h: 0.3, fontSize: 10, color: C.accent6, margin: 0, isTextBox: true, objectName: "pazar-kaynak" });
  s.addNotes("2028'de Türkiye'de yaklaşık 3,9 milyon 3–6 yaş çocuk ve 3,3 milyon hane olacak; KDV hariç toplam pazar yaklaşık 8,2 milyar TL. Hedef segmentimiz kentli, orta-üst gelirli 1 milyon hane. Dünyada kategori ekran kaygısıyla büyüyor: tonies 2025'te 630 milyon euro ciro yaptı. Türkiye'de 2.500–3.500 TL bandı boş.");

  // ---- 7 Rakipler ----
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "Kanıt ve pazar" });
  s.addText("Üç özelliği bir arada sunan tek ürün", { placeholder: "title" });
  const evet = { text: "✔", options: { color: HEX.accent3, bold: true } }, hayir = { text: "✘", options: { color: HEX.accent2, bold: true } }, kismen = { text: "~", options: { color: HEX.accent6, bold: true } };
  const hc = (o) => [{ ...o, options: { ...o.options } }];
  const bas = (t) => ({ text: t, options: { bold: true, color: HEX.lt1, fill: { color: HEX.dk1 } } });
  const satir = (et, ...h) => [{ text: et, options: { bold: true } }, ...h.map((x) => (typeof x === "string" ? { text: x } : hc(x)[0]))];
  s.addTable([
    [bas(""), bas("Eko"), bas("Toniebox / Yoto"), bas("Miko / Curio"), bas("Yerli sabit masallı")],
    satir("Her seferinde yeni hikâye", evet, hayir, evet, hayir),
    satir("İnternetsiz", evet, kismen, hayir, evet),
    satir("Veri göndermez", evet, kismen, hayir, evet),
    satir("Abonelik yok", evet, kismen, hayir, evet),
    satir("Türkçe", evet, hayir, kismen, evet),
    satir("Fiyat", "2.999 TL", "5.400–6.800 TL", "≈10.000 TL +", "≈1.600 TL"),
  ], { x: 0.5, y: 1.25, w: 9.0, colW: [2.6, 1.4, 1.75, 1.6, 1.65], rowH: 0.48, fontSize: 14, color: HEX.dk1, fontFace: THEME.bodyFontFace, valign: "middle", align: "center", border: { type: "solid", pt: 0.75, color: "D5DAEC" }, fill: { color: HEX.lt1 }, objectName: "rakip-tablosu" });
  s.addText("~ kısmen: kurulum için Wi-Fi, kart/figür satın alma ya da çeviri düzeyinde Türkçe", { x: 0.5, y: 4.75, w: 9, h: 0.3, fontSize: 10, color: C.accent6, margin: 0, isTextBox: true, objectName: "rakip-not" });
  s.addNotes("Ses kutuları sabit kayıt çalıyor, bulut oyuncakları veri gönderiyor ve abonelik istiyor, yerli sabit masallı oyuncaklar ise 3–5 masalla sınırlı. Eko yeni hikâye, internetsiz ve veri göndermeyen yapıyı Türkçe olarak, ithal rakiplerin yaklaşık yarı fiyatına sunuyor.");

  // ---- 8 İş modeli ve finans ----
  pres.addSection({ title: "İş planı" });
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "İş planı" });
  s.addText("Cihaz satışı + ek figür paketleri, abonelik yok", { placeholder: "title" });
  const fiyat = [["2.999 TL", "başlangıç seti", "cihaz + 3 figür + Ay Dede"], ["449 TL", "ek figür paketi", "3 figür, tekrar eden gelir"], ["12.000 TL", "okul öncesi seti", "5 cihaz + 13 figür (KDV hariç)"]];
  fiyat.forEach(([f, ad, alt], i) => {
    const y = 1.25 + i * 1.05;
    kart(s, 0.5, y, 3.6, 0.92, `fiyat${i + 1}`);
    s.addText(f, { x: 0.65, y, w: 1.55, h: 0.92, fontSize: 20, bold: true, color: C.text2, fontFace: THEME.headFontFace, valign: "middle", margin: 0, isTextBox: true, objectName: `fiyat${i + 1}-tutar` });
    s.addText([{ text: ad, options: { bold: true, breakLine: true } }, { text: alt, options: { fontSize: 11, color: HEX.dk2 } }], { x: 2.2, y, w: 1.85, h: 0.92, fontSize: 14, color: C.text1, valign: "middle", margin: 0, isTextBox: true, objectName: `fiyat${i + 1}-metin` });
  });
  s.addText("Katkı payı ≈1.140 TL/set (%46) · LTV/CAC ≈2,9 · sunucu maliyeti 0", { x: 0.5, y: 4.45, w: 3.6, h: 0.55, fontSize: 12, bold: true, color: C.accent3, margin: 0, valign: "top", isTextBox: true, objectName: "birim-ekonomi" });
  const yillar = oz.yillar.map((r) => r.kisa);
  s.addChart(pres.charts.BAR, [
    { name: "Ciro (M TL)", labels: yillar, values: oz.yillar.map((r) => Math.round(r.ciro / 1e5) / 10) },
    { name: "FAVÖK (M TL)", labels: yillar, values: oz.yillar.map((r) => Math.round(r.favok / 1e5) / 10) },
  ], {
    x: 4.4, y: 1.2, w: 5.1, h: 3.85, barDir: "col", barGrouping: "clustered",
    chartColors: [HEX.dk2, HEX.accent1], showLegend: true, legendPos: "b", legendFontSize: 11, legendFontFace: "+mn-lt",
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 9, dataLabelFontFace: "+mn-lt", dataLabelColor: HEX.dk1, dataLabelFormatCode: "0.0",
    showTitle: true, title: "Ciro ve FAVÖK (M TL, sabit 2026 fiyatları)", titleFontSize: 12, titleFontFace: "+mn-lt", titleColor: HEX.dk1,
    catAxisLabelColor: HEX.dk2, valAxisLabelColor: HEX.accent6, catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt",
    valGridLine: { color: "E3E7F3", size: 0.5 }, catGridLine: { style: "none" }, objectName: "finans-grafigi",
  });
  s.addNotes(`Başlangıç seti 2.999 TL, ek figür paketi 449 TL, okul öncesi seti 5 cihazlık. Birim katkı payı yaklaşık 1.140 TL; sunucu maliyeti olmadığı için satılan cihaz başına sürekli gider sıfır. Proje döneminde 1.000 set, beşinci ticari yılda ${tl(oz.yillar[5].adet)} set; FAVÖK ikinci ticari yılda pozitife dönüyor. Y0 18 aylık proje dönemidir.`);

  // ---- 9 18 aylık plan ----
  s = pres.addSlide({ masterName: "ICERIK", sectionTitle: "İş planı" });
  s.addText("18 ayda pilotta doğrulanmış, CE belgeli ürün", { placeholder: "title" });
  const kt = [["1–2", "Şirket, İP devri, hız/ses/pil ölçümü"], ["3–4", "Kendi kartımız (EVT), marka/tasarım"], ["5–7", "60 cihaz; 30–50 aile + 3–5 okul pilotu"], ["8–9", "DVT, ön uygunluk testi"], ["12", "Kitle fonlama ≥600 ön sipariş"], ["15–17", "CE/RED belgeleri, ilk 1.000 set"], ["18", "Web, pazaryeri, kurum satışı"]];
  s.addShape(pres.shapes.LINE, { x: 0.75, y: 1.62, w: 8.55, h: 0, line: { color: HEX.accent6, width: 1.5 }, objectName: "zaman-cizgisi" });
  kt.forEach(([ay, is], i) => {
    const x = 0.5 + i * 1.27;
    s.addShape(pres.shapes.OVAL, { x: x + 0.12, y: 1.38, w: 0.48, h: 0.48, fill: { color: i === 6 ? HEX.accent3 : HEX.accent1 }, line: { color: HEX.lt1, width: 1.5 }, objectName: `kt${i + 1}-nokta` });
    s.addText(`Ay ${ay}`, { x: x - 0.1, y: 1.92, w: 1.2, h: 0.3, fontSize: 12, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `kt${i + 1}-ay` });
    s.addText(is, { x: x - 0.1, y: 2.2, w: 1.2, h: 0.85, fontSize: 11, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: `kt${i + 1}-is` });
  });
  const bt = oz.butce;
  const yuzde = (x) => "%" + Math.round((100 * x) / bt.toplam);
  const kalem = [["Personel", bt.personel], ["Hizmet alımı", bt.hizmet], ["Malzeme", bt.malzeme], ["Teçhizat", bt.alet], ["Seyahat", bt.seyahat]].map(([a, v]) => [`${a} ${yuzde(v)}`, v]);
  s.addChart(pres.charts.DOUGHNUT, [{ name: "Bütçe", labels: kalem.map((k) => k[0]), values: kalem.map((k) => k[1]) }], {
    x: 0.45, y: 3.15, w: 1.9, h: 1.9, holeSize: 55, chartColors: [HEX.dk2, HEX.accent1, HEX.accent3, HEX.accent4, HEX.accent6],
    showLegend: false, showPercent: false, showValue: false, showLabel: false,
    showTitle: false, objectName: "butce-grafigi",
  });
  const renkler = [HEX.dk2, HEX.accent1, HEX.accent3, HEX.accent4, HEX.accent6];
  kalem.forEach(([et], i) => {
    const y = 3.35 + i * 0.3;
    s.addShape(pres.shapes.OVAL, { x: 2.4, y: y + 0.07, w: 0.14, h: 0.14, fill: { color: renkler[i] }, line: { color: renkler[i], width: 0 }, objectName: `butce-isaret${i + 1}` });
    s.addText(et, { x: 2.6, y, w: 1.15, h: 0.28, fontSize: 11, color: C.text1, margin: 0, valign: "middle", isTextBox: true, objectName: `butce-etiket${i + 1}` });
  });
  kart(s, 3.8, 3.2, 5.7, 1.85, "butce-kart");
  s.addText([
    { text: "1.350.000 TL · %3 hisse", options: { bold: true, fontSize: 20, color: HEX.dk2, breakLine: true } },
    { text: "TÜBİTAK BİGG Fonu tohum öncesi yatırımı, 18 ay", options: { fontSize: 13, breakLine: true } },
    { text: "Kalıp, belgelendirme ve ilk üretim: ön satış + devam yatırımı", options: { fontSize: 13 } },
  ], { x: 4.0, y: 3.3, w: 5.3, h: 1.65, color: C.text1, valign: "middle", margin: 0, isTextBox: true, objectName: "butce-metin" });
  s.addNotes("İlk iki ayda şirket kuruluşu ve kartta hız, ses ve pil ölçümleri; 3–4. ayda kendi devre kartımız ve marka başvurusu; 5. ayda 60 cihazlık pilot serisi, 6–7. ayda aileler ve okullarla pilot (etik kurul onayı hızlandırma programında alınmış olacak); 8–9. ayda DVT ve ön uygunluk testi; 12. ayda kitle fonlama; 15–17. ayda CE/RED belgeleri ve ilk 1.000 set. Bütçenin %54'ü personel, %29'u hizmet alımı (test laboratuvarı, PCB, endüstriyel tasarım, patent/marka, çocuk gelişimi), %11'i malzeme.");

  // ---- 10 Ekip ve istek ----
  pres.addSection({ title: "Kapanış" });
  s = pres.addSlide({ masterName: "KOYU", sectionTitle: "Kapanış" });
  s.addText("Ekip ve istek", { x: 0.6, y: 0.4, w: 8.8, h: 0.7, fontSize: 32, bold: true, color: C.background1, fontFace: THEME.headFontFace, margin: 0, isTextBox: true, objectName: "kapanis-baslik" });
  const ekip = [["[AD SOYAD]", "Kurucu, teknik lider", "Yapay zekâ ve gömülü yazılım"], ["[AD SOYAD / aranıyor]", "Donanım ve üretim", "PCB, EMC, seri üretim"], ["Danışmanlar", "Çocuk gelişimi, pazarlama", "[AD SOYAD], [AD SOYAD]"]];
  for (let i = 0; i < ekip.length; i++) {
    const [ad, rol, alt] = ekip[i];
    const x = 0.6 + i * 2.95;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.35, w: 2.75, h: 1.75, rectRadius: 0.12, fill: { color: C.text2 }, line: { color: C.text2, width: 0 }, objectName: `ekip${i + 1}` });
    s.addShape(pres.shapes.OVAL, { x: x + 0.2, y: 1.5, w: 0.55, h: 0.55, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, objectName: `ekip${i + 1}-daire` });
    s.addImage({ data: i === 2 ? ICON.ekip : ICON.kisi, x: x + 0.33, y: 1.63, w: 0.29, h: 0.29, objectName: `ekip${i + 1}-ikon` });
    s.addText([{ text: ad, options: { bold: true, fontSize: 15, breakLine: true } }, { text: rol, options: { fontSize: 13, breakLine: true } }, { text: alt, options: { fontSize: 11, color: HEX.lt2 } }],
      { x: x + 0.2, y: 2.12, w: 2.4, h: 0.95, color: C.background1, valign: "top", margin: 0, isTextBox: true, objectName: `ekip${i + 1}-metin` });
  }
  s.addText([{ text: "İstek: ", options: { bold: true, color: HEX.accent1 } }, { text: "hızlandırma programına kabul → 2027-2 BiGG Yatırım çağrısı: 1.350.000 TL, %3 hisse → ardından BiGG+ tohum turu" }],
    { x: 0.6, y: 3.35, w: 8.8, h: 0.7, fontSize: 16, color: C.background1, margin: 0, valign: "middle", isTextBox: true, objectName: "istek" });
  s.addText("“Yapay zekâyı çocuklara, verilerini almadan ulaştırmak istiyoruz.”", { x: 0.6, y: 4.2, w: 8.8, h: 0.6, fontSize: 20, italic: true, color: C.accent1, fontFace: THEME.headFontFace, margin: 0, isTextBox: true, objectName: "kapanis-soz" });
  s.addNotes("Ekip: kurucu ve teknik lider olarak ben; donanım ve üretim için bir kurucu ortak; çocuk gelişimi ve pazarlama danışmanları. İsteğimiz: hızlandırma programına kabul ve ardından 2027-2 tohum öncesi yatırım çağrısında 1.350.000 TL. Yapay zekâyı çocuklara, verilerini almadan ulaştırmak istiyoruz. Teşekkürler.");

  await pres.writeFile({ fileName: CIKTI });
  await applyTheme(CIKTI, THEME);
  console.log("yazıldı:", CIKTI);
})();
