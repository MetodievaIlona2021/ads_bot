from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Клавиатура меню для Администратора
admin_menu_keyboard = InlineKeyboardMarkup(row_width=1)

admin_btn = InlineKeyboardButton(text='Админка', callback_data='admin')
advantages_btn = InlineKeyboardButton(text=f'ADS Преимущества', callback_data='advantages')
services_btn = InlineKeyboardButton(text=f'Услуги агентства', callback_data='services')
interview_btn = InlineKeyboardButton(text=f'Интервью', switch_inline_query_current_chat='interview')
reviews_btn = InlineKeyboardButton(text=f'Отзывы', switch_inline_query_current_chat='review')
news_btn = InlineKeyboardButton(text=f'Новости', switch_inline_query_current_chat='news')
significant_btn = InlineKeyboardButton(text=f'Значимое', switch_inline_query_current_chat='significant')
articles_btn = InlineKeyboardButton(text=f'Статьи', switch_inline_query_current_chat='articles')
cases_btn = InlineKeyboardButton(text=f'Кейсы ADS', switch_inline_query_current_chat='cases')
contacts_btn = InlineKeyboardButton(text=f'Контакты', callback_data='contacts')
online_meeting_btn = InlineKeyboardButton(text=f'Онлайн-встреча', callback_data='online_meeting')
query_recruit_btn = InlineKeyboardButton(text='Запрос на рекрут', callback_data='query_recruit')
payment_btn = InlineKeyboardButton(text='Оплата услуг', callback_data='payment')
# support_btn = InlineKeyboardButton(text='Написать сообщение', callback_data='support')
support_btn = InlineKeyboardButton(text='Написать сообщение', url='https://t.me/IlonaMetodieva')
asks_btn = InlineKeyboardButton(text='Часто задаваемые вопросы', switch_inline_qcuery_current_chat='asks')


admin_menu_keyboard.add(admin_btn, advantages_btn, services_btn, interview_btn, reviews_btn, news_btn, significant_btn,
                        articles_btn, cases_btn, contacts_btn, online_meeting_btn, query_recruit_btn, payment_btn,
                        support_btn, asks_btn)


# Клавиатура выбора действия для Администратора
admin_action_keyboard = InlineKeyboardMarkup(row_width=1)

add_interview_btn = InlineKeyboardButton(text=f'Добавить интервью', callback_data='add_interview')
add_reviews_btn = InlineKeyboardButton(text=f'Добавить отзыв', callback_data='add_review')
add_news_btn = InlineKeyboardButton(text=f'Добавить новость', callback_data='add_news')
add_significant_btn = InlineKeyboardButton(text=f'Добавить значимое', callback_data='add_significant')
add_articles_btn = InlineKeyboardButton(text=f'Добавить статью', callback_data='add_articles')
add_cases_btn = InlineKeyboardButton(text=f'Добавить кейс', callback_data='add_cases')

admin_action_keyboard.add(add_interview_btn, add_reviews_btn, add_news_btn, add_significant_btn, add_articles_btn,
                          add_cases_btn)


# Клавиатура меню
menu_keyboard = InlineKeyboardMarkup(row_width=1)
# menu_keyboard = ReplyKeyboardMarkup(row_width=1)

