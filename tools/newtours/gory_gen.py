import os
H = os.path.dirname(os.path.abspath(__file__))
def T(ru, en, hy): return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'

LV = {'e': ('Несложно','Easy','Հեշտ'), 'm': ('Средне','Moderate','Միջին'), 'h': ('Сложно','Hard','Դժվար'), 'x': ('Для опытных','Experienced only','Փորձառուների համար')}
HIGH = ('Июль — сентябрь','July — September','Հուլիս — սեպտեմբեր')
MID = ('Май — октябрь','May — October','Մայիս — հոկտեմբեր')

# id, name, alt(m), region, level, season, route, story, link, img
peaks = [
 ('aragats', ('Арагац','Aragats','Արագած'), 4090, ('Арагацотн','Aragatsotn','Արագածոտն'), 'h', HIGH,
  ('Северная — от водопада у села Арагац, на джипе и пешком. Западная, Восточная и Южная — от озера Кари; Южная самая простая, 3–3,5 часа вверх.','North peak — from the waterfall above Aragats village, by jeep and on foot. West, East and South — from Lake Kari; the South peak is the easiest, 3–3.5 hours up.','Հյուսիսայինը՝ Արագած գյուղի մոտ ջրվեժից, ջիպով և ոտքով։ Արևմտյանը, Արևելյանը և Հարավայինը՝ Քարի լճից. Հարավայինն ամենահեշտն է, 3–3,5 ժամ վերելք։'),
  ('Крыша Армении: потухший вулкан с четырьмя вершинами вокруг кратера. Южная — лучшая первая высота, Северная — острый гребень и вид на весь кратер.','The roof of Armenia: an extinct volcano with four summits around its crater. The South peak is the best first big climb; the North peak has a sharp ridge and a view over the whole crater.','Հայաստանի տանիքը՝ հանգած հրաբուխ՝ խառնարանի շուրջ չորս գագաթով։ Հարավայինը լավագույն առաջին բարձունքն է, Հյուսիսայինը՝ սուր կատար և տեսարան ամբողջ խառնարանին։'),
  ('../aragats/', ('Наш тур на Северную →','Our North peak tour →','Մեր տուրը Հյուսիսային →')), 'aragats.jpg'),
 ('kaputjugh', ('Капутджух','Kaputjugh','Կապուտջուղ'), 3905, ('Сюник','Syunik','Սյունիք'), 'x', HIGH,
  ('Зангезурский хребет, вершина на самой границе с Нахичеванью.','The Zangezur range; the summit sits right on the border with Nakhchivan.','Զանգեզուրի լեռնաշղթա, գագաթը հենց Նախիջևանի սահմանին է։'),
  ('Вторая по высоте гора Армении и высшая точка Сюника. Из-за пограничной зоны восхождение возможно не всегда — обстановку уточняем перед выездом.','Armenia\'s second-highest mountain and the top of Syunik. Because of the border zone a climb is not always possible — we check the situation before going.','Հայաստանի երկրորդ ամենաբարձր լեռը և Սյունիքի ամենաբարձր կետը։ Սահմանային գոտու պատճառով վերելքը միշտ չէ, որ հնարավոր է՝ իրավիճակը ճշտում ենք մեկնելուց առաջ։'),
  None, None),
 ('azhdahak', ('Аждаак','Azhdahak','Աժդահակ'), 3597, ('Гегамский хребет','Gegham range','Գեղամա լեռնաշղթա'), 'm', HIGH,
  ('На джипе к подножию Пайтасара, дальше 5,5 км пешком, набор около 600 м.','By jeep to the foot of Mt Paytasar, then 5.5 km on foot with about 600 m of climbing.','Ջիպով մինչև Պայտասարի ստորոտ, հետո 5,5 կմ ոտքով, մոտ 600 մ բարձրացում։'),
  ('Высшая точка Гегама. В кратере — синее озеро, где летом можно искупаться, на склонах — петроглифы, с вершины видны Севан, Арагац и Арарат.','The highest point of the Gegham range. A blue lake fills the crater — you can swim in summer — there are petroglyphs on the slopes, and the summit looks out to Sevan, Aragats and Ararat.','Գեղամա լեռների ամենաբարձր կետը։ Խառնարանում կապույտ լիճ է, որտեղ ամռանը կարելի է լողալ, լանջերին՝ ժայռապատկերներ, գագաթից երևում են Սևանը, Արագածը և Արարատը։'),
  ('../skaly-i-vulkan/', ('В «Скалах и вулканах» →','In Rocks and Volcanoes →','«Ժայռեր և հրաբուխներ»-ում →')), None),
 ('ughtasar', ('Ухтасар','Ughtasar','Ուխտասար'), 3300, ('Сюник','Syunik','Սյունիք'), 'e', ('Июль — август','July — August','Հուլիս — օգոստոս'),
  ('Около 30 км от Сисиана: на джипе через село Ишханасар, последние сотни метров пешком.','About 30 km from Sisian: by jeep via Ishkhanasar village, the last few hundred metres on foot.','Սիսիանից մոտ 30 կմ՝ ջիպով Իշխանասար գյուղով, վերջին մի քանի հարյուր մետրը՝ ոտքով։'),
  ('Высокогорное плато у озера на 3 300 м и тысячи наскальных рисунков — самые древние до 7 000 лет. Дорога открыта только в хорошую погоду середины лета.','A high plateau by a lake at 3,300 m and thousands of rock carvings, the oldest up to 7,000 years old. The road is only passable in good midsummer weather.','Բարձրլեռնային սարահարթ՝ լճի մոտ 3 300 մ բարձրության վրա, և հազարավոր ժայռապատկերներ՝ ամենահները մինչև 7 000 տարեկան։ Ճանապարհը բաց է միայն ամռան կեսին՝ լավ եղանակին։'),
  None, None),
 ('khustup', ('Хуступ','Khustup','Խուստուփ'), 3201, ('Сюник, над Капаном','Syunik, above Kapan','Սյունիք, Կապանի վրա'), 'h', HIGH,
  ('От села Багабурдж под Капаном, обычно 2 дня с ночёвкой в лагере под вершиной.','From Baghaburj village near Kapan, usually 2 days with a camp below the summit.','Կապանի մոտ Բաղաբուրջ գյուղից, սովորաբար 2 օր՝ գագաթի տակ ճամբարով։'),
  ('Скальная корона над Капаном с коротким лазанием у вершины. Летом склоны в цветах, осенью внизу — море облаков.','A rocky crown above Kapan with a short scramble near the top. Flower-covered slopes in summer, a sea of clouds below in autumn.','Ժայռոտ թագ Կապանի վրա՝ գագաթի մոտ կարճ մագլցումով։ Ամռանը լանջերը ծաղիկների մեջ են, աշնանը ներքևում՝ ամպերի ծով։'),
  None, None),
 ('artavaz', ('Артаваз','Artavaz','Արտավազ'), 2929, ('Котайк, Памбакский хребет','Kotayk, Pambak range','Կոտայք, Փամբակի լեռնաշղթա'), 'm', MID,
  ('От села Артаваз и обратно — около 17 км, набор около 1&nbsp;050 м.','From Artavaz village and back — about 17 km with about 1,050 m of climbing.','Արտավազ գյուղից և հետ՝ մոտ 17 կմ, մոտ 1 050 մ բարձրացում։'),
  ('Одна из самых красивых и мощных вершин Памбака. Снег держится на склонах до лета — весной сюда ходят на скитур. С вершины видно Мармарикское водохранилище и Арагац.','One of the most beautiful and powerful peaks of the Pambak range. Snow lingers on its slopes into summer, so in spring it is a ski-touring spot. The summit looks out over the Marmarik reservoir and Aragats.','Փամբակի լեռնաշղթայի ամենագեղեցիկ և հզոր գագաթներից մեկը։ Ձյունը լանջերին մնում է մինչև ամառ, ուստի գարնանը այստեղ սկիտուր են անում։ Գագաթից երևում են Մարմարիկի ջրամբարը և Արագածը։'),
  None, None),
 ('teghenis', ('Тегенис','Teghenis','Թեղենիս'), 2851, ('Котайк, над Цахкадзором','Kotayk, above Tsaghkadzor','Կոտայք, Ծաղկաձորի վրա'), 'm', MID,
  ('Около 15 км, набор около 1 000 м. Час езды от Еревана.','About 15 km with about 1,000 m of climbing. An hour\'s drive from Yerevan.','Մոտ 15 կմ, մոտ 1 000 մ բարձրացում։ Երևանից մեկ ժամ ճանապարհ։'),
  ('Главная вершина Цахкуняцкого хребта. На склоне — монастырь Техенеац, зимой здесь катаются на лыжах, летом — один из лучших дневных подъёмов у Еревана.','The main peak of the Tsaghkunyats range. Teghenyats monastery stands on its slope; in winter this is ski country, in summer one of the best day climbs near Yerevan.','Ծաղկունյաց լեռնաշղթայի գլխավոր գագաթը։ Լանջին Թեղենյաց վանքն է, ձմռանը այստեղ դահուկ են քշում, ամռանը՝ Երևանի մոտ լավագույն մեկօրյա վերելքներից մեկը։'),
  None, None),
 ('ara', ('Ара (Араилер)','Ara (Arailer)','Արա (Արայի լեռ)'), 2577, ('Котайк — Арагацотн','Kotayk — Aragatsotn','Կոտայք — Արագածոտն'), 'm', MID,
  ('Около 11 км, набор около 870 м. Есть круговой и сквозной варианты.','About 11 km with about 870 m of climbing. Loop and through-hike options.','Մոտ 11 կմ, մոտ 870 մ բարձրացում։ Կան շրջանաձև և միակողմանի տարբերակներ։'),
  ('Издалека гора похожа на лежащего великана. По легенде, здесь погиб Ара Прекрасный, отвергший царицу Шамирам, — и его тело оставили в пещере на этой горе.','From afar the mountain looks like a sleeping giant. Legend says Ara the Beautiful, who rejected Queen Shamiram, fell here and his body was left in a cave on this mountain.','Հեռվից լեռը նման է պառկած հսկայի։ Ըստ ավանդության՝ այստեղ է զոհվել Շամիրամին մերժած Արա Գեղեցիկը, և նրա մարմինը թողել են այս լեռան քարայրում։'),
  ('../skaly-i-vulkan/', ('В «Скалах и вулканах» →','In Rocks and Volcanoes →','«Ժայռեր և հրաբուխներ»-ում →')), None),
 ('lalvar', ('Лалвар','Lalvar','Լալվար'), 2552, ('Лори','Lori','Լոռի'), 'm', MID,
  ('От села Качачкут и обратно — около 15 км, набор около 950 м.','From Kachachkut village and back — about 15 km with about 950 m of climbing.','Կաչաճկուտ գյուղից և հետ՝ մոտ 15 կմ, մոտ 950 մ բարձրացում։'),
  ('Одна из самых красивых гор севера: её видно из разных уголков Лори и даже из Грузии.','One of the most beautiful mountains of the north, visible from all over Lori and even from Georgia.','Հյուսիսի ամենագեղեցիկ լեռներից մեկը. այն երևում է Լոռու տարբեր անկյուններից և նույնիսկ Վրաստանից։'),
  None, None),
 ('hatis', ('Атис','Hatis','Հատիս'), 2528, ('Котайк','Kotayk','Կոտայք'), 'm', MID,
  ('От села Капутан, 5,6 км в одну сторону. 21 км от Еревана.','From Kaputan village, 5.6 km one way. 21 km from Yerevan.','Կապուտան գյուղից՝ 5,6 կմ մեկ ուղղությամբ։ Երևանից 21 կմ։'),
  ('Ровный конус потухшего вулкана, видный из Еревана. На вершине — руины крепости, которую связывают с царицей Шамирам, и маленькая пещера.','The neat cone of an extinct volcano, visible from Yerevan. On top are the ruins of a fortress linked to Queen Shamiram and a small cave.','Հանգած հրաբխի կանոնավոր կոն, որը երևում է Երևանից։ Գագաթին Շամիրամ թագուհու հետ կապվող ամրոցի ավերակներն են և փոքրիկ քարայր։'),
  ('../skaly-i-vulkan/', ('В «Скалах и вулканах» →','In Rocks and Volcanoes →','«Ժայռեր և հրաբուխներ»-ում →')), None),
 ('artanish', ('Артаниш','Artanish','Արտանիշ'), 2460, ('Севан','Sevan','Սևան'), 'e', MID,
  ('От Шоржи, 5 км в одну сторону, набор около 560 м.','From Shorzha, 5 km one way with about 560 m of climbing.','Շորժայից՝ 5 կմ մեկ ուղղությամբ, մոտ 560 մ բարձրացում։'),
  ('Единственная вершина, откуда виден весь Севан — оба его «озера». После спуска — купание.','The only summit from which you can see the whole of Lake Sevan, both its basins. A swim after the descent.','Միակ գագաթը, որտեղից երևում է ամբողջ Սևանը՝ նրա երկու մասերը։ Իջնելուց հետո՝ լողանալ։'),
  ('../trekking/', ('В «Армении пешком» →','In Armenia on Foot →','«Հայաստան ոտքով»-ում →')), None),
 ('dimats', ('Димац','Dimats','Դիմաց'), 2378, ('Тавуш','Tavush','Տավուշ'), 'h', MID,
  ('От села Техут, 8,5 км в одну сторону, набор около 1 260 м, около 7,5 часа.','From Teghut village, 8.5 km one way, about 1,260 m of climbing, about 7.5 hours.','Թեղուտ գյուղից՝ 8,5 կմ մեկ ուղղությամբ, մոտ 1 260 մ բարձրացում, մոտ 7,5 ժամ։'),
  ('Белые скалы над зелёными склонами, туманы и вид на водопад Шагот. Невысокая, но крутая.','White cliffs above green slopes, mist and a view of Shaghot waterfall. Not high, but steep.','Սպիտակ ժայռեր կանաչ լանջերի վրա, մշուշ և տեսարան Շաղոտի ջրվեժին։ Բարձր չէ, բայց զառիթափ է։'),
  ('../skaly-i-vulkan/', ('В «Скалах и вулканах» →','In Rocks and Volcanoes →','«Ժայռեր և հրաբուխներ»-ում →')), None),
]

