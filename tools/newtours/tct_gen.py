import os
H = os.path.dirname(os.path.abspath(__file__))
def T(ru, en, hy): return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'
def L(*a): return T(*a)

regions = [
 # (num, name, terrain, highlights, towns, note, stats, img, alt)
 ('01', ('Ширак','Shirak','Շիրակ'),
  ('Старт у озера Арпи на севере Армении. Высокое плато: болота, луга, безлесная степь и холмы, в основном грунтовки — идти несложно, но холодно и ветрено.',
   'The start at Lake Arpi in the far north of Armenia. A high plateau of wetlands, meadows, treeless steppe and hills, mostly on dirt tracks — easy walking, but cold and windy.',
   'Մեկնարկ Արփի լճից՝ Հայաստանի հյուսիսում։ Բարձր սարահարթ՝ ճահիճներ, մարգագետիններ, անտառազուրկ տափաստան և բլուրներ, հիմնականում գրունտային ճանապարհներ. քայլելը հեշտ է, բայց ցուրտ ու քամոտ։'),
  ('Нацпарк «Озеро Арпи», летние цветы, мегалиты у Арташена. Один из самых малопосещаемых уголков Армении.',
   'Lake Arpi National Park, summer wildflowers, megaliths near Hartashen. One of the least visited corners of Armenia.',
   '«Արփի լիճ» ազգային պարկ, ամառային ծաղիկներ, մեգալիթներ Հարթաշենի մոտ։ Հայաստանի ամենաքիչ այցելվող անկյուններից մեկը։'),
  None,
  ('Проход по нацпарку «Озеро Арпи» — с регистрацией заранее.','Lake Arpi National Park asks hikers to register in advance.','«Արփի լիճ» ազգային պարկով անցնելու համար պետք է նախապես գրանցվել։'),
  None, None, None),
 ('02', ('Лори','Lori','Լոռի'),
  ('Лесистые хребты и долины, тропы по каньонам Дзорагета и Дебеда, затем выход выше леса.',
   'Forested ridges and farm valleys, trails through the Dzoraget and Debed canyons, then up above the treeline.',
   'Անտառապատ լեռնաշղթաներ և հովիտներ, արահետներ Ձորագետի և Դեբեդի կիրճերով, հետո՝ անտառի գոտուց վեր։'),
  ('Сосновые леса и дендропарк у Степанавана, каменная лестница Кобайра, Одзун, Санаин (ЮНЕСКО). В Дебеде открыто больше 100 км новых троп.',
   'Pine forests and the arboretum near Stepanavan, the Kobayr stone staircase, Odzun, Sanahin (UNESCO). Over 100 km of new trails have opened in the Debed canyon.',
   'Սոճու անտառներ և դենդրոպարկ Ստեփանավանի մոտ, Քոբայրի քարե աստիճաններ, Օձուն, Սանահին (ՅՈՒՆԵՍԿՕ)։ Դեբեդի կիրճում բացվել է ավելի քան 100 կմ նոր արահետ։'),
  ('Степанаван, Алаверди','Stepanavan, Alaverdi','Ստեփանավան, Ալավերդի'),
  ('Самый длинный безлюдный отрезок севера — около 86 км под горой Джарсар: 3–4 дня без магазинов.',
   'The longest remote stretch in the north — about 86 km below Mt Dzharsar: 3–4 days without shops.',
   'Հյուսիսի ամենաերկար ամայի հատվածը՝ մոտ 86 կմ Ջարսար լեռան տակ. 3–4 օր առանց խանութների։'),
  None, None, None),
 ('03', ('Тавуш и Дилижан','Tavush & Dilijan','Տավուշ և Դիլիջան'),
  ('Высокогорные грунтовки и пастушьи тропы, скалы Иджеванского хребта, лесные тропы вокруг Дилижана и озера Парз.',
   'Highland tracks and shepherd paths, the cliffs of the Ijevan range, forest trails around Dilijan and Lake Parz.',
   'Բարձրլեռնային ճանապարհներ և հովվական արահետներ, Իջևանի լեռնաշղթայի ժայռեր, անտառային արահետներ Դիլիջանի և Պարզ լճի շուրջ։'),
  ('Нацпарк «Дилижан»: Агарцин, Гошаванк, озеро Гош. Участок по нацпарку — около 80 км, 4–5 дней, размечен красно-белым.',
   'Dilijan National Park: Haghartsin, Goshavank, Lake Gosh. The national park stretch is about 80 km, 4–5 days, waymarked in red and white.',
   '«Դիլիջան» ազգային պարկ՝ Հաղարծին, Գոշավանք, Գոշի լիճ։ Ազգային պարկի հատվածը մոտ 80 կմ է, 4–5 օր, նշագծված կարմիր-սպիտակ։'),
  ('Дилижан','Dilijan','Դիլիջան'),
  ('Один хребет не размечен и зарос — местами придётся продираться через кусты.','One ridge is unmarked and overgrown — expect some bushwhacking.','Մի լեռնաշղթա նշագծված չէ և խիտ բուսականությամբ է՝ տեղ-տեղ ստիպված կլինեք ճեղքել թփերը։'),
  ('80 км · 4–5 дней','80 km · 4–5 days','80 կմ · 4–5 օր'), 'trail_group.jpg', 'Группа White Irbis на лесной тропе Дилижана'),
 ('04', ('Гегамский хребет','Gegham Mountains','Գեղամա լեռներ'),
  ('Самая высокая и дикая часть: от Севана на вулканическое плато. Часто без тропы — осыпи, курумы, застывшая лава, кочевья пастухов.',
   'The highest and wildest part: from Sevan up onto the volcanic plateau. Often no trail at all — scree, boulder fields, old lava flows and shepherd camps.',
   'Ամենաբարձր և վայրի հատվածը՝ Սևանից դեպի հրաբխային սարահարթ։ Հաճախ առանց արահետի՝ քարաթափեր, քարակույտեր, սառած լավա, հովիվների վրաններ։'),
  ('Кратерные озёра, Аждаак (≈3 600 м), в ясный день — Арарат.',
   'Crater lakes, Mt Azhdahak (≈3,600 m) and, on a clear day, Ararat.',
   'Խառնարանային լճեր, Աժդահակ (≈3 600 մ), պարզ օրը՝ Արարատը։'),
  ('Севан','Sevan','Սևան'),
  ('С октября по июнь здесь снег — надёжно проходить только в июле–августе. Мало воды, частые грозы.',
   'Snowbound from October to June — only July and August are reliable. Little water, frequent thunderstorms.',
   'Հոկտեմբերից հունիս այստեղ ձյուն է՝ հուսալի է միայն հուլիսին և օգոստոսին։ Քիչ ջուր, հաճախակի ամպրոպներ։'),
  None, None, None),
 ('05', ('Вайоц Дзор','Vayots Dzor','Վայոց Ձոր'),
  ('Скалы, красные каньоны, старинные тропы — расчищенные и размеченные — и грунтовки между виноградниками.',
   'Cliffs, red canyons, cleared and waymarked ancient paths and dirt roads between vineyards.',
   'Ժայռեր, կարմիր կիրճեր, մաքրված և նշագծված հնագույն արահետներ, գրունտային ճանապարհներ խաղողի այգիների միջև։'),
  ('Нораванк, караван-сарай Селим, винодельни Арени. Для дня отдыха — кемпинг под Ехегнадзором.',
   'Noravank, Selim caravanserai, the wineries of Areni. Campsites near Yeghegnadzor for a rest day.',
   'Նորավանք, Սելիմի քարավանատուն, Արենիի գինեգործարաններ։ Հանգստի օրվա համար՝ ճամբար Եղեգնաձորի մոտ։'),
  ('Ехегнадзор','Yeghegnadzor','Եղեգնաձոր'),
  ('В 2025 году маршрут увели от Джермука: у границы усилилось военное присутствие. Идите по актуальной карте TCT.',
   'In 2025 the route was moved away from Jermuk because of increased military presence near the border. Follow the current TCT map.',
   '2025 թ. երթուղին հեռացվեց Ջերմուկից՝ սահմանի մոտ ռազմական ներկայության աճի պատճառով։ Հետևեք TCT-ի ընթացիկ քարտեզին։'),
  None, 'canyon_sunset.jpg', 'Ущелье Вайоц Дзора на закате'),
 ('06', ('Сюник','Syunik','Սյունիք'),
  ('Луга, глубокие каньоны, альпийские скалы и сухие склоны. В основном старинные тропы; большая часть совпадает с «Тропой легенд».',
   'Grasslands, deep canyons, alpine rock and dry slopes. Mostly ancient footpaths; much of it follows the Legends Trail.',
   'Մարգագետիններ, խոր կիրճեր, ալպյան ժայռեր և չոր լանջեր։ Հիմնականում հնագույն արահետներ, մեծ մասը համընկնում է «Լեգենդների արահետի» հետ։'),
  ('Татев над ущельем Воротан, водопад Шаки, гора Хуступ, пещерные сёла.',
   'Tatev above the Vorotan gorge, Shaki waterfall, Mt Khustup, cave villages.',
   'Տաթևը Որոտանի կիրճի վրա, Շաքիի ջրվեժ, Խուստուփ լեռ, քարանձավային գյուղեր։'),
  ('Сисиан, Горис, Капан','Sisian, Goris, Kapan','Սիսիան, Գորիս, Կապան'),
  ('Гадюки. В заповеднике Шикаог ставить палатку нельзя.','Vipers. Wild camping is forbidden in Shikahogh Reserve.','Իժեր։ Շիկահողի արգելոցում վրան խփել չի կարելի։'),
  ('≈150 км · 8–12 дней','≈150 km · 8–12 days','≈150 կմ · 8–12 օր'), None, None),
 ('07', ('Аревик и Мегри','Arevik & Meghri','Արևիկ և Մեղրի'),
  ('Финиш на юге Армении: горная полупустыня нацпарка «Аревик» и спуск к Мегри.',
   'The finish in the far south of Armenia: the mountain semi-desert of Arevik National Park and the descent to Meghri.',
   'Ավարտ Հայաստանի հարավում՝ «Արևիկ» ազգային պարկի լեռնային կիսաանապատ և վայրէջք դեպի Մեղրի։'),
  ('Самая глухая и трудная часть Армении. С юга на север идти тяжелее, чем наоборот.',
   'The remotest and toughest part of Armenia. Harder going south to north than the other way.',
   'Հայաստանի ամենահեռավոր և դժվար հատվածը։ Հարավից հյուսիս քայլելն ավելի դժվար է, քան հակառակը։'),
  ('Мегри','Meghri','Մեղրի'),
  ('Тропа ещё строится: крутые колючие склоны без тропы. В нацпарке «Аревик» — регистрация заранее.',
   'Still under construction: steep, thorny slopes with no path. Arevik National Park asks hikers to register in advance.',
   'Արահետը դեռ կառուցվում է՝ զառիթափ, փշոտ լանջեր առանց արահետի։ «Արևիկ» ազգային պարկում պետք է նախապես գրանցվել։'),
  None, None, None),
]

