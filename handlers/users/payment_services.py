from aiogram import types

from keyboards.inline.payment_keyboard import payment_services_keyboard
from loader import dp
from states.recruiting_states import PaymentService


@dp.callback_query_handler(text='payment')
async def vote_payments(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text='Выберите сервис для оплаты услуг:', reply_markup=payment_services_keyboard)
    await PaymentService.Payment.set()
