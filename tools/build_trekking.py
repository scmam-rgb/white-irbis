# Builds trekking/index.html — 7-day trekking tour by White Irbis (program by Antoine Ananyan)
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
base_css = (ROOT / "skaly-i-vulkan/index.html").read_text(encoding="utf-8")
base_css = re.search(r"<style>(.*?)</style>", base_css, re.S).group(1)

def _nb(x):
    return re.sub(r'(?<=\d) (?=\d{3}(?!\d))', '\u00a0', x)

def t(ru, en, hy):
    ru, en, hy = _nb(ru), _nb(en), _nb(hy)
    return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'

def ts(ru, en, hy):  # svg
    return f'<tspan lang="ru">{ru}</tspan><tspan lang="en">{en}</tspan><tspan lang="hy">{hy}</tspan>'

PHONE = "37491470331"
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2a9.8 9.8 0 0 0-8.4 14.8L2.3 21.7l4.8-1.3A9.8 9.8 0 1 0 12 2.2Zm0 1.9a7.9 7.9 0 1 1-4.1 14.6l-.3-.2-2.8.8.8-2.7-.2-.3A7.9 7.9 0 0 1 12 4.1Zm-3 3.9c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.6s1.1 3 1.3 3.2c.2.2 2.2 3.4 5.3 4.6 2.6 1 3.1.8 3.7.8.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.4l-2-1c-.3-.1-.5-.1-.7.2l-.9 1.1c-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.4.1-.6l.5-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5H9Z"/></svg>'
TG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M21.6 3.4 2.9 10.6c-1.2.5-1.2 1.2-.2 1.5l4.8 1.5 1.8 5.6c.2.6.4.8.8.8.4 0 .6-.2.9-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.3-.5-1.9-1.3-1.4ZM8.3 13.2l9.9-6.2c.5-.3.9-.1.5.2l-8.2 7.4-.3 3.4-1.9-4.8Z"/></svg>'

def credit(author, lic):
    return f'<figcaption class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}{author}, {lic}, Wikimedia Commons</figcaption>'

# ---------- days with trails (data from Antoine's programme) ----------
# stats: (up, down, low, high, time, km)
DAYS = [
 dict(n="02", img="symphony.jpg", alt="Базальтовые столбы «Симфония камней» в ущелье реки Азат",
      cr=("ՎԱՍ","CC BY-SA 4.0"), route="route-garni.png",
      h=t("Гарни, Симфония камней, Авуц Тар","Garni, Symphony of Stones, Havuts Tar","Գառնի, Քարերի սիմֆոնիա, Հավուց թառ"),
      p=t("Языческий храм Солнца Гарни (I век). Спускаемся пешком в ущелье реки Азат к базальтовым столбам «Симфония камней», поднимаемся к руинам монастыря Авуц Тар и возвращаемся в Гарни. Обед или ланч-боксы, затем монастырь Гегард (IV–XIII века) и Ереван.",
          "The pagan Temple of the Sun at Garni (1st century). We walk down into the Azat gorge to the basalt columns of the Symphony of Stones, climb to the ruins of Havuts Tar monastery and loop back to Garni. Lunch or lunch boxes, then Geghard monastery (4th–13th centuries) and back to Yerevan.",
          "Գառնիի հեթանոսական Արևի տաճարը (I դար)։ Ոտքով իջնում ենք Ազատ գետի կիրճ՝ «Քարերի սիմֆոնիա» բազալտե սյուներին, բարձրանում Հավուց թառ վանքի ավերակներին և վերադառնում Գառնի։ Ճաշ կամ ճաշատուփեր, ապա Գեղարդ վանք (IV–XIII դդ.) և Երևան։"),
      st=("628","630","1 227","1 619",t("3–4 ч","3–4 h","3–4 ժ"),"12"),
      se=t("Гарни → Азат → Авуц Тар → Гарни","Garni → Azat → Havuts Tar → Garni","Գառնի → Ազատ → Հավուց թառ → Գառնի"),
      tags=[t("Храм Гарни","Garni Temple","Գառնիի տաճար"),t("Симфония камней","Symphony of Stones","Քարերի սիմֆոնիա"),t("Гегард","Geghard","Գեղարդ")]),
 dict(n="03", img="tsakhkunyats.jpg", alt="Горное озеро со скалой на Цахкуняцком хребте",
      cr=("Emma YSU","CC BY-SA 4.0"), route="route-tsakhkunyats.png",
      h=t("Цахкуняцкий хребет и озеро","The Tsaghkunyats ridge and lake","Ծաղկունյաց լեռնաշղթա և լիճ"),
      p=t("Трансфер в Агверан. Кольцо по Цахкуняцкому хребту с подъёмом к озеру Цахкуняц (Нэнэ) — оттуда видно многие хребты Армении. Ланч-боксы на маршруте, спуск, вечером Ереван.",
          "Transfer to Aghveran. A loop along the Tsaghkunyats ridge up to Lake Tsaghkunyats (Nene), with views over many of Armenia's ranges. Lunch boxes on the trail, the descent, and Yerevan in the evening.",
          "Տեղափոխում Աղվերան։ Օղակաձև երթուղի Ծաղկունյաց լեռնաշղթայով դեպի Ծաղկունյաց (Նենե) լիճ, որտեղից երևում են Հայաստանի շատ լեռնաշղթաներ։ Ճաշատուփեր երթուղում, վայրէջք, երեկոյան՝ Երևան։"),
      st=("683","683","1 960","2 543",t("3–4 ч","3–4 h","3–4 ժ"),"9,3"),
      se=t("Агверан → озеро Цахкуняц → Агверан","Aghveran → Lake Tsaghkunyats → Aghveran","Աղվերան → Ծաղկունյաց լիճ → Աղվերան"),
      tags=[t("Агверан","Aghveran","Աղվերան"),t("Высокогорное озеро","Alpine lake","Բարձրլեռնային լիճ"),t("Кольцо","Loop","Օղակ")]),
 dict(n="04", img="parz.jpg", alt="Озеро Парз в лесу национального парка Дилижан",
      cr=("Dav Sargsyan","CC BY-SA 4.0"), route="route-parz-gosh.png",
      h=t("Дилижан: от Парз Лич до Гоша","Dilijan: Parz Lich to Gosh","Դիլիջան՝ Պարզ լճից Գոշ"),
      p=t("Национальный парк Дилижан, около 1 400 м над морем. От лесного озера Парз Лич идём пешком через лес и поляны к деревне Гош и монастырю Гошаванк (XII–XIII века). Ланч-боксы, вечером Ереван.",
          "Dilijan National Park, at around 1,400 m. From the forest lake Parz Lich we walk through woods and meadows to the village of Gosh and Goshavank monastery (12th–13th centuries). Lunch boxes, Yerevan in the evening.",
          "Դիլիջանի ազգային պարկ, ծովի մակերևույթից մոտ 1 400 մ։ Անտառային Պարզ լճից ոտքով անցնում ենք անտառով և բացատներով մինչև Գոշ գյուղ և Գոշավանք (XII–XIII դդ.)։ Ճաշատուփեր, երեկոյան՝ Երևան։"),
      st=("343","452","1 233","1 561",t("2,5–3 ч","2.5–3 h","2,5–3 ժ"),"8"),
      se=t("Парз Лич → Гош","Parz Lich → Gosh","Պարզ լիճ → Գոշ"),
      tags=[t("Национальный парк","National park","Ազգային պարկ"),t("Лес","Forest","Անտառ"),t("Гошаванк","Goshavank","Գոշավանք")]),
 dict(n="05", img="sevanavank.jpg", alt="Монастырь Севанаванк над синим озером Севан",
      cr=("Anastasiya Lvova","CC BY-SA 4.0"), route="route-artanish.png",
      h=t("Севан и гора Артаниш","Sevan and Mount Artanish","Սևան և Արտանիշ լեռ"),
      p=t("Монастырь Севанаванк на полуострове. Восхождение на гору Артаниш (2 461 м): с вершины видно всё зеркало Севана и пролив между Норатусским и Артанишским мысами. Ланч-боксы, спуск к берегу, отдых и купание по желанию, вечером Ереван.",
          "Sevanavank monastery on its peninsula. Ascent of Mount Artanish (2,461 m): from the top you see the whole of Lake Sevan and the strait between the Noratus and Artanish capes. Lunch boxes, down to the shore, rest and an optional swim, Yerevan in the evening.",
          "Սևանավանքը թերակղզում։ Վերելք Արտանիշ լեռ (2 461 մ)․ գագաթից երևում է Սևանի ամբողջ հայելին և Նորատուսի ու Արտանիշի հրվանդանների միջև նեղուցը։ Ճաշատուփեր, իջնում ենք ափ, հանգիստ և լողանք ըստ ցանկության, երեկոյան՝ Երևան։"),
      st=("536","536","1 925","2 461",t("2,5–3 ч","2.5–3 h","2,5–3 ժ"),"5,5"),
      se=t("Берег Севана → вершина Артаниш → берег","Sevan shore → Artanish summit → shore","Սևանի ափ → Արտանիշի գագաթ → ափ"),
      tags=[t("Севанаванк","Sevanavank","Սևանավանք"),t("Вершина 2 461 м","Summit 2,461 m","Գագաթ 2 461 մ"),t("Купание","Swim","Լողանք")]),
 dict(n="06", img="smbataberd.jpg", alt="Стены крепости Смбатаберд на гребне над ущельем",
      cr=("Well-read MountainMan","CC BY-SA 4.0"), route="route-smbataberd.png",
      h=t("Хор Вирап, Смбатаберд, Нораванк","Khor Virap, Smbataberd, Noravank","Խոր Վիրապ, Սմբատաբերդ, Նորավանք"),
      p=t("Монастырь Хор Вирап под Араратом. Из деревни Ехегис поднимаемся к крепости Смбатаберд (основана в V веке, расцвет — IX–X века) и спускаемся к машине. Ланч-боксы, затем Нораванк — монастырь XIII века среди красных скал ущелья Арпы, раскопки Арени-1 и карстовая пещера Магеллан. Вечером Ереван.",
          "Khor Virap monastery beneath Ararat. From the village of Yeghegis we climb to Smbataberd fortress (founded in the 5th century, at its height in the 9th–10th) and walk back down to the car. Lunch boxes, then Noravank, a 13th-century monastery among the red cliffs of the Arpa gorge, the Areni-1 excavations and the Magellan karst cave. Yerevan in the evening.",
          "Խոր Վիրապ վանքը Արարատի ստորոտին։ Եղեգիս գյուղից բարձրանում ենք Սմբատաբերդ ամրոց (հիմնադրվել է V դարում, ծաղկման շրջանը՝ IX–X դդ.) և իջնում մեքենայի մոտ։ Ճաշատուփեր, ապա Նորավանք՝ XIII դարի վանք Արփայի կիրճի կարմիր ժայռերի մեջ, Արենի-1-ի պեղումները և Մագելան կարստային քարանձավը։ Երեկոյան՝ Երևան։"),
      st=("393","486","1 552","1 913",t("3–5 ч","3–5 h","3–5 ժ"),"7"),
      se=t("Ехегис → Смбатаберд → к машине","Yeghegis → Smbataberd → back to the car","Եղեգիս → Սմբատաբերդ → մեքենայի մոտ"),
      tags=[t("Хор Вирап","Khor Virap","Խոր Վիրապ"),t("Крепость V века","5th-century fortress","V դարի ամրոց"),t("Нораванк","Noravank","Նորավանք"),t("Арени-1","Areni-1","Արենի-1")]),
]

