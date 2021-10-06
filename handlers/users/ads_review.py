from aiogram import types
from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='review')
async def interview_query(query: types.InlineQuery):
    all_reviews = await db.show_sorted_items(query.query or None)
    interviews = [types.InlineQueryResultVideo(
        id=review.id,
        video_url=review.url,
        caption=review.name,
        title=review.description,
        thumb_url=review.thumb_url,
        mime_type='text/html',
        input_message_content=types.InputTextMessageContent(
            message_text=review.url, parse_mode='html')
    )
        for review in all_reviews]

    await query.answer(interviews, cache_time=5, switch_pm_text='Наши отзывы', switch_pm_parameter='select_video')
