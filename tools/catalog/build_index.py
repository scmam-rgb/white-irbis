#!/usr/bin/env python3
"""Builds the catalog home page (index.html) from parts in this folder.
Run from the repo root:  python3 tools/catalog/build_index.py
"""
import os, re, urllib.parse
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(H, '..', '..'))
rd = lambda f: open(os.path.join(H, f), encoding='utf-8').read()

def T(ru, en, hy):
    return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'

WA = 'https://wa.me/37491470331'
TG = 'https://t.me/+37491470331'
def wa(text):
    return WA + '?text=' + urllib.parse.quote(text)
def waT(ru, en, hy, label_ru, label_en, label_hy, cls='btn'):
    return ''.join(f'<a class="{cls}" lang="{l}" href="{wa(t)}" target="_blank" rel="noopener">{lb}</a>'
                   for l, t, lb in (('ru', ru, label_ru), ('en', en, label_en), ('hy', hy, label_hy)))

# ---------- 1. trust strip ----------
trust = f'''<section class="trust">
  <p class="lead">{T("Горные туры по Армении с профессиональными инструкторами: скалы, вершины, тропы и лыжи. Всё продумано — остаётся идти.",
  "Mountain tours in Armenia with professional instructors: rock, summits, trails and skiing. Everything is taken care of — you just walk.",
  "Լեռնային տուրեր Հայաստանում պրոֆեսիոնալ հրահանգիչների հետ՝ ժայռեր, գագաթներ, արահետներ և դահուկներ։ Ամեն ինչ մտածված է, մնում է քայլել։")}</p>
  <ul class="tf">
    <li><b>2003</b>{T("первая группа","first group","առաջին խումբը")}</li>
    <li><b>1 000+</b>{T("человек уже с нами сходили","people have been with us","մարդ արդեն եղել է մեզ հետ")}</li>
    <li><b>{T("Страховка","Insurance","Ապահովագրություն")}</b>{T("включена в каждый тур","included in every tour","ներառված է յուրաքանչյուր տուրում")}</li>
    <li class="tf-fed"><a href="o-nas/#partners" class="fedl"><img src="o-nas/img/federation.jpg" width="1000" height="460" alt="Federation of Mountaineering of Armenia · UIAA"></a>{T("члены федерации альпинизма Армении","members of the Armenian mountaineering federation","Հայաստանի լեռնագնացության ֆեդերացիայի անդամ")}</li>
  </ul>
</section>'''

# ---------- 2. upcoming departures (ski, until March) ----------
DATES = [  # Saturday arrivals, 7 days / 6 nights
    ('2026-12-19', '2026-12-25'), ('2027-01-02', '2027-01-08'), ('2027-01-16', '2027-01-22'),
    ('2027-01-30', '2027-02-05'), ('2027-02-13', '2027-02-19'), ('2027-02-27', '2027-03-05'),
    ('2027-03-13', '2027-03-19')]
MRU = 'января февраля марта апреля мая июня июля августа сентября октября ноября декабря'.split()
MEN = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
MHY = 'հունվարի փետրվարի մարտի ապրիլի մայիսի հունիսի հուլիսի օգոստոսի սեպտեմբերի հոկտեմբերի նոյեմբերի դեկտեմբերի'.split()
def rng(a, b):
    ya, ma, da = map(int, a.split('-')); yb, mb, db = map(int, b.split('-'))
    if ma == mb:
        return (f'{da}–{db} {MRU[ma-1]}', f'{da}–{db} {MEN[ma-1]}', f'{MHY[ma-1]} {da}–{db}')
    return (f'{da} {MRU[ma-1]} – {db} {MRU[mb-1]}', f'{da} {MEN[ma-1]} – {db} {MEN[mb-1]}', f'{MHY[ma-1]} {da} – {MHY[mb-1]} {db}')