def region_card(r):
    num, name, terr, hi, towns, note, stats, img, alt = r
    out = ['<article class="rg">']
    if img:
        out.append(f'<div class="rg-img"><img src="img/{img}" alt="{alt}" loading="lazy"></div>')
    else:
        out.append(f'<div class="rg-img rg-none"><span>{num}</span></div>')
    out.append('<div class="rg-b">')
    out.append(f'<div class="rg-h"><b>{num}</b><h3>{T(*name)}</h3></div>')
    if stats: out.append(f'<div class="stats"><span>{T(*stats)}</span></div>')
    out.append(f'<p>{T(*terr)}</p>')
    out.append(f'<p class="rg-hi"><i>{T("Смотреть","Highlights","Տեսնել")}</i>{T(*hi)}</p>')
    if towns: out.append(f'<p class="rg-hi"><i>{T("Магазины","Resupply","Խանութներ")}</i>{T(*towns)}</p>')
    out.append(f'<p class="rg-note">{T(*note)}</p>')
    out.append('</div></article>')
    return '\n'.join(out)

# schematic route svg: vertical line with dots
pts = [('Арпи','Arpi','Արփի'),('Ширак','Shirak','Շիրակ'),('Лори','Lori','Լոռի'),('Дилижан','Dilijan','Դիլիջան'),('Севан','Sevan','Սևան'),('Гегам','Gegham','Գեղամ'),('Ехегнадзор','Yeghegnadzor','Եղեգնաձոր'),('Сисиан','Sisian','Սիսիան'),('Татев','Tatev','Տաթև'),('Капан','Kapan','Կապան'),('Мегри','Meghri','Մեղրի')]

