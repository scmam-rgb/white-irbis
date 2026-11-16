import re, os, shutil
R = '/home/claude/white-irbis'
H = os.path.dirname(os.path.abspath(__file__))
src = open(f'{R}/dolmatur/index.html').read()
lines = src.split('\n')
css = '\n'.join(lines[25:169])  # <style> ... gallery rules (lines 26-169)
contact = '\n'.join(lines[301:307])  # .msg + .reqs
assert contact.strip().startswith('<div class="msg">') and contact.strip().endswith('</dl>'), contact[:80]

extra = '''
.plan li{grid-template-columns:28px 1fr}
.plan b{opacity:.35}
.lead a,.next a{color:inherit;text-decoration-color:var(--eye);text-decoration-thickness:3px;text-underline-offset:4px}
.dgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:36px}
.dc{background:var(--card);border-radius:6px;padding:24px;display:flex;flex-direction:column;gap:10px}
.dc h3{font-size:24px;text-transform:uppercase}
.dc p{color:var(--muted)}
.dc .stats{margin-top:auto;padding-top:6px}
.dc .stats span{background:var(--paper)}
.dn{font-family:var(--display);font-size:48px;font-weight:700;line-height:.9;opacity:.18}
.dc.hi{background:var(--deep);color:var(--on-deep)}
.dc.hi p{color:var(--on-deep-muted)}.dc.hi .dn{color:var(--eye);opacity:1}
.dc.hi .stats span{background:var(--eye);color:var(--eye-ink)}
@media (max-width:900px){.dgrid{grid-template-columns:1fr 1fr}}
@media (max-width:600px){.dgrid{grid-template-columns:1fr}}
.media figure img,.next figure img{border-radius:6px}
.who4{grid-template-columns:repeat(4,1fr)}@media (max-width:960px){.who4{grid-template-columns:1fr 1fr}}@media (max-width:600px){.who4{grid-template-columns:1fr}}
.gsec{background:var(--card)}
.guides{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px}
.guide{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:22px;align-items:end}
.guide img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:6px}
.guide h3{font-size:30px;text-transform:uppercase}
.guide .role{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:6px}
.guide p{color:var(--muted);margin-top:10px}
@media (max-width:860px){.guides{grid-template-columns:1fr}}
.faq-list{margin-top:32px;border-top:1px solid var(--line);max-width:860px}
details{border-bottom:1px solid var(--line);padding:18px 0}
summary{cursor:pointer;font-family:var(--display);font-size:24px;text-transform:uppercase;list-style:none;display:flex;justify-content:space-between;gap:16px}
html[lang="hy"] summary{font-family:"Noto Sans Armenian",var(--display);font-stretch:75%;font-weight:700}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-family:var(--body);font-size:26px;line-height:1}
details[open] summary::after{content:"–"}
details p{margin-top:10px;color:var(--muted);max-width:62ch}
.dimg{display:block;margin:-24px -24px 6px;border-radius:6px 6px 0 0;overflow:hidden;position:relative}
.dimg img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
.gal-sec{background:var(--card)}
.gal3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:32px}
.gal3 figure{margin:0}.gal3 img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:6px;display:block}
@media (max-width:760px){.gal3{grid-template-columns:1fr}.gal3 img{aspect-ratio:4/3}}
.price .big{font-size:clamp(52px,7.4vw,100px)}.big>span[lang]{white-space:nowrap}
'''

def edge(fs):
    fz = ''.join(f'html[lang="{l}"] .hero h1{{font-size:min({"7vw" if l=="hy" else "9vw"},{v}px)}}' for l, v in fs.items())
    return ('<style id="hero-edge">@media (min-width:901px){.hero{--tl:calc(max(0px,(100vw - 1120px)/2) + 20px)}'
            '.hero-media{left:calc(var(--tl) + 640px)!important}.hero .wrap>*{max-width:600px}'
            f'.hero h1{{font-size:min(9vw,{fs["ru"]}px)}}{fz}}}</style>')