rows = []
for a, b in DATES:
    ru, en, hy = rng(a, b)
    ny = ' <em>' + T('новогодние каникулы', 'New Year holidays', 'Ամանորյա արձակուրդներ') + '</em>' if a == '2027-01-02' else ''
    btn = waT(f'Здравствуйте! Хочу на «Горные лыжи с нуля», заезд {ru}.',
              f'Hello! I\'d like to join "Skiing from scratch", {en}.',
              f'Բարև։ Ուզում եմ միանալ «Լեռնադահուկ զրոյից» տուրին՝ {hy}։',
              'Записаться', 'Book', 'Գրանցվել', 'btn sm')
    rows.append(f'<li data-end="{b}"><span class="dd">{T(ru, en, hy)}{ny}</span><span class="dt">{T("7 дней / 6 ночей","7 days / 6 nights","7 օր / 6 գիշեր")}</span>{btn}</li>')
dates = f'''<section class="sec" id="dates">
  <h2 class="sh">{T("Ближайшие выезды","Upcoming departures","Մոտակա մեկնումները")}</h2>
  <div class="dep">
    <a class="dep-h" href="ski/"><img src="ski/img/three_top.jpg" alt="" style="object-position:50% 35%"></a>
    <div class="dep-b">
      <div class="dep-t"><b>{T("Горные лыжи с нуля","Skiing from scratch","Լեռնադահուկ զրոյից")}</b><span class="pr">{T("97 000 ₽","€1,055","426 000 ֏")}<small>{T("с человека · группа до 6","per person · up to 6 people","մեկ անձի համար · մինչև 6 հոգի")}</small></span></div>
      <ul class="dl">{''.join(rows)}</ul>
      <p class="note">{T("Заезд в субботу. Другие туры — по запросу: подберём дату под вашу группу.","Arrivals on Saturdays. Other tours on request — we'll find a date for your group.","Ժամանումը՝ շաբաթ օրը։ Մյուս տուրերը՝ ըստ հարցման. կընտրենք ձեր խմբին հարմար օր։")}</p>
    </div>
  </div>
</section>'''

# ---------- 3. tours with a quick picker ----------
TAGS = {'ski/': 'first winter', 'skaly-i-vulkan/': 'first rocks peak', 'aragats/': 'peak', 'ararat/': 'peak',
        'trekking/': 'first walk', 'extreme-wine/': 'first', 'weekend/': 'first rocks'}
cards = rd('cards.html')
for href, tg in TAGS.items():
    cards = cards.replace(f'<a class="c" href="{href}">', f'<a class="c" href="{href}" data-t="{tg}">')
chips = [('all', T('Все', 'All', 'Բոլորը')), ('first', T('Впервые в горах', 'First time in the mountains', 'Առաջին անգամ լեռներում')),
         ('peak', T('Хочу вершину', 'I want a summit', 'Ուզում եմ գագաթ')), ('rocks', T('Хочу на скалы', 'I want to climb', 'Ուզում եմ ժայռեր')),
         ('walk', T('Пешком', 'On foot', 'Ոտքով')), ('winter', T('Зимой', 'In winter', 'Ձմռանը'))]
picker = '<div class="pick" role="group">' + ''.join(
    f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in chips) + '</div>'
tours = f'''<section class="sec" id="tours">
  <h2 class="sh">{T("Туры","Tours","Տուրեր")}</h2>
  {picker}
  <div class="g">{cards}</div>
</section>'''

