"""Builds aragats-yug/ (South peak) and aragats-zapad/ (West peak) from the live aragats/index.html
(North peak), keeping the exact page style. Run: python3 tools/newtours/aragats_sw_gen.py"""
import re, os, json, shutil
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = open(f'{R}/aragats/index.html', encoding='utf-8').read()

def tri(ru, en, hy):
    return (ru, en, hy)

# ---------- shared texts ----------
COMMON = {
 'Из Еревана · 1 день · июнь — октябрь': None,  # per page
 'Заброска': tri('Старт', 'Start', 'Մեկնարկ'),
 'Джип до водопада': tri('Озеро Кари, 3 200 м', 'Lake Kari, 3,200 m', 'Քարի լիճ, 3 200 մ'),
 'Утро · Заброска': tri('Утро · Дорога к озеру', 'Morning · Drive to the lake', 'Առավոտ · Ճանապարհ դեպի լիճ'),
 'Встреча в Ереване. Заранее обсуждаем с гидом одежду и снаряжение':
   tri('Встреча в назначенном месте в Ереване. Перед выходом гид проверяет одежду и снаряжение',
       'We meet at an agreed spot in Yerevan. Before the start the guide checks your clothing and gear',
       'Հանդիպում Երևանում պայմանավորված վայրում։ Մեկնարկից առաջ գիդը ստուգում է հագուստն ու սարքավորումը'),
 'Ранний выезд в село Арагац, там пересаживаемся на джип — он забрасывает к водопаду, отсюда начинаем подъём':
   tri('Трансфер к подножию Арагаца, к высокогорному озеру Кари на 3 200 м — дорога идёт прямо к воде',
       'Transfer to the foot of Aragats, to the high lake Kari at 3,200 m — the road goes right up to the water',
       'Տրանսֆեր դեպի Արագածի ստորոտ՝ 3 200 մ բարձրության վրա գտնվող Քարի լիճ, ճանապարհը հասնում է մինչև ջուրը'),
 'Инструктаж и старт': tri('Инструктаж и старт', 'Briefing and start', 'Հրահանգավորում և մեկնարկ'),
 'Вечер · Спуск': tri('Вечер · Спуск и Амберд', 'Evening · Descent and Amberd', 'Երեկո · Վայրէջք և Ամբերդ'),
 'Возвращение в Ереван': tri('Возвращение в Ереван к вечеру', 'Back in Yerevan by evening', 'Վերադարձ Երևան երեկոյան'),
 'Включено': tri('Включено', 'Included', 'Ներառված է'),
 'Джип от села Арагац до водопада и обратно':
   tri('Остановка у крепости Амберд на обратном пути', 'A stop at Amberd fortress on the way back', 'Կանգառ Ամբերդ ամրոցում վերադարձի ճանապարհին'),
 'Июнь — октябрь, дату выбираем вместе': None,
}

