// Ayar sayfası (ayar modunda telefonda açılır; captive portal). Tek dosya, dışarıdan hiçbir şey yüklemez (internet
// yok). Kart: GET / (bu sayfa), GET /durum (JSON), POST /kaydet, /saat, /dinle, /surpriz, /alarm_dene, /alarm_ses
// (dosya), /alarm_ses_dinle, /alarm_ses_sil, /tanit, /sil, /bitir (hikaye_oyuncak.ino web_*).
// Alanların doğrulaması kartta (ayarlar.h); sayfadaki sınırlar yalnız kolaylık.
// Sayfa açılınca telefonun saati karta gönderilir (alarm ve yatma vakti için; kartta pil destekli saat yok).
// Alarm sesi: seçilen dosya telefonda çözülür (Web Audio), tek kanala ve 8 kHz'e indirilir, en çok 10 saniyesi alınır,
// tepe değeri düzlenir, IMA ADPCM'e çevrilir ve başlığıyla yüklenir (alarm_ses.h; kodlayıcı C'dekiyle bayt bayt aynı,
// tools/alarm_ses_test.py dener).
#pragma once

static const char AYAR_SAYFA[] = R"rawliteral(<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Masalcı Ayarları</title>
<style>
:root{--z:#f6f4ff;--k:#fff;--y:#1d1b2e;--s:#6b6880;--a:#5b4fd8;--h:#c62d3a;--t:#1f8a5b}
@media (prefers-color-scheme:dark){:root{--z:#14131c;--k:#1f1d2b;--y:#ecebf5;--s:#a4a1b8;--a:#9c93ff;--h:#ff7b86;--t:#5fd39a}}
*{box-sizing:border-box}body{margin:0;background:var(--z);color:var(--y);font:16px/1.45 system-ui,sans-serif}
main{max-width:520px;margin:0 auto;padding:16px}h1{font-size:1.4em;margin:.2em 0 .3em}
section{background:var(--k);border-radius:14px;padding:14px 16px;margin:0 0 14px;box-shadow:0 1px 3px #0002}
h2{font-size:1.05em;margin:0 0 .6em}label{display:block;margin:.7em 0 .25em;font-weight:600}
input[type=text],input[type=time],input[type=number],select,textarea{width:100%;font:inherit;padding:.55em;border-radius:9px;
border:1px solid var(--s);background:var(--z);color:var(--y)}textarea{min-height:4.2em;resize:vertical}
input[type=range]{width:100%}.sec label{display:flex;gap:.5em;font-weight:400;margin:.35em 0;align-items:center}
.gunler{display:flex;flex-wrap:wrap;gap:.3em}.gunler label{display:flex;gap:.25em;font-weight:400;margin:.2em .4em .2em 0}
button{font-size:1em;padding:.65em 1.1em;border:0;border-radius:10px;background:var(--a);color:#fff;margin:.8em .4em 0 0}
button.ikinci{background:transparent;color:var(--a);border:1px solid var(--a)}button.tehlike{background:var(--h)}
button.ikinci.tehlike{background:transparent;color:var(--h);border-color:var(--h)}
button:disabled{opacity:.5}.not{color:var(--s);font-size:.9em}.ileti{margin-top:.6em;min-height:1.3em}.iyi{color:var(--t)}
.kotu{color:var(--h)}ul{padding-left:1.2em;margin:.3em 0}.kapali{opacity:.55}
</style></head><body><main>
<h1>Masalcı Ayarları</h1>
<p class="not" id="kalan">Bağlanıyor...</p>
<p class="not" id="saat"></p>

<section><h2>Çocuk</h2>
<label for="ad">Çocuğun adı</label>
<input type="text" id="ad" maxlength="20" autocomplete="off" placeholder="ör. Emre (boş bırakılabilir)">
<p class="not">Selamlarken, alarmda ve mesajlarda adıyla seslenir. En çok 20 harf.</p>
<label for="okunus">Okunuşu (isteğe bağlı)</label>
<input type="text" id="okunus" maxlength="20" autocomplete="off" placeholder="ör. Jasmine için: Yasmin">
<p class="not">Ad yanlış okunuyorsa söylendiği gibi yazın.</p>
<button class="ikinci" id="dinle">Adı dinle</button>
<button id="kaydet1">Kaydet</button><div class="ileti" id="kaydet1_i"></div>
</section>

<section><h2>Alarm</h2>
<div class="sec"><label><input type="checkbox" id="alarm_acik"> Sabah alarmı açık</label></div>
<div id="alarm_alan">
<label for="alarm_saat">Saat</label><input type="time" id="alarm_saat">
<label>Günler</label><div class="gunler" id="gunler"></div>
<button class="ikinci" id="haftaici" type="button">Hafta içi</button><button class="ikinci" id="hergun" type="button">Her gün</button>
<label for="alarm_gunes">Gün doğumu ışığı</label>
<select id="alarm_gunes"><option value="0">Yok</option><option value="5">5 dakika önce</option><option value="10">10 dakika önce</option>
<option value="15">15 dakika önce</option><option value="20">20 dakika önce</option><option value="30">30 dakika önce</option></select>
<p class="not">Alarmdan önce halka koyu kırmızıdan sıcak beyaza yavaşça aydınlanır.</p>
<label>Ne çalsın?</label>
<div class="sec"><label><input type="radio" name="alarm_tur" value="0"> Eko'nun sesi: "Günaydın, kalkma vakti!"</label>
<label><input type="radio" name="alarm_tur" value="1"> Müzik kutusu ezgisi</label>
<label><input type="radio" name="alarm_tur" value="2"> Yüklediğim ses</label></div>
<label for="alarm_mesaj">Günaydından sonra söylenecek mesaj (isteğe bağlı)</label>
<textarea id="alarm_mesaj" maxlength="120" placeholder="ör. Bugün anneannene gidiyoruz!"></textarea>
<p class="not">Alarmı susturmak için: standa bir oyuncak koymak ya da kaldırmak, ya da "Merhaba Eko, dur". En çok 3 dakika çalar.</p>
<button id="kaydet2">Kaydet</button><button class="ikinci" id="alarm_dene">Alarmı dene</button>
<div class="ileti" id="kaydet2_i"></div>
</div></section>

<section><h2>Alarm sesi yükle</h2>
<p class="not" id="ses_durum">Yüklü ses yok: "Yüklediğim ses" seçilirse müzik kutusu çalar.</p>
<label for="ses_dosya">Ses dosyası (şarkı, kayıt...)</label>
<input type="file" id="ses_dosya" accept="audio/*">
<label for="ses_bas">Başlangıç (saniye)</label><input type="number" id="ses_bas" min="0" value="0" step="1">
<p class="not">Dosyanın bu saniyesinden başlayan en çok <span id="ses_sn">10</span> saniye alınır, telefonda küçültülür ve oyuncağa yüklenir.</p>
<button id="ses_yukle">Yükle</button><button class="ikinci" id="ses_dinle">Dinle</button><button class="ikinci tehlike" id="ses_sil">Sil</button>
<div class="ileti" id="ses_i"></div>
</section>

<section><h2>Yatma vakti</h2>
<label for="yatma_saat">Yatma vakti</label><input type="time" id="yatma_saat">
<div class="sec"><label><input type="checkbox" id="yatma_acik"> Bu saatte hatırlat ("Uyku vakti geldi...")</label>
<label><input type="checkbox" id="kilit"> Bu saatten sabaha kadar hikâye yerine yalnız ninni (Ay Dede)</label></div>
<div id="sabah_alan"><label for="sabah_saat">Sabah</label><input type="time" id="sabah_saat"></div>
<button id="kaydet3">Kaydet</button><div class="ileti" id="kaydet3_i"></div>
</section>

<section><h2>Sürpriz mesaj</h2>
<p class="not">Çocuğunuz oyuncağı bir dahaki sefere standa koyduğunda, selamdan sonra bir kez söylenir.</p>
<p class="not" id="surpriz_durum"></p>
<textarea id="surpriz" maxlength="120" placeholder="ör. Annen seni çok seviyor, akşam görüşürüz!"></textarea>
<button id="surpriz_kaydet">Mesajı bırak</button><button class="ikinci" id="surpriz_sil">Sil</button>
<div class="ileti" id="surpriz_i"></div>
</section>

<section><h2>Ses ve ninni</h2>
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
<p class="not">Wi-Fi 10 dakika sonra ya da telefon ayrılınca kendiliğinden kapanır.</p>
</main><script>
var $=function(i){return document.getElementById(i)},ilk=true,izle=null,GUN=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'],SN=10;
function ileti(i,m,iyi){var e=$(i);e.textContent=m;e.className='ileti '+(iyi?'iyi':'kotu')}
function gonder(yol,veri,i,cb){var x=new XMLHttpRequest();x.open('POST',yol);
if(!(veri instanceof FormData))x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
x.onload=function(){var j={};try{j=JSON.parse(x.responseText)}catch(e){}
if(j.tamam){cb&&cb(j)}else ileti(i,j.hata||'Olmadı ('+x.status+')',false)};
x.onerror=function(){ileti(i,'Oyuncağa ulaşılamadı.',false)};x.send(veri)}
function sec(ad,d){var r=document.querySelectorAll('input[name='+ad+']');for(var i=0;i<r.length;i++)r[i].checked=r[i].value==d}
function secili(ad){var r=document.querySelector('input[name='+ad+']:checked');return r?r.value:''}
function gunMaske(){var m=0;for(var i=0;i<7;i++)if($('g'+i).checked)m|=1<<i;return m}
function gunKoy(m){for(var i=0;i<7;i++)$('g'+i).checked=!!(m>>i&1)}
(function(){var g=$('gunler');for(var i=0;i<7;i++){var l=document.createElement('label');l.innerHTML='<input type="checkbox" id="g'+i+'"> '+GUN[i];g.appendChild(l)}})();
function gorunum(){$('alarm_alan').className=$('alarm_acik').checked?'':'kapali';$('sabah_alan').className=$('kilit').checked?'':'kapali'}
function durum(){var x=new XMLHttpRequest();x.open('GET','/durum');x.onload=function(){var j=JSON.parse(x.responseText),a=j.ayar;
if(ilk){ilk=false;$('ad').value=a.ad;$('okunus').value=a.okunus;$('ses_maks').value=a.ses_maks;$('ses_maks_d').textContent=a.ses_maks;
sec('uyku_dk',a.uyku_dk);sec('cekilince',a.cekilince);$('parlaklik').value=[0,25,60,100].indexOf(a.parlaklik)<0?60:a.parlaklik;
$('nefes').checked=a.nefes;$('arka_goster').checked=a.arka_goster;$('muzik').checked=a.muzik;
$('alarm_acik').checked=a.alarm_acik;$('alarm_saat').value=a.alarm_saat;gunKoy(a.alarm_gunler);$('alarm_gunes').value=a.alarm_gunes;
sec('alarm_tur',a.alarm_tur);$('alarm_mesaj').value=a.alarm_mesaj;$('yatma_acik').checked=a.yatma_acik;$('yatma_saat').value=a.yatma_saat;
$('kilit').checked=a.kilit;$('sabah_saat').value=a.sabah_saat;gorunum();SN=j.alarm_ses.en_cok_sn;$('ses_sn').textContent=SN;
var s=$('figur');s.innerHTML='';j.figurler.forEach(function(f){var o=document.createElement('option');o.value=f.no;o.textContent=f.ad;s.appendChild(o)});
var o=document.createElement('option');o.value=j.ayar_karti;o.textContent='Ayar kartı (yedek)';s.appendChild(o)}
var u=$('sahip');u.innerHTML='';j.figurler.forEach(function(f){if(f.sahip){var l=document.createElement('li');
l.textContent=f.ad+(f.hazir>=0?' ('+f.hazir+' hazır hikâye)':f.gece?' (ninniler)':'');u.appendChild(l)}});
if(!u.children.length)u.innerHTML='<li>Henüz yok: oyuncak standa konunca tanınır.</li>';
$('kalan').textContent='Ayar modu açık: '+Math.ceil(j.kalan_sn/60)+' dakika kaldı.';
$('saat').textContent=j.saat.gecerli?'Oyuncağın saati: '+GUN[j.saat.gun]+' '+j.saat.simdi+' (telefonunuzdan alındı)':'Oyuncağın saati ayarlanamadı: alarm ve yatma vakti çalışmaz.';
var as=j.alarm_ses;$('ses_durum').textContent=!as.bolum?'Bu yazılımda alarm sesi bölümü yok.':as.var?'Yüklü ses: '+as.ad+' ('+as.sn.toFixed(1).replace('.',',')+' sn)':'Yüklü ses yok: "Yüklediğim ses" seçilirse müzik kutusu çalar.';
$('ses_dinle').disabled=$('ses_sil').disabled=!as.var;
$('surpriz_durum').textContent=j.surpriz?'Bekleyen mesaj: "'+j.surpriz+'"':'Bekleyen mesaj yok.';
if(j.tanit.durum==1)ileti('tanit_i',j.tanit.mesaj,true);else if(j.tanit.durum==2){ileti('tanit_i',j.tanit.mesaj,j.tanit.tamam);
if(izle){clearInterval(izle);izle=null}}};x.onerror=function(){$('kalan').textContent='Oyuncağa ulaşılamadı (Wi-Fi kapanmış olabilir).'};x.send()}
function saatGonder(){var x=new XMLHttpRequest();x.open('POST','/saat');x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
x.onloadend=durum;x.send('t='+Math.floor(Date.now()/1000)+'&tz='+(-new Date().getTimezoneOffset()))}
$('ses_maks').oninput=function(){$('ses_maks_d').textContent=this.value};
$('alarm_acik').onchange=$('kilit').onchange=gorunum;
$('haftaici').onclick=function(){gunKoy(31)};$('hergun').onclick=function(){gunKoy(127)};
var HARF=/^[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû ]{0,20}$/;
function kaydet(i){var ad=$('ad').value.trim().replace(/\s+/g,' '),ok=$('okunus').value.trim().replace(/\s+/g,' ');
if(!HARF.test(ad)||!HARF.test(ok)){ileti(i,'Ad ve okunuşta yalnız harf ve boşluk olabilir (en çok 20).',false);return}
if($('alarm_acik').checked&&!gunMaske()){ileti(i,'Alarm için en az bir gün seçin.',false);return}
var e=encodeURIComponent,v='ad='+e(ad)+'&okunus='+e(ok)+'&ses_maks='+$('ses_maks').value+'&uyku_dk='+secili('uyku_dk')+
'&parlaklik='+$('parlaklik').value+'&cekilince='+secili('cekilince')+'&nefes='+($('nefes').checked?1:0)+'&arka_goster='+
($('arka_goster').checked?1:0)+'&muzik='+($('muzik').checked?1:0)+'&alarm_acik='+($('alarm_acik').checked?1:0)+'&alarm_saat='+
e($('alarm_saat').value||'07:00')+'&alarm_gunler='+gunMaske()+'&alarm_gunes='+$('alarm_gunes').value+'&alarm_tur='+(secili('alarm_tur')||0)+
'&alarm_mesaj='+e($('alarm_mesaj').value)+'&yatma_acik='+($('yatma_acik').checked?1:0)+'&yatma_saat='+e($('yatma_saat').value||'20:30')+
'&kilit='+($('kilit').checked?1:0)+'&sabah_saat='+e($('sabah_saat').value||'07:00');
gonder('/kaydet',v,i,function(){ileti(i,'Kaydedildi.',true);durum()})}
['kaydet','kaydet1','kaydet2','kaydet3'].forEach(function(b){$(b).onclick=function(){kaydet(b+'_i')}});
$('dinle').onclick=function(){kaydet('kaydet1_i');setTimeout(function(){gonder('/dinle','','kaydet1_i',function(){ileti('kaydet1_i','Oyuncak adı söylüyor...',true)})},400)};
$('alarm_dene').onclick=function(){gonder('/alarm_dene','','kaydet2_i',function(){ileti('kaydet2_i','Alarm çalıyor (kısa deneme)...',true)})};
$('surpriz_kaydet').onclick=function(){gonder('/surpriz','mesaj='+encodeURIComponent($('surpriz').value),'surpriz_i',function(){ileti('surpriz_i','Mesaj bırakıldı.',true);$('surpriz').value='';durum()})};
$('surpriz_sil').onclick=function(){gonder('/surpriz','mesaj=','surpriz_i',function(){ileti('surpriz_i','Mesaj silindi.',true);durum()})};
$('ses_dinle').onclick=function(){gonder('/alarm_ses_dinle','','ses_i',function(){ileti('ses_i','Oyuncak sesi çalıyor...',true)})};
$('ses_sil').onclick=function(){gonder('/alarm_ses_sil','','ses_i',function(){ileti('ses_i','Ses silindi.',true);durum()})};
// ---- alarm sesi: çöz, tek kanal, 8 kHz, en çok SN saniye, düzle, IMA ADPCM (alarm_ses.h ile aynı) ----
var ADIM=[7,8,9,10,11,12,13,14,16,17,19,21,23,25,28,31,34,37,41,45,50,55,60,66,73,80,88,97,107,118,130,143,157,173,190,209,230,253,
279,307,337,371,408,449,494,544,598,658,724,796,876,963,1060,1166,1282,1411,1552,1707,1878,2066,2272,2499,2749,3024,3327,3660,4026,
4428,4871,5358,5894,6484,7132,7845,8630,9493,10442,11487,12635,13899,15289,16818,18500,20350,22385,24623,27086,29794,32767],
INDEKS=[-1,-1,-1,-1,2,4,6,8,-1,-1,-1,-1,2,4,6,8];
function adpcm(x){var o=new Uint8Array((x.length+1)>>1),t=0,ix=0;for(var i=0;i<x.length;i++){var a=ADIM[ix],f=x[i]-t,n=0;
if(f<0){n=8;f=-f}if(f>=a){n|=4;f-=a}a>>=1;if(f>=a){n|=2;f-=a}a>>=1;if(f>=a)n|=1;a=ADIM[ix];var d=a>>3;if(n&4)d+=a;if(n&2)d+=a>>1;
if(n&1)d+=a>>2;t+=(n&8)?-d:d;if(t>32767)t=32767;if(t<-32768)t=-32768;ix+=INDEKS[n];if(ix<0)ix=0;if(ix>88)ix=88;
if(i&1)o[i>>1]|=n<<4;else o[i>>1]=n}return o}
function crc32(p){var c=~0;for(var i=0;i<p.length;i++){c^=p[i];for(var k=0;k<8;k++)c=(c>>>1)^(0xEDB88320&-(c&1))}return(~c)>>>0}
function sekizK(buf,bas,sn){var sr=buf.sampleRate,k=buf.numberOfChannels,L=buf.length,i0=Math.min(L,Math.floor(bas*sr)),
n=Math.max(0,Math.min(Math.floor((L-i0)/sr*8000),sn*8000)),y=new Float32Array(n),ch=[];for(var c=0;c<k;c++)ch.push(buf.getChannelData(c));
for(var j=0;j<n;j++){var a=i0+Math.floor((j-.5)*sr/8000),b=i0+Math.floor((j+.5)*sr/8000),s=0,m=0;if(a<i0)a=i0;if(b>L)b=L;if(b<=a)b=a+1;
for(var q=a;q<b&&q<L;q++)for(c=0;c<k;c++){s+=ch[c][q];m++}y[j]=m?s/m:0}return y}
function paketle(y,ad){var tepe=0,i;for(i=0;i<y.length;i++)tepe=Math.max(tepe,Math.abs(y[i]));var g=tepe>1e-4?29000/tepe:0,
x=new Int16Array(y.length),z=160;for(i=0;i<y.length;i++){var f=Math.min(1,i/z,(y.length-1-i)/z);x[i]=Math.round(y[i]*g*f)}
var v=adpcm(x),h=new Uint8Array(64),d=new DataView(h.buffer);d.setUint32(0,0x4C414B45,true);d.setUint16(4,1,true);d.setUint16(6,8000,true);
d.setUint32(8,x.length,true);d.setUint32(12,crc32(v),true);var u=new TextEncoder().encode(ad);var m=Math.min(u.length,47);
while(m>0&&(u[m]&0xC0)==0x80)m--;h.set(u.subarray(0,m),16);var p=new Uint8Array(64+v.length);p.set(h,0);p.set(v,64);return p}
$('ses_yukle').onclick=function(){var f=$('ses_dosya').files[0];if(!f){ileti('ses_i','Önce bir ses dosyası seçin.',false);return}
var AC=window.AudioContext||window.webkitAudioContext;if(!AC){ileti('ses_i','Bu tarayıcı sesi çözemiyor.',false);return}
ileti('ses_i','Ses hazırlanıyor...',true);$('ses_yukle').disabled=true;var r=new FileReader();r.onload=function(){var ac=new AC();
ac.decodeAudioData(r.result,function(buf){try{ac.close&&ac.close()}catch(e){}var y=sekizK(buf,Math.max(0,+$('ses_bas').value||0),SN);
if(y.length<800){ileti('ses_i','Seçilen yerden sonra ses yok (başlangıç saniyesine bakın).',false);$('ses_yukle').disabled=false;return}
var p=paketle(y,f.name.replace(/\.[^.]*$/,'')),fd=new FormData();fd.append('dosya',new Blob([p],{type:'application/octet-stream'}),'alarm.eko');
ileti('ses_i','Yükleniyor ('+Math.round(p.length/1024)+' KB)...',true);gonder('/alarm_ses',fd,'ses_i',function(j){$('ses_yukle').disabled=false;
ileti('ses_i','Yüklendi: '+j.sn.toFixed(1).replace('.',',')+' sn. Alarmda çalması için "Yüklediğim ses"i seçip kaydedin.',true);durum()});
setTimeout(function(){$('ses_yukle').disabled=false},8000)},function(){ileti('ses_i','Bu dosya çözülemedi; başka bir biçim deneyin (mp3, m4a, wav).',false);
$('ses_yukle').disabled=false})};r.readAsArrayBuffer(f)};
$('tanit').onclick=function(){gonder('/tanit','no='+$('figur').value,'tanit_i',function(){ileti('tanit_i','Ayar kartını kaldırın, figürü standa koyun...',true);
if(!izle)izle=setInterval(durum,1000)})};
$('sil').onclick=function(){if(!confirm('Hazır hikâyelerin hepsi silinsin mi?'))return;
gonder('/sil','onay=1&unut='+($('unut').checked?1:0),'sil_i',function(j){ileti('sil_i',j.silinen+' hikâye silindi.',true);durum()})};
$('bitir').onclick=function(){gonder('/bitir','','kaydet_i',function(){document.body.innerHTML='<main><h1>Bitti</h1><p>Ayarlar kaydedildi, Wi-Fi kapandı.</p></main>'})};
saatGonder();setInterval(durum,15000);
</script></body></html>)rawliteral";
