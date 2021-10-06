from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = '''
Список команд:

/start - Начать диалог
/help - Получить справку

---------------------------------------------------------------

<i>Контактная информация</i>

<b>Адрес</b>: <i>119019, Москва, Россия, 14 С6, Староваганьковский пер.</i>
<b>Телефон</b>: +7 (499) 394-04-65
<b>Email</b>: ads@adsrecruiting.com
<b>Телеграм канал</b>: <a href="https://t.me/ADSrecruiting1">Наш канал</a>

Вы можете связаться с нами любым удобным для Вас способом: 
написав на емейл, позвонив нам, заполнив форму запроса на 
рекрутинг респондентов, отправив запрос в мессенджер.
        '''

    await message.answer(text)