SCRIPT = '''<script>
(function(){
  var html=document.documentElement, btns=[].slice.call(document.querySelectorAll('.lang button'));
  var msg=%(msg)s, titles=%(titles)s;
  function set(l){html.lang=l;btns.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.l===l)});
    document.getElementById('wa').href='https://wa.me/37491470331?text='+encodeURIComponent(msg[l]);
    document.title=titles[l];
    try{localStorage.setItem('wi-lang',l)}catch(e){}}
  var q=(location.search.match(/lang=(ru|en|hy)/)||[])[1], s=null; try{s=localStorage.getItem('wi-lang')}catch(e){}
  set(q||(['ru','en','hy'].indexOf(s)>=0?s:'ru'));
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.l)})});
  var hero=document.querySelector('.hero'), hv=hero.querySelector('video');
  if(hv&&!matchMedia('(prefers-reduced-motion: reduce)').matches){hv.addEventListener('playing',function(){hero.classList.add('on')});hv.addEventListener('ended',function(){hero.classList.remove('on')});var p=hv.play();if(p&&p.catch)p.catch(function(){})}
  var touch=matchMedia('(hover: none)').matches;
  [].slice.call(document.querySelectorAll('.hv')).forEach(function(el){var v=el.querySelector('video');if(!v)return;
    function on(){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){});el.classList.add('on')}
    function off(){v.pause();el.classList.remove('on')}
    if(touch){new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting&&e.intersectionRatio>.6?on():off()})},{threshold:[0,.6,1]}).observe(el)}
    else{el.addEventListener('mouseenter',on);el.addEventListener('mouseleave',off)}});
})();
</script>'''

TCT_CSS = """
@media (max-width:900px){.hero h1{font-size:clamp(30px,9.4vw,80px)!important}html[lang="hy"] .hero h1{font-size:clamp(28px,8.2vw,62px)!important}}
.ab{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:56px;align-items:start}
@media (max-width:860px){.ab{grid-template-columns:1fr}}
.sh3{font-size:24px;text-transform:uppercase;margin-top:32px}
.sfbar{display:flex;height:46px;border-radius:6px;overflow:hidden;margin-top:14px}
.sf{display:flex;align-items:center;justify-content:center;font-family:var(--display);font-size:16px;min-width:0}
.sf0{background:var(--eye);color:var(--eye-ink)}.sf1{background:#121212;color:#F7F4EC}.sf2{background:#B5462F;color:#fff}.sf3{background:#B9B5A8;color:#121212}
.sfleg{list-style:none;padding:0;margin:12px 0 0;display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14px;color:var(--muted)}
.sfleg i{display:inline-block;width:12px;height:12px;border-radius:2px;margin-right:6px;vertical-align:-1px}
.schema{background:var(--deep);color:var(--on-deep);border-radius:6px;padding:26px 28px}
.sch-cap{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--on-deep-muted)}
.schema ol{list-style:none;margin:14px 0;padding:0 0 0 26px;position:relative}
.schema ol::before{content:"";position:absolute;left:8px;top:8px;bottom:8px;border-left:3px dashed var(--eye)}
.sp{position:relative;padding:6px 0;font-family:var(--display);font-size:20px;text-transform:uppercase;letter-spacing:.03em}
.sp::before{content:"";position:absolute;left:-23px;top:13px;width:10px;height:10px;border-radius:50%;background:var(--on-deep);box-shadow:0 0 0 3px var(--deep)}
.sp.end::before{background:var(--eye);width:14px;height:14px;left:-25px;top:11px}
.sp.end{color:var(--eye)}
html[lang="hy"] .sp{font-family:"Noto Sans Armenian",var(--display);font-stretch:75%;font-weight:700}
.sec-rg{background:var(--card)}
.rgs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:34px}
@media (max-width:760px){.rgs{grid-template-columns:1fr}}
.rg{background:var(--paper);border-radius:6px;overflow:hidden;display:flex;flex-direction:column}
.rg-img img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.rg-none{height:64px;background:var(--deep);display:flex;align-items:flex-end;padding:18px 22px;background-image:radial-gradient(circle at 80% 20%,#2a2a26 0,#121212 70%)}
.rg-none span{font-family:var(--display);font-size:44px;font-weight:700;line-height:.8;color:var(--eye)}
.rg-b{padding:22px 24px 26px;display:flex;flex-direction:column;gap:10px}
.rg-h{display:flex;align-items:baseline;gap:12px}.rg-h b{font-family:var(--display);color:var(--muted);font-size:18px}
.rg-h h3{font-size:28px;text-transform:uppercase}
.rg p{color:var(--muted)}
.rg-hi i{display:block;font-style:normal;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);font-weight:600;margin-bottom:2px}
.rg-note{border-left:4px solid var(--eye);padding-left:12px;color:var(--ink)!important;font-size:15px}
.rg .stats{margin-top:0}
.rg-none + .rg-b .rg-h b{display:none}
.prac{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px 44px;margin-top:36px}
@media (max-width:760px){.prac{grid-template-columns:1fr}}
.prac h3{font-size:22px;text-transform:uppercase;color:var(--eye);margin-bottom:8px}
.prac p{color:var(--on-deep-muted)}
.bey{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:44px;margin-top:32px}
@media (max-width:860px){.bey{grid-template-columns:1fr}}
.bey h3{font-size:30px;text-transform:uppercase;margin-bottom:10px}
.bey h4{font-family:var(--display);font-size:20px;text-transform:uppercase;margin:22px 0 10px}
html[lang="hy"] .bey h4{font-family:"Noto Sans Armenian",var(--display);font-stretch:75%}
.bey p{color:var(--muted);margin-top:10px}
.tb{width:100%;border-collapse:collapse;font-size:15px}
.tb th{text-align:left;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);padding:6px 8px 6px 0}
.tb td{border-bottom:1px solid var(--line);padding:8px 8px 8px 0}
.tb td+td,.tb th+th{text-align:right;white-space:nowrap}
.price .big>span[lang]{white-space:normal}
"""

