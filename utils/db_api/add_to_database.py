from utils.db_api.db_commands_gino import add_video, add_review, add_news_item, add_article, add_significant_item, \
    add_case

import asyncio

from utils.db_api.database_gino import create_db


# Используем эту функцию, чтобы заполнить базу данных
async def add_videos():
    await add_video(
        name='UX исследования, рекрутинг респондентов, Опыт Банки Ру',
        description='UX исследования, рекрутинг респондентов, Опыт Банки Ру',
        thumb_url='https://i.ytimg.com/vi/lVLq6GGukRs/hqdefault.jpg',
        url='https://www.youtube.com/embed/lVLq6GGukRs',
        category='interview'
    ),
    await add_video(
        name='НИКОЛАС КОРО, ПОИСК РЕСПОНДЕНТОВ, БРЕНД, ФАТАЛЬНЫЕ ошибки БИЗНЕСА, ОПРЕДЕЛЕНИЕ ЦЕЛЕВОЙ АУДИТОРИИ',
        description='НИКОЛАС КОРО, ПОИСК РЕСПОНДЕНТОВ, БРЕНД, ФАТАЛЬНЫЕ ошибки БИЗНЕСА, ОПРЕДЕЛЕНИЕ ЦЕЛЕВОЙ АУДИТОРИИ',
        thumb_url='https://i.ytimg.com/vi/8zvqPqwar44/hqdefault.jpg',
        url='https://www.youtube.com/embed/8zvqPqwar44',
        category='interview'
    ),
    await add_video(
        name='Исследования собственными силами, рекрутинг респондентов. Опыт Лаборатории Касперского/Интервью!',
        description='Исследования собственными силами, рекрутинг респондентов. Опыт Лаборатории Касперского/Интервью!',
        thumb_url='https://i.ytimg.com/vi/5oxoLMwMYAI/hqdefault.jpg',
        url='https://www.youtube.com/embed/5oxoLMwMYAI',
        category='interview'
    )


async def add_reviews():
    await add_review(
        name='Отзыв от IVI RU о сотрудничестве с ADS по итогам трехлетней совместной работы',
        description='Отзыв от IVI RU о сотрудничестве с ADS по итогам трехлетней совместной работы',
        thumb_url='https://i.ytimg.com/vi/We7JOrC0Vzo/maxresdefault.jpg',
        url='https://www.youtube.com/embed/We7JOrC0Vzo',
        category='review'
    ),
    await add_review(
        name='Отзыв от Банки Ру о сотрудничестве с ADS по итогам двухлетней совместной работы',
        description='Отзыв от Банки Ру о сотрудничестве с ADS по итогам двухлетней совместной работы',
        thumb_url='https://i.ytimg.com/vi/l6syPPRTObk/maxresdefault.jpg',
        url='https://www.youtube.com/embed/l6syPPRTObk',
        category='review'
    ),
    await add_review(
        name='Отзыв от Лаборатории Касперского о сотрудничестве с ADS по итогам шестилетней совместной работы',
        description='Отзыв от Лаборатории Касперского о сотрудничестве с ADS по итогам шестилетней совместной работы',
        thumb_url='https://i.ytimg.com/vi/1EUMBF4g0Qw/maxresdefault.jpg',
        url='https://www.youtube.com/embed/1EUMBF4g0Qw',
        category='review'
    ),
    await add_review(
        name='Отзывы с Facebook',
        description='Отзывы с Facebook',
        thumb_url='https://i.ytimg.com/vi/5oxoLMwMYAI/hqdefault.jpg',
        url='https://m.facebook.com/Adsofficeone/reviews/?ref=bookmarks&mt_nav=0&paipv=1',
        category='review'
    )