# ---------- 4. gallery: own photos and videos ----------
G = [  # (img, video or None, caption)
    ('ararat/img/summit_top.jpg', None, ('Арарат, 5 137 м', 'Ararat, 5,137 m', 'Արարատ, 5 137 մ')),
    ('img/gal/aragats_slope.jpg', 'aragats/vid/slope.mp4', ('Арагац, северный склон', 'Aragats, north slope', 'Արագած, հյուսիսային լանջ')),
    ('skaly-i-vulkan/img/u_purple_smile.jpg', None, ('Первый раз на скалах', 'First day on rock', 'Առաջին անգամ ժայռերին')),
    ('img/gal/rocks_v02.jpg', 'skaly-i-vulkan/vid/v02.mp4', ('Скалолазание', 'Rock climbing', 'Մագլցում')),
    ('ski/img/gondola_group.jpg', None, ('Горные лыжи с нуля', 'Skiing from scratch', 'Լեռնադահուկ զրոյից')),
    ('img/gal/ski_top.jpg', 'ski/vid/v_top.mp4', ('На склоне', 'On the slope', 'Լանջին')),
    ('ararat/img/glacier.jpg', None, ('Ледник Арарата', 'Ararat glacier', 'Արարատի սառցադաշտ')),
    ('skaly-i-vulkan/img/u_tents.jpg', None, ('Ночь в палатках', 'A night in tents', 'Գիշեր վրաններում')),
    ('img/gal/trek_plateau.jpg', 'trekking/vid/tr_plateau.mp4', ('Армения пешком', 'Armenia on foot', 'Հայաստան ոտքով')),
    ('extreme-wine/img/zip_group.jpg', None, ('Экстрим вайн тур: зиплайн', 'Extreme wine tour: zipline', 'Էքստրիմ գինու տուր՝ զիփլայն')),
    ('aragats/img/ridge_top.jpg', None, ('Арагац, Северная вершина', 'Aragats, North peak', 'Արագած, Հյուսիսային գագաթ')),
    ('ararat/img/team.jpg', None, ('Наша группа', 'Our group', 'Մեր խումբը')),
]
tiles = []
for img, vid, cap in G:
    v = f'<video muted loop playsinline preload="none" data-src="{vid}"></video><i class="pl" aria-hidden="true"></i>' if vid else ''
    tiles.append(f'<figure class="gi{" gv" if vid else ""}"><img src="{img}" alt="" loading="lazy">{v}<figcaption>{T(*cap)}</figcaption></figure>')
gallery = f'''<section class="sec" id="gallery">
  <h2 class="sh">{T("Как это у нас","What it's like","Ինչպես է մեզ մոտ")}</h2>
  <p class="sub">{T("Только наши фото и видео — с настоящих выездов.","Only our own photos and videos — from real trips.","Միայն մեր լուսանկարներն ու տեսանյութերը՝ իրական ելքերից։")}</p>
  <div class="gal">{''.join(tiles)}</div>
</section>'''

# ---------- 5. custom / corporate / rental + gift ----------
def card(t, p, cta):
    return f'<div class="xc"><h3>{T(*t)}</h3><p>{T(*p)}</p>{cta}</div>'
