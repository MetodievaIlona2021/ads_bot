from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.inline.recruiting_keyboards import menu_keyboard, admin_menu_keyboard
from loader import dp, bot
from utils.db_api import db_commands_gino


db = db_commands_gino.DBCommands()


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await bot.send_chat_action(message.from_user.id, action='typing')
    await db.add_new_user()
    user_id = message.from_user.id
    text = f'Здравствуйте, {message.from_user.full_name}!\n\n' \
           f'Вас приветствует <b>Первое Агентство по рекрутингу респондентов ADS</b>, ' \
           f'Лауреат Гильдии маркетологов\n\n' \
           f'Для формирования запроса на рекрут нажмите кнопку <b>"Запрос на рекрут"</b>\n\n' \
           f'Если хотите задать вопрос, нажмите на кнопку <b>"Написать сообщение"</b>'
    if str(user_id) in ADMINS:
        await message.answer(text=text, reply_markup=admin_menu_keyboard)
    else:
        await message.answer(text=text, reply_markup=menu_keyboard)


@dp.callback_query_handler(text='on_main', state='*')
async def return_main_page(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await state.reset_state()
    await call.message.edit_text(text='ADS — Первое Агентство по рекрутингу респондентов', reply_markup=menu_keyboard)
