from aiogram import types
from handlers.users.start import db
from keyboards.inline.recruiting_keyboards import go_to_main_page_markup

from loader import dp


@dp.inline_handler(text='significant')
async def significant_query(query: types.InlineQuery):
    all_significant = await db.show_sorted_items(query.query or None)
    news = [types.InlineQueryResultArticle(
        id=significant.id,
        title=significant.name,
        input_message_content=types.InputTextMessageContent(
            message_text=significant.text,
            parse_mode='html'),
        description=significant.name,
        thumb_url=significant.thumb_url
    )
        for significant in all_significant]

    await query.answer(news, cache_time=5, switch_pm_text='ADS Значимое', switch_pm_parameter='select_significant')