def card(p):
    pid, name, alt, region, lv, season, route, story, link, img = p
    altf = f'{alt:,}'.replace(',', ' ')
    alten = f'{alt:,}'
    approx = pid == 'ughtasar'
    altxt = T(('≈ ' if approx else '') + altf + ' м', ('≈ ' if approx else '') + alten + ' m', ('≈ ' if approx else '') + altf + ' մ')
    head = (f'<div class="pk-img"><img src="img/{img}" alt="" loading="lazy"><b>{altxt}</b></div>' if img
            else f'<div class="pk-alt"><b>{altxt}</b></div>')
    four = ''
    if pid == 'aragats':
        four = '<div class="stats four">' + ''.join(f'<span>{T(a,b,c)} <b>{h}</b></span>' for a,b,c,h in [('Северная','North','Հյուսիսային','4 090'),('Западная','West','Արևմտյան','4 008'),('Восточная','East','Արևելյան','3 908'),('Южная','South','Հարավային','3 879')]) + '</div>'
    lk = f'<p class="pk-link"><a href="{link[0]}">{T(*link[1])}</a></p>' if link else ''
    return f'''<article class="pk" id="{pid}">
{head}
<div class="pk-b">
<h3>{T(*name)}</h3>
<div class="stats"><span>{T(*region)}</span><span class="lv lv-{lv}">{T(*LV[lv])}</span><span>{T(*season)}</span></div>
<p>{T(*story)}</p>
{four}
<p class="pk-r"><i>{T("Как идти","The route","Երթուղին")}</i>{T(*route)}</p>
{lk}
</div></article>'''