def stats(st):
    up, dn, lo, hi, tm, km = st
    return ('<dl class="st">'
        f'<div><dt>{t("Набор","Gain","Բարձրացում")}</dt><dd>↑ {up} {t("м","m","մ")}</dd></div>'
        f'<div><dt>{t("Спуск","Loss","Իջնում")}</dt><dd>↓ {dn} {t("м","m","մ")}</dd></div>'
        f'<div><dt>{t("Высоты","Altitude","Բարձրություն")}</dt><dd>{lo}–{hi} {t("м","m","մ")}</dd></div>'
        f'<div><dt>{t("Длина","Distance","Երկարություն")}</dt><dd>{km} {t("км","km","կմ")}</dd></div>'
        f'<div><dt>{t("Время","Time","Ժամանակ")}</dt><dd>{tm}</dd></div>'
        '</dl>')

def day_html(d):
    tags = "".join(f'<span class="tag">{x}</span>' for x in d["tags"])
    return f'''<li class="day">
  <figure><img src="img/{d["img"]}" alt="{d["alt"]}" loading="lazy">{credit(*d["cr"])}</figure>
  <div><div class="num">{d["n"]}</div><h3>{d["h"]}</h3><p>{d["p"]}</p><div class="tags">{tags}</div></div>
  <div class="trk">
    <div class="trk-map"><span class="trk-l">{t("Маршрут дня","Today's trail","Օրվա երթուղին")}</span><img src="img/{d["route"]}" alt="" loading="lazy"><span class="trk-se">{d["se"]}</span></div>
    {stats(d["st"])}
  </div>
</li>'''

days_html = "\n".join(day_html(d) for d in DAYS)

# ---------- overview map ----------
pts = [  # x,y from lat/lon projection; label, label offset, day
 (178,295,ts("Ереван","Yerevan","Երևան"),"big"),
 (79,173,ts("Арагац · оз. Кари","Aragats · Lake Kari","Արագած · Քարի լիճ"),"7"),
 (93,212,ts("Амберд","Amberd","Ամբերդ"),"s"),
 (202,164,ts("Агверан","Aghveran","Աղվերան"),"3"),
 (244,322,ts("Гарни","Garni","Գառնի"),"2"),
 (319,72,ts("Парз Лич · Гош","Parz Lich · Gosh","Պարզ լիճ · Գոշ"),"4"),
 (329,143,ts("Севанаванк","Sevanavank","Սևանավանք"),"s"),
 (418,186,ts("Артаниш","Artanish","Արտանիշ"),"5"),
 (198,414,ts("Хор Вирап","Khor Virap","Խոր Վիրապ"),"s"),
 (436,416,ts("Смбатаберд","Smbataberd","Սմբատաբերդ"),"6"),
 (395,491,ts("Нораванк","Noravank","Նորավանք"),"s"),
]
lab_pos = {"Ереван":(-14,30,"end"),"Арагац":(0,-22,"middle"),"Амберд":(14,18,"start"),"Агверан":(16,-8,"start"),
           "Гарни":(14,16,"start"),"Парз":(-14,-6,"end"),"Севанаванк":(12,-8,"start"),"Артаниш":(-12,-14,"end"),
           "Хор":(14,18,"start"),"Смбатаберд":(-14,-12,"end"),"Нораванк":(-14,6,"end")}
svg = ['<svg viewBox="0 0 520 540" role="img" aria-label="Схема: все выезды из Еревана — Гарни, Агверан, Дилижан, Севан, Вайоц Дзор, Арагац">',
       '<text x="20" y="32" font-family="Oswald, Arial, sans-serif" font-size="15" letter-spacing="2" fill="#FAEB0F">' + ts("ШЕСТЬ ВЫЕЗДОВ ИЗ ЕРЕВАНА","SIX DAY TRIPS FROM YEREVAN","ՎԵՑ ԵԼՔ ԵՐԵՎԱՆԻՑ") + '</text>',
       # schematic lake Sevan
       '<path d="M318 120 C338 112 352 128 352 150 C356 172 382 178 410 172 C440 168 458 186 452 210 C446 236 414 244 388 236 C360 228 342 212 330 192 C318 172 306 140 318 120Z" fill="#1E2A30" stroke="#33454F" stroke-width="1.2"/>',
       '<text x="404" y="230" font-family="Rubik, Arial, sans-serif" font-size="13" fill="#7FA3B5" text-anchor="middle">' + ts("оз. Севан","Lake Sevan","Սևանա լիճ") + '</text>',
       '<g fill="none" stroke="#2C2B27" stroke-width="1.2"><ellipse cx="79" cy="173" rx="46" ry="34"/><ellipse cx="79" cy="173" rx="78" ry="60"/></g>',
       '<g stroke="#FAEB0F" stroke-width="1.6" stroke-dasharray="5 6" fill="none" opacity=".75">']
