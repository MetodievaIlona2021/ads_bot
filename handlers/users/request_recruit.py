import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from data.config import RANGE_TABLE_NAME
from keyboards.inline.recruiting_keyboards import recruiting_keyboard, types_research_keyboard, \
    payment_types_keyboard, gender_types_keyboard, get_articles_keyboard, check_info_keyboard, screening_keyboard, \
    screening_criteria_keyboard, youtube_tiktok_keyboard
from loader import dp, bot
from states.recruiting_states import RecruitingQuery
from utils.db_api.models import RecruitQuery
from utils.google_sheets_api import GoogleSheet

RECRUIT_PHRASE = ['Цена', 'Стоимость', 'Сроки', 'Найти', 'Рекрут', 'Сколько стоит', 'Каковы сроки']


@dp.message_handler(filters.Text(startswith=RECRUIT_PHRASE, ignore_case=True))
async def start_recruit(message: types.Message):
    text = '<i>Оценка стоимости рекрутинга респондентов.</i>\n\n' \
           'Ответьте пожалуйста в свободной форме на нижеперечисленные вопросы, и ' \
           'мы оперативно сориентируем Вас по срокам и стоимости выполнения рекрутинга респондентов.\n' \
           'Ниже под каждым вопросом мы указали примерный образец ответов.'

    await message.answer(text, reply_markup=recruiting_keyboard, parse_mode='html')
    await RecruitingQuery.StartRecruit.set()


