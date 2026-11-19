import os
H = os.path.dirname(os.path.abspath(__file__))
def T(ru, en, hy): return f'<span lang="ru">{ru}</span><span lang="en">{en}</span><span lang="hy">{hy}</span>'
guides = open(f'{H}/guides.html').read().strip().replace('<section id="guides">', '<section id="guides" class="gsec">')

why = [
 (('Профессиональные инструкторы','Professional instructors','Պրոֆեսիոնալ հրահանգիչներ'),
  ('Каждую группу ведут профессиональные инструкторы по альпинизму и скалолазанию. На скалах их всегда не меньше двух: один готовит маршрут, другой страхует. Без исключений.','Every group is led by professional mountaineering and climbing instructors. On rock there are always at least two: one rigs the route, the other belays. No exceptions.','Յուրաքանչյուր խումբ առաջնորդում են լեռնագնացության և մագլցման պրոֆեսիոնալ հրահանգիչներ։ Ժայռերին նրանք միշտ առնվազն երկուսն են՝ մեկը պատրաստում է երթուղին, մյուսը ապահովագրում։ Առանց բացառության։')),
 (('Страховка в цене','Insurance included','Ապահովագրությունը գնի մեջ'),
  ('Страховка участника входит в каждый наш тур — отдельно оформлять не нужно.','Participant insurance is included in every tour — nothing to arrange separately.','Մասնակցի ապահովագրությունը ներառված է յուրաքանչյուր տուրում՝ առանձին ձևակերպել պետք չէ։')),
 (('Маленькие группы','Small groups','Փոքր խմբեր'),
  ('На скалах — до 8 человек, на лыжах — до 6. Инструктор видит каждого и подстраивает темп.','Up to 8 people on rock, up to 6 on skis. The instructor sees everyone and sets the pace to suit.','Ժայռերին՝ մինչև 8 հոգի, դահուկներին՝ մինչև 6։ Հրահանգիչը տեսնում է յուրաքանչյուրին և հարմարեցնում տեմպը։')),
 (('Снаряжение наше','Gear provided','Հանդերձանքը մերն է'),
  ('Верёвки, системы, каски, скальные туфли, палатки, спальники — проверенные, на всех участников.','Ropes, harnesses, helmets, climbing shoes, tents, sleeping bags — checked and enough for everyone.','Պարաններ, համակարգեր, սաղավարտներ, ժայռային կոշիկներ, վրաններ, քնապարկեր՝ ստուգված, բոլոր մասնակիցների համար։')),
 (('План под погоду','Plans that follow the weather','Պլան՝ ըստ եղանակի'),
  ('В горах решает погода. Если надо — меняем дни местами или вершину, чтобы вы получили лучший день, а не галочку.','In the mountains the weather decides. When needed we swap days or the peak so you get the best day, not just a tick.','Լեռներում եղանակն է որոշում։ Անհրաժեշտության դեպքում փոխում ենք օրերի հերթականությունը կամ գագաթը, որ ստանաք լավագույն օրը, ոչ թե պարզապես նշում։')),
 (('По-русски, по-английски, по-армянски','Russian, English, Armenian','Ռուսերեն, անգլերեն, հայերեն'),
  ('Говорим на вашем языке, цены показываем в вашей валюте: рубли, драмы или евро.','We speak your language and show prices in your currency: roubles, drams or euros.','Խոսում ենք ձեր լեզվով, գները ցույց ենք տալիս ձեր արժույթով՝ ռուբլի, դրամ կամ եվրո։')),
]

tours = [('../skaly-i-vulkan/',('Скалы и вулканы','Rocks and Volcanoes','Ժայռեր և հրաբուխներ')),('../aragats/',('Арагац, Северная','Aragats, North peak','Արագած, Հյուսիսային')),('../ararat/',('Арарат','Ararat','Արարատ')),('../trekking/',('Армения пешком','Armenia on Foot','Հայաստան ոտքով')),('../extreme-wine/',('Экстрим вайн тур','Extreme wine tour','Էքստրիմ գինու տուր')),('../weekend/',('Скалы за выходные','Rocks in a weekend','Ժայռեր հանգստյան օրերին')),('../ski/',('Горные лыжи с нуля','Skiing from scratch','Լեռնադահուկ զրոյից'))]
books = [('../gory/',('Горы Армении','Mountains of Armenia','Հայաստանի լեռները')),('../tct/',('Транскавказская тропа','Transcaucasian Trail','Անդրկովկասյան արահետ')),('../gaidbuk/',('Скалы Армении','Rocks of Armenia','Հայաստանի ժայռերը'))]

