from aiogram import types

from keyboards.inline.recruiting_keyboards import go_to_main_page_markup
from loader import dp


@dp.callback_query_handler(text='contacts')
async def show_contacts(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    text = '''
<b>Адрес</b>: <i>119019, Москва, Россия, 14 С6, Староваганьковский пер.</i>
<b>Телефон</b>: +7 (499) 394-04-65
<b>Email</b>: ads@adsrecruiting.com
<b>Телеграм канал</b>: <a href="https://t.me/ADSrecruiting1">Наш канал</a>

Вы можете связаться с нами любым удобным для Вас способом: 
написав на емейл, позвонив нам, заполнив форму запроса на 
рекрутинг респондентов, отправив запрос в мессенджер.
    '''
    await call.message.edit_text(text=text, parse_mode='html', reply_markup=go_to_main_page_markup)
