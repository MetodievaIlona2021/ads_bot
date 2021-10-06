from aiogram import types
from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='news')
async def interview_query(query: types.InlineQuery):
    all_news = await db.show_sorted_items(query.query or None)
    news = [types.InlineQueryResultArticle(
        id=new_item.id,
        title=new_item.title,
        input_message_content=types.InputTextMessageContent(
            message_text=f'{new_item.url}',
            parse_mode='html'),
        description=new_item.description,
        url=new_item.url,
        thumb_url=new_item.thumb_url,

    )
        for new_item in all_news]

    await query.answer(news, cache_time=5, switch_pm_text='Наши новости', switch_pm_parameter='select_news')