async def add_news():
    await add_news_item(
        title='Руководитель Агентства ADS взял интервью у Лаборатории Касперского',
        description='Руководитель Агентства ADS взял интервью у Лаборатории Касперского',
        thumb_url='https://static.wixstatic.com/media/4cd91a_c529af04626a4ab58d33b0e963c4880d~mv2.jpg/v1/fit/w_655%2Ch_435%2Cal_c%2Cq_80/file.jpg',
        url='https://www.adsrecruiting.com/post/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-ads-%D0%B2%D0%B7%D1%8F%D0%BB-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B2%D1%8C%D1%8E-%D1%83-%D0%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D0%B8-%D0%BA%D0%B0%D1%81%D0%BF%D0%B5%D1%80%D1%81%D0%BA%D0%BE%D0%B3%D0%BE',
        category='news'
    ),
    await add_news_item(
        title='Приняли участие в конкурсе Департамента Предпринимательства и Инновационного развития',
        description='Приняли участие в конкурсе Департамента Предпринимательства и Инновационного развития',
        thumb_url='https://static.wixstatic.com/media/fe526f_9d4dd923781e4025a5612fec2a720a0d~mv2.png/v1/fill/w_1300,h_984,al_c/fe526f_9d4dd923781e4025a5612fec2a720a0d~mv2.png',
        url='https://www.adsrecruiting.com/post/novator-msk-2021',
        category='news'
    ),
    await add_news_item(
        title='Руководитель Агентства ADS взял интервью у руководителя UX лаборатории Банки.Ру Максима Марченко',
        description='Руководитель Агентства ADS взял интервью у руководителя UX лаборатории Банки.Ру Максима Марченко',
        thumb_url='https://static.wixstatic.com/media/d952b7_cd3492e0443d4350baad2ac14abb5e1b~mv2.png/v1/fit/w_1000%2Ch_832%2Cal_c/file.png',
        url='https://www.adsrecruiting.com/post/interview-ads-maksim-marchenko',
        category='news'
    )