GORY_CSS = """
.ld{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:56px;align-items:center}
@media (max-width:860px){.ld{grid-template-columns:1fr;gap:28px}}
.ladder{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.ladder a{display:grid;grid-template-columns:150px 1fr 64px;gap:12px;align-items:center;text-decoration:none}
.ladder .ln{font-family:var(--display);font-size:17px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
html[lang="hy"] .ladder .ln{font-family:"Noto Sans Armenian",var(--display);font-stretch:75%;font-weight:700}
.ladder .lb{height:14px;background:var(--card);border-radius:3px;overflow:hidden}
.ladder .lb i{display:block;height:100%;background:var(--ink);border-radius:3px}
.ladder li:first-child .lb i{background:var(--eye)}
.ladder .la{font-family:var(--display);font-size:16px;text-align:right;color:var(--muted)}
.ladder a:hover .lb i{background:var(--eye)}
@media (max-width:520px){.ladder a{grid-template-columns:110px 1fr 56px}}
.sec-pk{background:var(--card)}
.pks{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:34px}
@media (max-width:760px){.pks{grid-template-columns:1fr}}
.pk{background:var(--paper);border-radius:6px;overflow:hidden;display:flex;flex-direction:column;scroll-margin-top:20px}
.pk-img{position:relative}.pk-img img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.pk-img b,.pk-alt b{font-family:var(--display);font-weight:700;color:var(--eye);line-height:.9}
.pk-img b{position:absolute;left:20px;bottom:16px;font-size:52px;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.pk-alt{background:var(--deep);padding:22px 24px 18px;background-image:radial-gradient(circle at 85% 0,#2c2b27 0,#121212 65%)}
.pk-alt b{font-size:52px}
.pk-b{padding:20px 24px 24px;display:flex;flex-direction:column;gap:10px}
.pk-b h3{font-size:30px;text-transform:uppercase}
.pk p{color:var(--muted)}
.pk .stats{margin-top:0}.pk .stats span{background:var(--card)}
.pk .stats .lv span{background:none!important;padding:0;border-radius:0;color:inherit}
.pk .four{flex-wrap:wrap}.pk .four span{background:var(--deep)!important;color:var(--on-deep)}.pk .four span span{background:none!important;padding:0;color:inherit}.pk .four b{color:var(--eye);font-family:var(--display);font-weight:600;margin-left:4px}
.pk .lv-e{background:#DDEBC8!important}.pk .lv-m{background:var(--eye)!important}.pk .lv-h{background:#121212!important;color:#F7F4EC}.pk .lv-x{background:#B5462F!important;color:#fff}
.pk-r i{display:block;font-style:normal;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);font-weight:600;margin-bottom:2px}
.pk-link a{color:var(--ink);font-weight:600;text-decoration-color:var(--eye);text-decoration-thickness:3px;text-underline-offset:4px}
.prac{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px 44px;margin-top:36px}
@media (max-width:760px){.prac{grid-template-columns:1fr}}
.prac h3{font-size:22px;text-transform:uppercase;color:var(--eye);margin-bottom:8px}
.prac p{color:var(--on-deep-muted)}
.price .big>span[lang]{white-space:normal}
"""

