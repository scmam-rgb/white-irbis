import os, re
H = os.path.dirname(os.path.abspath(__file__))
def T(ru, en, hy): return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'
def rep(s, a, b):
    assert s.count(a) == 1, a[:70]
    return s.replace(a, b)
guides = open(f'{H}/guides.html').read().strip()

def faq(items):
    out = []
    for i, (q, a) in enumerate(items):
        out.append(f'      <details{" open" if i == 0 else ""}><summary>{T(*q)}</summary><p>{T(*a)}</p></details>')
    return '\n'.join(out)

def sec_faq(title, items):
    return f'''<section class="faq" id="faq"><div class="wrap">
  <span class="eyebrow">{T('Вопросы','Questions','Հարցեր')}</span>
  <h2 class="h2">{T(*title)}</h2>
  <div class="faq-list">
{faq(items)}
  </div>
</div></section>
'''

def sec_ready(eyebrow, title, cards):
    cs = '\n'.join(f'    <div><h3>{T(*h)}</h3><p>{T(*p)}</p></div>' for h, p in cards)
    return f'''<section id="ready"><div class="wrap">
  <span class="eyebrow">{T(*eyebrow)}</span>
  <h2 class="h2">{T(*title)}</h2>
  <div class="who who4">
{cs}
  </div>
</div></section>
'''

# ---------------- ARAGATS ----------------
p = f'{H}/aragats_body.html'; s = open(p).read()
s = rep(s, 'Высшая точка Армении — 4 090 м. От озера Кари через кратер потухшего вулкана и по узкому гребню на вершину. Вечером снова в Ереване.',
        'Высшая точка Армении — 4 090 м. Джип забрасывает нас к старту, дальше пешком по краю кратера и узкому гребню на вершину. Вечером снова в Ереване.')
s = rep(s, 'The highest point in Armenia, 4,090 m. From Lake Kari across the crater of an extinct volcano and up a narrow ridge to the top. Back in Yerevan by evening.',
        'The highest point in Armenia, 4,090 m. A jeep drops us at the start, then we walk along the crater rim and up a narrow ridge to the top. Back in Yerevan by evening.')
s = rep(s, 'Հայաստանի ամենաբարձր կետը՝ 4 090 մ։ Քարի լճից հանգած հրաբխի խառնարանով և նեղ կատարով դեպի գագաթ։ Երեկոյան՝ կրկին Երևանում։',
        'Հայաստանի ամենաբարձր կետը՝ 4 090 մ։ Ջիպը մեզ հասցնում է մեկնարկ, հետո ոտքով՝ խառնարանի եզրով և նեղ կատարով դեպի գագաթ։ Երեկոյան՝ կրկին Երևանում։')
# facts
s = rep(s, '<div><dt><span lang="ru">Старт</span><span lang="en">Start</span><span lang="hy">Մեկնարկ</span></dt><dd><span lang="ru">Озеро Кари, 3 200 м</span><span lang="en">Lake Kari, 3,200 m</span><span lang="hy">Քարի լիճ, 3 200 մ</span></dd></div>',
        f'<div><dt>{T("Заброска","Approach","Մոտեցում")}</dt><dd>{T("На джипе","By jeep","Ջիպով")}</dd></div>')
s = rep(s, '<div><dt><span lang="ru">Набор</span><span lang="en">Elevation gain</span><span lang="hy">Բարձրացում</span></dt><dd><span lang="ru">≈ 900 м</span><span lang="en">≈ 900 m</span><span lang="hy">≈ 900 մ</span></dd></div>',
        f'<div><dt>{T("Сезон","Season","Սեզոն")}</dt><dd>{T("Июнь — октябрь","June — October","Հունիս — հոկտեմբեր")}</dd></div>')
s = rep(s, '<span lang="ru">От 3 человек</span><span lang="en">3 or more</span><span lang="hy">3 հոգուց</span>',
        T('От 2 человек', '2 or more', '2 հոգուց'))