custom = f'''<section class="sec" id="custom">
  <h2 class="sh">{T("Не нашли подходящее?","Didn't find what you need?","Չգտա՞ք համապատասխանը")}</h2>
  <div class="xg">
    {card(("Индивидуально","Tailor-made","Անհատական"),
          ("Соберём программу под вас: даты, маршрут, уровень, длительность. Семья или друзья — личный инструктор, своя машина и свой темп.","We'll build a programme around you: dates, route, level, length. Family or friends — a private instructor, your own vehicle and your own pace.","Կկազմենք ծրագիր ձեզ համար՝ ամսաթվեր, երթուղի, մակարդակ, տևողություն։ Ընտանիք կամ ընկերներ՝ անհատական հրահանգիչ, ձեր մեքենան և ձեր տեմպը։"),
          waT("Здравствуйте! Хочу индивидуальную программу.","Hello! I'd like a tailor-made programme.","Բարև։ Ուզում եմ անհատական ծրագիր։","Обсудить →","Let's talk →","Քննարկել →","lnk"))}
    {card(("Компании и клубы","Companies and clubs","Ընկերություններ և ակումբներ"),
          ("Корпоративный выезд, тимбилдинг или клубная поездка: восхождение, скалы, треккинг. Закрытая группа и программа под ваши задачи.","A corporate trip, team building or club outing: a summit, rock or trekking. A private group and a programme built around your goals.","Կորպորատիվ ելք, թիմային միջոցառում կամ ակումբային ճամփորդություն՝ վերելք, ժայռեր, արշավ։ Փակ խումբ և ծրագիր՝ ձեր նպատակներով։"),
          waT("Здравствуйте! Интересует выезд для компании/клуба.","Hello! We're interested in a trip for our company/club.","Բարև։ Հետաքրքրված ենք ընկերության/ակումբի ելքով։","Запросить →","Request →","Հարցում →","lnk"))}
    {card(("Прокат снаряжения","Gear rental","Հանդերձանքի վարձույթ"),
          ("Идёте в горы сами? Палатки, спальники, коврики, каски, системы, верёвки, скальные туфли и другое.","Heading out on your own? Tents, sleeping bags, mats, helmets, harnesses, ropes, climbing shoes and more.","Լեռներ եք գնում ինքնուրույն։ Վրաններ, քնապարկեր, ներքնակներ, սաղավարտներ, համակարգեր, պարաններ, ժայռային կոշիկներ և այլն։"),
          waT("Здравствуйте! Нужен прокат снаряжения.","Hello! I need to rent some gear.","Բարև։ Հանդերձանքի վարձույթ է պետք։","Узнать →","Ask →","Իմանալ →","lnk"))}
  </div>
  <div class="flip" id="gift" tabindex="0" aria-label="Gift certificate">
   <div class="fl-in">
    <div class="gift face fr">
      <div>
        <span class="gk">{T("Подарочный сертификат","Gift certificate","Նվեր-վկայական")}</span>
        <b>{T("Подарите горы","Give the mountains","Նվիրեք լեռներ")}</b>
        <p>{T("Сертификат на любой наш тур — на 5% дешевле цены тура. Именной, с датой на выбор: восхождение на Арагац, выходные на скалах, неделя на лыжах или Арарат.",
              "A certificate for any of our tours — 5% off the tour price. Personalised, with the date of their choice: Aragats, a weekend on rock, a week of skiing or Ararat.",
              "Վկայական մեր ցանկացած տուրի համար՝ տուրի գնից 5%-ով էժան։ Անվանական, ընտրովի ամսաթվով՝ Արագած, հանգստյան օրեր ժայռերին, դահուկային շաբաթ կամ Արարատ։")}</p>
      </div>
      <div class="gift-p"><span class="pct">−5%</span>{waT("Здравствуйте! Хочу подарочный сертификат.","Hello! I'd like a gift certificate.","Բարև։ Ուզում եմ նվեր-վկայական։","Хочу сертификат","Get a certificate","Ուզում եմ վկայական","btn dark")}</div>
    </div>
    <div class="gift face bk" aria-hidden="true">
      <div class="gw"><b class="gr on">{T("Поздравляем!","Congratulations!","Շնորհավորում ենք")}</b><b class="gr">{T("С днём рождения!","Happy birthday!","Շնորհավոր ծնունդդ")}</b><b class="gr">{T("С юбилеем!","Happy anniversary!","Շնորհավոր հոբելյանդ")}</b><b class="gr">{T("С праздником!","Happy holidays!","Շնորհավոր տոնդ")}</b></div>
      <span class="gs">White Irbis</span>
    </div>
   </div>
  </div>
</section>'''

# ---------- 6. FAQ ----------
FAQ = [
 (("Нужен ли опыт?","Do I need experience?","Փորձ պե՞տք է"),
  ("Для большинства туров — нет: на скалах и лыжах учим с нуля, в треккинге — темп для всех. Для Арагаца и Арарата техника не нужна, но нужна хорошая физическая форма.",
   "For most tours, no: we teach rock and skiing from scratch, and trekking goes at a pace for everyone. Aragats and Ararat need no technique, but you do need good fitness.",
   "Տուրերի մեծ մասի համար՝ ոչ. ժայռերին և դահուկներին սովորեցնում ենք զրոյից, արշավում տեմպը բոլորի համար է։ Արագածի և Արարատի համար տեխնիկա պետք չէ, բայց պետք է լավ ֆիզիկական պատրաստվածություն։")),
 (("Насколько это безопасно?","How safe is it?","Որքանո՞վ է անվտանգ"),
  ("Группы ведут профессиональные инструкторы, на скалах их всегда не меньше двух. Снаряжение проверенное, страховка участника включена в цену.",
   "Groups are led by professional instructors, and on rock there are always at least two. Gear is checked, and participant insurance is included in the price.",
   "Խմբերը առաջնորդում են պրոֆեսիոնալ հրահանգիչներ, ժայռերին նրանք միշտ առնվազն երկուսն են։ Հանդերձանքը ստուգված է, մասնակցի ապահովագրությունը ներառված է գնի մեջ։")),
 (("А если испортится погода?","What if the weather turns bad?","Իսկ եթե եղանակը վատանա՞"),
  ("В горах решает погода. Если надо — меняем дни местами или вершину, чтобы вы получили лучший день, а не галочку.",
   "In the mountains the weather decides. When needed we swap days or the peak so you get the best day, not just a tick.",
   "Լեռներում եղանակն է որոշում։ Անհրաժեշտության դեպքում փոխում ենք օրերի հերթականությունը կամ գագաթը, որ ստանաք լավագույն օրը։")),
 (("Что взять с собой?","What should I bring?","Ի՞նչ վերցնել հետս"),
  ("Техническое снаряжение даём мы. Список одежды и личных вещей пришлём после записи — он есть и на странице каждого тура.",
   "We provide the technical gear. We'll send a list of clothing and personal items after you book — it's also on each tour page.",
   "Տեխնիկական հանդերձանքը տալիս ենք մենք։ Հագուստի և անձնական իրերի ցանկը կուղարկենք գրանցվելուց հետո. այն կա նաև յուրաքանչյուր տուրի էջում։")),
 (("Как записаться?","How do I book?","Ինչպե՞ս գրանցվել"),
  ("Напишите в WhatsApp или Telegram: подберём тур и дату, ответим на вопросы, пришлём детали оплаты. Говорим по-русски, по-английски и по-армянски.",
   "Message us on WhatsApp or Telegram: we'll match a tour and date, answer your questions and send payment details. We speak Russian, English and Armenian.",
   "Գրեք WhatsApp-ով կամ Telegram-ով. կընտրենք տուր և ամսաթիվ, կպատասխանենք հարցերին, կուղարկենք վճարման մանրամասները։ Խոսում ենք ռուսերեն, անգլերեն և հայերեն։")),
]
faq = f'''<section class="sec" id="faq">
  <h2 class="sh">{T("Частые вопросы","FAQ","Հաճախ տրվող հարցեր")}</h2>
  <div class="faq">{''.join(f'<details><summary>{T(*q)}</summary><p>{T(*a)}</p></details>' for q, a in FAQ)}</div>
</section>'''