def schema():
    rows = []
    for i, p in enumerate(pts):
        cls = ' end' if i in (0, len(pts)-1) else ''
        rows.append(f'<li class="sp{cls}"><span>{T(*p)}</span></li>')
    return f'''<div class="schema" aria-hidden="true"><div class="sch-cap">{T("Север","North","Հյուսիս")}</div><ol>{''.join(rows)}</ol><div class="sch-cap">{T("Юг","South","Հարավ")}</div></div>'''

practical = [
 (('Когда идти','When to go','Երբ գնալ'),
  ('Лучше всего — июнь–сентябрь. С юга на север: примерно с середины мая до конца сентября. С севера на юг: с начала июля до середины октября. Гегамский хребет под снегом с октября по июнь — рассчитывайте пройти его в июле–августе. Летом в низинах бывает за +32 °C.',
   'Best from June to September. Northbound: roughly mid-May to the end of September. Southbound: early July to mid-October. The Gegham range is snowbound from October to June, so plan to cross it in July or August. Low-lying sections can top 32 °C in summer.',
   'Լավագույնը՝ հունիս–սեպտեմբեր։ Հարավից հյուսիս՝ մոտավորապես մայիսի կեսից մինչև սեպտեմբերի վերջ։ Հյուսիսից հարավ՝ հուլիսի սկզբից մինչև հոկտեմբերի կես։ Գեղամա լեռները ձյան տակ են հոկտեմբերից հունիս՝ պլանավորեք անցնել հուլիսին կամ օգոստոսին։ Ամռանը ցածրադիր վայրերում լինում է +32 °C-ից ավելի։')),
 (('Навигация','Navigation','Կողմնորոշում'),
  ('Размечено около трети пути — красно-белыми метками и указателями. Остальное — по GPS: треки GPX и KML на сайте TCT, приложения FarOut и Hiiker, бумажные карты 1:25 000 от Cartisan. Офлайн-карты скачайте заранее.',
   'About a third of the route is waymarked with red-and-white blazes and signposts. The rest is GPS navigation: GPX and KML tracks on the TCT website, the FarOut and Hiiker apps, and Cartisan 1:25,000 paper maps. Download offline maps in advance.',
   'Երթուղու մոտ մեկ երրորդը նշագծված է կարմիր-սպիտակ նշաններով և ցուցանակներով։ Մնացածը՝ GPS-ով. GPX և KML տրեկներ TCT-ի կայքում, FarOut և Hiiker հավելվածներ, Cartisan-ի 1:25 000 թղթային քարտեզներ։ Օֆլայն քարտեզները ներբեռնեք նախապես։')),
 (('Ночёвки','Where to sleep','Գիշերակաց'),
  ('Палатка обязательна. Дикий кемпинг в Армении обычно терпят — почти вся земля общинная, ставьтесь аккуратно. Гестхаусы есть во многих сёлах, платят наличными. В заповеднике Шикаог палатку ставить нельзя.',
   'A tent is essential. Wild camping is widely tolerated in Armenia, as most land is community-owned — camp considerately. Many villages have guesthouses, paid in cash. Camping is forbidden in Shikahogh Reserve.',
   'Վրանը պարտադիր է։ Վայրի ճամբարումը Հայաստանում սովորաբար հանդուրժվում է՝ հողի մեծ մասը համայնքային է, տեղավորվեք զգույշ։ Շատ գյուղերում կան հյուրատներ, վճարում են կանխիկ։ Շիկահողի արգելոցում վրան խփել չի կարելի։')),
 (('Еда и вода','Food & water','Սնունդ և ջուր'),
  ('Супермаркеты — каждые 50–100 км: Мегри, Капан, Горис, Сисиан, Ехегнадзор, Севан, Дилижан, Алаверди, Степанаван. На глухих участках несите еду до 7 дней. Воды мало, особенно в Гегаме: берите запас на несколько литров и фильтр.',
   'Supermarkets every 50–100 km: Meghri, Kapan, Goris, Sisian, Yeghegnadzor, Sevan, Dilijan, Alaverdi, Stepanavan. Carry up to 7 days of food on remote stretches. Water is scarce, especially in the Geghams — carry several litres and a filter.',
   'Սուպերմարկետներ՝ յուրաքանչյուր 50–100 կմ. Մեղրի, Կապան, Գորիս, Սիսիան, Եղեգնաձոր, Սևան, Դիլիջան, Ալավերդի, Ստեփանավան։ Ամայի հատվածներում վերցրեք մինչև 7 օրվա սնունդ։ Ջուրը քիչ է, հատկապես Գեղամում՝ վերցրեք մի քանի լիտր և ֆիլտր։')),
 (('Разрешения','Permits','Թույլտվություններ'),
  ('Для большей части пути разрешения не нужны. В нацпарках «Аревик» и «Озеро Арпи» нужна регистрация заранее, в некоторых парках — небольшой сбор.',
   'Most of the route needs no permit. Arevik and Lake Arpi national parks ask for advance registration; some parks charge a small fee.',
   'Երթուղու մեծ մասի համար թույլտվություն պետք չէ։ «Արևիկ» և «Արփի լիճ» ազգային պարկերում պետք է նախապես գրանցվել, որոշ պարկերում՝ փոքր վճար։')),
 (('Риски','Hazards','Ռիսկեր'),
  ('Пастушьи собаки, грозы с молниями, броды через холодные реки, размытые мосты, борщевик, гадюки, заросшие тропы. Спасатели и медицина на большей части пути далеко — идите со страховкой и сообщайте маршрут близким.',
   'Livestock guard dogs, lightning storms, cold river fords, washed-out bridges, giant hogweed, vipers and overgrown paths. Rescue and medical help are far away on most of the route — get insurance and share your plan with someone.',
   'Հովվական շներ, կայծակով ամպրոպներ, սառը գետերի անցումներ, քանդված կամուրջներ, խոզաղբյուր, իժեր, խիտ բուսականությամբ արահետներ։ Փրկարարներն ու բժշկական օգնությունը մեծ մասամբ հեռու են՝ ունեցեք ապահովագրություն և ձեր երթուղին հայտնեք մտերիմներին։')),
 (('Как добраться','Getting there','Ինչպես հասնել'),
  ('Прилёт в Ереван. На юг — маршрутка Ереван — Мегри, около 9 часов. На север — автобус до Гюмри и такси до озера Арпи. Билеты на маршрутки обычно бронируют по телефону.',
   'Fly into Yerevan. For the south — the Yerevan–Meghri minibus, about 9 hours. For the north — a bus to Gyumri and a taxi to Lake Arpi. Minibus seats are usually booked by phone.',
   'Ժամանում Երևան։ Դեպի հարավ՝ Երևան–Մեղրի երթուղային տաքսի, մոտ 9 ժամ։ Դեպի հյուսիս՝ ավտոբուս մինչև Գյումրի և տաքսի մինչև Արփի լիճ։ Երթուղայինների տեղերը սովորաբար ամրագրում են հեռախոսով։')),
 (('Деньги и связь','Money & mobile','Գումար և կապ'),
  ('Банкоматы — только в крупных городах, в сёлах нужны наличные драмы. Местная SIM-карта с безлимитным интернетом стоит недорого — для оформления нужен паспорт.',
   'ATMs only in larger towns; villages run on cash drams. A local SIM card with unlimited data is cheap — bring your passport to register it.',
   'Բանկոմատներ՝ միայն խոշոր քաղաքներում, գյուղերում պետք են կանխիկ դրամ։ Տեղական SIM քարտը անսահմանափակ ինտերնետով էժան է՝ ձևակերպման համար պետք է անձնագիր։')),
]

