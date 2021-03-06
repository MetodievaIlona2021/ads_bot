from aiogram import types

from keyboards.inline.recruiting_keyboards import services_markup
from loader import dp


@dp.callback_query_handler(text='services')
async def show_services(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text='Услуги агентства', reply_markup=services_markup)


@dp.callback_query_handler(text='recruit_respondents')
async def show_recruit_respondents(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    text = '<b>Успех проекта зависит от рекрутинга и компетентных по данной тематике респондентов.</b>\n\n' \
           'Мы помогаем компаниям и корпорациям достигать большего в своем бизнесе, с помощью верных респондентов, ' \
           'как следствие получение точных данных.\n\n На выходе благодаря верно подобранным респондентам, ' \
           'вы получаете данные, с которыми можно работать, которые можно внедрять, не опасаясь за дальнейшую ' \
           'репутацию вашей компании, пока ваши конкуренты опрашивают не верно подобранных респондентов и затем ' \
           'выводят на рынок продукт, в дальнейшем не пользующийся спросом, Вы блистаете на рынке, получая прибыль ' \
           'от потребителей и захватывая в свои сети все новых и новых клиентов.\n\n' \
           '<b>Агентство ADS осуществляет пререкрут респондентов в торговых центрах в местах скопления людей, ' \
           'снежным комом, через социальную сеть LinkedIn, с помощью наработанных методик.</b>\n\n' \
           'Так же ADS имеет большую базу респондентов (свыше 55 тыс. чел), в нее входят различные эксперты рынков ' \
           'товаров и услуг, респонденты высокого социального достатка (премиум-сегмент) База постоянно пополняется ' \
           'новыми респондентами, не принимавшими ранее участие в исследованиях.\n\n' \
           '- Агентство не прибегает к услугам сторонних рекрутеров. ADS имеет свой укомплектованный штат ' \
           'сотрудников.\n' \
           '- Все ваши проекты курируются непосредственно руководителем агентства, в любой момент Вы сможете с ним ' \
           'связаться напрямую и обсудить каждый вопрос!\n' \
           '- Сотрудниками агентства гарантируется мгновенный ответ на Ваш запрос. Вы оперативно получаете ' \
           'информацию по расценкам и срокам выполнения услуги рекрутинга респондентов.\n' \
           '- Мы предоставляем услуги без предоплаты, Вы платите только за респондента, который принял участие в ' \
           'исследовании и соответствовал всем критериям ТЗ.\n' \
           '- Ваши сотрудники будут избавлены от стрессовой работы с большим количеством рекрутеров, тем самым ' \
           'продуктивность вашего бизнеса повысится!\n' \
           '- Услуги агентства не облагаются НДС.\n' \
           '- Средние сроки проведения работ: 2-3 рабочих дня.'

    await call.message.edit_text(text=text, reply_markup=services_markup, parse_mode='html')


@dp.callback_query_handler(text='recruit_experts')
async def show_recruit_experts(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    text = '<b>Мы поможем Вам в рекрутинге для Вашего проекта.</b>\n\n' \
           'Имеем большую базу экспертов, работающих в различных сферах деятельности.\n' \
           'Мы обладаем значительным опытом в поиске и подборе таких экспертов, как:\n' \
           '- Генеральные, исполнительные, коммерческие, финансовые директора, директора по развитию.\n' \
           '- Заместители генерального директора.\n' \
           '- Представители компаний (технические директора, главные инженеры, руководители групп инженеров).\n' \
           '- Менеджеры по закупкам / снабжению.\n' \
           '- Директора по закупкам / снабжению.\n' \
           '- Эксперты в области теплоснабжения и теплосетей, и прочие эксперты различных сфер деятельности!\n' \
           '- Экспертный опрос — разновидность опроса, в ходе которого респондентами являются эксперты — ' \
           'высококвалифицированные специалисты в определенной области деятельности.\n\n' \
           '<b>Эксперт может участвовать в опросе как:</b>\n' \
           '- генератор, источник идей, гипотез и предложений\n' \
           '- арбитр по оценке имеющихся данных, характеристик и показателей объекта\n' \
           '- аудитор по оценке условий постановки эксперимента\n' \
           '- источник неизвестной исследователю информации, которая служит основой для дальнейшего анализа.'

    await call.message.edit_text(text=text, reply_markup=services_markup, parse_mode='html')