def links(items):
    return ''.join(f'<a href="{h}">{T(*n)} →</a>' for h, n in items)

body = f'''<header class="top"><div class="wrap">
  <a class="lockup" href="../"><img src="img/logo.png" alt="White Irbis"><span class="sl"><span class="s1">Follow the</span><span class="s2">White <b>Irbis</b></span></span></a>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-l="ru" aria-pressed="true">RU</button><button type="button" data-l="en" aria-pressed="false">EN</button><button type="button" data-l="hy" aria-pressed="false">ARM</button></div>
</div></header>

<section class="hero" id="top">
  <div class="hero-media" aria-hidden="true"><img src="img/hero.jpg" alt="" style="object-position:50% 30%"></div>
  <div class="wrap">
    <span class="alt">{T("О нас","About us","Մեր մասին")}</span>
    <h1>White<br><em>Irbis</em></h1>
    <p class="sub">{T("Горная команда из Еревана. Водим людей в горы Армении с 2003 года: скалы, вершины, тропы и лыжи — с профессиональными инструкторами, которые знают эти горы лучше всех.","A mountain team from Yerevan. We have been taking people into the mountains of Armenia since 2003: rock, summits, trails and skiing — with professional instructors who know these mountains best.","Լեռնային թիմ Երևանից։ 2003 թվականից մարդկանց տանում ենք Հայաստանի լեռներ՝ ժայռեր, գագաթներ, արահետներ և դահուկներ՝ պրոֆեսիոնալ հրահանգիչների հետ, ովքեր այս լեռներն ամենալավն են ճանաչում։")}</p>
    <div class="row"><a class="cta" href="#price">{T("Написать нам","Message us","Գրել մեզ")}</a></div>
  </div>
</section>

<section class="facts"><div class="wrap"><dl>
  <div><dt>{T("Первая группа","First group","Առաջին խումբը")}</dt><dd>2003</dd></div>
  <div><dt>{T("Уже сходили с нами","Already been with us","Արդեն եղել են մեզ հետ")}</dt><dd>{T("1 000+ человек","1,000+ people","1 000+ մարդ")}</dd></div>
  <div><dt>{T("Самый высокий тур","Highest tour","Ամենաբարձր տուրը")}</dt><dd>{T("Арарат, 5 137 м","Ararat, 5,137 m","Արարատ, 5 137 մ")}</dd></div>
  <div><dt>{T("Наши инструкторы ходили","Our instructors have climbed","Մեր հրահանգիչները եղել են")}</dt><dd>{T("От Альп до Гималаев","Alps to Himalayas","Ալպերից Հիմալայներ")}</dd></div>
</dl></div></section>

<section id="story"><div class="wrap st">
  <div>
    <span class="eyebrow">{T("Кто мы","Who we are","Ով ենք մենք")}</span>
    <h2 class="h2">Follow the White Irbis</h2>
    <p class="lead">{T("Ирбис — снежный барс, хозяин высоких гор. Наш девиз — отсылка к двум историям. Алиса пошла за Белым Кроликом, провалилась в нору и попала в Страну чудес. Нео в «Матрице» последовал за белым кроликом и увидел настоящий мир. Мы предлагаем последовать за White Irbis: из города, офиса и привычных дел — в горы, где всё по-настоящему и немного чудесно.","The irbis is the snow leopard, master of the high mountains. Our motto nods to two stories. Alice followed the White Rabbit down the rabbit hole and found Wonderland. In The Matrix, Neo followed the white rabbit and saw the real world. We invite you to follow the White Irbis: out of the city, the office and the routine, into the mountains, where everything is real and a little bit of a wonder.","Իրբիսը ձյունե ընձառյուծն է՝ բարձր լեռների տերը։ Մեր կարգախոսը հղում է երկու պատմության։ Ալիսը հետևեց Սպիտակ ճագարին, ընկավ փոսը և հայտնվեց Հրաշքների աշխարհում։ «Մատրիցայում» Նեոն հետևեց սպիտակ ճագարին և տեսավ իրական աշխարհը։ Մենք առաջարկում ենք հետևել White Irbis-ին՝ քաղաքից, գրասենյակից և սովորական գործերից դեպի լեռներ, որտեղ ամեն ինչ իրական է և մի քիչ հրաշալի։")}</p>
    <p class="lead">{T("Мы — альпинисты, а не турагентство. Наша команда — профессиональные инструкторы по альпинизму, скалолазанию и горным лыжам. Мы сами ходим на вершины по всему миру и сами ведём каждую группу: от первого выхода на скалу до восхождения на Арарат.","We are mountaineers, not a travel agency. Our team is made up of professional mountaineering, climbing and ski instructors. We climb peaks around the world ourselves and lead every group ourselves — from a first day on rock to the summit of Ararat.","Մենք ալպինիստներ ենք, ոչ թե տուրիստական գործակալություն։ Մեր թիմը լեռնագնացության, մագլցման և լեռնադահուկային սպորտի պրոֆեսիոնալ հրահանգիչներ են։ Ինքներս ենք բարձրանում գագաթներ ամբողջ աշխարհում և ինքներս ենք առաջնորդում յուրաքանչյուր խումբ՝ ժայռի վրա առաջին ելքից մինչև Արարատի գագաթ։")}</p>
  </div>
  <figure style="margin:0"><img src="img/belay.jpg" alt="Инструктор White Irbis на станции над ущельем" loading="lazy"></figure>
</div></section>

{guides}

<section id="partners"><div class="wrap">
  <span class="eyebrow">{T("Партнёры","Partners","Գործընկերներ")}</span>
  <h2 class="h2">{T("Мы в федерации","Part of the federation","Մենք ֆեդերացիայում ենք")}</h2>
  <div class="pt">
    <div class="ptc ptf">
      <a class="flogo" href="https://armalp.am/" target="_blank" rel="noopener"><img src="img/federation.jpg" width="1000" height="460" alt="Логотипы Федерации альпинизма и горного туризма Армении и UIAA" loading="lazy"></a>
      <div>
      <h3>{T("Федерация альпинизма и горного туризма Армении","Armenian Mountaineering and Mountain Tourism Federation","Հայաստանի լեռնագնացության և լեռնային զբոսաշրջության ֆեդերացիա")}</h3>
      <p>{T("Национальная федерация, которая с 2011 года отвечает за альпинизм, горный туризм и скалолазание в стране: проводит сборы, обучение и семинары. В октябре 2025 года стала полноправным членом UIAA — Международной федерации альпинизма и скалолазания.","The national federation responsible since 2011 for mountaineering, hiking and climbing in the country: it runs training camps, courses and seminars. In October 2025 it became a full member of the UIAA, the International Climbing and Mountaineering Federation.","Ազգային ֆեդերացիա, որը 2011 թվականից պատասխանատու է երկրում լեռնագնացության, լեռնային զբոսաշրջության և մագլցման համար՝ անցկացնում է հավաքներ, ուսուցումներ և սեմինարներ։ 2025 թ. հոկտեմբերին դարձավ UIAA-ի՝ Լեռնագնացության և մագլցման միջազգային ֆեդերացիայի լիիրավ անդամ։")}</p>
      <p class="ptn">{T("Антуан Ананян — вице-президент федерации.","Antoine Ananyan is the federation's vice-president.","Անտուան Անանյանը ֆեդերացիայի փոխնախագահն է։")}</p>
      </div>
    </div>
  </div>
</div></section>

<section class="inc" id="why"><div class="wrap">
  <span class="eyebrow">{T("Важно знать","Good to know","Կարևոր է իմանալ")}</span>
  <h2 class="h2">{T("Почему с нами спокойно","Why you're in safe hands","Ինչու է մեզ հետ հանգիստ")}</h2>
  <div class="prac">
{chr(10).join(f'    <div><h3>{T(*h)}</h3><p>{T(*p)}</p></div>' for h, p in why)}
  </div>
</div></section>

<section id="custom"><div class="wrap">
  <span class="eyebrow">{T("Кроме туров","Beyond the tours","Տուրերից բացի")}</span>
  <h2 class="h2">{T("Сделаем по-вашему","We'll do it your way","Կանենք ձեր ձևով")}</h2>
  <div class="pt">
    <div class="ptc">
      <h3>{T("Индивидуально","Tailor-made","Անհատական")}</h3>
      <p>{T("Любую программу соберём под вас: даты, маршрут, уровень, длительность. Семья, друзья, клуб или компания — личный инструктор, своя машина и свой темп.","We'll build any programme around you: dates, route, level, length. Family, friends, a club or a company — a private instructor, your own vehicle and your own pace.","Ցանկացած ծրագիր կկազմենք ձեզ համար՝ ամսաթվեր, երթուղի, մակարդակ, տևողություն։ Ընտանիք, ընկերներ, ակումբ կամ ընկերություն՝ անհատական հրահանգիչ, ձեր մեքենան և ձեր տեմպը։")}</p>
      <p class="ptn">{T("Однодневный выход, восхождение, скалы или неделя по Армении — напишите, что хотите.","A day out, a summit, rock climbing or a week around Armenia — tell us what you want.","Մեկօրյա ելք, վերելք, ժայռեր կամ մեկ շաբաթ Հայաստանով՝ գրեք, ինչ եք ուզում։")}</p>
    </div>
    <div class="ptc">
      <h3>{T("Прокат снаряжения","Gear rental","Հանդերձանքի վարձույթ")}</h3>
      <p>{T("Идёте в горы сами? Дадим снаряжение напрокат: палатки, спальники, коврики, каски, системы, верёвки, скальные туфли и другое.","Heading out on your own? We rent out gear: tents, sleeping bags, mats, helmets, harnesses, ropes, climbing shoes and more.","Լեռներ եք գնում ինքնուրույն։ Վարձով կտանք հանդերձանք՝ վրաններ, քնապարկեր, ներքնակներ, սաղավարտներ, համակարգեր, պարաններ, ժայռային կոշիկներ և այլն։")}</p>
      <p class="ptn">{T("Напишите, что нужно и на какие даты, — подготовим.","Tell us what you need and for which dates — we'll get it ready.","Գրեք, ինչ է պետք և որ ամսաթվերին՝ կպատրաստենք։")}</p>
    </div>
  </div>
</div></section>

<section id="what"><div class="wrap wh">
  <div>
    <span class="eyebrow">{T("Туры","Tours","Տուրեր")}</span>
    <h2 class="h2">{T("Куда мы водим","Where we go","Ուր ենք տանում")}</h2>
    <div class="lk">{links(tours)}</div>
  </div>
  <div>
    <span class="eyebrow">{T("Гайдбуки","Guidebooks","Ուղեցույցներ")}</span>
    <h2 class="h2">{T("Что мы знаем","What we know","Ինչ գիտենք")}</h2>
    <div class="lk">{links(books)}</div>
  </div>
</div></section>

<section class="price" id="price"><div class="wrap">
  <div>
    <span class="eyebrow" style="color:var(--eye-ink)">{T("Контакты","Contacts","Կոնտակտներ")}</span>
    <div class="big" style="font-size:clamp(44px,6vw,80px)">{T("Едем в горы?","Off to the mountains?","Գնո՞ւմ ենք լեռներ")}</div>
    <ul>
      <li>{T("Подберём тур или вершину под ваш опыт","We'll match a tour or peak to your experience","Կընտրենք տուր կամ գագաթ՝ ըստ ձեր փորձի")}</li>
      <li>{T("Закрытые группы, клубы и компании — по запросу","Private groups, clubs and companies on request","Փակ խմբեր, ակումբներ և ընկերություններ՝ ըստ հարցման")}</li>
    </ul>
  </div>
  <div class="contact">
    <h3>{T("Напишите нам","Message us","Գրեք մեզ")}</h3>
    <p>{T("Ответим в WhatsApp или Telegram.","We'll reply on WhatsApp or Telegram.","Կպատասխանենք WhatsApp-ով կամ Telegram-ով։")}</p>
    %%CONTACT%%
  </div>
</div></section>

<footer><div class="wrap">White Irbis · whiteirbis.am · +374 91 470 331<br><a href="../">{T("Все туры и гайдбуки","All tours and guidebooks","Բոլոր տուրերն ու ուղեցույցները")}</a></div></footer>
'''
open(f'{H}/o-nas_body.html', 'w').write(body)
print('ok', len(body))