def prac():
    return '\n'.join(f'    <div><h3>{T(*h)}</h3><p>{T(*p)}</p></div>' for h, p in practical)

svaneti = [('Чубери — Накра','Chuberi — Nakra','Չուբերի — Նակրա','27','2 300'),('Накра — Бечо','Nakra — Becho','Նակրա — Բեչո','35','2 400'),('Бечо — Местиа','Becho — Mestia','Բեչո — Մեստիա','21','1 600'),('Местиа — Адиши','Mestia — Adishi','Մեստիա — Ադիշի','28','2 000'),('Адиши — Ушгули','Adishi — Ushguli','Ադիշի — Ուշգուլի','29','1 400')]

def sv():
    rows = ''.join(f'<tr><td>{T(a,b,c)}</td><td>{km}</td><td>↑ {up}</td></tr>' for a,b,c,km,up in svaneti)
    return f'<table class="tb"><thead><tr><th>{T("Этап","Stage","Փուլ")}</th><th>{T("км","km","կմ")}</th><th>{T("Набор, м","Gain, m","Բարձրացում, մ")}</th></tr></thead><tbody>{rows}</tbody></table>'

surface = [(29, ('Тропа','Footpath','Արահետ')), (44, ('Грунтовки','Dirt roads','Գրունտային ճանապարհ')), (11, ('Без тропы','Off-trail','Առանց արահետի')), (14, ('Асфальт и сёла','Roads & villages','Ասֆալտ և գյուղեր'))]
def surf():
    bars = ''.join(f'<span class="sf sf{i}" style="flex:{p}"><b>{p}%</b></span>' for i, (p, _) in enumerate(surface))
    leg = ''.join(f'<li><i class="sf{i}"></i>{T(*n)} — {p}%</li>' for i, (p, n) in enumerate(surface))
    return f'<div class="sfbar">{bars}</div><ul class="sfleg">{leg}</ul>'

