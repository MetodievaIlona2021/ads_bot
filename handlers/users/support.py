from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.support_keyboards import support_keyboard, support_callback
from loader import dp, bot


@dp.callback_query_handler(text='support')
async def ask_support_call(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    text = 'Хотите написать сообщение менеджеру? Нажмите на кнопку ниже!'
    keyboard = await support_keyboard(messages='one')
    await call.message.answer(text=text, reply_markup=keyboard)


@dp.message_handler(Command('support'))
async def ask_support(message: types.Message):
    text = 'Хотите написать сообщение менеджеру? Нажмите на кнопку ниже!'
    keyboard = await support_keyboard(messages='one')
    await message.answer(text=text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages='one'))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=5)
    user_id = int(callback_data.get('user_id'))

    await call.message.answer(text='Напишите сообщение, которое хотите отправить')
    await state.set_state('wait_for_support_message')
    await state.update_data(second_id=user_id)


@dp.message_handler(state='wait_for_support_message', content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')

    await bot.send_message(second_id, 'Вам письмо! Вы можете ответить, нажав на кнопку ниже')
    keyboard = await support_keyboard(messages='one', user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)

    await message.answer('Сообщение отправлено!')
    await state.reset_state()