for x,y,_,k in pts[1:]:
    if k != "s":
        svg.append(f'<path d="M178 295 L{x} {y}"/>')
svg.append('</g><g font-family="Rubik, Arial, sans-serif">')
for x,y,lab,k in pts:
    ru = re.search(r'lang="ru">([^< ]+)', lab).group(1)
    dx,dy,anc = lab_pos[ru]
    if k == "big":
        svg.append(f'<circle cx="{x}" cy="{y}" r="12" fill="#FAEB0F" stroke="#121212" stroke-width="3"/><text x="{x+dx}" y="{y+dy}" fill="#F7F4EC" font-size="20" font-weight="600" text-anchor="{anc}">{lab}</text>')
    elif k == "s":
        svg.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#A8A497"/><text x="{x+dx}" y="{y+dy}" fill="#A8A497" font-size="13" text-anchor="{anc}">{lab}</text>')
    else:
        svg.append(f'<circle cx="{x}" cy="{y}" r="13" fill="#FAEB0F" stroke="#121212" stroke-width="2"/><text x="{x}" y="{y+5}" fill="#121212" font-family="Oswald, Arial, sans-serif" font-size="15" font-weight="600" text-anchor="middle">{k}</text>'
                   f'<text x="{x+dx+(4 if anc=="start" else (-4 if anc=="end" else 0))}" y="{y+dy}" fill="#F7F4EC" font-size="15" font-weight="600" text-anchor="{anc}">{lab}</text>')
svg.append('</g><image href="img/logo.png" x="20" y="476" width="44" height="44"/><text x="72" y="503" font-family="Oswald, Arial, sans-serif" font-size="14" letter-spacing="2" fill="#A8A497">WHITE IRBIS</text></svg>')
overview = "\n".join(svg)

CSS_EXTRA = r"""
@media (max-width:360px){.lang{margin-left:8px}.lang button{padding:6px 7px}.brand img{width:70px;height:70px}summary{overflow-wrap:anywhere}}

@media (max-width:640px){html[lang="hy"] .h2{font-size:clamp(26px,7.6vw,40px)}.h2{overflow-wrap:break-word}}

@media (max-width:1180px){.top nav{display:none}}
.price-chip small{display:block;margin:6px 0 0;font-size:14px}
.hero-photos::after{background:linear-gradient(90deg,var(--deep) 0%,rgba(18,18,18,.6) 14%,rgba(18,18,18,0) 40%),linear-gradient(180deg,rgba(10,10,9,.45) 0%,rgba(10,10,9,0) 30%)}
@media (max-width:640px){.hero .wrap{padding-top:196px}}

.pg-url{font-size:14px;letter-spacing:.04em;color:var(--on-deep-muted);text-decoration:none;align-self:flex-start;border-bottom:1px solid rgba(247,244,236,.25)}
.pg-url:hover{color:var(--eye)}
.reqs dd.url{font-size:18px;font-family:var(--body);overflow-wrap:anywhere}

.mo-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:36px}
.mo-grid img{width:100%;aspect-ratio:1/1;object-fit:cover}
.mo-grid figcaption{margin-top:10px;font-size:15px;color:var(--muted)}
.mo-grid figcaption b{display:block;font-family:var(--display);font-weight:600;font-size:20px;text-transform:uppercase;color:var(--ink)}
@media (max-width:960px){.mo-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* trekking additions */
.day .trk{grid-column:1 / -1;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:0;background:var(--deep);color:var(--on-deep);border-radius:6px;overflow:hidden}
.trk-map{position:relative;min-height:230px;display:flex;align-items:center;justify-content:center;padding:44px 24px 46px;
  background-color:#151513;background-image:linear-gradient(#22211e 1px,transparent 1px),linear-gradient(90deg,#22211e 1px,transparent 1px);background-size:28px 28px}
.trk-map img{max-height:220px;max-width:100%;width:auto;height:auto}
.trk-l{position:absolute;left:16px;top:14px;font:600 12px var(--body);letter-spacing:.16em;text-transform:uppercase;color:var(--eye)}
.trk-se{position:absolute;left:16px;right:16px;bottom:14px;font-size:14px;color:var(--on-deep-muted)}
.st{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin:0;align-content:center;padding:18px 22px;gap:4px 18px}
.st div{padding:10px 0;border-bottom:1px solid #2E2D29;min-width:0}
.st div:last-child{border-bottom:0}
.st dt{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--on-deep-muted)}
.st dd{margin:2px 0 0;font-family:var(--display);font-size:26px;line-height:1.1}
.day .trk{order:3}
.days .day + .day{border-top:1px solid var(--line);padding-top:36px}
.mapsrc{font-size:13px;color:var(--muted);margin-top:16px}
.route-map svg{width:100%;height:auto;display:block}
.route .route-map{background:#121212;border-radius:6px;padding:8px}
.rv{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.rv img{width:100%;height:180px;object-fit:cover;border-radius:6px}
.rv .route-map{grid-column:1 / span 2}
.summit7{display:grid;grid-template-columns:1.2fr 1fr;gap:28px;margin-top:36px;align-items:stretch}
.summit7 .trk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);background:var(--deep);color:var(--on-deep);border-radius:6px;overflow:hidden}
.summit7 figure img{width:100%;height:100%;min-height:260px;object-fit:cover;border-radius:6px}
.day1{background:var(--paper);border-radius:6px;padding:24px;margin-top:44px}
.day1 h3{font-size:30px;text-transform:uppercase;margin-top:6px}
.day1 p{color:var(--muted);margin-top:8px;max-width:70ch}
.ask{font-family:var(--display);font-size:clamp(52px,8vw,96px);font-weight:700;line-height:.95}
.ask small{font-size:17px;line-height:1.4;font-weight:500;display:block;margin-top:14px;font-family:var(--body);max-width:34ch}
@media (max-width:960px){.summit7{grid-template-columns:1fr}}
.summit7 .st{grid-template-columns:1fr}
@media (max-width:640px){
  .day .trk,.summit7 .trk{grid-template-columns:1fr}
  .trk-map{min-height:200px}
  .st dd{font-size:22px}
  .day h3{font-size:25px}
}
.day>div{min-width:0}.day h3{overflow-wrap:break-word;hyphens:auto}
@media print{
  .top nav,.hv-badge,video,.lang,.msg,.hero-row .cta{display:none!important}
  body{font-size:12.5px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  section{padding-block:28px;break-inside:auto}
  .hero .wrap{min-height:0;padding-block:110px 36px}
  .day,.summit7,.place,.guide,details,.who,.night{break-inside:avoid}
  .day figure img{aspect-ratio:16/9}
  .faq details{display:block}
  .faq details p{display:block}
  a{text-decoration:none}
  .eyebrow,.h2,.mark{break-after:avoid}
  .route,.inc-grid,.price .wrap,.guides{break-inside:avoid}
  .eyebrow{display:block}
  .hero .wrap{min-height:0;padding-block:190px 44px!important}
  .hero-photos::after{display:none!important}
  .hero-photos img{content:url(img/hero_valley_print.jpg);object-position:0 50%!important}
  #motion{padding-top:40px}
  .mo-grid img{aspect-ratio:4/3}
  .mo-grid{margin-top:20px}
  .who-grid{margin-top:20px}
  .route{margin-top:20px;gap:28px}
  .legs{gap:12px}
  .legs li{padding-top:10px}
  .rv img{display:none}
  .rv{max-width:460px;justify-self:end}
  #who{padding-bottom:12px}
  #route{padding-top:12px}
  .days-head{break-after:avoid}
  #stay{padding-bottom:8px}
  .lead,.day1{break-inside:avoid}
}
"""

page = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Армения пешком — White Irbis</title>
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-title" content="Армения пешком">
<meta name="theme-color" content="#121212">
<meta name="description" content="7 дней в Армении пешком: Гарни и Симфония камней, Цахкуняцкий хребет, Дилижан, гора Артаниш над Севаном, крепость Смбатаберд и вершина Арагаца. Уровень, доступный всем.">
<meta property="og:type" content="website"><meta property="og:site_name" content="White Irbis">
<meta property="og:title" content="Армения пешком — 7 дней, 6 троп">
<meta property="og:description" content="Гарни, Цахкуняцкий хребет, Дилижан, Артаниш над Севаном, Смбатаберд и Арагац. Гиды-альпинисты White Irbis, уровень доступный всем.">
<meta property="og:url" content="https://scmam-rgb.github.io/white-irbis/trekking/">
<meta property="og:image" content="https://scmam-rgb.github.io/white-irbis/trekking/img/preview.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Rubik:wght@400;500;600&family=Noto+Sans+Armenian:wdth,wght@62.5..100,400..700&display=swap">
<style>{base_css}{CSS_EXTRA}</style>
</head><body>

<header class="top">
  <div class="wrap">
    <a class="brand lockup" href="#top" aria-label="White Irbis — Follow the White Irbis"><img src="img/logo.png" alt="Логотип White Irbis"><span class="sl"><span class="s1">Follow the</span><span class="s2">White <b>Irbis</b></span></span></a>
    <div class="right"><nav aria-label="Разделы">
      <a href="#program">{t("Программа","Programme","Ծրագիր")}</a>
      <a href="#places">{t("Места","Places","Վայրեր")}</a>
      <a href="#included">{t("Что входит","What's included","Ինչ է ներառված")}</a>
      <a href="#price">{t("Цена","Price","Գին")}</a>
    </nav><div class="lang" role="group" aria-label="Language"><button type="button" data-l="ru" aria-pressed="true">RU</button><button type="button" data-l="en" aria-pressed="false">EN</button><button type="button" data-l="hy" aria-pressed="false">ARM</button></div></div>
  </div>
</header>

<section class="hero" id="top">
  <div class="hero-photos" aria-hidden="true"><img src="img/hero_valley.jpg" alt="" style="object-position:50% 55%"><video class="hero-vid" src="vid/hero_meadow.mp4" muted loop playsinline preload="metadata"></video></div>
  <div class="wrap">
    <span class="alt">{t("Армения · 7 дней · май — октябрь","Armenia · 7 days · May — October","Հայաստան · 7 օր · մայիս — հոկտեմբեր")}</span>
    <h1>{t("Армения","Armenia","Հայաստան")}<br><em>{t("пешком","on foot","ոտքով")}</em></h1>
    <p class="sub">{t("Шесть троп за неделю: от базальтовых столбов Гарни и лесов Дилижана до вершины Арагаца. Уровень, доступный всем.","Six trails in a week: from the basalt columns of Garni and the forests of Dilijan to the summit of Aragats. A level anyone can manage.","Վեց արահետ մեկ շաբաթում՝ Գառնիի բազալտե սյուներից և Դիլիջանի անտառներից մինչև Արագածի գագաթ։ Մակարդակ՝ հասանելի բոլորին։")}</p>
    <div class="hero-row">
      <a class="cta" href="#price">{t("Хочу в горы","Take me to the mountains","Ուզում եմ լեռներ")}</a>
      <span class="price-chip">{t("Цена по запросу","Price on request","Գինը՝ ըստ հարցման")}<small>{t("ответим в WhatsApp","we'll reply on WhatsApp","կպատասխանենք WhatsApp-ով")}</small></span>
    </div>
    <a class="pg-url" href="https://scmam-rgb.github.io/white-irbis/trekking/">scmam-rgb.github.io/white-irbis/trekking</a>
  </div>
</section>

<section class="facts" aria-label="Коротко о туре">
  <div class="wrap"><dl>
    <div><dt>{t("Длительность","Duration","Տևողություն")}</dt><dd>{t("7 дней","7 days","7 օր")}<small>{t("6 ночей в Ереване","6 nights in Yerevan","6 գիշեր Երևանում")}</small></dd></div>
    <div><dt>{t("Сезон","Season","Սեզոն")}</dt><dd>{t("Май — октябрь","May — October","Մայիս — հոկտեմբեր")}<small>{t("Арагац — июль–сентябрь","Aragats — July–September","Արագած՝ հուլիս–սեպտեմբեր")}</small></dd></div>
    <div><dt>{t("Пешком","On foot","Ոտքով")}</dt><dd>{t("≈ 42 км","≈ 42 km","≈ 42 կմ")}<small>{t("5 троп + Арагац","5 trails + Aragats","5 արահետ + Արագած")}</small></dd></div>
    <div><dt>{t("Уровень","Level","Մակարդակ")}</dt><dd>{t("Для всех","For everyone","Բոլորի համար")}<small>{t("2,5–5 часов в день","2.5–5 hours a day","օրական 2,5–5 ժամ")}</small></dd></div>
    <div><dt>{t("Высшая точка","Highest point","Ամենաբարձր կետ")}</dt><dd>{t("3 879 м","3,879 m","3 879 մ")}<small>{t("Южная вершина Арагаца","South summit of Aragats","Արագածի Հարավային գագաթ")}</small></dd></div>
  </dl></div>
</section>

<section class="motion" id="motion" style="padding-bottom:0">
  <div class="wrap">
    <span class="eyebrow">{t("Как это выглядит","What it looks like","Ինչպես է դա երևում")}</span>
    <h2 class="h2">{t("Как ходим мы","How we walk","Ինչպես ենք քայլում")}</h2>
    <div class="mo-grid">
      <figure><span class="hv"><img src="img/f_tr_gorge.jpg" alt="Группа с рюкзаками идёт по тропе в красном ущелье" loading="lazy"><video src="vid/tr_gorge.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Красное ущелье","The red gorge","Կարմիր կիրճ")}</b> {t("Идём цепочкой между скал","Single file between the cliffs","Շարքով քայլում ենք ժայռերի միջով")}</figcaption></figure>
      <figure><span class="hv"><img src="img/f_tr_plateau.jpg" alt="Две участницы с палками идут по плато, вдали Арарат" loading="lazy"><video src="vid/tr_plateau.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Плато","The plateau","Սարահարթ")}</b> {t("Широкая тропа и Арарат на горизонте","A broad trail with Ararat on the horizon","Լայն արահետ և Արարատը հորիզոնում")}</figcaption></figure>
      <figure><span class="hv"><img src="img/f_tr_fins.jpg" alt="Группа поднимается по узкому проходу между скальных гребней" loading="lazy"><video src="vid/tr_fins.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Скальный коридор","Rock corridor","Ժայռային միջանցք")}</b> {t("Местами тропа идёт между гребней","In places the trail squeezes between ridges","Տեղ-տեղ արահետն անցնում է կատարների միջով")}</figcaption></figure>
      <figure><span class="hv"><img src="img/f_tr_hand.jpg" alt="Гид подаёт руку участнице на скальном уступе" loading="lazy"><video src="vid/tr_hand.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Подадим руку","We'll give you a hand","Ձեռք կմեկնենք")}</b> {t("На сложных местах гид рядом","The guide is beside you on tricky bits","Բարդ հատվածներում գիդը կողքիդ է")}</figcaption></figure>
      <figure><span class="hv"><img src="img/f_tr_canyon.jpg" alt="Группа идёт по сухому каньону с песчаными стенами" loading="lazy"><video src="vid/tr_canyon.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Каньон","The canyon","Կանիոն")}</b> {t("Сухие русла и песчаные стены","Dry streambeds and sandstone walls","Չոր հուներ և ավազաքարե պատեր")}</figcaption></figure>
      <figure><span class="hv"><img src="img/f_v05.jpg" alt="Группа на вершине Арагаца у креста" loading="lazy"><video src="vid/v05.mp4" muted loop playsinline preload="none" aria-hidden="true"></video><i class="hv-badge" aria-hidden="true"></i></span><figcaption><b>{t("Арагац","Aragats","Արագած")}</b> {t("Вся группа на вершине","The whole group on the summit","Ամբողջ խումբը գագաթին")}</figcaption></figure>
    </div>
  </div>