# program
s = rep(s, '<h3><span lang="ru">Утро · К озеру Кари</span><span lang="en">Morning · To Lake Kari</span><span lang="hy">Առավոտ · Դեպի Քարի լիճ</span></h3>',
        f'<h3>{T("Утро · Заброска","Morning · Jeep approach","Առավոտ · Ջիպով մոտեցում")}</h3>')
s = rep(s, '<span lang="ru">Переезд к подножию Арагаца, к озеру Кари на 3 200 м</span><span lang="en">Drive to the foot of Aragats, to Lake Kari at 3,200 m</span><span lang="hy">Ճանապարհ դեպի Արագածի ստորոտ՝ Քարի լիճ, 3 200 մ</span>',
        T('Ранний выезд к Арагацу, пересадка на джип — он забрасывает группу к началу маршрута', 'Early drive to Aragats, then a jeep takes the group up to the start of the route', 'Վաղ մեկնում դեպի Արագած, հետո ջիպը խումբը հասցնում է երթուղու սկիզբ'))
s = rep(s, '<h3><span lang="ru">Вечер · Спуск и Амберд</span><span lang="en">Evening · Descent and Amberd</span><span lang="hy">Երեկո · Վայրէջք և Ամբերդ</span></h3>',
        f'<h3>{T("Вечер · Спуск","Evening · Descent","Երեկո · Վայրէջք")}</h3>')
s = rep(s, '<span lang="ru">Спуск тем же путём к озеру Кари</span><span lang="en">Descent the same way to Lake Kari</span><span lang="hy">Վայրէջք նույն ճանապարհով դեպի Քարի լիճ</span>',
        T('Спуск тем же путём к джипу', 'Descent the same way back to the jeep', 'Վայրէջք նույն ճանապարհով դեպի ջիպ'))
s = rep(s, '<span lang="ru">По дороге — остановка у средневековой крепости Амберд</span><span lang="en">On the way back, a stop at the medieval fortress of Amberd</span><span lang="hy">Ճանապարհին՝ կանգառ միջնադարյան Ամբերդ ամրոցի մոտ</span>',
        T('Джип спускает к машине, ужин по дороге — по желанию', 'The jeep takes us down to the car; dinner on the way if you like', 'Ջիպը մեզ իջեցնում է մեքենայի մոտ, ճանապարհին՝ ընթրիք ցանկության դեպքում'))
s = rep(s, '<span lang="ru">Транспорт Ереван — озеро Кари — Амберд — Ереван</span><span lang="en">Transport Yerevan — Lake Kari — Amberd — Yerevan</span><span lang="hy">Տրանսպորտ Երևան — Քարի լիճ — Ամբերդ — Երևան</span>',
        T('Транспорт из Еревана и обратно', 'Transport from Yerevan and back', 'Տրանսպորտ Երևանից և հետ') + '</li>\n      <li>' + T('Джип-заброска к старту и обратно', 'Jeep approach to the start and back', 'Ջիպով մոտեցում մեկնարկին և հետ'))
s = rep(s, '<span lang="ru">Обед на вершине и вода</span>', '<span lang="ru">Обед-ланчбокс и вода</span>')
s = rep(s, '<li><span lang="ru">Страховка участника</span><span lang="en">Participant insurance</span><span lang="hy">Մասնակցի ապահովագրություն</span></li>',
        '<li><span lang="ru">Верёвка и страховочное снаряжение на гребне</span><span lang="en">Rope and safety gear for the ridge</span><span lang="hy">Պարան և ապահովագրական հանդերձանք կատարի համար</span></li>\n      <li><span lang="ru">Аптечка и связь у гида</span><span lang="en">First-aid kit and communications with the guide</span><span lang="hy">Դեղատուփ և կապ գիդի մոտ</span></li>\n      <li><span lang="ru">Страховка участника</span><span lang="en">Participant insurance</span><span lang="hy">Մասնակցի ապահովագրություն</span></li>')