PAGES = {
 'aragats-yug': dict(
  slug='aragats-yug', apptitle='Арагац Южная', fs=(120, 112, 70),
  title=tri('Арагац, Южная вершина — White Irbis', 'Aragats, South peak — White Irbis', 'Արագած, Հարավային գագաթ — White Irbis'),
  desc='Восхождение на Южную вершину Арагаца, 3 879 м — первая высокая гора без технической подготовки. 1 день из Еревана, от озера Кари, на обратном пути крепость Амберд.',
  ogdesc='Первая вершина почти четыре тысячи метров за один день: озеро Кари, подъём 3,5 часа, обед на вершине и Амберд по дороге домой.',
  msg=tri('Здравствуйте! Хочу на Южную вершину Арагаца', 'Hi! I would like to climb the South peak of Aragats', 'Բարև Ձեզ։ Ուզում եմ բարձրանալ Արագածի Հարավային գագաթ'),
  T={
   'Из Еревана · 1 день · июнь — октябрь': tri('Из Еревана · 1 день · июнь — октябрь', 'From Yerevan · 1 day · June — October', 'Երևանից · 1 օր · հունիս — հոկտեմբեր'),
   'Арагац<br><em>Северная</em>': tri('Арагац<br><em>Южная</em>', 'Aragats<br><em>South</em>', 'Արագած<br><em>Հարավային</em>'),
   '4 090 метров — выше в Армении только небо.': tri(
     '3 879 метров — первая настоящая высота без альпинистской техники. Машина довозит до озера Кари, дальше три с половиной часа по широкому склону — и под ногами кратер старого вулкана. Обед на вершине, а по дороге домой — средневековая крепость Амберд.',
     '3,879 metres — your first real altitude, no climbing skills needed. The car takes you to Lake Kari, then three and a half hours up a broad slope, and the crater of an old volcano lies at your feet. Lunch on the summit, and the medieval fortress of Amberd on the way home.',
     '3 879 մետր՝ առաջին իսկական բարձրությունը առանց ալպինիստական տեխնիկայի։ Մեքենան հասցնում է Քարի լիճ, հետո երեքուկես ժամ լայն լանջով, և ոտքերի տակ հին հրաբխի խառնարանն է։ Ճաշ գագաթին, իսկ տուն վերադառնալիս՝ միջնադարյան Ամբերդ ամրոցը։'),
   'Хочу на вершину': tri('Хочу на Южную', 'I want the South peak', 'Ուզում եմ Հարավային'),
   '4 090 м': tri('3 879 м', '3,879 m', '3 879 մ'),
   'Один день — четыре тысячи': tri('Один день — почти четыре тысячи', 'One day — almost four thousand', 'Մեկ օր՝ գրեթե չորս հազար'),
   'Арагац — огромный потухший вулкан': tri(
     'Арагац — потухший вулкан и самая высокая гора современной Армении. В доисторические времена взрыв разрушил его вершину, и по краю кратера остались четыре пика. Южная — самая доступная из них: отсюда начинают знакомство с высотой.',
     'Aragats is an extinct volcano and the highest mountain of modern Armenia. In prehistoric times an eruption destroyed its top, leaving four peaks around the crater rim. The South peak is the most accessible: this is where people get to know altitude.',
     'Արագածը հանգած հրաբուխ է և ժամանակակից Հայաստանի ամենաբարձր լեռը։ Նախապատմական ժամանակներում պայթյունը քանդել է նրա գագաթը, և խառնարանի եզրին մնացել են չորս գագաթներ։ Հարավայինը դրանցից ամենահասանելին է՝ այստեղից են սկսում ծանոթությունը բարձրության հետ։'),
   'День · Склон и гребень': tri('День · Подъём и вершина', 'Day · Climb and summit', 'Օր · Վերելք և գագաթ'),
   'Подъём от водопада по северному склону': tri(
     'Подъём от озера Кари на Южную вершину — около 3,5 часа по широкому каменистому склону, без скальных участков',
     'The climb from Lake Kari to the South peak takes about 3.5 hours up a broad, rocky slope with no scrambling',
     'Վերելք Քարի լճից Հարավային գագաթ՝ մոտ 3,5 ժամ լայն քարքարոտ լանջով, առանց ժայռային հատվածների'),
   'Острый гребень к вершине': tri(
     'Последние метры — по краю кратера: внизу кратер и снежники, напротив — Северная и Западная вершины',
     'The last metres follow the crater rim: the crater and snowfields below, the North and West peaks right across',
     'Վերջին մետրերը խառնարանի եզրով են՝ ներքևում խառնարան և ձնադաշտեր, դիմացը՝ Հյուսիսային և Արևմտյան գագաթները'),
   'Вершина 4 090 м.': tri(
     'Вершина 3 879 м. Обед-ланчбокс прямо наверху, фотосессия, в ясный день видно Арарат',
     'Summit, 3,879 m. A lunch box right on top, photos, and Ararat on the horizon on a clear day',
     'Գագաթ, 3 879 մ։ Ճաշ-լանչբոքս հենց վերևում, լուսանկարներ, պարզ օրը երևում է Արարատը'),
   'Спуск тем же путём к водопаду': tri(
     'Спуск к озеру Кари — около 1,5 часа', 'Descent to Lake Kari — about 1.5 hours', 'Վայրէջք դեպի Քարի լիճ՝ մոտ 1,5 ժամ'),
   'Джип спускает в село Арагац': tri(
     'По дороге в Ереван — руины средневековой крепости Амберд на склоне Арагаца',
     'On the way to Yerevan — the ruins of the medieval fortress of Amberd on the slope of Aragats',
     'Երևան վերադառնալիս՝ Արագածի լանջին գտնվող միջնադարյան Ամբերդ ամրոցի ավերակները'),
   'Время на маршруте зависит': tri(
     'Время на маршруте зависит от темпа группы и снега — гид скажет точнее перед выходом.',
     'Timing depends on the group pace and snow — the guide will tell you more precisely before the start.',
     'Երթուղու ժամանակը կախված է խմբի տեմպից և ձյունից․ գիդը ավելի ճշգրիտ կասի մեկնարկից առաջ։'),
   'Ходим на Северную с июня по октябрь': tri(
     'Ходим на Южную с июня по октябрь, когда дорога к озеру Кари открыта и специальное снаряжение не нужно.',
     'We climb the South peak from June to October, when the road to Lake Kari is open and no special gear is needed.',
     'Հարավային ենք գնում հունիսից հոկտեմբեր, երբ Քարի լճի ճանապարհը բաց է և հատուկ սարքավորում պետք չէ։'),
   'Собираетесь на <a href="../ararat/">Арарат</a>?': tri(
     'Понравилось? Следующий шаг — <a href="../aragats/">Северная вершина</a>, высшая точка Армении, или <a href="../aragats-zapad/">Западная</a>.',
     'Enjoyed it? The next step is the <a href="../aragats/">North peak</a>, the highest point of Armenia, or the <a href="../aragats-zapad/">West peak</a>.',
     'Հավանեցի՞ք։ Հաջորդ քայլը <a href="../aragats/">Հյուսիսային գագաթն</a> է՝ Հայաստանի ամենաբարձր կետը, կամ <a href="../aragats-zapad/">Արևմտյանը</a>։'),
   'Весь день на ногах на высоте': tri(
     'Около пяти часов ходьбы на высоте 3 200–3 900 м. Достаточно обычной походной формы, альпинистская техника не нужна.',
     'About five hours of walking at 3,200–3,900 m. Ordinary hiking fitness is enough; no climbing technique required.',
     'Մոտ հինգ ժամ քայլք 3 200–3 900 մ բարձրության վրա։ Բավական է սովորական արշավային պատրաստվածությունը, ալպինիստական տեխնիկա պետք չէ։'),
   'Гребень': tri('Склон', 'Slope', 'Լանջ'),
   'Последний участок узкий и открытый.': tri(
     'Склон широкий, но под ногами камни и осыпь. Нужны треккинговые ботинки, палки сильно помогают на спуске.',
     'The slope is wide, but the ground is stones and scree. Trekking boots are a must; poles help a lot on the descent.',
     'Լանջը լայն է, բայց ոտքերի տակ քարեր և քարաթափ է։ Պետք են արշավային կոշիկներ, ձողերը շատ են օգնում վայրէջքին։'),
   'Первая четырёхтысячная': tri('Первая большая высота', 'Your first big altitude', 'Առաջին մեծ բարձրությունը'),
   'Хотите на крышу Армении': tri('Хотите попробовать высоту', 'Want to try altitude', 'Ուզում եք փորձել բարձրությունը'),
   'Северная — высшая точка страны': tri(
     'Почти 3 900 м за один день, без ночёвок и сложного рельефа.',
     'Almost 3,900 m in a single day, with no overnight stays and no hard terrain.',
     'Գրեթե 3 900 մ մեկ օրում, առանց գիշերակացի և բարդ ռելիեֆի։'),
   'Уже были на Южной': tri('Идёте всей семьёй или с друзьями', 'Going with family or friends', 'Գնում եք ընտանիքով կամ ընկերներով'),
   'Следующий шаг: гребень': tri(
     'Самый простой путь на Арагац — подходит для смешанной группы.',
     'The easiest way up Aragats — good for a mixed group.',
     'Արագածի ամենահեշտ ճանապարհը՝ հարմար է խառը խմբի համար։'),
   'Готовитесь к Арарату': tri('Готовитесь к Северной или Арарату', 'Preparing for the North peak or Ararat', 'Պատրաստվում եք Հյուսիսայինին կամ Արարատին'),
   'Проверите себя на 4 000 м': tri(
     'Хорошая первая ступень акклиматизации.', 'A good first step of acclimatisation.', 'Լավ առաջին քայլ ադապտացիայի համար։'),
   'Чем Северная отличается от Южной?': tri('Чем Южная отличается от Северной?', 'How is the South peak different from the North?', 'Ինչով է Հարավայինը տարբերվում Հյուսիսայինից'),
   'Южная (3 879 м) — самый простой путь на Арагац.': tri(
     'Южная (3 879 м) — самый простой путь на Арагац: старт от озера Кари, широкий склон, около 5 часов ходьбы. Северная (4 090 м) — высшая точка Армении: дольше, выше и с узким гребнем в конце.',
     'The South peak (3,879 m) is the easiest way up Aragats: start at Lake Kari, a broad slope, about 5 hours of walking. The North peak (4,090 m) is the highest point in Armenia: longer, higher, with a narrow ridge at the end.',
     'Հարավայինը (3 879 մ) Արագածի ամենահեշտ ճանապարհն է՝ մեկնարկ Քարի լճից, լայն լանջ, մոտ 5 ժամ քայլք։ Հյուսիսայինը (4 090 մ) Հայաստանի ամենաբարձր կետն է՝ ավելի երկար, ավելի բարձր և վերջում նեղ կատարով։'),
   'Идём на Северную?': tri('Идём на Южную?', 'Up the South peak?', 'Գնո՞ւմ ենք Հարավային'),
  },
  alts={'north_slope.jpg': 'Склон Арагаца над облаками', 'ridge_top.jpg': 'На краю кратера Арагаца',
        'summit.jpg': 'Группа White Irbis на Арагаце'}),
 'aragats-zapad': dict(
  slug='aragats-zapad', apptitle='Арагац Западная', fs=(120, 112, 70),
  title=tri('Арагац, Западная вершина — White Irbis', 'Aragats, West peak — White Irbis', 'Արագած, Արևմտյան գագաթ — White Irbis'),
  desc='Восхождение на Западную вершину Арагаца, 4 008 м — вторую по высоте в Армении. 1 день из Еревана, от озера Кари через седловину, на обратном пути крепость Амберд.',
  ogdesc='Четыре тысячи за один день: от озера Кари через седловину и крутую осыпь на Западную вершину 4 008 м.',
  msg=tri('Здравствуйте! Хочу на Западную вершину Арагаца', 'Hi! I would like to climb the West peak of Aragats', 'Բարև Ձեզ։ Ուզում եմ բարձրանալ Արագածի Արևմտյան գագաթ'),
  T={
   'Из Еревана · 1 день · июнь — октябрь': tri('Из Еревана · 1 день · июнь — октябрь', 'From Yerevan · 1 day · June — October', 'Երևանից · 1 օր · հունիս — հոկտեմբեր'),
   'Арагац<br><em>Северная</em>': tri('Арагац<br><em>Западная</em>', 'Aragats<br><em>West</em>', 'Արագած<br><em>Արևմտյան</em>'),
   '4 090 метров — выше в Армении только небо.': tri(
     '4 008 метров — вторая по высоте вершина Армении. От озера Кари уходим к седловине между Южной и Западной, дальше крутой подъём по осыпи — и вершина, куда добираются немногие. По дороге домой — крепость Амберд.',
     '4,008 metres — the second-highest summit in Armenia. From Lake Kari we head to the saddle between the South and West peaks, then a steep climb up the scree to a summit few people reach. On the way home — Amberd fortress.',
     '4 008 մետր՝ Հայաստանի երկրորդ ամենաբարձր գագաթը։ Քարի լճից գնում ենք դեպի Հարավային և Արևմտյան գագաթների միջև թամբը, հետո զառիթափ վերելք քարաթափով՝ դեպի գագաթ, որտեղ քչերն են հասնում։ Տուն վերադառնալիս՝ Ամբերդ ամրոցը։'),
   'Хочу на вершину': tri('Хочу на Западную', 'I want the West peak', 'Ուզում եմ Արևմտյան'),
   '4 090 м': tri('4 008 м', '4,008 m', '4 008 մ'),
   'Сезон': tri('Сезон', 'Season', 'Սեզոն'),
   'Сезон — июнь — октябрь': tri('Сезон — июнь — октябрь', 'Season — June — October', 'Սեզոն՝ հունիս — հոկտեմբեր'),
      'Один день — четыре тысячи': tri('Один день — четыре тысячи', 'One day — four thousand', 'Մեկ օր՝ չորս հազար'),
   'Арагац — огромный потухший вулкан': tri(
     'Арагац — потухший вулкан и самая высокая гора современной Армении: четыре его вершины стоят по краю кратера. Западная — вторая по высоте и самая крутая на подходе: тропы почти нет, последний час идём по осыпи.',
     'Aragats is an extinct volcano and the highest mountain of modern Armenia: its four peaks stand on the crater rim. The West peak is the second highest and the steepest to approach: there is hardly a trail, and the last hour is on scree.',
     'Արագածը հանգած հրաբուխ է և ժամանակակից Հայաստանի ամենաբարձր լեռը․ նրա չորս գագաթները կանգնած են խառնարանի եզրին։ Արևմտյանը բարձրությամբ երկրորդն է և ամենազառիթափը մոտեցման վրա․ արահետ գրեթե չկա, վերջին ժամը քարաթափով ենք գնում։'),
   'День · Склон и гребень': tri('День · Седловина и осыпь', 'Day · Saddle and scree', 'Օր · Թամբ և քարաթափ'),
   'Подъём от водопада по северному склону': tri(
     'От озера Кари к седловине между Южной и Западной вершинами, около 3 800 м',
     'From Lake Kari to the saddle between the South and West peaks, about 3,800 m',
     'Քարի լճից դեպի Հարավային և Արևմտյան գագաթների միջև թամբը՝ մոտ 3 800 մ'),
   'Острый гребень к вершине': tri(
     'Крутой подъём по сыпучему склону без тропы — самый трудный кусок дня, идём плотной группой и смотрим под ноги',
     'A steep climb up loose ground with no trail — the hardest part of the day; we keep the group tight and watch our step',
     'Զառիթափ վերելք փխրուն լանջով առանց արահետի՝ օրվա ամենադժվար հատվածը, գնում ենք սերտ խմբով և նայում ոտքերի տակ'),
   'Вершина 4 090 м.': tri(
     'Вершина 4 008 м — примерно 4 часа от озера. Обед-ланчбокс, фото, под ногами весь кратер со снежниками',
     'Summit, 4,008 m — about 4 hours from the lake. Lunch box, photos, the whole crater and its snowfields at your feet',
     'Գագաթ, 4 008 մ՝ լճից մոտ 4 ժամ։ Ճաշ-լանչբոքս, լուսանկարներ, ոտքերի տակ ամբողջ խառնարանը ձնադաշտերով'),
   'Спуск тем же путём к водопаду': tri(
     'Спуск на седловину и к озеру Кари — около 2 часов', 'Descent to the saddle and down to Lake Kari — about 2 hours', 'Վայրէջք թամբ և Քարի լիճ՝ մոտ 2 ժամ'),
   'Джип спускает в село Арагац': tri(
     'По дороге в Ереван — руины средневековой крепости Амберд',
     'On the way to Yerevan — the ruins of the medieval fortress of Amberd',
     'Երևան վերադառնալիս՝ միջնադարյան Ամբերդ ամրոցի ավերակները'),
   'Время на маршруте зависит': tri(
     'Время на маршруте зависит от темпа группы и снега — гид скажет точнее перед выходом.',
     'Timing depends on the group pace and snow — the guide will tell you more precisely before the start.',
     'Երթուղու ժամանակը կախված է խմբի տեմպից և ձյունից․ գիդը ավելի ճշգրիտ կասի մեկնարկից առաջ։'),
      'Ходим на Северную с июня по октябрь': tri(
     'На Западную ходим с июня по октябрь: подход по осыпи проходим без специального снаряжения.',
     'We climb the West peak from June to October: the scree approach needs no special gear.',
     'Արևմտյան ենք գնում հունիսից հոկտեմբեր․ քարաթափով մոտեցումը անցնում ենք առանց հատուկ սարքավորման։'),
   'Собираетесь на <a href="../ararat/">Арарат</a>?': tri(
     'Впервые на Арагаце? Начните с <a href="../aragats-yug/">Южной</a>. Хотите на высшую точку страны — <a href="../aragats/">Северная</a>.',
     'First time on Aragats? Start with the <a href="../aragats-yug/">South peak</a>. Want the highest point of the country — the <a href="../aragats/">North peak</a>.',
     'Առաջին անգա՞մ եք Արագածում։ Սկսեք <a href="../aragats-yug/">Հարավայինից</a>։ Ուզում եք երկրի ամենաբարձր կետը՝ <a href="../aragats/">Հյուսիսային</a>։'),
   'Весь день на ногах на высоте': tri(
     'Около шести часов ходьбы на высоте 3 200–4 000 м, в конце крутая осыпь. Нужен опыт горных походов. Альпинистская техника не нужна.',
     'About six hours of walking at 3,200–4,000 m with steep scree at the end. Mountain hiking experience is needed; no climbing technique required.',
     'Մոտ վեց ժամ քայլք 3 200–4 000 մ բարձրության վրա, վերջում զառիթափ քարաթափ։ Պետք է լեռնային արշավների փորձ։ Ալպինիստական տեխնիկա պետք չէ։'),
   'Гребень': tri('Осыпь', 'Scree', 'Քարաթափ'),
   'Последний участок узкий и открытый.': tri(
     'Под вершиной крутой сыпучий склон, возможны падающие камни. Идём плотно, в касках по решению гида.',
     'Below the summit is a steep, loose slope with possible rockfall. We keep together; helmets if the guide decides so.',
     'Գագաթի տակ զառիթափ փխրուն լանջ է, հնարավոր են քարաթափեր։ Գնում ենք սերտ, սաղավարտներով՝ գիդի որոշմամբ։'),
   'Первая четырёхтысячная': tri('Четыре тысячи без толпы', 'Four thousand without the crowds', 'Չորս հազար՝ առանց ամբոխի'),
   'Хотите на крышу Армении': tri('Были на Южной', 'Done the South peak', 'Եղել եք Հարավայինում'),
   'Северная — высшая точка страны': tri(
     'Западная — следующий шаг: выше, круче и почти без людей.',
     'The West peak is the next step: higher, steeper and almost empty.',
     'Արևմտյանը հաջորդ քայլն է՝ ավելի բարձր, ավելի զառիթափ և գրեթե առանց մարդկանց։'),
   'Уже были на Южной': tri('Любите дикие места', 'Love wild places', 'Սիրում եք վայրի վայրեր'),
   'Следующий шаг: гребень': tri(
     'Без тропы и толп — только кратер, снежники и ветер.',
     'No trail, no crowds — just the crater, the snowfields and the wind.',
     'Առանց արահետի և ամբոխի՝ միայն խառնարան, ձնադաշտեր և քամի։'),
   'Чем Северная отличается от Южной?': tri('Чем Западная отличается от Южной?', 'How is the West peak different from the South?', 'Ինչով է Արևմտյանը տարբերվում Հարավայինից'),
   'Южная (3 879 м) — самый простой путь на Арагац.': tri(
     'Южная (3 879 м) — самый простой путь на Арагац, по широкому склону. Западная (4 008 м) выше на 129 м, и последний подъём к ней — крутая осыпь без тропы. Если вы впервые на высоте, начните с Южной.',
     'The South peak (3,879 m) is the easiest way up Aragats, on a broad slope. The West peak (4,008 m) is 129 m higher, and the final climb is steep scree with no trail. If altitude is new to you, start with the South.',
     'Հարավայինը (3 879 մ) Արագածի ամենահեշտ ճանապարհն է՝ լայն լանջով։ Արևմտյանը (4 008 մ) 129 մ ավելի բարձր է, և վերջին վերելքը զառիթափ քարաթափ է առանց արահետի։ Եթե առաջին անգամ եք բարձրության վրա, սկսեք Հարավայինից։'),
         'Идём на Северную?': tri('Идём на Западную?', 'Up the West peak?', 'Գնո՞ւմ ենք Արևմտյան'),
  },
  alts={'north_slope.jpg': 'Склон Арагаца над облаками', 'ridge_top.jpg': 'На краю кратера Арагаца',
        'summit.jpg': 'Группа White Irbis на Арагаце'}),
}

