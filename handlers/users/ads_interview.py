from aiogram import types
from handlers.users.start import db
from loader import dp


@dp.inline_handler(text='interview')
async def interview_query(query: types.InlineQuery):
    all_interviews = await db.show_sorted_items(query.query or None)
    interviews = [types.InlineQueryResultVideo(
        id=interview.id,
        video_url=interview.url,
        caption=interview.name,
        title=interview.description,
        thumb_url=interview.thumb_url,
        mime_type='text/html',
        input_message_content=types.InputTextMessageContent(
            message_text=interview.url, parse_mode='html')
    )
        for interview in all_interviews]

    await query.answer(interviews, cache_time=5, switch_pm_text='Наши интервью', switch_pm_parameter='select_video')

    # await query.answer(
    #     results=[
    #         types.InlineQueryResultVideo(
    #             id='1',
    #             video_url='https://www.youtube.com/',
    #             caption='Подпись к видео',
    #             title='Какое-то видео',
    #             description='Описание к видео',
    #             thumb_url='https://i.ytimg.com/vi/lVLq6GGukRs/hqdefault.jpg',
    #             mime_type='text/html',
    #             input_message_content=types.InputTextMessageContent(
    #                 message_text='https://www.youtube.com/embed/lVLq6GGukRs', parse_mode='html'))
    #     ], cache_time=60
    # )


# @dp.inline_handler()
# async def empty_query(query: types.InlineQuery):
#     await query.answer(
#         results=[
#             types.InlineQueryResultArticle(
#                 id='1',
#                 title='Название статьи',
#                 input_message_content=types.InputTextMessageContent(
#                     message_text='Текст, при нажатии на кнопку'
#                 ),
#                 url='https://www.adsrecruiting.com/post/s-chego-nachinaetsya-kachestvennoe-issledovanie',
#                 thumb_url='https://static.wixstatic.com/media/a27d24_a97308a96bd54fb29f7b7295bc4b851d~mv2.jpg/v1/fill/w_925,h_617,al_c,q_90/a27d24_a97308a96bd54fb29f7b7295bc4b851d~mv2.webp',
#                 description='Описание в инлайн режиме'
#             ),
#             types.InlineQueryResultVideo(
#                 id='2',
#                 video_url='https://youtu.be/lVLq6GGukRs',
#                 caption='Подпись к видео',
#                 title='Какое-то видео',
#                 description='Описание к видео',
#                 thumb_url='https://i.ytimg.com/vi/lVLq6GGukRs/hqdefault.jpg',
#                 mime_type='video/mp4'
#             )
#         ])