async def add_articles():
    await add_article(
        name='С чего начинается качественное исследование или почему на респондентах не экономят.',
        text='С чего начинается качественное исследование или почему на респондентах не экономят. '
             'Рано или поздно в бизнесе возникает момент, когда для понимания стратегии необходимо провести '
             'серьезное маркетинговое исследование. То, какие выводы будут сделаны, и насколько они будут полезны, '
             'во многом зависит от качества респондентов, участвующих в опросе. И, если вы решили провести '
             'исследование, на отборе его участников лучше не экономить…\n\n'
             'Читать статью на сайте https://new-retail.ru/marketing/s_chego_nachinaetsya_kachestvennoe_issledovanie_ili_pochemu_na_respondentakh_ne_ekonomyat8712/',
        url='https://new-retail.ru/marketing/s_chego_nachinaetsya_kachestvennoe_issledovanie_ili_pochemu_na_respondentakh_ne_ekonomyat8712/',
        thumb_url='https://static.wixstatic.com/media/86da6968c96d4516959e0f9cbce5252e.jpg/v1/fit/w_1000%2Ch_1000%2Cal_c%2Cq_80/file.jpg',
        category='articles'
    ),
    await add_article(
            name='Прощайте немыслимые бюджеты на маркетинговые исследования!',
            text='Прощайте немыслимые бюджеты на маркетинговые исследования!'
                 'В маркетинговых и социологических исследованиях всегда стоит проблема, связанная с качеством '
                 'рекрутинга респондентов. Это связанно с тем, что во многих маркетинговых компаний подбором '
                 'респондентов занимаются внештатные сотрудники, которые часто грешат при отборе респондентов.\n\n'
                 'Прочитать статью на сайте https://new-retail.ru/marketing/kak_sokratit_byudzhet_na_marketingovye_issledovaniya3874/',
            url='https://new-retail.ru/marketing/kak_sokratit_byudzhet_na_marketingovye_issledovaniya3874/',
            thumb_url='https://static.wixstatic.com/media/4cd91a_25c6bf303f544906a3c5c881a6ffc205~mv2.jpeg/v1/fit/w_800%2Ch_710%2Cal_c%2Cq_80/file.jpeg',
            category='articles'
    ),
    await add_article(
        name='Почему качественный рекрутинг занимает ключевую позицию при отборе респондентов',
        text='Почему качественный рекрутинг занимает ключевую позицию при отборе респондентов'
             'Или частые ошибки исследователя. Топ 3 ошибки.\n\n'
             'Прочитать статью на сайте https://www.marketologi.ru/publikatsii/stati/4073/',
        url='https://www.marketologi.ru/publikatsii/stati/4073/',
        thumb_url='https://static.wixstatic.com/media/a27d24_299a9bd66ff94a23b9ecbe95bcfdee00~mv2_d_5732_4756_s_4_2.jpg/v1/fit/w_1000%2Ch_1000%2Cal_c%2Cq_80/file.jpg',
        category='articles'
    ),
    await add_article(
        name='Руководитель Агентства ADS подготовил статью для Гильдии маркетологов на тему: '
             'Стратегия компании и рекрутинг респондентов.',
        text='Руководитель Агентства ADS подготовил статью для Гильдии маркетологов на тему: '
             'Стратегия компании и рекрутинг респондентов.\n'
             'Прочитать статью на сайте https://www.marketologi.ru/news/consulting/4873/',
        url='https://www.marketologi.ru/news/consulting/4873/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Агентства ADS подготовило новый кейс для Гильдии Маркетологов: " Научно-исследовательский институт '
             'защиты интеллектуальной собственности и Первое Агентство по рекрутингу респондентов ADS рекрутируют '
             'юристов в направлении интеллектуальной.',
        text='Агентства ADS подготовило новый кейс для Гильдии Маркетологов: " Научно-исследовательский институт '
             'защиты интеллектуальной собственности и Первое Агентство по рекрутингу респондентов ADS рекрутируют '
             'юристов в направлении интеллектуальной.\n'
             'Прочитать статью на сайте https://www.marketologi.ru/news/cases/4892/',
        url='https://www.marketologi.ru/news/cases/4892/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Руководитель Агентства ADS взял интервью для New Retail и Гильдии Маркетологов у руководителя UX '
             'лаборатории крупнейшего финансового портала "Банки Ру Максима Марченко."',
        text='Руководитель Агентства ADS взял интервью для New Retail и Гильдии Маркетологов у руководителя UX '
             'лаборатории крупнейшего финансового портала "Банки Ру Максима Марченко." В любой непонятной ситуации '
             'идите к клиентам" Тема интервью: Опыт Банки ру в проведении UX исследований собственными силами.\n'
             'Статья доступна по ссылке https://new-retail.ru/persony/maksim_marchenko_banki_ru_v_lyuboy_neponyatnoy_situatsii_idite_k_klientam9616/'
             '\nВидео интервью полная версия доступна по ссылке: https://www.youtube.com/watch?v=lVLq6GGukRs',
        url='https://new-retail.ru/persony/maksim_marchenko_banki_ru_v_lyuboy_neponyatnoy_situatsii_idite_k_klientam9616/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Руководитель Агентства ADS взял интервью для Гильдии Маркетологов и New Retail у признанного гуру '
             'в сфере брендинга, маркетинга и нейроиследований Николаса Коро на тему: Как определить кто ваша целевая '
             'аудитория?',
        text='Руководитель Агентства ADS взял интервью для Гильдии Маркетологов и New Retail у признанного гуру '
             'в сфере брендинга, маркетинга и нейроиследований Николаса Коро на тему: Как определить кто ваша целевая '
             'аудитория? «Те, кто считают, что целевая аудитория одна – уже ошиблись» Николас Коро, Центр RCB&B.\n'
             'Статья доступна по ссылке https://new-retail.ru/persony/nikolas_koro_tsentr_rcb_b_te_kto_schitayut_chto_tselevaya_auditoriya_odna_uzhe_oshiblis4667/,\n'
             'видео интервью доступно по ссылке. https://youtu.be/8zvqPqwar44',
        url='https://new-retail.ru/persony/nikolas_koro_tsentr_rcb_b_te_kto_schitayut_chto_tselevaya_auditoriya_odna_uzhe_oshiblis4667/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Руководитель Агентства ADS взял интервью у руководителя международных юзабилити-исследований в '
             'Лаборатории Касперского Екатерины Логиновой',
        text='Руководитель Агентства ADS взял интервью у руководителя международных юзабилити-исследований в '
             'Лаборатории Касперского Екатерины Логиновой, Исследования собственными силами, рекрутинг респондентов, '
             'опыт Лаборатории Касперского '
             'https://new-retail.ru/business/ekaterina_loginova_kasperskiy_samoe_vazhnoe_chtoby_chelovek_vo_vremya_obshcheniya_s_nami_chuvstvoval4147/',
        url='https://new-retail.ru/business/ekaterina_loginova_kasperskiy_samoe_vazhnoe_chtoby_chelovek_vo_vremya_obshcheniya_s_nami_chuvstvoval4147/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Почему рекрутинг на дистанционные исследования не дешевле обычного?',
        text='Почему рекрутинг на дистанционные исследования не дешевле обычного?'
             'Прочитать статью на сайте https://www.marketologi.ru/news/consulting/4728/',
        url='https://www.marketologi.ru/news/consulting/4728/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Почему рекрутинг на дистанционные исследования не дешевле обычного?',
        text='Боты и живые люди. Как не получить на выходе недостоверные данные на онлайн-опрос\n'
             'https://www.marketologi.ru/news/consulting/4716/',
        url='https://www.marketologi.ru/news/consulting/4716/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Почему рекрутинг на дистанционные исследования не дешевле обычного?',
        text='Рекрутинг респондентов с помощью партнерской сети. Каких результатов можно добиться, какие плюсы и '
             'минусы?\n'
             'https://www.marketologi.ru/news/consulting/4615/',
        url='https://www.marketologi.ru/news/consulting/4615/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Banki.ru и ADS рекрутируют владельцев малого бизнеса?',
        text='Banki.ru и ADS рекрутируют владельцев малого бизнеса.\n'
             'https://www.marketologi.ru/news/cases/4683/',
        url='https://www.marketologi.ru/news/cases/4683/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Кейс. Банк Открытие и ADS, рекрутируют трудно-доступных респондентов.',
        text='Кейс. Банк Открытие и ADS, рекрутируют трудно-доступных респондентов.\n'
             'https://www.marketologi.ru/news/Case-Competition/4570/',
        url='https://www.marketologi.ru/news/Case-Competition/4570/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Кейс для Гильдии Маркетологов, как Агентство ADS и Лаборатория Касперского с помощью анкеты обратной '
             'связи сделали участие в исследованиях более комфортным',
        text='Кейс для Гильдии Маркетологов, как Агентство ADS и Лаборатория Касперского с помощью анкеты обратной '
             'связи сделали участие в исследованиях более комфортным"\n'
             'https://www.marketologi.ru/news/Case-Competition/4233/',
        url='https://www.marketologi.ru/news/Case-Competition/4233/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Европейская платформа Incling и ADS рекрутируют респондентов на 3-х дневное дневниковое исследование',
        text='Европейская платформа Incling и ADS рекрутируют респондентов на 3-х дневное дневниковое исследование\n'
             'https://www.marketologi.ru/news/cases/4766/',
        url='https://www.marketologi.ru/news/cases/4766/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Почему качественный рекрутинг занимает ключевую позицию в подборе респондентов или частые ошибки '
             'исследователя. Топ 3 ошибки.',
        text='Почему качественный рекрутинг занимает ключевую позицию в подборе респондентов или частые ошибки '
             'исследователя. Топ 3 ошибки.\n'
             'https://www.marketologi.ru/publikatsii/stati/4176/',
        url='https://www.marketologi.ru/publikatsii/stati/4176/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Рекрутинг респондентов на кончиках пальцев или как сделать исследование для респондента '
             'максимально комфортным?',
        text='Рекрутинг респондентов на кончиках пальцев или как сделать исследование для респондента '
             'максимально комфортным?\n'
             'https://www.marketologi.ru/publikatsii/stati/3970/',
        url='https://www.marketologi.ru/publikatsii/stati/3970/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Как сократить бюджет на маркетинговые исследования',
        text='Как сократить бюджет на маркетинговые исследования\n'
             'https://new-retail.ru/marketing/s_chego_nachinaetsya_kachestvennoe_issledovanie_ili_pochemu_na_respondentakh_ne_ekonomyat8712/',
        url='https://new-retail.ru/marketing/s_chego_nachinaetsya_kachestvennoe_issledovanie_ili_pochemu_na_respondentakh_ne_ekonomyat8712/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Прощайте немыслимые бюджеты на маркетинговые исследования!',
        text='Прощайте немыслимые бюджеты на маркетинговые исследования!\n'
             'https://www.marketologi.ru/publikatsii/stati/proshhajjte-nemyslimye-bjudzhety-na-marketingovye-issledovanija/ ',
        url='https://www.marketologi.ru/publikatsii/stati/proshhajjte-nemyslimye-bjudzhety-na-marketingovye-issledovanija/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Рекрутинг респондентов по базе клиента. В чем заключаются ключевые сложности работы с базой клиентов? '
             'Почему ADS не выполняет рекрутинг по базе клиента?',
        text='Рекрутинг респондентов по базе клиента. В чем заключаются ключевые сложности работы с базой клиентов? '
             'Почему ADS не выполняет рекрутинг по базе клиента?\n'
             'https://www.marketologi.ru/publikatsii/stati/4005/',
        url='https://www.marketologi.ru/publikatsii/stati/4005/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Качественный рекрутинг респондентов = долгосрочная прибыль компании.',
        text='Качественный рекрутинг респондентов = долгосрочная прибыль компании.\n'
             'В чем заключается взаимосвязь качественного рекрутинга респондентов и долгосрочной прибыли компании?\n'
             'https://www.marketologi.ru/publikatsii/stati/4433/',
        url='https://www.marketologi.ru/publikatsii/stati/4433/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    ),
    await add_article(
        name='Три основных критерия которым должен соответствовать респондент?',
        text='Три основных критерия которым должен соответствовать респондент?\n'
             'https://www.marketologi.ru/news/consulting/4510/',
        url='https://www.marketologi.ru/news/consulting/4510/',
        thumb_url='https://static.wixstatic.com/media/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png/v1/fit/w_2500,h_1330,al_c/4cd91a_7c02e50f680e47e1910186ffcc0c1e7d.png',
        category='articles'
    )


async def add_significant():
    await add_significant_item(
        name='Маркетинговая исследовательская компания',
        text='<i>Проект</i>\n\n'
             '<b>Оценка качества обслуживания на этапе продаж</b>\n\n'
             '--------------------------------------------\n\n'
             '<i>Подробности</i>\n\n'
             'Мужчины 25-45 лет, владельцы премиальных марок автомобилей (Land Cruiser, BMW, Ауди, Фольцваген '
             'Туарег, Лексус, Мерседес, LandRover, LandCruiser - 2012-2014 г.в). '
             'В исследовании приняло участие 10 тайных покупателей.',
        thumb_url='https://static.wixstatic.com/media/d952b7_5a2c129d8e25422aa9dc8b246b94e8ba~mv2.png',
        category='significant'
    ),
    await add_significant_item(
        name='Российский производитель антивирусного программного обеспечения для дома и бизнеса',
        text='<i>Проект</i>\n\n'
             '<b>Юзабилити-тестирование интерфейса обновленного программного обеспечения</b>\n\n'
             '--------------------------------------------\n\n'
             '<i>Подробности</i>\n\n'
             'Системные администраторы, специализирующиеся на обеспечении антивирусной безопасности корпоративной '
             'сети. Ежеквартальные серии юзабилити-тестирований.',
        thumb_url='https://static.wixstatic.com/media/d952b7_32a3a101cbd74110a99e1a6c7fefda0f~mv2.png',
        category='significant'
    ),
    await add_significant_item(
        name='Маркетинговая исследовательская компания',
        text='<i>Проект</i>\n\n'
             '<b>Тестирование нового дизайна элитной недвижимости</b>\n\n'
             '--------------------------------------------\n\n'
             '<i>Подробности</i>\n\n'
             'Юзабилити-тестирование интерфейса обновленного программного обеспечения. '
             'Потенциальные и реальные покупатели элитной недвижимости в г. Москве. '
             'Опрос был проведен посредством личного интервью face-to-face, skypa и телефонной связи. '
             'Выборка исследования: 90 человек.',
        thumb_url='https://static.wixstatic.com/media/d952b7_3b62bfcb865f45f1b54736238b2a918e~mv2.png',
        category='significant'
    )


async def add_cases():
    await add_case(
        name='Новый кейс для Гильдии маркетологов. ADS и Banki.ru',
        text='При рекрутинге важно было исключить людей, которые не ведут бизнес, а используют юр. лицо для черных '
             'схем, либо вынуждены были открыть ИП по требованию работодателя. Это, как правило, люди ведущие '
             'деятельность в строительной сфере, грузоперевозки, бухгалтерские услуги.\n\n'
             '<b>Проблема</b>: Одной из самых труднодостижимых аудиторий являются предприниматели, в т.ч. '
             'представители малого бизнеса. Не смотря на то, что легко найти информацию о них в интернете, '
             'мотивируется данная ЦА к участию очень сложно. Но как же быть, если специфика компании подразумевает '
             'взаимодействие с предпринимателями и услуги для них?\n\n'
             'Для компания Banki.ru мы взяли сложный процесс рекрутинга и подбора качественных респондентов на '
             'регулярной основе на себя. Требовалось два типа респондентов: 50% в течение последних 6 месяцев '
             'самостоятельно открывали счет для бизнеса (либо регистрируют юридическое лицо или индивидуальный '
             'предприниматель прямо сейчас). 50% имеют опыт самостоятельного открытия счета, но не удовлетворены '
             'своим банком или тарифом и хотели бы его сменить.\n\n'
             'Смотреть кейс на сайте «Гильдии Маркетологов» https://www.marketologi.ru/news/cases/4683/',
        thumb_url='https://static.wixstatic.com/media/fe526f_3218d3d5142a4a2b8695e2ef34987968~mv2.jpg',
        category='cases'
    ),
    await add_case(
        name='ADS и IVI RU',
        text='Кейс пререкрут респондентов с помощью таргетированной рекламы.\n\n'
             'Для запуска таргетированной рекламы мы решили выполнить пререкрут платных подписчиков онлайн '
             'кинотеатров для компании IVI, чтобы в дальнейшем использовать их на будующих проектах , так как '
             'практика показывает, что платных подписчиков искать труднее всего, чаще респонденты выбирают '
             'онлайн просмотр фильмов бесплатно.\n\n'
             '<b>Критерии для подбора были следующие ( их мы сделали на основе предыдущих проектов):</b>\n\n'
             'Мужчины и женщины в возрасте от 20 до 45 лет, которые пользуются платными подписками онлайн '
             'кинотеатров ( окко, иви, мегого, амедиатека идр.)\n'
             'Город проживания не важен. Опрос будет проходить по Skype.\n'
             'Вознаграждение: 1500 рублей на карту.\n'
             'Дата и время на выбор.\n\n'
             '<b>Процесс использования таргетированной рекламы:</b>\n\n'
             'Реклама была запущена в соц. сети Вконтакте, так как данная соц. сеть самая крупная в России и '
             'имеет наибольший охват. При настройке таргетированной рекламы был задан необходимый возраст '
             'респондентов, а в разделе интересов указан сайт компании IVI, так как мы планировали сделать '
             'акцент больше на подписчиках Ivi (на проектах компании Иви они требуются больше всего), но при '
             'этом понимали, что будут попадаться еще и конкуренты.  При данных настройках реклама показывалась '
             'пользователям Вконтакте 20-45 лет, которые зарегистрированы на сайте IVI, что позволяет нам охватить '
             'наиболее подходящую ЦА для наших целей. Показ рекламы был запущен на сутки. По истечении суток мы '
             'получили результат в размере 32 пользователей.\n\n'
             '<b>На выходе получили следующие результаты:</b>\n\n'
             'Платная подписка ИВИ - 18 пользователей.\n'
             'Платная подписка Амедиатека  - 2 пользователя.\n'
             'Платная подписка ОККО - 4 пользователя.\n'
             'Платная подписка Мегого - 2 пользователя.\n'
             'Пользователи платных подписок других онлайн кинотеатров - 2 пользователя.\n'
             'Пользователи бесплатных версий подписок - 4 респондента.\n\n'
             '<b>Выводы</b>: В итоге мы были очень довольны результатами использования таргетированной рекламы, '
             'несколько респондентов с платной подпиской IVI даже удалось привлечь в текущий удаленный проект '
             'для компании IVI, в котором они успешно поучаствовали. Предварительно у данных респондентов были '
             'запрошены скриншоты подписок, что подтверждало их принадлежность к ЦА.\n\n'
             '<b>Из минусов:</b> К сожалению, таргетированную рекламу возможно использовать не на всех проектах, '
             'так как наибольший успех имеют проекты, на которые требуются потребители какого-то конкретного '
             'продукта или услуги и у данного товара или услуги есть своя группа/сайт, либо есть сообщество '
             'интересов, тем самым удается попасть конкретно в ЦА и показывать рекламу точечно. Например, легче '
             'будет найти респондентов, которые покупают корм для кошки определенной марки, так как данных '
             'потенциальных респондентов можно будет найти в группах этой марки/сайте этой марки или в сообществе '
             'для владельцев кошек, притом найти респондентов, которые планируют проходить курсы по маркетингу '
             'будет гораздо сложнее, так как не будет конкретного сообщества/сайта, а будет много различных '
             'вариантов, при которых попасть в нужную ЦА будет сложно + затратно.',
        thumb_url='https://static.wixstatic.com/media/d952b7_f66b9494a70e4d1990bfeb0e2b4d7c0f~mv2.png',
        category='cases'
    ),
    await add_case(
        name='ADS и Банк Открытие',
        text='Рекрутинг респондентов, премиум сегмента. Выборка:30 респондентов Москва и Регионы. Рекрутинг премиум '
             'сегмента всегда сопровождается сложностями, требуется не только найти респондентов с высоким уровнем '
             'дохода, но и срекрутировать их соблюдая все квоты, в данном проекте квоты были: на ведение '
             'предпринимательской деятельности, возраст респондента, пол, уровень дохода от :150 тыс в Москве и '
             ':120 тыс в регионах, семейное положение. При том респонденты из каждого города делились на тех, кто '
             'является предпринимателем и кто является наемным рабочим, а так же были квоты на наличие накоплений и '
             'семейное положение. От всех респондентов требовалось подтверждение причастности к высокодоходному '
             'сегменту.\n\n'
             'В итоге получалось так, что выборка очень сильно сужалась, так как на одного респондента приходилось '
             'много критериев, например, респондент должен быть из Санкт-Петербурга, иметь высокий доход, быть '
             'предпринимателем, иметь накопления и иметь семью. Мы предоставили клиенту статус с потенциальными '
             'респондентами, из которого клиент мог самостоятельно выбрать наиболее подходящих респондентов. '
             'С каждым респондентом предварительно клиент самостоятельно созванивался и проводил небольшой опрос, '
             'чтобы убедиться в том, что респондент действительно им подходит. Мы изначально указывали удобное '
             'время для звонка респонденту.\n\n'
             '<b>Сложнее всего было выполнять рекрутинг респондентов в регионах с данным уровнем дохода и квотой '
             'на ведение предпринимательской деятельности.</b>\n\n'
             '<b>Мы рекрутировали респондентов:</b> с помощью собственной базы, приглашали участников предыдущих '
             'исследований для высокодоходных респондентов, которые уже подтвердили свою принадлежность к ЦА, '
             'так же просили данных респондетов порекомендовать своих знакомых, так как у такой категории респондетов,'
             ' скорее всего, будет соответствующее окружение, особенно интересовали рекомендации респондентов из '
             'регионов, за такую рекомендацию мы так же предлагали денежное вознаграждение. Следующим методом поиска '
             'был поиск респондетов с помощью популярного интернет сервиса, там происходил рекрут людей, которые '
             'продавали премиум поддержанные автомобили, но данный метод не увенчался успехом, люди, не знакомые '
             'с исследованиями или не по рекомендациям часто воспринимают такие предложения как обман. '
             'Так же использовали скрипт поиска по должностям ( искали респондентов с высокой должностью и '
             'предпринимателей), социальные сети и собственное мобильное приложение.\n\n'
             '<b>В итоге мы завершили проект с хорошим результатом</b>, из выборки всех респондентов по всей ЦА, '
             'нам удалось найти всех полностью подходящих респондентов. 4-х клиент нашел своими силами из регионов. '
             'Все респонденты полностью подходили под требования, прислали подтверждения и прошли предварительное '
             'телефонное короткое интервью.\n\n'
             'На выходе компания получила достоверные данные с которыми можно работать и можно внедрять не опасаясь '
             'за дальнейшую репутацию на рынке.\n\n'
             'При следующих сложных проектах мы начнем тестировать рекрутинг с помощью таргетированной рекламы, '
             'впоследствии можно будет увидеть уровень отклика и насколько это будет результативным при рекрутинге '
             'премиум сегмента или потребителей редких товаров и услуг. Таким опытом поделимся позднее.',
        thumb_url='https://static.wixstatic.com/media/4cd91a_14398e87708f4f66ac7afd49c028d644~mv2.jpeg',
        category='cases'
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
# loop.run_until_complete(add_videos())
# loop.run_until_complete(add_reviews())
# loop.run_until_complete(add_news())
# loop.run_until_complete((add_articles()))
# loop.run_until_complete(add_significant())
# loop.run_until_complete(add_cases())