@dp.callback_query_handler(text='query_recruit')
async def start_query_recruit(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    text = '<i>Оценка стоимости рекрутинга респондентов.</i>\n\n' \
           'Ответьте пожалуйста в свободной форме на нижеперечисленные вопросы, и ' \
           'мы оперативно сориентируем Вас по срокам и стоимости выполнения рекрутинга респондентов.\n' \
           'Ниже под каждым вопросом мы указали примерный образец ответов.'

    await call.message.answer(text, reply_markup=recruiting_keyboard, parse_mode='html')
    await RecruitingQuery.StartRecruit.set()


# 1. Укажите пожалуйста вашу должность и название компании, телефон и ник ней в телеграм.
@dp.callback_query_handler(text='start_test', state=RecruitingQuery.StartRecruit)
async def enter_company_info(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    text = 'Укажите, пожалуйста, какую компанию Вы представляете, должность, телефон, никнейм в Телеграм?\n\n' \
           '<i>Пример ответа: Руководитель исследовательских проектов, Компания: ПИК, ' \
           'телефон: 89167152222, никнейм: @name</i>'
    await call.message.answer(text=text, parse_mode='html')
    await RecruitingQuery.CompanyInfo.set()


# 2. Вид исследования? Тут выбрать из предложенного.
@dp.message_handler(state=RecruitingQuery.CompanyInfo)
async def type_research(message: types.Message, state: FSMContext):
    company_info = message.text
    await state.update_data(company_info=company_info)

    await message.answer('Выберете вид исследования', reply_markup=types_research_keyboard)
    await RecruitingQuery.Research.set()


# 3. Длительность исследования (час, два часа)
@dp.callback_query_handler(state=RecruitingQuery.Research)
async def enter_survey_time(call: types.CallbackQuery, state: FSMContext):
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
        await call.message.answer('Длительность исследования?\n\n'
                                  '<i>Пример ответа: час, два часа</i>', parse_mode='html')
        await RecruitingQuery.SurveyTime.set()


@dp.message_handler(state=RecruitingQuery.OtherResearchType)
async def enter_survey_time_other(message: types.Message, state: FSMContext):
    research_type = message.text
    await state.update_data(research_type=research_type)
    await message.answer('Длительность исследования?\n\n'
                         '<i>Пример ответа: час, два часа</i>', parse_mode='html')
    await RecruitingQuery.SurveyTime.set()


# 4. Укажите в свободной форме какая целевая аудитория вам требуется для исследования?
@dp.message_handler(state=RecruitingQuery.SurveyTime)
async def enter_target_audience(message: types.Message, state: FSMContext):
    survey_time = message.text
    await state.update_data(survey_time=survey_time)
    await message.answer('Укажите в свободной форме какая целевая аудитория Вам требуется для исследования?\n\n'
                         '<i>Пример ответа: покупатели жилья ПИК</i>', parse_mode='html')
    await RecruitingQuery.TargetAudience.set()


# 5. Выплата вознаграждения будет на вашей стороне или адс.
@dp.message_handler(state=RecruitingQuery.TargetAudience)
async def get_payments_type(message: types.Message, state: FSMContext):
    target_audience = message.text
    await state.update_data(target_audience=target_audience)
    await message.answer('Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения '
                         'респондентам по итогам исследования, выберете ответ:\n\n'
                         'кнопка <b>ADS</b> - Потребуется организовать выплату на стороне ADS\n\n'
                         'кнопка <b>Самостоятельно</b> - Моя компания самостоятельно организует выплату '
                         'вознаграждения после исследования', reply_markup=payment_types_keyboard, parse_mode='html')
    await RecruitingQuery.PaymentsType.set()


# 6. Какой бюджет вы закладываете на рекрутинг респондентов?
# (Исходя из это мы можем предложить вам один из трёх вариантов по стоимости подбора)
@dp.callback_query_handler(state=RecruitingQuery.PaymentsType)
async def enter_budget(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = call.data
    if data == 'payment_ads':
        payments_type = 'Потребуется организовать выплату на стороне ADS'
    else:
        payments_type = 'Моя компания самостоятельно организует выплату вознаграждения после исследования'
    await state.update_data(payments_type=payments_type)
    text = 'Какой бюджет Вы закладываете на рекрутинг респондентов?\n' \
           '(Исходя из это мы можем предложить вам один из трёх вариантов по стоимости подбора)'
    await call.message.answer(text=text, parse_mode='html')
    await RecruitingQuery.Budget.set()


# 7. Откуда узнали о адс? Варианты указать
@dp.message_handler(state=RecruitingQuery.Budget)
async def get_sources(message: types.Message, state: FSMContext):
    budget = message.text
    await state.update_data(budget=budget)
    text = 'Из каких источников Вы узнали об Агентстве ADS?\n\n' \
           '<i>Пример: По рекомендации Коллеги (укажите его имя).\n' \
           'Из поисковой системы Гугл/Яндекс, из социальной сети Facebook/LinkedIn.</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.WhatSources.set()


# 8. Какие данные потребуются от Респондентов ( пример паспорт, прочее)
@dp.message_handler(state=RecruitingQuery.WhatSources)
async def enter_respondent_data(message: types.Message, state: FSMContext):
    sources = message.text
    await state.update_data(sources=sources)
    text = 'Какие данные от респондента потребуются на исследовании?\n\n' \
           '<i>Пример ответа: От респондента потребуется его паспорт.</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.DataRespondent.set()


# 9. Потребуется ли вам двойной запас Респондентов на случай неявки участника на исследование
# обычно мы и продолжить этот вопрос из таблицы его могли бы взять пожалуйста.
@dp.message_handler(state=RecruitingQuery.DataRespondent)
async def stock_respondents(message: types.Message, state: FSMContext):
    respondent_data = message.text
    await state.update_data(respondent_data=respondent_data)
    text = 'Потребуется ли вам двойной запас Респондентов на случай неявки участника на исследование, ' \
           'обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
           'если кто-то из респондентов не дошел мы приглашаем его на следующий день, ' \
           'насколько это критично для Вас?\n\n' \
           '<i>Пример ответа: Потребуются запасные респонденты, количество запасных на Ваше усмотрение.</i>'
    await message.answer(text=text, parse_mode='html')
    await RecruitingQuery.CheckInfo.set()


# @dp.callback_query_handler(text='start_test', state=RecruitingQuery.StartRecruit)
# async def enter_basic_requirements(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     text = 'Укажите основные требования к респондентам в свободной форме: ' \
#            'пол, возраст, какой продукт они должны потреблять, их должность, сфера деятельности?\n\n' \
#            '<i>Пример ответа: Мужчины и Женщины 50%50 25-45 лет. Все респонденты должны планировать ' \
#            'покупку квартиры в Москве в ближайшее 6 месяцев, квартиры комфорт класса. ' \
#            'Доход на одного человека в семье не менее: 70 тысяч рублей. Рассматривают покупку квартиры ' \
#            'с помощью Ипотеки. Имеют информацию о застройщиках, то есть уже сейчас активно занимаются ' \
#            'поиском подходящей квартиры для покупки. Респонденты могут проживать как в Москве так и в ' \
#            'ближайшем Подмосковье, но покупку квартиры рассматривают только в Москве. ' \
#            'Все респонденты работают, имеют средний уровень дохода, то есть от 70 тыс рублей на ' \
#            'респондента в семье.</i>'
#
#     await call.message.answer(text=text, parse_mode='html')
#     await RecruitingQuery.BasicRequirements.set()
#
#
# @dp.message_handler(state=RecruitingQuery.BasicRequirements)
# async def enter_screening_question(message: types.Message, state: FSMContext):
#     basic_requirement = message.text
#     await state.update_data(basic_requirement=basic_requirement)
#     text = 'Нужно ли заполнять скрининговую анкету на каждого респондента? ' \
#            'Мы можем предоставить ответы респондента на вопросы скринговой анкеты в виде ' \
#            'электронной таблицы, устроит ли это Вас?'
#
#     await message.answer(text=text, parse_mode='html', reply_markup=screening_keyboard)
#     await RecruitingQuery.ScreeningQuestionnaire.set()
#
#
# @dp.callback_query_handler(state=RecruitingQuery.ScreeningQuestionnaire)
# async def enter_important_criteria(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'yes_scr':
#         screening_question = 'Да'
#     else:
#         screening_question = 'Нет'
#     await state.update_data(screening_question=screening_question)
#     await call.message.answer('Все ли важные критерии прописаны в скринере?', parse_mode='html',
#                               reply_markup=screening_criteria_keyboard)
#     await RecruitingQuery.ImportantCriteria.set()
#
#
# @dp.callback_query_handler(state=RecruitingQuery.ImportantCriteria)
# async def enter_project_timeline(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'yes_criteria':
#         screening_criteria = 'Да'
#     else:
#         screening_criteria = 'Нет'
#     await state.update_data(screening_criteria=screening_criteria)
#     await call.message.answer('Каковы предварительные сроки проведения проекта?', parse_mode='html')
#     await RecruitingQuery.ProjectTimeline.set()
#
#
# @dp.message_handler(state=RecruitingQuery.ProjectTimeline)
# async def enter_other_criteria(message: types.Message, state: FSMContext):
#     project_timeline = message.text
#     await state.update_data(project_timeline=project_timeline)
#     await message.answer('Планируется ли добавление в процессе рекрута респондентов каких-либо '
#                          'дополнительных критериев, ранее не прописанных в ТЗ?', parse_mode='html')
#     await RecruitingQuery.OtherCriteria.set()
#
#
# @dp.message_handler(state=RecruitingQuery.OtherCriteria)
# async def enter_requirements_respondent(message: types.Message, state: FSMContext):
#     other_criteria = message.text
#     await state.update_data(other_criteria=other_criteria)
#     await message.answer('Что от респондента потребуется выполнить в ходе исследования?', parse_mode='html')
#     await RecruitingQuery.RequirementsRespondent.set()
#
#
# @dp.message_handler(state=RecruitingQuery.RequirementsRespondent)
# async def enter_respondent_data(message: types.Message, state: FSMContext):
#     requirements_respondent = message.text
#     await state.update_data(requirements_respondent=requirements_respondent)
#     text = 'Какие данные от респондента потребуются на исследовании?\n\n' \
#            '<i>Пример ответа: От респондента потребуется его паспорт.</i>'
#     await message.answer(text=text, parse_mode='html')
#     await RecruitingQuery.DataRespondent.set()
#
#
# @dp.message_handler(state=RecruitingQuery.DataRespondent)
# async def stock_respondents(message: types.Message, state: FSMContext):
#     respondent_data = message.text
#     await state.update_data(respondent_data=respondent_data)
#     text = 'Обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
#            'если кто-то из респондентов не дошел мы приглашаем его на следующий день, ' \
#            'насколько это критично для Вас?\n\n' \
#            '<i>Пример ответа: Потребуются запасные респонденты, количество запасных на Ваше усмотрение.</i>'
#     await message.answer(text=text, parse_mode='html')
#     await RecruitingQuery.StockRespondents.set()
#
#
# @dp.message_handler(state=RecruitingQuery.StockRespondents)
# async def enter_research_topic(message: types.Message, state: FSMContext):
#     stock_respondents_info = message.text
#     await state.update_data(stock_respondents_info=stock_respondents_info)
#     await message.answer('Тема исследования?', parse_mode='html')
#     await RecruitingQuery.ResearchTopic.set()
#
#
# @dp.message_handler(state=RecruitingQuery.ResearchTopic)
# async def enter_basic_criteria(message: types.Message, state: FSMContext):
#     research_topic = message.text
#     await state.update_data(research_topic=research_topic)
#     await message.answer('Какие несколько основных критериев, которым должны соответствовать респонденты '
#                          'Вы можете обозначить?', parse_mode='html')
#     await RecruitingQuery.BasicCriteria.set()
#
#
# @dp.message_handler(state=RecruitingQuery.BasicCriteria)
# async def enter_preliminary_communication(message: types.Message, state: FSMContext):
#     basic_criteria = message.text
#     await state.update_data(basic_criteria=basic_criteria)
#     await message.answer('Требуется ли с Вами связаться предварительно по телефону обсудить проект или Вы будите '
#                          'ожидать от нас коммерческого предложения в ближайшее время на основе этих данных?',
#                          parse_mode='html')
#     await RecruitingQuery.PreliminaryCommunication.set()


# @dp.message_handler(state=RecruitingQuery.PreliminaryCommunication)
# async def enter_company_info(message: types.Message, state: FSMContext):
#     preliminary_communication = message.text
#     await state.update_data(preliminary_communication=preliminary_communication)
#     text = 'Укажите, пожалуйста, какую компанию Вы представляете, должность, телефон, никнейм в Телеграм?\n\n' \
#            '<i>Пример ответа: Руководитель исследовательских проектов, Компания: ПИК, ' \
#            'телефон: 89167152222, никнейм: @name</i>'
#     await message.answer(text=text, parse_mode='html')
#     await RecruitingQuery.CompanyInfo.set()


# @dp.message_handler(state=RecruitingQuery.CompanyInfo)
# async def enter_email_info(message: types.Message, state: FSMContext):
#     company_info = message.text
#     await state.update_data(company_info=company_info)
#     await message.answer('Укажите, пожалуйста, Ваш Емейл для отправки информации о сроках и стоимости '
#                          'рекрутинга респондентов?', parse_mode='html')
#     await RecruitingQuery.EmailInfo.set()
#
#
# @dp.message_handler(state=RecruitingQuery.EmailInfo)
# async def enter_project_screening_questionnaire(message: types.Message, state: FSMContext):
#     email_info = message.text
#     await state.update_data(email_info=email_info)
#     await message.answer('Есть ли скрининговая анкета для данного проекта или ориентироваться нужно на запрос или ТЗ? '
#                          'Если есть скрининговая анкета, то какое предусмотрено в ней количество вопросов?',
#                          parse_mode='html')
#     await RecruitingQuery.ProjectScreeningQuestionnaire.set()
#
#
# @dp.message_handler(state=RecruitingQuery.ProjectScreeningQuestionnaire)
# async def enter_field_activity(message: types.Message, state: FSMContext):
#     project_screening_questionnaire = message.text
#     await state.update_data(project_screening_questionnaire=project_screening_questionnaire)
#     await message.answer('Сфера их деятельности и должность?', parse_mode='html')
#     await RecruitingQuery.FieldActivity.set()
#
#
# @dp.message_handler(state=RecruitingQuery.FieldActivity)
# async def enter_education(message: types.Message, state: FSMContext):
#     field_activity = message.text
#     await state.update_data(field_activity=field_activity)
#     await message.answer('Образование и семейное положение?', parse_mode='html')
#     await RecruitingQuery.Education.set()
#
#
# @dp.message_handler(state=RecruitingQuery.Education)
# async def enter_product_service(message: types.Message, state: FSMContext):
#     education = message.text
#     await state.update_data(education=education)
#     await message.answer('Какой товар или услугу они должны потреблять?', parse_mode='html')
#     await RecruitingQuery.ProductService.set()
#
#
# @dp.message_handler(state=RecruitingQuery.ProductService)
# async def enter_consumption_frequency(message: types.Message, state: FSMContext):
#     product_service = message.text
#     await state.update_data(product_service=product_service)
#     await message.answer('Как часто они должны потреблять Вашу продукцию или продукцию конкурентов?',
#                          parse_mode='html')
#     await RecruitingQuery.ConsumptionFrequency.set()
#
#
# @dp.message_handler(state=RecruitingQuery.ConsumptionFrequency)
# async def enter_respondent_income(message: types.Message, state: FSMContext):
#     consumption_frequency = message.text
#     await state.update_data(consumption_frequency=consumption_frequency)
#     await message.answer('Доход респондента на одного человека в его семье?', parse_mode='html')
#     await RecruitingQuery.RespondentIncome.set()


# @dp.message_handler(state=RecruitingQuery.RespondentIncome)
# async def type_research(message: types.Message, state: FSMContext):
#     respondent_income = message.text
#     await state.update_data(respondent_income=respondent_income)
#
#     await message.answer('Выберете вид исследования', reply_markup=types_research_keyboard)
#     await RecruitingQuery.Research.set()


# @dp.callback_query_handler(state=RecruitingQuery.Research)
# async def enter_count_respondents(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'focus_group':
#         research_type = 'Фокус-группа'
#     elif data == 'hall_test':
#         research_type = 'Холл-тест'
#     elif data == 'expert_interviews':
#         research_type = 'Экспертные интервью'
#     elif data == 'usability_testing':
#         research_type = 'Юзабилити-тестирование'
#     elif data == 'home_visit':
#         research_type = 'Домашний визит'
#     elif data == 'going_store':
#         research_type = 'Поход в магазин'
#     elif data == 'secret_shopper':
#         research_type = 'Тайный покупатель'
#     elif data == 'online_survey':
#         research_type = 'Онлайн Опрос'
#     elif data == 'phone_interview':
#         research_type = 'Телефонное интервью'
#     else:
#         research_type = 'Другое'
#     if research_type == 'Другое':
#         await call.message.answer('Укажите другое:')
#         await RecruitingQuery.OtherResearchType.set()
#     else:
#         await state.update_data(research_type=research_type)
#         await call.message.answer('Введите общее количество респондентов')
#         await RecruitingQuery.CountRespondents.set()
#
#
# @dp.message_handler(state=RecruitingQuery.OtherResearchType)
# async def enter_count_respondents_other(message: types.Message, state: FSMContext):
#     research_type = message.text
#     await state.update_data(research_type=research_type)
#     await message.answer('Введите общее количество респондентов')
#     await RecruitingQuery.CountRespondents.set()


# @dp.message_handler(state=RecruitingQuery.CountRespondents)
# async def enter_survey_time(message: types.Message, state: FSMContext):
#     count_respondents = message.text
#     try:
#         count_respondents = int(message.text)
#     except ValueError:
#         await message.answer('Просьба ввести число')
#         return
#     await state.update_data(count_respondents=count_respondents)
#     await message.answer('Примерная длительность опроса?', parse_mode='html')
#     await RecruitingQuery.SurveyTime.set()


# @dp.message_handler(state=RecruitingQuery.SurveyTime)
# async def get_payments_type(message: types.Message, state: FSMContext):
#     survey_time = message.text
#     await state.update_data(survey_time=survey_time)
#     await message.answer('Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения '
#                          'респондентам по итогам исследования, выберете ответ:\n\n'
#                          'кнопка <b>ADS</b> - Потребуется организовать выплату на стороне ADS\n\n'
#                          'кнопка <b>Самостоятельно</b> - Моя компания самостоятельно организует выплату '
#                          'вознаграждения после исследования', reply_markup=payment_types_keyboard, parse_mode='html')
#     await RecruitingQuery.PaymentsType.set()
#
#
# @dp.callback_query_handler(state=RecruitingQuery.PaymentsType)
# async def enter_source(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'payment_ads':
#         payments_type = 'Потребуется организовать выплату на стороне ADS'
#     else:
#         payments_type = 'Моя компания самостоятельно организует выплату вознаграждения после исследования'
#     await state.update_data(payments_type=payments_type)
#     text = 'Из каких источников Вы узнали об Агентстве ADS?\n\n' \
#            '<i>Пример: По рекомендации Коллеги (укажите его имя).\n' \
#            'Из поисковой системы Гугл/Яндекс, из социальной сети Facebook/LinkedIn.</i>'
#     await call.message.answer(text=text, parse_mode='html')
#     await RecruitingQuery.WhatSources.set()


# @dp.message_handler(state=RecruitingQuery.WhatSources)
# async def get_articles(message: types.Message, state: FSMContext):
#     sources = message.text
#     await state.update_data(sources=sources)
#     text = 'Отправляя нам данную форму, вы соглашаетесь на получение статей от компании ADS.'
#     await message.answer(text=text, reply_markup=get_articles_keyboard)
#     await RecruitingQuery.GetArticles.set()
#
#
# @dp.callback_query_handler(state=RecruitingQuery.GetArticles)
# async def enter_name(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'yes':
#         send_articles = 'Да'
#     else:
#         send_articles = 'Нет'
#     await state.update_data(send_articles=send_articles)
#     await call.message.answer(text='Укажите, пожалуйста, ваше имя')
#     await RecruitingQuery.Name.set()
#
#
# @dp.message_handler(state=RecruitingQuery.Name)
# async def enter_gender(message: types.Message, state: FSMContext):
#     name = message.text
#     await state.update_data(name=name)
#     await message.answer(text='Укажите пол', reply_markup=gender_types_keyboard)
#     await RecruitingQuery.Gender.set()
#
#
# @dp.callback_query_handler(state=RecruitingQuery.Gender)
# async def enter_username_telegram(call: types.CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=60)
#     data = call.data
#     if data == 'man':
#         gender = 'мужской'
#     else:
#         gender = 'женский'
#     await state.update_data(gender=gender)
#     await call.message.answer('Укажите, пожалуйста, как Вам удобнее отправить коммерческое '
#                               'предложение на email или в Телеграм. Если на email, укажите,'
#                               'пожалуйста, ваш email, если в Телеграм, укажите, пожалуйста, '
#                               'ваш ник в телеграм?')
#     await RecruitingQuery.Username.set()
#
#
# @dp.message_handler(state=RecruitingQuery.Username)
# async def enter_budget(message: types.Message, state: FSMContext):
#     username_telegram = message.text
#     await state.update_data(username_telegram=username_telegram)
#     await message.answer('Подскажите, пожалуйста, какой бюджет Вы выделяете для вознаграждения респондентам?')
#     await RecruitingQuery.CheckInfo.set()


@dp.message_handler(state=RecruitingQuery.CheckInfo)
async def check_info(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    time_stamp = datetime.datetime.now()
    stock_respondents_info = message.text
    await state.update_data(stock_respondents_info=stock_respondents_info)

    data = await state.get_data()
    company_info = data.get('company_info')
    research_type = data.get('research_type')
    survey_time = data.get('survey_time')
    target_audience = data.get('target_audience')
    payments_type = data.get('payments_type')
    budget = data.get('budget')
    sources = data.get('sources')
    respondent_data = data.get('respondent_data')
    stock_respondents_info = data.get('stock_respondents_info')

    recruit_query = RecruitQuery(user_id=user_id,
                                 time_stamp=time_stamp,
                                 company_info=company_info,
                                 research_type=research_type,
                                 survey_time=survey_time,
                                 target_audience=target_audience,
                                 payments_type=payments_type,
                                 budget=budget,
                                 sources=sources,
                                 respondent_data=respondent_data,
                                 stock_respondents_info=stock_respondents_info
                                 )
    await state.update_data(recruit_query=recruit_query)

    text = f'Подтверждаете ли Вы введенную информацию:\n\n' \
           f'1.Укажите, пожалуйста, какую компанию Вы представляете, должность, телефон, никнейм в Телеграм:\n' \
           f'<i>Ваш ответ: {company_info}</i>\n\n' \
           f'2.Выберете вид исследования:\n' \
           f'<i>Ваш ответ: {research_type}</i>\n\n' \
           f'3.Длительность исследования:\n' \
           f'<i>Ваш ответ: {survey_time}</i>\n\n' \
           f'4.Укажите в свободной форме какая целевая аудитория Вам требуется для исследования:\n' \
           f'<i>Ваш ответ: {target_audience}</i>\n\n' \
           f'5.Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения ' \
           f'респондентам по итогам исследования:\n' \
           f'<i>Ваш ответ: {payments_type}</i>\n\n' \
           f'6.Какой бюджет Вы закладываете на рекрутинг респондентов:\n' \
           f'<i>Ваш ответ: {budget}</i>\n\n' \
           f'7.Из каких источников Вы узнали об Агентстве ADS:\n' \
           f'<i>Ваш ответ: {sources}</i>\n\n' \
           f'8.Какие данные от респондента потребуются на исследовании:\n' \
           f'<i>Ваш ответ: {respondent_data}</i>\n\n' \
           f'9.Обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
           f'если кто-то из респондентов не дошел мы приглашаем его на следующий день, ' \
           f'насколько это критично для Вас:\n' \
           f'<i>Ваш ответ: {stock_respondents_info}</i>\n\n' \

    await message.answer(text=text, parse_mode='html', reply_markup=check_info_keyboard)
    await RecruitingQuery.FinishRecruit.set()


@dp.callback_query_handler(text='correct', state=RecruitingQuery.FinishRecruit)
async def correct_info(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    time_stamp = datetime.datetime.now()

    data = await state.get_data()
    company_info = data.get('company_info')
    research_type = data.get('research_type')
    survey_time = data.get('survey_time')
    target_audience = data.get('target_audience')
    payments_type = data.get('payments_type')
    budget = data.get('budget')
    sources = data.get('sources')
    respondent_data = data.get('respondent_data')
    stock_respondents_info = data.get('stock_respondents_info')

    recruit_query: RecruitQuery = data.get('recruit_query')

    await recruit_query.create()

    google_sheet = GoogleSheet()
    range_recruit = RANGE_TABLE_NAME
    values_recruit = [[str(time_stamp), company_info, research_type, survey_time, target_audience, payments_type,
                       budget, sources, respondent_data, stock_respondents_info]]

    google_sheet.append_range_values(range_recruit, values_recruit)

    text = f'Получен запрос на рекрут:\n\n' \
           f'1.Укажите, пожалуйста, какую компанию Вы представляете, должность, телефон, никнейм в Телеграм:\n' \
           f'<i>Ваш ответ: {company_info}</i>\n\n' \
           f'2.Выберете вид исследования:\n' \
           f'<i>Ваш ответ: {research_type}</i>\n\n' \
           f'3.Длительность исследования:\n' \
           f'<i>Ваш ответ: {survey_time}</i>\n\n' \
           f'4.Укажите в свободной форме какая целевая аудитория Вам требуется для исследования:\n' \
           f'<i>Ваш ответ: {target_audience}</i>\n\n' \
           f'5.Подскажите, пожалуйста, как будет проходить организация выплаты вознаграждения ' \
           f'респондентам по итогам исследования:\n' \
           f'<i>Ваш ответ: {payments_type}</i>\n\n' \
           f'6.Какой бюджет Вы закладываете на рекрутинг респондентов:\n' \
           f'<i>Ваш ответ: {budget}</i>\n\n' \
           f'7.Из каких источников Вы узнали об Агентстве ADS:\n' \
           f'<i>Ваш ответ: {sources}</i>\n\n' \
           f'8.Какие данные от респондента потребуются на исследовании:\n' \
           f'<i>Ваш ответ: {respondent_data}</i>\n\n' \
           f'9.Потребуется ли вам двойной запас Респондентов на случай неявки участника на исследование, ' \
           f'обычно мы не делаем двойной запас респондентов с целью оптимизации бюджета, ' \
           f'если кто-то из респондентов не дошел, мы приглашаем его на следующий день, ' \
           f'насколько это критично для Вас:\n' \
           f'<i>Ваш ответ: {stock_respondents_info}</i>\n\n'

    await bot.send_message('1795343099', text, parse_mode='html')  # Отправляем сообщение с запросом в группу
    await call.message.edit_text('Большое спасибо. В ближайшее время я сообщу Вам информацию по стоимости, '
                                 'срокам и возможности реализации проекта.\n\n'
                                 'Можете ознакомиться с нашими Тик Ток Кейсам и Интервью с экспертами на Ютуб канале.',
                                 parse_mode='html', reply_markup=youtube_tiktok_keyboard)
    await state.reset_state()


@dp.callback_query_handler(text='incorrect', state=RecruitingQuery.FinishRecruit)
async def incorrect_info(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Для возврата в главное меню, нажмите /start')
    await state.reset_state()


@dp.callback_query_handler(text='cancel_test', state=RecruitingQuery.StartRecruit)
async def get_cancel_test(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await state.reset_state()
    await call.message.edit_text(text='Для возврата в главное меню, нажмите /start')