def ladder():
    mx = 4090
    rows = []
    for p in sorted(peaks, key=lambda x: -x[2]):
        pid, name, alt = p[0], p[1], p[2]
        w = round(100 * (alt - 1800) / (mx - 1800), 1)
        rows.append(f'<li><a href="#{pid}"><span class="ln">{T(*name)}</span><span class="lb"><i style="width:{w}%"></i></span><span class="la">{("≈ " if pid=="ughtasar" else "")}{alt:,}</span></a></li>'.replace(',', ' ', 0))
    return '<ol class="ladder">' + ''.join(rows).replace('4,090', '4 090') + '</ol>'

def fix_num(s):
    import re
    return re.sub(r'(?<=<span class="la">)(≈ )?(\d),(\d{3})', lambda m: (m.group(1) or '') + m.group(2) + ' ' + m.group(3), s)

tips = [
 (('Выходите рано','Start early','Մեկնեք վաղ'),
  ('Летом после обеда в горах часто собираются грозы. На высокие вершины выходим на рассвете, чтобы к обеду уже спускаться.','In summer, storms often build in the mountains after midday. We start high climbs at dawn so we are descending by lunchtime.','Ամռանը կեսօրից հետո լեռներում հաճախ ամպրոպներ են լինում։ Բարձր գագաթներ դուրս ենք գալիս արշալույսին, որպեսզի կեսօրին արդեն իջնենք։')),
 (('Высота','Altitude','Բարձրություն'),
  ('Выше 3 000 м многим тяжело с непривычки. Хороший план — сначала гора пониже, например Тегенис или Ара, потом Арагац или Аждаак.','Above 3,000 m many people struggle at first. A good plan is a lower peak first, such as Teghenis or Ara, then Aragats or Azhdahak.','3 000 մ-ից բարձր շատերի համար սկզբում դժվար է։ Լավ պլան է՝ նախ ավելի ցածր լեռ, օրինակ Թեղենիս կամ Արա, հետո Արագած կամ Աժդահակ։')),
 (('Дорога к старту','Getting to the start','Ճանապարհ դեպի մեկնարկ'),
  ('К Аждааку, Ухтасару и Северной Арагаца ведут грунтовки, где нужен джип. Остальные старты — у сёл, куда доезжает обычная машина.','Azhdahak, Ughtasar and the North peak of Aragats are reached by dirt roads that need a jeep. The other trailheads are by villages an ordinary car can reach.','Աժդահակ, Ուխտասար և Արագածի Հյուսիսային գագաթ տանում են գրունտային ճանապարհներ, որտեղ ջիպ է պետք։ Մյուս մեկնարկները գյուղերի մոտ են, ուր հասնում է սովորական մեքենան։')),
 (('Вода и собаки','Water and dogs','Ջուր և շներ'),
  ('На высоких маршрутах воды почти нет — берите 2 литра. У кошар пастушьи собаки: не подходите близко к отаре, держите палки под рукой.','There is hardly any water on the high routes — carry 2 litres. Shepherd dogs guard the flocks: keep your distance from the sheep and your poles handy.','Բարձր երթուղիներում ջուր գրեթե չկա՝ վերցրեք 2 լիտր։ Ոչխարների մոտ հովվական շներ են՝ մի մոտեցեք հոտին, ձողերը պահեք ձեռքի տակ։')),
]

