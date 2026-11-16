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
  if(hv&&!matchMedia('(prefers-reduced-motion: reduce)').matches){hv.addEventListener('playing',function(){hero.classList.add('on')});var p=hv.play();if(p&&p.catch)p.catch(function(){})}
  var touch=matchMedia('(hover: none)').matches;
  [].slice.call(document.querySelectorAll('.hv')).forEach(function(el){var v=el.querySelector('video');if(!v)return;
    function on(){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){});el.classList.add('on')}
    function off(){v.pause();el.classList.remove('on')}
    if(touch){new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting&&e.intersectionRatio>.6?on():off()})},{threshold:[0,.6,1]}).observe(el)}
    else{el.addEventListener('mouseenter',on);el.addEventListener('mouseleave',off)}});
})();
</script>'''

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
   desc='Восхождение на Арарат, 5 137 м: 6 дней из Еревана через Грузию и Турцию, лагеря 3 200 и 4 200 м, без технической подготовки. От 81 000 ₽ / 356 000 ֏.',
   ogdesc='6 дней из Еревана: Догубаязит, лагеря 3 200 и 4 200 м, ночной штурм и вершина 5 137 м. Без технической подготовки.',
   apptitle='Арарат', fs={'ru':120,'en':120,'hy':92},
   msg={'ru':'Здравствуйте! Хочу на Арарат','en':'Hi! I would like to climb Mount Ararat','hy':'Բարև Ձեզ։ Ուզում եմ բարձրանալ Արարատ'},
   titles={'ru':'Восхождение на Арарат — White Irbis','en':'Mount Ararat ascent — White Irbis','hy':'Վերելք Արարատ — White Irbis'},
   card='ararat'),
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
    out = head + css2 + extra + '</style>\n' + edge(p['fs']) + '\n</head>\n<body>\n\n' + body + '\n' + SCRIPT % dict(msg=json.dumps(p['msg'], ensure_ascii=False), titles=json.dumps(p['titles'], ensure_ascii=False)) + '\n</body>\n</html>\n'
    os.makedirs(f'{R}/{slug}/img', exist_ok=True); os.makedirs(f'{R}/{slug}/vid', exist_ok=True)
    open(f'{R}/{slug}/index.html', 'w').write(out)
    shutil.copy(f'{R}/dolmatur/img/logo.png', f'{R}/{slug}/img/logo.png')
    print(slug, len(out))
