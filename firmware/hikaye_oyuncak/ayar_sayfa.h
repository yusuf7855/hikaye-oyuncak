// Ayar sayfası (ayar modunda telefonda açılır; captive portal). Tek dosya, dışarıdan hiçbir şey yüklemez (internet
// yok). Kart: GET / (bu sayfa), GET /durum (JSON), POST /kaydet, /tanit, /sil, /bitir (hikaye_oyuncak.ino web_*).
// Alanların doğrulaması kartta (ayarlar.h); sayfadaki sınırlar yalnız kolaylık.
#pragma once

static const char AYAR_SAYFA[] = R"rawliteral(<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Masalcı Ayarları</title>
<style>
:root{--z:#f6f4ff;--k:#fff;--y:#1d1b2e;--s:#6b6880;--a:#5b4fd8;--h:#c62d3a;--t:#1f8a5b}
@media (prefers-color-scheme:dark){:root{--z:#14131c;--k:#1f1d2b;--y:#ecebf5;--s:#a4a1b8;--a:#9c93ff;--h:#ff7b86;--t:#5fd39a}}
*{box-sizing:border-box}body{margin:0;background:var(--z);color:var(--y);font:16px/1.45 system-ui,sans-serif}
main{max-width:520px;margin:0 auto;padding:16px}h1{font-size:1.4em;margin:.2em 0 .6em}
section{background:var(--k);border-radius:14px;padding:14px 16px;margin:0 0 14px;box-shadow:0 1px 3px #0002}
h2{font-size:1.05em;margin:0 0 .6em}label{display:block;margin:.7em 0 .25em;font-weight:600}
input[type=text],select{width:100%;font-size:1em;padding:.55em;border-radius:9px;border:1px solid var(--s);background:var(--z);color:var(--y)}
input[type=range]{width:100%}.sec label{display:flex;gap:.5em;font-weight:400;margin:.35em 0;align-items:center}
button{font-size:1em;padding:.65em 1.1em;border:0;border-radius:10px;background:var(--a);color:#fff;margin-top:.8em}
button.ikinci{background:transparent;color:var(--a);border:1px solid var(--a)}button.tehlike{background:var(--h)}
.not{color:var(--s);font-size:.9em}.ileti{margin-top:.6em;min-height:1.3em}.iyi{color:var(--t)}.kotu{color:var(--h)}
ul{padding-left:1.2em;margin:.3em 0}
</style></head><body><main>
<h1>Masalcı Ayarları</h1>
<p class="not" id="kalan">Bağlanıyor...</p>
<section><h2>Çocuk ve ses</h2>
<label for="ad">Çocuğun adı</label>
<input type="text" id="ad" maxlength="20" autocomplete="off" placeholder="ör. Emre (boş bırakılabilir)">
<p class="not">En çok 20 harf; yalnız harf ve boşluk. Selamlamada söylenir.</p>
<label for="ses_maks">En yüksek ses: <span id="ses_maks_d"></span></label>
<input type="range" id="ses_maks" min="1" max="7" step="1">
<label>Uyku zamanlayıcısı (Ay Dede: ninniler bu kadar sürer)</label>
<div class="sec" id="uyku_dk"><label><input type="radio" name="uyku_dk" value="10"> 10 dakika</label>
<label><input type="radio" name="uyku_dk" value="20"> 20 dakika</label>
<label><input type="radio" name="uyku_dk" value="30"> 30 dakika</label></div>
<div class="sec"><label><input type="checkbox" id="muzik"> Ninnide çok kısık müzik kutusu</label></div>
</section>
<section><h2>Işık ve oyuncak</h2>
<label for="parlaklik">Halka parlaklığı</label>
<select id="parlaklik"><option value="0">Kapalı</option><option value="25">Çok az</option>
<option value="60">Orta</option><option value="100">Tam</option></select>
<div class="sec"><label><input type="checkbox" id="nefes"> Boştayken sönük nefes ışığı</label>
<label><input type="checkbox" id="arka_goster"> Hikâye hazırlanırken dönen nokta</label></div>
<label>Oyuncak standdan alınınca</label>
<div class="sec"><label><input type="radio" name="cekilince" value="0"> Cümle bitince dursun</label>
<label><input type="radio" name="cekilince" value="1"> Hemen dursun</label>
<label><input type="radio" name="cekilince" value="2"> Hikâyeyi bitirsin</label></div>
<button id="kaydet">Kaydet</button><div class="ileti" id="kaydet_i"></div>
</section>
<section><h2>Oyuncak tanıt</h2>
<p class="not">Yeni bir figür tabanındaki etikete figürü yazar. Figürü seçin, "Etikete yaz"a basın, sonra ayar kartını
kaldırıp figürü standa koyun.</p>
<select id="figur"></select>
<button id="tanit">Etikete yaz</button><div class="ileti" id="tanit_i"></div>
<p class="not">Tanınan oyuncaklar (boşta hikâyeleri hazırlanır):</p><ul id="sahip"></ul>
</section>
<section><h2>Hikâyeleri sil</h2>
<p class="not">Hazırlanmış bütün hikâyeler silinir; oyuncak boştayken yenilerini yazar.</p>
<div class="sec"><label><input type="checkbox" id="unut"> Tanınan oyuncakları da unut</label></div>
<button class="tehlike" id="sil">Hikâyeleri sil</button><div class="ileti" id="sil_i"></div>
</section>
<button class="ikinci" id="bitir">Bitir ve Wi-Fi'yi kapat</button>
<p class="not">Ayar kartı standdan alınınca ya da 10 dakika sonra Wi-Fi kendiliğinden kapanır.</p>
</main><script>
var $=function(i){return document.getElementById(i)},ilk=true,izle=null;
function ileti(i,m,iyi){var e=$(i);e.textContent=m;e.className='ileti '+(iyi?'iyi':'kotu')}
function gonder(yol,veri,i,cb){var x=new XMLHttpRequest();x.open('POST',yol);
x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
x.onload=function(){var j={};try{j=JSON.parse(x.responseText)}catch(e){}
if(j.tamam){cb&&cb(j)}else ileti(i,j.hata||'Olmadı ('+x.status+')',false)};
x.onerror=function(){ileti(i,'Oyuncağa ulaşılamadı.',false)};x.send(veri)}
function sec(ad,d){var r=document.querySelectorAll('input[name='+ad+']');for(var i=0;i<r.length;i++)r[i].checked=r[i].value==d}
function secili(ad){var r=document.querySelector('input[name='+ad+']:checked');return r?r.value:''}
function durum(){var x=new XMLHttpRequest();x.open('GET','/durum');x.onload=function(){var j=JSON.parse(x.responseText),a=j.ayar;
if(ilk){ilk=false;$('ad').value=a.ad;$('ses_maks').value=a.ses_maks;$('ses_maks_d').textContent=a.ses_maks;sec('uyku_dk',a.uyku_dk);
sec('cekilince',a.cekilince);$('parlaklik').value=[0,25,60,100].indexOf(a.parlaklik)<0?60:a.parlaklik;$('nefes').checked=a.nefes;
$('arka_goster').checked=a.arka_goster;$('muzik').checked=a.muzik;var s=$('figur');s.innerHTML='';
j.figurler.forEach(function(f){var o=document.createElement('option');o.value=f.no;o.textContent=f.ad;s.appendChild(o)});
var o=document.createElement('option');o.value=j.ayar_karti;o.textContent='Ayar kartı (yedek)';s.appendChild(o)}
var u=$('sahip');u.innerHTML='';j.figurler.forEach(function(f){if(f.sahip){var l=document.createElement('li');
l.textContent=f.ad+(f.hazir>=0?' ('+f.hazir+' hazır hikâye)':f.gece?' (ninniler)':'');u.appendChild(l)}});
if(!u.children.length)u.innerHTML='<li>Henüz yok: oyuncak standa konunca tanınır.</li>';
$('kalan').textContent='Ayar modu açık: '+Math.ceil(j.kalan_sn/60)+' dakika kaldı.';
if(j.tanit.durum==1)ileti('tanit_i',j.tanit.mesaj,true);else if(j.tanit.durum==2){ileti('tanit_i',j.tanit.mesaj,j.tanit.tamam);
if(izle){clearInterval(izle);izle=null}}};x.onerror=function(){$('kalan').textContent='Oyuncağa ulaşılamadı (Wi-Fi kapanmış olabilir).'};x.send()}
$('ses_maks').oninput=function(){$('ses_maks_d').textContent=this.value};
$('kaydet').onclick=function(){var ad=$('ad').value.trim().replace(/\s+/g,' ');
if(!/^[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû ]{0,20}$/.test(ad)){ileti('kaydet_i','Adda yalnız harf ve boşluk olabilir (en çok 20).',false);return}
var v='ad='+encodeURIComponent(ad)+'&ses_maks='+$('ses_maks').value+'&uyku_dk='+secili('uyku_dk')+'&parlaklik='+$('parlaklik').value+
'&cekilince='+secili('cekilince')+'&nefes='+($('nefes').checked?1:0)+'&arka_goster='+($('arka_goster').checked?1:0)+'&muzik='+($('muzik').checked?1:0);
gonder('/kaydet',v,'kaydet_i',function(){ileti('kaydet_i','Kaydedildi.',true)})};
$('tanit').onclick=function(){gonder('/tanit','no='+$('figur').value,'tanit_i',function(){ileti('tanit_i','Ayar kartını kaldırın, figürü standa koyun...',true);
if(!izle)izle=setInterval(durum,1000)})};
$('sil').onclick=function(){if(!confirm('Hazır hikâyelerin hepsi silinsin mi?'))return;
gonder('/sil','onay=1&unut='+($('unut').checked?1:0),'sil_i',function(j){ileti('sil_i',j.silinen+' hikâye silindi.',true);durum()})};
$('bitir').onclick=function(){gonder('/bitir','','kaydet_i',function(){document.body.innerHTML='<main><h1>Bitti</h1><p>Ayarlar kaydedildi, Wi-Fi kapandı.</p></main>'})};
durum();setInterval(durum,15000);
</script></body></html>)rawliteral";