s = rep(s, '<li><span lang="ru">Треккинговые ботинки</span><span lang="en">Hiking boots</span><span lang="hy">Արշավային կոշիկներ</span></li>',
        '<li><span lang="ru">Треккинговые ботинки с жёсткой подошвой</span><span lang="en">Hiking boots with a stiff sole</span><span lang="hy">Կոշտ ներբանով արշավային կոշիկներ</span></li>\n      <li><span lang="ru">Треккинговые палки — по желанию</span><span lang="en">Trekking poles, if you like</span><span lang="hy">Արշավային ձողեր՝ ցանկության դեպքում</span></li>\n      <li><span lang="ru">Вода 1,5–2 л и перекус</span><span lang="en">1.5–2 l of water and snacks</span><span lang="hy">1,5–2 լ ջուր և նախուտեստ</span></li>')
ready = sec_ready(('Подготовка', 'Preparation', 'Նախապատրաստում'), ('Что нужно знать до выхода', 'What to know before you go', 'Ինչ պետք է իմանալ մինչ ելքը'), [
    (('Форма', 'Fitness', 'Ֆիզիկական վիճակ'), ('Весь день на ногах на высоте 3 500–4 000 м. Нужен опыт походов или регулярные тренировки. Альпинистская техника не нужна.', 'A full day on your feet at 3,500–4,000 m. You need some hiking experience or regular training. No mountaineering skills required.', 'Ամբողջ օրը ոտքի վրա՝ 3 500–4 000 մ բարձրության վրա։ Պետք է արշավների փորձ կամ կանոնավոր մարզումներ։ Ալպինիստական տեխնիկա պետք չէ։')),
    (('Высота', 'Altitude', 'Բարձրություն'), ('Идём в темпе самого медленного участника. Если кому-то плохо от высоты — гид решает, спускаться или ждать.', 'We walk at the pace of the slowest member. If someone feels the altitude, the guide decides whether to descend or wait.', 'Քայլում ենք ամենադանդաղ մասնակցի տեմպով։ Եթե որևէ մեկին բարձրությունը վատ է անդրադառնում, գիդն է որոշում՝ իջնել, թե սպասել։')),
    (('Погода', 'Weather', 'Եղանակ'), ('Наверху погода меняется быстро. Если гроза или сильный ветер — разворачиваемся или переносим дату.', 'Up high the weather changes fast. In a storm or strong wind we turn back or move the date.', 'Վերևում եղանակը արագ է փոխվում։ Ամպրոպի կամ ուժեղ քամու դեպքում հետ ենք դառնում կամ տեղափոխում ամսաթիվը։')),
    (('Гребень', 'The ridge', 'Կատարը'), ('Последний участок узкий. Без снега проходим пешком, со снегом гид провешивает верёвку.', 'The final stretch is narrow. Without snow we walk it; with snow the guide fixes a rope.', 'Վերջին հատվածը նեղ է։ Առանց ձյան անցնում ենք ոտքով, ձյան դեպքում գիդը պարան է ձգում։')),
])
faq_a = sec_faq(('Частые вопросы', 'Frequently asked', 'Հաճախ տրվող հարցեր'), [
    (('Чем Северная отличается от Южной?', 'How is the North peak different from the South?', 'Ինչով է Հյուսիսայինը տարբերվում Հարավայինից'),
     ('Южная (3 879 м) — самый простой путь на Арагац. Северная (4 090 м) — высшая точка Армении: дольше, выше и с узким гребнем в конце.', 'The South peak (3,879 m) is the easiest way up Aragats. The North peak (4,090 m) is the highest point in Armenia: longer, higher, with a narrow ridge at the end.', 'Հարավայինը (3 879 մ) Արագածի ամենահեշտ ճանապարհն է։ Հյուսիսայինը (4 090 մ) Հայաստանի ամենաբարձր կետն է՝ ավելի երկար, ավելի բարձր և վերջում նեղ կատարով։')),
    (('Можно без опыта?', 'Can I go without experience?', 'Կարելի՞ է առանց փորձի'),
     ('Альпинистский опыт не нужен, но нужна выносливость. Если сомневаетесь, напишите нам — подскажем, с чего начать.', 'You don\'t need mountaineering experience, but you do need stamina. If in doubt, message us and we\'ll suggest where to start.', 'Ալպինիստական փորձ պետք չէ, բայց պետք է տոկունություն։ Եթե կասկածում եք, գրեք մեզ՝ կառաջարկենք, թե որտեղից սկսել։')),
    (('Что если погода испортится?', 'What if the weather turns bad?', 'Իսկ եթե եղանակը վատանա'),
     ('Решение принимает гид. Если выход отменяем до старта, переносим на другую дату.', 'The guide makes the call. If we cancel before the start, we move you to another date.', 'Որոշումը կայացնում է գիդը։ Եթե ելքը չեղարկում ենք մինչև մեկնարկը, տեղափոխում ենք այլ ամսաթվի։')),
    (('Можно зимой?', 'Can I go in winter?', 'Կարելի՞ է ձմռանը'),
     ('Да, если позволяет снег: на снегоступах, в зимней одежде, с верёвкой на гребне. Дату подбираем по прогнозу.', 'Yes, if the snow allows: on snowshoes, in winter clothing, with a rope on the ridge. We pick the date by the forecast.', 'Այո, եթե ձյունը թույլ է տալիս՝ ձնագնացներով, ձմեռային հագուստով, կատարին՝ պարանով։ Ամսաթիվը ընտրում ենք ըստ կանխատեսման։')),
])
s = rep(s, '<section class="inc" id="included">', ready + '\n' + '<section class="inc" id="included">')
s = rep(s, '<section class="price" id="price">', guides.replace('<section id="guides">', '<section id="guides" class="gsec">') + '\n\n' + faq_a + '\n<section class="price" id="price">')
s = rep(s, '<span lang="ru">с человека, при группе от 3 человек</span><span lang="en">per person, groups of 3 or more</span><span lang="hy">մեկ անձի համար, 3 հոգուց խմբի դեպքում</span>',
        T('с человека, при группе от 4 человек', 'per person, groups of 4 or more', 'մեկ անձի համար, 4 հոգուց խմբի դեպքում'))