guides = f'''<section class="sec" id="guides">
  <h2 class="sh">{T("Гайдбуки","Guidebooks","Ուղեցույցներ")}</h2>
  {rd('guidebooks.html')}
</section>'''

contact = f'''<section class="cta-end" id="contact">
  <b>{T("Едем в горы?","Off to the mountains?","Գնո՞ւմ ենք լեռներ")}</b>
  <p>{T("Напишите — подберём тур, дату и ответим на вопросы.","Message us — we'll pick a tour and a date and answer your questions.","Գրեք մեզ՝ կընտրենք տուր, ամսաթիվ և կպատասխանենք հարցերին։")}</p>
  <div class="row"><a class="btn dark" href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a class="btn dark" href="{TG}" target="_blank" rel="noopener">Telegram</a><a class="tel" href="tel:+37491470331">+374 91 470 331</a></div>
</section>'''

footer = '''<footer><a href="o-nas/">''' + T('О нас', 'About us', 'Մեր մասին') + '''</a> · <a href="mailto:antuanvisit@gmail.com">antuanvisit@gmail.com</a> · <a href="https://whiteirbis.am">whiteirbis.am</a></footer>'''

fab = f'''<div class="fab" aria-label="Contact"><a class="fa-wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.2-.3-.2-.5-.3Z"/></svg></a><a class="fa-tg" href="{TG}" target="_blank" rel="noopener" aria-label="Telegram"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path fill="currentColor" d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.7.8l-4.8-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.9 8.9-8c.4-.3-.1-.5-.6-.2L6.5 13.2 1.8 11.7c-1-.3-1-1 .2-1.5L20.5 3c.9-.3 1.6.2 1.4 1.3Z"/></svg></a></div>'''

