from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ADMINS
from keyboards.inline.recruiting_keyboards import admin_action_keyboard
from loader import dp
from states.recruiting_states import NewItem
from utils.db_api import db_commands_gino
from utils.db_api.models import Video, Review, News, Significant, Article, Case

db = db_commands_gino.DBCommands()


@dp.callback_query_handler(user_id=ADMINS, text='admin')
async def get_admin_action(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Что хотите добавить?', reply_markup=admin_action_keyboard)


@dp.message_handler(user_id=ADMINS, commands=['cancel'], state='*')
async def cancel(message: types.Message, state: FSMContext):
    await message.answer('Вы отменили создание.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление нового интервью
@dp.callback_query_handler(user_id=ADMINS, text='add_interview')
async def add_new_interview(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название интервью или нажмите /cancel')
    await NewItem.NewInterview.set()


@dp.message_handler(state=NewItem.NewInterview)
async def interview_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Video()
    item.name = name

    await message.answer(f'Название: <b>{name}</b>\n\nПришлите мне описание интервью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewInterviewDesc.set()


@dp.message_handler(state=NewItem.NewInterviewDesc)
async def interview_desc(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    item: Video = data.get('item')
    item.description = description

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewInterviewThumb.set()


@dp.message_handler(state=NewItem.NewInterviewThumb)
async def interview_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: Video = data.get('item')
    item.thumb_url = thumb_url

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на интервью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewInterviewLink.set()


@dp.message_handler(state=NewItem.NewInterviewLink)
async def interview_link(message: types.Message, state: FSMContext):
    url = message.text
    data = await state.get_data()
    item: Video = data.get('item')
    item.url = url
    item.category = 'interview'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новое интервью:\n\n'
                              f'Название: <b>{item.name}</b>\n'
                              f'Описание: <b>{item.description}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Ссылка: <b>{item.url}</b>\n\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewInterviewConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='cancel', state='*')
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer('Вы отменили добавление.'
                              '\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewInterviewConfirm)
async def confirm(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Video = data.get('item')
    await item.create()
    await call.message.answer(f'Интервью удачно добавлено.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление нового отзыва
@dp.callback_query_handler(user_id=ADMINS, text='add_review')
async def add_new_review(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название отзыва или нажмите /cancel')
    await NewItem.NewReview.set()


@dp.message_handler(state=NewItem.NewReview)
async def review_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Review()
    item.name = name

    await message.answer(f'Название: <b>{name}</b>\n\nПришлите мне описание отзыва или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewReviewDesc.set()


@dp.message_handler(state=NewItem.NewReviewDesc)
async def review_desc(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    item: Review = data.get('item')
    item.description = description

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewReviewThumb.set()


@dp.message_handler(state=NewItem.NewReviewThumb)
async def review_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: Review = data.get('item')
    item.thumb_url = thumb_url

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на отзыв или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewReviewLink.set()


@dp.message_handler(state=NewItem.NewReviewLink)
async def review_link(message: types.Message, state: FSMContext):
    url = message.text
    data = await state.get_data()
    item: Review = data.get('item')
    item.url = url
    item.category = 'review'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новый отзыв:\n\n'
                              f'Название: <b>{item.name}</b>\n'
                              f'Описание: <b>{item.description}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Ссылка: <b>{item.url}</b>\n\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewReviewConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewReviewConfirm)
async def confirm_review(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Review = data.get('item')
    await item.create()
    await call.message.answer(f'Отзыв удачно добавлен.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление новой новости
@dp.callback_query_handler(user_id=ADMINS, text='add_news')
async def add_new_news(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название новости или нажмите /cancel')
    await NewItem.NewNews.set()


@dp.message_handler(state=NewItem.NewNews)
async def news_name(message: types.Message, state: FSMContext):
    title = message.text
    item = News()
    item.title = title

    await message.answer(f'Название: <b>{title}</b>\n\nПришлите мне описание новости или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewNewsDesc.set()


@dp.message_handler(state=NewItem.NewNewsDesc)
async def news_desc(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    item: News = data.get('item')
    item.description = description

    await message.answer(f'Название: <b>{item.title}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewNewsThumb.set()


@dp.message_handler(state=NewItem.NewNewsThumb)
async def news_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: News = data.get('item')
    item.thumb_url = thumb_url

    await message.answer(f'Название: <b>{item.title}</b>'
                         f'\n\nПришлите мне ссылку на новость или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewNewsLink.set()


@dp.message_handler(state=NewItem.NewNewsLink)
async def news_link(message: types.Message, state: FSMContext):
    url = message.text
    data = await state.get_data()
    item: News = data.get('item')
    item.url = url
    item.category = 'news'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новую новость:\n\n'
                              f'Название: <b>{item.title}</b>\n'
                              f'Описание: <b>{item.description}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Ссылка: <b>{item.url}</b>\n\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewNewsConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewNewsConfirm)
async def confirm_news(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: News = data.get('item')
    await item.create()
    await call.message.answer(f'Новость удачно добавлена.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление новой записи в значимое
@dp.callback_query_handler(user_id=ADMINS, text='add_significant')
async def add_new_significant(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название значимого или нажмите /cancel')
    await NewItem.NewSignificant.set()


@dp.message_handler(state=NewItem.NewSignificant)
async def significant_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Significant()
    item.name = name

    await message.answer(f'Название: <b>{name}</b>\n\nПришлите мне текст значимого или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewSignificantDesc.set()


@dp.message_handler(state=NewItem.NewSignificantDesc)
async def significant_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    item: Significant = data.get('item')
    item.text = text

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewSignificantThumb.set()


@dp.message_handler(state=NewItem.NewSignificantThumb)
async def significant_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: Significant = data.get('item')
    item.thumb_url = thumb_url
    item.category = 'significant'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новое значимое:\n\n'
                              f'Название: <b>{item.name}</b>\n'
                              f'Текст: <b>{item.text}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewSignificantConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewSignificantConfirm)
async def confirm_significant(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Significant = data.get('item')
    await item.create()
    await call.message.answer(f'Значимое удачно добавлена.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление новой статьи
@dp.callback_query_handler(user_id=ADMINS, text='add_articles')
async def add_new_article(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название статьи или нажмите /cancel')
    await NewItem.NewArticle.set()


@dp.message_handler(state=NewItem.NewArticle)
async def article_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Article()
    item.name = name

    await message.answer(f'Название: <b>{name}</b>\n\nПришлите мне текст статьи или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewArticleDesc.set()


@dp.message_handler(state=NewItem.NewArticleDesc)
async def article_desc(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    item: Article = data.get('item')
    item.text = text

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewArticleThumb.set()


@dp.message_handler(state=NewItem.NewArticleThumb)
async def article_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: Article = data.get('item')
    item.thumb_url = thumb_url

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на статью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewArticleLink.set()


@dp.message_handler(state=NewItem.NewArticleLink)
async def article_link(message: types.Message, state: FSMContext):
    url = message.text
    data = await state.get_data()
    item: Article = data.get('item')
    item.url = url
    item.category = 'articles'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новую статью:\n\n'
                              f'Название: <b>{item.name}</b>\n'
                              f'Описание: <b>{item.text}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Ссылка: <b>{item.url}</b>\n\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewArticleConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewArticleConfirm)
async def confirm_article(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Article = data.get('item')
    await item.create()
    await call.message.answer(f'Статья удачно добавлена.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()


# Добавление нового кейса
@dp.callback_query_handler(user_id=ADMINS, text='add_cases')
async def add_new_case(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Введите название кейса или нажмите /cancel')
    await NewItem.NewCase.set()


@dp.message_handler(state=NewItem.NewCase)
async def case_name(message: types.Message, state: FSMContext):
    name = message.text
    item = Case()
    item.name = name

    await message.answer(f'Название: <b>{name}</b>\n\nПришлите мне текст кейса или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewCaseDesc.set()


@dp.message_handler(state=NewItem.NewCaseDesc)
async def case_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    item: Case = data.get('item')
    item.text = text

    await message.answer(f'Название: <b>{item.name}</b>'
                         f'\n\nПришлите мне ссылку на превью или нажмите /cancel')
    await state.update_data(item=item)
    await NewItem.NewCaseThumb.set()


@dp.message_handler(state=NewItem.NewCaseThumb)
async def case_thumb(message: types.Message, state: FSMContext):
    thumb_url = message.text
    data = await state.get_data()
    item: Case = data.get('item')
    item.thumb_url = thumb_url
    item.category = 'cases'

    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Да', callback_data='confirm')],
            [InlineKeyboardButton(text='Отмена', callback_data='cancel')],
        ]
    )

    await message.answer(text=f'Вы хотите добавить новый кейс:\n\n'
                              f'Название: <b>{item.name}</b>\n'
                              f'Текст: <b>{item.text}</b>\n'
                              f'Превью: <b>{item.thumb_url}</b>\n'
                              f'Подтверждаете?', reply_markup=markup)
    await state.update_data(item=item)
    await NewItem.NewCaseConfirm.set()


@dp.callback_query_handler(user_id=ADMINS, text='confirm', state=NewItem.NewCaseConfirm)
async def confirm_case(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    item: Case = data.get('item')
    await item.create()
    await call.message.answer(f'Кейс удачно добавлен.\n\nЕсли хотите вернуться в главное меню, нажмите /start')
    await state.reset_state()