body = f'''<header class="top"><div class="wrap">
  <a class="lockup" href="../"><img src="img/logo.png" alt="White Irbis"><span class="sl"><span class="s1">Follow the</span><span class="s2">White <b>Irbis</b></span></span></a>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-l="ru" aria-pressed="true">RU</button><button type="button" data-l="en" aria-pressed="false">EN</button><button type="button" data-l="hy" aria-pressed="false">ARM</button></div>
</div></header>

<section class="hero" id="top">
  <div class="hero-media" aria-hidden="true"><img src="img/hero.jpg" alt="" style="object-position:50% 50%"></div>
  <div class="wrap">
    <span class="alt">{T("Гайдбук · Армения · 819 км","Guidebook · Armenia · 819 km","Ուղեցույց · Հայաստան · 819 կմ")}</span>
    <h1>{T("Транскавказская<br><em>тропа</em>","Transcaucasian<br><em>Trail</em>","Անդրկովկասյան<br><em>արահետ</em>")}</h1>
    <p class="sub">{T("819 км пешком через всю Армению — от озера Арпи на севере до Мегри у Аракса. Что ждёт на каждом участке, когда идти, где спать и как не потеряться.","819 km on foot across the whole of Armenia — from Lake Arpi in the north to Meghri on the Araks. What to expect on each section, when to go, where to sleep and how not to get lost.","819 կմ ոտքով ամբողջ Հայաստանով՝ հյուսիսում գտնվող Արփի լճից մինչև Արաքսի ափին գտնվող Մեղրի։ Ինչ է սպասվում յուրաքանչյուր հատվածում, երբ գնալ, որտեղ քնել և ինչպես չմոլորվել։")}</p>
    <div class="row"><a class="cta" href="#sections">{T("Смотреть участки","See the sections","Տեսնել հատվածները")}</a></div>
  </div>
</section>

<section class="facts"><div class="wrap"><dl>
  <div><dt>{T("В Армении","In Armenia","Հայաստանում")}</dt><dd>{T("819 км","819 km","819 կմ")}</dd></div>
  <div><dt>{T("Регионов","Regions","Մարզեր")}</dt><dd>7</dd></div>
  <div><dt>{T("Высшая точка","Highest point","Ամենաբարձր կետ")}</dt><dd>{T("≈ 3 470 м","≈ 3,470 m","≈ 3 470 մ")}</dd></div>
  <div><dt>{T("Сезон","Season","Սեզոն")}</dt><dd>{T("Июнь — сентябрь","June — September","Հունիս — սեպտեմբեր")}</dd></div>
</dl></div></section>

<section id="about"><div class="wrap ab">
  <div>
    <span class="eyebrow">{T("Что это за тропа","About the trail","Ինչ արահետ է")}</span>
    <h2 class="h2">{T("Тропа через всю Армению","A trail across all of Armenia","Արահետ ամբողջ Հայաստանով")}</h2>
    <p class="lead">{T("Транскавказская тропа (TCT) — длинный пеший маршрут по Кавказу. С 2016 года её строят волонтёры: соединяют старые пастушьи тропы, караванные пути и дороги между монастырями.","The Transcaucasian Trail (TCT) is a long-distance hiking route across the Caucasus. Since 2016 volunteers have been building it by linking old shepherd paths, caravan routes and roads between monasteries.","Անդրկովկասյան արահետը (TCT) երկար քայլարշավային երթուղի է Կովկասով։ 2016 թվականից կամավորները կառուցում են այն՝ միացնելով հին հովվական արահետները, քարավանային ուղիները և վանքերի միջև ճանապարհները։")}</p>
    <p class="lead">{T("Армянский участок открыли первым — в декабре 2021 года. Это самая полная национальная часть тропы: от границы до границы.","The Armenian section opened first, in December 2021. It is the most complete national part of the trail: border to border.","Հայկական հատվածը բացվեց առաջինը՝ 2021 թ. դեկտեմբերին։ Սա արահետի ամենաամբողջական ազգային հատվածն է՝ սահմանից սահման։")}</p>
    <h3 class="sh3">{T("Из чего состоит путь","What's underfoot","Ինչից է բաղկացած ճանապարհը")}</h3>
    {surf()}
  </div>
  {schema()}
</div></section>

<section id="sections" class="sec-rg"><div class="wrap">
  <span class="eyebrow">{T("Армения · с севера на юг","Armenia · north to south","Հայաստան · հյուսիսից հարավ")}</span>
  <h2 class="h2">{T("Семь регионов","Seven regions","Յոթ մարզ")}</h2>
  <p class="lead">{T("Идти можно в обе стороны. Километры по участкам — ориентир: маршрут уточняют каждый сезон.","You can walk it either way. Section distances are a guide: the route is refined every season.","Կարելի է քայլել երկու ուղղությամբ։ Հատվածների կիլոմետրերը կողմնորոշիչ են՝ երթուղին ճշգրտվում է յուրաքանչյուր սեզոն։")}</p>
  <div class="rgs">
{chr(10).join(region_card(r) for r in regions)}
  </div>
</div></section>

<section id="walking" class="gal-sec"><div class="wrap">
  <span class="eyebrow">{T("На тропе","On the trail","Արահետին")}</span>
  <h2 class="h2">{T("Так это выглядит","What it looks like","Ահա թե ինչպես է դա")}</h2>
  <div class="gal3">
    <figure><img src="img/walk_gorge.jpg" alt="Группа с рюкзаками идёт по тропе в красном ущелье" loading="lazy"></figure>
    <figure><img src="img/walk_plateau.jpg" alt="Две участницы с палками идут по плато, вдали Арарат" loading="lazy"></figure>
    <figure><img src="img/walk_ridge.jpg" alt="Группа идёт по каменистому гребню" loading="lazy"></figure>
  </div>
  <p class="credit">{T("Фото с выходов White Irbis","Photos from White Irbis trips","Լուսանկարներ White Irbis-ի ելքերից")}</p>
</div></section>

<section class="inc" id="practical"><div class="wrap">
  <span class="eyebrow">{T("Практика","Practicalities","Գործնական")}</span>
  <h2 class="h2">{T("Перед выходом","Before you set off","Մինչ ճանապարհ ընկնելը")}</h2>
  <div class="prac">
{prac()}
  </div>
</div></section>

<section class="next" id="with-us"><div class="wrap">
  <figure style="margin:0"><img src="img/forest.jpg" alt="Лесная тропа в национальном парке Дилижан" loading="lazy" style="aspect-ratio:4/3"></figure>
  <div>
    <span class="eyebrow">{T("С White Irbis","With White Irbis","White Irbis-ի հետ")}</span>
    <h2 class="h2">{T("Пройти кусок тропы с нами","Walk a piece of it with us","Անցնել արահետի մի մասը մեզ հետ")}</h2>
    <p class="lead">{T("Участки TCT уже входят в наши туры: лесная тропа от озера Парз к Гошаванку в «Армении пешком» и тропа к Амагу в «Скалах и вулканах». Если хотите пройти отрезок целиком — поможем подобрать участок, заброску, ночёвки и гида.","Sections of the TCT are already part of our tours: the forest trail from Lake Parz to Goshavank in Armenia on Foot and the trail to Amaghu in Rocks and Volcanoes. If you want to walk a whole section, we'll help you choose it and arrange transfers, overnights and a guide.","TCT-ի հատվածներն արդեն մեր տուրերում են՝ անտառային արահետը Պարզ լճից Գոշավանք «Հայաստան ոտքով» տուրում և արահետը դեպի Ամաղու «Ժայռեր և հրաբուխներ» տուրում։ Եթե ցանկանում եք անցնել մի ամբողջ հատված՝ կօգնենք ընտրել այն, կազմակերպել տեղափոխումը, գիշերակացը և գիդ։")}</p>
    <p class="lead"><a href="../trekking/">{T("Армения пешком →","Armenia on Foot →","Հայաստան ոտքով →")}</a> &nbsp; <a href="../skaly-i-vulkan/">{T("Скалы и вулканы →","Rocks and Volcanoes →","Ժայռեր և հրաբուխներ →")}</a></p>
  </div>
</div></section>

<section class="price" id="price"><div class="wrap">
  <div>
    <span class="eyebrow" style="color:var(--eye-ink)">{T("Спросить","Ask us","Հարցնել")}</span>
    <div class="big" style="font-size:clamp(44px,6vw,80px)">{T("Планируете тропу?","Planning the trail?","Պլանավորո՞ւմ եք արահետը")}</div>
    <ul>
      <li>{T("Подскажем, какой участок выбрать под ваши дни и форму","We'll suggest a section for your time and fitness","Կառաջարկենք հատված՝ ըստ ձեր օրերի և ֆիզիկական վիճակի")}</li>
      <li>{T("Организуем заброску, ночёвки и гида","We can arrange transfers, overnights and a guide","Կկազմակերպենք տեղափոխում, գիշերակաց և գիդ")}</li>
    </ul>
  </div>
  <div class="contact">
    <h3>{T("Напишите нам","Message us","Գրեք մեզ")}</h3>
    <p>{T("Расскажите, сколько у вас дней и какой участок интересен.","Tell us how many days you have and which section interests you.","Պատմեք, քանի օր ունեք և որ հատվածն է ձեզ հետաքրքրում։")}</p>
    %%CONTACT%%
  </div>
</div></section>

<footer><div class="wrap">White Irbis · irbis.am · +374 91 470 331<br>{T("Данные: ","Sources: ","Աղբյուրներ՝ ")}<a href="https://transcaucasiantrail.org" target="_blank" rel="noopener">transcaucasiantrail.org</a>, Lonely Planet, National Geographic (2026). {T("Маршрут меняется каждый сезон — перед выходом сверяйтесь с картой TCT. Схема на странице — не в масштабе. Фото — архив White Irbis.","The route changes every season — check the TCT map before you go. The diagram on this page is not to scale. Photos from the White Irbis archive.","Երթուղին փոխվում է յուրաքանչյուր սեզոն՝ մեկնելուց առաջ ստուգեք TCT-ի քարտեզը։ Էջի սխեման մասշտաբային չէ։ Լուսանկարները՝ White Irbis-ի արխիվից։")}<br><a href="../gaidbuk/">{T("Ещё гайдбук: «Скалы Армении»","Another guidebook: Rocks of Armenia","Եվս մեկ ուղեցույց՝ «Հայաստանի ժայռերը»")}</a></div></footer>
'''
open(f'{H}/tct_body.html', 'w').write(body)
print('ok', len(body))