advantages_btn = InlineKeyboardButton(text=f'ADS Преимущества', callback_data='advantages')
services_btn = InlineKeyboardButton(text=f'Услуги агентства', callback_data='services')
interview_btn = InlineKeyboardButton(text=f'Интервью', switch_inline_query_current_chat='interview')
reviews_btn = InlineKeyboardButton(text=f'Отзывы', switch_inline_query_current_chat='review')
news_btn = InlineKeyboardButton(text=f'Новости', switch_inline_query_current_chat='news')
significant_btn = InlineKeyboardButton(text=f'Значимое', switch_inline_query_current_chat='significant')
articles_btn = InlineKeyboardButton(text=f'Статьи', switch_inline_query_current_chat='articles')
cases_btn = InlineKeyboardButton(text=f'Кейсы ADS', switch_inline_query_current_chat='cases')
contacts_btn = InlineKeyboardButton(text=f'Контакты', callback_data='contacts')
online_meeting_btn = InlineKeyboardButton(text=f'Онлайн-встреча', callback_data='online_meeting')
query_recruit_btn = InlineKeyboardButton(text='Запрос на рекрут', callback_data='query_recruit')
payment_btn = InlineKeyboardButton(text='Оплата услуг', callback_data='payment')
# support_btn = InlineKeyboardButton(text='Написать сообщение', callback_data='support')
support_btn = InlineKeyboardButton(text='Написать сообщение', url='https://t.me/IlonaMetodieva')
asks_btn = InlineKeyboardButton(text='Часто задаваемые вопросы', switch_inline_query_current_chat='asks')


menu_keyboard.add(advantages_btn, services_btn, interview_btn, reviews_btn, news_btn, significant_btn,
                  articles_btn, cases_btn, contacts_btn, online_meeting_btn, query_recruit_btn, payment_btn,
                  support_btn, asks_btn)


# Клавиатура запроса на рекрутинг
recruiting_keyboard = InlineKeyboardMarkup(row_width=1)

start_test_btn = InlineKeyboardButton(text='Начать', callback_data='start_test')
cancel_test_btn = InlineKeyboardButton(text='Отменить', callback_data='cancel_test')

recruiting_keyboard.add(start_test_btn, cancel_test_btn)


# Клавиатура для вида исследования
types_research_keyboard = InlineKeyboardMarkup(row_width=1)

focus_group_btn = InlineKeyboardButton(text='Фокус-группа', callback_data='focus_group')
hall_test_btn = InlineKeyboardButton(text='Холл-тест', callback_data='hall_test')
expert_interviews_btn = InlineKeyboardButton(text='Экспертные интервью', callback_data='expert_interviews')
usability_testing_btn = InlineKeyboardButton(text='Юзабилити-тестирование', callback_data='usability_testing')
home_visit_btn = InlineKeyboardButton(text='Домашний визит', callback_data='home_visit')
going_store_btn = InlineKeyboardButton(text='Поход в магазин', callback_data='going_store')
secret_shopper_btn = InlineKeyboardButton(text='Тайный покупатель', callback_data='secret_shopper')
online_survey_btn = InlineKeyboardButton(text='Онлайн Опрос', callback_data='online_survey')
phone_interview_btn = InlineKeyboardButton(text='Телефонное интервью', callback_data='phone_interview')
other_btn = InlineKeyboardButton(text='Другое', callback_data='other')

types_research_keyboard.add(focus_group_btn, hall_test_btn, expert_interviews_btn, usability_testing_btn,
                            home_visit_btn, going_store_btn, secret_shopper_btn, online_survey_btn,
                            phone_interview_btn, other_btn)


# Клавиатура для вида оплаты
payment_types_keyboard = InlineKeyboardMarkup(row_width=1)

payment_ads_btn = InlineKeyboardButton(text='ADS', callback_data='payment_ads')
company_self_btn = InlineKeyboardButton(text='Самостоятельно', callback_data='company_self')

payment_types_keyboard.add(payment_ads_btn, company_self_btn)


# Клавиатура для выбора пола
gender_types_keyboard = InlineKeyboardMarkup(row_width=1)

man_btn = InlineKeyboardButton(text='мужской', callback_data='man')
woman_btn = InlineKeyboardButton(text='женский', callback_data='woman')

gender_types_keyboard.add(man_btn, woman_btn)


# Клавиатура для заполнения скрининговой анкеты
screening_keyboard = InlineKeyboardMarkup(row_width=1)

yes_scr_btn = InlineKeyboardButton(text='Да', callback_data='yes_scr')
no_scr_btn = InlineKeyboardButton(text='Нет', callback_data='no_scr')

screening_keyboard.add(yes_scr_btn, no_scr_btn)