open(p, 'w').write(s)

# ---------------- ARARAT ----------------
p = f'{H}/ararat_body.html'; s = open(p).read()
s = rep(s, '<div><dt><span lang="ru">Уровень</span><span lang="en">Level</span><span lang="hy">Մակարդակ</span></dt><dd><span lang="ru">Без техники</span><span lang="en">Non-technical</span><span lang="hy">Առանց տեխնիկայի</span></dd></div>',
        f'<div><dt>{T("Сезон","Season","Սեզոն")}</dt><dd>{T("Июль — сентябрь","July — September","Հուլիս — սեպտեմբեր")}</dd></div>')
s = rep(s, '<span lang="ru">Из Еревана · 6 дней / 5 ночей · через Турцию</span>', '<span lang="ru">Из Еревана · 6 дней · июль — сентябрь</span>')
s = rep(s, '<span lang="en">From Yerevan · 6 days / 5 nights · via Turkey</span>', '<span lang="en">From Yerevan · 6 days · July — September</span>')
s = rep(s, '<span lang="hy">Երևանից · 6 օր / 5 գիշեր · Թուրքիայով</span>', '<span lang="hy">Երևանից · 6 օր · հուլիս — սեպտեմբեր</span>')
s = rep(s, '<li><span lang="ru">Гид White Irbis</span><span lang="en">A White Irbis guide</span><span lang="hy">White Irbis-ի գիդ</span></li>',
        T('Гид White Irbis всю поездку и местная команда на горе: гиды и повар', 'A White Irbis guide for the whole trip, plus the local team on the mountain: guides and a cook', 'White Irbis-ի գիդ ամբողջ ճանապարհորդության ընթացքում և տեղական թիմ լեռան վրա՝ գիդեր և խոհարար').join(['<li>', '</li>']) + '\n      <li>' + T('Разрешение на восхождение', 'Climbing permit', 'Վերելքի թույլտվություն') + '</li>')
s = rep(s, '<li><span lang="ru">Лошади для багажа</span><span lang="en">Horses for luggage</span><span lang="hy">Ձիեր ուղեբեռի համար</span></li>',
        '<li><span lang="ru">Лошади для багажа</span><span lang="en">Horses for luggage</span><span lang="hy">Ձիեր ուղեբեռի համար</span></li>\n      <li>' + T('Кошки на время восхождения', 'Crampons for the climb', 'Կատվաճանկեր վերելքի ընթացքում') + '</li>')