body = f'''<header class="top"><div class="wrap">
  <a class="lockup" href="../"><img src="img/logo.png" alt="White Irbis"><span class="sl"><span class="s1">Follow the</span><span class="s2">White <b>Irbis</b></span></span></a>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-l="ru" aria-pressed="true">RU</button><button type="button" data-l="en" aria-pressed="false">EN</button><button type="button" data-l="hy" aria-pressed="false">ARM</button></div>
</div></header>

<section class="hero" id="top">
  <div class="hero-media" aria-hidden="true"><img src="img/hero.jpg" alt="" style="object-position:55% 60%"></div>
  <div class="wrap">
    <span class="alt">{T("Гайдбук · 12 вершин","Guidebook · 12 peaks","Ուղեցույց · 12 գագաթ")}</span>
    <h1>{T("Горы<br><em>Армении</em>","Mountains<br><em>of Armenia</em>","Հայաստանի<br><em>լեռները</em>")}</h1>
    <p class="sub">{T("Вершины, ради которых стоит ехать: от «спящего великана» Ара над Ереваном до 4 090 м Арагаца. Высота, старт, сложность и сезон — на одной странице.","The peaks worth the trip: from Ara, the 'sleeping giant' above Yerevan, to Aragats at 4,090 m. Height, trailhead, difficulty and season — all on one page.","Գագաթներ, որոնց համար արժե գալ՝ Երևանի վրա «քնած հսկա» Արայից մինչև 4 090 մ Արագած։ Բարձրություն, մեկնարկ, բարդություն և սեզոն՝ մեկ էջում։")}</p>
    <div class="row"><a class="cta" href="#peaks">{T("Смотреть вершины","See the peaks","Տեսնել գագաթները")}</a></div>
  </div>
</section>

<section class="facts"><div class="wrap"><dl>
  <div><dt>{T("Вершин","Peaks","Գագաթներ")}</dt><dd>12</dd></div>
  <div><dt>{T("Высшая","Highest","Ամենաբարձր")}</dt><dd>{T("Арагац, 4 090 м","Aragats, 4,090 m","Արագած, 4 090 մ")}</dd></div>
  <div><dt>{T("Ближе всего к Еревану","Closest to Yerevan","Երևանին ամենամոտ")}</dt><dd>{T("Атис, 21 км","Hatis, 21 km","Հատիս, 21 կմ")}</dd></div>
  <div><dt>{T("Сезон","Season","Սեզոն")}</dt><dd>{T("Май — октябрь","May — October","Մայիս — հոկտեմբեր")}</dd></div>
</dl></div></section>

<section id="ladder"><div class="wrap ld">
  <div>
    <span class="eyebrow">{T("Лестница высот","Height ladder","Բարձրությունների սանդուղք")}</span>
    <h2 class="h2">{T("От 2&nbsp;300 до 4&nbsp;090 метров","From 2,300 to 4,090 metres","2&nbsp;300-ից մինչև 4&nbsp;090 մետր")}</h2>
    <p class="lead">{T("Армения — горная страна: почти вся она лежит выше тысячи метров. Мы выбрали вершины, у которых есть своя история — кратерное озеро, древние петроглифы, легенда или вид, за которым стоит подняться.","Armenia is a mountain country: almost all of it lies above a thousand metres. We picked peaks that each have a story — a crater lake, ancient petroglyphs, a legend or a view worth the climb.","Հայաստանը լեռնային երկիր է՝ գրեթե ամբողջությամբ գտնվում է հազար մետրից բարձր։ Մենք ընտրել ենք գագաթներ, որոնցից յուրաքանչյուրն ունի իր պատմությունը՝ խառնարանային լիճ, հնագույն ժայռապատկերներ, ավանդություն կամ տեսարան, որի համար արժե բարձրանալ։")}</p>
  </div>
  {fix_num(ladder())}
</div></section>

<section id="peaks" class="sec-pk"><div class="wrap">
  <span class="eyebrow">{T("Вершины","The peaks","Գագաթները")}</span>
  <h2 class="h2">{T("Куда подняться","Where to climb","Ուր բարձրանալ")}</h2>
  <div class="pks">
{chr(10).join(card(p) for p in peaks)}
  </div>
  <p class="credit">{T("Километры и набор — ориентир по открытым источникам и нашим выходам; на месте всё зависит от погоды и выбранного варианта.","Distances and climbing figures are a guide from public sources and our own trips; on the day it depends on the weather and the route option.","Կիլոմետրերն ու բարձրացումը կողմնորոշիչ են՝ ըստ բաց աղբյուրների և մեր ելքերի. տեղում ամեն ինչ կախված է եղանակից և ընտրված տարբերակից։")}</p>
</div></section>

<section class="next" id="ararat"><div class="wrap">
  <figure style="margin:0"><img src="img/ararat.jpg" alt="Группа поднимается по леднику Арарата" loading="lazy" style="aspect-ratio:4/3"></figure>
  <div>
    <span class="eyebrow">{T("И главная гора","And the main mountain","Եվ գլխավոր լեռը")}</span>
    <h2 class="h2">{T("Арарат, 5 137 м","Ararat, 5,137 m","Արարատ, 5 137 մ")}</h2>
    <p class="lead">{T("Символ Армении виден почти с каждой вершины из этого списка, но стоит в Турции. Мы ходим на него через Грузию — 6 дней из Еревана.","The symbol of Armenia can be seen from almost every peak on this list, but it stands in Turkey. We climb it via Georgia — 6 days from Yerevan.","Հայաստանի խորհրդանիշը երևում է այս ցանկի գրեթե բոլոր գագաթներից, բայց գտնվում է Թուրքիայում։ Մենք բարձրանում ենք Վրաստանով՝ 6 օր Երևանից։")}</p>
    <p class="lead"><a href="../ararat/">{T("Восхождение на Арарат →","Mount Ararat ascent →","Վերելք Արարատ →")}</a></p>
  </div>
</div></section>

<section class="inc" id="tips"><div class="wrap">
  <span class="eyebrow">{T("Перед выходом","Before you go","Մինչ ելքը")}</span>
  <h2 class="h2">{T("Четыре правила армянских гор","Four rules of Armenian mountains","Հայկական լեռների չորս կանոն")}</h2>
  <div class="prac">
{chr(10).join(f'    <div><h3>{T(*h)}</h3><p>{T(*p)}</p></div>' for h, p in tips)}
  </div>
</div></section>

<section class="price" id="price"><div class="wrap">
  <div>
    <span class="eyebrow" style="color:var(--eye-ink)">{T("С White Irbis","With White Irbis","White Irbis-ի հետ")}</span>
    <div class="big" style="font-size:clamp(44px,6vw,80px)">{T("Пойдём вместе?","Shall we go together?","Գնա՞նք միասին")}</div>
    <ul>
      <li>{T("Подберём вершину под ваш опыт и дни","We'll match a peak to your experience and dates","Կընտրենք գագաթ՝ ըստ ձեր փորձի և օրերի")}</li>
      <li>{T("Транспорт, джип до старта и гид — на нас","Transport, a jeep to the trailhead and a guide — on us","Տրանսպորտ, ջիպ մինչև մեկնարկ և գիդ՝ մեր կողմից")}</li>
    </ul>
  </div>
  <div class="contact">
    <h3>{T("Напишите нам","Message us","Գրեք մեզ")}</h3>
    <p>{T("Скажите, какая гора приглянулась, — предложим дату и план.","Tell us which mountain caught your eye and we'll suggest a date and a plan.","Ասեք, որ լեռն է ձեզ դուր եկել, և կառաջարկենք ամսաթիվ ու պլան։")}</p>
    %%CONTACT%%
  </div>
</div></section>

<footer><div class="wrap">White Irbis · irbis.am · +374 91 470 331<br>{T("Высоты — по данным Armenian Geographic (armgeo.am) и открытым источникам. Фото — архив White Irbis.","Heights from Armenian Geographic (armgeo.am) and public sources. Photos from the White Irbis archive.","Բարձրությունները՝ ըստ Armenian Geographic-ի (armgeo.am) և բաց աղբյուրների։ Լուսանկարները՝ White Irbis-ի արխիվից։")}<br><a href="../tct/">{T("Гайдбук: Транскавказская тропа","Guidebook: Transcaucasian Trail","Ուղեցույց՝ Անդրկովկասյան արահետ")}</a> · <a href="../gaidbuk/">{T("Гайдбук: Скалы Армении","Guidebook: Rocks of Armenia","Ուղեցույց՝ Հայաստանի ժայռերը")}</a></div></footer>
'''
open(f'{H}/gory_body.html', 'w').write(body)
print('ok', len(body))