CSS = rd('base_css.css') + r'''
:root{--y:#FAEB0F;--ink:#F7F4EC;--mut:#B9B5A8;--card:#1E1E1C;--line:#3A3934}
.sec{margin-top:56px}
.sub{color:var(--mut);margin:-6px 0 18px;font-size:17px}
.btn{display:inline-flex;align-items:center;justify-content:center;background:var(--y);color:#121212;font-family:Oswald,Arial,sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:17px;padding:11px 18px;border-radius:6px;text-decoration:none;white-space:nowrap}
.btn:hover{background:#fff}
.btn.sm{font-size:15px;padding:8px 14px}
.btn.dark{background:#121212;color:var(--y)}.btn.dark:hover{background:#000}
html[lang="hy"] .btn{font-family:"Noto Sans Armenian",Oswald,sans-serif;font-size:15px;letter-spacing:.02em}
/* trust */
.trust .lead{font-size:clamp(20px,2.4vw,26px);line-height:1.35;margin:0 0 22px;max-width:860px}
.tf{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.tf li{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;gap:6px;color:var(--mut);font-size:15px;line-height:1.3}
.tf b{font-family:Oswald,Arial,sans-serif;font-size:28px;line-height:1;color:var(--y);font-weight:600}
html[lang="hy"] .tf b{font-family:"Noto Sans Armenian",Oswald,sans-serif;font-size:22px}
.fedl{display:block;background:#fff;border-radius:8px;padding:6px 10px;align-self:flex-start}
.fedl img{display:block;height:34px;width:auto}
@media(max-width:860px){.tf{grid-template-columns:1fr 1fr}}
/* departures */
.dep{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.dep-h img{display:block;width:100%;height:100%;object-fit:cover}
.dep-b{padding:22px 24px}
.dep-t{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;margin-bottom:12px}
.dep-t b{font-family:Oswald,Arial,sans-serif;text-transform:uppercase;font-size:28px;line-height:1.05}
html[lang="hy"] .dep-t b{font-family:"Noto Sans Armenian",Oswald,sans-serif;font-size:22px}
.pr{font-family:Oswald,Arial,sans-serif;font-size:26px;color:var(--y);text-align:right;line-height:1}
.pr small{display:block;font-family:Rubik,Arial,sans-serif;font-size:13px;color:var(--mut);margin-top:4px}
.dl{list-style:none;margin:0;padding:0}
.dl li{display:grid;grid-template-columns:1fr auto auto;gap:14px;align-items:center;padding:10px 0;border-top:1px solid var(--line)}
.dd{font-size:18px;font-weight:500}.dd em{display:inline-block;font-style:normal;font-size:12px;letter-spacing:.06em;text-transform:uppercase;background:var(--y);color:#121212;border-radius:4px;padding:2px 6px;margin-left:8px;vertical-align:2px}
.dt{color:var(--mut);font-size:14px}
.note{color:var(--mut);font-size:14px;margin:12px 0 0}
@media(max-width:760px){.dep{grid-template-columns:1fr}.dep-h img{aspect-ratio:1200/630;height:auto}.dl li{grid-template-columns:1fr auto}.dt{display:none}.dep-b{padding:18px 16px}}
/* picker */
.pick{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}
.pick button{font:500 15px Rubik,Arial,sans-serif;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:30px;padding:8px 16px;cursor:pointer}
.pick button[aria-pressed="true"]{background:var(--y);border-color:var(--y);color:#121212}
a.c.off{display:none}
/* gallery */
.gal{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.gi{position:relative;margin:0;border-radius:12px;overflow:hidden;aspect-ratio:1;background:#000}
.gi img,.gi video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.gi video{opacity:0;transition:opacity .4s}.gi.on video{opacity:1}
.gi figcaption{position:absolute;left:0;right:0;bottom:0;padding:24px 12px 10px;font-size:14px;background:linear-gradient(transparent,rgba(0,0,0,.65))}
.pl{position:absolute;top:10px;right:10px;width:26px;height:26px;border-radius:50%;background:rgba(0,0,0,.5)}
.pl:after{content:"";position:absolute;left:10px;top:7px;border-left:9px solid #fff;border-top:6px solid transparent;border-bottom:6px solid transparent}
.gi.on .pl{display:none}
@media(max-width:860px){.gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
/* custom + gift */
.xg{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.xc{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px}
.xc h3{margin:0;font-family:Oswald,Arial,sans-serif;text-transform:uppercase;font-size:24px;font-weight:600}
html[lang="hy"] .xc h3{font-family:"Noto Sans Armenian",Oswald,sans-serif;font-size:19px}
.xc p{margin:0;color:var(--mut);line-height:1.45;flex:1}
.lnk{color:var(--y);text-decoration:none;font-weight:500}
.gift{margin-top:14px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;background:var(--y);color:#121212;border-radius:18px;padding:28px 30px}
.gk{font-family:Oswald,Arial,sans-serif;font-weight:600;font-size:16px;letter-spacing:.22em;text-transform:uppercase}
.gift b{display:block;font-family:Oswald,Arial,sans-serif;text-transform:uppercase;font-size:clamp(34px,4.4vw,54px);line-height:1;margin:8px 0 10px}
html[lang="hy"] .gift b,html[lang="hy"] .gk{font-family:"Noto Sans Armenian",Oswald,sans-serif;letter-spacing:.04em}
.gift p{margin:0;font-size:17px;line-height:1.45;max-width:640px}
.gift-p{display:flex;flex-direction:column;align-items:center;gap:12px}
.pct{font-family:Oswald,Arial,sans-serif;font-weight:700;font-size:64px;line-height:1}
@media(max-width:760px){.xg{grid-template-columns:1fr}.gift{grid-template-columns:1fr;padding:22px 18px}.gift-p{flex-direction:row;justify-content:space-between}}
/* faq */
.faq details{border-top:1px solid var(--line);padding:14px 0}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;font-size:19px;font-weight:500;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";color:var(--y);font-size:24px;line-height:1}
.faq details[open] summary:after{content:"−"}
.faq p{color:var(--mut);margin:10px 0 0;line-height:1.5;max-width:820px}
/* final cta */
.cta-end{margin-top:56px;background:var(--y);color:#121212;border-radius:18px;padding:30px}
.cta-end b{display:block;font-family:Oswald,Arial,sans-serif;text-transform:uppercase;font-size:clamp(34px,4.4vw,54px);line-height:1}
html[lang="hy"] .cta-end b{font-family:"Noto Sans Armenian",Oswald,sans-serif}
.cta-end p{font-size:18px;margin:10px 0 18px}
.cta-end .row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.tel{color:#121212;font-weight:500;font-size:18px;margin-left:8px}
footer{color:var(--mut);margin-bottom:80px}
/* floating buttons */
.fab{position:fixed;right:16px;bottom:16px;display:flex;flex-direction:column;gap:10px;z-index:50}
.fab a{width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 6px 18px rgba(0,0,0,.4)}
.fa-wa{background:#25D366}.fa-tg{background:#229ED9}
@media(min-width:900px){.fab a{width:50px;height:50px}}

/* gift flip card */
.flip{margin-top:14px;perspective:1600px;cursor:pointer;outline:none}
.fl-in{display:grid;transition:transform .9s cubic-bezier(.45,.05,.2,1);transform-style:preserve-3d}
.flip.flipped .fl-in{transform:rotateY(180deg)}
.flip .face{grid-area:1/1;margin-top:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border:3px solid #fff;box-shadow:0 18px 40px rgba(0,0,0,.35);position:relative}
@media(min-width:761px){.flip .face{align-content:center}}
.flip .bk{transform:rotateY(180deg);background:#121212;color:var(--ink)}
.flip .bk{display:flex!important;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.gw{display:grid}.gw .gr{grid-area:1/1;opacity:0;color:var(--y);font-size:clamp(40px,6vw,76px)!important;margin:0!important}.gw .gr.on{opacity:1}
.gs{font-family:Oswald,Arial,sans-serif;letter-spacing:.3em;text-transform:uppercase;color:var(--mut);font-size:14px;margin-top:10px}
.flip .bk .gk{color:var(--y);display:block;margin-top:14px}
.flip .cg{font-size:18px}
.gl{margin:8px 0 0;padding:0;list-style:none;columns:2;column-gap:28px}
.gl li{break-inside:avoid;padding:4px 0 4px 18px;position:relative;line-height:1.35;color:var(--mut)}
.gl li:before{content:"";position:absolute;left:0;top:11px;width:8px;height:8px;border-radius:50%;background:var(--y)}
.turn{position:absolute;right:14px;top:10px;font-size:20px;opacity:.55}
.flip:focus-visible .face{outline:2px solid var(--y);outline-offset:4px}
@media(max-width:760px){.gl{columns:1}}
@media(prefers-reduced-motion:reduce){.gi video{display:none}}
.tf li{min-width:0;overflow-wrap:anywhere;hyphens:auto}
.fedl img{max-width:100%;height:auto;max-height:34px}
a.gb>div{min-width:0}
a.gb p{overflow-wrap:anywhere}
a.gb b{font-size:clamp(32px,3.9vw,48px)}
@media(max-width:760px){
 .gift{grid-template-columns:minmax(0,1fr)}
 .gift-p{flex-direction:column;align-items:stretch}
 .gift-p .btn{white-space:normal;text-align:center}
 .pct{font-size:52px}
 .pr{text-align:left}
 a.gb>div{padding:22px 18px}
 a.gb b{font-size:34px}
 html[lang="hy"] a.gb b{font-size:26px}
 .dd{font-size:16px}
}
'''