s = rep(s, '<li><span lang="ru">Страховка участника</span><span lang="en">Participant insurance</span><span lang="hy">Մասնակցի ապահովագրություն</span></li>',
        '<li>' + T('Страховка участника с покрытием высоты до 5 200 м', 'Participant insurance covering altitudes up to 5,200 m', 'Մասնակցի ապահովագրություն՝ մինչև 5 200 մ բարձրության ծածկույթով') + '</li>')
s = rep(s, '<li><span lang="ru">Трансфер из аэропорта</span><span lang="en">Airport transfer</span><span lang="hy">Տրանսֆեր օդանավակայանից</span></li>',
        '<li>' + T('Перелёт до Еревана', 'Flights to Yerevan', 'Թռիչք մինչև Երևան') + '</li>\n      <li>' + T('Входные билеты: Ани, дворец Исхак-паши', 'Entrance tickets: Ani, Ishak Pasha Palace', 'Մուտքի տոմսեր՝ Անի, Իսհակ փաշայի պալատ') + '</li>')
ready = sec_ready(('Подготовка', 'Preparation', 'Նախապատրաստում'), ('До выезда', 'Before you go', 'Մինչ մեկնելը'), [
    (('Форма', 'Fitness', 'Ֆիզիկական վիճակ'), ('Техника не нужна, но штурм — 10–12 часов на высоте за 4 000 м. За 2–3 месяца до поездки — регулярный бег, лестницы или походы с рюкзаком.', 'No technical skills, but summit day is 10–12 hours above 4,000 m. Start training 2–3 months ahead: regular running, stairs or hikes with a pack.', 'Տեխնիկա պետք չէ, բայց գրոհը 10–12 ժամ է 4 000 մ-ից բարձր։ Ճանապարհորդությունից 2–3 ամիս առաջ՝ կանոնավոր վազք, աստիճաններ կամ արշավներ ուսապարկով։')),
    (('Документы', 'Documents', 'Փաստաթղթեր'), ('Загранпаспорт со сроком больше полугода. Разрешение на восхождение оформляем мы — копию паспорта пришлите при бронировании. Про визу в Турцию для вашего гражданства подскажем.', 'A passport valid for over six months. We arrange the climbing permit — send a passport copy when you book. We\'ll advise on a Turkish visa for your citizenship.', 'Վեց ամսից ավելի վավերական անձնագիր։ Վերելքի թույլտվությունը ձևակերպում ենք մենք՝ անձնագրի պատճենը ուղարկեք ամրագրելիս։ Թուրքական վիզայի հարցում կօգնենք՝ ըստ ձեր քաղաքացիության։')),
    (('Снаряжение', 'Gear', 'Հանդերձանք'), ('Ботинки под кошки, спальник комфорт −10 °C, пуховка, мембрана, тёплые перчатки, налобный фонарь, очки 3–4 категории, палки. Полный список пришлём.', 'Crampon-compatible boots, a sleeping bag rated to −10 °C comfort, a down jacket, a waterproof shell, warm gloves, a headlamp, category 3–4 sunglasses, poles. We\'ll send the full list.', 'Կատվաճանկի համար կոշիկներ, −10 °C հարմարավետության քնապարկ, բմբուլե բաճկոն, թաղանթային շերտ, տաք ձեռնոցներ, ճակատի լապտեր, 3–4 կարգի ակնոց, ձողեր։ Ամբողջական ցանկը կուղարկենք։')),
    (('Высота', 'Altitude', 'Բարձրություն'), ('Акклиматизация встроена в программу, плюс Арагац до выезда. На штурме гид может развернуть любого, кому плохо, — безопасность важнее вершины.', 'Acclimatisation is built into the programme, plus Aragats before we leave. On summit day the guide may turn back anyone unwell — safety comes before the summit.', 'Կլիմայավարժումը ներառված է ծրագրում, գումարած Արագածը մեկնելուց առաջ։ Գրոհի ժամանակ գիդը կարող է հետ ուղարկել յուրաքանչյուրին, ով իրեն վատ է զգում. անվտանգությունն ավելի կարևոր է, քան գագաթը։')),
])
faq_r = sec_faq(('Частые вопросы', 'Frequently asked', 'Հաճախ տրվող հարցեր'), [
    (('Почему через Турцию и Грузию?', 'Why via Turkey and Georgia?', 'Ինչու՞ Թուրքիայով և Վրաստանով'),
     ('Арарат стоит на территории Турции, а армяно-турецкая граница закрыта. Поэтому едем через Грузию — дорога занимает день в каждую сторону.', 'Ararat is in Turkey, and the Armenian–Turkish border is closed. So we drive through Georgia — a day each way.', 'Արարատը Թուրքիայի տարածքում է, իսկ հայ-թուրքական սահմանը փակ է։ Ուստի գնում ենք Վրաստանով՝ ճանապարհը մեկական օր է յուրաքանչյուր ուղղությամբ։')),
    (('Нужен альпинистский опыт?', 'Do I need mountaineering experience?', 'Պե՞տք է ալպինիստական փորձ'),
     ('Нет. Ходить в кошках научим в штурмовом лагере. Но нужна хорошая выносливость — лучше заранее сходить на Арагац или другую высокую гору.', 'No. We teach crampon walking at high camp. But you need good stamina — ideally climb Aragats or another high peak beforehand.', 'Ոչ։ Կատվաճանկերով քայլել կսովորեցնենք գրոհային ճամբարում։ Բայց պետք է լավ տոկունություն՝ ավելի լավ է նախապես բարձրանալ Արագած կամ այլ բարձր լեռ։')),
    (('Что если я не дойду до вершины?', 'What if I can\'t reach the summit?', 'Իսկ եթե չհասնեմ գագաթին'),
     ('С вами спустится один из гидов, остальные продолжат. Дальше программа общая для всех.', 'One of the guides will go down with you while the others carry on. After that the programme is the same for everyone.', 'Գիդերից մեկը ձեզ հետ կիջնի, մյուսները կշարունակեն։ Հետո ծրագիրը բոլորի համար նույնն է։')),
    (('Где спим на горе?', 'Where do we sleep on the mountain?', 'Որտեղ ենք քնում լեռան վրա'),
     ('В палатках в лагерях на 3 200 и 4 200 м. Палатки и коврики даём, спальник — свой. Готовит повар.', 'In tents at the 3,200 m and 4,200 m camps. We provide tents and mats; bring your own sleeping bag. A cook prepares the meals.', 'Վրաններում՝ 3 200 և 4 200 մ ճամբարներում։ Վրաններն ու ներքնակները տալիս ենք, քնապարկը՝ ձերը։ Ճաշը պատրաստում է խոհարարը։')),
    (('Можно присоединиться одному?', 'Can I join on my own?', 'Կարելի՞ է միանալ մենակ'),
     ('Да. Собираем сборные группы на летние даты — напишите, и мы скажем, сколько уже записалось.', 'Yes. We put together mixed groups for summer dates — message us and we\'ll tell you how many have signed up.', 'Այո։ Ամառային ամսաթվերի համար հավաքում ենք խառը խմբեր՝ գրեք մեզ, և կասենք, քանի հոգի է արդեն գրանցվել։')),
])
s = rep(s, '<section class="inc" id="included">', ready + '\n' + '<section class="inc" id="included">')
s = rep(s, '<section class="price" id="price">', guides.replace('<section id="guides">', '<section id="guides" class="gsec">') + '\n\n' + faq_r + '\n<section class="price" id="price">')
open(p, 'w').write(s)

# build css additions
b = open(f'{H}/build.py').read()
if '.who4' not in b:
    b = b.replace(".price .big{font-size", """.who4{grid-template-columns:repeat(4,1fr)}@media (max-width:960px){.who4{grid-template-columns:1fr 1fr}}@media (max-width:600px){.who4{grid-template-columns:1fr}}
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
.price .big{font-size""", 1)
    open(f'{H}/build.py', 'w').write(b)
print('ok')