</section>

<section id="who">
  <div class="wrap">
    <span class="eyebrow">{t("Для кого","Who it's for","Ում համար է")}</span>
    <h2 class="h2">{t("Следуй за White Irbis","Follow the White Irbis","Հետևիր White Irbis-ին")}</h2>
    <div class="who-grid">
      <div class="who"><h3>{t("Первый поход","Your first hike","Առաջին արշավ")}</h3><p>{t("Тропы по 5–12 км, набор до 700 м в день. Рюкзак лёгкий: обед несём с собой, вечером возвращаемся в гостиницу.","Trails of 5–12 km with up to 700 m of climbing a day. A light pack: we carry lunch and return to the hotel every evening.","Արահետներ՝ 5–12 կմ, օրական մինչև 700 մ բարձրացում։ Թեթև ուսապարկ՝ ճաշը վերցնում ենք հետներս, երեկոյան վերադառնում հյուրանոց։")}</p></div>
      <div class="who"><h3>{t("Армения целиком","All of Armenia","Ամբողջ Հայաստանը")}</h3><p>{t("Каждый день новый пейзаж: ущелье с базальтом, альпийский хребет, лес Дилижана, Севан, красные скалы юга и вулкан.","A new landscape every day: a basalt gorge, an alpine ridge, the Dilijan forest, Sevan, the red cliffs of the south and a volcano.","Ամեն օր նոր բնանկար՝ բազալտե կիրճ, ալպյան լեռնաշղթա, Դիլիջանի անտառ, Սևան, հարավի կարմիր ժայռեր և հրաբուխ։")}</p></div>
      <div class="who dark"><h3>{t("Первая вершина","Your first summit","Առաջին գագաթ")}</h3><p>{t("В последний день — Южная вершина Арагаца, 3 879 м. Без альпинистской техники, старт на машине с 3 200 м.","On the last day, the South summit of Aragats, 3,879 m. No mountaineering technique; we drive up to 3,200 m to start.","Վերջին օրը՝ Արագածի Հարավային գագաթ, 3 879 մ։ Առանց լեռնագնացական տեխնիկայի, մեքենայով բարձրանում ենք մինչև 3 200 մ։")}</p></div>
    </div>
  </div>
</section>

<section id="route" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">{t("Маршрут","Route","Երթուղի")}</span>
    <h2 class="h2">{t("Живём в Ереване, ходим по всей стране","Based in Yerevan, walking all over the country","Ապրում ենք Երևանում, քայլում ամբողջ երկրով")}</h2>
    <div class="route">
      <ol class="legs">
        <li><b>{t("День 1","Day 1","Օր 1")}</b><span><strong>{t("Ереван.","Yerevan.","Երևան։")}</strong> {t("Встреча в аэропорту, экскурсия по городу, приветственный ужин.","Airport pick-up, city tour, welcome dinner.","Դիմավորում օդանավակայանում, էքսկուրսիա քաղաքում, ողջույնի ընթրիք։")}</span></li>
        <li><b>{t("Дни 2–3","Days 2–3","Օր 2–3")}</b><span><strong>{t("Котайк.","Kotayk.","Կոտայք։")}</strong> {t("Ущелье Гарни и Авуц Тар, потом Цахкуняцкий хребет над Агвераном.","The Garni gorge and Havuts Tar, then the Tsaghkunyats ridge above Aghveran.","Գառնիի կիրճ և Հավուց թառ, ապա Ծաղկունյաց լեռնաշղթան Աղվերանի վերևում։")}</span></li>
        <li><b>{t("Дни 4–5","Days 4–5","Օր 4–5")}</b><span><strong>{t("Дилижан и Севан.","Dilijan and Sevan.","Դիլիջան և Սևան։")}</strong> {t("Лесная тропа от Парз Лич к Гошаванку, затем гора Артаниш над Севаном.","A forest trail from Parz Lich to Goshavank, then Mount Artanish above Sevan.","Անտառային արահետ Պարզ լճից Գոշավանք, ապա Արտանիշ լեռը Սևանի վերևում։")}</span></li>
        <li><b>{t("День 6","Day 6","Օր 6")}</b><span><strong>{t("Юг.","The south.","Հարավ։")}</strong> {t("Хор Вирап, крепость Смбатаберд, Нораванк и Арени-1.","Khor Virap, Smbataberd fortress, Noravank and Areni-1.","Խոր Վիրապ, Սմբատաբերդ ամրոց, Նորավանք և Արենի-1։")}</span></li>
        <li><b>{t("День 7","Day 7","Օր 7")}</b><span><strong>{t("Арагац.","Aragats.","Արագած։")}</strong> {t("Вершина 3 879 м, крепость Амберд, вечером трансфер в аэропорт.","The 3,879 m summit, Amberd fortress, evening transfer to the airport.","Գագաթ 3 879 մ, Ամբերդ ամրոց, երեկոյան տեղափոխում օդանավակայան։")}</span></li>
      </ol>
      <div class="rv">
        <figure class="route-map">{overview}</figure>
        <img src="img/u_crater.jpg" alt="Группа на гребне кратера Арагаца" loading="lazy">
        <img src="img/u_ararat_view.jpg" alt="Привал со видом на Арарат" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="prog" id="program">
  <div class="wrap">
    <span class="eyebrow">{t("Программа","Programme","Ծրագիր")}</span>
    <h2 class="h2">{t("По дням","Day by day","Ըստ օրերի")}</h2>
    <div class="day1"><span class="mark">{t("День 1","Day 1","Օր 1")}</span><h3>{t("Прилёт в Ереван","Arrival in Yerevan","Ժամանում Երևան")}</h3><p>{t("Встречаем в аэропорту и везём в гостиницу. Экскурсия по Еревану и приветственный ужин всей группой.","We meet you at the airport and take you to the hotel. A tour of Yerevan and a welcome dinner with the whole group.","Դիմավորում ենք օդանավակայանում և տանում հյուրանոց։ Էքսկուրսիա Երևանում և ողջույնի ընթրիք ամբողջ խմբով։")}</p></div>
    <ol class="days">
{days_html}
    </ol>
    <div class="summit7">
      <figure><img src="img/kari.jpg" alt="Озеро Кари и склон Арагаца" loading="lazy">{credit("Wowan1978","CC BY-SA 4.0")}</figure>
      <div>
        <span class="mark">{t("День 7","Day 7","Օր 7")}</span>
        <h3 style="font-size:34px;text-transform:uppercase;margin-top:10px">{t("Вершина Арагаца","The summit of Aragats","Արագածի գագաթ")}</h3>
        <p style="color:var(--muted);margin-top:10px">{t("Ранний завтрак и на машине к озеру Кари на 3 200 м — талая вода снежников. Отсюда восхождение на Южную вершину Арагаца, 3 879 м: это потухший вулкан и самая высокая гора современной Армении. Спуск тем же путём, крепость Амберд на склоне, Ереван, свободное время и трансфер в аэропорт.","An early breakfast and a drive to Lake Kari at 3,200 m, fed by melting snowfields. From here we climb the South summit of Aragats, 3,879 m — an extinct volcano and the highest mountain in Armenia today. Down the same way, Amberd fortress on the slope, Yerevan, free time and the airport transfer.","Վաղ նախաճաշ և մեքենայով դեպի Քարի լիճ՝ 3 200 մ, որը սնվում է ձնադաշտերի հալոցքաջրով։ Այստեղից վերելք Արագածի Հարավային գագաթ՝ 3 879 մ․ հանգած հրաբուխ և ժամանակակից Հայաստանի ամենաբարձր լեռը։ Վայրէջք նույն ճանապարհով, Ամբերդ ամրոց լանջին, Երևան, ազատ ժամանակ և տեղափոխում օդանավակայան։")}</p>
        <div class="trk" style="margin-top:18px">
          <div class="trk-map" style="min-height:240px"><span class="trk-l">{t("Маршрут дня","Today's trail","Օրվա երթուղին")}</span><img src="img/route-aragats.png" alt="" loading="lazy"><span class="trk-se">{t("оз. Кари → Южная вершина","Lake Kari → South summit","Քարի լիճ → Հարավային գագաթ")}</span></div>
          <dl class="st">
            <div><dt>{t("Набор","Gain","Բարձրացում")}</dt><dd>{t("↑ ≈ 680 м","↑ ≈ 680 m","↑ ≈ 680 մ")}</dd></div>
            <div><dt>{t("Высоты","Altitude","Բարձրություն")}</dt><dd>{t("3 200–3 879 м","3,200–3,879 m","3 200–3 879 մ")}</dd></div>
            <div><dt>{t("Обратно","Return","Վերադարձ")}</dt><dd>{t("Тем же путём","Same way down","Նույն ճանապարհով")}</dd></div>
          </dl>
        </div>
      </div>
    </div>
    <div class="season"><span class="mark">{t("Запасной вариант","Plan B","Պահեստային տարբերակ")}</span><p><b>{t("Если погода не пускает на вершину или группе рано на 3 879 м —","If the weather closes the summit, or the group isn't ready for 3,879 m,","Եթե եղանակը թույլ չի տալիս բարձրանալ գագաթ, կամ խումբը պատրաստ չէ 3 879 մ-ին,")}</b> {t("идём пешком от крепости Амберд к селу Бюракан. Арагац обычно открыт с июля по сентябрь.","we walk from Amberd fortress down to the village of Byurakan. Aragats is usually open from July to September.","քայլում ենք Ամբերդ ամրոցից մինչև Բյուրական գյուղ։ Արագածը սովորաբար հասանելի է հուլիսից սեպտեմբեր։")}</p></div>
    <p class="mapsrc">{t("Цифры набора, длины и времени — по треку гида на каждом маршруте. Порядок дней может меняться по погоде.","Gain, distance and time figures come from our guide's GPS track on each trail. The order of days may change with the weather.","Բարձրացման, երկարության և ժամանակի թվերը՝ ըստ գիդի GPS-տրեկի յուրաքանչյուր երթուղում։ Օրերի հերթականությունը կարող է փոխվել եղանակից կախված։")}</p>
  </div>
