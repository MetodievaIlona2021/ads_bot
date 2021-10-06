from aiogram import types

from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='articles')
async def interview_query(query: types.InlineQuery):
    all_articles = await db.show_sorted_items(query.query or None)
    news = [types.InlineQueryResultArticle(
        id=article.id,
        title=article.name,
        input_message_content=types.InputTextMessageContent(
            message_text=article.text,
            parse_mode='html'),
        description=article.text,
        thumb_url=article.thumb_url,
        url=article.url
    )
        for article in all_articles]

    await query.answer(news, cache_time=5, switch_pm_text='ADS Статьи', switch_pm_parameter='select_news')


# @dp.callback_query_handler(pagination_call.filter(page='current_page'))
# async def current_page_error(call: types.CallbackQuery):
#     await call.answer(cache_time=60)
#
#
# @dp.callback_query_handler(pagination_call.filter(key='article'))
# async def show_chosen_page(call: types.CallbackQuery, callback_data: dict):
#     current_page = int(callback_data.get('page'))
#     text = get_page(page=current_page)
#     markup = get_page_keyboard(max_pages=5, page=current_page)
#     await call.message.edit_text(text=text, reply_markup=markup)
