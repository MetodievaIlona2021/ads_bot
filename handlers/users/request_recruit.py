from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.recruiting_keyboards import recruiting_keyboard, types_research_keyboard, \
    payment_types_keyboard, gender_types_keyboard, get_articles_keyboard, check_info_keyboard
from loader import dp
from states.recruiting_states import RecruitingQuery
from utils.db_api.models import RecruitQuery


@dp.callback_query_handler(text='query_recruit')
async def start_query_recruit(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    text = '<i>Оценка стоимости рекрутинга респондентов.</i>\n\n' \
           'Ответьте пожалуйста в свободной форме на нижеперечисленные вопросы, и ' \
           'мы оперативно сориентируем Вас по срокам и стоимости выполнения рекрутинга респондентов.\n' \
           'Ниже под каждым вопросом мы указали примерный образец ответов.'

    await call.message.answer(text, reply_markup=recruiting_keyboard, parse_mode='html')
    await RecruitingQuery.StartRecruit.set()


@dp.callback_query_handler(text='start_test', state=RecruitingQuery.StartRecruit)
async def enter_email(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)

    await call.message.answer('Введите адрес электронной почты')
    await RecruitingQuery.Email.set()


@dp.message_handler(state=RecruitingQuery.Email)
async def type_research(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)

    await message.answer('Выберете вид исследования', reply_markup=types_research_keyboard)
    await RecruitingQuery.Research.set()


@dp.callback_query_handler(state=RecruitingQuery.Research)
async def basic_requirements(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = call.data
    if data == 'focus_group':
        research_type = 'Фокус-группа'
    elif data == 'hall_test':
        research_type = 'Холл-тест'
    elif data == 'expert_interviews':
        research_type = 'Экспертные интервью'
    elif data == 'usability_testing':
        research_type = 'Юзабилити-тестирование'
    elif data == 'home_visit':
        research_type = 'Домашний визит'
    elif data == 'going_store':
        research_type = 'Поход в магазин'
    elif data == 'secret_shopper':
        research_type = 'Тайный покупатель'
    elif data == 'online_survey':
        research_type = 'Онлайн Опрос'
    elif data == 'phone_interview':
        research_type = 'Телефонное интервью'
    else:
        research_type = 'Другое'
    if research_type == 'Другое':
        await call.message.answer('Укажите другое:')
        await RecruitingQuery.OtherResearchType.set()
    else:
        await state.update_data(research_type=research_type)
        text = 'Укажите основные требования к респондентам в свободной форме: ' \
               'пол, возраст, какой продукт они должны потреблять, их должность, сфера деятельности?\n\n' \
               '<i>Пример ответа: Мужчины и Женщины 50%50 25-45 лет. Все респонденты должны планировать ' \
               'покупку квартиры в Москве в ближайшее 6 месяцев, квартиры комфорт класса. ' \
               'Доход на одного человека в семье не менее: 70 тысяч рублей. Рассматривают покупку квартиры ' \
               'с помощью Ипотеки. Имеют информацию о застройщиках, то есть уже сейчас активно занимаются ' \
               'поиском подходящей квартиры для покупки. Респонденты могут проживать как в Москве так и в ' \
               'ближайшем Подмосковье, но покупку квартиры рассматривают только в Москве. ' \
               'Все респонденты работают, имеют средний уровень дохода, то есть от 70 тыс рублей на ' \
               'респондента в семье.</i>'
        await call.message.answer(text=text, parse_mode='html')
        await RecruitingQuery.BasicRequirements.set()


@dp.message_handler(state=RecruitingQuery.OtherResearchType)
async def basic_requirements_other(message: types.Message, state: FSMContext):
    research_type = message.text
    await state.update_data(research_type=research_type)
    text = 'Укажите основные требования к респондентам в свободной форме: ' \
           'пол, возраст, какой продукт они должны потреблять, их должность, сфера деятельности?\n\n' \
           '<i>Пример ответа: Мужчины и Женщины 50%50 25-45 лет. Все респонденты должны планировать ' \
           'покупку квартиры в Москве в ближайшее 6 месяцев, квартиры комфорт класса. ' \
           'Доход на одного человека в семье не менее: 70 тысяч рублей. Рассматривают покупку квартиры ' \
           'с помощью Ипотеки. Имеют информацию о застройщиках, то есть уже сейчас активно занимаются ' \
           'поиском подходящей квартиры для покупки. Респонденты могут проживать как в Москве так и в ' \
           'ближайшем Подмосковье, но покупку квартиры рассматривают только в Москве. ' \
           'Все респонденты работают, имеют средний уровень дохода, то есть от 70 тыс рублей на ' \
           'респондента в семье.</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.BasicRequirements.set()


@dp.message_handler(state=RecruitingQuery.BasicRequirements)
async def enter_count_respondents(message: types.Message, state: FSMContext):
    basic_requirement = message.text
    await state.update_data(basic_requirement=basic_requirement)
    await message.answer('Введите общее количество респондентов')
    await RecruitingQuery.CountRespondents.set()


@dp.message_handler(state=RecruitingQuery.CountRespondents)
async def get_payments_type(message: types.Message, state: FSMContext):
    count_respondents = message.text
    try:
        count_respondents = int(message.text)
    except ValueError:
        await message.answer('Просьба ввести число')
        return
    await state.update_data(count_respondents=count_respondents)
    await message.answer('Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения '
                         'респондентам по итогам исследования, выберете ответ:\n\n'
                         'кнопка <b>ADS</b> - Потребуется организовать выплату на стороне ADS\n\n'
                         'кнопка <b>Самостоятельно</b> - Моя компания самостоятельно организует выплату '
                         'вознаграждения после исследования', reply_markup=payment_types_keyboard, parse_mode='html')
    await RecruitingQuery.DataRespondent.set()


@dp.callback_query_handler(state=RecruitingQuery.DataRespondent)
async def enter_respondent_data(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = call.data
    if data == 'ADS':
        payments_type = 'Потребуется организовать выплату на стороне ADS'
    else:
        payments_type = 'Моя компания самостоятельно организует выплату вознаграждения после исследования'
    await state.update_data(payments_type=payments_type)
    text = 'Какие данные от респондента потребуются на исследовании?\n\n' \
           '<i>Пример ответа: От респондента потребуется его паспорт.</i>'
    await call.message.answer(text=text, parse_mode='html')
    await RecruitingQuery.StockRespondents.set()


@dp.message_handler(state=RecruitingQuery.StockRespondents)
async def stock_respondents(message: types.Message, state: FSMContext):
    respondent_data = message.text
    await state.update_data(respondent_data=respondent_data)
    text = 'Обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
           'если кто-то из респондентов не дошел мы приглашаем его на следующий день, ' \
           'насколько это критично для Вас?\n\n' \
           '<i>Пример ответа: Потребуются запасные респонденты, количество запасных на Ваше усмотрение.</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.CompanyInfo.set()


@dp.message_handler(state=RecruitingQuery.CompanyInfo)
async def enter_company_info(message: types.Message, state: FSMContext):
    stock_respondents_info = message.text
    await state.update_data(stock_respondents_info=stock_respondents_info)
    text = 'Укажите какую компанию Вы представляете, должность, телефон?\n\n' \
           '<i>Пример ответа: Руководитель исследовательских проектов, Компания: ПИК, телефон: 89167152222</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.Name.set()


@dp.message_handler(state=RecruitingQuery.Name)
async def enter_name(message: types.Message, state: FSMContext):
    company_info = message.text
    await state.update_data(company_info=company_info)
    await message.answer(text='Укажите, пожалуйста, ваше имя')
    await RecruitingQuery.Gender.set()


@dp.message_handler(state=RecruitingQuery.Gender)
async def enter_gender(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Укажите пол', reply_markup=gender_types_keyboard)
    await RecruitingQuery.GetArticles.set()


@dp.callback_query_handler(state=RecruitingQuery.GetArticles)
async def get_articles(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = call.data
    if data == 'man':
        gender = 'мужской'
    else:
        gender = 'женский'
    await state.update_data(gender=gender)
    text = 'Отправляя нам данную форму, вы соглашаетесь на получение статей от компании ADS.'
    await call.message.answer(text=text, reply_markup=get_articles_keyboard)
    await RecruitingQuery.WhatSources.set()


@dp.callback_query_handler(state=RecruitingQuery.WhatSources)
async def what_sources(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = call.data
    if data == 'yes':
        response = 'Да'
    else:
        response = 'Нет'
    await state.update_data(send_articles=response)
    text = 'Из каких источников Вы узнали об Агентстве ADS?\n\n' \
           '<i>Пример: По рекомендации Коллеги (укажите его имя).\n' \
           'Из поисковой системы Гугл/Яндекс, из социальной сети Facebook/LinkedIn.</i>'
    await call.message.answer(text=text, parse_mode='html')
    await RecruitingQuery.CheckInfo.set()


@dp.message_handler(state=RecruitingQuery.CheckInfo)
async def check_info(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    sources = message.text
    await state.update_data(sources=sources)
    data = await state.get_data()
    email = data.get('email')
    research_type = data.get('research_type')
    basic_requirement = data.get('basic_requirement')
    count_respondents = data.get('count_respondents')
    payments_type = data.get('payments_type')
    respondent_data = data.get('respondent_data')
    stock_respondents_info = data.get('stock_respondents_info')
    company_info = data.get('company_info')
    name = data.get('name')
    gender = data.get('gender')
    send_articles = data.get('send_articles')

    recruit_query = RecruitQuery(email=email,
                                 user_id=user_id,
                                 research_type=research_type,
                                 basic_requirements=basic_requirement,
                                 count_respondents=count_respondents,
                                 payments_type=payments_type,
                                 respondent_data=respondent_data,
                                 stock_respondents_info=stock_respondents_info,
                                 company_info=company_info,
                                 name=name,
                                 gender=gender,
                                 send_articles=send_articles,
                                 sources=sources
                                 )
    await state.update_data(recruit_query=recruit_query)

    text = f'Подтверждаете ли Вы введенную информацию:\n\n' \
           f'1.Введите адрес электронной почты:\n' \
           f'<i>Ваш ответ: {email}</i>\n\n' \
           f'2.Выберете вид исследования:\n' \
           f'<i>Ваш ответ: {research_type}</i>\n\n' \
           f'3.Укажите основные требования к респондентам в свободной форме:\n' \
           f'<i>Ваш ответ: {basic_requirement}</i>\n\n' \
           f'4.Введите общее количество респондентов:\n' \
           f'<i>Ваш ответ: {count_respondents}</i>\n\n' \
           f'5.Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения ' \
           f'респондентам по итогам исследования:\n' \
           f'<i>Ваш ответ: {payments_type}</i>\n\n' \
           f'6.Какие данные от респондента потребуются на исследовании:\n' \
           f'<i>Ваш ответ: {respondent_data}</i>\n\n' \
           f'7.Обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
           f'если кто-то из респондентов не дошел мы приглашаем его на следующий день, ' \
           f'насколько это критично для Вас:\n' \
           f'<i>Ваш ответ: {stock_respondents_info}</i>\n\n' \
           f'8.Укажите какую компанию Вы представляете, должность, телефон:\n' \
           f'<i>Ваш ответ: {company_info}</i>\n\n' \
           f'9.Укажите, пожалуйста, ваше имя:\n' \
           f'<i>Ваш ответ: {name}</i>\n\n' \
           f'10.Укажите пол:\n' \
           f'<i>Ваш ответ: {gender}</i>\n\n' \
           f'11.Отправляя нам данную форму, вы соглашаетесь на получение статей от компании ADS:\n' \
           f'<i>Ваш ответ: {send_articles}</i>\n\n' \
           f'12.Из каких источников Вы узнали об Агентстве ADS:\n' \
           f'<i>Ваш ответ: {sources}</i>\n\n'
    await message.answer(text=text, parse_mode='html', reply_markup=check_info_keyboard)
    await RecruitingQuery.FinishRecruit.set()


@dp.callback_query_handler(text='correct', state=RecruitingQuery.FinishRecruit)
async def correct_info(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    recruit_query: RecruitQuery = data.get('recruit_query')
    await recruit_query.create()

    await call.message.answer('Большое спасибо. В ближайшее время я сообщу Вам информацию по стоимости, '
                              'срокам и возможности реализации проекта.')
    await state.reset_state()


@dp.callback_query_handler(text='incorrect', state=RecruitingQuery.FinishRecruit)
async def incorrect_info(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(text='Для возврата в главное меню, нажмите /start')
    await state.reset_state()


@dp.callback_query_handler(text='cancel_test', state=RecruitingQuery.StartRecruit)
async def get_cancel_test(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.reset_state()
    await call.message.answer(text='Для возврата в главное меню, нажмите /start')