PAGES = {
 'aragats': dict(
   title='Арагац, Северная вершина — White Irbis',
   desc='Восхождение на Северную вершину Арагаца, 4 090 м — высшую точку Армении. 1 день из Еревана, июнь — октябрь. 60 000 ֏ / 13 700 ₽.',
   ogdesc='Высшая точка Армении за один день из Еревана: озеро Кари, кратер и гребень к вершине 4 090 м.',
   apptitle='Арагац', fs={'ru':120,'en':112,'hy':70},
   msg={'ru':'Здравствуйте! Хочу на Северную вершину Арагаца','en':'Hi! I would like to climb the North peak of Aragats','hy':'Բարև Ձեզ։ Ուզում եմ բարձրանալ Արագածի Հյուսիսային գագաթ'},
   titles={'ru':'Арагац, Северная вершина — White Irbis','en':'Aragats, North peak — White Irbis','hy':'Արագած, Հյուսիսային գագաթ — White Irbis'},
   card='aragats'),
 'ararat': dict(
   title='Восхождение на Арарат — White Irbis',
   desc='Восхождение на Арарат, 5 137 м: 6 дней из Еревана через Грузию и Турцию, лагеря 3 200 и 4 200 м, без технической подготовки. От 96 600 ₽ / 424 000 ֏ / €1 050.',
   ogdesc='6 дней из Еревана: Догубаязит, лагеря 3 200 и 4 200 м, ночной штурм и вершина 5 137 м. Без технической подготовки.',
   apptitle='Арарат', fs={'ru':120,'en':120,'hy':92},
   msg={'ru':'Здравствуйте! Хочу на Арарат','en':'Hi! I would like to climb Mount Ararat','hy':'Բարև Ձեզ։ Ուզում եմ բարձրանալ Արարատ'},
   titles={'ru':'Восхождение на Арарат — White Irbis','en':'Mount Ararat ascent — White Irbis','hy':'Վերելք Արարատ — White Irbis'},
   card='ararat'),
 'tct': dict(
   title='Транскавказская тропа — гайдбук White Irbis',
   desc='Гайдбук по Транскавказской тропе: 819 км через Армению от озера Арпи до Мегри — 7 регионов, сезоны, навигация, ночёвки, вода, разрешения.',
   ogdesc='819 км через всю Армению: участки, сезоны, навигация, ночёвки и вода.',
   apptitle='TCT', fs={'ru':68,'en':74,'hy':56},
   msg={'ru':'Здравствуйте! Планирую Транскавказскую тропу, хочу посоветоваться','en':'Hi! I am planning the Transcaucasian Trail and would like some advice','hy':'Բարև Ձեզ։ Պլանավորում եմ Անդրկովկասյան արահետը, ուզում եմ խորհրդակցել'},
   titles={'ru':'Транскавказская тропа — гайдбук White Irbis','en':'Transcaucasian Trail — White Irbis guidebook','hy':'Անդրկովկասյան արահետ — White Irbis ուղեցույց'},
   card='tct', css=TCT_CSS),
 'gory': dict(
   title='Горы Армении — гайдбук White Irbis',
   desc='Гайдбук по горам Армении: Арагац, Аждаак, Капутджух, Хуступ, Ухтасар, Тегенис, Артаваз, Ара, Атис, Лалвар, Артаниш, Димац — высота, старт, сложность, сезон.',
   ogdesc='12 вершин Армении: высота, старт, сложность и сезон. От «спящего великана» Ара до 4 090 м Арагаца.',
   apptitle='Горы Армении', fs={'ru':120,'en':110,'hy':84},
   msg={'ru':'Здравствуйте! Хочу подняться на гору в Армении, подскажите','en':'Hi! I would like to climb a mountain in Armenia — can you advise?','hy':'Բարև Ձեզ։ Ուզում եմ բարձրանալ Հայաստանի լեռներից մեկը, խորհուրդ կտա՞ք'},
   titles={'ru':'Горы Армении — гайдбук White Irbis','en':'Mountains of Armenia — White Irbis guidebook','hy':'Հայաստանի լեռները — White Irbis ուղեցույց'},
   card='gory', css=GORY_CSS),
}
import json
for slug, p in PAGES.items():
    body = open(f'{H}/{slug}_body.html').read().replace('%%CONTACT%%', contact.strip())
    head = f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{p['title']}</title>
<meta property="og:type" content="website">
<meta property="og:site_name" content="White Irbis">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['ogdesc']}">
<meta property="og:url" content="https://scmam-rgb.github.io/white-irbis/{slug}/">
<meta property="og:image" content="https://scmam-rgb.github.io/white-irbis/img/cards/{p['card']}-ru.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../dolmatur/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="../dolmatur/img/favicon-32.png">
<link rel="apple-touch-icon" href="../dolmatur/img/apple-touch-icon.png">
<meta name="apple-mobile-web-app-title" content="{p['apptitle']}">
<meta name="theme-color" content="#121212">
<meta name="description" content="{p['desc']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Rubik:wght@400;500;600&family=Noto+Sans+Armenian:wdth,wght@62.5..100,400..700&display=swap">
'''
    css2 = css.replace('/* dolmatur additions */', '/* page additions */').rstrip()
    assert css2.startswith('<style>')
    out = head + css2 + extra + p.get('css','') + '</style>\n' + edge(p['fs']) + '\n</head>\n<body>\n\n' + body + '\n' + SCRIPT % dict(msg=json.dumps(p['msg'], ensure_ascii=False), titles=json.dumps(p['titles'], ensure_ascii=False)) + '\n</body>\n</html>\n'
    os.makedirs(f'{R}/{slug}/img', exist_ok=True)
    open(f'{R}/{slug}/index.html', 'w').write(out)
    shutil.copy(f'{R}/dolmatur/img/logo.png', f'{R}/{slug}/img/logo.png')
    print(slug, len(out))
