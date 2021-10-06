from aiogram import types

from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='cases')
async def cases_query(query: types.InlineQuery):
    all_cases = await db.show_sorted_items(query.query or None)
    news = [types.InlineQueryResultArticle(
        id=case.id,
        title=case.name,
        input_message_content=types.InputTextMessageContent(
            message_text=case.text,
            parse_mode='html'),
        description=case.text,
        thumb_url=case.thumb_url,
    )
        for case in all_cases]

    await query.answer(news, cache_time=5, switch_pm_text='ADS Кейсы', switch_pm_parameter='select_case')
