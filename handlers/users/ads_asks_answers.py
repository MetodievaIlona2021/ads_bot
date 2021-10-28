from aiogram import types

from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='asks')
async def cases_query(query: types.InlineQuery):
    all_asks = await db.show_sorted_items(query.query or None)
    asks = [types.InlineQueryResultArticle(
        id=ask.id,
        title=ask.name,
        input_message_content=types.InputTextMessageContent(
            message_text=ask.text,
            parse_mode='html'),
        description=ask.name,
        thumb_url=ask.thumb_url,
    )
        for ask in all_asks]

    await query.answer(asks, cache_time=5, switch_pm_text='Часто задаваемые вопросы',
                       switch_pm_parameter='select_ask')