</section>

<section id="places">
  <div class="wrap">
    <span class="eyebrow">{t("Места маршрута","Places on the route","Երթուղու վայրերը")}</span>
    <h2 class="h2">{t("Что увидите","What you'll see","Ինչ կտեսնեք")}</h2>
    <div class="places">
      <article class="place"><img src="img/azat.jpg" alt="Зелёное ущелье реки Азат под Гарни" loading="lazy"><h3>{t("Ущелье Азата","The Azat gorge","Ազատի կիրճ")}</h3><p>{t("Под храмом Гарни I века — зелёное ущелье с базальтовыми стенами. По нему идёт первая тропа тура.","Below the 1st-century Garni temple lies a green gorge with basalt walls. The tour's first trail runs through it.","I դարի Գառնիի տաճարի ներքևում կանաչ կիրճ է՝ բազալտե պատերով։ Դրանով է անցնում տուրի առաջին արահետը։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Vyacheslav Argenberg, CC BY 4.0, Wikimedia Commons</p></article>
      <article class="place"><img src="img/havuts.jpg" alt="Руины монастыря Авуц Тар" loading="lazy"><h3>{t("Авуц Тар","Havuts Tar","Հավուց թառ")}</h3><p>{t("Руины монастыря на плато над ущельем Гарни — верхняя точка тропы второго дня.","Monastery ruins on a plateau above the Garni gorge — the high point of the day-two trail.","Վանքի ավերակներ Գառնիի կիրճի վերևի սարահարթին՝ երկրորդ օրվա արահետի ամենաբարձր կետը։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Beko, CC BY-SA 4.0, Wikimedia Commons</p></article>
      <article class="place"><img src="img/geghard.jpg" alt="Монастырь Гегард среди скал" loading="lazy"><h3>{t("Гегард","Geghard","Գեղարդ")}</h3><p>{t("Монастырь IV–XIII веков, часть храмов высечена прямо в скале.","A monastery of the 4th–13th centuries; some of its churches are carved straight into the rock.","IV–XIII դդ. վանք, որի եկեղեցիների մի մասը փորված է հենց ժայռի մեջ։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Vyacheslav Argenberg, CC BY 4.0, Wikimedia Commons</p></article>
      <article class="place"><img src="img/goshavank.jpg" alt="Монастырь Гошаванк в деревне Гош" loading="lazy"><h3>{t("Гошаванк","Goshavank","Գոշավանք")}</h3><p>{t("Монастырь XII–XIII веков в деревне Гош — финиш лесной тропы от озера Парз.","A 12th–13th-century monastery in the village of Gosh, at the end of the forest trail from Lake Parz.","XII–XIII դդ. վանք Գոշ գյուղում՝ Պարզ լճից եկող անտառային արահետի վերջնակետը։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Pandukht, CC BY-SA 3.0, Wikimedia Commons</p></article>
      <article class="place"><img src="img/khorvirap.jpg" alt="Монастырь Хор Вирап на фоне Арарата" loading="lazy"><h3>{t("Хор Вирап","Khor Virap","Խոր Վիրապ")}</h3><p>{t("Монастырь на холме у подножия Арарата — лучший вид на гору из Армении.","A monastery on a hill at the foot of Ararat — the best view of the mountain from Armenia.","Վանք բլրի վրա Արարատի ստորոտին՝ լեռան լավագույն տեսարանը Հայաստանից։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Diego Delso, CC BY-SA 4.0, Wikimedia Commons</p></article>
      <article class="place"><img src="img/noravank.jpg" alt="Монастырь Нораванк среди красных скал" loading="lazy"><h3>{t("Нораванк и Арени-1","Noravank and Areni-1","Նորավանք և Արենի-1")}</h3><p>{t("Монастырь XIII века среди красных скал ущелья и пещера, где нашли древнейшую известную винодельню мира.","A 13th-century monastery among red cliffs, and the cave where the world's oldest known winery was found.","XIII դարի վանք կարմիր ժայռերի մեջ և քարանձավ, որտեղ գտել են աշխարհի ամենահին հայտնի գինեգործարանը։")}</p><p class="credit">{t("Фото: ","Photo: ","Լուսանկար՝ ")}Diego Delso, CC BY-SA 4.0, Wikimedia Commons</p></article>
    </div>
    <figure class="summit"><img src="img/aragpano.jpg" alt="Панорама вершин Арагаца из кратера" loading="lazy" style="border-radius:6px"><figcaption class="credit">{t("Вершины Арагаца из кратера. Фото: vahemart, CC BY-SA 3.0, Wikimedia Commons","The Aragats summits from the crater. Photo: vahemart, CC BY-SA 3.0, Wikimedia Commons","Արագածի գագաթները խառնարանից։ Լուսանկար՝ vahemart, CC BY-SA 3.0, Wikimedia Commons")}</figcaption></figure>
  </div>
</section>

<section id="stay" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">{t("Где живём","Where we stay","Որտեղ ենք ապրում")}</span>
    <h2 class="h2">{t("Одна гостиница на всю неделю","One hotel for the whole week","Մեկ հյուրանոց ամբողջ շաբաթվա համար")}</h2>
    <p class="lead">{t("Все шесть ночей — в гостинице в Ереване. Каждое утро выезжаем к тропе на машине, вечером возвращаемся: чемодан не таскаем, палатки не нужны.","All six nights are at a hotel in Yerevan. Every morning we drive to the trailhead and come back in the evening: no hauling luggage, no tents.","Բոլոր վեց գիշերները՝ Երևանի հյուրանոցում։ Ամեն առավոտ մեքենայով գնում ենք արահետ, երեկոյան վերադառնում՝ ճամպրուկ քարշ տալ պետք չէ, վրաններ էլ պետք չեն։")}</p>
  </div>
</section>

<section class="inc" id="included">
  <div class="wrap">
    <span class="eyebrow">{t("Что входит","What's included","Ինչ է ներառված")}</span>
    <h2 class="h2">{t("По программе","In the programme","Ծրագրով")}</h2>
    <div class="inc-grid">
      <div>
        <h3>{t("Входит","Included","Ներառված է")}</h3>
        <ul>
          <li>{t("Встреча в аэропорту и трансфер обратно","Airport pick-up and drop-off","Դիմավորում և ճանապարհում օդանավակայանում")}</li>
          <li>{t("Гостиница в Ереване — 6 ночей","Hotel in Yerevan — 6 nights","Հյուրանոց Երևանում՝ 6 գիշեր")}</li>
          <li>{t("Экскурсия по Еревану и приветственный ужин","Yerevan city tour and welcome dinner","Էքսկուրսիա Երևանում և ողջույնի ընթրիք")}</li>
          <li>{t("Все переезды к тропам","All transfers to the trails","Բոլոր տեղափոխումները դեպի արահետներ")}</li>
          <li>{t("Обеды или ланч-боксы на маршрутах","Lunches or lunch boxes on the trails","Ճաշեր կամ ճաշատուփեր երթուղիներում")}</li>
          <li>{t("Гиды-альпинисты на каждой тропе","Mountaineer guides on every trail","Լեռնագնաց գիդեր յուրաքանչյուր արահետում")}</li>
        </ul>
        <div class="no"><h3>{t("Не входит","Not included","Ներառված չէ")}</h3><ul><li>{t("Перелёт до Еревана","Flights to Yerevan","Թռիչք մինչև Երևան")}</li></ul></div>
      </div>
      <div>
        <h3>{t("Что взять","What to bring","Ինչ վերցնել")}</h3>
        <ul>
          <li>{t("Треккинговые ботинки, которые уже разношены","Hiking boots you've already broken in","Արշավային կոշիկներ, որոնք արդեն կրել եք")}</li>
          <li>{t("Небольшой рюкзак на день","A small daypack","Փոքր ուսապարկ մեկ օրվա համար")}</li>
          <li>{t("Ветровку и тёплый слой — на Арагаце холодно даже летом","A windproof jacket and a warm layer — Aragats is cold even in summer","Քամուց պաշտպանող բաճկոն և տաք շերտ՝ Արագածում ցուրտ է նույնիսկ ամռանը")}</li>
          <li>{t("Солнцезащитный крем, очки, кепку","Sunscreen, sunglasses, a cap","Արևապաշտպան քսուք, ակնոց, գլխարկ")}</li>
          <li>{t("Купальник — для Севана","Swimwear for Sevan","Լողազգեստ Սևանի համար")}</li>
        </ul>
      </div>
      <figure><img src="img/u_crater.jpg" alt="Группа на гребне кратера Арагаца" loading="lazy" style="aspect-ratio:3/4;object-fit:cover;border-radius:6px"><figcaption class="credit">{t("Выезд White Irbis на Арагац","A White Irbis trip to Aragats","White Irbis-ի ելքը Արագած")}</figcaption></figure>
    </div>
  </div>
</section>

<section id="guides">
  <div class="wrap">
    <span class="eyebrow">{t("Ваши гиды","Your guides","Ձեր գիդերը")}</span>
    <h2 class="h2">{t("С кем пойдёте","Who you'll walk with","Ում հետ կգնաք")}</h2>
    <div class="guides">
      <div class="guide"><img src="img/antoine.jpg" alt="Антуан Ананян, основатель White Irbis" loading="lazy" style="object-position:62% center"><div><h3>{t("Антуан Ананян","Antoine Ananyan","Անտուան Անանյան")}</h3><div class="role">{t("Основатель White Irbis","Founder of White Irbis","White Irbis-ի հիմնադիր")}</div><p>{t("Вице-президент Федерации альпинизма Армении. Водит группы в горах Армении с 2003 года. Автор этой программы.","Vice-president of the Mountaineering Federation of Armenia. Guiding groups in the mountains of Armenia since 2003. He designed this programme.","Հայաստանի լեռնագնացության ֆեդերացիայի փոխնախագահ։ Խմբեր է առաջնորդում Հայաստանի լեռներում 2003 թվականից։ Այս ծրագրի հեղինակն է։")}</p></div></div>
      <div class="guide"><img src="img/alexey.jpg" alt="Алексей Цисельский, гид White Irbis" loading="lazy" style="object-position:25% center"><div><h3>{t("Алексей Цисельский","Alexey Tsiselsky","Ալեքսեյ Ցիսելսկի")}</h3><div class="role">{t("Партнёр White Irbis","Partner at White Irbis","White Irbis-ի գործընկեր")}</div><p>{t("10 лет в альпинизме: Гималаи, Тянь-Шань, Кавказ, Альпы. 4 года в горах Армении.","10 years of mountaineering: Himalayas, Tian Shan, Caucasus, Alps. 4 years in the mountains of Armenia.","10 տարի լեռնագնացության մեջ՝ Հիմալայներ, Տյան-Շան, Կովկաս, Ալպեր։ 4 տարի Հայաստանի լեռներում։")}</p></div></div>
    </div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="wrap">
    <span class="eyebrow">{t("Частые вопросы","FAQ","Հաճախ տրվող հարցեր")}</span>
    <h2 class="h2">{t("Перед поездкой","Before you go","Մինչ ուղևորությունը")}</h2>
    <div class="faq-list">
      <details open><summary>{t("Я никогда не ходил в походы. Справлюсь?","I've never hiked. Can I do it?","Երբեք արշավի չեմ գնացել։ Կհաղթահարե՞մ")}</summary><p>{t("Да. Самая длинная тропа — 12 км за 3–4 часа, самый большой набор — около 700 м. Идём в темпе группы, с привалами.","Yes. The longest trail is 12 km in 3–4 hours and the biggest climb is about 700 m. We go at the group's pace, with rests.","Այո։ Ամենաերկար արահետը 12 կմ է՝ 3–4 ժամում, ամենամեծ բարձրացումը՝ մոտ 700 մ։ Քայլում ենք խմբի տեմպով, դադարներով։")}</p></details>
      <details><summary>{t("Обязательно идти на Арагац?","Do I have to climb Aragats?","Պարտադի՞ր է բարձրանալ Արագած")}</summary><p>{t("Нет. Если погода плохая или вы устали, вместо вершины идём от крепости Амберд к Бюракану.","No. If the weather is bad or you're tired, we walk from Amberd fortress to Byurakan instead.","Ոչ։ Եթե եղանակը վատ է կամ հոգնել եք, գագաթի փոխարեն քայլում ենք Ամբերդից Բյուրական։")}</p></details>
      <details><summary>{t("Когда лучше ехать?","When is the best time?","Երբ է լավագույն ժամանակը")}</summary><p>{t("Тропы открыты с мая по октябрь. Вершина Арагаца — обычно с июля по сентябрь, в остальные месяцы идём запасным маршрутом.","The trails are open from May to October. The Aragats summit is usually July to September; in other months we take the backup route.","Արահետները բաց են մայիսից հոկտեմբեր։ Արագածի գագաթը՝ սովորաբար հուլիսից սեպտեմբեր, մնացած ամիսներին գնում ենք պահեստային երթուղով։")}</p></details>
      <details><summary>{t("Что с едой на тропе?","What about food on the trail?","Իսկ սնունդը արահետում")}</summary><p>{t("Обед или ланч-боксы входят в программу. Воду на день лучше взять с собой — подскажем, сколько.","Lunch or lunch boxes are included. Bring water for the day — we'll tell you how much.","Ճաշը կամ ճաշատուփերը ներառված են։ Ջուրը օրվա համար ավելի լավ է վերցնել հետներդ՝ կասենք, թե որքան։")}</p></details>
    </div>
  </div>
</section>

<section class="price" id="price">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:var(--eye-ink)">{t("Цена","Price","Գին")}</span>
      <div class="ask">{t("По запросу","On request","Ըստ հարցման")}<small>{t("зависит от дат и размера группы — напишите, посчитаем","depends on dates and group size — message us and we'll quote","կախված է ամսաթվերից և խմբի չափից՝ գրեք, կհաշվենք")}</small></div>
      <ul>
        <li>{t("7 дней, 6 ночей в Ереване","7 days, 6 nights in Yerevan","7 օր, 6 գիշեր Երևանում")}</li>
        <li>{t("Май — октябрь, Арагац — июль–сентябрь","May — October, Aragats July–September","Մայիս — հոկտեմբեր, Արագած՝ հուլիս–սեպտեմբեր")}</li>
        <li>{t("Перелёт до Еревана — отдельно","Flights to Yerevan not included","Թռիչքը մինչև Երևան՝ առանձին")}</li>
      </ul>
    </div>
    <div class="contact">
      <h3>{t("Идём в горы?","Ready to walk?","Գնո՞ւմ ենք լեռներ")}</h3>
      <p>{t("Напишите нам — пришлём даты и цену и ответим на вопросы.","Message us — we'll send dates and the price and answer your questions.","Գրեք մեզ՝ կուղարկենք ամսաթվերն ու գինը և կպատասխանենք հարցերին։")}</p>
      <div class="msg"><a class="cta wa" href="https://wa.me/{PHONE}" target="_blank" rel="noopener">{WA_SVG}<span>WhatsApp</span></a><a class="cta tg" href="https://t.me/+{PHONE}" target="_blank" rel="noopener">{TG_SVG}<span>Telegram</span></a></div>
      <dl class="reqs">
        <div><dt>{t("Телефон, WhatsApp, Telegram","Phone, WhatsApp, Telegram","Հեռախոս, WhatsApp, Telegram")}</dt><dd><a href="tel:+{PHONE}">+374 91 470 331</a></dd></div>
        <div><dt>{t("Почта","Email","Էլ. փոստ")}</dt><dd><a href="mailto:antuanvisit@gmail.com">antuanvisit@gmail.com</a></dd></div>
        <div><dt>{t("Страница тура","Tour page","Տուրի էջը")}</dt><dd class="url"><a href="https://scmam-rgb.github.io/white-irbis/trekking/">scmam-rgb.github.io/white-irbis/trekking</a></dd></div>
        <div><dt>{t("Сайт","Website","Կայք")}</dt><dd><a href="https://irbis.am" target="_blank" rel="noopener">irbis.am</a></dd></div>
      </dl>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <p><b>White Irbis</b> {t("· горные программы в Армении · irbis.am ·","· mountain programmes in Armenia · irbis.am ·","· լեռնային ծրագրեր Հայաստանում · irbis.am ·")} <a href="tel:+{PHONE}">+374 91 470 331</a> (WhatsApp, Telegram) · antuanvisit@gmail.com · <a href="https://scmam-rgb.github.io/white-irbis/trekking/">scmam-rgb.github.io/white-irbis/trekking</a></p>
    <p>{t("Ещё у нас:","Also from us:","Նաև մեզ մոտ՝")} <a href="../skaly-i-vulkan/">{t("Скалы и вулкан","Rocks and Volcano","Ժայռեր և հրաբուխ")}</a> · <a href="../weekend/">{t("Скалы за выходные","Rocks in a weekend","Ժայռեր հանգստյան օրերին")}</a> · <a href="../ski/">{t("Горные лыжи с нуля","Skiing from scratch","Լեռնադահուկ զրոյից")}</a> · <a href="../gaidbuk/">{t("Гайдбук «Скалы Армении»","Guidebook «Rocks of Armenia»","«Հայաստանի ժայռեր» ուղեցույց")}</a></p>
    <p>{t("Фото Wikimedia Commons — по лицензиям CC BY и CC BY-SA, авторы указаны под снимками. Схемы троп нарисованы по трекам гида. Остальные фото — архив White Irbis.","Wikimedia Commons photos are used under CC BY and CC BY-SA licences; authors are credited under each image. Trail sketches are drawn from our guide's tracks. All other photos are from the White Irbis archive.","Wikimedia Commons-ի լուսանկարները՝ CC BY և CC BY-SA լիցենզիաներով, հեղինակները նշված են լուսանկարների տակ։ Արահետների սխեմաները գծված են գիդի տրեկերով։ Մնացած լուսանկարները White Irbis-ի արխիվից են։")}</p>
  </div>
</footer>

<script>
(function(){{
  var items=[].slice.call(document.querySelectorAll('.hv'));
  function play(el){{var v=el.querySelector('video');if(!v)return;var p=v.play();if(p&&p.catch)p.catch(function(){{}});el.classList.add('on');}}
  function stop(el){{var v=el.querySelector('video');if(!v)return;v.pause();el.classList.remove('on');}}
  var canHover=window.matchMedia&&window.matchMedia('(hover:hover)').matches;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  items.forEach(function(el){{el.addEventListener('mouseenter',function(){{play(el)}});el.addEventListener('mouseleave',function(){{stop(el)}});el.addEventListener('click',function(){{el.classList.contains('on')?stop(el):play(el)}});}});
  if(!canHover&&!reduce&&'IntersectionObserver' in window){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{e.intersectionRatio>0.6?play(e.target):stop(e.target)}})}},{{threshold:[0,0.6]}});items.forEach(function(el){{io.observe(el)}});}}
}})();
(function(){{
  var h=document.querySelector('.hero'),v=h&&h.querySelector('.hero-vid'),ph=h&&h.querySelector('.hero-photos');if(!v)return;
  function on(){{var p=v.play();if(p&&p.catch)p.catch(function(){{}});h.classList.add('on')}}
  function off(){{v.pause();h.classList.remove("on");setTimeout(function(){{if(!h.classList.contains("on"))v.currentTime=0}},650)}}
  var hover=window.matchMedia('(hover:hover)').matches,reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce)return;
  if(hover){{h.addEventListener('mousemove',function(e){{var r=ph.getBoundingClientRect();(e.clientX>=r.left)?(h.classList.contains('on')||on()):(h.classList.contains('on')&&off())}});h.addEventListener('mouseleave',off);setTimeout(on,2500)}}
  else{{setTimeout(on,2500)}}
}})();
(function(){{var h=document.documentElement,b=[].slice.call(document.querySelectorAll('.lang button'));
var t={{ru:'Армения пешком — White Irbis',en:'Armenia on Foot — White Irbis',hy:'Հայաստան ոտքով — White Irbis'}};
var m={{ru:'Здравствуйте! Интересует тур «Армения пешком»',en:'Hello! I am interested in the "Armenia on Foot" tour',hy:'Բարև Ձեզ։ Հետաքրքրում է «Հայաստան ոտքով» տուրը'}};
function set(l){{h.lang=l;b.forEach(function(x){{x.setAttribute('aria-pressed',x.dataset.l===l)}});document.title=t[l];
[].slice.call(document.querySelectorAll('a[href^="https://wa.me/{PHONE}"]')).forEach(function(a){{a.href='https://wa.me/{PHONE}?text='+encodeURIComponent(m[l])}});
try{{localStorage.setItem('wi-lang',l)}}catch(e){{}}}}
var q=(location.search.match(/lang=(ru|en|hy)/)||[])[1],s=null;try{{s=localStorage.getItem('wi-lang')}}catch(e){{}}
set(q||(['ru','en','hy'].indexOf(s)>=0?s:'ru'));b.forEach(function(x){{x.addEventListener('click',function(){{set(x.dataset.l)}})}});}})();
</script>
</body></html>
'''
(ROOT / "trekking/index.html").write_text(page, encoding="utf-8")
print("ok", len(page))