# Клавиатура для вопроса: Все ли важные критерии прописаны в скринере?
screening_criteria_keyboard = InlineKeyboardMarkup(row_width=1)

yes_criteria_btn = InlineKeyboardButton(text='Да', callback_data='yes_criteria')
no_criteria_btn = InlineKeyboardButton(text='Нет', callback_data='no_criteria')

screening_criteria_keyboard.add(yes_criteria_btn, no_criteria_btn)


# Клавиатура для получения статей
get_articles_keyboard = InlineKeyboardMarkup(row_width=1)

yes_btn = InlineKeyboardButton(text='Да', callback_data='yes')
no_btn = InlineKeyboardButton(text='Нет', callback_data='no')

get_articles_keyboard.add(yes_btn, no_btn)


# Клавиатура для подтверждения введенной информации
check_info_keyboard = InlineKeyboardMarkup(row_width=1)

correct_btn = InlineKeyboardButton(text='Подтверждаю', callback_data='correct')
incorrect_btn = InlineKeyboardButton(text='Не подтверждаю', callback_data='incorrect')

check_info_keyboard.add(correct_btn, incorrect_btn)


# Клавиатура для услуг
services_markup = InlineKeyboardMarkup(row_width=2)

recruit_respondents_btn = InlineKeyboardButton(text='Рекрут респондентов', callback_data='recruit_respondents')
recruit_experts_btn = InlineKeyboardButton(text='Рекрут экспертов', callback_data='recruit_experts')
on_main_btn = InlineKeyboardButton(text='На главную', callback_data='on_main')

services_markup.add(recruit_respondents_btn, recruit_experts_btn, on_main_btn)


# Клавиатура для перехода на главную страницу
go_to_main_page_markup = InlineKeyboardMarkup(row_width=1)

go_to_main_page_btn = InlineKeyboardButton(text='На главную', callback_data='on_main')
query_recruit_btn = InlineKeyboardButton(text='Сделать запрос на рекрут', callback_data='query_recruit')

go_to_main_page_markup.add(go_to_main_page_btn, query_recruit_btn)


# Клавиатура для записи на Онлайн-консультация в Zoom
zoom_markup = InlineKeyboardMarkup(row_width=1)

zoom_btn = InlineKeyboardButton(text='Записаться', callback_data='zoom')

zoom_markup.add(zoom_btn)


# Клавиатура с кнопками времени записи
time_zoom_markup = InlineKeyboardMarkup(row_width=1)

twelve_btn = InlineKeyboardButton(text='12:00', callback_data='twelve')
twelve_thirty_btn = InlineKeyboardButton(text='12:30', callback_data='twelve_thirty')
thirteen_btn = InlineKeyboardButton(text='13:00', callback_data='thirteen')
thirteen_thirty_btn = InlineKeyboardButton(text='13:30', callback_data='thirteen_thirty')
fourteen_btn = InlineKeyboardButton(text='14:00', callback_data='fourteen')
fourteen_thirty_btn = InlineKeyboardButton(text='14:30', callback_data='fourteen_thirty')
fifteen_btn = InlineKeyboardButton(text='15:00', callback_data='fifteen')
fifteen_thirty_btn = InlineKeyboardButton(text='15:30', callback_data='fifteen_thirty')

time_zoom_markup.add(twelve_btn, twelve_thirty_btn, thirteen_btn, thirteen_thirty_btn,
                     fourteen_btn, fourteen_thirty_btn, fifteen_btn, fifteen_thirty_btn)


# Клавиатура для Youtube и TikTok
youtube_tiktok_keyboard = InlineKeyboardMarkup(row_width=2)

youtube_btn = InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/channel/UC-Uw6fXdmjvKwt4C77RksQQ')
tiktok_btn = InlineKeyboardButton(text='TikTok', url='https://vm.tiktok.com/ZSeLWb1SY/')
on_main_btn = InlineKeyboardButton(text='На главную', callback_data='on_main')

youtube_tiktok_keyboard.add(youtube_btn, tiktok_btn, on_main_btn)