JS = rd('script.js.html').replace("var links=[].slice.call(document.querySelectorAll('a.c,a.gb,a.about'));",
  "var links=[].slice.call(document.querySelectorAll('a.c,a.gb,a.about,a.dep-h'));")
JS = JS.replace('})();\n</script>', r'''  // gift certificate: turns by itself to a greeting; hover/tap shows the offer
  var fl=document.getElementById('gift');
  if(fl){var gr=[].slice.call(fl.querySelectorAll('.gr')),gi=0,hold=0,hov=false,vis=false;
    var set=function(f){if(f&&!fl.classList.contains('flipped')){gr[gi].classList.remove('on');gi=(gi+1)%gr.length;gr[gi].classList.add('on')}
      fl.classList.toggle('flipped',f);fl.querySelector('.fr').setAttribute('aria-hidden',f);fl.querySelector('.bk').setAttribute('aria-hidden',!f)};
    gi=gr.length-1;gr.forEach(function(g){g.classList.remove('on')});gr[gi].classList.add('on');
    fl.addEventListener('pointerenter',function(e){if(e.pointerType!=='mouse')return;hov=true;set(false)});fl.addEventListener('pointerleave',function(e){if(e.pointerType!=='mouse')return;hov=false;hold=Date.now()+2500});
    fl.addEventListener('click',function(e){if(e.target.closest('a'))return;set(false);hold=Date.now()+12000});
    fl.addEventListener('focusin',function(){set(false);hold=Date.now()+12000});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting},{threshold:.3}).observe(fl);else vis=true;
    (function tick(){var f=fl.classList.contains('flipped');if(vis&&!hov&&Date.now()>hold){set(!f);f=!f}setTimeout(tick,f?2000:4000)})();
  }
  // hide past departures
  var today=new Date().toISOString().slice(0,10);
  [].forEach.call(document.querySelectorAll('.dl li'),function(li){if(li.dataset.end<today)li.remove()});
  if(!document.querySelector('.dl li')){var d=document.getElementById('dates');if(d)d.remove()}
  // quick picker
  var pb=[].slice.call(document.querySelectorAll('.pick button')),cs=[].slice.call(document.querySelectorAll('a.c'));
  pb.forEach(function(b){b.addEventListener('click',function(){var f=b.dataset.f;
    pb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    cs.forEach(function(c){c.classList.toggle('off',f!=='all'&&(' '+c.dataset.t+' ').indexOf(' '+f+' ')<0)})})});
  // gallery videos: play while visible
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){var g=e.target,v=g.querySelector('video');
      if(e.isIntersecting){if(!v.src)v.src=v.dataset.src;var p=v.play();if(p&&p.then)p.then(function(){g.classList.add('on')}).catch(function(){})}
      else{v.pause()}})},{threshold:.6});
    [].forEach.call(document.querySelectorAll('.gv'),function(g){io.observe(g)});
  }
})();
</script>''')
assert 'hide past departures' in JS and 'a.dep-h' in JS

head = rd('head.html').replace('<meta property="og:description" content="Скалы, вулканы, Арарат, треккинг и горные лыжи. Гиды-альпинисты, всё включено.">',
                               '<meta property="og:description" content="Скалы, вулканы, Арарат, треккинг и горные лыжи. Профессиональные инструкторы, страховка включена.">')
html = head + CSS + '</style></head><body><div class="w">\n' + rd('header.html') + '\n' + '\n'.join(
    [trust, dates, tours, gallery, custom, guides, faq, contact, footer]) + '\n</div>' + fab + JS + '\n</body></html>\n'
open(os.path.join(R, 'index.html'), 'w', encoding='utf-8').write(html)
print('ok', len(html))