TRI = re.compile(r'<span lang="ru">(.*?)</span>(\s*)<span lang="en">(.*?)</span>(\s*)<span lang="hy">(.*?)</span>', re.S)

def build(p, price):
    s = SRC
    T = dict((k, v) for k, v in COMMON.items() if v)
    T.update(p['T'])
    used = set()
    def rep(m):
        ru = m.group(1)
        keys = [k for k in T if ru == k] or sorted((k for k in T if ru.startswith(k)), key=len, reverse=True)
        for k in keys[:1]:
            v = T[k]
            if True:
                used.add(k)
                return f'<span lang="ru">{v[0]}</span>{m.group(2)}<span lang="en">{v[1]}</span>{m.group(4)}<span lang="hy">{v[2]}</span>'
        return m.group(0)
    s = TRI.sub(rep, s)
    missing = set(T) - used
    assert not missing, missing
    # price
    if price:
        rub, eur, amd = price
        s = s.replace('13 700 ₽', rub).replace('€149', eur).replace('60 000 ֏', amd)
        s = s.replace('≈ 13,700 ₽', '≈ ' + rub.replace(' ', ',', 1)).replace('60,000 AMD', amd.replace(' ֏', ' AMD').replace(' ', ',', 1))
    # head
    t = p['title']
    s = s.replace('Арагац, Северная вершина — White Irbis', t[0])
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{p["ogdesc"]}">', s)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{p["desc"]}">', s)
    s = s.replace('https://whiteirbis.am/aragats/', f'https://whiteirbis.am/{p["slug"]}/')
    s = s.replace('<meta name="apple-mobile-web-app-title" content="Арагац">', f'<meta name="apple-mobile-web-app-title" content="{p["apptitle"]}">')
    s = re.sub(r'var msg=\{[^{}]*\}', lambda m: 'var msg=' + json.dumps(dict(zip(('ru', 'en', 'hy'), p['msg'])), ensure_ascii=False), s, count=1)
    s = re.sub(r'titles=\{[^{}]*\}', lambda m: 'titles=' + json.dumps(dict(zip(('ru', 'en', 'hy'), t)), ensure_ascii=False), s, count=1)
    # media from the North page folder
    s = re.sub(r'(src|href)="(img|vid)/(?!logo\.png)', r'\1="../aragats/\2/', s)
    for f, alt in p['alts'].items():
        s = re.sub(rf'(src="../aragats/img/{re.escape(f)}" alt=")[^"]*', rf'\g<1>{alt}', s)
    os.makedirs(f'{R}/{p["slug"]}/img', exist_ok=True)
    shutil.copy(f'{R}/aragats/img/logo.png', f'{R}/{p["slug"]}/img/logo.png')
    open(f'{R}/{p["slug"]}/index.html', 'w', encoding='utf-8').write(s)
    print(p['slug'], len(s))

if __name__ == '__main__':
    import sys
    prices = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
    for k, p in PAGES.items():
        build(p, prices.get(k))
